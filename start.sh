#!/usr/bin/env bash
set -euo pipefail

SERVICE_NAME="backend"
DB_SERVICE="postgres"
DB_USER="postgres"
DB_NAME="rollercoaster"
WAIT_TIMEOUT=30
RESET_DB=${1:-false} # Pass 'reset' as first argument to nuke DB

echo "Starting Docker Compose stack..."
docker compose up --build -d

echo "Waiting for Postgres to be ready..."

start_time=$(date +%s)
until docker compose exec -T $DB_SERVICE pg_isready -U $DB_USER > /dev/null 2>&1; do
  sleep 1
  now=$(date +%s)
  if (( now - start_time > WAIT_TIMEOUT )); then
    echo "❌ Postgres did not become ready in time. Exiting."
    exit 1
  fi
done
echo "✅ Postgres is ready."

if [ "$RESET_DB" = "reset" ]; then
  echo "Reset flag detected — nuking database and Alembic history..."
  docker compose exec -T "$DB_SERVICE" psql -U "$DB_USER" -d "$DB_NAME" -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
  docker compose exec -T "$SERVICE_NAME" bash -c "rm -rf alembic/versions/*"
  echo "✅ Database and Alembic state wiped clean."
fi

echo "Checking Alembic integrity..."
if ! docker compose exec -T $SERVICE_NAME bash -c "alembic current" > /dev/null 2>&1; then
  echo "Alembic not initialized properly, creating baseline..."
  docker compose exec -T $SERVICE_NAME bash -c "rm -rf alembic/versions/*"
  docker compose exec -T $DB_SERVICE psql -U $DB_USER -d $DB_NAME -c 'DELETE FROM alembic_version;' || true
  docker compose exec -T $SERVICE_NAME bash -c "alembic revision --autogenerate -m 'initial baseline'"
fi

echo "Applying Alembic migrations..."
docker compose exec -T $SERVICE_NAME alembic upgrade head

echo "Environment bootstrap complete."
docker compose ps
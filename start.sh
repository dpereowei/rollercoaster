#!/bin/bash

set -e

docker-compose up --build

sleep 20

echo "Running alembic commands"
docker-compose exec backend alembic revision --autogenerate -m "init tables"
docker-compose exec backend alembic upgrade head

echo "Checking tables"
docker-compose exec db psql -U postgres -d rollercoaster -c "\dt"

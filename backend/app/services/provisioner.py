import time
from sqlalchemy.orm import Session
from ..models import Environment
from ..database import SessionLocal
from ..services.tf_runner import run_terraform

def simulate_provision(env_id: int, db_session: Session):
    time.sleep(10)
    env = db_session.query(Environment).filter(Environment.id == env_id).first()
    if env:
        env.status = "running"
        db_session.commit()

def provision_env(env_id: int):
    db = SessionLocal()
    try:
        env = db.query(Environment).get(env_id)
        success, output = run_terraform(env.id)
        env.status = "running" if success else "failed"
        env.tf_output = output
    except Exception as e:
        env = db.query(Environment).get(env_id)
        env.status = "failed"
        env.error_message = str(e)
    finally:
        db.commit()
        db.close()
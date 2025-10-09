import time
from sqlalchemy.orm import Session
from ..models import Environment

def simulate_provision(env_id: int, db_session: Session):
    time.sleep(10)
    env = db_session.query(Environment).filter(Environment.id == env_id).first()
    if env:
        env.status = "running"
        db_session.commit()
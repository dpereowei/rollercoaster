import time
from ..database import SessionLocal
from ..models import Environment
from ..services.tf_runner import destroy_terraform

def teardown_environment(env_id: int):
    db = SessionLocal()
    try:
        destroy_terraform(env_id)
        env = db.query(Environment).filter(Environment.id == env_id).first()
        if env:
            db.delete(env)
            db.commit()
    except Exception as e:
        print(f"Teardown failed for {env_id}: {e}")
    finally:
        db.close()
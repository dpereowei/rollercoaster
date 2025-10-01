from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from .. import models
from ..database import get_db

router = APIRouter(prefix="/environments", tags=["environments"])

@router.post("/create", response_model=dict)
def create_environment(name: str, config: dict, db: Session = Depends(get_db)):
    """
    Purpose: Creates a new environment with the provided JSON config
    """
    env = models.Environment(
        name=name,
        status="running",
        created_at=datetime.utcnow(),
        config=config
    )
    db.add(env)
    db.commit()
    db.refresh(env)
    return {"id": env.id, "status": env.status, "name": env.name}
# end def

@router.get("/list", response_model=List[dict])
def list_environments(db: Session = Depends(get_db)):
    """
    Purpose: Fetch Created Environments
    """
    envs = db.query(models.Environment).all()
    return [
        {
            "id": e.id,
            "name": e.name,
            "status": e.status,
            "created_at": e.created_at,
            "config": e.config
        } for e in envs
    ]
    
# end def

@router.delete("/delete/{env_id}", response_model=dict)
def delete_environment(env_id: int, db: Session = Depends(get_db)):
    """
    Purpose: Delete An environment Using it's unique Id
    """
    env = db.query(models.Environment).filter(models.Environment.id == env_id).first()
    if not env:
        raise HTTPException(status_code=404, detail="Environment not found")
    env.status = "terminated"
    db.commit()
    return {"id": env.id, "status": env.status}
# end def
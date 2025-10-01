from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from . import models
from .database import engine, SessionLocal, Base
from .routers import environment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RollerCoaster Environment Manager")
app.include_router(environment.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    """
    Purpose: Default get endpoint
    """
    return {"message": "RollerCoaster backend is upppp!"}
# end def

@app.get("/health")
def health(db: Session = Depends(get_db)):
    """
    Purpose: Healthcheck
    """
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
    
# end def
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, schemas, database, env_manager
import asyncio

app = FastAPI(title="RollerCoaster Environment Manager")

@app.post("/environments/", response_model=schemas.EnvironmentOut)
async def create_environment(env: schemas.EnvironmentCreate, db: AsyncSession = Depends(database.get_db)):
    db_env = await crud.create_environment(db, env)
    asyncio.create_task(env_manager.provision_environment(db_env.name))
    return db_env

@app.get("/environments/", response_model=list[schemas.EnvironmentOut])
async def list_environments(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_active_environments(db)
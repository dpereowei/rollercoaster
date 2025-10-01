from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas
from datetime import datetime, timedelta

async def create_environment(db: AsyncSession, env: schemas.EnvironmentCreate):
    new_env = models.Environment(
        name=env.name,
        owner=env.owner,
        ttl=datetime.utcnow() + timedelta(hours=env.ttl_hours)
    )
    db.add(new_env)
    await db.commit()
    await db.refresh(new_env)
    return new_env

async def get_active_environments(db: AsyncSession):
    result = await db.execute(select(models.Environment).where(models.Environment.status == "active"))
    return result.scalars().all()

async def expire_environments(db: AsyncSession, env_id: int):
    result = await db.execute(select(models.Environment).where(models.Environment.id == env_id))
    env = result.scalar_one_or_none()
    if env:
        env.status = "expired"
        await db.commit()
        await db.refresh(env)
    return env
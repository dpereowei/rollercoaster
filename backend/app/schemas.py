from pydantic import BaseModel
from datetime import datetime

class EnvironmentCreate(BaseModel):
    name: str
    owner: str
    ttl_hours: int = 2

class EnvironmentOut(BaseModel):
    id: int
    name: str
    owner: str
    status: str
    ttl: datetime
    created_at: datetime

    class Config:
        orm_mode = True
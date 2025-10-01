from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta
from .database import Base

class Environment(Base):
    __tablename__ = "environments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    owner = Column(String, index=True)
    status = Column(String, default="provisioning")
    ttl = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=2))
    created_at = Column(DateTime, default=datetime.utcnow)
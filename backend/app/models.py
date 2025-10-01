from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    environments = relationship("Environment", back_populates="owner")
class Environment(Base):
    __tablename__ = "environments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(String, default="provisioning")
    created_at = Column(DateTime, default=datetime.utcnow)
    config = Column(JSON)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="environments")

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    version = Column(String)
    environment_id = Column(Integer, ForeignKey("environments.id"))
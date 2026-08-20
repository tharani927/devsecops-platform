from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Deployment(Base):
    __tablename__ = "deployments"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    environment = Column(String, nullable=False)
    version = Column(String, nullable=False)
    status = Column(String, nullable=False)
    security_status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
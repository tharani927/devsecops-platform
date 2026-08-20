from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.deployment import Deployment

router = APIRouter(prefix="/deployments", tags=["Deployments"])


class DeploymentCreate(BaseModel):
    project_name: str
    environment: str
    version: str
    status: str
    security_status: str


@router.post("/")
def create_deployment(
    deployment: DeploymentCreate,
    db: Session = Depends(get_db)
):
    new_deployment = Deployment(
        project_name=deployment.project_name,
        environment=deployment.environment,
        version=deployment.version,
        status=deployment.status,
        security_status=deployment.security_status
    )

    db.add(new_deployment)
    db.commit()
    db.refresh(new_deployment)

    return new_deployment


@router.get("/")
def get_deployments(db: Session = Depends(get_db)):
    return db.query(Deployment).all()
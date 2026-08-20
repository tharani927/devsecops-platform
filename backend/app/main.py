from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.deployment import Deployment
from app.routes.health import router as health_router
from app.routes.deployments import router as deployments_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="DevSecOps Secure Delivery Platform",
    description="Secure software delivery platform using DevSecOps practices",
    version="1.0.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "DevSecOps Secure Delivery Platform",
        "status": "running"
    }


@app.get("/security/status")
def security_status():
    return {
        "security_pipeline": "active",
        "status": "secure"
    }


app.include_router(health_router)
app.include_router(deployments_router)
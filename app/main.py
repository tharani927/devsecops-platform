from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(
    title="DevSecOps Secure Delivery Platform",
    description="Secure software delivery platform using DevSecOps practices",
    version="1.0.0"
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
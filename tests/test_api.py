from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_security_status():
    response = client.get("/security/status")
    assert response.status_code == 200
    assert response.json()["status"] == "secure"


def test_get_deployments():
    response = client.get("/deployments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_deployment():
    deployment = {
        "project_name": "Test Project",
        "environment": "Testing",
        "version": "v1.0.0",
        "status": "Success",
        "security_status": "Passed"
    }

    response = client.post("/deployments/", json=deployment)

    assert response.status_code == 200

    data = response.json()

    assert data["project_name"] == "Test Project"
    assert data["environment"] == "Testing"
    assert data["version"] == "v1.0.0"
    assert data["status"] == "Success"
    assert data["security_status"] == "Passed"
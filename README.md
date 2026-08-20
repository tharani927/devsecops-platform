# DevSecOps Secure Delivery Platform

A containerized DevSecOps platform for secure software delivery using FastAPI, PostgreSQL, Docker, automated testing, and security validation.

## Project Overview

The DevSecOps Secure Delivery Platform demonstrates a secure and organized software delivery workflow.

The project integrates:

- FastAPI backend
- PostgreSQL database
- HTML, CSS and JavaScript frontend
- Docker and Docker Compose
- Automated API testing using Pytest
- Security scanning using Bandit
- Dependency vulnerability scanning using pip-audit
- Git and GitHub for version control

## Project Structure

```text
devsecops-platform/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   └── deployment.py
│   │   ├── routes/
│   │   │   ├── deployments.py
│   │   │   └── health.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── tests/
│   └── test_api.py
│
├── docker-compose.yml
└── README.md
Application Architecture
Frontend
   |
   | HTTP
   ↓
FastAPI Backend
   |
   | SQLAlchemy
   ↓
PostgreSQL Database

All services communicate through the Docker Compose network.

Database

The PostgreSQL database stores deployment information.

The deployments table contains:

ID
Project name
Environment
Version
Status
Security status
Creation timestamp
API Endpoints
Root
GET /

Returns the application status.

Health Check
GET /health

Checks backend health.

Security Status
GET /security/status

Returns the security pipeline status.

Get Deployments
GET /deployments/

Returns deployment records stored in PostgreSQL.

Create Deployment
POST /deployments/

Creates a new deployment record.

Example request:

{
  "project_name": "Test Project",
  "environment": "Testing",
  "version": "v1.0.0",
  "status": "Success",
  "security_status": "Passed"
}
Running the Application
Start the containers

From the project root:

docker compose up -d
Check running containers
docker compose ps

The following services are expected:

devsecops-backend
devsecops-frontend
devsecops-db
Frontend

Open:

http://localhost:3000
Backend

Open:

http://localhost:8000
API Documentation

FastAPI automatically provides:

http://localhost:8000/docs
Testing

Set the Python path:

$env:PYTHONPATH="backend"

Run the tests:

pytest -v

Current validation:

5 tests passed

The tests validate:

Root endpoint
Health endpoint
Security status endpoint
Deployment retrieval
Deployment creation
Security Validation
Dependency Audit
pip-audit -r backend\requirements.txt

Current result:

No known vulnerabilities found
Bandit
bandit -r backend\app -ll

Current result:

No issues identified.
Docker Services

Docker Compose provides three services:

Frontend → Port 3000
Backend  → Port 8000
Database → Port 5432

PostgreSQL data is stored using a persistent Docker volume.

Git Workflow

The project is maintained using Git and GitHub.

Feature development is performed using feature branches and changes are committed to the repository.

Current development branch:

feature/devsecops-final
Future Improvements

Possible future improvements include:

Authentication and authorization
More comprehensive automated tests
CI/CD security gates
Advanced monitoring
Improved frontend deployment dashboard
Additional security scanning tools
Conclusion

The project demonstrates the integration of development, testing, security validation, containerization, database management, and version control practices in a DevSecOps workflow.
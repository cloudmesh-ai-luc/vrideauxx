
Markdown
# Secure AI-Powered REST Microservice with Automated DevSecOps Pipeline

> A production-inspired, end-to-end CI/CD pipeline demonstrating modern DevSecOps practices, software supply-chain security, and automated cloud deployments across multiple providers using cloudmesh-ai-vm.

## Project Overview
This project bridges the gap between software development and multi-cloud operations. The core engineering centers on establishing automated guardrails, ensuring that code changes are rigorously tested, scanned for security vulnerabilities, and deployed safely across heterogeneous cloud environments without manual intervention.

The application is a lightweight Python FastAPI REST microservice that processes user requests and interfaces with an AI model.

## Cloud, DevOps, and AI Integration
This project explicitly combines the three pillars of the course:
* **DevOps:** GitHub Actions orchestrates a rigorous DevSecOps CI/CD pipeline (linting, testing, Trivy container scanning, Gitleaks secret detection), while UptimeRobot and Discord Webhooks provide post-deployment observability.
* **AI:** The microservice executes an AI inference workflow, accepting user prompts via REST, passing them to an AI model, and returning structured responses. 
* **Cloud Computing:** Infrastructure is managed and validated across three distinct cloud tiers using `cloudmesh-ai-vm`.

## Multi-Cloud Architecture & cm-x Integration
To demonstrate cloud portability, deployments and tests are orchestrated using `cloudmesh-ai-vm` across three distinct providers:
1. **Local Environment:** Multipass (Ubuntu) for local CI runner testing and initial container validation.
2. **OpenStack Cloud:** Chameleon Cloud (or Jetstream2) for staging the AI microservice.
3. **Public Cloud:** AWS / Azure / GCP for the production deployment tier.

By utilizing `cloudmesh-ai-vm`, the project ensures standardized VM provisioning and lifecycle management regardless of the underlying infrastructure.

## DevSecOps CI/CD Workflow

If Successful:
```text
Developer Pull Request
        ↓
GitHub Actions Pipeline
 ├─ Python tests & linting (Ruff)
 ├─ Secret scanning (Gitleaks)
 ├─ Dockerfile linting (Hadolint)
 └─ Container vulnerability scanning (Trivy)
        ↓
Build & Push Docker image
        ↓
Deploy to Multi-Cloud via cloudmesh-ai-vm
        ↓
Live FastAPI Service
        ↓
Uptime Monitoring & Webhook Alerts
```
If Failed:
```text
Developer Pull Request
        ↓
GitHub Actions Pipeline
        ↓
Trivy / Gitleaks detects security violation
        ↓
Pipeline Fails & Pull Request Blocked
        ↓
Deployment Aborted (Multi-cloud environments remain secure)
```
App Data Flow:
```text
User REST Request 
        ↓
FastAPI Endpoint (Input Validation)
        ↓
AI Inference Engine (Processing text/data)
        ↓
FastAPI Response Formatting
        ↓
JSON Response to User
```

## Tech Stack
* Application: Python (FastAPI), Docker, External AI Inference API

* Version Control: GitHub (Repositories, Branch Protection, Webhooks)

* CI/CD Orchestration: GitHub Actions

* Security Tooling: [Trivy](https://trivy.dev/), [Gitleaks](https://github.com/gitleaks/gitleaks), [Hadolint](https://github.com/hadolint/hadolint)

* Containerization: [Docker](https://docs.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

* Cloud Hosting: cloudmesh-ai-vm (cm-x)

* Monitoring: [UptimeRobot](https://uptimerobot.com) & Discord [Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Issues & Future Work
* AI Compute Allocation: Currently evaluating whether to host the AI model locally on a Chameleon DGX node versus using a lightweight external inference API, depending on resource availability and quota limits.
* cloudmesh-ai-vm API: Finalizing the Python API credential tests for the Public Cloud tier to match the successfully implemented Multipass and Chameleon tests.

## Production Limitations
> This project is an educational demonstration and is not intended for production use. The deployment platform uses a free-tier environment, so production availability guarantees are not applicable. In a production deployment, additional controls such as centralized secrets management, stronger authentication, comprehensive observability, infrastructure-as-code, artifact provenance, and multi-environment promotion would be considered.

## Getting Started Locally

### Prerequisites
- **Multipass:** Installed and configured for local VM provisioning.
- **Python 3.10+:** Required for the `cloudmesh-ai-vm` orchestrator.
- **Docker & Docker Compose:** For containerizing the FastAPI service.
- **API Key:** A free API key from your chosen AI provider.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/cloudmesh-ai/vrideauxx.git](https://github.com/cloudmesh-ai/vrideauxx.git)
   cd vrideauxx


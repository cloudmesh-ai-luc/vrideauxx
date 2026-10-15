
# Project Proposal: Secure AI-Powered REST Microservice with Automated DevSecOps Pipeline

> A production-inspired, end-to-end CI/CD pipeline demonstrating modern DevSecOps practices, software supply-chain security, and automated cloud deployment.

## Project Overview
This project bridges the gap between software development and cloud operations. Rather than focusing heavily on complex application logic, the core engineering centers on establishing automated guardrails, ensuring that code changes are rigorously tested, scanned for security vulnerabilities, and deployed safely without manual intervention.
The application itself is a lightweight REST microservice that processes user requests by securely integrating with a free public AI model API.

## Key Features & DevOps Practices
* **Shift-Left Security:** Automated secret detection [`Gitleaks`](https://github.com/gitleaks/gitleaks), static code analysis, and container vulnerability scanning [`Trivy`](https://trivy.dev/) that block insecure code before it reaches production.
* **Continuous Integration (CI):** Automated linting, unit testing, and container builds triggered on every pull request and merge via GitHub Actions.
* **Continuous Deployment (CD):** Automated cloud deployment with health checks and minimal deployment disruption of immutable Docker containers to a cloud platform upon a successful merge to the main branch.
* **Supply Chain Transparency:** Automated validation of base images and dependency trees.
* **Observability:** Post-deployment uptime monitoring and instant notification webhooks to alert developers of downtime.


## Architecture Overview

If Successful:
```text
Developer makes change
        ↓
Pull Request
        ↓
GitHub Actions
 ├─ Tests
 ├─ Linting
 ├─ Gitleaks
 ├─ Hadolint
 └─ Trivy
        ↓
Build Docker image
        ↓
Deploy
        ↓
Health check
        ↓
Live service
        ↓
Uptime monitoring
```

If Failed:
```text
Introduce vulnerable dependency
        ↓
CI detects vulnerability
        ↓
Pipeline fails
        ↓
Deployment never occurs
```

## Tech Stack
* Application: Python (FastAPI), External AI Inference API

* Version Control: GitHub (Repositories, Branch Protection, Webhooks)

* CI/CD Orchestration: GitHub Actions

* Security Tooling: [Trivy](https://trivy.dev/), [Gitleaks](https://github.com/gitleaks/gitleaks), [Hadolint](https://github.com/hadolint/hadolint)

* Containerization: [Docker](https://docs.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

* Cloud Hosting: [Render](https://render.com/) / [Fly.io](https://fly.io/) (Free Tier)

* Monitoring: [UptimeRobot](https://uptimerobot.com) & Discord [Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Production Limitations
> This project is an educational demonstration and is not intended for production use. The deployment platform uses a free-tier environment, so production availability guarantees are not applicable. In a production deployment, additional controls such as centralized secrets management, stronger authentication, comprehensive observability, infrastructure-as-code, artifact provenance, and multi-environment promotion would be considered.

## Getting Started Locally

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed.
- A free API key from your AI provider (e.g., Hugging Face).

### Installation & Execution
1. **Clone the repository:**


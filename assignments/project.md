
# Project Proposal: Secure AI-Powered REST Microservice with Automated DevSecOps Pipeline

> A production-grade, end-to-end CI/CD pipeline and microservice demonstrating modern DevSecOps practices, software supply chain security, and automated cloud deployment.

## Project Overview
This project bridges the gap between software development and cloud operations. Rather than focusing heavily on complex application logic, the core engineering centers on establishing automated guardrails, ensuring that code changes are rigorously tested, scanned for security vulnerabilities, and deployed safely without manual intervention.
The application itself is a lightweight REST microservice that processes user requests by securely integrating with a free public AI model API.

## Key Features & DevOps Practices
* **Shift-Left Security:** Automated secret detection [`Gitleaks`](https://github.com/gitleaks/gitleaks), static code analysis, and container vulnerability scanning [`Trivy`](https://trivy.dev/) that block insecure code before it reaches production.
* **Continuous Integration (CI):** Automated linting, unit testing, and container builds triggered on every pull request and merge via GitHub Actions.
* **Continuous Deployment (CD):** Zero-downtime, automated deployment of immutable Docker containers to a cloud platform upon a successful merge to the main branch.
* **Supply Chain Transparency:** Automated validation of base images and dependency trees.
* **Observability:** Post-deployment uptime monitoring and instant notification webhooks to alert developers of downtime.


## Architecture Overview

```text
[ Developer Commit ] 
        │
        ▼
   [ GitHub Repo ] ──(Branch Protection & PR Checks)
        │
        ▼
[ GitHub Actions CI/CD Pipeline ]
   ├── 1. Run Unit Tests & Linters
   ├── 2. Scan for Leaked Secrets (Gitleaks)
   ├── 3. Build Docker Container
   ├── 4. Scan Container for Vulnerabilities (Trivy)
   └── 5. Deploy to Cloud PaaS (Render / Fly.io)
        │
        ▼
[ Live AI Microservice ] ──(Queries)──> [ External AI API ]
        │
        ▼
[ Automated Uptime Monitoring (UptimeRobot)]
```

## Tech Stack
* Application: Python (FastAPI), External AI Inference API

* Version Control: GitHub (Repositories, Branch Protection, Webhooks)

* CI/CD Orchestration: GitHub Actions

* Security Tooling: [Trivy](https://trivy.dev/), [Gitleaks](https://github.com/gitleaks/gitleaks), [Hadolint](https://github.com/hadolint/hadolint)

* Containerization: [Docker](https://docs.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

* Cloud Hosting: [Render](https://render.com/) / [Fly.io](https://fly.io/) (Free Tier)

* Monitoring: [UptimeRobot](https://uptimerobot.com) & Discord [Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

## Getting Started Locally

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed.
- A free API key from your AI provider (e.g., Hugging Face).

### Installation & Execution
1. **Clone the repository:**


# Weekly Status Report

## Week 1
* **Completed:** Initialized project directory, created FastAPI boilerplate, set up `requirements.txt` and `.gitignore`.
* **Completed:** Wrote `Dockerfile` and `docker-compose.yml`, resolved WSL socket permissions, and successfully ran the containerized application locally.

## Week 2
* **Completed:** Designed and deployed the Continuous Integration (CI) pipeline using GitHub Actions (`.github/workflows/ci.yml`).
* **Completed:** Integrated automated DevSecOps tools into the CI pipeline: Gitleaks (secret scanning), Hadolint (Dockerfile linting), and Trivy (container vulnerability scanning).
* **Completed:** Configured the pipeline to automatically build the Docker image whenever code is pushed to the main branch.


* **Blockers:** None currently.
* **Next Steps:** Establish Continuous Deployment (CD) to a cloud environment and configure UptimeRobot monitoring.

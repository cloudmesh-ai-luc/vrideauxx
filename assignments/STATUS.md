# Updates
Project updates

## Completed
* **Completed:** Initialized project directory, created FastAPI boilerplate, set up `requirements.txt` and `.gitignore`
* **Completed:** Wrote `Dockerfile` and `docker-compose.yml`, resolved WSL socket permissions, and successfully ran the containerized application locally
* **Completed:** Designed and deployed the Continuous Integration (CI) pipeline using GitHub Actions (`.github/workflows/ci.yml`)
* **Completed:** Integrated automated DevSecOps tools into the CI pipeline: Gitleaks (secret scanning), Hadolint (Dockerfile linting), and Trivy (container vulnerability scanning)
* **Completed:** Configured the pipeline to automatically build the Docker image whenever code is pushed to the main branch
* **Completed:** Installed Cline and linked to Jetstream2. Verified that it is linked.

## Upcoming
* **Next Steps:** Establish Continuous Deployment (CD) to a cloud environment and configure UptimeRobot monitoring.

* **Blockers:** None currently.
# Updates
Project and `cloudmesh-ai-vm` progress updates.

## Completed
* **Project Setup:** Initialized project directory, created FastAPI boilerplate, and set up `requirements.txt` and `.gitignore`.
* **Containerization:** Wrote `Dockerfile` and `docker-compose.yml`, resolved WSL socket permissions, and successfully ran the containerized application locally.
* **DevSecOps CI Pipeline:** Designed and deployed the Continuous Integration (CI) pipeline using GitHub Actions (`.github/workflows/ci.yml`) with Python tests, Ruff linting, Gitleaks (secret scanning), Hadolint (Dockerfile linting), and Trivy (container vulnerability scanning).
* **Automated Image Builds:** Configured the pipeline to automatically build the Docker image whenever code is pushed to the `main` branch.
* **Documentation Site:** Configured MkDocs (`mkdocs.yml`) using the Material theme (`vrideauxx Documentation`) with site navigation linked to `index.md` and `project/project.md`.
* **Cloud Tooling & Provider Tests:** Installed Cline and verified linkage to Jetstream2. Implemented Multipass and Chameleon credential tests for `cloudmesh-ai-vm`.

## Cloudmesh-ai-vm Weekly Progress (Branch: `dev3`)
* **Branch Sync & Smoke Testing:** Keeping local repository synchronized with upstream `dev3` (including recent merges such as PR #119) and running existing smoke tests alongside provider `pytest` suites.
* **LLM-Assisted Review & Issue Verification:** Reviewing `dev3` provider modules with an LLM to identify targeted improvements, checking open/closed issues and PRs in `https://github.com/cloudmesh-ai/cloudmesh-ai-vm` to prevent duplicates, and filing unique issues where needed.
* **Provider Progress (3 Providers):**
  * **Provider 1 — WSL2:** Auditing `Wsl2Manager.py` on `dev3` (import standardization, binary detection, subprocess error handling, output normalization, and `link_ssh_dir` cleanup) and verifying local `pytest` / smoke tests before opening a PR.
  * **Provider 2 — Multipass:** Credential tests and local VM container validation implemented; verifying smoke tests on `dev3` and checking open issues for incremental improvements.
  * **Provider 3 — Chameleon Cloud:** Credential tests implemented and SSH/API setup verified; reviewing `dev3` OpenStack/Chameleon provider code and open issues to submit focused PRs.
* **Pull Requests:** Direct links to new PRs in `https://github.com/cloudmesh-ai/cloudmesh-ai-vm` will be listed below as each PR is opened.

## Project Weekly Progress (`vrideauxx`)
* **AI Inference & Deployment:** Finalizing AI compute allocation (evaluating Chameleon DGX hosting vs. external AI inference API) and establishing Continuous Deployment (CD) to a cloud environment via `cloudmesh-ai-vm`.
* **Observability:** Configuring UptimeRobot uptime monitoring and Discord Webhook alerts.
* **Documentation & Demo:** Linking `README.md` directly to the existing MkDocs documentation (`index.md` and `project/project.md`), keeping installation and execution steps current, and adding screenshots or a short walkthrough video if needed.
* **Blockers:** None currently.

## CATCHUP

### Missed Classes & Recordings
* **10/22 Lecture (Completed):** Will review lecture recording, slides, and notes per the 10/30 catch-up plan and verified configuration steps in WSL/Docker.
* **10/28 Lecture (Completed):** Reviewed lecture recording, slides, and notes per the 10/30 catch-up plan and verified configuration steps in WSL/Docker.
* **Piazza & Video Compliance:** Tracking all Piazza threads and follow-up responses via the Piazza web interface and watching lecture recordings while logged into the official Loyola University Chicago (LUC) Zoom account.

### Cloudmesh-ai-vm (Flexible / Milestone-Based Allocation)
* **Weekly Target:** ~4–6 hours/week total across all three providers (scaled dynamically by open issue availability, PR scope, and competing end-of-semester exam/schedule commitments; front-loaded earlier in the week where possible).
* **Provider 1 — WSL2:**
  * **Planned Hours:** ~1–2 hours/week (variable; Nov 14–18 focus)
  * **Status:** Syncing with `dev3`, verifying local `Wsl2Manager.py` cleanup and smoke/`pytest` checks, and preparing a focused PR.
* **Provider 2 — Multipass:**
  * **Planned Hours:** ~1–2 hours/week (variable; Nov 14–18 focus)
  * **Status:** Credential tests working; running `dev3` smoke tests and checking open Multipass issues for small PR contributions.
* **Provider 3 — Chameleon Cloud:**
  * **Planned Hours:** ~1–2 hours/week (variable; Nov 14–18 focus)
  * **Status:** Credential tests working; auditing `dev3` provider code and open issues to submit incremental PRs.

### Project: Secure AI-Powered REST Microservice with Automated DevSecOps Pipeline (Flexible / Milestone-Based Allocation)
* **Planned Hours:** ~3–6 hours/week (variable, milestone-driven)
* **Status:** Because the core FastAPI service, Docker Compose setup, MkDocs documentation site, and GitHub Actions DevSecOps CI pipeline (Ruff, Gitleaks, Hadolint, Trivy) are already complete, remaining hours scale dynamically around milestone completion—specifically CD automation via `cloudmesh-ai-vm`, final AI inference integration, UptimeRobot/Discord alerts, and linking `README.md` to the MkDocs site.
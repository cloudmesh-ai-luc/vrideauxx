## Project : Secure AI-Powered REST Microservice with Automated DevSecOps Pipeline

Changes to [`.gitignore`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/.gitignore) are in progress. The current .gitignore includes Python cache files, `.env`, `venv/`, and `.pytest_cache/`, but will be expanded for `.venv/`, `.env.*`, coverage, build outputs, editor files, and other generated artifacts as applicable.

```I will work on looking into your question about a shared repo and add an md file with the research on piazza.```

```For the `make check`, the intended development workflow is `make check` locally before `git add`, `git commit`, and pushing a PR. That target should execute the same relevant tests and static/security checks as CI, including Ruff, Hadolint, Gitleaks, and Trivy where installed. Implementation and successful execution of `make check` have not yet been verified. It's still currently an action item.```

## Completed
* **Completed:** Initialized project directory, created FastAPI boilerplate, set up [`requirements.txt`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/requirements.txt) and [`.gitignore`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/.gitignore)
* **Completed:** Wrote [`Dockerfile`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/Dockerfile) and [`docker-compose.yml`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/docker-compose.yml), resolved WSL socket permissions, and successfully ran the containerized application locally
* **Completed:** Designed and deployed the Continuous Integration (CI) pipeline using GitHub Actions ([`.github/workflows/ci.yml`](https://github.com/cloudmesh-ai-luc/vrideauxx/blob/main/.github/workflows/ci.yml))


## Upcoming

* **Next Steps:** Establish Continuous Deployment (CD) to a cloud environment and configure UptimeRobot monitoring.

  ```GitHub Actions could deploy to cloud services when the runner has network access and appropriate credentials. The current CI workflow only builds and scans; it has no deployment job or target to configure. Locally, deployment could be tested with Docker Compose and a shell script or Make target using environment variables kept outside Git. For a free class project, I would use GitHub Actions for CI and a small manually triggered deployment or self-hosted runner only when appropriate. For a large enterprise, I would evaluate GitHub Actions alongside Jenkins or another enterprise CI/CD platform based on security controls, network access, auditability, approvals, support, and operational cost; Jenkins offers infrastructure control but requires maintenance.```

## Project Weekly Progress (`vrideauxx`)

* **AI Inference & Deployment:** Finalizing AI compute allocation (evaluating Chameleon DGX hosting vs. external AI inference API) and establishing Continuous Deployment (CD) to a cloud environment via `cloudmesh-ai-vm`.
* **Observability:** Configuring UptimeRobot uptime monitoring and Discord Webhook alerts.
* **Documentation & Demo:** Linking `README.md` directly to the existing MkDocs documentation (`index.md` and `project/project.md`), keeping installation and execution steps current, and adding screenshots or a short walkthrough video if needed.


# Updates

**Clarification:** The completed items below relate to the class microservice project; cloudmesh-ai-vm contributions are documented separately in Cloudmesh-ai-vm Weekly Progress and Verified Cloudmesh Contribution Evidence below.

## Completed

### Verified Cloudmesh Contribution Evidence
* **October 4–5, 2026 — Merged PR:** [PR #24 — Contributions to Code](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/24), authored by `vrideauxx`, merged by `laszewsk` on October 5 into `main`. The PR includes [commit `d0dbedb`](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/commit/d0dbedb): added `test-multipass-with-credentials.py` in `tests/smoke-class` and updated `factory.py`. The PR description reports the test passed; this is one merged contribution, not an additional PR.
* **October 24, 2026 — Smoke-test issue reporting on `dev2`:**
  * [Issue #92 — Multipass invalid instance name (underscores)](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/issues/92).
  * [Issue #93 — Jetstream OpenStack SDK cloud resolution](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/issues/93).
  * [Issue #94 — Chameleon hardcoded SSH key path](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/issues/94).
* **Issue disposition:** All three issues are closed. The Chameleon report was reproduced and addressed by the instructor; the Multipass and Jetstream failures were not reproduced by the instructor. These are issue reports, not claims that I implemented fixes.
* **Status of further work:** WSL2 provider debugging and `dev3` compliance/smoke checks remain in progress. No additional PR is claimed here until a link is available.
* **Determined what the issue was with GitHub disconnect; created `work` directory with `vrideauxx`, `cloudmesh-ai-vm`, and `cloudmesh-ai-llm-mock` cloned. 
* Created video demo of CLI proficiency. Video to be uploaded to Piazza with screenshots included.


## Cloudmesh-ai-vm Weekly Progress (Branch: `dev3`)
* **Branch Sync & Smoke Testing:** Keeping local repository synchronized with upstream `dev3` (including recent merges such as PR #119) and running existing smoke tests alongside provider `pytest` suites.
* **LLM-Assisted Review & Issue Verification:** Reviewing `dev3` provider modules with an LLM to identify targeted improvements, checking open/closed issues and PRs in `https://github.com/cloudmesh-ai/cloudmesh-ai-vm` to prevent duplicates, and filing unique issues where needed.
* **Provider Progress (3 Providers):**
  * **Provider 1 — WSL2:** 

       **Previous Progress** Auditing `Wsl2Manager.py` on `dev3` (import standardization, binary detection, subprocess error handling, output normalization, and `link_ssh_dir` cleanup) and verifying local `pytest` / smoke tests before opening a PR.

    **Nov 17, 2026**

    * **Integration test fix.** Updated the shared fixture to read `name` from `provider.list()` and the info test to check `Name` from `provider.info()`.
    * **Cline review.** Used Cline to review `Wsl2Manager.py`. Cline identified that `run_command()` returns command failures as strings and suggested a broader provider refactor. I checked the suggestion against the source and used the reproduced `KeyError` to scope this PR to the two test expectations.
    * **Verification.** Before the fix, all three selected tests errored during setup with `KeyError: 'Name'`. After the fix, Windows Git Bash reported `3 passed, 7 deselected in 6.55s`.
    * **Pull request.** [PR #130 — Fix stale WSL2 integration test expectations](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/pull/130) is open against `dev3`.
      * merged into `dev3` Nov19.
    
  * **Provider 2 — Multipass:** 
  
    **Previous Progress:** Credential tests and local VM container validation implemented; verifying smoke tests on `dev3` and checking open issues for incremental improvements.
  
    **Nov 22, 2026**

    * **`info()` fix.** Updated the plain-text fallback to return `status` from `state` and default `ipv4` to `[]` and `ip` to `""` when no IPv4 address is reported. Preserved the existing `State` alias.
    * **Cline review.** Cline identified the missing fields and proposed a regression test for a stopped VM with no IPv4 address. I reviewed the proposal against the source and applied the fix. The regression tests cover output with and without a `State` line.
    * **Cross-provider check.** WSL2 and Chameleon use different `info()` paths and do not share the Multipass plain-text fallback.
    * **Verification.** Ran `python -m pytest -q tests/unit/test_multipass_manager*.py` in Windows Git Bash. Result was `27 passed in 1.23s`. Live smoke testing is pending.
    * **Pull request.** Pending submission against `dev3`.


  * **Provider 3 — Chameleon Cloud:** Credential tests implemented and SSH/API setup verified; reviewing `dev3` OpenStack/Chameleon provider code and open issues to submit focused PRs.
* **Pull Requests:** Direct links to new PRs in [https://github.com/cloudmesh-ai/cloudmesh-ai-vm](https://github.com/cloudmesh-ai/cloudmesh-ai-vm) will be listed below as each PR is opened.


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
* **Status:** Because the core FastAPI service, Docker Compose setup, MkDocs documentation site are already complete, remaining hours scale dynamically around GitHub Actions DevSecOps CI pipeline (Ruff, Gitleaks, Hadolint, Trivy) milestone completion—specifically CD automation via `cloudmesh-ai-vm`, final AI inference integration, UptimeRobot/Discord alerts, and linking `README.md` to the MkDocs site.

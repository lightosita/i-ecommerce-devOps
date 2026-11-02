# Nexvion: E-Commerce DevOps and Cloud-Native Delivery Platform

A DevOps delivery platform built around Nexvion, a static HTML/CSS/JavaScript storefront. The application is a front end only: login, cart and payment run in the browser as demo code, with no backend or database. The project is about the delivery pipeline around it.

## Repository layout

| Folder | Contents |
|---|---|
| `application/` | The Nexvion storefront (unchanged from the supplied app) |
| `docker/` | Dockerfile, Nginx config with `/health`, Docker Compose |
| `scripts/` | setup, deploy, health-check, backup and cleanup Bash scripts |
| `jenkins/` | Jenkinsfile (checkout, build, test, scan, push, deploy, health check) |
| `terraform/` | Azure resource group, network, firewall, public IP and VM |
| `ansible/` | Inventory, playbook and the VM Compose file |
| `kubernetes/` | Namespace, deployment, service, configmap, secret, ingress, kind config |
| `monitoring/` | Prometheus, Grafana, blackbox exporter and cAdvisor |
| `security/` | Gitleaks and Trivy reports, security notes |
| `ai/` | Rule-based log and incident analyzer |
| `docs/` | Architecture and troubleshooting notes |

## Workflow

Branches: `feature/*` into `develop` through pull requests, then `develop` into `main` for release.
Flow: GitHub, Jenkins (checkout, build, test, secret scan, image scan, push to Docker Hub, deploy, health check), Docker image `lightosita/nexvion`.

## How to run

- Local container: `./scripts/deploy.sh` (app on http://localhost:8081, health at /health)
- Monitoring: `docker compose -f monitoring/docker-compose.monitoring.yml up -d` (Prometheus :9091, Grafana :3001, cAdvisor :8082)
- Kubernetes (kind): `kind create cluster --name nexvion --config kubernetes/kind-config.yaml`, install the ingress-nginx controller, then `kubectl apply -f kubernetes/` (app on http://localhost:8088)
- Incident analysis: `python3 ai/incident-analysis/analyze.py <logfile>`

## Project status

| Area | Status |
|------|--------|
| Source control (feature/develop/main, PRs) | Done |
| Bash scripts | Done |
| Docker and Docker Compose | Done |
| Jenkins CI/CD pipeline | Done |
| Security scanning (Trivy, Gitleaks) | Done |
| Terraform on Azure | Done: 8 resources applied, then destroyed to avoid cost |
| Ansible | Written and tested locally; not run against an Azure VM (VM destroyed to avoid cost) |
| Kubernetes (local kind cluster) | Done |
| Prometheus and Grafana | Done |
| AI incident analysis | Done (rule-based, not an LLM) |
| Helm | Not done |
| Blue-Green and Canary | Not done (rolling updates only) |
| ELK stack | Not done |

## Known limitations

- The Azure VM was destroyed after testing, so there is no live cloud deployment.
- The app is static, with no backend or database.
- `kubernetes/secret.yaml` holds a placeholder, not a real secret.
- See `security/SECURITY.md` for the scan results.

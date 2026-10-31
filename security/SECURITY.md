# Security controls

## Implemented
- Secret scanning: Gitleaks runs in the Jenkins pipeline and was run locally (report in this folder).
- Image scanning: Trivy runs in the pipeline and fails the build on CRITICAL findings. Build 1 was blocked by 3 CRITICAL Alpine package findings; fixed with `apk upgrade` in the Dockerfile; build 2 passed.
- Pinned base image tag (nginx:1.27-alpine) for repeatable builds.
- .dockerignore keeps source control history and infrastructure folders out of the image.
- Kubernetes: resource limits, readiness and liveness probes, rolling updates with zero unavailable pods.
- Terraform: firewall allows only ports 22 and 80; VM login is SSH-key only.
- .gitignore excludes keys, state files and plan files from version control.

## Known gaps and what production would add
- SSH is open to all addresses in the demo firewall; production would restrict it to a known IP or use a bastion host.
- Nginx master process runs as root inside the container; production would use an unprivileged Nginx image.
- Kubernetes Secrets are base64-encoded, not encrypted; the demo secret is a placeholder. Production would use an external secret manager.
- No dependency scan: the application has no package manifest (static frontend), so there is nothing to scan.
- Application login and payment are browser-side demo code, not real authentication.

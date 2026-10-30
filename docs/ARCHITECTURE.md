# Architecture

See the architecture diagram in the report PDF.
Flow: GitHub -> Jenkins (test, scan, build, push) -> Docker image -> Compose / Kubernetes -> Prometheus and Grafana; logs -> AI analyzer; Terraform and Ansible written for Azure.

#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker compose -f docker/docker-compose.yml up -d --build
for i in $(seq 1 10); do
  if ./scripts/health-check.sh; then
    echo "Deployment verified"
    exit 0
  fi
  sleep 3
done
echo "Deployment FAILED health verification" >&2
exit 1

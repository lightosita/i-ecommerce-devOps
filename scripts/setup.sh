#!/usr/bin/env bash
set -euo pipefail
for tool in git docker curl; do
  command -v "$tool" > /dev/null || { echo "Missing: $tool" >&2; exit 1; }
done
docker compose version > /dev/null || { echo "Missing: docker compose" >&2; exit 1; }
echo "Environment ready:"
git --version
docker --version
docker compose version

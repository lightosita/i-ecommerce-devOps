#!/usr/bin/env bash
set -euo pipefail
URL="${1:-http://localhost:8081/health}"
if curl -fsS --max-time 3 "$URL" > /dev/null; then
  echo "OK: $URL"
else
  echo "FAIL: $URL" >&2
  exit 1
fi

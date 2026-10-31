#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p backups
FILE="backups/nexvion-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czf "$FILE" application docker
echo "Backup created: $FILE"

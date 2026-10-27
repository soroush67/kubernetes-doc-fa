#!/usr/bin/env bash
# Start the translation service in the background (web UI + update button on :8460).
set -euo pipefail
cd "$(dirname "$0")"
[ -x .venv/bin/python ] || { python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt; }
if [ ! -e website ] && [ -z "${K8S_WEBSITE:-}" ]; then
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/kubernetes/website.git website
  git -C website sparse-checkout set content/en
fi
if [ -f state/service.pid ] && kill -0 "$(cat state/service.pid)" 2>/dev/null; then
  echo "already running (pid $(cat state/service.pid))"; exit 0
fi
mkdir -p state
nohup .venv/bin/python service.py serve >> service.log 2>&1 &
echo $! > state/service.pid
sleep 1
echo "service running: http://${HOST:-127.0.0.1}:${PORT:-8460}/  (log: service.log)"

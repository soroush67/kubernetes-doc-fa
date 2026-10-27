#!/usr/bin/env bash
# Ask a running update to stop (it commits + pushes what is done), then stop the service.
set -uo pipefail
cd "$(dirname "$0")"
curl -fsS -X POST "http://${HOST:-127.0.0.1}:${PORT:-8460}/api/stop" >/dev/null 2>&1 && {
  echo "waiting for the running update to finish its current chunks..."
  while curl -fsS "http://${HOST:-127.0.0.1}:${PORT:-8460}/api/status" 2>/dev/null | grep -q '"running": true'; do sleep 5; done
}
[ -f state/service.pid ] && kill "$(cat state/service.pid)" 2>/dev/null && rm -f state/service.pid && echo stopped

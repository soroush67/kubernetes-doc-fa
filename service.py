#!/usr/bin/env python3
"""Translation service: serves html/ and, on demand, brings the Persian docs up to date.

  service.py serve [--port 8460]   web UI with the update button (POST /api/update)
  service.py update [--no-pull]    one update run in the foreground (e.g. from cron)

An update run: pull the English source -> find pages that are new, changed, or not yet
translated (by source hash in manifest.json) -> translate only those -> rebuild html/,
README.md, INDEX.md -> git commit + push, also every COMMIT_EVERY pages along the way.
"""
import argparse
import json
import os
import subprocess
import sys
import threading
import time
import traceback
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import readme
from check import check
from common import EN_DOCS, MD, OUT, ROOT, SITE, SOURCE_REPO, load_manifest, now, save_manifest, sha, sources
from translate import MODEL, Limiter, Stopped, translate_page

WORKERS = int(os.environ.get("WORKERS", "2"))
COMMIT_EVERY = int(os.environ.get("COMMIT_EVERY", "15"))
# pages translated by these models are redone (Sonnet output read too stiffly)
REDO_MODELS = set(filter(None, os.environ.get("REDO_MODELS", "sonnet").split(",")))


def sh(*cmd, cwd=ROOT, check=True):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"{' '.join(cmd)}: {(p.stderr or p.stdout).strip()[-400:]}")
    return p.stdout.strip()


class Runner:
    def __init__(self):
        self.lock = threading.Lock()
        self.publish_lock = threading.Lock()
        self.thread = None
        self.limiter = Limiter()
        self.log = deque(maxlen=60)
        self.state = {"running": False, "phase": "idle"}
        self.current = {}

    def say(self, msg):
        line = f"{time.strftime('%H:%M:%S')} {msg}"
        self.log.append(line)
        print(line, flush=True)

    # ------------------------------------------------------------ control
    def start(self, pull=True, retry_issues=False):
        with self.lock:
            if self.state["running"]:
                return False
            self.limiter = Limiter()
            self.state = {"running": True, "phase": "starting", "started": now(), "todo": 0, "done": 0, "issues": 0}
            self.thread = threading.Thread(target=self.run, args=(pull, retry_issues), daemon=True)
            self.thread.start()
            return True

    def stop(self):
        self.limiter.stop.set()
        self.say("stop requested: finishing current chunks, then commit + push")

    def status(self):
        m = load_manifest()
        src = sources()
        ok = sum(1 for r in src if r in m["files"])
        return {**self.state, "current": dict(self.current), "log": list(self.log)[-15:],
                "paused_until": self.limiter.until if self.limiter.until > time.time() else None,
                "translated": ok, "total": len(src), "model": MODEL, "workers": WORKERS}

    # ------------------------------------------------------------ pipeline
    def run(self, pull, retry_issues):
        m = load_manifest()
        run = {"started": now(), "translated": 0, "issues": 0, "removed": 0}
        try:
            if pull:
                self.state["phase"] = "pull"
                m["source_commit"] = pull_source(self.say)
            elif SITE.exists():
                m["source_commit"] = sh("git", "rev-parse", "HEAD", cwd=SITE, check=False) or m.get("source_commit")
            run["source_commit"] = m["source_commit"]
            self.state["phase"] = "plan"
            todo, run["removed"] = plan(m, retry_issues, self.say)
            save_manifest(m)
            self.state.update(phase="translate", todo=len(todo))
            self.say(f"{len(todo)} pages to translate, {WORKERS} workers, model {MODEL}")
            with ThreadPoolExecutor(WORKERS) as pool:
                for f in [pool.submit(self.work, m, rel, run) for rel in todo]:
                    f.result()
            run["result"] = "stopped" if self.limiter.stop.is_set() else "done"
        except Stopped:
            run["result"] = "stopped"
        except Exception as e:
            run["result"] = f"error: {e}"
            self.say(traceback.format_exc(limit=3))
        finally:
            run["finished"] = now()
            m["runs"] = (m.get("runs", []) + [run])[-50:]
            save_manifest(m)
            self.state["phase"] = "publish"
            try:
                self.publish(m, f"update: {run['translated']} pages translated ({run['result']})")
            except Exception as e:
                self.say(f"publish failed: {e}")
            self.say(f"run finished: {run['result']}")
            self.state.update(running=False, phase="idle", last_run=run)

    def work(self, m, rel, run):
        if self.limiter.stop.is_set():
            return
        text = (EN_DOCS / rel).read_text(encoding="utf-8")
        self.current[rel] = "start"
        try:
            fa, issues = translate_page(rel, text, self.limiter,
                                        on_chunk=lambda i, n: self.current.__setitem__(rel, f"{i}/{n}"))
        except Stopped:
            return
        except Exception as e:
            self.say(f"{rel}: {e}")
            return
        finally:
            self.current.pop(rel, None)
        out = MD / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fa, encoding="utf-8")
        with self.lock:
            m["files"][rel] = {"sha": sha(text), "status": "issues" if issues else "ok", "issues": issues[:5],
                               "model": MODEL, "at": now()}
            run["translated"] += 1
            run["issues"] += bool(issues)
            self.state["done"] = run["translated"]
            self.state["issues"] = run["issues"]
            save_manifest(m)
            due = run["translated"] % COMMIT_EVERY == 0
        self.say(f"translated {rel}" + (f" ({len(issues)} issues)" if issues else ""))
        if due and self.publish_lock.acquire(blocking=False):  # a slow publish never blocks translating
            try:
                self.publish(m, f"progress: {run['translated']} pages translated")
            except Exception as e:
                self.say(f"publish failed: {e}")
            finally:
                self.publish_lock.release()

    def publish(self, m, message):
        with self.lock:
            snapshot = json.loads(json.dumps(m))
        sh(sys.executable, "build_html.py")
        readme.write(snapshot)
        sh("git", "add", "-A", "md", "html", "manifest.json", "README.md", "INDEX.md")
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode == 0:
            return
        sh("git", "commit", "-qm", f"{message}\n\nCo-Authored-By: Claude {MODEL.capitalize()} 5.5 <noreply@anthropic.com>")
        push = subprocess.run(["git", "push", "-q"], cwd=ROOT, capture_output=True, text=True)
        self.say(f"committed: {message}" + ("" if push.returncode == 0 else f" (push failed: {push.stderr.strip()[-200:]})"))


def pull_source(say) -> str:
    """Clone (sparse: content/en only) or fast-forward the English source; return its commit."""
    if not SITE.exists():
        say(f"cloning {SOURCE_REPO} (content/en only)")
        sh("git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", SOURCE_REPO, str(SITE))
        sh("git", "sparse-checkout", "set", "content/en", cwd=SITE)
    elif sh("git", "status", "--porcelain", cwd=SITE, check=False):
        say("source checkout has local changes: not pulling, translating what is there")
    else:
        sh("git", "fetch", "-q", "--depth", "1", "origin", "main", cwd=SITE)
        sh("git", "reset", "-q", "--hard", "FETCH_HEAD", cwd=SITE)
    commit = sh("git", "rev-parse", "HEAD", cwd=SITE)
    say(f"source at {commit[:12]}")
    return commit


def plan(m, retry_issues, say):
    """Return (pages to translate, number removed). Pages translated before the manifest
    existed are adopted when they pass the check against the current source."""
    src, files = sources(), m["files"]
    removed = [r for r in files if r not in src]
    for rel in removed:
        (MD / rel).unlink(missing_ok=True)
        del files[rel]
    todo = []
    for rel, path in src.items():
        h, e = sha(path.read_text(encoding="utf-8")), files.get(rel)
        if (e and e["sha"] == h and (MD / rel).exists() and (e["status"] == "ok" or not retry_issues)
                and e["model"] not in REDO_MODELS):
            continue
        if not e and (MD / rel).exists() and not check(rel):
            files[rel] = {"sha": h, "status": "ok", "issues": [], "model": "opus (agents)", "at": now()}
            continue
        todo.append(rel)
    todo.sort(key=lambda r: r in files)  # untranslated pages first, then redos
    say(f"plan: {len(src)} pages, {len(todo)} to translate, {len(removed)} removed upstream")
    return todo, len(removed)


RUNNER = Runner()


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/api/status"):
            return self.send_json(RUNNER.status())
        super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/update"):
            started = RUNNER.start(pull="pull=0" not in self.path, retry_issues="retry_issues=1" in self.path)
            return self.send_json({"started": started}, 202 if started else 409)
        if self.path.startswith("/api/stop"):
            RUNNER.stop()
            return self.send_json({"stopping": True})
        self.send_json({"error": "not found"}, 404)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("serve")
    s.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8460")))
    s.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    u = sub.add_parser("update")
    u.add_argument("--no-pull", action="store_true")
    u.add_argument("--retry-issues", action="store_true")
    a = ap.parse_args()
    if a.cmd == "update":
        RUNNER.start(pull=not a.no_pull, retry_issues=a.retry_issues)
        try:
            RUNNER.thread.join()
        except KeyboardInterrupt:
            RUNNER.stop()
            RUNNER.thread.join()
        return
    port, host = (a.port, a.host) if a.cmd == "serve" else (8460, "127.0.0.1")
    OUT.mkdir(exist_ok=True)
    srv = ThreadingHTTPServer((host, port), partial(Handler, directory=str(OUT)))
    print(f"serving http://{host}:{port}/  (model {MODEL}, {WORKERS} workers)", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()

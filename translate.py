"""Translate one page with headless `claude -p` (subscription, no tools, short system prompt).

A page is cut into chunks of about CHUNK_WORDS English words at heading (or blank-line)
boundaries outside code fences; each chunk is translated and checked on its own and
retried with the checker's findings, so a long page never comes back truncated.
"""
import glob
import json
import os
import re
import shutil
import subprocess
import threading
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from check import check_text
from common import ROOT, STATE, words

MODEL = os.environ.get("TRANSLATE_MODEL", "opus")
CHUNK_WORDS = int(os.environ.get("CHUNK_WORDS", "2500"))
RETRIES = 2
PROMPT = (ROOT / "prompt.md").read_text(encoding="utf-8")
FENCE = re.compile(r"^\s*(```|~~~)")


class Stopped(Exception):
    pass


class Limiter:
    """Shared pause: when one call hits the subscription limit, every worker waits for the reset."""

    def __init__(self):
        self.until = 0.0
        self.stop = threading.Event()

    def wait(self):
        while time.time() < self.until:
            if self.stop.wait(min(30, self.until - time.time())):
                raise Stopped
        if self.stop.is_set():
            raise Stopped

    def hit(self, message: str):
        until = reset_time(message)
        if until > self.until:
            print(f"{time.strftime('%H:%M:%S')} subscription limit hit, waiting until "
                  f"{time.strftime('%H:%M', time.localtime(until))}: {message[:120]}", flush=True)
        self.until = max(self.until, until)


def reset_time(message: str) -> float:
    """'resets 2:30pm (Asia/Tehran)' or 'resets Oct 31, 7:30am (Asia/Tehran)' -> epoch (+2 min);
    30 min from now if unparsable."""
    m = re.search(r"resets\s+(?:([A-Z][a-z]{2})\s+(\d{1,2}),\s*)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)(?:\s*\(([^)]+)\))?",
                  message, re.I)
    if not m:
        return time.time() + 1800
    mon, day, h, mi, ampm, zone = m.groups()
    hour = int(h) % 12 + (12 if ampm.lower() == "pm" else 0)
    try:
        tz = ZoneInfo(zone) if zone else None
    except Exception:
        tz = None
    now = datetime.now(tz)
    at = now.replace(hour=hour, minute=int(mi or 0), second=0, microsecond=0)
    if mon:
        at = at.replace(month=datetime.strptime(mon, "%b").month, day=int(day))
        if at < now - timedelta(days=180):
            at = at.replace(year=at.year + 1)
    elif at <= now:
        at += timedelta(days=1)
    return at.timestamp() + 120


def claude_bin() -> str:
    found = os.environ.get("CLAUDE_BIN") or shutil.which("claude")
    if found:
        return found
    hits = sorted(glob.glob(os.path.expanduser(
        "~/.vscode-server/extensions/anthropic.claude-code-*/resources/native-binary/claude")))
    if not hits:
        raise RuntimeError("claude CLI not found; set CLAUDE_BIN")
    return hits[-1]


def chunks(text: str) -> list[str]:
    """Split at '##'/'###' headings outside fences; oversized sections again at blank lines."""
    sections, cur, infence = [], [], False
    for ln in text.split("\n"):
        if FENCE.match(ln):
            infence = not infence
        if not infence and re.match(r"^#{2,3}\s", ln) and cur:
            sections.append(cur); cur = []
        cur.append(ln)
    sections.append(cur)
    pieces = []
    for sec in sections:
        if words("\n".join(sec)) <= CHUNK_WORDS:
            pieces.append(sec); continue
        part, infence = [], False
        for ln in sec:
            if FENCE.match(ln):
                infence = not infence
            part.append(ln)
            if not infence and not ln.strip() and words("\n".join(part)) >= CHUNK_WORDS:
                pieces.append(part); part = []
        if part:
            pieces.append(part)
    out, cur = [], []
    for p in pieces:
        if cur and words("\n".join(cur + p)) > CHUNK_WORDS:
            out.append("\n".join(cur)); cur = []
        cur += p
    out.append("\n".join(cur))
    return [c for c in out if c.strip()] or [text]


def call(prompt: str, limiter: Limiter) -> str:
    STATE.mkdir(exist_ok=True)
    failures = 0
    while True:
        limiter.wait()
        p = subprocess.run(
            [claude_bin(), "-p", "--model", MODEL, "--tools", "", "--system-prompt", PROMPT,
             "--setting-sources", "", "--strict-mcp-config", "--no-session-persistence",
             "--output-format", "json"],
            input=prompt, capture_output=True, text=True, cwd=STATE, timeout=1800)
        try:
            res = json.loads(p.stdout)
        except json.JSONDecodeError:
            res = {"is_error": True, "result": (p.stdout + p.stderr)[-500:]}
        msg = str(res.get("result", ""))
        if not res.get("is_error") and p.returncode == 0:
            return msg
        if re.search(r"limit|429|rate", msg, re.I):
            limiter.hit(msg)
            continue
        failures += 1
        if failures > 3:
            raise RuntimeError(f"claude failed: {msg[:300]}")
        limiter.until = max(limiter.until, time.time() + 60 * failures)  # transient API error: back off


def clean(out: str) -> str:
    out = re.sub(r"^\s*</?(translation|source)>\s*|\s*</?(translation|source)>\s*$", "", out.strip())
    m = re.fullmatch(r"```(?:markdown|md)?\n(.*)\n```", out, re.S)
    return m.group(1) if m else out


def translate_chunk(en: str, where: str, limiter: Limiter) -> tuple[str, list[str]]:
    best, best_issues = None, None
    ask = f"Page {where}. Translate this chunk.\n\n<source>\n{en}\n</source>"
    for attempt in range(RETRIES + 1):
        fa = clean(call(ask, limiter))
        issues = check_text(en, fa)
        if best is None or len(issues) < len(best_issues):
            best, best_issues = fa, issues
        if not issues:
            break
        ask = (f"Page {where}. Your previous translation of the chunk below failed these checks: "
               f"{'; '.join(issues)}. Translate the whole chunk again, fixing them.\n\n<source>\n{en}\n</source>")
    return best, best_issues


def translate_page(rel: str, text: str, limiter: Limiter, on_chunk=None) -> tuple[str, list[str]]:
    parts = chunks(text)
    out, issues = [], []
    for i, en in enumerate(parts, 1):
        fa, iss = translate_chunk(en, f"{rel} (chunk {i} of {len(parts)})", limiter)
        out.append(fa.rstrip())
        issues += [f"chunk {i}: {x}" for x in iss]
        if on_chunk:
            on_chunk(i, len(parts))
    return "\n\n".join(out) + "\n", issues

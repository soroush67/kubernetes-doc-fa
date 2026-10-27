"""Shared paths and the manifest (what has been translated, from which source version)."""
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = Path(os.environ.get("K8S_WEBSITE", ROOT / "website"))
EN_DOCS = SITE / "content/en/docs"
MD = ROOT / "md"
OUT = ROOT / "html"
STATE = ROOT / "state"
MANIFEST = ROOT / "manifest.json"
SOURCE_REPO = "https://github.com/kubernetes/website.git"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z]{2,}", text))


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def sources() -> dict[str, Path]:
    """rel path under content/en/docs -> source file, for every page to translate."""
    return {str(p.relative_to(EN_DOCS)): p for p in sorted(EN_DOCS.rglob("*.md"))}


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"source_commit": None, "files": {}, "runs": []}


def save_manifest(m: dict) -> None:
    tmp = MANIFEST.with_suffix(".tmp")
    tmp.write_text(json.dumps(m, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(MANIFEST)

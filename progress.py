#!/usr/bin/env python3
"""One-line progress: words and pages translated so far (from manifest.json)."""
from common import load_manifest, sources, words

src, files = sources(), load_manifest()["files"]
wc = {r: words(p.read_text(encoding="utf-8")) for r, p in src.items()}
done = [r for r in src if r in files]
dw, tot = sum(wc[r] for r in done), sum(wc.values())
print(f"progress {100*dw/tot:.1f}% | words {dw:,}/{tot:,} | pages {len(done)}/{len(src)}", flush=True)

#!/usr/bin/env python3
"""One-line progress: words and files translated so far (by existing output files)."""
import json, os
T = "/home/soroush/kuber-doc/fa-translation"
b = json.load(open(f"{T}/batches.json"))
units = [u for x in b for u in x["units"]]
tot = sum(u["words"] for u in units)
done = [u for u in units if os.path.exists(f"{T}/md/{u['dst']}")]
dw = sum(u["words"] for u in done)
full = sum(1 for x in b if all(os.path.exists(f"{T}/md/{u['dst']}") for u in x["units"]))
print(f"progress {100*dw/tot:.1f}% | words {dw:,}/{tot:,} | files {len(done)}/{len(units)} | batches {full}/{len(b)}", flush=True)

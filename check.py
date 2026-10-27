#!/usr/bin/env python3
"""Structural completeness check: every translated unit vs its English source.

Fails a unit when headings / fenced code blocks / shortcodes / link targets differ,
when a code block's content changed, when English prose lines were left
untranslated, or when the translation is suspiciously short (summarised/cut).
Writes check-report.json and prints a summary.
"""
import json
import re
import sys
from pathlib import Path

TR = Path("/home/soroush/kuber-doc/fa-translation")
FA = re.compile(r"[؀-ۿ]")
FENCE = re.compile(r"^\s*(```|~~~)")


def split(text):
    """-> (prose lines, code blocks, front matter)"""
    fm = ""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if m:
        fm, text = m.group(1), text[m.end():]
    prose, code, cur, infence, marker = [], [], [], False, ""
    for ln in text.split("\n"):
        f = FENCE.match(ln)
        if f and (not infence or ln.strip().startswith(marker)):
            if infence:
                code.append("\n".join(cur).strip()); cur = []
                infence = False
            else:
                infence, marker = True, f.group(1)
            continue
        (cur if infence else prose).append(ln)
    return prose, code, fm


def headings(lines):
    return [ln for ln in lines if re.match(r"^#{1,6}\s", ln)]


def shortcodes(text):
    return sorted(re.findall(r"\{\{[<%]\s*/?([\w-]+)", text))


def targets(lines):
    return sorted(re.findall(r"\]\(([^)\s]+)", "\n".join(lines)))


def english_lines(lines):
    out = []
    for ln in lines:
        s = ln.strip()
        if not s or FA.search(s) or s.startswith(("|", "<", "{{", "[", "!", "#")) and not re.search(r"[a-z]{3,} [a-z]{3,} [a-z]{3,}", s):
            continue
        words = re.findall(r"[A-Za-z]{3,}", re.sub(r"`[^`]*`|\([^)]*\)|\{\{.*?\}\}|<[^>]+>", "", s))
        if len(words) >= 7:
            out.append(s[:140])
    return out


def check(src, dst):
    en, fa = src.read_text(encoding="utf-8"), dst.read_text(encoding="utf-8")
    ep, ec, _ = split(en)
    fp, fc, _ = split(fa)
    issues = []
    if len(headings(ep)) != len(headings(fp)):
        issues.append(f"headings {len(headings(ep))} -> {len(headings(fp))}")
    if len(ec) != len(fc):
        issues.append(f"code blocks {len(ec)} -> {len(fc)}")
    else:
        changed = sum(1 for a, b in zip(ec, fc) if a != b)
        if changed:
            issues.append(f"{changed} code block(s) changed")
    if shortcodes(en) != shortcodes(fa):
        issues.append("shortcodes differ")
    te, tf = targets(ep), targets(fp)
    if te != tf:
        missing = sorted(set(te) - set(tf))
        issues.append(f"links {len(te)} -> {len(tf)}" + (f" missing {missing[:3]}" if missing else ""))
    no_comments = re.sub(r"<!--.*?-->|\{\{<\s*mermaid\s*>\}\}.*?\{\{<\s*/mermaid\s*>\}\}", "", "\n".join(fp), flags=re.S)
    no_comments = [ln for ln in no_comments.split("\n") if not ln.lstrip().startswith("|") and ln.count("|") < 2]
    left = english_lines(no_comments)
    if len(left) > 2:
        issues.append(f"{len(left)} untranslated English lines, e.g. {left[0]!r}")
    def prose(lines):  # no link targets, mermaid or HTML comments in the word count
        t = re.sub(r"\]\([^)]*\)|<!--.*?-->|\{\{<\s*mermaid\s*>\}\}.*?\{\{<\s*/mermaid\s*>\}\}|https?://\S+", " ", "\n".join(lines), flags=re.S)
        return t
    en_words = len(re.findall(r"[A-Za-z]{2,}", prose(ep)))
    fa_words = len(re.findall(r"\S+", prose(fp)))
    if en_words > 150 and fa_words < 0.75 * en_words:
        issues.append(f"short: {fa_words} words vs {en_words} source words")
    return issues


def main():
    batches = json.loads((TR / "batches.json").read_text())
    report, ok, missing = {}, 0, []
    only = set(int(x) for x in sys.argv[1:])
    for b in batches:
        if only and b["id"] not in only:
            continue
        for u in b["units"]:
            dst = TR / "md" / u["dst"]
            if not dst.exists():
                missing.append(u["dst"]); continue
            iss = check(Path(u["src"]), dst)
            if iss:
                report[u["dst"]] = {"batch": b["id"], "issues": iss}
            else:
                ok += 1
    if not only:  # per-batch runs (by translation agents) only print
        (TR / "check-report.json").write_text(json.dumps({"failed": report, "missing": missing}, ensure_ascii=False, indent=1))
    print(f"ok {ok}  failed {len(report)}  missing {len(missing)}")
    for k, v in list(report.items())[:25]:
        print(f"  {k}: {'; '.join(v['issues'])}")


if __name__ == "__main__":
    main()

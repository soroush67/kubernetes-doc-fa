#!/usr/bin/env python3
"""Structural completeness check: a Persian translation vs its English source.

Fails when headings / fenced code blocks / shortcodes / link targets differ,
when a code block's content changed, when English prose lines were left
untranslated, or when the translation is suspiciously short (summarised/cut).

  check.py            check every translated page, write check-report.json
  check.py <rel>...   check only these pages (paths under content/en/docs)
"""
import json
import re
import sys

from common import EN_DOCS, MD, ROOT, sources

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


def check_text(en, fa):
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
    if sorted(re.findall(r"\{#[^}]+\}", "\n".join(ep))) != sorted(re.findall(r"\{#[^}]+\}", "\n".join(fp))):
        issues.append("heading anchors {#...} differ")
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


def check(rel):
    return check_text((EN_DOCS / rel).read_text(encoding="utf-8"), (MD / rel).read_text(encoding="utf-8"))


def main():
    only = sys.argv[1:]
    rels = only or [r for r in sources() if (MD / r).exists()]
    report = {r: iss for r in rels if (iss := check(r))}
    if not only:
        (ROOT / "check-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))
    print(f"ok {len(rels) - len(report)}  failed {len(report)}")
    for k, v in list(report.items())[:25]:
        print(f"  {k}: {'; '.join(v)}")


if __name__ == "__main__":
    main()

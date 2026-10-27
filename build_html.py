#!/usr/bin/env python3
"""Render the Persian Markdown translation of the Kubernetes docs as a static HTML site.

  md/<rel>.md (+ .partNN pieces of long pages)  ->  html/<rel>.html  + html/index.html

Persian text is right-to-left; code, commands, YAML and English-only blocks are
left-to-right. Hugo shortcodes are rendered the way the real site shows them
(admonitions, tabs, feature-state, code samples from content/en/examples, ...).
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path

import yaml
from lxml import html as lh
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.attrs import attrs_plugin
from mdit_py_plugins.deflist import deflist_plugin

from common import EN_DOCS, MD, OUT, ROOT as TR, SITE

EXAMPLES = SITE / "content/en/examples"
INCLUDES_FA = TR / "includes"

VERSION = "v1.37"
PATCH = "1.37.0"
HEADINGS = {
    "objectives": "اهداف", "prerequisites": "پیش از شروع", "whatsnext": "گام‌های بعدی", "cleanup": "پاکسازی",
    "synopsis": "خلاصه", "options": "گزینه‌ها", "seealso": "همچنین ببینید", "envvars": "متغیرهای محیطی",
    "examples": "مثال‌ها", "parentoptions": "گزینه‌های ارث‌بری شده از والد", "lessoncontent": "",
}
CALLOUT = {"note": "توجه:", "caution": "احتیاط:", "warning": "هشدار:"}
STATE = {"alpha": "آلفا", "beta": "بتا", "stable": "پایدار", "deprecated": "منسوخ"}
FA = re.compile(r"[؀-ۿ]")
LATIN = re.compile(r"[A-Za-z]")

md = (MarkdownIt("commonmark", {"html": True, "typographer": False})
      .enable("table").enable("strikethrough")
      .use(anchors_plugin, min_level=2, max_level=4, permalink=False, slug_func=lambda s: re.sub(r"[^\w؀-ۿ-]+", "-", s.strip().lower()).strip("-"))
      .use(attrs_plugin).use(deflist_plugin))


# ---------------------------------------------------------------- sources

def load_pages() -> dict[str, str]:
    """rel path (as in en/docs) -> Persian markdown."""
    return {str(p.relative_to(MD)): p.read_text(encoding="utf-8") for p in sorted(MD.rglob("*.md"))}


def split_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), text[m.end():]


def url_for(rel_md: str) -> str:
    """content path -> html path (index pages become index.html of their folder)."""
    rel = rel_md[:-3]
    if rel.endswith("_index"):
        return rel[: -len("_index")] + "index.html"
    return rel + ".html"


# ---------------------------------------------------------------- shortcodes

def sc_args(s: str) -> dict:
    return dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', s))


def code_sample(file: str) -> str:
    p = EXAMPLES / file
    lang = Path(file).suffix.lstrip(".") or "text"
    body = p.read_text(encoding="utf-8") if p.is_file() else f"# {file} (not found in content/en/examples)"
    return f'\n\n<div class="code-file ltr" dir="ltr">{html.escape(file)}</div>\n\n```{lang}\n{body.rstrip()}\n```\n\n'


def include(name: str) -> str:
    name = name.strip('"').strip()
    fa = INCLUDES_FA / (name if name.endswith(".md") else name + ".md")
    if fa.exists():
        return "\n\n" + split_front_matter(fa.read_text(encoding="utf-8"))[1] + "\n\n"
    en = SITE / "content/en/includes" / (name if name.endswith(".md") else name + ".md")
    if en.exists():
        return "\n\n" + split_front_matter(en.read_text(encoding="utf-8"))[1] + "\n\n"
    return ""


def skew(args: str) -> str:
    a = args.split()
    major, minor = (int(x) for x in VERSION.lstrip("v").split("."))
    if not a:
        return VERSION.lstrip("v")
    if a[0] == "currentVersion":
        return f"{major}.{minor}"
    if a[0] == "currentPatchVersion":
        return PATCH
    if a[0] == "currentVersionAddMinor":
        delta = int(a[1]) if len(a) > 1 else 0
        sep = a[2].strip('"') if len(a) > 2 else "."
        return f"{major}{sep}{minor + delta}"
    if a[0] == "latestVersion":
        return f"{major}.{minor}"
    return f"{major}.{minor}"


def render_shortcodes(text: str, page_url: str, pages_urls: dict[str, str]) -> str:
    t = text
    # ignore commented shortcodes {{</* x */>}}
    t = re.sub(r"\{\{<\s*/\*(.*?)\*/\s*>\}\}", lambda m: "{{<" + m.group(1) + ">}}", t)
    t = re.sub(r"\{\{[<%]\s*comment\s*[>%]\}\}.*?\{\{[<%]\s*/comment\s*[>%]\}\}", "", t, flags=re.S)
    t = re.sub(r'\{\{%\s*heading\s+"(\w+)"\s*%\}\}', lambda m: HEADINGS.get(m.group(1), m.group(1)), t)
    t = re.sub(r'\{\{[<%]\s*(?:code_sample|codenew)\s+([^}]*?)[>%]\}\}',
               lambda m: code_sample(sc_args(m.group(1)).get("file", "")), t)
    t = re.sub(r'\{\{[<%]\s*include\s+"?([^">%]+)"?\s*[>%]\}\}', lambda m: include(m.group(1)), t)
    t = re.sub(r"\{\{<\s*skew\s*([^>]*?)\s*>\}\}", lambda m: skew(m.group(1)), t)
    t = re.sub(r'\{\{<\s*param\s+"(\w+)"\s*>\}\}',
               lambda m: {"version": VERSION, "fullversion": "v" + PATCH, "githubbranch": "main",
                          "docsbranch": "main"}.get(m.group(1), m.group(1)), t)
    t = re.sub(r"\{\{<\s*(latest-version|latest-semver)\s*>\}\}", VERSION, t)

    def glossary(m):
        a = sc_args(m.group(1))
        txt = a.get("text") or a.get("term_id", "").replace("-", " ")
        return f'<span class="term" title="{html.escape(a.get("term_id", ""))}">{html.escape(txt)}</span>'
    t = re.sub(r"\{\{<\s*glossary_tooltip\s+([^>]*?)>\}\}", glossary, t)
    t = re.sub(r"\{\{<\s*glossary_definition\s+([^>]*?)>\}\}",
               lambda m: f'<em>(تعریف واژه‌نامه: {html.escape(sc_args(m.group(1)).get("term_id", ""))})</em>', t)

    def feature(m):
        a = sc_args(m.group(1))
        st = a.get("state", "")
        ver = a.get("for_k8s_version", "")
        if "{{" in ver:
            ver = VERSION
        return (f'\n\n<div class="feature-state">وضعیت ویژگی: <span class="ltr" dir="ltr">Kubernetes {html.escape(ver)} '
                f'[{html.escape(st)}]</span> ({STATE.get(st, st)})</div>\n\n')
    t = re.sub(r"\{\{<\s*feature-state\s+([^>]*?)>\}\}", feature, t)

    # admonitions
    for kind, label in CALLOUT.items():
        t = re.sub(r"\{\{[<%]\s*" + kind + r"\s*[>%]\}\}", f'\n\n<div class="callout {kind}"><div class="callout-title">{label}</div>\n\n', t)
        t = re.sub(r"\{\{[<%]\s*/" + kind + r"\s*[>%]\}\}", "\n\n</div>\n\n", t)
    t = re.sub(r"\{\{[<%]\s*alert\s*([^>%]*)[>%]\}\}", lambda m: f'\n\n<div class="callout note"><div class="callout-title">{html.escape(sc_args(m.group(1)).get("title", ""))}</div>\n\n', t)
    t = re.sub(r"\{\{[<%]\s*/alert\s*[>%]\}\}", "\n\n</div>\n\n", t)

    # tabs
    t = re.sub(r"\{\{[<%]\s*tabs\b[^>%]*[>%]\}\}", '\n\n<div class="tabs">\n\n', t)
    t = re.sub(r"\{\{[<%]\s*/tabs\s*[>%]\}\}", "\n\n</div>\n\n", t)

    def tab(m):
        a = sc_args(m.group(1))
        name = html.escape(a.get("name", ""))
        if a.get("codelang") or a.get("include"):
            return f'\n\n<div class="tab"><div class="tab-name">{name}</div>\n\n'
        return f'\n\n<div class="tab"><div class="tab-name">{name}</div>\n\n'
    t = re.sub(r"\{\{[<%]\s*tab\s+([^>%]*?)\s*/?[>%]\}\}", tab, t)
    t = re.sub(r"\{\{[<%]\s*/tab\s*[>%]\}\}", "\n\n</div>\n\n", t)

    # mermaid / highlight / table / example wrappers
    t = re.sub(r"\{\{<\s*mermaid\s*>\}\}(.*?)\{\{<\s*/mermaid\s*>\}\}", lambda m: f"\n\n```mermaid\n{m.group(1).strip()}\n```\n\n", t, flags=re.S)
    t = re.sub(r"\{\{<\s*highlight\s+(\w+)[^>]*>\}\}(.*?)\{\{<\s*/highlight\s*>\}\}", lambda m: f"\n\n```{m.group(1)}\n{m.group(2).strip()}\n```\n\n", t, flags=re.S)
    t = re.sub(r"\{\{[<%]\s*/?(table|example|thirdparty-content|release-branch|legacy-repos-deprecation)[^>%]*[>%]\}\}", "", t)

    def figure(m):
        a = sc_args(m.group(1))
        src = a.get("src", "")
        cap = a.get("caption", "") or a.get("alt", "")
        return f'\n\n<figure><img src="https://kubernetes.io{html.escape(src)}" alt="{html.escape(a.get("alt", ""))}"><figcaption>{html.escape(cap)}</figcaption></figure>\n\n'
    t = re.sub(r"\{\{<\s*figure\s+([^>]*?)>\}\}", figure, t)

    # ref / relref -> link targets
    def ref(m):
        target = m.group(1)
        if target.startswith("#"):
            return target
        return target
    t = re.sub(r'\{\{<\s*(?:ref|relref)\s+"([^"]+)"\s*>\}\}', ref, t)

    # anything left: drop the shortcode delimiters, keep nothing
    t = re.sub(r"\{\{[<%].*?[>%]\}\}", "", t, flags=re.S)
    return t


# ---------------------------------------------------------------- links & direction

def fix_links(doc, page_rel: str, url_map: dict[str, str]) -> None:
    here = Path(url_for(page_rel)).parent
    for a in doc.iter("a"):
        href = a.get("href") or ""
        if href.startswith("/docs/") or href.startswith("https://kubernetes.io/docs/"):
            path, _, frag = href.replace("https://kubernetes.io", "").partition("#")
            key = path[len("/docs/"):].strip("/")
            target = url_map.get(key)
            if target:
                rel = os.path.relpath(target, here) if str(here) != "." else target
                a.set("href", rel + (("#" + frag) if frag else ""))
            else:
                a.set("href", "https://kubernetes.io" + href.replace("https://kubernetes.io", ""))
                a.set("target", "_blank")
        elif re.match(r"^\.\.?/", href) and not href.endswith(".html"):
            path, _, frag = href.partition("#")
            base_dir = Path(page_rel).parent
            if page_rel.endswith(".md") and not page_rel.endswith("_index.md"):
                base_dir = Path(page_rel[:-3])  # Hugo resolves relative links from the page URL
            key = os.path.normpath(base_dir / path).strip("/")
            target = url_map.get(key)
            if target:
                a.set("href", os.path.relpath(target, here) + (("#" + frag) if frag else ""))
        elif href.startswith("http"):
            a.set("target", "_blank")
            a.set("rel", "noopener")


BLOCKS = ("p", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "dt", "dd", "blockquote", "figcaption", "summary")


def set_direction(doc) -> None:
    for el in doc.iter(*BLOCKS):
        txt = el.text_content()
        if FA.search(txt):
            el.set("dir", "rtl")
        elif LATIN.search(txt):
            el.set("dir", "ltr")
            el.set("class", (el.get("class", "") + " ltr").strip())
    for el in doc.iter("pre", "code", "kbd", "samp"):
        el.set("dir", "ltr")
    for tbl in doc.iter("table"):
        cells = [c.text_content() for c in tbl.iter("td", "th")]
        if cells and not any(FA.search(c) for c in cells):
            tbl.set("dir", "ltr")


# ---------------------------------------------------------------- page template

CSS = """
:root{--bg:#fff;--fg:#1f2328;--muted:#59636e;--border:#d1d9e0;--code-bg:#f6f8fa;--accent:#326ce5;--note:#e7f0ff;--caution:#fff4e5;--warning:#fdecec;--side:#f7f9fc}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--border:#30363d;--code-bg:#161b22;--accent:#6ea8fe;--note:#0f2547;--caution:#3a2a10;--warning:#3d1517;--side:#11161d}}
:root[data-theme=dark]{--bg:#0d1117;--fg:#e6edf3;--muted:#9198a1;--border:#30363d;--code-bg:#161b22;--accent:#6ea8fe;--note:#0f2547;--caution:#3a2a10;--warning:#3d1517;--side:#11161d}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:Vazirmatn,Tahoma,"Segoe UI",sans-serif;line-height:1.95;font-size:16px}
header.top{position:sticky;top:0;z-index:5;display:flex;gap:12px;align-items:center;padding:10px 16px;border-bottom:1px solid var(--border);background:var(--bg)}
header.top a{color:var(--accent);text-decoration:none;font-weight:600}
header.top .crumbs{color:var(--muted);font-size:13px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.layout{display:flex;max-width:1280px;margin:0 auto}
nav.toc{width:260px;flex-shrink:0;padding:16px;border-inline-start:1px solid var(--border);position:sticky;top:52px;align-self:flex-start;max-height:calc(100vh - 52px);overflow:auto;font-size:13.5px;background:var(--side)}
nav.toc a{display:block;color:var(--muted);text-decoration:none;padding:2px 0}
nav.toc a.l3{padding-inline-start:12px}
nav.toc a:hover{color:var(--accent)}
main{flex:1;min-width:0;padding:20px 32px 60px;text-align:right}
main h1{font-size:30px;line-height:1.5;margin:8px 0 16px}
main h2{font-size:23px;border-bottom:1px solid var(--border);padding-bottom:6px;margin-top:36px}
main h3{font-size:19px;margin-top:28px}
a{color:var(--accent)}
[dir=ltr],.ltr{text-align:left;direction:ltr}
pre{direction:ltr;text-align:left;background:var(--code-bg);border:1px solid var(--border);border-radius:8px;padding:12px 14px;overflow:auto;line-height:1.55;font-size:13.5px;unicode-bidi:isolate}
code,kbd,samp{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;direction:ltr;unicode-bidi:isolate;font-size:.9em}
:not(pre)>code{background:var(--code-bg);border:1px solid var(--border);border-radius:5px;padding:1px 5px}
.code-file{font-family:ui-monospace,monospace;font-size:12.5px;color:var(--muted);margin-bottom:-10px}
table{border-collapse:collapse;display:block;overflow:auto;max-width:100%;margin:14px 0}
th,td{border:1px solid var(--border);padding:6px 10px;vertical-align:top}
th{background:var(--code-bg)}
.callout{border-inline-start:4px solid var(--accent);background:var(--note);padding:10px 16px;border-radius:6px;margin:16px 0}
.callout.caution{border-color:#d4880f;background:var(--caution)}
.callout.warning{border-color:#cf222e;background:var(--warning)}
.callout-title{font-weight:700;margin-bottom:4px}
.feature-state{display:inline-block;background:var(--code-bg);border:1px solid var(--border);border-radius:6px;padding:4px 10px;font-size:13.5px;margin:6px 0}
.tabs{border:1px solid var(--border);border-radius:8px;padding:8px 14px;margin:16px 0}
.tab-name{font-weight:700;color:var(--accent);margin-top:10px;border-bottom:1px dashed var(--border)}
.term{border-bottom:1px dotted var(--muted)}
img{max-width:100%}
figure{margin:16px 0;text-align:center}
.page-meta{color:var(--muted);font-size:13px;margin-bottom:6px}
.index-tree ul{list-style:none;padding-inline-start:18px;border-inline-start:1px dashed var(--border)}
.index-tree>ul{border:0;padding:0}
.index-tree li{margin:2px 0}
.index-tree .sec{font-weight:700}
.missing{color:var(--muted)}
#upd[hidden]{display:none}
#upd{margin-inline-start:auto;display:flex;gap:8px;align-items:center;font-size:.85em}
#upd:not([hidden])+#theme{margin-inline-start:8px}
#upd button{background:var(--accent,#326ce5);color:#fff;border:0;border-radius:6px;padding:3px 12px;cursor:pointer;font:inherit}
#upd .upd-info{color:var(--muted)}
#theme{margin-inline-start:auto;background:none;border:1px solid var(--border);color:var(--fg);border-radius:6px;padding:2px 10px;cursor:pointer;font:inherit}
@media (max-width:900px){nav.toc{display:none}main{padding:16px}}
"""
THEME_JS = """<script>
(function(){var k='k8s-fa-theme';try{var t=localStorage.getItem(k);if(t)document.documentElement.dataset.theme=t;}catch(e){}
document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('theme');if(!b)return;b.onclick=function(){var d=document.documentElement;var dark=d.dataset.theme?d.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;d.dataset.theme=dark?'light':'dark';try{localStorage.setItem(k,d.dataset.theme)}catch(e){}};});})();
</script>"""


# Update button: only appears when the page is served by service.py (/api/status answers).
UPDATE_JS = """<script>
(function(){var box,busy=false;
function fmt(s){if(!s.running)return s.translated+' از '+s.total+' صفحه';
var t=s.phase==='translate'?('ترجمه '+s.done+' از '+s.todo):s.phase;
if(s.paused_until)t+=' — انتظار برای ریست سهمیه تا '+new Date(s.paused_until*1000).toLocaleTimeString('fa-IR');return t;}
function draw(s){box.hidden=false;box.innerHTML='';var b=document.createElement('button');b.type='button';
b.textContent=s.running?'توقف':'به‌روزرسانی';b.onclick=function(){if(busy)return;busy=true;
fetch(s.running?'/api/stop':'/api/update',{method:'POST'}).then(poll).finally(function(){busy=false});};
var i=document.createElement('span');i.className='upd-info';i.textContent=fmt(s);box.append(b,i);}
function poll(){return fetch('/api/status').then(function(r){if(!r.ok)throw 0;return r.json()}).then(draw).catch(function(){});}
document.addEventListener('DOMContentLoaded',function(){box=document.getElementById('upd');if(!box||location.protocol==='file:')return;poll();setInterval(poll,5000);});})();
</script>"""


def page_html(title: str, body: str, toc: str, crumbs: str, depth: int) -> str:
    up = "../" * depth
    return f"""<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | مستندات کوبرنتیز</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
{THEME_JS}
{UPDATE_JS}
</head>
<body>
<header class="top"><a href="{up}index.html">مستندات کوبرنتیز (فارسی)</a><span class="crumbs">{crumbs}</span><span id="upd" hidden></span><button id="theme" type="button">روشن / تاریک</button></header>
<div class="layout">
<main>{body}</main>
<nav class="toc" aria-label="فهرست این صفحه">{toc}</nav>
</div>
</body>
</html>
"""


def build() -> None:
    pages = load_pages()
    if INCLUDES_FA.exists():
        pass
    url_map: dict[str, str] = {}
    titles: dict[str, str] = {}
    for rel in pages:
        key = rel[:-3]
        if key.endswith("/_index") or key == "_index":
            key = key[: -len("_index")].rstrip("/")
        url_map[key] = url_for(rel)
    built = 0
    for rel, text in sorted(pages.items()):
        fm, body_md = split_front_matter(text)
        title = str(fm.get("title") or Path(rel).stem)
        titles[rel] = title
        body_md = render_shortcodes(body_md, url_for(rel), url_map)
        body_html = md.render(body_md)
        desc = fm.get("description")
        head = f"<h1>{html.escape(title)}</h1>"
        if desc and isinstance(desc, str):
            head += f'<p class="page-meta">{html.escape(desc)}</p>'
        doc = lh.fragment_fromstring(head + body_html, create_parent="div")
        fix_links(doc, rel, url_map)
        set_direction(doc)
        toc = []
        for h in doc.iter("h2", "h3"):
            if h.get("id"):
                toc.append(f'<a class="l{h.tag[1]}" href="#{h.get("id")}">{html.escape(h.text_content())}</a>')
        out_rel = url_for(rel)
        depth = out_rel.count("/")
        crumbs = " / ".join(html.escape(p) for p in Path(rel).parent.parts) or "docs"
        inner = lh.tostring(doc, encoding="unicode")[len("<div>"):-len("</div>")]
        out = OUT / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_html(title, inner, "<strong>در این صفحه</strong>" + "".join(toc), crumbs, depth), encoding="utf-8")
        built += 1
    write_index(pages, titles)
    print(f"built {built} pages -> {OUT}")


def write_index(pages: dict[str, str], titles: dict[str, str]) -> None:
    all_en = sorted(str(p.relative_to(EN_DOCS)) for p in EN_DOCS.rglob("*.md"))
    tree: dict = {}
    for rel in all_en:
        node = tree
        parts = rel.split("/")
        for d in parts[:-1]:
            node = node.setdefault(d, {})
        node.setdefault("__files__", []).append(rel)

    def render(node: dict, path: str) -> str:
        items = []
        idx = f"{path}/_index.md" if path else "_index.md"
        for f in sorted(node.get("__files__", [])):
            if f == idx:
                continue
            if f in pages:
                items.append(f'<li><a href="{url_for(f)}">{html.escape(titles.get(f, f))}</a></li>')
            else:
                items.append(f'<li class="missing">{html.escape(f)} (هنوز ترجمه نشده)</li>')
        for d in sorted(k for k in node if k != "__files__"):
            sub = f"{path}/{d}" if path else d
            sidx = f"{sub}/_index.md"
            label = html.escape(titles.get(sidx, d))
            link = f'<a href="{url_for(sidx)}">{label}</a>' if sidx in pages else label
            items.append(f'<li><span class="sec">{link}</span>{render(node[d], sub)}</li>')
        return "<ul>" + "".join(items) + "</ul>"

    done = sum(1 for f in all_en if f in pages)
    body = (f"<h1>مستندات کوبرنتیز به زبان فارسی</h1>"
            f'<p class="page-meta">ترجمه کامل مستندات رسمی کوبرنتیز ({VERSION}) — {done} از {len(all_en)} صفحه</p>'
            f'<div class="index-tree">{render(tree, "")}</div>')
    (OUT / "index.html").write_text(page_html("فهرست", body, "", "docs", 0), encoding="utf-8")


if __name__ == "__main__":
    build()
    sys.exit(0)

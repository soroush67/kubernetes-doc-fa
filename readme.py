"""Generate README.md (status, how to run / continue elsewhere) and INDEX.md (every page)."""
from collections import defaultdict

from common import ROOT, sources, words

ICON = {"ok": "✅", "issues": "⚠️", None: "⏳"}


def rtl(md: str) -> str:
    return f'<div dir="rtl">\n\n{md.strip()}\n\n</div>\n'


def ltr(code: str) -> str:
    return f'<div dir="ltr">\n\n```bash\n{code.strip()}\n```\n\n</div>\n'


def write(m: dict) -> None:
    src = sources()
    files = m["files"]
    wc = {r: words(p.read_text(encoding="utf-8")) for r, p in src.items()}
    done = [r for r in src if r in files]
    pct = 100 * sum(wc[r] for r in done) / max(1, sum(wc.values()))
    issues = [r for r in done if files[r]["status"] == "issues"]
    sections = defaultdict(lambda: [0, 0])
    for r in src:
        s = r.split("/")[0] if "/" in r else "(root)"
        sections[s][1] += 1
        sections[s][0] += r in files
    recent = sorted(done, key=lambda r: files[r]["at"], reverse=True)[:20]
    runs = m.get("runs", [])[-10:][::-1]
    commit = m.get("source_commit") or "?"

    parts = [rtl(f"""
# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **{pct:.1f}٪** |
| صفحات ترجمه‌شده | {len(done)} از {len(src)} |
| صفحات دارای ایراد ساختاری | {len(issues)} |
| نسخه‌ی منبع انگلیسی | `{commit[:12]}` |

## مشاهده

بعد از `git clone`، فایل `html/index.html` را مستقیم در مرورگر باز کنید؛ همه‌ی لینک‌ها نسبی هستند و به سرور نیاز ندارند. دکمه‌ی «به‌روزرسانی» فقط وقتی سرویس در حال اجراست نمایش داده می‌شود.

## سرویس به‌روزرسانی

سرویس، صفحات HTML را روی `http://127.0.0.1:8460` نمایش می‌دهد و بالای هر صفحه دکمه‌ی **به‌روزرسانی** دارد. با زدن آن:

1. منبع انگلیسی از `kubernetes/website` به‌روز می‌شود (فقط `content/en`).
2. برای هر صفحه، hash منبع با `manifest.json` مقایسه می‌شود؛ فقط صفحات **جدید، تغییرکرده یا ترجمه‌نشده** ترجمه می‌شوند و کار هیچ‌وقت از اول شروع نمی‌شود. صفحاتی که از منبع حذف شده‌اند حذف می‌شوند.
3. ترجمه با `claude -p` (Claude Code، مدل Opus، روی اشتراک خودتان، بدون ابزار و با system prompt کوتاه) و در تکه‌های حدود ۲۵۰۰ کلمه انجام می‌شود. هر تکه با `check.py` بررسی و در صورت ایراد دوباره ترجمه می‌شود.
4. اگر سقف مصرف اشتراک پر شود، سرویس تا زمان ریست صبر می‌کند و خودش ادامه می‌دهد.
5. هر ۱۵ صفحه و در پایان کار: `html/`، `README.md` و `INDEX.md` دوباره ساخته می‌شوند و commit و push انجام می‌شود. تاریخچه‌ی کامل در `git log` است.

## ادامه‌ی کار روی سیستم دیگر

پیش‌نیازها: `git`، `python3` (۳.۱۰ به بالا)، و Claude Code CLI که با `claude login` وارد اشتراک شده باشد. همه‌ی وضعیت کار در خود مخزن است (`manifest.json` + `md/`)، پس سرویس از همان‌جایی که مانده ادامه می‌دهد.
""")]
    parts.append(ltr("""
git clone https://github.com/soroush67/kubernetes-doc-fa.git
cd kubernetes-doc-fa
./start.sh          # venv + clones kubernetes/website (content/en) + starts the service on :8460
./stop.sh           # stop the service (a running update is asked to stop first)
# headless, without the web page (e.g. from cron):
.venv/bin/python service.py update
"""))
    parts.append(rtl("""
متغیرهای اختیاری: `WORKERS` (پیش‌فرض ۲ ترجمه‌ی هم‌زمان؛ کمتر = مصرف آرام‌تر)، `TRANSLATE_MODEL` (پیش‌فرض `opus`؛ صفحاتی که با مدل‌های `REDO_MODELS` ترجمه شده‌اند دوباره ترجمه می‌شوند)، `PORT`، `HOST`، `CLAUDE_BIN`، `K8S_WEBSITE` (مسیر منبع انگلیسی؛ پیش‌فرض `./website`).

با `POST /api/update?retry_issues=1` (یا `service.py update --retry-issues`) صفحاتی که با ایراد ساختاری ثبت شده‌اند هم دوباره ترجمه می‌شوند.

## ساختار مخزن

| مسیر | محتوا |
|---|---|
| `md/` | ترجمه‌ی فارسی Markdown، با همان مسیرهای `content/en/docs` |
| `html/` | خروجی HTML (راست‌چین برای فارسی، چپ‌چین برای کد و انگلیسی) |
| `includes/` | ترجمه‌ی snippetهای `content/en/includes` |
| `manifest.json` | برای هر صفحه: hash منبع، وضعیت، مدل، زمان ترجمه؛ و تاریخچه‌ی اجراها |
| `INDEX.md` | فهرست همه‌ی صفحات با وضعیت |
| `service.py`، `translate.py`، `check.py`، `build_html.py`، `prompt.md` | سرویس، ترجمه، بررسی ساختاری، ساخت HTML، قواعد ترجمه |

## پیشرفت هر بخش

| بخش | ترجمه‌شده | کل |
|---|---|---|
""" + "\n".join(f"| `{s}` | {d} | {t} |" for s, (d, t) in sorted(sections.items()))))

    parts.append(rtl("## آخرین اجراها\n\n| شروع | پایان | ترجمه‌شده | با ایراد | نتیجه |\n|---|---|---|---|---|\n" + "\n".join(
        f"| {r.get('started', '')} | {r.get('finished', '')} | {r.get('translated', 0)} | {r.get('issues', 0)} | {r.get('result', '')} |"
        for r in runs) if runs else "## آخرین اجراها\n\nهنوز اجرایی ثبت نشده است."))
    parts.append(rtl("## آخرین صفحات ترجمه‌شده\n\n" + "\n".join(
        f"- [{r}](md/{r}) — {files[r]['at']}" for r in recent)))
    if issues:
        parts.append(rtl("## صفحات دارای ایراد ساختاری\n\n" + "\n".join(
            f"- [{r}](md/{r}): {'; '.join(files[r]['issues'][:2])}" for r in issues)))
    parts.append(rtl("فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)"))
    (ROOT / "README.md").write_text("\n".join(parts), encoding="utf-8")

    by_dir = defaultdict(list)
    for r in src:
        by_dir[r.rsplit("/", 1)[0] if "/" in r else "."].append(r)
    lines = [f"# فهرست صفحات\n\n✅ ترجمه‌شده · ⚠️ ترجمه‌شده با ایراد ساختاری · ⏳ هنوز ترجمه نشده\n\n{len(done)} از {len(src)} صفحه\n"]
    for d in sorted(by_dir):
        lines.append(f"\n## `{d}`\n")
        for r in by_dir[d]:
            st = files.get(r, {}).get("status")
            name = r.rsplit("/", 1)[-1]
            lines.append(f"- {ICON[st]} " + (f"[{name}](md/{r})" if st else f"`{name}`"))
    (ROOT / "INDEX.md").write_text(rtl("\n".join(lines)), encoding="utf-8")

<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **15.6٪** |
| صفحات ترجمه‌شده | 223 از 1722 |
| صفحات دارای ایراد ساختاری | 4 |
| نسخه‌ی منبع انگلیسی | `ed70e311737a` |

## مشاهده

بعد از `git clone`، فایل `html/index.html` را مستقیم در مرورگر باز کنید؛ همه‌ی لینک‌ها نسبی هستند و به سرور نیاز ندارند. دکمه‌ی «به‌روزرسانی» فقط وقتی سرویس در حال اجراست نمایش داده می‌شود.

## سرویس به‌روزرسانی

سرویس، صفحات HTML را روی `http://127.0.0.1:8460` نمایش می‌دهد و بالای هر صفحه دکمه‌ی **به‌روزرسانی** دارد. با زدن آن:

1. منبع انگلیسی از `kubernetes/website` به‌روز می‌شود (فقط `content/en`).
2. برای هر صفحه، hash منبع با `manifest.json` مقایسه می‌شود؛ فقط صفحات **جدید، تغییرکرده یا ترجمه‌نشده** ترجمه می‌شوند و کار هیچ‌وقت از اول شروع نمی‌شود. صفحاتی که از منبع حذف شده‌اند حذف می‌شوند.
3. ترجمه با `claude -p` (Claude Code، مدل Sonnet، روی اشتراک خودتان، بدون ابزار و با system prompt کوتاه) و در تکه‌های حدود ۲۵۰۰ کلمه انجام می‌شود. هر تکه با `check.py` بررسی و در صورت ایراد دوباره ترجمه می‌شود.
4. اگر سقف مصرف اشتراک پر شود، سرویس تا زمان ریست صبر می‌کند و خودش ادامه می‌دهد.
5. هر ۱۵ صفحه و در پایان کار: `html/`، `README.md` و `INDEX.md` دوباره ساخته می‌شوند و commit و push انجام می‌شود. تاریخچه‌ی کامل در `git log` است.

## ادامه‌ی کار روی سیستم دیگر

پیش‌نیازها: `git`، `python3` (۳.۱۰ به بالا)، و Claude Code CLI که با `claude login` وارد اشتراک شده باشد. همه‌ی وضعیت کار در خود مخزن است (`manifest.json` + `md/`)، پس سرویس از همان‌جایی که مانده ادامه می‌دهد.

</div>

<div dir="ltr">

```bash
git clone https://github.com/soroush67/kubernetes-doc-fa.git
cd kubernetes-doc-fa
./start.sh          # venv + clones kubernetes/website (content/en) + starts the service on :8460
./stop.sh           # stop the service (a running update is asked to stop first)
# headless, without the web page (e.g. from cron):
.venv/bin/python service.py update
```

</div>

<div dir="rtl">

متغیرهای اختیاری: `WORKERS` (پیش‌فرض ۲ ترجمه‌ی هم‌زمان؛ کمتر = مصرف آرام‌تر)، `TRANSLATE_MODEL` (پیش‌فرض `sonnet`)، `PORT`، `HOST`، `CLAUDE_BIN`، `K8S_WEBSITE` (مسیر منبع انگلیسی؛ پیش‌فرض `./website`).

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
| `(root)` | 1 | 2 |
| `concepts` | 187 | 187 |
| `contribute` | 35 | 44 |
| `doc-contributor-tools` | 0 | 1 |
| `home` | 0 | 2 |
| `reference` | 0 | 1198 |
| `setup` | 0 | 22 |
| `tasks` | 0 | 221 |
| `tutorials` | 0 | 45 |

</div>

<div dir="rtl">

## آخرین اجراها

هنوز اجرایی ثبت نشده است.

</div>

<div dir="rtl">

## آخرین صفحات ترجمه‌شده

- [contribute/style/content-organization.md](md/contribute/style/content-organization.md) — 2026-10-27T16:15:18+03:30
- [contribute/style/content-guide.md](md/contribute/style/content-guide.md) — 2026-10-27T16:14:55+03:30
- [contribute/style/_index.md](md/contribute/style/_index.md) — 2026-10-27T16:14:44+03:30
- [contribute/review/for-approvers.md](md/contribute/review/for-approvers.md) — 2026-10-27T16:14:36+03:30
- [contribute/new-content/open-a-pr.md](md/contribute/new-content/open-a-pr.md) — 2026-10-27T16:14:16+03:30
- [contribute/review/_index.md](md/contribute/review/_index.md) — 2026-10-27T16:13:49+03:30
- [contribute/participate/roles-and-responsibilities.md](md/contribute/participate/roles-and-responsibilities.md) — 2026-10-27T16:13:44+03:30
- [contribute/participate/pr-wranglers.md](md/contribute/participate/pr-wranglers.md) — 2026-10-27T16:13:08+03:30
- [contribute/participate/issue-wrangler.md](md/contribute/participate/issue-wrangler.md) — 2026-10-27T16:12:35+03:30
- [contribute/participate/_index.md](md/contribute/participate/_index.md) — 2026-10-27T16:12:21+03:30
- [contribute/new-content/preview-locally.md](md/contribute/new-content/preview-locally.md) — 2026-10-27T16:11:55+03:30
- [contribute/new-content/new-features.md](md/contribute/new-content/new-features.md) — 2026-10-27T16:11:33+03:30
- [contribute/new-content/_index.md](md/contribute/new-content/_index.md) — 2026-10-27T16:11:28+03:30
- [contribute/new-content/case-studies.md](md/contribute/new-content/case-studies.md) — 2026-10-27T16:10:58+03:30
- [contribute/localization.md](md/contribute/localization.md) — 2026-10-27T16:10:51+03:30
- [contribute/generate-ref-docs/release-generation.md](md/contribute/generate-ref-docs/release-generation.md) — 2026-10-27T16:10:21+03:30
- [contribute/generate-ref-docs/quickstart.md](md/contribute/generate-ref-docs/quickstart.md) — 2026-10-27T16:09:27+03:30
- [contribute/generate-ref-docs/metrics-reference.md](md/contribute/generate-ref-docs/metrics-reference.md) — 2026-10-27T16:08:54+03:30
- [contribute/generate-ref-docs/prerequisites-ref-docs.md](md/contribute/generate-ref-docs/prerequisites-ref-docs.md) — 2026-10-27T16:08:54+03:30
- [contribute/generate-ref-docs/kubernetes-api.md](md/contribute/generate-ref-docs/kubernetes-api.md) — 2026-10-27T16:08:47+03:30

</div>

<div dir="rtl">

## صفحات دارای ایراد ساختاری

- [concepts/security/pod-security-standards.md](md/concepts/security/pod-security-standards.md): chunk 1: short: 909 words vs 1711 source words
- [contribute/docs.md](md/contribute/docs.md): chunk 1: 10 untranslated English lines, e.g. 'D[Look over the<br>kubernetes/website<br>repository] --- E[Check out the<br>Hugo static site<br>generator]'
- [contribute/new-content/_index.md](md/contribute/new-content/_index.md): chunk 1: 6 untranslated English lines, e.g. 'A[Sign the CNCF CLA] --> B[Choose Git branch]'
- [contribute/new-content/open-a-pr.md](md/contribute/new-content/open-a-pr.md): chunk 1: 18 untranslated English lines, e.g. '1[1. Edit this page] --> 2[2. Use GitHub markdown<br>editor to make changes]'

</div>

<div dir="rtl">

فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)

</div>

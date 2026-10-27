<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **11.2٪** |
| صفحات ترجمه‌شده | 163 از 1722 |
| صفحات دارای ایراد ساختاری | 0 |
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
| `concepts` | 153 | 187 |
| `contribute` | 9 | 44 |
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

- [concepts/resource-management/dynamic-resource-allocation/dra-features.md](md/concepts/resource-management/dynamic-resource-allocation/dra-features.md) — 2026-10-27T15:48:12+03:30
- [concepts/extend-kubernetes/_index.md](md/concepts/extend-kubernetes/_index.md) — 2026-10-27T15:47:06+03:30
- [concepts/extend-kubernetes/api-extension/apiserver-aggregation.md](md/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md) — 2026-10-27T15:47:04+03:30
- [concepts/extend-kubernetes/api-extension/_index.md](md/concepts/extend-kubernetes/api-extension/_index.md) — 2026-10-27T15:46:50+03:30
- [concepts/containers/images.md](md/concepts/containers/images.md) — 2026-10-27T15:46:41+03:30
- [concepts/containers/runtime-class.md](md/concepts/containers/runtime-class.md) — 2026-10-27T15:46:01+03:30
- [concepts/containers/container-lifecycle-hooks.md](md/concepts/containers/container-lifecycle-hooks.md) — 2026-10-27T15:45:08+03:30
- [concepts/containers/cri.md](md/concepts/containers/cri.md) — 2026-10-27T15:44:52+03:30
- [concepts/cluster-administration/observability.md](md/concepts/cluster-administration/observability.md) — 2026-10-27T15:44:33+03:30
- [concepts/cluster-administration/proxies.md](md/concepts/cluster-administration/proxies.md) — 2026-10-27T15:44:33+03:30
- [concepts/cluster-administration/node-shutdown.md](md/concepts/cluster-administration/node-shutdown.md) — 2026-10-27T15:44:17+03:30
- [concepts/cluster-administration/flow-control.md](md/concepts/cluster-administration/flow-control.md) — 2026-10-27T15:43:50+03:30
- [concepts/cluster-administration/node-autoscaling.md](md/concepts/cluster-administration/node-autoscaling.md) — 2026-10-27T15:43:25+03:30
- [concepts/cluster-administration/networking.md](md/concepts/cluster-administration/networking.md) — 2026-10-27T15:42:26+03:30
- [concepts/cluster-administration/logging.md](md/concepts/cluster-administration/logging.md) — 2026-10-27T15:42:06+03:30
- [_index.md](md/_index.md) — 2026-10-27T15:38:01+03:30
- [concepts/_index.md](md/concepts/_index.md) — 2026-10-27T15:38:01+03:30
- [concepts/architecture/_index.md](md/concepts/architecture/_index.md) — 2026-10-27T15:38:01+03:30
- [concepts/architecture/cgroups.md](md/concepts/architecture/cgroups.md) — 2026-10-27T15:38:01+03:30
- [concepts/architecture/cloud-controller.md](md/concepts/architecture/cloud-controller.md) — 2026-10-27T15:38:01+03:30

</div>

<div dir="rtl">

فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)

</div>

<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **20.4٪** |
| صفحات ترجمه‌شده | 688 از 1722 |
| صفحات دارای ایراد ساختاری | 9 |
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
| `contribute` | 44 | 44 |
| `doc-contributor-tools` | 1 | 1 |
| `home` | 2 | 2 |
| `reference` | 453 | 1198 |
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

- [reference/command-line-tools-reference/feature-gates/SupportIPVSProxyMode.md](md/reference/command-line-tools-reference/feature-gates/SupportIPVSProxyMode.md) — 2026-10-27T17:07:54+03:30
- [reference/command-line-tools-reference/feature-gates/SupplementalGroupsPolicy.md](md/reference/command-line-tools-reference/feature-gates/SupplementalGroupsPolicy.md) — 2026-10-27T17:07:50+03:30
- [reference/command-line-tools-reference/feature-gates/StructuredAuthorizationConfiguration.md](md/reference/command-line-tools-reference/feature-gates/StructuredAuthorizationConfiguration.md) — 2026-10-27T17:07:46+03:30
- [reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfigurationJWKSMetrics.md](md/reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfigurationJWKSMetrics.md) — 2026-10-27T17:07:43+03:30
- [reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfigurationEgressSelector.md](md/reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfigurationEgressSelector.md) — 2026-10-27T17:07:39+03:30
- [reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfiguration.md](md/reference/command-line-tools-reference/feature-gates/StructuredAuthenticationConfiguration.md) — 2026-10-27T17:07:38+03:30
- [reference/command-line-tools-reference/feature-gates/StrictIPCIDRValidation.md](md/reference/command-line-tools-reference/feature-gates/StrictIPCIDRValidation.md) — 2026-10-27T17:07:34+03:30
- [reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForWebhooks.md](md/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForWebhooks.md) — 2026-10-27T17:07:31+03:30
- [reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForVAP.md](md/reference/command-line-tools-reference/feature-gates/StrictCostEnforcementForVAP.md) — 2026-10-27T17:07:27+03:30
- [reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects.md](md/reference/command-line-tools-reference/feature-gates/StreamingProxyRedirects.md) — 2026-10-27T17:07:26+03:30
- [reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToProtobuf.md](md/reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToProtobuf.md) — 2026-10-27T17:07:21+03:30
- [reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToJSON.md](md/reference/command-line-tools-reference/feature-gates/StreamingCollectionEncodingToJSON.md) — 2026-10-27T17:07:14+03:30
- [reference/command-line-tools-reference/feature-gates/StorageVersionMigrator.md](md/reference/command-line-tools-reference/feature-gates/StorageVersionMigrator.md) — 2026-10-27T17:07:09+03:30
- [reference/command-line-tools-reference/feature-gates/StorageVersionHash.md](md/reference/command-line-tools-reference/feature-gates/StorageVersionHash.md) — 2026-10-27T17:07:02+03:30
- [reference/command-line-tools-reference/feature-gates/StorageVersionAPI.md](md/reference/command-line-tools-reference/feature-gates/StorageVersionAPI.md) — 2026-10-27T17:06:54+03:30
- [reference/command-line-tools-reference/feature-gates/StorageObjectInUseProtection.md](md/reference/command-line-tools-reference/feature-gates/StorageObjectInUseProtection.md) — 2026-10-27T17:06:53+03:30
- [reference/command-line-tools-reference/feature-gates/StorageNamespaceIndex.md](md/reference/command-line-tools-reference/feature-gates/StorageNamespaceIndex.md) — 2026-10-27T17:06:49+03:30
- [reference/command-line-tools-reference/feature-gates/StorageCapacityScoring.md](md/reference/command-line-tools-reference/feature-gates/StorageCapacityScoring.md) — 2026-10-27T17:06:47+03:30
- [reference/command-line-tools-reference/feature-gates/StatefulSetRecreateStrategy.md](md/reference/command-line-tools-reference/feature-gates/StatefulSetRecreateStrategy.md) — 2026-10-27T17:06:42+03:30
- [reference/command-line-tools-reference/feature-gates/StatefulSetStartOrdinal.md](md/reference/command-line-tools-reference/feature-gates/StatefulSetStartOrdinal.md) — 2026-10-27T17:06:40+03:30

</div>

<div dir="rtl">

## صفحات دارای ایراد ساختاری

- [concepts/security/pod-security-standards.md](md/concepts/security/pod-security-standards.md): chunk 1: short: 909 words vs 1711 source words
- [contribute/docs.md](md/contribute/docs.md): chunk 1: 10 untranslated English lines, e.g. 'D[Look over the<br>kubernetes/website<br>repository] --- E[Check out the<br>Hugo static site<br>generator]'
- [contribute/new-content/_index.md](md/contribute/new-content/_index.md): chunk 1: 6 untranslated English lines, e.g. 'A[Sign the CNCF CLA] --> B[Choose Git branch]'
- [contribute/new-content/open-a-pr.md](md/contribute/new-content/open-a-pr.md): chunk 1: 18 untranslated English lines, e.g. '1[1. Edit this page] --> 2[2. Use GitHub markdown<br>editor to make changes]'
- [contribute/review/reviewing-prs.md](md/contribute/review/reviewing-prs.md): chunk 1: 5 untranslated English lines, e.g. 'J[read description<br>and comments]--> K[preview changes in<br>Netlify preview build]'
- [contribute/style/hugo-shortcodes/index.md](md/contribute/style/hugo-shortcodes/index.md): chunk 1: 4 untranslated English lines, e.g. "// If you don't set a tab name, the site supplies one."
- [contribute/style/style-guide.md](md/contribute/style/style-guide.md): chunk 1: 37 untranslated English lines, e.g. "{{< comment >}}[If you're localizing this page, you can omit the point about US English.]{{< /comment >}}"
- [reference/access-authn-authz/authentication.md](md/reference/access-authn-authz/authentication.md): chunk 3: 54 untranslated English lines, e.g. '#          Do not use this for your own cluster!'
- [reference/access-authn-authz/psp-to-pod-security-standards.md](md/reference/access-authn-authz/psp-to-pod-security-standards.md): chunk 1: short: 716 words vs 997 source words

</div>

<div dir="rtl">

فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)

</div>

<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **19.7٪** |
| صفحات ترجمه‌شده | 418 از 1722 |
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
| `reference` | 183 | 1198 |
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

- [reference/command-line-tools-reference/feature-gates/EndpointSliceTerminatingCondition.md](md/reference/command-line-tools-reference/feature-gates/EndpointSliceTerminatingCondition.md) — 2026-10-27T16:50:06+03:30
- [reference/command-line-tools-reference/feature-gates/EnvFiles.md](md/reference/command-line-tools-reference/feature-gates/EnvFiles.md) — 2026-10-27T16:50:06+03:30
- [reference/command-line-tools-reference/feature-gates/EndpointSliceProxying.md](md/reference/command-line-tools-reference/feature-gates/EndpointSliceProxying.md) — 2026-10-27T16:50:01+03:30
- [reference/command-line-tools-reference/feature-gates/EndpointSliceNodeName.md](md/reference/command-line-tools-reference/feature-gates/EndpointSliceNodeName.md) — 2026-10-27T16:50:00+03:30
- [reference/command-line-tools-reference/feature-gates/EnableEquivalenceClassCache.md](md/reference/command-line-tools-reference/feature-gates/EnableEquivalenceClassCache.md) — 2026-10-27T16:49:55+03:30
- [reference/command-line-tools-reference/feature-gates/EndpointSlice.md](md/reference/command-line-tools-reference/feature-gates/EndpointSlice.md) — 2026-10-27T16:49:54+03:30
- [reference/command-line-tools-reference/feature-gates/EmptyDirVolumeMode.md](md/reference/command-line-tools-reference/feature-gates/EmptyDirVolumeMode.md) — 2026-10-27T16:49:48+03:30
- [reference/command-line-tools-reference/feature-gates/EnableAggregatedDiscoveryTimeout.md](md/reference/command-line-tools-reference/feature-gates/EnableAggregatedDiscoveryTimeout.md) — 2026-10-27T16:49:48+03:30
- [reference/command-line-tools-reference/feature-gates/ElasticIndexedJob.md](md/reference/command-line-tools-reference/feature-gates/ElasticIndexedJob.md) — 2026-10-27T16:49:43+03:30
- [reference/command-line-tools-reference/feature-gates/EfficientWatchResumption.md](md/reference/command-line-tools-reference/feature-gates/EfficientWatchResumption.md) — 2026-10-27T16:49:39+03:30
- [reference/command-line-tools-reference/feature-gates/DynamicResourceAllocation.md](md/reference/command-line-tools-reference/feature-gates/DynamicResourceAllocation.md) — 2026-10-27T16:49:36+03:30
- [reference/command-line-tools-reference/feature-gates/DynamicVolumeProvisioning.md](md/reference/command-line-tools-reference/feature-gates/DynamicVolumeProvisioning.md) — 2026-10-27T16:49:30+03:30
- [reference/command-line-tools-reference/feature-gates/DynamicKubeletConfig.md](md/reference/command-line-tools-reference/feature-gates/DynamicKubeletConfig.md) — 2026-10-27T16:49:25+03:30
- [reference/command-line-tools-reference/feature-gates/DynamicProvisioningScheduling.md](md/reference/command-line-tools-reference/feature-gates/DynamicProvisioningScheduling.md) — 2026-10-27T16:49:24+03:30
- [reference/command-line-tools-reference/feature-gates/DryRun.md](md/reference/command-line-tools-reference/feature-gates/DryRun.md) — 2026-10-27T16:49:16+03:30
- [reference/command-line-tools-reference/feature-gates/DynamicAuditing.md](md/reference/command-line-tools-reference/feature-gates/DynamicAuditing.md) — 2026-10-27T16:49:11+03:30
- [reference/command-line-tools-reference/feature-gates/DownwardAPIHugePages.md](md/reference/command-line-tools-reference/feature-gates/DownwardAPIHugePages.md) — 2026-10-27T16:49:06+03:30
- [reference/command-line-tools-reference/feature-gates/DisableNodeKubeProxyVersion.md](md/reference/command-line-tools-reference/feature-gates/DisableNodeKubeProxyVersion.md) — 2026-10-27T16:49:03+03:30
- [reference/command-line-tools-reference/feature-gates/DisableCloudProviders.md](md/reference/command-line-tools-reference/feature-gates/DisableCloudProviders.md) — 2026-10-27T16:48:58+03:30
- [reference/command-line-tools-reference/feature-gates/DisableKubeletCloudCredentialProviders.md](md/reference/command-line-tools-reference/feature-gates/DisableKubeletCloudCredentialProviders.md) — 2026-10-27T16:48:57+03:30

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

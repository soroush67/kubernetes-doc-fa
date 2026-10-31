<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **42.3٪** |
| صفحات ترجمه‌شده | 1089 از 1722 |
| صفحات دارای ایراد ساختاری | 33 |
| نسخه‌ی منبع انگلیسی | `ed70e311737a` |

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
| `(root)` | 1 | 2 |
| `concepts` | 187 | 187 |
| `contribute` | 44 | 44 |
| `doc-contributor-tools` | 1 | 1 |
| `home` | 2 | 2 |
| `reference` | 854 | 1198 |
| `setup` | 0 | 22 |
| `tasks` | 0 | 221 |
| `tutorials` | 0 | 45 |

</div>

<div dir="rtl">

## آخرین اجراها

| شروع | پایان | ترجمه‌شده | با ایراد | نتیجه |
|---|---|---|---|---|
| 2026-10-31T09:52:10+03:30 | 2026-10-31T09:55:49+03:30 | 0 | 0 | stopped |
| 2026-10-31T09:49:44+03:30 | 2026-10-31T09:51:55+03:30 | 0 | 0 | stopped |
| 2026-10-31T09:43:22+03:30 | 2026-10-31T09:49:30+03:30 | 0 | 0 | stopped |
| 2026-10-28T11:00:04+03:30 | 2026-10-28T11:56:52+03:30 | 217 | 13 | stopped |

</div>

<div dir="rtl">

## آخرین صفحات ترجمه‌شده

- [reference/kubernetes-api/admissionregistration/validating-webhook-configuration-v1.md](md/reference/kubernetes-api/admissionregistration/validating-webhook-configuration-v1.md) — 2026-10-31T10:19:35+03:30
- [reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1.md](md/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1.md) — 2026-10-31T10:12:06+03:30
- [reference/kubernetes-api/admissionregistration/mutating-webhook-configuration-v1.md](md/reference/kubernetes-api/admissionregistration/mutating-webhook-configuration-v1.md) — 2026-10-31T10:10:50+03:30
- [reference/kubernetes-api/admissionregistration/mutating-admission-policy-v1.md](md/reference/kubernetes-api/admissionregistration/mutating-admission-policy-v1.md) — 2026-10-31T10:04:29+03:30
- [reference/kubernetes-api/admissionregistration/mutating-admission-policy-binding-v1.md](md/reference/kubernetes-api/admissionregistration/mutating-admission-policy-binding-v1.md) — 2026-10-31T10:03:01+03:30
- [reference/kubectl/quick-reference.md](md/reference/kubectl/quick-reference.md) — 2026-10-29T13:56:59+03:30
- [reference/kubernetes-api/admissionregistration/_index.md](md/reference/kubernetes-api/admissionregistration/_index.md) — 2026-10-29T13:56:31+03:30
- [reference/kubernetes-api/_index.md](md/reference/kubernetes-api/_index.md) — 2026-10-29T13:56:26+03:30
- [reference/kubelet-api/stats.v1alpha1.md](md/reference/kubelet-api/stats.v1alpha1.md) — 2026-10-29T13:56:21+03:30
- [reference/kubelet-api/_index.md](md/reference/kubelet-api/_index.md) — 2026-10-29T13:54:00+03:30
- [reference/kubectl/kuberc.md](md/reference/kubectl/kuberc.md) — 2026-10-29T13:53:56+03:30
- [reference/kubectl/kubectl.md](md/reference/kubectl/kubectl.md) — 2026-10-29T13:52:29+03:30
- [reference/kubectl/jsonpath.md](md/reference/kubectl/jsonpath.md) — 2026-10-29T13:50:51+03:30
- [reference/kubectl/kubectl-cmds.md](md/reference/kubectl/kubectl-cmds.md) — 2026-10-29T13:50:43+03:30
- [reference/kubectl/introduction.md](md/reference/kubectl/introduction.md) — 2026-10-29T13:50:40+03:30
- [reference/kubectl/generated/kubectl_wait/_index.md](md/reference/kubectl/generated/kubectl_wait/_index.md) — 2026-10-29T13:50:28+03:30
- [reference/kubectl/generated/kubectl_version/_index.md](md/reference/kubectl/generated/kubectl_version/_index.md) — 2026-10-29T13:50:13+03:30
- [reference/kubectl/generated/kubectl_uncordon/_index.md](md/reference/kubectl/generated/kubectl_uncordon/_index.md) — 2026-10-29T13:49:25+03:30
- [reference/kubectl/generated/kubectl_top/kubectl_top_pod.md](md/reference/kubectl/generated/kubectl_top/kubectl_top_pod.md) — 2026-10-29T13:48:52+03:30
- [reference/kubectl/generated/kubectl_top/kubectl_top_node.md](md/reference/kubectl/generated/kubectl_top/kubectl_top_node.md) — 2026-10-29T13:47:58+03:30

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
- [reference/command-line-tools-reference/kube-apiserver.md](md/reference/command-line-tools-reference/kube-apiserver.md): chunk 2: short: 1797 words vs 2502 source words; chunk 3: short: 2074 words vs 3387 source words
- [reference/command-line-tools-reference/kube-controller-manager.md](md/reference/command-line-tools-reference/kube-controller-manager.md): chunk 2: short: 1856 words vs 2529 source words; chunk 3: short: 1329 words vs 2499 source words
- [reference/command-line-tools-reference/kube-proxy.md](md/reference/command-line-tools-reference/kube-proxy.md): chunk 2: short: 1546 words vs 2509 source words
- [reference/command-line-tools-reference/kube-scheduler.md](md/reference/command-line-tools-reference/kube-scheduler.md): chunk 2: short: 1359 words vs 2533 source words; chunk 3: short: 1553 words vs 2137 source words
- [reference/command-line-tools-reference/kubelet.md](md/reference/command-line-tools-reference/kubelet.md): chunk 3: short: 1550 words vs 2364 source words
- [reference/config-api/apiserver-config.v1.md](md/reference/config-api/apiserver-config.v1.md): chunk 1: 3 untranslated English lines, e.g. '&quot;iss&quot;: &quot;https://issuer.example.com&quot;,'
- [reference/config-api/imagepolicy.v1alpha1.md](md/reference/config-api/imagepolicy.v1alpha1.md): chunk 1: short: 354 words vs 514 source words
- [reference/config-api/kubeadm-config.v1beta3.md](md/reference/config-api/kubeadm-config.v1beta3.md): chunk 1: short: 1881 words vs 4131 source words
- [reference/config-api/kubeadm-config.v1beta4.md](md/reference/config-api/kubeadm-config.v1beta4.md): chunk 1: short: 2508 words vs 5597 source words; chunk 2: short: 1496 words vs 2029 source words
- [reference/config-api/kubelet-config.v1alpha1.md](md/reference/config-api/kubelet-config.v1alpha1.md): chunk 1: short: 1158 words vs 1573 source words
- [reference/external-api/custom-metrics.v1beta2.md](md/reference/external-api/custom-metrics.v1beta2.md): chunk 1: short: 351 words vs 548 source words
- [reference/external-api/external-metrics.v1beta1.md](md/reference/external-api/external-metrics.v1beta1.md): chunk 1: short: 224 words vs 345 source words
- [reference/external-api/metrics.v1.md](md/reference/external-api/metrics.v1.md): chunk 1: short: 374 words vs 606 source words
- [reference/external-api/metrics.v1beta1.md](md/reference/external-api/metrics.v1beta1.md): chunk 1: short: 388 words vs 620 source words
- [reference/instrumentation/metrics.md](md/reference/instrumentation/metrics.md): chunk 2: short: 1603 words vs 4479 source words; chunk 3: short: 2653 words vs 7422 source words
- [reference/kubectl/generated/kubectl_api-resources/_index.md](md/reference/kubectl/generated/kubectl_api-resources/_index.md): chunk 1: short: 1121 words vs 1550 source words
- [reference/kubectl/generated/kubectl_api-versions/_index.md](md/reference/kubectl/generated/kubectl_api-versions/_index.md): chunk 1: short: 903 words vs 1266 source words
- [reference/kubectl/generated/kubectl_apply/_index.md](md/reference/kubectl/generated/kubectl_apply/_index.md): chunk 2: short: 887 words vs 1254 source words
- [reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts.md](md/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts.md): chunk 1: short: 938 words vs 1313 source words
- [reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials.md](md/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials.md): chunk 1: short: 1121 words vs 1593 source words
- [reference/kubectl/generated/kubectl_expose/_index.md](md/reference/kubectl/generated/kubectl_expose/_index.md): chunk 2: short: 849 words vs 1205 source words
- [reference/kubectl/generated/kubectl_get/_index.md](md/reference/kubectl/generated/kubectl_get/_index.md): chunk 2: short: 860 words vs 1205 source words
- [reference/kubectl/generated/kubectl_run/_index.md](md/reference/kubectl/generated/kubectl_run/_index.md): chunk 2: short: 862 words vs 1205 source words
- [reference/kubectl/quick-reference.md](md/reference/kubectl/quick-reference.md): chunk 2: 16 code block(s) changed; chunk 2: 141 untranslated English lines, e.g. 'kubectl config view # Show Merged kubeconfig settings.'

</div>

<div dir="rtl">

فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)

</div>

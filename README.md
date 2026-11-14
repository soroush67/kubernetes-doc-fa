<div dir="rtl">

# مستندات کوبرنتیز به زبان فارسی

ترجمه‌ی کامل و وفادار مستندات رسمی کوبرنتیز (`content/en/docs` از مخزن [kubernetes/website](https://github.com/kubernetes/website)) به فارسی، به‌صورت Markdown و HTML قابل‌نمایش.

## وضعیت

| | |
|---|---|
| پیشرفت (بر اساس کلمات) | **90.6٪** |
| صفحات ترجمه‌شده | 1530 از 1722 |
| صفحات دارای ایراد ساختاری | 73 |
| نسخه‌ی منبع انگلیسی | `f652c6b8a26f` |

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
| `reference` | 1198 | 1198 |
| `setup` | 22 | 22 |
| `tasks` | 75 | 221 |
| `tutorials` | 0 | 45 |

</div>

<div dir="rtl">

## آخرین اجراها

| شروع | پایان | ترجمه‌شده | با ایراد | نتیجه |
|---|---|---|---|---|
| 2026-11-03T07:17:54+03:30 | 2026-11-03T14:39:34+03:30 | 102 | 3 | stopped |
| 2026-11-02T16:41:28+03:30 | 2026-11-02T16:56:09+03:30 | 0 | 0 | stopped |
| 2026-11-02T11:08:58+03:30 | 2026-11-02T16:34:51+03:30 | 24 | 7 | stopped |
| 2026-11-02T10:55:34+03:30 | 2026-11-02T11:08:47+03:30 | 0 | 0 | stopped |
| 2026-11-01T08:11:00+03:30 | 2026-11-01T08:39:46+03:30 | 5 | 0 | stopped |
| 2026-10-31T09:52:10+03:30 | 2026-10-31T09:55:49+03:30 | 0 | 0 | stopped |
| 2026-10-31T09:49:44+03:30 | 2026-10-31T09:51:55+03:30 | 0 | 0 | stopped |
| 2026-10-31T09:43:22+03:30 | 2026-10-31T09:49:30+03:30 | 0 | 0 | stopped |
| 2026-10-28T11:00:04+03:30 | 2026-10-28T11:56:52+03:30 | 217 | 13 | stopped |

</div>

<div dir="rtl">

## آخرین صفحات ترجمه‌شده

- [tasks/administer-cluster/running-cloud-controller.md](md/tasks/administer-cluster/running-cloud-controller.md) — 2026-11-14T10:31:14+03:30
- [tasks/administer-cluster/nodelocaldns.md](md/tasks/administer-cluster/nodelocaldns.md) — 2026-11-14T10:30:40+03:30
- [tasks/administer-cluster/quota-api-object.md](md/tasks/administer-cluster/quota-api-object.md) — 2026-11-14T10:30:39+03:30
- [tasks/administer-cluster/node-overprovisioning.md](md/tasks/administer-cluster/node-overprovisioning.md) — 2026-11-14T10:30:19+03:30
- [tasks/administer-cluster/network-policy-provider/kube-router-network-policy.md](md/tasks/administer-cluster/network-policy-provider/kube-router-network-policy.md) — 2026-11-14T10:29:57+03:30
- [tasks/administer-cluster/namespaces.md](md/tasks/administer-cluster/namespaces.md) — 2026-11-14T10:29:51+03:30
- [tasks/administer-cluster/network-policy-provider/cilium-network-policy.md](md/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md) — 2026-11-14T10:29:50+03:30
- [tasks/administer-cluster/network-policy-provider/calico-network-policy.md](md/tasks/administer-cluster/network-policy-provider/calico-network-policy.md) — 2026-11-14T10:29:32+03:30
- [tasks/administer-cluster/network-policy-provider/antrea-network-policy.md](md/tasks/administer-cluster/network-policy-provider/antrea-network-policy.md) — 2026-11-14T10:29:24+03:30
- [tasks/administer-cluster/network-policy-provider/_index.md](md/tasks/administer-cluster/network-policy-provider/_index.md) — 2026-11-14T10:29:17+03:30
- [tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md](md/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md) — 2026-11-14T10:29:15+03:30
- [tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors.md](md/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors.md) — 2026-11-14T10:28:59+03:30
- [tasks/administer-cluster/memory-manager.md](md/tasks/administer-cluster/memory-manager.md) — 2026-11-14T10:28:31+03:30
- [tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md](md/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md) — 2026-11-14T10:28:04+03:30
- [tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md](md/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md) — 2026-11-14T10:27:44+03:30
- [tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md](md/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md) — 2026-11-14T10:26:57+03:30
- [tasks/administer-cluster/migrating-from-dockershim/_index.md](md/tasks/administer-cluster/migrating-from-dockershim/_index.md) — 2026-11-14T10:26:35+03:30
- [tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md](md/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md) — 2026-11-14T10:26:22+03:30
- [tasks/administer-cluster/manage-resources/quota-pod-namespace.md](md/tasks/administer-cluster/manage-resources/quota-pod-namespace.md) — 2026-11-14T10:26:22+03:30
- [tasks/administer-cluster/manage-resources/memory-default-namespace.md](md/tasks/administer-cluster/manage-resources/memory-default-namespace.md) — 2026-11-14T10:26:04+03:30

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
- [reference/kubernetes-api/apps/replica-set-v1.md](md/reference/kubernetes-api/apps/replica-set-v1.md): chunk 9: 3 untranslated English lines, e.g. 'GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale'
- [reference/kubernetes-api/batch/cron-job-v1.md](md/reference/kubernetes-api/batch/cron-job-v1.md): chunk 2: heading anchors {#...} differ
- [reference/kubernetes-api/certificates/pod-certificate-request-v1.md](md/reference/kubernetes-api/certificates/pod-certificate-request-v1.md): chunk 8: 3 untranslated English lines, e.g. 'PATCH /apis/certificates.k8s.io/v1/namespaces/{namespace}/podcertificaterequests/{name}/status'
- [reference/kubernetes-api/coordination/lease-v1.md](md/reference/kubernetes-api/coordination/lease-v1.md): chunk 4: heading anchors {#...} differ
- [reference/kubernetes-api/core/node-v1.md](md/reference/kubernetes-api/core/node-v1.md): chunk 1: short: 1354 words vs 1864 source words; chunk 8: short: 566 words vs 1225 source words
- [reference/kubernetes-api/core/pod-v1.md](md/reference/kubernetes-api/core/pod-v1.md): chunk 25: short: 941 words vs 1914 source words; chunk 26: short: 1224 words vs 1810 source words
- [reference/kubernetes-api/core/replication-controller-v1.md](md/reference/kubernetes-api/core/replication-controller-v1.md): chunk 9: 3 untranslated English lines, e.g. 'GET /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale'
- [reference/kubernetes-api/core/resource-quota-v1.md](md/reference/kubernetes-api/core/resource-quota-v1.md): chunk 8: 3 untranslated English lines, e.g. 'PATCH /api/v1/namespaces/{namespace}/resourcequotas/{name}/status'
- [reference/kubernetes-api/core/service-v1.md](md/reference/kubernetes-api/core/service-v1.md): chunk 11: 10 untranslated English lines, e.g. 'POST /api/v1/namespaces/{namespace}/services/{name}/proxy'; chunk 11: short: 1017 words vs 1820 source words
- [reference/kubernetes-api/lifecycle/eviction-v1alpha1.md](md/reference/kubernetes-api/lifecycle/eviction-v1alpha1.md): chunk 4: heading anchors {#...} differ
- [reference/kubernetes-api/networking/ingress-v1.md](md/reference/kubernetes-api/networking/ingress-v1.md): chunk 5: heading anchors {#...} differ
- [reference/kubernetes-api/scheduling/pod-group-v1beta1.md](md/reference/kubernetes-api/scheduling/pod-group-v1beta1.md): chunk 2: 4 untranslated English lines, e.g. 'POST /apis/scheduling.k8s.io/v1beta1/namespaces/{namespace}/podgroups'
- [reference/kubernetes-api/storage/volume-attachment-v1.md](md/reference/kubernetes-api/storage/volume-attachment-v1.md): chunk 2: heading anchors {#...} differ
- [reference/setup-tools/kubeadm/generated/kubeadm_config/kubeadm_config_images_list.md](md/reference/setup-tools/kubeadm/generated/kubeadm_config/kubeadm_config_images_list.md): chunk 1: short: 340 words vs 459 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/_index.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/_index.md): chunk 1: short: 820 words vs 1131 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_addon_all.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_addon_all.md): chunk 1: short: 406 words vs 566 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_addon_kube-proxy.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_addon_kube-proxy.md): chunk 1: short: 365 words vs 494 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_certs_all.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_certs_all.md): chunk 1: short: 322 words vs 432 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_all.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_all.md): chunk 1: short: 473 words vs 658 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_apiserver.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_apiserver.md): chunk 1: short: 427 words vs 615 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_controller-manager.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_controller-manager.md): chunk 1: short: 332 words vs 470 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_scheduler.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_control-plane_scheduler.md): chunk 1: short: 300 words vs 425 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_etcd_local.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_etcd_local.md): chunk 1: short: 287 words vs 396 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_admin.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_admin.md): chunk 1: short: 300 words vs 412 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_all.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_all.md): chunk 1: short: 293 words vs 411 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_controller-manager.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_controller-manager.md): chunk 1: short: 293 words vs 410 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_scheduler.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_scheduler.md): chunk 1: short: 294 words vs 406 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_super-admin.md](md/reference/setup-tools/kubeadm/generated/kubeadm_init/kubeadm_init_phase_kubeconfig_super-admin.md): chunk 1: short: 286 words vs 398 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply.md): chunk 1: short: 515 words vs 705 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_addon_coredns.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_addon_coredns.md): chunk 1: short: 271 words vs 369 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_addon_kube-proxy.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_addon_kube-proxy.md): chunk 1: short: 269 words vs 371 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_control-plane.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_control-plane.md): chunk 1: short: 305 words vs 440 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node.md): chunk 1: short: 376 words vs 519 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_all.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_all.md): chunk 1: short: 270 words vs 370 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_coredns.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_coredns.md): chunk 1: short: 273 words vs 370 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_kube-proxy.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon_kube-proxy.md): chunk 1: short: 270 words vs 372 source words
- [reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_control-plane.md](md/reference/setup-tools/kubeadm/generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_control-plane.md): chunk 1: short: 318 words vs 448 source words
- [reference/setup-tools/kubeadm/kubeadm-init-phase.md](md/reference/setup-tools/kubeadm/kubeadm-init-phase.md): chunk 1: short: 826 words vs 1211 source words
- [reference/setup-tools/kubeadm/kubeadm-upgrade-phase.md](md/reference/setup-tools/kubeadm/kubeadm-upgrade-phase.md): chunk 1: short: 204 words vs 316 source words
- [tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md](md/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume.md): chunk 1: 6 untranslated English lines, e.g. 'echo Hello from the debian container > /pod-data/index.html'

</div>

<div dir="rtl">

فهرست کامل همه‌ی صفحات: [INDEX.md](INDEX.md)

</div>

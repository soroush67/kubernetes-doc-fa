---
title: برچسب‌ها، حاشیه‌نویسی‌ها و taintهای شناخته‌شده
content_type: concept
weight: 40
no_list: true
card:
  name: reference
  weight: 30
  anchors:
  - anchor: "#labels-annotations-and-taints-used-on-api-objects"
    title: برچسب‌ها، حاشیه‌نویسی‌ها و taintها
---

<!-- overview -->

کوبرنتیز همهٔ برچسب‌ها، حاشیه‌نویسی‌ها (annotation) و taintهای موجود در فضاهای نام (namespace) `kubernetes.io` و `k8s.io` را برای خود رزرو کرده است.

این سند هم مرجعی برای این مقادیر است و هم نقطهٔ هماهنگی برای تخصیص آن‌ها.

<!-- body -->

## برچسب‌ها، حاشیه‌نویسی‌ها و taintهای استفاده‌شده روی آبجکت‌های API


### apf.kubernetes.io/autoupdate-spec

نوع: حاشیه‌نویسی

نمونه: `apf.kubernetes.io/autoupdate-spec: "true"`

محل استفاده: [آبجکت‌های `FlowSchema` و `PriorityLevelConfiguration`](/docs/concepts/cluster-administration/flow-control/#defaults)

اگر مقدار این حاشیه‌نویسی روی یک FlowSchema یا PriorityLevelConfiguration برابر با true باشد، مدیریت `spec` آن آبجکت بر عهدهٔ kube-apiserver خواهد بود. اگر سرور API یک آبجکت APF را نشناسد و شما آن را برای به‌روزرسانی خودکار حاشیه‌نویسی کرده باشید، سرور API کل آن آبجکت را حذف می‌کند. در غیر این صورت، سرور API مشخصات آبجکت را مدیریت نمی‌کند.
برای جزئیات بیشتر، بخش [نگهداری آبجکت‌های پیکربندی اجباری و پیشنهادی](/docs/concepts/cluster-administration/flow-control/#maintenance-of-the-mandatory-and-suggested-configuration-objects) را بخوانید.

### app.kubernetes.io/component

نوع: برچسب

نمونه: `app.kubernetes.io/component: "database"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

مؤلفهٔ موردنظر در معماری برنامه را مشخص می‌کند.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### app.kubernetes.io/created-by (منسوخ‌شده)

نوع: برچسب

نمونه: `app.kubernetes.io/created-by: "controller-manager"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

کنترل‌کننده یا کاربری را که این منبع را ایجاد کرده است مشخص می‌کند.

{{< note >}}
این برچسب از نسخهٔ v1.9 منسوخ شده است.
{{< /note >}}

### app.kubernetes.io/instance

نوع: برچسب

نمونه: `app.kubernetes.io/instance: "mysql-abcxyz"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

نامی یکتا که نمونهٔ یک برنامه را شناسایی می‌کند.
برای تخصیص نامی غیریکتا، از [app.kubernetes.io/name](#app-kubernetes-io-name) استفاده کنید.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### app.kubernetes.io/managed-by

نوع: برچسب

نمونه: `app.kubernetes.io/managed-by: "helm"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

ابزاری را که برای مدیریت عملیات یک برنامه به کار می‌رود مشخص می‌کند.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### app.kubernetes.io/name

نوع: برچسب

نمونه: `app.kubernetes.io/name: "mysql"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

نام برنامه را مشخص می‌کند.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### app.kubernetes.io/part-of

نوع: برچسب

نمونه: `app.kubernetes.io/part-of: "wordpress"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

نام برنامهٔ سطح بالاتری را که این آبجکت بخشی از آن است مشخص می‌کند.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### app.kubernetes.io/version

نوع: برچسب

نمونه: `app.kubernetes.io/version: "5.7.21"`

محل استفاده: همهٔ آبجکت‌ها (معمولاً روی [منابع بار کاری](/docs/reference/kubernetes-api/workload-resources/) استفاده می‌شود).

نسخهٔ فعلی برنامه را مشخص می‌کند.

قالب‌های رایج مقدار این برچسب عبارت‌اند از:

- [نسخهٔ معنایی](https://semver.org/spec/v1.0.0.html)
- [هش بازبینی](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_single_revisions) گیت برای کد منبع.

این برچسب یکی از [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/#labels) است.

### applyset.kubernetes.io/additional-namespaces (آلفا) {#applyset-kubernetes-io-additional-namespaces}

نوع: حاشیه‌نویسی

نمونه: `applyset.kubernetes.io/additional-namespaces: "namespace1,namespace2"`

محل استفاده: آبجکت‌هایی که والد ApplySet هستند.

استفاده از این حاشیه‌نویسی در مرحلهٔ آلفا است.
در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، می‌توانید این حاشیه‌نویسی را روی Secretها، ConfigMapها یا منابع سفارشی به کار ببرید، به شرطی که {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} تعریف‌کنندهٔ آن‌ها برچسب `applyset.kubernetes.io/is-parent-type` را داشته باشد.

این حاشیه‌نویسی بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
این حاشیه‌نویسی روی آبجکت والدی قرار می‌گیرد که برای ردیابی یک ApplySet به کار می‌رود و دامنهٔ ApplySet را به فراتر از فضای نام خود آبجکت والد (در صورت وجود) گسترش می‌دهد.
مقدار آن فهرستی جداشده با کاما از نام فضاهای نامی است که آبجکت‌ها در آن‌ها قرار دارند و با فضای نام والد متفاوت‌اند.

### applyset.kubernetes.io/contains-group-kinds (آلفا) {#applyset-kubernetes-io-contains-group-kinds}

نوع: حاشیه‌نویسی

نمونه: `applyset.kubernetes.io/contains-group-kinds: "certificates.cert-manager.io,configmaps,deployments.apps,secrets,services"`

محل استفاده: آبجکت‌هایی که والد ApplySet هستند.

استفاده از این حاشیه‌نویسی در مرحلهٔ آلفا است.
در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، می‌توانید این حاشیه‌نویسی را روی Secretها، ConfigMapها یا منابع سفارشی به کار ببرید، به شرطی که CustomResourceDefinition تعریف‌کنندهٔ آن‌ها برچسب `applyset.kubernetes.io/is-parent-type` را داشته باشد.

این حاشیه‌نویسی بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
این حاشیه‌نویسی روی آبجکت والدی قرار می‌گیرد که برای ردیابی یک ApplySet به کار می‌رود و فهرست‌کردن آبجکت‌های عضو ApplySet را بهینه می‌کند. وجود آن در مشخصهٔ ApplySet اختیاری است، زیرا ابزارها می‌توانند عملیات کشف را انجام دهند یا از روش بهینه‌سازی دیگری استفاده کنند. با این حال، در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، ابزار kubectl به وجود آن نیاز دارد. در صورت وجود این حاشیه‌نویسی، مقدار آن باید فهرستی جداشده با کاما از group-kindها در قالب نام کاملاً مشخص، یعنی `<resource>.<group>`، باشد.

### applyset.kubernetes.io/contains-group-resources (منسوخ‌شده) {#applyset-kubernetes-io-contains-group-resources}

نوع: حاشیه‌نویسی

نمونه: `applyset.kubernetes.io/contains-group-resources: "certificates.cert-manager.io,configmaps,deployments.apps,secrets,services"`

محل استفاده: آبجکت‌هایی که والد ApplySet هستند.

در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، می‌توانید این حاشیه‌نویسی را روی Secretها، ConfigMapها یا منابع سفارشی به کار ببرید، به شرطی که CustomResourceDefinition تعریف‌کنندهٔ آن‌ها برچسب `applyset.kubernetes.io/is-parent-type` را داشته باشد.

این حاشیه‌نویسی بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
این حاشیه‌نویسی روی آبجکت والدی قرار می‌گیرد که برای ردیابی یک ApplySet به کار می‌رود و فهرست‌کردن آبجکت‌های عضو ApplySet را بهینه می‌کند. وجود آن در مشخصهٔ ApplySet اختیاری است، زیرا ابزارها می‌توانند عملیات کشف را انجام دهند یا از روش بهینه‌سازی دیگری استفاده کنند. با این حال، در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، ابزار kubectl به وجود آن نیاز دارد. در صورت وجود این حاشیه‌نویسی، مقدار آن باید فهرستی جداشده با کاما از group-kindها در قالب نام کاملاً مشخص، یعنی `<resource>.<group>`، باشد.

{{< note >}}
این حاشیه‌نویسی در حال حاضر منسوخ شده و [`applyset.kubernetes.io/contains-group-kinds`](#applyset-kubernetes-io-contains-group-kinds) جایگزین آن شده است. پشتیبانی از آن در نسخهٔ بتا یا GA قابلیت applyset حذف خواهد شد.
{{< /note >}}

### applyset.kubernetes.io/id (آلفا) {#applyset-kubernetes-io-id}

نوع: برچسب

نمونه: `applyset.kubernetes.io/id: "applyset-0eFHV8ySqp7XoShsGvyWFQD3s96yqwHmzc4e0HR1dsY-v1"`

محل استفاده: آبجکت‌هایی که والد ApplySet هستند.

استفاده از این برچسب در مرحلهٔ آلفا است.
در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، می‌توانید این برچسب را روی Secretها، ConfigMapها یا منابع سفارشی به کار ببرید، به شرطی که CustomResourceDefinition تعریف‌کنندهٔ آن‌ها برچسب `applyset.kubernetes.io/is-parent-type` را داشته باشد.

این برچسب بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
همین برچسب است که یک آبجکت را به آبجکت والد ApplySet تبدیل می‌کند.
مقدار آن شناسهٔ یکتای ApplySet است که از هویت خود آبجکت والد به دست می‌آید. این شناسه **باید** کدگذاری base64 (با کدگذاری ایمن برای URL طبق RFC4648) از هش group-kind-name-namespace آبجکتی باشد که برچسب روی آن قرار دارد، و این قالب را داشته باشد:
`<base64(sha256(<name>.<namespace>.<kind>.<group>))>`.
مقدار این برچسب هیچ ارتباطی با UID آبجکت ندارد.

### applyset.kubernetes.io/is-parent-type (آلفا) {#applyset-kubernetes-io-is-parent-type}

نوع: برچسب

نمونه: `applyset.kubernetes.io/is-parent-type: "true"`

محل استفاده: تعریف منبع سفارشی (CRD)

استفاده از این برچسب در مرحلهٔ آلفا است.
این برچسب بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
با قراردادن این برچسب روی یک CustomResourceDefinition (CRD)، نوع منبع سفارشی‌ای را که آن CRD تعریف می‌کند (نه خود CRD را) به‌عنوان والد مجاز برای ApplySet مشخص می‌کنید.
تنها مقدار مجاز برای این برچسب `"true"` است. اگر می‌خواهید مشخص کنید که یک CRD والد معتبری برای ApplySetها نیست، این برچسب را روی آن قرار ندهید.

### applyset.kubernetes.io/part-of (آلفا) {#applyset-kubernetes-io-part-of}

نوع: برچسب

نمونه: `applyset.kubernetes.io/part-of: "applyset-0eFHV8ySqp7XoShsGvyWFQD3s96yqwHmzc4e0HR1dsY-v1"`

محل استفاده: همهٔ آبجکت‌ها.

استفاده از این برچسب در مرحلهٔ آلفا است.
این برچسب بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
همین برچسب است که یک آبجکت را به عضوی از یک ApplySet تبدیل می‌کند.
مقدار این برچسب **باید** با مقدار برچسب `applyset.kubernetes.io/id` روی آبجکت والد یکسان باشد.

### applyset.kubernetes.io/tooling (آلفا) {#applyset-kubernetes-io-tooling}

نوع: حاشیه‌نویسی

نمونه: `applyset.kubernetes.io/tooling: "kubectl/v{{< skew currentVersion >}}"`

محل استفاده: آبجکت‌هایی که والد ApplySet هستند.

استفاده از این حاشیه‌نویسی در مرحلهٔ آلفا است.
در کوبرنتیز نسخهٔ {{< skew currentVersion >}}، می‌توانید این حاشیه‌نویسی را روی Secretها، ConfigMapها یا منابع سفارشی به کار ببرید، به شرطی که CustomResourceDefinition تعریف‌کنندهٔ آن‌ها برچسب `applyset.kubernetes.io/is-parent-type` را داشته باشد.

این حاشیه‌نویسی بخشی از مشخصه‌ای است که برای پیاده‌سازی [هرس مبتنی بر ApplySet در kubectl](/docs/tasks/manage-kubernetes-objects/declarative-config/#alternative-kubectl-apply-f-directory-prune) استفاده می‌شود.
این حاشیه‌نویسی روی آبجکت والدی قرار می‌گیرد که برای ردیابی یک ApplySet به کار می‌رود و نشان می‌دهد کدام ابزار آن ApplySet را مدیریت می‌کند. ابزارها باید از تغییردادن ApplySetهای متعلق به ابزارهای دیگر خودداری کنند.
مقدار آن باید در قالب `<toolname>/<semver>` باشد.

### apps.kubernetes.io/pod-index (بتا) {#apps-kubernetes.io-pod-index}

نوع: برچسب

نمونه: `apps.kubernetes.io/pod-index: "0"`

محل استفاده: Pod

هنگامی که کنترل‌کنندهٔ StatefulSet یک Pod برای StatefulSet ایجاد می‌کند، این برچسب را روی آن Pod قرار می‌دهد.
مقدار برچسب، اندیس ترتیبی Pod در حال ایجاد است.

برای جزئیات بیشتر، بخش [برچسب اندیس Pod](/docs/concepts/workloads/controllers/statefulset/#pod-index-label) را در مبحث StatefulSet ببینید.
توجه کنید که برای افزوده‌شدن این برچسب به Podها، باید feature gate با نام [PodIndexLabel](/docs/reference/command-line-tools-reference/feature-gates/) فعال باشد.

### resource.kubernetes.io/pod-claim-name

نوع: حاشیه‌نویسی

نمونه: `resource.kubernetes.io/pod-claim-name: "my-pod-claim"`

محل استفاده: ResourceClaim

این حاشیه‌نویسی به ResourceClaimهای تولیدشده اختصاص داده می‌شود.
مقدار آن با نام درخواست منبع در `.spec` هر Pod یا Podهایی که ResourceClaim برای آن‌ها ایجاد شده است مطابقت دارد.
در [تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/)، قابلیت فرادادهٔ قابل‌کشف دستگاه از این حاشیه‌نویسی استفاده می‌کند تا در درخواست‌های مبتنی بر الگو، ResourceClaim تولیدشده را به نام درخواست در Pod (`pod.spec.resourceClaims[].name`) نگاشت کند.
کوبرنتیز این حاشیه‌نویسی را مدیریت می‌کند، بنابراین نباید آن را تغییر دهید.

### cluster-autoscaler.kubernetes.io/safe-to-evict

نوع: حاشیه‌نویسی

نمونه: `cluster-autoscaler.kubernetes.io/safe-to-evict: "true"`

محل استفاده: Pod

وقتی مقدار این حاشیه‌نویسی `"true"` باشد، مقیاس‌دهندهٔ خودکار کلاستر (cluster autoscaler) می‌تواند یک Pod را بیرون کند، حتی اگر قوانین دیگر در حالت عادی مانع این کار شوند.
مقیاس‌دهندهٔ خودکار کلاستر هرگز Podهایی را که مقدار این حاشیه‌نویسی در آن‌ها صراحتاً `"false"` تنظیم شده است بیرون نمی‌کند. می‌توانید این مقدار را روی Podهای مهمی تنظیم کنید که می‌خواهید همچنان در حال اجرا بمانند.
اگر این حاشیه‌نویسی تنظیم نشده باشد، مقیاس‌دهندهٔ خودکار کلاستر از رفتار خود در سطح Pod پیروی می‌کند.

### config.kubernetes.io/local-config

نوع: حاشیه‌نویسی

نمونه: `config.kubernetes.io/local-config: "true"`

محل استفاده: همهٔ آبجکت‌ها

از این حاشیه‌نویسی در مانیفست‌ها استفاده می‌شود تا یک آبجکت به‌عنوان پیکربندی محلی علامت‌گذاری شود که نباید به API کوبرنتیز ارسال شود.

مقدار `"true"` برای این حاشیه‌نویسی اعلام می‌کند که این آبجکت فقط در ابزارهای سمت کلاینت مصرف می‌شود و نباید به سرور API ارسال شود.

با مقدار `"false"` می‌توان اعلام کرد که آبجکت باید به سرور API ارسال شود، حتی اگر در غیر این صورت محلی فرض شود.

این حاشیه‌نویسی بخشی از مشخصهٔ توابع مدل منابع کوبرنتیز (Kubernetes Resource Model یا KRM) است که Kustomize و ابزارهای شخص ثالث مشابه از آن استفاده می‌کنند.
برای مثال، Kustomize آبجکت‌های دارای این حاشیه‌نویسی را از خروجی نهایی ساخت خود حذف می‌کند.


### container.apparmor.security.beta.kubernetes.io/* (منسوخ‌شده) {#container-apparmor-security-beta-kubernetes-io}

نوع: حاشیه‌نویسی

نمونه: `container.apparmor.security.beta.kubernetes.io/my-container: my-custom-profile`

محل استفاده: Podها

با این حاشیه‌نویسی می‌توانید پروفایل امنیتی AppArmor را برای یک کانتینر درون Pod کوبرنتیز مشخص کنید. از نسخهٔ v1.30 کوبرنتیز، باید به‌جای آن از فیلد `appArmorProfile` استفاده کرد.
برای اطلاعات بیشتر، آموزش [AppArmor](/docs/tutorials/security/apparmor/) را ببینید.
این آموزش نشان می‌دهد که چگونه می‌توان با AppArmor توانایی‌ها و دسترسی‌های یک کانتینر را محدود کرد.

پروفایل مشخص‌شده، مجموعه قوانین و محدودیت‌هایی را تعیین می‌کند که فرایند کانتینری‌شده باید از آن‌ها پیروی کند. این کار به اعمال سیاست‌های امنیتی و جداسازی کانتینرها کمک می‌کند.

### csi.alpha.kubernetes.io/node-id (منسوخ‌شده) {#csi-alpha-kubernetes-io-node-id}

نوع: حاشیه‌نویسی

نمونه: `csi.alpha.kubernetes.io/node-id: "node-12345"`

محل استفاده: VolumeAttachmentها

این حاشیه‌نویسی شناسهٔ نودی را که درایور CSI از آن استفاده می‌کند ثبت می‌کند تا در صورت دردسترس‌نبودن آبجکت [CSINode](/docs/reference/kubernetes-api/storage/csi-node-v1/) به‌عنوان جایگزین به کار رود.
کانتینر کناری external-attacher در CSI پیش از اتصال حجم (volume)، مقدار آن را پر می‌کند.

این حاشیه‌نویسی سازوکاری جایگزین برای جداکردن حجم‌ها در مواقعی فراهم می‌کند که CSINode مناسبی وجود ندارد.

از آنجا که این حاشیه‌نویسی منسوخ شده است، پروژهٔ کوبرنتیز توصیه می‌کند آن را روی VolumeAttachment یا هیچ آبجکت دیگری تنظیم **نکنید**.

### csi.volume.kubernetes.io/nodeid (منسوخ‌شده) {#csi-volume-kubernetes-io-nodeid}

نوع: حاشیه‌نویسی

نمونه: `csi.volume.kubernetes.io/nodeid: "node-12345"`

محل استفاده: Nodeها

این حاشیه‌نویسی شناسهٔ یک نود را به شکلی که درایور رابط ذخیره‌سازی کانتینر (Container Storage Interface یا CSI) می‌شناسد مشخص می‌کند. کامپوننت `kubelet` هنگام ثبت درایور، با فراخوانی متد gRPC با نام `NodeGetInfo` از درایور CSI، شناسهٔ نود را دریافت می‌کند و مقدار این حاشیه‌نویسی را پر می‌کند. کانتینر کناری external-attacher نیز هنگام اتصال یا جداکردن حجم‌ها، این حاشیه‌نویسی را می‌خواند تا شناسهٔ نود را به دست آورد.

این حاشیه‌نویسی به نفع آبجکت CSINode منسوخ شده است؛ آبجکتی که همین قابلیت را از طریق [فیلد `spec.drivers[].nodeID`](/docs/reference/kubernetes-api/storage/csi-node-v1/#CSINodeDriver) فراهم می‌کند.

### deployment.kubernetes.io/desired-replicas

نوع: حاشیه‌نویسی

نمونه: `deployment.kubernetes.io/desired-replicas: "3"`

محل استفاده: ReplicaSet

کنترل‌کنندهٔ Deployment این حاشیه‌نویسی را روی ReplicaSetهایی که مدیریت می‌کند تنظیم می‌کند.
مقدار آن تعداد مطلوب رپلیکاها (`.spec.replicas`) در Deployment مالک این ReplicaSet را نشان می‌دهد. کنترل‌کنندهٔ Deployment از این حاشیه‌نویسی برای پیگیری وضعیت مطلوب در طول به‌روزرسانی‌های تدریجی و عملیات مقیاس‌دهی استفاده می‌کند.

این حاشیه‌نویسی داخلی است و کنترل‌کنندهٔ Deployment از آن استفاده می‌کند، بنابراین نباید آن را به‌صورت دستی تغییر داد.

### deployment.kubernetes.io/max-replicas

نوع: حاشیه‌نویسی

نمونه: `deployment.kubernetes.io/max-replicas: "5"`

محل استفاده: ReplicaSet

کنترل‌کنندهٔ Deployment این حاشیه‌نویسی را روی ReplicaSetهایی که مدیریت می‌کند تنظیم می‌کند.
مقدار آن حداکثر تعداد رپلیکاهایی را نشان می‌دهد که این ReplicaSet در طول یک به‌روزرسانی تدریجی می‌تواند داشته باشد. از این مقدار برای پیاده‌سازی پارامتر `maxSurge` در راهبرد به‌روزرسانی تدریجی Deployment استفاده می‌شود؛ پارامتری که تعیین می‌کند در طول به‌روزرسانی چند Pod اضافی بیش از تعداد مطلوب می‌توان ایجاد کرد.

این حاشیه‌نویسی داخلی است و کنترل‌کنندهٔ Deployment از آن استفاده می‌کند، بنابراین نباید آن را به‌صورت دستی تغییر داد.

### deployment.kubernetes.io/revision

نوع: حاشیه‌نویسی (annotation)

مثال: `deployment.kubernetes.io/revision: "2"`

محل استفاده: ReplicaSet

کنترل‌کنندهٔ Deployment این حاشیه‌نویسی را روی ReplicaSetهایی که مدیریت می‌کند تنظیم می‌کند. مقدار آن شمارهٔ بازبینی Deployment را نشان می‌دهد. هر بار که قالب Pod در Deployment (`.spec.template`) تغییر کند، شمارهٔ بازبینی یک واحد افزایش می‌یابد. از این حاشیه‌نویسی برای پیگیری تاریخچهٔ انتشار استفاده می‌شود و به کمک آن می‌توان با دستور `kubectl rollout undo` به بازبینی‌های قبلی بازگشت.

شمارهٔ بازبینی در خروجی دستور `kubectl rollout history deployment/<name>` نیز دیده می‌شود.

این حاشیه‌نویسی داخلی است و کنترل‌کنندهٔ Deployment از آن استفاده می‌کند، بنابراین نباید آن را به‌صورت دستی تغییر دهید.

### deployment.kubernetes.io/revision-history

نوع: حاشیه‌نویسی

مثال: `deployment.kubernetes.io/revision-history: "1,3"`

محل استفاده: ReplicaSet

وقتی بازگردانی (rollback) باعث استفادهٔ دوباره از یک ReplicaSet شود، کنترل‌کنندهٔ Deployment این حاشیه‌نویسی را روی آن ReplicaSet تنظیم می‌کند. مقدار آن فهرستی جداشده با کاما از تمام شماره‌های بازبینی قبلی است که آن ReplicaSet برای یک Deployment به کار رفته است. این فهرست هنگام به‌روزرسانی حاشیه‌نویسی `deployment.kubernetes.io/revision` به شمارهٔ بازبینی جدید، به‌عنوان تاریخچه نگه داشته می‌شود.

این حاشیه‌نویسی داخلی است و کنترل‌کنندهٔ Deployment از آن استفاده می‌کند، بنابراین نباید آن را به‌صورت دستی تغییر دهید.

### internal.config.kubernetes.io/* (پیشوند رزروشده) {#internal.config.kubernetes.io-reserved-wildcard}

نوع: حاشیه‌نویسی

محل استفاده: همهٔ آبجکت‌ها

این پیشوند برای استفادهٔ داخلی ابزارهایی رزرو شده است که طبق مشخصات Kubernetes Resource Model (KRM) Functions Specification نقش هماهنگ‌کننده (orchestrator) را بر عهده دارند. حاشیه‌نویسی‌های دارای این پیشوند فقط درون فرایند هماهنگ‌سازی کاربرد دارند و در مانیفست‌های روی سیستم فایل ذخیره نمی‌شوند. به بیان دیگر، ابزار هماهنگ‌کننده باید هنگام خواندن فایل‌ها از سیستم فایل محلی این حاشیه‌نویسی‌ها را تنظیم کند و هنگام نوشتن خروجی تابع‌ها در سیستم فایل، آن‌ها را حذف کند.

هیچ تابع KRM **نباید** حاشیه‌نویسی‌های دارای این پیشوند را تغییر دهد، مگر اینکه برای حاشیه‌نویسی خاصی ترتیب دیگری مشخص شده باشد. به این ترتیب، ابزارهای هماهنگ‌کننده می‌توانند بدون نیاز به تغییر تابع‌های موجود، حاشیه‌نویسی‌های داخلی بیشتری اضافه کنند.

### internal.config.kubernetes.io/path

نوع: حاشیه‌نویسی

مثال: `internal.config.kubernetes.io/path: "relative/file/path.yaml"`

محل استفاده: همهٔ آبجکت‌ها

این حاشیه‌نویسی مسیر نسبی فایل مانیفستی را که آبجکت از آن بارگذاری شده است ثبت می‌کند. اجزای این مسیر با اسلش از هم جدا می‌شوند و قالب آن به سیستم‌عامل وابسته نیست. مسیر نسبت به مکان ثابتی روی سیستم فایل سنجیده می‌شود که ابزار هماهنگ‌کننده آن را تعیین می‌کند.

این حاشیه‌نویسی بخشی از مشخصات Kubernetes Resource Model (KRM) Functions Specification است که Kustomize و ابزارهای شخص ثالث مشابه از آن استفاده می‌کنند.

تابع KRM **نباید** این حاشیه‌نویسی را روی آبجکت‌های ورودی تغییر دهد، مگر اینکه فایل‌های ارجاع‌داده‌شده را تغییر دهد. تابع KRM **می‌تواند** این حاشیه‌نویسی را روی آبجکت‌هایی که تولید می‌کند قرار دهد.

### internal.config.kubernetes.io/index

نوع: حاشیه‌نویسی

مثال: `internal.config.kubernetes.io/index: "2"`

محل استفاده: همهٔ آبجکت‌ها

این حاشیه‌نویسی موقعیت سند YAML حاوی آبجکت را درون فایل مانیفستی که آبجکت از آن بارگذاری شده است ثبت می‌کند. شمارش این موقعیت از صفر آغاز می‌شود. سندهای YAML با سه خط تیره (`---`) از هم جدا می‌شوند و هر کدام می‌توانند یک آبجکت داشته باشند. اگر این حاشیه‌نویسی مشخص نشده باشد، مقدار آن ۰ در نظر گرفته می‌شود.

این حاشیه‌نویسی بخشی از مشخصات Kubernetes Resource Model (KRM) Functions Specification است که Kustomize و ابزارهای شخص ثالث مشابه از آن استفاده می‌کنند.

تابع KRM **نباید** این حاشیه‌نویسی را روی آبجکت‌های ورودی تغییر دهد، مگر اینکه فایل‌های ارجاع‌داده‌شده را تغییر دهد. تابع KRM **می‌تواند** این حاشیه‌نویسی را روی آبجکت‌هایی که تولید می‌کند قرار دهد.

### kube-scheduler-simulator.sigs.k8s.io/bind-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/bind-result: '{"DefaultBinder":"success"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های bind زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/filter-result

نوع: حاشیه‌نویسی

مثال:

```yaml
kube-scheduler-simulator.sigs.k8s.io/filter-result: >-
      {"node-282x7":{"AzureDiskLimits":"passed","EBSLimits":"passed","GCEPDLimits":"passed","InterPodAffinity":"passed","NodeAffinity":"passed","NodeName":"passed","NodePorts":"passed","NodeResourcesFit":"passed","NodeUnschedulable":"passed","NodeVolumeLimits":"passed","PodTopologySpread":"passed","TaintToleration":"passed","VolumeBinding":"passed","VolumeRestrictions":"passed","VolumeZone":"passed"},"node-gp9t4":{"AzureDiskLimits":"passed","EBSLimits":"passed","GCEPDLimits":"passed","InterPodAffinity":"passed","NodeAffinity":"passed","NodeName":"passed","NodePorts":"passed","NodeResourcesFit":"passed","NodeUnschedulable":"passed","NodeVolumeLimits":"passed","PodTopologySpread":"passed","TaintToleration":"passed","VolumeBinding":"passed","VolumeRestrictions":"passed","VolumeZone":"passed"}}
```

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های filter زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/finalscore-result

نوع: حاشیه‌نویسی

مثال:

```yaml
kube-scheduler-simulator.sigs.k8s.io/finalscore-result: >-
      {"node-282x7":{"ImageLocality":"0","InterPodAffinity":"0","NodeAffinity":"0","NodeNumber":"0","NodeResourcesBalancedAllocation":"76","NodeResourcesFit":"73","PodTopologySpread":"200","TaintToleration":"300","VolumeBinding":"0"},"node-gp9t4":{"ImageLocality":"0","InterPodAffinity":"0","NodeAffinity":"0","NodeNumber":"0","NodeResourcesBalancedAllocation":"76","NodeResourcesFit":"73","PodTopologySpread":"200","TaintToleration":"300","VolumeBinding":"0"}}
```

محل استفاده: Pod

این حاشیه‌نویسی امتیازهای نهایی را ثبت می‌کند که زمان‌بند از روی امتیازهای افزونه‌های score خود محاسبه می‌کند. ابزار https://sigs.k8s.io/kube-scheduler-simulator از این حاشیه‌نویسی استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/permit-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/permit-result: '{"CustomPermitPlugin":"success"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های permit زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/permit-result-timeout

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/permit-result-timeout: '{"CustomPermitPlugin":"10s"}'`

محل استفاده: Pod

این حاشیه‌نویسی مهلت‌های زمانی برگشتی از افزونه‌های permit زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/postfilter-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/postfilter-result: '{"DefaultPreemption":"success"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های postfilter زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/prebind-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/prebind-result: '{"VolumeBinding":"success"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های prebind زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/prefilter-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/prebind-result: '{"NodeAffinity":"[\"node-\a"]"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ PreFilter افزونه‌های prefilter زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/prefilter-result-status

نوع: حاشیه‌نویسی

مثال:

```yaml
kube-scheduler-simulator.sigs.k8s.io/prefilter-result-status: >-
      {"InterPodAffinity":"success","NodeAffinity":"success","NodePorts":"success","NodeResourcesFit":"success","PodTopologySpread":"success","VolumeBinding":"success","VolumeRestrictions":"success"}
```

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های prefilter زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/prescore-result

نوع: حاشیه‌نویسی

مثال:

```yaml
    kube-scheduler-simulator.sigs.k8s.io/prescore-result: >-
      {"InterPodAffinity":"success","NodeAffinity":"success","NodeNumber":"success","PodTopologySpread":"success","TaintToleration":"success"}
```

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های prefilter زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/reserve-result

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/reserve-result: '{"VolumeBinding":"success"}'`

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های reserve زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/result-history

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/result-history: '[]'`

محل استفاده: Pod

این حاشیه‌نویسی تمام نتایج زمان‌بندی گذشته را که از افزونه‌های زمان‌بند به دست آمده‌اند ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/score-result

نوع: حاشیه‌نویسی

```yaml
    kube-scheduler-simulator.sigs.k8s.io/score-result: >-
      {"node-282x7":{"ImageLocality":"0","InterPodAffinity":"0","NodeAffinity":"0","NodeNumber":"0","NodeResourcesBalancedAllocation":"76","NodeResourcesFit":"73","PodTopologySpread":"0","TaintToleration":"0","VolumeBinding":"0"},"node-gp9t4":{"ImageLocality":"0","InterPodAffinity":"0","NodeAffinity":"0","NodeNumber":"0","NodeResourcesBalancedAllocation":"76","NodeResourcesFit":"73","PodTopologySpread":"0","TaintToleration":"0","VolumeBinding":"0"}}
```

محل استفاده: Pod

این حاشیه‌نویسی نتیجهٔ افزونه‌های score زمان‌بند را ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kube-scheduler-simulator.sigs.k8s.io/selected-node

نوع: حاشیه‌نویسی

مثال: `kube-scheduler-simulator.sigs.k8s.io/selected-node: node-282x7`

محل استفاده: Pod

این حاشیه‌نویسی نودی را که در چرخهٔ زمان‌بندی انتخاب شده است ثبت می‌کند و ابزار https://sigs.k8s.io/kube-scheduler-simulator از آن استفاده می‌کند.

### kubernetes.io/arch

نوع: برچسب

مثال: `kubernetes.io/arch: "amd64"`

محل استفاده: Node

مقدار این برچسب را kubelet برابر با `runtime.GOARCH`، طبق تعریف زبان Go، تنظیم می‌کند. اگر نودهای ARM و x86 را در کنار هم به کار می‌برید، این برچسب می‌تواند مفید باشد.

### kubernetes.io/os

نوع: برچسب

مثال: `kubernetes.io/os: "linux"`

محل استفاده: Node، Pod

در مورد نودها، kubelet مقدار این برچسب را برابر با `runtime.GOOS`، طبق تعریف زبان Go، تنظیم می‌کند. اگر در کلاستر خود از چند سیستم‌عامل استفاده می‌کنید (برای مثال، نودهای Linux و Windows را در کنار هم دارید)، این برچسب می‌تواند مفید باشد.

این برچسب را روی Pod نیز می‌توانید تنظیم کنید. کوبرنتیز اجازه می‌دهد هر مقداری برای این برچسب تعیین کنید، اما اگر از آن استفاده می‌کنید، باید مقدارش را برابر با رشتهٔ `runtime.GOOS` زبان Go برای سیستم‌عاملی قرار دهید که این Pod واقعاً با آن کار می‌کند.

اگر مقدار برچسب `kubernetes.io/os` در یک Pod با مقدار همین برچسب روی نود مطابقت نداشته باشد، kubelet روی آن نود Pod را نمی‌پذیرد. با این حال، kube-scheduler این موضوع را در نظر نمی‌گیرد. از سوی دیگر، اگر برای Pod سیستم‌عاملی مشخص کرده باشید که با سیستم‌عامل نود محل اجرای kubelet یکسان نباشد، kubelet از اجرای آن Pod خودداری می‌کند. برای جزئیات بیشتر، بخش [سیستم‌عامل Pod](/docs/concepts/workloads/pods/#pod-os) را ببینید.

### kubernetes.io/metadata.name

نوع: برچسب

مثال: `kubernetes.io/metadata.name: "mynamespace"`

محل استفاده: Namespaces

سرور API کوبرنتیز (بخشی از {{< glossary_tooltip text="control plane" term_id="control-plane" >}}) این برچسب را روی تمام فضاهای نام (namespace) تنظیم می‌کند. مقدار برچسب برابر با نام فضای نام است و نمی‌توانید آن را تغییر دهید.

اگر بخواهید با یک {{< glossary_tooltip text="انتخابگر" term_id="selector" >}} (selector) برچسب، فضای نام مشخصی را هدف بگیرید، این برچسب مفید است.

### kubernetes.io/limit-ranger

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/limit-ranger: "LimitRanger plugin set: cpu, memory request for container nginx; cpu, memory limit for container nginx"`

محل استفاده: Pod

کوبرنتیز به‌طور پیش‌فرض هیچ محدودیتی برای منابع تعیین نمی‌کند؛ بنابراین تا زمانی که محدودیت‌ها را صریحاً تعریف نکنید، کانتینر شما می‌تواند بدون محدودیت از CPU و حافظه استفاده کند. می‌توانید برای Podها مقدار پیش‌فرض درخواست یا محدودیت تعریف کنید. برای این کار، یک LimitRange در فضای نام مربوط ایجاد کنید. محدودیت‌های تعریف‌شده روی Podهایی اعمال می‌شوند که پس از تعریف LimitRange مستقر شوند. حاشیه‌نویسی `kubernetes.io/limit-ranger` نشان می‌دهد که مقادیر پیش‌فرض منابع برای Pod مشخص شده و با موفقیت اعمال شده‌اند. برای جزئیات بیشتر، دربارهٔ [LimitRangeها](/docs/concepts/policy/limit-range) بخوانید.

### kubernetes.io/config.hash

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/config.hash: "df7cc47f8477b6b1226d7d23a904867b"`

محل استفاده: Pod

وقتی kubelet یک Pod ایستا را بر اساس یک مانیفست مشخص ایجاد می‌کند، این حاشیه‌نویسی را به آن می‌افزاید. مقدار حاشیه‌نویسی همان UID مربوط به Pod است. توجه کنید که kubelet فیلد `.spec.nodeName` را نیز برابر با نام نود فعلی قرار می‌دهد، گویی Pod روی آن نود زمان‌بندی شده است.

### kubernetes.io/config.mirror

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/config.mirror: "df7cc47f8477b6b1226d7d23a904867b"`

محل استفاده: Pod

برای هر Pod ایستایی که kubelet روی یک نود ایجاد می‌کند، یک {{< glossary_tooltip text="Pod آینه‌ای" term_id="mirror-pod" >}} روی سرور API ساخته می‌شود. kubelet با افزودن یک حاشیه‌نویسی مشخص می‌کند که این Pod در واقع یک Pod آینه‌ای است. مقدار این حاشیه‌نویسی از حاشیه‌نویسی [`kubernetes.io/config.hash`](#kubernetes-io-config-hash) کپی می‌شود که همان UID مربوط به Pod است.

هنگام به‌روزرسانی Podی که این حاشیه‌نویسی را دارد، نمی‌توان حاشیه‌نویسی را تغییر داد یا حذف کرد. اگر Podی این حاشیه‌نویسی را نداشته باشد، نمی‌توان آن را هنگام به‌روزرسانی Pod اضافه کرد.

### kubernetes.io/config.source

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/config.source: "file"`

محل استفاده: Pod

این حاشیه‌نویسی را kubelet اضافه می‌کند تا مشخص شود Pod از کجا آمده است. برای Podهای ایستا، بسته به محل قرارگیری مانیفست Pod، مقدار این حاشیه‌نویسی می‌تواند `file` یا `http` باشد. برای Podی که روی سرور API ایجاد و سپس روی نود فعلی زمان‌بندی شده است، مقدار این حاشیه‌نویسی `api` است.

### kubernetes.io/config.seen

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/config.seen: "2023-10-27T04:04:56.011314488Z"`

محل استفاده: Pod

وقتی kubelet برای نخستین بار یک Pod را می‌بیند، ممکن است این حاشیه‌نویسی را با مقدار مُهر زمانی فعلی در قالب RFC3339 به آن Pod اضافه کند.

### addonmanager.kubernetes.io/mode

نوع: برچسب

مثال: `addonmanager.kubernetes.io/mode: "Reconcile"`

محل استفاده: همهٔ آبجکت‌ها

برای تعیین شیوهٔ مدیریت یک افزونهٔ کلاستر (add-on) می‌توانید از برچسب `addonmanager.kubernetes.io/mode` استفاده کنید. این برچسب می‌تواند یکی از سه مقدار `Reconcile`، `EnsureExists` یا `Ignore` را داشته باشد.

- مقدار `Reconcile`: منابع افزونه به‌صورت دوره‌ای با وضعیت مورد انتظار تطبیق داده می‌شوند. در صورت وجود هرگونه تفاوت، مدیر افزونه‌ها منابع را در صورت نیاز دوباره ایجاد، بازپیکربندی یا حذف می‌کند. اگر برچسبی مشخص نشده باشد، این حالت پیش‌فرض است.
- مقدار `EnsureExists`: فقط وجود منابع افزونه بررسی می‌شود و این منابع پس از ایجاد تغییر نمی‌کنند. اگر نمونه‌ای از منبع با آن نام وجود نداشته باشد، مدیر افزونه‌ها منبع را ایجاد یا دوباره ایجاد می‌کند.
- مقدار `Ignore`: منابع افزونه نادیده گرفته می‌شوند. این حالت برای افزونه‌هایی مفید است که با مدیر افزونه‌ها سازگار نیستند یا کنترل‌کنندهٔ دیگری آن‌ها را مدیریت می‌کند.

برای جزئیات بیشتر، [مدیر افزونه‌ها](https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/addon-manager/README.md) را ببینید.

### beta.kubernetes.io/arch (منسوخ‌شده)

نوع: برچسب

این برچسب منسوخ شده است. لطفاً به‌جای آن از [`kubernetes.io/arch`](#kubernetes-io-arch) استفاده کنید.

### beta.kubernetes.io/os (منسوخ‌شده)

نوع: برچسب

این برچسب منسوخ شده است. لطفاً به‌جای آن از [`kubernetes.io/os`](#kubernetes-io-os) استفاده کنید.

### kube-aggregator.kubernetes.io/automanaged {#kube-aggregator-kubernetesio-automanaged}

نوع: برچسب

مثال: `kube-aggregator.kubernetes.io/automanaged: "onstart"`

محل استفاده: APIService

مؤلفهٔ `kube-apiserver` این برچسب را روی هر آبجکت APIService که سرور API به‌طور خودکار ایجاد کرده باشد تنظیم می‌کند. این برچسب مشخص می‌کند که control plane باید آن APIService را چگونه مدیریت کند. نباید این برچسب را خودتان اضافه، تغییر یا حذف کنید.

{{< note >}}
اگر kube-apiserver هیچ API داخلی یا منبع سفارشی متناظر با گروه/نسخهٔ API یک APIService خودکارمدیریت‌شده نداشته باشد، آن آبجکت APIService را حذف می‌کند.
{{< /note >}}

دو مقدار ممکن وجود دارد:

- مقدار `onstart`: این APIService باید هنگام راه‌اندازی سرور API تطبیق داده شود و در زمان‌های دیگر تطبیق داده نمی‌شود.
- مقدار `true`: سرور API باید این APIService را به‌طور پیوسته تطبیق دهد.

### service.alpha.kubernetes.io/tolerate-unready-endpoints (منسوخ‌شده)

نوع: حاشیه‌نویسی

محل استفاده: Service

در گذشته از این حاشیه‌نویسی برای اعلام این موضوع استفاده می‌شد که کنترل‌کنندهٔ Endpoints باید برای Podهای آماده‌نشده نیز Endpoints ایجاد کند. از کوبرنتیز نسخهٔ 1.11 به بعد، API ترجیحی برای این قابلیت، فیلد `.publishNotReadyAddresses` در {{< glossary_tooltip term_id="service" >}} است. این حاشیه‌نویسی در کوبرنتیز {{< skew currentVersion >}} هیچ تأثیری ندارد.

### autoscaling.alpha.kubernetes.io/behavior (منسوخ‌شده) {#autoscaling-alpha-kubernetes-io-behavior}

نوع: حاشیه‌نویسی

محل استفاده: HorizontalPodAutoscaler

در نسخه‌های قدیمی‌تر کوبرنتیز، از این حاشیه‌نویسی برای پیکربندی رفتار مقیاس‌دهی یک HorizontalPodAutoscaler (HPA) استفاده می‌شد. با این حاشیه‌نویسی می‌شد نحوهٔ افزایش یا کاهش مقیاس Podها را در HPA، از جمله پنجره‌های پایدارسازی و سیاست‌های مقیاس‌دهی، مشخص کرد. تنظیم این حاشیه‌نویسی در هیچ‌یک از نسخه‌های پشتیبانی‌شدهٔ کوبرنتیز تأثیری ندارد.

### kubernetes.io/hostname {#kubernetesiohostname}

نوع: برچسب

مثال: `kubernetes.io/hostname: "ip-172-20-114-199.ec2.internal"`

محل استفاده: Node

مقدار این برچسب را kubelet برابر با نام میزبان نود تنظیم می‌کند. توجه کنید که با ارسال فلگ `--hostname-override` به `kubelet` می‌توان نام میزبان را به مقداری غیر از نام میزبان «واقعی» تغییر داد.

این برچسب به‌عنوان بخشی از سلسله‌مراتب توپولوژی نیز استفاده می‌شود. برای اطلاعات بیشتر، [topology.kubernetes.io/zone](#topologykubernetesiozone) را ببینید.

### kubernetes.io/change-cause {#change-cause}

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/change-cause: "kubectl edit --record deployment foo"`

محل استفاده: همهٔ آبجکت‌ها

این حاشیه‌نویسی بهترین حدس دربارهٔ علت تغییر یک مورد را نشان می‌دهد.

این حاشیه‌نویسی زمانی مقدار می‌گیرد که `--record` را به دستوری از `kubectl` اضافه کنید که ممکن است آبجکتی را تغییر دهد.

### kubernetes.io/description {#description}

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/description: "Description of K8s object."`

محل استفاده: همهٔ آبجکت‌ها

از این حاشیه‌نویسی برای توصیف رفتار خاص آبجکت موردنظر استفاده می‌شود.

### kubernetes.io/enforce-mountable-secrets (منسوخ‌شده) {#enforce-mountable-secrets}

نوع: حاشیه‌نویسی (annotation)

مثال: `kubernetes.io/enforce-mountable-secrets: "true"`

محل استفاده: ServiceAccount

{{< note >}}
حاشیه‌نویسی `kubernetes.io/enforce-mountable-secrets` از نسخهٔ v1.32 کوبرنتیز منسوخ شده است. برای جداسازی دسترسی به Secretهای مانت‌شده، از فضاهای نام (namespace) جداگانه استفاده کنید.
{{< /note >}}

مقدار این حاشیه‌نویسی باید **true** باشد تا اعمال شود. اگر مقدار آن را "true" قرار دهید، کوبرنتیز قوانین زیر را برای Podهایی که با این ServiceAccount اجرا می‌شوند اعمال می‌کند:

1. نام Secretهایی که به‌صورت حجم (volume) مانت می‌شوند باید در فیلد `secrets` مربوط به ServiceAccount فهرست شده باشد.
1. نام Secretهایی که در `envFrom` کانتینرها (از جمله کانتینرهای sidecar و init) به آن‌ها ارجاع داده می‌شود نیز باید در فیلد secrets مربوط به ServiceAccount فهرست شده باشد.
   اگر هر یک از کانتینرهای یک Pod به Secretای ارجاع دهد که در فیلد `secrets` مربوط به ServiceAccount فهرست نشده است (حتی اگر این ارجاع با `optional` مشخص شده باشد)، آن Pod راه‌اندازی نمی‌شود و خطایی تولید می‌شود که ارجاع نامعتبر به Secret را نشان می‌دهد.
1. Secretهایی که در `imagePullSecrets` یک Pod به آن‌ها ارجاع داده می‌شود باید در فیلد `imagePullSecrets` مربوط به ServiceAccount نیز وجود داشته باشند؛ در غیر این صورت، آن Pod راه‌اندازی نمی‌شود و خطایی تولید می‌شود که ارجاع نامعتبر به Secret دریافت ایمیج را نشان می‌دهد.

این قوانین هنگام ایجاد یا به‌روزرسانی یک Pod بررسی می‌شوند. اگر Pod از این قوانین پیروی نکند، راه‌اندازی نمی‌شود و پیام خطایی نمایش داده خواهد شد.
اگر Pod در حال اجرا باشد و مقدار حاشیه‌نویسی `kubernetes.io/enforce-mountable-secrets` را به true تغییر دهید، یا ServiceAccount مرتبط را طوری ویرایش کنید که ارجاع به Secret مورد استفادهٔ آن Pod حذف شود، Pod همچنان به اجرای خود ادامه می‌دهد.

### node.alpha.kubernetes.io/ttl (منسوخ‌شده)

نوع: برچسب

مثال: `node.alpha.kubernetes.io/ttl: "0"`

محل استفاده: Node

برخی ابزارها (مانند minikube) در گذشته از این برچسب برای تعیین مقدار زمان حیات (time-to-live) نودها استفاده می‌کردند. این برچسب منسوخ شده است و نباید در استقرارهای جدید از آن استفاده کرد.

{{< note >}}
این برچسب منسوخ شده است و در نسخه‌های فعلی کوبرنتیز هیچ تأثیری ندارد. با این حال، ممکن است ابزارهای قدیمی‌تر برای حفظ سازگاری با نسخه‌های پیشین همچنان آن را تنظیم کنند.
{{< /note >}}

### node.kubernetes.io/exclude-from-external-load-balancers

نوع: برچسب

مثال: `node.kubernetes.io/exclude-from-external-load-balancers`

محل استفاده: Node

می‌توانید با افزودن برچسب به نودهای کارگر مشخص، آن‌ها را از فهرست سرورهای بک‌اندی که متعادل‌کننده‌های بار خارجی استفاده می‌کنند کنار بگذارید.
با دستور زیر می‌توانید یک نود کارگر را از فهرست سرورهای بک‌اند در یک مجموعهٔ بک‌اند حذف کنید:

```shell
kubectl label nodes <node-name> node.kubernetes.io/exclude-from-external-load-balancers=true
```

### controller.kubernetes.io/pod-deletion-cost {#pod-deletion-cost}

نوع: حاشیه‌نویسی

مثال: `controller.kubernetes.io/pod-deletion-cost: "10"`

محل استفاده: Pod

از این حاشیه‌نویسی برای تعیین [هزینهٔ حذف Pod](/docs/concepts/workloads/controllers/replicaset/#pod-deletion-cost) استفاده می‌شود و کاربران با آن می‌توانند بر ترتیب کاهش مقیاس ReplicaSet اثر بگذارند.
مقدار این حاشیه‌نویسی به نوع `int32` تجزیه می‌شود.

### cluster-autoscaler.kubernetes.io/enable-ds-eviction

نوع: حاشیه‌نویسی

مثال: `cluster-autoscaler.kubernetes.io/enable-ds-eviction: "true"`

محل استفاده: Pod

این حاشیه‌نویسی تعیین می‌کند که آیا ClusterAutoscaler می‌تواند یک Pod متعلق به DaemonSet را بیرون کند یا نه.
این حاشیه‌نویسی باید برای Podهای DaemonSet در مانیفست DaemonSet مشخص شود.
اگر مقدار آن `"true"` باشد، ClusterAutoscaler مجاز است Pod متعلق به DaemonSet را بیرون کند، حتی اگر قوانین دیگر در حالت عادی مانع این کار شوند.
برای جلوگیری از بیرون‌راندن Podهای مهم DaemonSet توسط ClusterAutoscaler، می‌توانید مقدار این حاشیه‌نویسی را برای آن‌ها `"false"` قرار دهید.
اگر این حاشیه‌نویسی تنظیم نشده باشد، ClusterAutoscaler از رفتار کلی خود پیروی می‌کند؛ یعنی DaemonSetها را بر اساس پیکربندی خود بیرون می‌کند.

{{< note >}}
این حاشیه‌نویسی فقط بر Podهای DaemonSet اثر می‌گذارد.
{{< /note >}}

### kubernetes.io/ingress-bandwidth

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/ingress-bandwidth: 10M`

محل استفاده: Pod

می‌توانید شکل‌دهی ترافیک (traffic shaping) مبتنی بر کیفیت سرویس را روی یک Pod اعمال کنید و پهنای باند در دسترس آن را عملاً محدود سازید. ترافیک ورودی به Pod با شکل‌دهی بسته‌های صف‌شده مدیریت می‌شود تا داده‌ها به‌طور مؤثر پردازش شوند. برای محدود کردن پهنای باند یک Pod، فایل JSON تعریف آبجکت را بنویسید و سرعت ترافیک داده را با حاشیه‌نویسی `kubernetes.io/ingress-bandwidth` مشخص کنید. واحد نرخ ورودی، بیت بر ثانیه است و به‌صورت یک [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/) مشخص می‌شود.
برای مثال، `10M` به معنای ۱۰ مگابیت بر ثانیه است.

{{< note >}}
حاشیه‌نویسی شکل‌دهی ترافیک ورودی یک قابلیت آزمایشی است.
برای فعال‌سازی پشتیبانی از شکل‌دهی ترافیک، باید افزونهٔ `bandwidth` را به فایل پیکربندی CNI خود (به‌طور پیش‌فرض `/etc/cni/net.d`) اضافه کنید و مطمئن شوید که فایل اجرایی آن در پوشهٔ bin مربوط به CNI (به‌طور پیش‌فرض `/opt/cni/bin`) قرار دارد.
{{< /note >}}

### kubernetes.io/egress-bandwidth

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/egress-bandwidth: 10M`

محل استفاده: Pod

ترافیک خروجی از Pod با روش پلیسینگ (policing) مدیریت می‌شود؛ در این روش، بسته‌هایی که از نرخ پیکربندی‌شده فراتر بروند به‌سادگی دور ریخته می‌شوند. محدودیت‌هایی که روی یک Pod اعمال می‌کنید بر پهنای باند Podهای دیگر اثری ندارد.
برای محدود کردن پهنای باند یک Pod، فایل JSON تعریف آبجکت را بنویسید و سرعت ترافیک داده را با حاشیه‌نویسی `kubernetes.io/egress-bandwidth` مشخص کنید. واحد نرخ خروجی، بیت بر ثانیه است و به‌صورت یک [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/) مشخص می‌شود.
برای مثال، `10M` به معنای ۱۰ مگابیت بر ثانیه است.

{{< note >}}
حاشیه‌نویسی شکل‌دهی ترافیک خروجی یک قابلیت آزمایشی است.
برای فعال‌سازی پشتیبانی از شکل‌دهی ترافیک، باید افزونهٔ `bandwidth` را به فایل پیکربندی CNI خود (به‌طور پیش‌فرض `/etc/cni/net.d`) اضافه کنید و مطمئن شوید که فایل اجرایی آن در پوشهٔ bin مربوط به CNI (به‌طور پیش‌فرض `/opt/cni/bin`) قرار دارد.
{{< /note >}}

### beta.kubernetes.io/instance-type (منسوخ‌شده)

نوع: برچسب

{{< note >}}
از نسخهٔ v1.17، این برچسب منسوخ شده و [node.kubernetes.io/instance-type](#nodekubernetesioinstance-type) جایگزین آن شده است.
{{< /note >}}

### node.kubernetes.io/instance-type {#nodekubernetesioinstance-type}

نوع: برچسب

مثال: `node.kubernetes.io/instance-type: "m3.medium"`

محل استفاده: Node

مقدار این برچسب را kubelet بر اساس نوع نمونه‌ای که ارائه‌دهندهٔ ابر تعریف کرده است تنظیم می‌کند.
این برچسب فقط در صورت استفاده از ارائه‌دهندهٔ ابر تنظیم می‌شود. این تنظیم زمانی مفید است که بخواهید بارهای کاری مشخصی را روی انواع مشخصی از نمونه‌ها اجرا کنید، اما معمولاً بهتر است زمان‌بندی مبتنی بر منابع را به زمان‌بند کوبرنتیز بسپارید.
بهتر است زمان‌بندی را بر پایهٔ ویژگی‌ها انجام دهید، نه بر پایهٔ نوع نمونه (برای مثال، به‌جای الزام به `g2.2xlarge`، وجود GPU را الزامی کنید).

### failure-domain.beta.kubernetes.io/region (منسوخ‌شده) {#failure-domainbetakubernetesioregion}

نوع: برچسب

{{< note >}}
از نسخهٔ v1.17، این برچسب منسوخ شده و [topology.kubernetes.io/region](#topologykubernetesioregion) جایگزین آن شده است.
{{< /note >}}

### failure-domain.beta.kubernetes.io/zone (منسوخ‌شده) {#failure-domainbetakubernetesiozone}

نوع: برچسب

{{< note >}}
از نسخهٔ v1.17، این برچسب منسوخ شده و [topology.kubernetes.io/zone](#topologykubernetesiozone) جایگزین آن شده است.
{{< /note >}}

### pv.kubernetes.io/bind-completed {#pv-kubernetesiobind-completed}

نوع: حاشیه‌نویسی

مثال: `pv.kubernetes.io/bind-completed: "yes"`

محل استفاده: PersistentVolumeClaim

وجود این حاشیه‌نویسی روی یک PersistentVolumeClaim (PVC) نشان می‌دهد که چرخهٔ حیات PVC از مرحلهٔ راه‌اندازی اولیهٔ اتصال گذشته است. این اطلاعات، در صورت وجود، نحوهٔ تفسیر وضعیت آبجکت‌های PVC را در control plane تغییر می‌دهد.
مقدار این حاشیه‌نویسی برای کوبرنتیز اهمیتی ندارد.

### pv.kubernetes.io/bound-by-controller {#pv-kubernetesioboundby-controller}

نوع: حاشیه‌نویسی

مثال: `pv.kubernetes.io/bound-by-controller: "yes"`

محل استفاده: PersistentVolume، PersistentVolumeClaim

وجود این حاشیه‌نویسی روی یک PersistentVolume یا PersistentVolumeClaim نشان می‌دهد که اتصال ذخیره‌سازی (PersistentVolume → PersistentVolumeClaim یا PersistentVolumeClaim → PersistentVolume) را {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} برقرار کرده است.
اگر این حاشیه‌نویسی تنظیم نشده باشد و اتصال ذخیره‌سازی وجود داشته باشد، نبود آن به این معناست که اتصال به‌صورت دستی برقرار شده است.
مقدار این حاشیه‌نویسی اهمیتی ندارد.

### pv.kubernetes.io/provisioned-by {#pv-kubernetesiodynamically-provisioned}

نوع: حاشیه‌نویسی

مثال: `pv.kubernetes.io/provisioned-by: "kubernetes.io/rbd"`

محل استفاده: PersistentVolume

این حاشیه‌نویسی به PersistentVolume (PV) که کوبرنتیز آن را به‌صورت پویا تأمین کرده است افزوده می‌شود.
مقدار آن نام افزونهٔ حجمی است که این حجم را ایجاد کرده است. این حاشیه‌نویسی هم برای کاربران مفید است (تا منشأ PV را نشان دهد) و هم برای کوبرنتیز (تا PVهای تأمین‌شدهٔ پویا را در تصمیم‌گیری‌های خود تشخیص دهد).

### pv.kubernetes.io/migrated-to {#pv-kubernetesio-migratedto}

نوع: حاشیه‌نویسی

مثال: `pv.kubernetes.io/migrated-to: pd.csi.storage.gke.io`

محل استفاده: PersistentVolume، PersistentVolumeClaim

این حاشیه‌نویسی به PersistentVolume (PV) و PersistentVolumeClaim (PVC) افزوده می‌شود که قرار است درایور CSI متناظر آن‌ها، از طریق feature gate با نام `CSIMigration`، آن‌ها را به‌صورت پویا تأمین یا حذف کند.
هنگامی که این حاشیه‌نویسی تنظیم شده باشد، مؤلفه‌های کوبرنتیز کنار می‌کشند و `external-provisioner` عملیات لازم را روی این آبجکت‌ها انجام می‌دهد.

### statefulset.kubernetes.io/pod-name {#statefulsetkubernetesiopod-name}

نوع: برچسب

مثال: `statefulset.kubernetes.io/pod-name: "mystatefulset-7"`

محل استفاده: Pod

هنگامی که کنترل‌کنندهٔ StatefulSet یک Pod برای StatefulSet ایجاد می‌کند، control plane این برچسب را روی آن Pod تنظیم می‌کند. مقدار برچسب، نام Pod در حال ایجاد است.

برای جزئیات بیشتر، بخش [برچسب نام Pod](/docs/concepts/workloads/controllers/statefulset/#pod-name-label) را در مبحث StatefulSet ببینید.

### scheduler.alpha.kubernetes.io/node-selector {#schedulerkubernetesnode-selector}

نوع: حاشیه‌نویسی

مثال: `scheduler.alpha.kubernetes.io/node-selector: "name-of-node-selector"`

محل استفاده: Namespace

کنترل‌کنندهٔ پذیرش [PodNodeSelector](/docs/reference/access-authn-authz/admission-controllers/#podnodeselector) از این کلید حاشیه‌نویسی برای اختصاص انتخابگرهای (selector) نود به Podهای موجود در فضاهای نام استفاده می‌کند.

### topology.kubernetes.io/region {#topologykubernetesioregion}

نوع: برچسب

مثال: `topology.kubernetes.io/region: "us-east-1"`

محل استفاده: Node، PersistentVolume

به [topology.kubernetes.io/zone](#topologykubernetesiozone) مراجعه کنید.

### topology.kubernetes.io/zone {#topologykubernetesiozone}

نوع: برچسب

مثال: `topology.kubernetes.io/zone: "us-east-1c"`

محل استفاده: Node، PersistentVolume

**روی Node**: مؤلفهٔ `kubelet` یا `cloud-controller-manager` خارجی این برچسب را با اطلاعات دریافتی از ارائه‌دهندهٔ ابر پر می‌کند. این برچسب فقط در صورت استفاده از ارائه‌دهندهٔ ابر تنظیم می‌شود. با این حال، اگر با توپولوژی شما سازگار باشد، می‌توانید آن را روی نودها تنظیم کنید.

**روی PersistentVolume**: تأمین‌کننده‌های حجم آگاه از توپولوژی، محدودیت‌های وابستگی نود (node affinity) را به‌طور خودکار روی `PersistentVolume` تنظیم می‌کنند.

هر ناحیه (zone) یک دامنهٔ خرابی منطقی را نشان می‌دهد. کلاسترهای کوبرنتیز معمولاً برای افزایش دسترس‌پذیری در چند ناحیه گسترده می‌شوند.
تعریف دقیق ناحیه به پیاده‌سازی زیرساخت واگذار شده است، اما از ویژگی‌های رایج یک ناحیه می‌توان به تأخیر بسیار کم شبکه در داخل ناحیه، رایگان بودن ترافیک شبکه در داخل ناحیه و مستقل بودن خرابی آن از نواحی دیگر اشاره کرد.
برای مثال، نودهای درون یک ناحیه ممکن است از یک سوئیچ شبکهٔ مشترک استفاده کنند، اما نودهای نواحی مختلف نباید چنین اشتراکی داشته باشند.

هر منطقه (region) دامنهٔ بزرگ‌تری است که از یک یا چند ناحیه تشکیل می‌شود.
گسترش کلاسترهای کوبرنتیز در چند منطقه رایج نیست.
تعریف دقیق ناحیه یا منطقه به پیاده‌سازی زیرساخت واگذار شده است، اما از ویژگی‌های رایج مناطق می‌توان به تأخیر بیشتر شبکه میان مناطق نسبت به داخل آن‌ها، غیرصفر بودن هزینهٔ ترافیک شبکه میان مناطق و مستقل بودن خرابی از نواحی یا مناطق دیگر اشاره کرد.
برای مثال، نودهای درون یک منطقه ممکن است زیرساخت برق مشترکی (مانند UPS یا ژنراتور) داشته باشند، اما نودهای مناطق مختلف معمولاً چنین اشتراکی ندارند.

کوبرنتیز چند فرض دربارهٔ ساختار نواحی و مناطق دارد:

1. مناطق و نواحی ساختار سلسله‌مراتبی دارند: نواحی زیرمجموعه‌های سرهٔ مناطق هستند و هیچ ناحیه‌ای نمی‌تواند در ۲ منطقه قرار داشته باشد.
2. نام نواحی در میان مناطق یکتاست؛ برای مثال، منطقهٔ "africa-east-1" ممکن است از نواحی "africa-east-1a" و "africa-east-1b" تشکیل شده باشد.

می‌توان با اطمینان فرض کرد که برچسب‌های توپولوژی تغییر نمی‌کنند.
با اینکه برچسب‌ها از نظر فنی تغییرپذیرند، مصرف‌کنندگان آن‌ها می‌توانند فرض کنند که یک نود بدون حذف و ایجاد مجدد، میان نواحی جابه‌جا نمی‌شود.

کوبرنتیز می‌تواند از این اطلاعات به روش‌های گوناگون استفاده کند.
برای مثال، زمان‌بند به‌طور خودکار می‌کوشد Podهای یک ReplicaSet را در میان نودهای یک کلاستر تک‌ناحیه‌ای توزیع کند تا تأثیر خرابی نودها کاهش یابد (به [kubernetes.io/hostname](#kubernetesiohostname) مراجعه کنید).
در کلاسترهای چندناحیه‌ای، این رفتار توزیع در سطح نواحی نیز اعمال می‌شود تا تأثیر خرابی نواحی کاهش یابد.
این کار با _SelectorSpreadPriority_ انجام می‌شود.

جای‌گذاری با _SelectorSpreadPriority_ به‌صورت بهترین تلاش انجام می‌شود. اگر نواحی کلاستر شما ناهمگن باشند (برای مثال، تعداد یا نوع نودها یا نیازمندی‌های منابع Podها متفاوت باشد)، این جای‌گذاری ممکن است مانع توزیع یکسان Podها در میان نواحی شود.
در صورت تمایل، می‌توانید با استفاده از نواحی همگن (با تعداد و نوع یکسان نودها) احتمال توزیع نابرابر را کاهش دهید.

زمان‌بند (از طریق گزارهٔ _VolumeZonePredicate_) همچنین تضمین می‌کند که Podهای درخواست‌کنندهٔ یک حجم مشخص، فقط در همان ناحیه‌ای قرار بگیرند که آن حجم در آن است.
حجم‌ها را نمی‌توان میان نواحی مختلف متصل کرد.

اگر `PersistentVolumeLabel` از برچسب‌گذاری خودکار PersistentVolumeهای شما پشتیبانی نمی‌کند، بهتر است برچسب‌ها را به‌صورت دستی اضافه کنید (یا پشتیبانی از `PersistentVolumeLabel` را بیفزایید).
با `PersistentVolumeLabel`، زمان‌بند از مانت شدن حجم‌های ناحیه‌ای دیگر در Podها جلوگیری می‌کند.
اگر زیرساخت شما چنین محدودیتی ندارد، اصلاً نیازی به افزودن برچسب‌های ناحیه به حجم‌ها نیست.

### volume.alpha.kubernetes.io/node-affinity (منسوخ‌شده) {#volume-alpha-kubernetes-io-node-affinity}

نوع: حاشیه‌نویسی

محل استفاده: PersistentVolume

این حاشیه‌نویسی قوانین وابستگی نود را برای یک PersistentVolume به‌صورت آبجکت `NodeAffinity` سریال‌شده در قالب JSON ذخیره می‌کرد. زمان‌بند با این قوانین مشخص می‌کرد که کدام نودها به حجم دسترسی داشته باشند.

این حاشیه‌نویسی از نسخهٔ v1.10 کوبرنتیز منسوخ شده است. به‌جای آن از [فیلد `nodeAffinity`](/docs/concepts/storage/persistent-volumes/#node-affinity) در spec مربوط به PersistentVolume استفاده کنید.

### volume.beta.kubernetes.io/storage-provisioner (منسوخ‌شده)

نوع: حاشیه‌نویسی

مثال: `volume.beta.kubernetes.io/storage-provisioner: "k8s.io/minikube-hostpath"`

محل استفاده: PersistentVolumeClaim

این حاشیه‌نویسی از نسخهٔ v1.23 منسوخ شده است.
به [volume.kubernetes.io/storage-provisioner](#volume-kubernetes-io-storage-provisioner) مراجعه کنید.

### volume.beta.kubernetes.io/storage-class (منسوخ‌شده)

نوع: حاشیه‌نویسی

مثال: `volume.beta.kubernetes.io/storage-class: "example-class"`

محل استفاده: PersistentVolume، PersistentVolumeClaim

از این حاشیه‌نویسی می‌توان برای مشخص کردن نام [StorageClass](/docs/concepts/storage/storage-classes/) در PersistentVolume (PV) یا PersistentVolumeClaim (PVC) استفاده کرد.
اگر هم ویژگی `storageClassName` و هم حاشیه‌نویسی `volume.beta.kubernetes.io/storage-class` مشخص شده باشند، حاشیه‌نویسی `volume.beta.kubernetes.io/storage-class` بر ویژگی `storageClassName` اولویت دارد.

این حاشیه‌نویسی منسوخ شده است. به‌جای آن، [فیلد `storageClassName`](/docs/concepts/storage/persistent-volumes/#class) را برای PersistentVolumeClaim یا PersistentVolume تنظیم کنید.

### volume.beta.kubernetes.io/mount-options (منسوخ‌شده) {#mount-options}

نوع: حاشیه‌نویسی

مثال: `volume.beta.kubernetes.io/mount-options: "ro,soft"`

محل استفاده: PersistentVolume

مدیر کوبرنتیز می‌تواند برای زمان مانت شدن یک PersistentVolume روی نود، [گزینه‌های مانت](/docs/concepts/storage/persistent-volumes/#mount-options) بیشتری مشخص کند.

### volume.kubernetes.io/storage-provisioner  {#volume-kubernetes-io-storage-provisioner}

نوع: حاشیه‌نویسی

محل استفاده: PersistentVolumeClaim

این حاشیه‌نویسی به PVCای افزوده می‌شود که قرار است به‌صورت پویا تأمین شود.
مقدار آن نام افزونهٔ حجمی است که باید حجم این PVC را تأمین کند.

### volume.kubernetes.io/selected-node

نوع: حاشیه‌نویسی

محل استفاده: PersistentVolumeClaim

این حاشیه‌نویسی به PVCای افزوده می‌شود که تأمین پویای آن را زمان‌بند آغاز کرده است. مقدار آن نام نود انتخاب‌شده است.

### volumes.kubernetes.io/controller-managed-attach-detach

نوع: حاشیه‌نویسی

محل استفاده: Node

اگر نودی حاشیه‌نویسی `volumes.kubernetes.io/controller-managed-attach-detach` را داشته باشد، عملیات اتصال و جداسازی ذخیره‌سازی آن را {{< glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller" >}} _اتصال/جداسازی حجم_ مدیریت می‌کند.

مقدار این حاشیه‌نویسی اهمیتی ندارد.

### node.kubernetes.io/windows-build {#nodekubernetesiowindows-build}

نوع: برچسب

مثال: `node.kubernetes.io/windows-build: "10.0.17763"`

محل استفاده: Node

هنگامی که kubelet روی Microsoft Windows اجرا می‌شود، Node خود را به‌طور خودکار برچسب‌گذاری می‌کند تا نسخهٔ Windows Server در حال استفاده را ثبت کند.

مقدار این برچسب در قالب "MajorVersion.MinorVersion.BuildNumber" است.

### storage.alpha.kubernetes.io/migrated-plugins {#storagealphakubernetesiomigrated-plugins}

نوع: حاشیه‌نویسی (annotation)

نمونه: `storage.alpha.kubernetes.io/migrated-plugins: "kubernetes.io/cinder"`

محل استفاده: CSINode (یک API افزونه)

این حاشیه‌نویسی به‌طور خودکار به آبجکت CSINode متناظر با نودی که CSIDriver روی آن نصب می‌شود، اضافه می‌شود. این حاشیه‌نویسی نام افزونهٔ درون‌درختی (in-tree) مهاجرت‌داده‌شده را نشان می‌دهد. مقدار آن به نوع ذخیره‌سازی درون‌درختی ارائه‌دهندهٔ ابری کلاستر شما بستگی دارد.

برای مثال، اگر نوع ذخیره‌سازی درون‌درختی ارائه‌دهندهٔ ابری `CSIMigrationvSphere` باشد، نمونهٔ CSINode مربوط به نود باید با این مقدار به‌روزرسانی شود:
`storage.alpha.kubernetes.io/migrated-plugins: "kubernetes.io/vsphere-volume"`

### service.kubernetes.io/headless {#servicekubernetesioheadless}

نوع: برچسب

نمونه: `service.kubernetes.io/headless: ""`

محل استفاده: EndpointSlice، Endpoints

هنگامی که {{< glossary_tooltip term_id="service" >}} مالک از نوع headless باشد، {{< glossary_tooltip term_id="control-plane" text="control plane" >}} این {{< glossary_tooltip term_id="label" text="برچسب" >}} را به آبجکت‌های EndpointSlice و Endpoints اضافه می‌کند تا به پروکسی سرویس اعلام کند که می‌تواند این endpointها را نادیده بگیرد. برای آشنایی بیشتر، [سرویس‌های Headless](/docs/concepts/services-networking/service/#headless-services) را بخوانید.

### service.kubernetes.io/topology-aware-hints (منسوخ‌شده) {#servicekubernetesiotopology-aware-hints}

نمونه: `service.kubernetes.io/topology-aware-hints: "Auto"`

محل استفاده: Service

این حاشیه‌نویسی نام مستعار منسوخ‌شدهٔ حاشیه‌نویسی [`service.kubernetes.io/topology-mode`](#service-kubernetes-io-topology-mode) است و همان کارکرد را دارد.

### service.kubernetes.io/topology-mode

نوع: حاشیه‌نویسی

نمونه: `service.kubernetes.io/topology-mode: Auto`

محل استفاده: Service

با این حاشیه‌نویسی می‌توان نحوهٔ برخورد Serviceها با توپولوژی شبکه را تعریف کرد؛ برای مثال، می‌توانید یک Service را طوری پیکربندی کنید که کوبرنتیز ترجیح دهد ترافیک بین کلاینت و سرور در یک ناحیهٔ توپولوژی واحد باقی بماند. این کار در برخی موارد به کاهش هزینه‌ها یا بهبود کارایی شبکه کمک می‌کند.

برای جزئیات بیشتر، [مسیریابی آگاه از توپولوژی](/docs/concepts/services-networking/topology-aware-routing/) را ببینید.

### kubernetes.io/service-name {#kubernetesioservice-name}

نوع: برچسب

نمونه: `kubernetes.io/service-name: "my-website"`

محل استفاده: EndpointSlice

کوبرنتیز با استفاده از این برچسب، [EndpointSlice‌ها](/docs/concepts/services-networking/endpoint-slices/) را به [Service‌ها](/docs/concepts/services-networking/service/) مرتبط می‌کند.

این برچسب {{< glossary_tooltip term_id="name" text="نام">}} Serviceای را که EndpointSlice پشتیبان آن است، ثبت می‌کند. مقدار این برچسب باید در همهٔ EndpointSlice‌ها برابر با نام Service مرتبط با آن‌ها باشد.

### kubernetes.io/service-account.name

نوع: حاشیه‌نویسی

نمونه: `kubernetes.io/service-account.name: "sa-name"`

محل استفاده: Secret

این حاشیه‌نویسی {{< glossary_tooltip term_id="name" text="نام">}} ServiceAccountای را ثبت می‌کند که توکن ذخیره‌شده در Secret از نوع `kubernetes.io/service-account-token` نمایندهٔ آن است.

### kubernetes.io/service-account.uid

نوع: حاشیه‌نویسی

نمونه: `kubernetes.io/service-account.uid: da68f9c6-9d26-11e7-b84e-002dc52800da`

محل استفاده: Secret

این حاشیه‌نویسی {{< glossary_tooltip term_id="uid" text="شناسهٔ یکتای" >}} ServiceAccountای را ثبت می‌کند که توکن ذخیره‌شده در Secret از نوع `kubernetes.io/service-account-token` نمایندهٔ آن است.

### kubernetes.io/legacy-token-last-used

نوع: برچسب

نمونه: `kubernetes.io/legacy-token-last-used: 2022-10-24`

محل استفاده: Secret

مؤلفهٔ control plane این برچسب را فقط به Secret‌هایی از نوع `kubernetes.io/service-account-token` اضافه می‌کند. مقدار این برچسب تاریخ آخرین باری را ثبت می‌کند که control plane درخواستی را دیده است که کلاینت آن با این توکن حساب سرویس احراز هویت شده باشد. این تاریخ در قالب ISO 8601 و در منطقهٔ زمانی UTC است.

اگر آخرین استفاده از یک توکن قدیمی پیش از افزوده‌شدن این قابلیت به کلاستر (معرفی‌شده در Kubernetes v1.26) باشد، این برچسب تنظیم نمی‌شود.

### kubernetes.io/legacy-token-invalid-since

نوع: برچسب

نمونه: `kubernetes.io/legacy-token-invalid-since: 2023-10-27`

محل استفاده: Secret

مؤلفهٔ control plane این برچسب را به‌طور خودکار به Secret‌های خودکارساخته‌شده از نوع `kubernetes.io/service-account-token` اضافه می‌کند. این برچسب، توکن مبتنی بر Secret را برای احراز هویت نامعتبر علامت‌گذاری می‌کند. مقدار این برچسب تاریخی را ثبت می‌کند که control plane تشخیص می‌دهد Secret خودکارساخته‌شده طی مدت مشخصی (به‌طور پیش‌فرض یک سال) استفاده نشده است. این تاریخ در قالب ISO 8601 و در منطقهٔ زمانی UTC است.

### endpoints.kubernetes.io/managed-by (منسوخ‌شده) {#endpoints-kubernetes-io-managed-by}

نوع: برچسب

نمونه: `endpoints.kubernetes.io/managed-by: endpoint-controller`

محل استفاده: Endpoints

از این برچسب به‌صورت داخلی برای علامت‌گذاری آبجکت‌های Endpoints ایجادشده به دست کوبرنتیز استفاده می‌شود تا از Endpoints‌هایی که کاربران یا کنترل‌کننده‌های خارجی ایجاد کرده‌اند، متمایز شوند.

{{< note >}}
رابط [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/) منسوخ شده و باید به‌جای آن از [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) استفاده کرد.
{{< /note >}}

### endpointslice.kubernetes.io/managed-by {#endpointslicekubernetesiomanaged-by}

نوع: برچسب

نمونه: `endpointslice.kubernetes.io/managed-by: endpointslice-controller.k8s.io`

محل استفاده: EndpointSlice‌ها

این برچسب کنترل‌کننده یا موجودیتی را که EndpointSlice را مدیریت می‌کند، مشخص می‌کند. هدف از این برچسب آن است که بتوان آبجکت‌های مختلف EndpointSlice را در یک کلاستر با کنترل‌کننده‌ها یا موجودیت‌های گوناگون مدیریت کرد. مقدار `endpointslice-controller.k8s.io` نشان می‌دهد که کوبرنتیز این آبجکت EndpointSlice را به‌طور خودکار برای یک Service دارای {{< glossary_tooltip text="انتخابگر" term_id="selector" >}} ایجاد کرده است.

### endpointslice.kubernetes.io/skip-mirror {#endpointslicekubernetesioskip-mirror}

نوع: برچسب

نمونه: `endpointslice.kubernetes.io/skip-mirror: "true"`

محل استفاده: Endpoints

با تنظیم این برچسب روی `"true"` در یک منبع Endpoints، مشخص می‌شود که کنترل‌کنندهٔ EndpointSliceMirroring نباید این منبع را با EndpointSlice‌ها بازتاب دهد.

### service.kubernetes.io/service-proxy-name {#servicekubernetesioservice-proxy-name}

نوع: برچسب

نمونه: `service.kubernetes.io/service-proxy-name: "foo-bar"`

محل استفاده: Service

با تعیین مقداری برای این برچسب، به kube-proxy اعلام می‌شود که این Service را در پروکسی‌کردن نادیده بگیرد. به این ترتیب می‌توان برای این Service از پیاده‌سازی‌های جایگزین پروکسی استفاده کرد (برای مثال، اجرای یک DaemonSet که nftables را به شیوهٔ خود مدیریت می‌کند). با استفاده از این فیلد، چند پیاده‌سازی جایگزین پروکسی می‌توانند هم‌زمان فعال باشند؛ برای مثال، هر پیاده‌سازی جایگزین مقدار یکتای خود را داشته باشد و مسئول Service‌های مربوط به خود باشد.

### experimental.windows.kubernetes.io/isolation-type (منسوخ‌شده) {#experimental-windows-kubernetes-io-isolation-type}

نوع: حاشیه‌نویسی

نمونه: `experimental.windows.kubernetes.io/isolation-type: "hyperv"`

محل استفاده: Pod

از این حاشیه‌نویسی برای اجرای کانتینرهای ویندوز با جداسازی Hyper-V استفاده می‌شود.

{{< note >}}
این حاشیه‌نویسی از نسخهٔ v1.20 منسوخ شده است. پشتیبانی آزمایشی از Hyper-V نیز در نسخهٔ 1.21 حذف شد.
{{< /note >}}

### gateway.networking.k8s.io/generator

نوع: حاشیه‌نویسی

نمونه: `gateway.networking.k8s.io/generator: "ingress2gateway"`

محل استفاده: Gateway، HTTPRoute و سایر منابع Gateway API

ابزارهایی که منابع [Gateway API](/docs/concepts/services-networking/gateway/) را به‌طور خودکار تولید می‌کنند، این حاشیه‌نویسی را اضافه می‌کنند. مقدار آن ابزار سازندهٔ منبع را مشخص می‌کند (برای مثال، `ingress2gateway`). این حاشیه‌نویسی صرفاً جنبهٔ اطلاع‌رسانی دارد و بر رفتار هیچ پیاده‌سازی‌ای از Gateway API تأثیر نمی‌گذارد.

### ingressclass.kubernetes.io/is-default-class

نوع: حاشیه‌نویسی

نمونه: `ingressclass.kubernetes.io/is-default-class: "true"`

محل استفاده: IngressClass

وقتی این حاشیه‌نویسی در یک منبع IngressClass روی `"true"` تنظیم شده باشد، این کلاس پیش‌فرض به منابع Ingress جدیدی که کلاسی برایشان مشخص نشده است، اختصاص می‌یابد.

### kubernetes.io/ingress.class (منسوخ‌شده)

نوع: حاشیه‌نویسی

محل استفاده: Ingress

{{< note >}}
این حاشیه‌نویسی از نسخهٔ v1.18 منسوخ شده و باید به‌جای آن از `spec.ingressClassName` استفاده کرد.
{{< /note >}}

### kubernetes.io/cluster-service (منسوخ‌شده) {#kubernetes-io-cluster-service}

نوع: برچسب

نمونه: `kubernetes.io/cluster-service: "true"`

محل استفاده: Service

اگر مقدار این برچسب true باشد، نشان می‌دهد که این Service سرویسی را به کلاستر ارائه می‌کند. هنگام اجرای `kubectl cluster-info`، این ابزار Service‌هایی را جست‌وجو می‌کند که این برچسب در آن‌ها روی true تنظیم شده باشد.

با این حال، تنظیم این برچسب روی هر Service منسوخ شده است.

### storageclass.kubernetes.io/is-default-class

نوع: حاشیه‌نویسی

نمونه: `storageclass.kubernetes.io/is-default-class: "true"`

محل استفاده: StorageClass

وقتی این حاشیه‌نویسی تنها در یک منبع StorageClass روی `"true"` تنظیم شده باشد، این کلاس پیش‌فرض به منابع PersistentVolumeClaim جدیدی که کلاسی برایشان مشخص نشده است، اختصاص می‌یابد.

### alpha.kubernetes.io/provided-node-ip (آلفا) {#alpha-kubernetes-io-provided-node-ip}

نوع: حاشیه‌نویسی

نمونه: `alpha.kubernetes.io/provided-node-ip: "10.0.0.1"`

محل استفاده: Node

مؤلفهٔ kubelet می‌تواند این حاشیه‌نویسی را روی یک Node تنظیم کند تا نشانی IPv4 و/یا IPv6 پیکربندی‌شدهٔ آن را مشخص کند.

وقتی kubelet با پرچم `--cloud-provider` و هر مقداری برای آن (شامل ارائه‌دهندگان ابری خارجی و ارائه‌دهندگان درون‌درختی قدیمی) راه‌اندازی شود، این حاشیه‌نویسی را روی Node تنظیم می‌کند تا نشانی IP تعیین‌شده با پرچم خط فرمان `--node-ip` را مشخص کند. سپس cloud-controller-manager معتبربودن این IP را نزد ارائه‌دهندهٔ ابری بررسی می‌کند.

### batch.kubernetes.io/job-completion-index

نوع: حاشیه‌نویسی، برچسب

نمونه: `batch.kubernetes.io/job-completion-index: "3"`

محل استفاده: Pod

کنترل‌کنندهٔ Job در kube-controller-manager این مقدار را به‌صورت برچسب و حاشیه‌نویسی برای Pod‌هایی تنظیم می‌کند که با [حالت تکمیل](/docs/concepts/workloads/controllers/job/#completion-mode) Indexed ایجاد شده‌اند.

توجه کنید که برای افزوده‌شدن این مقدار به‌عنوان **برچسب** Pod، باید feature gate با نام [PodIndexLabel](/docs/reference/command-line-tools-reference/feature-gates/) فعال باشد؛ در غیر این صورت، این مقدار فقط به‌صورت حاشیه‌نویسی اضافه می‌شود.

### batch.kubernetes.io/cronjob-scheduled-timestamp

نوع: حاشیه‌نویسی

نمونه: `batch.kubernetes.io/cronjob-scheduled-timestamp: "2016-05-19T03:00:00-07:00"`

محل استفاده: Job‌ها و Pod‌هایی که CronJob‌ها آن‌ها را کنترل می‌کنند

وقتی یک Job بخشی از یک CronJob باشد، از این حاشیه‌نویسی برای ثبت مُهر زمانی اصلی (مورد انتظار) ایجاد آن Job استفاده می‌شود. مؤلفهٔ control plane مقدار آن را برابر با این مُهر زمانی در قالب RFC3339 تنظیم می‌کند. اگر Job به CronJobای با منطقهٔ زمانی مشخص تعلق داشته باشد، مُهر زمانی در همان منطقهٔ زمانی است. در غیر این صورت، مُهر زمانی بر اساس زمان محلی controller-manager خواهد بود.

### cronjob.kubernetes.io/instantiate {#cronjob-kubernetes-io-instantiate}

نوع: حاشیه‌نویسی

نمونه: `cronjob.kubernetes.io/instantiate: "manual"`

محل استفاده: Job‌ها

وقتی با دستور `kubectl create job` و پرچم `--from=cronjob/<cronjob-name>` یک Job را به‌صورت دستی از الگوی یک CronJob موجود ایجاد می‌کنید، `kubectl` این حاشیه‌نویسی را روی Job جدید تنظیم می‌کند. مقدار این حاشیه‌نویسی همیشه `manual` است. با این حاشیه‌نویسی می‌توانید Job‌هایی را که کاربر در صورت نیاز ایجاد کرده است، از Job‌هایی که کنترل‌کنندهٔ CronJob به‌طور خودکار در زمان‌بندی مقرر ایجاد می‌کند، تشخیص دهید.

### kubectl.kubernetes.io/default-container

نوع: حاشیه‌نویسی

نمونه: `kubectl.kubernetes.io/default-container: "front-end-app"`

مقدار این حاشیه‌نویسی نام کانتینر پیش‌فرض این Pod است. برای مثال، دستورهای `kubectl logs` یا `kubectl exec` بدون پرچم `-c` یا `--container` از این کانتینر پیش‌فرض استفاده می‌کنند.

### kubectl.kubernetes.io/default-logs-container (منسوخ‌شده)

نوع: حاشیه‌نویسی

نمونه: `kubectl.kubernetes.io/default-logs-container: "front-end-app"`

مقدار این حاشیه‌نویسی نام کانتینر پیش‌فرض این Pod برای لاگ‌گیری است. برای مثال، دستور `kubectl logs` بدون پرچم `-c` یا `--container` از این کانتینر پیش‌فرض استفاده می‌کند.

{{< note >}}
این حاشیه‌نویسی منسوخ شده است و باید به‌جای آن از حاشیه‌نویسی [`kubectl.kubernetes.io/default-container`](#kubectl-kubernetes-io-default-container) استفاده کنید. کوبرنتیز از نسخهٔ 1.25 به بعد این حاشیه‌نویسی را نادیده می‌گیرد.
{{< /note >}}

### kubectl.kubernetes.io/last-applied-configuration

نوع: حاشیه‌نویسی

نمونه: _قطعه‌کد زیر را ببینید_
```yaml
    kubectl.kubernetes.io/last-applied-configuration: >
      {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"name":"example","namespace":"default"},"spec":{"selector":{"matchLabels":{"app.kubernetes.io/name":foo}},"template":{"metadata":{"labels":{"app.kubernetes.io/name":"foo"}},"spec":{"containers":[{"image":"container-registry.example/foo-bar:1.42","name":"foo-bar","ports":[{"containerPort":42}]}]}}}}
```

محل استفاده: همهٔ آبجکت‌ها

ابزار خط فرمان kubectl از این حاشیه‌نویسی به‌عنوان سازوکاری قدیمی برای ردیابی تغییرات استفاده می‌کند. [اعمال سمت سرور](/docs/reference/using-api/server-side-apply/) جایگزین این سازوکار شده است.

### kubectl.kubernetes.io/restartedAt {#kubectl-k8s-io-restart-at}

نوع: حاشیه‌نویسی

نمونه: `kubectl.kubernetes.io/restartedAt: "2024-06-21T17:27:41Z"`

محل استفاده: Deployment، ReplicaSet، StatefulSet، DaemonSet، Pod

این حاشیه‌نویسی زمان آخرین راه‌اندازی مجدد یک منبع (Deployment، ReplicaSet، StatefulSet یا DaemonSet) را در خود دارد؛ راه‌اندازی مجددی که در آن kubectl برای اجبار به ایجاد Pod‌های جدید، یک rollout را آغاز کرده است. دستور `kubectl rollout restart <RESOURCE>` با افزودن این حاشیه‌نویسی به فرادادهٔ الگوی همهٔ Pod‌های منبع، راه‌اندازی مجدد را آغاز می‌کند. در نمونهٔ بالا، زمان آخرین راه‌اندازی مجدد ۲۱ ژوئن ۲۰۲۴ ساعت 17:27:41 به وقت UTC است.

نباید فرض کنید که این حاشیه‌نویسی تاریخ و زمان جدیدترین به‌روزرسانی را نشان می‌دهد؛ ممکن است پس از آخرین rollout دستی، تغییر دیگری اعمال شده باشد.

اگر این حاشیه‌نویسی را به‌صورت دستی روی یک Pod تنظیم کنید، اتفاقی نمی‌افتد. اثر جانبی راه‌اندازی مجدد ناشی از نحوهٔ کارکرد مدیریت بار کاری و الگوی Pod است.

### endpoints.kubernetes.io/over-capacity (منسوخ‌شده) {#endpoints-kubernetes-io-over-capacity}

نوع: حاشیه‌نویسی

نمونه: `endpoints.kubernetes.io/over-capacity: truncated`

محل استفاده: Endpoints

اگر {{< glossary_tooltip term_id="service" >}} مرتبط بیش از ۱۰۰۰ endpoint پشتیبان داشته باشد، {{< glossary_tooltip text="control plane" term_id="control-plane" >}} این حاشیه‌نویسی را به آبجکت [Endpoints](/docs/concepts/services-networking/service/#endpoints) اضافه می‌کند. این حاشیه‌نویسی نشان می‌دهد که ظرفیت آبجکت Endpoints پر شده و تعداد endpointها به ۱۰۰۰ محدود شده است.

اگر تعداد endpointهای پشتیبان به کمتر از ۱۰۰۰ برسد، control plane این حاشیه‌نویسی را حذف می‌کند.

{{< note >}}
رابط [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/) منسوخ شده و باید به‌جای آن از [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) استفاده کرد. هر Service می‌تواند چند آبجکت EndpointSlice داشته باشد؛ در نتیجه، نیازی به کوتاه‌سازی فهرست در EndpointSlice‌ها نیست.
{{< /note >}}

### endpoints.kubernetes.io/last-change-trigger-time (منسوخ‌شده) {#endpoints-kubernetes-io-last-change-trigger-time}

نوع: حاشیه‌نویسی

نمونه: `endpoints.kubernetes.io/last-change-trigger-time: "2023-07-20T04:45:21Z"`

محل استفاده: Endpoints

این حاشیه‌نویسی روی آبجکت [Endpoints](/docs/concepts/services-networking/service/#endpoints) تنظیم می‌شود و یک مُهر زمانی را نشان می‌دهد. این مُهر زمانی در قالب رشتهٔ تاریخ-زمان RFC 3339 ذخیره می‌شود؛ برای مثال، '2018-10-22T19:32:52.1Z'. این مقدار، مُهر زمانی آخرین تغییر در یک آبجکت Pod یا Service است که باعث تغییر آبجکت Endpoints شده است.

{{< note >}}
رابط [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/) منسوخ شده و باید به‌جای آن از [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) استفاده کرد.
{{< /note >}}

### control-plane.alpha.kubernetes.io/leader (منسوخ‌شده) {#control-plane-alpha-kubernetes-io-leader}

نوع: حاشیه‌نویسی

نمونه: `control-plane.alpha.kubernetes.io/leader={"holderIdentity":"controller-0","leaseDurationSeconds":15,"acquireTime":"2023-01-19T13:12:57Z","renewTime":"2023-01-19T13:13:54Z","leaderTransitions":1}`

محل استفاده: Endpoints

مؤلفهٔ {{< glossary_tooltip text="control plane" term_id="control-plane" >}} پیش‌تر برای هماهنگی تعیین رهبر در control plane کوبرنتیز از یک آبجکت [Endpoints](/docs/concepts/services-networking/service/#endpoints) استفاده می‌کرد. این آبجکت Endpoints حاشیه‌نویسی‌ای با جزئیات زیر داشت:

- رهبر فعلی چه کسی است.
- زمانی که رهبری فعلی به دست آمده است.
- مدت اجاره (رهبری) بر حسب ثانیه.
- زمانی که اجارهٔ فعلی (رهبری فعلی) باید تمدید شود.
- تعداد جابه‌جایی‌های رهبری که در گذشته رخ داده است.

اکنون کوبرنتیز برای مدیریت تعیین رهبر در control plane از [Lease‌ها](/docs/concepts/architecture/leases/) استفاده می‌کند.

### batch.kubernetes.io/job-tracking (منسوخ‌شده) {#batch-kubernetes-io-job-tracking}

نوع: حاشیه‌نویسی

نمونه: `batch.kubernetes.io/job-tracking: ""`

محل استفاده: Job‌ها

وجود این حاشیه‌نویسی روی یک Job پیش‌تر نشان می‌داد که control plane [وضعیت Job را با استفاده از finalizerها ردیابی می‌کند](/docs/concepts/workloads/controllers/job/#job-tracking-with-finalizers). افزودن یا حذف این حاشیه‌نویسی دیگر تأثیری ندارد (Kubernetes v1.27 و نسخه‌های بعدی). همهٔ Job‌ها با finalizerها ردیابی می‌شوند.

### job-name (منسوخ‌شده) {#job-name}

نوع: برچسب

نمونه: `job-name: "pi"`

محل استفاده: Job‌ها و Pod‌هایی که Job‌ها آن‌ها را کنترل می‌کنند

{{< note >}}
این برچسب از Kubernetes 1.27 منسوخ شده است. کوبرنتیز 1.27 و نسخه‌های جدیدتر این برچسب را نادیده می‌گیرند و از برچسب `job-name` پیشونددار استفاده می‌کنند.
{{< /note >}}

### controller-uid (منسوخ‌شده) {#controller-uid}

نوع: برچسب

نمونه: `controller-uid: "$UID"`

محل استفاده: Job‌ها و Pod‌هایی که Job‌ها آن‌ها را کنترل می‌کنند

{{< note >}}
این برچسب از Kubernetes 1.27 منسوخ شده است. کوبرنتیز 1.27 و نسخه‌های جدیدتر این برچسب را نادیده می‌گیرند و از برچسب `controller-uid` پیشونددار استفاده می‌کنند.
{{< /note >}}

### batch.kubernetes.io/job-name {#batchkubernetesio-job-name}

نوع: برچسب

نمونه: `batch.kubernetes.io/job-name: "pi"`

محل استفاده: Job‌ها و Pod‌هایی که Job‌ها آن‌ها را کنترل می‌کنند

این برچسب راهی ساده و کاربرپسند برای یافتن Pod‌های متناظر با یک Job فراهم می‌کند. مقدار `job-name` از `name` آن Job گرفته می‌شود و یافتن Pod‌های متناظر با آن Job را آسان می‌کند.

### batch.kubernetes.io/controller-uid {#batchkubernetesio-controller-uid}

نوع: برچسب

مثال: `batch.kubernetes.io/controller-uid: "$UID"`

استفاده‌شده روی: Jobها و Podهایی که Jobها آن‌ها را کنترل می‌کنند

از این برچسب می‌توان برای دریافت برنامه‌نویسانهٔ همهٔ Podهای متناظر با یک Job استفاده کرد.
مقدار `controller-uid` شناسه‌ای یکتا است که در فیلد `selector` تنظیم می‌شود تا کنترل‌کنندهٔ Job بتواند همهٔ Podهای متناظر را پیدا کند.

### scheduler.alpha.kubernetes.io/defaultTolerations {#scheduleralphakubernetesio-defaulttolerations}

نوع: حاشیه‌نویسی (annotation)

مثال: `scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Equal", "value": "value1", "effect": "NoSchedule", "key": "dedicated-node"}]'`

استفاده‌شده روی: Namespace

برای استفاده از این حاشیه‌نویسی، باید کنترل‌کنندهٔ پذیرش [PodTolerationRestriction](/docs/reference/access-authn-authz/admission-controllers/#podtolerationrestriction) فعال باشد. با این کلید حاشیه‌نویسی می‌توانید tolerationهایی را به یک فضای نام (namespace) اختصاص دهید تا به همهٔ Podهای جدیدی که در آن فضای نام ایجاد می‌شوند افزوده شوند.

### scheduler.alpha.kubernetes.io/tolerationsWhitelist {#schedulerkubernetestolerations-whitelist}

نوع: حاشیه‌نویسی

مثال: `scheduler.alpha.kubernetes.io/tolerationsWhitelist: '[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'`

استفاده‌شده روی: Namespace

این حاشیه‌نویسی فقط زمانی کاربرد دارد که کنترل‌کنندهٔ پذیرش (آلفای) [PodTolerationRestriction](/docs/reference/access-authn-authz/admission-controllers/#podtolerationrestriction) فعال باشد. مقدار حاشیه‌نویسی یک سند JSON است که فهرست tolerationهای مجاز را برای فضای نامی که این حاشیه‌نویسی روی آن قرار دارد تعریف می‌کند. هنگامی که یک Pod ایجاد می‌کنید یا tolerationهای آن را تغییر می‌دهید، API server بررسی می‌کند که آیا این tolerationها در فهرست مجاز آمده‌اند یا نه. Pod فقط در صورت موفقیت این بررسی پذیرفته می‌شود.

### scheduler.alpha.kubernetes.io/preferAvoidPods (منسوخ‌شده) {#scheduleralphakubernetesio-preferavoidpods}

نوع: حاشیه‌نویسی

استفاده‌شده روی: Node

برای استفاده از این حاشیه‌نویسی، باید [افزونهٔ زمان‌بندی NodePreferAvoidPods](/docs/reference/scheduling/config/#scheduling-plugins) فعال باشد. این افزونه از نسخهٔ ۱٫۲۲ کوبرنتیز منسوخ شده است. به‌جای آن از [Taintها و Tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration/) استفاده کنید.

### node.kubernetes.io/not-ready

نوع: Taint

مثال: `node.kubernetes.io/not-ready: "NoExecute"`

استفاده‌شده روی: Node

کنترل‌کنندهٔ Node با پایش سلامت هر نود، آماده‌بودن آن را تشخیص می‌دهد و بر همین اساس این taint را اضافه یا حذف می‌کند.

### node.kubernetes.io/unreachable

نوع: Taint

مثال: `node.kubernetes.io/unreachable: "NoExecute"`

استفاده‌شده روی: Node

کنترل‌کنندهٔ Node این taint را به نودی اضافه می‌کند که مقدار `Ready` در [NodeCondition](/docs/concepts/architecture/nodes/#condition) آن `Unknown` باشد.

### node.kubernetes.io/unschedulable

نوع: Taint

مثال: `node.kubernetes.io/unschedulable: "NoSchedule"`

استفاده‌شده روی: Node

این taint برای جلوگیری از شرایط رقابتی (race condition) هنگام راه‌اندازی اولیهٔ نود به آن اضافه می‌شود.

### node.kubernetes.io/memory-pressure

نوع: Taint

مثال: `node.kubernetes.io/memory-pressure: "NoSchedule"`

استفاده‌شده روی: Node

مؤلفهٔ kubelet فشار حافظه را بر اساس مقادیر `memory.available` و `allocatableMemory.available` مشاهده‌شده روی نود تشخیص می‌دهد. سپس این مقادیر را با آستانه‌های متناظری که می‌توان روی kubelet تنظیم کرد مقایسه می‌کند تا مشخص شود وضعیت نود و این taint باید اضافه یا حذف شوند یا نه.

### node.kubernetes.io/disk-pressure

نوع: Taint

مثال: `node.kubernetes.io/disk-pressure :"NoSchedule"`

استفاده‌شده روی: Node

مؤلفهٔ kubelet فشار دیسک را بر اساس مقادیر `imagefs.available`، `imagefs.inodesFree`، `nodefs.available` و `nodefs.inodesFree` (فقط در لینوکس) مشاهده‌شده روی نود تشخیص می‌دهد. سپس این مقادیر را با آستانه‌های متناظری که می‌توان روی kubelet تنظیم کرد مقایسه می‌کند تا مشخص شود وضعیت نود و این taint باید اضافه یا حذف شوند یا نه.

### node.kubernetes.io/network-unavailable

نوع: Taint

مثال: `node.kubernetes.io/network-unavailable: "NoSchedule"`

استفاده‌شده روی: Node

اگر ارائه‌دهندهٔ ابری مورد استفاده اعلام کند که به پیکربندی شبکهٔ بیشتری نیاز است، kubelet در ابتدا این taint را تنظیم می‌کند. ارائه‌دهندهٔ ابری فقط پس از پیکربندی درست مسیر در فضای ابری این taint را حذف می‌کند.

### node.kubernetes.io/pid-pressure

نوع: Taint

مثال: `node.kubernetes.io/pid-pressure: "NoSchedule"`

استفاده‌شده روی: Node

مؤلفهٔ kubelet اختلاف میان اندازهٔ `/proc/sys/kernel/pid_max` و تعداد PIDهایی را که کوبرنتیز روی نود مصرف کرده است بررسی می‌کند تا تعداد PIDهای در دسترس را به دست آورد؛ این مقدار متریک `pid.available` نام دارد. سپس این متریک با آستانهٔ متناظری که می‌توان روی kubelet تنظیم کرد مقایسه می‌شود تا مشخص شود وضعیت نود و این taint باید اضافه یا حذف شوند یا نه.

### node.kubernetes.io/out-of-service

نوع: Taint

مثال: `node.kubernetes.io/out-of-service:NoExecute`

استفاده‌شده روی: Node

کاربر می‌تواند این taint را به‌صورت دستی به یک نود اضافه کند و آن را خارج از سرویس علامت بزند. اگر نودی با این taint خارج از سرویس علامت‌گذاری شود، Podهایی از آن که toleration منطبق با این taint را نداشته باشند به‌اجبار حذف می‌شوند و عملیات جداسازی حجم‌ها (volume) برای Podهای در حال خاتمه روی آن نود بلافاصله انجام می‌شود. به این ترتیب، Podهای نود خارج از سرویس می‌توانند به‌سرعت روی نود دیگری بازیابی شوند.

{{< caution >}}
برای جزئیات بیشتر دربارهٔ زمان و نحوهٔ استفاده از این taint، به [خاموش‌شدن غیرعادی نود](/docs/concepts/cluster-administration/node-shutdown/#non-graceful-node-shutdown) مراجعه کنید.
{{< /caution >}}

### node.cloudprovider.kubernetes.io/uninitialized

نوع: Taint

مثال: `node.cloudprovider.kubernetes.io/uninitialized: "NoSchedule"`

استفاده‌شده روی: Node

هنگامی که kubelet با ارائه‌دهندهٔ ابری «external» راه‌اندازی می‌شود، این taint روی نود تنظیم می‌شود تا نود غیرقابل‌استفاده علامت بخورد. سپس کنترل‌کننده‌ای از cloud-controller-manager این نود را راه‌اندازی اولیه می‌کند و taint را برمی‌دارد.

### node.cloudprovider.kubernetes.io/shutdown

نوع: Taint

مثال: `node.cloudprovider.kubernetes.io/shutdown: "NoSchedule"`

استفاده‌شده روی: Node

اگر نودی در وضعیت خاموشی مشخص‌شده از سوی ارائه‌دهندهٔ ابری باشد، taint با کلید `node.cloudprovider.kubernetes.io/shutdown` و اثر `NoSchedule` روی آن قرار می‌گیرد.

### feature.node.kubernetes.io/*

نوع: برچسب

مثال: `feature.node.kubernetes.io/network-sriov.capable: "true"`

استفاده‌شده روی: Node

مؤلفهٔ Node Feature Discovery (NFD) از این برچسب‌ها برای اعلام قابلیت‌های یک نود استفاده می‌کند. همهٔ برچسب‌های داخلی از فضای نام برچسب `feature.node.kubernetes.io` استفاده می‌کنند و قالب آن‌ها `feature.node.kubernetes.io/<feature-name>: "true"` است. این مؤلفه نقاط توسعهٔ بسیاری برای ایجاد برچسب‌های ویژهٔ فروشندگان و برنامه‌ها دارد. برای جزئیات بیشتر، [راهنمای سفارشی‌سازی](https://kubernetes-sigs.github.io/node-feature-discovery/v0.12/usage/customization-guide) را ببینید.

### nfd.node.kubernetes.io/master.version

نوع: حاشیه‌نویسی

مثال: `nfd.node.kubernetes.io/master.version: "v0.6.0"`

استفاده‌شده روی: Node

این حاشیه‌نویسی روی نودهایی که [master](https://kubernetes-sigs.github.io/node-feature-discovery/stable/usage/nfd-master.html) مربوط به Node Feature Discovery روی آن‌ها زمان‌بندی شده است، نسخهٔ NFD master را ثبت می‌کند. کاربرد آن فقط اطلاع‌رسانی است.

### nfd.node.kubernetes.io/worker.version

نوع: حاشیه‌نویسی

مثال: `nfd.node.kubernetes.io/worker.version: "v0.4.0"`

استفاده‌شده روی: Nodeها

اگر [worker](https://kubernetes-sigs.github.io/node-feature-discovery/stable/usage/nfd-worker.html) مربوط به Node Feature Discovery روی نودی در حال اجرا باشد، این حاشیه‌نویسی نسخهٔ آن را ثبت می‌کند. کاربرد آن فقط اطلاع‌رسانی است.

### nfd.node.kubernetes.io/feature-labels

نوع: حاشیه‌نویسی

مثال: `nfd.node.kubernetes.io/feature-labels: "cpu-cpuid.ADX,cpu-cpuid.AESNI,cpu-hardware_multithreading,kernel-version.full"`

استفاده‌شده روی: Nodeها

این حاشیه‌نویسی فهرستی جداشده با کاما از برچسب‌های قابلیت نود را ثبت می‌کند که [Node Feature Discovery](https://kubernetes-sigs.github.io/node-feature-discovery/) (NFD) آن‌ها را مدیریت می‌کند. NFD از این فهرست در یک سازوکار داخلی استفاده می‌کند. شما نباید این حاشیه‌نویسی را خودتان ویرایش کنید.

### nfd.node.kubernetes.io/extended-resources

نوع: حاشیه‌نویسی

مثال: `nfd.node.kubernetes.io/extended-resources: "accelerator.acme.example/q500,example.com/coprocessor-fx5"`

استفاده‌شده روی: Nodeها

این حاشیه‌نویسی فهرستی جداشده با کاما از [منابع توسعه‌یافته](/docs/concepts/configuration/manage-resources-containers/#extended-resources) را ثبت می‌کند که [Node Feature Discovery](https://kubernetes-sigs.github.io/node-feature-discovery/) (NFD) آن‌ها را مدیریت می‌کند. NFD از این فهرست در یک سازوکار داخلی استفاده می‌کند. شما نباید این حاشیه‌نویسی را خودتان ویرایش کنید.

### nfd.node.kubernetes.io/node-name

نوع: برچسب

مثال: `nfd.node.kubernetes.io/node-name: node-1`

استفاده‌شده روی: Nodeها

این برچسب مشخص می‌کند که آبجکت NodeFeature کدام نود را هدف گرفته است. سازندگان آبجکت‌های NodeFeature باید این برچسب را تنظیم کنند و مصرف‌کنندگان این آبجکت‌ها باید از آن برای پالایش قابلیت‌های تعیین‌شده برای یک نود مشخص استفاده کنند.

{{< note >}}
این برچسب‌ها و حاشیه‌نویسی‌های Node Feature Discovery (NFD) فقط روی نودهایی اعمال می‌شوند که NFD روی آن‌ها در حال اجرا است. برای آشنایی بیشتر با NFD و مؤلفه‌های آن، به [مستندات](https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/) رسمی آن مراجعه کنید.
{{< /note >}}

### service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval (بتا) {#service-beta-kubernetes-io-aws-load-balancer-access-log-emit-interval}

مثال: `service.beta.kubernetes.io/aws-load-balancer-access-log-emit-interval: "5"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار (load balancer) مربوط به یک Service را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. این مقدار تعیین می‌کند که متعادل‌کنندهٔ بار هر چند وقت یک‌بار ورودی‌های لاگ را بنویسد. برای مثال، اگر مقدار را ۵ تنظیم کنید، نوشتن لاگ‌ها با فاصلهٔ ۵ ثانیه انجام می‌شود.

### service.beta.kubernetes.io/aws-load-balancer-access-log-enabled (بتا) {#service-beta-kubernetes-io-aws-load-balancer-access-log-enabled}

مثال: `service.beta.kubernetes.io/aws-load-balancer-access-log-enabled: "false"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار مربوط به یک Service را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. اگر مقدار این حاشیه‌نویسی را "true" تنظیم کنید، ثبت لاگ دسترسی فعال می‌شود.

### service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-name (بتا) {#service-beta-kubernetes-io-aws-load-balancer-access-log-s3-bucket-name}

مثال: `service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-name: example`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار مربوط به یک Service را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. متعادل‌کنندهٔ بار لاگ‌ها را در باکت S3 با نامی که مشخص می‌کنید می‌نویسد.

### service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-prefix (بتا) {#service-beta-kubernetes-io-aws-load-balancer-access-log-s3-bucket-prefix}

مثال: `service.beta.kubernetes.io/aws-load-balancer-access-log-s3-bucket-prefix: "/example"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار مربوط به یک Service را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. متعادل‌کنندهٔ بار آبجکت‌های لاگ را با پیشوندی که مشخص می‌کنید می‌نویسد.

### service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags (بتا) {#service-beta-kubernetes-io-aws-load-balancer-additional-resource-tags}

مثال: `service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: "Environment=demo,Project=example"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، تگ‌های متعادل‌کنندهٔ بار (مفهومی در AWS) را بر اساس جفت‌های کلید/مقدار جداشده با کاما در مقدار این حاشیه‌نویسی پیکربندی می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-alpn-policy (بتا) {#service-beta-kubernetes-io-aws-load-balancer-alpn-policy}

مثال: `service.beta.kubernetes.io/aws-load-balancer-alpn-policy: HTTP2Optional`

استفاده‌شده روی: Service

[کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-attributes (بتا) {#service-beta-kubernetes-io-aws-load-balancer-attributes}

مثال: `service.beta.kubernetes.io/aws-load-balancer-attributes: "deletion_protection.enabled=true"`

استفاده‌شده روی: Service

[کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-backend-protocol (بتا) {#service-beta-kubernetes-io-aws-load-balancer-backend-protocol}

مثال: `service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، شنوندهٔ متعادل‌کنندهٔ بار را بر اساس مقدار این حاشیه‌نویسی پیکربندی می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-connection-draining-enabled (بتا) {#service-beta-kubernetes-io-aws-load-balancer-connection-draining-enabled}

مثال: `service.beta.kubernetes.io/aws-load-balancer-connection-draining-enabled: "false"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. تنظیم تخلیهٔ اتصال (connection draining) در متعادل‌کنندهٔ بار به مقداری بستگی دارد که تعیین می‌کنید.

### service.beta.kubernetes.io/aws-load-balancer-connection-draining-timeout (بتا) {#service-beta-kubernetes-io-aws-load-balancer-connection-draining-timeout}

مثال: `service.beta.kubernetes.io/aws-load-balancer-connection-draining-timeout: "60"`

استفاده‌شده روی: Service

اگر [تخلیهٔ اتصال](#service-beta-kubernetes-io-aws-load-balancer-connection-draining-enabled) را برای یک Service از نوع `type: LoadBalancer` پیکربندی کنید و از فضای ابری AWS استفاده کنید، این یکپارچه‌سازی دورهٔ تخلیه را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقداری که تنظیم می‌کنید مهلت تخلیه را برحسب ثانیه تعیین می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-ip-address-type (بتا) {#service-beta-kubernetes-io-aws-load-balancer-ip-address-type}

مثال: `service.beta.kubernetes.io/aws-load-balancer-ip-address-type: ipv4`

استفاده‌شده روی: Service

[کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کنندهٔ متعادل‌کنندهٔ بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout (بتا) {#service-beta-kubernetes-io-aws-load-balancer-connection-idle-timeout}

مثال: `service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: "60"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. متعادل‌کنندهٔ بار یک مهلت بیکاری پیکربندی‌شده (برحسب ثانیه) دارد که روی اتصال‌های آن اعمال می‌شود. اگر تا پایان این مهلت هیچ داده‌ای ارسال یا دریافت نشود، متعادل‌کنندهٔ بار اتصال را می‌بندد.

### service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled (بتا) {#service-beta-kubernetes-io-aws-load-balancer-cross-zone-load-balancing-enabled}

مثال: `service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. اگر مقدار این حاشیه‌نویسی را "true" تنظیم کنید، هر نود متعادل‌کنندهٔ بار درخواست‌ها را به‌طور یکنواخت میان هدف‌های ثبت‌شده در همهٔ [ناحیه‌های دسترس‌پذیری](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) فعال توزیع می‌کند. اگر متعادل‌سازی بار میان‌ناحیه‌ای را غیرفعال کنید، هر نود متعادل‌کنندهٔ بار درخواست‌ها را فقط میان هدف‌های ثبت‌شده در ناحیهٔ دسترس‌پذیری خودش به‌طور یکنواخت توزیع می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-eip-allocations (بتا) {#service-beta-kubernetes-io-aws-load-balancer-eip-allocations}

مثال: `service.beta.kubernetes.io/aws-load-balancer-eip-allocations: "eipalloc-01bcdef23bcdef456,eipalloc-def1234abc4567890"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار آن فهرستی جداشده با کاما از شناسه‌های تخصیص نشانی IP الاستیک است.

این حاشیه‌نویسی فقط برای Serviceهایی از نوع `type: LoadBalancer` کاربرد دارد که متعادل‌کنندهٔ بار آن‌ها یک AWS Network Load Balancer باشد.

### service.beta.kubernetes.io/aws-load-balancer-extra-security-groups (بتا) {#service-beta-kubernetes-io-aws-load-balancer-extra-security-groups}

مثال: `service.beta.kubernetes.io/aws-load-balancer-extra-security-groups: "sg-12abcd3456,sg-34dcba6543"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کنندهٔ بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی فهرستی جداشده با کاما از گروه‌های امنیتی اضافی AWS VPC است که باید برای متعادل‌کنندهٔ بار پیکربندی شوند.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-healthy-threshold}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold: "3"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار (load balancer) را بر اساس این حاشیه‌نویسی (annotation) پیکربندی می‌کند. مقدار این حاشیه‌نویسی تعیین می‌کند که یک بک‌اند (backend) باید چند بررسی سلامت (health check) موفق پیاپی را بگذراند تا برای دریافت ترافیک سالم به شمار آید.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-interval}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-interval: "30"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی فاصله زمانی میان کاوش‌های بررسی سلامت متعادل‌کننده بار را بر حسب ثانیه مشخص می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-path (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-papth}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-path: /healthcheck`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی بخش مسیر URL مورد استفاده در بررسی‌های سلامت HTTP را تعیین می‌کند.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-port (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-port}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-port: "24"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی تعیین می‌کند که متعادل‌کننده بار هنگام انجام بررسی سلامت به کدام پورت متصل شود.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-protocol}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol: TCP`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی تعیین می‌کند که متعادل‌کننده بار سلامت مقصدهای بک‌اند را چگونه بررسی کند.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-timeout (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-timeout}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-timeout: "3"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی مدت زمانی را بر حسب ثانیه مشخص می‌کند که پس از سپری شدن آن، کاوشی که هنوز موفق نشده است به‌طور خودکار ناموفق در نظر گرفته می‌شود.

### service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold (بتا) {#service-beta-kubernetes-io-aws-load-balancer-healthcheck-unhealthy-threshold}

مثال: `service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold: "3"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی تعیین می‌کند که پس از چند بررسی سلامت ناموفق پیاپی، یک بک‌اند برای دریافت ترافیک ناسالم به شمار می‌آید.

### service.beta.kubernetes.io/aws-load-balancer-internal (بتا) {#service-beta-kubernetes-io-aws-load-balancer-internal}

مثال: `service.beta.kubernetes.io/aws-load-balancer-internal: "true"`

استفاده‌شده روی: Service

یکپارچه‌سازی cloud controller manager با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. اگر مقدار این حاشیه‌نویسی را "true" قرار دهید، این یکپارچه‌سازی یک متعادل‌کننده بار داخلی پیکربندی می‌کند.

اگر از [کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) استفاده می‌کنید، به [`service.beta.kubernetes.io/aws-load-balancer-scheme`](#service-beta-kubernetes-io-aws-load-balancer-scheme) مراجعه کنید.

### service.beta.kubernetes.io/aws-load-balancer-manage-backend-security-group-rules (بتا) {#service-beta-kubernetes-io-aws-load-balancer-manage-backend-security-group-rules}

مثال: `service.beta.kubernetes.io/aws-load-balancer-manage-backend-security-group-rules: "true"`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-name (بتا) {#service-beta-kubernetes-io-aws-load-balancer-name}

مثال: `service.beta.kubernetes.io/aws-load-balancer-name: my-elb`

استفاده‌شده روی: Service

اگر این حاشیه‌نویسی را روی یک Service تنظیم کنید، حاشیه‌نویسی `service.beta.kubernetes.io/aws-load-balancer-type: "external"` را نیز به همان Service بیفزایید و در کلاستر خود از [کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) استفاده کنید، این کنترل‌کننده نام متعادل‌کننده بار را برابر با مقداری قرار می‌دهد که برای _این_ حاشیه‌نویسی تعیین کرده‌اید.

برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-nlb-target-type (بتا) {#service-beta-kubernetes-io-aws-load-balancer-nlb-target-type}

مثال: `service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: "true"`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-private-ipv4-addresses (بتا) {#service-beta-kubernetes-io-aws-load-balancer-private-ipv4-addresses}

مثال: `service.beta.kubernetes.io/aws-load-balancer-private-ipv4-addresses: "198.51.100.0,198.51.100.64"`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-proxy-protocol (بتا) {#service-beta-kubernetes-io-aws-load-balancer-proxy-protocol}

مثال: `service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"`

استفاده‌شده روی: Service

یکپارچه‌سازی رسمی کوبرنتیز با سرویس Elastic Load Balancing در AWS، متعادل‌کننده بار را بر اساس این حاشیه‌نویسی پیکربندی می‌کند. تنها مقدار مجاز `"*"` است و نشان می‌دهد که متعادل‌کننده بار باید اتصال‌های TCP به Pod بک‌اند را با پروتکل PROXY پوشش دهد.

### service.beta.kubernetes.io/aws-load-balancer-scheme (بتا) {#service-beta-kubernetes-io-aws-load-balancer-scheme}

مثال: `service.beta.kubernetes.io/aws-load-balancer-scheme: internal`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-security-groups (منسوخ‌شده) {#service-beta-kubernetes-io-aws-load-balancer-security-groups}

مثال: `service.beta.kubernetes.io/aws-load-balancer-security-groups: "sg-53fae93f,sg-8725gr62r"`

استفاده‌شده روی: Service

کنترل‌کننده متعادل‌کننده بار AWS با این حاشیه‌نویسی فهرستی جداشده با ویرگول از گروه‌های امنیتی (security group) را مشخص می‌کند که باید به یک متعادل‌کننده بار AWS متصل شوند. هم نام و هم شناسه گروه امنیتی پشتیبانی می‌شود؛ منظور از نام، مقدار برچسب `Name` است، نه ویژگی `groupName`.

وقتی این حاشیه‌نویسی به یک Service افزوده می‌شود، کنترل‌کننده متعادل‌کننده بار گروه‌های امنیتی ذکرشده در آن را به متعادل‌کننده بار متصل می‌کند. اگر این حاشیه‌نویسی را حذف کنید، کنترل‌کننده متعادل‌کننده بار AWS به‌طور خودکار یک گروه امنیتی جدید می‌سازد و آن را به متعادل‌کننده بار متصل می‌کند.

{{< note >}}
کوبرنتیز نسخه ۱٫۲۷ و نسخه‌های بعدی این حاشیه‌نویسی را مستقیماً تنظیم نمی‌کنند و نمی‌خوانند. با این حال، کنترل‌کننده متعادل‌کننده بار AWS (که بخشی از پروژه کوبرنتیز است) همچنان از حاشیه‌نویسی `service.beta.kubernetes.io/aws-load-balancer-security-groups` استفاده می‌کند.
{{< /note >}}

### service.beta.kubernetes.io/load-balancer-source-ranges (منسوخ‌شده) {#service-beta-kubernetes-io-load-balancer-source-ranges}

مثال: `service.beta.kubernetes.io/load-balancer-source-ranges: "192.0.2.0/25"`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. به‌جای آن باید فیلد `.spec.loadBalancerSourceRanges` را برای Service تنظیم کنید.

### service.beta.kubernetes.io/aws-load-balancer-ssl-cert (بتا) {#service-beta-kubernetes-io-aws-load-balancer-ssl-cert}

مثال: `service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012"`

استفاده‌شده روی: Service

یکپارچه‌سازی رسمی با سرویس Elastic Load Balancing در AWS، پروتکل TLS را برای Serviceای با `type: LoadBalancer` بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی، نام منبع AWS (ARN) مربوط به گواهی X.509 است که شنونده متعادل‌کننده بار باید از آن استفاده کند.

(پروتکل TLS بر پایه فناوری قدیمی‌تری است که نام اختصاری آن SSL است.)

### service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy (بتا) {#service-beta-kubernetes-io-aws-load-balancer-ssl-negotiation-policy}

مثال: `service.beta.kubernetes.io/aws-load-balancer-ssl-negotiation-policy: ELBSecurityPolicy-TLS-1-2-2017-01`

یکپارچه‌سازی رسمی با سرویس Elastic Load Balancing در AWS، پروتکل TLS را برای Serviceای با `type: LoadBalancer` بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی نام یک سیاست AWS برای مذاکره TLS با کلاینت طرف مقابل است.

### service.beta.kubernetes.io/aws-load-balancer-ssl-ports (بتا) {#service-beta-kubernetes-io-aws-load-balancer-ssl-ports}

مثال: `service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "*"`

یکپارچه‌سازی رسمی با سرویس Elastic Load Balancing در AWS، پروتکل TLS را برای Serviceای با `type: LoadBalancer` بر اساس این حاشیه‌نویسی پیکربندی می‌کند. مقدار این حاشیه‌نویسی یا `"*"` است، به این معنا که همه پورت‌های متعادل‌کننده بار باید از TLS استفاده کنند، یا فهرستی از شماره پورت‌ها که با ویرگول از هم جدا شده‌اند.

### service.beta.kubernetes.io/aws-load-balancer-subnets (بتا) {#service-beta-kubernetes-io-aws-load-balancer-subnets}

مثال: `service.beta.kubernetes.io/aws-load-balancer-subnets: "private-a,private-b"`

یکپارچه‌سازی رسمی کوبرنتیز با AWS از این حاشیه‌نویسی برای پیکربندی متعادل‌کننده بار و تعیین نواحی دسترس‌پذیری AWS برای استقرار سرویس مدیریت‌شده متعادل‌سازی بار استفاده می‌کند. مقدار آن یا فهرستی از نام‌های زیرشبکه (subnet) است که با ویرگول از هم جدا شده‌اند، یا فهرستی از شناسه‌های زیرشبکه با همین قالب.

### service.beta.kubernetes.io/aws-load-balancer-target-group-attributes (بتا) {#service-beta-kubernetes-io-aws-load-balancer-target-group-attributes}

مثال: `service.beta.kubernetes.io/aws-load-balancer-target-group-attributes: "stickiness.enabled=true,stickiness.type=source_ip"`

استفاده‌شده روی: Service

[کنترل‌کننده متعادل‌کننده بار AWS](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) از این حاشیه‌نویسی استفاده می‌کند. برای جزئیات بیشتر، بخش [حاشیه‌نویسی‌ها](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/) را در مستندات کنترل‌کننده متعادل‌کننده بار AWS ببینید.

### service.beta.kubernetes.io/aws-load-balancer-target-node-labels (بتا) {#service-beta-kubernetes-io-aws-target-node-labels}

مثال: `service.beta.kubernetes.io/aws-load-balancer-target-node-labels: "kubernetes.io/os=Linux,topology.kubernetes.io/region=us-east-2"`

یکپارچه‌سازی رسمی کوبرنتیز با AWS از این حاشیه‌نویسی استفاده می‌کند تا مشخص کند کدام نودهای کلاستر شما مقصدهای معتبر متعادل‌کننده بار به شمار می‌آیند.

### service.beta.kubernetes.io/aws-load-balancer-type (بتا) {#service-beta-kubernetes-io-aws-load-balancer-type}

مثال: `service.beta.kubernetes.io/aws-load-balancer-type: external`

یکپارچه‌سازی‌های رسمی کوبرنتیز با AWS از این حاشیه‌نویسی استفاده می‌کنند تا مشخص کنند آیا یکپارچه‌سازی ارائه‌دهنده ابری AWS باید Serviceای با `type: LoadBalancer` را مدیریت کند یا نه.

دو مقدار مجاز وجود دارد:

`nlb`
: مؤلفه cloud controller manager یک Network Load Balancer پیکربندی می‌کند

`external`
: مؤلفه cloud controller manager هیچ متعادل‌کننده باری را پیکربندی نمی‌کند

اگر Serviceای با `type: LoadBalancer` را در AWS مستقر کنید و حاشیه‌نویسی `service.beta.kubernetes.io/aws-load-balancer-type` را تنظیم نکنید، یکپارچه‌سازی AWS یک Elastic Load Balancer کلاسیک مستقر می‌کند. این رفتار در نبود حاشیه‌نویسی، پیش‌فرض است، مگر اینکه خلاف آن را مشخص کنید.

وقتی مقدار این حاشیه‌نویسی را روی Serviceای با `type: LoadBalancer` برابر با `external` قرار دهید و کلاستر شما یک استقرار فعال از کنترل‌کننده متعادل‌کننده بار AWS داشته باشد، این کنترل‌کننده تلاش می‌کند متعادل‌کننده باری را بر اساس مشخصات Service مستقر کند.

{{< caution >}}
حاشیه‌نویسی `service.beta.kubernetes.io/aws-load-balancer-type` را روی آبجکت Service موجود تغییر ندهید و به آن اضافه نکنید. برای جزئیات بیشتر، مستندات AWS در این زمینه را ببینید.
{{< /caution >}}

### service.beta.kubernetes.io/azure-load-balancer-disable-tcp-reset (منسوخ‌شده) {#service-beta-kubernetes-azure-load-balancer-disble-tcp-reset}

مثال: `service.beta.kubernetes.io/azure-load-balancer-disable-tcp-reset: "false"`

استفاده‌شده روی: Service

این حاشیه‌نویسی فقط برای Serviceهایی کار می‌کند که از متعادل‌کننده بار استاندارد Azure بهره می‌برند. از این حاشیه‌نویسی روی Service استفاده می‌شود تا مشخص شود متعادل‌کننده بار هنگام پایان مهلت بیکاری، بازنشانی TCP را غیرفعال کند یا فعال. فعال بودن این قابلیت به برنامه‌ها کمک می‌کند رفتار قابل‌پیش‌بینی‌تری داشته باشند، پایان یافتن اتصال را تشخیص دهند، اتصال‌های منقضی‌شده را حذف کنند و اتصال‌های جدید برقرار کنند. مقدار آن می‌تواند true یا false باشد.

برای اطلاعات بیشتر، [Load Balancer TCP Reset](https://learn.microsoft.com/en-gb/azure/load-balancer/load-balancer-tcp-reset) را ببینید.

{{< note >}}
این حاشیه‌نویسی منسوخ شده است.
{{< /note >}}

### pod-security.kubernetes.io/enforce

نوع: برچسب

مثال: `pod-security.kubernetes.io/enforce: "baseline"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** یکی از `privileged`، `baseline` یا `restricted` باشد که با سطوح [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) متناظر هستند. به‌طور مشخص، برچسب `enforce` ایجاد هر Podای را که الزامات سطح تعیین‌شده را برآورده نکند، در Namespace برچسب‌خورده _ممنوع_ می‌کند.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح Namespace](/docs/concepts/security/pod-security-admission) را ببینید.

### pod-security.kubernetes.io/enforce-version

نوع: برچسب

مثال: `pod-security.kubernetes.io/enforce-version: "{{< skew currentVersion >}}"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** `latest` یا یک نسخه معتبر کوبرنتیز با قالب `v<major>.<minor>` باشد. این مقدار تعیین می‌کند که هنگام اعتبارسنجی یک Pod، کدام نسخه از سیاست‌های [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) اعمال شود.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح Namespace](/docs/concepts/security/pod-security-admission) را ببینید.

### pod-security.kubernetes.io/audit

نوع: برچسب

مثال: `pod-security.kubernetes.io/audit: "baseline"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** یکی از `privileged`، `baseline` یا `restricted` باشد که با سطوح [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) متناظر هستند. به‌طور مشخص، برچسب `audit` مانع ایجاد Podای که الزامات سطح تعیین‌شده را برآورده نکند در Namespace برچسب‌خورده نمی‌شود، اما این حاشیه‌نویسی را به آن Pod اضافه می‌کند.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح Namespace](/docs/concepts/security/pod-security-admission) را ببینید.

### pod-security.kubernetes.io/audit-version

نوع: برچسب

مثال: `pod-security.kubernetes.io/audit-version: "{{< skew currentVersion >}}"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** `latest` یا یک نسخه معتبر کوبرنتیز با قالب `v<major>.<minor>` باشد. این مقدار تعیین می‌کند که هنگام اعتبارسنجی یک Pod، کدام نسخه از سیاست‌های [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) اعمال شود.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح Namespace](/docs/concepts/security/pod-security-admission) را ببینید.

### pod-security.kubernetes.io/warn

نوع: برچسب

مثال: `pod-security.kubernetes.io/warn: "baseline"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** یکی از `privileged`، `baseline` یا `restricted` باشد که با سطوح [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) متناظر هستند. به‌طور مشخص، برچسب `warn` مانع ایجاد Podای که الزامات سطح تعیین‌شده را برآورده نکند در Namespace برچسب‌خورده نمی‌شود، اما پس از ایجاد آن، هشداری به کاربر برمی‌گرداند. این هشدارها هنگام ایجاد یا به‌روزرسانی آبجکت‌هایی که الگوی Pod دارند، مانند Deploymentها، Jobها، StatefulSetها و موارد مشابه نیز نمایش داده می‌شوند.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح Namespace](/docs/concepts/security/pod-security-admission) را ببینید.

### pod-security.kubernetes.io/warn-version

نوع: برچسب

مثال: `pod-security.kubernetes.io/warn-version: "{{< skew currentVersion >}}"`

استفاده‌شده روی: Namespace

مقدار این برچسب **باید** `latest` یا یک نسخهٔ معتبر کوبرنتیز با قالب `v<major>.<minor>` باشد. این مقدار تعیین می‌کند که هنگام اعتبارسنجی Pod ارسال‌شده، کدام نسخه از سیاست‌های [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) اعمال شود. توجه کنید که هنگام ایجاد یا به‌روزرسانی آبجکت‌های دارای قالب Pod، مانند Deploymentها، Jobها، StatefulSetها و موارد مشابه نیز هشدارها نمایش داده می‌شوند.

برای اطلاعات بیشتر، [اعمال امنیت Pod در سطح فضای نام (namespace)](/docs/concepts/security/pod-security-admission) را ببینید.

### rbac.authorization.kubernetes.io/autoupdate

نوع: حاشیه‌نویسی (annotation)

مثال: `rbac.authorization.kubernetes.io/autoupdate: "false"`

استفاده‌شده روی: ClusterRole، ClusterRoleBinding، Role، RoleBinding

اگر مقدار این حاشیه‌نویسی روی آبجکت‌های پیش‌فرض RBAC که API server ایجاد کرده است برابر `"true"` باشد، این آبجکت‌ها هنگام راه‌اندازی سرور به‌طور خودکار به‌روزرسانی می‌شوند تا مجوزها و سوژه‌های (subject) جاافتاده به آن‌ها افزوده شود؛ مجوزها و سوژه‌های اضافی نیز دست‌نخورده باقی می‌مانند. برای جلوگیری از به‌روزرسانی خودکار یک Role یا RoleBinding مشخص، مقدار این حاشیه‌نویسی را `"false"` قرار دهید. اگر آبجکت‌های RBAC خود را ایجاد کنید و مقدار این حاشیه‌نویسی را `"false"` بگذارید، دستور `kubectl auth reconcile` (که امکان تطبیق آبجکت‌های دلخواه RBAC موجود در یک {{< glossary_tooltip text="مانیفست" term_id="manifest" >}} را فراهم می‌کند) این حاشیه‌نویسی را رعایت می‌کند و مجوزها و سوژه‌های جاافتاده را به‌طور خودکار نمی‌افزاید.

### kubernetes.io/psp (منسوخ‌شده) {#kubernetes-io-psp}

نوع: حاشیه‌نویسی

مثال: `kubernetes.io/psp: restricted`

استفاده‌شده روی: Pod

این حاشیه‌نویسی فقط در صورت استفاده از آبجکت‌های [PodSecurityPolicy](/docs/concepts/security/pod-security-policy/) کاربرد داشت. کوبرنتیز نسخهٔ v{{< skew currentVersion >}} از API مربوط به PodSecurityPolicy پشتیبانی نمی‌کند.

هنگامی که کنترل‌کنندهٔ پذیرش PodSecurityPolicy یک Pod را می‌پذیرفت، این حاشیه‌نویسی را به آن Pod اضافه می‌کرد. مقدار حاشیه‌نویسی، نام PodSecurityPolicy به‌کاررفته برای اعتبارسنجی بود.

### seccomp.security.alpha.kubernetes.io/pod (بدون کارکرد) {#seccomp-security-alpha-kubernetes-io-pod}

نوع: حاشیه‌نویسی

استفاده‌شده روی: Pod

در نسخه‌های پیش از v1.25 کوبرنتیز می‌شد رفتار seccomp را با این حاشیه‌نویسی پیکربندی کرد. برای آشنایی با روش پشتیبانی‌شدهٔ تعیین محدودیت‌های seccomp برای یک Pod، [محدود کردن فراخوانی‌های سیستمی کانتینر با seccomp](/docs/tutorials/security/seccomp/) را ببینید.

### container.seccomp.security.alpha.kubernetes.io/[NAME] (بدون کارکرد) {#container-seccomp-security-alpha-kubernetes-io}

نوع: حاشیه‌نویسی

استفاده‌شده روی: Pod

در نسخه‌های پیش از v1.25 کوبرنتیز می‌شد رفتار seccomp را با این حاشیه‌نویسی پیکربندی کرد. برای آشنایی با روش پشتیبانی‌شدهٔ تعیین محدودیت‌های seccomp برای یک Pod، [محدود کردن فراخوانی‌های سیستمی کانتینر با seccomp](/docs/tutorials/security/seccomp/) را ببینید.

### snapshot.storage.kubernetes.io/allow-volume-mode-change

نوع: حاشیه‌نویسی

مثال: `snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"`

استفاده‌شده روی: VolumeSnapshotContent

مقدار این حاشیه‌نویسی می‌تواند `true` یا `false` باشد. این مقدار تعیین می‌کند که آیا کاربر می‌تواند هنگام ایجاد یک PersistentVolumeClaim از روی یک VolumeSnapshot، حالت حجم (volume) مبدأ را تغییر دهد یا نه.

برای اطلاعات بیشتر، [تبدیل حالت حجم یک Snapshot](/docs/concepts/storage/volume-snapshots/#convert-volume-mode) و [مستندات توسعه‌دهندگان CSI کوبرنتیز](https://kubernetes-csi.github.io/docs/) را ببینید.

### scheduler.alpha.kubernetes.io/critical-pod (منسوخ‌شده)

نوع: حاشیه‌نویسی

مثال: `scheduler.alpha.kubernetes.io/critical-pod: ""`

استفاده‌شده روی: Pod

این حاشیه‌نویسی به control plane کوبرنتیز اعلام می‌کند که یک Pod حیاتی است تا descheduler آن را حذف نکند.

{{< note >}}
از نسخهٔ v1.16 این حاشیه‌نویسی حذف شد و [اولویت Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) جای آن را گرفت.
{{< /note >}}

### jobset.sigs.k8s.io/jobset-name

نوع: برچسب، حاشیه‌نویسی

مثال:  `jobset.sigs.k8s.io/jobset-name: "my-jobset"`

استفاده‌شده روی: Jobها، Podها

این برچسب یا حاشیه‌نویسی نام JobSet دربرگیرندهٔ یک Job یا Pod را ذخیره می‌کند. [JobSet](https://jobset.sigs.k8s.io) یک API افزونه است که می‌توانید آن را در کلاستر کوبرنتیز خود مستقر کنید.

### jobset.sigs.k8s.io/replicatedjob-replicas

نوع: برچسب، حاشیه‌نویسی

مثال: `jobset.sigs.k8s.io/replicatedjob-replicas: "5"`

استفاده‌شده روی: Jobها، Podها

این برچسب یا حاشیه‌نویسی تعداد رپلیکاهای یک ReplicatedJob را مشخص می‌کند.

### jobset.sigs.k8s.io/replicatedjob-name

نوع: برچسب، حاشیه‌نویسی

مثال: `jobset.sigs.k8s.io/replicatedjob-name: "my-replicatedjob"`

استفاده‌شده روی: Jobها، Podها

این برچسب یا حاشیه‌نویسی نام Job تکثیرشده‌ای (replicated job) را که این Job یا Pod بخشی از آن است، ذخیره می‌کند.

### jobset.sigs.k8s.io/job-index

نوع: برچسب، حاشیه‌نویسی

مثال: `jobset.sigs.k8s.io/job-index: "0"`

استفاده‌شده روی: Jobها، Podها

کنترل‌کنندهٔ JobSet این برچسب یا حاشیه‌نویسی را روی Jobها و Podهای فرزند تنظیم می‌کند. مقدار آن، اندیس رپلیکای Job درون ReplicatedJob والد است.

### jobset.sigs.k8s.io/job-key

نوع: برچسب، حاشیه‌نویسی

مثال: `jobset.sigs.k8s.io/job-key: "0f1e93893c4cb372080804ddb9153093cb0d20cefdd37f653e739c232d363feb"`

استفاده‌شده روی: Jobها، Podها

کنترل‌کنندهٔ JobSet این برچسب (و نیز حاشیه‌نویسی‌ای با همین کلید) را روی Jobها و Podهای فرزند یک JobSet تنظیم می‌کند. مقدار آن، هش SHA256 نام Job همراه با فضای نام آن است.

### alpha.jobset.sigs.k8s.io/exclusive-topology

نوع: حاشیه‌نویسی

مثال: `alpha.jobset.sigs.k8s.io/exclusive-topology: "zone"`

استفاده‌شده روی: JobSetها، Jobها

با تنظیم این برچسب یا حاشیه‌نویسی روی یک [JobSet](https://jobset.sigs.k8s.io) می‌توانید جای‌گیری انحصاری Jobها را در هر گروه توپولوژی تضمین کنید. همچنین می‌توانید این برچسب یا حاشیه‌نویسی را روی قالب یک Job تکثیرشده تعریف کنید. برای اطلاعات بیشتر، مستندات JobSet را بخوانید.

### alpha.jobset.sigs.k8s.io/node-selector

نوع: حاشیه‌نویسی

مثال: `alpha.jobset.sigs.k8s.io/node-selector: "true"`

استفاده‌شده روی: Jobها، Podها

این برچسب یا حاشیه‌نویسی را می‌توان روی یک JobSet اعمال کرد. در صورت تنظیم آن، کنترل‌کنندهٔ JobSet با افزودن انتخابگرهای (selector) نود و tolerationها، Jobها و Podهای متناظر آن‌ها را تغییر می‌دهد. به این ترتیب، جای‌گیری انحصاری Jobها در هر دامنهٔ توپولوژی تضمین می‌شود و زمان‌بندی این Podها بر اساس راهبرد انتخاب‌شده به نودهای مشخصی محدود می‌ماند.

### alpha.jobset.sigs.k8s.io/namespaced-job

نوع: برچسب

مثال: `alpha.jobset.sigs.k8s.io/namespaced-job: "default_myjobset-replicatedjob-0"`

استفاده‌شده روی: Nodeها

این برچسب به‌صورت دستی یا خودکار (مثلاً با یک cluster autoscaler) روی نودها تنظیم می‌شود. وقتی مقدار `alpha.jobset.sigs.k8s.io/node-selector` برابر `"true"` باشد، کنترل‌کنندهٔ JobSet یک nodeSelector برای این برچسب نود اضافه می‌کند (و همراه با آن، toleration مربوط به taint با نام `alpha.jobset.sigs.k8s.io/no-schedule` را که در ادامه توضیح داده شده است نیز می‌افزاید).

### alpha.jobset.sigs.k8s.io/no-schedule

نوع: Taint

مثال: `alpha.jobset.sigs.k8s.io/no-schedule: "NoSchedule"`

استفاده‌شده روی: Nodeها

این taint به‌صورت دستی یا خودکار (مثلاً با یک cluster autoscaler) روی نودها تنظیم می‌شود. وقتی مقدار `alpha.jobset.sigs.k8s.io/node-selector` برابر `"true"` باشد، کنترل‌کنندهٔ JobSet یک toleration برای این taint نود اضافه می‌کند (و همراه با آن، انتخابگر نود مربوط به برچسب `alpha.jobset.sigs.k8s.io/namespaced-job` را که پیش‌تر توضیح داده شد نیز می‌افزاید).

### jobset.sigs.k8s.io/coordinator

نوع: حاشیه‌نویسی، برچسب

مثال: `jobset.sigs.k8s.io/coordinator: "myjobset-workers-0-0.headless-svc"`

استفاده‌شده روی: Jobها، Podها

اگر در spec یک [JobSet](https://jobset.sigs.k8s.io) فیلد `.spec.coordinator` تعریف شده باشد، این حاشیه‌نویسی یا برچسب روی Jobها و Podها قرار می‌گیرد تا یک نقطهٔ پایانی شبکهٔ پایدار را برای دسترسی به Pod هماهنگ‌کننده ذخیره کند.

## حاشیه‌نویسی‌های ویژهٔ ممیزی

<!-- sorted by annotation -->
- [`authorization.k8s.io/decision`](/docs/reference/labels-annotations-taints/audit-annotations/#authorization-k8s-io-decision)
- [`authorization.k8s.io/reason`](/docs/reference/labels-annotations-taints/audit-annotations/#authorization-k8s-io-reason)
- [`insecure-sha1.invalid-cert.kubernetes.io/$hostname`](/docs/reference/labels-annotations-taints/audit-annotations/#insecure-sha1-invalid-cert-kubernetes-io-hostname)
- [`missing-san.invalid-cert.kubernetes.io/$hostname`](/docs/reference/labels-annotations-taints/audit-annotations/#missing-san-invalid-cert-kubernetes-io-hostname)
- [`pod-security.kubernetes.io/audit-violations`](/docs/reference/labels-annotations-taints/audit-annotations/#pod-security-kubernetes-io-audit-violations)
- [`pod-security.kubernetes.io/enforce-policy`](/docs/reference/labels-annotations-taints/audit-annotations/#pod-security-kubernetes-io-enforce-policy)
- [`pod-security.kubernetes.io/exempt`](/docs/reference/labels-annotations-taints/audit-annotations/#pod-security-kubernetes-io-exempt)
- [`validation.policy.admission.k8s.io/validation_failure`](/docs/reference/labels-annotations-taints/audit-annotations/#validation-policy-admission-k8s-io-validation-failure)
  
برای جزئیات بیشتر، [حاشیه‌نویسی‌های ممیزی](/docs/reference/labels-annotations-taints/audit-annotations/) را ببینید.

## kubeadm

### kubeadm.alpha.kubernetes.io/cri-socket (منسوخ‌شده) {#kubeadm-alpha-kubernetes-io-cri-socket}

نوع: حاشیه‌نویسی

مثال: `kubeadm.alpha.kubernetes.io/cri-socket: unix:///run/containerd/container.sock`

استفاده‌شده روی: Node

{{< note >}}
این حاشیه‌نویسی از نسخهٔ v1.34 منسوخ شده است و kubeadm دیگر آن را به‌طور فعال تنظیم نمی‌کند و به کار نمی‌برد.
{{< /note >}}


### kubeadm.kubernetes.io/etcd.advertise-client-urls

نوع: حاشیه‌نویسی

مثال: `kubeadm.kubernetes.io/etcd.advertise-client-urls: https://172.17.0.18:2379`

استفاده‌شده روی: Pod

ابزار kubeadm این حاشیه‌نویسی را روی Podهای etcd با مدیریت محلی قرار می‌دهد تا فهرست URLهایی را که کلاینت‌های etcd باید به آن‌ها متصل شوند نگه دارد. این حاشیه‌نویسی عمدتاً برای بررسی سلامت کلاستر etcd به کار می‌رود.

### kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint

نوع: حاشیه‌نویسی

مثال: `kubeadm.kubernetes.io/kube-apiserver.advertise-address.endpoint: https://172.17.0.18:6443`

استفاده‌شده روی: Pod

ابزار kubeadm این حاشیه‌نویسی را روی Podهای `kube-apiserver` با مدیریت محلی قرار می‌دهد تا نقطهٔ پایانی نشانی و درگاه اعلام‌شدهٔ آن نمونه از API server را نگه دارد.

### kubeadm.kubernetes.io/component-config.hash

نوع: حاشیه‌نویسی

مثال: `kubeadm.kubernetes.io/component-config.hash: 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae`

استفاده‌شده روی: ConfigMap

ابزار kubeadm این حاشیه‌نویسی را روی ConfigMapهایی قرار می‌دهد که برای پیکربندی مؤلفه‌ها مدیریت می‌کند. این حاشیه‌نویسی شامل یک هش (SHA-256) است که با آن مشخص می‌شود آیا کاربر برای یک مؤلفهٔ خاص، تنظیماتی متفاوت با مقادیر پیش‌فرض kubeadm اعمال کرده است یا نه.

### node-role.kubernetes.io/control-plane

نوع: برچسب

استفاده‌شده روی: Node

این برچسب نشانگری است که مشخص می‌کند نود برای اجرای مؤلفه‌های control plane به کار می‌رود. ابزار kubeadm این برچسب را روی نودهای control plane تحت مدیریت خود اعمال می‌کند. سایر ابزارهای مدیریت کلاستر نیز معمولاً این taint را تنظیم می‌کنند.

با افزودن این برچسب به نودهای control plane می‌توانید زمان‌بندی Podها را فقط روی این نودها ساده‌تر کنید یا از اجرای Podها روی control plane جلوگیری کنید. اگر این برچسب تنظیم شده باشد، [کنترل‌کنندهٔ EndpointSlice](/docs/concepts/services-networking/topology-aware-routing/#implementation-control-plane) هنگام محاسبهٔ راهنماهای آگاه از توپولوژی (Topology Aware Hints) آن نود را نادیده می‌گیرد.

### node-role.kubernetes.io/*

نوع: برچسب

مثال: `node-role.kubernetes.io/gpu: gpu`

استفاده‌شده روی: Node

این برچسب اختیاری زمانی روی یک نود اعمال می‌شود که بخواهید نقش آن نود را مشخص کنید. نقش نود (متن پس از `/` در کلید برچسب) را می‌توان تعیین کرد، مشروط بر اینکه کل کلید از قواعد [نحو](/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set) برچسب‌های آبجکت پیروی کند.

کوبرنتیز یک نقش نود مشخص به نام **control-plane** تعریف می‌کند. برای علامت‌گذاری این نقش نود می‌توانید از برچسب [`node-role.kubernetes.io/control-plane`](#node-role-kubernetes-io-control-plane) استفاده کنید.

### node-role.kubernetes.io/control-plane {#node-role-kubernetes-io-control-plane-taint}

نوع: Taint

مثال: `node-role.kubernetes.io/control-plane:NoSchedule`

استفاده‌شده روی: Node

ابزار kubeadm این taint را روی نودهای control plane اعمال می‌کند تا قرارگیری Podها روی این نودها را محدود کند و فقط به Podهای مشخصی اجازهٔ زمان‌بندی روی آن‌ها را بدهد.

اگر این taint اعمال شده باشد، نودهای control plane فقط اجازهٔ زمان‌بندی بارهای کاری حیاتی را روی خود می‌دهند. می‌توانید با دستور زیر این taint را به‌صورت دستی از یک نود مشخص حذف کنید.

```shell
kubectl taint nodes <node-name> node-role.kubernetes.io/control-plane:NoSchedule-
```

### node-role.kubernetes.io/master (منسوخ‌شده) {#node-role-kubernetes-io-master-taint}

نوع: Taint

استفاده‌شده روی: Node

مثال: `node-role.kubernetes.io/master:NoSchedule`

ابزار kubeadm پیش‌تر این taint را روی نودهای control plane اعمال می‌کرد تا فقط بارهای کاری حیاتی روی آن‌ها زمان‌بندی شوند. اکنون taint با نام [`node-role.kubernetes.io/control-plane`](#node-role-kubernetes-io-control-plane-taint) جایگزین آن شده است. ابزار kubeadm دیگر این taint منسوخ‌شده را تنظیم نمی‌کند و به کار نمی‌برد.

### resource.kubernetes.io/admin-access {resource-kubernetes-io-admin-access}

نوع: برچسب

مثال: `resource.kubernetes.io/admin-access: "true"`

استفاده‌شده روی: Namespace

از این برچسب برای اعطای دسترسی مدیریتی به برخی از نوع‌های API گروه resource.k8s.io در یک فضای نام استفاده می‌شود. وقتی این برچسب با مقدار `"true"` (با حساسیت به بزرگی و کوچکی حروف) روی یک فضای نام تنظیم شود، می‌توان از `adminAccess: true` در همهٔ نوع‌های API فضای‌نام‌دار `resource.k8s.io` استفاده کرد. در حال حاضر، این مجوز بر آبجکت‌های `ResourceClaim` و `ResourceClaimTemplate` اعمال می‌شود.

برای اطلاعات بیشتر، [دسترسی مدیریتی در تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#admin-access) را ببینید.

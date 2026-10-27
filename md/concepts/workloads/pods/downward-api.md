---
title: Downward API
content_type: concept
weight: 170
description: >
  دو روش برای در اختیار قرار دادن فیلدهای Pod و کانتینر به یک کانتینر در حال اجرا وجود دارد:
  متغیرهای محیطی، و فایل‌هایی که توسط یک نوع حجم (volume) ویژه پر می‌شوند.
  این دو روش در کنار هم برای در اختیار قرار دادن فیلدهای Pod و کانتینر، downward API نامیده می‌شوند.
---

<!-- overview -->

گاهی لازم است یک کانتینر اطلاعاتی درباره خودش داشته باشد، بدون آن‌که بیش از حد به کوبرنتیز وابسته باشد. _downward API_ به کانتینرها امکان می‌دهد بدون استفاده از کلاینت کوبرنتیز یا API server، اطلاعات مربوط به خودشان یا کلاستر را دریافت کنند.

برای مثال، یک برنامه موجود را در نظر بگیرید که فرض می‌کند یک متغیر محیطی شناخته‌شده و مشخص، شناسه‌ای یکتا را نگهداری می‌کند. یک راه این است که برنامه را در یک لایه واسط بپیچید، اما این کار خسته‌کننده و مستعد خطاست و با هدف وابستگی کم (low coupling) در تضاد است. گزینه بهتر این است که از نام Pod به‌عنوان شناسه استفاده شود و نام Pod درون همان متغیر محیطی شناخته‌شده تزریق گردد.

در کوبرنتیز دو روش برای در اختیار قرار دادن فیلدهای Pod و کانتینر به یک کانتینر در حال اجرا وجود دارد:

* به‌صورت [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* به‌صورت [فایل‌هایی در یک حجم `downwardAPI`](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

این دو روش در کنار هم برای در اختیار قرار دادن فیلدهای Pod و کانتینر، _downward API_ نامیده می‌شوند.

<!-- body -->

## فیلدهای در دسترس {#available-fields}

تنها برخی از فیلدهای API کوبرنتیز از طریق downward API در دسترس هستند. این بخش فهرست فیلدهایی را که می‌توانید در دسترس قرار دهید ارائه می‌کند.

می‌توانید اطلاعات فیلدهای در دسترس در سطح Pod را با استفاده از `fieldRef` منتقل کنید.
در سطح API، بخش `spec` یک Pod همیشه دست‌کم یک [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) تعریف می‌کند.
می‌توانید اطلاعات فیلدهای در دسترس در سطح کانتینر را با استفاده از `resourceFieldRef` منتقل کنید.

### اطلاعات در دسترس از طریق `fieldRef` {#downwardapi-fieldRef}

برخی از فیلدهای سطح Pod را می‌توانید یا به‌صورت متغیر محیطی یا با استفاده از یک حجم `downwardAPI` در اختیار کانتینر قرار دهید. فیلدهای در دسترس از طریق هر دو سازوکار عبارت‌اند از:

`metadata.name`
: نام pod

`metadata.namespace`
: {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} (namespace) مربوط به pod

`metadata.uid`
: شناسه یکتای pod

`metadata.annotations['<KEY>']`
: مقدار {{< glossary_tooltip text="حاشیه‌نویسی" term_id="annotation" >}} (annotation) مربوط به pod با نام `<KEY>` (برای مثال، `metadata.annotations['myannotation']`)

`metadata.labels['<KEY>']`
: مقدار متنی {{< glossary_tooltip text="برچسب" term_id="label" >}} (label) مربوط به pod با نام `<KEY>` (برای مثال، `metadata.labels['mylabel']`)

اطلاعات زیر از طریق متغیرهای محیطی در دسترس است
**اما نه به‌عنوان fieldRef در حجم downwardAPI**:

`spec.serviceAccountName`
: نام {{< glossary_tooltip text="service account" term_id="service-account" >}} مربوط به pod

`spec.nodeName`
: نام {{< glossary_tooltip term_id="node" text="نود">}}ی که Pod روی آن در حال اجراست

`status.hostIP`
: آدرس IP اصلی نودی که Pod به آن تخصیص داده شده است

`status.hostIPs`
: آدرس‌های IP، نسخه dual-stack مربوط به `status.hostIP` هستند و اولین آدرس همیشه با `status.hostIP` یکسان است.

`status.podIP`
: آدرس IP اصلی pod (معمولاً آدرس IPv4 آن)

`status.podIPs`
: آدرس‌های IP، نسخه dual-stack مربوط به `status.podIP` هستند و اولین آدرس همیشه با `status.podIP` یکسان است

اطلاعات زیر از طریق `fieldRef` در یک حجم `downwardAPI` در دسترس است،
**اما نه به‌صورت متغیر محیطی**:

`metadata.labels`
: تمام برچسب‌های pod، با قالب `label-key="escaped-label-value"` و هر برچسب در یک خط

`metadata.annotations`
: تمام حاشیه‌نویسی‌های pod، با قالب `annotation-key="escaped-annotation-value"` و هر حاشیه‌نویسی در یک خط

### اطلاعات در دسترس از طریق `resourceFieldRef` {#downwardapi-resourceFieldRef}

این فیلدهای سطح کانتینر به شما امکان می‌دهند اطلاعاتی درباره
[درخواست‌ها و محدودیت‌ها (requests and limits)](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
برای منابعی مانند CPU و حافظه ارائه دهید.

{{< note >}}
{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}
منابع CPU و حافظه کانتینر را می‌توان در زمان اجرای کانتینر تغییر اندازه داد.
در این صورت، حجم downward API به‌روزرسانی می‌شود،
اما متغیرهای محیطی تا زمانی که کانتینر راه‌اندازی مجدد نشود به‌روزرسانی نخواهند شد.
برای جزئیات بیشتر، [تغییر اندازه منابع CPU و حافظه تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) را ببینید.
{{< /note >}}


`resource: limits.cpu`
: محدودیت CPU یک کانتینر

`resource: requests.cpu`
: درخواست CPU یک کانتینر

`resource: limits.memory`
: محدودیت حافظه یک کانتینر

`resource: requests.memory`
: درخواست حافظه یک کانتینر

`resource: limits.hugepages-*`
: محدودیت hugepages یک کانتینر

`resource: requests.hugepages-*`
: درخواست hugepages یک کانتینر

`resource: limits.ephemeral-storage`
: محدودیت ephemeral-storage یک کانتینر

`resource: requests.ephemeral-storage`
: درخواست ephemeral-storage یک کانتینر

#### اطلاعات جایگزین برای محدودیت منابع {#fallback-information-for-resource-limits}

اگر محدودیت‌های CPU و حافظه برای یک کانتینر مشخص نشده باشند و شما بخواهید با استفاده از downward API این اطلاعات را در دسترس قرار دهید، kubelet به‌طور پیش‌فرض بیشینه مقدار قابل تخصیص (allocatable) برای CPU و حافظه را بر پایه محاسبه [منابع قابل تخصیص نود (node allocatable)](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) در اختیار قرار می‌دهد.

## {{% heading "whatsnext" %}}

می‌توانید درباره [حجم‌های `downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) مطالعه کنید.

می‌توانید با استفاده از downward API اطلاعات سطح کانتینر یا Pod را در دسترس قرار دهید:
* به‌صورت [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* به‌صورت [فایل‌هایی در حجم `downwardAPI`](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

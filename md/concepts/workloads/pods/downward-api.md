---
title: Downward API
content_type: concept
weight: 170
description: >
  دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر برای یک کانتینر در حال اجرا وجود دارد:
  متغیرهای محیطی، و فایل‌هایی که یک نوع خاص از حجم (volume) آن‌ها را پر می‌کند.
  این دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر، روی هم downward API نامیده می‌شوند.
---

<!-- overview -->

گاهی مفید است که یک کانتینر بدون وابستگی بیش از حد به کوبرنتیز، اطلاعاتی درباره‌ی خودش داشته باشد. به کمک _downward API_، کانتینرها می‌توانند بدون استفاده از کلاینت کوبرنتیز یا API server، اطلاعاتی درباره‌ی خود یا کلاستر به دست آورند.

برای نمونه، برنامه‌ای موجود را در نظر بگیرید که فرض می‌کند یک متغیر محیطی شناخته‌شده‌ی مشخص، شناسه‌ای یکتا را در خود نگه می‌دارد. یک راه این است که برنامه را درون پوششی (wrapper) قرار دهید، اما این کار خسته‌کننده و مستعد خطاست و با هدف کاهش وابستگی نیز در تضاد است. راه بهتر این است که از نام Pod به‌عنوان شناسه استفاده کنید و نام Pod را در همان متغیر محیطی شناخته‌شده تزریق کنید.

در کوبرنتیز، دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر برای یک کانتینر در حال اجرا وجود دارد:

* به‌صورت [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* به‌صورت [فایل‌هایی در یک حجم `downwardAPI`](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

این دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر، روی هم _downward API_ نامیده می‌شوند.

<!-- body -->

## فیلدهای در دسترس

تنها برخی از فیلدهای API کوبرنتیز از طریق downward API در دسترس هستند. این بخش فهرست فیلدهایی را که می‌توانید در دسترس قرار دهید ارائه می‌کند.

می‌توانید اطلاعات فیلدهای در دسترس در سطح Pod را با استفاده از `fieldRef` منتقل کنید. در سطح API، بخش `spec` هر Pod همواره دست‌کم یک [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) را تعریف می‌کند. اطلاعات فیلدهای در دسترس در سطح Container را نیز می‌توانید با استفاده از `resourceFieldRef` منتقل کنید.

### اطلاعات در دسترس از طریق `fieldRef` {#downwardapi-fieldRef}

برخی از فیلدهای سطح Pod را می‌توانید یا به‌صورت متغیر محیطی یا با استفاده از یک حجم `downwardAPI` در اختیار کانتینر قرار دهید. فیلدهایی که از طریق هر دو سازوکار در دسترس هستند عبارت‌اند از:

`metadata.name`
: نام پاد

`metadata.namespace`
: {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} پاد

`metadata.uid`
: شناسه‌ی یکتای پاد

`metadata.annotations['<KEY>']`
: مقدار {{< glossary_tooltip text="حاشیه‌نویسی" term_id="annotation" >}} پاد با نام `<KEY>` (برای مثال، `metadata.annotations['myannotation']`)

`metadata.labels['<KEY>']`
: مقدار متنی {{< glossary_tooltip text="برچسب" term_id="label" >}} پاد با نام `<KEY>` (برای مثال، `metadata.labels['mylabel']`)

اطلاعات زیر از طریق متغیرهای محیطی در دسترس هستند، **اما نه به‌صورت fieldRef در حجم downwardAPI**:

`spec.serviceAccountName`
: نام {{< glossary_tooltip text="حساب سرویس" term_id="service-account" >}} پاد

`spec.nodeName`
: نام {{< glossary_tooltip term_id="node" text="نودی">}} که پاد روی آن اجرا می‌شود

`status.hostIP`
: نشانی IP اصلی نودی که پاد به آن اختصاص داده شده است

`status.hostIPs`
: نشانی‌های IP که نسخه‌ی دوپشته‌ای (dual-stack) از `status.hostIP` هستند؛ نخستین نشانی همواره با `status.hostIP` یکسان است.

`status.podIP`
: نشانی IP اصلی پاد (معمولاً نشانی IPv4 آن)

`status.podIPs`
: نشانی‌های IP که نسخه‌ی دوپشته‌ای از `status.podIP` هستند؛ نخستین نشانی همواره با `status.podIP` یکسان است

اطلاعات زیر از طریق `fieldRef` در یک حجم `downwardAPI` در دسترس هستند، **اما نه به‌صورت متغیرهای محیطی**:

`metadata.labels`
: همه‌ی برچسب‌های پاد، با قالب `label-key="escaped-label-value"` و هر برچسب در یک خط

`metadata.annotations`
: همه‌ی حاشیه‌نویسی‌های پاد، با قالب `annotation-key="escaped-annotation-value"` و هر حاشیه‌نویسی در یک خط

### اطلاعات در دسترس از طریق `resourceFieldRef` {#downwardapi-resourceFieldRef}

با این فیلدهای سطح کانتینر می‌توانید اطلاعاتی درباره‌ی [درخواست‌ها و محدودیت‌ها](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) برای منابعی مانند CPU و حافظه فراهم کنید.

{{< note >}}
{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}
منابع CPU و حافظه‌ی کانتینر را می‌توان در حین اجرای کانتینر تغییر اندازه داد. در این صورت، حجم downward API به‌روزرسانی می‌شود، اما متغیرهای محیطی تا زمانی که کانتینر دوباره راه‌اندازی نشود به‌روزرسانی نمی‌شوند. برای جزئیات بیشتر، [تغییر اندازه‌ی منابع CPU و حافظه‌ی اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) را ببینید.
{{< /note >}}


`resource: limits.cpu`
: محدودیت CPU کانتینر

`resource: requests.cpu`
: درخواست CPU کانتینر

`resource: limits.memory`
: محدودیت حافظه‌ی کانتینر

`resource: requests.memory`
: درخواست حافظه‌ی کانتینر

`resource: limits.hugepages-*`
: محدودیت hugepages کانتینر

`resource: requests.hugepages-*`
: درخواست hugepages کانتینر

`resource: limits.ephemeral-storage`
: محدودیت ذخیره‌سازی موقت (ephemeral-storage) کانتینر

`resource: requests.ephemeral-storage`
: درخواست ذخیره‌سازی موقت کانتینر

#### اطلاعات جایگزین برای محدودیت‌های منابع

اگر محدودیت‌های CPU و حافظه برای یک کانتینر مشخص نشده باشند و شما بکوشید این اطلاعات را با downward API در دسترس قرار دهید، kubelet به‌طور پیش‌فرض بیشینه‌ی مقدار قابل تخصیص CPU و حافظه را بر پایه‌ی محاسبه‌ی [منابع قابل تخصیص نود](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) در دسترس قرار می‌دهد.

## {{% heading "whatsnext" %}}

می‌توانید درباره‌ی [حجم‌های `downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) مطالعه کنید.

می‌توانید استفاده از downward API را برای در دسترس قرار دادن اطلاعات سطح کانتینر یا Pod امتحان کنید:
* به‌صورت [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* به‌صورت [فایل‌هایی در حجم `downwardAPI`](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

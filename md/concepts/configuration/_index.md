---
title: "پیکربندی"
weight: 80
description: >
  سازوکارهای پیکربندی در کوبرنتیز.
simple_list: true
---

کوبرنتیز روش‌هایی برای _جداسازی پیکربندی از کد_ فراهم می‌کند. این یک رویهٔ رایج
است که با DevOps به‌عنوان یک رویه و با معماری بومی ابر (cloud native) هم‌راستاست.

اگر یک {{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} دارید که
امکان پیکربندی جداگانه را فراهم می‌کند، می‌توانید **همان** کد برنامه را در
زمینه‌های مختلف مستقر کنید. برای نمونه، می‌توانید آزمون‌ها را روی ایمیج ساخته‌شده اجرا کنید و
سپس دقیقاً همان ایمیج را در محیط عملیاتی اجرا کنید. این کار در مقایسه با حالتی که برنامه را
برای آزمون به یک شیوه و در محیط عملیاتی به شیوه‌ای دیگر مستقر کنید،
اطمینان بیشتری به آزمون‌هایتان می‌دهد.

برای آشنایی با پیکربندی ابزار خط فرمان `kubectl`،
مطلب [پیکربندی دسترسی به چندین کلاستر](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) را بخوانید.

<!-- body -->
## APIهای مرتبط با پیکربندی در کوبرنتیز {#api-kinds}

کوبرنتیز دو نوع (kind) اصلی API فراهم می‌کند که می‌توانید از آن‌ها برای ذخیرهٔ پیکربندی استفاده کنید،
به‌گونه‌ای که آمادهٔ بارگذاری و استفاده توسط یک Pod (یا جزء دیگر) باشد:
[ConfigMap](/docs/concepts/configuration/configmap/) و
[Secret](/docs/concepts/configuration/secret/).

انواع API با کاربرد ویژهٔ
[CertificateSigningRequest](/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests)
و
[ClusterTrustBundle](/docs/reference/access-authn-authz/certificate-signing-requests/#cluster-trust-bundles)
نیز داده‌های پیکربندی‌ای را نگه می‌دارند که به برخی موارد خاص،
مانند پیکربندی TLS، مربوط است.

همهٔ این سازوکارهای پیکربندی، حتی برای گواهی‌ها، به‌گونه‌ای طراحی شده‌اند که پیکربندی
بتواند میان چندین Pod مجدداً استفاده و به اشتراک گذاشته شود. معمولاً لازم نیست پیکربندی را
برای هر Pod یک بار بنویسید، و تا حد امکان باید برنامه‌ها را طوری طراحی کنید که بتوانند با
پیکربندی مشترک کار کنند.

برای آشنایی با استفاده از پیکربندی در برنامه‌هایتان، مطلب
[تزریق داده به برنامه‌ها](/docs/tasks/inject-data-application/) را بخوانید.

### ConfigMapها

{{< glossary_definition term_id="configmap" prepend="A ConfigMap is" length="all" >}}

### Secretها

Secret آبجکتی است که مقداری دادهٔ محرمانه،
مانند گذرواژه، توکن یا کلید را در خود دارد.

Secretها مشابه {{< glossary_tooltip text="ConfigMapها" term_id="configmap" >}} هستند،
اما به‌طور خاص برای نگهداری داده‌های محرمانه در نظر گرفته شده‌اند. صفحهٔ مربوط به [Secretها](/docs/concepts/configuration/secret/) را بخوانید
تا با مزایا (و محدودیت‌های) مربوط به امنیت اطلاعات و Secretها آشنا شوید.

## پیکربندی از طریق کانتینرهای sidecar یا کانتینرهای init {#config-helper-overview}

همچنین می‌توانید از یک
{{< glossary_tooltip text="کانتینر init" term_id="init-container" >}} یا یک
{{< glossary_tooltip text="کانتینر sidecar" term_id="sidecar-container" >}}
برای فراهم کردن پیکربندی برای بار کاری خود استفاده کنید.

این روش زمانی سودمند است که از قبل ابزاری بیرون از کوبرنتیز برای ذخیرهٔ
پیکربندی، کلیدهای امنیتی یا سایر اطلاعاتی دارید که کانتینرهای شما باید
از آن‌ها استفاده کنند و نباید در ایمیج‌های کانتینر ذخیره شوند.

### کانتینر کمکی sidecar {#config-helper-sidecar}

یک کمک‌کنندهٔ پیکربندی از نوع _sidecar_ در همان Podی اجرا می‌شود که کانتینر برنامه در آن است، بنابراین
هر Pod sidecar مخصوص به خود را دارد. یک sidecar پیکربندی معمولی، داده‌های پیکربندی را از طریق
شبکهٔ Pod دریافت می‌کند و سپس آن را در یک {{< glossary_tooltip text="حجم (volume)" term_id="volume" >}}
می‌نویسد که در هر دو کانتینر mount شده است.

گونه‌های متعددی از این الگوی پایه وجود دارد که همچنان در آن‌ها یک کانتینر
کمکی پیکربندی را برای مصرف کانتینر برنامه می‌نویسد.

### کانتینر کمکی init {#config-helper-init-container}

Podها می‌توانند کانتینرهای _init_ داشته باشند که پیش از برنامهٔ اصلی آغاز می‌شوند. برخلاف sidecarها،
کانتینرهای init پیش از آغاز کانتینرهای اصلی (برنامهٔ) Pod به پایان می‌رسند، بنابراین
پیکربندی تنها یک بار تنظیم می‌شود.

برای پیکربندی با استفاده از کانتینرهای init دو گزینهٔ اصلی دارید:

#### پیکربندی از طریق سیستم فایل {#init-container-shared-volume}

در این گزینه، کانتینر init پیکربندی را دریافت می‌کند و آن را در
یک یا چند فایل می‌نویسد، که معمولاً در یک
{{< glossary_tooltip text="حجم (volume)" term_id="volume" >}} محلیِ Pod قرار دارند.

#### پیکربندی از طریق متغیرهای محیطی {#init-container-env-files}

{{< feature-state feature_gate_name="EnvFiles" >}}

این کار با استفاده از یک حجم محلی انجام می‌شود، اما تنها کانتینر init آن حجم را mount می‌کند. سپس kubelet پیش از آغاز کانتینر برنامه، از آن حجم می‌خواند.

برای اطلاعات بیشتر، مطلب [تعریف مقادیر متغیرهای محیطی با استفاده از یک کانتینر init](/docs/tasks/inject-data-application/define-environment-variable-via-file/)
را بخوانید.

## پیکربندی کلاستر

این بخش از مستندات دربارهٔ پیکربندی است. با این حال،
اگر در حال انجام پیکربندی در سطح پلتفرم یا سطح کلاستر هستید،
صفحه‌های [مدیریت کلاستر](/docs/concepts/cluster-administration/) را بخوانید
و فهرست [وظایف مدیریت کلاستر](/docs/tasks/administer-cluster/) را مرور کنید.

## {{% heading "whatsnext" %}}

پیوندهای زیر همگی با ایدهٔ کلی _پیکربندی_ و کوبرنتیز مرتبط‌اند:

* [پیکربندی Podها و کانتینرها](/docs/tasks/configure-pod-container/)
* [تزریق داده به برنامه‌ها](/docs/tasks/inject-data-application/)
* [سیاست‌ها](/docs/concepts/policy/)، شکل دیگری از پیکربندی
* [مدیریت آبجکت‌های کوبرنتیز با استفاده از فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/declarative-config/)،
  که دربارهٔ {{< glossary_tooltip text="مانیفست‌های" term_id="manifest" >}} کوبرنتیز است
  * [مدیریت آبجکت‌های کوبرنتیز](/docs/concepts/overview/working-with-objects/object-management/) نیز دربارهٔ مدیریت / پیکربندی آبجکت‌هاست
* [پیکربندی Redis با استفاده از یک ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)
  (یک آموزش)
* [به‌روزرسانی پیکربندی از طریق یک ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/)
  (آموزشی دیگر)

و می‌توانید [فهرست قالب‌های فایل پیکربندی](/docs/reference/config-api/)
را در بخش مرجع مرور کنید.

در **این** بخش از مستندات، می‌توانید دربارهٔ موارد زیر بخوانید:

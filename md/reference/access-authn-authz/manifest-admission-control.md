---
reviewers:
- liggitt
- jpbetz
title: کنترل پذیرش مبتنی بر مانیفست
content_type: concept
---

<!-- overview -->

{{< feature-state feature_gate_name="ManifestBasedAdmissionControlConfig" >}}

این صفحه مروری بر پیکربندی کنترل پذیرش مبتنی بر مانیفست (manifest-based admission control) ارائه می‌دهد. با کنترل پذیرش مبتنی بر مانیفست می‌توانید
[وب‌هوک‌های پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/)
و سیاست‌های پذیرش مبتنی بر CEL را به‌جای API کوبرنتیز، از فایل‌های ایستا روی دیسک بارگذاری کنید. این سیاست‌ها از لحظهٔ راه‌اندازی سرور API فعال هستند، مستقل از {{< glossary_tooltip text="etcd" term_id="etcd" >}} عمل می‌کنند و می‌توانند از منابع پذیرش مبتنی بر API در برابر تغییر محافظت کنند.

برای استفاده از این قابلیت، فیلد `staticManifestsDir` را در فایل
[AdmissionConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-k8s-io-v1-AdmissionConfiguration)
پیکربندی کنید؛ این فایل از طریق `--admission-control-config-file` به kube-apiserver داده می‌شود.
همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig)
با نام `ManifestBasedAdmissionControlConfig` باید فعال باشد؛ این feature gate از نسخهٔ v1.37 کوبرنتیز به‌طور پیش‌فرض فعال است.

<!-- body -->

## چرا از کنترل پذیرش مبتنی بر مانیفست استفاده کنیم؟

سیاست‌ها و وب‌هوک‌های پذیرشی که از طریق API کوبرنتیز ثبت می‌شوند (مانند
ValidatingAdmissionPolicy، MutatingAdmissionPolicy،
ValidatingWebhookConfiguration و MutatingWebhookConfiguration) چند محدودیت ذاتی دارند:

- **شکاف راه‌اندازی اولیه**: اعمال سیاست‌های مبتنی بر REST مستلزم آن است که آبجکت‌های API ایجاد شوند و کنترل‌کنندهٔ پذیرش پویا آن‌ها را بارگذاری کند. تا پیش از این مرحله، سیاست‌ها اعمال نمی‌شوند.
- **شکاف محافظت از خود**: منابع پیکربندی پذیرش (مانند
  ValidatingWebhookConfiguration) برای جلوگیری از وابستگی‌های چرخه‌ای، خودشان مشمول پذیرش وب‌هوک نیستند. بنابراین کاربری با سطح دسترسی کافی می‌تواند سیاست‌های پذیرش حیاتی را حذف یا تغییر دهد.
- **وابستگی به etcd**: پیکربندی‌های پذیرش مبتنی بر REST به در دسترس بودن etcd وابسته‌اند. اگر etcd در دسترس نباشد یا داده‌هایش خراب شود، ممکن است سیاست‌های پذیرش به‌درستی بارگذاری نشوند.

کنترل پذیرش مبتنی بر مانیفست با بارگذاری پیکربندی‌ها از فایل‌های روی دیسک، این محدودیت‌ها را برطرف می‌کند. این پیکربندی‌ها:

- به‌محض آماده شدن سرور API برای پاسخ‌گویی به درخواست‌ها فعال می‌شوند
- از طریق API کوبرنتیز قابل مشاهده یا تغییر نیستند
- مستقل از در دسترس بودن etcd هستند
- می‌توانند عملیات روی خودِ منابع پذیرش مبتنی بر API را رهگیری کنند

## انواع منابع پشتیبانی‌شده

می‌توانید انواع منابع زیر را در فایل‌های مانیفست قرار دهید. تنها نسخهٔ API
`admissionregistration.k8s.io/v1` پشتیبانی می‌شود.

{{< table caption="انواع منابع پشتیبانی‌شده برای کنترل پذیرش مبتنی بر مانیفست" >}}
| نام افزونه | انواع منابع پشتیبانی‌شده |
|:------------|:------------------------|
| `ValidatingAdmissionWebhook` | ValidatingWebhookConfiguration |
| `MutatingAdmissionWebhook` | MutatingWebhookConfiguration |
| `ValidatingAdmissionPolicy` | ValidatingAdmissionPolicy، ValidatingAdmissionPolicyBinding |
| `MutatingAdmissionPolicy` | MutatingAdmissionPolicy، MutatingAdmissionPolicyBinding |
{{< /table >}}

همچنین می‌توانید با استفاده از `v1.List` چند منبع از یک نوع افزونه را در یک سند واحد قرار دهید.

پوشهٔ `staticManifestsDir` هر افزونهٔ پذیرش فقط باید شامل انواع منابعی باشد که برای آن افزونه مجاز هستند. برای مثال، پوشه‌ای که برای افزونهٔ
`ValidatingAdmissionPolicy` پیکربندی شده است، فقط می‌تواند منابع ValidatingAdmissionPolicy
و ValidatingAdmissionPolicyBinding را در خود داشته باشد.

## پیکربندی کنترل پذیرش مبتنی بر مانیفست {#configuration}

برای فعال‌سازی کنترل پذیرش مبتنی بر مانیفست، به موارد زیر نیاز دارید:

1. فعال بودن feature gate با نام `ManifestBasedAdmissionControlConfig` روی
   kube-apiserver (که از نسخهٔ v1.37 کوبرنتیز به‌طور پیش‌فرض فعال است).
1. یک فایل `AdmissionConfiguration` که فیلدهای `staticManifestsDir` آن به پوشه‌های حاوی فایل‌های مانیفست شما اشاره کنند.
1. خودِ فایل‌های مانیفست روی دیسک، به‌طوری که فرایند kube-apiserver به آن‌ها دسترسی داشته باشد.

### AdmissionConfiguration

برای هر افزونهٔ پذیرشی که باید مانیفست‌ها را از دیسک بارگذاری کند، فیلد `staticManifestsDir` را به پیکربندی آن افزونه اضافه کنید. هر افزونه به پوشهٔ مخصوص به خود نیاز دارد.

{{% code_sample language="yaml" file="access/manifest-admission-control/admission-configuration.yaml" %}}

فیلد `staticManifestsDir` مسیر مطلق یک پوشه را می‌پذیرد. همهٔ فایل‌هایی که مستقیماً در این پوشه قرار دارند و پسوند `.yaml`، `.yml` یا `.json` دارند بارگذاری می‌شوند. زیرپوشه‌ها و فایل‌های دارای پسوندهای دیگر نادیده گرفته می‌شوند. الگوهای glob و مسیرهای نسبی پشتیبانی نمی‌شوند.

این فایل را با فلگ `--admission-control-config-file` به kube-apiserver بدهید.

### انواع پیکربندی

هر افزونهٔ پذیرش از نوع (kind) پیکربندی مشخصی استفاده می‌کند:

{{< table caption="انواع پیکربندی برای هر افزونهٔ پذیرش" >}}
| افزونه | apiVersion | kind |
|:-------|:-----------|:-----|
| `ValidatingAdmissionWebhook` | `apiserver.config.k8s.io/v1` | `WebhookAdmissionConfiguration` |
| `MutatingAdmissionWebhook` | `apiserver.config.k8s.io/v1` | `WebhookAdmissionConfiguration` |
| `ValidatingAdmissionPolicy` | `apiserver.config.k8s.io/v1` | `ValidatingAdmissionPolicyConfiguration` |
| `MutatingAdmissionPolicy` | `apiserver.config.k8s.io/v1` | `MutatingAdmissionPolicyConfiguration` |
{{< /table >}}

## نوشتن فایل‌های مانیفست {#manifest-files}

فایل‌های مانیفست شامل تعریف‌های استاندارد منابع کوبرنتیز هستند. می‌توانید با استفاده از جداکنندهٔ اسناد YAML (`---`) چند منبع را در یک فایل قرار دهید.

### قرارداد نام‌گذاری {#naming}

نام همهٔ آبجکت‌های موجود در فایل‌های مانیفست باید به پسوند `.static.k8s.io` ختم شود. برای مثال: `deny-privileged.static.k8s.io`.

وقتی feature gate با نام `ManifestBasedAdmissionControlConfig` فعال باشد، ایجاد آبجکت‌های پذیرش مبتنی بر API که نامشان به `.static.k8s.io` ختم می‌شود مسدود می‌شود. وقتی این feature gate غیرفعال باشد، به‌جای آن یک هشدار برگردانده می‌شود.

{{< note >}}
اگر دو فایل مانیفست آبجکت‌هایی از یک نوع با نام یکسان تعریف کنند، سرور API با نمایش یک خطای توصیفی راه‌اندازی نمی‌شود.
{{< /note >}}

### محدودیت‌ها

پیکربندی‌های پذیرش مبتنی بر مانیفست به‌صورت مجزا وجود دارند و نمی‌توانند به منابع API ارجاع دهند. محدودیت‌های زیر اعمال می‌شوند:

- **وب‌هوک‌ها**: باید از `clientConfig.url` استفاده کنند. استفاده از فیلد `clientConfig.service` مجاز نیست، زیرا ممکن است شبکهٔ سرویس‌ها هنگام راه‌اندازی سرور API در دسترس نباشد.
- **سیاست‌ها**: استفاده از فیلد `spec.paramKind` مجاز نیست. سیاست‌ها نمی‌توانند برای پارامترها به ConfigMapها یا دیگر آبجکت‌های کلاستر ارجاع دهند.
- **اتصال‌ها (Bindings)**: استفاده از فیلد `spec.paramRef` مجاز نیست. فیلد `spec.policyName` باید به سیاستی ارجاع دهد که در همان مجموعه فایل‌های مانیفست تعریف شده است و باید به `.static.k8s.io` ختم شود.

فایل‌های مانیفست با رمزگشای سخت‌گیر (strict decoder) رمزگشایی می‌شوند؛ این رمزگشا فایل‌هایی را که فیلدهای تکراری یا ناشناخته دارند رد می‌کند. روی هر آبجکت همان مقداردهی پیش‌فرض و اعتبارسنجی‌ای انجام می‌شود که REST API اعمال می‌کند.

## نمونه‌ها {#examples}

### محافظت از منابع پذیرش مبتنی بر API {#protecting-admission-resources}

یکی از قابلیت‌های کلیدی کنترل پذیرش مبتنی بر مانیفست، امکان رهگیری عملیات روی خودِ منابع پیکربندی پذیرش است
(ValidatingAdmissionPolicy، MutatingAdmissionPolicy،
ValidatingWebhookConfiguration، MutatingWebhookConfiguration و اتصال‌های آن‌ها). برای جلوگیری از وابستگی‌های چرخه‌ای، وب‌هوک‌ها و سیاست‌های پذیرش مبتنی بر REST روی این انواع منابع فراخوانی نمی‌شوند؛ اما سیاست‌های مبتنی بر مانیفست می‌توانند قواعدی را روی آن‌ها اعمال کنند، زیرا چنین وابستگی چرخه‌ای ندارند.

نمونهٔ زیر از حذف یا تغییر منابع پذیرشی که برچسب `platform.example.com/protected: "true"` دارند جلوگیری می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/protect-admission-resources.yaml" %}}

### اعمال یک ValidatingAdmissionPolicy از دیسک

نمونهٔ زیر سیاستی تعریف می‌کند که کانتینرهای ممتاز (privileged) را در همهٔ فضاهای نام به‌جز `kube-system` رد می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/deny-privileged-policy.yaml" %}}

این فایل را در پوشه‌ای قرار دهید که به‌عنوان `staticManifestsDir` برای افزونهٔ
`ValidatingAdmissionPolicy` پیکربندی شده است. این سیاست و اتصال آن با هم و به‌صورت اتمی بارگذاری می‌شوند.

### پیکربندی یک ValidatingWebhookConfiguration از دیسک

نمونهٔ زیر یک وب‌هوک اعتبارسنجی را پیکربندی می‌کند که یک URL خارجی را فراخوانی می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/validating-webhook.yaml" %}}

{{< note >}}
آدرس‌های URL وب‌هوک باید هنگام راه‌اندازی از kube-apiserver قابل دسترسی باشند. در پیکربندی‌های وب‌هوک مبتنی بر مانیفست فقط نقاط پایانی مبتنی بر URL پشتیبانی می‌شوند و ارجاع به سرویس‌ها مجاز نیست.
{{< /note >}}

### استفاده از قالب List

می‌توانید با استفاده از `v1.List` منابع مرتبط را در یک سند واحد گروه‌بندی کنید:

{{% code_sample language="yaml" file="access/manifest-admission-control/list-format-policy.yaml" %}}

## ترتیب ارزیابی

پیکربندی‌های مبتنی بر مانیفست پیش از پیکربندی‌های مبتنی بر API ارزیابی می‌شوند. به این ترتیب، سیاست‌های سطح پلتفرم که از طریق پیکربندی ایستا اعمال می‌شوند بر سیاست‌های مبتنی بر API اولویت دارند.

برای خودِ منابع پیکربندی پذیرش (ValidatingAdmissionPolicy،
MutatingAdmissionPolicy، ValidatingAdmissionPolicyBinding،
MutatingAdmissionPolicyBinding، ValidatingWebhookConfiguration و
MutatingWebhookConfiguration)، فقط قلاب‌های پذیرش مبتنی بر مانیفست ارزیابی می‌شوند. برای جلوگیری از وابستگی‌های چرخه‌ای، قلاب‌های مبتنی بر API برای این انواع منابع نادیده گرفته می‌شوند.

{{< note >}}
منابع احراز هویت و مجوزدهی غیرماندگار (مجازی)، مانند
TokenReview و SubjectAccessReview، هم از
[وب‌هوک‌های پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources)
و هم از سیاست‌های پذیرش مستثنا هستند. پیکربندی‌های مبتنی بر مانیفست نیز نمی‌توانند آن‌ها را رهگیری کنند، زیرا چنین کاری ممکن است دسترسی کلاستر به مسیر احراز هویت و مجوزدهی خودش را قفل کند.
{{< /note >}}

## پایش فایل‌ها و بارگذاری مجدد پویا {#dynamic-reloading}

kube-apiserver پوشه‌های پیکربندی‌شده را برای شناسایی تغییرات پایش می‌کند:

1. **بارگذاری اولیه**: هنگام راه‌اندازی، همهٔ مسیرهای پیکربندی‌شده خوانده و اعتبارسنجی می‌شوند.
   سرور API تا زمانی که همهٔ مانیفست‌ها با موفقیت بارگذاری نشوند، آماده نمی‌شود. مانیفست‌های نامعتبر باعث شکست در راه‌اندازی می‌شوند.

1. **بارگذاری مجدد در زمان اجرا**: تغییر در فایل‌های مانیفست یک چرخهٔ بارگذاری مجدد را آغاز می‌کند:
   - تغییرات فایل‌ها با استفاده از
     [fsnotify](https://github.com/fsnotify/fsnotify) و با سازوکار جایگزین نظرسنجی دوره‌ای (polling) با بازهٔ پیش‌فرض ۱ دقیقه شناسایی می‌شوند؛ این روش مشابه بارگذاری مجدد سایر فایل‌های پیکربندی در kube-apiserver است.
   - در هر بررسی، یک هش از محتوای همهٔ فایل‌های مانیفست محاسبه می‌شود. اگر هش تغییری نکرده باشد، بارگذاری مجددی انجام نمی‌شود.
   - پیکربندی‌های جدید پیش از اعمال، اعتبارسنجی می‌شوند.
   - اگر اعتبارسنجی شکست بخورد، خطا در لاگ ثبت می‌شود، متریک‌ها به‌روزرسانی می‌شوند و آخرین پیکربندی معتبر حفظ می‌شود.
   - بارگذاری‌های مجدد موفق، پیکربندی قبلی را به‌صورت اتمی جایگزین می‌کنند.

<!-- -->

1. **به‌روزرسانی اتمی فایل‌ها**: برای جلوگیری از خوانده شدن ناقص فایل‌ها در حین نوشتن، تغییرات را به‌صورت اتمی اعمال کنید (برای مثال، محتوا را در یک فایل موقت بنویسید و سپس نام آن را تغییر دهید).
   این نکته به‌ویژه هنگام به‌روزرسانی ConfigMapها یا Secretهای mount‌شده در محیط‌های کانتینری اهمیت دارد.

{{< caution >}}
اگر هنگام راه‌اندازی یک فایل مانیفست نامعتبر وجود داشته باشد، سرور API راه‌اندازی نمی‌شود. در زمان اجرا، اگر بارگذاری مجدد به دلیل خطاهای اعتبارسنجی شکست بخورد، آخرین پیکربندی معتبر حفظ می‌شود و خطا در لاگ ثبت می‌شود.
{{< /caution >}}

## مشاهده‌پذیری {#observability}

### متریک‌ها

کنترل پذیرش مبتنی بر مانیفست متریک‌های زیر را برای پایش سلامت بارگذاری مجدد ارائه می‌دهد:

{{< table caption="متریک‌های کنترل پذیرش مبتنی بر مانیفست" >}}
| نوع | توضیحات | متریک |
|:-----|:------------|:-------|
| شمارنده (Counter) | تعداد کل تلاش‌های بارگذاری مجدد، با برچسب‌های `status` (`success` یا `failure`)، `plugin` و `apiserver_id_hash`. | `apiserver_manifest_admission_config_controller_automatic_reloads_total` |
| سنجه (Gauge) | برچسب زمانی آخرین تلاش برای بارگذاری مجدد، با برچسب‌های `status`، `plugin` و `apiserver_id_hash`. | `apiserver_manifest_admission_config_controller_automatic_reload_last_timestamp_seconds` |
| سنجه (Gauge) | اطلاعات پیکربندی فعلی (مقدار آن همیشه ۱ است)، با برچسب‌های `plugin`، `apiserver_id_hash` و `hash`. از برچسب `hash` برای تشخیص ناهمخوانی پیکربندی میان سرورهای API استفاده کنید. | `apiserver_manifest_admission_config_controller_last_config_info` |
{{< /table >}}

برچسب `plugin` مشخص می‌کند که متریک مربوط به کدام افزونهٔ پذیرش است:
`ValidatingAdmissionWebhook`، `MutatingAdmissionWebhook`،
`ValidatingAdmissionPolicy` یا `MutatingAdmissionPolicy`.

از آنجا که نام آبجکت‌های مبتنی بر مانیفست به `.static.k8s.io` ختم می‌شود، با فیلتر کردن برچسب `name` در متریک‌های پذیرش موجود (مانند `apiserver_admission_webhook_rejection_count`) می‌توان تصمیم‌های مبتنی بر مانیفست را شناسایی کرد.

### حاشیه‌نویسی‌های ممیزی

حاشیه‌نویسی‌های ممیزی (audit annotations) موجود (مانند
`validation.policy.admission.k8s.io/validation_failure` و
`mutation.webhook.admission.k8s.io/round_0_index_0`) شامل نام آبجکت هستند.
می‌توانید با فیلتر کردن نام‌هایی که به `.static.k8s.io` ختم می‌شوند، تصمیم‌های پذیرش مبتنی بر مانیفست را شناسایی کنید.

## ملاحظات دسترس‌پذیری بالا {#ha-considerations}

هر نمونهٔ kube-apiserver فایل‌های مانیفست خود را به‌طور مستقل بارگذاری می‌کند. در پیکربندی‌های با دسترس‌پذیری بالا (high availability) که چند نمونهٔ سرور API دارند:

- هر سرور API باید به‌صورت جداگانه پیکربندی شود. هیچ همگام‌سازی‌ای میان سرورهای API برای پیکربندی‌های مبتنی بر مانیفست وجود ندارد.
- برای یکسان نگه داشتن فایل‌های مانیفست در همهٔ نمونه‌ها، از ابزارهای خارجی مدیریت پیکربندی (مانند Ansible، Puppet یا mountهای ذخیره‌سازی مشترک) استفاده کنید.
- متریک `apiserver_manifest_admission_config_controller_last_config_info` برچسبی به نام `hash` ارائه می‌دهد که می‌توانید از آن برای تشخیص ناهمخوانی پیکربندی میان نمونه‌های سرور API استفاده کنید.

این رفتار مشابه سایر پیکربندی‌های فایل‌محور kube-apiserver، مانند
[رمزنگاری داده‌ها در حالت سکون](/docs/tasks/administer-cluster/encrypt-data/) و
[احراز هویت](/docs/reference/access-authn-authz/authentication/) است.

## ارتقا و تنزل نسخه {#upgrade-downgrade}

**ارتقا**: فعال‌سازی این قابلیت و ارائهٔ پیکربندی مانیفست اختیاری است. در کلاسترهای موجودی که پیکربندی مانیفست ندارند، هیچ تغییری در رفتار ایجاد نمی‌شود.

**تنزل نسخه**: پیش از تنزل به نسخه‌ای که این قابلیت را ندارد:

1. مدخل‌های `staticManifestsDir` را از فایل `AdmissionConfiguration` حذف کنید.
1. اگر به سیاست‌های مبتنی بر مانیفست متکی هستید، در صورت امکان آن‌ها را به‌صورت آبجکت‌های API از نو ایجاد کنید.
1. kube-apiserver را دوباره راه‌اندازی کنید.

{{< warning >}}
اگر بدون حذف پیکربندی `staticManifestsDir` نسخه را تنزل دهید، سرور API به دلیل وجود فیلدهای پیکربندی ناشناخته راه‌اندازی نمی‌شود.
{{< /warning >}}

## عیب‌یابی {#troubleshooting}

{{< table caption="مشکلات رایج و راه‌حل آن‌ها" >}}
| نشانه | علت احتمالی | راه‌حل |
|:--------|:--------------|:-----------|
| سرور API راه‌اندازی نمی‌شود | وجود فایل مانیفست نامعتبر هنگام راه‌اندازی | لاگ‌های سرور API را برای یافتن خطاهای اعتبارسنجی بررسی کنید. فایل مانیفست را اصلاح و سرور را دوباره راه‌اندازی کنید. |
| سرور API راه‌اندازی نمی‌شود | نام‌های تکراری آبجکت‌ها در فایل‌های مانیفست | مطمئن شوید که نام همهٔ آبجکت‌ها در پوشهٔ `staticManifestsDir` هر افزونه یکتا است. |
| سیاست‌ها پس از به‌روزرسانی فایل اعمال نمی‌شوند | شکست اعتبارسنجی در بارگذاری مجدد | متریک `automatic_reloads_total{status="failure"}` و لاگ‌های سرور API را بررسی کنید. مانیفست را اصلاح کنید و منتظر چرخهٔ بعدی بارگذاری مجدد بمانید. |
| درخواست‌های وب‌هوک با شکست مواجه می‌شوند | آدرس URL وب‌هوک در دسترس نیست | بررسی کنید که آدرس مشخص‌شده در `clientConfig.url` از kube-apiserver قابل دسترسی باشد. |
| آبجکت‌های API با پسوند `.static.k8s.io` ایجاد نمی‌شوند | این پسوند نام توسط feature gate رزرو شده است | وقتی feature gate فعال باشد، پسوند `.static.k8s.io` برای پیکربندی‌های مبتنی بر مانیفست رزرو شده است. برای آبجکت‌های مبتنی بر API از نام دیگری استفاده کنید. |
{{< /table >}}

## {{% heading "whatsnext" %}}

- دربارهٔ [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)
  برای سیاست‌های اعتبارسنجی مبتنی بر CEL بیشتر بیاموزید.
- دربارهٔ [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/)
  برای سیاست‌های تغییر (mutation) مبتنی بر CEL بیشتر بیاموزید.
- دربارهٔ [کنترل پذیرش پویا](/docs/reference/access-authn-authz/extensible-admission-controllers/)
  برای کنترل پذیرش مبتنی بر وب‌هوک بیشتر بیاموزید.
- سند طراحی [KEP-5793](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/5793-manifest-based-admission-control-config)
  را مطالعه کنید.

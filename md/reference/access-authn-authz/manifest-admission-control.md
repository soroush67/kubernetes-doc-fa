---
reviewers:
- liggitt
- jpbetz
title: کنترل پذیرش مبتنی بر مانیفست
content_type: concept
---

<!-- overview -->

{{< feature-state feature_gate_name="ManifestBasedAdmissionControlConfig" >}}

این صفحه مروری بر پیکربندی کنترل پذیرش (admission control) مبتنی بر مانیفست ارائه می‌دهد.
کنترل پذیرش مبتنی بر مانیفست به شما امکان می‌دهد
[admission webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/)
و سیاست‌های پذیرش مبتنی بر CEL را به‌جای API کوبرنتیز، از فایل‌های ایستا روی دیسک بارگذاری کنید.
این سیاست‌ها از زمان راه‌اندازی API server فعال هستند، مستقل از {{< glossary_tooltip text="etcd" term_id="etcd" >}} عمل می‌کنند و می‌توانند از منابع پذیرش مبتنی بر API در برابر تغییر محافظت کنند.

برای استفاده از این قابلیت، فیلد `staticManifestsDir` را در فایل
[AdmissionConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-k8s-io-v1-AdmissionConfiguration)
که از طریق `--admission-control-config-file` به kube-apiserver داده می‌شود، پیکربندی کنید.
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig)
با نام `ManifestBasedAdmissionControlConfig` باید فعال باشد؛ این feature gate از کوبرنتیز v1.37 به‌صورت پیش‌فرض فعال است.

<!-- body -->

## چرا از کنترل پذیرش مبتنی بر مانیفست استفاده کنیم؟

سیاست‌ها و webhookهای پذیرشی که از طریق API کوبرنتیز ثبت می‌شوند (مانند
ValidatingAdmissionPolicy، MutatingAdmissionPolicy،
ValidatingWebhookConfiguration و MutatingWebhookConfiguration) چند محدودیت ذاتی دارند:

- **شکاف راه‌اندازی اولیه (Bootstrap gap)**: اِعمال سیاست مبتنی بر REST مستلزم آن است که آبجکت‌های API
  ایجاد شوند و توسط کنترل‌کننده پذیرش پویا بارگذاری گردند. تا زمانی که این اتفاق نیفتد،
  سیاست‌ها اِعمال نمی‌شوند.
- **شکاف خودمحافظتی (Self-protection gap)**: منابع پیکربندی پذیرش (مانند
  ValidatingWebhookConfiguration) خودشان مشمول پذیرش از طریق webhook نیستند تا از وابستگی‌های دایره‌ای جلوگیری شود. کاربری با سطح دسترسی کافی
  می‌تواند سیاست‌های پذیرش حیاتی را حذف یا تغییر دهد.
- **وابستگی به etcd**: پیکربندی‌های پذیرش مبتنی بر REST به در دسترس بودن etcd وابسته‌اند.
  اگر etcd در دسترس نباشد یا آسیب دیده باشد، ممکن است سیاست‌های پذیرش به‌درستی بارگذاری نشوند.

کنترل پذیرش مبتنی بر مانیفست با بارگذاری پیکربندی‌ها از فایل‌های روی دیسک، این محدودیت‌ها را برطرف می‌کند. این پیکربندی‌ها:

- به محض آماده شدن API server برای پاسخ‌گویی به درخواست‌ها فعال هستند
- از طریق API کوبرنتیز قابل مشاهده یا تغییر نیستند
- مستقل از در دسترس بودن etcd هستند
- می‌توانند عملیات روی خود منابع پذیرش مبتنی بر API را رهگیری کنند

## انواع منابع پشتیبانی‌شده

می‌توانید انواع منابع زیر را در فایل‌های مانیفست قرار دهید. فقط نسخه API با نام
`admissionregistration.k8s.io/v1` پشتیبانی می‌شود.

{{< table caption="انواع منابع پشتیبانی‌شده برای کنترل پذیرش مبتنی بر مانیفست" >}}
| نام افزونه | انواع منابع پشتیبانی‌شده |
|:------------|:------------------------|
| `ValidatingAdmissionWebhook` | ValidatingWebhookConfiguration |
| `MutatingAdmissionWebhook` | MutatingWebhookConfiguration |
| `ValidatingAdmissionPolicy` | ValidatingAdmissionPolicy, ValidatingAdmissionPolicyBinding |
| `MutatingAdmissionPolicy` | MutatingAdmissionPolicy, MutatingAdmissionPolicyBinding |
{{< /table >}}

همچنین می‌توانید از `v1.List` برای قرار دادن چند منبع از یک نوع افزونه در یک سند واحد استفاده کنید.

`staticManifestsDir` هر افزونه پذیرش باید فقط شامل انواع منابعی باشد
که برای آن افزونه مجاز است. برای مثال، دایرکتوری پیکربندی‌شده برای افزونه
`ValidatingAdmissionPolicy` فقط می‌تواند شامل منابع ValidatingAdmissionPolicy
و ValidatingAdmissionPolicyBinding باشد.

## پیکربندی کنترل پذیرش مبتنی بر مانیفست {#configuration}

برای فعال‌سازی کنترل پذیرش مبتنی بر مانیفست به موارد زیر نیاز دارید:

1. فعال بودن feature gate با نام `ManifestBasedAdmissionControlConfig` روی
   kube-apiserver (از کوبرنتیز v1.37 به‌صورت پیش‌فرض فعال است).
1. یک فایل `AdmissionConfiguration` با فیلدهای `staticManifestsDir` که به
   دایرکتوری‌های حاوی فایل‌های مانیفست شما اشاره می‌کنند.
1. خود فایل‌های مانیفست روی دیسک، به‌گونه‌ای که برای فرایند kube-apiserver قابل دسترسی باشند.

### AdmissionConfiguration

`staticManifestsDir` را به پیکربندی افزونه‌ی هر افزونه پذیرشی که باید مانیفست‌ها را از دیسک بارگذاری کند اضافه کنید.
هر افزونه به دایرکتوری مخصوص به خود نیاز دارد.

{{% code_sample language="yaml" file="access/manifest-admission-control/admission-configuration.yaml" %}}

فیلد `staticManifestsDir` یک مسیر مطلق به یک دایرکتوری می‌پذیرد. همه‌ی فایل‌های
مستقیم درون دایرکتوری که پسوند `.yaml`، `.yml` یا `.json` دارند بارگذاری می‌شوند. زیردایرکتوری‌ها و فایل‌هایی با پسوندهای دیگر نادیده گرفته می‌شوند.
الگوهای glob و مسیرهای نسبی پشتیبانی نمی‌شوند.

این فایل را با فلگ `--admission-control-config-file` به kube-apiserver بدهید.

### انواع پیکربندی

هر افزونه پذیرش از یک kind پیکربندی مشخص استفاده می‌کند:

{{< table caption="انواع پیکربندی برای هر افزونه پذیرش" >}}
| افزونه | apiVersion | kind |
|:-------|:-----------|:-----|
| `ValidatingAdmissionWebhook` | `apiserver.config.k8s.io/v1` | `WebhookAdmissionConfiguration` |
| `MutatingAdmissionWebhook` | `apiserver.config.k8s.io/v1` | `WebhookAdmissionConfiguration` |
| `ValidatingAdmissionPolicy` | `apiserver.config.k8s.io/v1` | `ValidatingAdmissionPolicyConfiguration` |
| `MutatingAdmissionPolicy` | `apiserver.config.k8s.io/v1` | `MutatingAdmissionPolicyConfiguration` |
{{< /table >}}

## نوشتن فایل‌های مانیفست {#manifest-files}

فایل‌های مانیفست شامل تعریف‌های استاندارد منابع کوبرنتیز هستند. می‌توانید با استفاده از جداکننده‌های سند YAML (`---`) چند منبع را در یک فایل قرار دهید.

### قرارداد نام‌گذاری {#naming}

نام همه‌ی آبجکت‌ها در فایل‌های مانیفست باید با پسوند `.static.k8s.io` پایان یابد.
برای مثال: `deny-privileged.static.k8s.io`.

وقتی feature gate با نام `ManifestBasedAdmissionControlConfig` فعال باشد، ایجاد
آبجکت‌های پذیرش مبتنی بر API با نام‌هایی که به `.static.k8s.io` ختم می‌شوند مسدود می‌شود.
وقتی feature gate غیرفعال باشد، به‌جای آن یک هشدار بازگردانده می‌شود.

{{< note >}}
اگر دو فایل مانیفست آبجکت‌هایی از یک نوع با نام یکسان تعریف کنند،
API server راه‌اندازی نمی‌شود و یک خطای توصیفی نمایش می‌دهد.
{{< /note >}}

### محدودیت‌ها

پیکربندی‌های پذیرش مبتنی بر مانیفست به‌صورت مجزا وجود دارند و نمی‌توانند
به منابع API ارجاع دهند. محدودیت‌های زیر اعمال می‌شوند:

- **Webhookها**: باید از `clientConfig.url` استفاده کنند. فیلد `clientConfig.service`
  مجاز نیست، زیرا ممکن است شبکه‌ی سرویس در زمان راه‌اندازی API server در دسترس نباشد.
- **سیاست‌ها**: فیلد `spec.paramKind` مجاز نیست. سیاست‌ها نمی‌توانند
  برای پارامترها به ConfigMapها یا سایر آبجکت‌های کلاستر ارجاع دهند.
- **Bindingها**: فیلد `spec.paramRef` مجاز نیست. مقدار `spec.policyName`
  باید به سیاستی ارجاع دهد که در همان مجموعه فایل‌های مانیفست تعریف شده است و باید با `.static.k8s.io` پایان یابد.

فایل‌های مانیفست با استفاده از رمزگشای سخت‌گیر (strict decoder) خوانده می‌شوند که فایل‌های
دارای فیلدهای تکراری یا فیلدهای ناشناخته را رد می‌کند. هر آبجکت همان مقداردهی پیش‌فرض و اعتبارسنجی‌ای را طی می‌کند که REST API اعمال می‌کند.

## مثال‌ها {#examples}

### محافظت از منابع پذیرش مبتنی بر API {#protecting-admission-resources}

یکی از قابلیت‌های کلیدی کنترل پذیرش مبتنی بر مانیفست، توانایی رهگیری
عملیات روی خود منابع پیکربندی پذیرش است
(ValidatingAdmissionPolicy، MutatingAdmissionPolicy،
ValidatingWebhookConfiguration، MutatingWebhookConfiguration و bindingهای آن‌ها).
webhookها و سیاست‌های پذیرش مبتنی بر REST برای جلوگیری از وابستگی‌های دایره‌ای روی این انواع منابع فراخوانی نمی‌شوند، اما سیاست‌های مبتنی بر مانیفست
می‌توانند روی آن‌ها قوانین را اِعمال کنند، زیرا این وابستگی دایره‌ای را ندارند.

مثال زیر از حذف یا تغییر منابع پذیرشی که برچسب
`platform.example.com/protected: "true"` را دارند جلوگیری می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/protect-admission-resources.yaml" %}}

### اِعمال یک ValidatingAdmissionPolicy از روی دیسک

مثال زیر سیاستی را تعریف می‌کند که کانتینرهای privileged را در همه‌ی
فضاهای نام (namespace) به‌جز `kube-system` رد می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/deny-privileged-policy.yaml" %}}

این فایل را در دایرکتوری‌ای قرار دهید که به‌عنوان `staticManifestsDir` برای افزونه
`ValidatingAdmissionPolicy` پیکربندی شده است. سیاست و binding آن
با هم و به‌صورت اتمیک بارگذاری می‌شوند.

### پیکربندی یک ValidatingWebhookConfiguration از روی دیسک

مثال زیر یک validating webhook را پیکربندی می‌کند که یک URL خارجی را فراخوانی می‌کند:

{{% code_sample language="yaml" file="access/manifest-admission-control/validating-webhook.yaml" %}}

{{< note >}}
URL webhookها باید در زمان راه‌اندازی از kube-apiserver قابل دسترسی باشند. فقط
نقاط انتهایی مبتنی بر URL پشتیبانی می‌شوند؛ ارجاع به service در
پیکربندی‌های webhook مبتنی بر مانیفست مجاز نیست.
{{< /note >}}

### استفاده از قالب List

می‌توانید از `v1.List` برای گروه‌بندی منابع مرتبط در یک سند واحد استفاده کنید:

{{% code_sample language="yaml" file="access/manifest-admission-control/list-format-policy.yaml" %}}

## ترتیب ارزیابی

پیکربندی‌های مبتنی بر مانیفست پیش از پیکربندی‌های مبتنی بر API ارزیابی می‌شوند.
این تضمین می‌کند که سیاست‌های سطح پلتفرم که از طریق پیکربندی ایستا اِعمال می‌شوند
بر سیاست‌های مبتنی بر API اولویت دارند.

برای خود منابع پیکربندی پذیرش (ValidatingAdmissionPolicy،
MutatingAdmissionPolicy، ValidatingAdmissionPolicyBinding،
MutatingAdmissionPolicyBinding، ValidatingWebhookConfiguration،
MutatingWebhookConfiguration) فقط hookهای پذیرش مبتنی بر مانیفست
ارزیابی می‌شوند. hookهای مبتنی بر API برای این انواع منابع نادیده گرفته می‌شوند تا از
وابستگی‌های دایره‌ای جلوگیری شود.

{{< note >}}
منابع مجازی (غیرپایدار) احراز هویت و مجوزدهی، مانند
TokenReview و SubjectAccessReview، هم از
[admission webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources)
و هم از سیاست‌های پذیرش مستثنا هستند. پیکربندی‌های مبتنی بر مانیفست نیز
نمی‌توانند آن‌ها را رهگیری کنند، زیرا انجام این کار می‌تواند کلاستر را از مسیر احراز هویت و مجوزدهی خودش قفل کند.
{{< /note >}}

## پایش فایل و بارگذاری مجدد پویا {#dynamic-reloading}

kube-apiserver دایرکتوری‌های پیکربندی‌شده را برای تغییرات پایش می‌کند:

1. **بارگذاری اولیه**: در زمان راه‌اندازی، همه‌ی مسیرهای پیکربندی‌شده خوانده و اعتبارسنجی می‌شوند.
   API server تا زمانی که همه‌ی مانیفست‌ها با موفقیت بارگذاری نشوند آماده نمی‌شود.
   مانیفست‌های نامعتبر باعث شکست راه‌اندازی می‌شوند.

1. **بارگذاری مجدد در زمان اجرا**: تغییرات فایل‌های مانیفست یک چرخه‌ی بارگذاری مجدد را راه‌اندازی می‌کند:
   - تغییرات فایل‌ها با استفاده از
     [fsnotify](https://github.com/fsnotify/fsnotify) همراه با یک جایگزین مبتنی بر polling
     (با فاصله‌ی پیش‌فرض ۱ دقیقه) شناسایی می‌شوند، مشابه بارگذاری مجدد سایر فایل‌های پیکربندی در
     kube-apiserver.
   - در هر بررسی، یک هش محتوایی از همه‌ی فایل‌های مانیفست محاسبه می‌شود. اگر هش
     تغییر نکرده باشد، بارگذاری مجدد انجام نمی‌شود.
   - پیکربندی‌های جدید پیش از اِعمال اعتبارسنجی می‌شوند.
   - اگر اعتبارسنجی شکست بخورد، خطا ثبت می‌شود، metricها به‌روزرسانی می‌شوند و
     آخرین پیکربندی معتبر قبلی حفظ می‌شود.
   - بارگذاری‌های مجدد موفق، پیکربندی قبلی را به‌صورت اتمیک جایگزین می‌کنند.

<!-- -->

1. **به‌روزرسانی اتمیک فایل‌ها**: برای جلوگیری از خوانده شدن ناقص هنگام نوشتن فایل‌ها،
   تغییرات را به‌صورت اتمیک اعمال کنید (برای مثال، در یک فایل موقت بنویسید و سپس نام آن را تغییر دهید).
   این موضوع به‌ویژه هنگام به‌روزرسانی ConfigMapها یا Secretهای mount‌شده در
   محیط‌های کانتینری اهمیت دارد.

{{< caution >}}
اگر هنگام راه‌اندازی یک فایل مانیفست نامعتبر وجود داشته باشد، API server
راه‌اندازی نمی‌شود. در زمان اجرا، اگر بارگذاری مجدد به‌دلیل خطاهای اعتبارسنجی شکست بخورد، آخرین
پیکربندی معتبر حفظ می‌شود و خطا ثبت می‌شود.
{{< /caution >}}

## قابلیت مشاهده‌پذیری {#observability}

### Metricها

کنترل پذیرش مبتنی بر مانیفست metricهای زیر را برای پایش سلامت
بارگذاری مجدد فراهم می‌کند:

{{< table caption="Metricهای کنترل پذیرش مبتنی بر مانیفست" >}}
| نوع | توضیحات | Metric |
|:-----|:------------|:-------|
| Counter | تعداد کل تلاش‌های بارگذاری مجدد، با برچسب‌های `status` (`success` یا `failure`)، `plugin` و `apiserver_id_hash`. | `apiserver_manifest_admission_config_controller_automatic_reloads_total` |
| Gauge | زمان‌مهر آخرین تلاش بارگذاری مجدد، با برچسب‌های `status`، `plugin` و `apiserver_id_hash`. | `apiserver_manifest_admission_config_controller_automatic_reload_last_timestamp_seconds` |
| Gauge | اطلاعات پیکربندی فعلی (مقدار همیشه ۱ است)، با برچسب‌های `plugin`، `apiserver_id_hash` و `hash`. از برچسب `hash` برای شناسایی ناهمگونی پیکربندی میان API serverها استفاده کنید. | `apiserver_manifest_admission_config_controller_last_config_info` |
{{< /table >}}

برچسب `plugin` مشخص می‌کند metric به کدام افزونه پذیرش مربوط است:
`ValidatingAdmissionWebhook`، `MutatingAdmissionWebhook`،
`ValidatingAdmissionPolicy` یا `MutatingAdmissionPolicy`.

از آنجا که نام آبجکت‌های مبتنی بر مانیفست به `.static.k8s.io` ختم می‌شود، metricهای پذیرش موجود (مانند `apiserver_admission_webhook_rejection_count`)
می‌توانند با فیلتر کردن بر اساس برچسب `name`، تصمیم‌های مبتنی بر مانیفست را مشخص کنند.

### حاشیه‌نویسی‌های ممیزی (Audit annotations)

حاشیه‌نویسی‌های ممیزی موجود (مانند
`validation.policy.admission.k8s.io/validation_failure` و
`mutation.webhook.admission.k8s.io/round_0_index_0`) شامل نام آبجکت هستند.
می‌توانید تصمیم‌های پذیرش مبتنی بر مانیفست را با فیلتر کردن نام‌هایی که
به `.static.k8s.io` ختم می‌شوند شناسایی کنید.

## ملاحظات دسترسی‌پذیری بالا {#ha-considerations}

هر نمونه‌ی kube-apiserver فایل‌های مانیفست خود را به‌طور مستقل بارگذاری می‌کند. در
محیط‌های دسترسی‌پذیری بالا با چند نمونه API server:

- هر API server باید به‌صورت جداگانه پیکربندی شود. هیچ همگام‌سازی میان API serverها
  برای پیکربندی‌های مبتنی بر مانیفست وجود ندارد.
- از ابزارهای مدیریت پیکربندی خارجی (مانند Ansible، Puppet یا
  mountهای ذخیره‌سازی مشترک) برای حفظ یکسانی فایل‌های مانیفست میان نمونه‌ها استفاده کنید.
- metric با نام `apiserver_manifest_admission_config_controller_last_config_info`
  یک برچسب `hash` ارائه می‌دهد که می‌توانید از آن برای شناسایی ناهمگونی پیکربندی میان
  نمونه‌های API server استفاده کنید.

این رفتار مشابه سایر پیکربندی‌های فایل‌محور kube-apiserver مانند
[رمزنگاری داده‌ها در حالت سکون](/docs/tasks/administer-cluster/encrypt-data/) و
[احراز هویت](/docs/reference/access-authn-authz/authentication/) است.

## ارتقا و تنزل نسخه {#upgrade-downgrade}

**ارتقا**: فعال‌سازی این قابلیت و ارائه‌ی پیکربندی مانیفست
اختیاری است. کلاسترهای موجود که پیکربندی مانیفست ندارند هیچ تغییر رفتاری مشاهده نمی‌کنند.

**تنزل نسخه**: پیش از تنزل به نسخه‌ای که این قابلیت را ندارد:

1. ورودی‌های `staticManifestsDir` را از فایل `AdmissionConfiguration` حذف کنید.
1. اگر به سیاست‌های مبتنی بر مانیفست متکی هستید، در صورت امکان آن‌ها را به‌صورت آبجکت‌های API دوباره ایجاد کنید.
1. kube-apiserver را مجدداً راه‌اندازی کنید.

{{< warning >}}
تنزل نسخه بدون حذف پیکربندی `staticManifestsDir` باعث می‌شود
API server به‌دلیل فیلدهای پیکربندی ناشناخته راه‌اندازی نشود.
{{< /warning >}}

## عیب‌یابی {#troubleshooting}

{{< table caption="مشکلات رایج و راه‌حل آن‌ها" >}}
| نشانه | علت احتمالی | راه‌حل |
|:--------|:--------------|:-----------|
| API server راه‌اندازی نمی‌شود | فایل مانیفست نامعتبر در زمان راه‌اندازی | لاگ‌های API server را برای خطاهای اعتبارسنجی بررسی کنید. فایل مانیفست را اصلاح کنید و مجدداً راه‌اندازی کنید. |
| API server راه‌اندازی نمی‌شود | نام‌های تکراری آبجکت‌ها در فایل‌های مانیفست | مطمئن شوید همه‌ی نام‌های آبجکت در `staticManifestsDir` هر افزونه یکتا هستند. |
| سیاست‌ها پس از به‌روزرسانی فایل اِعمال نمی‌شوند | شکست اعتبارسنجی بارگذاری مجدد | metric با نام `automatic_reloads_total{status="failure"}` و لاگ‌های API server را بررسی کنید. مانیفست را اصلاح کنید و منتظر چرخه‌ی بعدی بارگذاری مجدد بمانید. |
| درخواست‌های webhook با شکست مواجه می‌شوند | URL مربوط به webhook در دسترس نیست | بررسی کنید که URL مشخص‌شده در `clientConfig.url` از kube-apiserver قابل دسترسی باشد. |
| امکان ایجاد آبجکت‌های API با پسوند `.static.k8s.io` وجود ندارد | پسوند نام توسط feature gate رزرو شده است | وقتی feature gate فعال است، پسوند `.static.k8s.io` برای پیکربندی‌های مبتنی بر مانیفست رزرو می‌شود. برای آبجکت‌های مبتنی بر API از نام دیگری استفاده کنید. |
{{< /table >}}

## {{% heading "whatsnext" %}}

- درباره‌ی [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)
  برای سیاست‌های اعتبارسنجی مبتنی بر CEL بیاموزید.
- درباره‌ی [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/)
  برای سیاست‌های تغییر (mutation) مبتنی بر CEL بیاموزید.
- درباره‌ی [کنترل پذیرش پویا](/docs/reference/access-authn-authz/extensible-admission-controllers/)
  برای کنترل پذیرش مبتنی بر webhook بیاموزید.
- سند طراحی [KEP-5793](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/5793-manifest-based-admission-control-config)
  را مطالعه کنید.

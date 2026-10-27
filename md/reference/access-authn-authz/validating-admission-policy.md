---
reviewers:
- liggitt
- jpbetz
- cici37
title: سیاست پذیرش اعتبارسنجی (Validating Admission Policy)
content_type: concept
---

<!-- overview -->

{{< feature-state state="stable" for_k8s_version="v1.30" >}}

این صفحه مروری بر Validating Admission Policy ارائه می‌دهد.


<!-- body -->

## Validating Admission Policy چیست؟

سیاست‌های پذیرش اعتبارسنجی (Validating Admission Policy) یک جایگزین اعلانی و درون‌فرایندی (in-process) برای وب‌هوک‌های پذیرش اعتبارسنجی (validating admission webhooks) ارائه می‌دهند.

سیاست‌های پذیرش اعتبارسنجی برای اعلام قواعد اعتبارسنجی یک سیاست از Common Expression Language (CEL) استفاده می‌کنند.
این سیاست‌ها بسیار قابل پیکربندی هستند و به نویسندگان سیاست امکان می‌دهند سیاست‌هایی تعریف کنند که بر حسب نیاز مدیران کلاستر، پارامتری‌شده و محدود به منابع مشخص باشند.

## چه منابعی یک سیاست را می‌سازند

یک سیاست معمولاً از سه منبع تشکیل می‌شود:

- `ValidatingAdmissionPolicy` منطق انتزاعی یک سیاست را توصیف می‌کند
  (مثلاً: «این سیاست اطمینان می‌دهد که یک برچسب مشخص روی یک مقدار مشخص تنظیم شده است»).

- یک منبع پارامتر (parameter resource) اطلاعاتی را در اختیار ValidatingAdmissionPolicy قرار می‌دهد تا آن را به یک گزاره‌ی مشخص تبدیل کند
  (مثلاً: «برچسب `owner` باید روی مقداری تنظیم شود که به `.company.com` ختم می‌شود»).
  یک نوع بومی مانند ConfigMap یا یک CRD، طرح‌واره (schema) منبع پارامتر را تعریف می‌کند.
  آبجکت‌های `ValidatingAdmissionPolicy` مشخص می‌کنند که برای منبع پارامتر خود چه Kind ای را انتظار دارند.

- یک `ValidatingAdmissionPolicyBinding` منابع بالا را به یکدیگر پیوند می‌دهد و دامنه‌ی اعمال را مشخص می‌کند.
  اگر فقط بخواهید تنظیم برچسب `owner` را برای `Pods` الزامی کنید، این محدودیت را در binding مشخص می‌کنید.

برای اینکه یک سیاست اثر داشته باشد، دست‌کم یک `ValidatingAdmissionPolicy` و یک `ValidatingAdmissionPolicyBinding` متناظر با آن باید تعریف شود.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
رزرو شده‌اند و نمی‌توان از آن‌ها برای سیاست‌ها یا bindingهای مبتنی بر API استفاده کرد. این رزرو
زمانی اعمال می‌شود که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) با نام `ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

اگر یک `ValidatingAdmissionPolicy` نیازی به پیکربندی از طریق پارامترها نداشته باشد، کافی است
`spec.paramKind` را در `ValidatingAdmissionPolicy` مشخص نکنید.

## شروع کار با Validating Admission Policy

Validating Admission Policy بخشی از control plane کلاستر است. باید آن‌ها را با نهایت احتیاط بنویسید و مستقر کنید. در ادامه نحوه‌ی آزمایش سریع Validating Admission Policy شرح داده شده است.

### ایجاد یک ValidatingAdmissionPolicy

در ادامه نمونه‌ای از یک ValidatingAdmissionPolicy آمده است.

{{% code_sample language="yaml" file="validatingadmissionpolicy/basic-example-policy.yaml" %}}

`spec.validations` شامل عبارت‌های CEL است که برای اعتبارسنجی درخواست از [Common Expression Language (CEL)](https://github.com/google/cel-spec) استفاده می‌کنند.
اگر نتیجه‌ی ارزیابی یک عبارت false باشد، بررسی اعتبارسنجی مطابق با فیلد `spec.failurePolicy` اعمال می‌شود.

{{< note >}}
می‌توانید عبارت‌های CEL را به‌سرعت در [CEL Playground](https://playcel.undistro.io) آزمایش کنید.
{{< /note >}}

برای پیکربندی یک سیاست پذیرش اعتبارسنجی جهت استفاده در کلاستر، وجود یک binding الزامی است.
در ادامه نمونه‌ای از یک ValidatingAdmissionPolicyBinding آمده است:

{{% code_sample language="yaml" file="validatingadmissionpolicy/basic-example-binding.yaml" %}}

هنگام تلاش برای ایجاد یک deployment که مقدار replicas آن عبارت اعتبارسنجی را برآورده نمی‌کند،
خطایی با پیام زیر بازگردانده می‌شود:

```none
ValidatingAdmissionPolicy 'demo-policy.example.com' with binding 'demo-binding-test.example.com' denied request: failed expression: object.spec.replicas <= 5
```

مثال بالا یک نمونه‌ی ساده از استفاده از ValidatingAdmissionPolicy بدون پیکربندی پارامتر است.

#### اقدام‌های اعتبارسنجی (Validation actions) {#validation-actions}

هر `ValidatingAdmissionPolicyBinding` باید یک یا چند مقدار
`validationActions` مشخص کند تا نحوه‌ی اِعمال `validations` یک سیاست را تعیین کند.

مقادیر پشتیبانی‌شده‌ی `validationActions` عبارت‌اند از:

- `Deny`: شکست اعتبارسنجی به رد شدن درخواست منجر می‌شود.
- `Warn`: شکست اعتبارسنجی به‌صورت [هشدار](/blog/2020/09/03/warnings/) به کلاینت درخواست‌دهنده گزارش می‌شود.
- `Audit`: شکست اعتبارسنجی در رویداد ممیزی (audit event) مربوط به درخواست API درج می‌شود.

برای مثال، برای اینکه هم به کلاینت‌ها درباره‌ی شکست اعتبارسنجی هشدار داده شود و هم
شکست‌های اعتبارسنجی ممیزی شوند، از این مقدار استفاده کنید:

```yaml
validationActions: [Warn, Audit]
```

`Deny` و `Warn` را نمی‌توان با هم به کار برد، زیرا این ترکیب شکست اعتبارسنجی را بی‌دلیل هم در
بدنه‌ی پاسخ API و هم در هدرهای هشدار HTTP تکرار می‌کند.

یک `validation` که نتیجه‌ی ارزیابی آن false باشد، همیشه بر اساس این اقدام‌ها اِعمال می‌شود.
شکست‌های تعریف‌شده توسط `failurePolicy` فقط در صورتی بر اساس این اقدام‌ها اِعمال می‌شوند که `failurePolicy` روی `Fail` تنظیم شده باشد (یا مشخص نشده باشد)؛
در غیر این صورت، این شکست‌ها نادیده گرفته می‌شوند.

برای جزئیات بیشتر درباره‌ی حاشیه‌نویسی (annotation) ممیزی شکست اعتبارسنجی، به
[Audit Annotations: validation failures](/docs/reference/labels-annotations-taints/audit-annotations/#validation-policy-admission-k8s-io-validation-failure) مراجعه کنید.

### منابع پارامتر {#parameter-resources}

منابع پارامتر امکان می‌دهند پیکربندی یک سیاست از تعریف آن جدا باشد.
یک سیاست می‌تواند paramKind را تعریف کند که GVK منبع پارامتر را مشخص می‌کند،
و سپس یک policy binding، سیاست را با نام (از طریق policyName) از راه paramRef به یک منبع پارامتر مشخص پیوند می‌دهد.

اگر پیکربندی پارامتر لازم باشد، در ادامه نمونه‌ای از یک ValidatingAdmissionPolicy
با پیکربندی پارامتر آمده است.

{{% code_sample language="yaml" file="validatingadmissionpolicy/policy-with-param.yaml" %}}

فیلد `spec.paramKind` در ValidatingAdmissionPolicy نوع منابعی را که برای پارامتری‌کردن این سیاست به کار می‌روند مشخص می‌کند. در این مثال، این کار با custom resourceهای ReplicaLimit پیکربندی شده است.
توجه کنید که در این مثال، عبارت CEL از طریق متغیر params در CEL به پارامترها ارجاع می‌دهد،
مثلاً `params.maxReplicas`. فیلد `spec.matchConstraints` مشخص می‌کند که این سیاست برای اعتبارسنجی چه منابعی طراحی شده است. توجه داشته باشید که نوع‌های بومی مانند `ConfigMap` نیز می‌توانند به‌عنوان مرجع پارامتر استفاده شوند.

فیلدهای `spec.validations` شامل عبارت‌های CEL هستند. اگر نتیجه‌ی ارزیابی یک عبارت false باشد،
بررسی اعتبارسنجی مطابق با فیلد `spec.failurePolicy` اِعمال می‌شود.

نویسنده‌ی سیاست پذیرش اعتبارسنجی مسئول ارائه‌ی CRD پارامتر ReplicaLimit است.

برای پیکربندی یک سیاست پذیرش اعتبارسنجی جهت استفاده در کلاستر، یک binding و یک منبع پارامتر
ایجاد می‌شوند. در ادامه نمونه‌ای از یک ValidatingAdmissionPolicyBinding آمده است
که از یک پارامتر **سراسری در سطح کلاستر** استفاده می‌کند؛ یعنی همان پارامتر برای اعتبارسنجی
هر درخواست منبعی که با binding مطابقت داشته باشد به کار می‌رود:

{{% code_sample language="yaml" file="validatingadmissionpolicy/binding-with-param.yaml" %}}

توجه کنید که این binding یک پارامتر را برای همه‌ی منابعی که در محیط `test` قرار دارند به سیاست اعمال می‌کند.

منبع پارامتر می‌تواند به شکل زیر باشد:

{{% code_sample language="yaml" file="validatingadmissionpolicy/replicalimit-param.yaml" %}}

این منبع پارامتر سیاست، استقرارها (deployments) را به حداکثر ۳ replica محدود می‌کند.

یک سیاست پذیرش می‌تواند چندین binding داشته باشد. برای اینکه سایر محیط‌ها
حد maxReplicas برابر ۱۰۰ داشته باشند، یک ValidatingAdmissionPolicyBinding دیگر ایجاد کنید:

{{% code_sample language="yaml" file="validatingadmissionpolicy/binding-with-param-prod.yaml" %}}

توجه کنید که این binding یک پارامتر متفاوت را برای منابعی اعمال می‌کند که
در محیط `test` نیستند.

و یک منبع پارامتر داشته باشید:

{{% code_sample language="yaml" file="validatingadmissionpolicy/replicalimit-param-prod.yaml" %}}

برای هر درخواست پذیرش، API server عبارت‌های CEL مربوط به هر ترکیب
(policy, binding, param) را که با درخواست مطابقت دارد ارزیابی می‌کند. برای اینکه یک درخواست
پذیرفته شود، باید در **همه‌ی** ارزیابی‌ها موفق شود.

اگر چند binding با درخواست مطابقت داشته باشند، سیاست برای هر یک ارزیابی می‌شود،
و برای اینکه سیاست موفق در نظر گرفته شود، همه‌ی آن‌ها باید در ارزیابی موفق شوند.

اگر چند پارامتر با یک binding مطابقت داشته باشند، قواعد سیاست برای هر پارامتر ارزیابی می‌شوند،
و برای اینکه binding موفق در نظر گرفته شود، همه‌ی آن‌ها نیز باید موفق شوند.
bindingها می‌توانند معیارهای تطبیق همپوشان داشته باشند. سیاست برای هر
ترکیب binding-پارامتر مطابق ارزیابی می‌شود. حتی ممکن است یک سیاست چندین بار ارزیابی شود،
اگر چند binding با آن مطابقت داشته باشند یا یک binding واحد با چند پارامتر مطابقت داشته باشد.

اگر منبع پارامتر به سیاست متصل (bind) نشده باشد، آبجکت params که نمایانگر منبع پارامتر است تنظیم نخواهد شد؛
بنابراین برای سیاست‌هایی که به یک منبع پارامتر نیاز دارند، افزودن بررسی‌ای برای اطمینان از متصل‌بودن آن می‌تواند مفید باشد. اگر `paramKind` سیاست یا `paramRef` در binding مشخص نشده باشد، هیچ منبع پارامتری متصل نمی‌شود و `params` برابر null خواهد بود.

برای موارد استفاده‌ای که به پیکربندی پارامتر نیاز دارند، توصیه می‌کنیم یک بررسی پارامتر را در
`spec.validations[0].expression` اضافه کنید:

```
- expression: "params != null"
  message: "params missing but required to bind to this policy"
```

#### پارامترهای اختیاری {#optional-parameters}

داشتن پارامترهای اختیاری به‌عنوان بخشی از یک منبع پارامتر، و اعتبارسنجی آن‌ها فقط در صورت وجود، می‌تواند راحت باشد. CEL ماکروی `has()` را فراهم می‌کند که پیش از آنکه یک عبارت CEL به مقدار یک فیلد دسترسی پیدا کند، وجود آن فیلد را بررسی می‌کند.
CEL همچنین میان‌بر منطقی (short-circuiting) بولی را پیاده‌سازی می‌کند. اگر نیمه‌ی اول یک OR منطقی true ارزیابی شود،
نیمه‌ی دیگر ارزیابی نمی‌شود (زیرا نتیجه‌ی کل OR صرف‌نظر از آن true خواهد بود).

با ترکیب این دو، می‌توانیم راهی برای اعتبارسنجی پارامترهای اختیاری فراهم کنیم:

`!has(params.optionalNumber) || (params.optionalNumber >= 5 && params.optionalNumber <= 10)`

در اینجا، ابتدا با `!has(params.optionalNumber)` بررسی می‌کنیم که آیا پارامتر اختیاری وجود ندارد.

- اگر `optionalNumber` تعریف نشده باشد، عبارت میان‌بر می‌زند، زیرا
  `!has(params.optionalNumber)` برابر true ارزیابی می‌شود.
- اگر `optionalNumber` تعریف شده باشد، نیمه‌ی دوم عبارت CEL ارزیابی می‌شود،
  و optionalNumber بررسی می‌شود تا اطمینان حاصل شود که مقداری بین ۵ و ۱۰ (با احتساب هر دو مرز) دارد.

برای بررسی وجود یک فیلد از `has()` استفاده کنید. برای بررسی اینکه یک map حاوی یک کلید است، به‌جای آن از عملگر `in` استفاده کنید. برای مثال،
`has(object.metadata.labels) && 'example.com/environment' in object.metadata.labels` بررسی می‌کند که
فیلد `metadata.labels` وجود دارد و map شامل کلید `example.com/environment` است.
برای دسترسی به فیلدهای اختیاری چندسطحی، نحو اختیاری CEL را ترجیح دهید (کوبرنتیز ۱.۲۹ و بالاتر):
`object.?metadata.labels['example.com/block'].orValue('')` فیلدهای میانیِ غایب را به‌صورت ایمن پیمایش می‌کند
و مقدار پیش‌فرض داده‌شده را بازمی‌گرداند.

#### پارامترهای هر فضای نام (Per-namespace Parameters) {#per-namespace-parameters}

به‌عنوان نویسنده‌ی یک ValidatingAdmissionPolicy و ValidatingAdmissionPolicyBinding آن،
می‌توانید پارامترهای سراسری در سطح کلاستر یا پارامترهای مخصوص هر فضای نام را مشخص کنید.
اگر برای `paramRef` در binding یک `namespace` مشخص کنید، control plane فقط
در آن فضای نام به دنبال پارامترها می‌گردد.

با این حال، اگر `namespace` در ValidatingAdmissionPolicyBinding مشخص نشده باشد،
API server می‌تواند پارامترهای مرتبط را در فضای نامی که درخواست علیه آن انجام شده جست‌وجو کند.
برای مثال، اگر درخواستی برای تغییر یک ConfigMap در فضای نام `default` ارسال کنید و
یک ValidatingAdmissionPolicyBinding مرتبط بدون `namespace` وجود داشته باشد،
API server به دنبال یک آبجکت پارامتر در `default` می‌گردد.
این طراحی پیکربندی سیاستی را ممکن می‌سازد که به فضای نام منبعِ در حال دست‌کاری وابسته است، و کنترل دقیق‌تری فراهم می‌کند.

#### انتخابگر پارامتر (Parameter selector) {#parameter-selector}

علاوه بر مشخص‌کردن یک پارامتر در binding با `name`، می‌توانید
به‌جای آن یک انتخابگر برچسب (label selector) مشخص کنید، به‌گونه‌ای که همه‌ی منابعی از
`paramKind` سیاست، و `namespace` پارامتر (در صورت کاربرد) که با
انتخابگر برچسب مطابقت دارند، برای ارزیابی انتخاب شوند. برای اطلاعات بیشتر درباره‌ی نحوه‌ی تطبیق انتخابگرهای برچسب با منابع، به {{< glossary_tooltip text="انتخابگر (selector)" term_id="selector">}} مراجعه کنید.

اگر مشخص شود که چند پارامتر شرط را برآورده می‌کنند، قواعد سیاست برای
هر پارامتر یافت‌شده ارزیابی می‌شوند و نتایج با هم AND می‌شوند.

اگر `namespace` ارائه شود، فقط آبجکت‌هایی از `paramKind` که در فضای نام ارائه‌شده قرار دارند
واجد شرایط انتخاب هستند. در غیر این صورت، وقتی `namespace` خالی باشد و
`paramKind` در سطح فضای نام (namespace-scoped) باشد، از `namespace` درخواستی که
در حال پذیرش است استفاده خواهد شد.

#### بررسی‌های مجوزدهی (Authorization checks) {#authorization-check}

بررسی مجوزدهی برای منابع پارامتر معرفی شده است.
انتظار می‌رود کاربر به منابعی که در `paramKind` در
`ValidatingAdmissionPolicy` و در `paramRef` در `ValidatingAdmissionPolicyBinding` به آن‌ها ارجاع داده شده، دسترسی `read` داشته باشد.

توجه داشته باشید که اگر تعیین یک منبع در `paramKind` از طریق restmapper با شکست مواجه شود، دسترسی `read` به همه‌ی
منابع گروه‌ها لازم است.

#### `paramRef`

فیلد `paramRef` منبع پارامتری را که سیاست استفاده می‌کند مشخص می‌کند. این فیلد دارای فیلدهای زیر است:

- **name**: نام منبع پارامتر.
- **namespace**: فضای نام منبع پارامتر.
- **selector**: یک انتخابگر برچسب برای تطبیق چند منبع پارامتر.
- **parameterNotFoundAction**: (الزامی) رفتار را هنگامی که پارامترهای مشخص‌شده یافت نشوند کنترل می‌کند.

  - **مقادیر مجاز**:
    - **`Allow`**: نبودِ پارامترهای مطابق، توسط binding به‌عنوان اعتبارسنجی موفق تلقی می‌شود.
    - **`Deny`**: نبودِ پارامترهای مطابق مشمول `failurePolicy` سیاست می‌شود.

باید یکی از `name` یا `selector` تنظیم شود، اما نه هر دو.

{{< note >}}
فیلد `parameterNotFoundAction` در `paramRef` **الزامی** است. این فیلد اقدامی را که باید هنگام نبودِ پارامتر مطابق با `paramRef` انجام شود مشخص می‌کند. اگر مشخص نشود، ممکن است policy binding نامعتبر تلقی شود و نادیده گرفته شود یا به رفتار پیش‌بینی‌نشده منجر شود.

- **`Allow`**: اگر روی `Allow` تنظیم شود و هیچ پارامتری یافت نشود، binding نبودِ پارامترها را اعتبارسنجی موفق تلقی می‌کند و سیاست گذرانده‌شده در نظر گرفته می‌شود.
- **`Deny`**: اگر روی `Deny` تنظیم شود و هیچ پارامتری یافت نشود، binding مقدار `failurePolicy` سیاست را اِعمال می‌کند. اگر `failurePolicy` برابر `Fail` باشد، درخواست رد می‌شود.

حتماً `parameterNotFoundAction` را مطابق با رفتار مطلوب در زمان نبودِ پارامترها تنظیم کنید.
{{< /note >}}

#### مدیریت پارامترهای مفقود با `parameterNotFoundAction` {#handling-missing-parameters-with-parameternotfoundaction}

هنگام استفاده از `paramRef` همراه با selector، ممکن است هیچ پارامتری با selector مطابقت نداشته باشد. فیلد `parameterNotFoundAction` تعیین می‌کند که binding در این سناریو چگونه رفتار کند.

**مثال:**

```yaml
apiVersion: admissionregistration.k8s.io/v1alpha1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: example-binding
spec:
  policyName: example-policy
  paramRef:
    selector:
      matchLabels:
        environment: test
    parameterNotFoundAction: Allow
  validationActions:
  - Deny
```  

### سیاست شکست (Failure Policy) {#failure-policy}

`failurePolicy` تعیین می‌کند که پیکربندی‌های نادرست و عبارت‌های CEL که در سیاست پذیرش به خطا منجر می‌شوند
چگونه مدیریت شوند. مقادیر مجاز `Ignore` یا `Fail` هستند.

- `Ignore` به این معناست که خطا در فراخوانی ValidatingAdmissionPolicy نادیده گرفته می‌شود و اجازه داده می‌شود
  درخواست API ادامه یابد.
- `Fail` به این معناست که خطا در فراخوانی ValidatingAdmissionPolicy باعث شکست پذیرش
  و رد شدن درخواست API می‌شود.

توجه داشته باشید که `failurePolicy` درون `ValidatingAdmissionPolicy` تعریف می‌شود:

{{% code_sample language="yaml" file="validatingadmissionpolicy/failure-policy-ignore.yaml" %}}

### عبارت اعتبارسنجی (Validation Expression)

`spec.validations[i].expression` عبارتی را نمایش می‌دهد که توسط CEL ارزیابی خواهد شد.
برای کسب اطلاعات بیشتر، [مشخصات زبان CEL](https://github.com/google/cel-spec) را ببینید.
عبارت‌های CEL به محتوای درخواست/پاسخ پذیرش (Admission) دسترسی دارند که در قالب متغیرهای CEL سازمان‌دهی شده است، و همچنین به چند متغیر مفید دیگر:

- 'object' - آبجکت موجود در درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- 'oldObject' - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- 'request' - ویژگی‌های [درخواست پذیرش](/docs/reference/config-api/apiserver-admission.v1/#admission-k8s-io-v1-AdmissionRequest).
- 'params' - منبع پارامتر که توسط policy binding در حال ارزیابی به آن ارجاع داده شده است. اگر `ParamKind` مشخص نشده باشد، مقدار آن null است.
- `namespaceObject` - فضای نام (namespace)، به‌صورت یک منبع کوبرنتیز، که آبجکت ورودی به آن تعلق دارد. اگر آبجکت ورودی در سطح کلاستر (cluster-scoped) باشد، مقدار آن null است.
- `authorizer` - یک CEL Authorizer. می‌توان از آن برای انجام بررسی‌های احراز مجوز (authorization) برای principal (کاربر احراز هویت‌شده) درخواست استفاده کرد. برای جزئیات بیشتر، [AuthzSelectors](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors) و [Authz](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz) را در مستندات کتابخانه CEL کوبرنتیز ببینید.
- `authorizer.requestResource` - میان‌بری برای یک بررسی احراز مجوز که با منبع درخواست (group، resource، (subresource)، namespace، name) پیکربندی شده است.

در عبارت‌های CEL، متغیرهایی مانند `object` و `oldObject` به‌صورت قوی‌نوع (strongly-typed) هستند.
می‌توانید به هر فیلد در طرحواره (schema) آبجکت، مانند `object.metadata.labels` و فیلدهای داخل `spec`، دسترسی داشته باشید.

برای هر آبجکت کوبرنتیز، از جمله Custom Resourceهای بدون طرحواره (schemaless)، CEL دسترسی به مجموعه‌ای حداقلی از ویژگی‌ها را تضمین می‌کند:
`apiVersion`، `kind`، `metadata.name` و `metadata.generateName`.

مقایسه برابری روی آرایه‌هایی که نوع فهرست آن‌ها 'set' یا 'map' است، ترتیب عناصر را نادیده می‌گیرد؛ یعنی [1, 2] == [2, 1].
الحاق (concatenation) روی آرایه‌هایی که x-kubernetes-list-type دارند از معناشناسی نوع فهرست پیروی می‌کند:

- 'set': عبارت `X + Y` یک اجتماع (union) انجام می‌دهد که در آن موقعیت آرایه‌ای همه عناصر `X` حفظ می‌شود و عناصر `Y` که با `X` اشتراک ندارند، با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.
- 'map': عبارت `X + Y` یک ادغام (merge) انجام می‌دهد که در آن موقعیت آرایه‌ای همه کلیدهای `X` حفظ می‌شود، اما در صورت اشتراک مجموعه کلیدهای `X` و `Y`، مقادیر با مقادیر `Y` بازنویسی می‌شوند. عناصر `Y` که کلیدهای غیرمشترک دارند، با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.

#### نمونه‌هایی از عبارت‌های اعتبارسنجی

| عبارت                                                                                        | هدف                                                                               |
|----------------------------------------------------------------------------------------------| ------------                                                                      |
| `object.minReplicas <= object.replicas && object.replicas <= object.maxReplicas`             | اعتبارسنجی اینکه سه فیلدِ تعریف‌کننده replicas به‌درستی مرتب شده‌اند               |
| `'Available' in object.stateCounts`                                                          | اعتبارسنجی اینکه ورودی‌ای با کلید 'Available' در یک map وجود دارد                 |
| `(size(object.list1) == 0) != (size(object.list2) == 0)`                                     | اعتبارسنجی اینکه یکی از دو فهرست خالی نیست، اما هر دو با هم غیرخالی نیستند        |
| <code>!('MY_KEY' in object.map1) &#124;&#124; object.map1['MY_KEY'].matches('^[a-zA-Z]*$')</code> | اعتبارسنجی مقدار یک map برای یک کلید مشخص، در صورتی که آن کلید در map وجود داشته باشد |
| `object.envars.filter(e, e.name == 'MY_ENV').all(e, e.value.matches('^[a-zA-Z]*$')`          | اعتبارسنجی فیلد 'value' در ورودی listMap که فیلد کلید 'name' آن برابر 'MY_ENV' است |
| `has(object.expired) && object.created + object.ttl < object.expired`                        | اعتبارسنجی اینکه تاریخ 'expired' پس از تاریخ 'create' به‌اضافه مدت 'ttl' است      |
| `object.health.startsWith('ok')`                                                             | اعتبارسنجی اینکه فیلد رشته‌ای 'health' با پیشوند 'ok' آغاز می‌شود                 |
| `object.widgets.exists(w, w.key == 'x' && w.foo < 10)`                                       | اعتبارسنجی اینکه ویژگی 'foo' از آیتم listMap با کلید 'x' کمتر از 10 است           |
| `type(object) == string ? object == '100%' : object == 1000`                                 | اعتبارسنجی یک فیلد int-or-string برای هر دو حالت عدد صحیح و رشته                  |
| `object.metadata.name.startsWith(object.prefix)`                                             | اعتبارسنجی اینکه نام یک آبجکت با مقدار فیلدی دیگر پیشوند دارد                     |
| `object.set1.all(e, !(e in object.set2))`                                                    | اعتبارسنجی اینکه دو listSet از هم جدا (disjoint) هستند                            |
| `size(object.names) == size(object.details) && object.names.all(n, n in object.details)`     | اعتبارسنجی اینکه map با نام 'details' بر اساس آیتم‌های listSet با نام 'names' کلیدگذاری شده است |
| `size(object.clusters.filter(c, c.name == object.primary)) == 1`                             | اعتبارسنجی اینکه ویژگی 'primary' دقیقاً یک بار در listMap با نام 'clusters' رخ داده است |

برای اطلاعات بیشتر درباره قواعد CEL، [Supported evaluation on CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#evaluation) را مطالعه کنید.

`spec.validation[i].reason` توصیفی قابل‌خواندن برای ماشین است که علت شکست این اعتبارسنجی را بیان می‌کند.
اگر این نخستین اعتبارسنجی در فهرست باشد که شکست می‌خورد، این reason و همچنین کد پاسخ HTTP متناظر با آن در پاسخ HTTP به کلاینت استفاده می‌شود.
reasonهای پشتیبانی‌شده در حال حاضر عبارت‌اند از: `Unauthorized`، `Forbidden`، `Invalid`، `RequestEntityTooLarge`.
اگر مقداردهی نشود، `StatusReasonInvalid` در پاسخ به کلاینت استفاده می‌شود.

### تطبیق درخواست‌ها: `matchConditions` {#matching-requests-matchconditions}

اگر به فیلتر کردن دقیق‌تر درخواست‌ها نیاز دارید، می‌توانید برای یک `ValidatingAdmissionPolicy` _شرایط تطبیق_ (match conditions) تعریف کنید. این
شرایط زمانی مفیدند که قواعد تطبیق، `objectSelectors` و `namespaceSelectors` همچنان
فیلتر مورد نظر شما را فراهم نمی‌کنند. شرایط تطبیق
[عبارت‌های CEL](/docs/reference/using-api/cel/) هستند. برای اینکه منبع ارزیابی شود، همه شرایط تطبیق باید true ارزیابی شوند.

در ادامه مثالی آمده است که چند کاربرد مختلف شرایط تطبیق را نشان می‌دهد:

{{% code_sample file="access/validating-admission-policy-match-conditions.yaml" %}}

شرایط تطبیق به همان متغیرهای CEL دسترسی دارند که عبارت‌های اعتبارسنجی دارند، به‌جز
`namespaceObject` و `variables`:

- `namespaceObject` برای شرایط تطبیق مقداردهی نمی‌شود و همیشه null ارزیابی می‌شود. برای انتخاب
  درخواست‌ها بر اساس برچسب‌های namespace، از یک `namespaceSelector` در `matchConstraints` سیاست
  یا در `matchResources` مربوط به binding استفاده کنید. برای بررسی سایر فیلدهای namespace، از یک عبارت
  اعتبارسنجی استفاده کنید که در آن `namespaceObject` در دسترس است.
- به `variables` نمی‌توان از شرایط تطبیق ارجاع داد، زیرا شرایط تطبیق
  پیش از بقیه بخش‌های سیاست ارزیابی می‌شوند.

در صورت بروز خطا هنگام ارزیابی یک شرط تطبیق، سیاست ارزیابی نمی‌شود. اینکه درخواست رد شود یا نه، به شکل زیر تعیین می‌شود:

1. اگر **هر** شرط تطبیقی `false` ارزیابی شود (صرف‌نظر از خطاهای دیگر)، سرور API سیاست را نادیده می‌گیرد.
2. در غیر این صورت:
   - برای [`failurePolicy: Fail`](#failure-policy)، درخواست رد می‌شود (بدون ارزیابی سیاست).
   - برای [`failurePolicy: Ignore`](#failure-policy)، درخواست ادامه می‌یابد اما سیاست نادیده گرفته می‌شود.

### حاشیه‌نویسی‌های ممیزی (Audit annotations) {#audit-annotations}

`auditAnnotations` را می‌توان برای افزودن حاشیه‌نویسی‌های ممیزی (audit annotations) به رویداد ممیزی درخواست API به کار برد.

برای مثال، در ادامه یک سیاست پذیرش (admission policy) همراه با یک audit annotation آمده است:

{{% code_sample file="access/validating-admission-policy-audit-annotation.yaml" %}}

هنگامی که یک درخواست API با این سیاست پذیرش اعتبارسنجی شود، رویداد ممیزی حاصل به شکل زیر خواهد بود:

```
# the audit event recorded
{
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "annotations": {
        "demo-policy.example.com/high-replica-count": "Deployment spec.replicas set to 128"
        # other annotations
        ...
    }
    # other fields
    ...
}
```

در این مثال، annotation تنها در صورتی درج می‌شود که مقدار `spec.replicas` در Deployment بیشتر از 50 باشد؛ در غیر این صورت، عبارت CEL مقدار null را برمی‌گرداند و annotation درج نخواهد شد.

توجه کنید که کلیدهای audit annotation با نام `ValidatingAdmissionPolicy` و یک `/` پیشوند می‌گیرند. اگر
کنترل‌کننده پذیرش دیگری، مانند یک admission webhook، دقیقاً از همان کلید audit annotation استفاده کند،
مقدار نخستین کنترل‌کننده پذیرشی که audit annotation را درج کرده است در رویداد ممیزی قرار می‌گیرد
و سایر مقادیر نادیده گرفته می‌شوند.

### عبارت پیام (Message expression) {#message-expression}

برای بازگرداندن پیامی کاربرپسندتر هنگامی که سیاست یک درخواست را رد می‌کند، می‌توانیم از یک عبارت CEL
برای ساخت پیام با `spec.validations[i].messageExpression` استفاده کنیم. مشابه عبارت اعتبارسنجی،
عبارت پیام به `object`، `oldObject`، `request`، `params` و `namespaceObject` دسترسی دارد.
برخلاف اعتبارسنجی‌ها، عبارت پیام باید به یک رشته ارزیابی شود.

برای مثال، برای اطلاع‌رسانی بهتر به کاربر درباره علت رد درخواست، وقتی سیاست به یک پارامتر ارجاع می‌دهد،
می‌توانیم اعتبارسنجی زیر را داشته باشیم:

{{% code_sample file="access/deployment-replicas-policy.yaml" %}}

پس از ایجاد یک آبجکت params که replicas را به 3 محدود می‌کند و برپا کردن binding،
هنگامی که تلاش کنیم یک deployment با 5 replica ایجاد کنیم، پیام زیر را دریافت خواهیم کرد.

```
$ kubectl create deploy --image=nginx nginx --replicas=5
error: failed to create deployment: deployments.apps "nginx" is forbidden: ValidatingAdmissionPolicy 'deploy-replica-policy.example.com' with binding 'demo-binding-test.example.com' denied request: object.spec.replicas must be no greater than 3
```

این پیام از یک پیام ایستا مانند "too many replicas" اطلاعات بیشتری می‌دهد.

اگر هر دو تعریف شده باشند، عبارت پیام بر پیام ایستای تعریف‌شده در `spec.validations[i].message` اولویت دارد.
با این حال، اگر ارزیابی عبارت پیام با شکست مواجه شود، به‌جای آن از پیام ایستا استفاده می‌شود.
افزون بر این، اگر عبارت پیام به یک رشته چندخطی ارزیابی شود،
نتیجه ارزیابی کنار گذاشته می‌شود و در صورت وجود، از پیام ایستا استفاده خواهد شد.
توجه کنید که پیام ایستا از نظر چندخطی بودن اعتبارسنجی می‌شود.

### بررسی نوع (Type checking) {#type-checking}

هنگامی که تعریف یک سیاست ایجاد یا به‌روزرسانی می‌شود، فرایند اعتبارسنجی عبارت‌های موجود در آن را تجزیه می‌کند
و هر گونه خطای نحوی (syntax) را گزارش می‌دهد و در صورت یافتن هر خطا، تعریف را رد می‌کند.
سپس، متغیرهای ارجاع‌شده از نظر خطاهای نوع، از جمله فیلدهای ناموجود و اشتباه گرفتن نوع‌ها،
در برابر نوع‌های تطبیق‌یافته در `spec.matchConstraints` بررسی می‌شوند.
نتیجه بررسی نوع را می‌توان از `status.typeChecking` بازیابی کرد.
وجود `status.typeChecking` نشان‌دهنده تکمیل بررسی نوع است،
و خالی بودن `status.typeChecking` به این معناست که هیچ خطایی شناسایی نشده است.

برای مثال، با توجه به تعریف سیاست زیر:

{{< code_sample language="yaml" file="validatingadmissionpolicy/typechecking.yaml" >}}

وضعیت (status) اطلاعات زیر را نتیجه خواهد داد:

```yaml
status:
  typeChecking:
    expressionWarnings:
    - fieldRef: spec.validations[0].expression
      warning: |-
        apps/v1, Kind=Deployment: ERROR: <input>:1:7: undefined field 'replicas'
         | object.replicas > 1
         | ......^
```

اگر در `spec.matchConstraints` چند منبع تطبیق داده شوند، همه منابع تطبیق‌یافته بررسی خواهند شد.
برای مثال، تعریف سیاست زیر

{{% code_sample language="yaml" file="validatingadmissionpolicy/typechecking-multiple-match.yaml" %}}


چندین نوع خواهد داشت و نتیجه بررسی نوع هر نوع در پیام هشدار آمده است.

```yaml
status:
  typeChecking:
    expressionWarnings:
    - fieldRef: spec.validations[0].expression
      warning: |-
        apps/v1, Kind=Deployment: ERROR: <input>:1:7: undefined field 'replicas'
         | object.replicas > 1
         | ......^
        apps/v1, Kind=ReplicaSet: ERROR: <input>:1:7: undefined field 'replicas'
         | object.replicas > 1
         | ......^
```

بررسی نوع محدودیت‌های زیر را دارد:

- تطبیق با نویسه عام (wildcard) پشتیبانی نمی‌شود. اگر `spec.matchConstraints.resourceRules` در هر یک از `apiGroups`، `apiVersions` یا `resources` شامل `"*"` باشد،
  نوع‌هایی که `"*"` با آن‌ها تطبیق می‌یابد بررسی نخواهند شد.
- تعداد نوع‌های تطبیق‌یافته به 10 محدود شده است. این کار برای جلوگیری از سیاستی است که با تعیین دستی نوع‌های بسیار زیاد،
  منابع محاسباتی بیش از حد مصرف کند. به ترتیب صعودی group، سپس version و سپس resource، ترکیب یازدهم و بعد از آن نادیده گرفته می‌شوند.
- بررسی نوع به هیچ وجه بر رفتار سیاست تأثیر نمی‌گذارد. حتی اگر بررسی نوع خطاهایی را شناسایی کند، سیاست همچنان
  ارزیابی خواهد شد. اگر در هنگام ارزیابی خطایی رخ دهد، failure policy نتیجه آن را تعیین می‌کند.
- بررسی نوع برای CRDها، از جمله نوع‌های CRD تطبیق‌یافته و ارجاع paramKind، اعمال نمی‌شود. پشتیبانی از CRDها در نسخه‌های آینده خواهد آمد.

### ترکیب متغیرها (Variable composition) {#variable-composition}

اگر یک عبارت بیش از حد پیچیده شود، یا بخشی از عبارت قابل استفاده مجدد و ارزیابی آن از نظر محاسباتی پرهزینه باشد،
می‌توانید بخشی از عبارت‌ها را به متغیرها استخراج کنید. متغیر یک عبارت نام‌دار است که بعداً می‌توان
از طریق `variables` در عبارت‌های دیگر به آن ارجاع داد.

```yaml
spec:
  variables:
    - name: foo
      expression: "'foo' in object.spec.metadata.labels ? object.spec.metadata.labels['foo'] : 'default'"
  validations:
    - expression: variables.foo == 'bar'
```

یک متغیر به‌صورت تنبل (lazy) و هنگام نخستین ارجاع ارزیابی می‌شود. هر خطایی که در طول ارزیابی رخ دهد،
در زمان ارزیابی عبارتِ ارجاع‌دهنده گزارش می‌شود. هم نتیجه و هم خطای احتمالی حفظ می‌شوند
و فقط یک بار در هزینه زمان اجرا محاسبه می‌شوند.

ترتیب متغیرها مهم است، زیرا یک متغیر می‌تواند به متغیرهایی که پیش از آن تعریف شده‌اند ارجاع دهد.
این ترتیب از ارجاع‌های دوری جلوگیری می‌کند.

در ادامه مثالی پیچیده‌تر آمده است که اعمال می‌کند نام مخزن‌های ایمیج با محیط تعریف‌شده در namespace آن‌ها مطابقت داشته باشد.

{{< code_sample file="access/image-matches-namespace-environment.policy.yaml" >}}

وقتی سیاست به namespace با نام `default` که برچسب `environment: prod` دارد متصل شده باشد،
تلاش زیر برای ایجاد یک deployment رد خواهد شد.
```shell
kubectl create deploy --image=dev.example.com/nginx invalid
```
پیام خطا مشابه زیر است.
```console
error: failed to create deployment: deployments.apps "invalid" is forbidden: ValidatingAdmissionPolicy 'image-matches-namespace-environment.policy.example.com' with binding 'demo-binding-test.example.com' denied request: only prod images are allowed in namespace default
```

## انواع API معاف از اعتبارسنجی پذیرش {#api-kinds-exempt-from-admission-validation}

برخی انواع API از بررسی‌های اعتبارسنجی در زمان پذیرش معاف هستند. برای مثال، نمی‌توانید یک ValidatingAdmissionPolicy ایجاد کنید که از تغییر ValidatingAdmissionPolicyBindingها جلوگیری کند.

انواع پیکربندی پذیرش زیر از سیاست‌هایی که از طریق REST API ایجاد می‌شوند معاف هستند، تا از وابستگی‌های دوری جلوگیری شود:

* [ValidatingAdmissionPolicies]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-v1/" >}})
* [ValidatingAdmissionPolicyBindings]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1/" >}})
* MutatingAdmissionPolicies
* MutatingAdmissionPolicyBindings

{{< note >}}
هنگامی که از طریق
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/) پیکربندی شود،
یک ValidatingAdmissionPolicy می‌تواند انواع پیکربندی پذیرشِ فهرست‌شده در بالا را رهگیری کند. این کار
محدودیت‌هایی را که معمولاً برای سیاست‌های ایجادشده از طریق REST API اعمال می‌شود دور می‌زند و به شما امکان می‌دهد
حتی پیکربندی پذیرش و منابع حساس از نظر امنیتی را اعتبارسنجی کنید. برخلاف REST API، یک سیاست پذیرش مبتنی بر مانیفست
که اشتباه پیکربندی شده و این منابع را رهگیری می‌کند غیرقابل بازیابی نخواهد بود، زیرا به‌جای تعریف از طریق API، روی دیسک تعریف می‌شود.
{{< /note >}}

افزون بر این، انواع API احراز هویت و احراز مجوز غیرپایدار (مجازی) زیر از همه سیاست‌های پذیرش، از جمله سیاست‌های مبتنی بر مانیفست، معاف هستند، زیرا رهگیری آن‌ها می‌تواند کلاستر را از مسیر احراز هویت و احراز مجوز خودش قفل کند:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

از کوبرنتیز نسخه v1.37 به بعد،
[admission webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources)
نیز این منابع مجازی را به‌صورت پیش‌فرض مستثنا می‌کنند.

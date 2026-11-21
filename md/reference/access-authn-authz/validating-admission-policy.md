---
reviewers:
- liggitt
- jpbetz
- cici37
title: سیاست پذیرش اعتبارسنجی
content_type: concept
---

<!-- overview -->

{{< feature-state state="stable" for_k8s_version="v1.30" >}}

این صفحه مروری بر سیاست پذیرش اعتبارسنجی (Validating Admission Policy) ارائه می‌دهد.


<!-- body -->

## سیاست پذیرش اعتبارسنجی چیست؟

سیاست‌های پذیرش اعتبارسنجی جایگزینی اعلانی (declarative) و درون‌فرایندی (in-process) برای وب‌هوک‌های پذیرش اعتبارسنجی (validating admission webhooks) هستند.

این سیاست‌ها قواعد اعتبارسنجی هر سیاست را با زبان عبارت مشترک (Common Expression Language یا CEL) تعریف می‌کنند.
سیاست‌های پذیرش اعتبارسنجی بسیار پیکربندی‌پذیر هستند. نویسندگان سیاست می‌توانند سیاست‌هایی تعریف کنند که مدیران کلاستر بر حسب نیاز آن‌ها را پارامتری کنند و دامنهٔ اعمالشان را به منابع مشخصی محدود کنند.

## یک سیاست از چه منابعی تشکیل می‌شود

هر سیاست معمولاً از سه منبع تشکیل می‌شود:

- منبع `ValidatingAdmissionPolicy` منطق انتزاعی سیاست را توصیف می‌کند
  (برای مثال: «این سیاست اطمینان حاصل می‌کند که یک برچسب مشخص مقدار مشخصی داشته باشد»).

- منبع پارامتر اطلاعاتی را در اختیار ValidatingAdmissionPolicy قرار می‌دهد تا آن را به یک حکم مشخص و عینی تبدیل کند
  (برای مثال: «برچسب `owner` باید مقداری داشته باشد که به `.company.com` ختم شود»).
  طرح‌وارهٔ (schema) منبع پارامتر را یک نوع بومی مانند ConfigMap یا یک CRD تعریف می‌کند.
  آبجکت‌های `ValidatingAdmissionPolicy` مشخص می‌کنند که برای منبع پارامتر خود انتظار چه Kind ای را دارند.

- منبع `ValidatingAdmissionPolicyBinding` منابع بالا را به یکدیگر پیوند می‌دهد و دامنهٔ اعمال سیاست را تعیین می‌کند.
  اگر فقط می‌خواهید تنظیم برچسب `owner` را برای `Pods` الزامی کنید، این محدودیت را باید در همین اتصال (binding)
  مشخص کنید.

برای اینکه یک سیاست اثر داشته باشد، دست‌کم باید یک `ValidatingAdmissionPolicy` و یک `ValidatingAdmissionPolicyBinding`
متناظر با آن تعریف شده باشند.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
رزرو شده‌اند و نمی‌توان از آن‌ها برای سیاست‌ها یا اتصال‌های مبتنی بر API استفاده کرد. این محدودیت
زمانی اعمال می‌شود که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) با نام
`ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

اگر یک `ValidatingAdmissionPolicy` نیازی به پیکربندی از طریق پارامترها ندارد، کافی است فیلد
`spec.paramKind` را در `ValidatingAdmissionPolicy` مشخص نکنید.

## شروع کار با سیاست پذیرش اعتبارسنجی

سیاست پذیرش اعتبارسنجی بخشی از control plane کلاستر است. این سیاست‌ها را باید با احتیاط فراوان بنویسید و مستقر کنید.
در ادامه توضیح داده می‌شود که چگونه می‌توانید به‌سرعت با سیاست پذیرش اعتبارسنجی آزمایش کنید.

### ایجاد یک ValidatingAdmissionPolicy

نمونهٔ زیر یک ValidatingAdmissionPolicy را نشان می‌دهد.

{{% code_sample language="yaml" file="validatingadmissionpolicy/basic-example-policy.yaml" %}}

فیلد `spec.validations` شامل عبارت‌هایی است که با استفاده از [زبان عبارت مشترک (CEL)](https://github.com/google/cel-spec)
درخواست را اعتبارسنجی می‌کنند. اگر یک عبارت به false ارزیابی شود، بررسی اعتبارسنجی
مطابق فیلد `spec.failurePolicy` اعمال می‌شود.

{{< note >}}
می‌توانید عبارت‌های CEL را به‌سرعت در [CEL Playground](https://playcel.undistro.io) آزمایش کنید.
{{< /note >}}

برای پیکربندی یک سیاست پذیرش اعتبارسنجی جهت استفاده در کلاستر، به یک اتصال نیاز است.
نمونهٔ زیر یک ValidatingAdmissionPolicyBinding را نشان می‌دهد:

{{% code_sample language="yaml" file="validatingadmissionpolicy/basic-example-binding.yaml" %}}

اگر بخواهید یک Deployment با تعداد replicaهایی ایجاد کنید که عبارت اعتبارسنجی را برآورده نمی‌کند،
خطایی با پیام زیر بازگردانده می‌شود:

```none
ValidatingAdmissionPolicy 'demo-policy.example.com' with binding 'demo-binding-test.example.com' denied request: failed expression: object.spec.replicas <= 5
```

نمونهٔ بالا مثال ساده‌ای از استفاده از ValidatingAdmissionPolicy بدون پیکربندی پارامتر است.

#### کنش‌های اعتبارسنجی

هر `ValidatingAdmissionPolicyBinding` باید یک یا چند مقدار
`validationActions` مشخص کند تا نحوهٔ اعمال `validations` سیاست را تعیین کند.

مقادیر پشتیبانی‌شده برای `validationActions` عبارت‌اند از:

- مقدار `Deny`: شکست اعتبارسنجی به رد درخواست منجر می‌شود.
- مقدار `Warn`: شکست اعتبارسنجی به‌صورت یک [هشدار](/blog/2020/09/03/warnings/)
  به کلاینت درخواست‌دهنده گزارش می‌شود.
- مقدار `Audit`: شکست اعتبارسنجی در رویداد ممیزی (audit event) مربوط به درخواست API درج می‌شود.

برای مثال، اگر می‌خواهید هم به کلاینت‌ها دربارهٔ شکست اعتبارسنجی هشدار دهید و هم
شکست‌های اعتبارسنجی را ممیزی کنید، از این تنظیم استفاده کنید:

```yaml
validationActions: [Warn, Audit]
```

نمی‌توان `Deny` و `Warn` را همزمان به کار برد، زیرا این ترکیب
شکست اعتبارسنجی را بی‌جهت هم در بدنهٔ پاسخ API
و هم در سرآیندهای هشدار HTTP تکرار می‌کند.

هر `validation` که به false ارزیابی شود، همواره مطابق این کنش‌ها
اعمال می‌شود. شکست‌هایی که با `failurePolicy` تعریف می‌شوند فقط در صورتی
مطابق این کنش‌ها اعمال می‌شوند که `failurePolicy` روی `Fail` تنظیم شده باشد (یا مشخص نشده باشد)؛
در غیر این صورت، این شکست‌ها نادیده گرفته می‌شوند.

برای جزئیات بیشتر دربارهٔ حاشیه‌نویسی (annotation) ممیزیِ شکست اعتبارسنجی، به
[حاشیه‌نویسی‌های ممیزی: شکست‌های اعتبارسنجی](/docs/reference/labels-annotations-taints/audit-annotations/#validation-policy-admission-k8s-io-validation-failure)
مراجعه کنید.

### منابع پارامتر

منابع پارامتر باعث می‌شوند پیکربندی سیاست از تعریف آن جدا باشد.
هر سیاست می‌تواند فیلد paramKind را تعریف کند که GVK منبع پارامتر را مشخص می‌کند؛
سپس یک اتصال سیاست، آن سیاست را با نامش (از طریق policyName) و از طریق paramRef به یک منبع پارامتر مشخص پیوند می‌دهد.

اگر به پیکربندی پارامتر نیاز باشد، نمونهٔ زیر یک ValidatingAdmissionPolicy
همراه با پیکربندی پارامتر را نشان می‌دهد.

{{% code_sample language="yaml" file="validatingadmissionpolicy/policy-with-param.yaml" %}}

فیلد `spec.paramKind` در ValidatingAdmissionPolicy نوع منابعی را مشخص می‌کند که برای
پارامتری کردن این سیاست به کار می‌روند. در این مثال، سیاست با منابع سفارشی ReplicaLimit پیکربندی می‌شود.
به این نکته توجه کنید که در این مثال، عبارت CEL از طریق متغیر params در CEL به پارامترها ارجاع می‌دهد،
مانند `params.maxReplicas`. فیلد `spec.matchConstraints` مشخص می‌کند که این سیاست
برای اعتبارسنجی چه منابعی طراحی شده است. توجه داشته باشید که انواع بومی مانند `ConfigMap` نیز می‌توانند
به‌عنوان مرجع پارامتر استفاده شوند.

فیلدهای `spec.validations` شامل عبارت‌های CEL هستند. اگر یک عبارت به false ارزیابی شود،
بررسی اعتبارسنجی مطابق فیلد `spec.failurePolicy` اعمال می‌شود.

تأمین CRD پارامتر ReplicaLimit بر عهدهٔ نویسندهٔ سیاست پذیرش اعتبارسنجی است.

برای پیکربندی یک سیاست پذیرش اعتبارسنجی جهت استفاده در کلاستر، یک اتصال و یک منبع پارامتر
ایجاد می‌شوند. نمونهٔ زیر یک ValidatingAdmissionPolicyBinding را نشان می‌دهد
که از یک پارامتر **در سطح کل کلاستر** استفاده می‌کند؛ یعنی همان پارامتر برای اعتبارسنجی
همهٔ درخواست‌های منبعی که با این اتصال مطابقت دارند به کار می‌رود:

{{% code_sample language="yaml" file="validatingadmissionpolicy/binding-with-param.yaml" %}}

توجه کنید که این اتصال، پارامتر را برای همهٔ منابعی که
در محیط `test` قرار دارند به سیاست اعمال می‌کند.

منبع پارامتر می‌تواند به شکل زیر باشد:

{{% code_sample language="yaml" file="validatingadmissionpolicy/replicalimit-param.yaml" %}}

این منبع پارامتر سیاست، تعداد replicaهای Deploymentها را حداکثر به ۳ محدود می‌کند.

یک سیاست پذیرش می‌تواند چندین اتصال داشته باشد. برای اینکه همهٔ محیط‌های دیگر
محدودیت maxReplicas برابر ۱۰۰ داشته باشند، یک ValidatingAdmissionPolicyBinding دیگر ایجاد کنید:

{{% code_sample language="yaml" file="validatingadmissionpolicy/binding-with-param-prod.yaml" %}}

توجه کنید که این اتصال، پارامتر متفاوتی را بر منابعی اعمال می‌کند که
در محیط `test` قرار ندارند.

و منبع پارامتر زیر را نیز ایجاد کنید:

{{% code_sample language="yaml" file="validatingadmissionpolicy/replicalimit-param-prod.yaml" %}}

سرور API برای هر درخواست پذیرش، عبارت‌های CEL هر ترکیب
(سیاست، اتصال، پارامتر) را که با درخواست مطابقت دارد ارزیابی می‌کند. درخواست
فقط زمانی پذیرفته می‌شود که از **همهٔ** ارزیابی‌ها با موفقیت عبور کند.

اگر چند اتصال با درخواست مطابقت داشته باشند، سیاست برای هر یک از آن‌ها ارزیابی می‌شود
و برای اینکه سیاست موفق تلقی شود، همهٔ این ارزیابی‌ها باید موفق باشند.

اگر چند پارامتر با یک اتصال واحد مطابقت داشته باشند، قواعد سیاست برای هر پارامتر ارزیابی
می‌شوند و برای اینکه اتصال موفق تلقی شود، همهٔ این ارزیابی‌ها نیز باید موفق باشند.
معیارهای تطبیق اتصال‌ها می‌توانند با یکدیگر همپوشانی داشته باشند. سیاست برای هر ترکیب
اتصال-پارامترِ مطابق ارزیابی می‌شود. حتی ممکن است یک سیاست چندین بار ارزیابی شود؛
چه به این دلیل که چند اتصال با آن مطابقت دارند و چه به این دلیل که یک اتصال واحد
با چند پارامتر مطابقت دارد.

اگر هیچ منبع پارامتری متصل نشده باشد، آبجکت params که نمایانگر منبع پارامتر است مقداردهی نمی‌شود؛
بنابراین در سیاست‌هایی که به منبع پارامتر نیاز دارند، افزودن بررسی‌ای برای اطمینان از
متصل بودن یک منبع پارامتر می‌تواند مفید باشد. اگر `paramKind` سیاست یا `paramRef` اتصال
مشخص نشده باشد، هیچ منبع پارامتری متصل نمی‌شود و `params` برابر null خواهد بود.

برای مواردی که به پیکربندی پارامتر نیاز دارند، توصیه می‌کنیم یک بررسی پارامتر در
`spec.validations[0].expression` اضافه کنید:

```
- expression: "params != null"
  message: "params missing but required to bind to this policy"
```

#### پارامترهای اختیاری

گاهی مفید است که منبع پارامتر شامل پارامترهای اختیاری باشد و این پارامترها
فقط در صورت وجود اعتبارسنجی شوند. زبان CEL ماکروی `has()` را فراهم می‌کند که پیش از
دسترسی یک عبارت CEL به مقدار یک فیلد، وجود آن فیلد را بررسی می‌کند.
همچنین CEL ارزیابی کوتاه‌مدار (short-circuit) عبارت‌های بولی را پیاده‌سازی می‌کند. اگر نیمهٔ اول یک OR منطقی به true ارزیابی شود،
نیمهٔ دیگر ارزیابی نمی‌شود (زیرا نتیجهٔ کل OR در هر صورت true خواهد بود).

با ترکیب این دو، می‌توان پارامترهای اختیاری را اعتبارسنجی کرد:

`!has(params.optionalNumber) || (params.optionalNumber >= 5 && params.optionalNumber <= 10)`

در اینجا ابتدا با `!has(params.optionalNumber)` بررسی می‌کنیم که آیا پارامتر اختیاری وجود ندارد.

- اگر `optionalNumber` تعریف نشده باشد، ارزیابی عبارت کوتاه‌مدار می‌شود، زیرا
  `!has(params.optionalNumber)` به true ارزیابی خواهد شد.
- اگر `optionalNumber` تعریف شده باشد، نیمهٔ دوم عبارت CEL ارزیابی می‌شود
  و optionalNumber بررسی می‌شود تا اطمینان حاصل شود که مقداری بین ۵ تا ۱۰
  (شامل خود این دو عدد) دارد.

برای بررسی وجود فیلد از `has()` استفاده کنید. برای بررسی اینکه یک نگاشت (map) کلید مشخصی دارد یا نه،
به‌جای آن از عملگر `in` استفاده کنید. برای مثال، عبارت
`has(object.metadata.labels) && 'example.com/environment' in object.metadata.labels` بررسی می‌کند که
فیلد `metadata.labels` وجود دارد و نگاشت شامل کلید `example.com/environment` است.
برای دسترسی به فیلدهای اختیاری چندسطحی، بهتر است از نحو اختیاری CEL (کوبرنتیز 1.29 و بالاتر) استفاده کنید:
عبارت `object.?metadata.labels['example.com/block'].orValue('')` فیلدهای میانیِ غایب را به‌صورت ایمن
پیمایش می‌کند و مقدار پیش‌فرض داده‌شده را بازمی‌گرداند.

#### پارامترهای مختص هر فضای نام

شما به‌عنوان نویسندهٔ یک ValidatingAdmissionPolicy و ValidatingAdmissionPolicyBinding آن،
می‌توانید پارامترها را در سطح کل کلاستر یا به‌صورت مختص هر فضای نام (namespace) مشخص کنید.
اگر برای `paramRef` اتصال یک `namespace` مشخص کنید، control plane فقط
در همان فضای نام به دنبال پارامترها می‌گردد.

اما اگر `namespace` در ValidatingAdmissionPolicyBinding مشخص نشده باشد،
سرور API می‌تواند در فضای نامی که درخواست به آن مربوط است به دنبال پارامترهای مرتبط بگردد.
برای مثال، اگر درخواستی برای تغییر یک ConfigMap در فضای نام `default` ارسال کنید و
یک ValidatingAdmissionPolicyBinding مرتبط بدون تنظیم `namespace` وجود داشته باشد،
سرور API در `default` به دنبال یک آبجکت پارامتر می‌گردد.
این طراحی امکان پیکربندی سیاستی را فراهم می‌کند که به فضای نام منبعِ در حال تغییر
وابسته است و به این ترتیب کنترل دقیق‌تری به دست می‌دهد.

#### انتخابگر پارامتر

به‌جای مشخص کردن پارامتر با `name` در اتصال، می‌توانید
یک انتخابگر برچسب (label selector) تعیین کنید تا همهٔ منابعی از نوع `paramKind` سیاست که
در `namespace` پارامتر قرار دارند (در صورت کاربرد) و با انتخابگر برچسب مطابقت دارند،
برای ارزیابی انتخاب شوند. برای اطلاعات بیشتر دربارهٔ نحوهٔ تطبیق انتخابگرهای برچسب با منابع، به {{< glossary_tooltip text="انتخابگر" term_id="selector">}} مراجعه کنید.

اگر چند پارامتر شرط را برآورده کنند، قواعد سیاست برای هر یک از پارامترهای
یافت‌شده ارزیابی می‌شوند و نتایج با AND منطقی با یکدیگر ترکیب می‌شوند.

اگر `namespace` مشخص شده باشد، فقط آبجکت‌هایی از نوع `paramKind` که در
فضای نام مشخص‌شده قرار دارند قابل انتخاب هستند. در غیر این صورت، وقتی `namespace` خالی باشد و
`paramKind` در محدودهٔ فضای نام تعریف شده باشد (namespace-scoped)، از `namespace` درخواستِ
در حال پذیرش استفاده می‌شود.

#### بررسی‌های مجوز {#authorization-check}

بررسی مجوز برای منابع پارامتر معرفی شده است.
انتظار می‌رود کاربر به منابعی که با `paramKind` در
`ValidatingAdmissionPolicy` و با `paramRef` در `ValidatingAdmissionPolicyBinding` ارجاع داده می‌شوند، دسترسی `read` داشته باشد.

توجه داشته باشید که اگر تفکیک (resolve) یک منبع در `paramKind` از طریق restmapper ناموفق باشد،
دسترسی `read` به همهٔ منابع گروه‌ها لازم است.

#### فیلد `paramRef`

فیلد `paramRef` منبع پارامتری را که سیاست از آن استفاده می‌کند مشخص می‌کند. این فیلد شامل فیلدهای زیر است:

- فیلد **name**: نام منبع پارامتر.
- فیلد **namespace**: فضای نام منبع پارامتر.
- فیلد **selector**: یک انتخابگر برچسب برای تطبیق با چند منبع پارامتر.
- فیلد **parameterNotFoundAction**: (الزامی) رفتار را در زمانی که پارامترهای مشخص‌شده یافت نشوند کنترل می‌کند.

  - **مقادیر مجاز**:
    - مقدار **`Allow`**: اتصال، نبودِ پارامترهای مطابق را اعتبارسنجی موفق تلقی می‌کند.
    - مقدار **`Deny`**: نبودِ پارامترهای مطابق، تابع `failurePolicy` سیاست است.

باید یکی از `name` یا `selector` تنظیم شود، اما نه هر دو.

{{< note >}}
فیلد `parameterNotFoundAction` در `paramRef` **الزامی** است. این فیلد کنشی را مشخص می‌کند که وقتی هیچ پارامتری مطابق با `paramRef` یافت نشود انجام می‌شود. اگر این فیلد مشخص نشود، ممکن است اتصال سیاست نامعتبر تلقی و نادیده گرفته شود یا به رفتار غیرمنتظره‌ای منجر شود.

- مقدار **`Allow`**: اگر این فیلد روی `Allow` تنظیم شده باشد و هیچ پارامتری یافت نشود، اتصال نبودِ پارامترها را اعتبارسنجی موفق تلقی می‌کند و سیاست موفق در نظر گرفته می‌شود.
- مقدار **`Deny`**: اگر این فیلد روی `Deny` تنظیم شده باشد و هیچ پارامتری یافت نشود، اتصال `failurePolicy` سیاست را اعمال می‌کند. اگر `failurePolicy` برابر `Fail` باشد، درخواست رد می‌شود.

مطمئن شوید که `parameterNotFoundAction` را مطابق رفتار مطلوب در زمان نبودِ پارامترها تنظیم می‌کنید.
{{< /note >}}

#### مدیریت پارامترهای غایب با `parameterNotFoundAction`

وقتی از `paramRef` همراه با یک انتخابگر استفاده می‌کنید، ممکن است هیچ پارامتری با انتخابگر مطابقت نداشته باشد. فیلد `parameterNotFoundAction` تعیین می‌کند که اتصال در این وضعیت چگونه رفتار کند.

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

### سیاست شکست

فیلد `failurePolicy` تعیین می‌کند که پیکربندی‌های نادرست و عبارت‌های CEL که در سیاست پذیرش
به خطا ارزیابی می‌شوند چگونه مدیریت شوند. مقادیر مجاز `Ignore` یا `Fail` هستند.

- مقدار `Ignore` یعنی خطا در فراخوانی ValidatingAdmissionPolicy نادیده گرفته می‌شود و
  درخواست API اجازهٔ ادامه پیدا می‌کند.
- مقدار `Fail` یعنی خطا در فراخوانی ValidatingAdmissionPolicy باعث شکست پذیرش
  و رد شدن درخواست API می‌شود.

توجه داشته باشید که `failurePolicy` درون `ValidatingAdmissionPolicy` تعریف می‌شود:

{{% code_sample language="yaml" file="validatingadmissionpolicy/failure-policy-ignore.yaml" %}}

### عبارت اعتبارسنجی

فیلد `spec.validations[i].expression` عبارتی را مشخص می‌کند که CEL آن را ارزیابی می‌کند. برای آگاهی بیشتر، [مشخصات زبان CEL](https://github.com/google/cel-spec) را ببینید.
عبارت‌های CEL به محتوای درخواست و پاسخ پذیرش (Admission) دسترسی دارند. این محتوا در قالب متغیرهای CEL سازمان‌دهی شده است و چند متغیر مفید دیگر نیز در دسترس است:

- متغیر 'object': آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- متغیر 'oldObject': آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- متغیر 'request': ویژگی‌های [درخواست پذیرش](/docs/reference/config-api/apiserver-admission.v1/#admission-k8s-io-v1-AdmissionRequest).
- متغیر 'params': منبع پارامتری که اتصال سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. اگر `ParamKind` مشخص نشده باشد، مقدار آن null است.
- متغیر `namespaceObject`: فضای نامی که آبجکت ورودی به آن تعلق دارد، در قالب یک منبع کوبرنتیز. اگر آبجکت ورودی در سطح کلاستر باشد، مقدار آن null است.
- متغیر `authorizer`: یک مجوزدهندهٔ (Authorizer) CEL. با آن می‌توان بررسی‌های مجوزدهی را برای هویت اصلی (کاربر احرازهویت‌شده) درخواست انجام داد. برای جزئیات بیشتر، [AuthzSelectors](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors) و [Authz](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz) را در مستندات کتابخانهٔ CEL کوبرنتیز ببینید.
- متغیر `authorizer.requestResource`: میان‌بری برای بررسی مجوزدهی که با منبعِ درخواست (گروه، منبع، (زیرمنبع)، فضای نام، نام) پیکربندی شده است.
	
در عبارت‌های CEL، متغیرهایی مانند `object` و `oldObject` نوع‌دهی قوی دارند. می‌توانید به هر فیلدی در شِمای آبجکت، مانند `object.metadata.labels` و فیلدهای درون `spec`، دسترسی داشته باشید.

برای هر آبجکت کوبرنتیز، از جمله منابع سفارشی (Custom Resources) بدون شِما، CEL دسترسی به مجموعه‌ای حداقلی از ویژگی‌ها را تضمین می‌کند:
`apiVersion`، `kind`، `metadata.name` و `metadata.generateName`.

در آرایه‌هایی که نوع فهرست آن‌ها 'set' یا 'map' است، مقایسهٔ برابری ترتیب عناصر را نادیده می‌گیرد؛ یعنی [1, 2] == [2, 1].
الحاق آرایه‌هایی که x-kubernetes-list-type دارند از معنای همان نوع فهرست پیروی می‌کند:

- نوع 'set': عبارت `X + Y` اجتماع دو آرایه را می‌سازد؛ به این صورت که جایگاه همهٔ عناصر `X` در آرایه حفظ می‌شود و عناصرِ غیرمشترکِ `Y` با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.
- نوع 'map': عبارت `X + Y` دو آرایه را ادغام می‌کند؛ به این صورت که جایگاه همهٔ کلیدهای `X` در آرایه حفظ می‌شود، اما هرجا مجموعهٔ کلیدهای `X` و `Y` اشتراک داشته باشند، مقادیر `Y` جایگزین مقادیر قبلی می‌شوند. عناصری از `Y` که کلیدهای غیرمشترک دارند با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.

#### نمونه‌های عبارت اعتبارسنجی

| عبارت                                                                                   | هدف                                                                           |
|----------------------------------------------------------------------------------------------| ------------                                                                      |
| `object.minReplicas <= object.replicas && object.replicas <= object.maxReplicas`             | اعتبارسنجی اینکه سه فیلدِ تعیین‌کنندهٔ تعداد نسخه‌ها (replicas) ترتیب درستی دارند        |
| `'Available' in object.stateCounts`                                                          | اعتبارسنجی وجود ورودی‌ای با کلید 'Available' در یک نگاشت (map)                   |
| `(size(object.list1) == 0) != (size(object.list2) == 0)`                                     | اعتبارسنجی اینکه یکی از دو فهرست خالی نیست، اما هر دو هم‌زمان غیرخالی نیستند                         |
| <code>!('MY_KEY' in object.map1) &#124;&#124; object.map1['MY_KEY'].matches('^[a-zA-Z]*$')</code> | اعتبارسنجی مقدار یک کلید مشخص در نگاشت، در صورتی که آن کلید در نگاشت وجود داشته باشد        |
| `object.envars.filter(e, e.name == 'MY_ENV').all(e, e.value.matches('^[a-zA-Z]*$')`          | اعتبارسنجی فیلد 'value' در ورودی‌ای از یک listMap که فیلد کلیدی 'name' آن برابر 'MY_ENV' است  |
| `has(object.expired) && object.created + object.ttl < object.expired`                        | اعتبارسنجی اینکه تاریخ 'expired' پس از تاریخ 'create' به‌علاوهٔ مدت 'ttl' است       |
| `object.health.startsWith('ok')`                                                             | اعتبارسنجی اینکه فیلد رشته‌ای 'health' با پیشوند 'ok' آغاز می‌شود                              |
| `object.widgets.exists(w, w.key == 'x' && w.foo < 10)`                                       | اعتبارسنجی اینکه ویژگی 'foo' در عضوی از listMap با کلید 'x' کمتر از ۱۰ است |
| `type(object) == string ? object == '100%' : object == 1000`                                 | اعتبارسنجی یک فیلد از نوع int-or-string، هم در حالت عدد صحیح و هم در حالت رشته             |
| `object.metadata.name.startsWith(object.prefix)`                                             | اعتبارسنجی اینکه نام آبجکت با مقدار فیلدی دیگر به‌عنوان پیشوند آغاز می‌شود              |
| `object.set1.all(e, !(e in object.set2))`                                                    | اعتبارسنجی اینکه دو listSet هیچ عضو مشترکی ندارند                                           |
| `size(object.names) == size(object.details) && object.names.all(n, n in object.details)`     | اعتبارسنجی اینکه کلیدهای نگاشت 'details' همان اعضای listSet با نام 'names' هستند           |
| `size(object.clusters.filter(c, c.name == object.primary)) == 1`                             | اعتبارسنجی اینکه ویژگی 'primary' دقیقاً یک بار در listMap با نام 'clusters' آمده است           |

برای اطلاعات بیشتر دربارهٔ قواعد CEL، [ارزیابی پشتیبانی‌شده در CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#evaluation) را بخوانید.

فیلد `spec.validation[i].reason` توصیفی ماشین‌خوان از علت شکست این اعتبارسنجی ارائه می‌دهد.
اگر این نخستین اعتبارسنجیِ ناموفق در فهرست باشد، همین علت به‌همراه کد پاسخ HTTP متناظر با آن در پاسخ HTTP به کلاینت به کار می‌رود.
علت‌هایی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از: `Unauthorized`، `Forbidden`، `Invalid` و `RequestEntityTooLarge`.
اگر این فیلد تنظیم نشود، `StatusReasonInvalid` در پاسخ به کلاینت استفاده می‌شود.

### تطبیق درخواست‌ها: `matchConditions`

اگر به پالایش دقیق‌تر درخواست‌ها نیاز دارید، می‌توانید برای یک `ValidatingAdmissionPolicy` _شرط‌های تطبیق_ تعریف کنید. این شرط‌ها زمانی مفیدند که قواعد تطبیق، `objectSelectors` و `namespaceSelectors` هنوز پالایش مورد نظرتان را فراهم نمی‌کنند. شرط‌های تطبیق در واقع [عبارت‌های CEL](/docs/reference/using-api/cel/) هستند. برای اینکه منبع ارزیابی شود، همهٔ شرط‌های تطبیق باید به true ارزیابی شوند.

در ادامه نمونه‌ای آمده است که چند کاربرد مختلف شرط‌های تطبیق را نشان می‌دهد:

{{% code_sample file="access/validating-admission-policy-match-conditions.yaml" %}}

شرط‌های تطبیق به همان متغیرهای CEL دسترسی دارند که عبارت‌های اعتبارسنجی دارند، به‌جز `namespaceObject` و `variables`:

- متغیر `namespaceObject` برای شرط‌های تطبیق مقداردهی نمی‌شود و همیشه به null ارزیابی می‌شود. برای انتخاب درخواست‌ها بر اساس برچسب‌های فضای نام، از یک `namespaceSelector` در `matchConstraints` سیاست یا در `matchResources` اتصال استفاده کنید. برای بررسی سایر فیلدهای فضای نام، از یک عبارت اعتبارسنجی استفاده کنید که `namespaceObject` در آن در دسترس است.
- در شرط‌های تطبیق نمی‌توان به `variables` ارجاع داد، زیرا شرط‌های تطبیق پیش از بقیهٔ سیاست ارزیابی می‌شوند.

اگر هنگام ارزیابی یک شرط تطبیق خطایی رخ دهد، سیاست ارزیابی نمی‌شود. رد شدن یا نشدن درخواست به این صورت تعیین می‌شود:

1. اگر **هر یک** از شرط‌های تطبیق به `false` ارزیابی شده باشد (صرف‌نظر از سایر خطاها)، سرور API از آن سیاست صرف‌نظر می‌کند.
2. در غیر این صورت:
   - برای [`failurePolicy: Fail`](#failure-policy)، درخواست (بدون ارزیابی سیاست) رد می‌شود.
   - برای [`failurePolicy: Ignore`](#failure-policy)، درخواست ادامه می‌یابد، اما از سیاست صرف‌نظر می‌شود.

### حاشیه‌نویسی‌های ممیزی

با `auditAnnotations` می‌توان حاشیه‌نویسی‌های (annotation) ممیزی را در رویداد ممیزیِ درخواست API گنجاند.

برای نمونه، سیاست پذیرش زیر یک حاشیه‌نویسی ممیزی دارد:

{{% code_sample file="access/validating-admission-policy-audit-annotation.yaml" %}}

وقتی یک درخواست API با این سیاست پذیرش اعتبارسنجی شود، رویداد ممیزیِ حاصل به این شکل خواهد بود:

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

در این نمونه، حاشیه‌نویسی فقط زمانی گنجانده می‌شود که مقدار `spec.replicas` در Deployment بیشتر از ۵۰ باشد؛ در غیر این صورت، عبارت CEL به null ارزیابی می‌شود و حاشیه‌نویسی گنجانده نخواهد شد.

توجه کنید که کلیدهای حاشیه‌نویسی ممیزی با نام `ValidatingAdmissionPolicy` و یک `/` پیشوند می‌گیرند. اگر کنترل‌کنندهٔ پذیرش دیگری، مانند یک وب‌هوک پذیرش، دقیقاً از همان کلید حاشیه‌نویسی ممیزی استفاده کند، مقدارِ نخستین کنترل‌کنندهٔ پذیرشی که آن حاشیه‌نویسی را اضافه کرده است در رویداد ممیزی گنجانده می‌شود و همهٔ مقادیر دیگر نادیده گرفته می‌شوند.

### عبارت پیام

برای اینکه هنگام رد شدن درخواست توسط سیاست پیام گویاتری برگردانده شود، می‌توان با `spec.validations[i].messageExpression` و یک عبارت CEL پیامی ترکیبی ساخت. عبارت پیام، همانند عبارت اعتبارسنجی، به `object`، `oldObject`، `request`، `params` و `namespaceObject` دسترسی دارد. اما برخلاف اعتبارسنجی‌ها، عبارت پیام باید به یک رشته ارزیابی شود.

برای نمونه، اگر سیاست به یک پارامتر ارجاع دهد، برای آگاه‌کردن بهتر کاربر از علت رد شدن درخواست می‌توان اعتبارسنجی زیر را تعریف کرد:

{{% code_sample file="access/deployment-replicas-policy.yaml" %}}

پس از ایجاد یک آبجکت پارامتر که تعداد نسخه‌ها را به ۳ محدود می‌کند و برپاسازی اتصال، اگر بخواهیم یک Deployment با ۵ نسخه ایجاد کنیم، پیام زیر را دریافت خواهیم کرد.

```
$ kubectl create deploy --image=nginx nginx --replicas=5
error: failed to create deployment: deployments.apps "nginx" is forbidden: ValidatingAdmissionPolicy 'deploy-replica-policy.example.com' with binding 'demo-binding-test.example.com' denied request: object.spec.replicas must be no greater than 3
```

این پیام از پیام ایستایی مانند «too many replicas» گویاتر است.

اگر هر دو تعریف شده باشند، عبارت پیام بر پیام ایستای تعریف‌شده در `spec.validations[i].message` اولویت دارد.
با این حال، اگر ارزیابی عبارت پیام با شکست روبه‌رو شود، به‌جای آن از پیام ایستا استفاده می‌شود.
همچنین اگر عبارت پیام به رشته‌ای چندخطی ارزیابی شود، نتیجهٔ ارزیابی کنار گذاشته می‌شود و در صورت وجود، پیام ایستا به کار می‌رود.
توجه کنید که پیام ایستا نیز از نظر چندخطی بودن اعتبارسنجی می‌شود.

### بررسی نوع

هنگام ایجاد یا به‌روزرسانی تعریف یک سیاست، فرایند اعتبارسنجی عبارت‌های درون آن را تجزیه می‌کند، هر خطای نحوی را گزارش می‌دهد و در صورت یافتن خطا، تعریف را رد می‌کند.
پس از آن، متغیرهای ارجاع‌شده در برابر نوع‌های تطبیق‌یافته در `spec.matchConstraints` از نظر خطاهای نوع، از جمله فیلدهای ناموجود و ابهام در نوع، بررسی می‌شوند.
نتیجهٔ بررسی نوع را می‌توان از `status.typeChecking` دریافت کرد.
وجود `status.typeChecking` نشان می‌دهد که بررسی نوع کامل شده است، و خالی بودن `status.typeChecking` به این معناست که هیچ خطایی شناسایی نشده است.

برای نمونه، تعریف سیاست زیر را در نظر بگیرید:

{{< code_sample language="yaml" file="validatingadmissionpolicy/typechecking.yaml" >}}

وضعیت آن اطلاعات زیر را نشان می‌دهد:

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

اگر چند منبع در `spec.matchConstraints` تطبیق داده شوند، همهٔ منابع تطبیق‌یافته بررسی می‌شوند.
برای نمونه، تعریف سیاست زیر

{{% code_sample language="yaml" file="validatingadmissionpolicy/typechecking-multiple-match.yaml" %}}


چند نوع خواهد داشت و نتیجهٔ بررسی هر نوع در پیام هشدار آمده است.

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

- تطبیق با نویسهٔ عام (wildcard) پشتیبانی نمی‌شود. اگر `spec.matchConstraints.resourceRules` در هر یک از `apiGroups`، `apiVersions` یا `resources` مقدار `"*"` داشته باشد، نوع‌هایی که با `"*"` تطبیق می‌یابند بررسی نمی‌شوند.
- تعداد نوع‌های تطبیق‌یافته به ۱۰ محدود است. این محدودیت جلوی آن را می‌گیرد که سیاستی با تعیین دستیِ تعداد بسیار زیادی نوع، منابع محاسباتی را بیش از حد مصرف کند. ترکیب‌ها به ترتیب صعودی گروه، سپس نسخه و سپس منبع مرتب می‌شوند و ترکیب یازدهم و پس از آن نادیده گرفته می‌شوند.
- بررسی نوع به هیچ وجه بر رفتار سیاست اثر نمی‌گذارد. حتی اگر بررسی نوع خطاهایی را شناسایی کند، ارزیابی سیاست ادامه می‌یابد. اگر در حین ارزیابی خطایی رخ دهد، سیاست شکست (failure policy) نتیجهٔ آن را تعیین می‌کند.
- بررسی نوع روی CRDها، از جمله نوع‌های CRD تطبیق‌یافته و ارجاع paramKind، اعمال نمی‌شود. پشتیبانی از CRDها در نسخه‌های آینده اضافه خواهد شد.

### ترکیب متغیرها

اگر عبارتی بیش از حد پیچیده شود، یا بخشی از آن قابل استفادهٔ دوباره باشد و ارزیابی آن هزینهٔ محاسباتی زیادی داشته باشد، می‌توانید بخشی از عبارت‌ها را در قالب متغیر جدا کنید. متغیر عبارتی نام‌دار است که بعدها می‌توان در عبارت‌های دیگر از طریق `variables` به آن ارجاع داد.

```yaml
spec:
  variables:
    - name: foo
      expression: "'foo' in object.spec.metadata.labels ? object.spec.metadata.labels['foo'] : 'default'"
  validations:
    - expression: variables.foo == 'bar'
```

هر متغیر به‌صورت تنبل (lazy) و در نخستین ارجاع به آن ارزیابی می‌شود. هر خطایی که در حین این ارزیابی رخ دهد، هنگام ارزیابی عبارتِ ارجاع‌دهنده گزارش می‌شود. هم نتیجه و هم خطای احتمالی به خاطر سپرده می‌شوند و فقط یک بار در هزینهٔ زمان اجرا محاسبه می‌شوند.

ترتیب متغیرها اهمیت دارد، زیرا هر متغیر فقط می‌تواند به متغیرهایی ارجاع دهد که پیش از آن تعریف شده‌اند.
این ترتیب از ارجاع‌های چرخه‌ای جلوگیری می‌کند.

نمونهٔ پیچیده‌تر زیر الزام می‌کند که نام مخزن‌های ایمیج با محیطی که در فضای نام آن‌ها تعریف شده است مطابقت داشته باشد.

{{< code_sample file="access/image-matches-namespace-environment.policy.yaml" >}}

اگر این سیاست به فضای نام `default` متصل شده باشد که برچسب `environment: prod` دارد، تلاش زیر برای ایجاد یک Deployment رد خواهد شد.
```shell
kubectl create deploy --image=dev.example.com/nginx invalid
```
پیام خطا مشابه زیر است.
```console
error: failed to create deployment: deployments.apps "invalid" is forbidden: ValidatingAdmissionPolicy 'image-matches-namespace-environment.policy.example.com' with binding 'demo-binding-test.example.com' denied request: only prod images are allowed in namespace default
```

## انواع API معاف از اعتبارسنجی پذیرش

برخی انواع API از بررسی‌های اعتبارسنجی در زمان پذیرش معاف‌اند. برای نمونه، نمی‌توانید یک ValidatingAdmissionPolicy ایجاد کنید که جلوی تغییر ValidatingAdmissionPolicyBindingها را بگیرد.

برای جلوگیری از وابستگی‌های چرخه‌ای، انواع پیکربندی پذیرش زیر از سیاست‌هایی که از طریق REST API ایجاد می‌شوند معاف‌اند:

* [ValidatingAdmissionPolicies]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-v1/" >}})
* [ValidatingAdmissionPolicyBindings]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1/" >}})
* MutatingAdmissionPolicies
* MutatingAdmissionPolicyBindings

{{< note >}}
اگر یک ValidatingAdmissionPolicy از طریق [کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/) پیکربندی شود، می‌تواند انواع پیکربندی پذیرشِ فهرست‌شده در بالا را رهگیری کند. در این حالت، محدودیت‌هایی که معمولاً بر سیاست‌های ایجادشده از طریق REST API اعمال می‌شوند دور زده می‌شوند و می‌توانید حتی پیکربندی پذیرش و منابع حساس از نظر امنیتی را نیز اعتبارسنجی کنید. برخلاف REST API، یک سیاست پذیرشِ نادرستِ مبتنی بر مانیفست که این منابع را رهگیری می‌کند وضعیت غیرقابل بازیابی ایجاد نمی‌کند، زیرا روی دیسک تعریف شده است، نه از طریق API.
{{< /note >}}

افزون بر این، انواع API احرازهویت و مجوزدهیِ ذخیره‌نشده (مجازی) زیر از همهٔ سیاست‌های پذیرش، از جمله سیاست‌های مبتنی بر مانیفست، معاف‌اند؛ زیرا رهگیری آن‌ها ممکن است کلاستر را از مسیر احرازهویت و مجوزدهیِ خودش محروم کند:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

از کوبرنتیز نسخهٔ v1.37 به بعد، [وب‌هوک‌های پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources) نیز به‌طور پیش‌فرض این منابع مجازی را مستثنا می‌کنند.

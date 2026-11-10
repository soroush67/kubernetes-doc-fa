---
title: اعتبارسنجی اعلانی API
reviewers:
- aaron-prindle
- yongruilin
- jpbetz
- thockin
content_type: concept
weight: 20
---

<!-- overview -->

{{< feature-state feature_gate_name="DeclarativeValidation" >}}

کوبرنتیز {{< skew currentVersion >}} برای مجموعه‌ای رو به گسترش از APIها از
_اعتبارسنجی اعلانی_ (declarative validation) استفاده می‌کند. در این روش، نویسندگان API به‌جای نوشتن دستی کد Go (`validation.go`)، قواعد اعتبارسنجی را به‌صورت تگ‌های توضیحی روی تعریف‌های نوع (`types.go`) اعلام می‌کنند؛ برای مثال `+k8s:minimum=0`. سپس یک مولد کد به نام `validation-gen` این تگ‌ها را به کد اعتبارسنجی تبدیل می‌کند.

این موضوع عمدتاً به مشارکت‌کنندگان کوبرنتیز و نویسندگان
[سرورهای API افزونه](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
مربوط است، اما مدیران کلاستر نیز باید بدانند که این سازوکار در دوره‌ای که اعتبارسنجی‌های دست‌نویس موجود در حال مهاجرت هستند، چگونه رفتار می‌کند.

<!-- body -->

## چرخه‌ی حیات اعتبارسنجی {#lifecycle}

برای فیلدهای جدید API، تگ را مستقیماً به کار ببرید؛ مانند `+k8s:minimum=1`. این تگ‌ها همیشه اعمال می‌شوند.

مهاجرت دادن یک اعتبارسنجی دست‌نویسِ *موجود* پرخطرتر است، زیرا کد تولیدشده باید دقیقاً مانند کدی رفتار کند که جایگزین آن می‌شود. در این مهاجرت‌ها، تگ درون یک _پیشوند چرخه‌ی حیات_ (`+k8s:alpha` یا `+k8s:beta`) قرار می‌گیرد. این پیشوند تعیین می‌کند که آیا نتیجه‌ی اعتبارسنجی اعلانی، نتیجه‌ی مرجع (authoritative) است یا نه.

{{< table caption="Behavior of a declarative validation tag by lifecycle prefix" >}}

| شکل تگ | رفتار |
| --- | --- |
| `+k8s:minimum=1` (بدون پیشوند) | **اعمال می‌شود.** نتیجه‌ی اعتبارسنجی اعلانی مرجع است. |
| `+k8s:beta(since:"1.37")=+k8s:minimum=1` | وقتی feature gate `DeclarativeValidationBeta` فعال باشد (حالت پیش‌فرض) **اعمال می‌شود**؛ در غیر این صورت در حالت سایه اجرا می‌شود. |
| `+k8s:alpha(since:"1.36")=+k8s:minimum=1` | **همیشه در حالت سایه اجرا می‌شود.** اعتبارسنجی دست‌نویس همچنان مرجع باقی می‌ماند. |

{{< /table >}}

در _حالت سایه_ (shadow mode)، اعتبارسنجی اعلانی همچنان اجرا می‌شود، اما سرور API خطاهای آن را بازنمی‌گرداند. سرور این خطاها را با خطاهای اعتبارسنجی دست‌نویس مقایسه می‌کند و هر تفاوتی را در لاگ ثبت و شمارش می‌کند. به این ترتیب، می‌توان یک قاعده‌ی مهاجرت‌داده‌شده را پیش از آنکه شروع به رد کردن درخواست‌ها کند، روی یک کلاستر واقعی ارزیابی کرد.

## تنظیمات feature gate

* فعال بودن [`DeclarativeValidation`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidation)
  باعث می‌شود {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
  برای قواعد `+k8s:alpha` و `+k8s:beta`، نتایج اعتبارسنجی اعلانی و دست‌نویس را با هم مقایسه کند و ناهمخوانی‌ها را گزارش دهد. اعتبارسنجی اعلانی در هر حال اجرا می‌شود؛ این گیت فقط گزارش‌دهی را کنترل می‌کند.

* کلید ایمنی سراسری برای قواعد `+k8s:beta`، گیت
  [`DeclarativeValidationBeta`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidationBeta)
  است. اگر این گیت فعال باشد، این قواعد اعمال می‌شوند و اگر غیرفعال باشد، به حالت سایه بازمی‌گردند.

* گیت [`DeclarativeValidationTakeover`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidationTakeover)
  با `DeclarativeValidationBeta` جایگزین شده است و دیگر به آن ترتیب اثر داده نمی‌شود. با این حال، تنظیم آن همچنان پذیرفته می‌شود.

{{< alert color="info" title="Note" >}}
هیچ feature gateای بر تگ‌های بدون پیشوند اثر ندارد. سرور API همیشه این تگ‌ها را اعمال می‌کند، زیرا همتای دست‌نویس آن‌ها پیش‌تر حذف شده است.
{{< /alert >}}

برای آشنایی با نحوه‌ی تنظیم این گیت‌ها، به
[feature gateها](/docs/reference/command-line-tools-reference/feature-gates/)
مراجعه کنید.

## پایش اعتبارسنجی اعلانی {#metrics}

سرور API متریک‌های زیر را ارائه می‌کند:

{{< table caption="Metrics for declarative validation" >}}

| متریک | توضیح |
| --- | --- |
| `declarative_validation_mismatch_total` | تعداد دفعاتی که نتایج اعتبارسنجی اعلانی با نتایج اعتبارسنجی دست‌نویس متفاوت بوده است. |
| `declarative_validation_parity_discrepancies_total` | همان ناهمخوانی‌ها، به همراه برچسب `validation_identifier` که گروه، نسخه، kind، زیرمنبع (subresource) و عملیات را ثبت می‌کند. |
| `declarative_validation_panic_total` | تعداد دفعاتی که اعتبارسنجی اعلانی دچار panic شده است. |
| `declarative_validation_panics_total` | همان panicها، به همراه برچسب `validation_identifier`. |

{{< /table >}}

ناهمخوانی‌ها در لاگ نیز ثبت می‌شوند. برای یک قاعده‌ی اعمال‌شده (`+k8s:beta`)، ورودی لاگ پیشنهاد می‌کند که `DeclarativeValidationBeta` را غیرفعال کنید تا داده‌های ذخیره‌شده در etcd با نسخه‌های قبلی کوبرنتیز سازگار بمانند.

## غیرفعال کردن DeclarativeValidationBeta {#opt-out}

اگر با هر یک از موارد زیر روبه‌رو شدید، تنظیم `DeclarativeValidationBeta=false` را در نظر بگیرید:

* **رفتار غیرمنتظره در اعتبارسنجی:** درخواست‌هایی که باید معتبر باشند رد می‌شوند، یا آبجکت‌هایی که پیش‌تر رد می‌شدند اکنون پذیرفته می‌شوند.

* **افت کارایی:** افزایش تأخیر (برای مثال در
  `apiserver_request_duration_seconds`) که با این قابلیت همبستگی دارد.

* **نرخ بالای ناهمخوانی:** افزایش‌های مکرر
  `declarative_validation_mismatch_total` که بارهای کاری شما را تحت تأثیر قرار می‌دهد.

برای بازگرداندن قواعد `+k8s:beta` به حالت سایه، فلگ
`--feature-gates=DeclarativeValidationBeta=false` را ارسال کنید.

## ملاحظات کاهش نسخه (downgrade) و بازگشت (rollback)

غیرفعال کردن این گیت یک سازوکار ایمنی است، اما به یک حالت مرزی نامحتمل توجه کنید: اگر یک باگ باعث شده باشد که اعتبارسنجی اعلانی آبجکتی نامعتبر را ذخیره کند، با غیرفعال کردن گیت، اعتبارسنجی دست‌نویسِ صحیح دوباره مرجع می‌شود و ممکن است جلوی به‌روزرسانی‌های بعدی آن آبجکت را بگیرد. رفع این مشکل ممکن است به ویرایش مستقیم آبجکت ذخیره‌شده نیاز داشته باشد.

## تگ‌های اعتبارسنجی اعلانی {#declarative-validation-tag-reference}

### نحوه‌ی خواندن این مرجع {#how-to-read}

هر تگ یک **سطح پایداری** (آلفا، بتا یا پایدار) دارد که میزان بلوغ *خود تگ* را توصیف می‌کند. این مفهوم از [پیشوندهای چرخه‌ی حیات](#lifecycle) `+k8s:alpha` و `+k8s:beta` جداست؛ این پیشوندها میزان بلوغ یک *کاربرد* مشخص از یک تگ را توصیف می‌کنند.

لینتر مولد کد بر اساس سطح پایداری تعیین می‌کند که هر تگ در کجا مجاز است:

* در یک بسته‌ی GA (برای مثال `v1`)، تگ بدون پیشوند باید پایدار باشد.

* در یک بسته‌ی `beta`، تگ‌های بتای بدون پیشوند نیز مجازند.

* در یک بسته‌ی `alpha`، تگ‌های آلفا و بتای بدون پیشوند نیز مجازند.

* درون `+k8s:alpha=...` تگ‌های آلفا مجازند و درون `+k8s:beta=...` تگ‌های بتا.

* درون `+k8s:ifEnabled(...)` یا `+k8s:ifDisabled(...)`، تگ‌های بتا حتی در یک بسته‌ی GA نیز مجازند، زیرا اعتبارسنجی از قبل به یک گزینه مشروط شده است.

برای هر مورد، **دامنه‌هایی** (scopes) که تگ می‌تواند در آن‌ها به کار رود نیز فهرست شده است: فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map یا مقادیر ثابت.

{{< alert color="info" title="Note" >}}
مولد کد تگ‌هایی را نیز ثبت می‌کند که فقط برای آزمودن خود آن وجود دارند
(`+k8s:validateTrue`، `+k8s:validateFalse`، `+k8s:validateError`،
`+k8s:validateTrueAlpha`، `+k8s:validateTrueBeta`). از این تگ‌ها در تعریف‌های API استفاده نکنید. برای دریافت فهرست مرجعِ هر نسخه، دستور
`validation-gen --docs` را از `k8s.io/code-generator` اجرا کنید.
{{< /alert >}}

### فهرست تگ‌ها {#catalog}

{{< table caption="Declarative validation tags" >}}

| تگ | توضیح | سطح پایداری |
| --- | --- | --- |
| [`+k8s:alpha`](#tag-alpha) | یک تگ اعتبارسنجی را در حالت سایه قرار می‌دهد (فقط ثبت متریک). | بتا |
| [`+k8s:beta`](#tag-beta) | یک تگ اعتبارسنجی را در حالت اعمال قرار می‌دهد (با `DeclarativeValidationBeta` قابل غیرفعال‌سازی است). | بتا |
| [`+k8s:customUnique`](#tag-customUnique) | نشان می‌دهد که اعتبارسنجی دست‌نویس، یکتایی عناصر یک لیست را بررسی می‌کند. | پایدار |
| [`+k8s:customValidation`](#tag-customValidation) | یک تابع اعتبارسنجی دست‌نویس را از کد پیمایش تولیدشده فراخوانی می‌کند. | پایدار |
| [`+k8s:dependentForbidden`](#tag-dependentForbidden) | نشان می‌دهد که وقتی این فیلد مقدار دارد، یک فیلد هم‌سطحِ نام‌برده نباید مقدار داشته باشد. | آلفا |
| [`+k8s:dependentRequired`](#tag-dependentRequired) | نشان می‌دهد که وقتی این فیلد مقدار دارد، یک فیلد هم‌سطحِ نام‌برده نیز باید مقدار داشته باشد. | آلفا |
| [`+k8s:eachKey`](#tag-eachKey) | یک اعتبارسنجی برای هر کلید یک map اعلام می‌کند. | پایدار |
| [`+k8s:eachVal`](#tag-eachVal) | یک اعتبارسنجی برای هر مقدار یک map یا لیست اعلام می‌کند. | پایدار |
| [`+k8s:enum`](#tag-enum) | نشان می‌دهد که یک نوع رشته‌ای، enum است. | پایدار |
| [`+k8s:enumExclude`](#tag-enumExclude) | یک ثابت را از مقادیر enum نوع آن مستثنا می‌کند. | آلفا |
| [`+k8s:forbidden`](#tag-forbidden) | نشان می‌دهد که یک فیلد نباید مشخص شود. | بتا |
| [`+k8s:format`](#tag-format) | نشان می‌دهد که یک فیلد رشته‌ای قالب مشخصی دارد. | پایدار |
| [`+k8s:ifDisabled`](#tag-ifDisabled) | اعتبارسنجی‌ای اعلام می‌کند که فقط وقتی یک گزینه غیرفعال است اعمال می‌شود. | پایدار |
| [`+k8s:ifEnabled`](#tag-ifEnabled) | اعتبارسنجی‌ای اعلام می‌کند که فقط وقتی یک گزینه فعال است اعمال می‌شود. | پایدار |
| [`+k8s:ifMode`](#tag-ifMode) | اعتبارسنجی‌ای اعلام می‌کند که فقط برای مقدار مشخصی از یک متمایزکننده‌ی حالت (mode discriminator) اعمال می‌شود. | پایدار |
| [`+k8s:immutable`](#tag-immutable) | نشان می‌دهد که یک فیلد نباید به‌روزرسانی شود. | پایدار |
| [`+k8s:isSubresource`](#tag-isSubresource) | مشخص می‌کند که اعتبارسنجی‌های یک بسته فقط به یک زیرمنبع خاص اعمال می‌شوند. | پایدار |
| [`+k8s:item`](#tag-item) | یک اعتبارسنجی برای یک آیتم از sliceای اعلام می‌کند که به‌صورت `+k8s:listType=map` تعریف شده است. | پایدار |
| [`+k8s:listMapKey`](#tag-listMapKey) | یک زیرفیلد نام‌دار از نوع مقدار لیست را بخشی از کلید list-map اعلام می‌کند. | پایدار |
| [`+k8s:listType`](#tag-listType) | نوع معنایی یک فیلد لیستی را اعلام می‌کند. | پایدار |
| [`+k8s:maxBytes`](#tag-maxBytes) | نشان می‌دهد که طول یک فیلد رشته‌ای بر حسب بایت محدودیت دارد. | پایدار |
| [`+k8s:maxItems`](#tag-maxItems) | نشان می‌دهد که اندازه‌ی یک لیست محدودیت دارد. | پایدار |
| [`+k8s:maxLength`](#tag-maxLength) | نشان می‌دهد که طول یک فیلد رشته‌ای بر حسب کاراکتر محدودیت دارد. | پایدار |
| [`+k8s:maxProperties`](#tag-maxProperties) | نشان می‌دهد که تعداد ورودی‌های یک map محدودیت دارد. | پایدار |
| [`+k8s:maximum`](#tag-maximum) | نشان می‌دهد که یک فیلد عددی مقدار بیشینه دارد. | پایدار |
| [`+k8s:minItems`](#tag-minItems) | نشان می‌دهد که یک لیست اندازه‌ی کمینه دارد. | پایدار |
| [`+k8s:minLength`](#tag-minLength) | نشان می‌دهد که یک فیلد رشته‌ای طول کمینه بر حسب کاراکتر دارد. | پایدار |
| [`+k8s:minProperties`](#tag-minProperties) | نشان می‌دهد که یک map تعداد کمینه‌ای از ورودی‌ها دارد. | پایدار |
| [`+k8s:minimum`](#tag-minimum) | نشان می‌دهد که یک فیلد عددی مقدار کمینه دارد. | پایدار |
| [`+k8s:modeDiscriminator`](#tag-modeDiscriminator) | نشان می‌دهد که این فیلد متمایزکننده‌ای برای اعتبارسنجی مبتنی بر وضعیت است. | پایدار |
| [`+k8s:monotonic`](#tag-monotonic) | تضمین می‌کند که مقدار یک فیلد در به‌روزرسانی هرگز کاهش نیابد. | آلفا |
| [`+k8s:neq`](#tag-neq) | بررسی می‌کند که مقدار فیلد با یک مقدار غیرمجازِ مشخص برابر نباشد. | آلفا |
| [`+k8s:opaqueType`](#tag-opaqueType) | نشان می‌دهد که مولد کد هر اعتبارسنجیِ اعلام‌شده روی نوع ارجاع‌شده را نادیده می‌گیرد. | پایدار |
| [`+k8s:optional`](#tag-optional) | نشان می‌دهد که مشخص کردن یک فیلد برای کلاینت‌ها اختیاری است. | پایدار |
| [`+k8s:required`](#tag-required) | نشان می‌دهد که کلاینت‌ها باید یک فیلد را مشخص کنند. | پایدار |
| [`+k8s:subfield`](#tag-subfield) | یک اعتبارسنجی برای یک زیرفیلد از یک struct اعلام می‌کند. | پایدار |
| [`+k8s:supportsSubresource`](#tag-supportsSubresource) | یک زیرمنبع پشتیبانی‌شده برای نوع‌های درون یک بسته اعلام می‌کند. | پایدار |
| [`+k8s:unionDiscriminator`](#tag-unionDiscriminator) | نشان می‌دهد که این فیلد متمایزکننده‌ی یک union است. | بتا |
| [`+k8s:unionMember`](#tag-unionMember) | نشان می‌دهد که این فیلد عضوی از یک گروه union است. | پایدار |
| [`+k8s:unique`](#tag-unique) | اعلام می‌کند که عناصر یک فیلد لیستی یکتا هستند. | پایدار |
| [`+k8s:update`](#tag-update) | گذارهای مجاز در به‌روزرسانی یک فیلد را محدود می‌کند. | پایدار |
| [`+k8s:zeroOrOneOfMember`](#tag-zeroOrOneOfMember) | نشان می‌دهد که این فیلد عضوی از یک گروه «صفر یا یکی از» (zero-or-one-of) است. | پایدار |

{{< /table >}}

## مرجع تگ‌ها

### `+k8s:alpha` {#tag-alpha}

**توضیح:**

یک قاعده‌ی اعتبارسنجی را در _حالت سایه_ قرار می‌دهد که نخستین مرحله از
[چرخه‌ی حیات اعتبارسنجی](#lifecycle) است. از این تگ فقط هنگام مهاجرت اعتبارسنجی دست‌نویس موجود استفاده کنید، نه روی فیلدهای جدید.

اعتبارسنجی دست‌نویس همچنان مرجع می‌ماند و قاعده‌ی اعلانی در کنار آن اجرا می‌شود؛ ناهمخوانی‌ها و panicها نیز به‌صورت [متریک](#metrics) ثبت می‌شوند. به این ترتیب، پیش از ارتقای قاعده به بتا، تأیید می‌شود که این دو رفتاری یکسان دارند.

سرور API، صرف‌نظر از وضعیت feature gateها، هرگز قواعد `+k8s:alpha` را اعمال نمی‌کند.

**سطح پایداری:** بتا

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**آرگومان‌ها:**

* آرگومان `since` (رشته، اختیاری): نسخه‌ای از کوبرنتیز که اعتبارسنجی برای نخستین بار در آن در حالت سایه قرار گرفت.

**محتوا (payload):**

* مقدار `<validation-tag>` (الزامی): تگ اعتبارسنجی اعلانی‌ای که باید در حالت سایه اجرا شود.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:alpha(since:"1.36")=+k8s:minimum=1
    MyField int `json:"myField"`
}
```

### `+k8s:beta` {#tag-beta}

**توضیح:**

یک قاعده‌ی اعتبارسنجیِ مهاجرت‌داده‌شده را در _حالت اعمال_ قرار می‌دهد که دومین مرحله از
[چرخه‌ی حیات اعتبارسنجی](#lifecycle) است. از این تگ فقط هنگام مهاجرت اعتبارسنجی دست‌نویس موجود استفاده کنید، نه روی فیلدهای جدید.

وقتی `DeclarativeValidationBeta` فعال باشد (حالت پیش‌فرض)، این قاعده مرجع است و سرور API خطاهای دست‌نویسی را که این قاعده پوشش می‌دهد کنار می‌گذارد. با غیرفعال کردن این گیت، قاعده به حالت سایه بازمی‌گردد.

**سطح پایداری:** بتا

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**آرگومان‌ها:**

* آرگومان `since` (رشته، اختیاری): نسخه‌ای از کوبرنتیز که اعتبارسنجی در آن به بتا ارتقا یافت.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگ اعتبارسنجی اعلانی‌ای که باید اعمال شود.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:beta(since:"1.37")=+k8s:minimum=1
    MyField int `json:"myField"`
}
```

### `+k8s:customUnique` {#tag-customUnique}

**توضیح:**

نشان می‌دهد که یک اعتبارسنجی سفارشی و دست‌نویس، بررسی یکتایی این لیست را انجام می‌دهد. این تگ تولید اعتبارسنجی یکتایی را برای این لیست غیرفعال می‌کند؛ اعتبارسنجی‌ای که در غیر این صورت `+k8s:listType=set`، `+k8s:listType=map` و [`+k8s:unique`](#tag-unique) به‌طور ضمنی آن را ایجاب می‌کنند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:listType=map
    // +k8s:listMapKey=key
    // +k8s:customUnique
    MyList []Item `json:"myList"`
}
```

در این مثال، مولد کد ثبت می‌کند که `MyList` یک list-map است، اما بررسی یکتایی برای آن تولید نمی‌کند؛ مسئولیت این بررسی بر عهده‌ی کد دست‌نویس است.

### `+k8s:customValidation` {#tag-customValidation}

**توضیح:**

یک تابع اعتبارسنجی دست‌نویس را از کد پیمایش تولیدشده فراخوانی می‌کند. از این تگ برای منطقی استفاده کنید که با سایر تگ‌ها قابل بیان نیست.

این تابع باید در بسته‌ی تولیدشده و با امضای زیر تعریف شود:

```go
func(ctx context.Context, op operation.Operation, fldPath *field.Path, value, oldValue <ValueType>) field.ErrorList
```

نوع `<ValueType>` همان نوع مقدار است که nil‌پذیر شده است: یک اشاره‌گر مانند `*string`، یا اگر نوع از قبل nil‌پذیر باشد (slice، map، اشاره‌گر)، خود آن نوع. هر بسته‌ی تولیدشده به تعریف مخصوص خود نیاز دارد، زیرا هر نسخه از کد تولیدشده تابعی را فراخوانی می‌کند که در کنار خودش قرار دارد.

در نام تابع، `<Type>` و `<Field>` شناسه‌های Go هستند (`Replicas`، نه
`replicas`):

* دامنه‌ی فیلد: تابع `ValidateCustom_<Type>_<Field>` یک فیلد را اعتبارسنجی می‌کند. در به‌روزرسانی، اگر آن فیلد تغییر نکرده باشد، این تابع اجرا نمی‌شود.

* دامنه‌ی نوع: تابع `ValidateCustom_<Type>` بررسی‌هایی را میان چند فیلد انجام می‌دهد. این تابع در به‌روزرسانی *رد نمی‌شود*؛ بنابراین یک بررسی پرهزینه باید در صورت برابر بودن `value` و `oldValue` زودتر بازگردد.

برای بررسی‌های مربوط به هر عنصر، نوع عنصر را تگ‌گذاری کنید، یا از دامنه‌ی فیلد استفاده کنید و درون تابع روی عناصر حلقه بزنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع

**مثال کاربرد:**

```go
// +k8s:customValidation
type MyStruct struct {
    // +k8s:customValidation
    StringField string `json:"stringField"`

    // Both validations run on this field.
    // +k8s:maxLength=3
    // +k8s:customValidation
    MaxLengthField string `json:"maxLengthField"`
}
```

### `+k8s:dependentForbidden` {#tag-dependentForbidden}

**توضیح:**

نشان می‌دهد که وقتی این فیلد مقدار دارد، فیلد هم‌سطحِ (sibling) نام‌برده نباید مقدار داشته باشد. یک فیلد زمانی «مقداردار» به شمار می‌آید که اشاره‌گری غیر nil، یک slice یا map غیرخالی، یا یک نوع داخلی با مقدار غیرصفر باشد. وابستگی‌ها یک‌طرفه‌اند. برای ممنوع کردن چند فیلد هم‌سطح، تگ را تکرار کنید.

**سطح پایداری:** آلفا

**دامنه‌ها:** فیلدهای struct

**آرگومان‌ها:**

* آرگومان `<sibling-field-json-name>` (رشته، الزامی): نام JSON فیلد هم‌سطح.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:optional
    // +k8s:dependentForbidden("dependentA")
    // +k8s:dependentForbidden("dependentB")
    Trigger *string `json:"trigger"`

    // +k8s:optional
    DependentA *string `json:"dependentA"`

    // +k8s:optional
    DependentB *string `json:"dependentB"`
}
```

در این مثال، اگر `trigger` مقدار داشته باشد، هیچ‌یک از `dependentA` و `dependentB` نباید مقدار داشته باشند.

### `+k8s:dependentRequired` {#tag-dependentRequired}

**توضیح:**

نشان می‌دهد که وقتی این فیلد مقدار دارد، فیلد هم‌سطحِ نام‌برده نیز باید مقدار داشته باشد. یک فیلد زمانی «مقداردار» به شمار می‌آید که اشاره‌گری غیر nil، یک slice یا map غیرخالی، یا یک نوع داخلی با مقدار غیرصفر باشد. وابستگی‌ها یک‌طرفه‌اند. برای الزامی کردن چند فیلد هم‌سطح، تگ را تکرار کنید.

**سطح پایداری:** آلفا

**دامنه‌ها:** فیلدهای struct

**آرگومان‌ها:**

* آرگومان `<sibling-field-json-name>` (رشته، الزامی): نام JSON فیلد هم‌سطح.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:optional
    // +k8s:dependentRequired("dependent")
    Trigger *string `json:"trigger"`

    // +k8s:optional
    Dependent *string `json:"dependent"`
}
```

در این مثال، اگر `trigger` مقدار داشته باشد، `dependent` نیز باید مقدار داشته باشد. مقدار دادن به `dependent` به‌تنهایی مجاز است.

### `+k8s:eachKey` {#tag-eachKey}

**توضیح:**

یک اعتبارسنجی برای هر کلید یک map اعلام می‌کند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگی که باید برای هر کلید ارزیابی شود.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:eachKey=+k8s:minimum=1
    MyMap map[int]string `json:"myMap"`
}
```

### `+k8s:eachVal` {#tag-eachVal}

**توضیح:**

یک اعتبارسنجی برای هر مقدار یک map یا لیست اعلام می‌کند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگی که باید برای هر مقدار ارزیابی شود.

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:eachVal=+k8s:minimum=1
    MyMap map[string]int `json:"myMap"`

    // +k8s:eachVal=+k8s:maxLength=10
    MyList []string `json:"myList"`
}
```

### `+k8s:enum` {#tag-enum}

**توضیح:**

نشان می‌دهد که یک نوع رشته‌ای، enum است. همه‌ی مقادیر ثابت این نوع جزو مقادیر enum هستند، مگر اینکه آن‌ها را با
[`+k8s:enumExclude`](#tag-enumExclude) مستثنا کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** تعریف‌های نوع

**مثال کاربرد:**

ابتدا یک نوع رشته‌ای جدید و چند ثابت از آن نوع تعریف کنید:

```go
// +k8s:enum
type MyEnum string

const (
    MyEnumA MyEnum = "A"
    MyEnumB MyEnum = "B"
)
```

سپس از این نوع در یک struct دیگر استفاده کنید:

```go
type MyStruct struct {
    MyField MyEnum `json:"myField"`
}
```

منطق اعتبارسنجی تضمین می‌کند که مقدار `MyField` یکی از مقادیر تعریف‌شده‌ی enum
(`"A"` یا `"B"`) باشد.

### `+k8s:enumExclude` {#tag-enumExclude}

**توضیح:**

نشان می‌دهد که یک مقدار ثابت جزو enum نیست، حتی اگر نوع آن ثابت تگ `+k8s:enum` داشته باشد. می‌توانید با قرار دادن این تگ درون [`+k8s:ifEnabled`](#tag-ifEnabled) یا
[`+k8s:ifDisabled`](#tag-ifDisabled)، این استثنا را شرطی کنید. اگر از چند تگ شرطی استفاده کنید، مولد کد مقدار را در صورتی مستثنا می‌کند که *هر یک* از شرط‌ها برقرار باشد.

**سطح پایداری:** آلفا

**دامنه‌ها:** مقادیر ثابت

**مثال کاربرد:**

```go
// +k8s:enum
type MyEnum string

const (
    MyEnumA MyEnum = "A"

    // Never a valid value.
    // +k8s:enumExclude
    MyEnumB MyEnum = "B"

    // Only a valid value while "MyFeature" is disabled.
    // +k8s:ifEnabled(MyFeature)=+k8s:enumExclude
    MyEnumC MyEnum = "C"
)
```

### `+k8s:forbidden` {#tag-forbidden}

**توضیح:**

نشان می‌دهد که یک فیلد نباید مشخص شود.

**سطح پایداری:** بتا

**دامنه‌ها:** فیلدهای struct

**مثال کاربرد:**

```go
type MyStruct struct {
    // +k8s:forbidden
    MyField string `json:"myField"`
}
```

### `+k8s:format` {#tag-format}

**توضیح:**

نشان می‌دهد که یک فیلد رشته‌ای قالب مشخصی دارد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتواها (payload):**

{{< table caption="محتواهای پشتیبانی‌شده برای تگ k8s:format" >}}

| محتوا | معنا |
| --- | --- |
| `k8s-extended-resource-name` | نام منبع توسعه‌یافته (extended resource) در کوبرنتیز: نامی با پیشوند دامنه که نباید پیشوند `kubernetes.io` یا `requests.` داشته باشد. اگر `requests.` را به ابتدای آن اضافه کنید، حاصل باید یک کلید برچسب معتبر باشد؛ همان‌گونه که در سهمیه (quota) استفاده می‌شود. |
| `k8s-label-key` | یک کلید برچسب کوبرنتیز. |
| `k8s-label-value` | یک مقدار برچسب کوبرنتیز. |
| `k8s-long-name` | مقدار «نام بلند» (long name) کوبرنتیز که «زیردامنهٔ DNS» (DNS subdomain) نیز نامیده می‌شود. |
| `k8s-long-name-caseless` | منسوخ‌شده: «نام بلند» کوبرنتیز بدون حساسیت به بزرگی و کوچکی حروف. |
| `k8s-path-segment-name` | مقدار «نام بخش مسیر» (path segment name) در کوبرنتیز. |
| `k8s-prefixed-label-key` | کلید برچسب کوبرنتیز که داشتن پیشوند در آن الزامی است. |
| `k8s-resource-fully-qualified-name` | یک پیشوند و یک نام غیرخالی که با اسلش از هم جدا شده‌اند (برای مثال `prefix/name`). پیشوند باید یک زیردامنهٔ DNS باشد و نام باید یک شناسهٔ C با حداکثر ۳۲ نویسه باشد. |
| `k8s-resource-pool-name` | یک یا چند بخش «نام بلند» کوبرنتیز که با `/` از هم جدا شده‌اند و طول کل آن‌ها از ۲۵۳ نویسه بیشتر نیست. |
| `k8s-short-name` | مقدار «نام کوتاه» (short name) کوبرنتیز که «برچسب DNS» (DNS label) نیز نامیده می‌شود. |
| `k8s-uuid` | یک UUID مطابق با RFC 4122. |

{{< /table >}}

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:format=k8s-long-name
    Subdomain string `json:"subdomain"`

    // +k8s:format=k8s-short-name
    Label string `json:"label"`

    // +k8s:format=k8s-uuid
    ID string `json:"id"`
}
```

### `+k8s:ifDisabled` {#tag-ifDisabled}

**توضیح:**

اعتبارسنجی‌ای را اعلام می‌کند که فقط وقتی یک گزینه غیرفعال است اعمال می‌شود. گزینه‌ها
متناظر با گزینه‌های اعتبارسنجی‌ای هستند که سرور API از روی feature gateها به دست می‌آورد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map،
مقادیر ثابت

**آرگومان‌ها:**

* آرگومان `<option>` (رشته، الزامی): نام گزینه.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگ اعتبارسنجی‌ای که فقط وقتی گزینه
  غیرفعال است ارزیابی می‌شود.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:ifDisabled(MyFeature)=+k8s:required
    MyField string `json:"myField"`
}
```

### `+k8s:ifEnabled` {#tag-ifEnabled}

**توضیح:**

اعتبارسنجی‌ای را اعلام می‌کند که فقط وقتی یک گزینه فعال است اعمال می‌شود. گزینه‌ها
متناظر با گزینه‌های اعتبارسنجی‌ای هستند که سرور API از روی feature gateها به دست می‌آورد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map،
مقادیر ثابت

**آرگومان‌ها:**

* آرگومان `<option>` (رشته، الزامی): نام گزینه.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگ اعتبارسنجی‌ای که فقط وقتی گزینه
  فعال است ارزیابی می‌شود.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:ifEnabled(MyFeature)=+k8s:required
    MyField string `json:"myField"`
}
```

### `+k8s:ifMode` {#tag-ifMode}

**توضیح:**

اعتبارسنجی‌ای را اعلام می‌کند که فقط وقتی [متمایزکنندهٔ حالت](#tag-modeDiscriminator)
در struct مقدار مشخصی داشته باشد اعمال می‌شود. این تگ اعتبارسنجی مبتنی بر وضعیت را
بیان می‌کند؛ یعنی حالتی که شکل یک آبجکت به یک فیلد حالت بستگی دارد.

فیلدی که دست‌کم یک تگ `+k8s:ifMode` دارد، در هر حالتی که در هیچ‌یک از تگ‌هایش نام
برده نشده باشد *به‌طور ضمنی ممنوع* است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct

**آرگومان‌ها:**

* آرگومان `<mode>` (رشته، موقعیتی): مقدار متمایزکننده (discriminator) که این
  اعتبارسنجی برای آن اعمال می‌شود.
* آرگومان `modality` (رشته، اختیاری): نام گروه متمایزکننده، در صورتی که struct
  بیش از یک گروه داشته باشد.
* آرگومان `mode` (رشته، اختیاری): مقدار متمایزکننده، به‌عنوان جایگزینی نام‌دار برای
  آرگومان موقعیتی.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگی که هنگام تطابق حالت ارزیابی می‌شود.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:modeDiscriminator
    Mode string `json:"mode"`

    // Required in mode "A", and additionally length-limited.
    // +k8s:ifMode("A")=+k8s:required
    // +k8s:ifMode("A")=+k8s:maxLength=5
    FieldA *string `json:"fieldA,omitempty"`

    // Optional in mode "B", implicitly forbidden in every other mode.
    // +k8s:ifMode("B")=+k8s:optional
    FieldB *string `json:"fieldB,omitempty"`
}
```

### `+k8s:immutable` {#tag-immutable}

**توضیح:**

نشان می‌دهد که یک فیلد را نمی‌توان به‌روزرسانی کرد. برخلاف [`+k8s:update`](#tag-update)
که گذارهای دقیق‌تری ارائه می‌دهد، تگ `+k8s:immutable` هرگونه تغییر در مقدار را پس از
ایجاد ممنوع می‌کند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، مقادیر map

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:immutable
    StringField string `json:"stringField"`

    // +k8s:immutable
    SliceField []string `json:"sliceField"`
}

// +k8s:immutable
type ImmutableType string
```

### `+k8s:isSubresource` {#tag-isSubresource}

**توضیح:**

تگی در سطح پکیج که قواعد اعتبارسنجی پکیج را به یک زیرمنبع (subresource) محدود می‌کند،
به‌طوری که این قواعد روی آبجکت ریشه یا هیچ زیرمنبع دیگری اعمال نمی‌شوند. با این کار
می‌توانید اعتبارسنجی مختص هر زیرمنبع را در پکیجی جداگانه و جدا از نوع‌های API نگه دارید.

**سطح پایداری:** پایدار

**دامنه:** پکیج

**محتوا:**

* مقدار `<subresource-path>`: مسیر زیرمنبعی که اعتبارسنجی‌های این پکیج روی آن
  اعمال می‌شوند (برای مثال `"/status"` یا `"/scale"`).

{{< alert color="caution" title="Caution" >}}
این تگ به یک تگ [`+k8s:supportsSubresource`](#tag-supportsSubresource) متناظر در
پکیجی که نوع API را تعریف می‌کند نیاز دارد. بدون آن، مولد (generator) کد اعتبارسنجی را
تولید می‌کند، اما توزیع‌کننده (dispatcher) مسیر زیرمنبع را تشخیص نمی‌دهد و در نتیجه
هیچ درخواستی به آن نمی‌رسد.
{{< /alert >}}

**نمونهٔ استفاده:**

در فایل `staging/src/k8s.io/api/apps/v1/doc.go` اعلام کنید که این نوع از
`/scale` پشتیبانی می‌کند:

```go
// +k8s:supportsSubresource="/scale"
package v1
```

در فایل `staging/src/k8s.io/api/apps/v1/validations/scale/doc.go` قواعدی را تعریف کنید
که فقط برای `/scale` اجرا می‌شوند:

```go
// +k8s:isSubresource="/scale"
package scale
```

### `+k8s:item` {#tag-item}

**توضیح:**

اعتبارسنجی‌ای را برای یکی از آیتم‌های یک slice اعلام می‌کند که به‌صورت `+k8s:listType=map`
تعریف شده است. آیتم موردنظر را با ارائهٔ آرگومان‌هایی به شکل جفت فیلد-مقدار مشخص می‌کنید
که در آن‌ها فیلد یک `listMapKey` است. باید همهٔ فیلدهای `listMapKey` را مشخص کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**نحوهٔ استفاده:**

`+k8s:item(<listMapKey-JSON-field-name>: <value>,...)=<validation-tag>`

`+k8s:item(stringKey: "value", intKey: 42, boolKey: true)=<validation-tag>`

آرگومان‌ها را با نام‌های JSON فیلدهای کلید list-map نام‌گذاری کنید. مقادیر می‌توانند
رشته، عدد صحیح یا بولی باشند.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگی که برای آیتم منطبق از لیست ارزیابی می‌شود.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:listType=map
    // +k8s:listMapKey=type
    // +k8s:item(type: "Approved")=+k8s:zeroOrOneOfMember
    // +k8s:item(type: "Denied")=+k8s:zeroOrOneOfMember
    MyConditions []MyCondition `json:"conditions"`
}

type MyCondition struct {
    Type   string `json:"type"`
    Status string `json:"status"`
}
```

در این مثال، شرط‌هایی (condition) که مقدار `type` آن‌ها "Approved" و "Denied" است، عضو
یک گروه مشترک zero-or-one-of (صفر یا یکی) هستند؛ بنابراین حداکثر یکی از آن‌ها می‌تواند
وجود داشته باشد.

### `+k8s:listMapKey` {#tag-listMapKey}

**توضیح:**

یک زیرفیلد نام‌دار از نوع مقدار (value-type) لیست را به‌عنوان بخشی از کلید list-map اعلام
می‌کند. هنگام استفاده از `+k8s:listType=map` یا `+k8s:unique=map` این تگ الزامی است.
می‌توانید از چند تگ `+k8s:listMapKey` استفاده کنید تا مشخص شود کلید لیست از چند فیلد
تشکیل می‌شود.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<field-json-name>` (الزامی): نام JSON فیلدی که به‌عنوان کلید استفاده می‌شود.

**نمونهٔ استفاده:**

```go
// +k8s:listType=map
// +k8s:listMapKey=keyFieldOne
// +k8s:listMapKey=keyFieldTwo
type MyList []MyItem

type MyItem struct {
    KeyFieldOne string `json:"keyFieldOne"`
    KeyFieldTwo string `json:"keyFieldTwo"`
    ValueField  string `json:"valueField"`
}
```

کلید، ترکیبی از `keyFieldOne` و `keyFieldTwo` است.

### `+k8s:listType` {#tag-listType}

**توضیح:**

نوع معنایی و رفتار مالکیت یک فیلد لیستی را اعلام می‌کند:

* مقدار `atomic`: مالکیت واحد؛ کل لیست به‌عنوان یک مقدار واحد در نظر گرفته می‌شود.
* مقدار `set`: مالکیت مشترک همراه با یکتایی؛ هر عنصر باید یکتا باشد.
* مقدار `map`: مالکیت مشترک همراه با یکتایی مبتنی بر کلید؛ به
  [`+k8s:listMapKey`](#tag-listMapKey) نیاز دارد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* یکی از مقادیر `atomic | map | set` (الزامی)

**نمونهٔ استفاده:**

```go
// +k8s:listType=map
// +k8s:listMapKey=keyField
type MyList []MyItem

type MyItem struct {
    KeyField   string `json:"keyField"`
    ValueField string `json:"valueField"`
}
```

هر عنصر `MyList` باید مقدار `keyField` یکتایی داشته باشد.

### `+k8s:maxBytes` {#tag-maxBytes}

**توضیح:**

نشان می‌دهد که طول یک فیلد رشته‌ای بر حسب بایت محدود است. در این حالت ممکن است فقط
N/4 نویسهٔ چندبایتی مجاز باشد. برای محدودکردن تعداد نویسه‌ها، از
[`+k8s:maxLength`](#tag-maxLength) استفاده کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): طول این فیلد نباید بیشتر از X بایت
  باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:maxBytes=1024
    MyString string `json:"myString"`
}
```

### `+k8s:maxItems` {#tag-maxItems}

**توضیح:**

نشان می‌دهد که اندازهٔ یک لیست محدود است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، مقادیر map

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): این لیست نباید بیشتر از X آیتم
  داشته باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:maxItems=5
    MyList []string `json:"myList"`
}
```

### `+k8s:maxLength` {#tag-maxLength}

**توضیح:**

نشان می‌دهد که طول یک فیلد رشته‌ای بر حسب نویسه محدود است. اگر مقدار از نویسه‌های
چندبایتی استفاده کند، ممکن است تا 4*N بایت مجاز باشد. برای محدودکردن تعداد بایت‌ها،
از [`+k8s:maxBytes`](#tag-maxBytes) استفاده کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): طول این فیلد نباید بیشتر از X
  نویسه باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:maxLength=10
    MyString string `json:"myString"`
}
```

### `+k8s:maxProperties` {#tag-maxProperties}

**توضیح:**

محدودیتی برای ویژگی‌های (properties) یک آبجکت، طبق تعریف JSON Schema، تعیین می‌کند.
در کوبرنتیز فقط می‌توانید از آن برای محدودکردن تعداد ورودی‌های فیلدی استفاده کنید که
به‌صورت map در Go تعریف شده است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): این map نباید بیشتر از X ویژگی
  داشته باشد (که در آن X <= 100000).

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:maxProperties=32
    MyMap map[string]string `json:"myMap"`
}
```

### `+k8s:maximum` {#tag-maximum}

**توضیح:**

نشان می‌دهد که یک فیلد عددی مقدار بیشینه دارد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<integer>` (الزامی): این فیلد باید کوچک‌تر از X یا برابر با آن باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:maximum=100
    MyInt int `json:"myInt"`
}
```

### `+k8s:minItems` {#tag-minItems}

**توضیح:**

نشان می‌دهد که یک لیست حداقل اندازه‌ای دارد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، مقادیر map

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): این لیست باید دست‌کم X آیتم داشته باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:minItems=1
    MyList []string `json:"myList"`
}
```

### `+k8s:minLength` {#tag-minLength}

**توضیح:**

نشان می‌دهد که یک فیلد رشته‌ای حداقل طولی بر حسب نویسه دارد. اگر مقدار از نویسه‌های
چندبایتی استفاده کند، حداقل اندازه بر حسب بایت بین X تا 4X خواهد بود.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<integer>` (الزامی): طول این فیلد باید دست‌کم X نویسه باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:minLength=3
    MyString string `json:"myString"`
}
```

### `+k8s:minProperties` {#tag-minProperties}

**توضیح:**

حد پایینی برای ویژگی‌های یک آبجکت، طبق تعریف JSON Schema، تعیین می‌کند. در کوبرنتیز
فقط می‌توانید از آن برای محدودکردن تعداد ورودی‌های فیلدی استفاده کنید که به‌صورت map
در Go تعریف شده است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع

**محتوا:**

* مقدار `<non-negative integer>` (الزامی): این map باید دست‌کم X ویژگی داشته باشد
  (که در آن X <= 100000).

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:minProperties=1
    MyMap map[string]string `json:"myMap"`
}
```

### `+k8s:minimum` {#tag-minimum}

**توضیح:**

نشان می‌دهد که یک فیلد عددی مقدار کمینه دارد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<integer>` (الزامی): این فیلد باید بزرگ‌تر از X یا برابر با آن باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:minimum=0
    MyInt int `json:"myInt"`
}
```

### `+k8s:modeDiscriminator` {#tag-modeDiscriminator}

**توضیح:**

نشان می‌دهد که این فیلد یک متمایزکننده برای اعتبارسنجی مبتنی بر وضعیت است: مقدار آن
تعیین می‌کند که کدام قواعد [`+k8s:ifMode`](#tag-ifMode) روی فیلدهای هم‌سطح در همان
struct اعمال شوند.

متمایزکننده باید از نوع `string` یا `bool` و غیراشاره‌گر باشد. هر struct می‌تواند بیش از
یک گروه متمایزکننده داشته باشد؛ گروه‌های اضافی را با آرگومان `modality` نام‌گذاری کنید.
نام گروه `default` رزرو شده است و نام گروه‌ها باید با الگوی `^[a-zA-Z][a-zA-Z0-9_]*$`
مطابقت داشته باشد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct

**آرگومان‌ها:**

* آرگومان `modality` (رشته، اختیاری): نام گروه متمایزکننده، در صورتی که بیش از یک
  گروه وجود داشته باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:modeDiscriminator
    Mode string `json:"mode"`

    // +k8s:modeDiscriminator(modality:"Legacy")
    Legacy bool `json:"legacy"`

    // +k8s:ifMode("A")=+k8s:required
    FieldA *string `json:"fieldA,omitempty"`

    // +k8s:ifMode(modality:"Legacy", mode:"true")=+k8s:required
    FieldB *string `json:"fieldB,omitempty"`
}
```

### `+k8s:monotonic` {#tag-monotonic}

**توضیح:**

تضمین می‌کند که مقدار یک فیلد عددی هنگام به‌روزرسانی هرگز کاهش نیابد.

**سطح پایداری:** آلفا

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:minimum=0
    // +k8s:monotonic
    Generation int64 `json:"generation"`
}
```

### `+k8s:neq` {#tag-neq}

**توضیح:**

بررسی می‌کند که مقدار فیلد با یک مقدار غیرمجاز مشخص برابر نباشد. از نوع‌های رشته،
عدد صحیح و بولی پشتیبانی می‌کند.

**سطح پایداری:** آلفا

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* مقدار `<value>` (الزامی): مقدار غیرمجاز. تجزیه‌گر نوع آن (string، int، bool) را
  استنتاج می‌کند.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:neq="disallowed"
    MyString string `json:"myString"`

    // +k8s:neq=0
    MyInt int `json:"myInt"`

    // +k8s:neq=true
    MyBool bool `json:"myBool"`
}
```

### `+k8s:opaqueType` {#tag-opaqueType}

**توضیح:**

نشان می‌دهد که مولد همهٔ اعتبارسنجی‌های اعلام‌شده روی نوع ارجاع‌شده را نادیده می‌گیرد.
اگر فلگ‌های فعلی مولد شامل پکیج یک نوع ارجاع‌شده نباشند، باید این تگ را تنظیم کنید؛
در غیر این صورت تولید کد با شکست مواجه می‌شود (و همین از خطاهای پنهان جلوگیری می‌کند).
اگر مولد نباید این اعتبارسنجی‌ها را نادیده بگیرد، پکیج آن نوع را با فلگ `--readonly-pkg`
به مولد اضافه کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**نمونهٔ استفاده:**

```go
import "some/external/package"

type MyStruct struct {
    // +k8s:opaqueType
    ExternalField package.ExternalType `json:"externalField"`
}
```

### `+k8s:optional` {#tag-optional}

**توضیح:**

نشان می‌دهد که تعیین یک فیلد برای کلاینت‌ها اختیاری است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:optional
    MyField string `json:"myField"`
}
```

### `+k8s:required` {#tag-required}

**توضیح:**

نشان می‌دهد که کلاینت‌ها باید یک فیلد را مشخص کنند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:required
    MyField string `json:"myField"`
}
```

### `+k8s:subfield` {#tag-subfield}

**توضیح:**

اعتبارسنجی‌ای را برای یک زیرفیلد از یک struct اعلام می‌کند. زیرفیلد نام‌برده باید فیلد
مستقیم خود struct یا فیلد مستقیم یک struct جاسازی‌شده (embedded) در آن باشد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**آرگومان‌ها:**

* آرگومان `<field-json-name>` (رشته، الزامی): نام JSON زیرفیلد.

**محتوا:**

* مقدار `<validation-tag>` (الزامی): تگی که برای زیرفیلد ارزیابی می‌شود.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:subfield(mySubfield)=+k8s:required
    Inner MyInnerStruct `json:"inner"`
}

type MyInnerStruct struct {
    MySubfield string `json:"mySubfield"`
}
```

### `+k8s:supportsSubresource` {#tag-supportsSubresource}

**توضیح:**

تگی در سطح پکیج که یک مسیر زیرمنبع را در تابع توزیع (dispatch) ثبت می‌کند تا درخواست‌های
ارسالی به آن بتوانند به یک پیاده‌سازی اعتبارسنجی هدایت شوند. برای پشتیبانی از چند زیرمنبع،
این تگ را تکرار کنید.

بدون هیچ تگ `+k8s:supportsSubresource`، فقط منبع ریشه اعتبارسنجی می‌شود و درخواست‌های
زیرمنبع با خطای "no validation found" شکست می‌خورند. اگر این تگ وجود داشته باشد اما تگ
[`+k8s:isSubresource`](#tag-isSubresource) متناظری نباشد، زیرمنبع از قواعد آبجکت ریشه
استفاده می‌کند.

**سطح پایداری:** پایدار

**دامنه:** پکیج

**محتوا:**

* مقدار `<subresource-path>`: مسیر زیرمنبعی که باید پشتیبانی شود (برای مثال
  `"/status"` یا `"/scale"`).

**نمونهٔ استفاده:**

برای مدیریت `/status` و `/scale` برای نوع‌های پکیج `v1`، در فایل
`staging/src/k8s.io/api/core/v1/doc.go` چنین بنویسید:

```go
// +k8s:supportsSubresource="/status"
// +k8s:supportsSubresource="/scale"
package v1
```

### `+k8s:unionDiscriminator` {#tag-unionDiscriminator}

**توضیح:**

نشان می‌دهد که این فیلد متمایزکنندهٔ یک union است. مقدار متمایزکننده تعیین می‌کند که
کدام عضو union باید وجود داشته باشد.

**سطح پایداری:** بتا

**دامنه‌ها:** فیلدهای struct، مقادیر لیست

**آرگومان‌ها:**

* آرگومان `union` (رشته، اختیاری): نام union، در صورتی که بیش از یک union وجود
  داشته باشد.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    TypeMeta int

    // +k8s:unionDiscriminator
    D D `json:"d"`

    // +k8s:unionMember
    // +k8s:optional
    M1 *M1 `json:"m1"`

    // +k8s:unionMember
    // +k8s:optional
    M2 *M2 `json:"m2"`
}

type D string

const (
    DM1 D = "M1"
    DM2 D = "M2"
)

type M1 struct{}

type M2 struct{}
```

مقدار `D` تعیین می‌کند که کدام عضو، یعنی `M1` یا `M2`، باید وجود داشته باشد.

### `+k8s:unionMember` {#tag-unionMember}

**توضیح:**

نشان می‌دهد که این فیلد عضوی از یک union است. دقیقاً یک عضو از هر union باید تنظیم
شده باشد.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، مقادیر لیست

**آرگومان‌ها:**

* آرگومان `union` (رشته، اختیاری): نام union، در صورتی که بیش از یک union وجود
  داشته باشد.
* آرگومان `memberName` (رشته، اختیاری): مقدار متمایزکننده برای این عضو. مقدار
  پیش‌فرض آن نام فیلد است.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:unionMember(union: "union1")
    // +k8s:optional
    M1 *M1 `json:"u1m1"`

    // +k8s:unionMember(union: "union1")
    // +k8s:optional
    M2 *M2 `json:"u1m2"`
}

type M1 struct{}

type M2 struct{}
```

### `+k8s:unique` {#tag-unique}

**توضیح:**

اعلام می‌کند که عناصر یک فیلد لیستی یکتا هستند. می‌توانید این تگ را همراه با
`+k8s:listType=atomic` به کار ببرید تا بدون تغییر معنای ادغام (merge semantics) لیست،
یک قید یکتایی اضافه کنید؛ یا آن را به‌تنهایی برای مشخص‌کردن معنای یکتایی استفاده کنید.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، تعریف‌های نوع، مقادیر لیست، کلیدهای map، مقادیر map

**محتوا:**

* یکی از مقادیر `map | set` (الزامی). با `map`، هویت هر عنصر از فیلدهای
  [`+k8s:listMapKey`](#tag-listMapKey) به دست می‌آید و با `set`، از کل مقدار عنصر.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:listType=atomic
    // +k8s:unique=set
    Names []string `json:"names"`

    // +k8s:listType=atomic
    // +k8s:unique=map
    // +k8s:listMapKey=key
    Items []Item `json:"items"`
}
```

### `+k8s:update` {#tag-update}

**توضیحات:**

این تگ محدودیت‌هایی را بر عملیات به‌روزرسانی مجاز یک فیلد اعمال می‌کند. با به‌کاربردن چند تگ می‌توانید چند محدودیت را هم‌زمان مشخص کنید.

{{< table caption="محدودیت‌های تگ k8s:update" >}}

| محدودیت | اثر |
| --- | --- |
| `NoSet` | از گذار از حالت تنظیم‌نشده به تنظیم‌شده جلوگیری می‌کند. |
| `NoUnset` | از گذار از حالت تنظیم‌شده به تنظیم‌نشده جلوگیری می‌کند. |
| `NoModify` | از تغییر مقدار جلوگیری می‌کند، اما گذار به حالت تنظیم‌شده و تنظیم‌نشده را مجاز می‌داند. |
| `NoAddItem` | از افزودن آیتم به یک slice یا map جلوگیری می‌کند. |
| `NoRemoveItem` | از حذف آیتم از یک slice یا map جلوگیری می‌کند. |

{{< /table >}}

برای structهای غیراشاره‌گر، `NoSet` و `NoUnset` اثری ندارند، زیرا نمی‌توان این فیلدها را به حالت تنظیم‌نشده برگرداند. برای فیلدهای slice و map، «تنظیم‌نشده» به معنای `len == 0` است. هویت آیتم‌های slice در `NoAddItem` و `NoRemoveItem` از [`+k8s:listType`](#tag-listType)، [`+k8s:listMapKey`](#tag-listMapKey) و [`+k8s:unique`](#tag-unique) تعیین می‌شود؛ در mapها، کلید هر آیتم هویت آن را مشخص می‌کند.

تگ `NoModify` به‌طور مستقیم روی sliceها یا mapها پشتیبانی نمی‌شود؛ برای تغییرناپذیری در سطح هر آیتم از `+k8s:eachVal=+k8s:update=NoModify` استفاده کنید. روی لیست‌ها، `+k8s:eachVal=+k8s:update=NoModify` به `listType=map` یا `unique=map` نیاز دارد، زیرا در غیر این صورت تغییرات محتوا قابل تشخیص نیستند.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، مقادیر لیست، مقادیر map

**محتوا (Payload):**

* `NoSet | NoUnset | NoModify | NoAddItem | NoRemoveItem`

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // Set-once: may be set at any time, but never changed or cleared.
    // +k8s:update=NoModify
    // +k8s:update=NoUnset
    SetOnce *string `json:"setOnce,omitempty"`

    // Must be set at creation or never.
    // +k8s:update=NoSet
    AtCreationOnly *string `json:"atCreationOnly,omitempty"`

    // Freeze the shape of the list; individual items may still change.
    // +k8s:listType=map
    // +k8s:listMapKey=key
    // +k8s:update=NoAddItem
    // +k8s:update=NoRemoveItem
    FrozenShape []Item `json:"frozenShape"`
}
```

### `+k8s:zeroOrOneOfMember` {#tag-zeroOrOneOfMember}

**توضیحات:**

نشان می‌دهد که این فیلد عضوی از یک اجتماع (union) از نوع «صفر یا یکی» است. در چنین اجتماعی حداکثر یکی از اعضا می‌تواند تنظیم شود. برخلاف اجتماع‌های معمولی، تنظیم‌نشدن هیچ‌یک از اعضا نیز معتبر است.

**سطح پایداری:** پایدار

**دامنه‌ها:** فیلدهای struct، مقادیر لیست

{{< alert color="caution" title="احتیاط" >}}
این تگ برای مجموعه‌هایی از آیتم‌های لیست در نظر گرفته شده است که از طریق [`+k8s:item`](#tag-item) اعمال می‌شود، نه برای اعمال مستقیم روی فیلدهای struct.
{{< /alert >}}

**آرگومان‌ها:**

* `union` (رشته، اختیاری): نام اجتماع، در صورتی که بیش از یک اجتماع وجود داشته باشد.
* `memberName` (رشته، اختیاری): نام سفارشی این عضو. مقدار پیش‌فرض آن نام فیلد است.

**نمونهٔ استفاده:**

```go
type MyStruct struct {
    // +k8s:listType=map
    // +k8s:listMapKey=type
    // +k8s:item(type: "Approved")=+k8s:zeroOrOneOfMember
    // +k8s:item(type: "Denied")=+k8s:zeroOrOneOfMember
    Conditions []MyCondition `json:"conditions"`
}

type MyCondition struct {
    Type   string `json:"type"`
    Status string `json:"status"`
}
```

در این نمونه، حداکثر یکی از دو شرط «Approved» و «Denied» می‌تواند وجود داشته باشد. نبودن هیچ‌یک از آن دو نیز معتبر است.

## {{% heading "whatsnext" %}}

* دربارهٔ [Feature Gateها](/docs/reference/command-line-tools-reference/feature-gates/) بخوانید.
* سند [KEP-5073: Declarative Validation Of Kubernetes Native Types](https://kep.k8s.io/5073) را بخوانید.

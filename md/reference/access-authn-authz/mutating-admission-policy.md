---
reviewers:
- deads2k
- sttts
- cici37
title: سیاست پذیرش تغییردهنده (Mutating Admission Policy)
content_type: concept
---

<!-- overview -->

{{< feature-state feature_gate_name="MutatingAdmissionPolicy" >}}
<!-- due to feature gate history, use manual version specification here -->

این صفحه مروری بر _MutatingAdmissionPolicies_ ارائه می‌دهد.
MutatingAdmissionPolicies به شما امکان می‌دهند آنچه را که هنگام نوشتن یک تغییر در API کوبرنتیز رخ می‌دهد، تغییر دهید.
اگر می‌خواهید از سیاست‌های اعلانی (declarative) فقط برای جلوگیری از یک نوع خاص تغییر در منابع استفاده کنید (برای مثال: محافظت از فضاهای نام (namespace) پلتفرم در برابر حذف)،
[ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)
جایگزینی ساده‌تر و مؤثرتر است.



<!-- body -->

## MutatingAdmissionPolicies چیست؟

سیاست‌های پذیرش تغییردهنده (Mutating admission policies) جایگزینی اعلانی و درون‌فرایندی (in-process) برای webhookهای پذیرش تغییردهنده ارائه می‌کنند.

سیاست‌های پذیرش تغییردهنده برای تعریف تغییرات منابع از Common Expression Language (CEL) استفاده می‌کنند.
تغییرات را می‌توان یا با یک *apply configuration* تعریف کرد که با
[راهبرد ادغام server side apply](/docs/reference/using-api/server-side-apply/#merge-strategy)
ادغام می‌شود، یا با یک [JSON patch](https://jsonpatch.com/).

سیاست‌های پذیرش تغییردهنده بسیار قابل پیکربندی هستند و به نویسندگان سیاست امکان می‌دهند سیاست‌هایی تعریف کنند
که بتوانند پارامتری شوند و بر حسب نیاز مدیران کلاستر، به منابع مشخصی محدود شوند.

## چه منابعی یک سیاست را می‌سازند

یک سیاست معمولاً از سه منبع تشکیل می‌شود:

- MutatingAdmissionPolicy منطق انتزاعی یک سیاست را توصیف می‌کند
  (مثلاً: «این سیاست یک برچسب مشخص را روی یک مقدار مشخص تنظیم می‌کند»).

- یک _منبع پارامتر_ (parameter resource) اطلاعاتی را در اختیار MutatingAdmissionPolicy قرار می‌دهد تا آن را به یک
  گزاره‌ی مشخص تبدیل کند (مثلاً «برچسب `owner` را روی مقداری مانند `company.example.com` تنظیم کن»).
  منابع پارامتر به منابع کوبرنتیز اشاره می‌کنند که در API کوبرنتیز در دسترس هستند. آن‌ها می‌توانند انواع درونی یا افزونه‌ها باشند،
  مانند {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} (CRD). برای مثال، می‌توانید از یک ConfigMap به‌عنوان پارامتر استفاده کنید.
- MutatingAdmissionPolicyBinding منابع بالا (MutatingAdmissionPolicy و پارامتر) را به یکدیگر پیوند می‌دهد و دامنه‌بندی را فراهم می‌کند.
  اگر فقط می‌خواهید برچسب `owner` را برای `Pods` تنظیم کنید و نه برای سایر انواع API، این تغییر را در binding
  مشخص می‌کنید.



برای اینکه یک سیاست اثر داشته باشد، دست‌کم یک MutatingAdmissionPolicy و یک MutatingAdmissionPolicyBinding متناظر
باید تعریف شده باشند.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
رزرو شده‌اند و نمی‌توان از آن‌ها برای سیاست‌ها یا bindingهای مبتنی بر API استفاده کرد. این رزرو
زمانی اعمال می‌شود که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) با نام `ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

اگر MutatingAdmissionPolicy نیازی به پیکربندی از طریق پارامترها ندارد، کافی است
`spec.paramKind` را در MutatingAdmissionPolicy مشخص نکنید.

## شروع کار با MutatingAdmissionPolicies

سیاست پذیرش تغییردهنده بخشی از control plane کلاستر است. باید آن‌ها را با نهایت احتیاط بنویسید
و مستقر کنید. در ادامه شرح داده می‌شود که چگونه می‌توان به‌سرعت با سیاست پذیرش تغییردهنده
آزمایش کرد.

### ایجاد یک MutatingAdmissionPolicy

در ادامه نمونه‌ای از یک MutatingAdmissionPolicy آمده است. این سیاست، Podهای تازه‌ایجادشده را طوری تغییر می‌دهد که در صورت نبودن کانتینر sidecar، آن را داشته باشند.

{{% code_sample language="yaml" file="mutatingadmissionpolicy/applyconfiguration-example.yaml" %}}

فیلد `.spec.mutations` شامل فهرستی از عبارت‌هاست که به patchهای منبع ارزیابی می‌شوند.
patchهای تولیدشده می‌توانند [apply configurationها](#patch-type-apply-configuration) یا patchهای [JSON Patch](#patch-type-json-patch)
باشند. نمی‌توانید فهرست خالی از mutationها مشخص کنید. پس از ارزیابی همه‌ی
عبارت‌ها، سرور API آن تغییرات را بر منبعی که از مرحله‌ی پذیرش
عبور می‌کند اعمال می‌کند.

برای پیکربندی یک سیاست پذیرش تغییردهنده جهت استفاده در کلاستر، یک binding
لازم است. MutatingAdmissionPolicy تنها زمانی فعال خواهد بود که binding متناظری
وجود داشته باشد که `spec.policyName` ارجاع‌شده در آن با `spec.name`
سیاست مطابقت داشته باشد.

پس از ایجاد binding و سیاست، هر درخواست منبعی که با
`spec.matchConditions` سیاست مطابقت داشته باشد، مجموعه‌ی mutationهای تعریف‌شده را فعال می‌کند.

شرایط تطبیق (match conditions) نمی‌توانند از `namespaceObject` یا `variables` استفاده کنند. `namespaceObject` برای
شرایط تطبیق مقداردهی نمی‌شود و همیشه به null ارزیابی می‌شود، و به `variables` نمی‌توان ارجاع داد زیرا
شرایط تطبیق پیش از بقیه‌ی سیاست ارزیابی می‌شوند. برای انتخاب درخواست‌ها بر اساس برچسب‌های فضای نام،
از یک `namespaceSelector` در `matchConstraints` سیاست یا در `matchResources` مربوط به binding
استفاده کنید.

در مثال بالا، ایجاد یک Pod باعث افزوده‌شدن mutation مربوط به initContainer با نام `mesh-proxy` می‌شود:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
  namespace: default
spec:
  ...
  initContainers:
  - name: mesh-proxy
    image: mesh/proxy:v1.0.0
    args: ["proxy", "sidecar"]
    restartPolicy: Always
  - name: myapp-initializer
    image: example/initializer:v1.0.0
  ...
```

#### منابع پارامتر

منابع پارامتر به پیکربندی سیاست اجازه می‌دهند از تعریف آن جدا باشد.
یک سیاست می‌تواند `paramKind` را تعریف کند که GVK منبع پارامتر را مشخص می‌کند،
و سپس یک binding سیاست، سیاست را با نام (از طریق `policyName`) به
یک منبع پارامتر مشخص از طریق `paramRef` پیوند می‌دهد.

برای اطلاعات بیشتر به [منابع پارامتر](/docs/reference/access-authn-authz/validating-admission-policy/#parameter-resources) مراجعه کنید.

#### `ApplyConfiguration` {#patch-type-apply-configuration}

عبارت‌های MutatingAdmissionPolicy همیشه CEL هستند. هر `expression` از نوع apply configuration
باید به یک آبجکت CEL ارزیابی شود (که با مقداردهی اولیه‌ی `Object()` اعلام می‌شود).

Apply configurationها نمی‌توانند structها، mapها یا آرایه‌های اتمیک (atomic) را تغییر دهند، زیرا خطر حذف ناخواسته‌ی
مقادیری که در apply configuration نیامده‌اند وجود دارد.

عبارت‌های CEL به انواع آبجکت لازم برای ساخت apply configurationها دسترسی دارند:

- `Object` - نوع CEL آبجکت منبع.
- `Object.<fieldName>` - نوع CEL فیلد آبجکت (مانند `Object.spec`)
- `Object.<fieldName1>.<fieldName2>...<fieldNameN>` - نوع CEL فیلد تو در تو (مانند `Object.spec.containers`)

عبارت‌های CEL به محتوای درخواست API دسترسی دارند که در قالب متغیرهای CEL سازمان‌دهی شده است، و همچنین به چند متغیر مفید دیگر:

- `object` - آبجکت موجود در درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- `oldObject` - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- `request` - ویژگی‌های درخواست API.
- `params` - منبع پارامتری که binding سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. فقط در صورتی مقداردهی می‌شود که سیاست دارای ParamKind باشد.
- `namespaceObject` - آبجکت فضای نامی که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع با دامنه‌ی کلاستر برابر null است.
- `variables` - نگاشتی از متغیرهای ترکیب‌شده، از نام هر متغیر به مقدار ارزیابی‌شده‌ی تنبل (lazy) آن.
  برای مثال، متغیری با نام `foo` را می‌توان با `variables.foo` در دسترس قرار داد.
- `authorizer` - یک CEL Authorizer. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای principal (کاربر یا حساب سرویس) درخواست استفاده کرد.
  به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید.
- `authorizer.requestResource` - یک CEL ResourceCheck که از `authorizer` ساخته شده و با
  منبع درخواست پیکربندی شده است.

`apiVersion`، `kind`، `metadata.name`، `metadata.generateName` و `metadata.labels` همیشه از ریشه‌ی
آبجکت در دسترس هستند. هیچ ویژگی دیگری از metadata در دسترس نیست.

#### `JSONPatch` {#patch-type-json-patch}

همان mutation را می‌توان به‌صورت [JSON Patch](https://jsonpatch.com/) به شکل زیر نوشت:

{{% code_sample language="yaml" file="mutatingadmissionpolicy/json-patch-example.yaml" %}}

عبارت توسط CEL ارزیابی می‌شود تا یک [JSON patch](https://jsonpatch.com/) ساخته شود.
مرجع: https://github.com/google/cel-spec

هر `expression` ارزیابی‌شده باید آرایه‌ای از مقادیر `JSONPatch` برگرداند.
نوع `JSONPatch` یک عملیات از یک JSON patch را نمایش می‌دهد.

برای مثال، این عبارت CEL یک JSON patch برمی‌گرداند تا یک مقدار را به‌صورت مشروط تغییر دهد:

```
  [
    JSONPatch{op: "test", path: "/spec/example", value: "Red"},
    JSONPatch{op: "replace", path: "/spec/example", value: "Green"}
  ]
```

برای تعریف یک آبجکت JSON به‌عنوان `value` عملیات patch، از انواع `Object` در CEL استفاده کنید. برای مثال:

```
  [
    JSONPatch{
      op: "add",
      path: "/spec/selector",
      value: Object.spec.selector{matchLabels: {"environment": "test"}}
    }
  ]
```

برای استفاده از رشته‌های حاوی '/' و '~' به‌عنوان کلیدهای مسیر JSONPatch، از `jsonpatch.escapeKey()` استفاده کنید. برای مثال:

```
  [
    JSONPatch{
      op: "add",
      path: "/metadata/labels/" + jsonpatch.escapeKey("example.com/environment"),
      value: "test"
    },
  ]
```

عبارت‌های CEL به انواع لازم برای ساخت JSON patchها و آبجکت‌ها دسترسی دارند:

- `JSONPatch` - نوع CEL عملیات JSON Patch. JSONPatch دارای فیلدهای `op`، `from`، `path` و `value` است.
  برای جزئیات بیشتر به [JSON patch](https://jsonpatch.com/) مراجعه کنید. فیلد `value` را می‌توان روی هر یک از این‌ها تنظیم کرد: رشته،
  عدد صحیح، آرایه، نگاشت (map) یا آبجکت. در صورت تنظیم، فیلدهای `path` و `from` باید روی یک رشته‌ی
  [JSON pointer](https://datatracker.ietf.org/doc/html/rfc6901/) تنظیم شوند، که در آن می‌توان از تابع CEL با نام `jsonpatch.escapeKey()`
  برای escape کردن کلیدهای مسیر حاوی `/` و `~` استفاده کرد.
- `Object` - نوع CEL آبجکت منبع.
- `Object.<fieldName>` - نوع CEL فیلد آبجکت (مانند `Object.spec`)
- `Object.<fieldName1>.<fieldName2>...<fieldNameN>` - نوع CEL فیلد تو در تو (مانند `Object.spec.containers`)

عبارت‌های CEL به محتوای درخواست API دسترسی دارند که در قالب متغیرهای CEL سازمان‌دهی شده است، و همچنین به چند متغیر مفید دیگر:

- `object` - آبجکت موجود در درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- `oldObject` - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- `request` - ویژگی‌های درخواست API.
- `params` - منبع پارامتری که binding سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. فقط در صورتی مقداردهی می‌شود که سیاست دارای ParamKind باشد.
- `namespaceObject` - آبجکت فضای نامی که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع با دامنه‌ی کلاستر برابر null است.
- `variables` - نگاشتی از متغیرهای ترکیب‌شده، از نام هر متغیر به مقدار ارزیابی‌شده‌ی تنبل (lazy) آن.
  برای مثال، متغیری با نام `foo` را می‌توان با `variables.foo` در دسترس قرار داد.
- `authorizer` - یک CEL Authorizer. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای principal (کاربر یا حساب سرویس) درخواست استفاده کرد.
  به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید.
- `authorizer.requestResource` - یک CEL ResourceCheck که از `authorizer` ساخته شده و با
  منبع درخواست پیکربندی شده است.

عبارت‌های CEL به [کتابخانه‌های تابع CEL کوبرنتیز](/docs/reference/using-api/cel/#cel-options-language-features-and-libraries)
دسترسی دارند و همچنین به موارد زیر:

- `jsonpatch.escapeKey` - escape کردن کلید JSONPatch را انجام می‌دهد. `~` و `/` به ترتیب به `~0` و `~1` تبدیل می‌شوند.

فقط نام ویژگی‌هایی با قالب `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس هستند.

## انواع API معاف از پذیرش تغییردهنده

برخی انواع API از تغییر در زمان پذیرش معاف هستند. برای مثال، نمی‌توانید MutatingAdmissionPolicy‌ای ایجاد کنید که یک MutatingAdmissionPolicy را تغییر دهد.

برای جلوگیری از وابستگی‌های حلقوی، انواع پیکربندی پذیرش زیر از سیاست‌هایی که
از طریق REST API ایجاد شده‌اند معاف هستند:

* [ValidatingAdmissionPolicies]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-v1/" >}})
* [ValidatingAdmissionPolicyBindings]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1/" >}})
* MutatingAdmissionPolicies
* MutatingAdmissionPolicyBindings

{{< note >}}
هنگامی که از طریق
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
پیکربندی شود، یک MutatingAdmissionPolicy می‌تواند انواع پیکربندی پذیرش
فهرست‌شده در بالا را رهگیری کند. این کار محدودیت‌هایی را که معمولاً بر سیاست‌های
ایجادشده از طریق REST API اعمال می‌شود دور می‌زند و به شما امکان می‌دهد حتی پیکربندی پذیرش
و منابع حساس از نظر امنیتی را تغییر دهید. برخلاف REST API، یک سیاست پذیرش مبتنی بر مانیفست معیوب
که این منابع را رهگیری کند، غیرقابل بازیابی نخواهد بود،
زیرا روی دیسک تعریف شده است و نه از طریق API.
{{< /note >}}

علاوه بر این، انواع API غیرپایدار (مجازی) احراز هویت و
مجوزدهی زیر از همه‌ی سیاست‌های پذیرش، از جمله سیاست‌های مبتنی بر مانیفست، معاف هستند، زیرا رهگیری آن‌ها می‌تواند
کلاستر را از مسیر احراز هویت و مجوزدهی خودش قفل کند:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

از کوبرنتیز v1.37 به بعد،
[webhookهای پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources)
نیز این منابع مجازی را به‌صورت پیش‌فرض مستثنا می‌کنند.

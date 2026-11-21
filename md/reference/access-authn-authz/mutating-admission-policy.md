---
reviewers:
- deads2k
- sttts
- cici37
title: سیاست پذیرش تغییردهنده
content_type: concept
---

<!-- overview -->

{{< feature-state feature_gate_name="MutatingAdmissionPolicy" >}}
<!-- due to feature gate history, use manual version specification here -->

این صفحه مروری بر _MutatingAdmissionPolicy‌ها_ ارائه می‌کند. با MutatingAdmissionPolicy‌ها می‌توانید رفتار سیستم را هنگامی که کسی تغییری را در API کوبرنتیز می‌نویسد، تغییر دهید. اگر می‌خواهید از سیاست‌های اعلانی فقط برای جلوگیری از نوع خاصی از تغییر در منابع استفاده کنید (برای مثال: محافظت از فضاهای نام پلتفرم در برابر حذف)، [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) جایگزینی ساده‌تر و مؤثرتر است.



<!-- body -->

## سیاست‌های MutatingAdmissionPolicy چه هستند؟

سیاست‌های پذیرش تغییردهنده جایگزینی اعلانی و درون‌فرایندی (in-process) برای وب‌هوک‌های پذیرش تغییردهنده (mutating admission webhooks) هستند.

سیاست‌های پذیرش تغییردهنده برای اعلام تغییرات منابع از زبان Common Expression Language (CEL) استفاده می‌کنند. تغییرات را می‌توان یا با یک *پیکربندی اعمال* (apply configuration) تعریف کرد که با [راهبرد ادغام server side apply](/docs/reference/using-api/server-side-apply/#merge-strategy) ادغام می‌شود، یا با یک [JSON patch](https://jsonpatch.com/).

سیاست‌های پذیرش تغییردهنده بسیار پیکربندی‌پذیرند و نویسندگان سیاست می‌توانند سیاست‌هایی تعریف کنند که مدیران کلاستر در صورت نیاز آن‌ها را پارامتری کنند و دامنهٔ اعمالشان را به منابع مشخصی محدود سازند.

## یک سیاست از چه منابعی تشکیل می‌شود

هر سیاست معمولاً از سه منبع تشکیل می‌شود:

- آبجکت MutatingAdmissionPolicy منطق انتزاعی سیاست را توصیف می‌کند (برای نمونه: «این سیاست برچسب مشخصی را روی مقدار مشخصی تنظیم می‌کند»).

- یک _منبع پارامتر_ اطلاعاتی در اختیار MutatingAdmissionPolicy قرار می‌دهد تا آن را به یک حکم مشخص تبدیل کند (برای نمونه: «برچسب `owner` را روی مقداری مانند `company.example.com` تنظیم کن»).
  منابع پارامتر به منابعی از کوبرنتیز اشاره دارند که در API کوبرنتیز در دسترس هستند. این منابع می‌توانند از انواع داخلی یا افزونه‌ها باشند، مانند یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} (CRD). برای مثال، می‌توانید از یک ConfigMap به‌عنوان پارامتر استفاده کنید.
- آبجکت MutatingAdmissionPolicyBinding منابع بالا (MutatingAdmissionPolicy و پارامتر) را به یکدیگر پیوند می‌دهد و دامنهٔ اعمال را تعیین می‌کند.
  اگر فقط می‌خواهید برچسب `owner` را برای `Pods` تنظیم کنید و نه برای سایر انواع API، این تغییر را در اتصال (binding) مشخص می‌کنید.



برای اینکه یک سیاست اثر داشته باشد، دست‌کم باید یک MutatingAdmissionPolicy و یک MutatingAdmissionPolicyBinding متناظر با آن تعریف شده باشد.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای [کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/) رزرو شده‌اند و نمی‌توان از آن‌ها برای سیاست‌ها یا اتصال‌های مبتنی بر API استفاده کرد. این محدودیت زمانی اعمال می‌شود که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) با نام `ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

اگر یک MutatingAdmissionPolicy نیازی به پیکربندی از طریق پارامترها ندارد، کافی است فیلد `spec.paramKind` را در MutatingAdmissionPolicy مشخص نکنید.

## شروع کار با MutatingAdmissionPolicy‌ها

سیاست پذیرش تغییردهنده بخشی از control plane کلاستر است. این سیاست‌ها را باید با احتیاط فراوان بنویسید و مستقر کنید. در ادامه توضیح داده می‌شود که چگونه می‌توانید به‌سرعت با سیاست پذیرش تغییردهنده آزمایش کنید.

### ایجاد یک MutatingAdmissionPolicy

در ادامه نمونه‌ای از یک MutatingAdmissionPolicy آمده است. این سیاست، Podهای تازه ایجادشده را طوری تغییر می‌دهد که اگر کانتینر sidecar نداشته باشند، این کانتینر به آن‌ها افزوده شود.

{{% code_sample language="yaml" file="mutatingadmissionpolicy/applyconfiguration-example.yaml" %}}

فیلد `.spec.mutations` شامل فهرستی از عبارت‌هاست که حاصل ارزیابی هر یک، وصله‌ای (patch) برای منبع است. وصله‌های تولیدشده می‌توانند از نوع [پیکربندی اعمال](#patch-type-apply-configuration) یا [JSON Patch](#patch-type-json-patch) باشند. نمی‌توانید فهرست خالی از تغییرات تعیین کنید. سرور API پس از ارزیابی همهٔ عبارت‌ها، این تغییرات را روی منبعی که در حال گذر از مرحلهٔ پذیرش است اعمال می‌کند.

برای پیکربندی یک سیاست پذیرش تغییردهنده جهت استفاده در کلاستر، به یک اتصال نیاز است. هر MutatingAdmissionPolicy تنها زمانی فعال می‌شود که اتصال متناظری وجود داشته باشد که مقدار `spec.policyName` آن با `spec.name` سیاست مطابقت داشته باشد.

پس از ایجاد اتصال و سیاست، هر درخواست منبعی که با `spec.matchConditions` یک سیاست مطابقت داشته باشد، مجموعهٔ تغییرات تعریف‌شده را به اجرا درمی‌آورد.

شرط‌های تطبیق (match conditions) نمی‌توانند از `namespaceObject` یا `variables` استفاده کنند. مقدار `namespaceObject` برای شرط‌های تطبیق پر نمی‌شود و همیشه null ارزیابی می‌شود. همچنین نمی‌توان به `variables` ارجاع داد، زیرا شرط‌های تطبیق پیش از بقیهٔ سیاست ارزیابی می‌شوند. برای انتخاب درخواست‌ها بر اساس برچسب‌های فضای نام، از یک `namespaceSelector` در `matchConstraints` سیاست یا در `matchResources` اتصال استفاده کنید.

در مثال بالا، با ایجاد یک Pod، تغییر مربوط به initContainer با نام `mesh-proxy` اعمال می‌شود:

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

با منابع پارامتر می‌توان پیکربندی یک سیاست را از تعریف آن جدا کرد. هر سیاست می‌تواند `paramKind` را تعریف کند که GVK منبع پارامتر را مشخص می‌کند. سپس یک اتصال سیاست، سیاست را با نامش (از طریق `policyName`) و به‌واسطهٔ `paramRef` به یک منبع پارامتر مشخص پیوند می‌دهد.

برای اطلاعات بیشتر به [منابع پارامتر](/docs/reference/access-authn-authz/validating-admission-policy/#parameter-resources) مراجعه کنید.

#### نوع `ApplyConfiguration` {#patch-type-apply-configuration}

عبارت‌های MutatingAdmissionPolicy همیشه به زبان CEL نوشته می‌شوند. هر `expression` پیکربندی اعمال باید به یک آبجکت CEL ارزیابی شود (که با مقداردهی اولیهٔ `Object()` اعلام می‌شود).

پیکربندی‌های اعمال نمی‌توانند ساختارها (struct)، نگاشت‌ها (map) یا آرایه‌های اتمیک را تغییر دهند، زیرا این کار خطر حذف تصادفی مقادیری را به همراه دارد که در پیکربندی اعمال گنجانده نشده‌اند.

عبارت‌های CEL به انواع آبجکتی که برای ایجاد پیکربندی‌های اعمال لازم است دسترسی دارند:

- نوع `Object`: نوع CEL آبجکت منبع.
- نوع `Object.<fieldName>`: نوع CEL فیلد آبجکت (مانند `Object.spec`)
- نوع `Object.<fieldName1>.<fieldName2>...<fieldNameN>`: نوع CEL فیلد تودرتو (مانند `Object.spec.containers`)

عبارت‌های CEL به محتوای درخواست API که در قالب متغیرهای CEL سازمان‌دهی شده و نیز به چند متغیر مفید دیگر دسترسی دارند:

- متغیر `object`: آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- متغیر `oldObject`: آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- متغیر `request`: ویژگی‌های درخواست API.
- متغیر `params`: منبع پارامتری که اتصالِ سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. این متغیر فقط در صورتی پر می‌شود که سیاست دارای ParamKind باشد.
- متغیر `namespaceObject`: آبجکت فضای نامی که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع در سطح کلاستر برابر null است.
- متغیر `variables`: نگاشتی از متغیرهای ترکیبی که نام هر متغیر را به مقدار آن، که به‌صورت تنبل (lazy) ارزیابی می‌شود، نگاشت می‌کند.
  برای مثال، به متغیری با نام `foo` می‌توان از طریق `variables.foo` دسترسی داشت.
- متغیر `authorizer`: یک Authorizer در CEL. می‌توان از آن برای بررسی مجوزهای principal درخواست (کاربر یا حساب سرویس) استفاده کرد.
  به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید.
- متغیر `authorizer.requestResource`: یک ResourceCheck در CEL که از `authorizer` ساخته شده و با منبعِ درخواست پیکربندی شده است.

فیلدهای `apiVersion`، `kind`، `metadata.name`، `metadata.generateName` و `metadata.labels` همیشه از ریشهٔ آبجکت در دسترس هستند. هیچ ویژگی دیگری از metadata در دسترس نیست.

#### نوع `JSONPatch` {#patch-type-json-patch}

همین تغییر را می‌توان به‌صورت یک [JSON Patch](https://jsonpatch.com/) به شکل زیر نوشت:

{{% code_sample language="yaml" file="mutatingadmissionpolicy/json-patch-example.yaml" %}}

زبان CEL این عبارت را ارزیابی می‌کند تا یک [JSON patch](https://jsonpatch.com/) ایجاد شود.
مرجع: https://github.com/google/cel-spec

هر `expression` ارزیابی‌شده باید آرایه‌ای از مقادیر `JSONPatch` برگرداند. نوع `JSONPatch` نمایانگر یک عملیات از یک JSON patch است.

برای مثال، عبارت CEL زیر یک JSON patch برمی‌گرداند که مقداری را به‌صورت شرطی تغییر می‌دهد:

```
  [
    JSONPatch{op: "test", path: "/spec/example", value: "Red"},
    JSONPatch{op: "replace", path: "/spec/example", value: "Green"}
  ]
```

برای تعریف یک آبجکت JSON به‌عنوان `value` عملیات وصله، از انواع `Object` در CEL استفاده کنید. برای مثال:

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

عبارت‌های CEL به انواعی که برای ایجاد وصله‌ها و آبجکت‌های JSON لازم است دسترسی دارند:

- نوع `JSONPatch`: نوع CEL عملیات‌های JSON Patch. این نوع فیلدهای `op`، `from`، `path` و `value` را دارد.
  برای جزئیات بیشتر به [JSON patch](https://jsonpatch.com/) مراجعه کنید. فیلد `value` را می‌توان روی هر یک از این انواع تنظیم کرد: رشته، عدد صحیح، آرایه، نگاشت یا آبجکت. در صورت تنظیم، فیلدهای `path` و `from` باید روی یک رشتهٔ [JSON pointer](https://datatracker.ietf.org/doc/html/rfc6901/) تنظیم شوند که در آن می‌توان از تابع CEL `jsonpatch.escapeKey()` برای escape کردن کلیدهای مسیرِ حاوی `/` و `~` استفاده کرد.
- نوع `Object`: نوع CEL آبجکت منبع.
- نوع `Object.<fieldName>`: نوع CEL فیلد آبجکت (مانند `Object.spec`)
- نوع `Object.<fieldName1>.<fieldName2>...<fieldNameN>`: نوع CEL فیلد تودرتو (مانند `Object.spec.containers`)

عبارت‌های CEL به محتوای درخواست API که در قالب متغیرهای CEL سازمان‌دهی شده و نیز به چند متغیر مفید دیگر دسترسی دارند:

- متغیر `object`: آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است.
- متغیر `oldObject`: آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- متغیر `request`: ویژگی‌های درخواست API.
- متغیر `params`: منبع پارامتری که اتصالِ سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. این متغیر فقط در صورتی پر می‌شود که سیاست دارای ParamKind باشد.
- متغیر `namespaceObject`: آبجکت فضای نامی که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع در سطح کلاستر برابر null است.
- متغیر `variables`: نگاشتی از متغیرهای ترکیبی که نام هر متغیر را به مقدار آن، که به‌صورت تنبل ارزیابی می‌شود، نگاشت می‌کند.
  برای مثال، به متغیری با نام `foo` می‌توان از طریق `variables.foo` دسترسی داشت.
- متغیر `authorizer`: یک Authorizer در CEL. می‌توان از آن برای بررسی مجوزهای principal درخواست (کاربر یا حساب سرویس) استفاده کرد.
  به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید.
- متغیر `authorizer.requestResource`: یک ResourceCheck در CEL که از `authorizer` ساخته شده و با منبعِ درخواست پیکربندی شده است.

عبارت‌های CEL به [کتابخانه‌های توابع CEL کوبرنتیز](/docs/reference/using-api/cel/#cel-options-language-features-and-libraries) و همچنین به موارد زیر دسترسی دارند:

- تابع `jsonpatch.escapeKey`: کلیدهای JSONPatch را escape می‌کند. نویسه‌های `~` و `/` به‌ترتیب به‌صورت `~0` و `~1` escape می‌شوند.

فقط نام ویژگی‌هایی به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس هستند.

## انواع API معاف از پذیرش تغییردهنده

برخی انواع API از تغییر در زمان پذیرش معاف هستند. برای مثال، نمی‌توانید MutatingAdmissionPolicy‌ای ایجاد کنید که یک MutatingAdmissionPolicy دیگر را تغییر دهد.

برای جلوگیری از وابستگی‌های چرخه‌ای، انواع پیکربندی پذیرش زیر از سیاست‌هایی که از طریق REST API ایجاد می‌شوند معاف هستند:

* [ValidatingAdmissionPolicies]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-v1/" >}})
* [ValidatingAdmissionPolicyBindings]({{< relref "/docs/reference/kubernetes-api/admissionregistration/validating-admission-policy-binding-v1/" >}})
* MutatingAdmissionPolicies
* MutatingAdmissionPolicyBindings

{{< note >}}
هنگامی که یک MutatingAdmissionPolicy از طریق [کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/) پیکربندی شود، می‌تواند انواع پیکربندی پذیرشِ فهرست‌شده در بالا را رهگیری کند. این کار محدودیت‌هایی را که معمولاً بر سیاست‌های ایجادشده از طریق REST API اعمال می‌شود دور می‌زند و به شما امکان می‌دهد حتی پیکربندی پذیرش و منابع حساس از نظر امنیتی را نیز تغییر دهید. برخلاف REST API، اگر یک سیاست پذیرش مبتنی بر مانیفستِ نادرست این منابع را رهگیری کند، وضعیت غیرقابل بازیابی نخواهد شد، زیرا این سیاست به‌جای API روی دیسک تعریف شده است.
{{< /note >}}

افزون بر این، انواع API احراز هویت و مجوزدهیِ ذخیره‌نشده (مجازی) زیر از همهٔ سیاست‌های پذیرش، از جمله سیاست‌های مبتنی بر مانیفست، معاف هستند، زیرا رهگیری آن‌ها ممکن است دسترسی کلاستر به مسیر احراز هویت و مجوزدهیِ خودش را مسدود کند:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

از کوبرنتیز نسخهٔ v1.37 به بعد، [وب‌هوک‌های پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources) نیز به‌طور پیش‌فرض این منابع مجازی را مستثنا می‌کنند.

---
title: گسترش API کوبرنتیز با CustomResourceDefinitionها
reviewers:
- deads2k
- jpbetz
- liggitt
- roycaihw
- sttts
content_type: task
min-kubernetes-server-version: 1.16
weight: 20
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه با ایجاد یک
[CustomResourceDefinition](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#customresourcedefinition-v1-apiextensions-k8s-io)،
یک [منبع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) (custom resource)
را در API کوبرنتیز نصب کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}
اگر از نسخهٔ قدیمی‌تری از کوبرنتیز استفاده می‌کنید که هنوز پشتیبانی می‌شود، به مستندات همان نسخه
بروید تا توصیه‌های متناسب با کلاستر خود را ببینید.

<!-- steps -->

## ایجاد یک CustomResourceDefinition

هنگامی که یک CustomResourceDefinition (CRD) جدید ایجاد می‌کنید، سرور API کوبرنتیز برای هر نسخه‌ای
که مشخص کرده‌اید یک مسیر منبع RESTful جدید می‌سازد. منبع سفارشی‌ای که از یک آبجکت CRD ساخته می‌شود،
بسته به مقدار فیلد `spec.scope` در CRD، می‌تواند در محدودهٔ فضای نام (namespace) یا در محدودهٔ کل
کلاستر باشد. همانند آبجکت‌های داخلی موجود، حذف یک فضای نام همهٔ آبجکت‌های سفارشی آن فضای نام را نیز
حذف می‌کند. خودِ CustomResourceDefinitionها به هیچ فضای نامی تعلق ندارند و در همهٔ فضاهای نام در
دسترس هستند.

برای مثال، اگر CustomResourceDefinition زیر را در فایل `resourcedefinition.yaml` ذخیره کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.stable.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: stable.example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
    - name: v1
      # Each version can be enabled/disabled by Served flag.
      served: true
      # One and only one version must be marked as the storage version.
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  # either Namespaced or Cluster
  scope: Namespaced
  names:
    # plural name to be used in the URL: /apis/<group>/<version>/<plural>
    plural: crontabs
    # singular name to be used as an alias on the CLI and for display
    singular: crontab
    # kind is normally the CamelCased singular type. Your resource manifests use this.
    kind: CronTab
    # shortNames allow shorter string to match your resource on the CLI
    shortNames:
    - ct
```

و آن را ایجاد کنید:

```shell
kubectl apply -f resourcedefinition.yaml
```

آنگاه یک نقطهٔ پایانی (endpoint) جدید API از نوع RESTful و در محدودهٔ فضای نام در مسیر زیر ایجاد می‌شود:

```
/apis/stable.example.com/v1/namespaces/*/crontabs/...
```

سپس می‌توانید از این URL نقطهٔ پایانی برای ایجاد و مدیریت آبجکت‌های سفارشی استفاده کنید.
مقدار `kind` این آبجکت‌ها برابر با `CronTab` خواهد بود که از spec آبجکت CustomResourceDefinition
ایجادشده در بالا گرفته می‌شود.

ممکن است ایجاد نقطهٔ پایانی چند ثانیه طول بکشد. می‌توانید شرط `Established` در CustomResourceDefinition
خود را زیر نظر بگیرید تا true شود، یا اطلاعات کشف (discovery) سرور API را دنبال کنید تا منبع شما در آن
ظاهر شود.

## ایجاد آبجکت‌های سفارشی

پس از ایجاد آبجکت CustomResourceDefinition، می‌توانید آبجکت‌های سفارشی بسازید. آبجکت‌های سفارشی
می‌توانند فیلدهای سفارشی داشته باشند و این فیلدها می‌توانند هر JSON دلخواهی را در خود نگه دارند.
در مثال زیر، فیلدهای سفارشی `cronSpec` و `image` در یک آبجکت سفارشی از نوع `CronTab` مقداردهی
شده‌اند. نوع `CronTab` از spec آبجکت CustomResourceDefinition ایجادشده در بالا می‌آید.

اگر YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```

و آن را ایجاد کنید:

```shell
kubectl apply -f my-crontab.yaml
```

آنگاه می‌توانید آبجکت‌های CronTab خود را با kubectl مدیریت کنید. برای مثال:

```shell
kubectl get crontab
```

باید فهرستی مانند زیر چاپ شود:

```none
NAME                 AGE
my-new-cron-object   6s
```

هنگام استفاده از kubectl، نام منابع به بزرگی و کوچکی حروف حساس نیست و می‌توانید از شکل مفرد یا جمعِ
تعریف‌شده در CRD و نیز از هر یک از نام‌های کوتاه استفاده کنید.

همچنین می‌توانید داده‌های خام YAML را ببینید:

```shell
kubectl get ct -o yaml
```

باید ببینید که خروجی شامل فیلدهای سفارشی `cronSpec` و `image` از YAMLی است که برای ایجاد آبجکت
به کار بردید:

```yaml
apiVersion: v1
items:
- apiVersion: stable.example.com/v1
  kind: CronTab
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"stable.example.com/v1","kind":"CronTab","metadata":{"annotations":{},"name":"my-new-cron-object","namespace":"default"},"spec":{"cronSpec":"* * * * */5","image":"my-awesome-cron-image"}}
    creationTimestamp: "2021-06-20T07:35:27Z"
    generation: 1
    name: my-new-cron-object
    namespace: default
    resourceVersion: "1326"
    uid: 9aab1d66-628e-41bb-a422-57b8b3b1f5a9
  spec:
    cronSpec: '* * * * */5'
    image: my-awesome-cron-image
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
```

## حذف یک CustomResourceDefinition

هنگامی که یک CustomResourceDefinition را حذف می‌کنید، سرور نقطهٔ پایانی API از نوع RESTful را
حذف می‌کند و همهٔ آبجکت‌های سفارشی ذخیره‌شده در آن را نیز پاک می‌کند.

```shell
kubectl delete -f resourcedefinition.yaml
kubectl get crontabs
```

```none
Error from server (NotFound): Unable to list {"stable.example.com" "v1" "crontabs"}: the server could not
find the requested resource (get crontabs.stable.example.com)
```

اگر بعداً همان CustomResourceDefinition را دوباره ایجاد کنید، در ابتدا خالی خواهد بود.

## تعیین یک طرح‌وارهٔ ساختاری

منابع سفارشی (CustomResources) داده‌های ساخت‌یافته را در فیلدهای سفارشی ذخیره می‌کنند (در کنار
فیلدهای داخلی `apiVersion`، `kind` و `metadata` که سرور API به‌طور ضمنی اعتبارسنجی می‌کند). با
[اعتبارسنجی OpenAPI v3.0](#validation) می‌توان یک طرح‌واره (schema) تعیین کرد که هنگام ایجاد و
به‌روزرسانی اعتبارسنجی می‌شود. برای جزئیات و محدودیت‌های چنین طرح‌واره‌ای، توضیحات زیر را ببینید.

در `apiextensions.k8s.io/v1`، تعریف یک طرح‌وارهٔ ساختاری برای CustomResourceDefinitionها الزامی
است. در نسخهٔ بتای CustomResourceDefinition، طرح‌وارهٔ ساختاری اختیاری بود.

طرح‌وارهٔ ساختاری یک [طرح‌وارهٔ اعتبارسنجی OpenAPI v3.0](#validation) است که:

1. برای ریشه، برای هر فیلد مشخص‌شده از یک گرهٔ آبجکت (از طریق `properties` یا `additionalProperties`
   در OpenAPI) و برای هر آیتم در یک گرهٔ آرایه (از طریق `items` در OpenAPI) یک نوع غیرخالی (از طریق
   `type` در OpenAPI) تعیین می‌کند، به‌جز موارد زیر:
   * گره‌ای با `x-kubernetes-int-or-string: true`
   * گره‌ای با `x-kubernetes-preserve-unknown-fields: true`
2. برای هر فیلد در یک آبجکت و هر آیتم در یک آرایه که درون یکی از `allOf`، `anyOf`، `oneOf` یا `not`
   مشخص شده باشد، آن فیلد یا آیتم را بیرون از این عملگرهای منطقی نیز مشخص می‌کند (مثال ۱ و ۲ را مقایسه
   کنید).
3. مقادیر `description`، `type`، `default`، `additionalProperties` و `nullable` را درون `allOf`،
   `anyOf`، `oneOf` یا `not` تنظیم نمی‌کند، به‌جز دو الگوی مربوط به `x-kubernetes-int-or-string: true`
   (در ادامه را ببینید).
4. اگر `metadata` مشخص شده باشد، فقط محدودیت‌هایی روی `metadata.name` و `metadata.generateName` مجاز
   است.

مثال غیرساختاری ۱:

```yaml
allOf:
- properties:
    foo:
      # ...
```

با قاعدهٔ ۲ در تعارض است. شکل درست آن چنین است:

```yaml
properties:
  foo:
    # ...
allOf:
- properties:
    foo:
      # ...
```

مثال غیرساختاری ۲:

```yaml
allOf:
- items:
    properties:
      foo:
        # ...
```
با قاعدهٔ ۲ در تعارض است. شکل درست آن چنین است:

```yaml
items:
  properties:
    foo:
      # ...
allOf:
- items:
    properties:
      foo:
        # ...
```

مثال غیرساختاری ۳:

```yaml
properties:
  foo:
    pattern: "abc"
  metadata:
    type: object
    properties:
      name:
        type: string
        pattern: "^a"
      finalizers:
        type: array
        items:
          type: string
          pattern: "my-finalizer"
anyOf:
- properties:
    bar:
      type: integer
      minimum: 42
  required: ["bar"]
  description: "foo bar object"
```

به دلیل تخلف‌های زیر یک طرح‌وارهٔ ساختاری نیست:

* نوعِ ریشه مشخص نشده است (قاعدهٔ ۱).
* نوعِ `foo` مشخص نشده است (قاعدهٔ ۱).
* فیلد `bar` درون `anyOf` بیرون از آن مشخص نشده است (قاعدهٔ ۲).
* مقدار `type` برای `bar` درون `anyOf` قرار دارد (قاعدهٔ ۳).
* توضیح (description) درون `anyOf` تنظیم شده است (قاعدهٔ ۳).
* فیلد `metadata.finalizers` نباید محدود شود (قاعدهٔ ۴).

در مقابل، طرح‌وارهٔ متناظر زیر ساختاری است:

```yaml
type: object
description: "foo bar object"
properties:
  foo:
    type: string
    pattern: "abc"
  bar:
    type: integer
  metadata:
    type: object
    properties:
      name:
        type: string
        pattern: "^a"
anyOf:
- properties:
    bar:
      minimum: 42
  required: ["bar"]
```

تخلف از قواعد طرح‌وارهٔ ساختاری در شرط `NonStructural` در CustomResourceDefinition گزارش می‌شود.

### هرس فیلدها

CustomResourceDefinitionها داده‌های اعتبارسنجی‌شدهٔ منابع را در ذخیره‌گاه ماندگار کلاستر، یعنی
{{< glossary_tooltip term_id="etcd" text="etcd">}}، ذخیره می‌کنند. همانند منابع بومی کوبرنتیز مانند
{{< glossary_tooltip text="ConfigMap" term_id="configmap" >}}، اگر فیلدی را مشخص کنید که سرور API آن
را نمی‌شناسد، آن فیلد ناشناخته پیش از ذخیره‌شدن _هرس_ (حذف) می‌شود.

ممکن است CRDهایی که از `apiextensions.k8s.io/v1beta1` به `apiextensions.k8s.io/v1` تبدیل شده‌اند
طرح‌وارهٔ ساختاری نداشته باشند و مقدار `spec.preserveUnknownFields` در آن‌ها `true` باشد.

برای آبجکت‌های قدیمی CustomResourceDefinition که به‌صورت `apiextensions.k8s.io/v1beta1` و با
مقدار `true` برای `spec.preserveUnknownFields` ایجاد شده‌اند، موارد زیر نیز صدق می‌کند:

* هرس فعال نیست.
* می‌توانید داده‌های دلخواه ذخیره کنید.

برای سازگاری با `apiextensions.k8s.io/v1`، تعریف‌های منابع سفارشی خود را به‌گونه‌ای به‌روزرسانی کنید
که:

1. از یک طرح‌وارهٔ ساختاری OpenAPI استفاده کنند.
2. مقدار `spec.preserveUnknownFields` را `false` قرار دهند.

اگر YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
  someRandomField: 42
```

و آن را ایجاد کنید:

```shell
kubectl create --validate=false -f my-crontab.yaml -o yaml
```

خروجی شما مشابه زیر خواهد بود:

```yaml
apiVersion: stable.example.com/v1
kind: CronTab
metadata:
  creationTimestamp: 2017-05-31T12:56:35Z
  generation: 1
  name: my-new-cron-object
  namespace: default
  resourceVersion: "285"
  uid: 9423255b-4600-11e7-af6a-28d2447dc82b
spec:
  cronSpec: '* * * * */5'
  image: my-awesome-cron-image
```

توجه کنید که فیلد `someRandomField` هرس شده است.

در این مثال، برای نمایش رفتار سرور API، اعتبارسنجی سمت کلاینت با افزودن گزینهٔ خط فرمان
`--validate=false` غیرفعال شده است. از آنجا که
[طرح‌واره‌های اعتبارسنجی OpenAPI برای کلاینت‌ها نیز منتشر می‌شوند](#publish-validation-schema-in-openapi)،
`kubectl` نیز فیلدهای ناشناخته را بررسی می‌کند و چنین آبجکت‌هایی را مدت‌ها پیش از ارسال به سرور API
رد می‌کند.

#### کنترل هرس

به‌طور پیش‌فرض، همهٔ فیلدهای مشخص‌نشدهٔ یک منبع سفارشی در همهٔ نسخه‌ها هرس می‌شوند. با این حال،
می‌توان با افزودن `x-kubernetes-preserve-unknown-fields: true` در
[طرح‌وارهٔ ساختاری اعتبارسنجی OpenAPI v3](#specifying-a-structural-schema)، زیردرخت‌های مشخصی از
فیلدها را از این رفتار مستثنا کرد.

برای مثال:

```yaml
type: object
properties:
  json:
    x-kubernetes-preserve-unknown-fields: true
```

فیلد `json` می‌تواند هر مقدار JSON را بدون هرس شدن هیچ بخشی ذخیره کند.

همچنین می‌توانید JSON مجاز را به‌صورت جزئی مشخص کنید؛ برای مثال:

```yaml
type: object
properties:
  json:
    x-kubernetes-preserve-unknown-fields: true
    type: object
    description: this is arbitrary JSON
```

با این کار، فقط مقادیری از نوع `object` مجاز هستند.

برای هر ویژگی مشخص‌شده (یا `additionalProperties`)، هرس دوباره فعال می‌شود:

```yaml
type: object
properties:
  json:
    x-kubernetes-preserve-unknown-fields: true
    type: object
    properties:
      spec:
        type: object
        properties:
          foo:
            type: string
          bar:
            type: string
```

با این تعریف، مقدار زیر:

```yaml
json:
  spec:
    foo: abc
    bar: def
    something: x
  status:
    something: x
```

به این شکل هرس می‌شود:

```yaml
json:
  spec:
    foo: abc
    bar: def
  status:
    something: x
```

یعنی فیلد `something` در آبجکت مشخص‌شدهٔ `spec` هرس می‌شود، اما هیچ‌چیز بیرون از آن هرس نمی‌شود.

### IntOrString

گره‌هایی از طرح‌واره که `x-kubernetes-int-or-string: true` دارند از قاعدهٔ ۱ مستثنا هستند، به‌طوری
که طرح‌وارهٔ زیر ساختاری است:

```yaml
type: object
properties:
  foo:
    x-kubernetes-int-or-string: true
```

همچنین این گره‌ها تا حدی از قاعدهٔ ۳ مستثنا هستند، به این معنا که دو الگوی زیر مجاز است (دقیقاً
همین دو الگو، بدون تغییر در ترتیب یا افزودن فیلدهای دیگر):

```yaml
x-kubernetes-int-or-string: true
anyOf:
  - type: integer
  - type: string
...
```

و

```yaml
x-kubernetes-int-or-string: true
allOf:
  - anyOf:
      - type: integer
      - type: string
  - # ... zero or more
...
```

با هر یک از این تعریف‌ها، هم عدد صحیح و هم رشته معتبر شناخته می‌شوند.

در [انتشار طرح‌وارهٔ اعتبارسنجی](#publish-validation-schema-in-openapi)،
`x-kubernetes-int-or-string: true` به یکی از دو الگوی بالا گسترش داده می‌شود.

### RawExtension

ساختارهای RawExtension (مانند [`runtime.RawExtension`](/docs/reference//kubernetes-api/workload-resources/controller-revision-v1#RawExtension))
آبجکت‌های کامل کوبرنتیز، یعنی آبجکت‌هایی دارای فیلدهای `apiVersion` و `kind`، را در خود نگه می‌دارند.

می‌توان این آبجکت‌های تعبیه‌شده را (چه کاملاً بدون محدودیت و چه به‌صورت جزئی) با تنظیم
`x-kubernetes-embedded-resource: true` مشخص کرد. برای مثال:

```yaml
type: object
properties:
  foo:
    x-kubernetes-embedded-resource: true
    x-kubernetes-preserve-unknown-fields: true
```

در اینجا، فیلد `foo` یک آبجکت کامل را نگه می‌دارد؛ برای نمونه:

```yaml
foo:
  apiVersion: v1
  kind: Pod
  spec:
    # ...
```

از آنجا که `x-kubernetes-preserve-unknown-fields: true` نیز در کنار آن مشخص شده است، هیچ‌چیز هرس
نمی‌شود. البته استفاده از `x-kubernetes-preserve-unknown-fields: true` اختیاری است.

با `x-kubernetes-embedded-resource: true`، فیلدهای `apiVersion`، `kind` و `metadata` به‌طور ضمنی
مشخص و اعتبارسنجی می‌شوند.

## ارائهٔ چند نسخه از یک CRD

برای اطلاعات بیشتر دربارهٔ ارائهٔ چند نسخه از CustomResourceDefinition و انتقال آبجکت‌ها از یک نسخه به
نسخهٔ دیگر، به
[نسخه‌بندی تعریف منابع سفارشی](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
مراجعه کنید.

<!-- discussion -->
## مباحث پیشرفته

### نهایی‌کننده‌ها

*نهایی‌کننده‌ها* (Finalizers) به کنترل‌کننده‌ها امکان می‌دهند قلاب‌های (hooks) ناهمگامِ پیش از حذف
را پیاده‌سازی کنند. آبجکت‌های سفارشی، همانند آبجکت‌های داخلی، از نهایی‌کننده‌ها پشتیبانی می‌کنند.

می‌توانید یک نهایی‌کننده را به این شکل به یک آبجکت سفارشی اضافه کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  finalizers:
  - stable.example.com/finalizer
```

شناسهٔ نهایی‌کننده‌های سفارشی از یک نام دامنه، یک کاراکتر اسلش (/) و نام نهایی‌کننده تشکیل می‌شود.
هر کنترل‌کننده‌ای می‌تواند یک نهایی‌کننده را به فهرست نهایی‌کننده‌های هر آبجکتی اضافه کند.

نخستین درخواست حذف روی آبجکتی که نهایی‌کننده دارد، مقداری برای فیلد `metadata.deletionTimestamp`
تنظیم می‌کند، اما آبجکت را حذف نمی‌کند. پس از تنظیم این مقدار، فقط می‌توان مدخل‌هایی را از فهرست
`finalizers` حذف کرد. تا زمانی که نهایی‌کننده‌ای باقی مانده باشد، حذف اجباری آبجکت نیز ممکن نیست.

هنگامی که فیلد `metadata.deletionTimestamp` تنظیم می‌شود، کنترل‌کننده‌هایی که آبجکت را زیر نظر دارند
نهایی‌کننده‌های مربوط به خود را اجرا می‌کنند و پس از پایان کار، آن‌ها را از فهرست حذف می‌کنند. حذف
نهایی‌کنندهٔ هر کنترل‌کننده از فهرست، بر عهدهٔ خودِ آن کنترل‌کننده است.

مقدار `metadata.deletionGracePeriodSeconds` فاصلهٔ زمانی میان به‌روزرسانی‌های نظرسنجی (polling) را
کنترل می‌کند.

هنگامی که فهرست نهایی‌کننده‌ها خالی شود، یعنی همهٔ نهایی‌کننده‌ها اجرا شده باشند، کوبرنتیز منبع را
حذف می‌کند.

### اعتبارسنجی

منابع سفارشی با استفاده از
[OpenAPI v3.0 schemas](https://github.com/OAI/OpenAPI-Specification/blob/3.0.0/versions/3.0.0.md#schema-object)
اعتبارسنجی می‌شوند. اگر [قابلیت قواعد اعتبارسنجی](#validation-rules) فعال باشد، اعتبارسنجی با x-kubernetes-validations نیز انجام می‌شود. همچنین می‌توانید با استفاده از
[وب‌هوک‌های پذیرش (admission webhooks)](/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)
اعتبارسنجی‌های بیشتری اضافه کنید.

افزون بر این، محدودیت‌های زیر بر schema اعمال می‌شوند:

- فیلدهای زیر را نمی‌توان تنظیم کرد:

  - `definitions`,
  - `dependencies`,
  - `deprecated`,
  - `discriminator`,
  - `id`,
  - `patternProperties`,
  - `readOnly`,
  - `writeOnly`,
  - `xml`,
  - `$ref`.

- فیلد `uniqueItems` را نمی‌توان روی `true` تنظیم کرد.
- فیلد `additionalProperties` را نمی‌توان روی `false` تنظیم کرد.
- فیلد `additionalProperties` با `properties` مانعهٔ‌الجمع است و نمی‌توان هر دو را با هم به کار برد.

اگر قابلیت [قواعد اعتبارسنجی](#validation-rules) فعال باشد و schema آبجکت CustomResourceDefinition یک
[schema ساختاری (structural schema)](#specifying-a-structural-schema) باشد، می‌توان از افزونهٔ `x-kubernetes-validations` برای اعتبارسنجی منابع سفارشی با عبارت‌های
[Common Expression Language (CEL)](https://github.com/google/cel-spec) استفاده کرد.

برای آشنایی با سایر محدودیت‌ها و قابلیت‌های CustomResourceDefinition، به بخش
[schemaهای ساختاری](#specifying-a-structural-schema) مراجعه کنید.

این schema در CustomResourceDefinition تعریف می‌شود. در مثال زیر، CustomResourceDefinition اعتبارسنجی‌های زیر را بر آبجکت سفارشی اعمال می‌کند:

- فیلد `spec.cronSpec` باید رشته باشد و با الگوی توصیف‌شده در عبارت باقاعده (regular expression) مطابقت داشته باشد.
- فیلد `spec.replicas` باید عدد صحیح باشد و مقدار آن حداقل ۱ و حداکثر ۱۰ باشد.

این CustomResourceDefinition را در فایل `resourcedefinition.yaml` ذخیره کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        # openAPIV3Schema is the schema for validating custom objects.
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                  pattern: '^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$'
                image:
                  type: string
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 10
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

و آن را ایجاد کنید:

```shell
kubectl apply -f resourcedefinition.yaml
```

اگر فیلدهای یک آبجکت سفارشی از نوع CronTab مقادیر نامعتبر داشته باشند، درخواست ایجاد آن رد می‌شود.
در مثال زیر، آبجکت سفارشی فیلدهایی با مقادیر نامعتبر دارد:

- فیلد `spec.cronSpec` با عبارت باقاعده مطابقت ندارد.
- مقدار فیلد `spec.replicas` بیشتر از ۱۰ است.

اگر YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * *"
  image: my-awesome-cron-image
  replicas: 15
```

و بکوشید آن را ایجاد کنید:

```shell
kubectl apply -f my-crontab.yaml
```

با خطای زیر روبه‌رو می‌شوید:

```console
The CronTab "my-new-cron-object" is invalid: []: Invalid value: map[string]interface {}{"apiVersion":"stable.example.com/v1", "kind":"CronTab", "metadata":map[string]interface {}{"name":"my-new-cron-object", "namespace":"default", "deletionTimestamp":interface {}(nil), "deletionGracePeriodSeconds":(*int64)(nil), "creationTimestamp":"2017-09-05T05:20:07Z", "uid":"e14d79e7-91f9-11e7-a598-f0761cb232d1", "clusterName":""}, "spec":map[string]interface {}{"cronSpec":"* * * *", "image":"my-awesome-cron-image", "replicas":15}}:
validation failure list:
spec.cronSpec in body should match '^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$'
spec.replicas in body should be less than or equal to 10
```

اگر فیلدها مقادیر معتبر داشته باشند، درخواست ایجاد آبجکت پذیرفته می‌شود.

YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
  replicas: 5
```

و آن را ایجاد کنید:

```shell
kubectl apply -f my-crontab.yaml
crontab "my-new-cron-object" created
```
### رچتینگ اعتبارسنجی

{{< feature-state feature_gate_name="CRDValidationRatcheting" >}}

اگر از نسخه‌ای از کوبرنتیز قدیمی‌تر از v1.30 استفاده می‌کنید، برای بهره‌گیری از این رفتار باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام
`CRDValidationRatcheting` را به‌صراحت فعال کنید. در این صورت، این رفتار بر همهٔ CustomResourceDefinitionهای کلاستر شما اعمال می‌شود.

به شرط فعال بودن این feature gate، کوبرنتیز _رچتینگ اعتبارسنجی_ (validation ratcheting) را برای CustomResourceDefinitionها پیاده‌سازی می‌کند. در این حالت، سرور API به‌روزرسانی‌هایی را که منبع را پس از به‌روزرسانی نامعتبر باقی می‌گذارند می‌پذیرد، به این شرط که هیچ‌یک از بخش‌هایی از منبع که در اعتبارسنجی رد شده‌اند در عملیات به‌روزرسانی تغییر نکرده باشند. به بیان دیگر، هر بخش نامعتبری از منبع که همچنان نامعتبر می‌ماند باید از پیش نیز نادرست بوده باشد.
نمی‌توانید از این سازوکار برای به‌روزرسانی یک منبع معتبر به‌گونه‌ای استفاده کنید که نامعتبر شود.

این قابلیت به نویسندگان CRDها امکان می‌دهد در شرایطی مشخص، با اطمینان اعتبارسنجی‌های جدیدی به schema نوع OpenAPIV3 اضافه کنند. کاربران نیز می‌توانند بی‌آنکه نسخهٔ آبجکت را افزایش دهند یا روندهای کاری خود را مختل کنند، با خیال آسوده به schema جدید ارتقا یابند.

اگرچه بیشتر اعتبارسنجی‌هایی که در schema نوع OpenAPIV3 یک CRD تعریف می‌شوند از رچتینگ پشتیبانی می‌کنند، چند استثنا وجود دارد. در پیاده‌سازی کوبرنتیز {{< skew currentVersion >}}، اعتبارسنجی‌های زیر در schema نوع OpenAPIV3 از رچتینگ پشتیبانی نمی‌کنند و در صورت نقض شدن، مانند حالت عادی خطا تولید می‌کنند:

- کمیت‌نماها (Quantors)
  - `allOf`
  - `oneOf`
  - `anyOf`
  - `not`
  -  هر اعتبارسنجی در زیرشاخه‌های یکی از این فیلدها
- افزونهٔ `x-kubernetes-validations`
  در کوبرنتیز 1.28، [قواعد اعتبارسنجی](#validation-rules) CRD در رچتینگ نادیده گرفته می‌شوند. از نسخهٔ Alpha 2 در کوبرنتیز 1.29 به بعد، `x-kubernetes-validations` تنها در صورتی مشمول رچتینگ می‌شوند که به `oldSelf` ارجاع ندهند.

  قواعد گذار (Transition Rules) هرگز مشمول رچتینگ نمی‌شوند: تنها خطاهایی که قواعدِ بدون استفاده از `oldSelf` ایجاد می‌کنند، در صورت تغییر نکردن مقادیرشان، به‌طور خودکار مشمول رچتینگ می‌شوند.

  برای نوشتن منطق رچتینگ سفارشی برای عبارت‌های CEL، به بخش [optionalOldSelf](#field-optional-oldself) مراجعه کنید.
- افزونهٔ `x-kubernetes-list-type`
  خطاهای ناشی از تغییر نوع لیست در یک زیر‌schema مشمول رچتینگ نمی‌شوند. برای نمونه، افزودن `set` به لیستی که عناصر تکراری دارد همواره به خطا می‌انجامد.
- افزونهٔ `x-kubernetes-list-map-keys`
  خطاهای ناشی از تغییر کلیدهای map در schema یک لیست مشمول رچتینگ نمی‌شوند.
- فیلد `required`
  خطاهای ناشی از تغییر فهرست فیلدهای الزامی مشمول رچتینگ نمی‌شوند.
- فیلد `properties`
  افزودن، حذف یا تغییر نام ویژگی‌ها مشمول رچتینگ نمی‌شود، اما تغییر اعتبارسنجی‌ها در schema و زیر‌schemaهای هر ویژگی، در صورتی که نام آن ویژگی ثابت بماند، ممکن است مشمول رچتینگ شود.
- فیلد `additionalProperties`
  حذف اعتبارسنجی `additionalProperties` که پیش‌تر تعیین شده است مشمول رچتینگ نمی‌شود.
- فیلد `metadata`
  خطاهای ناشی از اعتبارسنجی داخلی کوبرنتیز روی `metadata` یک آبجکت (مانند نام آبجکت یا نویسه‌های موجود در مقدار یک برچسب) مشمول رچتینگ نمی‌شوند. اگر قواعد اضافی خودتان را برای metadata یک منبع سفارشی تعیین کنید، این اعتبارسنجی اضافی مشمول رچتینگ می‌شود.

### قواعد اعتبارسنجی

{{< feature-state state="stable" for_k8s_version="v1.29" >}}

قواعد اعتبارسنجی برای اعتبارسنجی مقادیر منابع سفارشی از [زبان عبارت مشترک (Common Expression Language یا CEL)](https://github.com/google/cel-spec) استفاده می‌کنند. این قواعد با افزونهٔ `x-kubernetes-validations` در طرح‌واره‌های (schema) CustomResourceDefinition قرار می‌گیرند.

محدودهٔ هر قاعده همان جایی از طرح‌واره است که افزونهٔ `x-kubernetes-validations` در آن قرار دارد. متغیر `self` در عبارت CEL نیز به مقدارِ همین محدوده متصل می‌شود.

محدودهٔ همهٔ قواعد اعتبارسنجی به آبجکت فعلی محدود است؛ قواعد اعتبارسنجی میان‌آبجکتی یا حالت‌مند (stateful) پشتیبانی نمی‌شوند.

برای نمونه:

```yaml
  # ...
  openAPIV3Schema:
    type: object
    properties:
      spec:
        type: object
        x-kubernetes-validations:
          - rule: "self.minReplicas <= self.replicas"
            message: "replicas should be greater than or equal to minReplicas."
          - rule: "self.replicas <= self.maxReplicas"
            message: "replicas should be smaller than or equal to maxReplicas."
        properties:
          # ...
          minReplicas:
            type: integer
          replicas:
            type: integer
          maxReplicas:
            type: integer
        required:
          - minReplicas
          - replicas
          - maxReplicas
```

درخواست ایجاد منبع سفارشی زیر را رد می‌کند:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  minReplicas: 0
  replicas: 20
  maxReplicas: 10
```

و این پاسخ را برمی‌گرداند:

```
The CronTab "my-new-cron-object" is invalid:
* spec: Invalid value: map[string]interface {}{"maxReplicas":10, "minReplicas":0, "replicas":20}: replicas should be smaller than or equal to maxReplicas.
```

افزونهٔ `x-kubernetes-validations` می‌تواند چند قاعده داشته باشد. کلید `rule` زیر `x-kubernetes-validations` عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند. کلید `message` پیامی است که هنگام شکست اعتبارسنجی نمایش داده می‌شود. اگر پیامی تنظیم نشده باشد، پاسخ بالا چنین خواهد بود:

```
The CronTab "my-new-cron-object" is invalid:
* spec: Invalid value: map[string]interface {}{"maxReplicas":10, "minReplicas":0, "replicas":20}: failed rule: self.replicas <= self.maxReplicas
```

{{< note >}}
می‌توانید عبارت‌های CEL را به‌سرعت در [CEL Playground](https://playcel.undistro.io) آزمایش کنید.
{{< /note >}}

قواعد اعتبارسنجی هنگام ایجاد یا به‌روزرسانی CRDها کامپایل می‌شوند. اگر کامپایل قواعد اعتبارسنجی با شکست روبه‌رو شود، درخواست ایجاد یا به‌روزرسانی CRD نیز شکست می‌خورد. فرایند کامپایل شامل بررسی نوع‌ها نیز هست.

خطاهای کامپایل:

- `no_matching_overload`: این تابع هیچ سربارگذاری (overload) متناسب با نوع آرگومان‌ها ندارد.

  برای نمونه، قاعده‌ای مانند `self == true` روی فیلدی از نوع عدد صحیح این خطا را می‌دهد:

  ```none
  Invalid value: apiextensions.ValidationRule{Rule:"self == true", Message:""}: compilation failed: ERROR: \<input>:1:6: found no matching overload for '_==_' applied to '(int, bool)'
  ```

- `no_such_field`: فیلد مورد نظر وجود ندارد.

  برای نمونه، قاعده‌ای مانند `self.nonExistingField > 0` روی فیلدی ناموجود خطای زیر را برمی‌گرداند:

  ```none
  Invalid value: apiextensions.ValidationRule{Rule:"self.nonExistingField > 0", Message:""}: compilation failed: ERROR: \<input>:1:5: undefined field 'nonExistingField'
  ```

- `invalid argument`: آرگومان نامعتبر برای ماکروها.

  برای نمونه، قاعده‌ای مانند `has(self)` این خطا را برمی‌گرداند:

  ```none
  Invalid value: apiextensions.ValidationRule{Rule:"has(self)", Message:""}: compilation failed: ERROR: <input>:1:4: invalid argument to has() macro
  ```

نمونه‌هایی از قواعد اعتبارسنجی:

| قاعده                                                                             | هدف                                                                           |
| ----------------                                                                 | ------------                                                                      |
| `self.minReplicas <= self.replicas && self.replicas <= self.maxReplicas`         | بررسی اینکه سه فیلدِ تعریف‌کنندهٔ replicas به‌ترتیب درستی باشند        |
| `'Available' in self.stateCounts`                                                | بررسی اینکه مدخلی با کلید 'Available' در یک نگاشت (map) وجود داشته باشد                   |
| `(size(self.list1) == 0) != (size(self.list2) == 0)`                             | بررسی اینکه یکی از دو فهرست خالی نباشد، اما نه هر دو                         |
| <code>!('MY_KEY' in self.map1) &#124;&#124; self['MY_KEY'].matches('^[a-zA-Z]*$')</code>               | اعتبارسنجی مقدارِ یک کلید مشخص در نگاشت، در صورتی که آن کلید در نگاشت وجود داشته باشد               |
| `self.envars.filter(e, e.name == 'MY_ENV').all(e, e.value.matches('^[a-zA-Z]*$')` | اعتبارسنجی فیلد 'value' در مدخلی از listMap که فیلد کلیدی 'name' آن برابر 'MY_ENV' است  |
| `has(self.expired) && self.created + self.ttl < self.expired`                    | بررسی اینکه تاریخ 'expired' پس از تاریخ 'create' به‌اضافهٔ مدت 'ttl' باشد       |
| `self.health.startsWith('ok')`                                                   | بررسی اینکه فیلد رشته‌ای 'health' با پیشوند 'ok' شروع شود                              |
| `self.widgets.exists(w, w.key == 'x' && w.foo < 10)`                             | بررسی اینکه ویژگی 'foo' در عضوی از listMap با کلید 'x' کمتر از 10 باشد |
| `type(self) == string ? self == '100%' : self == 1000`                           | اعتبارسنجی فیلدی از نوع int-or-string در هر دو حالت عدد صحیح و رشته             |
| `self.metadata.name.startsWith(self.prefix)`                                     | بررسی اینکه نام آبجکت با مقدار فیلدی دیگر به‌عنوان پیشوند شروع شود              |
| `self.set1.all(e, !(e in self.set2))`                                            | بررسی اینکه دو listSet هیچ عضو مشترکی نداشته باشند                                           |
| `size(self.names) == size(self.details) && self.names.all(n, n in self.details)` | بررسی اینکه کلیدهای نگاشت 'details' همان اعضای listSet با نام 'names' باشند           |
| `size(self.clusters.filter(c, c.name == self.primary)) == 1`                     | بررسی اینکه ویژگی 'primary' دقیقاً یک بار در listMap با نام 'clusters' آمده باشد           |

همچنین ببینید: [ارزیابی پشتیبانی‌شده در CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#evaluation)

- اگر محدودهٔ قاعده ریشهٔ یک منبع باشد، می‌توان در آن هر یک از فیلدهای اعلام‌شده در طرح‌وارهٔ OpenAPIv3 مربوط به CRD و همچنین `apiVersion`، `kind`، `metadata.name` و `metadata.generateName` را انتخاب کرد. این شامل انتخاب فیلدها از هر دو بخش `spec` و `status` در یک عبارت واحد نیز می‌شود:

  ```yaml
    # ...
    openAPIV3Schema:
      type: object
      x-kubernetes-validations:
        - rule: "self.status.availableReplicas >= self.spec.minReplicas"
      properties:
          spec:
            type: object
            properties:
              minReplicas:
                type: integer
              # ...
          status:
            type: object
            properties:
              availableReplicas:
                type: integer
  ```

- اگر محدودهٔ قاعده آبجکتی دارای ویژگی (property) باشد، ویژگی‌های در دسترس آن آبجکت را می‌توان با `self.field` انتخاب کرد و وجود فیلد را با `has(self.field)` بررسی کرد. در عبارت‌های CEL، فیلدهایی که مقدارشان null است فیلدهای غایب به شمار می‌آیند.

  ```yaml
    # ...
    openAPIV3Schema:
      type: object
      properties:
        spec:
          type: object
          x-kubernetes-validations:
            - rule: "has(self.foo)"
          properties:
            # ...
            foo:
              type: integer
  ```

- اگر محدودهٔ قاعده آبجکتی دارای additionalProperties (یعنی یک نگاشت) باشد، مقادیر نگاشت از طریق `self[mapKey]` در دسترس‌اند، وجود کلید در نگاشت را می‌توان با `mapKey in self` بررسی کرد و به همهٔ مدخل‌های نگاشت می‌توان با ماکروها و توابع CEL مانند `self.all(...)` دسترسی داشت.

  ```yaml
    # ...
    openAPIV3Schema:
      type: object
      properties:
        spec:
          type: object
          x-kubernetes-validations:
            - rule: "self['xyz'].foo > 0"
          additionalProperties:
            # ...
            type: object
            properties:
              foo:
                type: integer
  ```

- اگر محدودهٔ قاعده یک آرایه باشد، عناصر آرایه از طریق `self[i]` و همچنین با ماکروها و توابع در دسترس‌اند.

  ```yaml
    # ...
    openAPIV3Schema:
      type: object
      properties:
        # ...
        foo:
          type: array
          x-kubernetes-validations:
            - rule: "size(self) == 1"
          items:
            type: string
  ```

- اگر محدودهٔ قاعده یک مقدار نرده‌ای (scalar) باشد، `self` به همان مقدار نرده‌ای متصل می‌شود.

  ```yaml
    # ...
    openAPIV3Schema:
      type: object
      properties:
        spec:
          type: object
          properties:
            # ...
            foo:
              type: integer
              x-kubernetes-validations:
              - rule: "self > 0"
  ```

نمونه‌ها:

|نوع فیلدی که محدودهٔ قاعده است    | نمونهٔ قاعده             |
| -----------------------| -----------------------|
| آبجکت ریشه            | `self.status.actual <= self.spec.maxDesired` |
| نگاشتی از آبجکت‌ها         | `self.components['Widget'].priority < 10` |
| فهرستی از اعداد صحیح       | `self.values.all(value, value >= 0 && value < 100)` |
| رشته                 | `self.startsWith('kube')` |


فیلدهای `apiVersion`، `kind`، `metadata.name` و `metadata.generateName` همیشه از ریشهٔ آبجکت و از هر آبجکتی که با `x-kubernetes-embedded-resource` حاشیه‌نویسی شده باشد در دسترس‌اند. هیچ ویژگی دیگری از metadata در دسترس نیست.

داده‌های ناشناخته‌ای که با `x-kubernetes-preserve-unknown-fields` در منابع سفارشی حفظ می‌شوند، در عبارت‌های CEL در دسترس نیستند. این موارد عبارت‌اند از:

- مقادیر فیلدهای ناشناخته‌ای که طرح‌واره‌های آبجکت دارای `x-kubernetes-preserve-unknown-fields` آن‌ها را حفظ می‌کنند.
- ویژگی‌هایی از آبجکت که طرح‌وارهٔ آن‌ها از «نوع ناشناخته» است. «نوع ناشناخته» به‌صورت بازگشتی چنین تعریف می‌شود:

  - طرح‌واره‌ای بدون نوع که x-kubernetes-preserve-unknown-fields در آن برابر true است
  - آرایه‌ای که طرح‌وارهٔ اعضای آن (items) از «نوع ناشناخته» است
  - آبجکتی که طرح‌وارهٔ additionalProperties آن از «نوع ناشناخته» است


فقط نام ویژگی‌هایی به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس‌اند. نام ویژگی‌های در دسترس، هنگام استفاده در عبارت، طبق قواعد زیر گریزداده (escape) می‌شوند:

| دنبالهٔ گریز         | نام ویژگی معادل  |
| ----------------------- | -----------------------|
| `__underscores__`       | `__`                  |
| `__dot__`               | `.`                   |
|`__dash__`               | `-`                   |
| `__slash__`             | `/`                   |
| `__{keyword}__`         | [کلیدواژهٔ رزروشدهٔ CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#syntax)       |

نکته: کلیدواژهٔ رزروشدهٔ CEL فقط زمانی گریزداده می‌شود که دقیقاً با نام ویژگی منطبق باشد (برای نمونه، int در واژهٔ sprint گریزداده نمی‌شود).

نمونه‌هایی از گریزدادن:

|نام ویژگی    | قاعده با نام ویژگی گریزداده‌شده     |
| ----------------| -----------------------             |
| namespace       | `self.__namespace__ > 0`            |
| x-prop          | `self.x__dash__prop > 0`            |
| redact__d       | `self.redact__underscores__d > 0`   |
| string          | `self.startsWith('kube')`           |


در آرایه‌هایی که `x-kubernetes-list-type` آن‌ها `set` یا `map` است، مقایسهٔ برابری ترتیب عناصر را نادیده می‌گیرد؛ یعنی `[1, 2] == [2, 1]`. الحاق آرایه‌هایی که x-kubernetes-list-type دارند از معناشناسی همان نوع فهرست پیروی می‌کند:

- `set`: عبارت `X + Y` اجتماعی انجام می‌دهد که در آن جایگاه همهٔ عناصر `X` در آرایه حفظ می‌شود و عناصرِ غیرمشترکِ `Y` با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.

- `map`: عبارت `X + Y` ادغامی انجام می‌دهد که در آن جایگاه همهٔ کلیدهای `X` در آرایه حفظ می‌شود، اما هنگامی که مجموعه‌کلیدهای `X` و `Y` اشتراک داشته باشند، مقادیر با مقادیر `Y` بازنویسی می‌شوند. عناصرِ `Y` که کلیدهای غیرمشترک دارند، با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.


نگاشت نوع‌های OpenAPIv3 به نوع‌های CEL به این صورت است:

| نوع OpenAPIv3                                     | نوع CEL                                                                                                                     |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 'object' با Properties                           | object / "message type"                                                                                                      |
| 'object' با AdditionalProperties                 | map                                                                                                                          |
| 'object' با x-kubernetes-embedded-type           | object / "message type"؛ 'apiVersion'، 'kind'، 'metadata.name' و 'metadata.generateName' به‌طور ضمنی در طرح‌واره گنجانده می‌شوند |
| 'object' با x-kubernetes-preserve-unknown-fields | object / "message type"؛ فیلدهای ناشناخته در عبارت CEL در دسترس نیستند                                                 |
| x-kubernetes-int-or-string                         | آبجکت پویایی که یا int است یا string؛ برای بررسی نوع می‌توان از `type(value)` استفاده کرد                                |
| 'array                                             | list                                                                                                                         |
| 'array' با x-kubernetes-list-type=map            | list با برابری مبتنی بر map و تضمین یکتایی کلیدها                                                                         |
| 'array' با x-kubernetes-list-type=set            | list با برابری مبتنی بر set و تضمین یکتایی مدخل‌ها                                                                       |
| 'boolean'                                          | boolean                                                                                                                      |
| 'number' (همهٔ قالب‌ها)                             | double                                                                                                                       |
| 'integer' (همهٔ قالب‌ها)                            | int (64)                                                                                                                     |
| 'null'                                             | null_type                                                                                                                    |
| 'string'                                           | string                                                                                                                       |
| 'string' با format=byte (کدگذاری‌شده با base64)         | bytes                                                                                                                        |
| 'string' با format=date                          | timestamp (google.protobuf.Timestamp)                                                                                        |
| 'string' با format=datetime                      | timestamp (google.protobuf.Timestamp)                                                                                        |
| 'string' با format=duration                      | duration (google.protobuf.Duration)                                                                                          |

همچنین ببینید: [نوع‌های CEL](https://github.com/google/cel-spec/blob/v0.6.0/doc/langdef.md#values)،
[نوع‌های OpenAPI](https://swagger.io/specification/#data-types)،
[طرح‌واره‌های ساختاری کوبرنتیز](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#specifying-a-structural-schema).

#### فیلد messageExpression

فیلد `messageExpression` نیز مانند فیلد `message` که رشتهٔ گزارش‌شده هنگام شکست یک قاعدهٔ اعتبارسنجی را تعریف می‌کند، به کار می‌رود، با این تفاوت که به شما امکان می‌دهد رشتهٔ پیام را با یک عبارت CEL بسازید. به این ترتیب می‌توانید اطلاعات توصیفی‌تری در پیام شکست اعتبارسنجی بگنجانید. حاصل ارزیابی `messageExpression` باید یک رشته باشد و این عبارت می‌تواند از همان متغیرهایی استفاده کند که در فیلد `rule` در دسترس‌اند. برای نمونه:

```yaml
x-kubernetes-validations:
- rule: "self.x <= self.maxLimit"
  messageExpression: '"x exceeded max limit of " + string(self.maxLimit)'
```

توجه کنید که الحاق رشته در CEL (عملگر `+`) به‌طور خودکار مقدار را به رشته تبدیل نمی‌کند. اگر مقدار نرده‌ای غیررشته‌ای دارید، همان‌طور که در نمونهٔ بالا آمده است، با تابع `string(<value>)` آن را به رشته تبدیل کنید.

حاصل ارزیابی `messageExpression` باید یک رشته باشد و این موضوع هنگام نوشتن CRD بررسی می‌شود. توجه کنید که می‌توان `message` و `messageExpression` را در یک قاعده هم‌زمان تنظیم کرد؛ در این صورت از `messageExpression` استفاده می‌شود. با این حال، اگر ارزیابی `messageExpression` به خطا بینجامد، به‌جای آن از رشتهٔ تعریف‌شده در `message` استفاده می‌شود و خطای `messageExpression` در لاگ ثبت می‌شود. اگر عبارت CEL تعریف‌شده در `messageExpression` رشته‌ای خالی یا رشته‌ای دارای شکست خط تولید کند نیز همین جایگزینی رخ می‌دهد.

اگر یکی از شرایط بالا برقرار باشد و هیچ `message` تنظیم نشده باشد، به‌جای آن از پیام پیش‌فرض شکست اعتبارسنجی استفاده می‌شود.

از آنجا که `messageExpression` یک عبارت CEL است، محدودیت‌های فهرست‌شده در [مصرف منابع توسط توابع اعتبارسنجی](#resource-use-by-validation-functions) در مورد آن نیز صدق می‌کند. اگر ارزیابی در حین اجرای `messageExpression` به دلیل محدودیت منابع متوقف شود، هیچ قاعدهٔ اعتبارسنجی دیگری اجرا نخواهد شد.

تنظیم `messageExpression` اختیاری است.

#### فیلد `message` {#field-message}

اگر می‌خواهید پیامی ثابت تنظیم کنید، می‌توانید به‌جای `messageExpression` از `message` استفاده کنید. در صورت شکست اعتبارسنجی، مقدار `message` به‌عنوان یک رشتهٔ خطای مبهم (opaque) به کار می‌رود.

تنظیم `message` اختیاری است.

#### فیلد `reason` {#field-reason}

می‌توانید در یک `validation` دلیلی ماشین‌خوان برای شکست اعتبارسنجی اضافه کنید تا هر بار که درخواستی این قاعدهٔ اعتبارسنجی را نقض کرد، بازگردانده شود.

برای نمونه:

```yaml
x-kubernetes-validations:
- rule: "self.x <= self.maxLimit"
  reason: "FieldValueInvalid"
```

کد وضعیت HTTP که به فراخواننده بازگردانده می‌شود، با دلیلِ نخستین قاعدهٔ اعتبارسنجیِ شکست‌خورده مطابقت دارد. دلایلی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از: "FieldValueInvalid"، "FieldValueForbidden"، "FieldValueRequired" و "FieldValueDuplicate". اگر دلیلی تنظیم نشده باشد یا دلیل ناشناخته باشد، به‌طور پیش‌فرض از "FieldValueInvalid" استفاده می‌شود.

تنظیم `reason` اختیاری است.

#### فیلد `fieldPath` {#field-field-path}

می‌توانید مسیر فیلدی را که هنگام شکست اعتبارسنجی بازگردانده می‌شود، مشخص کنید.

برای نمونه:

```yaml
x-kubernetes-validations:
- rule: "self.foo.test.x <= self.maxLimit"
  fieldPath: ".foo.test.x"
```

در نمونهٔ بالا، اعتبارسنجی بررسی می‌کند که مقدار فیلد `x` کمتر از مقدار `maxLimit` باشد. اگر هیچ `fieldPath` مشخص نشده باشد، هنگام شکست اعتبارسنجی، مسیر فیلد به‌طور پیش‌فرض همان جایی خواهد بود که `self` به آن محدود شده است. با مشخص کردن `fieldPath`، خطای بازگردانده‌شده در `fieldPath` به‌درستی به محل فیلد `x` اشاره خواهد کرد.

مقدار `fieldPath` باید یک مسیر JSON نسبی باشد که محدوده‌اش محل همین افزونهٔ x-kubernetes-validations در طرح‌واره است. افزون بر این، باید به فیلدی موجود در طرح‌واره اشاره کند. برای نمونه، هنگامی که اعتبارسنجی یک ویژگی مشخص `foo` را زیر نگاشت `testMap` بررسی می‌کند، می‌توانید `fieldPath` را برابر `".testMap.foo"` یا `.testMap['foo']'` قرار دهید. اگر اعتبارسنجی نیازمند بررسی یکتایی ویژگی‌ها در دو فهرست باشد، می‌توان fieldPath را روی هر یک از این دو فهرست تنظیم کرد؛ برای نمونه، می‌توان آن را برابر `.testList1` یا `.testList2` قرار داد. در حال حاضر، این فیلد از عملیات فرزند برای اشاره به یک فیلد موجود پشتیبانی می‌کند. برای اطلاعات بیشتر به [پشتیبانی از JSONPath در کوبرنتیز](/docs/reference/kubectl/jsonpath/) مراجعه کنید. فیلد `fieldPath` از اندیس‌گذاری عددی آرایه‌ها پشتیبانی نمی‌کند.

تنظیم `fieldPath` اختیاری است.

#### فیلد `optionalOldSelf` {#field-optional-oldself}

{{< feature-state feature_gate_name="CRDValidationRatcheting" >}}

اگر [اعتبارسنجی تدریجی (ratcheting) CRD](#validation-ratcheting) در کلاستر شما فعال نباشد، API مربوط به CustomResourceDefinition این فیلد را شامل نمی‌شود و تلاش برای تنظیم آن ممکن است به خطا بینجامد.

فیلد `optionalOldSelf` یک فیلد بولی است که رفتار [قواعد گذار](#transition-rules) را که در ادامه شرح داده می‌شوند، تغییر می‌دهد. در حالت عادی، اگر نتوان `oldSelf` را تعیین کرد، قاعدهٔ گذار ارزیابی نمی‌شود؛ یعنی هنگام ایجاد آبجکت یا وقتی مقدار جدیدی در یک به‌روزرسانی اضافه می‌شود.

اگر `optionalOldSelf` برابر true باشد، قواعد گذار همیشه ارزیابی می‌شوند و نوع `oldSelf` به نوع [`Optional`](https://pkg.go.dev/github.com/google/cel-go/cel#OptionalTypes) در CEL تغییر می‌کند.

فیلد `optionalOldSelf` در مواردی سودمند است که نویسندگان طرح‌واره ابزار کنترلی قوی‌تر [از رفتار پیش‌فرض مبتنی بر برابری](#validation-ratcheting) بخواهند تا محدودیت‌های جدیدتر و معمولاً سخت‌گیرانه‌تری را بر مقادیر جدید اعمال کنند و در عین حال اجازه دهند مقادیر قدیمی با اعتبارسنجی قدیمی‌تر همچنان معتبر بمانند (grandfathered) یا به‌صورت تدریجی اعتبارسنجی شوند.

نمونهٔ کاربرد:

| CEL                                     | توضیح |
|-----------------------------------------|-------------|
| <code>self.foo == "foo" &#124;&#124; (oldSelf.hasValue() && oldSelf.value().foo != "foo")</code> | قاعدهٔ تدریجی. هنگامی که مقداری برابر "foo" شد، باید همان foo باقی بماند. اما اگر این مقدار پیش از اعمال محدودیت "foo" وجود داشته است، می‌تواند هر مقداری داشته باشد |
| <code>[oldSelf.orValue(""), self].all(x, ["OldCase1", "OldCase2"].exists(case, x == case)) &#124;&#124; ["NewCase1", "NewCase2"].exists(case, self == case) &#124;&#124; ["NewCase"].has(self)</code> | «اعتبارسنجی تدریجی برای حالت‌های حذف‌شدهٔ enum، در صورتی که oldSelf از آن‌ها استفاده کرده باشد» |
| <code>oldSelf.optMap(o, o.size()).orValue(0) < 4 &#124;&#124; self.size() >= 4</code> | اعتبارسنجی تدریجی برای حداقل اندازهٔ تازه افزایش‌یافتهٔ نگاشت یا فهرست |


#### توابع اعتبارسنجی {#available-validation-functions}

توابع در دسترس عبارت‌اند از:

- توابع استاندارد CEL که در [فهرست تعاریف استاندارد](https://github.com/google/cel-spec/blob/v0.7.0/doc/langdef.md#list-of-standard-definitions) تعریف شده‌اند
- [ماکروهای](https://github.com/google/cel-spec/blob/v0.7.0/doc/langdef.md#macros) استاندارد CEL
- [کتابخانهٔ توابع رشته‌ای گسترش‌یافتهٔ](https://pkg.go.dev/github.com/google/cel-go@v0.11.2/ext#Strings) CEL
- [کتابخانهٔ افزونهٔ CEL](https://pkg.go.dev/k8s.io/apiextensions-apiserver@v0.24.0/pkg/apiserver/schema/cel/library#pkg-functions) در کوبرنتیز

#### قواعد گذار

قاعده‌ای که عبارتش به شناسهٔ `oldSelf` ارجاع می‌دهد، به‌طور ضمنی یک _قاعدهٔ گذار_ (transition rule) به شمار می‌آید. با قواعد گذار، نویسندگان طرح‌واره می‌توانند از برخی گذارها میان دو حالتی که هر کدام به‌تنهایی معتبرند، جلوگیری کنند. برای نمونه:

```yaml
type: string
enum: ["low", "medium", "high"]
x-kubernetes-validations:
- rule: "!(self == 'high' && oldSelf == 'low') && !(self == 'low' && oldSelf == 'high')"
  message: cannot transition directly between 'low' and 'high'
```

برخلاف سایر قواعد، قواعد گذار فقط بر عملیاتی اعمال می‌شوند که معیارهای زیر را داشته باشند:

- عملیات باید یک آبجکت موجود را به‌روزرسانی کند. قواعد انتقال هرگز بر عملیات ایجاد اعمال نمی‌شوند.

- هم مقدار قدیمی و هم مقدار جدید باید وجود داشته باشند. با قرار دادن یک قاعدهٔ انتقال روی گرهٔ والد، همچنان می‌توان بررسی کرد که مقداری اضافه یا حذف شده است یا نه. قواعد انتقال هرگز هنگام ایجاد منبع سفارشی اعمال نمی‌شوند. اگر قاعدهٔ انتقال روی یک فیلد اختیاری قرار گیرد، بر عملیات به‌روزرسانی‌ای که آن فیلد را مقداردهی یا حذف می‌کند اعمال نمی‌شود.

- مسیر گرهٔ طرح‌واره (schema) که قاعدهٔ انتقال آن را اعتبارسنجی می‌کند باید به گره‌ای برسد که میان آبجکت قدیمی و آبجکت جدید قابل مقایسه باشد. برای مثال، آیتم‌های فهرست و زیرشاخه‌های آن‌ها (`spec.foo[10].bar`) را لزوماً نمی‌توان میان یک آبجکت موجود و به‌روزرسانی بعدی همان آبجکت متناظر کرد.

اگر یک گرهٔ طرح‌واره شامل قاعدهٔ انتقالی باشد که هرگز نمی‌تواند اعمال شود، هنگام نوشتن CRD خطا تولید می‌شود؛ برای نمونه: "oldSelf cannot be used on the uncorrelatable portion of the schema within *path*".

قواعد انتقال فقط روی _بخش‌های همبسته‌پذیر_ (correlatable portions) طرح‌واره مجاز هستند.
بخشی از طرح‌واره زمانی همبسته‌پذیر است که همهٔ طرح‌واره‌های والدِ از نوع `array` دارای `x-kubernetes-list-type=map` باشند؛
وجود هر طرح‌وارهٔ والدِ آرایه‌ای از نوع `set` یا `atomic` باعث می‌شود نتوان `self` را بدون ابهام با `oldSelf` متناظر کرد.

در ادامه چند نمونه از قواعد انتقال آمده است:

{{< table caption="نمونه‌هایی از قواعد انتقال" >}}
| مورد استفاده                                                          | قاعده
| --------                                                          | --------
| تغییرناپذیری                                                      | `self.foo == oldSelf.foo`
| جلوگیری از تغییر یا حذف پس از مقداردهی                        | `oldSelf != 'bar' \|\| self == 'bar'` یا `!has(oldSelf.field) \|\| has(self.field)`
| مجموعهٔ فقط‌افزودنی                                                   | `self.all(element, element in oldSelf)`
| اگر مقدار قبلی X بوده است، مقدار جدید فقط می‌تواند A یا B باشد، نه Y یا Z | `oldSelf != 'X' \|\| self in ['A', 'B']`
| شمارنده‌های یکنوا (غیرنزولی)                               | `self >= oldSelf`
{{< /table >}}

#### مصرف منابع در توابع اعتبارسنجی

هنگامی که یک CustomResourceDefinition دارای قواعد اعتبارسنجی را ایجاد یا به‌روزرسانی می‌کنید،
سرور API تأثیر احتمالی اجرای این قواعد را بررسی می‌کند. اگر برآورد شود که اجرای یک قاعده بیش از حد پرهزینه است،
سرور API عملیات ایجاد یا به‌روزرسانی را رد می‌کند و یک پیام خطا برمی‌گرداند.
سازوکار مشابهی نیز در زمان اجرا وجود دارد که اقدامات مفسر را زیر نظر می‌گیرد. اگر مفسر دستورالعمل‌های بیش از حدی اجرا کند،
اجرای قاعده متوقف می‌شود و خطا رخ می‌دهد.
برای هر CustomResourceDefinition نیز مقدار مشخصی منبع جهت اجرای کامل همهٔ قواعد اعتبارسنجی‌اش در نظر گرفته شده است.
اگر در زمان ایجاد برآورد شود که مجموع هزینهٔ قواعد آن از این حد فراتر می‌رود، باز هم خطای اعتبارسنجی رخ می‌دهد.

اگر فقط قواعدی تعریف کنید که صرف‌نظر از اندازهٔ ورودی، همواره زمان یکسانی برای اجرا لازم دارند،
بعید است با محدودیت بودجهٔ منابع اعتبارسنجی به مشکل بربخورید.
برای مثال، قاعده‌ای که شرط `self.foo == 1` را بررسی می‌کند، به‌تنهایی هیچ
خطری از بابت رد شدن به دلیل بودجهٔ منابع اعتبارسنجی ندارد.
اما اگر `foo` یک رشته باشد و قاعدهٔ اعتبارسنجی `self.foo.contains("someString")` را تعریف کنید، زمان اجرای این قاعده
به طول `foo` بستگی دارد و ممکن است طولانی‌تر شود.
نمونهٔ دیگر حالتی است که `foo` یک آرایه باشد و قاعدهٔ اعتبارسنجی `self.foo.all(x, x > 5)` را تعیین کنید.
اگر محدودیتی برای طول `foo` مشخص نشده باشد، سامانهٔ برآورد هزینه همواره بدترین حالت ممکن را فرض می‌کند،
و این موضوع برای هر چیزی که بتوان روی آن پیمایش کرد (فهرست‌ها، نگاشت‌ها و غیره) صادق است.

به همین دلیل، بهترین روش این است که برای هر چیزی که در یک قاعدهٔ اعتبارسنجی پردازش می‌شود، با استفاده از `maxItems`، `maxProperties` و
`maxLength` محدودیت تعیین کنید تا هنگام برآورد هزینه با خطای اعتبارسنجی مواجه نشوید.
برای مثال، این طرح‌واره را با یک قاعده در نظر بگیرید:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      items:
        type: string
      x-kubernetes-validations:
        - rule: "self.all(x, x.contains('a string'))"
```

در این حالت، سرور API این قاعده را به دلیل بودجهٔ اعتبارسنجی رد می‌کند و این خطا را برمی‌گرداند:

```
spec.validation.openAPIV3Schema.properties[spec].properties[foo].x-kubernetes-validations[0].rule: Forbidden:
CEL rule exceeded budget by more than 100x (try simplifying the rule, or adding maxItems, maxProperties, and
maxLength where arrays, maps, and strings are used)
```

علت رد شدن این است که `self.all` به معنای فراخوانی `contains()` روی تک‌تک رشته‌های `foo` است
و این تابع نیز به نوبهٔ خود هر رشته را بررسی می‌کند تا ببیند `'a string'` را در بر دارد یا نه. بدون تعیین محدودیت،
این قاعده بسیار پرهزینه است.

اگر هیچ محدودیت اعتبارسنجی‌ای تعیین نکنید، هزینهٔ برآوردشدهٔ این قاعده از سقف هزینهٔ هر قاعده
فراتر می‌رود. اما اگر در جاهای مناسب محدودیت اضافه کنید، این قاعده پذیرفته می‌شود:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      maxItems: 25
      items:
        type: string
        maxLength: 10
      x-kubernetes-validations:
        - rule: "self.all(x, x.contains('a string'))"
```

سامانهٔ برآورد هزینه علاوه بر هزینهٔ برآوردشدهٔ خود قاعده، تعداد دفعات اجرای آن را نیز در نظر می‌گیرد.
برای نمونه، هزینهٔ برآوردشدهٔ قاعدهٔ زیر با نمونهٔ قبلی برابر است
(با اینکه این بار قاعده روی تک‌تک آیتم‌های آرایه تعریف شده است):

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      maxItems: 25
      items:
        type: string
        x-kubernetes-validations:
          - rule: "self.contains('a string'))"
        maxLength: 10
```

اگر فهرستی که درون یک فهرست دیگر قرار دارد قاعدهٔ اعتبارسنجی‌ای داشته باشد که از `self.all` استفاده می‌کند، هزینهٔ آن
به‌مراتب بیشتر از یک فهرست غیرتودرتو با همان قاعده است. قاعده‌ای که روی یک فهرست غیرتودرتو پذیرفته می‌شد، ممکن است
برای پذیرفته شدن نیاز داشته باشد که روی هر دو فهرست تودرتو محدودیت‌های کمتری تعیین شود. برای مثال، قاعدهٔ زیر
حتی بدون تعیین محدودیت پذیرفته می‌شود:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      items:
        type: integer
    x-kubernetes-validations:
      - rule: "self.all(x, x == 5)"
```

اما همین قاعده روی طرح‌وارهٔ زیر (که یک آرایهٔ تودرتو به آن اضافه شده است) خطای اعتبارسنجی ایجاد می‌کند:

```yaml
openAPIV3Schema:
  type: object
  properties:
    foo:
      type: array
      items:
        type: array
        items:
          type: integer
        x-kubernetes-validations:
          - rule: "self.all(x, x == 5)"
```

دلیل این است که هر آیتم `foo` خودش یک آرایه است و هر زیرآرایه نیز به نوبهٔ خود `self.all` را فراخوانی می‌کند.
در جاهایی که از قواعد اعتبارسنجی استفاده می‌شود، تا حد امکان از فهرست‌ها و نگاشت‌های تودرتو پرهیز کنید.

### مقداردهی پیش‌فرض

{{< note >}}
برای استفاده از مقداردهی پیش‌فرض، CustomResourceDefinition شما باید از نسخهٔ API `apiextensions.k8s.io/v1` استفاده کند.
{{< /note >}}

با مقداردهی پیش‌فرض (defaulting) می‌توانید مقادیر پیش‌فرض را در [طرح‌وارهٔ اعتبارسنجی OpenAPI v3](#validation) تعیین کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        # openAPIV3Schema is the schema for validating custom objects.
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                  pattern: '^(\d+|\*)(/\d+)?(\s+(\d+|\*)(/\d+)?){4}$'
                  default: "5 0 * * *"
                image:
                  type: string
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 10
                  default: 1
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

با این پیکربندی، هر دو فیلد `cronSpec` و `replicas` مقدار پیش‌فرض می‌گیرند؛ یعنی آبجکت زیر:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  image: my-awesome-cron-image
```

به این صورت درمی‌آید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "5 0 * * *"
  image: my-awesome-cron-image
  replicas: 1
```

مقداردهی پیش‌فرض روی آبجکت در این موارد انجام می‌شود:

* در درخواست ارسالی به سرور API، با استفاده از مقادیر پیش‌فرض نسخهٔ درخواست،
* هنگام خواندن از etcd، با استفاده از مقادیر پیش‌فرض نسخهٔ ذخیره‌سازی،
* پس از پلاگین‌های admission تغییردهنده (mutating) که patch غیرخالی دارند، با استفاده از مقادیر پیش‌فرض نسخهٔ آبجکت در webhook admission.

مقادیر پیش‌فرضی که هنگام خواندن داده از etcd اعمال می‌شوند، به‌طور خودکار در etcd بازنویسی نمی‌شوند.
برای ماندگار کردن این مقادیر پیش‌فرض در etcd، باید یک درخواست به‌روزرسانی از طریق API ارسال شود.

مقادیر پیش‌فرض فیلدهای غیربرگ باید هرس شوند (به‌جز مقادیر پیش‌فرض فیلدهای `metadata`) و باید
با طرح‌وارهٔ ارائه‌شده اعتبارسنجی شوند. برای مثال، در نمونهٔ بالا مقدار پیش‌فرض `{"replicas": "foo", "badger": 1}`
برای فیلد `spec` نامعتبر است، زیرا `badger` یک فیلد ناشناخته است و `replicas` رشته نیست.

مقادیر پیش‌فرض فیلدهای `metadata` در گره‌هایی که `x-kubernetes-embedded-resources: true` دارند (یا بخش‌هایی از
یک مقدار پیش‌فرض که `metadata` را پوشش می‌دهند) هنگام ایجاد CustomResourceDefinition هرس نمی‌شوند،
بلکه در مرحلهٔ هرس هنگام رسیدگی به درخواست‌ها هرس می‌شوند.

#### مقداردهی پیش‌فرض و Nullable

مقادیر null در فیلدهایی که پرچم nullable را مشخص نمی‌کنند یا مقدار آن را
`false` قرار می‌دهند، پیش از انجام مقداردهی پیش‌فرض هرس می‌شوند. اگر مقدار پیش‌فرضی وجود داشته باشد،
اعمال می‌شود. وقتی nullable برابر `true` باشد، مقادیر null حفظ می‌شوند و مقدار پیش‌فرض نمی‌گیرند.

برای مثال، طرح‌وارهٔ OpenAPI زیر را در نظر بگیرید:

```yaml
type: object
properties:
  spec:
    type: object
    properties:
      foo:
        type: string
        nullable: false
        default: "default"
      bar:
        type: string
        nullable: true
      baz:
        type: string
```

ایجاد یک آبجکت با مقادیر null برای `foo` و `bar` و `baz`

```yaml
spec:
  foo: null
  bar: null
  baz: null
```

به این نتیجه می‌انجامد:

```yaml
spec:
  foo: "default"
  bar: null
```

در اینجا `foo` هرس شده و مقدار پیش‌فرض گرفته است، زیرا این فیلد nullable نیست؛ `bar` به دلیل `nullable: true`
مقدار null خود را حفظ کرده است؛ و `baz` هرس شده است، زیرا این فیلد nullable نیست و مقدار پیش‌فرضی
ندارد.

### انتشار طرح‌وارهٔ اعتبارسنجی در OpenAPI

[طرح‌واره‌های اعتبارسنجی OpenAPI v3](#validation) در CustomResourceDefinition که
[ساختاریافته](#specifying-a-structural-schema) باشند و [هرس را فعال کنند](#field-pruning)، از سوی سرور API کوبرنتیز
به‌صورت [OpenAPI v3](/docs/concepts/overview/kubernetes-api/#openapi-and-swagger-definitions) و
OpenAPI v2 منتشر می‌شوند. توصیه می‌شود از سند OpenAPI v3 استفاده کنید،
زیرا بازنمایی بدون اتلافی از طرح‌وارهٔ اعتبارسنجی OpenAPI v3 در CustomResourceDefinition است،
در حالی که OpenAPI v2 حاصل یک تبدیل همراه با اتلاف است.

ابزار خط فرمان [kubectl](/docs/reference/kubectl/) از طرح‌وارهٔ منتشرشده برای انجام
اعتبارسنجی سمت کلاینت (`kubectl create` و `kubectl apply`) و توضیح طرح‌واره (`kubectl explain`)
روی منابع سفارشی استفاده می‌کند. از طرح‌وارهٔ منتشرشده می‌توان برای مقاصد دیگری مانند تولید کلاینت یا مستندسازی نیز استفاده کرد.

#### سازگاری با OpenAPI V2

برای سازگاری با OpenAPI V2، طرح‌وارهٔ اعتبارسنجی OpenAPI v3 با یک تبدیل همراه با اتلاف
به طرح‌وارهٔ OpenAPI v2 تبدیل می‌شود. این طرح‌واره در فیلدهای `definitions` و `paths` در
[مشخصات OpenAPI v2](/docs/concepts/overview/kubernetes-api/#openapi-and-swagger-definitions) نمایش داده می‌شود.

تغییرات زیر در حین تبدیل اعمال می‌شوند تا سازگاری با نسخه‌های قدیمی‌تر kubectl
در نسخهٔ 1.13 حفظ شود. این تغییرات مانع می‌شوند که kubectl بیش از حد سخت‌گیر باشد و
طرح‌واره‌های معتبر OpenAPI را که نمی‌شناسد رد کند. این تبدیل طرح‌وارهٔ اعتبارسنجی تعریف‌شده در CRD را تغییر نمی‌دهد
و در نتیجه بر [اعتبارسنجی](#validation) در سرور API تأثیری ندارد.

1. فیلدهای زیر حذف می‌شوند، زیرا OpenAPI v2 از آن‌ها پشتیبانی نمی‌کند.

   - فیلدهای `allOf`، `anyOf`، `oneOf` و `not` حذف می‌شوند

2. اگر `nullable: true` تنظیم شده باشد، `type`، `nullable`، `items` و `properties` را حذف می‌کنیم، زیرا OpenAPI v2
   نمی‌تواند nullable را بیان کند. این کار برای جلوگیری از رد شدن آبجکت‌های معتبر از سوی kubectl ضروری است.

### ستون‌های چاپ اضافی

ابزار kubectl به قالب‌بندی خروجی در سمت سرور متکی است. سرور API کلاستر شما تعیین می‌کند که
فرمان `kubectl get` کدام ستون‌ها را نمایش دهد. می‌توانید این ستون‌ها را برای یک
CustomResourceDefinition سفارشی کنید. نمونهٔ زیر ستون‌های `Spec`، `Replicas` و `Age`
را اضافه می‌کند.

این CustomResourceDefinition را در فایل `resourcedefinition.yaml` ذخیره کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              cronSpec:
                type: string
              image:
                type: string
              replicas:
                type: integer
    additionalPrinterColumns:
    - name: Spec
      type: string
      description: The cron spec defining the interval a CronJob is run
      jsonPath: .spec.cronSpec
    - name: Replicas
      type: integer
      description: The number of jobs launched by the CronJob
      jsonPath: .spec.replicas
    - name: Age
      type: date
      jsonPath: .metadata.creationTimestamp
```

این CustomResourceDefinition را ایجاد کنید:

```shell
kubectl apply -f resourcedefinition.yaml
```

با استفاده از فایل `my-crontab.yaml` از بخش قبلی یک نمونه ایجاد کنید.

چاپ سمت سرور را فراخوانی کنید:

```shell
kubectl get crontab my-new-cron-object
```

به ستون‌های `NAME`، `SPEC`، `REPLICAS` و `AGE` در خروجی توجه کنید:

```
NAME                 SPEC        REPLICAS   AGE
my-new-cron-object   * * * * *   1          7s
```

{{< note >}}
ستون `NAME` به‌صورت ضمنی وجود دارد و نیازی به تعریف آن در CustomResourceDefinition نیست.
{{< /note >}}


#### اولویت

هر ستون یک فیلد `priority` دارد. در حال حاضر، اولویت
مشخص می‌کند که ستون در نمای استاندارد نمایش داده شود یا در نمای گسترده (با استفاده از پرچم `-o wide`).

- ستون‌هایی با اولویت `0` در نمای استاندارد نمایش داده می‌شوند.
- ستون‌هایی با اولویت بزرگ‌تر از `0` فقط در نمای گسترده نمایش داده می‌شوند.

#### نوع

فیلد `type` یک ستون می‌تواند یکی از مقادیر زیر باشد (با
[انواع داده در OpenAPI v3](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes) مقایسه کنید):

- نوع `integer` – اعداد غیراعشاری
- نوع `number` – اعداد اعشاری (ممیز شناور)
- نوع `string` – رشته‌ها
- نوع `boolean` – `true` یا `false`
- نوع `date` – به‌صورت مدت زمان سپری‌شده از این برچسب زمانی نمایش داده می‌شود.

اگر مقدار درون یک CustomResource با نوع تعیین‌شده برای ستون مطابقت نداشته باشد،
آن مقدار نمایش داده نمی‌شود. برای اطمینان از درست بودن نوع مقادیر، از اعتبارسنجی CustomResource
استفاده کنید.

#### قالب

فیلد `format` یک ستون می‌تواند یکی از مقادیر زیر باشد:

- `int32`
- `int64`
- `float`
- `double`
- `byte`
- `date`
- `date-time`
- `password`

فیلد `format` ستون، سبکی را که `kubectl` هنگام چاپ مقدار به کار می‌برد تعیین می‌کند.

### انتخابگرهای فیلد

با [انتخابگرهای فیلد](/docs/concepts/overview/working-with-objects/field-selectors/)
کلاینت‌ها می‌توانند منابع سفارشی را بر اساس مقدار یک یا چند فیلد منبع
انتخاب کنند.

همهٔ منابع سفارشی از انتخابگرهای فیلد `metadata.name` و `metadata.namespace`
پشتیبانی می‌کنند.

فیلدهای اعلام‌شده در یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}}
نیز در صورتی که در فیلد `spec.versions[*].selectableFields` آن
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} گنجانده شوند، با انتخابگرهای فیلد قابل استفاده هستند.

#### فیلدهای قابل انتخاب برای منابع سفارشی {#crd-selectable-fields}

{{< feature-state feature_gate_name="CustomResourceFieldSelectors" >}}

با فیلد `spec.versions[*].selectableFields` در یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} می‌توان
اعلام کرد که کدام فیلدهای دیگرِ یک منبع سفارشی در انتخابگرهای فیلد قابل استفاده باشند.
این قابلیت به [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `CustomResourceFieldSelectors`
وابسته است (این feature gate از کوبرنتیز v1.31 به‌طور پیش‌فرض فعال است).
نمونهٔ زیر فیلدهای `.spec.color` و `.spec.size` را به‌عنوان
فیلدهای قابل انتخاب اضافه می‌کند.

این CustomResourceDefinition را در فایل `shirt-resource-definition.yaml` ذخیره کنید:

{{% code_sample file="customresourcedefinition/shirt-resource-definition.yaml" %}}

این CustomResourceDefinition را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/customresourcedefinition/shirt-resource-definition.yaml
```

با ویرایش فایل `shirt-resources.yaml` چند Shirt تعریف کنید؛ برای نمونه:

{{% code_sample file="customresourcedefinition/shirt-resources.yaml" %}}

منابع سفارشی را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/customresourcedefinition/shirt-resources.yaml
```

همهٔ منابع را دریافت کنید:

```shell
kubectl get shirts.stable.example.com
```

خروجی به این صورت است:

```
NAME       COLOR  SIZE
example1   blue   S
example2   blue   M
example3   green  M
```

پیراهن‌های آبی را واکشی کنید (یعنی Shirtهایی که `color` آن‌ها `blue` است):

```shell
kubectl get shirts.stable.example.com --field-selector spec.color=blue
```

خروجی باید به این صورت باشد:

```
NAME       COLOR  SIZE
example1   blue   S
example2   blue   M
```

فقط منابعی را دریافت کنید که `color` آن‌ها `green` و `size` آن‌ها `M` است:

```shell
kubectl get shirts.stable.example.com --field-selector spec.color=green,spec.size=M
```

خروجی باید به این صورت باشد:

```
NAME       COLOR   SIZE
example3   green   M
```

### زیرمنبع‌ها

منابع سفارشی از زیرمنبع‌های (subresources) `/status` و `/scale` پشتیبانی می‌کنند.

می‌توانید زیرمنبع‌های status و scale را به‌صورت اختیاری و با تعریف آن‌ها در CustomResourceDefinition فعال کنید.

#### زیرمنبع status

وقتی زیرمنبع status فعال باشد، زیرمنبع `/status` برای منبع سفارشی در دسترس قرار می‌گیرد.

- بخش‌های status و spec در داخل منبع سفارشی به‌ترتیب با JSONPathهای `.status` و `.spec` نمایش داده می‌شوند.
- درخواست‌های `PUT` به زیرمنبع `/status` یک آبجکت منبع سفارشی دریافت می‌کنند و تغییرات همه‌چیز به‌جز بخش status را نادیده می‌گیرند.
- درخواست‌های `PUT` به زیرمنبع `/status` فقط بخش status منبع سفارشی را اعتبارسنجی می‌کنند.
- درخواست‌های `PUT`/`POST`/`PATCH` به منبع سفارشی، تغییرات بخش status را نادیده می‌گیرند.
- مقدار `.metadata.generation` با هر تغییری افزایش می‌یابد، مگر تغییراتی که در `.metadata` یا `.status` رخ دهند.
- در ریشهٔ شِمای اعتبارسنجی OpenAPI در CRD فقط ساختارهای زیر مجاز هستند:

  - `description`
  - `example`
  - `exclusiveMaximum`
  - `exclusiveMinimum`
  - `externalDocs`
  - `format`
  - `items`
  - `maximum`
  - `maxItems`
  - `maxLength`
  - `minimum`
  - `minItems`
  - `minLength`
  - `multipleOf`
  - `pattern`
  - `properties`
  - `required`
  - `title`
  - `type`
  - `uniqueItems`

#### زیرمنبع scale

وقتی زیرمنبع scale فعال باشد، زیرمنبع `/scale` برای منبع سفارشی در دسترس قرار می‌گیرد.
آبجکت `autoscaling/v1.Scale` به‌عنوان محتوای (payload) درخواست‌های `/scale` ارسال می‌شود.

برای فعال‌کردن زیرمنبع scale، فیلدهای زیر در CustomResourceDefinition تعریف می‌شوند.

- فیلد `specReplicasPath` مسیر JSONPath درون منبع سفارشی را تعریف می‌کند که با `scale.spec.replicas` متناظر است.

  - مقدار این فیلد الزامی است.
  - فقط JSONPathهایی مجاز هستند که زیر `.spec` قرار دارند و با نشانه‌گذاری نقطه‌ای نوشته شده‌اند.
  - اگر در منبع سفارشی هیچ مقداری زیر `specReplicasPath` وجود نداشته باشد،
    زیرمنبع `/scale` هنگام GET خطا برمی‌گرداند.

- فیلد `statusReplicasPath` مسیر JSONPath درون منبع سفارشی را تعریف می‌کند که با `scale.status.replicas` متناظر است.

  - مقدار این فیلد الزامی است.
  - فقط JSONPathهایی مجاز هستند که زیر `.status` قرار دارند و با نشانه‌گذاری نقطه‌ای نوشته شده‌اند.
  - اگر در منبع سفارشی هیچ مقداری زیر `statusReplicasPath` وجود نداشته باشد،
    مقدار پیش‌فرض تعداد رپلیکا در وضعیت زیرمنبع `/scale` برابر 0 خواهد بود.

- فیلد `labelSelectorPath` مسیر JSONPath درون منبع سفارشی را تعریف می‌کند که با
  `Scale.Status.Selector` متناظر است.

  - مقدار این فیلد اختیاری است.
  - برای کار با HPA و VPA باید این فیلد را تنظیم کنید.
  - فقط JSONPathهایی مجاز هستند که زیر `.status` یا `.spec` قرار دارند و با نشانه‌گذاری نقطه‌ای نوشته شده‌اند.
  - اگر در منبع سفارشی هیچ مقداری زیر `labelSelectorPath` وجود نداشته باشد،
    مقدار پیش‌فرض انتخابگر وضعیت در زیرمنبع `/scale` رشتهٔ خالی خواهد بود.
  - فیلدی که این مسیر JSON به آن اشاره می‌کند باید یک فیلد رشته‌ای باشد (نه یک ساختار پیچیدهٔ انتخابگر)
    که یک انتخابگر برچسب سریال‌شده را به‌صورت رشته در خود دارد.

در مثال زیر، هر دو زیرمنبع status و scale فعال شده‌اند.

این CustomResourceDefinition را در فایل `resourcedefinition.yaml` ذخیره کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
            status:
              type: object
              properties:
                replicas:
                  type: integer
                labelSelector:
                  type: string
      # subresources describes the subresources for custom resources.
      subresources:
        # status enables the status subresource.
        status: {}
        # scale enables the scale subresource.
        scale:
          # specReplicasPath defines the JSONPath inside of a custom resource that corresponds to Scale.Spec.Replicas.
          specReplicasPath: .spec.replicas
          # statusReplicasPath defines the JSONPath inside of a custom resource that corresponds to Scale.Status.Replicas.
          statusReplicasPath: .status.replicas
          # labelSelectorPath defines the JSONPath inside of a custom resource that corresponds to Scale.Status.Selector.
          labelSelectorPath: .status.labelSelector
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

و آن را ایجاد کنید:

```shell
kubectl apply -f resourcedefinition.yaml
```

پس از ایجاد آبجکت CustomResourceDefinition، می‌توانید آبجکت‌های سفارشی بسازید.

اگر YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
  replicas: 3
```

و آن را ایجاد کنید:

```shell
kubectl apply -f my-crontab.yaml
```

آنگاه نقطه‌های پایانی (endpoint) جدید RESTful API در سطح فضای نام (namespace) در مسیرهای زیر ایجاد می‌شوند:

```none
/apis/stable.example.com/v1/namespaces/*/crontabs/status
```

و

```none
/apis/stable.example.com/v1/namespaces/*/crontabs/scale
```

می‌توان یک منبع سفارشی را با دستور `kubectl scale` مقیاس‌دهی کرد.
برای نمونه، دستور زیر مقدار `.spec.replicas` منبع سفارشی‌ای را که در بالا ایجاد شد
روی 5 تنظیم می‌کند:

```shell
kubectl scale --replicas=5 crontabs/my-new-cron-object
crontabs "my-new-cron-object" scaled

kubectl get crontabs my-new-cron-object -o jsonpath='{.spec.replicas}'
5
```

می‌توانید از یک [PodDisruptionBudget](/docs/tasks/run-application/configure-pdb/) برای محافظت از
منابع سفارشی‌ای که زیرمنبع scale در آن‌ها فعال است استفاده کنید.

### دسته‌ها

دسته‌ها (categories) فهرستی از منابع گروه‌بندی‌شده‌ای است که منبع سفارشی به آن‌ها تعلق دارد (مانند `all`).
با `kubectl get <category-name>` می‌توانید منابع متعلق به آن دسته را فهرست کنید.

مثال زیر `all` را به فهرست دسته‌ها در CustomResourceDefinition اضافه می‌کند
و نشان می‌دهد که چگونه می‌توان منبع سفارشی را با `kubectl get all` در خروجی نمایش داد.

این CustomResourceDefinition را در فایل `resourcedefinition.yaml` ذخیره کنید:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
    # categories is a list of grouped resources the custom resource belongs to.
    categories:
    - all
```

و آن را ایجاد کنید:

```shell
kubectl apply -f resourcedefinition.yaml
```

پس از ایجاد آبجکت CustomResourceDefinition، می‌توانید آبجکت‌های سفارشی بسازید.

YAML زیر را در فایل `my-crontab.yaml` ذخیره کنید:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```

و آن را ایجاد کنید:

```shell
kubectl apply -f my-crontab.yaml
```

هنگام استفاده از `kubectl get` می‌توانید دسته را مشخص کنید:

```shell
kubectl get all
```

خروجی این دستور منابع سفارشی از نوع `CronTab` را نیز شامل می‌شود:

```none
NAME                          AGE
crontabs/my-new-cron-object   3s
```

## {{% heading "whatsnext" %}}

* دربارهٔ [منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) مطالعه کنید.

* مستندات [CustomResourceDefinition](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#customresourcedefinition-v1-apiextensions-k8s-io) را ببینید.

* [چند نسخه](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/) از یک
  CustomResourceDefinition را ارائه دهید.

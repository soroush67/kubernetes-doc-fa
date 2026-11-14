---
title: نسخه‌ها در CustomResourceDefinitionها
reviewers:
- sttts
- liggitt
content_type: task
weight: 30
min-kubernetes-server-version: v1.16
---

<!-- overview -->
این صفحه توضیح می‌دهد که چگونه اطلاعات نسخه‌بندی را به
[CustomResourceDefinitionها](/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/) اضافه کنید. با این کار می‌توانید سطح پایداری CustomResourceDefinitionهای خود را مشخص کنید یا API خود را به نسخه‌ای جدید ارتقا دهید و میان نمایش‌های مختلف API تبدیل انجام دهید. همچنین در این صفحه توضیح داده می‌شود که چگونه یک آبجکت را از یک نسخه به نسخهٔ دیگر ارتقا دهید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

باید درک اولیه‌ای از [منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) داشته باشید.

{{< version-check >}}

<!-- steps -->

## مرور کلی

رابط API مربوط به CustomResourceDefinition یک گردش کار برای معرفی نسخه‌های جدید یک CustomResourceDefinition و ارتقا به آن‌ها فراهم می‌کند.

هنگام ایجاد یک CustomResourceDefinition، نخستین نسخه با سطح پایداری مناسب و یک شمارهٔ نسخه در فهرست `spec.versions` آن تنظیم می‌شود. برای مثال، `v1beta1` نشان می‌دهد که نخستین نسخه هنوز پایدار نیست. همهٔ آبجکت‌های منبع سفارشی در ابتدا با همین نسخه ذخیره می‌شوند.

پس از ایجاد CustomResourceDefinition، کلاینت‌ها می‌توانند استفاده از API نسخهٔ `v1beta1` را آغاز کنند.

ممکن است بعدها لازم شود نسخهٔ جدیدی مانند `v1` اضافه شود.

افزودن نسخهٔ جدید:

1. یک راهبرد تبدیل (conversion strategy) انتخاب کنید. از آنجا که آبجکت‌های منبع سفارشی باید بتوانند در هر دو نسخه ارائه شوند، گاهی در نسخه‌ای متفاوت با نسخهٔ ذخیره‌شده ارائه خواهند شد. برای اینکه این امر ممکن شود، آبجکت‌های منبع سفارشی گاهی باید میان نسخه‌ای که با آن ذخیره شده‌اند و نسخه‌ای که با آن ارائه می‌شوند تبدیل شوند. اگر تبدیل شامل تغییرات طرح‌واره (schema) باشد و به منطق سفارشی نیاز داشته باشد، باید از یک وب‌هوک تبدیل (conversion webhook) استفاده کرد. اگر طرح‌واره تغییری نکرده باشد، می‌توان از راهبرد تبدیل پیش‌فرض `None` استفاده کرد؛ در این حالت هنگام ارائهٔ نسخه‌های مختلف، تنها فیلد `apiVersion` تغییر می‌کند.
1. اگر از وب‌هوک‌های تبدیل استفاده می‌کنید، وب‌هوک تبدیل را ایجاد و مستقر کنید. برای جزئیات بیشتر، بخش [تبدیل با وب‌هوک](#webhook-conversion) را ببینید.
1. آبجکت CustomResourceDefinition را به‌روزرسانی کنید تا نسخهٔ جدید با `served:true` در فهرست `spec.versions` قرار گیرد. همچنین فیلد `spec.conversion` را روی راهبرد تبدیل انتخاب‌شده تنظیم کنید. اگر از وب‌هوک تبدیل استفاده می‌کنید، فیلد `spec.conversion.webhookClientConfig` را طوری پیکربندی کنید که وب‌هوک فراخوانی شود.

پس از افزودن نسخهٔ جدید، کلاینت‌ها می‌توانند به‌تدریج به نسخهٔ جدید مهاجرت کنند. کاملاً بی‌خطر است که برخی کلاینت‌ها از نسخهٔ قدیمی و برخی دیگر از نسخهٔ جدید استفاده کنند.

مهاجرت آبجکت‌های ذخیره‌شده به نسخهٔ جدید:

1. بخش [ارتقای آبجکت‌های موجود به نسخهٔ ذخیره‌سازی جدید](#upgrade-existing-objects-to-a-new-stored-version) را ببینید.

کلاینت‌ها پیش از ارتقای آبجکت‌ها به نسخهٔ ذخیره‌سازی جدید، در حین آن و پس از آن، می‌توانند بدون خطر از هر دو نسخهٔ قدیمی و جدید استفاده کنند.

حذف نسخهٔ قدیمی:

1. مطمئن شوید همهٔ کلاینت‌ها به‌طور کامل به نسخهٔ جدید مهاجرت کرده‌اند. برای شناسایی کلاینت‌هایی که هنوز از طریق نسخهٔ قدیمی دسترسی دارند، می‌توانید لاگ‌های kube-apiserver را بررسی کنید.
1. مقدار `served` را برای نسخهٔ قدیمی در فهرست `spec.versions` روی `false` تنظیم کنید. اگر کلاینتی به‌طور غیرمنتظره هنوز از نسخهٔ قدیمی استفاده کند، ممکن است هنگام تلاش برای دسترسی به آبجکت‌های منبع سفارشی در نسخهٔ قدیمی، خطا گزارش دهد. در این صورت، دوباره `served:true` را برای نسخهٔ قدیمی تنظیم کنید، کلاینت‌های باقی‌مانده را به نسخهٔ جدید مهاجرت دهید و این گام را تکرار کنید.
1. مطمئن شوید گام [ارتقای آبجکت‌های موجود به نسخهٔ ذخیره‌سازی جدید](#upgrade-existing-objects-to-a-new-stored-version) کامل شده است.
   1. بررسی کنید که در فهرست `spec.versions` آبجکت CustomResourceDefinition، مقدار `storage` برای نسخهٔ جدید روی `true` تنظیم شده باشد.
   1. بررسی کنید که نسخهٔ قدیمی دیگر در `status.storedVersions` آبجکت CustomResourceDefinition فهرست نشده باشد.
1. نسخهٔ قدیمی را از فهرست `spec.versions` آبجکت CustomResourceDefinition حذف کنید.
1. پشتیبانی از تبدیل نسخهٔ قدیمی را از وب‌هوک‌های تبدیل حذف کنید.

## تعیین چند نسخه

فیلد `versions` در API مربوط به CustomResourceDefinition را می‌توان برای پشتیبانی از چند نسخه از منابع سفارشی‌ای که توسعه داده‌اید به کار برد. نسخه‌ها می‌توانند طرح‌واره‌های متفاوتی داشته باشند و وب‌هوک‌های تبدیل می‌توانند منابع سفارشی را میان نسخه‌ها تبدیل کنند.
تبدیل‌های وب‌هوک باید هر جا که کاربرد دارد از [قراردادهای API کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md) پیروی کنند.
به‌ویژه، برای مجموعه‌ای از نکات ظریف و پیشنهادهای مفید، [مستندات تغییر API](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api_changes.md) را ببینید.

{{< note >}}
در `apiextensions.k8s.io/v1beta1`، به‌جای `versions` فیلدی به نام `version` وجود داشت. فیلد `version` منسوخ (deprecated) و اختیاری است، اما اگر خالی نباشد، باید با نخستین مورد در فیلد `versions` مطابقت داشته باشد.
{{< /note >}}

این مثال یک CustomResourceDefinition با دو نسخه را نشان می‌دهد. در مثال نخست، فرض بر این است که همهٔ نسخه‌ها طرح‌وارهٔ یکسانی دارند و هیچ تبدیلی میان آن‌ها انجام نمی‌شود. توضیحات درون YAML زمینهٔ بیشتری فراهم می‌کنند.

{{< tabs name="CustomResourceDefinition_versioning_example_1" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
    # A schema is required
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  - name: v1
    served: true
    storage: false
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  # The conversion section is introduced in Kubernetes 1.13+ with a default value of
  # None conversion (strategy sub-field set to None).
  conversion:
    # None conversion assumes the same schema for all versions and only sets the apiVersion
    # field of custom resources to the proper value
    strategy: None
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
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
  - name: v1
    served: true
    storage: false
  validation:
    openAPIV3Schema:
      type: object
      properties:
        host:
          type: string
        port:
          type: string
  # The conversion section is introduced in Kubernetes 1.13+ with a default value of
  # None conversion (strategy sub-field set to None).
  conversion:
    # None conversion assumes the same schema for all versions and only sets the apiVersion
    # field of custom resources to the proper value
    strategy: None
  # either Namespaced or Cluster
  scope: Namespaced
  names:
    # plural name to be used in the URL: /apis/<group>/<version>/<plural>
    plural: crontabs
    # singular name to be used as an alias on the CLI and for display
    singular: crontab
    # kind is normally the PascalCased singular type. Your resource manifests use this.
    kind: CronTab
    # shortNames allow shorter string to match your resource on the CLI
    shortNames:
    - ct
```
{{% /tab %}}
{{< /tabs >}}

می‌توانید CustomResourceDefinition را در یک فایل YAML ذخیره کنید و سپس با `kubectl apply` آن را ایجاد کنید.

```shell
kubectl apply -f my-versioned-crontab.yaml
```

پس از ایجاد، سرور API ارائهٔ هر نسخهٔ فعال را در یک endpoint از نوع HTTP REST آغاز می‌کند. در مثال بالا، نسخه‌های API در `/apis/example.com/v1beta1` و `/apis/example.com/v1` در دسترس هستند.

### اولویت نسخه

صرف‌نظر از ترتیب تعریف نسخه‌ها در یک CustomResourceDefinition، ابزار kubectl نسخهٔ دارای بالاترین اولویت را به‌عنوان نسخهٔ پیش‌فرض برای دسترسی به آبجکت‌ها به کار می‌برد. اولویت با تجزیهٔ فیلد _name_ تعیین می‌شود تا شمارهٔ نسخه، سطح پایداری (GA، Beta یا Alpha) و ترتیب درون آن سطح پایداری مشخص شود.

الگوریتمی که برای مرتب‌سازی نسخه‌ها به کار می‌رود طوری طراحی شده است که نسخه‌ها را به همان شیوه‌ای مرتب کند که پروژهٔ کوبرنتیز نسخه‌های کوبرنتیز را مرتب می‌کند. نسخه‌ها با حرف `v` شروع می‌شوند و پس از آن یک عدد، یک پسوند اختیاری `beta` یا `alpha` و اطلاعات عددی اختیاری دیگری برای نسخه‌بندی می‌آید. به‌طور کلی، رشتهٔ نسخه ممکن است شبیه `v2` یا `v2beta1` باشد. نسخه‌ها با الگوریتم زیر مرتب می‌شوند:

- ورودی‌هایی که از الگوهای نسخهٔ کوبرنتیز پیروی می‌کنند، پیش از ورودی‌هایی قرار می‌گیرند که از این الگوها پیروی نمی‌کنند.
- در ورودی‌هایی که از الگوهای نسخهٔ کوبرنتیز پیروی می‌کنند، بخش‌های عددی رشتهٔ نسخه از بزرگ به کوچک مرتب می‌شوند.
- اگر رشته‌های `beta` یا `alpha` پس از نخستین بخش عددی بیایند، به همین ترتیب و پس از رشتهٔ معادلی که پسوند `beta` یا `alpha` ندارد (و فرض می‌شود نسخهٔ GA است) مرتب می‌شوند.
- اگر عدد دیگری پس از `beta` یا `alpha` بیاید، آن اعداد نیز از بزرگ به کوچک مرتب می‌شوند.
- رشته‌هایی که با قالب بالا سازگار نیستند به ترتیب الفبایی مرتب می‌شوند و با بخش‌های عددی آن‌ها رفتار ویژه‌ای نمی‌شود. توجه کنید که در مثال زیر، `foo1` بالاتر از `foo10` قرار گرفته است. این رفتار با مرتب‌سازی بخش عددی ورودی‌هایی که از الگوهای نسخهٔ کوبرنتیز پیروی می‌کنند متفاوت است.

با نگاه به فهرست مرتب‌شدهٔ زیر، این قواعد روشن‌تر می‌شوند:

```none
- v10
- v2
- v1
- v11beta2
- v10beta3
- v3beta1
- v12alpha1
- v11alpha2
- foo1
- foo10
```

در مثال بخش [تعیین چند نسخه](#specify-multiple-versions)، ترتیب مرتب‌سازی نسخه‌ها ابتدا `v1` و سپس `v1beta1` است. در نتیجه، فرمان kubectl از `v1` به‌عنوان نسخهٔ پیش‌فرض استفاده می‌کند، مگر اینکه آبجکت ارائه‌شده نسخه را مشخص کرده باشد.

### منسوخ‌شدن نسخه

{{< feature-state state="stable" for_k8s_version="v1.19" >}}

از نسخهٔ v1.19 به بعد، یک CustomResourceDefinition می‌تواند مشخص کند که نسخهٔ خاصی از منبعی که تعریف می‌کند منسوخ شده است.
هنگامی که درخواست‌های API به نسخهٔ منسوخ آن منبع ارسال شوند، یک پیام هشدار به‌صورت header در پاسخ API بازگردانده می‌شود.
در صورت تمایل، می‌توان پیام هشدار هر نسخهٔ منسوخ منبع را سفارشی کرد.

پیام هشدار سفارشی باید گروه API، نسخه و kind منسوخ را مشخص کند و در صورت امکان، گروه API، نسخه و kind جایگزین را نیز نشان دهد.

{{< tabs name="CustomResourceDefinition_versioning_deprecated" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.example.com
spec:
  group: example.com
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: false
    # This indicates the v1alpha1 version of the custom resource is deprecated.
    # API requests to this version receive a warning header in the server response.
    deprecated: true
    # This overrides the default warning returned to API clients making v1alpha1 API requests.
    deprecationWarning: "example.com/v1alpha1 CronTab is deprecated; see http://example.com/v1alpha1-v1 for instructions to migrate to example.com/v1 CronTab"
    
    schema: ...
  - name: v1beta1
    served: true
    # This indicates the v1beta1 version of the custom resource is deprecated.
    # API requests to this version receive a warning header in the server response.
    # A default warning message is returned for this version.
    deprecated: true
    schema: ...
  - name: v1
    served: true
    storage: true
    schema: ...
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: crontabs.example.com
spec:
  group: example.com
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
  scope: Namespaced
  validation: ...
  versions:
  - name: v1alpha1
    served: true
    storage: false
    # This indicates the v1alpha1 version of the custom resource is deprecated.
    # API requests to this version receive a warning header in the server response.
    deprecated: true
    # This overrides the default warning returned to API clients making v1alpha1 API requests.
    deprecationWarning: "example.com/v1alpha1 CronTab is deprecated; see http://example.com/v1alpha1-v1 for instructions to migrate to example.com/v1 CronTab"
  - name: v1beta1
    served: true
    # This indicates the v1beta1 version of the custom resource is deprecated.
    # API requests to this version receive a warning header in the server response.
    # A default warning message is returned for this version.
    deprecated: true
  - name: v1
    served: true
    storage: true
```
{{% /tab %}}
{{< /tabs >}}


### حذف نسخه

یک نسخهٔ قدیمی‌تر API را نمی‌توان از مانیفست CustomResourceDefinition حذف کرد، مگر اینکه داده‌های ذخیره‌شدهٔ موجود در همهٔ کلاسترهایی که نسخهٔ قدیمی‌تر منبع سفارشی را ارائه می‌کردند به نسخهٔ جدیدتر API مهاجرت داده شده باشند و نسخهٔ قدیمی از `status.storedVersions` آبجکت CustomResourceDefinition حذف شده باشد.

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.example.com
spec:
  group: example.com
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
  scope: Namespaced
  versions:
  - name: v1beta1
    # This indicates the v1beta1 version of the custom resource is no longer served.
    # API requests to this version receive a not found error in the server response.
    served: false
    schema: ...
  - name: v1
    served: true
    # The new served version should be set as the storage version
    storage: true
    schema: ...
```

## تبدیل با وب‌هوک

{{< feature-state state="stable" for_k8s_version="v1.16" >}}

{{< note >}}
تبدیل با وب‌هوک از نسخهٔ 1.15 به‌صورت بتا و از کوبرنتیز 1.13 به‌صورت آلفا در دسترس است. قابلیت `CustomResourceWebhookConversion` باید فعال باشد؛ در بسیاری از کلاسترها این قابلیت برای ویژگی‌های بتا به‌طور خودکار فعال است. برای اطلاعات بیشتر، مستندات [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) را ببینید.
{{< /note >}}

در مثال بالا، تبدیل میان نسخه‌ها از نوع None است که هنگام تبدیل فقط فیلد `apiVersion` را تنظیم می‌کند و بقیهٔ آبجکت را تغییر نمی‌دهد. سرور API از تبدیل‌های وب‌هوک نیز پشتیبانی می‌کند که در صورت نیاز به تبدیل، یک سرویس خارجی را فراخوانی می‌کنند. برای مثال، در موارد زیر:

* منبع سفارشی در نسخه‌ای متفاوت با نسخهٔ ذخیره‌شده درخواست شود.
* یک Watch در یک نسخه ایجاد شده باشد، اما آبجکت تغییریافته در نسخه‌ای دیگر ذخیره شده باشد.
* درخواست PUT منبع سفارشی در نسخه‌ای متفاوت با نسخهٔ ذخیره‌سازی باشد.

برای پوشش همهٔ این موارد و بهینه‌سازی تبدیل در سرور API، درخواست‌های تبدیل ممکن است شامل چند آبجکت باشند تا تعداد فراخوانی‌های خارجی به حداقل برسد. وب‌هوک باید این تبدیل‌ها را به‌طور مستقل انجام دهد.

### نوشتن سرور وب‌هوک تبدیل

لطفاً به پیاده‌سازی [سرور وب‌هوک تبدیل منبع
سفارشی](https://github.com/kubernetes/kubernetes/tree/v1.25.3/test/images/agnhost/crd-conversion-webhook/main.go)
مراجعه کنید که در یک آزمون e2e کوبرنتیز اعتبارسنجی می‌شود. این وب‌هوک درخواست‌های `ConversionReview` ارسال‌شده از سوی سرورهای API را پردازش می‌کند و نتایج تبدیل را در قالب `ConversionResponse` بازمی‌گرداند. توجه کنید که درخواست شامل فهرستی از منابع سفارشی است که باید بدون تغییر ترتیب آبجکت‌ها، به‌طور مستقل تبدیل شوند.
سرور نمونه به گونه‌ای سازمان‌دهی شده است که بتوان آن را برای تبدیل‌های دیگر نیز دوباره به کار برد.
بیشتر کدهای مشترک در
[فایل framework](https://github.com/kubernetes/kubernetes/tree/v1.25.3/test/images/agnhost/crd-conversion-webhook/converter/framework.go)
قرار دارند و تنها
[یک تابع](https://github.com/kubernetes/kubernetes/tree/v1.25.3/test/images/agnhost/crd-conversion-webhook/converter/example_converter.go#L29-L80)
باقی می‌ماند که باید برای تبدیل‌های مختلف پیاده‌سازی شود.

{{< note >}}
سرور وب‌هوک تبدیل نمونه، فیلد `ClientAuth` را
[خالی](https://github.com/kubernetes/kubernetes/tree/v1.25.3/test/images/agnhost/crd-conversion-webhook/config.go#L47-L48)
می‌گذارد که مقدار پیش‌فرض آن `NoClientCert` است. این یعنی سرور وب‌هوک هویت کلاینت‌ها را، که قاعدتاً سرورهای API هستند، احراز نمی‌کند. اگر به TLS دوطرفه یا روش‌های دیگری برای احراز هویت کلاینت‌ها نیاز دارید، بخش [احراز هویت سرورهای API](/docs/reference/access-authn-authz/extensible-admission-controllers/#authenticate-apiservers) را ببینید.
{{< /note >}}

#### تغییرات مجاز

وب‌هوک تبدیل نباید چیزی درون `metadata` آبجکت تبدیل‌شده را به‌جز `labels` و `annotations` تغییر دهد.
تلاش برای تغییر `name`، `UID` و `namespace` رد می‌شود و درخواستی که موجب تبدیل شده است شکست می‌خورد. همهٔ تغییرات دیگر نادیده گرفته می‌شوند.

### استقرار سرویس وب‌هوک تبدیل

مستندات استقرار وب‌هوک تبدیل (conversion webhook) همانند مستندات
[سرویس نمونهٔ وب‌هوک پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#deploy-the-admission-webhook-service) است.
در بخش‌های بعدی فرض بر این است که سرور وب‌هوک تبدیل در سرویسی به نام `example-conversion-webhook-server` در فضای نام (namespace) `default` مستقر شده است و ترافیک را روی مسیر `/crdconvert` پاسخ می‌دهد.

{{< note >}}
وقتی سرور وب‌هوک به‌صورت یک سرویس در کلاستر کوبرنتیز مستقر می‌شود، باید از طریق یک سرویس روی پورت 443 در دسترس قرار گیرد. خود سرور می‌تواند از هر پورت دلخواهی استفاده کند، اما آبجکت Service باید آن را به پورت 443 نگاشت کند.
اگر برای سرویس از پورت دیگری استفاده شود، ممکن است ارتباط میان سرور API و سرویس وب‌هوک با شکست مواجه شود.
{{< /note >}}

### پیکربندی CustomResourceDefinition برای استفاده از وب‌هوک‌های تبدیل

می‌توان مثال تبدیل `None` را با تغییر بخش `conversion` در `spec` طوری گسترش داد که از وب‌هوک تبدیل استفاده کند:

{{< tabs name="CustomResourceDefinition_versioning_example_2" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
    # Each version can define its own schema when there is no top-level
    # schema is defined.
    schema:
      openAPIV3Schema:
        type: object
        properties:
          hostPort:
            type: string
  - name: v1
    served: true
    storage: false
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  conversion:
    # the Webhook strategy instructs the API server to call an external webhook for any conversion between custom resources.
    strategy: Webhook
    # webhook is required when strategy is `Webhook` and it configures the webhook endpoint to be called by API server.
    webhook:
      # conversionReviewVersions indicates what ConversionReview versions are understood/preferred by the webhook.
      # The first version in the list understood by the API server is sent to the webhook.
      # The webhook must respond with a ConversionReview object in the same version it received.
      conversionReviewVersions: ["v1","v1beta1"]
      clientConfig:
        service:
          namespace: default
          name: example-conversion-webhook-server
          path: /crdconvert
        caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
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
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  # name must match the spec fields below, and be in the form: <plural>.<group>
  name: crontabs.example.com
spec:
  # group name to use for REST API: /apis/<group>/<version>
  group: example.com
  # prunes object fields that are not specified in OpenAPI schemas below.
  preserveUnknownFields: false
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
    # Each version can define its own schema when there is no top-level
    # schema is defined.
    schema:
      openAPIV3Schema:
        type: object
        properties:
          hostPort:
            type: string
  - name: v1
    served: true
    storage: false
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  conversion:
    # the Webhook strategy instructs the API server to call an external webhook for any conversion between custom resources.
    strategy: Webhook
    # webhookClientConfig is required when strategy is `Webhook` and it configures the webhook endpoint to be called by API server.
    webhookClientConfig:
      service:
        namespace: default
        name: example-conversion-webhook-server
        path: /crdconvert
      caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
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
{{% /tab %}}
{{< /tabs >}}

می‌توانید این CustomResourceDefinition را در یک فایل YAML ذخیره کنید و سپس با
`kubectl apply` آن را اعمال کنید.

```shell
kubectl apply -f my-versioned-crontab-with-conversion.yaml
```

پیش از اعمال تغییرات جدید، مطمئن شوید که سرویس تبدیل راه‌اندازی شده و در حال اجراست.

### برقراری ارتباط با وب‌هوک

هنگامی که سرور API تشخیص داد که یک درخواست باید به وب‌هوک تبدیل فرستاده شود،
باید بداند چگونه با وب‌هوک ارتباط برقرار کند. این موضوع در بخش `webhookClientConfig`
از پیکربندی وب‌هوک مشخص می‌شود.

وب‌هوک‌های تبدیل را می‌توان از طریق یک URL یا یک ارجاع به سرویس فراخوانی کرد.
همچنین می‌توان به‌صورت اختیاری یک بستهٔ CA سفارشی برای اعتبارسنجی اتصال TLS در نظر گرفت.

### URL

فیلد `url` مکان وب‌هوک را در قالب استاندارد URL
(`scheme://host:port/path`) مشخص می‌کند.

مقدار `host` نباید به سرویسی اشاره کند که درون کلاستر اجرا می‌شود؛ در این حالت
به‌جای آن با تعیین فیلد `service` از ارجاع به سرویس استفاده کنید.
در برخی از سرورهای API ممکن است نام میزبان از طریق DNS خارجی تفکیک شود
(یعنی `kube-apiserver` نمی‌تواند DNS درون کلاستر را تفکیک کند، زیرا این کار
نقض لایه‌بندی است). مقدار `host` می‌تواند یک نشانی IP نیز باشد.

توجه کنید که استفاده از `localhost` یا `127.0.0.1` به‌عنوان `host` پرخطر است،
مگر آنکه با دقت زیاد این وب‌هوک را روی همهٔ میزبان‌هایی اجرا کنید که سرور APIای
روی آن‌ها اجرا می‌شود که ممکن است لازم باشد این وب‌هوک را فراخوانی کند. چنین نصب‌هایی
احتمالاً قابل‌حمل نیستند و نمی‌توان آن‌ها را به‌سادگی در یک کلاستر جدید اجرا کرد.

طرح (scheme) باید "https" باشد؛ یعنی URL باید با "https://" آغاز شود.

استفاده از نام کاربری یا احراز هویت پایه (برای مثال "user:password@") مجاز نیست.
بخش‌های قطعه (‎"#..."‎) و پارامترهای پرس‌وجو (‎"?..."‎) نیز مجاز نیستند.

در ادامه نمونه‌ای از یک وب‌هوک تبدیل آمده است که برای فراخوانی یک URL پیکربندی شده است
(و انتظار دارد گواهی TLS با استفاده از ریشه‌های اعتماد سیستم اعتبارسنجی شود؛ به همین دلیل caBundle را مشخص نمی‌کند):

{{< tabs name="CustomResourceDefinition_versioning_example_3" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        url: "https://my-webhook.example.com:9443/my-webhook-path"
...
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    webhookClientConfig:
      url: "https://my-webhook.example.com:9443/my-webhook-path"
...
```
{{% /tab %}}
{{< /tabs >}}

### ارجاع به سرویس

بخش `service` درون `webhookClientConfig` ارجاعی به سرویسِ وب‌هوک تبدیل است.
اگر وب‌هوک درون کلاستر اجرا می‌شود، باید به‌جای `url` از `service` استفاده کنید.
تعیین فضای نام و نام سرویس الزامی است. پورت اختیاری است و مقدار پیش‌فرض آن 443 است.
مسیر نیز اختیاری است و مقدار پیش‌فرض آن "/" است.

در ادامه نمونه‌ای از وب‌هوکی آمده است که برای فراخوانی یک سرویس روی پورت "1234"
در زیرمسیر "/my-path" پیکربندی شده است و اتصال TLS را با استفاده از یک بستهٔ CA سفارشی
در برابر ServerName‏ `my-service-name.my-service-namespace.svc` اعتبارسنجی می‌کند.

{{< tabs name="CustomResourceDefinition_versioning_example_4" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        service:
          namespace: my-service-namespace
          name: my-service-name
          path: /my-path
          port: 1234
        caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
...
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    webhookClientConfig:
      service:
        namespace: my-service-namespace
        name: my-service-name
        path: /my-path
        port: 1234
      caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
...
```
{{% /tab %}}
{{< /tabs >}}

## درخواست و پاسخ وب‌هوک

### درخواست

به وب‌هوک‌ها یک درخواست POST با `Content-Type: application/json` فرستاده می‌شود
که بدنهٔ آن یک آبجکت API از نوع `ConversionReview` در گروه API‏ `apiextensions.k8s.io`
است که به JSON سریال‌سازی شده است.

وب‌هوک‌ها می‌توانند با فیلد `conversionReviewVersions` در CustomResourceDefinition خود
مشخص کنند که کدام نسخه‌های آبجکت‌های `ConversionReview` را می‌پذیرند:

{{< tabs name="conversionReviewVersions" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    webhook:
      conversionReviewVersions: ["v1", "v1beta1"]
      ...
```

فیلد `conversionReviewVersions` هنگام ایجاد تعریف‌های منبع سفارشی
`apiextensions.k8s.io/v1` الزامی است.
وب‌هوک‌ها باید دست‌کم از یک نسخهٔ `ConversionReview` پشتیبانی کنند
که سرور API فعلی و سرور API نسخهٔ قبلی آن را می‌شناسند.
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
# Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
...
spec:
  ...
  conversion:
    strategy: Webhook
    conversionReviewVersions: ["v1", "v1beta1"]
    ...
```

اگر هیچ مقداری برای `conversionReviewVersions` مشخص نشود، مقدار پیش‌فرض هنگام ایجاد
تعریف‌های منبع سفارشی `apiextensions.k8s.io/v1beta1` برابر `v1beta1` است.
{{% /tab %}}
{{< /tabs >}}

سرورهای API نخستین نسخهٔ `ConversionReview` در فهرست `conversionReviewVersions` را که پشتیبانی می‌کنند، ارسال می‌کنند.
اگر سرور API از هیچ‌یک از نسخه‌های این فهرست پشتیبانی نکند، اجازهٔ ایجاد تعریف منبع سفارشی داده نمی‌شود.
اگر سرور API با پیکربندی وب‌هوک تبدیلی روبه‌رو شود که پیش‌تر ایجاد شده و از هیچ‌یک از نسخه‌های `ConversionReview`
که سرور API می‌تواند ارسال کند پشتیبانی نمی‌کند، تلاش‌ها برای فراخوانی وب‌هوک با شکست مواجه می‌شوند.

این مثال داده‌های موجود در یک آبجکت `ConversionReview` را برای درخواستی نشان می‌دهد
که آبجکت‌های `CronTab` را به `example.com/v1` تبدیل می‌کند:


{{< tabs name="ConversionReview_request" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
{
  "apiVersion": "apiextensions.k8s.io/v1",
  "kind": "ConversionReview",
  "request": {
    # Random uid uniquely identifying this conversion call
    "uid": "705ab4f5-6393-11e8-b7cc-42010a800002",
    
    # The API group and version the objects should be converted to
    "desiredAPIVersion": "example.com/v1",
    
    # The list of objects to convert.
    # May contain one or more objects, in one or more versions.
    "objects": [
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1beta1",
        "metadata": {
          "creationTimestamp": "2019-09-04T14:03:02Z",
          "name": "local-crontab",
          "namespace": "default",
          "resourceVersion": "143",
          "uid": "3415a7fc-162b-4300-b5da-fd6083580d66"
        },
        "hostPort": "localhost:1234"
      },
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1beta1",
        "metadata": {
          "creationTimestamp": "2019-09-03T13:02:01Z",
          "name": "remote-crontab",
          "resourceVersion": "12893",
          "uid": "359a83ec-b575-460d-b553-d859cedde8a0"
        },
        "hostPort": "example.com:2345"
      }
    ]
  }
}
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
{
  # Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
  "apiVersion": "apiextensions.k8s.io/v1beta1",
  "kind": "ConversionReview",
  "request": {
    # Random uid uniquely identifying this conversion call
    "uid": "705ab4f5-6393-11e8-b7cc-42010a800002",
    
    # The API group and version the objects should be converted to
    "desiredAPIVersion": "example.com/v1",
    
    # The list of objects to convert.
    # May contain one or more objects, in one or more versions.
    "objects": [
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1beta1",
        "metadata": {
          "creationTimestamp": "2019-09-04T14:03:02Z",
          "name": "local-crontab",
          "namespace": "default",
          "resourceVersion": "143",
          "uid": "3415a7fc-162b-4300-b5da-fd6083580d66"
        },
        "hostPort": "localhost:1234"
      },
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1beta1",
        "metadata": {
          "creationTimestamp": "2019-09-03T13:02:01Z",
          "name": "remote-crontab",
          "resourceVersion": "12893",
          "uid": "359a83ec-b575-460d-b553-d859cedde8a0"
        },
        "hostPort": "example.com:2345"
      }
    ]
  }
}
```
{{% /tab %}}
{{< /tabs >}}

### پاسخ

وب‌هوک‌ها با کد وضعیت HTTP‏ 200، سرآیند `Content-Type: application/json`
و بدنه‌ای پاسخ می‌دهند که شامل یک آبجکت `ConversionReview` (در همان نسخه‌ای که برایشان ارسال شده)
با بخش `response` پرشده است و به JSON سریال‌سازی شده است.

اگر تبدیل موفقیت‌آمیز باشد، وب‌هوک باید بخش `response` را با فیلدهای زیر برگرداند:
* فیلد `uid` که از `request.uid` ارسال‌شده به وب‌هوک کپی می‌شود
* فیلد `result` با مقدار `{"status":"Success"}`
* فیلد `convertedObjects` که شامل همهٔ آبجکت‌های `request.objects` است که به `request.desiredAPIVersion` تبدیل شده‌اند

نمونه‌ای از یک پاسخ موفق حداقلی از وب‌هوک:

{{< tabs name="ConversionReview_response_success" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
{
  "apiVersion": "apiextensions.k8s.io/v1",
  "kind": "ConversionReview",
  "response": {
    # must match <request.uid>
    "uid": "705ab4f5-6393-11e8-b7cc-42010a800002",
    "result": {
      "status": "Success"
    },
    # Objects must match the order of request.objects, and have apiVersion set to <request.desiredAPIVersion>.
    # kind, metadata.uid, metadata.name, and metadata.namespace fields must not be changed by the webhook.
    # metadata.labels and metadata.annotations fields may be changed by the webhook.
    # All other changes to metadata fields by the webhook are ignored.
    "convertedObjects": [
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1",
        "metadata": {
          "creationTimestamp": "2019-09-04T14:03:02Z",
          "name": "local-crontab",
          "namespace": "default",
          "resourceVersion": "143",
          "uid": "3415a7fc-162b-4300-b5da-fd6083580d66"
        },
        "host": "localhost",
        "port": "1234"
      },
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1",
        "metadata": {
          "creationTimestamp": "2019-09-03T13:02:01Z",
          "name": "remote-crontab",
          "resourceVersion": "12893",
          "uid": "359a83ec-b575-460d-b553-d859cedde8a0"
        },
        "host": "example.com",
        "port": "2345"
      }
    ]
  }
}
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
{
  # Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
  "apiVersion": "apiextensions.k8s.io/v1beta1",
  "kind": "ConversionReview",
  "response": {
    # must match <request.uid>
    "uid": "705ab4f5-6393-11e8-b7cc-42010a800002",
    "result": {
      "status": "Failed"
    },
    # Objects must match the order of request.objects, and have apiVersion set to <request.desiredAPIVersion>.
    # kind, metadata.uid, metadata.name, and metadata.namespace fields must not be changed by the webhook.
    # metadata.labels and metadata.annotations fields may be changed by the webhook.
    # All other changes to metadata fields by the webhook are ignored.
    "convertedObjects": [
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1",
        "metadata": {
          "creationTimestamp": "2019-09-04T14:03:02Z",
          "name": "local-crontab",
          "namespace": "default",
          "resourceVersion": "143",
          "uid": "3415a7fc-162b-4300-b5da-fd6083580d66"
        },
        "host": "localhost",
        "port": "1234"
      },
      {
        "kind": "CronTab",
        "apiVersion": "example.com/v1",
        "metadata": {
          "creationTimestamp": "2019-09-03T13:02:01Z",
          "name": "remote-crontab",
          "resourceVersion": "12893",
          "uid": "359a83ec-b575-460d-b553-d859cedde8a0"
        },
        "host": "example.com",
        "port": "2345"
      }
    ]
  }
}
```
{{% /tab %}}
{{< /tabs >}}

اگر تبدیل با شکست مواجه شود، وب‌هوک باید بخش `response` را با فیلدهای زیر برگرداند:
* فیلد `uid` که از `request.uid` ارسال‌شده به وب‌هوک کپی می‌شود
* فیلد `result` با مقدار `{"status":"Failed"}`

{{< warning >}}
شکست در تبدیل می‌تواند دسترسی خواندن و نوشتن به منابع سفارشی، از جمله امکان به‌روزرسانی
یا حذف این منابع، را مختل کند. تا جای ممکن باید از شکست در تبدیل جلوگیری کرد و نباید
از آن برای اعمال محدودیت‌های اعتبارسنجی استفاده کرد (به‌جای آن از طرح‌واره‌های اعتبارسنجی
یا وب‌هوک پذیرش استفاده کنید).
{{< /warning >}}

نمونه‌ای از پاسخ وب‌هوک که نشان می‌دهد درخواست تبدیل با شکست مواجه شده است، همراه با یک پیام اختیاری:
{{< tabs name="ConversionReview_response_failure" >}}
{{% tab name="apiextensions.k8s.io/v1" %}}
```yaml
{
  "apiVersion": "apiextensions.k8s.io/v1",
  "kind": "ConversionReview",
  "response": {
    "uid": "<value from request.uid>",
    "result": {
      "status": "Failed",
      "message": "hostPort could not be parsed into a separate host and port"
    }
  }
}
```
{{% /tab %}}
{{% tab name="apiextensions.k8s.io/v1beta1" %}}
```yaml
{
  # Deprecated in v1.16 in favor of apiextensions.k8s.io/v1
  "apiVersion": "apiextensions.k8s.io/v1beta1",
  "kind": "ConversionReview",
  "response": {
    "uid": "<value from request.uid>",
    "result": {
      "status": "Failed",
      "message": "hostPort could not be parsed into a separate host and port"
    }
  }
}
```
{{% /tab %}}
{{< /tabs >}}

## نوشتن، خواندن و به‌روزرسانی آبجکت‌های CustomResourceDefinition نسخه‌بندی‌شده

هنگام نوشتن یک آبجکت، آن آبجکت در نسخه‌ای ذخیره می‌شود که در لحظهٔ نوشتن به‌عنوان نسخهٔ ذخیره‌سازی (storage version) تعیین شده است. اگر نسخهٔ ذخیره‌سازی تغییر کند، آبجکت‌های موجود هرگز به‌طور خودکار تبدیل نمی‌شوند. با این حال، آبجکت‌هایی که تازه ایجاد یا به‌روزرسانی می‌شوند، در نسخهٔ ذخیره‌سازی جدید نوشته می‌شوند. ممکن است آبجکتی در نسخه‌ای نوشته شده باشد که دیگر ارائه نمی‌شود.

هنگام خواندن یک آبجکت، نسخه را به‌عنوان بخشی از مسیر مشخص می‌کنید. می‌توانید آبجکت را در هر نسخه‌ای که در حال حاضر ارائه می‌شود درخواست کنید. اگر نسخه‌ای متفاوت با نسخهٔ ذخیره‌شدهٔ آبجکت مشخص کنید، کوبرنتیز آبجکت را در همان نسخهٔ درخواستی به شما برمی‌گرداند، اما آبجکت ذخیره‌شده روی دیسک تغییری نمی‌کند.

اینکه هنگام پاسخ به درخواست خواندن چه اتفاقی برای آبجکت بازگردانده‌شده می‌افتد، به مقداری بستگی دارد که در `spec.conversion` مربوط به CRD مشخص شده است:
- اگر مقدار پیش‌فرض `None` برای `strategy` مشخص شده باشد، تنها تغییرات اعمال‌شده روی آبجکت، تغییر رشتهٔ `apiVersion` و احتمالاً [هرس فیلدهای ناشناخته](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning) (بسته به پیکربندی) است. توجه کنید که اگر شِماهای نسخهٔ ذخیره‌سازی و نسخهٔ درخواستی با هم متفاوت باشند، بعید است این روش نتیجهٔ خوبی داشته باشد. به‌ویژه، اگر داده‌های یکسان در نسخه‌های مختلف در فیلدهای متفاوتی نمایش داده می‌شوند، نباید از این راهبرد استفاده کنید.
- اگر [تبدیل از طریق وب‌هوک](#webhook-conversion) مشخص شده باشد، این سازوکار فرایند تبدیل را کنترل می‌کند.

اگر آبجکت موجودی را به‌روزرسانی کنید، آن آبجکت در نسخه‌ای که در حال حاضر نسخهٔ ذخیره‌سازی است بازنویسی می‌شود. این تنها راهی است که آبجکت‌ها از یک نسخه به نسخهٔ دیگر تغییر می‌کنند.

برای روشن‌تر شدن موضوع، دنبالهٔ فرضی رویدادهای زیر را در نظر بگیرید:

1. نسخهٔ ذخیره‌سازی `v1beta1` است. آبجکتی ایجاد می‌کنید. این آبجکت در نسخهٔ `v1beta1` ذخیره می‌شود.
2. نسخهٔ `v1` را به CustomResourceDefinition خود اضافه می‌کنید و آن را به‌عنوان نسخهٔ ذخیره‌سازی تعیین می‌کنید. در اینجا شِماهای `v1` و `v1beta1` یکسان هستند؛ این وضعیت معمولاً هنگام ارتقای یک API به سطح پایدار در اکوسیستم کوبرنتیز رخ می‌دهد.
3. آبجکت خود را در نسخهٔ `v1beta1` می‌خوانید و سپس دوباره آن را در نسخهٔ `v1` می‌خوانید. هر دو آبجکت بازگردانده‌شده به‌جز فیلد apiVersion کاملاً یکسان هستند.
4. آبجکت جدیدی ایجاد می‌کنید. این آبجکت در نسخهٔ `v1` ذخیره می‌شود. اکنون دو آبجکت دارید که یکی در نسخهٔ `v1beta1` و دیگری در نسخهٔ `v1` است.
5. آبجکت اول را به‌روزرسانی می‌کنید. اکنون این آبجکت در نسخهٔ `v1` ذخیره می‌شود، زیرا این نسخه نسخهٔ ذخیره‌سازی فعلی است.

### نسخه‌های ذخیره‌سازی قبلی

سرور API هر نسخه‌ای را که تاکنون به‌عنوان نسخهٔ ذخیره‌سازی علامت‌گذاری شده باشد، در فیلد وضعیت `storedVersions` ثبت می‌کند. آبجکت‌ها ممکن است در هر نسخه‌ای که زمانی به‌عنوان نسخهٔ ذخیره‌سازی تعیین شده است ذخیره شده باشند. هیچ آبجکتی نمی‌تواند در نسخه‌ای که هرگز نسخهٔ ذخیره‌سازی نبوده است، در ذخیره‌سازی وجود داشته باشد.

## ارتقای آبجکت‌های موجود به یک نسخهٔ ذخیره‌شدهٔ جدید

هنگام منسوخ کردن نسخه‌ها و حذف پشتیبانی از آن‌ها، یک روال ارتقای ذخیره‌سازی انتخاب کنید.

*گزینهٔ ۱:* استفاده از مهاجرت نسخهٔ ذخیره‌سازی (Storage Version Migration)

1. [مهاجرت نسخهٔ ذخیره‌سازی](/docs/tasks/manage-kubernetes-objects/storage-version-migration/) را برای منبع سفارشی اجرا کنید.

   برای مثال، می‌توانید یک منبع `StorageVersionMigration` را در همان مانیفستی قرار دهید که `CustomResourceDefinition` به‌روزرسانی‌شدهٔ شما در آن است:

   ```yaml
   apiVersion: apiextensions.k8s.io/v1
   kind: CustomResourceDefinition
   metadata:
     name: crontabs.example.com
   spec:
     group: example.com
     ...
   ---
   apiVersion: storagemigration.k8s.io/v1
   kind: StorageVersionMigration
   metadata:
     name: crontabs-migration
   spec:
     resource:
       group: example.com
       resource: crontabs
   ```

2. پس از موفقیت‌آمیز بودن مهاجرت، نسخهٔ قدیمی از فیلد `status.storedVersions` در CustomResourceDefinition حذف می‌شود.

*گزینهٔ ۲:* ارتقای دستی آبجکت‌های موجود به یک نسخهٔ ذخیره‌شدهٔ جدید

در ادامه، نمونه‌ای از روال ارتقا از `v1beta1` به `v1` آمده است.

1. در فایل CustomResourceDefinition، نسخهٔ `v1` را به‌عنوان نسخهٔ ذخیره‌سازی تنظیم کنید و آن را با kubectl اعمال کنید. اکنون مقدار `storedVersions` برابر `v1beta1, v1` است.
2. یک روال ارتقا بنویسید که همهٔ آبجکت‌های موجود را فهرست کند و آن‌ها را با همان محتوا دوباره بنویسد. این کار بک‌اند را وادار می‌کند آبجکت‌ها را در نسخهٔ ذخیره‌سازی فعلی، یعنی `v1`، بنویسد.
3. نسخهٔ `v1beta1` را از فیلد `status.storedVersions` در CustomResourceDefinition حذف کنید.

{{< note >}}
در اینجا نمونه‌ای از نحوهٔ وصله کردن (patch) زیرمنبع `status` برای یک آبجکت CRD با استفاده از `kubectl` آمده است:
```bash
kubectl patch customresourcedefinitions <CRD_Name> --subresource='status' --type='merge' -p '{"status":{"storedVersions":["v1"]}}'
```
{{< /note >}}

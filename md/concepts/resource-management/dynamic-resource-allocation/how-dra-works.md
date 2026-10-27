---
reviewers:
- klueska
- pohly
title: نحوهٔ کار DRA
content_type: concept
weight: 20
---

<!-- overview -->

این صفحه توضیح می‌دهد که کوبرنتیز چگونه با تخصیص پویای منابع (DRA) دستگاه‌ها را به بارهای کاری تخصیص می‌دهد و Podهای از پیش زمان‌بندی‌شده چگونه با این فرایند تعامل دارند.

<!-- body -->

## نحوهٔ کار تخصیص منابع با DRA {#how-it-works}

بخش‌های زیر گردش کار مربوط به
[انواع کاربران DRA](/docs/concepts/resource-management/dynamic-resource-allocation/#dra-user-types)
و نیز گردش کار سامانهٔ کوبرنتیز را در طول
تخصیص پویای منابع شرح می‌دهند.

### گردش کار کاربران {#user-workflow}

1. **ایجاد درایور**: مالکان دستگاه‌ها یا نهادهای شخص ثالث درایورهایی ایجاد می‌کنند
   که می‌توانند ResourceSliceها را در کلاستر ایجاد و مدیریت کنند. این درایورها
   به‌طور اختیاری DeviceClassهایی نیز ایجاد می‌کنند که یک دسته از دستگاه‌ها و
   نحوهٔ درخواست آن‌ها را تعریف می‌کنند.
1. **پیکربندی کلاستر**: مدیران کلاستر، کلاسترها را ایجاد می‌کنند، دستگاه‌ها را به
   نودها متصل می‌کنند و درایورهای دستگاه DRA را نصب می‌کنند. مدیران کلاستر به‌طور اختیاری
   DeviceClassهایی ایجاد می‌کنند که دسته‌هایی از دستگاه‌ها و نحوهٔ درخواست آن‌ها را تعریف می‌کنند.
1. **درخواست‌های منبع (Resource claims)**: گردانندگان بار کاری، ResourceClaimTemplateها یا
   ResourceClaimهایی ایجاد می‌کنند که پیکربندی‌های مشخصی از دستگاه را در یک
   DeviceClass درخواست می‌کنند. در همین مرحله، گردانندگان بار کاری مانیفست‌های کوبرنتیز
   خود را طوری تغییر می‌دهند که آن ResourceClaimTemplateها یا ResourceClaimها را درخواست کنند.

### گردش کار کوبرنتیز {#kubernetes-workflow}

1. **ایجاد ResourceSlice**: درایورهای موجود در کلاستر ResourceSliceهایی ایجاد می‌کنند که
   نمایانگر یک یا چند دستگاه در یک مخزن (pool) مدیریت‌شده از دستگاه‌های مشابه هستند.
1. **ایجاد بار کاری**: control plane کلاستر، بارهای کاری جدید را از نظر وجود ارجاع
   به ResourceClaimTemplateها یا ResourceClaimهای مشخص بررسی می‌کند.

   * اگر بار کاری از یک ResourceClaimTemplate استفاده کند، کنترل‌کننده‌ای به نام
     `resourceclaim-controller` برای آن بار کاری ResourceClaimهایی تولید می‌کند.
   * اگر بار کاری از یک ResourceClaim مشخص استفاده کند، کوبرنتیز بررسی می‌کند که آیا
     آن ResourceClaim در کلاستر وجود دارد یا نه. اگر ResourceClaim وجود نداشته
     باشد، Podها مستقر نخواهند شد.

1. **فیلتر کردن ResourceSliceها**: کوبرنتیز برای هر Pod، ResourceSliceهای کلاستر را
   بررسی می‌کند تا دستگاهی بیابد که همهٔ معیارهای
   زیر را برآورده کند:

   * نودهایی که می‌توانند به منابع دسترسی داشته باشند، واجد شرایط اجرای Pod باشند.
   * ResourceSlice منابع تخصیص‌نیافته‌ای داشته باشد که با الزامات
     ResourceClaim مربوط به Pod مطابقت کند.

1. **تخصیص منبع**: پس از یافتن یک ResourceSlice واجد شرایط برای ResourceClaim
   یک Pod، زمان‌بند کوبرنتیز ResourceClaim را با جزئیات تخصیص
   به‌روزرسانی می‌کند. زمان‌بند از راهبرد اولین تطابق (first-fit) استفاده می‌کند و
   مخزن‌ها و ResourceSliceها را به ترتیب واژه‌نامه‌ای (lexicographical) نام‌هایشان ارزیابی می‌کند.
   درایورها می‌توانند با نام‌گذاری مناسب، برش‌ها یا مخزن‌های مشخصی را در اولویت قرار دهند.
   برای جزئیات، به
   [نام‌گذاری و اولویت‌بندی](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceslice-naming-and-prioritization) مراجعه کنید.
1. **زمان‌بندی Pod**: پس از تکمیل تخصیص منبع، زمان‌بند
   Pod را روی نودی قرار می‌دهد که بتواند به منبع تخصیص‌یافته دسترسی داشته باشد. درایور
   دستگاه و `kubelet` روی آن نود از طریق gRPC با یکدیگر هماهنگ می‌شوند تا دستگاه
   و دسترسی Pod به دستگاه را پیکربندی کنند، مگر اینکه درایور برای دستگاه‌هایی که به آماده‌سازی یا پاک‌سازی محلی روی نود نیاز ندارند،
   [عملیات اختیاری نود](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#optional-node-operations)
   را اعلام کرده باشد.

## Podهای از پیش زمان‌بندی‌شده

وقتی شما یا یک کلاینت API دیگر، Podی ایجاد می‌کنید که `spec.nodeName` آن از قبل تنظیم شده است، زمان‌بند دور زده می‌شود.
اگر یکی از ResourceClaimهای موردنیاز آن Pod هنوز وجود نداشته باشد، تخصیص نیافته باشد
یا برای آن Pod رزرو نشده باشد، kubelet در اجرای Pod ناکام می‌ماند و
به‌طور دوره‌ای دوباره بررسی می‌کند، زیرا ممکن است آن الزامات بعداً برآورده شوند.

چنین وضعیتی همچنین ممکن است زمانی پیش آید که پشتیبانی از تخصیص پویای منابع
در زمان زمان‌بندی Pod در زمان‌بند فعال نبوده است
(ناهمخوانی نسخه‌ها، پیکربندی، feature gate و غیره). kube-controller-manager
این وضعیت را تشخیص می‌دهد و می‌کوشد با رزرو ResourceClaimهای موردنیاز، Pod را قابل اجرا کند.
با این حال، این کار تنها در صورتی جواب می‌دهد که آن ResourceClaimها توسط
زمان‌بند برای Pod دیگری تخصیص یافته باشند.

بهتر است از دور زدن زمان‌بند پرهیز کنید، زیرا Podی که به یک نود اختصاص داده شده است،
منابع عادی (RAM، CPU) را مسدود می‌کند و این منابع تا زمانی که Pod گیر کرده است
برای Podهای دیگر قابل استفاده نیستند. برای اینکه یک Pod روی نودی مشخص اجرا شود و در عین حال
از جریان عادی زمان‌بندی عبور کند، Pod را با یک انتخابگر نود (node selector) ایجاد کنید که
دقیقاً با نود موردنظر مطابقت داشته باشد:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-cats
spec:
  nodeSelector:
    kubernetes.io/hostname: name-of-the-intended-node
  ...
```

همچنین ممکن است بتوانید Pod ورودی را در زمان پذیرش (admission) تغییر دهید تا
فیلد `.spec.nodeName` حذف شود و به‌جای آن از یک انتخابگر نود استفاده شود.

## شرایط اتصال دستگاه (Device binding conditions)

{{< feature-state feature_gate_name="DRADeviceBindingConditions" >}}

شرایط اتصال دستگاه به زمان‌بند کوبرنتیز اجازه می‌دهند اتصال (binding) Pod را تا زمانی
به تأخیر بیندازد که آمادگی منابع خارجی، مانند GPUهای متصل به فابریک یا FPGAهای قابل برنامه‌ریزی مجدد،
تأیید شود.

این رفتار انتظار در
[مرحلهٔ PreBind](/docs/concepts/scheduling-eviction/scheduling-framework/#pre-bind)
چارچوب زمان‌بندی پیاده‌سازی شده است.
در این مرحله، زمان‌بند پیش از ادامهٔ اتصال بررسی می‌کند که آیا همهٔ شرایط موردنیاز دستگاه
برآورده شده‌اند یا نه.

این کار با جلوگیری از اتصال زودهنگام، قابلیت اطمینان زمان‌بندی را بهبود می‌بخشد و هماهنگی
با کنترل‌کننده‌های خارجی دستگاه را ممکن می‌سازد.

برای استفاده از این قابلیت، درایورهای دستگاه (که معمولاً توسط مالکان درایور مدیریت می‌شوند) باید
فیلدهای زیر را در بخش `Device` یک `ResourceSlice` منتشر کنند. مدیران کلاستر
باید feature gateهای `DRADeviceBindingConditions` و `DRAResourceClaimDeviceStatus`
را فعال کنند تا زمان‌بند این فیلدها را رعایت کند.

`bindingConditions`
: فهرستی از _انواع شرط (condition types)_ که باید پیش از اتصال Pod (در فیلد `.status.conditions` مربوط به ResourceClaim مرتبط) روی True تنظیم شوند. این شرط‌ها معمولاً نمایانگر سیگنال‌های آمادگی، مانند DeviceAttached یا DeviceInitialized، هستند.

`bindingFailureConditions`
: فهرستی از انواع شرط که اگر در
  فیلد status.conditions مربوط به ResourceClaim مرتبط روی True تنظیم شوند، نشان‌دهندهٔ وضعیت شکست هستند.
  اگر هر یک از این شرط‌ها True باشد، زمان‌بند اتصال را لغو می‌کند و Pod را دوباره زمان‌بندی می‌کند.

`bindsToNode`
: اگر روی `true` تنظیم شود، زمان‌بند نام نود انتخاب‌شده را در
  فیلد `status.allocation.nodeSelector` مربوط به ResourceClaim ثبت می‌کند.
  این کار بر `spec.nodeSelector` مربوط به Pod تأثیری ندارد. در عوض، یک انتخابگر نود
  درون ResourceClaim تنظیم می‌کند که کنترل‌کننده‌های خارجی می‌توانند از آن برای انجام عملیات
  مختص نود، مانند اتصال یا آماده‌سازی دستگاه، استفاده کنند.

همهٔ انواع شرط فهرست‌شده در bindingConditions و bindingFailureConditions از روی
فیلد `status.conditions` مربوط به ResourceClaim ارزیابی می‌شوند.
کنترل‌کننده‌های خارجی مسئول به‌روزرسانی این شرط‌ها با استفاده از معناشناسی استاندارد
شرط‌های کوبرنتیز (`type`، `status`، `reason`، `message`، `lastTransitionTime`) هستند.

زمان‌بند حداکثر **۶۰۰ ثانیه** (پیش‌فرض) منتظر می‌ماند تا همهٔ `bindingConditions` به `True` تبدیل شوند.
اگر این مهلت به پایان برسد یا هر یک از `bindingFailureConditions` برابر `True` باشد، زمان‌بند
تخصیص را پاک می‌کند و Pod را دوباره زمان‌بندی می‌کند.
مدیر کلاستر می‌تواند مدت این مهلت را با ویرایش فایل پیکربندی kube-scheduler تنظیم کند.

نمونه‌ای از پیکربندی این مهلت در `KubeSchedulerConfiguration` در ادامه آمده است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: default-scheduler
  pluginConfig:
  - name: DynamicResources
    args:
      apiVersion: kubescheduler.config.k8s.io/v1
      kind: DynamicResourcesArgs
      bindingTimeout: 60s
```

### مثال {#device-binding-conditions-example}

در اینجا نمونه‌ای از یک ResourceSlice آمده است که ممکن است در کلاستری ببینید که در آن یک درایور DRA در حال استفاده است و آن درایور از شرایط اتصال پشتیبانی می‌کند:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-slice-1
spec:
  driver: dra.example.com
  nodeSelector:
    nodeSelectorTerms:
    - matchExpressions:
      - key: accelerator-type
        operator: In
        values:
        - "high-performance"
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 1
  devices:
    - name: gpu-1
      attributes:
        vendor:
          string: "example"
        model:
          string: "example-gpu"
      bindsToNode: true
      bindingConditions:
        - dra.example.com/is-prepared
      bindingFailureConditions:
        - dra.example.com/preparing-failed
```
این ResourceSlice نمونه ویژگی‌های زیر را دارد:

- این ResourceSlice نودهایی را هدف می‌گیرد که برچسب `accelerator-type=high-performance` دارند،
تا زمان‌بند تنها از مجموعهٔ مشخصی از نودهای واجد شرایط استفاده کند.
- زمان‌بند یک نود را از گروه انتخاب‌شده برمی‌گزیند (برای مثال `node-3`) و
فیلد `status.allocation.nodeSelector` را در ResourceClaim روی نام آن نود تنظیم می‌کند.
- شرط اتصال `dra.example.com/is-prepared` نشان می‌دهد که دستگاه `gpu-1`
باید پیش از اتصال آماده شده باشد (وضعیت شرط `is-prepared` برابر `True` باشد).
- اگر آماده‌سازی دستگاه `gpu-1` با شکست مواجه شود (وضعیت شرط `preparing-failed` برابر `True` باشد)، زمان‌بند اتصال را لغو می‌کند.
- زمان‌بند حداکثر ۶۰۰ ثانیه (پیش‌فرض) منتظر می‌ماند تا دستگاه آماده شود.
- کنترل‌کننده‌های خارجی می‌توانند از انتخابگر نود موجود در ResourceClaim برای انجام
راه‌اندازی مختص نود روی نود انتخاب‌شده استفاده کنند.

قابلیت شرایط اتصال دستگاه توسط
[feature gate با نام `DRADeviceBindingConditions`](/docs/reference/command-line-tools-reference/feature-gates/#DRADeviceBindingConditions)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.


## منابع قابل تخصیص نود {#node-allocatable-resources}

{{< feature-state feature_gate_name="DRANodeAllocatableResources" >}}

دستگاه‌هایی که توسط DRA مدیریت می‌شوند، ممکن است ردپای زیربنایی‌ای متشکل از منابع قابل تخصیص نود،
مانند `cpu`، `memory` یا `hugepages`، داشته باشند.
این قابلیت، این درخواست‌های مبتنی بر DRA را در کنار درخواست‌های عادی `spec` مربوط به Pod
برای این منابع، در حسابداری استاندارد زمان‌بند ادغام می‌کند.

درایورهای DRA با استفاده از دو مدل متمایز تعریف می‌کنند که دستگاه‌ها چگونه منابع قابل تخصیص نود را مصرف می‌کنند:

*   **نگاشت مستقیم منبع (`mapping`)**: دستگاه DRA مستقیماً یک منبع استاندارد نود (مانند یک مخزن سفارشی از هسته‌های CPU یا یک بلوک حافظه) را فراهم می‌کند. تخصیص درخواست مستقیماً به ظرفیت استاندارد CPU یا حافظهٔ نود نگاشت می‌شود.
*   **سربار دستگاه کمکی (`overhead`)**: دستگاه DRA (مانند یک GPU یا شتاب‌دهنده) برای کار کردن، هنگامی که به یک Pod یا کانتینر تخصیص می‌یابد، به منابع میزبان (مانند RAM میزبان) به‌عنوان سربار ثانویه نیاز دارد.

### ملاحظات برای نویسندگان Pod

هنگام نوشتن یک PodSpec که از درخواست‌هایی برای این نوع دستگاه‌ها استفاده می‌کند، باید به چند نکته توجه داشته باشید:

*   وقتی از منابع سطح Pod استفاده می‌شود، زمان‌بند آن‌ها را به‌طور سخت‌گیرانه با درخواست‌ها و محدودیت‌های کانتینرها اعتبارسنجی می‌کند:
    *  مجموع درخواست‌های همهٔ کانتینرها و منابع درخواست‌های DRA نباید از درخواست‌های سطح Pod بیشتر شود؛ در غیر این صورت، زمان‌بندی Pod با شکست مواجه می‌شود.
    *  محدودیت هر کانتینر به‌علاوهٔ تخصیص‌های DRA آن نباید از محدودیت‌های سطح Pod بیشتر شود؛ در غیر این صورت، زمان‌بندی Pod با شکست مواجه می‌شود.
*   کل نیاز منبع یک کانتینر برابر است با مجموع منابع سطح کانتینر آن
    و هرگونه منابع قابل تخصیص نود از درخواست‌های منبع مرتبط با آن.
*   **محدودیت اشتراک درخواست**: درخواست‌هایی که از نگاشت مستقیم منبع (`mapping`) استفاده می‌کنند، نمی‌توانند بین چند Pod به اشتراک گذاشته شوند. درخواست‌های مربوط به دستگاه‌هایی
    که `overhead` دارند، می‌توانند از اشتراک دستگاه پشتیبانی کنند و سربار به‌ازای هر Pod یا هر کانتینر ردیابی می‌شود.
*   Podهایی که درخواست DRA دارند، از تغییر اندازهٔ درجا (in-place resizing) برای درخواست‌های استاندارد در `spec` پشتیبانی می‌کنند. زمان‌بند اطمینان حاصل می‌کند
    که درخواست‌های استاندارد تغییر اندازه‌یافته، همراه با تخصیص‌های ثابت DRA، همچنان در نود جا می‌شوند.

### جزئیات برای نویسندگان درایور DRA

درایورهای DRA این ردپای منابع قابل تخصیص نود را با استفاده از
فیلد `nodeAllocatableResources` روی دستگاه‌های درون یک ResourceSlice اعلام می‌کنند.
این فیلد نحوهٔ ترجمهٔ دستگاه یا ظرفیت DRA درخواست‌شده به منابع استانداردی را تعریف می‌کند
که در `status.allocatable` نود ردیابی می‌شوند (توجه داشته باشید که منابع
توسعه‌یافته (extended resources) برای این فیلد پشتیبانی نمی‌شوند). این قابلیت هم برای درایورهایی که مستقیماً
منابع بومی را در اختیار می‌گذارند (مانند یک درایور DRA برای CPU یا حافظه) و هم برای دستگاه‌هایی که
به وابستگی‌های کمکی نود نیاز دارند (مانند شتاب‌دهنده‌ای که به حافظهٔ میزبان نیاز دارد) مفید است.

فیلد `nodeAllocatableResources` از دو مورد استفادهٔ متفاوت پشتیبانی می‌کند:

*   **نگاشت (Mapping)**: زمانی استفاده می‌شود که دستگاه DRA مستقیماً نمایانگر منبع استاندارد باشد
    (برای مثال، یک درایور DRA برای CPU یا حافظه). زمان‌بند مقدار دقیق را
    با مقیاس‌دهی ظرفیت با استفاده از `capacityMultiplier`، یا مقیاس‌دهی تعداد دستگاه‌ها
    با استفاده از `deviceMultiplier` محاسبه می‌کند.
*   **سربار (Overhead)**: زمانی استفاده می‌شود که دستگاه به وابستگی‌های کمکی نود نیاز داشته باشد (برای مثال،
    حافظهٔ میزبانی که توسط یک GPU مصرف می‌شود). این مقدار می‌تواند به‌صورت یک هزینهٔ ثابت `perPod` یا
    یک هزینهٔ متغیر `perContainer` تعریف شود که به‌صورت خطی با تعداد
    کانتینرهای ارجاع‌دهنده افزایش می‌یابد.

#### مثال: درایور DRA برای CPU (نگاشت)

در اینجا مثالی آمده است که در آن یک درایور DRA برای CPU، یک سوکت CPU را به‌صورت مخزنی از ۱۲۸
CPU با استفاده از [ظرفیت مصرفی DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) در اختیار می‌گذارد. کلید `capacityKey` ظرفیت مصرف‌شدهٔ
`cpu.example.com/cpu` را مستقیماً به منبع قابل تخصیص استاندارد `cpu`
نود پیوند می‌دهد:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-cpus
spec:
  driver: cpu.example.com
  nodeName: my-node
  pool:
    name: socket-cpus
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: socket0cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResources:
      mapping:
        cpu:
          capacityKey: "cpu.example.com/cpu"
  - name: socket1cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResources:
      mapping:
        cpu:
          capacityKey: "cpu.example.com/cpu"
          capacityMultiplier: 1
```

#### مثال: شتاب‌دهنده با منابع کمکی (سربار)

در اینجا نمونه‌ای از یک resource slice آمده است که در آن یک شتاب‌دهنده برای کار کردن
به‌ازای هر Pod به ۸Gi حافظهٔ اضافی نیاز دارد:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-xpus
spec:
  driver: xpu.example.com
  nodeName: my-node
  pool:
    name: xpu-pool
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: xpu-model-x-001
    attributes:
      example.com/model:
        string: "model-x"
    nodeAllocatableResources:
      overhead:
        memory:
          perPod: "8Gi"
```

پس از اینکه یک Pod با موفقیت به نود متصل شد، مقادیر دقیق
منابع قابل تخصیص نود که از طریق DRA تخصیص یافته‌اند، توسط `kube-scheduler` تجمیع می‌شوند
و مستقیماً در فیلد `status.nodeAllocatableResourceClaimStatuses` مربوط به Pod درج می‌شوند.
این کار یک تحویل روشن و ماندگار از زمان‌بند به `kubelet` فراهم می‌کند.

نکتهٔ مهم این است که `kubelet` به‌طور بومی این API را مصرف می‌کند تا مرزهای سطح سیستم را به‌طور کامل هم‌راستا کند:
- **cgroups**: cgroupهای Pod و کانتینر اکنون تخصیص‌های مبتنی بر DRA را نیز شامل می‌شوند و از محدودسازی مصنوعی بارهای کاری توسط کرنل جلوگیری می‌کنند.
- **امتیازهای OOM**: `kubelet` درخواست‌های حافظهٔ DRA کانتینر را در درخواست حافظهٔ مؤثر آن لحاظ می‌کند.

منابع قابل تخصیص نود یک قابلیت آلفا است و زمانی فعال می‌شود که
[feature gate با نام `DRANodeAllocatableResources`](/docs/reference/command-line-tools-reference/feature-gates/#DRANodeAllocatableResources) در `kube-apiserver`،
`kube-scheduler` و `kubelet` فعال باشد.

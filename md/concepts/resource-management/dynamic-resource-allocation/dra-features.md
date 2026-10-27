---
reviewers:
- klueska
- pohly
title: ویژگی‌های DRA
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه ویژگی‌های اختیاری DRA را برای موارد استفاده پیشرفته توضیح می‌دهد. برخی از
این ویژگی‌ها به پشتیبانی از سوی درایور DRA نیاز دارند. در مورد هر ویژگی، سطح بلوغ آن و
feature gate فعال‌کننده‌اش ذکر شده است.

<!-- body -->

## دستگاه‌های قابل‌پارتیشن‌بندی {#partitionable-devices}

{{< feature-state feature_gate_name="DRAPartitionableDevices" >}}

دستگاه‌هایی که در DRA نمایش داده می‌شوند لزوماً یک واحد منفرد متصل به یک ماشین نیستند،
بلکه می‌توانند یک دستگاه منطقی باشند که از چندین دستگاه متصل به چندین ماشین تشکیل شده است.
این دستگاه‌ها ممکن است منابع هم‌پوشان دستگاه‌های فیزیکی زیرین را مصرف کنند؛
به این معنا که وقتی یک دستگاه منطقی تخصیص داده می‌شود، سایر دستگاه‌ها دیگر در دسترس نخواهند بود.

در API مربوط به ResourceSlice، این موضوع به‌صورت فهرستی از CounterSetهای نام‌گذاری‌شده نمایش داده می‌شود که هر یک
شامل مجموعه‌ای از شمارنده‌های (counter) نام‌گذاری‌شده است. این شمارنده‌ها منابع موجود در دستگاه فیزیکی را نشان می‌دهند
که توسط دستگاه‌های منطقی اعلام‌شده از طریق DRA مصرف می‌شوند.

دستگاه‌های منطقی می‌توانند فهرست ConsumesCounters را مشخص کنند. هر مدخل شامل ارجاعی به یک CounterSet
و مجموعه‌ای از شمارنده‌های نام‌گذاری‌شده همراه با مقادیری است که مصرف خواهند کرد. بنابراین برای اینکه یک دستگاه قابل تخصیص باشد،
مجموعه‌های شمارنده‌ی ارجاع‌شده باید مقدار کافی برای شمارنده‌هایی که دستگاه به آن‌ها ارجاع می‌دهد داشته باشند.

CounterSetها باید در ResourceSliceهایی جدا از دستگاه‌ها مشخص شوند.
دستگاه‌ها می‌توانند از هر CounterSet که در همان resource pool دستگاه تعریف شده است، شمارنده مصرف کنند.

در ادامه مثالی از دو دستگاه آمده است که هر یک ۶ گیبی‌بایت (6Gi) حافظه را از یک شمارنده‌ی مشترک با ۸ گیبی‌بایت (8Gi) حافظه مصرف می‌کنند.
بنابراین در هر لحظه فقط یکی از این دستگاه‌ها قابل تخصیص است.
زمان‌بند این موضوع را مدیریت می‌کند و برای مصرف‌کننده شفاف است، زیرا API مربوط به ResourceClaim تحت تأثیر قرار نمی‌گیرد.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-countersets
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  sharedCounters:
  - name: gpu-1-counters
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-devices
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  devices:
  - name: device-1
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
  - name: device-2
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
```

دستگاه‌های قابل‌پارتیشن‌بندی توسط
[feature gate با نام `DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.


## گروه‌های سازگاری دستگاه {#device-compatibility-groups}

{{< feature-state feature_gate_name="DRADeviceCompatibilityGroups" >}}

گروه‌های سازگاری دستگاه به درایور DRA امکان می‌دهند اعلام کند کدام دستگاه‌های پارتیشن‌بندی‌شده
می‌توانند هم‌زمان روی یک سخت‌افزار فیزیکی تخصیص داده شوند. بدون این ویژگی،
ترکیب‌های ناسازگار دستگاه‌ها فقط زمانی شناسایی می‌شوند که kubelet در حال آماده‌سازی
Pod روی یک نود است که به شکست در آماده‌سازی منجر می‌شود. با وجود گروه‌های سازگاری،
زمان‌بند ترکیب‌های ناسازگار را در زمان زمان‌بندی و پیش از آغاز هرگونه کار سمت نود رد می‌کند.

این ویژگی بیش از همه برای سخت‌افزارهایی مفید است که از حالت‌های عملیاتی متقابلاً ناسازگار پشتیبانی می‌کنند.
برای مثال، یک GPU که می‌تواند یا در حالت MIG یا در حالت vGPU اجرا شود: یک
دستگاه در حالت MIG و یک دستگاه در حالت vGPU نمی‌توانند هم‌زمان تخصیص داده شوند، زیرا
منابع فیزیکی هم‌پوشان را به شیوه‌هایی ناسازگار مصرف می‌کنند. درایور با اعلام
`compatibilityGroups` این محدودیت را برای زمان‌بند قابل مشاهده می‌کند.

این ویژگی بر پایه‌ی [دستگاه‌های قابل‌پارتیشن‌بندی](#partitionable-devices) ساخته شده است:
فیلد `compatibilityGroups` روی مدخل‌های `device.consumesCounters[]` قرار دارد که
تنها برای دستگاه‌های قابل‌پارتیشن‌بندی وجود دارند. هر دو feature gate با نام‌های `DRADeviceCompatibilityGroups`
و `DRAPartitionableDevices` باید در `kube-apiserver` و `kube-scheduler` فعال باشند.

### نحوه‌ی کار {#device-compatibility-groups-how-it-works}

درایور برای هر مدخل `device.consumesCounters[]` در یک ResourceSlice، یک فهرست
`compatibilityGroups` تعریف می‌کند. این فهرست حداکثر ۲ نام رشته‌ای مبهم (opaque) دارد که نشان‌دهنده‌ی حالت عملیاتی
یا نوع پارتیشن آن دستگاه روی آن counter set مشخص است.

وقتی زمان‌بند چند دستگاه را که از همان counter set مصرف می‌کنند تخصیص می‌دهد، اشتراک
`compatibilityGroups` آن‌ها را محاسبه می‌کند. تخصیص فقط زمانی موفق می‌شود که این اشتراک
تهی نباشد؛ یعنی هر دستگاهِ هم‌تخصیص‌یافته دست‌کم یک نام گروه مشترک داشته باشد.
دستگاه‌هایی که از counter setهای متفاوت مصرف می‌کنند هرگز با یکدیگر مقایسه نمی‌شوند.

دستگاهی که هیچ گروهی اعلام نکرده باشد (فهرست تنظیم‌نشده، nil یا خالی) یک
حالت خاص محسوب می‌شود: این دستگاه فقط با سایر دستگاه‌های بدون گروه روی همان counter set
قابل هم‌تخصیص است. هرگز با دستگاهی که یک یا چند گروه اعلام کرده باشد قابل هم‌تخصیص نیست.

این محدودیت در تمام claimهایی که در یک چرخه‌ی زمان‌بندی تخصیص داده می‌شوند اعمال می‌شود:
اگر دو claim هر یک دستگاهی از همان counter set را تخصیص دهند، اشتراک گروه‌ها
میان claimها نیز اعمال می‌شود.

### مثال {#device-compatibility-groups-example}

GPUی را در نظر بگیرید که می‌تواند یا در حالت MIG یا در حالت vGPU کار کند. درایور
دو دستگاه منتشر می‌کند که هر یک ۴ گیبی‌بایت (4 GiB) از همان شمارنده‌ی حافظه‌ی مشترک
۸ گیبی‌بایتی را مصرف می‌کنند. تنها بر اساس ظرفیت شمارنده، هر دو دستگاه می‌توانستند با هم تخصیص داده شوند.
هر دستگاه حالت عملیاتی خود را به‌عنوان یک گروه سازگاری اعلام می‌کند
و بدین ترتیب این دو حالت را متقابلاً ناسازگار می‌سازد:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-counters
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  sharedCounters:
  - name: gpu-0-memory
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-devices
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  devices:
  - name: gpu-0-mig
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - mig
  - name: gpu-0-vgpu
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - vgpu
```

در این مثال:
- `gpu-0-mig` به گروه `mig` تعلق دارد.
- `gpu-0-vgpu` به گروه `vgpu` تعلق دارد.

اگر یک Pod یا PodGroup دو دستگاه از این pool درخواست کند، زمان‌بند بررسی می‌کند
که آیا دو دستگاه انتخاب‌شده روی counter set با نام `gpu-0-memory` یک گروه سازگاری مشترک دارند یا خیر.
از آنجا که `{"mig"} ∩ {"vgpu"} = ∅`، این جفت رد می‌شود، حتی اگر counter set حافظه‌ی کافی برای هر دو داشته باشد.
هر دو درخواست فقط با دو دستگاه MIG (یا دو دستگاه vGPU) از
poolی که چنین جفت‌هایی در آن وجود دارد برآورده می‌شوند.

### محدودیت‌ها {#device-compatibility-groups-constraints}

- هر مدخل `consumesCounters[]` می‌تواند حداکثر **۲** نام گروه اعلام کند.
- نام گروه‌ها در یک مدخل واحد باید یکتا باشند.
- نام گروه‌ها برای کوبرنتیز مبهم (opaque) هستند؛ آن‌ها فقط در چارچوب pool
  درایور منتشرکننده معنا دارند.
- گروه‌ها به‌ازای هر counter set مقایسه می‌شوند: گروه‌های یک counter set هیچ تأثیری
  بر تصمیم‌های هم‌تخصیص برای counter set دیگر ندارند.

### ایمنی در برابر ناهمگونی نسخه‌ها {#device-compatibility-groups-version-skew}

وقتی feature gate با نام `DRADeviceCompatibilityGroups` غیرفعال است (پیش‌فرض در
مرحله‌ی آلفا)، kube-apiserver فیلد `compatibilityGroups` را از هر ResourceSlice
جدید یا به‌روزرسانی‌شده حذف می‌کند، مگر اینکه آبجکت قدیمی از قبل این فیلد را
تنظیم‌شده داشته باشد. در این حالت زمان‌بند دستگاه‌های هر pool را که پیش‌تر دستگاه‌های گروه‌دار داشته است
به‌عنوان بخشی از یک pool ناقص در نظر می‌گیرد و به‌طور کامل از آن‌ها صرف‌نظر می‌کند.

فقط یک فهرست غیرخالی به‌منزله‌ی تنظیم‌شدن فیلد به‌شمار می‌آید: `compatibilityGroups: null`
و `compatibilityGroups: []` دقیقاً مانند حذف فیلد رفتار می‌شوند.
دستگاه‌هایی که این مقادیر را دارند دقیقاً مانند دستگاه‌های بدون گروه عمل می‌کنند و
باعث نمی‌شوند زمان‌بند pool را ناقص در نظر بگیرد.

گروه‌های سازگاری دستگاه توسط
[feature gate با نام `DRADeviceCompatibilityGroups`](/docs/reference/command-line-tools-reference/feature-gates/#DRADeviceCompatibilityGroups)
در kube-apiserver و kube-scheduler کنترل می‌شود.
[feature gate با نام `DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
نیز باید فعال باشد.

## ظرفیت قابل مصرف {#consumable-capacity}

{{< feature-state feature_gate_name="DRAConsumableCapacity" >}}

ویژگی ظرفیت قابل مصرف (consumable capacity) اجازه می‌دهد یک دستگاه واحد توسط چندین ResourceClaim مستقل مصرف شود
و زمان‌بند کوبرنتیز مدیریت کند که هر claim چه مقدار از ظرفیت دستگاه را مصرف می‌کند.
این موضوع مشابه نحوه‌ای است که Podها می‌توانند منابع یک نود را به اشتراک بگذارند؛ ResourceClaimها می‌توانند منابع یک دستگاه را به اشتراک بگذارند.

درایور دستگاه می‌تواند فیلد `allowMultipleAllocations` را که در `.spec.devices` از `ResourceSlice` افزوده شده است تنظیم کند
تا تخصیص آن دستگاه به چند ResourceClaim مستقل یا به چند درخواست درون یک ResourceClaim مجاز شود.

هنگام درخواست دقیقاً یک نوع دستگاه در یک `ResourceClaim`، فیلد
`spec.devices.requests[].exactly.capacity` را برای مشخص کردن نیازمندی‌های منبع دستگاه
در هر تخصیص تنظیم کنید. برای فهرستی اولویت‌دار از گزینه‌های مختلف، `capacity` را درون
مدخل‌های مربوط به `spec.devices.requests[].firstAvailable[]` تنظیم کنید.

برای دستگاهی که تخصیص‌های متعدد را مجاز می‌کند، ظرفیت درخواستی از ظرفیت کل آن برداشت (یا مصرف) می‌شود؛
مفهومی که **ظرفیت قابل مصرف** نامیده می‌شود.
سپس زمان‌بند اطمینان حاصل می‌کند که مجموع ظرفیت مصرف‌شده در تمام claimها از ظرفیت کلی دستگاه فراتر نرود.
علاوه بر این، نویسندگان درایور می‌توانند با استفاده از محدودیت‌های `requestPolicy` روی ظرفیت‌های منفرد دستگاه کنترل کنند
که این ظرفیت‌ها چگونه مصرف شوند.
برای مثال، نویسنده‌ی درایور می‌تواند مشخص کند که یک ظرفیت معین فقط در گام‌های ۱ گیبی‌بایت (1Gi) مصرف شود.

در ادامه مثالی از یک دستگاه شبکه آمده است که تخصیص‌های متعدد را مجاز می‌کند و یک ظرفیت قابل مصرف پهنای باند دارد.

```yaml
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: eth1
    allowMultipleAllocations: true
    attributes:
      name:
        string: "eth1"
    capacity:
      bandwidth:
        requestPolicy:
          default: "1M"
          validRange:
            min: "1M"
            step: "8"
        value: "10G"
```

ظرفیت قابل مصرف را می‌توان همان‌طور که در مثال زیر نشان داده شده است درخواست کرد.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: bandwidth-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          capacity:
            requests:
              bandwidth: 1G
```

نتیجه‌ی تخصیص شامل ظرفیت مصرف‌شده و شناسه‌ی سهم (share) خواهد بود.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - consumedCapacity:
          bandwidth: 1G
        device: eth1
        shareID: "a671734a-e8e5-11e4-8fde-42010af09327"
```

در این مثال، یک دستگاه با قابلیت تخصیص چندگانه انتخاب شده است. با این حال، هر دستگاه `resource.example.com`
که دست‌کم پهنای باند ۱G درخواستی را داشته باشد می‌توانست این نیاز را برآورده کند.
اگر دستگاهی بدون قابلیت تخصیص چندگانه انتخاب می‌شد، تخصیص به کل آن دستگاه منجر می‌شد.
برای اجبار به استفاده‌ی صرف از دستگاه‌های دارای قابلیت تخصیص چندگانه، می‌توانید از معیار CEL با عبارت `device.allowMultipleAllocations == true` استفاده کنید.

### محدودیت DistinctAttribute {#distinctattribute-constraint}

هنگام درخواست چند دستگاه در یک ResourceClaim، می‌توانید از محدودیت DistinctAttribute
استفاده کنید تا اطمینان یابید که هر دستگاه تخصیص‌یافته برای یک
attribute مشخص مقدار متفاوتی دارد. این محدودیت همراه با ویژگی ظرفیت قابل مصرف معرفی شد.

محدودیت DistinctAttribute به‌ویژه هنگام کار با
دستگاه‌های دارای قابلیت تخصیص چندگانه مفید است. این محدودیت از تخصیص چندباره‌ی یک
دستگاه واحد در یک ResourceClaim توسط زمان‌بند جلوگیری می‌کند، حتی زمانی که آن دستگاه
تخصیص‌های متعدد را مجاز می‌داند.

علاوه بر جلوگیری از تخصیص‌های تکراری، این محدودیت با اطمینان از توزیع دستگاه‌ها بر اساس attributeهایشان
به بهینه‌سازی عملکرد کمک می‌کند. برای مثال، می‌توانید
از آن برای توزیع دستگاه‌ها در نودهای NUMA مختلف استفاده کنید تا پهنای باند حافظه بهینه شود
و رقابت کاهش یابد.


## مجوزدهی granular برای status {#granular-status-authorization}

{{< feature-state feature_gate_name="DRAResourceClaimGranularStatusAuthorization" >}}

از کوبرنتیز نسخه‌ی v1.36، DRA برای به‌روزرسانی‌های status مربوط به `ResourceClaim`
بررسی‌های مجوزدهی ریزدانه را با استفاده از زیرمنبع‌های مصنوعی (synthetic subresources) و فعل‌های آگاه از نود (node-aware verbs) اعمال می‌کند.

برای راهنمای سخت‌سازی امنیتی، شامل نمونه‌های RBAC برای زمان‌بند و درایورهای DRA،
به
[راهنمای سخت‌سازی - تخصیص پویای منابع](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
مراجعه کنید.

برای روش گام‌به‌گام مدیر کلاستر، به
[سخت‌سازی تخصیص پویای منابع در کلاستر شما](/docs/tasks/administer-cluster/hardening-dra/)
مراجعه کنید.


## عملیات اختیاری نود {#optional-node-operations}

{{< feature-state feature_gate_name="DRAOptionalNodeOperations" >}}

در تخصیص پویای منابع (DRA)، `kubelet` از طریق gRPC با یک درایور محلی نود هماهنگ می‌شود
تا دستگاه‌های تخصیص‌یافته را پیش از شروع کانتینر آماده کند
(`NodePrepareResources`) و پس از پایان Pod آن‌ها را از حالت آماده خارج کند
(`NodeUnprepareResources`). اگرچه این ساختار برای سخت‌افزارهای محلی نود
مانند GPUها یا FPGAها حیاتی است، برخی منابع به‌طور کامل در control plane مدیریت می‌شوند
و به هیچ راه‌اندازی محلی نود نیاز ندارند.

ویژگی عملیات اختیاری نود به درایورهای منابع اجازه می‌دهد اعلام کنند که
عملیات gRPC محلی نود مشخصی را می‌توان نادیده گرفت. در صورت پیکربندی، `kubelet`
جست‌وجوی درایور و فراخوانی‌های gRPC را برای آن دستگاه‌ها دور می‌زند و نیاز به
استقرار و نگهداری درایورهای محلی نود خالی روی هر نود کارگر را از بین می‌برد.

### پیکربندی درایور {#driver-configuration}

نویسندگان درایور می‌توانند فیلد `skipNodeOperations` را در
`.spec.skipNodeOperations` از یک ResourceSlice مشخص کنند. این فیلد فهرستی از رشته‌های
یکتا است که عملیات محلی نودی را که باید برای تمام دستگاه‌های آن
slice نادیده گرفته شوند مشخص می‌کند.

مقادیر معتبر عبارت‌اند از:

* `"NodePrepareResources"`: فراخوانی‌های gRPC با نام `NodePrepareResources` را نادیده می‌گیرد. این مقدار
  نمی‌تواند مشخص شود مگر اینکه `"NodeUnprepareResources"` نیز در فهرست آمده باشد (یا `"*"`
  مشخص شده باشد). این محدودیت از گیرکردن Podها در وضعیت Terminating جلوگیری می‌کند، در صورتی که
  افزونه‌ی محلی نود وجود نداشته باشد؛ زیرا وقتی آماده‌سازی نادیده گرفته می‌شود،
  افزونه در زمان راه‌اندازی Pod بررسی نمی‌شود.
* `"NodeUnprepareResources"`: فراخوانی‌های gRPC با نام `NodeUnprepareResources` را نادیده می‌گیرد.
* `"*"`: تمام عملیات منبع محلی نود را نادیده می‌گیرد.

در ادامه مثالی از یک ResourceSlice برای منبعی در control plane آمده است که
تمام عملیات محلی نود را نادیده می‌گیرد:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: control-plane-resources
spec:
  nodeName: worker-1
  pool:
    name: central-pool
    generation: 1
    resourceSliceCount: 1
  driver: control-plane.example.com
  skipNodeOperations:
  - "*"
  devices:
  - name: virtual-device-1
```

### نتیجه‌ی تخصیص و اجرا {#allocation-result-and-execution}

وقتی زمان‌بند کوبرنتیز یک دستگاه را به یک ResourceClaim تخصیص می‌دهد، فهرست
`skipNodeOperations` را از ResourceSlice به نتیجه‌ی تخصیص کپی می‌کند:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - device: virtual-device-1
        driver: control-plane.example.com
        pool: central-pool
        skipNodeOperations:
        - "*"
```

وقتی یک Pod روی یک نود اجرا می‌شود، `kubelet` نتایج تخصیص را می‌خواند. اگر تمام
دستگاه‌های تخصیص‌یافته برای یک درایور مشخص در یک ResourceClaim یک عملیات معین را
نادیده بگیرند، `kubelet` فراخوانی آن hook از نوع gRPC را برای آن
درایور به‌طور کامل دور می‌زند.

### ملاحظات عملیاتی {#operational-considerations}

#### به‌روزرسانی درجای درایور {#in-place-driver-updates}

از آنجا که تنظیم `skipNodeOperations` در زمان تخصیص از ResourceSlice به
ResourceClaim کپی می‌شود، Podهای در حال اجرا و تخصیص‌های فعال
همان تنظیمی را حفظ می‌کنند که در زمان زمان‌بندی آن‌ها برقرار بوده است.

اگر نیازمندی‌های عملیات نود یک درایور به‌صورت درجا به‌روزرسانی شود (برای مثال،
تغییر از نیاز به عملیات نود به نادیده گرفتن آن‌ها)، claimهای موجود همچنان
از پیکربندی قبلی استفاده خواهند کرد. برای پرهیز از مشکلاتی مانند
گیر کردن Podهای در حال پایان یافتن در انتظار یک افزونه‌ی نود برچیده‌شده، مدیران کلاستر
باید پیش از تغییر نیازمندی‌های عملیات نود یک درایور یا حذف DaemonSetهای درایور محلی نود،
اطمینان یابند که هیچ claim فعالی برای آن درایور وجود ندارد.

#### یکپارچگی با Node Declared Features {#node-declared-features-integration}

برای جلوگیری از زمان‌بندی Podها روی نودهایی که `kubelet` آن‌ها از
نادیده گرفتن عملیات DRA پشتیبانی نمی‌کند (که باعث می‌شود `kubelet` هنگام
انتظار برای یک افزونه‌ی نود غایب با شکست مواجه شود)، این ویژگی با [Node Declared
Features](/docs/concepts/scheduling-eviction/node-declared-features/) یکپارچه می‌شود. وقتی
یک Pod از ResourceClaimی استفاده می‌کند که `skipNodeOperations` در آن پیکربندی شده است،
زمان‌بند کوبرنتیز پیش از زمان‌بندی Pod بررسی می‌کند که نود هدف
پشتیبانی از ویژگی `DRAOptionalNodeOperations` را در `.status.declaredFeatures` خود اعلام کرده باشد.

عملیات اختیاری نود توسط
feature gate با نام [`DRAOptionalNodeOperations`](/docs/reference/command-line-tools-reference/feature-gates/#DRAOptionalNodeOperations)
در `kube-apiserver`، `kube-scheduler` و `kubelet` کنترل می‌شود.

---
reviewers:
- klueska
- pohly
title: ویژگی‌های DRA
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه ویژگی‌های اختیاری DRA را برای موارد استفادهٔ پیشرفته شرح می‌دهد. برخی از این ویژگی‌ها به پشتیبانی درایور DRA نیاز دارند. برای هر ویژگی، سطح بلوغ آن و feature gate فعال‌کننده‌اش ذکر شده است.

<!-- body -->

## دستگاه‌های قابل‌تقسیم {#partitionable-devices}

{{< feature-state feature_gate_name="DRAPartitionableDevices" >}}

دستگاه‌هایی که در DRA نمایش داده می‌شوند لزوماً یک واحد منفرد متصل به یک ماشین نیستند. آن‌ها می‌توانند دستگاهی منطقی نیز باشند که از چندین دستگاه متصل به چندین ماشین تشکیل شده است. این دستگاه‌ها ممکن است منابع هم‌پوشانِ دستگاه‌های فیزیکی زیربنایی را مصرف کنند؛ یعنی با تخصیص یک دستگاه منطقی، دستگاه‌های دیگر دیگر در دسترس نخواهند بود.

در API مربوط به ResourceSlice، این موضوع به‌صورت فهرستی از CounterSetهای نام‌دار نمایش داده می‌شود که هر کدام مجموعه‌ای از شمارنده‌های (counter) نام‌دار را در بر دارد. این شمارنده‌ها نمایانگر منابع موجود روی دستگاه فیزیکی هستند که دستگاه‌های منطقیِ اعلام‌شده از طریق DRA از آن‌ها استفاده می‌کنند.

دستگاه‌های منطقی می‌توانند فهرست ConsumesCounters را مشخص کنند. هر مدخل این فهرست شامل ارجاعی به یک CounterSet و مجموعه‌ای از شمارنده‌های نام‌دار همراه با مقداری است که مصرف خواهند کرد. بنابراین، برای اینکه یک دستگاه قابل‌تخصیص باشد، مجموعه‌های شمارندهٔ ارجاع‌شده باید برای شمارنده‌هایی که دستگاه به آن‌ها ارجاع داده است، مقدار کافی داشته باشند.

مجموعه‌های شمارنده (CounterSet) باید در ResourceSliceهایی جدا از ResourceSliceهای دستگاه‌ها مشخص شوند. دستگاه‌ها می‌توانند از هر CounterSet تعریف‌شده در همان استخر منابع (resource pool) دستگاه، شمارنده مصرف کنند.

در ادامه نمونه‌ای از دو دستگاه آمده است که هر کدام 6Gi حافظه از یک شمارندهٔ مشترک با 8Gi حافظه مصرف می‌کنند. بنابراین، در هر لحظه فقط یکی از این دستگاه‌ها قابل تخصیص است. زمان‌بند این موضوع را مدیریت می‌کند و از آنجا که API مربوط به ResourceClaim تحت تأثیر قرار نمی‌گیرد، این فرایند برای مصرف‌کننده شفاف است.

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

قابلیت دستگاه‌های قابل‌تقسیم با
[feature gate `DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.


## گروه‌های سازگاری دستگاه {#device-compatibility-groups}

{{< feature-state feature_gate_name="DRADeviceCompatibilityGroups" >}}

گروه‌های سازگاری دستگاه به درایور DRA امکان می‌دهند اعلام کند کدام دستگاه‌های تقسیم‌شده را می‌توان هم‌زمان روی یک سخت‌افزار فیزیکی تخصیص داد. بدون این ویژگی، ترکیب‌های ناسازگار دستگاه‌ها تنها زمانی شناسایی می‌شوند که kubelet در حال آماده‌سازی Pod روی نود است و نتیجهٔ آن، شکست در آماده‌سازی است. با گروه‌های سازگاری، زمان‌بند ترکیب‌های ناسازگار را در زمان زمان‌بندی و پیش از آغاز هر کاری در سمت نود رد می‌کند.

این قابلیت بیش از همه برای سخت‌افزارهایی مفید است که از حالت‌های عملیاتی متقابلاً انحصاری پشتیبانی می‌کنند. برای مثال، یک GPU را در نظر بگیرید که می‌تواند در حالت MIG یا حالت vGPU کار کند: دستگاهی در حالت MIG و دستگاهی در حالت vGPU را نمی‌توان هم‌زمان تخصیص داد، زیرا آن‌ها منابع فیزیکی هم‌پوشان را به شیوه‌هایی ناسازگار مصرف می‌کنند. درایور با اعلام `compatibilityGroups` این محدودیت را برای زمان‌بند قابل‌مشاهده می‌کند.

این ویژگی بر پایهٔ [دستگاه‌های قابل‌تقسیم](#partitionable-devices) بنا شده است: فیلد `compatibilityGroups` در مدخل‌های `device.consumesCounters[]` قرار دارد که تنها برای دستگاه‌های قابل‌تقسیم وجود دارند. هر دو feature gate یعنی `DRADeviceCompatibilityGroups` و `DRAPartitionableDevices` باید در `kube-apiserver` و `kube-scheduler` فعال باشند.

### نحوهٔ کار {#device-compatibility-groups-how-it-works}

درایور برای هر مدخل `device.consumesCounters[]` در یک ResourceSlice، فهرستی به نام `compatibilityGroups` تعریف می‌کند. این فهرست حداکثر ۲ نام رشته‌ای غیرشفاف (opaque) دارد که نمایانگر حالت عملیاتی یا نوع پارتیشن آن دستگاه روی آن مجموعهٔ شمارندهٔ خاص هستند.

وقتی زمان‌بند چند دستگاه را تخصیص می‌دهد که از یک مجموعهٔ شمارندهٔ یکسان برداشت می‌کنند، اشتراک `compatibilityGroups` آن‌ها را محاسبه می‌کند. تخصیص تنها در صورتی موفق است که این اشتراک ناتهی باشد؛ یعنی همهٔ دستگاه‌هایی که هم‌زمان تخصیص می‌یابند، دست‌کم یک نام گروه مشترک داشته باشند. دستگاه‌هایی که از مجموعه‌های شمارندهٔ متفاوت برداشت می‌کنند، هرگز با یکدیگر مقایسه نمی‌شوند.

دستگاهی که هیچ گروهی اعلام نمی‌کند (فهرستی تنظیم‌نشده، nil یا خالی) حالتی ویژه در نظر گرفته می‌شود: این دستگاه را تنها می‌توان هم‌زمان با دیگر دستگاه‌های بدون گروه روی همان مجموعهٔ شمارنده تخصیص داد. چنین دستگاهی هرگز هم‌زمان با دستگاهی که یک یا چند گروه اعلام کرده است، قابل تخصیص نیست.

این محدودیت بر همهٔ claimهایی که در یک چرخهٔ زمان‌بندی واحد تخصیص داده می‌شوند اعمال می‌شود: اگر دو claim هر کدام دستگاهی از یک مجموعهٔ شمارندهٔ یکسان تخصیص دهند، شرط اشتراک گروه‌ها میان این claimها نیز اعمال می‌شود.

### نمونه {#device-compatibility-groups-example}

یک GPU را در نظر بگیرید که می‌تواند در حالت MIG یا حالت vGPU کار کند. درایور دو دستگاه منتشر می‌کند که هر کدام 4 GiB از یک شمارندهٔ حافظهٔ مشترک 8 GiB مصرف می‌کنند. اگر فقط ظرفیت شمارنده ملاک باشد، می‌توان هر دو دستگاه را با هم تخصیص داد. هر دستگاه حالت عملیاتی خود را به‌عنوان یک گروه سازگاری اعلام می‌کند و به این ترتیب، دو حالت متقابلاً انحصاری می‌شوند:

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
- دستگاه `gpu-0-mig` به گروه `mig` تعلق دارد.
- دستگاه `gpu-0-vgpu` به گروه `vgpu` تعلق دارد.

اگر یک Pod یا PodGroup دو دستگاه از این استخر درخواست کند، زمان‌بند بررسی می‌کند که آیا دو دستگاه انتخاب‌شده روی مجموعهٔ شمارندهٔ `gpu-0-memory` گروه سازگاری مشترکی دارند یا نه. از آنجا که `{"mig"} ∩ {"vgpu"} = ∅`، این جفت رد می‌شود؛ حتی با اینکه مجموعهٔ شمارنده حافظهٔ کافی برای هر دو دستگاه دارد. هر دو درخواست تنها با دو دستگاه MIG (یا دو دستگاه vGPU) از استخری برآورده می‌شوند که چنین جفت‌هایی در آن وجود داشته باشد.

### محدودیت‌ها {#device-compatibility-groups-constraints}

- هر مدخل `consumesCounters[]` می‌تواند حداکثر **۲** نام گروه اعلام کند.
- نام‌های گروه باید درون یک مدخل یکتا باشند.
- نام‌های گروه برای کوبرنتیز غیرشفاف هستند و تنها درون استخر درایورِ منتشرکننده معنا دارند.
- گروه‌ها به‌ازای هر مجموعهٔ شمارنده مقایسه می‌شوند: گروه‌های یک مجموعهٔ شمارنده هیچ تأثیری بر تصمیم‌های تخصیص هم‌زمان برای مجموعهٔ شمارندهٔ دیگر ندارند.

### ایمنی در برابر ناهمخوانی نسخه‌ها {#device-compatibility-groups-version-skew}

وقتی feature gate `DRADeviceCompatibilityGroups` غیرفعال باشد (که در مرحلهٔ آلفا پیش‌فرض است)، kube-apiserver فیلد `compatibilityGroups` را از هر ResourceSlice جدید یا به‌روزرسانی‌شده حذف می‌کند؛ مگر اینکه این فیلد در آبجکت قبلی از پیش تنظیم شده باشد. در این حالت، زمان‌بند دستگاه‌های هر استخری را که پیش‌تر دستگاه‌های گروه‌دار داشته است، متعلق به استخری ناقص در نظر می‌گیرد و آن‌ها را به‌طور کامل نادیده می‌گیرد.

تنها فهرست ناتهی به معنای تنظیم‌شدن فیلد است: `compatibilityGroups: null` و `compatibilityGroups: []` دقیقاً مانند حذف فیلد تلقی می‌شوند. دستگاه‌های دارای این مقادیر دقیقاً مانند دستگاه‌های بدون گروه رفتار می‌کنند و باعث نمی‌شوند زمان‌بند استخر را ناقص در نظر بگیرد.

قابلیت گروه‌های سازگاری دستگاه با
[feature gate `DRADeviceCompatibilityGroups`](/docs/reference/command-line-tools-reference/feature-gates/#DRADeviceCompatibilityGroups)
در kube-apiserver و kube-scheduler کنترل می‌شود. علاوه بر آن،
[feature gate `DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
نیز باید فعال باشد.

## ظرفیت قابل‌مصرف

{{< feature-state feature_gate_name="DRAConsumableCapacity" >}}

با ویژگی ظرفیت قابل‌مصرف، چند ResourceClaim مستقل می‌توانند از دستگاه‌های یکسانی استفاده کنند و زمان‌بند کوبرنتیز مدیریت می‌کند که هر claim چه مقدار از ظرفیت دستگاه را مصرف کند. این وضعیت مشابه اشتراک منابع یک نود میان Podهاست؛ ResourceClaimها نیز می‌توانند منابع یک دستگاه را به اشتراک بگذارند.

درایور دستگاه می‌تواند فیلد `allowMultipleAllocations` را که به `.spec.devices` در `ResourceSlice` افزوده شده است تنظیم کند تا تخصیص آن دستگاه به چند ResourceClaim مستقل یا به چند درخواست درون یک ResourceClaim ممکن شود.

وقتی دقیقاً یک نوع دستگاه را در یک `ResourceClaim` درخواست می‌کنید، فیلد `spec.devices.requests[].exactly.capacity` را تنظیم کنید تا نیازمندی‌های منبع دستگاه برای هر تخصیص مشخص شود. برای فهرستی اولویت‌بندی‌شده از گزینه‌های جایگزین مختلف، `capacity` را درون مدخل‌های مربوطِ `spec.devices.requests[].firstAvailable[]` تنظیم کنید.

در دستگاهی که اجازهٔ تخصیص چندگانه می‌دهد، ظرفیت درخواستی از ظرفیت کل آن برداشت یا مصرف می‌شود؛ مفهومی که **ظرفیت قابل‌مصرف** نام دارد. سپس زمان‌بند اطمینان می‌یابد که مجموع ظرفیت مصرف‌شده در همهٔ claimها از ظرفیت کلی دستگاه فراتر نرود. افزون بر این، نویسندگان درایور می‌توانند با محدودیت‌های `requestPolicy` روی ظرفیت‌های تک‌تک دستگاه‌ها، نحوهٔ مصرف این ظرفیت‌ها را کنترل کنند. برای مثال، نویسندهٔ درایور می‌تواند مشخص کند که یک ظرفیت معین فقط در گام‌های 1Gi مصرف شود.

در ادامه نمونه‌ای از یک دستگاه شبکه آمده است که اجازهٔ تخصیص چندگانه می‌دهد و ظرفیت پهنای باند قابل‌مصرفی دارد.

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

ظرفیت قابل‌مصرف را می‌توان مطابق نمونهٔ زیر درخواست کرد.

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

نتیجهٔ تخصیص شامل ظرفیت مصرف‌شده و شناسهٔ سهم (share) خواهد بود.

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

در این مثال، دستگاهی با قابلیت تخصیص چندگانه انتخاب شده است. با این حال، هر دستگاه `resource.example.com` که دست‌کم پهنای باند درخواستیِ 1G را داشته باشد نیز می‌توانست این نیاز را برآورده کند. اگر دستگاهی بدون قابلیت تخصیص چندگانه انتخاب می‌شد، کل دستگاه تخصیص داده می‌شد. برای اینکه فقط دستگاه‌های دارای قابلیت تخصیص چندگانه استفاده شوند، می‌توانید از معیار CEL `device.allowMultipleAllocations == true` استفاده کنید.

### محدودیت DistinctAttribute

وقتی چند دستگاه را در یک ResourceClaim درخواست می‌کنید، می‌توانید از محدودیت DistinctAttribute استفاده کنید تا مطمئن شوید هر دستگاه تخصیص‌یافته برای یک صفت (attribute) مشخص، مقدار متفاوتی دارد. این محدودیت همراه با ویژگی ظرفیت قابل‌مصرف معرفی شد.

محدودیت DistinctAttribute به‌ویژه هنگام کار با دستگاه‌های دارای قابلیت تخصیص چندگانه مفید است. این محدودیت مانع می‌شود که زمان‌بند یک دستگاه را چند بار درون یک ResourceClaim تخصیص دهد، حتی اگر آن دستگاه اجازهٔ تخصیص چندگانه بدهد.

این محدودیت علاوه بر جلوگیری از تخصیص‌های تکراری، با توزیع دستگاه‌ها بر اساس صفاتشان به بهینه‌سازی کارایی کمک می‌کند. برای مثال، می‌توانید از آن برای توزیع دستگاه‌ها میان نودهای NUMA مختلف استفاده کنید تا پهنای باند حافظه بهینه شود و رقابت بر سر منابع کاهش یابد.


## مجوزدهی جزئی وضعیت {#granular-status-authorization}

{{< feature-state feature_gate_name="DRAResourceClaimGranularStatusAuthorization" >}}

از کوبرنتیز v1.36 به بعد، DRA برای به‌روزرسانی‌های status آبجکت `ResourceClaim`، با استفاده از زیرمنابع (subresource) مصنوعی و فعل‌های آگاه از نود، بررسی‌های مجوزدهی ریزدانه را اعمال می‌کند.

برای راهنمای سخت‌سازی امنیتی، از جمله نمونه‌های RBAC برای زمان‌بند و درایورهای DRA، به
[راهنمای سخت‌سازی - تخصیص پویای منابع](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/) مراجعه کنید.

برای روال گام‌به‌گامِ مخصوص مدیران کلاستر، به
[سخت‌سازی تخصیص پویای منابع در کلاستر شما](/docs/tasks/administer-cluster/hardening-dra/) مراجعه کنید.


## عملیات اختیاری نود {#optional-node-operations}

{{< feature-state feature_gate_name="DRAOptionalNodeOperations" >}}

در تخصیص پویای منابع (DRA)، `kubelet` از طریق gRPC با یک درایور محلی نود هماهنگ می‌شود تا دستگاه‌های تخصیص‌یافته را پیش از شروع کانتینر آماده کند (`NodePrepareResources`) و پس از پایان کار Pod، آماده‌سازی آن‌ها را لغو کند (`NodeUnprepareResources`). این سازوکار برای سخت‌افزارهای محلی نود مانند GPU یا FPGA حیاتی است، اما برخی منابع به‌طور کامل در control plane مدیریت می‌شوند و به هیچ آماده‌سازی محلی روی نود نیاز ندارند.

ویژگی عملیات اختیاری نود به درایورهای منبع امکان می‌دهد اعلام کنند که می‌توان از برخی عملیات gRPC محلی نود صرف‌نظر کرد. با این پیکربندی، `kubelet` جست‌وجوی درایور و فراخوانی‌های gRPC را برای آن دستگاه‌ها کنار می‌گذارد و دیگر نیازی به استقرار و نگهداری درایورهای محلیِ خالی روی تک‌تک نودهای کارگر نیست.

### پیکربندی درایور

نویسندگان درایور می‌توانند فیلد `skipNodeOperations` را در `.spec.skipNodeOperations` یک ResourceSlice مشخص کنند. این فیلد فهرستی از رشته‌های یکتاست که عملیات محلی نود را مشخص می‌کند که باید برای همهٔ دستگاه‌های آن slice از آن‌ها صرف‌نظر شود.

مقادیر معتبر عبارت‌اند از:

* مقدار `"NodePrepareResources"`: از فراخوانی‌های gRPC مربوط به `NodePrepareResources` صرف‌نظر می‌کند. این مقدار را نمی‌توان مشخص کرد، مگر اینکه `"NodeUnprepareResources"` نیز در فهرست آمده باشد (یا `"*"` مشخص شده باشد). این محدودیت مانع از گیر کردن Podها در وضعیت Terminating در صورت نبودِ پلاگین محلی نود می‌شود؛ زیرا وقتی از آماده‌سازی صرف‌نظر شود، وجود پلاگین هنگام راه‌اندازی Pod بررسی نمی‌شود.
* مقدار `"NodeUnprepareResources"`: از فراخوانی‌های gRPC مربوط به `NodeUnprepareResources` صرف‌نظر می‌کند.
* مقدار `"*"`: از همهٔ عملیات محلی نود برای منابع صرف‌نظر می‌کند.

در ادامه نمونه‌ای از یک ResourceSlice برای منبعی در control plane آمده است که از همهٔ عملیات محلی نود صرف‌نظر می‌کند:

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

### نتیجهٔ تخصیص و اجرا

وقتی زمان‌بند کوبرنتیز دستگاهی را به یک ResourceClaim تخصیص می‌دهد، فهرست `skipNodeOperations` را از ResourceSlice در نتیجهٔ تخصیص کپی می‌کند:

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

وقتی یک Pod روی نودی اجرا می‌شود، `kubelet` نتایج تخصیص را می‌خواند. اگر همهٔ دستگاه‌های تخصیص‌یافته برای یک درایور معین درون یک ResourceClaim از عملیات خاصی صرف‌نظر کنند، `kubelet` فراخوانی آن hook در gRPC را برای آن درایور به‌طور کامل کنار می‌گذارد.

### ملاحظات عملیاتی

#### به‌روزرسانی درجای درایورها

از آنجا که تنظیم `skipNodeOperations` در زمان تخصیص از ResourceSlice به ResourceClaim کپی می‌شود، Podهای در حال اجرا و تخصیص‌های فعال همان تنظیمی را حفظ می‌کنند که هنگام زمان‌بندی‌شان برقرار بوده است.

اگر نیازمندی‌های عملیات نودِ یک درایور به‌صورت درجا به‌روزرسانی شوند (برای مثال، از نیاز به عملیات نود به صرف‌نظر کردن از آن‌ها تغییر کنند)، claimهای موجود همچنان از پیکربندی قبلی استفاده خواهند کرد. برای جلوگیری از مشکلاتی مانند معلق ماندن Podهای در حال خاتمه در انتظار پلاگین نودی که از رده خارج شده است، مدیران کلاستر باید پیش از تغییر نیازمندی‌های عملیات نود یک درایور یا حذف DaemonSetهای درایور محلی نود، اطمینان یابند که هیچ claim فعالی برای آن درایور وجود ندارد.

#### یکپارچگی با ویژگی‌های اعلام‌شدهٔ نود

برای جلوگیری از زمان‌بندی Podها روی نودهایی که `kubelet` آن‌ها از صرف‌نظر کردن از عملیات DRA پشتیبانی نمی‌کند (که باعث می‌شود `kubelet` در انتظار پلاگین نودِ ناموجود با شکست مواجه شود)، این ویژگی با [ویژگی‌های اعلام‌شدهٔ
نود](/docs/concepts/scheduling-eviction/node-declared-features/) یکپارچه شده است. وقتی یک Pod از ResourceClaimای با `skipNodeOperations` پیکربندی‌شده استفاده می‌کند، زمان‌بند کوبرنتیز پیش از زمان‌بندی Pod بررسی می‌کند که نود مقصد پشتیبانی از ویژگی `DRAOptionalNodeOperations` را در `.status.declaredFeatures` خود اعلام کرده باشد.

قابلیت عملیات اختیاری نود با feature gate
[`DRAOptionalNodeOperations`](/docs/reference/command-line-tools-reference/feature-gates/#DRAOptionalNodeOperations)
در `kube-apiserver`، `kube-scheduler` و `kubelet` کنترل می‌شود.

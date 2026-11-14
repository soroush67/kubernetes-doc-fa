---
title: کنترل سیاست‌های مدیریت حافظه روی یک نود
reviewers:
- klueska
- derekwaynecarr
content_type: task
min-kubernetes-server-version: v1.32
weight: 145
math: true
---

<!-- overview -->

{{< feature-state feature_gate_name="MemoryManager" >}}

*مدیر حافظه* (Memory Manager) در کوبرنتیز قابلیت تخصیص تضمین‌شدهٔ حافظه (و hugepages) را برای پادهایی فراهم می‌کند که در {{< glossary_tooltip text="کلاس QoS" term_id="qos-class" >}} `Guaranteed` قرار دارند.

مدیر حافظه با به‌کارگیری یک پروتکل تولید راهنما (hint)، مناسب‌ترین وابستگی NUMA (NUMA affinity) را برای هر پاد به دست می‌آورد.
مدیر حافظه این راهنماهای وابستگی را در اختیار مدیر مرکزی، یعنی *مدیر توپولوژی* (Topology Manager)، قرار می‌دهد.
بر اساس این راهنماها و سیاست مدیر توپولوژی، پاد یا رد می‌شود یا در نود پذیرفته می‌شود.

افزون بر این، مدیر حافظه تضمین می‌کند که حافظهٔ درخواستیِ هر پاد از کمترین تعداد ممکن نودهای NUMA تخصیص داده شود.

برای آشنایی با پیش‌زمینهٔ منابع حافظه برای پادها، صفحهٔ
[تخصیص منابع حافظه به کانتینرها و پادها](/docs/tasks/configure-pod-container/assign-memory-resource/) را بخوانید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

{{< version-check >}} اگر از نسخهٔ قدیمی‌تری از کوبرنتیز استفاده می‌کنید، مستندات مربوط به همان نسخه را بررسی کنید.

### پیش‌نیازهای هم‌ترازی منابع

برای هم‌تراز کردن منابع حافظه با سایر منابع درخواست‌شده در مشخصات (spec) یک پاد:

- مدیر CPU باید فعال باشد و سیاست مناسبی برای آن روی نود پیکربندی شده باشد.
  به [کنترل سیاست‌های مدیریت CPU](/docs/tasks/administer-cluster/cpu-management-policies/) مراجعه کنید؛
- مدیر توپولوژی باید فعال باشد و سیاست مناسبی برای آن روی نود پیکربندی شده باشد.
  به [کنترل سیاست‌های مدیریت توپولوژی](/docs/tasks/administer-cluster/topology-manager/) مراجعه کنید.

### پشتیبانی از ویندوز

{{< feature-state feature_gate_name="WindowsCPUAndMemoryAffinity" >}}

پشتیبانی از ویندوز را می‌توان از طریق feature gate با نام `WindowsCPUAndMemoryAffinity` فعال کرد و این کار به پشتیبانی محیط اجرای کانتینر نیز نیاز دارد.  
در ویندوز فقط سیاست‌های [None](#policy-none) و [BestEffort](#policy-best-effort) پشتیبانی می‌شوند.

## مدیر حافظه چگونه کار می‌کند؟

در نودهای لینوکسی، مدیر حافظه تخصیص تضمین‌شدهٔ حافظه (و hugepages) را برای پادهای کلاس QoS از نوع Guaranteed فراهم می‌کند.
برای به‌کار انداختن فوری مدیر حافظه، دستورالعمل‌های بخش
[پیکربندی مدیر حافظه](#memory-manager-configuration) را دنبال کنید و سپس، همان‌طور که در بخش
[قرار دادن یک پاد در کلاس QoS از نوع Guaranteed](#placing-a-pod-in-the-guaranteed-qos-class) نشان داده شده است،
یک پاد `Guaranteed` آماده و مستقر کنید.

مدیر حافظه یک فراهم‌کنندهٔ راهنما (hint provider) است و راهنماهای توپولوژی را در اختیار مدیر توپولوژی قرار می‌دهد؛ سپس مدیر توپولوژی منابع درخواست‌شده را بر اساس این راهنماها هم‌تراز می‌کند.
در لینوکس، مدیر حافظه `cgroups` (به‌طور مشخص `cpuset.mems`) را نیز برای پادها اعمال می‌کند.
نمودار جریان کامل فرایند پذیرش و استقرار پاد در ادامه نشان داده شده است:

![مدیر حافظه در فرایند پذیرش و استقرار پاد](/images/docs/memory-manager-diagram.svg)

در طول این فرایند، مدیر حافظه شمارنده‌های داخلی خود را که در
[نقشهٔ نود و نقشه‌های حافظه][2] ذخیره شده‌اند به‌روزرسانی می‌کند تا تخصیص تضمین‌شدهٔ حافظه را مدیریت کند.

اگر مدیر نود مقدار `reservedMemory` را برای kubelet پیکربندی کرده باشد (بخش [پیکربندی حافظهٔ رزروشده](#reserved-memory-flag))، مدیر حافظه هنگام راه‌اندازی kubelet فعال می‌شود.
در این حالت، kubelet نقشهٔ نود خود را به‌روزرسانی می‌کند تا این رزرو در آن منعکس شود.

هنگامی که سیاست `Static` پیکربندی شده باشد، **باید** حافظهٔ رزروشده را برای نود پیکربندی کنید
(برای مثال، با فیلد پیکربندی `reservedMemory` در پیکربندی kubelet).

یکی از موضوعات مهم در عملکرد مدیر حافظه، مدیریت گروه‌های NUMA است.
هر بار که درخواست حافظهٔ یک پاد از ظرفیت یک نود NUMA بیشتر باشد، مدیر حافظه تلاش می‌کند گروهی متشکل از چند نود NUMA ایجاد کند که ظرفیت حافظهٔ بیشتری داشته باشد.

## پیکربندی مدیر حافظه

سایر مدیرها باید از قبل پیکربندی شده باشند (به [پیش‌نیازهای هم‌ترازی منابع](#resource-alignment-prerequisites) مراجعه کنید).
فیلد پیکربندی `memoryManagerPolicy` را در [پیکربندی kubelet]({{< relref "/docs/reference/config-api/kubelet-config.v1beta1" >}}) برابر با نام [سیاست](#policies) انتخابی خود قرار دهید.

در صورت تمایل، می‌توان مقداری از حافظه را برای فرایندهای سیستم یا kubelet رزرو کرد تا پایداری نود افزایش یابد (بخش [پیکربندی حافظهٔ رزروشده](#reserved-memory-flag)).

### سیاست‌ها

مدیر حافظهٔ کوبرنتیز سه سیاست ارائه می‌دهد. می‌توانید سیاست را از طریق فیلد پیکربندی `memoryManagerPolicy` در پیکربندی kubelet انتخاب کنید؛ مقادیر موجود در کوبرنتیز {{< skew currentVersion >}} عبارت‌اند از:

* [`None`](#policy-none) (پیش‌فرض)
* [`Static`](#policy-static) (فقط لینوکس)
* [`BestEffort`](#policy-best-effort) (فقط ویندوز)

#### سیاست None {#policy-none}

این سیاست پیش‌فرض است و به هیچ وجه بر تخصیص حافظه اثر نمی‌گذارد.
رفتار آن دقیقاً مانند حالتی است که مدیر حافظه اصلاً وجود نداشته باشد.

سیاست `None` راهنمای توپولوژی پیش‌فرض را برمی‌گرداند. این راهنمای ویژه نشان می‌دهد که فراهم‌کنندهٔ راهنما (در اینجا مدیر حافظه) هیچ ترجیحی برای وابستگی NUMA با هیچ منبعی ندارد.

#### سیاست Static {#policy-static}

{{< feature-state feature_gate_name="MemoryManager" >}}

**این سیاست فقط در لینوکس پشتیبانی می‌شود.**

در مورد پادهای `Guaranteed`، سیاست `Static` مدیر حافظه راهنماهای توپولوژی مربوط به مجموعه‌ای از نودهای NUMA را برمی‌گرداند که حافظه در آن‌ها قابل تضمین است، و با به‌روزرسانی آبجکت داخلی [NodeMap][2] حافظه را رزرو می‌کند.

در مورد پادهای `BestEffort` یا `Burstable`، سیاست `Static` مدیر حافظه راهنمای توپولوژی پیش‌فرض را بازمی‌گرداند، زیرا درخواستی برای حافظهٔ تضمین‌شده وجود ندارد، و حافظه‌ای را در آبجکت داخلی [NodeMap][2] رزرو نمی‌کند.

این سیاست فقط در لینوکس پشتیبانی می‌شود.

#### سیاست BestEffort {#policy-best-effort}

{{< feature-state feature_gate_name="WindowsCPUAndMemoryAffinity" >}}

**این سیاست فقط در ویندوز پشتیبانی می‌شود.**

در ویندوز، تخصیص نود NUMA به شکلی متفاوت از لینوکس انجام می‌شود.
هیچ سازوکاری وجود ندارد که تضمین کند دسترسی به حافظه فقط از یک نود NUMA مشخص انجام شود.
در عوض، زمان‌بند سیستم‌عامل ویندوز بهینه‌ترین نود NUMA را بر اساس تخصیص CPUها انتخاب می‌کند.
ممکن است ویندوز در صورتی که زمان‌بند آن نودهای NUMA دیگری را بهینه تشخیص دهد، از آن‌ها استفاده کند.

این سیاست مقدار حافظهٔ موجود و درخواست‌شده را از طریق _نقشهٔ نود_ (node map) داخلی پیگیری می‌کند.
مدیر حافظه پیش از تخصیص منبع، تمام تلاش خود را می‌کند تا اطمینان یابد حافظهٔ کافی روی یک نود NUMA در دسترس است.  
این یعنی در بیشتر موارد، تخصیص حافظه باید مطابق آنچه مشخص شده است عمل کند.

## پیکربندی حافظهٔ رزروشده {#reserved-memory-flag}

به‌عنوان مدیر، می‌توانید مقدار کل حافظهٔ رزروشده را برای یک نود پیکربندی کنید. این مقدار ازپیش‌پیکربندی‌شده سپس برای محاسبهٔ مقدار واقعی حافظهٔ [قابل‌تخصیص نود](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) که در دسترس پادها است، به کار می‌رود.

زمان‌بند کوبرنتیز از اطلاعات حافظهٔ قابل‌تخصیص برای بهینه‌سازی
[زمان‌بندی](/docs/concepts/scheduling-eviction/) پادها استفاده می‌کند.
. مدیران نود معمولاً از سازوکار _قابل‌تخصیص نود_ (node allocatable) برای رزرو منابع سیستمی نود کوبرنتیز برای kubelet یا فرایندهای سیستم‌عامل استفاده می‌کنند تا پایداری نود تضمین شود.

تنظیمات مرتبط kubelet عبارت‌اند از `kubeReserved`، `systemReserved` و `reservedMemory`.
با تنظیم `reservedMemory` می‌توانید کل حافظهٔ رزروشده را تقسیم کنید و آن را میان چندین نود NUMA توزیع کنید.

برای هر نود NUMA، فهرستی از رزروهای حافظه از انواع مختلف حافظه را با جداکنندهٔ کاما مشخص می‌کنید.
همچنین می‌توانید رزروهایی را که چند نود NUMA را در بر می‌گیرند، با استفاده از نقطه‌ویرگول به‌عنوان جداکننده مشخص کنید.

مدیر حافظه از این حافظهٔ رزروشده برای اجرای بارهای کاری کانتینری استفاده نمی‌کند.

برای مثال، اگر یک نود NUMA با نام «NUMA0» با ۱۰GiB حافظهٔ در دسترس داشته باشید و `reservedMemory` را طوری پیکربندی کنید که `1Gi` (حافظه) را برای NUMA0 رزرو کند، مدیر حافظه فرض می‌کند که فقط ۹GiB برای پادها در دسترس است.

می‌توانید این پارامتر را حذف کنید، اما باید بدانید که مقدار حافظهٔ رزروشده از همهٔ نودهای NUMA باید برابر با مقدار حافظهٔ _قابل‌تخصیص نود_ باشد.

اگر دست‌کم یکی از پارامترهای قابل‌تخصیص نود غیرصفر باشد، باید `reservedMemory` را دست‌کم برای یک نود NUMA مشخص کنید.
در واقع، مقدار آستانهٔ `evictionHard` به‌طور پیش‌فرض برابر با `100Mi` است؛ بنابراین اگر از سیاست `Static` استفاده می‌کنید، مشخص کردن `reservedMemory` الزامی است.

### نحو حافظهٔ رزروشدهٔ مدیر حافظه {#reserved-memory-syntax}

در ادامه چند نمونه از نحوهٔ تنظیم پیکربندی `reservedMemory` برای kubelet آمده است.

```yaml
  # Example 1
  reservedMemory:
  - numaNode: 0 # NUMA node index
    limits:
      memory: "1Gi" # byte quantity
  - numaNode: 1
    limits:
      memory: "2Gi" # byte quantity
```

```yaml
  # Example 2
  reservedMemory:
  - numaNode: 0
    limits:
      "memory": "512Gi"
  - numaNode: 1
    limits:
      "memory": "512Gi"
      "hugepages-1Gi": "2Gi" # only relevant on Linux
```

### محدودیت‌های رزرو حافظهٔ NUMA

هنگامی که مقادیری برای `reservedMemory` مشخص می‌کنید، این مقادیر باید با مقادیر فعلی `kubeReserved` و `systemReserved`، و همچنین با هر تنظیم `memory.available` که در `evictionHard` انجام می‌دهید، سازگار باشند.

```math
\begin{equation*}
\sum_{ \textnormal{i} = 0}^{ \textnormal{node count}} { \textit{reservedMemory} [ \textnormal{i} ]} = \textit{kubeReserved} + \textit{systemReserved} + \textit{evictionHard} \, \boxed{\textnormal{memory.available}}
\end{equation*}\\\
\text{where i is an index of a NUMA node}
```

اگر از فرمول بالا پیروی نکنید، مدیر حافظه هنگام راه‌اندازی خطا نشان می‌دهد.

به بیان دیگر، مثال ۱ (در بالا) نشان می‌دهد که کوبرنتیز برای حافظهٔ متعارف (`type=memory`) در مجموع ۳GiB رزرو می‌کند؛ یعنی:

```math
\begin{equation*}
\sum_{ \textnormal{i} = 0}^{ \textnormal{node count}} \textit{reservedMemory}_{ [ \textnormal{i} ] }  =  \underbrace{\textit{reservedMemory} [ 0 ] + \textit{reservedMemory} [ 1 ] }_{\textnormal{type=memory}}
            = 1 \textnormal{GiB} + 2 \textnormal{GiB}
            = 3 \textnormal{GiB}
\end{equation*}\\\
\text{where i is an index of a NUMA node}
```

چند نمونه از تنظیمات پیکربندی kubelet که به پیکربندی قابل‌تخصیص نود مربوط هستند:

```yaml
  kubeReserved: { cpu: "500m", memory: "50Mi" } # half a CPU, 50MiB of memory
  systemReserved: { cpu: "500m", memory: "256Mi" } # half a CPU, 256MiB of memory
```

{{< note >}}
آستانهٔ پیش‌فرض تخلیهٔ سخت (hard eviction) برابر با ۱۰۰MiB است و صفر **نیست**.
به یاد داشته باشید که مقدار حافظه‌ای را که با تنظیم `reservedMemory` رزرو می‌کنید، به اندازهٔ همین آستانهٔ تخلیهٔ سخت افزایش دهید. در غیر این صورت، kubelet مدیر حافظه را راه‌اندازی نمی‌کند و خطا نشان می‌دهد.

در ادامه نمونه‌ای از یک پیکربندی درست با استفاده از `reservedMemory` آمده است:
```yaml
  # this snippet relies on the default value of evictionHard
  memoryManagerPolicy: Static
  kubeReserved: { cpu: "4", memory: "4Gi" }
  systemReserved: { cpu: "1", memory: "1Gi" }
  reservedMemory:
  - numaNode: 0
    limits:
      memory: "3Gi"
  - numaNode: 1
    limits:
      memory: "2148Mi" # 3GiB minus 100MiB
```
{{< /note >}}

### پیکربندی‌هایی که باید از آن‌ها پرهیز کرد {#reserved-memory-configurations-to-avoid}

از پیکربندی‌های زیر پرهیز کنید:

1. موارد تکراری: همان نود NUMA یا نوع حافظه، اما با مقداری متفاوت؛
1. تعیین محدودیت صفر برای هر یک از انواع حافظه؛
1. شناسه‌های نود NUMA که در سخت‌افزار ماشین وجود ندارند؛
1. نام‌های نوع حافظه‌ای غیر از `memory` یا `hugepages-<size>`
   (hugepages با `<size>` مشخص‌شده نیز باید وجود داشته باشند).

## قرار دادن یک پاد در کلاس QoS از نوع Guaranteed

اگر سیاست انتخاب‌شده چیزی غیر از `None` باشد، مدیر حافظه پادهایی را که در کلاس QoS از نوع `Guaranteed` قرار دارند شناسایی می‌کند.
مدیر حافظه برای هر پاد `Guaranteed` راهنماهای توپولوژی مشخصی در اختیار مدیر توپولوژی قرار می‌دهد.
برای پادهایی که در کلاس QoS دیگری غیر از `Guaranteed` هستند، مدیر حافظه راهنماهای توپولوژی پیش‌فرض را در اختیار مدیر توپولوژی قرار می‌دهد.

بخش‌های زیر از مانیفست‌های پاد، یک پاد را در کلاس QoS از نوع `Guaranteed` قرار می‌دهند.

پادی که CPU(های) آن عدد صحیح است، زمانی در کلاس QoS از نوع `Guaranteed` اجرا می‌شود که `requests` برابر با `limits` باشد:

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
      requests:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
```

همچنین پادی که CPU(ها) را به اشتراک می‌گذارد، زمانی در کلاس QoS از نوع `Guaranteed` اجرا می‌شود که `requests` برابر با `limits` باشد.

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "300m"
        example.com/device: "1"
      requests:
        memory: "200Mi"
        cpu: "300m"
        example.com/device: "1"
```

توجه کنید که برای قرار گرفتن یک پاد در کلاس QoS از نوع Guaranteed، باید درخواست‌های CPU و حافظه هر دو مشخص شوند.

## {{% heading "whatsnext" %}}

- [عیب‌یابی مدیریت توپولوژی](/docs/tasks/debug/debug-cluster/topology/) را بخوانید.
- [KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/1769-memory-manager) (پیشنهاد بهبود کوبرنتیز) مربوط به مدیر حافظه را بخوانید.
- دربارهٔ [مدیرهای منابع در سطح پاد](/docs/concepts/resource-management/resource-managers/#pod-level-resource-managers) مطالعه کنید.

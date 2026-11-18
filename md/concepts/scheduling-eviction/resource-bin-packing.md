---
reviewers:
- bsalamat
- k82cn
- ahg-g
title: بسته‌بندی منابع (Bin Packing)
content_type: concept
weight: 80
---

<!-- overview -->

{{< note >}}
این مقاله به بسته‌بندی منابع در زمینهٔ زمان‌بندی یک Pod منفرد می‌پردازد. برای آشنایی با بسته‌بندی هنگام زمان‌بندی گروه‌های Pod، [مقالهٔ زمان‌بندی آگاه از توپولوژی](/docs/concepts/scheduling-eviction/topology-aware-scheduling/) را بخوانید.
{{< /note >}}

در [افزونهٔ زمان‌بندی](/docs/reference/scheduling/config/#scheduling-plugins) `NodeResourcesFit` در kube-scheduler، دو راهبرد امتیازدهی وجود دارد که از بسته‌بندی منابع پشتیبانی می‌کنند: `MostAllocated` و `RequestedToCapacityRatio`.

<!-- body -->

## فعال‌سازی بسته‌بندی با راهبرد MostAllocated
راهبرد `MostAllocated` نودها را بر اساس میزان بهره‌برداری از منابع امتیازدهی می‌کند و نودهایی را که تخصیص بیشتری دارند ترجیح می‌دهد.
برای هر نوع منبع می‌توانید وزنی تعیین کنید تا میزان تأثیر آن در امتیاز نود تغییر کند.

برای تنظیم راهبرد `MostAllocated` در افزونهٔ `NodeResourcesFit`، از
[پیکربندی زمان‌بند](/docs/reference/scheduling/config) مشابه نمونهٔ زیر استفاده کنید:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- pluginConfig:
  - args:
      scoringStrategy:
        resources:
        - name: cpu
          weight: 1
        - name: memory
          weight: 1
        - name: intel.com/foo
          weight: 3
        - name: intel.com/bar
          weight: 3
        type: MostAllocated
    name: NodeResourcesFit
```

با این پیکربندی، امتیاز نودها با میانگین وزنی بهره‌برداری از هر چهار منبع محاسبه می‌شود. از آنجا که وزن هر یک از منابع `intel.com/foo` و `intel.com/bar` برابر `3` و وزن CPU و حافظه برابر `1` است، بهره‌برداری از این منابع توسعه‌یافته سه برابر بیشتر بر امتیاز نهایی نود اثر می‌گذارد. زمان‌بند نودی را که بالاترین امتیاز را دارد انتخاب می‌کند تا Podها روی نودهایی با بهره‌برداری بالا زمان‌بندی شوند. این کار زمینه را برای کاهش مقیاس (scale-down) نودهایی که کمترین بهره‌برداری را دارند فراهم می‌کند.

برای آشنایی بیشتر با سایر پارامترها و پیکربندی پیش‌فرض آن‌ها، مستندات API مربوط به
[`NodeResourcesFitArgs`](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs) را ببینید.

## فعال‌سازی بسته‌بندی با RequestedToCapacityRatio

راهبرد `RequestedToCapacityRatio` به کاربران امکان می‌دهد منابع را همراه با وزن هر منبع مشخص کنند تا نودها بر اساس نسبت درخواست به ظرفیت امتیازدهی شوند. به این ترتیب، کاربران می‌توانند با استفاده از پارامترهای مناسب، منابع توسعه‌یافته را بسته‌بندی کنند و بهره‌برداری از منابع کمیاب را در کلاسترهای بزرگ بهبود دهند. این راهبرد نودها را بر اساس تابعی پیکربندی‌شده از منابع تخصیص‌یافته ترجیح می‌دهد. رفتار `RequestedToCapacityRatio` در تابع امتیازدهی `NodeResourcesFit` را می‌توان با فیلد
[scoringStrategy](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-ScoringStrategy) کنترل کرد.
در فیلد `scoringStrategy` می‌توانید دو پارامتر را پیکربندی کنید: `requestedToCapacityRatio` و `resources`. با `shape` در پارامتر `requestedToCapacityRatio`، کاربر می‌تواند تابع را بر اساس مقادیر `utilization` و `score` به‌صورت «کمترین درخواست» (least requested) یا «بیشترین درخواست» (most requested) تنظیم کند. پارامتر `resources` شامل `name` منبعی است که باید در امتیازدهی لحاظ شود و `weight` متناظر با آن که وزن هر منبع را مشخص می‌کند.

در ادامه نمونه‌ای از پیکربندی آمده است که رفتار بسته‌بندی را برای منابع توسعه‌یافتهٔ `intel.com/foo` و `intel.com/bar` با استفاده از فیلد `requestedToCapacityRatio` تنظیم می‌کند.

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- pluginConfig:
  - args:
      scoringStrategy:
        resources:
        - name: intel.com/foo
          weight: 3
        - name: intel.com/bar
          weight: 3
        requestedToCapacityRatio:
          shape:
          - utilization: 0
            score: 0
          - utilization: 100
            score: 10
        type: RequestedToCapacityRatio
    name: NodeResourcesFit
```

در این نمونه، فقط منابع توسعه‌یافتهٔ `intel.com/foo` و `intel.com/bar` در `resources` فهرست شده‌اند. بنابراین افزونهٔ `NodeResourcesFit` نودها را تنها بر اساس بهره‌برداری از این دو منبع امتیازدهی می‌کند و CPU و حافظه در امتیاز این افزونه نقشی ندارند. از آنجا که shape پیکربندی‌شده با افزایش بهره‌برداری امتیاز بالاتری می‌دهد (از `score: 0` در `utilization: 0` تا `score: 10` در `utilization: 100`)، زمان‌بند نودهایی را ترجیح می‌دهد که بخش بیشتری از این منابع توسعه‌یافته در آن‌ها در حال استفاده است و درخواست‌های مربوط به این منابع را روی کمترین تعداد ممکن از نودها بسته‌بندی می‌کند.

برای اینکه CPU و حافظه نیز در این راهبرد امتیازدهی لحاظ شوند، آن‌ها را به فهرست `resources` اضافه کنید. توجه کنید که همهٔ منابع این فهرست از تابع `shape` یکسانی استفاده می‌کنند؛ بنابراین با این کار همان منحنی بسته‌بندی روی این منابع نیز اعمال خواهد شد.

با ارجاع به فایل `KubeSchedulerConfiguration` از طریق فلگ `--config=/path/to/config/file` در kube-scheduler، پیکربندی به زمان‌بند منتقل می‌شود.

برای آشنایی بیشتر با سایر پارامترها و پیکربندی پیش‌فرض آن‌ها، مستندات API مربوط به
[`NodeResourcesFitArgs`](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs) را ببینید.

### تنظیم تابع امتیازدهی

از `shape` برای مشخص کردن رفتار تابع `RequestedToCapacityRatio` استفاده می‌شود.

```yaml
shape:
  - utilization: 0
    score: 0
  - utilization: 100
    score: 10
```

آرگومان‌های بالا به نود در صورتی که `utilization` برابر ۰٪ باشد `score` صفر، و در صورتی که `utilization` برابر ۱۰۰٪ باشد امتیاز ۱۰ می‌دهند و به این ترتیب رفتار بسته‌بندی را فعال می‌کنند. برای فعال کردن حالت «کمترین درخواست»، باید مقدار امتیاز را به‌صورت زیر معکوس کرد.

```yaml
shape:
  - utilization: 0
    score: 10
  - utilization: 100
    score: 0
```

پارامتر `resources` اختیاری است و مقدار پیش‌فرض آن به این صورت است:

```yaml
resources:
  - name: cpu
    weight: 1
  - name: memory
    weight: 1
```

می‌توان از آن برای افزودن منابع توسعه‌یافته به‌صورت زیر استفاده کرد:

```yaml
resources:
  - name: intel.com/foo
    weight: 5
  - name: cpu
    weight: 3
  - name: memory
    weight: 1
```

پارامتر `weight` اختیاری است و اگر مشخص نشود، مقدار آن ۱ در نظر گرفته می‌شود. همچنین مقدار `weight` نمی‌تواند منفی باشد.

### امتیازدهی نود برای تخصیص ظرفیت

این بخش برای کسانی است که می‌خواهند جزئیات درونی این قابلیت را درک کنند.
در ادامه نمونه‌ای از نحوهٔ محاسبهٔ امتیاز نود برای مجموعه‌ای مشخص از مقادیر آمده است.

منابع درخواست‌شده:

```
intel.com/foo : 2
memory: 256MB
cpu: 2
```

وزن منابع:

```
intel.com/foo : 5
memory: 1
cpu: 3
```

FunctionShapePoint {{0, 0}, {100, 10}}

مشخصات نود ۱:

```
Available:
  intel.com/foo: 4
  memory: 1 GB
  cpu: 8

Used:
  intel.com/foo: 1
  memory: 256MB
  cpu: 1
```

امتیاز نود:

```
intel.com/foo  = resourceScoringFunction((2+1),4)
               = (100 - ((4-3)*100/4))
               = (100 - 25)
               = 75                       # requested + used = 75% * available
               = rawScoringFunction(75)
               = 7                        # floor(75/10)

memory         = resourceScoringFunction((256+256),1024)
               = (100 -((1024-512)*100/1024))
               = 50                       # requested + used = 50% * available
               = rawScoringFunction(50)
               = 5                        # floor(50/10)

cpu            = resourceScoringFunction((2+1),8)
               = (100 -((8-3)*100/8))
               = 37.5                     # requested + used = 37.5% * available
               = rawScoringFunction(37.5)
               = 3                        # floor(37.5/10)

NodeScore   =  ((7 * 5) + (5 * 1) + (3 * 3)) / (5 + 1 + 3)
            =  5
```

مشخصات نود ۲:

```
Available:
  intel.com/foo: 8
  memory: 1GB
  cpu: 8
Used:
  intel.com/foo: 2
  memory: 512MB
  cpu: 6
```

امتیاز نود:

```
intel.com/foo  = resourceScoringFunction((2+2),8)
               =  (100 - ((8-4)*100/8)
               =  (100 - 50)
               =  50
               =  rawScoringFunction(50)
               = 5

memory         = resourceScoringFunction((256+512),1024)
               = (100 -((1024-768)*100/1024))
               = 75
               = rawScoringFunction(75)
               = 7

cpu            = resourceScoringFunction((2+6),8)
               = (100 -((8-8)*100/8))
               = 100
               = rawScoringFunction(100)
               = 10

NodeScore   =  ((5 * 5) + (7 * 1) + (10 * 3)) / (5 + 1 + 3)
            =  7

```

## {{% heading "whatsnext" %}}

- دربارهٔ [چارچوب زمان‌بندی](/docs/concepts/scheduling-eviction/scheduling-framework/) بیشتر بخوانید
- دربارهٔ [پیکربندی زمان‌بند](/docs/reference/scheduling/config/) بیشتر بخوانید

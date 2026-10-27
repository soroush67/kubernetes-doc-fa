---
reviewers:
- bsalamat
- k82cn
- ahg-g
title: بسته‌بندی منابع (Resource Bin Packing)
content_type: concept
weight: 80
---

<!-- overview -->

{{< note >}}
این مقاله به بسته‌بندی منابع در زمینه زمان‌بندی یک Pod منفرد می‌پردازد. برای آگاهی از بسته‌بندی در زمان‌بندی گروه‌های Pod، لطفاً [مقاله درباره زمان‌بندی آگاه از توپولوژی](/docs/concepts/scheduling-eviction/topology-aware-scheduling/) را مطالعه کنید.
{{< /note >}}

در [افزونه زمان‌بندی](/docs/reference/scheduling/config/#scheduling-plugins) با نام `NodeResourcesFit` در kube-scheduler، دو
راهبرد امتیازدهی وجود دارد که از بسته‌بندی (bin packing) منابع پشتیبانی می‌کنند: `MostAllocated` و `RequestedToCapacityRatio`.

<!-- body -->

## فعال‌سازی بسته‌بندی با استفاده از راهبرد MostAllocated
راهبرد `MostAllocated` نودها را بر اساس میزان بهره‌برداری از منابع امتیازدهی می‌کند و نودهایی را که تخصیص بیشتری دارند ترجیح می‌دهد.
برای هر نوع منبع می‌توانید وزنی تعیین کنید تا میزان تأثیر آن بر امتیاز نود تغییر کند.

برای تنظیم راهبرد `MostAllocated` در افزونه `NodeResourcesFit`، از یک
[پیکربندی زمان‌بند](/docs/reference/scheduling/config) مشابه نمونه زیر استفاده کنید:

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

با این پیکربندی، نودها با استفاده از میانگین وزنی میزان بهره‌برداری در هر چهار
منبع امتیازدهی می‌شوند. از آنجا که وزن `intel.com/foo` و `intel.com/bar` هرکدام `3` است، در حالی که وزن
CPU و memory برابر `1` است، میزان بهره‌برداری از این منابع توسعه‌یافته (extended resources) سه برابر بیشتر بر
امتیاز نهایی نود اثر می‌گذارد. زمان‌بند نودی را که بالاترین امتیاز را دارد انتخاب می‌کند و هدفش این است که Podها را روی
نودهایی با بهره‌برداری بالا زمان‌بندی کند. این کار به آماده‌سازی برای کاهش مقیاس (scale-down) نودهایی که کمترین بهره‌برداری را دارند کمک می‌کند.

برای کسب اطلاعات بیشتر درباره سایر پارامترها و پیکربندی پیش‌فرض آن‌ها، مستندات API مربوط به
[`NodeResourcesFitArgs`](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs) را مطالعه کنید.

## فعال‌سازی بسته‌بندی با استفاده از RequestedToCapacityRatio

راهبرد `RequestedToCapacityRatio` به کاربران امکان می‌دهد منابع را همراه با وزن هر منبع مشخص کنند تا نودها بر اساس
نسبت درخواست به ظرفیت امتیازدهی شوند. این قابلیت
به کاربران اجازه می‌دهد با استفاده از پارامترهای مناسب، منابع توسعه‌یافته را بسته‌بندی کنند
تا بهره‌برداری از منابع کمیاب در کلاسترهای بزرگ بهبود یابد. این راهبرد نودها را بر اساس یک
تابع پیکربندی‌شده از منابع تخصیص‌یافته ترجیح می‌دهد. رفتار `RequestedToCapacityRatio` در
تابع امتیازدهی `NodeResourcesFit` را می‌توان با فیلد
[scoringStrategy](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-ScoringStrategy) کنترل کرد.
در فیلد `scoringStrategy` می‌توانید دو پارامتر را پیکربندی کنید: `requestedToCapacityRatio` و
`resources`. مقدار `shape` در پارامتر `requestedToCapacityRatio`
به کاربر امکان می‌دهد تابع را بر اساس مقادیر `utilization` و `score` به‌صورت کمترین درخواست‌شده (least requested) یا بیشترین
درخواست‌شده (most requested) تنظیم کند. پارامتر `resources`
شامل `name` منبعی است که در امتیازدهی در نظر گرفته می‌شود
و `weight` متناظر با آن، که وزن هر منبع را مشخص می‌کند.

در ادامه نمونه‌ای از پیکربندی آمده است که رفتار بسته‌بندی را برای منابع توسعه‌یافته `intel.com/foo` و `intel.com/bar`
با استفاده از فیلد `requestedToCapacityRatio` تنظیم می‌کند.

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

در این نمونه، فقط منابع توسعه‌یافته `intel.com/foo` و `intel.com/bar` در
`resources` فهرست شده‌اند. بنابراین افزونه `NodeResourcesFit` نودها را صرفاً بر اساس میزان بهره‌برداری
از همین دو منبع امتیازدهی می‌کند؛ CPU و memory در امتیاز این افزونه نقشی ندارند. از آنجا که
شکل (shape) پیکربندی‌شده با افزایش بهره‌برداری امتیاز بالاتری اختصاص می‌دهد (`score: 0` در `utilization: 0`
که تا `score: 10` در `utilization: 100` افزایش می‌یابد)، زمان‌بند نودهایی را ترجیح می‌دهد که بخش بیشتری از این
منابع توسعه‌یافته در آن‌ها از قبل در حال استفاده است، و درخواست‌های مربوط به آن‌ها را روی کمترین تعداد ممکن نود بسته‌بندی می‌کند.

برای اینکه CPU و memory نیز در این راهبرد امتیازدهی لحاظ شوند، آن‌ها را به فهرست `resources` اضافه کنید. توجه داشته باشید که همه
منابع موجود در فهرست از یک تابع `shape` مشترک استفاده می‌کنند، بنابراین این کار همان منحنی بسته‌بندی را
برای این منابع نیز اعمال می‌کند.

با ارجاع به فایل `KubeSchedulerConfiguration` از طریق فلگ
`--config=/path/to/config/file` در kube-scheduler، پیکربندی به
زمان‌بند ارسال می‌شود.

برای کسب اطلاعات بیشتر درباره سایر پارامترها و پیکربندی پیش‌فرض آن‌ها، مستندات API مربوط به
[`NodeResourcesFitArgs`](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs) را مطالعه کنید.

### تنظیم تابع امتیازدهی

از `shape` برای مشخص کردن رفتار تابع `RequestedToCapacityRatio` استفاده می‌شود.

```yaml
shape:
  - utilization: 0
    score: 0
  - utilization: 100
    score: 10
```

آرگومان‌های بالا اگر `utilization` برابر ۰٪ باشد به نود `score` برابر ۰ و اگر
`utilization` برابر ۱۰۰٪ باشد امتیاز ۱۰ می‌دهند و به این ترتیب رفتار بسته‌بندی را فعال می‌کنند. برای فعال‌سازی رفتار کمترین
درخواست‌شده (least requested)، مقدار امتیاز باید به شکل زیر معکوس شود.

```yaml
shape:
  - utilization: 0
    score: 10
  - utilization: 100
    score: 0
```

`resources` یک پارامتر اختیاری است که مقدار پیش‌فرض آن به شرح زیر است:

```yaml
resources:
  - name: cpu
    weight: 1
  - name: memory
    weight: 1
```

می‌توان از آن برای افزودن منابع توسعه‌یافته به شکل زیر استفاده کرد:

```yaml
resources:
  - name: intel.com/foo
    weight: 5
  - name: cpu
    weight: 3
  - name: memory
    weight: 1
```

پارامتر `weight` اختیاری است و در صورت مشخص نشدن، مقدار آن ۱ در نظر گرفته می‌شود. همچنین،
مقدار `weight` نمی‌تواند منفی باشد.

### امتیازدهی نود برای تخصیص ظرفیت

این بخش برای کسانی است که می‌خواهند جزئیات داخلی این قابلیت را درک کنند.
در ادامه نمونه‌ای آمده است که نشان می‌دهد امتیاز نود برای مجموعه‌ای مشخص از مقادیر چگونه محاسبه می‌شود.

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

- درباره [چارچوب زمان‌بندی (scheduling framework)](/docs/concepts/scheduling-eviction/scheduling-framework/) بیشتر بخوانید
- درباره [پیکربندی زمان‌بند](/docs/reference/scheduling/config/) بیشتر بخوانید

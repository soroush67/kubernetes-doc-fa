---
title: زمان‌بندی بار کاری آگاه از توپولوژی
content_type: concept
weight: 85
---

<!-- overview -->
{{< feature-state feature_gate_name="TopologyAwareWorkloadScheduling" >}}

*زمان‌بندی آگاه از توپولوژی* (Topology-Aware Scheduling یا TAS) یک [الگوریتم زمان‌بندی جای‌گذاری](/docs/concepts/scheduling-eviction/podgroup-scheduling/#placement-scheduling-algorithm)
است که امکان یافتن جای‌گذاری بهینه برای PodGroup موردنظر را فراهم می‌کند و تضمین می‌کند که همهٔ پادها
در یک دامنهٔ توپولوژی واحد در کنار هم قرار گیرند. کاربران می‌توانند با تغییر پیکربندی افزونه‌های TAS،
آن را با نیازهای خاص خود سازگار کنند.

## چارچوب زمان‌بندی: پیکربندی افزونه‌های TAS

زمان‌بند شامل افزونه‌های درون‌درختی (in-tree) جدید و توسعه‌یافته‌ای است که نقاط توسعهٔ TAS را پیاده‌سازی می‌کنند:

*   `TopologyPlacement`: رابط `PlacementGeneratePlugin` را پیاده‌سازی می‌کند. این افزونه با گروه‌بندی نودها
بر اساس مقادیر متمایز `key` توپولوژی درخواست‌شده (که در PodGroup تعریف شده است)،
جای‌گذاری‌های نامزد را تولید می‌کند.

*   `NodeResourcesFit`: برای پیاده‌سازی رابط `PlacementScorePlugin` توسعه داده شده است. این افزونه با پیروی از
منطقی مشابه bin-packing استاندارد پادها، جای‌گذاری‌ها را بر اساس نسبت تخصیص
در همهٔ نودهای درون جای‌گذاری امتیازدهی می‌کند. این افزونه از راهبرد `MostAllocated` برای بیشینه کردن
بهره‌وری منابع درون یک جای‌گذاری استفاده می‌کند و وزن‌های منابع را از تنظیمات استاندارد افزونه
در حالت پادبه‌پاد به ارث می‌برد.

*   `PodGroupPodsCount`: رابط `PlacementScorePlugin` را پیاده‌سازی می‌کند. این افزونه جای‌گذاری‌های نامزد را
بر اساس تعداد کل پادهایی از PodGroup که می‌توانید با موفقیت زمان‌بندی کنید، امتیازدهی می‌کند.

### سفارشی‌سازی وزن افزونه‌ها و وزن منابع در bin-packing

به‌طور پیش‌فرض، افزونه‌های `NodeResourcesFit` و `PodGroupPodsCount` با وزن‌های برابر پیکربندی شده‌اند
(مقدار پیش‌فرض هر دو برابر با 1 است) تا توازن مناسبی میان منطق bin-packing و زمان‌بندی
بیشترین تعداد ممکن از پادها برقرار شود.

می‌توانید این وزن‌ها یا وزن منابع در راهبرد bin-packing را در
KubeSchedulerConfiguration خود تنظیم کنید. در اینجا قطعه‌ای نمونه آمده است که نشان می‌دهد چگونه وزن هر دو
افزونه را تغییر دهید و چگونه وزن منابع `NodeResourcesFit` را بازنویسی کنید. تغییر دوم
هم بر الگوریتم امتیازدهی پادبه‌پاد و هم بر الگوریتم امتیازدهی جای‌گذاری اعمال می‌شود:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: default-scheduler
    plugins:
      placementScore:
        enabled:
          # 1) Change the default weights of the placement score plugins
          - name: NodeResourcesFit
            weight: 2
          - name: PodGroupPodsCount
            weight: 5
    pluginConfig:
      - name: NodeResourcesFit
        args:
          # 2) Changing the scoring resource weights for both pod-by-pod and placement scoring
          # algorithms
          scoringStrategy:
            # The type will only be considered in pod-by-pod scheduling. Placement scoring always
            # uses MostAllocated strategy
            type: LeastAllocated
            # Resource weights will be used in both pod-by-pod and placement scoring algorithms
            resources:
              - name: cpu
                weight: 2
              - name: memory
                weight: 3
```

## جای‌گذاری‌های توپولوژی چندسطحی

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate با نام [`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
و {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3`
فعال باشند، افزونه‌های زمان‌بندی آگاه از توپولوژی پشتیبانی خود را به سلسله‌مراتب‌های چندسطحی
`CompositePodGroup` گسترش می‌دهند. این افزونه‌ها در طول
[زمان‌بندی سلسله‌مراتبی](/docs/concepts/scheduling-eviction/podgroup-scheduling) برای `CompositePodGroups` فراخوانی می‌شوند.

### تولید جای‌گذاری‌های نامزد

برای بارهای کاری‌ای که با یک سلسله‌مراتب `CompositePodGroup` تعریف شده‌اند، افزونهٔ `TopologyPlacement`
جای‌گذاری‌های نامزد را از بالا به پایین در سراسر سلسله‌مراتب گروه و با تقسیم‌بندی متوالی تولید می‌کند:

* برای یک `CompositePodGroup` ریشه، `TopologyPlacement` جای‌گذاری‌های نامزد را در میان همهٔ
  نودهای موجود کلاستر و با گروه‌بندی نودها بر اساس مقادیر متمایز `key` توپولوژی
  درخواست‌شده تولید می‌کند.
* برای یک `CompositePodGroup` فرزند یا یک `PodGroup` برگ، `TopologyPlacement` جای‌گذاری‌های نامزدی
  تولید می‌کند که محدود به جای‌گذاری فرض‌شده برای گروه والد هستند. این افزونه مجموعهٔ نودهای
  جای‌گذاری گروه والد را با گروه‌بندی آن نودها بر اساس `key` توپولوژی درخواست‌شده توسط گروه فرزند
  تقسیم‌بندی می‌کند.

{{< note >}}
اگر هیچ قید توپولوژی مشخص نشده باشد، افزونهٔ `TopologyPlacement` یک جای‌گذاری نامزد واحد
معادل با جای‌گذاری والد تولید می‌کند.

به همین ترتیب، اگر گروه ریشه هیچ قید توپولوژی‌ای مشخص نکند، افزونه یک جای‌گذاری نامزد واحد
متناظر با همهٔ نودهای موجود در کلاستر تولید می‌کند. این موضوع برای
بارهای کاری تک‌سطحی که از API `PodGroup` استفاده می‌کنند و هیچ قید توپولوژی‌ای برایشان مشخص نشده است نیز صادق است.
{{< /note >}}

### امتیازدهی جای‌گذاری

هنگام امتیازدهی به یک جای‌گذاری نامزد برای یک `CompositePodGroup`، افزونه‌های امتیازدهی منطقی
مشابه حالت `PodGroup` تک‌سطحی را اعمال می‌کنند:

* `PodGroupPodsCount`: جای‌گذاری‌های نامزد را بر اساس تعداد کل پادها (هم پادهای
  از قبل زمان‌بندی‌شده و هم پادهای تازه فرض‌شده) در همهٔ `PodGroups` برگِ نوادگان آن
  `CompositePodGroup` امتیازدهی می‌کند. جای‌گذاری‌های نامزدی که قادر به جای دادن تعداد کل بیشتری از پادها
  در زیرسلسله‌مراتب باشند، امتیاز بالاتری دریافت می‌کنند.
* `NodeResourcesFit`: درخواست‌های منابع همهٔ پادهای پیشنهادی را در همهٔ `PodGroups`
  نوادگان آن `CompositePodGroup` تجمیع می‌کند و بهره‌وری منابع را در همهٔ نودهای درون
  دامنهٔ جای‌گذاری نامزد ارزیابی می‌کند.

## {{% heading "whatsnext" %}}

* دربارهٔ [API زمان‌بندی آگاه از توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/) بیشتر بیاموزید.
* دربارهٔ [زمان‌بندی گروه پاد](/docs/concepts/scheduling-eviction/podgroup-scheduling/) مطالعه کنید.
* دربارهٔ [سیاست‌های گروه پاد](/docs/concepts/workloads/workload-api/policies/) مطالعه کنید.

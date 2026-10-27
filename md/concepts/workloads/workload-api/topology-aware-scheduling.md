---
title: زمان‌بندی بار کاری آگاه از توپولوژی
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="TopologyAwareWorkloadScheduling" >}}

*زمان‌بندی آگاه از توپولوژی* (TAS) قابلیتی از Workload API است که جای‌گذاری
Podها را درون کلاستر بهینه می‌کند.

TAS تضمین می‌کند که همه‌ی Podهای درون یک PodGroup در یک دامنه‌ی توپولوژی مشخص،
مانند یک رک سرور یا یک zone، در کنار هم قرار گیرند. این کار تأخیر ارتباط میان Podها را به حداقل می‌رساند و از
پراکندگی بار کاری در زیرساخت کلاستر جلوگیری می‌کند.

## زمان‌بندی آگاه از توپولوژی با سیاست زمان‌بندی gang

هنگامی که TAS روی PodGroupهایی با سیاست زمان‌بندی `gang` اعمال می‌شود، تخصیص بالقوه
(*جای‌گذاری*) کل گروه Podها را به‌طور یکجا شبیه‌سازی می‌کند. TAS پیش از متعهدکردن منابع تضمین می‌کند که دست‌کم
`minCount` Pod تعیین‌شده بتوانند با هم در یک دامنه‌ی توپولوژی جای گیرند.
اگر هیچ جای‌گذاری امکان‌پذیری یافت نشود، کل PodGroup غیرقابل‌زمان‌بندی می‌شود.

این رویکرد توصیه‌شده برای بارهای کاری‌ای مانند آموزش توزیع‌شده‌ی هوش مصنوعی و یادگیری ماشین است که
برای به حداقل رساندن تأخیر ارتباط میان Podها، به‌طور قطعی به نزدیکی نیاز دارند.

اگر Podهای جدیدی به PodGroupی اضافه شوند که برخی Podهای آن قبلاً زمان‌بندی شده‌اند (برای مثال، اگر Podها
دوباره ایجاد شوند)، زمان‌بند همه‌ی Podهای جدید ورودی را وادار می‌کند دقیقاً در همان دامنه‌ی توپولوژی‌ای
قرار گیرند که Podهای موجود در حال حاضر در آن قرار دارند. اگر آن دامنه‌ی مشخص ظرفیت کافی
برای Podهای جدید نداشته باشد، Podها در وضعیت pending باقی می‌مانند، حتی اگر این به معنای آن باشد که کمتر از `minCount` Pod
در این لحظه زمان‌بندی شده باشند.

{{< note >}}
از v1.36، زمان‌بندی آگاه از توپولوژی باعث پس‌گیری بار کاری یا Pod نمی‌شود. اگر بدون
پس‌گیری هیچ جای‌گذاری امکان‌پذیری یافت نشود، PodGroup غیرقابل‌زمان‌بندی می‌شود.
{{< /note >}}

## زمان‌بندی آگاه از توپولوژی با سیاست زمان‌بندی basic

استفاده از TAS با سیاست زمان‌بندی `basic` ممکن است رفتار ناسازگاری نشان دهد. زمان‌بند ممکن است هنگام
ورود به چرخه‌ی زمان‌بندی PodGroup تنها زیرمجموعه‌ای از Podها را مشاهده کند؛ بنابراین امکان‌پذیری جای‌گذاری
تنها برای Podهای مشاهده‌شده ارزیابی می‌شود، نه برای کل PodGroup. برای کاهش نسبی
این محدودیت، می‌توانید از دروازه‌های زمان‌بندی (scheduling gates) استفاده کنید تا زمان‌بندی PodGroup را تا زمانی که همه‌ی
Podهای درون PodGroup در صف زمان‌بندی قرار گیرند به تعویق بیندازید.

اگر هیچ جای‌گذاری امکان‌پذیری برای کل PodGroup یافت نشود، ممکن است تنها زیرمجموعه‌ای از Podها زمان‌بندی شوند
و تضمین می‌شود که این Podها محدودیت‌های زمان‌بندی را برآورده کنند.

اگر Podهای جدیدی به PodGroupی اضافه شوند که برخی Podهای آن قبلاً زمان‌بندی شده‌اند، زمان‌بند همانند
حالت سیاست `gang` عمل می‌کند؛ یعنی Podهای جدید را وادار می‌کند در همان دامنه قرار گیرند، مگر آنکه
ظرفیت کافی وجود نداشته باشد (که در این صورت Podهای جدید در وضعیت pending باقی می‌مانند).

## پیکربندی API: محدودیت‌های زمان‌بندی

هر PodGroup (یا PodGroupTemplate) می‌تواند به‌صورت اختیاری فیلد `schedulingConstraints` را اعلام کند
که توسط [الگوریتم زمان‌بندی PodGroup مبتنی بر جای‌گذاری](/docs/concepts/scheduling-eviction/podgroup-scheduling/#placement-scheduling-algorithm) تفسیر می‌شود.
اگر محدودیت‌ها در PodGroupTemplate تعریف شده باشند، در PodGroupهایی که به آن ارجاع می‌دهند کپی می‌شوند.

از کوبرنتیز v1.36، API از محدودیت‌های توپولوژی پشتیبانی می‌کند.

{{< note >}}
از کوبرنتیز v1.36، در هر PodGroup تنها می‌توانید یک محدودیت توپولوژی تعیین کنید.
{{< /note >}}

### محدودیت توپولوژی

برای تعریف یک محدودیت توپولوژی برای یک PodGroup، باید یک `key` تنظیم کنید که متناظر با
یک برچسب نود در کوبرنتیز است و دامنه‌ی توپولوژی هدف (برای مثال، یک رک یا یک zone) را نشان می‌دهد.
زمان‌بند به‌طور قطعی اعمال می‌کند که همه‌ی Podهای درون PodGroup روی نودهایی قرار گیرند که
دقیقاً مقدار یکسانی برای این برچسب مشخص دارند.

در اینجا نمونه‌ای از یک PodGroup آمده است که با یک محدودیت توپولوژی پیکربندی شده است:

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: example-podgroup
spec:
  schedulingPolicy:
    gang:
      minCount: 4
  schedulingConstraints:
    topology:
      - key: topology.example.com/rack
```

## زمان‌بندی چندسطحی آگاه از توپولوژی

{{< feature-state feature_gate_name="CompositePodGroup" >}}

بارهای کاری پیچیده ممکن است به هم‌مکانی Podهای خود در سطوح مختلف زیرساخت
کلاستر نیاز داشته باشند. برای مثال، کل یک بار کاری ممکن است لازم باشد درون یک availability zone اجرا شود،
در حالی که بخش‌های مختلف آن بار کاری ممکن است به هم‌مکانی قطعی درون رک‌های سرور مشخصی نیاز داشته باشند.

چنین الزامات هم‌مکانی چندسطحی را می‌توان با استفاده از API مربوط به `CompositePodGroup` و
با تعیین محدودیت‌های توپولوژی در سطوح مختلف یک سلسله‌مراتب گروه بیان کرد.

استفاده از API مربوط به `CompositePodGroup` مستلزم فعال‌کردن
feature gate [`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
و
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3` است.

### تعیین محدودیت‌های توپولوژی چندسطحی

هر گروه درون یک سلسله‌مراتب `CompositePodGroup` می‌تواند یک محدودیت توپولوژی تعیین کند که
تضمین می‌کند همه‌ی Podهای نواده‌ی آن گروه در همان دامنه‌ی توپولوژی، مطابق با
محدودیت آن گروه، زمان‌بندی شوند.

در طول [زمان‌بندی سلسله‌مراتبی](/docs/concepts/scheduling-eviction/podgroup-scheduling)،
زمان‌بند این محدودیت‌ها را به شیوه‌ی **بالا به پایین** تعیین می‌کند. به‌طور مشخص، دامنه‌های توپولوژی‌ای که
در هنگام زمان‌بندی یک گروه فرزند در نظر گرفته می‌شوند، درون دامنه‌ی توپولوژی‌ای محدود می‌شوند که
متناظر با جای‌گذاری فرض‌شده برای گروه والد است.

کوبرنتیز هیچ الزام سختی بر سلسله‌مراتب فیزیکی برچسب‌های توپولوژی تحمیل نمی‌کند؛ کلیدهای
توپولوژی برچسب‌های دلخواه نود هستند. با این حال، ترتیبی که محدودیت‌های توپولوژی را از
والد به فرزند تعیین می‌کنید، ترتیب تقسیم دامنه‌های توپولوژی توسط زمان‌بند را مشخص می‌کند.

{{< note >}}
از کوبرنتیز v1.37، در هر
`CompositePodGroup` تنها می‌توانید یک محدودیت توپولوژی تعیین کنید.
{{< /note >}}

### مثال

مثال زیر یک `Workload` را پیکربندی می‌کند که در آن `CompositePodGroupTemplate` والد
کل بار کاری را به یک availability zone واحد (`topology.example.com/zone`) محدود می‌کند، در حالی که
دو مدخل `PodGroupTemplate` فرزند (`workers` و `driver`) Podهای مربوط به خود را
به رک‌های سرور (`topology.example.com/rack`) درون آن zone محدود می‌کنند:

```yaml
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: example-workload
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        minGroupCount: 2
    schedulingConstraints:
      topology:
      - key: topology.example.com/zone
    podGroupTemplates:
    - name: workers
      schedulingPolicy:
        gang:
          minCount: 8
      schedulingConstraints:
        topology:
        - key: topology.example.com/rack
    - name: driver
      schedulingPolicy:
        gang:
          minCount: 1
      schedulingConstraints:
        topology:
        - key: topology.example.com/rack
```

پس از ایجاد آبجکت `Workload`، آبجکت‌های گروه متناظر به شرح زیر ایجاد می‌شوند:

- یک `CompositePodGroup` ریشه که به الگوی `root` ارجاع می‌دهد.
- دو آبجکت `PodGroup` فرزند (`workers` و `driver`) که هر کدام به
  `CompositePodGroup` ریشه به‌عنوان گروه والد خود ارجاع می‌دهند.

```yaml
apiVersion: scheduling.k8s.io/v1alpha3
kind: CompositePodGroup
metadata:
  name: workload-root
spec:
  workloadRef:
    workloadName: example-workload
    templateName: root
  schedulingPolicy:
    gang:
      minGroupCount: 2
  schedulingConstraints:
    topology:
    - key: topology.example.com/zone
---
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: workload-workers
spec:
  parentCompositePodGroupName: workload-root
  workloadRef:
    workloadName: example-workload
    templateName: workers
  schedulingPolicy:
    gang:
      minCount: 8
  schedulingConstraints:
    topology:
    - key: topology.example.com/rack
---
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: workload-driver
spec:
  parentCompositePodGroupName: workload-root
  workloadRef:
    workloadName: example-workload
    templateName: driver
  schedulingPolicy:
    gang:
      minCount: 1
  schedulingConstraints:
    topology:
    - key: topology.example.com/rack
```

در هنگام زمان‌بندی، زمان‌بند ابتدا یک availability zone برای `workload-root` انتخاب می‌کند. سپس
نودهای آن zone را بر اساس رک تقسیم می‌کند تا جای‌گذاری‌های رک امکان‌پذیر را برای `workload-workers`
و `workload-driver` درون zone انتخاب‌شده بیابد.

برای مثال، کلاستری با پنج نود را در نظر بگیرید که به شکل زیر برچسب‌گذاری شده‌اند:

| نود | `topology.example.com/zone` | `topology.example.com/rack` |
| --- | --- | --- |
| `node-a` | `zone-1` | `rack-1` |
| `node-b` | `zone-1` | `rack-1` |
| `node-c` | `zone-1` | `rack-2` |
| `node-d` | `zone-2` | `rack-1` |
| `node-e` | `zone-2` | `rack-3` |

هنگام پردازش `workload-root`، زمان‌بند جای‌گذاری‌های نامزد را در میان همه‌ی نودهای کلاستر
بر اساس کلید توپولوژی `topology.example.com/zone` ارزیابی می‌کند:

| جای‌گذاری نامزد ارزیابی‌شده | نودهای جای‌گذاری نامزد |
| --- | --- |
| `zone-1` | `node-a`، `node-b`، `node-c` |
| `zone-2` | `node-d`، `node-e` |

هنگام ارزیابی جای‌گذاری‌های نامزد برای `workload-workers`، زمان‌بند تنها نودهای درون
جای‌گذاری فرض‌شده برای `workload-root` را بر اساس کلید توپولوژی `topology.example.com/rack` تقسیم می‌کند:

| جای‌گذاری والد | جای‌گذاری نامزد ارزیابی‌شده | نودهای جای‌گذاری نامزد |
| --- | --- | --- |
| `zone-1` | `rack-1` | `node-a`، `node-b` |
| `zone-1` | `rack-2` | `node-c` |
| `zone-2` | `rack-1` | `node-d` |
| `zone-2` | `rack-3` | `node-e` |

جای‌گذاری‌های نامزدی که برای PodGroup هم‌سطح `workload-driver` تولید می‌شوند، با جای‌گذاری‌هایی که
برای `workload-workers` تولید می‌شوند یکسان هستند، زیرا هر دو گروه کلید توپولوژی یکسانی
(`topology.example.com/rack`) تعیین می‌کنند.

## {{% heading "whatsnext" %}}

* درباره‌ی [سیاست‌های گروه Pod](/docs/concepts/workloads/workload-api/policies/) بیاموزید.
* درباره‌ی [افزونه‌های مرتبط با زمان‌بندی آگاه از توپولوژی](/docs/concepts/scheduling-eviction/topology-aware-scheduling/) بیاموزید
* درباره‌ی الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) بخوانید.
* درباره‌ی [بلوک‌های سازنده‌ی زمان‌بندی و کتابخانه‌ی workloadbuilder](/docs/concepts/workloads/workload-api/workloadbuilder/)، از جمله بلوک سازنده‌ی محدودیت‌های زمان‌بندی، بیاموزید.

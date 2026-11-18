---
title: اختلال و اولویت در گروه‌های Pod
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

هر PodGroup می‌تواند یک حالت اختلال (disruption mode) اعلام کند. این حالت تعیین می‌کند که
زمان‌بند چگونه می‌تواند یک PodGroup در حال اجرا را مختل کند؛ برای نمونه، تا جا را برای یک PodGroup
با اولویت بالاتر باز کند. هر PodGroup همچنین یک اولویت دارد که در رویدادهای
[پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
جایگزین اولویت تک‌تک Podهای آن گروه می‌شود.

<!-- body -->

## انواع حالت اختلال

{{< note >}}
در نسخهٔ v1.36، فیلدهای `priority` و `disruptionMode` در PodGroup فقط در
[پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) رعایت می‌شوند.
زمان‌بند در مرحلهٔ زمان‌بندی Pod، فیلدهای `priority` و `disruptionMode` در PodGroup را در نظر نمی‌گیرد.
این محدودیت در نسخهٔ v1.37 دیگر وجود ندارد.
{{< /note >}}

این API از دو حالت اختلال پشتیبانی می‌کند: `Single` و `All`.
حالت پیش‌فرض `Single` است.

### Single

حالت `Single` به زمان‌بند دستور می‌دهد که همهٔ Podهای گروه را موجودیت‌هایی جداگانه در نظر بگیرد؛
به این ترتیب، هر Pod از یک PodGroup را می‌توان به‌طور مستقل مختل کرد.

### All

حالت `All` بر معنای «همه یا هیچ» در اختلال تأکید دارد.
این حالت به زمان‌بند اعلام می‌کند که همهٔ Podهای یک PodGroup باید با هم مختل شوند.

## CompositePodGroup

{{< feature-state feature_gate_name="CompositePodGroup" >}}

یک `CompositePodGroup` نیز می‌تواند در مشخصات (specification) خود یک `disruptionMode` اعلام کند.
این فیلد تعیین می‌کند که زمان‌بند در رویدادهای پیش‌دستی، گروه‌های فرزند درون گروه مرکب را چگونه مختل کند.

این API برای `CompositePodGroups` از دو حالت اختلال پشتیبانی می‌کند:

- **`Single`**: اجازه می‌دهد هر یک از گروه‌های فرزند درون `CompositePodGroup` در هنگام پیش‌دستی
  به‌طور مستقل مختل شود.
- **`All`**: معنای «همه یا هیچ» را در سراسر سلسله‌مراتب `CompositePodGroup` اعمال می‌کند.
  اگر لازم باشد هر یک از Podهای موجود در سلسله‌مراتبِ زیر این `CompositePodGroup` مشمول پیش‌دستی شود،
  همهٔ Podهای کل سلسله‌مراتب باید مشمول پیش‌دستی شوند.

اگر حالتی مشخص نشود، مقدار پیش‌فرض `Single` است.

{{< note >}}
در نسخهٔ v1.37، یک گروه می‌تواند حالت اختلال خود را `All` تنظیم کند و گروه‌های فرزندی داشته باشد که حالتشان
`Single` است. در چنین وضعیتی، حالت `All` در سطح بالا بر حالت‌های `Single` در نوادگان غلبه می‌کند.

به دلیل مبهم بودن معنای این پیکربندی، استفاده از آن توصیه نمی‌شود.
{{< /note >}}

## اولویت گروه Pod

مفهوم [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
در PodGroup به همان شکلی به کار می‌رود که در Podهای منفرد.
پس از ایجاد یک یا چند PriorityClass، می‌توانید PodGroupای بسازید که نام یکی از آن PriorityClassها را
در مشخصات خود تعیین کند.
کنترل‌کنندهٔ پذیرش اولویت (priority admission controller) از فیلد `priorityClassName` استفاده می‌کند
و مقدار عددی اولویت را پر می‌کند.
اگر کلاس اولویت پیدا نشود، PodGroup رد می‌شود.
اگر `priorityClassName` برای یک PodGroup تنظیم نشده باشد، کوبرنتیز به دنبال یک کلاس پیش‌فرض
(یعنی PriorityClassای که `globalDefault` آن true است) می‌گردد.
اگر هیچ PriorityClassای با `globalDefault` برابر true وجود نداشته باشد، اولویت PodGroupای که
`priorityClassName` ندارد صفر خواهد بود.

اولویت PodGroup در رویدادهای [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
اولویت مرجع برای همهٔ Podهای گروه است.
از این مقدار برای ترتیب‌دادن PodGroupها در صف زمان‌بندی نیز استفاده می‌شود.
اگر اولویت Podهای تشکیل‌دهندهٔ این PodGroup با اولویت خود PodGroup متفاوت باشد،
PodGroup با خطای `all pods in a single pod group should have the same priority as the pod group`
زمان‌بندی نخواهد شد.

وقتی feature gate با نام [PodGroupPreemptionPolicy](/docs/reference/command-line-tools-reference/feature-gates/podgroup-preemption-policy/)
فعال باشد، PodGroup فیلد `preemptionPolicy` را نیز دارد. مقدار این فیلد نیز از PriorityClass گرفته می‌شود.
این فیلد برای همهٔ Podهای گروه مرجع است و تعیین می‌کند که آیا PodGroup می‌تواند برای باز کردن جا برای خود،
Podها و گروه‌های Pod با اولویت پایین‌تر را مشمول پیش‌دستی کند یا نه. وقتی این feature gate فعال باشد،
همهٔ Podهای درون PodGroup باید `preemptionPolicy` یکسانی با PodGroup داشته باشند. در غیر این صورت، PodGroup با خطای
`all pods in a single pod group should have the same preemption policy as the pod group's preemption policy`
زمان‌بندی نخواهد شد.
وقتی PodGroup دارای `preemptionPolicy: Never` باشد، پیش‌دستی آگاه از بار کاری انجام نمی‌دهد.
اگر این feature gate غیرفعال باشد، همهٔ Podهای تشکیل‌دهندهٔ PodGroup باید `preemptionPolicy` یکسانی داشته باشند.
در غیر این صورت، PodGroup با خطای
`all pods in a single pod group should have the same preemption policy`
زمان‌بندی نخواهد شد.

قطعه YAML زیر نمونه‌ای از پیکربندی یک PodGroup است که از PriorityClass با نام `high-priority` استفاده می‌کند؛
این کلاس به مقدار عددی اولویت 1000000 نگاشت می‌شود.
کنترل‌کنندهٔ پذیرش اولویت، مشخصات را بررسی می‌کند و اولویت PodGroup را 1000000 تعیین می‌کند.

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  namespace: ns-1
  name: job-1
spec:
  priorityClassName: high-priority
```

### اولویت CompositePodGroup

{{< feature-state feature_gate_name="CompositePodGroup" >}}

در API مربوط به `CompositePodGroup` نیز فیلدهای `priorityClassName` و `priority` وجود دارند و مقدار آن‌ها
به همان روشی که برای `PodGroups` گفته شد، از طریق کنترل‌کنندهٔ پذیرش اولویت تعیین می‌شود.

در رویدادهای [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)،
اولویت `CompositePodGroup` ریشه، اولویت مرجع برای همهٔ گروه‌های فرزند و Podهای درون سلسله‌مراتب آن است.
همهٔ Podهای درون یک سلسله‌مراتب گروهی باید دقیقاً اولویت یکسانی داشته باشند و این اولویت باید با
اولویت `CompositePodGroup` ریشه برابر باشد.

از مقدار اولویت برای ترتیب‌دادن `CompositePodGroups` ریشه در صف فعال زمان‌بندی نیز استفاده می‌شود.

{{< note >}}
در نسخهٔ v1.37، زمان‌بند بررسی نمی‌کند که مقدار اولویت گروه‌های غیرریشه با اولویت
`CompositePodGroup` ریشه برابر باشد.
{{< /note >}}

### سیاست پیش‌دستی در CompositePodGroup

{{< feature-state feature_gate_name="PodGroupPreemptionPolicy" >}}

در API مربوط به `CompositePodGroup` نیز فیلد `preemptionPolicy` وجود دارد و مقدار آن دقیقاً به همان روشی
تعیین می‌شود که در API مربوط به `PodGroup`.

مقدار `preemptionPolicy` در `CompositePodGroup` ریشه تعیین می‌کند که آیا در صورت نیاز می‌توان
[پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) را
برای جا دادن Podهای آن در هنگام زمان‌بندی فراخواند یا نه:

- سیاست `PreemptLowerPriority` اجازه می‌دهد قربانیانی با اولویت پایین‌تر مشمول پیش‌دستی شوند،
- سیاست `Never` پیش‌دستی آگاه از بار کاری را برای آن `CompositePodGroup` ریشه غیرفعال می‌کند.

همهٔ Podهای درون یک سلسله‌مراتب گروهی باید دقیقاً سیاست پیش‌دستی یکسانی داشته باشند و این سیاست باید با
سیاست پیش‌دستی `CompositePodGroup` ریشه برابر باشد.

اگر این feature gate غیرفعال باشد، `CompositePodGroup` ریشه مجاز به انجام پیش‌دستی خواهد بود،
مگر آنکه `preemptionPolicy` یکی از Podهای متعلق به سلسله‌مراتب گروه روی `Never` تنظیم شده باشد.

{{< note >}}
در نسخهٔ v1.37، وقتی این feature gate فعال باشد، زمان‌بند بررسی نمی‌کند که سیاست پیش‌دستی گروه‌های غیرریشه
با سیاست پیش‌دستی `CompositePodGroup` ریشه برابر باشد.
{{< /note >}}

## {{% heading "whatsnext" %}}

* دربارهٔ الگوریتم [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) مطالعه کنید.
* با [Workload API](/docs/concepts/workloads/workload-api/) آشنا شوید.
* با [اجزای سازندهٔ زمان‌بندی و کتابخانهٔ workloadbuilder](/docs/concepts/workloads/workload-api/workloadbuilder/)، از جمله جزء سازندهٔ حالت اختلال، آشنا شوید.

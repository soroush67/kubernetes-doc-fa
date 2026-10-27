---
title: اختلال و اولویت گروه Pod
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

PodGroup می‌تواند یک حالت اختلال (disruption mode) اعلام کند. این حالت تعیین می‌کند که
زمان‌بند چگونه می‌تواند یک PodGroup در حال اجرا را دچار اختلال کند، برای مثال برای جادادن
یک PodGroup با اولویت بالاتر. یک PodGroup همچنین یک اولویت دارد
که در رویدادهای [پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
بر اولویت تک‌تک Podهای آن گروه مقدم است.

<!-- body -->

## انواع حالت اختلال

{{< note >}}
در v1.36، فیلدهای `priority` یا `disruptionMode` آن PodGroup تنها
در [پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) رعایت می‌شوند.
در مرحله‌ی زمان‌بندی Pod، زمان‌بند فیلدهای `priority` یا `disruptionMode`
آن PodGroup را در نظر نمی‌گیرد. این محدودیت در v1.37 دیگر
وجود ندارد.
{{< /note >}}

API از دو حالت اختلال پشتیبانی می‌کند: `Single` و `All`.
حالت پیش‌فرض `Single` است.

### Single

حالت `Single` به زمان‌بند دستور می‌دهد با همه‌ی Podهای گروه به‌عنوان موجودیت‌های جداگانه رفتار کند
و اجازه می‌دهد یک Pod از یک PodGroup به‌طور مستقل دچار اختلال شود.

### All

حالت `All` بر معنای «همه یا هیچ» برای اختلال تأکید دارد.
این حالت به زمان‌بند اعلام می‌کند که همه‌ی Podهای آن PodGroup باید با هم دچار اختلال شوند.

## CompositePodGroup

{{< feature-state feature_gate_name="CompositePodGroup" >}}

یک `CompositePodGroup` نیز می‌تواند در مشخصات خود یک `disruptionMode` اعلام کند که کنترل می‌کند
زمان‌بند در رویدادهای پس‌گیری، گروه‌های فرزند درون گروه مرکب را چگونه دچار اختلال کند.

API از دو حالت اختلال برای `CompositePodGroups` پشتیبانی می‌کند:

- **`Single`**: اجازه می‌دهد تک‌تک گروه‌های فرزند درون `CompositePodGroup` در هنگام پس‌گیری
  به‌طور مستقل دچار اختلال شوند.
- **`All`**: معنای اختلال همه یا هیچ را در سراسر سلسله‌مراتب `CompositePodGroup` اعمال می‌کند.
  اگر هر Podی که در سلسله‌مراتب زیر این `CompositePodGroup` قرار دارد باید پس گرفته شود، همه‌ی
  Podهای کل سلسله‌مراتب باید پس گرفته شوند.

اگر حالتی تعیین نشود، حالت پیش‌فرض `Single` است.

{{< note >}}
در v1.37، یک گروه می‌تواند حالت اختلال خود را روی `All` تنظیم کند و گروه‌های فرزندی داشته باشد که حالت آن‌ها
`Single` است. در چنین حالتی، حالت `All` سطح بالا بر حالت‌های `Single` نوادگان مقدم است.

به دلیل مبهم بودن معنای این پیکربندی، استفاده از آن توصیه نمی‌شود.
{{< /note >}}

## اولویت گروه Pod

PodGroup از همان مفهوم [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) استفاده می‌کند که Podهای منفرد استفاده می‌کنند.
پس از آنکه یک یا چند PriorityClass ایجاد کردید،
می‌توانید یک PodGroup ایجاد کنید که یکی از این نام‌های PriorityClass را در مشخصات خود تعیین کند.
کنترل‌کننده‌ی پذیرش اولویت (priority admission controller) از فیلد `priorityClassName` استفاده می‌کند و مقدار عددی اولویت را پر می‌کند.
اگر کلاس اولویت یافت نشود، آن PodGroup رد می‌شود.
هنگامی که `priorityClassName` برای یک PodGroup تنظیم نشده باشد، کوبرنتیز به دنبال یک مقدار پیش‌فرض می‌گردد (یک PriorityClass که `globalDefault` آن روی true تنظیم شده است).
اگر هیچ PriorityClassی با `globalDefault` برابر true وجود نداشته باشد، PodGroupی که `priorityClassName` ندارد اولویت صفر خواهد داشت.

اولویت PodGroup در رویدادهای [پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) اولویت مرجع برای همه‌ی Podهای گروه است.
این مقدار همچنین برای مرتب‌سازی PodGroupها در صف زمان‌بندی استفاده می‌شود.
هنگامی که اولویت تک‌تک Podهای تشکیل‌دهنده‌ی این PodGroup با اولویت PodGroup متفاوت باشد،
آن PodGroup با خطای `all pods in a single pod group should have the same priority as the pod group` زمان‌بندی نمی‌شود.

هنگامی که feature gate [PodGroupPreemptionPolicy](/docs/reference/command-line-tools-reference/feature-gates/podgroup-preemption-policy/)
فعال باشد، PodGroup فیلد `preemptionPolicy` را نیز دارد. این فیلد نیز از PriorirtyClass گرفته می‌شود.
این فیلد برای همه‌ی Podهای گروه مرجع است و تعیین می‌کند که آیا PodGroup می‌تواند Podها و گروه‌های Pod با
اولویت پایین‌تر را پس بگیرد تا برای خود جا باز کند یا خیر. هنگامی که این feature gate فعال باشد، همه‌ی Podهای آن PodGroup
باید همان `preemptionPolicy` آن PodGroup را داشته باشند. در غیر این صورت، آن PodGroup با خطای
`all pods in a single pod group should have the same preemption policy as the pod group's preemption policy` زمان‌بندی نمی‌شود.
هنگامی که PodGroup دارای `preemptionPolicy: Never` باشد، پس‌گیری آگاه از بار کاری را انجام نمی‌دهد.
اگر این feature flag غیرفعال باشد، همه‌ی Podهای تشکیل‌دهنده‌ی PodGroup باید `preemptionPolicy` یکسانی داشته باشند.
در غیر این صورت، آن PodGroup با خطای
`all pods in a single pod group should have the same preemption policy` زمان‌بندی نمی‌شود.

YAML زیر نمونه‌ای از پیکربندی یک PodGroup است که از PriorityClass با نام `high-priority` استفاده می‌کند،
که به مقدار عددی اولویت 1000000 نگاشت می‌شود.
کنترل‌کننده‌ی پذیرش اولویت مشخصات را بررسی می‌کند و اولویت PodGroup را 1000000 تعیین می‌کند.

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

API مربوط به `CompositePodGroup` نیز فیلدهای `priorityClassName` و `priority` را دارد و مقدار آن‌ها
به همان روشی که برای `PodGroups` انجام می‌شود، از طریق کنترل‌کننده‌ی پذیرش اولویت تعیین می‌شود.

اولویت یک `CompositePodGroup` ریشه در رویدادهای
[پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
به‌عنوان اولویت مرجع برای همه‌ی گروه‌های فرزند و Podهای درون سلسله‌مراتب آن عمل می‌کند.
همه‌ی Podهای درون یک سلسله‌مراتب گروه باید دقیقاً اولویت یکسانی داشته باشند و این اولویت باید با
اولویت `CompositePodGroup` ریشه برابر باشد.

مقدار اولویت همچنین برای مرتب‌سازی `CompositePodGroups` ریشه در صف فعال
زمان‌بندی استفاده می‌شود.

{{< note >}}
در v1.37، زمان‌بند بررسی نمی‌کند که آیا گروه‌های غیرریشه مقدار اولویتی برابر با
اولویت `CompositePodGroup` ریشه دارند یا خیر.
{{< /note >}}

### PreemptionPolicy در CompositePodGroup

{{< feature-state feature_gate_name="PodGroupPreemptionPolicy" >}}

API مربوط به `CompositePodGroup` فیلد `preemptionPolicy` را نیز دارد و مقدار آن دقیقاً
به همان روشی که برای API مربوط به `PodGroup` انجام می‌شود تعیین می‌گردد.

مقدار `preemptionPolicy` در `CompositePodGroup` ریشه تعیین می‌کند که آیا
[پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) می‌تواند
در صورت نیاز در هنگام زمان‌بندی برای جادادن Podهای آن فراخوانی شود یا خیر:

- سیاست `PreemptLowerPriority` اجازه‌ی پس‌گرفتن قربانیانی با اولویت پایین‌تر را می‌دهد،
- سیاست `Never` پس‌گیری آگاه از بار کاری را برای آن `CompositePodGroup` ریشه غیرفعال می‌کند.

همه‌ی Podهای درون یک سلسله‌مراتب گروه باید دقیقاً سیاست پس‌گیری یکسانی داشته باشند که باید
با سیاست پس‌گیری `CompositePodGroup` ریشه برابر باشد.

اگر این feature flag غیرفعال باشد، `CompositePodGroup` ریشه مجاز به انجام پس‌گیری خواهد بود،
مگر آنکه یکی از Podهای متعلق به سلسله‌مراتب گروه، `preemptionPolicy` را روی `Never` تنظیم کرده باشد.

{{< note >}}
در v1.37، هنگامی که این feature gate فعال باشد، زمان‌بند بررسی نمی‌کند که آیا گروه‌های غیرریشه
سیاست پس‌گیری‌ای برابر با سیاست پس‌گیری `CompositePodGroup` ریشه دارند یا خیر.
{{< /note >}}

## {{% heading "whatsnext" %}}

* درباره‌ی الگوریتم [پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) بخوانید.
* درباره‌ی [Workload API](/docs/concepts/workloads/workload-api/) بیاموزید.
* درباره‌ی [بلوک‌های سازنده‌ی زمان‌بندی و کتابخانه‌ی workloadbuilder](/docs/concepts/workloads/workload-api/workloadbuilder/)، از جمله بلوک سازنده‌ی حالت اختلال، بیاموزید.

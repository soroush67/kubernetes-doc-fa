---
title: "شرایط Pod"
content_type: concept
weight: 35
---

در کوبرنتیز، بسیاری از آبجکت‌ها دارای _شرایط_ (conditions) هستند.
شرایط، نشانگرهایی برای جنبه‌ای از وضعیت واقعی چیزی هستند که آبجکت نمایانگر آن است.
Podها نیز شرایطی دارند و شرایط Pod در کوبرنتیز جنبه مهمی از چگونگی درک سلامت یک Pod
توسط کنترل‌کننده‌ها (و افرادی که عیب‌یابی می‌کنند) است.

[فاز](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) یک Pod خلاصه‌ای سطح‌بالا از جایگاه Pod در چرخه حیات آن ارائه می‌دهد، اما یک مقدار واحد نمی‌تواند تصویر کامل را نشان دهد. برای مثال، ممکن است یک Pod در فاز `Running` باشد، اما هنوز آماده سرویس‌دهی به ترافیک نباشد.
شرایط Pod با پیگیری مستقل جنبه‌های مختلف وضعیت Pod، فاز را تکمیل می‌کنند؛ جنبه‌هایی مانند اینکه Pod زمان‌بندی شده است یا نه، کانتینرهای آن آماده‌اند یا نه، تغییر اندازه (resize) در حال انجام است یا نه، یا اینکه Pod به دلیل یک {{< glossary_tooltip text="taint" term_id="taint" >}} در آستانه مختل شدن (disruption) است یا نه.

## ساختار شرط Pod {#structure-of-a-pod-condition}

وضعیت (status) یک Pod شامل آرایه‌ای از
[PodConditions](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podcondition-v1-core)
است که نشان می‌دهد Pod از چه نقاط بررسی‌ای عبور کرده است.

هر عنصر آرایه PodCondition دارای فیلدهای زیر است:

{{< table caption="فیلدهای PodCondition" >}}
| نام فیلد             | توضیحات                                                                                              |
|:---------------------|:-----------------------------------------------------------------------------------------------------|
| `type`               | نام این شرط Pod.                                                                                     |
| `status`             | نشان می‌دهد که آیا آن شرط برقرار است یا خیر؛ مقادیر ممکن `"True"`، `"False"` یا `"Unknown"` هستند. |
| `lastProbeTime`      | مهر زمانی آخرین باری که شرط Pod بررسی (probe) شده است.                                               |
| `lastTransitionTime` | مهر زمانی آخرین باری که Pod از یک وضعیت به وضعیت دیگر گذار کرده است.                                 |
| `reason`             | متنی قابل‌پردازش برای ماشین، به قالب UpperCamelCase، که دلیل آخرین گذار شرط را نشان می‌دهد.         |
| `message`            | پیامی قابل‌خواندن برای انسان که جزئیات آخرین گذار وضعیت را بیان می‌کند.                              |
| `observedGeneration` | مقدار `.metadata.generation` مربوط به Pod در زمان ثبت شرط. به [نسل Pod](/docs/concepts/workloads/pods/#pod-generation) مراجعه کنید. |
{{< /table >}}

## شرایط درون‌ساخت Pod {#built-in-pod-conditions}

کوبرنتیز شرایط Pod زیر را مدیریت می‌کند:

[شرایط چرخه حیات](#lifecycle-pod-conditions): با پیشرفت Pod در چرخه حیات خود و تقریباً به این ترتیب تنظیم می‌شوند:
`PodScheduled`، `PodReadyToStartContainers`، `Initialized`، `ContainersReady`، `Ready`.

[سایر شرایط](#other-pod-conditions): در پاسخ به عملیات یا رویدادهای خاص تنظیم می‌شوند:
`DisruptionTarget`، `PodResizePending`، `PodResizeInProgress`.

علاوه بر شرایط درون‌ساخت بالا، می‌توانید با استفاده از
[readiness gateهای Pod](#enhanced-pod-readiness) شرایط سفارشی تعریف کنید.

## شرایط چرخه حیات Pod {#lifecycle-pod-conditions}

با پیشرفت Pod در چرخه حیات خود، kubelet شرایط زیر را تقریباً به این ترتیب تنظیم می‌کند:

1. `PodScheduled`: Pod روی یک نود زمان‌بندی شده است.
1. `PodReadyToStartContainers`: sandbox مربوط به Pod با موفقیت ایجاد شده و شبکه پیکربندی شده است. sandbox و شبکه توسط {{< glossary_tooltip text="container runtime" term_id="container-runtime" >}} و افزونه {{< glossary_tooltip text="CNI" term_id="cni" >}} راه‌اندازی می‌شوند.
1. `Initialized`: همه [init containerها](/docs/concepts/workloads/pods/init-containers/) با موفقیت تکمیل شده‌اند. برای Podای که init container ندارد، این شرط پیش از ایجاد sandbox روی `True` تنظیم می‌شود.
1. `ContainersReady`: همه کانتینرهای Pod آماده هستند. آماده بودن یک کانتینر، در صورت پیکربندی، با [readiness probe](/docs/concepts/workloads/pods/probes/#readiness-probe) آن تعیین می‌شود.
1. `Ready`: Pod قادر به پاسخ‌گویی به درخواست‌هاست و باید به مجموعه‌های توزیع بار (load balancing) همه [Serviceهای](/docs/concepts/services-networking/service/) منطبق افزوده شود. Podهایی که `Ready` نیستند از endpointهای Service حذف می‌شوند.

{{< note >}}
شرط `Ready` فقط به `ContainersReady` وابسته نیست. اگر Pod مقدار `readinessGates` را مشخص کرده باشد، همه آن شرایط سفارشی نیز باید `True` باشند تا Pod در وضعیت `Ready` قرار گیرد. برای جزئیات به [آماده بودن Pod](#enhanced-pod-readiness) مراجعه کنید.
{{< /note >}}

می‌توانید شرایط یک Pod را با kubectl بررسی کنید:

```shell
kubectl get pod <pod-name> -o yaml
```

آنچه در ادامه می‌آید نشان می‌دهد `status.conditions` برای یک Pod در حال اجرا چگونه به نظر می‌رسد:

```yaml
status:
  conditions:
    - type: PodScheduled
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: PodReadyToStartContainers
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:16Z"
      observedGeneration: 1
    - type: Initialized
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: ContainersReady
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
    - type: Ready
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
```

### PodReadyToStartContainers {#pod-ready-to-start-containers}

{{< feature-state feature_gate_name="PodReadyToStartContainersCondition" >}}

{{< note >}}
در مراحل اولیه توسعه، این شرط `PodHasNetwork` نام داشت.
{{< /note >}}

پس از آنکه یک Pod روی یک نود زمان‌بندی شد، باید توسط kubelet پذیرش شود
و حجم‌های (volumes) ذخیره‌سازی موردنیاز آن نصب (mount) شوند. پس از تکمیل این مراحل،
kubelet با یک container runtime همکاری می‌کند
(با استفاده از {{< glossary_tooltip text="Container Runtime Interface (CRI)" term_id="cri" >}})
تا یک sandbox زمان اجرا راه‌اندازی کند و شبکه Pod را پیکربندی نماید.
شرط `PodReadyToStartContainers` به فیلد `status.conditions` یک Pod افزوده می‌شود.

زمانی که kubelet تشخیص دهد Pod فاقد sandbox زمان اجرا با شبکه پیکربندی‌شده است، این شرط را روی `False` تنظیم می‌کند. این وضعیت در سناریوهای زیر رخ می‌دهد:

- در مراحل ابتدایی چرخه حیات Pod، زمانی که kubelet هنوز با استفاده از container runtime شروع به راه‌اندازی sandbox برای Pod نکرده است.
- در مراحل بعدی چرخه حیات Pod، زمانی که sandbox مربوط به Pod به یکی از دلایل زیر از بین رفته باشد:
  - راه‌اندازی مجدد نود، بدون آنکه Pod اخراج (evict) شده باشد
  - برای container runtimeهایی که از ماشین‌های مجازی برای ایزوله‌سازی استفاده می‌کنند، راه‌اندازی مجدد ماشین مجازی sandbox مربوط به Pod، که در نتیجه نیازمند ایجاد یک sandbox جدید و پیکربندی تازه شبکه کانتینر است.

شرط `PodReadyToStartContainers` پس از تکمیل موفقیت‌آمیز ایجاد sandbox و پیکربندی شبکه Pod توسط افزونه runtime، به‌وسیله kubelet روی `True` تنظیم می‌شود. kubelet می‌تواند پس از آنکه شرط `PodReadyToStartContainers` روی `True` تنظیم شد، دریافت ایمیج‌های کانتینر و ایجاد کانتینرها را آغاز کند.

برای Podای که init container دارد، kubelet پس از تکمیل موفقیت‌آمیز init containerها (که پس از ایجاد موفق sandbox و پیکربندی شبکه توسط افزونه runtime رخ می‌دهد) شرط `Initialized` را روی `True` تنظیم می‌کند. برای Podای که init container ندارد، kubelet شرط `Initialized` را پیش از آغاز ایجاد sandbox و پیکربندی شبکه روی `True` تنظیم می‌کند.

## سایر شرایط Pod {#other-pod-conditions}

شرایط زیر بخشی از روند عادی چرخه حیات Pod نیستند.
آن‌ها در پاسخ به عملیات یا رویدادهای خاص تنظیم می‌شوند.

### DisruptionTarget {#disruption-target}

یک شرط اختصاصی Pod با نام `DisruptionTarget` افزوده می‌شود تا نشان دهد
Pod به دلیل یک {{<glossary_tooltip term_id="disruption" text="اختلال (disruption)">}} در آستانه حذف شدن است.
فیلد `reason` این شرط علاوه بر آن،
یکی از دلایل زیر را برای خاتمه یافتن Pod نشان می‌دهد:

`PreemptionByScheduler`
: Pod قرار است توسط یک زمان‌بند به‌منظور جاسازی یک Pod جدید با اولویت بالاتر {{<glossary_tooltip term_id="preemption" text="پیشدستی (preempt)">}} شود. برای اطلاعات بیشتر، به [پیشدستی بر اساس اولویت Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) مراجعه کنید.

`DeletionByTaintManager`
: Pod قرار است توسط Taint Manager (که بخشی از کنترل‌کننده چرخه حیات نود در `kube-controller-manager` است) به دلیل یک taint از نوع `NoExecute` که Pod آن را تحمل نمی‌کند حذف شود؛ به اخراج‌های مبتنی بر {{<glossary_tooltip term_id="taint" text="taint">}} مراجعه کنید.

`EvictionByEvictionAPI`
: Pod برای {{<glossary_tooltip term_id="api-eviction" text="اخراج با استفاده از API کوبرنتیز">}} علامت‌گذاری شده است.

`DeletionByPodGC`
: Podای که به نودی متصل است که دیگر وجود ندارد، قرار است توسط [زباله‌روبی Pod (Pod garbage collection)](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) حذف شود.

`TerminationByKubelet`
: Pod توسط kubelet خاتمه یافته است، به یکی از دلایل {{<glossary_tooltip term_id="node-pressure-eviction" text="اخراج ناشی از فشار نود">}}،
  [خاموش شدن مدیریت‌شده نود (graceful node shutdown)](/docs/concepts/architecture/nodes/#graceful-node-shutdown)،
  یا پیشدستی برای [Podهای حیاتی سیستم](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).

در تمام سناریوهای اختلال دیگر، مانند اخراج به دلیل تجاوز از
[محدودیت‌های کانتینر Pod](/docs/concepts/configuration/manage-resources-containers/)،
Podها شرط `DisruptionTarget` را دریافت نمی‌کنند، زیرا این اختلال‌ها
احتمالاً توسط خود Pod ایجاد شده‌اند و با تلاش مجدد دوباره رخ خواهند داد.

{{< note >}}
یک اختلال در Pod ممکن است قطع شود. control plane ممکن است دوباره تلاش کند
اختلال همان Pod را ادامه دهد، اما این امر تضمین‌شده نیست. در نتیجه،
شرط `DisruptionTarget` ممکن است به یک Pod افزوده شود، ولی آن Pod در عمل حذف نشود. در چنین وضعیتی، پس از مدتی،
شرط اختلال Pod پاک خواهد شد.
{{< /note >}}

همزمان با پاکسازی Podها، زباله‌روب Pod (PodGC) آن‌ها را در صورتی که در فازی غیرپایانی باشند، ناموفق (failed) نیز علامت‌گذاری می‌کند
(همچنین به [زباله‌روبی Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) مراجعه کنید).

هنگام استفاده از Job (یا CronJob)، ممکن است بخواهید از این شرایط اختلال Pod به‌عنوان بخشی از
[سیاست شکست Pod](/docs/concepts/workloads/controllers/job#pod-failure-policy) در Job خود استفاده کنید.

برای جزئیات بیشتر، به [اختلال‌ها (Disruptions)](/docs/concepts/workloads/pods/disruptions/) مراجعه کنید.

### PodResizePending و PodResizeInProgress {#pod-resize-conditions}

kubelet شرایط وضعیت Pod را به‌روزرسانی می‌کند تا وضعیت یک درخواست تغییر اندازه (resize) را نشان دهد:

- `type: PodResizePending`: kubelet نمی‌تواند درخواست را بلافاصله بپذیرد. فیلد `message` توضیح می‌دهد که چرا.
  - `reason: Infeasible`: تغییر اندازه درخواستی روی نود فعلی غیرممکن است (برای مثال، درخواست منابعی بیش از آنچه نود دارد).
  - `reason: Deferred`: تغییر اندازه درخواستی در حال حاضر ممکن نیست، اما ممکن است بعداً شدنی شود (برای مثال اگر Pod دیگری حذف شود). kubelet دوباره تلاش خواهد کرد.
- `type: PodResizeInProgress`: kubelet تغییر اندازه را پذیرفته و منابع را تخصیص داده است، اما تغییرات هنوز در حال اعمال شدن هستند. این مرحله معمولاً کوتاه است، اما بسته به نوع منبع و رفتار runtime ممکن است بیشتر طول بکشد. هر خطایی در حین اعمال تغییرات در فیلد `message` (همراه با `reason: Error`) گزارش می‌شود.

اگر تغییر اندازه درخواستی در وضعیت _Deferred_ باشد، kubelet به‌صورت دوره‌ای دوباره تلاش می‌کند تغییر اندازه را انجام دهد، برای مثال زمانی که Pod دیگری حذف یا کوچک‌مقیاس (scale down) شود.

برای جزئیات بیشتر درباره تغییر اندازه Pod، به [تغییر اندازه منابع CPU و حافظه تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) مراجعه کنید.

## آماده بودن پیشرفته Pod {#enhanced-pod-readiness}

برنامه شما می‌تواند بازخوردها یا سیگنال‌های اضافی را به `.status` مربوط به Pod تزریق کند؛
این قابلیت _آماده بودن پیشرفته Pod_ (enhanced Pod readiness) نامیده می‌شود.
برای استفاده از آن، مقدار `readinessGates` را در `spec` مربوط به Pod تنظیم کنید تا فهرستی از
شرایط اضافی را که kubelet برای آماده بودن Pod ارزیابی می‌کند مشخص نمایید.
سپس یک کنترل‌کننده پیاده‌سازی یا نصب می‌کنید که این شرایط سفارشی را مدیریت کند،
و kubelet از آن به‌عنوان ورودی اضافی برای تصمیم‌گیری درباره آماده بودن Pod استفاده می‌کند.

readiness gateها بر اساس وضعیت فعلی فیلدهای `status.condition` مربوط به Pod تعیین می‌شوند.
اگر کوبرنتیز نتواند چنین شرطی را در فیلد `status.conditions` یک Pod پیدا کند، وضعیت آن شرط به‌طور پیش‌فرض "`False`" در نظر گرفته می‌شود.

```yaml
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

شرایط Pod که اضافه می‌کنید باید نام‌هایی داشته باشند که با [قالب کلید برچسب](/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set) کوبرنتیز مطابقت داشته باشد.

### وضعیت برای آماده بودن Pod {#status-for-pod-readiness}

برای تنظیم این `status.conditions` در Pod، برنامه‌ها و
{{< glossary_tooltip term_id="operator-pattern" text="اپراتورها">}} باید از
عمل `PATCH` روی زیرمنبع status مربوط به Pod استفاده کنند. می‌توانید از `kubectl patch`
همراه با `--subresource=status` یا یک [کتابخانه کلاینت کوبرنتیز](/docs/reference/using-api/client-libraries/) برای نوشتن
کدی استفاده کنید که شرایط سفارشی Pod را برای آماده بودن Pod تنظیم می‌کند.

برای Podای که از شرایط سفارشی استفاده می‌کند، آن Pod **فقط** زمانی آماده ارزیابی می‌شود که هر دو گزاره زیر برقرار باشند:

- همه کانتینرهای Pod آماده باشند.
- همه شرایط مشخص‌شده در `readinessGates` برابر `True` باشند.

هنگامی که کانتینرهای یک Pod آماده (Ready) هستند اما دست‌کم یک شرط سفارشی وجود ندارد یا `False` است،
kubelet شرط `Ready` مربوط به Pod را با `status: "False"` و `reason: ReadinessGatesNotReady` تنظیم می‌کند.

## {{% heading "whatsnext" %}}

- درباره [چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/) بیاموزید.
- درباره [اختلال‌ها (Disruptions)](/docs/concepts/workloads/pods/disruptions/) بیاموزید.
- درباره [probeهای کانتینر](/docs/concepts/workloads/pods/probes/) و چگونگی تأثیر آن‌ها بر آماده بودن Pod بیاموزید.
- بیاموزید چگونه [منابع Pod را به‌صورت درجا (in-place) تغییر اندازه دهید](/docs/tasks/configure-pod-container/resize-container-resources/).

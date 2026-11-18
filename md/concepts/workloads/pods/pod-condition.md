---
title: "وضعیت‌های Pod"
content_type: concept
weight: 35
---

در کوبرنتیز، بسیاری از آبجکت‌ها دارای _وضعیت (condition)_ هستند.
وضعیت‌ها نشانگرهایی هستند که جنبه‌ای از حالت واقعیِ چیزی را که آبجکت نمایندهٔ آن است نشان می‌دهند.
Podها نیز وضعیت دارند. وضعیت‌های Pod در کوبرنتیز نقش مهمی دارند، زیرا کنترل‌کننده‌ها
(و افرادی که عیب‌یابی می‌کنند) به کمک آن‌ها سلامت یک Pod را درک می‌کنند.

[فاز](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) یک Pod خلاصه‌ای سطح‌بالا
از جایگاه Pod در چرخهٔ عمرش ارائه می‌دهد، اما یک مقدار واحد نمی‌تواند تصویر کامل را
نشان دهد. برای مثال، ممکن است یک Pod در فاز `Running` باشد، اما هنوز آمادهٔ پاسخ‌گویی به ترافیک نباشد.
وضعیت‌های Pod فاز را تکمیل می‌کنند؛ آن‌ها چندین جنبه از حالت Pod را به‌طور مستقل
دنبال می‌کنند؛ برای نمونه اینکه آیا Pod زمان‌بندی شده است، آیا کانتینرهای آن آماده‌اند،
آیا تغییر اندازه‌ای در جریان است، یا آیا Pod به دلیل یک
{{< glossary_tooltip text="taint" term_id="taint" >}} در آستانهٔ اختلال قرار دارد.

## ساختار یک وضعیت Pod

بخش status هر Pod شامل آرایه‌ای از
[PodConditionها](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podcondition-v1-core)
است که نشان می‌دهد آیا Pod از نقاط بررسی مشخصی عبور کرده است یا نه.

هر عنصر از آرایهٔ PodCondition فیلدهای زیر را دارد:

{{< table caption="فیلدهای یک PodCondition" >}}
| نام فیلد           | توضیحات                                                                                          |
|:---------------------|:-----------------------------------------------------------------------------------------------------|
| `type`               | نام این وضعیت Pod.                                                                          |
| `status`             | نشان می‌دهد که آیا آن وضعیت برقرار است یا نه؛ مقادیر ممکن `"True"`، `"False"` یا `"Unknown"` هستند. |
| `lastProbeTime`      | مُهر زمانیِ آخرین باری که وضعیت Pod بررسی شده است.                                                 |
| `lastTransitionTime` | مُهر زمانیِ آخرین باری که Pod از یک حالت به حالت دیگر گذار کرده است.                             |
| `reason`             | متنی ماشین‌خوان به شکل UpperCamelCase که دلیل آخرین گذار وضعیت را نشان می‌دهد.     |
| `message`            | پیامی انسان‌خوان که جزئیات آخرین گذار حالت را بیان می‌کند.                          |
| `observedGeneration` | مقدار `.metadata.generation` مربوط به Pod در زمانی که وضعیت ثبت شده است. [نسل Pod](/docs/concepts/workloads/pods/#pod-generation) را ببینید. |
{{< /table >}}

## وضعیت‌های داخلی Pod {#built-in-pod-conditions}

کوبرنتیز وضعیت‌های زیر را برای Pod مدیریت می‌کند:

[وضعیت‌های چرخهٔ عمر](#lifecycle-pod-conditions): این وضعیت‌ها با پیشرفت Pod در چرخهٔ عمرش، تقریباً به این ترتیب تنظیم می‌شوند:
`PodScheduled`، `PodReadyToStartContainers`، `Initialized`، `ContainersReady`، `Ready`.

[سایر وضعیت‌ها](#other-pod-conditions): این وضعیت‌ها در واکنش به عملیات یا رویدادهای مشخص تنظیم می‌شوند:
`DisruptionTarget`، `PodResizePending`، `PodResizeInProgress`.

افزون بر وضعیت‌های داخلی بالا، می‌توانید با استفاده از
[دروازه‌های آمادگی Pod](#enhanced-pod-readiness) وضعیت‌های سفارشی تعریف کنید.

## وضعیت‌های چرخهٔ عمر Pod {#lifecycle-pod-conditions}

با پیشرفت Pod در چرخهٔ عمرش، kubelet وضعیت‌های زیر را تقریباً به این ترتیب تنظیم می‌کند:

1. وضعیت `PodScheduled`: Pod روی یک نود زمان‌بندی شده است.
1. وضعیت `PodReadyToStartContainers`: سندباکس (sandbox) Pod با موفقیت ایجاد شده و شبکهٔ آن پیکربندی شده است. سندباکس و شبکه به‌وسیلهٔ {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} و افزونهٔ {{< glossary_tooltip text="CNI" term_id="cni" >}} راه‌اندازی می‌شوند.
1. وضعیت `Initialized`: همهٔ [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/) با موفقیت به پایان رسیده‌اند. برای Podی که کانتینر init ندارد، این وضعیت پیش از ایجاد سندباکس روی `True` تنظیم می‌شود.
1. وضعیت `ContainersReady`: همهٔ کانتینرهای Pod آماده‌اند. آمادگی هر کانتینر، در صورت پیکربندی، با [کاوشگر آمادگی (readiness probe)](/docs/concepts/workloads/pods/probes/#readiness-probe) آن تعیین می‌شود.
1. وضعیت `Ready`: Pod می‌تواند به درخواست‌ها پاسخ دهد و باید به مخزن‌های توزیع بار همهٔ [Serviceهای](/docs/concepts/services-networking/service/) منطبق افزوده شود. Podهایی که `Ready` نیستند از endpointهای Service حذف می‌شوند.

{{< note >}}
وضعیت `Ready` به چیزی بیش از `ContainersReady` وابسته است. اگر Pod فیلد `readinessGates` را مشخص کرده باشد، همهٔ آن وضعیت‌های سفارشی نیز باید `True` باشند تا Pod در حالت `Ready` قرار گیرد. برای جزئیات، [آمادگی Pod](#enhanced-pod-readiness) را ببینید.
{{< /note >}}

می‌توانید وضعیت‌های یک Pod را با kubectl بررسی کنید:

```shell
kubectl get pod <pod-name> -o yaml
```

نمونهٔ زیر نشان می‌دهد که `status.conditions` برای یک Pod در حال اجرا چگونه است:

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

### وضعیت PodReadyToStartContainers {#pod-ready-to-start-containers}

{{< feature-state feature_gate_name="PodReadyToStartContainersCondition" >}}

{{< note >}}
نام این وضعیت در مراحل اولیهٔ توسعه `PodHasNetwork` بود.
{{< /note >}}

پس از آنکه یک Pod روی نودی زمان‌بندی شد، kubelet باید آن را بپذیرد
و حجم‌های ذخیره‌سازی موردنیاز آن mount شوند. پس از کامل شدن این مراحل،
kubelet با همکاری محیط اجرای کانتینر
(از طریق {{< glossary_tooltip text="رابط محیط اجرای کانتینر (CRI)" term_id="cri" >}})
یک سندباکس اجرایی راه‌اندازی می‌کند و شبکهٔ Pod را پیکربندی می‌کند.
وضعیت `PodReadyToStartContainers` به فیلد `status.conditions` مربوط به Pod افزوده می‌شود.

هرگاه kubelet تشخیص دهد که Pod سندباکس اجرایی با شبکهٔ پیکربندی‌شده ندارد، این وضعیت را روی `False` تنظیم می‌کند. این اتفاق در سناریوهای زیر رخ می‌دهد:

- در اوایل چرخهٔ عمر Pod، زمانی که kubelet هنوز راه‌اندازی سندباکس Pod را به کمک محیط اجرای کانتینر آغاز نکرده است.
- در مراحل بعدی چرخهٔ عمر Pod، زمانی که سندباکس Pod به یکی از دلایل زیر از بین رفته باشد:
  - راه‌اندازی دوبارهٔ نود، بدون آنکه Pod بیرون رانده (evict) شود
  - در محیط‌های اجرای کانتینری که برای جداسازی از ماشین مجازی استفاده می‌کنند، راه‌اندازی دوبارهٔ ماشین مجازیِ سندباکس Pod؛ در این حالت باید سندباکس جدیدی ایجاد و شبکهٔ کانتینر از نو پیکربندی شود.

پس از آنکه افزونهٔ محیط اجرا ایجاد سندباکس و پیکربندی شبکهٔ Pod را با موفقیت به پایان رساند، kubelet وضعیت `PodReadyToStartContainers` را روی `True` تنظیم می‌کند. پس از تنظیم این وضعیت روی `True`، kubelet می‌تواند دریافت ایمیج‌های کانتینر و ایجاد کانتینرها را آغاز کند.

برای Podی که کانتینر init دارد، kubelet وضعیت `Initialized` را پس از پایان موفقیت‌آمیز کانتینرهای init روی `True` تنظیم می‌کند (این مرحله پس از ایجاد موفق سندباکس و پیکربندی شبکه به‌وسیلهٔ افزونهٔ محیط اجرا رخ می‌دهد). برای Podی که کانتینر init ندارد، kubelet وضعیت `Initialized` را پیش از آغاز ایجاد سندباکس و پیکربندی شبکه روی `True` تنظیم می‌کند.

## سایر وضعیت‌های Pod {#other-pod-conditions}

وضعیت‌های زیر بخشی از روند عادی چرخهٔ عمر Pod نیستند،
بلکه در واکنش به عملیات یا رویدادهای مشخص تنظیم می‌شوند.

### وضعیت DisruptionTarget {#disruption-target}

وضعیت اختصاصی `DisruptionTarget` به Pod افزوده می‌شود تا نشان دهد
Pod به دلیل یک {{<glossary_tooltip term_id="disruption" text="اختلال">}} در آستانهٔ حذف است.
فیلد `reason` این وضعیت همچنین
یکی از دلایل زیر را برای خاتمهٔ Pod مشخص می‌کند:

`PreemptionByScheduler`
: قرار است Pod به‌وسیلهٔ زمان‌بند {{<glossary_tooltip term_id="preemption" text="پس‌رانده (preempt)">}} شود تا جا برای Pod جدیدی با اولویت بالاتر باز شود. برای اطلاعات بیشتر، [پس‌رانی بر اساس اولویت Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) را ببینید.

`DeletionByTaintManager`
: قرار است Pod به‌وسیلهٔ Taint Manager (که بخشی از کنترل‌کنندهٔ چرخهٔ عمر نود در `kube-controller-manager` است) حذف شود، زیرا taint‌ای از نوع `NoExecute` وجود دارد که Pod آن را تحمل نمی‌کند؛ بیرون‌رانی‌های مبتنی بر {{<glossary_tooltip term_id="taint" text="taint">}} را ببینید.

`EvictionByEvictionAPI`
: این Pod برای {{<glossary_tooltip term_id="api-eviction" text="بیرون‌رانی با استفاده از API کوبرنتیز">}} علامت‌گذاری شده است.

`DeletionByPodGC`
: این Pod به نودی متصل است که دیگر وجود ندارد و قرار است به‌وسیلهٔ [جمع‌آوری زبالهٔ Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) حذف شود.

`TerminationByKubelet`
: این Pod به‌وسیلهٔ kubelet خاتمه یافته است؛ به دلیل {{<glossary_tooltip term_id="node-pressure-eviction" text="بیرون‌رانی ناشی از فشار نود">}}،
  [خاموش‌شدن آرام نود](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
  یا پس‌رانی به نفع [Podهای حیاتی سیستم](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).

در همهٔ سناریوهای اختلال دیگر، مانند بیرون‌رانی به دلیل فراتر رفتن از
[محدودیت‌های کانتینر Pod](/docs/concepts/configuration/manage-resources-containers/)،
وضعیت `DisruptionTarget` به Podها افزوده نمی‌شود، زیرا این اختلال‌ها
احتمالاً از خود Pod ناشی شده‌اند و با تلاش دوباره نیز تکرار خواهند شد.

{{< note >}}
ممکن است اختلال یک Pod قطع شود. control plane ممکن است دوباره تلاش کند تا
اختلال همان Pod را ادامه دهد، اما این کار تضمین‌شده نیست. در نتیجه،
ممکن است وضعیت `DisruptionTarget` به یک Pod افزوده شود، اما آن Pod در عمل
حذف نشود. در چنین شرایطی، پس از مدتی
وضعیت اختلال Pod پاک می‌شود.
{{< /note >}}

جمع‌آوری‌کنندهٔ زبالهٔ Pod (PodGC) افزون بر پاک‌سازی Podها، اگر آن‌ها در فازی غیرپایانی
باشند، آن‌ها را به‌عنوان شکست‌خورده علامت‌گذاری می‌کند (همچنین [جمع‌آوری زبالهٔ Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) را ببینید).

هنگام استفاده از Job (یا CronJob)، ممکن است بخواهید از این وضعیت‌های اختلال Pod در
[سیاست شکست Pod](/docs/concepts/workloads/controllers/job#pod-failure-policy) مربوط به Job خود استفاده کنید.

برای جزئیات بیشتر، [اختلال‌ها](/docs/concepts/workloads/pods/disruptions/) را ببینید.

### وضعیت‌های PodResizePending و PodResizeInProgress {#pod-resize-conditions}

kubelet وضعیت‌های status مربوط به Pod را به‌روزرسانی می‌کند تا حالت یک درخواست تغییر اندازه را نشان دهد:

- نوع `type: PodResizePending`: kubelet نمی‌تواند درخواست را بی‌درنگ اجابت کند. فیلد `message` دلیل آن را توضیح می‌دهد.
  - دلیل `reason: Infeasible`: تغییر اندازهٔ درخواست‌شده روی نود فعلی ممکن نیست (برای نمونه، درخواست منابعی بیش از آنچه نود در اختیار دارد).
  - دلیل `reason: Deferred`: تغییر اندازهٔ درخواست‌شده در حال حاضر ممکن نیست، اما ممکن است بعداً امکان‌پذیر شود (برای نمونه، اگر Pod دیگری حذف شود). kubelet تغییر اندازه را دوباره امتحان خواهد کرد.
- نوع `type: PodResizeInProgress`: kubelet تغییر اندازه را پذیرفته و منابع را تخصیص داده است، اما تغییرات هنوز در حال اعمال هستند. این مرحله معمولاً کوتاه است، اما بسته به نوع منبع و رفتار محیط اجرا ممکن است طولانی‌تر شود. هر خطایی که هنگام اعمال تغییرات رخ دهد در فیلد `message` گزارش می‌شود (همراه با `reason: Error`).

اگر تغییر اندازهٔ درخواست‌شده در حالت _Deferred_ باشد، kubelet به‌طور دوره‌ای تغییر اندازه را دوباره امتحان می‌کند؛ برای نمونه، زمانی که Pod دیگری حذف یا کوچک‌مقیاس شود.

برای جزئیات بیشتر دربارهٔ تغییر اندازهٔ Pod، [تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) را ببینید.

## آمادگی پیشرفتهٔ Pod

برنامهٔ شما می‌تواند بازخورد یا سیگنال‌های بیشتری را به `.status` مربوط به Pod تزریق کند؛
به این قابلیت _آمادگی پیشرفتهٔ Pod_ گفته می‌شود.
برای استفاده از آن، در `spec` مربوط به Pod فیلد `readinessGates` را تنظیم کنید تا فهرستی از
وضعیت‌های اضافی را مشخص کنید که kubelet برای تعیین آمادگی Pod ارزیابی می‌کند.
سپس کنترل‌کننده‌ای را پیاده‌سازی یا نصب می‌کنید که این وضعیت‌های سفارشی را مدیریت کند،
و kubelet از آن به‌عنوان ورودی اضافی برای تصمیم‌گیری دربارهٔ آماده بودن Pod استفاده می‌کند.

دروازه‌های آمادگی بر اساس حالت فعلی فیلدهای `status.condition` مربوط به Pod تعیین می‌شوند.
اگر کوبرنتیز چنین وضعیتی را در فیلد `status.conditions` یک Pod پیدا نکند، مقدار پیش‌فرض آن وضعیت "`False`" در نظر گرفته می‌شود.

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

نام وضعیت‌هایی که به Pod می‌افزایید باید با [قالب کلید برچسب](/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set) کوبرنتیز سازگار باشد.

### وضعیت آمادگی Pod

برای تنظیم این `status.conditions` برای Pod، برنامه‌ها و
{{< glossary_tooltip term_id="operator-pattern" text="اپراتورها">}} باید از
عملیات `PATCH` روی زیرمنبع status مربوط به Pod استفاده کنند. می‌توانید از `kubectl patch`
همراه با `--subresource=status` یا از یک [کتابخانهٔ کلاینت کوبرنتیز](/docs/reference/using-api/client-libraries/) استفاده کنید و
کدی بنویسید که وضعیت‌های سفارشی Pod را برای آمادگی Pod تنظیم کند.

Podی که از وضعیت‌های سفارشی استفاده می‌کند **تنها** زمانی آماده ارزیابی می‌شود که هر دو شرط زیر برقرار باشند:

- همهٔ کانتینرهای Pod آماده باشند.
- همهٔ وضعیت‌هایی که در `readinessGates` مشخص شده‌اند `True` باشند.

هنگامی که کانتینرهای یک Pod در حالت Ready هستند، اما دست‌کم یکی از وضعیت‌های سفارشی وجود ندارد یا `False` است،
kubelet وضعیت `Ready` مربوط به Pod را با `reason: ReadinessGatesNotReady` روی `status: "False"` تنظیم می‌کند.

## {{% heading "whatsnext" %}}

- دربارهٔ [چرخهٔ عمر Pod](/docs/concepts/workloads/pods/pod-lifecycle/) بیاموزید.
- دربارهٔ [اختلال‌ها](/docs/concepts/workloads/pods/disruptions/) بیاموزید.
- دربارهٔ [کاوشگرهای کانتینر](/docs/concepts/workloads/pods/probes/) و تأثیر آن‌ها بر آمادگی Pod بیاموزید.
- بیاموزید چگونه [منابع Pod را درجا تغییر اندازه دهید](/docs/tasks/configure-pod-container/resize-container-resources/).

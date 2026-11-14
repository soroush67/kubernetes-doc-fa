---
title: تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به کانتینرها
content_type: task
weight: 30
min-kubernetes-server-version: 1.33
---


<!-- overview -->

{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}

این صفحه توضیح می‌دهد که چگونه می‌توان درخواست‌ها (requests) و محدودیت‌های (limits) منابع CPU و حافظهٔ تخصیص‌یافته به یک کانتینر را *بدون ایجاد دوبارهٔ Pod* تغییر داد.

در گذشته، برای تغییر نیازمندی‌های منابع یک Pod باید Pod موجود را حذف و Pod جایگزینی ایجاد می‌کردید. این کار اغلب بر عهدهٔ یک [کنترل‌کنندهٔ بار کاری](/docs/concepts/workloads/controllers/) بود. قابلیت تغییر اندازهٔ درجای Pod (In-place Pod Resize) امکان می‌دهد تخصیص CPU و حافظهٔ کانتینرهای یک Pod در حال اجرا را تغییر دهید و در بسیاری از موارد از اختلال در برنامه جلوگیری کنید. فرایند تغییر اندازهٔ منابع در سطح Pod در صفحهٔ [تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به Podها](/docs/tasks/configure-pod-container/resize-pod-resources) شرح داده شده است.

**مفاهیم کلیدی:**

* **منابع مطلوب (Desired Resources):** فیلد `spec.containers[*].resources` هر کانتینر منابع *مطلوب* آن کانتینر را نشان می‌دهد و مقادیر CPU و حافظهٔ آن قابل تغییر هستند.
* **منابع واقعی (Actual Resources):** فیلد `status.containerStatuses[*].resources` منابعی را نشان می‌دهد که *در حال حاضر* برای کانتینر در حال اجرا پیکربندی شده‌اند. برای کانتینرهایی که هنوز شروع نشده‌اند یا راه‌اندازی مجدد شده‌اند، این فیلد منابعی را نشان می‌دهد که در شروع بعدی به آن‌ها تخصیص داده می‌شود.
* **آغاز تغییر اندازه:** برای درخواست تغییر اندازه، مقادیر مطلوب `requests` و `limits` را در مشخصات Pod به‌روزرسانی کنید. این کار معمولاً با `kubectl patch`، `kubectl apply` یا `kubectl edit` و با هدف قرار دادن زیرمنبع (subresource) `resize` در Pod انجام می‌شود. هنگامی که منابع مطلوب با منابع تخصیص‌یافته مطابقت نداشته باشند، Kubelet تلاش می‌کند اندازهٔ کانتینر را تغییر دهد.
* **منابع تخصیص‌یافته (پیشرفته):** فیلد `status.containerStatuses[*].allocatedResources` مقادیر منابعی را که Kubelet تأیید کرده است ردیابی می‌کند و عمدتاً در منطق داخلی زمان‌بندی استفاده می‌شود. برای بیشتر کارهای پایش و اعتبارسنجی، بهتر است بر `status.containerStatuses[*].resources` تمرکز کنید.

اگر روی یک نود، Podهایی با تغییر اندازهٔ در انتظار یا ناتمام وجود داشته باشد (به بخش [وضعیت تغییر اندازهٔ Pod](#pod-resize-status) در ادامه مراجعه کنید)، {{< glossary_tooltip text="زمان‌بند" term_id="kube-scheduler" >}} هنگام تصمیم‌گیری برای زمان‌بندی، *بیشینهٔ* درخواست‌های مطلوب، درخواست‌های تخصیص‌یافته و درخواست‌های واقعی ثبت‌شده در وضعیت کانتینر را در نظر می‌گیرد.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `InPlacePodVerticalScaling` برای control plane و همهٔ نودهای کلاستر شما فعال باشد.

برای فعال‌سازی پیش‌دستی (preemption) خودکار زمان‌بند برای درخواست‌های تغییر اندازهٔ به‌تعویق‌افتاده، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `InPlacePodVerticalScalingSchedulerPreemption` نیز برای control plane فعال باشد.

برای تغییر اندازهٔ پویای حجم‌های (volume) `emptyDir` مبتنی بر حافظه (`medium: Memory`)، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `InPlacePodVerticalScalingMemoryBackedVolumes` نیز برای control plane و نودها فعال باشد و نودهای زیرین نیز باید از cgroup v2 استفاده کنند.

برای استفاده از فلگ `--subresource=resize`، نسخهٔ کلاینت `kubectl` باید دست‌کم v1.32 باشد.

## وضعیت تغییر اندازهٔ Pod

‏Kubelet شرایط (conditions) وضعیت Pod را به‌روزرسانی می‌کند تا وضعیت درخواست تغییر اندازه را نشان دهد:

* `type: PodResizePending`: ‏Kubelet نمی‌تواند درخواست را فوراً بپذیرد. فیلد `message` علت آن را توضیح می‌دهد.
    * `reason: Infeasible`: تغییر اندازهٔ درخواستی روی نود فعلی امکان‌پذیر نیست (برای مثال، درخواست منابعی بیش از ظرفیت نود).
    * `reason: Deferred`: تغییر اندازهٔ درخواستی در حال حاضر ممکن نیست، اما ممکن است بعداً امکان‌پذیر شود (برای مثال، اگر Pod دیگری حذف شود). ‏Kubelet تغییر اندازه را دوباره امتحان می‌کند.
* `type: PodResizeInProgress`: ‏Kubelet تغییر اندازه را پذیرفته و منابع را تخصیص داده است، اما اعمال تغییرات هنوز ادامه دارد. این مرحله معمولاً کوتاه است، اما بسته به نوع منبع و رفتار محیط اجرا ممکن است طولانی‌تر شود. هر خطایی که هنگام اعمال تغییرات رخ دهد، در فیلد `message` (همراه با `reason: Error`) گزارش می‌شود.

### نحوهٔ تلاش مجدد و پیش‌دستی برای تغییر اندازه‌های به‌تعویق‌افتاده

اگر تغییر اندازهٔ درخواستی در وضعیت _Deferred_ باشد، kubelet به‌طور دوره‌ای تغییر اندازه را دوباره امتحان می‌کند؛ برای مثال، زمانی که Pod دیگری حذف یا کوچک‌تر شود.

{{< note >}}
{{< feature-state feature_gate_name="InPlacePodVerticalScalingSchedulerPreemption" >}}

هنگامی که feature gate با نام `InPlacePodVerticalScalingSchedulerPreemption` فعال باشد، `kube-scheduler` بر Podهایی که وضعیت تغییر اندازهٔ آن‌ها `Deferred` است نظارت می‌کند. اگر نودی ظرفیت کافی برای پاسخ به درخواست تغییر اندازهٔ یک Pod با اولویت بالاتر را نداشته باشد، زمان‌بند می‌تواند Podهای با اولویت پایین‌تر را روی آن نود پیش‌دستی (بیرون‌رانی) کند تا ظرفیت CPU یا حافظهٔ لازم آزاد شود. برای جزئیات بیشتر، به [پیش‌دستی برای تغییر اندازهٔ درجای Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption-for-in-place-pod-resize) مراجعه کنید.
{{< /note >}}

اگر چند تغییر اندازهٔ به‌تعویق‌افتاده وجود داشته باشد، تلاش مجدد برای آن‌ها به ترتیب اولویت زیر انجام می‌شود:

* درخواست تغییر اندازهٔ Podهایی که اولویت (Priority) بالاتری دارند (بر اساس PriorityClass)، زودتر دوباره امتحان می‌شود.
* اگر دو Pod اولویت یکسانی داشته باشند، تغییر اندازهٔ Podهای guaranteed پیش از Podهای burstable دوباره امتحان می‌شود.
* اگر همهٔ موارد دیگر یکسان باشند، Podهایی که مدت طولانی‌تری در وضعیت Deferred بوده‌اند در اولویت قرار می‌گیرند.

در انتظار ماندن یک تغییر اندازهٔ با اولویت بالاتر، مانع از تلاش برای سایر تغییر اندازه‌های در انتظار نمی‌شود؛ حتی اگر تغییر اندازهٔ با اولویت بالاتر دوباره به تعویق بیفتد، همهٔ تغییر اندازه‌های در انتظار باقی‌مانده همچنان دوباره امتحان می‌شوند.


### بهره‌گیری از فیلدهای `observedGeneration`

{{< feature-state feature_gate_name="PodObservedGenerationTracking" >}}

* فیلد سطح بالای `status.observedGeneration` مقدار `metadata.generation` مربوط به آخرین مشخصات Pod را که kubelet دریافت آن را تأیید کرده است نشان می‌دهد. با این فیلد می‌توانید آخرین درخواست تغییر اندازه‌ای را که kubelet پردازش کرده است مشخص کنید.
* در شرط `PodResizeInProgress`، فیلد `conditions[].observedGeneration` مقدار `metadata.generation` مربوط به podSpec را در زمان آغاز تغییر اندازهٔ در حال انجام نشان می‌دهد.
* در شرط `PodResizePending`، فیلد `conditions[].observedGeneration` مقدار `metadata.generation` مربوط به podSpec را در آخرین باری که برای تخصیص تغییر اندازهٔ در انتظار تلاش شده است نشان می‌دهد.

## سیاست‌های تغییر اندازهٔ کانتینر

با تنظیم `resizePolicy` در مشخصات کانتینر می‌توانید تعیین کنید که آیا کانتینر هنگام تغییر اندازه باید راه‌اندازی مجدد شود یا نه. با این کار می‌توانید کنترل دقیقی بر اساس نوع منبع (CPU یا حافظه) داشته باشید.

```yaml
    resizePolicy:
    - resourceName: cpu
      restartPolicy: NotRequired
    - resourceName: memory
      restartPolicy: RestartContainer
```

* `NotRequired`: (پیش‌فرض) تغییر منبع بدون راه‌اندازی مجدد، روی کانتینر در حال اجرا اعمال می‌شود.
* `RestartContainer`: کانتینر برای اعمال مقادیر جدید منبع راه‌اندازی مجدد می‌شود. این گزینه اغلب برای تغییرات حافظه لازم است، زیرا بسیاری از برنامه‌ها و محیط‌های اجرا نمی‌توانند تخصیص حافظهٔ خود را به‌صورت پویا تنظیم کنند.

اگر `resizePolicy[*].restartPolicy` برای منبعی مشخص نشده باشد، مقدار پیش‌فرض آن `NotRequired` است.

{{< note >}}
اگر `restartPolicy` کلی یک Pod برابر `Never` باشد، `resizePolicy` همهٔ کانتینرها باید برای همهٔ منابع `NotRequired` باشد. در چنین Podهایی نمی‌توانید سیاست تغییر اندازه‌ای پیکربندی کنید که به راه‌اندازی مجدد نیاز داشته باشد.
{{< /note >}}

**سناریوی نمونه:**

کانتینری را در نظر بگیرید که برای CPU با `restartPolicy: NotRequired` و برای حافظه با `restartPolicy: RestartContainer` پیکربندی شده است.
* اگر فقط منابع CPU تغییر کند، اندازهٔ کانتینر به‌صورت درجا تغییر می‌کند.
* اگر فقط منابع حافظه تغییر کند، کانتینر راه‌اندازی مجدد می‌شود.
* اگر منابع CPU و حافظه *هر دو* هم‌زمان تغییر کنند، کانتینر (به دلیل سیاست حافظه) راه‌اندازی مجدد می‌شود.

## تغییر اندازهٔ حجم‌های emptyDir مبتنی بر حافظه

{{< feature-state feature_gate_name="InPlacePodVerticalScalingMemoryBackedVolumes" >}}

هنگامی که feature gate با نام `InPlacePodVerticalScalingMemoryBackedVolumes` فعال باشد، زیرمنبع `/resize` در Pod از به‌روزرسانی `sizeLimit` حجم‌های `emptyDir` مبتنی بر حافظه (`medium: Memory`) در Podهای در حال اجرا، بدون راه‌اندازی مجدد کانتینرها یا ایجاد دوبارهٔ Pod، پشتیبانی می‌کند.

هنگامی که `sizeLimit` یک حجم از طریق زیرمنبع `/resize` به‌روزرسانی شود، Kubelet اتصال (mount) زیرین `tmpfs` را بدون اختلال در کانتینر و به‌صورت پویا به‌روزرسانی می‌کند و در عین حال با اطمینان از بروز خطاهای کمبود حافظه یا فعال‌شدن نادرست بیرون‌رانی (eviction) جلوگیری می‌کند.

برای تغییر اندازهٔ یک حجم `emptyDir` مبتنی بر حافظه، `spec.volumes[].emptyDir.sizeLimit` را با هدف قرار دادن زیرمنبع `resize` در Pod به‌روزرسانی کنید:

```shell
kubectl patch pod <pod-name> --subresource resize --patch \
  '{"spec":{"volumes":[{"name":"cache-volume", "emptyDir":{"sizeLimit":"200Mi"}}]}}'
```

می‌توانید پیشرفت تغییر اندازه را با استفاده از شرایط وضعیت Pod (`PodResizePending` و `PodResizeInProgress`) پایش کنید. پس از پایان کار، می‌توانید ظرفیت واقعی حجم را درون کانتینر در حال اجرا بررسی کنید (برای مثال، با استفاده از `kubectl exec` برای اجرای `df -h`).

## محدودیت‌ها

در کوبرنتیز {{< skew currentVersion >}}، تغییر اندازهٔ درجای منابع Pod محدودیت‌های زیر را دارد:

* **انواع منابع:** فقط اندازهٔ منابع CPU و حافظه قابل تغییر است.
* **کاهش حافظه:** اگر سیاست راه‌اندازی مجدد برای تغییر اندازهٔ حافظه `NotRequired` باشد (یا مشخص نشده باشد)، kubelet هنگام کاهش محدودیت‌های حافظه، تمام تلاش خود را برای جلوگیری از oom-kill انجام می‌دهد، اما هیچ تضمینی نمی‌دهد. پیش از کاهش محدودیت حافظهٔ کانتینر، اگر مصرف حافظه از محدودیت درخواستی بیشتر باشد، تغییر اندازه نادیده گرفته می‌شود و وضعیت در حالت «In Progress» باقی می‌ماند. این رویکرد «بهترین تلاش» به شمار می‌رود، زیرا همچنان در معرض شرایط رقابتی (race condition) است و ممکن است مصرف حافظه درست پس از انجام بررسی به‌شدت افزایش یابد.
* **کلاس QoS:** [کلاس کیفیت خدمات (QoS)](/docs/concepts/workloads/pods/pod-qos/) اولیهٔ Pod (Guaranteed، Burstable یا BestEffort) هنگام ایجاد تعیین می‌شود و با تغییر اندازه **قابل تغییر نیست**. مقادیر جدید منابع همچنان باید از قواعد کلاس QoS اولیه پیروی کنند:
    * *Guaranteed*: پس از تغییر اندازه، درخواست‌ها باید همچنان برای CPU و حافظه هر دو با محدودیت‌ها برابر باشند.
    * *Burstable*: درخواست‌ها و محدودیت‌ها نمی‌توانند به‌طور هم‌زمان برای CPU و حافظه *هر دو* برابر شوند (زیرا در این صورت کلاس به Guaranteed تغییر می‌کند).
    * *BestEffort*: نمی‌توان نیازمندی‌های منابع (`requests` یا `limits`) را اضافه کرد (زیرا در این صورت کلاس به Burstable یا Guaranteed تغییر می‌کند).
* **انواع کانتینر:** اندازهٔ {{< glossary_tooltip text="کانتینرهای init" term_id="init-container" >}} غیرقابل‌راه‌اندازی‌مجدد و {{< glossary_tooltip text="کانتینرهای موقت" term_id="ephemeral-container" >}} قابل تغییر نیست. اندازهٔ [کانتینرهای sidecar](/docs/concepts/workloads/pods/sidecar-containers/) قابل تغییر است.
* **حذف منابع:** درخواست‌ها و محدودیت‌های منابع پس از تنظیم، به‌طور کامل قابل حذف نیستند و فقط می‌توان آن‌ها را به مقادیر دیگری تغییر داد.
* **سیستم‌عامل:** ‏Podهای Windows از تغییر اندازهٔ درجا پشتیبانی نمی‌کنند.
* **سیاست‌های نود:** اندازهٔ Podهایی که با [سیاست‌های static مدیر CPU یا حافظه](/docs/tasks/administer-cluster/cpu-management-policies/) مدیریت می‌شوند، به‌صورت درجا قابل تغییر نیست.
* **حافظهٔ Swap:** ‏Podهایی که از [حافظهٔ swap](/docs/concepts/architecture/nodes/#swap-memory) استفاده می‌کنند، نمی‌توانند درخواست‌های حافظه را تغییر دهند، مگر اینکه `resizePolicy` حافظه برابر `RestartContainer` باشد.
* **تغییر اندازهٔ حجم‌های مبتنی بر حافظه:** تغییر اندازهٔ درجای حجم‌های `emptyDir` مبتنی بر حافظه (`medium: Memory`) به نودهایی با cgroup v2 نیاز دارد. در نودهای cgroup v1، درخواست‌های تغییر اندازهٔ درجای حجم به‌عنوان غیرممکن (infeasible) رد می‌شوند. اندازهٔ حجم‌های `emptyDir` مبتنی بر دیسک و حجم‌های پایدار (persistent volume) را نمی‌توان از طریق زیرمنبع `/resize` در Pod تغییر داد.

ممکن است این محدودیت‌ها در نسخه‌های آیندهٔ کوبرنتیز کاهش یابند.

## ایجاد یک فضای نام

یک فضای نام (namespace) ایجاد کنید تا منابعی که در این تمرین ایجاد می‌کنید از بقیهٔ کلاستر شما جدا باشند.

```shell
kubectl create namespace qos-example
```

## مثال ۱: تغییر اندازهٔ CPU بدون راه‌اندازی مجدد

ابتدا یک Pod ایجاد کنید که برای تغییر اندازهٔ درجای CPU و تغییر اندازهٔ حافظه با نیاز به راه‌اندازی مجدد طراحی شده است.

{{% code_sample file="pods/resource/pod-resize.yaml" %}}

‏Pod را ایجاد کنید:

```shell
kubectl create -f pod-resize.yaml -n qos-example
```

این Pod در کلاس QoS نوع Guaranteed شروع به کار می‌کند. وضعیت اولیهٔ آن را بررسی کنید:

```shell
# Wait a moment for the pod to be running
kubectl get pod resize-demo --output=yaml -n qos-example
```

فیلدهای `spec.containers[0].resources` و `status.containerStatuses[0].resources` را بررسی کنید. مقادیر آن‌ها باید با مانیفست (700m CPU و 200Mi حافظه) مطابقت داشته باشد. به مقدار `status.containerStatuses[0].restartCount` نیز توجه کنید (باید 0 باشد).

اکنون درخواست و محدودیت CPU را به `800m` افزایش دهید. برای این کار از `kubectl patch` همراه با آرگومان خط فرمان `--subresource resize` استفاده می‌کنید.

```shell
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"800m"}, "limits":{"cpu":"800m"}}}]}}'

# Alternative methods:
# kubectl -n qos-example edit pod resize-demo --subresource resize
# kubectl -n qos-example apply -f <updated-manifest> --subresource resize --server-side
```

{{< note >}}
آرگومان خط فرمان `--subresource resize` به کلاینت `kubectl` با نسخهٔ v1.32.0 یا بالاتر نیاز دارد. نسخه‌های قدیمی‌تر خطای `invalid subresource` را گزارش می‌کنند.
{{< /note >}}

پس از اعمال patch، وضعیت Pod را دوباره بررسی کنید:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

باید موارد زیر را ببینید:
* فیلد `spec.containers[0].resources` اکنون `cpu: 800m` را نشان می‌دهد.
* فیلد `status.containerStatuses[0].resources` نیز `cpu: 800m` را نشان می‌دهد؛ این یعنی تغییر اندازه روی نود با موفقیت انجام شده است.
* مقدار `status.containerStatuses[0].restartCount` همچنان `0` است، زیرا `resizePolicy` مربوط به CPU برابر `NotRequired` بود.

## مثال ۲: تغییر اندازهٔ حافظه با راه‌اندازی مجدد

اکنون حافظهٔ *همان* Pod را با افزایش آن به `300Mi` تغییر دهید. از آنجا که `resizePolicy` حافظه برابر `RestartContainer` است، انتظار می‌رود کانتینر راه‌اندازی مجدد شود.

```shell
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"memory":"300Mi"}, "limits":{"memory":"300Mi"}}}]}}'
```

کمی پس از اعمال patch، وضعیت Pod را بررسی کنید:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

اکنون باید موارد زیر را مشاهده کنید:
* فیلد `spec.containers[0].resources` مقدار `memory: 300Mi` را نشان می‌دهد.
* فیلد `status.containerStatuses[0].resources` نیز `memory: 300Mi` را نشان می‌دهد.
* مقدار `status.containerStatuses[0].restartCount` به `1` (یا بیشتر، اگر پیش‌تر راه‌اندازی مجدد رخ داده باشد) افزایش یافته است؛ این یعنی کانتینر برای اعمال تغییر حافظه راه‌اندازی مجدد شده است.

## عیب‌یابی: درخواست تغییر اندازهٔ غیرممکن

در ادامه، مقدار نامعقولی از CPU را درخواست کنید، مثلاً ۱۰۰۰ هستهٔ کامل (که به‌جای `"1000m"` برای میلی‌هسته، به‌صورت `"1000"` نوشته می‌شود)؛ این مقدار به احتمال زیاد از ظرفیت نود بیشتر است.

```shell
# Attempt to patch with an excessively large CPU request
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"1000"}, "limits":{"cpu":"1000"}}}]}}'
```

جزئیات Pod را دریافت کنید:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

تغییراتی را خواهید دید که نشان‌دهندهٔ مشکل هستند:

* فیلد `spec.containers[0].resources` وضعیت *مطلوب* (`cpu: "1000"`) را نشان می‌دهد.
* شرطی با `type: PodResizePending` و `reason: Infeasible` به Pod اضافه شده است.
* فیلد `message` این شرط علت را توضیح می‌دهد (`Node didn't have enough capacity: cpu, requested: 800000, capacity: ...`).
* نکتهٔ مهم این است که `status.containerStatuses[0].resources` *همچنان مقادیر قبلی* (`cpu: 800m` و `memory: 300Mi`) را نشان می‌دهد، زیرا Kubelet تغییر اندازهٔ غیرممکن را اعمال نکرده است.
* مقدار `restartCount` به دلیل این تلاش ناموفق تغییر نکرده است.

برای رفع این مشکل، باید Pod را دوباره با مقادیر منابع امکان‌پذیر patch کنید.

## پاک‌سازی

فضای نام خود را حذف کنید. با این کار همهٔ Podهایی که برای این تمرین ایجاد کرده‌اید حذف می‌شوند:

```shell
kubectl delete namespace qos-example
```

## {{% heading "whatsnext" %}}


### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی قیدهای کمینه و بیشینهٔ حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی قیدهای کمینه و بیشینهٔ CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

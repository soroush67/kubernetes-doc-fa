---
title: تغییر اندازهٔ منابع CPU و حافظهٔ اختصاص‌یافته به Podها
content_type: task
weight: 30
min-kubernetes-server-version: 1.35
---

<!-- overview -->

{{< feature-state feature_gate_name="InPlacePodLevelResourcesVerticalScaling" >}}

این صفحه توضیح می‌دهد که چگونه می‌توان منابع CPU و حافظهٔ تنظیم‌شده در سطح Pod را بدون ایجاد دوبارهٔ Pod تغییر داد.

قابلیت تغییر اندازهٔ درجای Pod (In-place Pod Resize) امکان تغییر تخصیص منابع یک Pod در حال اجرا را فراهم می‌کند و از اختلال در کار برنامه جلوگیری می‌کند. فرایند تغییر اندازهٔ منابع هر کانتینر به‌تنهایی در صفحهٔ [تغییر اندازهٔ منابع CPU و حافظهٔ اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources) شرح داده شده است.

تمرکز این صفحه بر تغییر اندازهٔ درجای منابع در سطح Pod است. منابع سطح Pod در `spec.resources` تعریف می‌شوند و حد بالای مجموع منابعی را تعیین می‌کنند که همهٔ کانتینرهای Pod مصرف می‌کنند. با قابلیت تغییر اندازهٔ درجای منابع سطح Pod می‌توانید این تخصیص‌های کلی CPU و حافظه را برای یک Pod در حال اجرا مستقیماً تغییر دهید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

[feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/) زیر باید برای control plane و برای همهٔ نودهای کلاستر فعال باشند:

* [`InPlacePodLevelResourcesVerticalScaling`](/docs/reference/command-line-tools-reference/feature-gates/#InPlacePodLevelResourcesVerticalScaling)
* [`PodLevelResources`](/docs/reference/command-line-tools-reference/feature-gates/#PodLevelResources)
* [`InPlacePodVerticalScaling`](/docs/reference/command-line-tools-reference/feature-gates/#InPlacePodVerticalScaling)
* [`NodeDeclaredFeatures`](/docs/reference/command-line-tools-reference/feature-gates/#NodeDeclaredFeatures)

برای استفاده از فلگ `--subresource=resize`، نسخهٔ کلاینت kubectl باید دست‌کم v1.32 باشد.

## وضعیت تغییر اندازهٔ Pod و منطق تلاش دوباره

سازوکاری که `kubelet` برای پیگیری تغییرات منابع و تلاش دوباره برای اعمال آن‌ها به کار می‌برد، میان درخواست‌های تغییر اندازه در سطح کانتینر و در سطح Pod مشترک است.

وضعیت‌ها، دلیل‌ها و اولویت‌های تلاش دوباره همان مواردی هستند که برای تغییر اندازهٔ کانتینر تعریف شده‌اند:

* شرایط وضعیت (Status Conditions): ‏`kubelet` با استفاده از PodResizePending (همراه با دلیل‌هایی مانند Infeasible یا Deferred) و PodResizeInProgress وضعیت درخواست را اعلام می‌کند.

* اولویت تلاش دوباره: تلاش دوباره برای تغییر اندازه‌های به تعویق افتاده (Deferred) ابتدا بر اساس PriorityClass، سپس بر اساس کلاس QoS (‏Guaranteed بر Burstable مقدم است) و در پایان بر اساس مدت‌زمانی که به تعویق افتاده‌اند انجام می‌شود.

* پیگیری: با فیلدهای `observedGeneration` می‌توانید مشخص کنید که وضعیت آخرین درخواست تغییر اندازهٔ پردازش‌شده به کدام مشخصهٔ Pod ‏(metadata.generation) مربوط است.

برای شرح کامل این شرایط و منطق تلاش دوباره، به بخش [وضعیت تغییر اندازهٔ Pod](/docs/tasks/configure-pod-container/resize-container-resources/#pod-resize-status) در مستندات تغییر اندازهٔ کانتینر مراجعه کنید.

## سیاست تغییر اندازهٔ کانتینر و تغییر اندازه در سطح Pod

تغییر اندازهٔ منابع در سطح Pod از سیاست راه‌اندازی مجدد جداگانه‌ای پشتیبانی نمی‌کند و به آن نیازی هم ندارد.

* نبود سیاست در سطح Pod: تغییرات منابع کلی Pod ‏(spec.resources) همیشه به‌صورت درجا و بدون راه‌اندازی مجدد اعمال می‌شوند؛ زیرا منابع سطح Pod نقش یک محدودیت کلی بر cgroup مربوط به Pod را دارند و محیط اجرای برنامه در داخل کانتینرها را مستقیماً مدیریت نمی‌کنند.

* [سیاست کانتینر](/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-policies) همچنان تعیین‌کننده است: فیلد resizePolicy همچنان باید در سطح کانتینر (spec.containers[*].resizePolicy) پیکربندی شود. این سیاست تعیین می‌کند که آیا هر کانتینر هنگام تغییر درخواست‌ها (requests) یا حدهای (limits) منابعش دوباره راه‌اندازی شود یا نه؛ فرقی نمی‌کند این تغییر از یک تغییر اندازهٔ مستقیم در سطح کانتینر ناشی شده باشد یا از به‌روزرسانی محدودهٔ کلی منابع در سطح Pod.

## محدودیت‌ها

در کوبرنتیز {{< skew currentVersion >}}، تغییر اندازهٔ درجای منابع سطح Pod مشمول همهٔ محدودیت‌هایی است که برای تغییر اندازهٔ منابع در سطح کانتینر شرح داده شده‌اند. این محدودیت‌ها را می‌توانید در این صفحه ببینید: [تغییر اندازهٔ منابع CPU و حافظهٔ اختصاص‌یافته به کانتینرها: محدودیت‌ها](/docs/tasks/configure-pod-container/resize-container-resources/#limitations).

افزون بر این، محدودیت زیر مخصوص تغییر اندازهٔ منابع در سطح Pod است:
* اعتبارسنجی درخواست‌های کانتینر: تغییر اندازه تنها در صورتی مجاز است که درخواست‌های منابع سطح Pod پس از تغییر (spec.resources.requests) بزرگ‌تر یا مساوی مجموع درخواست‌های متناظر همهٔ کانتینرهای داخل Pod باشند. به این ترتیب، حداقل منابع تضمین‌شده برای Pod حفظ می‌شود.

* اعتبارسنجی حدهای کانتینر: تغییر اندازه در صورتی مجاز است که حد هر کانتینر کوچک‌تر یا مساوی حدهای منابع سطح Pod ‏(spec.resources.limits) باشد. حد سطح Pod مرزی است که هیچ کانتینری به‌تنهایی نمی‌تواند از آن فراتر رود، اما مجموع حدهای کانتینرها می‌تواند از حد سطح Pod بیشتر باشد؛ به این ترتیب کانتینرهای داخل Pod می‌توانند منابع را به‌صورت اشتراکی استفاده کنند.

## مثال: تغییر اندازهٔ منابع سطح Pod

ابتدا یک Pod بسازید که برای تغییر اندازهٔ درجای CPU و تغییر اندازهٔ حافظه همراه با راه‌اندازی مجدد طراحی شده است.

{{% code_sample file="pods/resource/pod-level-resize.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl create -f pod-level-resize.yaml
```

از آنجا که درخواست‌های سطح Pod با حدها برابرند، این Pod در کلاس QoS از نوع Guaranteed آغاز به کار می‌کند. وضعیت اولیهٔ آن را بررسی کنید:

```shell
# Wait a moment for the pod to be running
kubectl get pod pod-level-resize-demo --output=yaml
```

به `spec.resources` (‏200m CPU و 200Mi حافظه) توجه کنید. همچنین مقدار `status.containerStatuses[0].restartCount` (که باید 0 باشد) و `status.containerStatuses[1].restartCount` (که باید 0 باشد) را بررسی کنید.

اکنون درخواست و حد CPU در سطح Pod را به `300m` افزایش دهید. برای این کار از `kubectl patch` همراه با آرگومان خط فرمان `--subresource resize` استفاده کنید.

```shell
kubectl patch pod pod-level-resize-demo --subresource resize --patch \
  '{"spec":{"resources":{"requests":{"cpu":"300m"}, "limits":{"cpu":"300m"}}}}'

# Alternative methods:
# kubectl edit pod pod-level-resize-demo --subresource resize
# kubectl apply -f <updated-manifest> --subresource resize --server-side
```

{{< note >}}
آرگومان خط فرمان `--subresource resize` به کلاینت `kubectl` با نسخهٔ v1.32.0 یا بالاتر نیاز دارد. نسخه‌های قدیمی‌تر خطای `invalid subresource` را گزارش می‌کنند.
{{< /note >}}

پس از اعمال patch، وضعیت Pod را دوباره بررسی کنید:

```shell
kubectl get pod pod-level-resize-demo --output=yaml
```

باید موارد زیر را ببینید:
* اکنون `spec.resources.requests` و `spec.resources.limits` مقدار `cpu: 300m` را نشان می‌دهند.
* مقدار `status.containerStatuses[0].restartCount` همچنان `0` باقی می‌ماند، زیرا `resizePolicy` مربوط به CPU برابر `NotRequired` بود.
* مقدار `status.containerStatuses[1].restartCount` به `1` افزایش یافته است؛ این نشان می‌دهد که کانتینر برای اعمال تغییر CPU دوباره راه‌اندازی شده است. با اینکه تغییر اندازه در سطح Pod اعمال شد، کانتینر 1 به دلیل رابطهٔ پیچیدهٔ میان حدهای سطح Pod و سیاست‌های سطح کانتینر دوباره راه‌اندازی شد. از آنجا که کانتینر 1 حد CPU صریحی تعیین نکرده بود، پیکربندی زیربنایی منابع آن (برای مثال cgroupها) به‌طور ضمنی حد کلی CPU در Pod را به‌عنوان مرز مؤثر حداکثر مصرف خود پذیرفته بود. وقتی حد CPU سطح Pod از 200m به 300m تغییر داده شد، حد ضمنی اعمال‌شده بر کانتینر 1 نیز در نتیجه تغییر کرد. چون resizePolicy کانتینر 1 برای CPU به‌طور صریح روی RestartContainer تنظیم شده بود، `kubelet` ناگزیر بود کانتینر را دوباره راه‌اندازی کند تا این تغییر به‌درستی در سازوکار زیربنایی اعمال منابع اعمال شود. این موضوع تأیید می‌کند که تغییر حدهای سطح Pod می‌تواند سیاست‌های راه‌اندازی مجدد کانتینر را فعال کند، حتی وقتی حدهای کانتینر مستقیماً تعریف نشده باشند.

## پاک‌سازی

Pod را حذف کنید:

```shell
kubectl delete pod pod-level-resize-demo
```

## {{% heading "whatsnext" %}}


### برای توسعه‌دهندگان برنامه

* [اختصاص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [اختصاص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [اختصاص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

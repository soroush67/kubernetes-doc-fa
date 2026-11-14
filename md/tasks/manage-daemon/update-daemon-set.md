---
reviewers:
- janetkuo
title: انجام به‌روزرسانی غلتان (Rolling Update) روی یک DaemonSet
content_type: task
weight: 10
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان یک به‌روزرسانی غلتان را روی یک DaemonSet انجام داد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## راهبرد به‌روزرسانی DaemonSet

برای DaemonSet دو نوع راهبرد به‌روزرسانی وجود دارد:

* `OnDelete`: در راهبرد به‌روزرسانی `OnDelete`، پس از آنکه الگوی (template) یک DaemonSet را به‌روزرسانی کردید،
  پادهای جدید DaemonSet *فقط* زمانی ایجاد می‌شوند که پادهای قدیمی DaemonSet را به‌صورت دستی حذف کنید.
  این همان رفتار DaemonSet در کوبرنتیز نسخهٔ 1.5 یا نسخه‌های پیش از آن است.
* `RollingUpdate`: این راهبرد، راهبرد پیش‌فرض به‌روزرسانی است.  
  در راهبرد به‌روزرسانی `RollingUpdate`، پس از آنکه الگوی یک DaemonSet را به‌روزرسانی کردید،
  پادهای قدیمی DaemonSet به‌صورت خودکار و کنترل‌شده خاتمه می‌یابند و پادهای جدید DaemonSet ایجاد می‌شوند.
  در طول کل فرایند به‌روزرسانی، روی هر نود حداکثر یک پاد از DaemonSet در حال اجرا خواهد بود.

## انجام به‌روزرسانی غلتان

برای فعال‌کردن قابلیت به‌روزرسانی غلتان یک DaemonSet، باید مقدار
`.spec.updateStrategy.type` آن را برابر `RollingUpdate` قرار دهید.

همچنین ممکن است بخواهید مقادیر
[`.spec.updateStrategy.rollingUpdate.maxUnavailable`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(پیش‌فرض: 1)،
[`.spec.minReadySeconds`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(پیش‌فرض: 0) و
[`.spec.updateStrategy.rollingUpdate.maxSurge`](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/#DaemonSetSpec)
(پیش‌فرض: 0) را نیز تنظیم کنید.

### ایجاد یک DaemonSet با راهبرد به‌روزرسانی `RollingUpdate`

این فایل YAML یک DaemonSet را با راهبرد به‌روزرسانی 'RollingUpdate' تعریف می‌کند:

{{% code_sample file="controllers/fluentd-daemonset.yaml" %}}

پس از بررسی راهبرد به‌روزرسانی در مانیفست DaemonSet، آن را ایجاد کنید:

```shell
kubectl create -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

اگر قصد دارید DaemonSet را با `kubectl apply` به‌روزرسانی کنید، می‌توانید به‌جای دستور بالا
از `kubectl apply` برای ایجاد همان DaemonSet استفاده کنید.

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml
```

### بررسی راهبرد به‌روزرسانی `RollingUpdate` در DaemonSet

راهبرد به‌روزرسانی DaemonSet خود را بررسی کنید و مطمئن شوید که روی
`RollingUpdate` تنظیم شده است:

```shell
kubectl get ds/fluentd-elasticsearch -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}' -n kube-system
```

اگر هنوز DaemonSet را در سیستم ایجاد نکرده‌اید، به‌جای آن مانیفست DaemonSet خود را
با دستور زیر بررسی کنید:

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset.yaml --dry-run=client -o go-template='{{.spec.updateStrategy.type}}{{"\n"}}'
```

خروجی هر دو دستور باید به این صورت باشد:

```
RollingUpdate
```

اگر خروجی `RollingUpdate` نیست، برگردید و آبجکت یا مانیفست DaemonSet را
متناسب با آن اصلاح کنید.


### به‌روزرسانی الگوی DaemonSet

هر تغییری در `.spec.template` یک DaemonSet از نوع `RollingUpdate` باعث آغاز یک به‌روزرسانی
غلتان می‌شود. بیایید DaemonSet را با اعمال یک فایل YAML جدید به‌روزرسانی کنیم. این کار را می‌توان با چند دستور مختلف `kubectl` انجام داد.

{{% code_sample file="controllers/fluentd-daemonset-update.yaml" %}}

#### دستورهای اعلانی

اگر DaemonSetها را با استفاده از
[فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/declarative-config/)
به‌روزرسانی می‌کنید، از `kubectl apply` استفاده کنید:

```shell
kubectl apply -f https://k8s.io/examples/controllers/fluentd-daemonset-update.yaml
```

#### دستورهای دستوری (Imperative)

اگر DaemonSetها را با استفاده از
[دستورهای دستوری](/docs/tasks/manage-kubernetes-objects/imperative-command/)
به‌روزرسانی می‌کنید، از `kubectl edit` استفاده کنید:

```shell
kubectl edit ds/fluentd-elasticsearch -n kube-system
```

##### به‌روزرسانی فقط ایمیج کانتینر

اگر فقط لازم است ایمیج کانتینر را در الگوی DaemonSet، یعنی
`.spec.template.spec.containers[*].image`، به‌روزرسانی کنید، از `kubectl set image` استفاده کنید:

```shell
kubectl set image ds/fluentd-elasticsearch fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.6.0 -n kube-system
```

### پایش وضعیت به‌روزرسانی غلتان

در پایان، وضعیت عرضهٔ (rollout) آخرین به‌روزرسانی غلتان DaemonSet را پایش کنید:

```shell
kubectl rollout status ds/fluentd-elasticsearch -n kube-system
```

پس از کامل‌شدن عرضه، خروجی مشابه زیر خواهد بود:

```shell
daemonset "fluentd-elasticsearch" successfully rolled out
```

## عیب‌یابی

### به‌روزرسانی غلتان DaemonSet متوقف شده است

گاهی ممکن است به‌روزرسانی غلتان یک DaemonSet متوقف شود. برخی از علت‌های احتمالی
در ادامه آمده‌اند:

#### منابع برخی نودها تمام شده است

عرضه متوقف شده است، زیرا پادهای جدید DaemonSet دست‌کم روی یک نود قابل زمان‌بندی نیستند.
این وضعیت زمانی رخ می‌دهد که
[منابع نود رو به اتمام باشد](/docs/concepts/scheduling-eviction/node-pressure-eviction/).

در این صورت، نودهایی را که پادهای DaemonSet روی آن‌ها زمان‌بندی نشده‌اند پیدا کنید؛
برای این کار خروجی `kubectl get nodes` را با خروجی دستور زیر مقایسه کنید:

```shell
kubectl get pods -l name=fluentd-elasticsearch -o wide -n kube-system
```

پس از یافتن آن نودها، برخی از پادهای غیر DaemonSet را از نود حذف کنید تا
برای پادهای جدید DaemonSet جا باز شود.

{{< note >}}
اگر پادهای حذف‌شده تحت کنترل هیچ کنترل‌کننده‌ای نباشند یا پادها تکثیر (replicate) نشده باشند،
این کار باعث اختلال در سرویس می‌شود. همچنین این کار
[PodDisruptionBudget](/docs/tasks/run-application/configure-pdb/) را نیز رعایت نمی‌کند.
{{< /note >}}

#### عرضهٔ معیوب

اگر آخرین به‌روزرسانی الگوی DaemonSet معیوب باشد، برای مثال کانتینر مدام از کار بیفتد
و دوباره راه‌اندازی شود (crash looping) یا ایمیج کانتینر وجود نداشته باشد (که اغلب ناشی از غلط تایپی است)،
عرضهٔ DaemonSet پیش نخواهد رفت.

برای رفع این مشکل، الگوی DaemonSet را دوباره به‌روزرسانی کنید. عرضه‌های ناسالم قبلی
مانع عرضهٔ جدید نخواهند شد.

#### ناهمخوانی ساعت

اگر `.spec.minReadySeconds` در DaemonSet مشخص شده باشد، ناهمخوانی ساعت (clock skew) میان
master و نودها باعث می‌شود DaemonSet نتواند پیشرفت درست عرضه را تشخیص دهد.

## پاک‌سازی

یک DaemonSet را از یک فضای نام (namespace) حذف کنید:

```shell
kubectl delete ds fluentd-elasticsearch -n kube-system
```

## {{% heading "whatsnext" %}}

* [انجام بازگردانی (rollback) روی یک DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/) را ببینید.
* [ایجاد یک DaemonSet برای در اختیار گرفتن پادهای موجود DaemonSet](/docs/concepts/workloads/controllers/daemonset/) را ببینید.

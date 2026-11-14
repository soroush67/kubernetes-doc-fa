---
title: تخصیص منابع حافظه به کانتینرها و Podها
content_type: task
weight: 10
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک *درخواست* (request) حافظه و یک *حد* (limit) حافظه را به یک کانتینر اختصاص دهید. کانتینر به‌طور تضمین‌شده به اندازهٔ حافظه‌ای که درخواست کرده است حافظه در اختیار دارد، اما اجازه ندارد بیش از حد خود حافظه مصرف کند.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

هر نود در کلاستر شما باید دست‌کم 300 MiB حافظه داشته باشد.

برای انجام برخی از گام‌های این صفحه باید سرویس [metrics-server](https://github.com/kubernetes-sigs/metrics-server) را در کلاستر خود اجرا کنید. اگر metrics-server در کلاستر شما در حال اجراست، می‌توانید از این گام‌ها صرف‌نظر کنید.

اگر از Minikube استفاده می‌کنید، برای فعال‌سازی metrics-server دستور زیر را اجرا کنید:

```shell
minikube addons enable metrics-server
```

برای بررسی اینکه آیا metrics-server یا ارائه‌دهندهٔ دیگری از API معیارهای منابع (`metrics.k8s.io`) در حال اجراست، دستور زیر را اجرا کنید:

```shell
kubectl get apiservices
```

اگر API معیارهای منابع در دسترس باشد، خروجی شامل ارجاعی به `metrics.k8s.io` خواهد بود.

```shell
NAME
v1beta1.metrics.k8s.io
```



<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام (namespace) ایجاد کنید تا منابعی که در این تمرین ایجاد می‌کنید از بقیهٔ کلاستر شما جدا باشند.

```shell
kubectl create namespace mem-example
```

## تعیین درخواست حافظه و حد حافظه

برای تعیین درخواست حافظه برای یک کانتینر، فیلد `resources.requests.memory` را در مانیفست منبع کانتینر قرار دهید. برای تعیین حد حافظه نیز فیلد `resources.limits.memory` را اضافه کنید.

در این تمرین، یک Pod با یک کانتینر ایجاد می‌کنید. درخواست حافظهٔ این کانتینر 100 MiB و حد حافظهٔ آن 200 MiB است. فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/resource/memory-request-limit.yaml" options="hl_lines=10-14" %}}

بخش `args` در فایل پیکربندی، آرگومان‌هایی را فراهم می‌کند که هنگام شروع کانتینر به آن داده می‌شوند. آرگومان‌های `"--vm-bytes", "150M"` به کانتینر می‌گویند که تلاش کند 150 MiB حافظه تخصیص دهد.

این Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit.yaml --namespace=mem-example
```

بررسی کنید که کانتینر این Pod در حال اجرا باشد:

```shell
kubectl get pod memory-demo --namespace=mem-example
```

اطلاعات مفصل Pod را مشاهده کنید:

```shell
kubectl get pod memory-demo --output=yaml --namespace=mem-example
```

خروجی نشان می‌دهد که درخواست حافظهٔ تنها کانتینر این Pod برابر 100 MiB و حد حافظهٔ آن 200 MiB است.


```yaml
...
resources:
  requests:
    memory: 100Mi
  limits:
    memory: 200Mi
...
```

برای دریافت معیارهای Pod، دستور `kubectl top` را اجرا کنید:

```shell
kubectl top pod memory-demo --namespace=mem-example
```

خروجی نشان می‌دهد که این Pod حدود ۱۶۲٬۹۰۰٬۰۰۰ بایت حافظه مصرف می‌کند که تقریباً برابر 150 MiB است. این مقدار از درخواست 100 MiB این Pod بیشتر است، اما همچنان در محدودهٔ حد 200 MiB آن قرار دارد.

```
NAME                        CPU(cores)   MEMORY(bytes)
memory-demo                 <something>  162856960
```

اکنون Pod خود را حذف کنید:

```shell
kubectl delete pod memory-demo --namespace=mem-example
```

## فراتر رفتن از حد حافظهٔ کانتینر

اگر نود حافظهٔ آزاد داشته باشد، کانتینر می‌تواند از درخواست حافظهٔ خود فراتر برود، اما اجازه ندارد بیش از حد حافظهٔ خود مصرف کند. اگر کانتینری بیش از حد خود حافظه تخصیص دهد، در فهرست نامزدهای خاتمه قرار می‌گیرد. اگر کانتینر همچنان بیش از حد خود حافظه مصرف کند، خاتمه داده می‌شود. اگر امکان راه‌اندازی مجدد کانتینرِ خاتمه‌یافته وجود داشته باشد، kubelet آن را مانند هر نوع دیگری از خطای زمان اجرا دوباره راه‌اندازی می‌کند.

در این تمرین، یک Pod ایجاد می‌کنید که تلاش می‌کند بیش از حد خود حافظه تخصیص دهد. فایل پیکربندی زیر مربوط به Podای است که یک کانتینر با درخواست حافظهٔ 50 MiB و حد حافظهٔ 100 MiB دارد:

{{% code_sample file="pods/resource/memory-request-limit-2.yaml" options="hl_lines=10-14" %}}

در بخش `args` فایل پیکربندی می‌بینید که کانتینر تلاش خواهد کرد 250 MiB حافظه تخصیص دهد؛ این مقدار بسیار بیشتر از حد 100 MiB است.

این Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit-2.yaml --namespace=mem-example
```

اطلاعات مفصل Pod را مشاهده کنید:

```shell
kubectl get pod memory-demo-2 --namespace=mem-example
```

در این مرحله، کانتینر ممکن است در حال اجرا باشد یا از بین رفته باشد. دستور قبلی را آن‌قدر تکرار کنید تا کانتینر از بین برود:

```shell
NAME            READY     STATUS      RESTARTS   AGE
memory-demo-2   0/1       OOMKilled   1          24s
```

وضعیت کانتینر را با جزئیات بیشتری مشاهده کنید:

```shell
kubectl get pod memory-demo-2 --output=yaml --namespace=mem-example
```

خروجی نشان می‌دهد که کانتینر به دلیل کمبود حافظه (OOM) از بین رفته است:

```yaml
lastState:
   terminated:
     containerID: 65183c1877aaec2e8427bc95609cc52677a454b56fcb24340dbd22917c23b10f
     exitCode: 137
     finishedAt: 2017-06-20T20:52:19Z
     reason: OOMKilled
     startedAt: null
```

کانتینر این تمرین قابل راه‌اندازی مجدد است، بنابراین kubelet آن را دوباره راه‌اندازی می‌کند. این دستور را چند بار تکرار کنید تا ببینید کانتینر پیوسته از بین می‌رود و دوباره راه‌اندازی می‌شود:

```shell
kubectl get pod memory-demo-2 --namespace=mem-example
```

خروجی نشان می‌دهد که کانتینر از بین می‌رود، دوباره راه‌اندازی می‌شود، باز از بین می‌رود، دوباره راه‌اندازی می‌شود و این چرخه ادامه پیدا می‌کند:

```
kubectl get pod memory-demo-2 --namespace=mem-example
NAME            READY     STATUS      RESTARTS   AGE
memory-demo-2   0/1       OOMKilled   1          37s
```
```

kubectl get pod memory-demo-2 --namespace=mem-example
NAME            READY     STATUS    RESTARTS   AGE
memory-demo-2   1/1       Running   2          40s
```

اطلاعات مفصل تاریخچهٔ Pod را مشاهده کنید:

```
kubectl describe pod memory-demo-2 --namespace=mem-example
```

خروجی نشان می‌دهد که کانتینر بارها شروع به کار می‌کند و با شکست مواجه می‌شود:

```
... Normal  Created   Created container with id 66a3a20aa7980e61be4922780bf9d24d1a1d8b7395c09861225b0eba1b1f8511
... Warning BackOff   Back-off restarting failed container
```

اطلاعات مفصل نودهای کلاستر خود را مشاهده کنید:

```
kubectl describe nodes
```

خروجی شامل سابقه‌ای از ازبین‌رفتن کانتینر به دلیل کمبود حافظه است:

```
Warning OOMKilling Memory cgroup out of memory: Kill process 4481 (stress) score 1994 or sacrifice child
```

اکنون Pod خود را حذف کنید:

```shell
kubectl delete pod memory-demo-2 --namespace=mem-example
```

## تعیین درخواست حافظه‌ای بزرگ‌تر از ظرفیت نودها

درخواست‌ها و حدهای حافظه به کانتینرها مربوط می‌شوند، اما مفید است که برای Pod نیز درخواست و حد حافظه در نظر بگیریم. درخواست حافظهٔ یک Pod برابر با مجموع درخواست‌های حافظهٔ همهٔ کانتینرهای آن است. به همین ترتیب، حد حافظهٔ Pod برابر با مجموع حدهای همهٔ کانتینرهای آن است.

زمان‌بندی Podها بر اساس درخواست‌ها انجام می‌شود. یک Pod تنها زمانی برای اجرا روی یک نود زمان‌بندی می‌شود که آن نود حافظهٔ آزاد کافی برای پاسخ‌گویی به درخواست حافظهٔ Pod داشته باشد.

در این تمرین، Podای ایجاد می‌کنید که درخواست حافظهٔ آن به قدری بزرگ است که از ظرفیت همهٔ نودهای کلاستر شما فراتر می‌رود. فایل پیکربندی زیر مربوط به Podای است که یک کانتینر با درخواست 1000 GiB حافظه دارد؛ این مقدار به احتمال زیاد از ظرفیت هر نودی در کلاستر شما بیشتر است.

{{% code_sample file="pods/resource/memory-request-limit-3.yaml" options="hl_lines=10-14" %}}

این Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/memory-request-limit-3.yaml --namespace=mem-example
```

وضعیت Pod را مشاهده کنید:

```shell
kubectl get pod memory-demo-3 --namespace=mem-example
```

خروجی نشان می‌دهد که وضعیت Pod برابر PENDING است؛ یعنی Pod برای اجرا روی هیچ نودی زمان‌بندی نشده است و برای مدت نامحدود در وضعیت PENDING باقی می‌ماند:

```
kubectl get pod memory-demo-3 --namespace=mem-example
NAME            READY     STATUS    RESTARTS   AGE
memory-demo-3   0/1       Pending   0          25s
```

اطلاعات مفصل Pod را به همراه رویدادهای آن مشاهده کنید:

```shell
kubectl describe pod memory-demo-3 --namespace=mem-example
```

خروجی نشان می‌دهد که به دلیل کمبود حافظه روی نودها، کانتینر قابل زمان‌بندی نیست:

```
Events:
  ...  Reason            Message
       ------            -------
  ...  FailedScheduling  No nodes are available that match all of the following predicates:: Insufficient memory (3).
```

## واحدهای حافظه

منبع حافظه بر حسب بایت اندازه‌گیری می‌شود. می‌توانید حافظه را به صورت یک عدد صحیح ساده یا یک عدد ممیز ثابت (fixed-point) با یکی از این پسوندها بیان کنید: E, P, T, G, M, K, Ei, Pi, Ti, Gi, Mi, Ki. برای مثال، مقادیر زیر تقریباً یک مقدار را نشان می‌دهند:

```
128974848, 129e6, 129M, 123Mi
```

اکنون Pod خود را حذف کنید:

```shell
kubectl delete pod memory-demo-3 --namespace=mem-example
```

## اگر حد حافظه را تعیین نکنید

اگر برای یک کانتینر حد حافظه تعیین نکنید، یکی از وضعیت‌های زیر پیش می‌آید:

* کانتینر هیچ سقفی برای میزان حافظهٔ مصرفی خود ندارد. کانتینر ممکن است تمام حافظهٔ موجود روی نودی را که روی آن اجرا می‌شود مصرف کند و این به نوبهٔ خود ممکن است OOM Killer را فعال کند. افزون بر این، در صورت وقوع OOM Kill، کانتینری که حد منبع ندارد با احتمال بیشتری از بین می‌رود.

* کانتینر در فضای نامی اجرا می‌شود که حد حافظهٔ پیش‌فرض دارد و این حد پیش‌فرض به‌طور خودکار به کانتینر اختصاص داده می‌شود. مدیران کلاستر می‌توانند با استفاده از یک [LimitRange](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#limitrange-v1-core) مقدار پیش‌فرضی برای حد حافظه تعیین کنند.

## انگیزهٔ استفاده از درخواست‌ها و حدهای حافظه

با پیکربندی درخواست‌ها و حدهای حافظه برای کانتینرهایی که در کلاستر شما اجرا می‌شوند، می‌توانید از منابع حافظهٔ موجود روی نودهای کلاستر به‌طور کارآمد استفاده کنید. با پایین نگه داشتن درخواست حافظهٔ یک Pod، شانس زمان‌بندی‌شدن آن را افزایش می‌دهید. با تعیین حد حافظه‌ای بزرگ‌تر از درخواست حافظه، به دو هدف دست می‌یابید:

* این Pod می‌تواند دوره‌هایی از فعالیت ناگهانی و شدید (burst) داشته باشد که در آن‌ها از حافظهٔ آزادِ موجود استفاده می‌کند.
* میزان حافظه‌ای که یک Pod در طول این فعالیت شدید می‌تواند مصرف کند، به مقداری معقول محدود می‌شود.

## پاک‌سازی

فضای نام خود را حذف کنید. با این کار همهٔ Podهایی که برای این تمرین ایجاد کرده‌اید حذف می‌شوند:

```shell
kubectl delete namespace mem-example
```



## {{% heading "whatsnext" %}}


### برای توسعه‌دهندگان برنامه

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس (Quality of Service) برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

* [تغییر اندازهٔ منابع CPU و حافظهٔ اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

* [تغییر اندازهٔ منابع CPU و حافظهٔ اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/)

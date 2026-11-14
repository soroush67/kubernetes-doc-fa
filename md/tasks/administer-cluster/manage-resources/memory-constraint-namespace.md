---
title: پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام
content_type: task
weight: 30
description: >-
  بازه‌ای از محدودیت‌های معتبر منبع حافظه را برای یک فضای نام تعریف کنید تا هر Pod جدید
  در آن فضای نام در بازه‌ای که پیکربندی کرده‌اید قرار بگیرد.
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه برای حافظه‌ای که کانتینرهای در حال اجرا در یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} (namespace) مصرف می‌کنند، مقدار حداقل و حداکثر تعیین کنید.
مقادیر حداقل و حداکثر حافظه را در یک آبجکت
[LimitRange](/docs/reference/kubernetes-api/core/limit-range-v1/)
مشخص می‌کنید. اگر یک Pod محدودیت‌هایی را که LimitRange اعمال می‌کند رعایت نکند،
نمی‌توان آن را در فضای نام ایجاد کرد.



## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

باید دسترسی ایجاد فضای نام در کلاستر خود را داشته باشید.

هر نود در کلاستر شما باید دست‌کم ۱ گیبی‌بایت (GiB) حافظهٔ در دسترس برای Podها داشته باشد.

<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیهٔ کلاستر شما
جدا باشند.

```shell
kubectl create namespace constraints-mem-example
```

## ایجاد یک LimitRange و یک Pod

در ادامه یک مانیفست نمونه برای LimitRange آمده است:

{{% code_sample file="admin/resource/memory-constraints.yaml" %}}

LimitRange را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints.yaml --namespace=constraints-mem-example
```

اطلاعات تفصیلی LimitRange را مشاهده کنید:

```shell
kubectl get limitrange mem-min-max-demo-lr --namespace=constraints-mem-example --output=yaml
```

خروجی، همان‌طور که انتظار می‌رود، محدودیت‌های حداقل و حداکثر حافظه را نشان می‌دهد.
اما توجه کنید که با اینکه در فایل پیکربندی LimitRange هیچ مقدار پیش‌فرضی مشخص
نکرده بودید، این مقادیر به‌طور خودکار ایجاد شده‌اند.

```
  limits:
  - default:
      memory: 1Gi
    defaultRequest:
      memory: 1Gi
    max:
      memory: 1Gi
    min:
      memory: 500Mi
    type: Container
```

از این پس، هر بار که یک Pod را در فضای نام constraints-mem-example تعریف کنید،
کوبرنتیز این مراحل را انجام می‌دهد:

* اگر هر یک از کانتینرهای آن Pod درخواست (request) و محدودیت (limit) حافظهٔ خود را مشخص نکرده باشد،
control plane درخواست و محدودیت پیش‌فرض حافظه را به آن کانتینر اختصاص می‌دهد.

* بررسی می‌کند که هر کانتینر در آن Pod دست‌کم ۵۰۰ مبی‌بایت (MiB) حافظه درخواست کرده باشد.

* بررسی می‌کند که هیچ کانتینری در آن Pod بیش از ۱۰۲۴ مبی‌بایت (۱ گیبی‌بایت)
  حافظه درخواست نکرده باشد.

در ادامه مانیفست یک Pod با یک کانتینر آمده است. در مشخصات Pod، تنها کانتینر آن
درخواست حافظهٔ ۶۰۰ مبی‌بایت و محدودیت حافظهٔ ۸۰۰ مبی‌بایت را مشخص می‌کند. این مقادیر
محدودیت‌های حداقل و حداکثر حافظه‌ای را که LimitRange اعمال می‌کند برآورده می‌کنند.

{{% code_sample file="admin/resource/memory-constraints-pod.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod.yaml --namespace=constraints-mem-example
```

بررسی کنید که Pod در حال اجرا باشد و کانتینر آن سالم باشد:

```shell
kubectl get pod constraints-mem-demo --namespace=constraints-mem-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod constraints-mem-demo --output=yaml --namespace=constraints-mem-example
```

خروجی نشان می‌دهد که کانتینر درون آن Pod درخواست حافظهٔ ۶۰۰ مبی‌بایت و محدودیت حافظهٔ
۸۰۰ مبی‌بایت دارد. این مقادیر محدودیت‌هایی را که LimitRange برای این فضای نام
اعمال می‌کند برآورده می‌کنند:

```yaml
resources:
  limits:
     memory: 800Mi
  requests:
    memory: 600Mi
```

Pod خود را حذف کنید:

```shell
kubectl delete pod constraints-mem-demo --namespace=constraints-mem-example
```

## تلاش برای ایجاد Podی که از محدودیت حداکثر حافظه فراتر می‌رود

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر درخواست حافظهٔ
۸۰۰ مبی‌بایت و محدودیت حافظهٔ ۱٫۵ گیبی‌بایت را مشخص می‌کند.

{{% code_sample file="admin/resource/memory-constraints-pod-2.yaml" %}}

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-2.yaml --namespace=constraints-mem-example
```

خروجی نشان می‌دهد که Pod ایجاد نمی‌شود، زیرا کانتینری را تعریف می‌کند که
بیش از مقدار مجاز حافظه درخواست کرده است:

```
Error from server (Forbidden): error when creating "examples/admin/resource/memory-constraints-pod-2.yaml":
pods "constraints-mem-demo-2" is forbidden: maximum memory usage per Container is 1Gi, but limit is 1536Mi.
```

## تلاش برای ایجاد Podی که حداقل درخواست حافظه را برآورده نمی‌کند

در ادامه مانیفست یک Pod با یک کانتینر آمده است. آن کانتینر درخواست حافظهٔ
۱۰۰ مبی‌بایت و محدودیت حافظهٔ ۸۰۰ مبی‌بایت را مشخص می‌کند.

{{% code_sample file="admin/resource/memory-constraints-pod-3.yaml" %}}

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-3.yaml --namespace=constraints-mem-example
```

خروجی نشان می‌دهد که Pod ایجاد نمی‌شود، زیرا کانتینری را تعریف می‌کند که
کمتر از حداقل الزامی حافظه درخواست کرده است:

```
Error from server (Forbidden): error when creating "examples/admin/resource/memory-constraints-pod-3.yaml":
pods "constraints-mem-demo-3" is forbidden: minimum memory usage per Container is 500Mi, but request is 100Mi.
```

## ایجاد Podی که هیچ درخواست یا محدودیت حافظه‌ای مشخص نمی‌کند

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر نه درخواست حافظه
و نه محدودیت حافظه را مشخص می‌کند.

{{% code_sample file="admin/resource/memory-constraints-pod-4.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-constraints-pod-4.yaml --namespace=constraints-mem-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod constraints-mem-demo-4 --namespace=constraints-mem-example --output=yaml
```

خروجی نشان می‌دهد که تنها کانتینر این Pod درخواست حافظهٔ ۱ گیبی‌بایت و محدودیت حافظهٔ ۱ گیبی‌بایت دارد.
آن کانتینر این مقادیر را از کجا به دست آورده است؟

```
resources:
  limits:
    memory: 1Gi
  requests:
    memory: 1Gi
```

از آنجا که Pod شما هیچ درخواست و محدودیت حافظه‌ای برای آن کانتینر تعریف نکرده بود،
کلاستر یک
[درخواست و محدودیت پیش‌فرض حافظه](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
را از LimitRange اعمال کرد.

بنابراین تعریف آن Pod این مقادیر را نشان می‌دهد. می‌توانید این موضوع را با
`kubectl describe` بررسی کنید:

```shell
# Look for the "Requests:" section of the output
kubectl describe pod constraints-mem-demo-4 --namespace=constraints-mem-example
```

در این مرحله، ممکن است Pod شما در حال اجرا باشد یا نباشد. به یاد بیاورید که یکی از
پیش‌نیازهای این کار این است که نودهای شما دست‌کم ۱ گیبی‌بایت حافظه داشته باشند. اگر هر یک
از نودهای شما فقط ۱ گیبی‌بایت حافظه داشته باشد، هیچ نودی حافظهٔ قابل‌تخصیص کافی برای
پاسخ‌گویی به درخواست حافظهٔ ۱ گیبی‌بایتی ندارد. اما اگر از نودهایی با ۲ گیبی‌بایت حافظه
استفاده می‌کنید، احتمالاً فضای کافی برای پاسخ‌گویی به درخواست ۱ گیبی‌بایتی دارید.

Pod خود را حذف کنید:

```shell
kubectl delete pod constraints-mem-demo-4 --namespace=constraints-mem-example
```

## اعمال محدودیت‌های حداقل و حداکثر حافظه

محدودیت‌های حداکثر و حداقل حافظه‌ای که یک LimitRange بر یک فضای نام اعمال می‌کند،
فقط هنگام ایجاد یا به‌روزرسانی یک Pod اجرا می‌شوند. اگر LimitRange را تغییر دهید،
این تغییر بر Podهایی که پیش‌تر ایجاد شده‌اند اثری ندارد.

{{< note >}}
هنگام استفاده از [تغییر اندازهٔ درجای Pod](/docs/tasks/configure-pod-container/resize-container-resources/)،
محدودیت‌های حافظه نیز اعمال می‌شوند. اگر تغییر اندازه باعث شود مقادیر حافظهٔ Pod
محدودیت‌های LimitRange را نقض کنند (چه با فراتر رفتن از حداکثر و چه با کمتر شدن از حداقل)،
تغییر اندازه رد می‌شود و منابع Pod در همان مقادیر قبلی باقی می‌مانند.
{{< /note >}}

## انگیزهٔ استفاده از محدودیت‌های حداقل و حداکثر حافظه

به‌عنوان مدیر کلاستر، ممکن است بخواهید مقدار حافظه‌ای را که Podها می‌توانند مصرف کنند محدود کنید.
برای مثال:

* هر نود در یک کلاستر ۲ گیبی‌بایت حافظه دارد. نمی‌خواهید هیچ Podی را بپذیرید که
بیش از ۲ گیبی‌بایت حافظه درخواست کند، زیرا هیچ نودی در کلاستر نمی‌تواند از آن درخواست پشتیبانی کند.

* یک کلاستر میان بخش‌های تولید (production) و توسعهٔ سازمان شما مشترک است.
می‌خواهید به بارهای کاری تولید اجازه دهید تا ۸ گیبی‌بایت حافظه مصرف کنند، اما
بارهای کاری توسعه به ۵۱۲ مبی‌بایت محدود باشند. برای تولید و توسعه فضاهای نام جداگانه
ایجاد می‌کنید و بر هر فضای نام محدودیت‌های حافظه اعمال می‌کنید.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace constraints-mem-example
```


## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت خدمات (Quality of Service) برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

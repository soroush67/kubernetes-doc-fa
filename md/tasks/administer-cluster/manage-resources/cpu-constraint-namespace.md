---
title: پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام
content_type: task
weight: 40
description: >-
  بازه‌ای از حدهای مجاز منبع CPU را برای یک فضای نام تعریف کنید تا هر Pod جدید
  در آن فضای نام در بازه‌ای که پیکربندی کرده‌اید قرار گیرد.
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان مقادیر حداقل و حداکثر را برای منابع CPU مورد استفادهٔ کانتینرها
و Podها در یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} تعیین کرد. مقادیر حداقل
و حداکثر CPU را در یک آبجکت
[LimitRange](/docs/reference/kubernetes-api/core/limit-range-v1/)
مشخص می‌کنید. اگر یک Pod محدودیت‌های اعمال‌شده از سوی LimitRange را رعایت نکند، نمی‌توان آن را
در آن فضای نام ایجاد کرد.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

باید دسترسی ایجاد فضای نام (namespace) در کلاستر خود را داشته باشید.

هر نود در کلاستر شما باید دست‌کم ۱٫۰ CPU آزاد برای Podها داشته باشد.
برای آشنایی با منظور کوبرنتیز از «۱ CPU»، بخش [معنای CPU](/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu)
را ببینید.


<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیهٔ
کلاستر شما جدا باشند.

```shell
kubectl create namespace constraints-cpu-example
```

## ایجاد یک LimitRange و یک Pod

این یک مانیفست نمونه برای یک {{< glossary_tooltip text="LimitRange" term_id="limitrange" >}} است:

{{% code_sample file="admin/resource/cpu-constraints.yaml" %}}

LimitRange را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints.yaml --namespace=constraints-cpu-example
```

اطلاعات دقیق LimitRange را مشاهده کنید:

```shell
kubectl get limitrange cpu-min-max-demo-lr --output=yaml --namespace=constraints-cpu-example
```

همان‌طور که انتظار می‌رود، خروجی محدودیت‌های حداقل و حداکثر CPU را نشان می‌دهد. اما
توجه کنید که با اینکه در فایل پیکربندی LimitRange مقادیر پیش‌فرض را مشخص نکرده بودید،
این مقادیر به‌طور خودکار ایجاد شده‌اند.

```yaml
limits:
- default:
    cpu: 800m
  defaultRequest:
    cpu: 800m
  max:
    cpu: 800m
  min:
    cpu: 200m
  type: Container
```

از این پس، هر بار که یک Pod در فضای نام constraints-cpu-example ایجاد کنید (یا کلاینت دیگری
از API کوبرنتیز یک Pod معادل ایجاد کند)، کوبرنتیز این مراحل را انجام می‌دهد:

* اگر هر یک از کانتینرهای آن Pod درخواست و حد CPU خود را مشخص نکرده باشد، control plane
  درخواست و حد پیش‌فرض CPU را به آن کانتینر اختصاص می‌دهد.

* بررسی می‌کند که هر کانتینر در آن Pod درخواست CPU بزرگ‌تر یا مساوی ۲۰۰ میلی‌CPU مشخص کرده باشد.

* بررسی می‌کند که هر کانتینر در آن Pod حد CPU کوچک‌تر یا مساوی ۸۰۰ میلی‌CPU مشخص کرده باشد.

{{< note >}}
هنگام ایجاد یک آبجکت `LimitRange`، می‌توانید برای huge-pageها
یا GPUها نیز حد تعیین کنید. با این حال، وقتی هم `default` و هم `defaultRequest`
برای این منابع مشخص شده باشند، این دو مقدار باید یکسان باشند.
{{< /note >}}

این یک مانیفست برای Podای است که یک کانتینر دارد. مانیفست کانتینر
درخواست CPU برابر ۵۰۰ میلی‌CPU و حد CPU برابر ۸۰۰ میلی‌CPU را مشخص می‌کند. این مقادیر
محدودیت‌های حداقل و حداکثر CPU را که LimitRange برای این فضای نام اعمال کرده است، رعایت می‌کنند.

{{% code_sample file="admin/resource/cpu-constraints-pod.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod.yaml --namespace=constraints-cpu-example
```

بررسی کنید که Pod در حال اجرا است و کانتینر آن سالم است:

```shell
kubectl get pod constraints-cpu-demo --namespace=constraints-cpu-example
```

اطلاعات دقیق Pod را مشاهده کنید:

```shell
kubectl get pod constraints-cpu-demo --output=yaml --namespace=constraints-cpu-example
```

خروجی نشان می‌دهد که تنها کانتینر Pod درخواست CPU برابر ۵۰۰ میلی‌CPU و حد CPU
برابر ۸۰۰ میلی‌CPU دارد. این مقادیر محدودیت‌های اعمال‌شده از سوی LimitRange را رعایت می‌کنند.

```yaml
resources:
  limits:
    cpu: 800m
  requests:
    cpu: 500m
```

## حذف Pod

```shell
kubectl delete pod constraints-cpu-demo --namespace=constraints-cpu-example
```

## تلاش برای ایجاد Podای که از محدودیت حداکثر CPU فراتر می‌رود

این یک مانیفست برای Podای است که یک کانتینر دارد. این کانتینر
درخواست CPU برابر ۵۰۰ میلی‌CPU و حد CPU برابر ۱٫۵ CPU را مشخص می‌کند.

{{% code_sample file="admin/resource/cpu-constraints-pod-2.yaml" %}}

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-2.yaml --namespace=constraints-cpu-example
```

خروجی نشان می‌دهد که Pod ایجاد نمی‌شود، زیرا یک کانتینر غیرقابل‌قبول تعریف کرده است.
این کانتینر پذیرفته نیست، چون حد CPU بیش از اندازه بزرگی را مشخص کرده است:

```
Error from server (Forbidden): error when creating "examples/admin/resource/cpu-constraints-pod-2.yaml":
pods "constraints-cpu-demo-2" is forbidden: maximum cpu usage per Container is 800m, but limit is 1500m.
```

## تلاش برای ایجاد Podای که حداقل درخواست CPU را رعایت نمی‌کند

این یک مانیفست برای Podای است که یک کانتینر دارد. این کانتینر
درخواست CPU برابر ۱۰۰ میلی‌CPU و حد CPU برابر ۸۰۰ میلی‌CPU را مشخص می‌کند.

{{% code_sample file="admin/resource/cpu-constraints-pod-3.yaml" %}}

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-3.yaml --namespace=constraints-cpu-example
```

خروجی نشان می‌دهد که Pod ایجاد نمی‌شود، زیرا یک کانتینر غیرقابل‌قبول تعریف کرده است.
این کانتینر پذیرفته نیست، چون درخواست CPUای کمتر از حداقل
اعمال‌شده مشخص کرده است:

```
Error from server (Forbidden): error when creating "examples/admin/resource/cpu-constraints-pod-3.yaml":
pods "constraints-cpu-demo-3" is forbidden: minimum cpu usage per Container is 200m, but request is 100m.
```

## ایجاد Podای که هیچ درخواست یا حد CPU مشخص نمی‌کند

این یک مانیفست برای Podای است که یک کانتینر دارد. این کانتینر
نه درخواست CPU و نه حد CPU مشخص می‌کند.

{{% code_sample file="admin/resource/cpu-constraints-pod-4.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-constraints-pod-4.yaml --namespace=constraints-cpu-example
```

اطلاعات دقیق Pod را مشاهده کنید:

```
kubectl get pod constraints-cpu-demo-4 --namespace=constraints-cpu-example --output=yaml
```

خروجی نشان می‌دهد که تنها کانتینر Pod درخواست CPU برابر ۸۰۰ میلی‌CPU و
حد CPU برابر ۸۰۰ میلی‌CPU دارد.
این کانتینر چگونه این مقادیر را به دست آورده است؟

```yaml
resources:
  limits:
    cpu: 800m
  requests:
    cpu: 800m
```

از آنجا که این کانتینر درخواست و حد CPU خود را مشخص نکرده بود، control plane
[درخواست و حد پیش‌فرض CPU](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
را از LimitRange این فضای نام بر آن اعمال کرد.

در این مرحله، ممکن است Pod شما در حال اجرا باشد یا نباشد. به یاد داشته باشید که یکی از پیش‌نیازهای
این تکلیف این است که نودهای شما دست‌کم ۱ CPU آزاد برای استفاده داشته باشند. اگر هر یک از نودهای شما فقط ۱ CPU داشته باشد،
ممکن است روی هیچ نودی CPU قابل‌تخصیص کافی برای پاسخ به درخواست ۸۰۰ میلی‌CPU وجود نداشته باشد.
اگر از نودهایی با ۲ CPU استفاده می‌کنید، احتمالاً CPU کافی برای پاسخ به درخواست ۸۰۰ میلی‌CPU دارید.

Pod خود را حذف کنید:

```
kubectl delete pod constraints-cpu-demo-4 --namespace=constraints-cpu-example
```

## اعمال محدودیت‌های حداقل و حداکثر CPU

محدودیت‌های حداکثر و حداقل CPU که یک LimitRange بر یک فضای نام اعمال می‌کند، تنها
هنگام ایجاد یا به‌روزرسانی یک Pod اجرا می‌شوند. اگر LimitRange را تغییر دهید، این تغییر بر
Podهایی که پیش‌تر ایجاد شده‌اند اثری ندارد.

{{< note >}}
هنگام استفاده از [تغییر اندازهٔ درجای Pod](/docs/tasks/configure-pod-container/resize-container-resources/)،
محدودیت‌های CPU نیز اعمال می‌شوند. اگر تغییر اندازه باعث شود مقادیر CPU مربوط به Pod
محدودیت‌های LimitRange را نقض کنند (چه از حداکثر فراتر روند و چه از حداقل کمتر شوند)،
تغییر اندازه رد می‌شود و منابع Pod در همان مقادیر قبلی باقی می‌مانند.
{{< /note >}}

## انگیزهٔ استفاده از محدودیت‌های حداقل و حداکثر CPU

ممکن است شما به‌عنوان مدیر کلاستر بخواهید محدودیت‌هایی بر منابع CPU قابل‌استفاده برای Podها اعمال کنید.
برای مثال:

* هر نود در یک کلاستر ۲ CPU دارد. نمی‌خواهید هیچ Podای را بپذیرید که
بیش از ۲ CPU درخواست کند، زیرا هیچ نودی در کلاستر نمی‌تواند به این درخواست پاسخ دهد.

* یک کلاستر میان واحدهای تولید و توسعهٔ شما مشترک است.
می‌خواهید به بارهای کاری تولید اجازه دهید تا ۳ CPU مصرف کنند، اما بارهای کاری توسعه را به
۱ CPU محدود کنید. برای تولید و توسعه فضاهای نام جداگانه ایجاد می‌کنید و بر هر
فضای نام محدودیت‌های CPU اعمال می‌کنید.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace constraints-cpu-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [اختصاص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [اختصاص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [اختصاص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

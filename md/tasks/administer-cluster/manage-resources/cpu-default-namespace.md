---
title: پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام
content_type: task
weight: 20
description: >-
  برای یک فضای نام محدودیت‌های پیش‌فرض منبع CPU تعریف کنید تا هر Pod جدید
  در آن فضای نام یک محدودیت منبع CPU پیکربندی‌شده داشته باشد.
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان درخواست‌ها و محدودیت‌های پیش‌فرض CPU را برای یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} پیکربندی کرد.

یک کلاستر کوبرنتیز را می‌توان به چند فضای نام (namespace) تقسیم کرد. اگر در فضای نامی که
[محدودیت](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) پیش‌فرض CPU دارد
یک Pod ایجاد کنید و یکی از کانتینرهای آن Pod محدودیت CPU خود را مشخص نکرده باشد،
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} محدودیت پیش‌فرض CPU را به آن کانتینر اختصاص می‌دهد.

کوبرنتیز یک
[درخواست](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
پیش‌فرض CPU نیز اختصاص می‌دهد، اما فقط در شرایط خاصی که در ادامه‌ی همین صفحه توضیح داده شده است.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

باید در کلاستر خود دسترسی ایجاد فضای نام را داشته باشید.

اگر هنوز با مفهوم 1.0 CPU در کوبرنتیز آشنا نیستید،
[معنای CPU](/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu) را بخوانید.

<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیه‌ی کلاستر جدا بمانند.

```shell
kubectl create namespace default-cpu-example
```

## ایجاد یک LimitRange و یک Pod

در ادامه مانیفست یک {{< glossary_tooltip text="LimitRange" term_id="limitrange" >}} نمونه آمده است.
این مانیفست یک درخواست پیش‌فرض CPU و یک محدودیت پیش‌فرض CPU را مشخص می‌کند.

{{% code_sample file="admin/resource/cpu-defaults.yaml" %}}

این LimitRange را در فضای نام default-cpu-example ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults.yaml --namespace=default-cpu-example
```

اکنون اگر یک Pod در فضای نام default-cpu-example ایجاد کنید و یکی از کانتینرهای آن Pod
مقادیر خود را برای درخواست و محدودیت CPU مشخص نکرده باشد،
control plane مقادیر پیش‌فرض را اعمال می‌کند: درخواست CPU برابر با 0.5 و محدودیت پیش‌فرض
CPU برابر با 1.

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر
درخواست و محدودیت CPU را مشخص نمی‌کند.

{{% code_sample file="admin/resource/cpu-defaults-pod.yaml" %}}

Pod را ایجاد کنید.

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod.yaml --namespace=default-cpu-example
```

مشخصات Pod را مشاهده کنید:

```shell
kubectl get pod default-cpu-demo --output=yaml --namespace=default-cpu-example
```

خروجی نشان می‌دهد که تنها کانتینر این Pod درخواست CPU برابر با 500m `cpu`
(که می‌توان آن را «۵۰۰ میلی‌CPU» خواند) و محدودیت CPU برابر با 1 `cpu` دارد.
این‌ها همان مقادیر پیش‌فرضی هستند که LimitRange مشخص کرده است.

```shell
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-cpu-demo-ctr
  resources:
    limits:
      cpu: "1"
    requests:
      cpu: 500m
```

## اگر محدودیت کانتینر را مشخص کنید ولی درخواست آن را نه، چه می‌شود؟

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر
محدودیت CPU را مشخص می‌کند، اما درخواست را نه:

{{% code_sample file="admin/resource/cpu-defaults-pod-2.yaml" %}}

Pod را ایجاد کنید:


```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-2.yaml --namespace=default-cpu-example
```

[مشخصات](/docs/concepts/overview/working-with-objects/#object-spec-and-status)
Pod ایجادشده را مشاهده کنید:

```
kubectl get pod default-cpu-demo-2 --output=yaml --namespace=default-cpu-example
```

خروجی نشان می‌دهد که درخواست CPU کانتینر برابر با محدودیت CPU آن تنظیم شده است.
توجه کنید که مقدار پیش‌فرض درخواست CPU، یعنی 0.5 `cpu`، به این کانتینر اختصاص داده نشده است:

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: "1"
```

## اگر درخواست کانتینر را مشخص کنید ولی محدودیت آن را نه، چه می‌شود؟

در ادامه مانیفست نمونه‌ی یک Pod با یک کانتینر آمده است. این کانتینر
درخواست CPU را مشخص می‌کند، اما محدودیت را نه:

{{% code_sample file="admin/resource/cpu-defaults-pod-3.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/cpu-defaults-pod-3.yaml --namespace=default-cpu-example
```

مشخصات Pod ایجادشده را مشاهده کنید:

```
kubectl get pod default-cpu-demo-3 --output=yaml --namespace=default-cpu-example
```

خروجی نشان می‌دهد که درخواست CPU کانتینر برابر با مقداری تنظیم شده است که هنگام ایجاد Pod
مشخص کرده بودید (به بیان دیگر، با مانیفست مطابقت دارد).
اما محدودیت CPU همین کانتینر برابر با 1 `cpu` تنظیم شده است که همان محدودیت پیش‌فرض CPU
برای آن فضای نام است.

```
resources:
  limits:
    cpu: "1"
  requests:
    cpu: 750m
```

## انگیزه‌ی تعیین محدودیت‌ها و درخواست‌های پیش‌فرض CPU

اگر برای فضای نام شما یک {{< glossary_tooltip text="سهمیه‌ی منبع" term_id="resource-quota" >}} برای CPU
پیکربندی شده باشد،
داشتن یک مقدار پیش‌فرض برای محدودیت CPU مفید است.
دو مورد از محدودیت‌هایی که سهمیه‌ی منبع CPU بر یک فضای نام اعمال می‌کند در ادامه آمده است:

* برای هر Pod که در این فضای نام اجرا می‌شود، تک‌تک کانتینرهای آن باید محدودیت CPU داشته باشند.
* محدودیت‌های CPU روی نودی که Pod مورد نظر روی آن زمان‌بندی شده است، منبع رزرو می‌کنند.
  مجموع CPU رزروشده برای استفاده‌ی همه‌ی Podهای این فضای نام نباید
  از یک حد مشخص فراتر برود.

هنگامی که یک LimitRange اضافه می‌کنید:

اگر یکی از Podهای آن فضای نام کانتینری داشته باشد که محدودیت CPU خود را مشخص نکرده است،
control plane محدودیت پیش‌فرض CPU را به آن کانتینر اعمال می‌کند و آن Pod می‌تواند
در فضای نامی که با یک ResourceQuota برای CPU محدود شده است، اجرا شود.


## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace default-cpu-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیه‌ی Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [اختصاص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [اختصاص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [اختصاص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت خدمات برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

---
title: پیکربندی سهمیهٔ Pod برای یک فضای نام
content_type: task
weight: 60
description: >-
  محدود کردن تعداد Podهایی که می‌توانید در یک فضای نام ایجاد کنید.
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان برای تعداد کل Podهایی که در یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} اجرا می‌شوند سهمیه (quota) تعیین کرد.
سهمیه‌ها را در یک آبجکت
[ResourceQuota](/docs/reference/kubernetes-api/core/resource-quota-v1/)
مشخص می‌کنید.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

باید در کلاستر خود دسترسی لازم برای ایجاد فضای نام را داشته باشید.

<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیهٔ کلاستر
جدا بمانند.

```shell
kubectl create namespace quota-pod-example
```

## ایجاد یک ResourceQuota

در ادامه نمونه‌ای از مانیفست یک ResourceQuota آمده است:

{{% code_sample file="admin/resource/quota-pod.yaml" %}}

آبجکت ResourceQuota را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-pod.yaml --namespace=quota-pod-example
```

اطلاعات جزئی ResourceQuota را مشاهده کنید:

```shell
kubectl get resourcequota pod-demo --namespace=quota-pod-example --output=yaml
```

خروجی نشان می‌دهد که سهمیهٔ این فضای نام دو Pod است و در حال حاضر هیچ Podای
وجود ندارد؛ یعنی هیچ بخشی از سهمیه مصرف نشده است.

```yaml
spec:
  hard:
    pods: "2"
status:
  hard:
    pods: "2"
  used:
    pods: "0"
```

در ادامه نمونه‌ای از مانیفست یک {{< glossary_tooltip term_id="deployment" >}} آمده است:

{{% code_sample file="admin/resource/quota-pod-deployment.yaml" %}}

در این مانیفست، `replicas: 3` به کوبرنتیز می‌گوید که برای ایجاد سه Pod جدید
تلاش کند که همگی یک برنامهٔ یکسان را اجرا می‌کنند.

آبجکت Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-pod-deployment.yaml --namespace=quota-pod-example
```

اطلاعات جزئی Deployment را مشاهده کنید:

```shell
kubectl get deployment pod-quota-demo --namespace=quota-pod-example --output=yaml
```

خروجی نشان می‌دهد که با وجود اینکه Deployment سه رونوشت (replica) تعیین کرده است،
به دلیل سهمیه‌ای که پیش‌تر تعریف کردید، تنها دو Pod ایجاد شده‌اند:

```yaml
spec:
  ...
  replicas: 3
...
status:
  availableReplicas: 2
...
lastUpdateTime: 2021-04-02T20:57:05Z
    message: 'unable to create pods: pods "pod-quota-demo-1650323038-" is forbidden:
      exceeded quota: pod-demo, requested: pods=1, used: pods=2, limited: pods=2'
```

### انتخاب منبع

در این تمرین یک ResourceQuota تعریف کردید که تعداد کل Podها را محدود می‌کرد،
اما می‌توانید تعداد کل انواع دیگر آبجکت‌ها را نیز محدود کنید. برای مثال،
ممکن است تصمیم بگیرید تعداد
{{< glossary_tooltip text="CronJobهایی" term_id="cronjob" >}}
را که می‌توانند در یک فضای نام وجود داشته باشند محدود کنید.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace quota-pod-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیه برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس (Quality of Service) برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

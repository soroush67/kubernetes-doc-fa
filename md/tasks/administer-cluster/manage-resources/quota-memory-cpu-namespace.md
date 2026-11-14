---
title: پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام
content_type: task
weight: 50
description: >-
  محدودیت‌های کلی منابع حافظه و CPU را برای یک فضای نام تعریف کنید.
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه برای مجموع حافظه و CPU قابل استفاده توسط همهٔ Podهای در حال اجرا در یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} سهمیه (quota) تعیین کنید.
سهمیه‌ها را در یک آبجکت
[ResourceQuota](/docs/reference/kubernetes-api/core/resource-quota-v1/)
مشخص می‌کنید.




## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

باید دسترسی ایجاد فضای نام در کلاستر خود را داشته باشید.

هر نود در کلاستر شما باید دست‌کم ۱ GiB حافظه داشته باشد.


<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیهٔ کلاستر شما جدا بمانند.

```shell
kubectl create namespace quota-mem-cpu-example
```

## ایجاد یک ResourceQuota

در ادامه مانیفست یک ResourceQuota نمونه آمده است:

{{% code_sample file="admin/resource/quota-mem-cpu.yaml" %}}

ResourceQuota را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu.yaml --namespace=quota-mem-cpu-example
```

اطلاعات دقیق ResourceQuota را مشاهده کنید:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml
```

این ResourceQuota الزامات زیر را بر فضای نام quota-mem-cpu-example اعمال می‌کند:

* برای هر Pod در این فضای نام، هر کانتینر باید درخواست حافظه، حد حافظه، درخواست CPU و حد CPU داشته باشد.
* مجموع درخواست‌های حافظهٔ همهٔ Podهای آن فضای نام نباید از ۱ GiB بیشتر شود.
* مجموع حدهای حافظهٔ همهٔ Podهای آن فضای نام نباید از ۲ GiB بیشتر شود.
* مجموع درخواست‌های CPU همهٔ Podهای آن فضای نام نباید از ۱ CPU بیشتر شود.
* مجموع حدهای CPU همهٔ Podهای آن فضای نام نباید از ۲ CPU بیشتر شود.

برای آشنایی با منظور کوبرنتیز از «۱ CPU»، بخش [معنای CPU](/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu)
را ببینید.

## ایجاد یک Pod

در ادامه مانیفست یک Pod نمونه آمده است:

{{% code_sample file="admin/resource/quota-mem-cpu-pod.yaml" %}}


Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod.yaml --namespace=quota-mem-cpu-example
```

بررسی کنید که Pod در حال اجرا باشد و تنها کانتینر آن سالم باشد:

```shell
kubectl get pod quota-mem-cpu-demo --namespace=quota-mem-cpu-example
```

بار دیگر اطلاعات دقیق ResourceQuota را مشاهده کنید:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml
```

خروجی، سهمیه را همراه با میزان مصرف‌شده از آن نشان می‌دهد.
می‌بینید که درخواست‌ها و حدهای حافظه و CPU مربوط به Pod شما از سهمیه فراتر نمی‌روند.

```
status:
  hard:
    limits.cpu: "2"
    limits.memory: 2Gi
    requests.cpu: "1"
    requests.memory: 1Gi
  used:
    limits.cpu: 800m
    limits.memory: 800Mi
    requests.cpu: 400m
    requests.memory: 600Mi
```

اگر ابزار `jq` را در اختیار دارید، می‌توانید فقط مقادیر `used` را (با استفاده از [JSONPath](/docs/reference/kubectl/jsonpath/)) پرس‌وجو کنید **و** خروجی را به شکلی خوانا نمایش دهید. برای مثال:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example -o jsonpath='{ .status.used }' | jq .
```

## تلاش برای ایجاد Pod دوم

در ادامه مانیفست Pod دوم آمده است:

{{% code_sample file="admin/resource/quota-mem-cpu-pod-2.yaml" %}}

در این مانیفست می‌بینید که Pod درخواست حافظه‌ای برابر با ۷۰۰ MiB دارد.
توجه کنید که مجموع درخواست حافظهٔ مصرف‌شده و این درخواست حافظهٔ جدید از سهمیهٔ درخواست حافظه بیشتر است: 600 MiB + 700 MiB > 1 GiB.

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod-2.yaml --namespace=quota-mem-cpu-example
```

Pod دوم ایجاد نمی‌شود. خروجی نشان می‌دهد که ایجاد Pod دوم باعث می‌شد مجموع درخواست‌های حافظه از سهمیهٔ درخواست حافظه فراتر رود.

```
Error from server (Forbidden): error when creating "examples/admin/resource/quota-mem-cpu-pod-2.yaml":
pods "quota-mem-cpu-demo-2" is forbidden: exceeded quota: mem-cpu-demo,
requested: requests.memory=700Mi,used: requests.memory=600Mi, limited: requests.memory=1Gi
```

## بحث

همان‌طور که در این تمرین دیدید، می‌توانید با یک ResourceQuota مجموع درخواست‌های حافظهٔ همهٔ Podهای در حال اجرا در یک فضای نام را محدود کنید.
همچنین می‌توانید مجموع حدهای حافظه، درخواست‌های CPU و حدهای CPU را نیز محدود کنید.

ممکن است به‌جای مدیریت مجموع مصرف منابع در یک فضای نام، بخواهید تک‌تک Podها یا کانتینرهای درون آن‌ها را محدود کنید. برای چنین محدودسازی‌ای از یک
[LimitRange](/docs/concepts/policy/limit-range/) استفاده کنید.

{{< note >}}
هنگام استفاده از [تغییر اندازهٔ درجای Pod](/docs/tasks/configure-pod-container/resize-container-resources/)،
اعمال ResourceQuota روی مقادیر تغییریافته انجام می‌شود. اگر تغییر اندازه باعث شود فضای نام از حدهای سهمیهٔ خود فراتر رود،
تغییر اندازه رد می‌شود و منابع Pod بدون تغییر باقی می‌مانند.
{{< /note >}}

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace quota-mem-cpu-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینهٔ حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینهٔ CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

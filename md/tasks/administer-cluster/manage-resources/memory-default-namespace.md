---
title: پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام
content_type: task
weight: 10
description: >-
  برای یک فضای نام، محدودیت پیش‌فرض منبع حافظه تعریف کنید تا هر Pod جدید
  در آن فضای نام، محدودیت منبع حافظهٔ پیکربندی‌شده داشته باشد.
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان درخواست‌ها و محدودیت‌های پیش‌فرض حافظه را برای یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} (namespace) پیکربندی کرد.

یک کلاستر کوبرنتیز را می‌توان به چند فضای نام تقسیم کرد. اگر فضای نامی داشته باشید که
[محدودیت](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits)
پیش‌فرض حافظه برای آن تعیین شده است و سپس بخواهید Podای ایجاد کنید که کانتینر آن محدودیت
حافظهٔ خود را مشخص نکرده است،
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} محدودیت پیش‌فرض
حافظه را به آن کانتینر اختصاص می‌دهد.

کوبرنتیز در شرایط خاصی که در ادامهٔ این مبحث توضیح داده می‌شود، یک درخواست پیش‌فرض حافظه نیز اختصاص می‌دهد.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

باید دسترسی لازم برای ایجاد فضای نام در کلاستر خود را داشته باشید.

هر نود در کلاستر شما باید دست‌کم ۲ GiB حافظه داشته باشد.



<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین ایجاد می‌کنید از بقیهٔ کلاستر
جدا باشند.

```shell
kubectl create namespace default-mem-example
```

## ایجاد یک LimitRange و یک Pod

در ادامه، مانیفست یک {{< glossary_tooltip text="LimitRange" term_id="limitrange" >}} نمونه آمده است.
این مانیفست یک درخواست پیش‌فرض حافظه و یک محدودیت پیش‌فرض حافظه را مشخص می‌کند.

{{% code_sample file="admin/resource/memory-defaults.yaml" %}}

این LimitRange را در فضای نام default-mem-example ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults.yaml --namespace=default-mem-example
```

اکنون اگر در فضای نام default-mem-example یک Pod ایجاد کنید و هر یک از کانتینرهای
آن Pod مقادیر درخواست و محدودیت حافظهٔ خود را مشخص نکرده باشد،
{{< glossary_tooltip text="control plane" term_id="control-plane" >}}
مقادیر پیش‌فرض را اعمال می‌کند: درخواست حافظهٔ 256MiB و محدودیت حافظهٔ 512MiB.


در ادامه، مانیفست نمونهٔ یک Pod با یک کانتینر آمده است. این کانتینر
درخواست و محدودیت حافظه را مشخص نمی‌کند.

{{% code_sample file="admin/resource/memory-defaults-pod.yaml" %}}

Pod را ایجاد کنید.

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod.yaml --namespace=default-mem-example
```

اطلاعات جزئی Pod را مشاهده کنید:

```shell
kubectl get pod default-mem-demo --output=yaml --namespace=default-mem-example
```

خروجی نشان می‌دهد که کانتینر Pod درخواست حافظهٔ 256 MiB و محدودیت حافظهٔ 512 MiB
دارد. این‌ها همان مقادیر پیش‌فرضی هستند که LimitRange مشخص کرده است.

```shell
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-mem-demo-ctr
  resources:
    limits:
      memory: 512Mi
    requests:
      memory: 256Mi
```

Pod خود را حذف کنید:

```shell
kubectl delete pod default-mem-demo --namespace=default-mem-example
```

## اگر محدودیت کانتینر را مشخص کنید اما درخواست آن را مشخص نکنید، چه می‌شود؟

در ادامه، مانیفست یک Pod با یک کانتینر آمده است. این کانتینر
محدودیت حافظه را مشخص می‌کند، اما درخواست را مشخص نمی‌کند:

{{% code_sample file="admin/resource/memory-defaults-pod-2.yaml" %}}

Pod را ایجاد کنید:


```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-2.yaml --namespace=default-mem-example
```

اطلاعات جزئی Pod را مشاهده کنید:

```shell
kubectl get pod default-mem-demo-2 --output=yaml --namespace=default-mem-example
```

خروجی نشان می‌دهد که درخواست حافظهٔ کانتینر برابر با محدودیت حافظهٔ آن تنظیم شده است.
توجه کنید که مقدار پیش‌فرض درخواست حافظه، یعنی 256Mi، به کانتینر اختصاص داده نشده است.

```
resources:
  limits:
    memory: 1Gi
  requests:
    memory: 1Gi
```

## اگر درخواست کانتینر را مشخص کنید اما محدودیت آن را مشخص نکنید، چه می‌شود؟

در ادامه، مانیفست یک Pod با یک کانتینر آمده است. این کانتینر
درخواست حافظه را مشخص می‌کند، اما محدودیت را مشخص نمی‌کند:

{{% code_sample file="admin/resource/memory-defaults-pod-3.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-3.yaml --namespace=default-mem-example
```

مشخصات Pod را مشاهده کنید:

```shell
kubectl get pod default-mem-demo-3 --output=yaml --namespace=default-mem-example
```

خروجی نشان می‌دهد که درخواست حافظهٔ کانتینر برابر با مقداری تنظیم شده است که در
مانیفست کانتینر مشخص شده است. کانتینر مجاز است حداکثر 512MiB حافظه مصرف کند
که با محدودیت پیش‌فرض حافظه برای این فضای نام مطابقت دارد.

```
resources:
  limits:
    memory: 512Mi
  requests:
    memory: 128Mi
```

{{< note >}}

هر `LimitRange` سازگاری مقادیر پیش‌فرضی را که اعمال می‌کند بررسی **نمی‌کند**. یعنی ممکن است مقدار پیش‌فرض _محدودیت_ که `LimitRange` تعیین می‌کند، کمتر از مقدار _درخواست_ باشد که کلاینت در مشخصات کانتینر به API server ارسال کرده است. در این صورت، Pod نهایی قابل زمان‌بندی نخواهد بود.
برای جزئیات بیشتر، [محدودیت‌های مربوط به محدودیت‌ها و درخواست‌های منابع](/docs/concepts/policy/limit-range/#constraints-on-resource-limits-and-requests) را ببینید.

{{< /note >}}


## انگیزهٔ تعیین محدودیت‌ها و درخواست‌های پیش‌فرض حافظه

اگر برای فضای نام شما یک {{< glossary_tooltip text="سهمیهٔ منبع" term_id="resource-quota" >}} (resource quota)
برای حافظه پیکربندی شده باشد،
بهتر است یک مقدار پیش‌فرض برای محدودیت حافظه نیز تعیین شده باشد.
در ادامه سه مورد از محدودیت‌هایی که سهمیهٔ منبع بر یک فضای نام اعمال می‌کند آمده است:

* برای هر Pod که در فضای نام اجرا می‌شود، خود Pod و تک‌تک کانتینرهای آن باید محدودیت حافظه داشته باشند.
  (اگر برای همهٔ کانتینرهای یک Pod محدودیت حافظه مشخص کنید، کوبرنتیز می‌تواند با جمع‌زدن محدودیت‌های
  کانتینرها، محدودیت حافظه در سطح Pod را استنتاج کند).
* محدودیت‌های حافظه، روی نودی که Pod موردنظر روی آن زمان‌بندی شده است، منبع رزرو می‌کنند.
  مجموع حافظهٔ رزروشده برای همهٔ Podهای فضای نام نباید از یک حد مشخص بیشتر شود.
* مجموع حافظه‌ای که همهٔ Podهای فضای نام واقعاً مصرف می‌کنند نیز نباید از یک حد مشخص بیشتر شود.

هنگامی که یک LimitRange اضافه می‌کنید:

اگر هر Podای در آن فضای نام که کانتینری دارد، محدودیت حافظهٔ خود را مشخص نکند،
control plane محدودیت پیش‌فرض حافظه را به آن کانتینر اعمال می‌کند و آن Pod می‌تواند
در فضای نامی که با یک ResourceQuota حافظه محدود شده است اجرا شود.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace default-mem-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

### برای توسعه‌دهندگان برنامه

* [اختصاص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [اختصاص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [اختصاص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

---
title: تخصیص منابع CPU و حافظه در سطح Pod
content_type: task
weight: 30
min-kubernetes-server-version: 1.34
---


<!-- overview -->

{{< feature-state feature_gate_name="PodLevelResources" >}}

این صفحه نشان می‌دهد که چگونه می‌توانید علاوه بر مشخص‌کردن منابع در سطح کانتینر، منابع CPU و حافظه را برای یک Pod در سطح خودِ Pod نیز تعیین کنید. هر نود کوبرنتیز منابع را بر اساس درخواست‌های منابع (resource requests) یک پاد به آن تخصیص می‌دهد. این درخواست‌ها را می‌توان در سطح پاد یا به‌طور جداگانه برای هر یک از کانتینرهای درون پاد تعریف کرد. اگر هر دو تعریف شده باشند، درخواست‌های سطح پاد اولویت دارند.

به همین ترتیب، مصرف منابع یک پاد با محدودیت‌ها (limits) کنترل می‌شود. محدودیت‌ها را نیز می‌توان در سطح پاد یا به‌طور جداگانه برای کانتینرهای درون پاد تنظیم کرد و در این حالت هم، اگر هر دو وجود داشته باشند، محدودیت‌های سطح پاد اولویت دارند. این رویکرد مدیریت منابع را انعطاف‌پذیر می‌کند و به شما امکان می‌دهد تخصیص منابع را هم در سطح پاد و هم در سطح کانتینر کنترل کنید.

برای مشخص‌کردن منابع در سطح پاد، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `PodLevelResources` را فعال کنید.

درباره‌ی منابع سطح پاد:
* اولویت: اگر منابع هم در سطح پاد و هم در سطح کانتینر مشخص شده باشند، منابع سطح پاد اولویت دارند.
* کیفیت سرویس (QoS): منابع سطح پاد در تعیین کلاس QoS پاد اولویت دارند.
* امتیاز OOM: در محاسبه‌ی تنظیم امتیاز OOM، هم منابع سطح پاد و هم منابع سطح کانتینر در نظر گرفته می‌شوند.
* سازگاری: منابع سطح پاد به‌گونه‌ای طراحی شده‌اند که با قابلیت‌های موجود سازگار باشند.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `PodLevelResources` باید برای control plane و برای همه‌ی نودهای کلاستر شما فعال باشد.

## محدودیت‌ها

در کوبرنتیز {{< skew currentVersion >}}، منابع سطح پاد محدودیت‌های زیر را دارند:

* **انواع منابع:** فقط منابع CPU، حافظه و hugepages را می‌توان در سطح پاد مشخص کرد.
* **سیستم‌عامل:** منابع سطح پاد برای پادهای ویندوزی پشتیبانی نمی‌شوند.
* **مدیران منابع:** اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `PodLevelResourceManagers` فعال باشد، Topology Manager و Memory Manager و CPU Manager از منابع سطح پاد پشتیبانی می‌کنند. برای جزئیات بیشتر، [مدیران منابع سطح پاد](/docs/concepts/resource-management/resource-managers/#pod-level-resource-managers) را ببینید. اگر این feature gate فعال نباشد، این مدیران پادها و کانتینرها را بر اساس منابع سطح پاد هم‌تراز نمی‌کنند.
* **تغییر اندازه‌ی درجا:** [تغییر اندازه‌ی درجا](/docs/tasks/configure-pod-container/resize-container-resources/)ی منابع سطح پاد به feature gate با نام `InPlacePodLevelResourcesVerticalScaling` نیاز دارد که در کوبرنتیز {{< skew currentVersion >}} در وضعیت آلفا است. برای جزئیات بیشتر، [تغییر اندازه‌ی منابع CPU و حافظه‌ی Pod](/docs/tasks/configure-pod-container/resize-pod-resources/) را ببینید.

<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام (namespace) ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیه‌ی کلاستر شما جدا بمانند.

```shell
kubectl create namespace pod-resources-example
```

## ایجاد پادی با درخواست و محدودیت حافظه در سطح پاد

برای مشخص‌کردن درخواست حافظه برای یک Pod در سطح پاد، فیلد `resources.requests.memory` را در مانیفست مشخصات Pod قرار دهید. برای مشخص‌کردن محدودیت حافظه نیز `resources.limits.memory` را اضافه کنید.

در این تمرین، پادی با یک کانتینر ایجاد می‌کنید. این پاد درخواست حافظه‌ی ۱۰۰ MiB و محدودیت حافظه‌ی ۲۰۰ MiB دارد. فایل پیکربندی Pod در ادامه آمده است:

{{% code_sample file="pods/resource/pod-level-memory-request-limit.yaml" %}}

بخش `args` در مانیفست، آرگومان‌هایی را که کانتینر هنگام شروع به کار دریافت می‌کند فراهم می‌کند. آرگومان‌های `"--vm-bytes", "150M"` به کانتینر می‌گویند که تلاش کند ۱۵۰ MiB حافظه تخصیص دهد.

پاد را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-memory-request-limit.yaml --namespace=pod-resources-example
```

بررسی کنید که پاد در حال اجرا باشد:

```shell
kubectl get pod memory-demo --namespace=pod-resources-example
```

اطلاعات دقیق پاد را مشاهده کنید:

```shell
kubectl get pod memory-demo --output=yaml --namespace=pod-resources-example
```

خروجی نشان می‌دهد که پاد درخواست حافظه‌ی ۱۰۰ MiB و محدودیت حافظه‌ی ۲۰۰ MiB دارد.


```yaml
...
spec:
  containers:
  ...
  resources:
    requests:
      memory: 100Mi
    limits:
      memory: 200Mi
...
```

برای دریافت معیارهای (metrics) پاد، دستور `kubectl top` را اجرا کنید:

```shell
kubectl top pod memory-demo --namespace=pod-resources-example
```

خروجی نشان می‌دهد که پاد حدود ۱۶۲٬۹۰۰٬۰۰۰ بایت حافظه، یعنی تقریباً ۱۵۰ MiB، مصرف می‌کند. این مقدار از درخواست ۱۰۰ MiB پاد بیشتر است، اما از محدودیت ۲۰۰ MiB آن فراتر نمی‌رود.

```
NAME                        CPU(cores)   MEMORY(bytes)
memory-demo                 <something>  162856960
```

## ایجاد پادی با درخواست و محدودیت CPU در سطح پاد
برای مشخص‌کردن درخواست CPU برای یک Pod، فیلد `resources.requests.cpu` را در مانیفست مشخصات Pod قرار دهید. برای مشخص‌کردن محدودیت CPU نیز `resources.limits.cpu` را اضافه کنید.

در این تمرین، پادی با یک کانتینر ایجاد می‌کنید. این پاد درخواست ۰٫۵ CPU و محدودیت ۱ CPU دارد. فایل پیکربندی Pod در ادامه آمده است:

{{% code_sample file="pods/resource/pod-level-cpu-request-limit.yaml" %}}

بخش `args` در فایل پیکربندی، آرگومان‌هایی را که کانتینر هنگام شروع به کار دریافت می‌کند فراهم می‌کند. آرگومان `-cpus "2"` به کانتینر می‌گوید که تلاش کند از ۲ CPU استفاده کند.

پاد را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-cpu-request-limit.yaml --namespace=pod-resources-example
```

بررسی کنید که پاد در حال اجرا باشد:

```shell
kubectl get pod cpu-demo --namespace=pod-resources-example
```

اطلاعات دقیق پاد را مشاهده کنید:

```shell
kubectl get pod cpu-demo --output=yaml --namespace=pod-resources-example
```

خروجی نشان می‌دهد که پاد درخواست CPU برابر با ۵۰۰ میلی‌CPU و محدودیت CPU برابر با ۱ CPU دارد.

```yaml
spec:
  containers:
  ...
  resources:
    limits:
      cpu: "1"
    requests:
      cpu: 500m
```

برای دریافت معیارهای پاد، از `kubectl top` استفاده کنید:

```shell
kubectl top pod cpu-demo --namespace=pod-resources-example
```

این خروجی نمونه نشان می‌دهد که پاد ۹۷۴ میلی‌CPU مصرف می‌کند که اندکی کمتر از محدودیت ۱ CPU تعیین‌شده در پیکربندی پاد است.

```
NAME                        CPU(cores)   MEMORY(bytes)
cpu-demo                    974m         <something>
```

به یاد داشته باشید که با تنظیم `-cpu "2"`، کانتینر را طوری پیکربندی کردید که تلاش کند از ۲ CPU استفاده کند، اما کانتینر تنها اجازه دارد حدود ۱ CPU مصرف کند. مصرف CPU کانتینر محدود (throttle) می‌شود، زیرا کانتینر تلاش می‌کند بیش از محدودیت CPU پاد از منابع CPU استفاده کند.

## ایجاد پادی با درخواست و محدودیت منابع هم در سطح پاد و هم در سطح کانتینر

برای تخصیص منابع CPU و حافظه به یک Pod، می‌توانید آن‌ها را هم در سطح پاد و هم در سطح کانتینر مشخص کنید. برای تعریف منابع کل پاد، فیلد `resources` را در مشخصات Pod قرار دهید. همچنین برای تعیین نیازمندی‌های منابع مخصوص هر کانتینر، فیلد `resources` را درون مشخصات آن کانتینر در مانیفست Pod اضافه کنید.

در این تمرین، پادی با دو کانتینر ایجاد می‌کنید تا تعامل میان مشخصات منابع سطح پاد و سطح کانتینر را بررسی کنید. خودِ پاد درخواست‌ها و محدودیت‌های CPU تعریف‌شده دارد، در حالی که فقط یکی از کانتینرها درخواست‌ها و محدودیت‌های منابع صریح خودش را دارد. کانتینر دیگر محدودیت‌های منابع را از تنظیمات سطح پاد به ارث می‌برد. فایل پیکربندی Pod در ادامه آمده است:

{{% code_sample file="pods/resource/pod-level-resources.yaml" %}}

پاد را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-resources.yaml --namespace=pod-resources-example
```

بررسی کنید که کانتینر پاد در حال اجرا باشد:

```shell
kubectl get pod pod-resources-demo --namespace=pod-resources-example
```

اطلاعات دقیق پاد را مشاهده کنید:

```shell
kubectl get pod pod-resources-demo --output=yaml --namespace=pod-resources-example
```

خروجی نشان می‌دهد که یکی از کانتینرهای پاد درخواست حافظه‌ی ۵۰ MiB و درخواست CPU برابر با ۰٫۵ هسته، و محدودیت حافظه‌ی ۱۰۰ MiB و محدودیت CPU برابر با ۰٫۵ هسته دارد. خودِ پاد درخواست حافظه‌ی ۱۰۰ MiB و درخواست CPU برابر با ۱ هسته، و محدودیت حافظه‌ی ۲۰۰ MiB و محدودیت CPU برابر با ۱ هسته دارد.

```yaml
...
  containers:
  -
    name: pod-resources-demo-ctr-1
    resources:
      limits:
        cpu: 500m
        memory: 100Mi
      requests:
        cpu: 500m
        memory: 50Mi
...
  -
    name: pod-resources-demo-ctr-2
    resources: {}
...
  resources:
    limits:
      cpu: "1"
      memory: 200Mi
    requests:
      cpu: "1"
      memory: 100Mi
...
```

از آنجا که درخواست‌ها و محدودیت‌های سطح پاد مشخص شده‌اند، منابع تضمین‌شده برای هر دو کانتینر پاد در مجموع برابر با ۱ هسته‌ی CPU و ۱۰۰Mi حافظه خواهد بود. علاوه بر این، دو کانتینر روی هم نمی‌توانند بیش از محدودیت‌های سطح پاد از منابع استفاده کنند؛ بنابراین مجموع مصرف آن‌ها از ۲۰۰ MiB حافظه و ۱ هسته‌ی CPU فراتر نخواهد رفت.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace pod-resources-example
```

## {{% heading "whatsnext" %}}


### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و پادها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و پادها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینه‌ی حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینه‌ی CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [مدیران منابع سطح پاد](/docs/concepts/resource-management/resource-managers/#pod-level-resource-managers)

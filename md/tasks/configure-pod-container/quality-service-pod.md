---
title: پیکربندی کیفیت سرویس برای Podها
content_type: task
weight: 60
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه Podها را طوری پیکربندی کنید که
{{< glossary_tooltip text="کلاس‌های کیفیت سرویس (QoS)" term_id="qos-class" >}} مشخصی به آن‌ها اختصاص یابد.
کوبرنتیز از کلاس‌های QoS برای تصمیم‌گیری دربارهٔ بیرون‌راندن (evict) Podها در زمانی استفاده می‌کند که مصرف منابع نود از حد مجاز فراتر رود.


کوبرنتیز هنگام ایجاد یک Pod، یکی از کلاس‌های QoS زیر را به آن اختصاص می‌دهد:

* [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
* [Burstable](/docs/concepts/workloads/pods/pod-qos/#burstable)
* [BestEffort](/docs/concepts/workloads/pods/pod-qos/#besteffort)

{{< note >}}
کوبرنتیز کلاس QoS را هنگام ایجاد Pod اختصاص می‌دهد و این کلاس در تمام طول عمر Pod بدون تغییر باقی می‌ماند.
اگر بخواهید [منابع Pod را تغییر اندازه دهید](/docs/tasks/configure-pod-container/resize-container-resources/)
و مقادیر جدید به کلاس QoS متفاوتی منجر شوند، control plane درخواست شما را با یک پیام خطا رد می‌کند.
{{< /note >}}


## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

همچنین باید بتوانید فضاهای نام (namespace) را ایجاد و حذف کنید.



<!-- steps -->


## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیهٔ کلاستر شما جدا بمانند.

```shell
kubectl create namespace qos-example
```

## ایجاد یک Pod با کلاس QoS از نوع Guaranteed

برای اینکه کلاس QoS یک Pod از نوع `Guaranteed` باشد:

* هر کانتینر در Pod باید یک حد (limit) حافظه و یک درخواست (request) حافظه داشته باشد.
* برای هر کانتینر در Pod، حد حافظه باید با درخواست حافظه برابر باشد.
* هر کانتینر در Pod باید یک حد CPU و یک درخواست CPU داشته باشد.
* برای هر کانتینر در Pod، حد CPU باید با درخواست CPU برابر باشد.

این محدودیت‌ها به‌طور یکسان برای کانتینرهای init و کانتینرهای برنامه اعمال می‌شوند.
[کانتینرهای موقت](/docs/concepts/workloads/pods/ephemeral-containers/)
نمی‌توانند منابع تعریف کنند، بنابراین این محدودیت‌ها شامل آن‌ها نمی‌شود.

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر یک حد حافظه و یک درخواست حافظه دارد
که هر دو برابر با 200 MiB هستند. همچنین یک حد CPU و یک درخواست CPU دارد که هر دو برابر با 700 میلی‌CPU هستند:

{{% code_sample file="pods/qos/qos-pod.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod.yaml --namespace=qos-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod qos-demo --namespace=qos-example --output=yaml
```

خروجی نشان می‌دهد که کوبرنتیز کلاس QoS از نوع `Guaranteed` را به Pod داده است. خروجی همچنین
تأیید می‌کند که درخواست حافظهٔ کانتینر Pod با حد حافظهٔ آن و درخواست CPU آن با حد CPU آن برابر است.

```yaml
spec:
  containers:
    ...
    resources:
      limits:
        cpu: 700m
        memory: 200Mi
      requests:
        cpu: 700m
        memory: 200Mi
    ...
status:
  qosClass: Guaranteed
```

{{< note >}}
اگر یک کانتینر حد حافظهٔ خود را مشخص کند اما درخواست حافظه را مشخص نکند، کوبرنتیز
به‌طور خودکار یک درخواست حافظه برابر با آن حد اختصاص می‌دهد. به همین ترتیب، اگر یک کانتینر حد CPU
خود را مشخص کند اما درخواست CPU را مشخص نکند، کوبرنتیز به‌طور خودکار یک درخواست CPU برابر با
آن حد اختصاص می‌دهد.
{{< /note >}}

<!-- 4th level heading to suppress entry in nav -->
#### پاک‌سازی {#clean-up-guaranteed}

Pod خود را حذف کنید:

```shell
kubectl delete pod qos-demo --namespace=qos-example
```

## ایجاد یک Pod با کلاس QoS از نوع Burstable

کلاس QoS یک Pod در صورتی `Burstable` است که:

* آن Pod معیارهای کلاس QoS از نوع `Guaranteed` را نداشته باشد.
* دست‌کم یکی از کانتینرهای Pod درخواست یا حد حافظه یا CPU داشته باشد.

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر حد حافظهٔ 200 MiB
و درخواست حافظهٔ 100 MiB دارد.

{{% code_sample file="pods/qos/qos-pod-2.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-2.yaml --namespace=qos-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod qos-demo-2 --namespace=qos-example --output=yaml
```

خروجی نشان می‌دهد که کوبرنتیز کلاس QoS از نوع `Burstable` را به Pod داده است:

```yaml
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: qos-demo-2-ctr
    resources:
      limits:
        memory: 200Mi
      requests:
        memory: 100Mi
  ...
status:
  qosClass: Burstable
```

<!-- 4th level heading to suppress entry in nav -->
#### پاک‌سازی {#clean-up-burstable}

Pod خود را حذف کنید:

```shell
kubectl delete pod qos-demo-2 --namespace=qos-example
```

## ایجاد یک Pod با کلاس QoS از نوع BestEffort

برای اینکه کلاس QoS یک Pod از نوع `BestEffort` باشد، کانتینرهای آن Pod نباید
هیچ حد یا درخواست حافظه یا CPU داشته باشند.

در ادامه مانیفست یک Pod با یک کانتینر آمده است. این کانتینر هیچ حد یا درخواست حافظه یا CPU
ندارد:

{{% code_sample file="pods/qos/qos-pod-3.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-3.yaml --namespace=qos-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod qos-demo-3 --namespace=qos-example --output=yaml
```

خروجی نشان می‌دهد که کوبرنتیز کلاس QoS از نوع `BestEffort` را به Pod داده است:

```yaml
spec:
  containers:
    ...
    resources: {}
  ...
status:
  qosClass: BestEffort
```

<!-- 4th level heading to suppress entry in nav -->
#### پاک‌سازی {#clean-up-besteffort}

Pod خود را حذف کنید:

```shell
kubectl delete pod qos-demo-3 --namespace=qos-example
```

## ایجاد یک Pod با دو کانتینر

در ادامه مانیفست یک Pod با دو کانتینر آمده است. یکی از کانتینرها درخواست حافظهٔ
200 MiB را مشخص می‌کند و کانتینر دیگر هیچ درخواست یا حدی مشخص نمی‌کند.

{{% code_sample file="pods/qos/qos-pod-4.yaml" %}}

توجه کنید که این Pod معیارهای کلاس QoS از نوع `Burstable` را دارد؛ یعنی معیارهای
کلاس QoS از نوع `Guaranteed` را ندارد و یکی از کانتینرهایش درخواست حافظه دارد.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-4.yaml --namespace=qos-example
```

اطلاعات تفصیلی Pod را مشاهده کنید:

```shell
kubectl get pod qos-demo-4 --namespace=qos-example --output=yaml
```

خروجی نشان می‌دهد که کوبرنتیز کلاس QoS از نوع `Burstable` را به Pod داده است:

```yaml
spec:
  containers:
    ...
    name: qos-demo-4-ctr-1
    resources:
      requests:
        memory: 200Mi
    ...
    name: qos-demo-4-ctr-2
    resources: {}
    ...
status:
  qosClass: Burstable
```

## دریافت کلاس QoS یک Pod

به‌جای مشاهدهٔ همهٔ فیلدها، می‌توانید فقط فیلد مورد نیاز خود را ببینید:

```bash
kubectl --namespace=qos-example get pod qos-demo-4 -o jsonpath='{ .status.qosClass}{"\n"}'
```

```none
Burstable
```


## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace qos-example
```



## {{% heading "whatsnext" %}}



### برای توسعه‌دهندگان برنامه

* [اختصاص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [اختصاص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و حدهای پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینهٔ حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های کمینه و بیشینهٔ CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیهٔ Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

* [کنترل سیاست‌های مدیریت توپولوژی روی یک نود](/docs/tasks/administer-cluster/topology-manager/)

---
title: تخصیص منابع توسعه‌یافته به یک کانتینر
content_type: task
weight: 70
---

<!-- overview -->

{{< feature-state state="stable" >}}

این صفحه نشان می‌دهد که چگونه می‌توانید منابع توسعه‌یافته (extended resources) را به یک کانتینر تخصیص دهید.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

پیش از انجام این تمرین، تمرین
[اعلام منابع توسعه‌یافته برای یک نود](/docs/tasks/administer-cluster/extended-resource-node/) را انجام دهید.
با انجام آن تمرین، یکی از نودهای شما طوری پیکربندی می‌شود که یک منبع dongle را اعلام کند.




<!-- steps -->

## تخصیص یک منبع توسعه‌یافته به یک Pod

برای درخواست یک منبع توسعه‌یافته، فیلد `resources.requests.<resource_name>` را
در مانیفست کانتینر قرار دهید.
`*.kubernetes.io/`. نام‌های معتبر منابع توسعه‌یافته به شکل `example.com/foo` هستند که در آن
به جای `example.com` دامنهٔ سازمان شما و به جای `foo` یک نام توصیفی برای منبع قرار می‌گیرد.

فایل پیکربندی یک Pod که یک کانتینر دارد در ادامه آمده است:

{{% code_sample file="pods/resource/extended-resource-pod.yaml" %}}

در این فایل پیکربندی می‌بینید که کانتینر ۳ dongle درخواست می‌کند.

یک Pod ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod.yaml
```

بررسی کنید که Pod در حال اجرا باشد:

```shell
kubectl get pod extended-resource-demo
```

جزئیات Pod را مشاهده کنید:

```shell
kubectl describe pod extended-resource-demo
```

خروجی، درخواست‌های dongle را نشان می‌دهد:

```yaml
Limits:
  example.com/dongle: 3
Requests:
  example.com/dongle: 3
```

## تلاش برای ایجاد Pod دوم

فایل پیکربندی یک Pod که یک کانتینر دارد در ادامه آمده است. این کانتینر
دو dongle درخواست می‌کند.

{{% code_sample file="pods/resource/extended-resource-pod-2.yaml" %}}

کوبرنتیز نمی‌تواند درخواست دو dongle را برآورده کند، زیرا Pod اول
سه dongle از چهار dongle موجود را استفاده کرده است.

برای ایجاد Pod تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod-2.yaml
```

جزئیات Pod را مشاهده کنید:

```shell
kubectl describe pod extended-resource-demo-2
```

خروجی نشان می‌دهد که Pod زمان‌بندی نمی‌شود، زیرا هیچ نودی وجود ندارد که
۲ dongle در دسترس داشته باشد:


```
Conditions:
  Type    Status
  PodScheduled  False
...
Events:
  ...
  ... Warning   FailedScheduling  pod (extended-resource-demo-2) failed to fit in any node
fit failure summary on nodes : Insufficient example.com/dongle (1)
```

وضعیت Pod را مشاهده کنید:

```shell
kubectl get pod extended-resource-demo-2
```

خروجی نشان می‌دهد که Pod ایجاد شده، اما برای اجرا روی هیچ نودی زمان‌بندی نشده است.
وضعیت آن Pending است:

```yaml
NAME                       READY     STATUS    RESTARTS   AGE
extended-resource-demo-2   0/1       Pending   0          6m
```

## پاک‌سازی

Podهایی را که برای این تمرین ایجاد کرده‌اید حذف کنید:

```shell
kubectl delete pod extended-resource-demo
kubectl delete pod extended-resource-demo-2
```

## منابع توسعه‌یافته مبتنی بر DRA

{{< feature-state feature_gate_name="DRAExtendedResource" >}}

تمرین بالا از یک منبع توسعه‌یافته استفاده می‌کند که یک نود آن را اعلام می‌کند. منابع
توسعه‌یافته را می‌توان با
{{< glossary_tooltip text="تخصیص پویای منابع" term_id="dra" >}} (DRA) نیز فراهم کرد:
در این حالت، یک DeviceClass مقدار `extendedResourceName` را تعیین می‌کند و زمان‌بند
درخواست‌های منطبق برای منابع توسعه‌یافته را به جای ظرفیت اعلام‌شده توسط نود، با دستگاه‌های DRA برآورده می‌کند.

یک Pod در هر دو حالت منبع را به یک شکل درخواست می‌کند، یعنی از طریق
`resources.requests.<resource_name>`؛ بنابراین بار کاری نیازی ندارد بداند که این منبع را
یک افزونهٔ دستگاه (device plugin) فراهم می‌کند یا DRA. حتی ممکن است یک نام منبع واحد روی برخی نودها
با افزونهٔ دستگاه و روی نودهای دیگر با DRA فراهم شود.

برای راه‌اندازی DeviceClass و دیدن نمونه‌ها، به
[تخصیص منابع توسعه‌یافته با DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#extended-resource) مراجعه کنید.

## {{% heading "whatsnext" %}}


### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)
* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

### برای مدیران کلاستر

* [اعلام منابع توسعه‌یافته برای یک نود](/docs/tasks/administer-cluster/extended-resource-node/)

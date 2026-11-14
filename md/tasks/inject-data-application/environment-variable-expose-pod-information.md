---
title: نمایش اطلاعات Pod به کانتینرها از طریق متغیرهای محیطی
content_type: task
weight: 30
---

<!-- overview -->

این صفحه نشان می‌دهد که یک Pod چگونه می‌تواند با استفاده از _downward API_ و از طریق متغیرهای محیطی، اطلاعاتی دربارهٔ خودش را در اختیار کانتینرهایی بگذارد که در آن Pod اجرا می‌شوند.
با متغیرهای محیطی می‌توانید فیلدهای Pod، فیلدهای کانتینر یا هر دو را در دسترس قرار دهید.

در کوبرنتیز، دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر برای یک کانتینر در حال اجرا وجود دارد:

* _متغیرهای محیطی_، همان‌طور که در این تمرین توضیح داده شده است
* [فایل‌های حجم (volume)](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

این دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر، روی هم downward API نامیده می‌شوند.

از آنجا که Serviceها اصلی‌ترین راه ارتباط میان برنامه‌های کانتینری‌شده‌ای هستند که کوبرنتیز آن‌ها را مدیریت می‌کند، بهتر است بتوان آن‌ها را در زمان اجرا کشف کرد.

دربارهٔ دسترسی به Serviceها [اینجا](/docs/tutorials/services/connect-applications-service/#accessing-the-service) بیشتر بخوانید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## استفاده از فیلدهای Pod به‌عنوان مقدار متغیرهای محیطی

در این بخش از تمرین، یک Pod با یک کانتینر ایجاد می‌کنید و فیلدهای سطح Pod را به‌صورت متغیرهای محیطی در کانتینر در حال اجرا قرار می‌دهید.

{{% code_sample file="pods/inject/dapi-envars-pod.yaml" %}}

در این مانیفست، پنج متغیر محیطی را می‌بینید. فیلد `env` آرایه‌ای از تعریف‌های متغیرهای محیطی است.
نخستین عنصر این آرایه مشخص می‌کند که متغیر محیطی `MY_NODE_NAME` مقدار خود را از فیلد `spec.nodeName` در Pod می‌گیرد. به همین ترتیب، سایر متغیرهای محیطی نیز نام‌های خود را از فیلدهای Pod می‌گیرند.

{{< note >}}
فیلدهای این مثال، فیلدهای Pod هستند و فیلدهای کانتینرِ درون Pod به شمار نمی‌آیند.
{{< /note >}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-pod.yaml
```

بررسی کنید که کانتینر درون Pod در حال اجرا باشد:

```shell
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

لاگ‌های کانتینر را مشاهده کنید:

```shell
kubectl logs dapi-envars-fieldref
```

خروجی، مقادیر متغیرهای محیطی انتخاب‌شده را نشان می‌دهد:

```
minikube
dapi-envars-fieldref
default
172.17.0.4
default
```

برای اینکه ببینید چرا این مقادیر در لاگ آمده‌اند، به فیلدهای `command` و `args` در فایل پیکربندی نگاه کنید. هنگامی که کانتینر شروع به کار می‌کند، مقادیر پنج متغیر محیطی را در stdout می‌نویسد و این کار را هر ده ثانیه یک‌بار تکرار می‌کند.

سپس، یک شل در کانتینری که در Pod شما اجرا می‌شود باز کنید:

```shell
kubectl exec -it dapi-envars-fieldref -- sh
```

در شل خود، متغیرهای محیطی را مشاهده کنید:

```shell
# Run this in a shell inside the container
printenv
```

خروجی نشان می‌دهد که مقادیر فیلدهای Pod به برخی از متغیرهای محیطی اختصاص داده شده است:

```
MY_POD_SERVICE_ACCOUNT=default
...
MY_POD_NAMESPACE=default
MY_POD_IP=172.17.0.4
...
MY_NODE_NAME=minikube
...
MY_POD_NAME=dapi-envars-fieldref
```

## استفاده از فیلدهای کانتینر به‌عنوان مقدار متغیرهای محیطی

در تمرین قبل، از اطلاعات فیلدهای سطح Pod به‌عنوان مقدار متغیرهای محیطی استفاده کردید.
در تمرین بعدی، فیلدهایی را منتقل می‌کنید که بخشی از تعریف Pod هستند، اما به‌جای کل Pod، از یک [کانتینر](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) مشخص گرفته می‌شوند.

در ادامه، مانیفست Pod دیگری آمده است که این بار نیز تنها یک کانتینر دارد:

{{% code_sample file="pods/inject/dapi-envars-container.yaml" %}}

در این مانیفست، چهار متغیر محیطی را می‌بینید. فیلد `env` آرایه‌ای از تعریف‌های متغیرهای محیطی است.
نخستین عنصر این آرایه مشخص می‌کند که متغیر محیطی `MY_CPU_REQUEST` مقدار خود را از فیلد `requests.cpu` در کانتینری به نام `test-container` می‌گیرد. به همین ترتیب، سایر متغیرهای محیطی نیز مقادیر خود را از فیلدهایی می‌گیرند که مختص همین کانتینر هستند.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-container.yaml
```

بررسی کنید که کانتینر درون Pod در حال اجرا باشد:

```shell
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

لاگ‌های کانتینر را مشاهده کنید:

```shell
kubectl logs dapi-envars-resourcefieldref
```

خروجی، مقادیر متغیرهای محیطی انتخاب‌شده را نشان می‌دهد:

```
1
1
33554432
67108864
```

## {{% heading "whatsnext" %}}


* [تعریف متغیرهای محیطی برای یک کانتینر](/docs/tasks/inject-data-application/define-environment-variable-container/) را بخوانید.
* تعریف API مربوط به [`spec`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec) در Pod را بخوانید.
  این تعریف شامل تعریف Container (بخشی از Pod) نیز هست.
* فهرست [فیلدهای موجود](/docs/concepts/workloads/pods/downward-api/#available-fields) را که می‌توانید با downward API در دسترس قرار دهید، بخوانید.

دربارهٔ Podها، کانتینرها و متغیرهای محیطی در مرجع قدیمی API بخوانید:

* [PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core)
* [Container](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#container-v1-core)
* [EnvVar](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#envvar-v1-core)
* [EnvVarSource](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#envvarsource-v1-core)
* [ObjectFieldSelector](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#objectfieldselector-v1-core)
* [ResourceFieldSelector](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#resourcefieldselector-v1-core)

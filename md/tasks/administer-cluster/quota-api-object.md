---
title: پیکربندی سهمیه‌ها برای آبجکت‌های API
content_type: task
weight: 130
---


<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید برای آبجکت‌های API، از جمله
PersistentVolumeClaimها و Serviceها، سهمیه (quota) پیکربندی کنید. سهمیه تعداد
آبجکت‌هایی از یک نوع مشخص را که می‌توان در یک فضای نام (namespace) ایجاد کرد محدود می‌کند.
سهمیه‌ها را در یک آبجکت
[ResourceQuota](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#resourcequota-v1-core)
مشخص می‌کنید.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}




<!-- steps -->

## ایجاد یک فضای نام

یک فضای نام ایجاد کنید تا منابعی که در این تمرین می‌سازید از بقیه‌ی کلاستر
شما جدا بمانند.

```shell
kubectl create namespace quota-object-example
```

## ایجاد یک ResourceQuota

فایل پیکربندی یک آبجکت ResourceQuota در ادامه آمده است:

{{% code_sample file="admin/resource/quota-objects.yaml" %}}

آبجکت ResourceQuota را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects.yaml --namespace=quota-object-example
```

اطلاعات دقیق ResourceQuota را مشاهده کنید:

```shell
kubectl get resourcequota object-quota-demo --namespace=quota-object-example --output=yaml
```

خروجی نشان می‌دهد که در فضای نام quota-object-example حداکثر یک
PersistentVolumeClaim و حداکثر دو Service از نوع LoadBalancer می‌تواند وجود داشته باشد
و هیچ Service از نوع NodePort مجاز نیست.

```yaml
status:
  hard:
    persistentvolumeclaims: "1"
    services.loadbalancers: "2"
    services.nodeports: "0"
  used:
    persistentvolumeclaims: "0"
    services.loadbalancers: "0"
    services.nodeports: "0"
```

## ایجاد یک PersistentVolumeClaim

فایل پیکربندی یک آبجکت PersistentVolumeClaim در ادامه آمده است:

{{% code_sample file="admin/resource/quota-objects-pvc.yaml" %}}

آبجکت PersistentVolumeClaim را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects-pvc.yaml --namespace=quota-object-example
```

بررسی کنید که PersistentVolumeClaim ایجاد شده باشد:

```shell
kubectl get persistentvolumeclaims --namespace=quota-object-example
```

خروجی نشان می‌دهد که PersistentVolumeClaim وجود دارد و وضعیت آن Pending است:

```
NAME             STATUS
pvc-quota-demo   Pending
```

## تلاش برای ایجاد دومین PersistentVolumeClaim

فایل پیکربندی دومین PersistentVolumeClaim در ادامه آمده است:

{{% code_sample file="admin/resource/quota-objects-pvc-2.yaml" %}}

برای ایجاد دومین PersistentVolumeClaim تلاش کنید:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects-pvc-2.yaml --namespace=quota-object-example
```

خروجی نشان می‌دهد که دومین PersistentVolumeClaim ایجاد نشده است، زیرا
ایجاد آن از سهمیه‌ی فضای نام فراتر می‌رفت.

```
persistentvolumeclaims "pvc-quota-demo-2" is forbidden:
exceeded quota: object-quota-demo, requested: persistentvolumeclaims=1,
used: persistentvolumeclaims=1, limited: persistentvolumeclaims=1
```

## نکته‌ها

رشته‌هایی که برای شناسایی منابع API قابل‌محدودسازی با سهمیه به کار می‌روند
در ادامه آمده‌اند:

<table>
<tr><th>رشته</th><th>آبجکت API</th></tr>
<tr><td>"pods"</td><td>Pod</td></tr>
<tr><td>"services"</td><td>Service</td></tr>
<tr><td>"replicationcontrollers"</td><td>ReplicationController</td></tr>
<tr><td>"resourcequotas"</td><td>ResourceQuota</td></tr>
<tr><td>"secrets"</td><td>Secret</td></tr>
<tr><td>"configmaps"</td><td>ConfigMap</td></tr>
<tr><td>"persistentvolumeclaims"</td><td>PersistentVolumeClaim</td></tr>
<tr><td>"services.nodeports"</td><td>Service از نوع NodePort</td></tr>
<tr><td>"services.loadbalancers"</td><td>Service از نوع LoadBalancer</td></tr>
</table>

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace quota-object-example
```



## {{% heading "whatsnext" %}}


### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیه‌ی Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

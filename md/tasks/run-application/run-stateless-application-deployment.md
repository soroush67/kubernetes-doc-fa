---
title: اجرای یک برنامهٔ بدون حالت با استفاده از Deployment
min-kubernetes-server-version: v1.9
content_type: tutorial
weight: 10
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان یک برنامه را با استفاده از آبجکت Deployment در کوبرنتیز اجرا کرد.

## {{% heading "objectives" %}}

- یک استقرار nginx ایجاد کنید.
- با استفاده از kubectl اطلاعات مربوط به استقرار را فهرست کنید.
- استقرار را به‌روزرسانی کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- lessoncontent -->

## ایجاد و بررسی یک استقرار nginx

برای اجرای یک برنامه می‌توانید یک آبجکت Deployment در کوبرنتیز ایجاد کنید و
مشخصات این Deployment را در یک فایل YAML بنویسید. برای نمونه، فایل YAML زیر
یک Deployment را توصیف می‌کند که ایمیج Docker با نام nginx:1.14.2 را اجرا می‌کند:

{{% code_sample file="application/deployment.yaml" %}}

1. بر اساس فایل YAML یک Deployment ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment.yaml
   ```

1. اطلاعات مربوط به Deployment را نمایش دهید:

   ```shell
   kubectl describe deployment nginx-deployment
   ```

   خروجی مشابه زیر است:

   ```
   Name:     nginx-deployment
   Namespace:    default
   CreationTimestamp:  Tue, 30 Aug 2016 18:11:37 -0700
   Labels:     app=nginx
   Annotations:    deployment.kubernetes.io/revision=1
   Selector:   app=nginx
   Replicas:   2 desired | 2 updated | 2 total | 2 available | 0 unavailable
   StrategyType:   RollingUpdate
   MinReadySeconds:  0
   RollingUpdateStrategy:  1 max unavailable, 1 max surge
   Pod Template:
     Labels:       app=nginx
     Containers:
       nginx:
       Image:              nginx:1.14.2
       Port:               80/TCP
       Environment:        <none>
       Mounts:             <none>
     Volumes:              <none>
   Conditions:
     Type          Status  Reason
     ----          ------  ------
     Available     True    MinimumReplicasAvailable
     Progressing   True    NewReplicaSetAvailable
   OldReplicaSets:   <none>
   NewReplicaSet:    nginx-deployment-1771418926 (2/2 replicas created)
   No events.
   ```

1. Podهایی را که این استقرار ایجاد کرده است فهرست کنید:

   ```shell
   kubectl get pods -l app=nginx
   ```

   خروجی مشابه زیر است:

   ```
   NAME                                READY     STATUS    RESTARTS   AGE
   nginx-deployment-1771418926-7o5ns   1/1       Running   0          16h
   nginx-deployment-1771418926-r18az   1/1       Running   0          16h
   ```

1. اطلاعات مربوط به یک Pod را نمایش دهید:

   ```shell
   kubectl describe pod <pod-name>
   ```

   در این دستور، `<pod-name>` نام یکی از Podهای شماست.

## به‌روزرسانی استقرار

برای به‌روزرسانی استقرار می‌توانید یک فایل YAML جدید را اعمال کنید. فایل YAML
زیر مشخص می‌کند که استقرار باید طوری به‌روزرسانی شود که از nginx 1.16.1 استفاده کند.

{{% code_sample file="application/deployment-update.yaml" %}}

1. فایل YAML جدید را اعمال کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment-update.yaml
   ```

1. مشاهده کنید که استقرار، Podهایی با نام‌های جدید ایجاد می‌کند و Podهای قدیمی را حذف می‌کند:

   ```shell
   kubectl get pods -l app=nginx
   ```

## مقیاس‌دهی برنامه با افزایش تعداد رپلیکاها

با اعمال یک فایل YAML جدید می‌توانید تعداد Podهای Deployment خود را افزایش دهید.
این فایل YAML مقدار `replicas` را برابر با ۴ قرار می‌دهد؛ یعنی Deployment باید
چهار Pod داشته باشد:

{{% code_sample file="application/deployment-scale.yaml" %}}

1. فایل YAML جدید را اعمال کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment-scale.yaml
   ```

1. بررسی کنید که Deployment چهار Pod دارد:

   ```shell
   kubectl get pods -l app=nginx
   ```

   خروجی مشابه زیر است:

   ```
   NAME                               READY     STATUS    RESTARTS   AGE
   nginx-deployment-148880595-4zdqq   1/1       Running   0          25s
   nginx-deployment-148880595-6zgi1   1/1       Running   0          25s
   nginx-deployment-148880595-fxcez   1/1       Running   0          2m
   nginx-deployment-148880595-rwovn   1/1       Running   0          2m
   ```

برای آشنایی با روش‌های دقیق مقیاس‌دهی، از جمله کاهش مقیاس و مقیاس‌دهی تا صفر، به
[مقیاس‌دهی دستی یک Deployment](/docs/tasks/run-application/scale-deployment/) مراجعه کنید.

## حذف یک استقرار

استقرار را با استفاده از نام آن حذف کنید:

```shell
kubectl delete deployment nginx-deployment
```

## ReplicationControllerها؛ روش قدیمی

روش ترجیحی برای ایجاد یک برنامهٔ تکثیرشده، استفاده از Deployment است که خود از
ReplicaSet استفاده می‌کند. پیش از آنکه Deployment و ReplicaSet به کوبرنتیز
افزوده شوند، برنامه‌های تکثیرشده با استفاده از
[ReplicationController](/docs/concepts/workloads/controllers/replicationcontroller/) پیکربندی می‌شدند.

## {{% heading "whatsnext" %}}

- دربارهٔ [آبجکت‌های Deployment](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.
- با نحوهٔ [به‌روزرسانی یک Deployment بدون وقفه در سرویس‌دهی](/docs/tasks/run-application/update-deployment-rolling/) آشنا شوید.

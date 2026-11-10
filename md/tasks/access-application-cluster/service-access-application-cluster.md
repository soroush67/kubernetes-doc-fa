---
title: استفاده از Service برای دسترسی به یک برنامه در کلاستر
content_type: tutorial
weight: 60
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه یک آبجکت Service در کوبرنتیز ایجاد کنید که کلاینت‌های خارجی بتوانند با آن به برنامه‌ای که در یک کلاستر اجرا می‌شود دسترسی پیدا کنند. این Service برای برنامه‌ای که دو نمونهٔ در حال اجرا دارد، توزیع بار (load balancing) فراهم می‌کند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

## {{% heading "objectives" %}}

- دو نمونه از یک برنامهٔ Hello World را اجرا کنید.
- یک آبجکت Service ایجاد کنید که یک پورت نود (node port) را در دسترس قرار دهد.
- با استفاده از آبجکت Service به برنامهٔ در حال اجرا دسترسی پیدا کنید.

<!-- lessoncontent -->

## ایجاد یک Service برای برنامه‌ای که در دو پاد اجرا می‌شود

فایل پیکربندی Deployment برنامه در ادامه آمده است:

{{% code_sample file="service/access/hello-application.yaml" %}}

1. یک برنامهٔ Hello World را در کلاستر خود اجرا کنید:
   با استفاده از فایل بالا، Deployment برنامه را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/service/access/hello-application.yaml
   ```

   دستور بالا یک
   {{< glossary_tooltip text="Deployment" term_id="deployment" >}}
   و یک
   {{< glossary_tooltip term_id="replica-set" text="ReplicaSet" >}}
   مرتبط با آن ایجاد می‌کند. این ReplicaSet دو
   {{< glossary_tooltip text="پاد" term_id="pod" >}}
   دارد که هر کدام برنامهٔ Hello World را اجرا می‌کنند.

1. اطلاعات Deployment را نمایش دهید:

   ```shell
   kubectl get deployments hello-world
   kubectl describe deployments hello-world
   ```

1. اطلاعات آبجکت‌های ReplicaSet خود را نمایش دهید:

   ```shell
   kubectl get replicasets
   kubectl describe replicasets
   ```

1. یک آبجکت Service ایجاد کنید که این Deployment را در دسترس قرار دهد:

   ```shell
   kubectl expose deployment hello-world --type=NodePort --name=example-service
   ```

1. اطلاعات Service را نمایش دهید:

   ```shell
   kubectl describe services example-service
   ```

   خروجی مشابه زیر است:

   ```none
   Name:                   example-service
   Namespace:              default
   Labels:                 run=load-balancer-example
   Annotations:            <none>
   Selector:               run=load-balancer-example
   Type:                   NodePort
   IP:                     10.32.0.16
   Port:                   <unset> 8080/TCP
   TargetPort:             8080/TCP
   NodePort:               <unset> 31496/TCP
   Endpoints:              10.200.1.4:8080,10.200.2.5:8080
   Session Affinity:       None
   Events:                 <none>
   ```

   مقدار NodePort این Service را یادداشت کنید. برای مثال، در خروجی بالا
   مقدار NodePort برابر 31496 است.

1. پادهایی را که برنامهٔ Hello World را اجرا می‌کنند فهرست کنید:

   ```shell
   kubectl get pods --selector="run=load-balancer-example" --output=wide
   ```

   خروجی مشابه زیر است:

   ```none
   NAME                           READY   STATUS    ...  IP           NODE
   hello-world-2895499144-bsbk5   1/1     Running   ...  10.200.1.4   worker1
   hello-world-2895499144-m1pwt   1/1     Running   ...  10.200.2.5   worker2
   ```

1. نشانی IP عمومی یکی از نودهایی را که یک پاد Hello World روی آن اجرا می‌شود
   به دست آورید. روش به دست آوردن این نشانی به نحوهٔ راه‌اندازی کلاستر شما بستگی دارد.
   برای مثال، اگر از Minikube استفاده می‌کنید، می‌توانید با اجرای `kubectl cluster-info`
   نشانی نود را ببینید. اگر از نمونه‌های Google Compute Engine استفاده می‌کنید،
   می‌توانید با دستور `gcloud compute instances list` نشانی‌های عمومی نودهای خود را ببینید.

1. روی نود انتخاب‌شده، یک قانون فایروال ایجاد کنید که ترافیک TCP را روی پورت نود
   مجاز کند. برای مثال، اگر مقدار NodePort سرویس شما 31568 است، یک قانون فایروال
   ایجاد کنید که ترافیک TCP را روی پورت 31568 مجاز کند. ارائه‌دهندگان ابری مختلف
   روش‌های متفاوتی برای پیکربندی قوانین فایروال ارائه می‌دهند.

1. با استفاده از نشانی نود و پورت نود به برنامهٔ Hello World دسترسی پیدا کنید:

   ```shell
   curl http://<public-node-ip>:<node-port>
   ```

   در اینجا `<public-node-ip>` نشانی IP عمومی نود شما و `<node-port>` مقدار
   NodePort سرویس شما است. پاسخ یک درخواست موفق، یک پیام خوشامد است:

   ```none
   Hello, world!
   Version: 2.0.0
   Hostname: hello-world-cdd4458f4-m47c8
   ```

## استفاده از فایل پیکربندی Service

به‌جای استفاده از `kubectl expose`، می‌توانید با یک
[فایل پیکربندی Service](/docs/concepts/services-networking/service/)
یک Service ایجاد کنید.

## {{% heading "cleanup" %}}

برای حذف Service، این دستور را وارد کنید:

    kubectl delete services example-service

برای حذف Deployment، ReplicaSet و پادهایی که برنامهٔ Hello World را اجرا می‌کنند،
این دستور را وارد کنید:

    kubectl delete deployment hello-world

## {{% heading "whatsnext" %}}

آموزش
[اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/)
را دنبال کنید.

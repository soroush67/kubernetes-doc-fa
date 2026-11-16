---
title: در دسترس قرار دادن یک آدرس IP خارجی برای دسترسی به یک برنامه در کلاستر
content_type: tutorial
weight: 10
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک آبجکت Service در کوبرنتیز ایجاد کنید که یک آدرس IP خارجی را در دسترس قرار می‌دهد.

## {{% heading "prerequisites" %}}

* ابزار [kubectl](/docs/tasks/tools/) را نصب کنید.
* برای ایجاد یک کلاستر کوبرنتیز، از یک ارائه‌دهندهٔ ابری مانند Google Kubernetes Engine یا Amazon Web Services استفاده کنید. این آموزش یک
  [متعادل‌کنندهٔ بار خارجی (external load balancer)](/docs/tasks/access-application-cluster/create-external-load-balancer/)
  ایجاد می‌کند که به یک ارائه‌دهندهٔ ابری نیاز دارد.
* ابزار `kubectl` را طوری پیکربندی کنید که با سرور API کوبرنتیز شما ارتباط برقرار کند. برای دستورالعمل‌ها، به مستندات ارائه‌دهندهٔ ابری خود مراجعه کنید.

## {{% heading "objectives" %}}

* پنج نمونه از یک برنامهٔ Hello World را اجرا کنید.
* یک آبجکت Service ایجاد کنید که یک آدرس IP خارجی را در دسترس قرار می‌دهد.
* با استفاده از آبجکت Service به برنامهٔ در حال اجرا دسترسی پیدا کنید.

<!-- lessoncontent -->

## ایجاد یک سرویس برای برنامه‌ای که در پنج پاد اجرا می‌شود

1. یک برنامهٔ Hello World را در کلاستر خود اجرا کنید:

   {{% code_sample file="service/load-balancer-example.yaml" %}}

   ```shell
   kubectl apply -f https://k8s.io/examples/service/load-balancer-example.yaml
   ```
   فرمان بالا یک
   {{< glossary_tooltip text="Deployment" term_id="deployment" >}}
   و یک
   {{< glossary_tooltip term_id="replica-set" text="ReplicaSet" >}}
   مرتبط با آن ایجاد می‌کند.
   این ReplicaSet پنج
   {{< glossary_tooltip text="Pod" term_id="pod" >}}
   دارد که هر یک از آن‌ها برنامهٔ Hello World را اجرا می‌کند.

1. اطلاعات مربوط به Deployment را نمایش دهید:

   ```shell
   kubectl get deployments hello-world
   kubectl describe deployments hello-world
   ```

1. اطلاعات مربوط به آبجکت‌های ReplicaSet خود را نمایش دهید:

   ```shell
   kubectl get replicasets
   kubectl describe replicasets
   ```

1. یک آبجکت Service ایجاد کنید که این Deployment را در دسترس قرار می‌دهد:

   ```shell
   kubectl expose deployment hello-world --type=LoadBalancer --name=my-service
   ```

1. اطلاعات مربوط به Service را نمایش دهید:

   ```shell
   kubectl get services my-service
   ```

   خروجی مشابه زیر است:

   ```console
   NAME         TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)    AGE
   my-service   LoadBalancer   10.3.245.137   104.198.205.71   8080/TCP   54s
   ```

   {{< alert color="info" title="Note" >}}

   سرویس از نوع `type=LoadBalancer` به پشتیبانی ارائه‌دهندگان ابری خارجی متکی است که در این مثال به آن پرداخته نمی‌شود. برای جزئیات بیشتر، به [تنظیم `type: LoadBalancer` برای Service](/docs/concepts/services-networking/service/#loadbalancer) مراجعه کنید.

   {{< /alert >}}

   {{< alert color="info" title="Note" >}}

   اگر آدرس IP خارجی به‌صورت \<pending\> نمایش داده شد، یک دقیقه صبر کنید و همان فرمان را دوباره وارد کنید.

   {{< /alert >}}

1. اطلاعات تفصیلی مربوط به Service را نمایش دهید:

   ```shell
   kubectl describe services my-service
   ```

   خروجی مشابه زیر است:

   ```console
   Name:           my-service
   Namespace:      default
   Labels:         app.kubernetes.io/name=load-balancer-example
   Annotations:    <none>
   Selector:       app.kubernetes.io/name=load-balancer-example
   Type:           LoadBalancer
   IP:             10.3.245.137
   LoadBalancer Ingress:   104.198.205.71
   Port:           <unset> 8080/TCP
   NodePort:       <unset> 32377/TCP
   Endpoints:      10.0.0.6:8080,10.0.1.6:8080,10.0.1.7:8080 + 2 more...
   Session Affinity:   None
   Events:         <none>
   ```

   آدرس IP خارجی (`LoadBalancer Ingress`) را که سرویس شما در دسترس قرار داده است یادداشت کنید. در این مثال، آدرس IP خارجی 104.198.205.71 است. مقدار `Port` و `NodePort` را نیز یادداشت کنید. در این مثال، مقدار `Port` برابر 8080 و مقدار `NodePort` برابر 32377 است.

1. در خروجی بالا می‌بینید که سرویس چند نقطهٔ پایانی (endpoint) دارد:
   10.0.0.6:8080,10.0.1.6:8080,10.0.1.7:8080 + 2 more. این‌ها آدرس‌های داخلی پادهایی هستند که برنامهٔ Hello World را اجرا می‌کنند. برای اطمینان از اینکه این‌ها آدرس‌های پادها هستند، این فرمان را وارد کنید:

   ```shell
   kubectl get pods --output=wide
   ```

   خروجی مشابه زیر است:

   ```console
   NAME                         ...  IP         NODE
   hello-world-2895499144-1jaz9 ...  10.0.1.6   gke-cluster-1-default-pool-e0b8d269-1afc
   hello-world-2895499144-2e5uh ...  10.0.1.8   gke-cluster-1-default-pool-e0b8d269-1afc
   hello-world-2895499144-9m4h1 ...  10.0.0.6   gke-cluster-1-default-pool-e0b8d269-5v7a
   hello-world-2895499144-o4z13 ...  10.0.1.7   gke-cluster-1-default-pool-e0b8d269-1afc
   hello-world-2895499144-segjf ...  10.0.2.5   gke-cluster-1-default-pool-e0b8d269-cpuc
   ```

1. با استفاده از آدرس IP خارجی (`LoadBalancer Ingress`) به برنامهٔ Hello World دسترسی پیدا کنید:

   ```shell
   curl http://<external-ip>:<port>
   ```

   در این فرمان، `<external-ip>` آدرس IP خارجی (`LoadBalancer Ingress`) سرویس شما و `<port>` مقدار `Port` در توصیف سرویس شماست.
   اگر از minikube استفاده می‌کنید، با وارد کردن `minikube service my-service` برنامهٔ Hello World به‌طور خودکار در مرورگر باز می‌شود.

   پاسخ یک درخواست موفق، یک پیام خوشامدگویی است:

   ```console
   Hello, world!
   Version: 2.0.0
   Hostname: 0bd46b45f32f
   ```

## {{% heading "cleanup" %}}

برای حذف Service، این فرمان را وارد کنید:

```shell
kubectl delete services my-service
```

برای حذف Deployment، ReplicaSet و پادهایی که برنامهٔ Hello World را اجرا می‌کنند، این فرمان را وارد کنید:

```shell
kubectl delete deployment hello-world
```

## {{% heading "whatsnext" %}}

دربارهٔ [اتصال برنامه‌ها با سرویس‌ها](/docs/tutorials/services/connect-applications-service/) بیشتر بیاموزید.
آموزش [استقرار یک نسخهٔ قناری (Canary Release)](/docs/tutorials/stateless-application/canary-deployment/) را امتحان کنید تا یاد بگیرید چگونه نسخه‌های جدید برنامه را به‌طور ایمن در محیط عملیاتی آزمایش کنید.

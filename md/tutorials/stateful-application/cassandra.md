---
title: "مثال: استقرار کاساندرا با StatefulSet"
reviewers:
- ahmetb
content_type: tutorial
weight: 30
---

<!-- overview -->
این آموزش نشان می‌دهد که چگونه [Apache Cassandra](https://cassandra.apache.org/) را روی کوبرنتیز اجرا کنید.
کاساندرا یک پایگاه داده است و برای تضمین ماندگاری داده‌ها (_وضعیت_ برنامه) به ذخیره‌سازی پایدار نیاز دارد.
در این مثال، یک ارائه‌دهندهٔ seed سفارشی برای کاساندرا به پایگاه داده امکان می‌دهد نمونه‌های جدید کاساندرا را هنگام پیوستن به کلاستر کاساندرا شناسایی کند.

آبجکت‌های *StatefulSet* استقرار برنامه‌های دارای وضعیت (stateful) را در کلاستر کوبرنتیز آسان‌تر می‌کنند.
برای آشنایی بیشتر با قابلیت‌هایی که در این آموزش استفاده می‌شوند، صفحهٔ
[StatefulSet](/docs/concepts/workloads/controllers/statefulset/) را ببینید.

{{< alert color="info" title="Note" >}}
کاساندرا و کوبرنتیز هر دو اصطلاح _نود_ را برای اشاره به یکی از اعضای کلاستر به کار می‌برند. در این
آموزش، Podهایی که به StatefulSet تعلق دارند نودهای کاساندرا هستند و عضو
کلاستر کاساندرا (که _حلقه_ یا ring نامیده می‌شود) به شمار می‌روند. وقتی این Podها در کلاستر کوبرنتیز شما اجرا می‌شوند،
control plane کوبرنتیز آن‌ها را روی
{{< glossary_tooltip text="نودهای" term_id="node" >}} کوبرنتیز زمان‌بندی می‌کند.

هر نود کاساندرا هنگام راه‌اندازی از یک _فهرست seed_ برای آغاز فرایند شناسایی سایر
نودهای حلقه استفاده می‌کند.
این آموزش یک ارائه‌دهندهٔ seed سفارشی برای کاساندرا مستقر می‌کند که به پایگاه داده امکان می‌دهد
Podهای جدید کاساندرا را به محض ظاهر شدن در کلاستر کوبرنتیز شما شناسایی کند.
{{< /alert >}}


## {{% heading "objectives" %}}

* یک {{< glossary_tooltip text="Service" term_id="service" >}} از نوع headless برای کاساندرا ایجاد و اعتبارسنجی کنید.
* با استفاده از یک {{< glossary_tooltip term_id="StatefulSet" >}}، حلقهٔ کاساندرا را ایجاد کنید.
* آبجکت StatefulSet را اعتبارسنجی کنید.
* آبجکت StatefulSet را تغییر دهید.
* آبجکت StatefulSet و {{< glossary_tooltip text="Podهای" term_id="pod" >}} آن را حذف کنید.


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای انجام این آموزش، باید از پیش با مفاهیم پایهٔ
{{< glossary_tooltip text="Podها" term_id="pod" >}}،
{{< glossary_tooltip text="Serviceها" term_id="service" >}} و
{{< glossary_tooltip text="StatefulSetها" term_id="StatefulSet" >}} آشنا باشید.

### دستورالعمل‌های تکمیلی راه‌اندازی Minikube

{{< alert color="caution" title="Caution" >}}
ابزار [Minikube](https://minikube.sigs.k8s.io/docs/) به‌طور پیش‌فرض از ۲۰۴۸ مگابایت حافظه و ۲ پردازنده استفاده می‌کند.
اجرای Minikube با پیکربندی پیش‌فرض منابع، در طول این آموزش به خطاهای کمبود منابع
منجر می‌شود. برای جلوگیری از این خطاها، Minikube را با تنظیمات زیر راه‌اندازی کنید:

```shell
minikube start --memory 5120 --cpus=4
```
{{< /alert >}}


<!-- lessoncontent -->
## ایجاد یک Service از نوع headless برای کاساندرا {#creating-a-cassandra-headless-service}

در کوبرنتیز، یک {{< glossary_tooltip text="Service" term_id="service" >}} مجموعه‌ای از
{{< glossary_tooltip text="Podها" term_id="pod" >}} را توصیف می‌کند که وظیفهٔ یکسانی انجام می‌دهند.

از Service زیر برای جست‌وجوهای DNS میان Podهای کاساندرا و کلاینت‌های درون کلاستر شما استفاده می‌شود:

{{% code_sample file="application/cassandra/cassandra-service.yaml" %}}

با استفاده از فایل `cassandra-service.yaml`، یک Service ایجاد کنید تا همهٔ اعضای StatefulSet کاساندرا را دنبال کند:

```shell
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-service.yaml
```


### اعتبارسنجی (اختیاری) {#validating}

اطلاعات Service کاساندرا را دریافت کنید.

```shell
kubectl get svc cassandra
```

پاسخ به این صورت است:

```
NAME        TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
cassandra   ClusterIP   None         <none>        9042/TCP   45s
```

اگر Serviceای با نام `cassandra` نمی‌بینید، یعنی ایجاد آن ناموفق بوده است. برای کمک به
عیب‌یابی مشکلات رایج، صفحهٔ [اشکال‌زدایی Serviceها](/docs/tasks/debug/debug-application/debug-service/)
را مطالعه کنید.

## استفاده از StatefulSet برای ایجاد حلقهٔ کاساندرا

مانیفست StatefulSet که در ادامه آمده است، یک حلقهٔ کاساندرا متشکل از سه Pod ایجاد می‌کند.

{{< alert color="info" title="Note" >}}
این مثال از provisioner پیش‌فرض Minikube استفاده می‌کند.
لطفاً StatefulSet زیر را متناسب با محیط ابری‌ای که با آن کار می‌کنید به‌روزرسانی کنید.
{{< /alert >}}

{{% code_sample file="application/cassandra/cassandra-statefulset.yaml" %}}

با استفاده از فایل `cassandra-statefulset.yaml`، آبجکت StatefulSet کاساندرا را ایجاد کنید:

```shell
# Use this if you are able to apply cassandra-statefulset.yaml unmodified
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml
```

اگر لازم است فایل `cassandra-statefulset.yaml` را متناسب با کلاستر خود تغییر دهید، فایل
https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml را دانلود کنید و سپس
مانیفست را از پوشه‌ای که نسخهٔ تغییریافته را در آن ذخیره کرده‌اید اعمال کنید:
```shell
# Use this if you needed to modify cassandra-statefulset.yaml locally
kubectl apply -f cassandra-statefulset.yaml
```


## اعتبارسنجی StatefulSet کاساندرا

1. اطلاعات StatefulSet کاساندرا را دریافت کنید:

    ```shell
    kubectl get statefulset cassandra
    ```

    پاسخ باید مشابه زیر باشد:

    ```
    NAME        DESIRED   CURRENT   AGE
    cassandra   3         0         13s
    ```

    منبع `StatefulSet` پادها را به‌ترتیب و یکی پس از دیگری مستقر می‌کند.

1. برای مشاهدهٔ وضعیت ایجاد ترتیبی Podها، فهرست آن‌ها را دریافت کنید:

    ```shell
    kubectl get pods -l="app=cassandra"
    ```

    پاسخ باید مشابه زیر باشد:

    ```shell
    NAME          READY     STATUS              RESTARTS   AGE
    cassandra-0   1/1       Running             0          1m
    cassandra-1   0/1       ContainerCreating   0          8s
    ```

    استقرار هر سه Pod ممکن است چند دقیقه طول بکشد. پس از استقرار آن‌ها، همین فرمان
    خروجی‌ای مشابه زیر برمی‌گرداند:

    ```
    NAME          READY     STATUS    RESTARTS   AGE
    cassandra-0   1/1       Running   0          10m
    cassandra-1   1/1       Running   0          9m
    cassandra-2   1/1       Running   0          8m
    ```

3. برای نمایش وضعیت حلقه، ابزار [nodetool](https://cwiki.apache.org/confluence/display/CASSANDRA2/NodeTool) کاساندرا را
   درون نخستین Pod اجرا کنید.

    ```shell
    kubectl exec -it cassandra-0 -- nodetool status
    ```

    پاسخ باید تقریباً به این شکل باشد:

    ```
    Datacenter: DC1-K8Demo
    ======================
    Status=Up/Down
    |/ State=Normal/Leaving/Joining/Moving
    --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
    UN  172.17.0.5  83.57 KiB  32           74.0%             e2dd09e6-d9d3-477e-96c5-45094c08db0f  Rack1-K8Demo
    UN  172.17.0.4  101.04 KiB  32           58.8%             f89d6835-3a42-4419-92b3-0e62cae1479c  Rack1-K8Demo
    UN  172.17.0.6  84.74 KiB  32           67.1%             a6a1e8c2-3dc5-4417-b1a0-26507af2aaad  Rack1-K8Demo
    ```

## تغییر StatefulSet کاساندرا

برای تغییر اندازهٔ StatefulSet کاساندرا از `kubectl edit` استفاده کنید.

1. فرمان زیر را اجرا کنید:

    ```shell
    kubectl edit statefulset cassandra
    ```

    این فرمان یک ویرایشگر را در ترمینال شما باز می‌کند. خطی که باید تغییر دهید فیلد `replicas` است.
    نمونهٔ زیر بخشی از فایل StatefulSet است:

    ```yaml
    # Please edit the object below. Lines beginning with a '#' will be ignored,
    # and an empty file will abort the edit. If an error occurs while saving this file will be
    # reopened with the relevant failures.
    #
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      creationTimestamp: 2016-08-13T18:40:58Z
      generation: 1
      labels:
      app: cassandra
      name: cassandra
      namespace: default
      resourceVersion: "323"
      uid: 7a219483-6185-11e6-a910-42010a8a0fc0
    spec:
      replicas: 3
    ```

1. تعداد رپلیکاها را به ۴ تغییر دهید و سپس مانیفست را ذخیره کنید.

    اکنون StatefulSet مقیاس‌پذیری می‌کند تا با ۴ Pod اجرا شود.

1. برای اطمینان از اعمال تغییر، اطلاعات StatefulSet کاساندرا را دریافت کنید:

    ```shell
    kubectl get statefulset cassandra
    ```

    پاسخ باید مشابه زیر باشد:

    ```
    NAME        DESIRED   CURRENT   AGE
    cassandra   4         4         36m
    ```



## {{% heading "cleanup" %}}

حذف یک StatefulSet یا کاهش مقیاس آن، حجم‌های (volume) مرتبط با آن را حذف نمی‌کند.
این تنظیم برای حفظ امنیت شماست، زیرا داده‌های شما ارزشمندتر از آن هستند که همهٔ منابع مرتبط با StatefulSet به‌طور خودکار پاک شوند.

{{< alert color="danger" title="Warning" >}}
بسته به کلاس ذخیره‌سازی و سیاست بازپس‌گیری (reclaim policy)، حذف *PersistentVolumeClaimها* ممکن است باعث شود حجم‌های مرتبط
نیز حذف شوند. هرگز فرض نکنید که پس از حذف درخواست‌های حجم، همچنان به داده‌های آن‌ها دسترسی خواهید داشت.
{{< /alert >}}

1. برای حذف همهٔ اجزای StatefulSet کاساندرا، فرمان‌های زیر را (که در قالب یک فرمان واحد به هم زنجیر شده‌اند) اجرا کنید:

    ```shell
    grace=$(kubectl get pod cassandra-0 -o=jsonpath='{.spec.terminationGracePeriodSeconds}') \
      && kubectl delete statefulset -l app=cassandra \
      && echo "Sleeping ${grace} seconds" 1>&2 \
      && sleep $grace \
      && kubectl delete persistentvolumeclaim -l app=cassandra
    ```

1. برای حذف Serviceای که برای کاساندرا راه‌اندازی کرده‌اید، فرمان زیر را اجرا کنید:

    ```shell
    kubectl delete service -l app=cassandra
    ```

## متغیرهای محیطی کانتینر کاساندرا

پادهای این آموزش از ایمیج [`gcr.io/google-samples/cassandra:v13`](https://github.com/kubernetes/examples/blob/master/databases/cassandra/image/Dockerfile)
موجود در [رجیستری کانتینر](https://cloud.google.com/container-registry/docs/) گوگل استفاده می‌کنند.
این ایمیج داکر بر پایهٔ [debian-base](https://github.com/kubernetes/release/tree/master/images/build/debian-base)
ساخته شده و OpenJDK 8 را در خود دارد.

این ایمیج شامل یک نصب استاندارد کاساندرا از مخزن Debian بنیاد Apache است.
با استفاده از متغیرهای محیطی می‌توانید مقادیری را که در فایل `cassandra.yaml` درج می‌شوند تغییر دهید.

| متغیر محیطی     | مقدار پیش‌فرض    |
| ------------------------ |:---------------: |
| `CASSANDRA_CLUSTER_NAME` | `'Test Cluster'` |
| `CASSANDRA_NUM_TOKENS`   | `32`             |
| `CASSANDRA_RPC_ADDRESS`  | `0.0.0.0`        |



## {{% heading "whatsnext" %}}


* با نحوهٔ [تغییر مقیاس یک StatefulSet](/docs/tasks/run-application/scale-stateful-set/) آشنا شوید.
* دربارهٔ [*KubernetesSeedProvider*](https://github.com/kubernetes/examples/blob/master/databases/cassandra/java/src/main/java/io/k8s/cassandra/KubernetesSeedProvider.java) بیشتر بیاموزید.
* [پیکربندی‌های سفارشی بیشتری برای ارائه‌دهندهٔ seed](https://github.com/kubernetes/examples/blob/master/databases/cassandra/java/README.md) را ببینید.

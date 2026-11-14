---
title: تخصیص Podها به نودها با استفاده از وابستگی نود
min-kubernetes-server-version: v1.10
content_type: task
weight: 160
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توانید در یک کلاستر کوبرنتیز، یک Pod را با استفاده از وابستگی نود (Node Affinity) به نودی مشخص تخصیص دهید.


## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}



<!-- steps -->

## افزودن برچسب به یک نود

1. نودهای کلاستر خود را همراه با برچسب‌هایشان فهرست کنید:

    ```shell
    kubectl get nodes --show-labels
    ```
    خروجی مشابه زیر است:

    ```shell
    NAME      STATUS    ROLES    AGE     VERSION        LABELS
    worker0   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker0
    worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
    worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
    ```
1. یکی از نودهای خود را انتخاب کنید و برچسبی به آن اضافه کنید:

    ```shell
    kubectl label nodes <your-node-name> disktype=ssd
    ```
    در این دستور، `<your-node-name>` نام نود انتخاب‌شدهٔ شماست.

1. بررسی کنید که نود انتخاب‌شده برچسب `disktype=ssd` را دارد:

    ```shell
    kubectl get nodes --show-labels
    ```

    خروجی مشابه زیر است:

    ```
    NAME      STATUS    ROLES    AGE     VERSION        LABELS
    worker0   Ready     <none>   1d      v1.13.0        ...,disktype=ssd,kubernetes.io/hostname=worker0
    worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
    worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
    ```

    در خروجی بالا می‌بینید که نود `worker0` برچسب `disktype=ssd` را دارد.

## زمان‌بندی یک Pod با استفاده از وابستگی نود الزامی

این مانیفست یک Pod را توصیف می‌کند که وابستگی نود `requiredDuringSchedulingIgnoredDuringExecution` با مقدار `disktype: ssd` دارد.
معنای این تنظیم آن است که Pod فقط روی نودی زمان‌بندی می‌شود که برچسب `disktype=ssd` داشته باشد.

{{% code_sample file="pods/pod-nginx-required-affinity.yaml" %}}

1. مانیفست را اعمال کنید تا Podای ایجاد شود که روی نود انتخاب‌شدهٔ شما زمان‌بندی می‌شود:
    
    ```shell
    kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml
    ```

1. بررسی کنید که Pod روی نود انتخاب‌شدهٔ شما در حال اجراست:

    ```shell
    kubectl get pods --output=wide
    ```

    خروجی مشابه زیر است:
    
    ```
    NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
    nginx    1/1       Running   0          13s    10.200.0.4   worker0
    ```
    
## زمان‌بندی یک Pod با استفاده از وابستگی نود ترجیحی

این مانیفست یک Pod را توصیف می‌کند که وابستگی نود `preferredDuringSchedulingIgnoredDuringExecution` با مقدار `disktype: ssd` دارد.
معنای این تنظیم آن است که Pod نودی را که برچسب `disktype=ssd` دارد ترجیح می‌دهد.

{{% code_sample file="pods/pod-nginx-preferred-affinity.yaml" %}}

1. مانیفست را اعمال کنید تا Podای ایجاد شود که روی نود انتخاب‌شدهٔ شما زمان‌بندی می‌شود:
    
    ```shell
    kubectl apply -f https://k8s.io/examples/pods/pod-nginx-preferred-affinity.yaml
    ```

1. بررسی کنید که Pod روی نود انتخاب‌شدهٔ شما در حال اجراست:

    ```shell
    kubectl get pods --output=wide
    ```

    خروجی مشابه زیر است:
    
    ```
    NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
    nginx    1/1       Running   0          13s    10.200.0.4   worker0
    ```



## {{% heading "whatsnext" %}}

دربارهٔ [وابستگی نود](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) بیشتر بیاموزید.

---
title: تخصیص Podها به نودها
content_type: task
weight: 150
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان یک Pod کوبرنتیز را به نودی مشخص در یک کلاستر کوبرنتیز تخصیص داد.


## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}



<!-- steps -->

## افزودن برچسب به یک نود

1. {{< glossary_tooltip term_id="node" text="نودهای" >}} کلاستر خود را همراه با برچسب‌هایشان فهرست کنید:

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

    در این دستور، `<your-node-name>` نام نودی است که انتخاب کرده‌اید.

1. بررسی کنید که نود انتخاب‌شده برچسب `disktype=ssd` را دارد:

    ```shell
    kubectl get nodes --show-labels
    ```

    خروجی مشابه زیر است:

    ```shell
    NAME      STATUS    ROLES    AGE     VERSION        LABELS
    worker0   Ready     <none>   1d      v1.13.0        ...,disktype=ssd,kubernetes.io/hostname=worker0
    worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
    worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
    ```

    در خروجی بالا می‌بینید که نود `worker0` برچسب `disktype=ssd` را دارد.

## ایجاد یک Pod که روی نود انتخاب‌شده زمان‌بندی می‌شود

این فایل پیکربندی، یک Pod را توصیف می‌کند که انتخابگر نود (node selector) آن `disktype: ssd` است. این یعنی Pod روی نودی زمان‌بندی می‌شود که برچسب `disktype=ssd` داشته باشد.

{{% code_sample file="pods/pod-nginx.yaml" %}}

1. با استفاده از این فایل پیکربندی، یک Pod ایجاد کنید که روی نود انتخاب‌شده زمان‌بندی شود:
    
    ```shell
    kubectl apply -f https://k8s.io/examples/pods/pod-nginx.yaml
    ```

1. بررسی کنید که Pod روی نود انتخاب‌شده در حال اجرا است:

    ```shell
    kubectl get pods --output=wide
    ```

    خروجی مشابه زیر است:
    
    ```shell
    NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
    nginx    1/1       Running   0          13s    10.200.0.4   worker0
    ```
## ایجاد یک Pod که روی یک نود مشخص زمان‌بندی می‌شود

همچنین می‌توانید با تنظیم فیلد `nodeName`، یک Pod را روی یک نود مشخص زمان‌بندی کنید.

{{% code_sample file="pods/pod-nginx-specific-node.yaml" %}}

با استفاده از این فایل پیکربندی، یک Pod ایجاد کنید که فقط روی `foo-node` زمان‌بندی شود.



## {{% heading "whatsnext" %}}

* درباره‌ی [برچسب‌ها و انتخابگرها](/docs/concepts/overview/working-with-objects/labels/) بیشتر بیاموزید.
* درباره‌ی [نودها](/docs/concepts/architecture/nodes/) بیشتر بیاموزید.

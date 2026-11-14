---
title: "راه‌اندازی DRA در یک کلاستر"
content_type: task
min-kubernetes-server-version: v1.34
weight: 10
---
{{< feature-state feature_gate_name="DynamicResourceAllocation" >}}

<!-- overview -->

این صفحه نشان می‌دهد چگونه می‌توانید _تخصیص پویای منابع (Dynamic Resource Allocation یا DRA)_ را در یک کلاستر کوبرنتیز پیکربندی کنید. برای این کار باید گروه‌های API را فعال و کلاس‌های دستگاه را پیکربندی کنید. این دستورالعمل‌ها برای مدیران کلاستر نوشته شده‌اند.

<!-- body -->

## درباره DRA {#about-dra}

{{< glossary_definition term_id="dra" length="all" >}}

پیش از ادامه، با نحوه کار DRA و اصطلاحات آن، مانند
{{< glossary_tooltip text="DeviceClassها" term_id="deviceclass" >}}،
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} و
{{< glossary_tooltip text="ResourceClaimTemplateها" term_id="resourceclaimtemplate" >}}
آشنا شوید. برای جزئیات بیشتر،
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/) را ببینید.

<!-- prerequisites -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* دستگاه‌ها را به‌طور مستقیم یا غیرمستقیم به کلاستر خود متصل کنید. برای جلوگیری از مشکلات احتمالی درایورها، تا پیش از راه‌اندازی قابلیت DRA در کلاستر، درایورها را نصب نکنید.

<!-- steps -->

## اختیاری: فعال‌سازی گروه‌های API اضافی DRA {#enable-dra}

قابلیت DRA در مجموع یک قابلیت پایدار در کوبرنتیز است، اما برخی از جنبه‌های آن ممکن است هنوز در مرحله آلفا یا بتا باشند.
اگر می‌خواهید از جنبه‌ای از DRA استفاده کنید که هنوز پایدار نشده است و آن قابلیت به یک نوع API اختصاصی وابسته است، باید گروه‌های API آلفا یا بتای مربوط به آن را فعال کنید.

برخی از درایورها یا بارهای کاری قدیمی‌تر DRA ممکن است هنوز به API نسخه v1beta1 از کوبرنتیز 1.30 یا نسخه v1beta2 از کوبرنتیز 1.32 نیاز داشته باشند.
تنها در صورتی که به پشتیبانی از این نسخه‌ها نیاز دارید،
{{< glossary_tooltip text="گروه‌های API" term_id="api-group" >}} زیر را فعال کنید:

    * `resource.k8s.io/v1beta1`
    * `resource.k8s.io/v1beta2`

قابلیت‌های آلفا که نوع‌های API جداگانه دارند، به این گروه نیاز دارند:

   * `resource.k8s.io/v1alpha3`

برای اطلاعات بیشتر،
[فعال یا غیرفعال کردن گروه‌های API](/docs/reference/using-api/#enabling-or-disabling) را ببینید.

## بررسی فعال بودن DRA {#verify}

برای اطمینان از اینکه کلاستر به‌درستی پیکربندی شده است، فهرست DeviceClassها را دریافت کنید:

```shell
kubectl get deviceclasses
```
اگر پیکربندی مؤلفه‌ها درست باشد، خروجی مشابه زیر خواهد بود:

```
No resources found
```

اگر DRA به‌درستی پیکربندی نشده باشد، خروجی دستور قبلی مشابه زیر خواهد بود:
   
```
error: the server doesn't have a resource type "deviceclasses"
```

برای مثال، این وضعیت زمانی رخ می‌دهد که گروه API با نام resource.k8s.io غیرفعال شده باشد.
بررسی مشابهی برای نوع‌های سطح بالای آلفا یا بتا نیز قابل انجام است.

مراحل عیب‌یابی زیر را امتحان کنید:

1. مؤلفه `kube-apiserver` را دوباره پیکربندی و راه‌اندازی مجدد کنید.

1. اگر کل فیلد `.spec.resourceClaims` از Podها حذف می‌شود، یا Podها بدون در نظر گرفتن ResourceClaimها زمان‌بندی می‌شوند، بررسی کنید که
   [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `DynamicResourceAllocation` برای kube-apiserver، kube-controller-manager، kube-scheduler یا kubelet خاموش نشده باشد.

## نصب درایورهای دستگاه {#install-drivers}

پس از فعال‌سازی DRA در کلاستر، می‌توانید درایورهای دستگاه‌های متصل را نصب کنید. برای دستورالعمل نصب، به مستندات مالک دستگاه یا پروژه‌ای که درایورهای دستگاه را نگهداری می‌کند مراجعه کنید. درایورهایی که نصب می‌کنید باید با DRA سازگار باشند.

برای اطمینان از اینکه درایورهای نصب‌شده طبق انتظار کار می‌کنند، فهرست ResourceSliceهای کلاستر را دریافت کنید:

```shell
kubectl get resourceslices
```
خروجی مشابه زیر است:

```
NAME                                                  NODE                DRIVER               POOL                             AGE
00000-driver.example.com-cluster-1-node-1-abcde      cluster-1-node-1    driver.example.com   cluster-1-device-pool-1-r1gc     7s
00000-driver.example.com-cluster-1-node-2-fghij      cluster-1-node-2    driver.example.com   cluster-1-device-pool-2-446z     8s
```

مراحل عیب‌یابی زیر را امتحان کنید:

1. سلامت درایور DRA را بررسی کنید و در خروجی لاگ آن به دنبال پیام‌های خطای مربوط به انتشار ResourceSliceها بگردید. ممکن است فروشنده درایور دستورالعمل‌های بیشتری درباره نصب و عیب‌یابی ارائه کرده باشد.

## ایجاد DeviceClassها {#create-deviceclasses}

با ایجاد
{{< glossary_tooltip text="DeviceClassها" term_id="deviceclass" >}}
می‌توانید دسته‌هایی از دستگاه‌ها را تعریف کنید که اپراتورهای برنامه بتوانند آن‌ها را در بارهای کاری درخواست کنند. برخی از ارائه‌دهندگان درایور دستگاه نیز ممکن است از شما بخواهند که در حین نصب درایور، DeviceClassهایی ایجاد کنید.

آبجکت‌های ResourceSlice که درایور شما منتشر می‌کند، اطلاعاتی درباره دستگاه‌های تحت مدیریت آن درایور، مانند ظرفیت، فراداده و ویژگی‌ها، در خود دارند. می‌توانید با استفاده از {{< glossary_tooltip term_id="cel" >}} ویژگی‌ها را در DeviceClassها فیلتر کنید. با این کار، یافتن دستگاه‌ها برای اپراتورهای بار کاری آسان‌تر می‌شود.

1.  برای یافتن ویژگی‌هایی از دستگاه که می‌توانید با عبارت‌های CEL در DeviceClassها انتخاب کنید، مشخصات یک ResourceSlice را دریافت کنید:

    ```shell
    kubectl get resourceslice <resourceslice-name> -o yaml
    ```
    خروجی مشابه زیر است:

    ```yaml
    apiVersion: resource.k8s.io/v1
    kind: ResourceSlice
    # lines omitted for clarity
    spec:
      devices:
      - attributes:
          type:
            string: gpu
        capacity:
          memory:
            value: 64Gi
        name: gpu-0
      - attributes:
          type:
            string: gpu
        capacity:
          memory:
            value: 64Gi
        name: gpu-1
      driver: driver.example.com
      nodeName: cluster-1-node-1
    # lines omitted for clarity
    ```
    همچنین می‌توانید ویژگی‌ها و مقادیر موجود را در مستندات ارائه‌دهنده درایور بررسی کنید.

1.  مانیفست نمونه DeviceClass زیر را بررسی کنید. این مانیفست هر دستگاهی را که درایور دستگاه `driver.example.com` مدیریت می‌کند انتخاب می‌کند:

    {{% code_sample file="dra/deviceclass.yaml" %}}

1.  این DeviceClass را در کلاستر خود ایجاد کنید:

    ```shell
    kubectl apply -f https://k8s.io/examples/dra/deviceclass.yaml
    ```

## پاک‌سازی {#clean-up}

برای حذف DeviceClass که در این تمرین ایجاد کردید، دستور زیر را اجرا کنید:

```shell
kubectl delete -f https://k8s.io/examples/dra/deviceclass.yaml
```

## {{% heading "whatsnext" %}}

* [اطلاعات بیشتر درباره DRA](/docs/concepts/resource-management/dynamic-resource-allocation/)
* [تخصیص دستگاه‌ها به بارهای کاری با DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra)

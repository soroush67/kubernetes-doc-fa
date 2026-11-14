---
title: تخصیص دستگاه‌ها به بارهای کاری با DRA
content_type: task
min-kubernetes-server-version: v1.34
weight: 20
---
{{< feature-state feature_gate_name="DynamicResourceAllocation" >}}

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با استفاده از _تخصیص پویای منابع (dynamic resource allocation یا DRA)_ دستگاه‌ها را به Podهای خود تخصیص دهید. این دستورالعمل‌ها برای گردانندگان بار کاری (workload operators) نوشته شده‌اند. پیش از خواندن این صفحه، با نحوهٔ کار DRA و اصطلاحات آن، مانند
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} و
{{< glossary_tooltip text="ResourceClaimTemplateها" term_id="resourceclaimtemplate" >}}، آشنا شوید.
برای اطلاعات بیشتر، به
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/) مراجعه کنید.

<!-- body -->

## دربارهٔ تخصیص دستگاه با DRA {#about-device-allocation-dra}

به‌عنوان گردانندهٔ بار کاری، می‌توانید با ایجاد ResourceClaimها یا ResourceClaimTemplateها، دستگاه‌هایی را برای بارهای کاری خود _درخواست (claim)_ کنید. هنگامی که بار کاری خود را مستقر می‌کنید، کوبرنتیز و درایورهای دستگاه، دستگاه‌های در دسترس را پیدا می‌کنند، آن‌ها را به Podهای شما تخصیص می‌دهند و Podها را روی نودهایی قرار می‌دهند که به آن دستگاه‌ها دسترسی دارند.

<!-- prerequisites -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* اطمینان حاصل کنید که مدیر کلاستر شما DRA را راه‌اندازی کرده، دستگاه‌ها را متصل کرده و درایورها را نصب کرده است. برای اطلاعات بیشتر، به
  [راه‌اندازی DRA در یک کلاستر](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster) مراجعه کنید.

<!-- steps -->

## شناسایی دستگاه‌هایی که باید درخواست شوند {#identify-devices}

مدیر کلاستر شما یا درایورهای دستگاه،
_{{< glossary_tooltip term_id="deviceclass" text="DeviceClassها" >}}_ را ایجاد می‌کنند که دسته‌هایی از دستگاه‌ها را تعریف می‌کنند. می‌توانید با استفاده از
{{< glossary_tooltip term_id="cel" >}} و فیلتر کردن بر اساس ویژگی‌های مشخصی از دستگاه، دستگاه‌ها را درخواست کنید.

فهرست DeviceClassهای موجود در کلاستر را دریافت کنید:

```shell
kubectl get deviceclasses
```
خروجی مشابه زیر است:

```
NAME                 AGE
driver.example.com   16m
```
اگر با خطای مجوز (permission error) مواجه شدید، ممکن است دسترسی لازم برای دریافت DeviceClassها را نداشته باشید. برای آگاهی از ویژگی‌های دستگاه‌های در دسترس، با مدیر کلاستر یا ارائه‌دهندهٔ درایور مشورت کنید.

## درخواست منابع {#claim-resources}

می‌توانید با استفاده از
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} منابعی را از یک DeviceClass درخواست کنید. برای ایجاد یک ResourceClaim، یکی از کارهای زیر را انجام دهید:

* اگر می‌خواهید چند Pod به‌طور مشترک به دستگاه‌های یکسانی دسترسی داشته باشند، یا می‌خواهید یک درخواست فراتر از طول عمر یک Pod باقی بماند، یک ResourceClaim را به‌صورت دستی ایجاد کنید.
* از یک
  {{< glossary_tooltip text="ResourceClaimTemplate" term_id="resourceclaimtemplate" >}}
  استفاده کنید تا کوبرنتیز برای هر Pod یک ResourceClaim جداگانه تولید و مدیریت کند. اگر می‌خواهید هر Pod به دستگاه‌های جداگانه‌ای با پیکربندی‌های مشابه دسترسی داشته باشد، یک ResourceClaimTemplate ایجاد کنید. برای نمونه، ممکن است بخواهید Podهای یک Job که از
  [اجرای موازی](/docs/concepts/workloads/controllers/job/#parallel-jobs)
  استفاده می‌کند، هم‌زمان به دستگاه‌ها دسترسی داشته باشند.

اگر در یک Pod مستقیماً به یک ResourceClaim مشخص ارجاع دهید، آن ResourceClaim باید از قبل در کلاستر وجود داشته باشد. اگر ResourceClaim ارجاع‌شده وجود نداشته باشد، Pod تا زمان ایجاد آن ResourceClaim در وضعیت معلق (pending) باقی می‌ماند. می‌توانید در یک Pod به یک ResourceClaim خودکار تولیدشده ارجاع دهید، اما این کار توصیه نمی‌شود، زیرا طول عمر ResourceClaimهای خودکار تولیدشده به طول عمر Podی وابسته است که تولید آن‌ها را آغاز کرده است.

برای ایجاد یک بار کاری که منابعی را درخواست می‌کند، یکی از گزینه‌های زیر را انتخاب کنید:

{{< tabs name="claim-resources" >}}
{{% tab name="ResourceClaimTemplate" %}}

مانیفست نمونهٔ زیر را بررسی کنید:

{{% code_sample file="dra/resourceclaimtemplate.yaml" %}}

این مانیفست یک ResourceClaimTemplate ایجاد می‌کند که دستگاه‌هایی از DeviceClass با نام
`example-device-class` را درخواست می‌کند که با هر دو پارامتر زیر مطابقت داشته باشند:

  * دستگاه‌هایی که ویژگی `driver.example.com/type` آن‌ها مقدار
    `gpu` دارد.
  * دستگاه‌هایی که ظرفیت آن‌ها `64Gi` است.

برای ایجاد ResourceClaimTemplate، فرمان زیر را اجرا کنید:

```shell
kubectl apply -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml
```

{{% /tab %}}
{{% tab name="ResourceClaim" %}}

مانیفست نمونهٔ زیر را بررسی کنید:

{{% code_sample file="dra/resourceclaim.yaml" %}}

این مانیفست یک ResourceClaim ایجاد می‌کند که دستگاه‌هایی از DeviceClass با نام
`example-device-class` را درخواست می‌کند که با هر دو پارامتر زیر مطابقت داشته باشند:

  * دستگاه‌هایی که ویژگی `driver.example.com/type` آن‌ها مقدار
    `gpu` دارد.
  * دستگاه‌هایی که ظرفیت آن‌ها `64Gi` است.

برای ایجاد ResourceClaim، فرمان زیر را اجرا کنید:

```shell
kubectl apply -f https://k8s.io/examples/dra/resourceclaim.yaml
```

{{% /tab %}}
{{< /tabs >}}

## درخواست دستگاه در بارهای کاری با استفاده از DRA {#request-devices-workloads}

برای درخواست تخصیص دستگاه، یک ResourceClaim یا یک ResourceClaimTemplate را در فیلد `resourceClaims` مشخصات Pod تعیین کنید. سپس در فیلد `resources.claims` یکی از کانتینرهای آن Pod، درخواست مشخصی را با نامش فراخوانی کنید. می‌توانید چندین مدخل در فیلد `resourceClaims` تعیین کنید و درخواست‌های مشخصی را در کانتینرهای مختلف به کار ببرید.

1. Job نمونهٔ زیر را بررسی کنید:

   {{% code_sample file="dra/dra-example-job.yaml" %}}

   هر Pod در این Job ویژگی‌های زیر را دارد:
   
   * یک ResourceClaimTemplate با نام `separate-gpu-claim` و یک ResourceClaim با نام `shared-gpu-claim` را در اختیار کانتینرها قرار می‌دهد.
   * کانتینرهای زیر را اجرا می‌کند:
       * کانتینر `container0` دستگاه‌ها را از ResourceClaimTemplate با نام `separate-gpu-claim` درخواست می‌کند.
       * کانتینرهای `container1` و `container2` به‌طور مشترک به دستگاه‌های ResourceClaim با نام `shared-gpu-claim` دسترسی دارند.

1. Job را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-example-job.yaml
   ```

گام‌های عیب‌یابی زیر را امتحان کنید:

1. اگر بار کاری آن‌طور که انتظار می‌رود آغاز نشد، از Job به Podها و از Podها به ResourceClaimها بروید و آبجکت‌های هر سطح را با `kubectl describe` بررسی کنید تا ببینید آیا فیلد وضعیت (status) یا رویدادی وجود دارد که علت آغاز نشدن بار کاری را توضیح دهد.
1. اگر ایجاد یک Pod با خطای `must specify one of: resourceClaimName,
   resourceClaimTemplateName` ناموفق شد، بررسی کنید که در همهٔ مدخل‌های `pod.spec.resourceClaims` دقیقاً یکی از این فیلدها تنظیم شده باشد. اگر چنین است، ممکن است یک webhook تغییردهندهٔ Pod (mutating Pod webhook) در کلاستر نصب شده باشد که بر اساس APIهای کوبرنتیز نسخهٔ پایین‌تر از 1.32 ساخته شده است. برای بررسی این موضوع با مدیر کلاستر خود همکاری کنید.

## پاک‌سازی {#clean-up}

برای حذف آبجکت‌های کوبرنتیزی که در این تمرین ایجاد کردید، گام‌های زیر را دنبال کنید:

1.  Job نمونه را حذف کنید:

    ```shell
    kubectl delete -f https://k8s.io/examples/dra/dra-example-job.yaml
    ```

1.  برای حذف درخواست‌های منابع خود، یکی از فرمان‌های زیر را اجرا کنید:

    * حذف ResourceClaimTemplate:

      ```shell
      kubectl delete -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml
      ```
    * حذف ResourceClaim:

      ```shell
      kubectl delete -f https://k8s.io/examples/dra/resourceclaim.yaml
      ```

## {{% heading "whatsnext" %}}

* [اطلاعات بیشتر دربارهٔ DRA](/docs/concepts/resource-management/dynamic-resource-allocation/)

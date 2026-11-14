---
title: استفاده از حجم ایمیج (Image Volume) در یک Pod
reviewers:
content_type: task
weight: 210
min-kubernetes-server-version: v1.31
---

<!-- overview -->

{{< feature-state feature_gate_name="ImageVolume" >}}

این صفحه نشان می‌دهد که چگونه یک پاد را با استفاده از حجم‌های ایمیج پیکربندی کنید. با این کار می‌توانید محتوای رجیستری‌های OCI را درون کانتینرها مانت کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

- محیط اجرای کانتینر باید از قابلیت حجم‌های ایمیج پشتیبانی کند.
- باید بتوانید روی میزبان دستور اجرا کنید.
- باید بتوانید با exec به درون پادها دسترسی پیدا کنید.

<!-- steps -->

## اجرای یک Pod که از حجم ایمیج استفاده می‌کند {#create-pod}

برای فعال کردن حجم ایمیج در یک پاد، فیلد `volumes[*].image` در `.spec` را روی یک ارجاع معتبر تنظیم کنید و سپس آن را در `volumeMounts` کانتینر به کار ببرید. برای مثال:

{{% code_sample file="pods/image-volumes.yaml" %}}

1. پاد را روی کلاستر خود ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/image-volumes.yaml
   ```

1. به کانتینر متصل شوید:

   ```shell
   kubectl exec image-volume -it -- bash
   ```

1. محتوای یک فایل را در حجم بررسی کنید:

   ```shell
   cat /volume/dir/file
   ```

   خروجی مشابه زیر است:

   ```none
   1
   ```

   همچنین می‌توانید فایل دیگری را در مسیری متفاوت بررسی کنید:

   ```shell
   cat /volume/file
   ```

   خروجی مشابه زیر است:

   ```none
   2
   ```

## استفاده از `subPath` (یا `subPathExpr`)

از نسخهٔ v1.33 کوبرنتیز، هنگام استفاده از قابلیت حجم ایمیج می‌توانید از
[`subPath`](/docs/concepts/storage/volumes/#using-subpath) یا
[`subPathExpr`](/docs/concepts/storage/volumes/#using-subpath-expanded-environment)
استفاده کنید.

{{% code_sample file="pods/image-volumes-subpath.yaml" %}}

1. پاد را روی کلاستر خود ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/image-volumes-subpath.yaml
   ```

1. به کانتینر متصل شوید:

   ```shell
   kubectl exec image-volume -it -- bash
   ```

1. محتوای فایلی را که از زیرمسیر `dir` در حجم آمده است بررسی کنید:

   ```shell
   cat /volume/file
   ```

   خروجی مشابه زیر است:

   ```none
   1
   ```

## مطالعهٔ بیشتر

- [حجم‌های `image`](/docs/concepts/storage/volumes/#image)

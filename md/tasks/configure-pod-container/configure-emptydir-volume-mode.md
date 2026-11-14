---
title: تنظیم مجوزها روی یک حجم emptyDir
content_type: task
weight: 215
min-kubernetes-server-version: v1.37
---

<!-- overview -->

{{< feature-state feature_gate_name="EmptyDirVolumeMode" >}}

این صفحه نشان می‌دهد چگونه با استفاده از فیلد `mode` بیت‌های مجوز یونیکس (Unix permission bits) را روی دایرکتوری یک حجم (volume) از نوع `emptyDir` تنظیم کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

لازم است [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `EmptyDirVolumeMode` هم روی API server **و** هم روی kubelet فعال باشد.

<!-- steps -->

## ایجاد یک Pod که از حجم emptyDir با مجوزهای سفارشی استفاده می‌کند {#create-pod}

با فیلد `emptyDir.mode` می‌توانید بیت‌های مجوز یونیکس (از `0000` تا `01777` در مبنای هشت) را روی دایرکتوری حجم تنظیم کنید. اگر این فیلد مشخص نشود، دایرکتوری با مجوزهای پیش‌فرض `0777` ایجاد می‌شود.

برای مثال، برای ایجاد یک دایرکتوری اشتراکی `/tmp` که بیت چسبنده (sticky bit) آن فعال است تا فقط مالک هر فایل بتواند فایل‌های خودش را حذف کند:

{{% code_sample file="pods/emptydir-volume-mode.yaml" %}}

1. Pod را در کلاستر خود ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/emptydir-volume-mode.yaml
   ```

1. بررسی کنید که Pod در حال اجرا باشد:

   ```shell
   kubectl get pod emptydir-mode-demo
   ```

1. مجوزهای حجم سوارشده (mount) را بررسی کنید:

   ```shell
   kubectl exec emptydir-mode-demo -- ls -ld /tmp
   ```

   خروجی مشابه زیر است:

   ```none
   drwxrwxrwt 2 root root 4096 Jul 28 00:00 /tmp
   ```

   حرف `t` در انتهای خروجی تأیید می‌کند که بیت چسبنده فعال است.

1. Pod‌ای را که برای این تمرین ایجاد کردید حذف کنید:

   ```shell
   kubectl delete pod emptydir-mode-demo
   ```

## {{% heading "whatsnext" %}}

- درباره‌ی [حجم‌های `emptyDir`](/docs/concepts/storage/volumes/#emptydir) بیشتر بیاموزید.

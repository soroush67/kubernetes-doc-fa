---
title: تنظیم گزینه‌های bind mount برای mountهای حجم
content_type: task
weight: 216
min-kubernetes-server-version: v1.37
---

<!-- overview -->

{{< feature-state feature_gate_name="VolumeBindMountOptions" >}}

این صفحه نشان می‌دهد که چگونه می‌توان گزینه‌های امنیتی bind mount (`noexec`،
`nodev` و `nosuid`) را روی mountهای حجم (volume) در یک Pod اعمال کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

باید feature gate با نام `VolumeBindMountOptions` را
([feature gate](/docs/reference/command-line-tools-reference/feature-gates/)) هم روی API server **و** هم روی kubelet فعال کنید.
محیط اجرای کانتینر نیز باید از فیلد `mount_options` در پیام `Mount` در CRI پشتیبانی کند.

<!-- steps -->

## ایجاد یک Pod با گزینه‌های bind mount {#create-pod}

فیلد `.spec.containers[*].volumeMounts[*].bindMountOptions` فهرستی از پرچم‌های bind mount را می‌پذیرد.
مقادیر مجاز عبارت‌اند از `noexec`، `nodev` و `nosuid`.

برای مثال، برای اینکه یک حجم emptyDir را با گزینه‌های `noexec` و `nosuid` در مسیر `/tmp` mount کنید،
به‌طوری که فایل‌های اجرایی قابل اجرا نباشند و بیت‌های set-user-ID نادیده گرفته شوند، از مانیفست زیر استفاده کنید:

{{% code_sample file="pods/bind-mount-options.yaml" %}}

1. Pod را در کلاستر خود ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/bind-mount-options.yaml
   ```

1. بررسی کنید که Pod در حال اجرا باشد:

   ```shell
   kubectl get pod bind-mount-options-demo
   ```

1. گزینه‌های mount را روی حجم بررسی کنید:

   ```shell
   kubectl exec bind-mount-options-demo -- mount | grep /tmp
   ```

   خروجی باید شامل `noexec` و `nosuid` در میان گزینه‌های mount باشد.

1. بررسی کنید که اجرای یک فایل اجرایی روی این mount با شکست مواجه می‌شود:

   ```shell
   kubectl exec bind-mount-options-demo -- sh -c 'cp /bin/ls /tmp/ls && /tmp/ls'
   ```

   خروجی مشابه زیر است:

   ```none
   sh: /tmp/ls: Permission denied
   ```

1. Podای را که برای این تمرین ایجاد کردید حذف کنید:

   ```shell
   kubectl delete pod bind-mount-options-demo
   ```

## {{% heading "whatsnext" %}}

- درباره‌ی [گزینه‌های bind mount](/docs/concepts/storage/volumes/#bind-mount-options) برای حجم‌ها بیشتر بیاموزید.

---
title: تغییر StorageClass پیش‌فرض
content_type: task
weight: 90
---

<!-- overview -->
این صفحه نشان می‌دهد چگونه کلاس ذخیره‌سازی (Storage Class) پیش‌فرض را تغییر دهید؛ کلاسی که برای تأمین حجم‌ها (volume) برای PersistentVolumeClaimهایی به کار می‌رود که نیازمندی خاصی ندارند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## چرا کلاس ذخیره‌سازی پیش‌فرض را تغییر دهیم؟

بسته به روش نصب، ممکن است کلاستر کوبرنتیز شما همراه با یک StorageClass موجود مستقر شود که به‌عنوان پیش‌فرض علامت‌گذاری شده است. سپس از این StorageClass پیش‌فرض برای تأمین پویای ذخیره‌سازی برای PersistentVolumeClaimهایی استفاده می‌شود که به کلاس ذخیره‌سازی مشخصی نیاز ندارند. برای جزئیات بیشتر،
[مستندات PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
را ببینید.

ممکن است StorageClass پیش‌فرضی که از پیش نصب شده است با بار کاری مورد انتظار شما تناسب چندانی نداشته باشد؛ برای مثال، ممکن است ذخیره‌سازی‌ای تأمین کند که بیش از حد گران است. در این صورت، می‌توانید StorageClass پیش‌فرض را تغییر دهید یا آن را به‌طور کامل غیرفعال کنید تا از تأمین پویای ذخیره‌سازی جلوگیری شود.

ممکن است حذف StorageClass پیش‌فرض کارساز نباشد، زیرا ممکن است مدیر افزونه‌ها (addon manager) که در کلاستر شما اجرا می‌شود، آن را به‌طور خودکار دوباره ایجاد کند. برای جزئیات مربوط به مدیر افزونه‌ها و نحوهٔ غیرفعال کردن هر افزونه، لطفاً به مستندات روش نصب خود مراجعه کنید.

## تغییر StorageClass پیش‌فرض

1. فهرست StorageClassهای کلاستر خود را بگیرید:

   ```bash
   kubectl get storageclass
   ```

   خروجی مشابه زیر است:

   ```bash
   NAME                 PROVISIONER               AGE
   standard (default)   kubernetes.io/gce-pd      1d
   gold                 kubernetes.io/gce-pd      1d
   ```

   StorageClass پیش‌فرض با `(default)` مشخص شده است.

1. StorageClass پیش‌فرض را به‌عنوان غیرپیش‌فرض علامت‌گذاری کنید:

   در StorageClass پیش‌فرض، حاشیه‌نویسی (annotation)
   `storageclass.kubernetes.io/is-default-class` برابر با `true` تنظیم شده است. هر مقدار دیگر یا نبودِ این حاشیه‌نویسی به‌معنای `false` تفسیر می‌شود.

   برای علامت‌گذاری یک StorageClass به‌عنوان غیرپیش‌فرض، باید مقدار آن را به `false` تغییر دهید:

   ```bash
   kubectl patch storageclass standard -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
   ```

   در این دستور، `standard` نام StorageClass انتخابی شماست.

1. یک StorageClass را به‌عنوان پیش‌فرض علامت‌گذاری کنید:

   مشابه مرحلهٔ قبل، باید حاشیه‌نویسی
   `storageclass.kubernetes.io/is-default-class=true` را اضافه یا تنظیم کنید.

   ```bash
   kubectl patch storageclass gold -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
   ```

   توجه داشته باشید که می‌توانید چند `StorageClass` را به‌عنوان پیش‌فرض علامت‌گذاری کنید. اگر بیش از یک `StorageClass` به‌عنوان پیش‌فرض علامت‌گذاری شده باشد، هر `PersistentVolumeClaim` که `storageClassName` آن به‌صراحت تعریف نشده باشد، با استفاده از جدیدترین `StorageClass` پیش‌فرض ایجادشده ساخته می‌شود.
   وقتی یک `PersistentVolumeClaim` با `volumeName` مشخص ایجاد می‌شود، اگر `storageClassName` حجم ایستا با `StorageClass` موجود در `PersistentVolumeClaim` مطابقت نداشته باشد، این `PersistentVolumeClaim` در وضعیت معلق (pending) باقی می‌ماند.

1. بررسی کنید که StorageClass انتخابی شما پیش‌فرض شده باشد:

   ```bash
   kubectl get storageclass
   ```

   خروجی مشابه زیر است:

   ```bash
   NAME             PROVISIONER               AGE
   standard         kubernetes.io/gce-pd      1d
   gold (default)   kubernetes.io/gce-pd      1d
   ```

## {{% heading "whatsnext" %}}

* دربارهٔ [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) بیشتر بیاموزید.

---
title: تولید مستندات مرجع برای متریک‌ها
content_type: task
weight: 100
---

<!-- overview -->

این صفحه نحوهٔ تولید مستندات مرجع متریک‌ها را نشان می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## کلون کردن مخزن کوبرنتیز

تولید متریک‌ها در مخزن کوبرنتیز انجام می‌شود.
برای کلون کردن مخزن، ابتدا به دایرکتوری‌ای بروید که می‌خواهید نسخهٔ کلون‌شده در آن قرار بگیرد.

سپس دستور زیر را اجرا کنید:

```shell
git clone https://www.github.com/kubernetes/kubernetes 
```

با این کار، پوشه‌ای به نام `kubernetes` در دایرکتوری کاری فعلی شما ایجاد می‌شود.

## تولید متریک‌ها

در مخزن کلون‌شدهٔ کوبرنتیز، دایرکتوری `test/instrumentation/documentation` را پیدا کنید.
مستندات متریک‌ها در این دایرکتوری تولید می‌شود.

در هر انتشار، متریک‌های جدیدی اضافه می‌شوند.
پس از اجرای اسکریپت تولید مستندات متریک‌ها، این مستندات را در وب‌سایت کوبرنتیز کپی کنید و
مستندات به‌روزشدهٔ متریک‌ها را منتشر کنید.

برای تولید جدیدترین متریک‌ها، مطمئن شوید که در ریشهٔ دایرکتوری کلون‌شدهٔ کوبرنتیز قرار دارید.
سپس دستور زیر را اجرا کنید:

```shell
./test/instrumentation/update-documentation.sh
```

برای بررسی تغییرات، دستور زیر را اجرا کنید:

```shell
git status
```

خروجی مشابه زیر است:

```
./test/instrumentation/documentation/documentation.md
./test/instrumentation/documentation/documentation-list.yaml
```

## کپی کردن فایل مستندات تولیدشدهٔ متریک‌ها در مخزن وب‌سایت کوبرنتیز

1. متغیر محیطی ریشهٔ وب‌سایت کوبرنتیز را تنظیم کنید.

   برای تنظیم ریشهٔ وب‌سایت، دستور زیر را اجرا کنید:

   ```shell
   export WEBSITE_ROOT=<path to website root>
   ```

2. فایل متریک‌های تولیدشده را در مخزن وب‌سایت کوبرنتیز کپی کنید.

   ```shell
   cp ./test/instrumentation/documentation/documentation.md "${WEBSITE_ROOT}/content/en/docs/reference/instrumentation/metrics.md"
   ```

   {{< note >}}
   اگر با خطا مواجه شدید، بررسی کنید که مجوز کپی کردن فایل را دارید.
   برای برگرداندن مالکیت فایل به کاربر خودتان می‌توانید از `chown` استفاده کنید.
   {{< /note >}}

## ایجاد درخواست ادغام (pull request)

برای ایجاد درخواست ادغام، دستورالعمل‌های صفحهٔ [باز کردن درخواست ادغام](/docs/contribute/new-content/open-a-pr/) را دنبال کنید.

## {{% heading "whatsnext" %}}

* [مشارکت در بالادست](/docs/contribute/generate-ref-docs/contribute-upstream/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)

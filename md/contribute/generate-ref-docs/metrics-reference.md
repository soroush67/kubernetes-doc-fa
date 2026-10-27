---
title: تولید مستندات مرجع برای متریک‌ها
content_type: task
weight: 100
---

<!-- overview -->

این صفحه روش تولید مستندات مرجع متریک‌ها را نشان می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## کلون کردن مخزن کوبرنتیز

تولید متریک‌ها در مخزن کوبرنتیز انجام می‌شود.
برای کلون کردن مخزن، به پوشه‌ای بروید که می‌خواهید کلون در آن ایجاد شود.

سپس دستور زیر را اجرا کنید:

```shell
git clone https://www.github.com/kubernetes/kubernetes 
```

این کار یک پوشه `kubernetes` در دایرکتوری کاری فعلی شما ایجاد می‌کند.

## تولید متریک‌ها

در مخزن کلون‌شده کوبرنتیز، دایرکتوری
`test/instrumentation/documentation` را پیدا کنید.
مستندات متریک‌ها در این دایرکتوری تولید می‌شود.

با هر نسخه، متریک‌های جدیدی اضافه می‌شوند.
پس از اجرای اسکریپت تولید مستندات متریک‌ها، مستندات متریک‌ها را به وب‌سایت کوبرنتیز کپی کنید و
مستندات به‌روزشده متریک‌ها را منتشر کنید.

برای تولید آخرین متریک‌ها، مطمئن شوید که در ریشه دایرکتوری کلون‌شده کوبرنتیز قرار دارید.
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

## کپی کردن فایل مستندات تولیدشده متریک‌ها به مخزن وب‌سایت کوبرنتیز

1. متغیر محیطی ریشه وب‌سایت کوبرنتیز را تنظیم کنید.

   برای تنظیم ریشه وب‌سایت، دستور زیر را اجرا کنید:

   ```shell
   export WEBSITE_ROOT=<path to website root>
   ```

2. فایل متریک‌های تولیدشده را به مخزن وب‌سایت کوبرنتیز کپی کنید.

   ```shell
   cp ./test/instrumentation/documentation/documentation.md "${WEBSITE_ROOT}/content/en/docs/reference/instrumentation/metrics.md"
   ```

   {{< note >}}
   اگر با خطا مواجه شدید، بررسی کنید که مجوز کپی کردن فایل را دارید.
   می‌توانید با استفاده از `chown` مالکیت فایل را به کاربر خودتان بازگردانید.
   {{< /note >}}

## ایجاد یک pull request

برای ایجاد یک pull request، دستورالعمل‌های موجود در [باز کردن یک pull request](/docs/contribute/new-content/open-a-pr/) را دنبال کنید.

## {{% heading "whatsnext" %}}

* [مشارکت در پروژه بالادستی (Contribute-upstream)](/docs/contribute/generate-ref-docs/contribute-upstream/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورات kubectl](/docs/contribute/generate-ref-docs/kubectl/)

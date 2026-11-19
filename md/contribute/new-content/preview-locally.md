---
title: پیش‌نمایش محلی
content_type: concept
weight: 11
---

<!-- overview -->

توصیه می‌شود پیش از آنکه [یک PR جدید باز کنید](/docs/contribute/new-content/open-a-pr/)،
تغییرات خود را پیش‌نمایش کنید. با پیش‌نمایش می‌توانید خطاهای ساخت (build) یا مشکلات قالب‌بندی
markdown را پیدا کنید.

## پیش‌نمایش محلی تغییرات {#preview-locally}

می‌توانید ایمیج کانتینر وب‌سایت را بسازید یا Hugo را به‌صورت محلی اجرا کنید. ساختن ایمیج کانتینر
کندتر است، اما [شورت‌کدهای Hugo](/docs/contribute/style/hugo-shortcodes/) را نمایش می‌دهد که
می‌تواند برای اشکال‌زدایی مفید باشد.

{{< tabs name="tab_with_hugo" >}}
{{% tab name="Hugo در یک کانتینر" %}}

{{< note >}}
دستورهای زیر به‌طور پیش‌فرض از Docker به‌عنوان موتور کانتینر استفاده می‌کنند. برای تغییر این رفتار،
متغیر محیطی `CONTAINER_ENGINE` را تنظیم کنید.
{{< /note >}}

1. ایمیج کانتینر را به‌صورت محلی بسازید  
   _این مرحله فقط زمانی لازم است که تغییری در خودِ ابزار Hugo را آزمایش می‌کنید_

   ```shell
   # Run this in a terminal (if required)
   make container-image
   ```

1. وابستگی‌های زیرماژول‌ها (submodule) را در مخزن محلی خود دریافت کنید:

   ```shell
   # Run this in a terminal
   make module-init
   ```

1. Hugo را در یک کانتینر اجرا کنید:

   ```shell
   # Run this in a terminal
   make container-serve
   ```

1. در مرورگر وب به نشانی `http://localhost:1313` بروید. Hugo تغییرات را زیر نظر می‌گیرد و
   در صورت نیاز سایت را دوباره می‌سازد.

1. برای متوقف کردن نمونهٔ محلی Hugo، به ترمینال برگردید و `Ctrl+C` را بزنید،
   یا پنجرهٔ ترمینال را ببندید.

{{% /tab %}}
{{% tab name="Hugo در خط فرمان" %}}

به‌عنوان راه دیگر، می‌توانید دستور `hugo` را روی رایانهٔ خود نصب و از آن استفاده کنید:

1. نسخه‌های [Hugo (ویرایش Extended)](https://gohugo.io/getting-started/installing/) و [Node](https://nodejs.org/en) را که در
   [`website/netlify.toml`](https://raw.githubusercontent.com/kubernetes/website/main/netlify.toml) مشخص شده‌اند نصب کنید.

1. همهٔ وابستگی‌ها را نصب کنید:

   ```shell
   npm ci
   ```

1. در یک ترمینال به مخزن وب‌سایت کوبرنتیز بروید و سرور Hugo را اجرا کنید:

   ```shell
   cd <path_to_your_repo>/website
   make serve
   ```
   اگر از سیستم Windows استفاده می‌کنید یا نمی‌توانید دستور `make` را اجرا کنید، از دستور زیر استفاده کنید:

   ```
   hugo server --config hugo.toml,hugo.server.toml --buildFuture
   ```

1. در مرورگر وب به نشانی `http://localhost:1313` بروید. Hugo تغییرات را زیر نظر می‌گیرد و
   در صورت نیاز سایت را دوباره می‌سازد.

1. برای متوقف کردن نمونهٔ محلی Hugo، به ترمینال برگردید و `Ctrl+C` را بزنید،
   یا پنجرهٔ ترمینال را ببندید.

{{% /tab %}}
{{< /tabs >}}

## عیب‌یابی {#troubleshooting}

### error: failed to transform resource: TOCSS: failed to transform "scss/main.scss" (text/x-scss): this feature is not available in your current Hugo version

به دلایل فنی، Hugo در دو مجموعه فایل اجرایی (binary) منتشر می‌شود. وب‌سایت فعلی
فقط بر پایهٔ نسخهٔ **Hugo Extended** اجرا می‌شود. در [صفحهٔ انتشارها](https://github.com/gohugoio/hugo/releases)
به دنبال آرشیوهایی بگردید که در نامشان `extended` آمده است. برای اطمینان، دستور `hugo version`
را اجرا کنید و به دنبال واژهٔ `extended` بگردید.

### عیب‌یابی خطای «too many open files» در macOS

اگر دستور `make serve` را در macOS اجرا کنید و با خطای زیر روبه‌رو شوید:

```bash
ERROR 2020/08/01 19:09:18 Error: listen tcp 127.0.0.1:1313: socket: too many open files
make: *** [serve] Error 1
```

ابتدا محدودیت فعلی تعداد فایل‌های باز را بررسی کنید:

`launchctl limit maxfiles`

سپس دستورهای زیر را اجرا کنید (برگرفته از <https://gist.github.com/tombigel/d503800a282fcadbee14b537735d202c>):

```shell
#!/bin/sh

# These are the original gist links, linking to my gists now.
# curl -O https://gist.githubusercontent.com/a2ikm/761c2ab02b7b3935679e55af5d81786a/raw/ab644cb92f216c019a2f032bbf25e258b01d87f9/limit.maxfiles.plist
# curl -O https://gist.githubusercontent.com/a2ikm/761c2ab02b7b3935679e55af5d81786a/raw/ab644cb92f216c019a2f032bbf25e258b01d87f9/limit.maxproc.plist

curl -O https://gist.githubusercontent.com/tombigel/d503800a282fcadbee14b537735d202c/raw/ed73cacf82906fdde59976a0c8248cce8b44f906/limit.maxfiles.plist
curl -O https://gist.githubusercontent.com/tombigel/d503800a282fcadbee14b537735d202c/raw/ed73cacf82906fdde59976a0c8248cce8b44f906/limit.maxproc.plist

sudo mv limit.maxfiles.plist /Library/LaunchDaemons
sudo mv limit.maxproc.plist /Library/LaunchDaemons

sudo chown root:wheel /Library/LaunchDaemons/limit.maxfiles.plist
sudo chown root:wheel /Library/LaunchDaemons/limit.maxproc.plist

sudo launchctl load -w /Library/LaunchDaemons/limit.maxfiles.plist
```

این روش هم در macOS Catalina و هم در macOS Mojave کار می‌کند.

### خطای Unable to find image 'gcr.io/k8s-staging-sig-docs/k8s-website-hugo:VERSION' locally

اگر دستور `make container-serve` را اجرا کنید و این خطا را ببینید، ممکن است علت آن
تغییرات محلی در فایل‌های مشخصی باشد که در `$IMAGE_VERSION` فایل `Makefile`
[تعریف شده‌اند](https://github.com/kubernetes/website/blob/main/Makefile#L10).

نسخه‌گذاری ایمیج وب‌سایت شامل یک hash است که بر اساس محتوای فایل‌های فهرست‌شده
تولید می‌شود. برای نمونه، اگر hash این فایل‌ها `1b9242684415` باشد،
نام ایمیج وب‌سایت `k8s-website-hugo:v0.133.0-1b9242684415` خواهد بود.
اجرای `make container-serve` تلاش می‌کند چنین ایمیجی را از GCR وب‌سایت کوبرنتیز
دریافت کند. اگر این نسخه، نسخهٔ فعلی نباشد، خطایی می‌بینید که می‌گوید این ایمیج وجود ندارد.

اگر لازم است این فایل‌ها را تغییر دهید و وب‌سایت را پیش‌نمایش کنید،
باید به‌جای دریافت ایمیج ازپیش‌ساخته، ایمیج محلی خود را بسازید.
برای این کار، دستور `make container-image` را اجرا کنید.

### مشکلات دیگر

اگر در اجرای محلی وب‌سایت یا پیش‌نمایش تغییرات خود با مشکل دیگری روبه‌رو شدید،
می‌توانید در مخزن GitHub با نام `kubernetes/website` [یک issue باز کنید](https://github.com/kubernetes/website/issues/new/choose).

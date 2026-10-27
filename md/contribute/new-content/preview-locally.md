---
title: پیش‌نمایش محلی
content_type: concept
weight: 11
---

<!-- overview -->

پیش از آنکه [یک PR جدید باز کنید](/docs/contribute/new-content/open-a-pr/)،
توصیه می‌شود تغییرات خود را پیش‌نمایش کنید. پیش‌نمایش به شما کمک می‌کند خطاهای ساخت
یا مشکلات قالب‌بندی markdown را پیش از ارسال شناسایی کنید.

## پیش‌نمایش محلی تغییرات {#preview-locally}

می‌توانید ایمیج کانتینر وب‌سایت را بسازید یا Hugo را به‌صورت محلی اجرا کنید. ساخت ایمیج کانتینر
کندتر است، اما [شورت‌کدهای Hugo](/docs/contribute/style/hugo-shortcodes/) را نمایش می‌دهد که
می‌تواند برای اشکال‌زدایی مفید باشد.

{{< tabs name="tab_with_hugo" >}}
{{% tab name="Hugo in a container" %}}

{{< note >}}
دستورهای زیر به‌طور پیش‌فرض از Docker به‌عنوان موتور کانتینر استفاده می‌کنند. برای تغییر این رفتار،
متغیر محیطی `CONTAINER_ENGINE` را تنظیم کنید.
{{< /note >}}

1. ایمیج کانتینر را به‌صورت محلی بسازید  
   _این مرحله فقط زمانی لازم است که تغییری را در خود ابزار Hugo آزمایش می‌کنید_

   ```shell
   # Run this in a terminal (if required)
   make container-image
   ```

1. وابستگی‌های submodule را در مخزن محلی خود دریافت کنید:

   ```shell
   # Run this in a terminal
   make module-init
   ```

1. Hugo را در یک کانتینر اجرا کنید:

   ```shell
   # Run this in a terminal
   make container-serve
   ```

1. در یک مرورگر وب به نشانی `http://localhost:1313` بروید. Hugo تغییرات را
   زیر نظر دارد و در صورت نیاز، سایت را دوباره می‌سازد.

1. برای متوقف کردن نمونه محلی Hugo، به ترمینال بازگردید و `Ctrl+C` را تایپ کنید
   یا پنجره ترمینال را ببندید.

{{% /tab %}}
{{% tab name="Hugo on the command line" %}}

به‌طور جایگزین، می‌توانید دستور `hugo` را روی رایانه خود نصب و استفاده کنید:

1. نسخه [Hugo (Extended edition)](https://gohugo.io/getting-started/installing/) و [Node](https://nodejs.org/en) مشخص‌شده در
   [`website/netlify.toml`](https://raw.githubusercontent.com/kubernetes/website/main/netlify.toml) را نصب کنید.

1. وابستگی‌ها را نصب کنید:

   ```shell
   npm ci
   ```

1. در یک ترمینال، به مخزن وب‌سایت کوبرنتیز خود بروید و سرور Hugo را اجرا کنید:

   ```shell
   cd <path_to_your_repo>/website
   make serve
   ```
   اگر از رایانه ویندوزی استفاده می‌کنید یا نمی‌توانید دستور `make` را اجرا کنید، از دستور زیر استفاده کنید:

   ```
   hugo server --config hugo.toml,hugo.server.toml --buildFuture
   ```

1. در یک مرورگر وب به نشانی `http://localhost:1313` بروید. Hugo تغییرات را
   زیر نظر دارد و در صورت نیاز، سایت را دوباره می‌سازد.

1. برای متوقف کردن نمونه محلی Hugo، به ترمینال بازگردید و `Ctrl+C` را تایپ کنید
   یا پنجره ترمینال را ببندید.

{{% /tab %}}
{{< /tabs >}}

## عیب‌یابی {#troubleshooting}

### error: failed to transform resource: TOCSS: failed to transform "scss/main.scss" (text/x-scss): this feature is not available in your current Hugo version

به دلایل فنی، Hugo در دو مجموعه فایل باینری عرضه می‌شود. وب‌سایت فعلی
فقط بر پایه نسخه **Hugo Extended** اجرا می‌شود. در [صفحه انتشارها](https://github.com/gohugoio/hugo/releases)
به‌دنبال آرشیوهایی باشید که در نام آن‌ها `extended` وجود دارد. برای اطمینان، دستور `hugo version` را اجرا کنید
و دنبال واژه `extended` بگردید.

### عیب‌یابی خطای «too many open files» در macOS

اگر `make serve` را روی macOS اجرا کنید و خطای زیر را دریافت کنید:

```bash
ERROR 2020/08/01 19:09:18 Error: listen tcp 127.0.0.1:1313: socket: too many open files
make: *** [serve] Error 1
```

ابتدا محدودیت فعلی فایل‌های باز را بررسی کنید:

`launchctl limit maxfiles`

سپس دستورهای زیر را اجرا کنید (اقتباس‌شده از <https://gist.github.com/tombigel/d503800a282fcadbee14b537735d202c>):

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

این روش هم برای macOS Catalina و هم برای Mojave کار می‌کند.

### Unable to find image 'gcr.io/k8s-staging-sig-docs/k8s-website-hugo:VERSION' locally

اگر `make container-serve` را اجرا کنید و این خطا را ببینید، ممکن است به‌دلیل
تغییرات محلی در فایل‌های مشخصی باشد که در `$IMAGE_VERSION` فایل `Makefile`
[تعریف شده‌اند](https://github.com/kubernetes/website/blob/main/Makefile#L10).

نسخه‌بندی ایمیج وب‌سایت شامل یک هش است که بر اساس
محتوای فایل‌های فهرست‌شده تولید می‌شود. برای مثال، اگر `1b9242684415` هش
این فایل‌ها باشد، ایمیج وب‌سایت `k8s-website-hugo:v0.133.0-1b9242684415` نام خواهد داشت.
اجرای `make container-serve` تلاش می‌کند چنین ایمیجی را از GCR وب‌سایت
کوبرنتیز دریافت کند. اگر این نسخه، نسخه فعلی نباشد، خطایی می‌بینید که
می‌گوید این ایمیج وجود ندارد.

اگر لازم است در این فایل‌ها تغییر ایجاد کنید و وب‌سایت را پیش‌نمایش کنید،
باید به‌جای دریافت یک ایمیج از پیش ساخته‌شده، ایمیج محلی خود را بسازید.
برای این کار، دستور `make container-image` را اجرا کنید.

### مشکلات دیگر

اگر هنگام اجرای محلی وب‌سایت و/یا پیش‌نمایش تغییرات خود با مشکلات دیگری روبه‌رو شدید،
می‌توانید در مخزن GitHub با نام `kubernetes/website` [یک issue باز کنید](https://github.com/kubernetes/website/issues/new/choose).

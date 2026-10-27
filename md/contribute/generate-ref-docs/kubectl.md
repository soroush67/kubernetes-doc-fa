---
title: تولید مستندات مرجع برای دستورهای kubectl
content_type: task
weight: 90
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه مرجع دستورهای `kubectl` را تولید کنید.

{{< note >}}
این مبحث نشان می‌دهد چگونه مستندات مرجع را برای
[دستورهای kubectl](/docs/reference/generated/kubectl/kubectl-commands) مانند
[kubectl apply](/docs/reference/generated/kubectl/kubectl-commands#apply) و
[kubectl taint](/docs/reference/generated/kubectl/kubectl-commands#taint) تولید کنید.
این مبحث نشان نمی‌دهد که چگونه صفحه مرجع گزینه‌های
[kubectl](/docs/reference/generated/kubectl/kubectl-commands/)
را تولید کنید. برای دستورالعمل تولید صفحه مرجع گزینه‌های kubectl،
به
[تولید صفحات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
مراجعه کنید.
{{< /note >}}

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخزن‌های محلی

یک فضای کاری محلی ایجاد کنید و `GOPATH` را تنظیم کنید:

```shell
mkdir -p $HOME/<workspace>

export GOPATH=$HOME/<workspace>
```

یک کلون محلی از مخزن‌های زیر دریافت کنید:

```shell
go get -u github.com/spf13/pflag
go get -u github.com/spf13/cobra
go get -u gopkg.in/yaml.v2
go get -u github.com/kubernetes-sigs/reference-docs
```

اگر هنوز مخزن kubernetes/website را ندارید، اکنون آن را دریافت کنید:

```shell
git clone https://github.com/<your-username>/website $GOPATH/src/github.com/<your-username>/website
```

یک کلون از مخزن kubernetes/kubernetes را با نام k8s.io/kubernetes دریافت کنید:

```shell
git clone https://github.com/kubernetes/kubernetes $GOPATH/src/k8s.io/kubernetes
```

بسته spf13 را از `$GOPATH/src/k8s.io/kubernetes/vendor/github.com` حذف کنید:

```shell
rm -rf $GOPATH/src/k8s.io/kubernetes/vendor/github.com/spf13
```

مخزن kubernetes/kubernetes کد منبع `kubectl` و `kustomize` را فراهم می‌کند.

* دایرکتوری پایه کلون خود از مخزن
  [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) را مشخص کنید.
  برای مثال، اگر مرحله قبل را برای دریافت مخزن دنبال کرده باشید،
  دایرکتوری پایه شما `$GOPATH/src/k8s.io/kubernetes` است.
  در مراحل بعدی، این دایرکتوری پایه با نام `<k8s-base>` به آن اشاره می‌شود.

* دایرکتوری پایه کلون خود از مخزن
  [kubernetes/website](https://github.com/kubernetes/website) را مشخص کنید.
  برای مثال، اگر مرحله قبل را برای دریافت مخزن دنبال کرده باشید،
  دایرکتوری پایه شما `$GOPATH/src/github.com/<your-username>/website` است.
  در مراحل بعدی، این دایرکتوری پایه با نام `<web-base>` به آن اشاره می‌شود.

* دایرکتوری پایه کلون خود از مخزن
  [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) را مشخص کنید.
  برای مثال، اگر مرحله قبل را برای دریافت مخزن دنبال کرده باشید،
  دایرکتوری پایه شما `$GOPATH/src/github.com/kubernetes-sigs/reference-docs` است.
  در مراحل بعدی، این دایرکتوری پایه با نام `<rdocs-base>` به آن اشاره می‌شود.

در مخزن محلی k8s.io/kubernetes خود، شاخه مورد نظر را checkout کنید
و مطمئن شوید که به‌روز است. برای مثال، اگر می‌خواهید مستندات کوبرنتیز
{{< skew prevMinorVersion >}}.0 را تولید کنید، می‌توانید از این دستورها استفاده کنید:

```shell
cd <k8s-base>
git checkout v{{< skew prevMinorVersion >}}.0
git pull https://github.com/kubernetes/kubernetes {{< skew prevMinorVersion >}}.0
```

اگر نیازی به ویرایش کد منبع `kubectl` ندارید، دستورالعمل‌های
[تنظیم متغیرهای ساخت](#set-build-variables) را دنبال کنید.

## ویرایش کد منبع kubectl

مستندات مرجع دستورهای kubectl به‌صورت خودکار از کد منبع kubectl تولید می‌شود.
اگر می‌خواهید مستندات مرجع را تغییر دهید، گام نخست این است که یک یا چند کامنت را
در کد منبع kubectl تغییر دهید. این تغییر را در مخزن محلی kubernetes/kubernetes خود
اعمال کنید و سپس یک pull request به شاخه master مخزن
[github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) ارسال کنید.

[PR 56673](https://github.com/kubernetes/kubernetes/pull/56673/files)
نمونه‌ای از یک pull request است که یک غلط تایپی را در کد منبع kubectl اصلاح می‌کند.

pull request خود را پیگیری کنید و به نظرات بازبینان پاسخ دهید. تا زمانی که
pull request شما در شاخه هدف مخزن kubernetes/kubernetes ادغام نشده است،
آن را پیگیری کنید.

## Cherry pick کردن تغییر خود در یک شاخه انتشار

تغییر شما اکنون در شاخه master است که برای توسعه نسخه بعدی کوبرنتیز استفاده می‌شود.
اگر می‌خواهید تغییر شما در مستندات نسخه‌ای از کوبرنتیز که قبلاً منتشر شده است
نیز ظاهر شود، باید پیشنهاد دهید که تغییر شما در شاخه انتشار cherry pick شود.

برای مثال، فرض کنید شاخه master برای توسعه کوبرنتیز {{< skew currentVersion >}}
استفاده می‌شود و می‌خواهید تغییر خود را به شاخه release-{{< skew prevMinorVersion >}}
backport کنید. برای مشاهده دستورالعمل انجام این کار، به
[پیشنهاد یک Cherry Pick](https://git.k8s.io/community/contributors/devel/sig-release/cherry-picks.md)
مراجعه کنید.

pull request مربوط به cherry-pick را تا زمانی که در شاخه انتشار ادغام شود، پیگیری کنید.

{{< note >}}
برای پیشنهاد یک cherry pick لازم است مجوز تنظیم برچسب و milestone را
در pull request خود داشته باشید. اگر این مجوزها را ندارید، باید با فردی همکاری کنید
که بتواند برچسب و milestone را برای شما تنظیم کند.
{{< /note >}}

## تنظیم متغیرهای ساخت

به `<rdocs-base>` بروید. در خط فرمان خود، متغیرهای محیطی زیر را تنظیم کنید.

* `K8S_ROOT` را روی `<k8s-base>` تنظیم کنید.
* `K8S_WEBROOT` را روی `<web-base>` تنظیم کنید.
* `K8S_RELEASE` را روی نسخه‌ای از مستندات که می‌خواهید بسازید تنظیم کنید.
  برای مثال، اگر می‌خواهید مستندات کوبرنتیز {{< skew prevMinorVersion >}} را بسازید،
  `K8S_RELEASE` را روی {{< skew prevMinorVersion >}} تنظیم کنید.

برای مثال:

```shell
export K8S_WEBROOT=$GOPATH/src/github.com/<your-username>/website
export K8S_ROOT=$GOPATH/src/k8s.io/kubernetes
export K8S_RELEASE={{< skew prevMinorVersion >}}
```

## ایجاد یک دایرکتوری نسخه‌دار

هدف ساخت `createversiondirs` یک دایرکتوری نسخه‌دار ایجاد می‌کند
و فایل‌های پیکربندی مرجع kubectl را در آن کپی می‌کند.
نام دایرکتوری نسخه‌دار از الگوی `v<major>_<minor>` پیروی می‌کند.

در دایرکتوری `<rdocs-base>`، هدف ساخت زیر را اجرا کنید:

```shell
cd <rdocs-base>
make createversiondirs
```

## Checkout کردن یک تگ انتشار در k8s.io/kubernetes

در مخزن محلی `<k8s-base>` خود، شاخه‌ای را checkout کنید که نسخه‌ای از کوبرنتیز
را که می‌خواهید مستند کنید در بر دارد. برای مثال، اگر می‌خواهید مستندات کوبرنتیز
{{< skew prevMinorVersion >}}.0 را تولید کنید، تگ
`v{{< skew prevMinorVersion >}}` را checkout کنید. مطمئن شوید شاخه محلی شما به‌روز است.

```shell
cd <k8s-base>
git checkout v{{< skew prevMinorVersion >}}.0
git pull https://github.com/kubernetes/kubernetes v{{< skew prevMinorVersion >}}.0
```

## اجرای کد تولید مستندات

در `<rdocs-base>` محلی خود، هدف ساخت `copycli` را اجرا کنید. این دستور با دسترسی `root` اجرا می‌شود:

```shell
cd <rdocs-base>
make copycli
```

دستور `copycli` دایرکتوری موقت ساخت را پاک می‌کند، فایل‌های دستورهای kubectl را تولید می‌کند
و صفحه HTML تجمیع‌شده مرجع دستورهای kubectl و دارایی‌های (assets) آن را به `<web-base>` کپی می‌کند.

## یافتن فایل‌های تولیدشده

بررسی کنید که این دو فایل تولید شده باشند:

```shell
[ -e "<rdocs-base>/gen-kubectldocs/generators/build/index.html" ] && echo "index.html built" || echo "no index.html"
[ -e "<rdocs-base>/gen-kubectldocs/generators/build/navData.js" ] && echo "navData.js built" || echo "no navData.js"
```

## یافتن فایل‌های کپی‌شده

بررسی کنید که همه فایل‌های تولیدشده در `<web-base>` شما کپی شده باشند:

```shell
cd <web-base>
git status
```

خروجی باید شامل فایل‌های تغییریافته زیر باشد:

```
static/docs/reference/generated/kubectl/kubectl-commands.html
static/docs/reference/generated/kubectl/navData.js
```

خروجی ممکن است شامل موارد زیر نیز باشد:

```
static/docs/reference/generated/kubectl/scroll.js
static/docs/reference/generated/kubectl/stylesheet.css
static/docs/reference/generated/kubectl/tabvisibility.js
static/docs/reference/generated/kubectl/node_modules/bootstrap/dist/css/bootstrap.min.css
static/docs/reference/generated/kubectl/node_modules/highlight.js/styles/default.css
static/docs/reference/generated/kubectl/node_modules/jquery.scrollto/jquery.scrollTo.min.js
static/docs/reference/generated/kubectl/node_modules/jquery/dist/jquery.min.js
static/docs/reference/generated/kubectl/node_modules/font-awesome/css/font-awesome.min.css
```

## آزمایش محلی مستندات

مستندات کوبرنتیز را در `<web-base>` محلی خود بسازید.

```shell
cd <web-base>
git submodule update --init --recursive --depth 1 # if not already done
make container-serve
```

[پیش‌نمایش محلی](https://localhost:1313/docs/reference/generated/kubectl/kubectl-commands/) را مشاهده کنید.

## افزودن و commit کردن تغییرات در kubernetes/website

برای commit کردن فایل‌ها، `git add` و `git commit` را اجرا کنید.

## ایجاد یک pull request

یک pull request به مخزن `kubernetes/website` ایجاد کنید. pull request خود را
پیگیری کنید و در صورت نیاز به نظرات بازبینی پاسخ دهید. تا زمانی که
pull request شما ادغام نشده است، آن را پیگیری کنید.

چند دقیقه پس از ادغام pull request شما، مباحث مرجع به‌روزشده شما
در [مستندات منتشرشده](/docs/home) قابل مشاهده خواهند بود.

## {{% heading "whatsnext" %}}

* [شروع سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)

---
title: تولید مستندات مرجع برای فرمان‌های kubectl
content_type: task
weight: 90
---

<!-- overview -->

این صفحه نحوهٔ تولید مرجع فرمان‌های `kubectl` را نشان می‌دهد.

{{< note >}}
این مبحث نحوهٔ تولید مستندات مرجع برای
[فرمان‌های kubectl](/docs/reference/generated/kubectl/kubectl-commands) مانند
[kubectl apply](/docs/reference/generated/kubectl/kubectl-commands#apply) و
[kubectl taint](/docs/reference/generated/kubectl/kubectl-commands#taint) را نشان می‌دهد.
این مبحث نحوهٔ تولید صفحهٔ مرجع گزینه‌های
[kubectl](/docs/reference/generated/kubectl/kubectl-commands/)
را توضیح نمی‌دهد. برای آشنایی با نحوهٔ تولید صفحهٔ مرجع گزینه‌های kubectl، به
[تولید صفحات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
مراجعه کنید.
{{< /note >}}

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخزن‌های محلی

یک فضای کاری محلی ایجاد کنید و `GOPATH` خود را تنظیم کنید:

```shell
mkdir -p $HOME/<workspace>

export GOPATH=$HOME/<workspace>
```

یک نسخهٔ محلی (clone) از مخزن‌های زیر تهیه کنید:

```shell
go get -u github.com/spf13/pflag
go get -u github.com/spf13/cobra
go get -u gopkg.in/yaml.v2
go get -u github.com/kubernetes-sigs/reference-docs
```

اگر مخزن kubernetes/website را هنوز ندارید، اکنون آن را دریافت کنید:

```shell
git clone https://github.com/<your-username>/website $GOPATH/src/github.com/<your-username>/website
```

یک نسخه از مخزن kubernetes/kubernetes را با نام k8s.io/kubernetes تهیه کنید:

```shell
git clone https://github.com/kubernetes/kubernetes $GOPATH/src/k8s.io/kubernetes
```

بستهٔ spf13 را از مسیر `$GOPATH/src/k8s.io/kubernetes/vendor/github.com` حذف کنید:

```shell
rm -rf $GOPATH/src/k8s.io/kubernetes/vendor/github.com/spf13
```

مخزن kubernetes/kubernetes کد منبع `kubectl` و `kustomize` را فراهم می‌کند.

* پوشهٔ پایهٔ نسخهٔ محلی خود از مخزن
  [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) را مشخص کنید.
  برای مثال، اگر مخزن را با مرحلهٔ قبل دریافت کرده باشید، پوشهٔ پایهٔ شما
  `$GOPATH/src/k8s.io/kubernetes` است.
  در مراحل بعدی، از این پوشهٔ پایه با نام `<k8s-base>` یاد می‌شود.

* پوشهٔ پایهٔ نسخهٔ محلی خود از مخزن
  [kubernetes/website](https://github.com/kubernetes/website) را مشخص کنید.
  برای مثال، اگر مخزن را با مرحلهٔ قبل دریافت کرده باشید، پوشهٔ پایهٔ شما
  `$GOPATH/src/github.com/<your-username>/website` است.
  در مراحل بعدی، از این پوشهٔ پایه با نام `<web-base>` یاد می‌شود.

* پوشهٔ پایهٔ نسخهٔ محلی خود از مخزن
  [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) را مشخص کنید.
  برای مثال، اگر مخزن را با مرحلهٔ قبل دریافت کرده باشید، پوشهٔ پایهٔ شما
  `$GOPATH/src/github.com/kubernetes-sigs/reference-docs` است.
  در مراحل بعدی، از این پوشهٔ پایه با نام `<rdocs-base>` یاد می‌شود.

در مخزن محلی k8s.io/kubernetes، شاخهٔ موردنظر را checkout کنید و مطمئن شوید
که به‌روز است. برای مثال، اگر می‌خواهید مستندات کوبرنتیز
{{< skew prevMinorVersion >}}.0 را تولید کنید، می‌توانید از این فرمان‌ها استفاده کنید:

```shell
cd <k8s-base>
git checkout v{{< skew prevMinorVersion >}}.0
git pull https://github.com/kubernetes/kubernetes {{< skew prevMinorVersion >}}.0
```

اگر نیازی به ویرایش کد منبع `kubectl` ندارید، دستورالعمل‌های بخش
[تنظیم متغیرهای ساخت](#set-build-variables) را دنبال کنید.

## ویرایش کد منبع kubectl

مستندات مرجع فرمان‌های kubectl به‌طور خودکار از کد منبع kubectl تولید می‌شود.
اگر می‌خواهید مستندات مرجع را تغییر دهید، نخستین گام تغییر یک یا چند توضیح (comment)
در کد منبع kubectl است. این تغییر را در مخزن محلی kubernetes/kubernetes خود اعمال کنید
و سپس یک درخواست ادغام (pull request) به شاخهٔ master مخزن
[github.com/kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) ارسال کنید.

[PR 56673](https://github.com/kubernetes/kubernetes/pull/56673/files)
نمونه‌ای از یک درخواست ادغام است که یک اشتباه تایپی را در کد منبع kubectl اصلاح می‌کند.

درخواست ادغام خود را پیگیری کنید و به نظرات بازبینان پاسخ دهید. این پیگیری را تا زمانی
ادامه دهید که درخواست ادغام شما در شاخهٔ هدف مخزن kubernetes/kubernetes ادغام شود.

## انتقال گزینشی (cherry pick) تغییر به یک شاخهٔ انتشار

اکنون تغییر شما در شاخهٔ master قرار دارد که برای توسعهٔ انتشار بعدی کوبرنتیز
استفاده می‌شود. اگر می‌خواهید تغییرتان در مستندات نسخه‌ای از کوبرنتیز که پیش‌تر
منتشر شده است نیز دیده شود، باید پیشنهاد دهید که تغییرتان به‌صورت گزینشی
به شاخهٔ انتشار منتقل شود.

برای مثال، فرض کنید شاخهٔ master برای توسعهٔ کوبرنتیز {{< skew currentVersion >}}
استفاده می‌شود و شما می‌خواهید تغییرتان را به شاخهٔ release-{{< skew prevMinorVersion >}}
منتقل کنید. برای آشنایی با نحوهٔ انجام این کار، به
[پیشنهاد یک انتقال گزینشی](https://git.k8s.io/community/contributors/devel/sig-release/cherry-picks.md)
مراجعه کنید.

درخواست ادغام مربوط به انتقال گزینشی را تا زمان ادغام آن در شاخهٔ انتشار پیگیری کنید.

{{< note >}}
برای پیشنهاد یک انتقال گزینشی، باید مجوز تعیین برچسب و نقطهٔ عطف (milestone)
را در درخواست ادغام خود داشته باشید. اگر این مجوزها را ندارید، باید با فردی همکاری کنید
که بتواند برچسب و نقطهٔ عطف را برای شما تعیین کند.
{{< /note >}}

## تنظیم متغیرهای ساخت

به `<rdocs-base>` بروید و در خط فرمان، متغیرهای محیطی زیر را تنظیم کنید.

* مقدار `K8S_ROOT` را برابر `<k8s-base>` قرار دهید.
* مقدار `K8S_WEBROOT` را برابر `<web-base>` قرار دهید.
* مقدار `K8S_RELEASE` را برابر نسخه‌ای از مستندات قرار دهید که می‌خواهید بسازید.
  برای مثال، اگر می‌خواهید مستندات کوبرنتیز {{< skew prevMinorVersion >}} را بسازید،
  مقدار `K8S_RELEASE` را برابر {{< skew prevMinorVersion >}} قرار دهید.

برای مثال:

```shell
export K8S_WEBROOT=$GOPATH/src/github.com/<your-username>/website
export K8S_ROOT=$GOPATH/src/k8s.io/kubernetes
export K8S_RELEASE={{< skew prevMinorVersion >}}
```

## ایجاد یک پوشهٔ نسخه‌دار

هدف ساخت `createversiondirs` یک پوشهٔ نسخه‌دار ایجاد می‌کند و فایل‌های پیکربندی
مرجع kubectl را در آن کپی می‌کند. نام پوشهٔ نسخه‌دار از الگوی `v<major>_<minor>` پیروی می‌کند.

در پوشهٔ `<rdocs-base>`، هدف ساخت زیر را اجرا کنید:

```shell
cd <rdocs-base>
make createversiondirs
```

## دریافت (checkout) یک برچسب انتشار در k8s.io/kubernetes

در مخزن محلی `<k8s-base>`، شاخه‌ای را checkout کنید که نسخهٔ موردنظر شما از کوبرنتیز
را برای مستندسازی در خود دارد. برای مثال، اگر می‌خواهید مستندات کوبرنتیز
{{< skew prevMinorVersion >}}.0 را تولید کنید، برچسب `v{{< skew prevMinorVersion >}}`
را checkout کنید. مطمئن شوید که شاخهٔ محلی شما به‌روز است.

```shell
cd <k8s-base>
git checkout v{{< skew prevMinorVersion >}}.0
git pull https://github.com/kubernetes/kubernetes v{{< skew prevMinorVersion >}}.0
```

## اجرای کد تولید مستندات

در `<rdocs-base>` محلی خود، هدف ساخت `copycli` را اجرا کنید. این فرمان با کاربر `root` اجرا می‌شود:

```shell
cd <rdocs-base>
make copycli
```

فرمان `copycli` پوشهٔ موقت ساخت را پاک می‌کند، فایل‌های فرمان‌های kubectl را تولید می‌کند
و صفحهٔ HTML گردآوری‌شدهٔ مرجع فرمان‌های kubectl را همراه با فایل‌های جانبی آن در `<web-base>` کپی می‌کند.

## یافتن فایل‌های تولیدشده

بررسی کنید که این دو فایل تولید شده باشند:

```shell
[ -e "<rdocs-base>/gen-kubectldocs/generators/build/index.html" ] && echo "index.html built" || echo "no index.html"
[ -e "<rdocs-base>/gen-kubectldocs/generators/build/navData.js" ] && echo "navData.js built" || echo "no navData.js"
```

## یافتن فایل‌های کپی‌شده

بررسی کنید که همهٔ فایل‌های تولیدشده در `<web-base>` کپی شده باشند:

```shell
cd <web-base>
git status
```

خروجی باید شامل فایل‌های تغییریافتهٔ زیر باشد:

```
static/docs/reference/generated/kubectl/kubectl-commands.html
static/docs/reference/generated/kubectl/navData.js
```

خروجی ممکن است شامل این فایل‌ها نیز باشد:

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

## افزودن و ثبت (commit) تغییرات در kubernetes/website

برای ثبت فایل‌ها، فرمان‌های `git add` و `git commit` را اجرا کنید.

## ایجاد یک درخواست ادغام

یک درخواست ادغام به مخزن `kubernetes/website` ایجاد کنید. درخواست ادغام خود را
پیگیری کنید و در صورت نیاز به نظرات بازبینی پاسخ دهید. این پیگیری را تا زمان
ادغام درخواست ادامه دهید.

چند دقیقه پس از ادغام درخواست شما، مباحث مرجع به‌روزشده در
[مستندات منتشرشده](/docs/home) قابل مشاهده خواهند بود.

## {{% heading "whatsnext" %}}

* [راهنمای سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)

---
title: تولید مستندات مرجع برای API کوبرنتیز
content_type: task
weight: 50
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه مستندات مرجع API کوبرنتیز را به‌روزرسانی کنید.

مستندات مرجع API کوبرنتیز از روی
[مشخصات OpenAPI کوبرنتیز](https://github.com/kubernetes/kubernetes/blob/master/api/openapi-spec/swagger.json)
و با استفاده از کد تولیدکنندهٔ [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) ساخته می‌شود.

اگر در مستندات تولیدشده با اشکال مواجه شدید، باید
[آن‌ها را در مخزن بالادستی (upstream) رفع کنید](/docs/contribute/generate-ref-docs/contribute-upstream/).

اگر فقط لازم است مستندات مرجع را از روی مشخصات
[OpenAPI](https://github.com/OAI/OpenAPI-Specification)
دوباره تولید کنید، مطالعهٔ این صفحه را ادامه دهید.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخازن محلی

یک فضای کاری محلی ایجاد کنید و `GOPATH` را تنظیم کنید:

```shell
mkdir -p $HOME/<workspace>

export GOPATH=$HOME/<workspace>
```

یک کلون محلی از مخازن زیر دریافت کنید:

```shell
git clone github.com/kubernetes-sigs/reference-docs
```
به دایرکتوری `gen-apidocs` در مخزن `reference-docs` بروید و بسته‌های Go موردنیاز را نصب کنید:
```shell
go get -u github.com/go-openapi/loads
go get -u github.com/go-openapi/spec
```

اگر هنوز مخزن kubernetes/website را ندارید، اکنون آن را دریافت کنید:

```shell
git clone https://github.com/<your-username>/website 
```

یک کلون از مخزن kubernetes/kubernetes دریافت کنید:

```shell
git clone https://github.com/kubernetes/kubernetes 
```

* دایرکتوری پایهٔ کلون شما از مخزن
  [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
  برابر `<your-path-to>/kubernetes/kubernetes.` است.
  در مراحل بعدی، به این دایرکتوری پایه با عنوان `<k8s-base>` اشاره می‌شود.

* دایرکتوری پایهٔ کلون شما از مخزن
  [kubernetes/website](https://github.com/kubernetes/website)
  برابر `<your-path-to>/website` است.
  در مراحل بعدی، به این دایرکتوری پایه با عنوان `<web-base>` اشاره می‌شود.

* دایرکتوری پایهٔ کلون شما از مخزن
  [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs)
  برابر `<your-path-to>/reference-docs` است.
  در مراحل بعدی، به این دایرکتوری پایه با عنوان `<rdocs-base>` اشاره می‌شود.

## تولید مستندات مرجع API

این بخش نشان می‌دهد چگونه
[مستندات مرجع منتشرشدهٔ API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
را تولید کنید.

### تنظیم متغیرهای ساخت

* مقدار `K8S_ROOT` را برابر `<k8s-base>` قرار دهید.
* مقدار `K8S_WEBROOT` را برابر `<web-base>` قرار دهید.
* مقدار `K8S_RELEASE` را برابر نسخهٔ مستنداتی قرار دهید که می‌خواهید بسازید.
  برای مثال، اگر می‌خواهید مستندات کوبرنتیز 1.17.0 را بسازید، `K8S_RELEASE` را برابر 1.17.0 قرار دهید.

برای مثال:

```shell
export K8S_WEBROOT=<your-path-to>/website
export K8S_ROOT=<your-path-to>/kubernetes
export K8S_RELEASE=1.17.0
```

### ایجاد دایرکتوری نسخه‌دار و دریافت مشخصات Open API

هدف ساخت (build target) با نام `updateapispec` دایرکتوری ساخت نسخه‌دار را ایجاد می‌کند.
پس از ایجاد این دایرکتوری، مشخصات Open API از مخزن
`<k8s-base>` دریافت می‌شود. این مراحل تضمین می‌کنند که نسخهٔ
فایل‌های پیکربندی و مشخصات Open API کوبرنتیز با نسخهٔ انتشار مطابقت داشته باشد.
نام دایرکتوری نسخه‌دار از الگوی `v<major>_<minor>` پیروی می‌کند.

در دایرکتوری `<rdocs-base>`، هدف ساخت زیر را اجرا کنید:

```shell
cd <rdocs-base>
make updateapispec
```

### ساخت مستندات مرجع API

هدف `copyapi` مرجع API را می‌سازد و
فایل‌های تولیدشده را در دایرکتوری‌هایی در `<web-base>` کپی می‌کند.
دستور زیر را در `<rdocs-base>` اجرا کنید:

```shell
cd <rdocs-base>
make copyapi
```

بررسی کنید که این دو فایل تولید شده باشند:

```shell
[ -e "<rdocs-base>/gen-apidocs/build/index.html" ] && echo "index.html built" || echo "no index.html"
[ -e "<rdocs-base>/gen-apidocs/build/navData.js" ] && echo "navData.js built" || echo "no navData.js"
```

به دایرکتوری پایهٔ `<web-base>` محلی خود بروید و
فایل‌های تغییریافته را مشاهده کنید:

```shell
cd <web-base>
git status
```

خروجی مشابه زیر است:

```
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/bootstrap.min.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/font-awesome.min.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/stylesheet.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/FontAwesome.otf
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.eot
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.svg
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.ttf
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.woff
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.woff2
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/index.html
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/jquery.scrollTo.min.js
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/navData.js
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/scroll.js
```

## محل و نسخه‌بندی مرجع API

فایل‌های تولیدشدهٔ مرجع API (نسخهٔ HTML) در مسیر `<web-base>/static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/` کپی می‌شوند. این دایرکتوری شامل مستندات مستقل HTML برای API است.

{{< note >}}
نسخهٔ Markdown مرجع API که در مسیر `<web-base>/content/en/docs/reference/kubernetes-api/` قرار دارد،
به‌صورت جداگانه و با استفاده از تولیدکنندهٔ [gen-resourcesdocs](https://github.com/kubernetes-sigs/reference-docs/tree/master/gen-resourcesdocs) تولید می‌شود.
{{< /note >}}

## آزمایش محلی مرجع API

یک نسخهٔ محلی از مرجع API را منتشر کنید.
[پیش‌نمایش محلی](http://localhost:1313/docs/reference/generated/kubernetes-api/{{< param "version">}}/) را بررسی کنید.

```shell
cd <web-base>
git submodule update --init --recursive --depth 1 # if not already done
make container-serve
```

## ثبت تغییرات (commit)

در `<web-base>`، دستورهای `git add` و `git commit` را برای ثبت تغییر اجرا کنید.

تغییرات خود را به‌صورت یک
[pull request](/docs/contribute/new-content/open-a-pr/) به مخزن
[kubernetes/website](https://github.com/kubernetes/website) ارسال کنید.
pull request خود را پیگیری کنید و در صورت نیاز به نظرات بازبینان پاسخ دهید. پیگیری
pull request را تا زمان ادغام شدن (merge) آن ادامه دهید.

## {{% heading "whatsnext" %}}

* [راهنمای سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)

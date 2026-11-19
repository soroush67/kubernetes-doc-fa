---
title: تولید مستندات مرجع برای API کوبرنتیز
content_type: task
weight: 50
---

<!-- overview -->

این صفحه نحوهٔ به‌روزرسانی مستندات مرجع API کوبرنتیز را نشان می‌دهد.

مستندات مرجع API کوبرنتیز از روی
[مشخصات OpenAPI کوبرنتیز](https://github.com/kubernetes/kubernetes/blob/master/api/openapi-spec/swagger.json)
و با استفاده از کد تولید [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) ساخته می‌شود.

اگر در مستندات تولیدشده با اشکالی روبه‌رو شدید، باید
[آن را در مخزن بالادستی (upstream) اصلاح کنید](/docs/contribute/generate-ref-docs/contribute-upstream/).

اگر فقط می‌خواهید مستندات مرجع را از روی مشخصات
[OpenAPI](https://github.com/OAI/OpenAPI-Specification)
دوباره تولید کنید، خواندن این صفحه را ادامه دهید.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخزن‌های محلی

یک فضای کاری محلی بسازید و متغیر `GOPATH` را تنظیم کنید:

```shell
mkdir -p $HOME/<workspace>

export GOPATH=$HOME/<workspace>
```

یک نسخهٔ محلی (clone) از مخزن زیر تهیه کنید:

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

یک نسخهٔ محلی از مخزن kubernetes/kubernetes تهیه کنید:

```shell
git clone https://github.com/kubernetes/kubernetes 
```

* دایرکتوری پایهٔ نسخهٔ محلی شما از مخزن
  [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
  مسیر `<your-path-to>/kubernetes/kubernetes.` است.
  در ادامهٔ مراحل، از این دایرکتوری پایه با نام `<k8s-base>` یاد می‌شود.

* دایرکتوری پایهٔ نسخهٔ محلی شما از مخزن
  [kubernetes/website](https://github.com/kubernetes/website)
  مسیر `<your-path-to>/website` است.
  در ادامهٔ مراحل، از این دایرکتوری پایه با نام `<web-base>` یاد می‌شود.

* دایرکتوری پایهٔ نسخهٔ محلی شما از مخزن
  [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs)
  مسیر `<your-path-to>/reference-docs` است.
  در ادامهٔ مراحل، از این دایرکتوری پایه با نام `<rdocs-base>` یاد می‌شود.

## تولید مستندات مرجع API

این بخش نشان می‌دهد که چگونه
[مستندات مرجع منتشرشدهٔ API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/) را تولید کنید.

### تنظیم متغیرهای ساخت

* متغیر `K8S_ROOT` را برابر با `<k8s-base>` قرار دهید.
* متغیر `K8S_WEBROOT` را برابر با `<web-base>` قرار دهید.
* متغیر `K8S_RELEASE` را برابر با نسخه‌ای از مستندات قرار دهید که می‌خواهید بسازید.
  برای مثال، اگر می‌خواهید مستندات کوبرنتیز 1.17.0 را بسازید، مقدار `K8S_RELEASE` را 1.17.0 قرار دهید.

برای مثال:

```shell
export K8S_WEBROOT=<your-path-to>/website
export K8S_ROOT=<your-path-to>/kubernetes
export K8S_RELEASE=1.17.0
```

### ایجاد دایرکتوری نسخه‌دار و دریافت مشخصات Open API

هدف ساخت `updateapispec` دایرکتوری ساخت نسخه‌دار را ایجاد می‌کند.
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
فایل‌های تولیدشده را در دایرکتوری‌هایی درون `<web-base>` کپی می‌کند.
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

به ریشهٔ دایرکتوری محلی `<web-base>` بروید و
ببینید کدام فایل‌ها تغییر کرده‌اند:

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

فایل‌های تولیدشدهٔ مرجع API (نسخهٔ HTML) در مسیر `<web-base>/static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/` کپی می‌شوند. این دایرکتوری شامل مستندات مستقل API در قالب HTML است.

{{< note >}}
نسخهٔ Markdown مرجع API که در مسیر `<web-base>/content/en/docs/reference/kubernetes-api/` قرار دارد،
به‌طور جداگانه و با استفاده از مولد [gen-resourcesdocs](https://github.com/kubernetes-sigs/reference-docs/tree/master/gen-resourcesdocs) تولید می‌شود.
{{< /note >}}

## آزمایش محلی مرجع API

یک نسخهٔ محلی از مرجع API منتشر کنید.
سپس [پیش‌نمایش محلی](http://localhost:1313/docs/reference/generated/kubernetes-api/{{< param "version">}}/) را بررسی کنید.

```shell
cd <web-base>
git submodule update --init --recursive --depth 1 # if not already done
make container-serve
```

## ثبت تغییرات

در `<web-base>`، دستورهای `git add` و `git commit` را اجرا کنید تا تغییرات ثبت شوند.

تغییرات خود را در قالب یک
[درخواست ادغام (pull request)](/docs/contribute/new-content/open-a-pr/) به مخزن
[kubernetes/website](https://github.com/kubernetes/website) ارسال کنید.
درخواست ادغام خود را پیگیری کنید و در صورت نیاز به نظرات بازبینان پاسخ دهید.
پیگیری درخواست ادغام را تا زمانی که ادغام شود ادامه دهید.

## {{% heading "whatsnext" %}}

* [راهنمای شروع سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)

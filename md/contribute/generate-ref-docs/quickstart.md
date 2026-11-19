---
title: راهنمای سریع مستندات مرجع
linkTitle: راهنمای سریع
content_type: task
weight: 10
hide_summary: true
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با اسکریپت `update-imported-docs.py` مستندات مرجع کوبرنتیز را تولید کنید. این اسکریپت آماده‌سازی محیط ساخت (build) را خودکار می‌کند و مستندات مرجع یک نسخهٔ انتشار را تولید می‌کند.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## دریافت مخزن مستندات

مطمئن شوید که فورک `website` شما با مخزن راه دور `kubernetes/website` در GitHub (شاخهٔ `main`) به‌روز است و سپس فورک `website` خود را کلون کنید.

```shell
mkdir github.com
cd github.com
git clone git@github.com:<your_github_username>/website.git
```

پوشهٔ پایهٔ کلون خود را مشخص کنید. برای مثال، اگر مخزن را با مرحلهٔ قبل دریافت کرده باشید، پوشهٔ پایهٔ شما `github.com/website.` است. در مراحل بعدی، از پوشهٔ پایهٔ شما با نام `<web-base>` یاد می‌شود.

{{< note>}}
اگر می‌خواهید محتوای مرجع ابزارهای کامپوننت‌ها و مرجع API را تغییر دهید، [راهنمای مشارکت در بالادست](/docs/contribute/generate-ref-docs/contribute-upstream) را ببینید.
{{< /note >}}

## نمای کلی update-imported-docs

اسکریپت `update-imported-docs.py` در پوشهٔ `<web-base>/update-imported-docs/` قرار دارد.

این اسکریپت مراجع زیر را می‌سازد:

* صفحه‌های مرجع کامپوننت‌ها و ابزارها
* مرجع دستورهای `kubectl`
* مرجع API کوبرنتیز

{{< note >}}
[صفحهٔ مرجع `kubelet`](/docs/reference/command-line-tools-reference/kubelet/) با این اسکریپت تولید نمی‌شود و به‌صورت دستی نگهداری می‌شود.
برای به‌روزرسانی مرجع kubelet، فرایند استاندارد مشارکت را که در [ایجاد یک درخواست ادغام](/docs/contribute/new-content/open-a-pr/) شرح داده شده است دنبال کنید.
{{< /note >}}


اسکریپت `update-imported-docs.py` مستندات مرجع کوبرنتیز را از کد منبع کوبرنتیز تولید می‌کند. این اسکریپت یک پوشهٔ موقت در مسیر `/tmp` روی دستگاه شما ایجاد می‌کند و مخزن‌های موردنیاز، یعنی `kubernetes/kubernetes` و `kubernetes-sigs/reference-docs`، را در این پوشه کلون می‌کند.
اسکریپت مقدار `GOPATH` شما را برابر با این پوشهٔ موقت قرار می‌دهد.
سه متغیر محیطی دیگر نیز تنظیم می‌شوند:

* `K8S_RELEASE`
* `K8S_ROOT`
* `K8S_WEBROOT`

این اسکریپت برای اجرای موفق به دو آرگومان نیاز دارد:

* یک فایل پیکربندی YAML (`reference.yml`)
* یک نسخهٔ انتشار، برای مثال: `1.17`

فایل پیکربندی یک فیلد `generate-command` دارد.
فیلد `generate-command` مجموعه‌ای از دستورالعمل‌های ساخت را از `kubernetes-sigs/reference-docs/Makefile` تعریف می‌کند. متغیر `K8S_RELEASE` نسخهٔ انتشار را تعیین می‌کند.

اسکریپت `update-imported-docs.py` مراحل زیر را انجام می‌دهد:

1. مخزن‌های مرتبطی را که در فایل پیکربندی مشخص شده‌اند کلون می‌کند. برای تولید مستندات مرجع، مخزنی که به‌طور پیش‌فرض کلون می‌شود `kubernetes-sigs/reference-docs` است.
1. دستورهایی را در مخزن‌های کلون‌شده اجرا می‌کند تا تولیدکنندهٔ مستندات آماده شود و سپس فایل‌های HTML و Markdown را تولید می‌کند.
1. فایل‌های HTML و Markdown تولیدشده را در مکان‌هایی که در فایل پیکربندی مشخص شده‌اند، در کلون محلی مخزن `<web-base>` کپی می‌کند.
1. پیوندهای دستورهای `kubectl` را در `kubectl`.md به‌روز می‌کند تا به بخش‌های مربوط در مرجع دستورهای `kubectl` ارجاع دهند.

وقتی فایل‌های تولیدشده در کلون محلی مخزن `<web-base>` قرار گرفتند، می‌توانید آن‌ها را در قالب یک [درخواست ادغام (pull request)](/docs/contribute/new-content/open-a-pr/) به `<web-base>` ارسال کنید.

## قالب فایل پیکربندی

هر فایل پیکربندی می‌تواند چند مخزن را در بر بگیرد که با هم وارد می‌شوند. در صورت نیاز، می‌توانید فایل پیکربندی را با ویرایش دستی سفارشی کنید. همچنین می‌توانید برای واردکردن گروه‌های دیگری از اسناد، فایل‌های پیکربندی جدیدی بسازید.
نمونهٔ زیر یک فایل پیکربندی YAML است:

```yaml
repos:
- name: community
  remote: https://github.com/kubernetes/community.git
  branch: master
  files:
  - src: contributors/devel/README.md
    dst: docs/imported/community/devel.md
  - src: contributors/guide/README.md
    dst: docs/imported/community/guide.md
```

اسناد تک‌صفحه‌ای Markdown که این ابزار وارد می‌کند باید از [راهنمای سبک مستندات](/docs/contribute/style/style-guide/) پیروی کنند.

## سفارشی‌سازی reference.yml

فایل `<web-base>/update-imported-docs/reference.yml` را برای ویرایش باز کنید.
تا زمانی که نمی‌دانید دستور فیلد `generate-command` چگونه برای ساخت مراجع به کار می‌رود، محتوای آن را تغییر ندهید.
معمولاً نیازی به به‌روزرسانی `reference.yml` نخواهید داشت. گاهی تغییرات کد منبع بالادست ممکن است تغییراتی را در فایل پیکربندی لازم کند (برای مثال، وابستگی به نسخهٔ golang و تغییرات کتابخانه‌های شخص ثالث).
اگر با مشکلی در ساخت روبه‌رو شدید، با تیم SIG-Docs در [کانال #sig-docs در Slack کوبرنتیز](https://kubernetes.slack.com) تماس بگیرید.

{{< note >}}
مدخل `generate-command` اختیاری است و می‌توان از آن برای اجرای یک دستور مشخص یا یک اسکریپت کوتاه استفاده کرد تا مستندات از درون یک مخزن تولید شوند.
{{< /note >}}

در `reference.yml`، فیلد `files` فهرستی از فیلدهای `src` و `dst` را در بر دارد.
فیلد `src` مکان یک فایل Markdown تولیدشده در پوشهٔ ساخت مخزن کلون‌شدهٔ `kubernetes-sigs/reference-docs` را نگه می‌دارد و فیلد `dst` مشخص می‌کند که این فایل در کجای مخزن کلون‌شدهٔ `kubernetes/website` کپی شود.
برای مثال:

```yaml
repos:
- name: reference-docs
  remote: https://github.com/kubernetes-sigs/reference-docs.git
  files:
  - src: gen-compdocs/build/kube-apiserver.md
    dst: content/en/docs/reference/command-line-tools-reference/kube-apiserver.md
  ...
```

توجه کنید که وقتی باید فایل‌های زیادی از یک پوشهٔ مبدأ به یک پوشهٔ مقصد کپی شوند، می‌توانید در مقدار `src` از نویسه‌های عام (wildcard) استفاده کنید. در این حالت باید نام پوشه را به‌عنوان مقدار `dst` وارد کنید.
برای مثال:

```yaml
  files:
  - src: gen-compdocs/build/kubeadm*.md
    dst: content/en/docs/reference/setup-tools/kubeadm/generated/
```

## اجرای ابزار update-imported-docs

ابزار `update-imported-docs.py` را می‌توانید به این شکل اجرا کنید:

```shell
cd <web-base>/update-imported-docs
./update-imported-docs.py <configuration-file.yml> <release-version>
```

برای مثال:

```shell
./update-imported-docs.py reference.yml 1.17
```

<!-- Revisit: is the release configuration used -->
## اصلاح پیوندها

فایل پیکربندی `release.yml` دستورالعمل‌هایی برای اصلاح پیوندهای نسبی دارد.
برای اصلاح پیوندهای نسبی در فایل‌های واردشده، ویژگی `gen-absolute-links` را برابر با `true` قرار دهید. نمونه‌ای از این کار را می‌توانید در [`release.yml`](https://github.com/kubernetes/website/blob/main/update-imported-docs/release.yml) ببینید.

## افزودن و کامیت تغییرات در kubernetes/website

فایل‌هایی را که تولید و در `<web-base>` کپی شده‌اند فهرست کنید:

```shell
cd <web-base>
git status
```

خروجی، فایل‌های جدید و تغییریافته را نشان می‌دهد. خروجی تولیدشده بسته به تغییراتی که در کد منبع بالادست ایجاد شده است متفاوت خواهد بود.

### فایل‌های تولیدشدهٔ ابزارهای کامپوننت‌ها

```
content/en/docs/reference/command-line-tools-reference/kube-apiserver.md
content/en/docs/reference/command-line-tools-reference/kube-controller-manager.md
content/en/docs/reference/command-line-tools-reference/kube-proxy.md
content/en/docs/reference/command-line-tools-reference/kube-scheduler.md
content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm.md
content/en/docs/reference/kubectl/kubectl.md
```

### فایل‌های تولیدشدهٔ مرجع دستورهای kubectl

```
static/docs/reference/generated/kubectl/kubectl-commands.html
static/docs/reference/generated/kubectl/navData.js
static/docs/reference/generated/kubectl/scroll.js
static/docs/reference/generated/kubectl/stylesheet.css
static/docs/reference/generated/kubectl/tabvisibility.js
static/docs/reference/generated/kubectl/node_modules/bootstrap/dist/css/bootstrap.min.css
static/docs/reference/generated/kubectl/node_modules/highlight.js/styles/default.css
static/docs/reference/generated/kubectl/node_modules/jquery.scrollto/jquery.scrollTo.min.js
static/docs/reference/generated/kubectl/node_modules/jquery/dist/jquery.min.js
static/docs/reference/generated/kubectl/css/font-awesome.min.css
```

### پوشه‌ها و فایل‌های تولیدشدهٔ مرجع API کوبرنتیز

```
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/index.html
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/navData.js
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/scroll.js
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/js/query.scrollTo.min.js
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/font-awesome.min.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/bootstrap.min.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/css/stylesheet.css
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/FontAwesome.otf
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.eot
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.svg
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.ttf
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.woff
static/docs/reference/generated/kubernetes-api/{{< param "version" >}}/fonts/fontawesome-webfont.woff2
```

برای کامیت فایل‌ها، دستورهای `git add` و `git commit` را اجرا کنید.

## ایجاد درخواست ادغام

یک درخواست ادغام به مخزن `kubernetes/website` ایجاد کنید. درخواست ادغام خود را پیگیری کنید و در صورت نیاز به نظرهای بازبینی پاسخ دهید. پیگیری درخواست ادغام را تا زمانی که ادغام شود ادامه دهید.

چند دقیقه پس از ادغام درخواست شما، مباحث مرجع به‌روزشده در [مستندات منتشرشده](/docs/home/) نمایش داده می‌شوند.



## {{% heading "whatsnext" %}}


برای تولید دوبارهٔ همهٔ مجموعه‌های مرجع یک نسخهٔ انتشار و ارسال خروجی در قالب درخواست‌های ادغام، [تولید مستندات مرجع برای یک نسخهٔ انتشار](/docs/contribute/generate-ref-docs/release-generation/) را ببینید.

برای تولید جداگانهٔ هر یک از مستندات مرجع با راه‌اندازی دستی مخزن‌های ساخت موردنیاز و اجرای هدف‌های ساخت، راهنماهای زیر را ببینید:

* [تولید مستندات مرجع برای کامپوننت‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)
* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)

---
title: شروع سریع مستندات مرجع
linkTitle: شروع سریع
content_type: task
weight: 10
hide_summary: true
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه از اسکریپت `update-imported-docs.py` برای تولید
مستندات مرجع کوبرنتیز استفاده کنید. این اسکریپت
تنظیمات ساخت را خودکار می‌کند و مستندات مرجع یک نسخه (release) را تولید می‌کند.

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## دریافت مخزن مستندات

مطمئن شوید که fork مخزن `website` شما با remote با نام `kubernetes/website` در
GitHub (شاخه `main`) به‌روز است، و سپس fork مخزن `website` خود را کلون کنید.

```shell
mkdir github.com
cd github.com
git clone git@github.com:<your_github_username>/website.git
```

دایرکتوری پایه کلون خود را مشخص کنید. برای مثال، اگر مراحل قبلی را برای دریافت مخزن
دنبال کرده باشید، دایرکتوری پایه شما `github.com/website.` است.
در مراحل بعدی، از دایرکتوری پایه شما با عنوان `<web-base>` یاد می‌شود.

{{< note>}}
اگر می‌خواهید محتوای ابزارهای مؤلفه‌ها و مرجع API را تغییر دهید،
[راهنمای مشارکت در بالادست (upstream)](/docs/contribute/generate-ref-docs/contribute-upstream) را ببینید.
{{< /note >}}

## مروری بر update-imported-docs

اسکریپت `update-imported-docs.py` در دایرکتوری `<web-base>/update-imported-docs/`
قرار دارد.

این اسکریپت مرجع‌های زیر را می‌سازد:

* صفحات مرجع مؤلفه‌ها و ابزارها
* مرجع دستورهای `kubectl`
* مرجع API کوبرنتیز

{{< note >}}
[صفحه مرجع `kubelet`](/docs/reference/command-line-tools-reference/kubelet/) توسط این اسکریپت تولید نمی‌شود و به‌صورت دستی نگهداری می‌شود.
برای به‌روزرسانی مرجع kubelet، فرایند استاندارد مشارکت را که در
[ارسال pull request](/docs/contribute/new-content/open-a-pr/) شرح داده شده است دنبال کنید.
{{< /note >}}


اسکریپت `update-imported-docs.py` مستندات مرجع کوبرنتیز را
از کد منبع کوبرنتیز تولید می‌کند. این اسکریپت یک دایرکتوری موقت
در مسیر `/tmp` روی دستگاه شما ایجاد می‌کند و مخازن موردنیاز یعنی `kubernetes/kubernetes` و
`kubernetes-sigs/reference-docs` را در آن کلون می‌کند.
این اسکریپت مقدار `GOPATH` شما را روی همین دایرکتوری موقت تنظیم می‌کند.
سه متغیر محیطی دیگر نیز تنظیم می‌شوند:

* `K8S_RELEASE`
* `K8S_ROOT`
* `K8S_WEBROOT`

این اسکریپت برای اجرای موفق به دو آرگومان نیاز دارد:

* یک فایل پیکربندی YAML (`reference.yml`)
* یک نسخه انتشار، برای مثال: `1.17`

فایل پیکربندی شامل فیلدی با نام `generate-command` است.
فیلد `generate-command` مجموعه‌ای از دستورالعمل‌های ساخت را
از `kubernetes-sigs/reference-docs/Makefile` تعریف می‌کند. متغیر `K8S_RELEASE`
نسخه انتشار را تعیین می‌کند.

اسکریپت `update-imported-docs.py` مراحل زیر را انجام می‌دهد:

1. مخازن مرتبطی را که در یک فایل پیکربندی مشخص شده‌اند کلون می‌کند. برای
   تولید مستندات مرجع، مخزنی که به‌طور پیش‌فرض کلون می‌شود
   `kubernetes-sigs/reference-docs` است.
1. دستورهایی را درون مخازن کلون‌شده اجرا می‌کند تا تولیدکننده مستندات را آماده کند و
   سپس فایل‌های HTML و Markdown را تولید می‌کند.
1. فایل‌های HTML و Markdown تولیدشده را در مسیرهایی که در فایل پیکربندی مشخص شده است،
   به یک کلون محلی از مخزن `<web-base>` کپی می‌کند.
1. پیوندهای دستورهای `kubectl` را از `kubectl`.md به بخش‌های مرجع دستورهای `kubectl`
   به‌روزرسانی می‌کند.

وقتی فایل‌های تولیدشده در کلون محلی مخزن `<web-base>` شما قرار گرفتند،
می‌توانید آن‌ها را در قالب یک [pull request](/docs/contribute/new-content/open-a-pr/)
به `<web-base>` ارسال کنید.

## قالب فایل پیکربندی

هر فایل پیکربندی می‌تواند شامل چندین مخزن باشد که با هم درون‌ریزی (import) می‌شوند. در صورت
نیاز، می‌توانید فایل پیکربندی را با ویرایش دستی سفارشی کنید. همچنین
می‌توانید فایل‌های پیکربندی جدیدی برای درون‌ریزی گروه‌های دیگری از اسناد ایجاد کنید.
در ادامه نمونه‌ای از فایل پیکربندی YAML آمده است:

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

اسناد Markdown تک‌صفحه‌ای که توسط این ابزار درون‌ریزی می‌شوند، باید از
[راهنمای سبک مستندات](/docs/contribute/style/style-guide/) پیروی کنند.

## سفارشی‌سازی reference.yml

فایل `<web-base>/update-imported-docs/reference.yml` را برای ویرایش باز کنید.
محتوای فیلد `generate-command` را تغییر ندهید، مگر اینکه بدانید
این دستور چگونه برای ساخت مرجع‌ها استفاده می‌شود.
معمولاً نیازی به به‌روزرسانی `reference.yml` نخواهید داشت. گاهی تغییرات
در کد منبع بالادست (upstream) ممکن است به تغییر در فایل پیکربندی نیاز داشته باشد
(برای مثال: وابستگی‌های نسخه golang و تغییرات کتابخانه‌های شخص ثالث).
اگر با مشکلات ساخت مواجه شدید، با تیم SIG-Docs در
[کانال Slack کوبرنتیز با نام #sig-docs](https://kubernetes.slack.com) تماس بگیرید.

{{< note >}}
`generate-command` یک مدخل اختیاری است که می‌توان از آن برای اجرای
یک دستور مشخص یا یک اسکریپت کوتاه برای تولید مستندات از درون یک مخزن استفاده کرد.
{{< /note >}}

در `reference.yml`، بخش `files` شامل فهرستی از فیلدهای `src` و `dst` است.
فیلد `src` مکان یک فایل Markdown تولیدشده را در دایرکتوری ساخت کلون‌شده
`kubernetes-sigs/reference-docs` مشخص می‌کند و فیلد `dst` تعیین می‌کند
این فایل در مخزن کلون‌شده `kubernetes/website` به کجا کپی شود.
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

توجه کنید که وقتی فایل‌های زیادی باید از یک دایرکتوری مبدأ
به یک دایرکتوری مقصد کپی شوند، می‌توانید در مقدار `src` از wildcard استفاده کنید.
در این حالت باید نام دایرکتوری را به‌عنوان مقدار `dst` ارائه کنید.
برای مثال:

```yaml
  files:
  - src: gen-compdocs/build/kubeadm*.md
    dst: content/en/docs/reference/setup-tools/kubeadm/generated/
```

## اجرای ابزار update-imported-docs

می‌توانید ابزار `update-imported-docs.py` را به‌صورت زیر اجرا کنید:

```shell
cd <web-base>/update-imported-docs
./update-imported-docs.py <configuration-file.yml> <release-version>
```

برای مثال:

```shell
./update-imported-docs.py reference.yml 1.17
```

<!-- Revisit: is the release configuration used -->
## رفع پیوندها

فایل پیکربندی `release.yml` شامل دستورالعمل‌هایی برای رفع پیوندهای نسبی است.
برای رفع پیوندهای نسبی درون فایل‌های درون‌ریزی‌شده، ویژگی `gen-absolute-links`
را روی `true` تنظیم کنید. نمونه‌ای از این مورد را می‌توانید در
[`release.yml`](https://github.com/kubernetes/website/blob/main/update-imported-docs/release.yml) ببینید.

## افزودن و کامیت تغییرات در kubernetes/website

فایل‌هایی را که تولید و در `<web-base>` کپی شده‌اند فهرست کنید:

```shell
cd <web-base>
git status
```

خروجی، فایل‌های جدید و تغییریافته را نشان می‌دهد. خروجی تولیدشده
بسته به تغییراتی که در کد منبع بالادست (upstream) اعمال شده است، متفاوت خواهد بود.

### فایل‌های تولیدشده ابزارهای مؤلفه‌ها

```
content/en/docs/reference/command-line-tools-reference/kube-apiserver.md
content/en/docs/reference/command-line-tools-reference/kube-controller-manager.md
content/en/docs/reference/command-line-tools-reference/kube-proxy.md
content/en/docs/reference/command-line-tools-reference/kube-scheduler.md
content/en/docs/reference/setup-tools/kubeadm/generated/kubeadm.md
content/en/docs/reference/kubectl/kubectl.md
```

### فایل‌های تولیدشده مرجع دستورهای kubectl

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

### دایرکتوری‌ها و فایل‌های تولیدشده مرجع API کوبرنتیز

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

برای کامیت کردن فایل‌ها، `git add` و `git commit` را اجرا کنید.

## ایجاد pull request

یک pull request به مخزن `kubernetes/website` ایجاد کنید. pull request خود را
پایش کنید و در صورت نیاز به نظرات بازبینی پاسخ دهید. تا زمانی که
pull request شما ادغام (merge) شود، آن را پایش کنید.

چند دقیقه پس از ادغام pull request شما، موضوعات مرجع به‌روزشده
در [مستندات منتشرشده](/docs/home/) قابل مشاهده خواهند بود.



## {{% heading "whatsnext" %}}


برای تولید مجدد همه مجموعه‌های مرجع یک نسخه انتشار و ارسال خروجی در قالب pull request،
[تولید مستندات مرجع برای یک نسخه انتشار](/docs/contribute/generate-ref-docs/release-generation/) را ببینید.

برای تولید مستندات مرجع جداگانه با راه‌اندازی دستی مخازن موردنیاز ساخت و
اجرای هدف‌های ساخت، راهنماهای زیر را ببینید:

* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)
* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)

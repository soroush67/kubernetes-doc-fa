---
title: تولید مستندات مرجع برای APIهای پیکربندی
content_type: task
weight: 60
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه می‌توانید مستندات مرجع به‌روز‌شده را برای APIهای پیکربندی (Configuration API) کوبرنتیز تولید کنید. این صفحه برای افرادی نوشته شده است که در توسعه کوبرنتیز مشارکت می‌کنند.

مرجع Configuration API قالب‌های پیکربندی ابزارها و مؤلفه‌های کوبرنتیز را مستند می‌کند؛ برای مثال قالب‌های `kubelet`، `kube-apiserver`، `kube-scheduler`، `kubeconfig` و
`kubeadm`. مرجع منتشرشده در [/docs/reference/config-api/](/docs/reference/config-api/) در دسترس است.

`genref` که در [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) قرار دارد،
مولدی است که این مرجع را می‌سازد. این ابزار انواع پیکربندی Go هر مؤلفه را می‌خواند و آن‌ها را به‌صورت markdown تولید می‌کند.

اگر در محتوای تولیدشده به اشکال برخوردید، به احتمال زیاد باید
[آن‌ها را در مخزن بالادستی (upstream) اصلاح کنید](/docs/contribute/generate-ref-docs/contribute-upstream/).

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخازن محلی

به کلون‌های محلی `kubernetes/website` و `kubernetes-sigs/reference-docs` نیاز دارید.

اگر هنوز `kubernetes/website` را fork و کلون نکرده‌اید، به
[کار با یک کلون محلی](/docs/contribute/new-content/open-a-pr/#fork-the-repo) مراجعه کنید.
مخزن `reference-docs` را کلون کنید:

```shell
git clone https://github.com/kubernetes-sigs/reference-docs
```

در مراحل بعدی، کلون `kubernetes/website` شما با `<web-base>` و
کلون `reference-docs` شما با `<rdocs-base>` نمایش داده می‌شود.

## تنظیم متغیرهای ساخت

این مقدار را در shell خود تنظیم کنید. این تنظیم بر همه دستورهای `make` در مراحل
بعدی اعمال می‌شود، فارغ از اینکه آن‌ها را از کدام دایرکتوری اجرا کنید.

```shell
export K8S_WEBROOT=/path/to/your/website   # your website clone (<web-base>)
```

## ساخت و انتشار مرجع Configuration API

از دایرکتوری `<rdocs-base>`:

```shell
cd <rdocs-base>
make copyconfigapi
```

این دستور در دو مرحله اجرا می‌شود:
1. **`configapi`** - `genref` را می‌سازد و اجرا می‌کند و فایل‌های Markdown را در `genref/output/md` تولید می‌کند
2. **`copyconfigapi`** - فایل‌های تولیدشده را در کلون وب‌سایت شما در
`<web-base>/content/en/docs/reference/config-api/` کپی می‌کند.

در اولین اجرا، وابستگی‌های ماژول Go دانلود می‌شوند و ممکن است چند دقیقه طول بکشد.

بررسی کنید چه تغییری در کلون وب‌سایت شما ایجاد شده است:
```shell
cd <web-base>
git status
```

به دنبال به‌روزرسانی‌هایی در مسیر `content/en/docs/reference/config-api` بگردید؛ برای مثال:

```text
content/en/docs/reference/config-api/kubelet-config.v1beta1.md
content/en/docs/reference/config-api/kubeadm-config.v1beta4.md
content/en/docs/reference/config-api/apiserver-config.v1.md
content/en/docs/reference/config-api/client-authentication.v1.md
```

## پیش‌نمایش وب‌سایت و آزمایش محلی

به‌روزرسانی‌های خود را پیش‌نمایش کنید:
```shell
cd <web-base>
git submodule update --init --recursive --depth 1   # if not already done
make container-serve
```

سپس یک پیش‌نمایش محلی را در مرورگر وب خود باز کنید و بررسی کنید که
صفحه‌هایی که به‌روزرسانی کرده‌اید به‌درستی بارگذاری می‌شوند.
Hugo این پیش‌نمایش محلی را در http://localhost:1313/ ارائه می‌کند.
بنابراین صفحه‌ای که باید بررسی کنید http://localhost:1313/docs/reference/config-api/ است.

## ثبت تغییرات (commit)

اگر مرجع Configuration API را برای به‌روزرسانی یک انتشار (release) بازتولید کرده‌اید،
فایل‌های تغییریافته در مسیر `content/en/docs/reference/config-api/` را در
`<web-base>` commit کنید، سپس یک [pull request](/docs/contribute/new-content/open-a-pr/)
به [kubernetes/website](https://github.com/kubernetes/website) باز کنید.

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [شروع سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [مشارکت در مستندات مرجع بالادستی](/docs/contribute/generate-ref-docs/contribute-upstream/)

---
title: تولید مستندات مرجع برای APIهای پیکربندی
content_type: task
weight: 60
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید مستندات مرجع به‌روزشده را برای APIهای پیکربندی کوبرنتیز تولید کنید. مخاطب این صفحه کسانی هستند که در کوبرنتیز مشارکت می‌کنند.

مرجع API پیکربندی، قالب‌های پیکربندی ابزارها و مؤلفه‌های کوبرنتیز را مستند می‌کند؛ برای نمونه، قالب‌های `kubelet`، `kube-apiserver`، `kube-scheduler`، `kubeconfig` و `kubeadm`. نسخهٔ منتشرشدهٔ این مرجع در [/docs/reference/config-api/](/docs/reference/config-api/) در دسترس است.

ابزار `genref` در مخزن [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) مولّدی است که این مرجع را می‌سازد. این ابزار نوع‌های پیکربندی Go هر مؤلفه را می‌خواند و آن‌ها را به‌صورت Markdown تولید می‌کند.

اگر در محتوای تولیدشده اشکالی پیدا کردید، به احتمال زیاد باید [آن را در مخزن بالادستی (upstream) اصلاح کنید](/docs/contribute/generate-ref-docs/contribute-upstream/).

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخزن‌های محلی

به نسخه‌های محلی (clone) از مخزن‌های `kubernetes/website` و `kubernetes-sigs/reference-docs` نیاز دارید.

اگر هنوز مخزن `kubernetes/website` را fork و clone نکرده‌اید، به [کار با یک نسخهٔ محلی](/docs/contribute/new-content/open-a-pr/#fork-the-repo) مراجعه کنید.
مخزن `reference-docs` را clone کنید:

```shell
git clone https://github.com/kubernetes-sigs/reference-docs
```

در ادامهٔ مراحل، نسخهٔ محلی `kubernetes/website` با `<web-base>` و نسخهٔ محلی `reference-docs` با `<rdocs-base>` مشخص می‌شود.

## تنظیم متغیرهای ساخت

این متغیر را در پوستهٔ (shell) خود تنظیم کنید. این تنظیم برای همهٔ فرمان‌های `make` در مراحل بعدی اعمال می‌شود، فارغ از اینکه آن‌ها را از کدام دایرکتوری اجرا کنید.

```shell
export K8S_WEBROOT=/path/to/your/website   # your website clone (<web-base>)
```

## ساخت و انتشار مرجع API پیکربندی

از دایرکتوری `<rdocs-base>`:

```shell
cd <rdocs-base>
make copyconfigapi
```

این فرمان در دو مرحله اجرا می‌شود:
1. **`configapi`**: ابزار `genref` را می‌سازد و اجرا می‌کند و این ابزار فایل‌های Markdown را در `genref/output/md` تولید می‌کند.
2. **`copyconfigapi`**: فایل‌های تولیدشده را در نسخهٔ محلی وب‌سایت شما، در مسیر `<web-base>/content/en/docs/reference/config-api/`، کپی می‌کند.

در نخستین اجرا، وابستگی‌های ماژول Go دانلود می‌شوند و ممکن است این کار چند دقیقه طول بکشد.

تغییرات نسخهٔ محلی وب‌سایت خود را بررسی کنید:
```shell
cd <web-base>
git status
```

به‌دنبال به‌روزرسانی‌هایی در مسیر `content/en/docs/reference/config-api` بگردید؛ برای نمونه:

```text
content/en/docs/reference/config-api/kubelet-config.v1beta1.md
content/en/docs/reference/config-api/kubeadm-config.v1beta4.md
content/en/docs/reference/config-api/apiserver-config.v1.md
content/en/docs/reference/config-api/client-authentication.v1.md
```

## پیش‌نمایش وب‌سایت و آزمایش محلی

پیش‌نمایش به‌روزرسانی‌های خود را ببینید:
```shell
cd <web-base>
git submodule update --init --recursive --depth 1   # if not already done
make container-serve
```

سپس پیش‌نمایش محلی را در مرورگر وب خود باز کنید و مطمئن شوید که صفحه‌هایی که به‌روزرسانی کرده‌اید به‌درستی بارگذاری می‌شوند.
ابزار Hugo این پیش‌نمایش محلی را در نشانی http://localhost:1313/ ارائه می‌کند.
بنابراین صفحه‌ای که باید بررسی کنید http://localhost:1313/docs/reference/config-api/ است.

## ثبت (commit) تغییرات

اگر مرجع API پیکربندی را برای به‌روزرسانی یک انتشار دوباره تولید کرده‌اید، فایل‌های تغییریافته در مسیر `content/en/docs/reference/config-api/` را در `<web-base>` ثبت کنید و سپس یک [درخواست ادغام (pull request)](/docs/contribute/new-content/open-a-pr/) برای مخزن [kubernetes/website](https://github.com/kubernetes/website) باز کنید.

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [راهنمای سریع تولید مستندات مرجع](/docs/contribute/generate-ref-docs/quickstart/)
* [مشارکت در مستندات مرجع بالادستی](/docs/contribute/generate-ref-docs/contribute-upstream/)

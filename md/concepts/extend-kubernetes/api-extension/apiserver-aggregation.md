---
title: لایه تجمیع API کوبرنتیز
reviewers:
- lavalamp
- cheftako
- chenopis
content_type: concept
weight: 20
---

<!-- overview -->

لایه تجمیع (aggregation layer) امکان می‌دهد کوبرنتیز با APIهای اضافی گسترش یابد، فراتر از آنچه APIهای اصلی کوبرنتیز ارائه می‌کنند.
این APIهای اضافی می‌توانند راه‌حل‌های آماده‌ای مانند
[metrics server](https://github.com/kubernetes-sigs/metrics-server) باشند، یا APIهایی که خودتان توسعه می‌دهید.

لایه تجمیع با
[Custom Resource Definitions](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
متفاوت است؛ Custom Resource Definitionها روشی هستند برای اینکه {{< glossary_tooltip term_id="kube-apiserver" text="kube-apiserver" >}}
انواع جدیدی از آبجکت را بشناسد.

<!-- body -->

## لایه تجمیع {#aggregation-layer}

لایه تجمیع درون همان پردازش kube-apiserver اجرا می‌شود. تا زمانی که یک منبع افزونه ثبت نشده باشد، لایه تجمیع کاری انجام نمی‌دهد. برای ثبت یک API، یک آبجکت _APIService_ اضافه می‌کنید که مسیر URL مورد نظر را در API کوبرنتیز «مطالبه» (claim) می‌کند. از آن پس، لایه تجمیع هر درخواستی را که به آن مسیر API ارسال شود (برای مثال `/apis/myextension.mycompany.io/v1/…`) به APIService ثبت‌شده پراکسی می‌کند.

رایج‌ترین روش پیاده‌سازی APIService، اجرای یک *extension API server* در Pod(های) درون کلاستر شماست. اگر از extension API server برای مدیریت منابع در کلاستر خود استفاده می‌کنید، این سرور (که به صورت «extension-apiserver» نیز نوشته می‌شود) معمولاً با یک یا چند {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} همراه می‌شود. کتابخانه apiserver-builder یک اسکلت برای هر دو، یعنی extension API serverها و کنترل‌کننده(های) مرتبط با آن‌ها، فراهم می‌کند.

### تأخیر پاسخ {#response-latency}

extension API serverها باید شبکه‌ای با تأخیر کم از و به kube-apiserver داشته باشند.
درخواست‌های کشف (discovery) باید در پنج ثانیه یا کمتر یک رفت‌وبرگشت کامل با kube-apiserver انجام دهند.

اگر extension API server شما نمی‌تواند این الزام تأخیر را برآورده کند، تغییراتی را در نظر بگیرید که امکان رسیدن به آن را فراهم می‌کنند.

## {{% heading "whatsnext" %}}

* برای راه‌اندازی aggregator در محیط خود، [لایه تجمیع را پیکربندی کنید](/docs/tasks/extend-kubernetes/configure-aggregation-layer/).
* سپس [یک extension api-server راه‌اندازی کنید](/docs/tasks/extend-kubernetes/setup-extension-api-server/) تا با لایه تجمیع کار کند.
* درباره [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) در مرجع API مطالعه کنید.
* با [مفاهیم اعتبارسنجی اعلانی (Declarative Validation)](/docs/reference/using-api/declarative-validation/) آشنا شوید؛ سازوکاری داخلی برای تعریف قواعد اعتبارسنجی که در آینده به پشتیبانی از اعتبارسنجی در توسعه extension API server کمک خواهد کرد.

به‌عنوان گزینه‌ای دیگر: یاد بگیرید چگونه API کوبرنتیز را با استفاده از
[Custom Resource Definitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
گسترش دهید.

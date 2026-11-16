---
title: لایه تجمیع API در کوبرنتیز
reviewers:
- lavalamp
- cheftako
- chenopis
content_type: concept
weight: 20
---

<!-- overview -->

لایه تجمیع (aggregation layer) امکان می‌دهد کوبرنتیز را با APIهای اضافی، فراتر از آنچه APIهای هسته کوبرنتیز ارائه می‌کنند، گسترش دهید.
این APIهای اضافی می‌توانند راهکارهای آماده‌ای مانند
[سرور معیارها (metrics server)](https://github.com/kubernetes-sigs/metrics-server) باشند یا APIهایی که خودتان توسعه می‌دهید.

لایه تجمیع با
[تعاریف منابع سفارشی (Custom Resource Definitions)](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
تفاوت دارد؛ تعاریف منابع سفارشی راهی هستند برای اینکه {{< glossary_tooltip term_id="kube-apiserver" text="kube-apiserver" >}}
انواع جدیدی از آبجکت‌ها را بشناسد.

<!-- body -->

## لایه تجمیع

لایه تجمیع درون همان فرایند kube-apiserver اجرا می‌شود. تا زمانی که یک منبع افزونه ثبت نشده باشد، لایه تجمیع هیچ کاری انجام نمی‌دهد. برای ثبت یک API، یک آبجکت _APIService_ اضافه می‌کنید که مسیر URL مربوط را در API کوبرنتیز «تصاحب» می‌کند. از آن پس، لایه تجمیع هر درخواستی را که به آن مسیر API (برای مثال `/apis/myextension.mycompany.io/v1/…`) ارسال شود، به APIService ثبت‌شده پراکسی می‌کند.

رایج‌ترین روش پیاده‌سازی APIService، اجرای یک *سرور API افزونه* در یک یا چند Pod درون کلاستر است. اگر از سرور API افزونه برای مدیریت منابع کلاستر خود استفاده می‌کنید، این سرور (که با نام «extension-apiserver» نیز نوشته می‌شود) معمولاً همراه با یک یا چند {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} به کار می‌رود. کتابخانه apiserver-builder یک اسکلت اولیه هم برای سرورهای API افزونه و هم برای کنترل‌کننده‌های مرتبط با آن‌ها فراهم می‌کند.

### تأخیر پاسخ

ارتباط شبکه‌ای سرورهای API افزونه با kube-apiserver، در هر دو جهت، باید تأخیر کمی داشته باشد. رفت‌وبرگشت درخواست‌های کشف (discovery) از kube-apiserver باید حداکثر در پنج ثانیه انجام شود.

اگر سرور API افزونه شما نمی‌تواند این الزام تأخیر را برآورده کند، تغییراتی را در نظر بگیرید که برآورده‌شدن آن را ممکن سازد.

## {{% heading "whatsnext" %}}

* برای راه‌اندازی تجمیع‌کننده در محیط خود، [لایه تجمیع را پیکربندی کنید](/docs/tasks/extend-kubernetes/configure-aggregation-layer/).
* سپس [یک سرور API افزونه راه‌اندازی کنید](/docs/tasks/extend-kubernetes/setup-extension-api-server/) تا با لایه تجمیع کار کند.
* درباره [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) در مرجع API مطالعه کنید.
* با [مفاهیم اعتبارسنجی اعلانی](/docs/reference/using-api/declarative-validation/) آشنا شوید؛
  سازوکاری داخلی برای تعریف قواعد اعتبارسنجی که در آینده به پشتیبانی از اعتبارسنجی در توسعه سرورهای API افزونه کمک خواهد کرد.

به‌عنوان راه دیگر، می‌توانید یاد بگیرید که چگونه API کوبرنتیز را با استفاده از
[تعاریف منابع سفارشی](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) گسترش دهید.

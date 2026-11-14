---
title: راه‌اندازی سرور API افزونه
reviewers:
- lavalamp
- cheftako
- chenopis
content_type: task
weight: 15
---

<!-- overview -->

با راه‌اندازی یک سرور API افزونه (extension API server) که با لایهٔ تجمیع (aggregation layer) کار می‌کند، می‌توان apiserver کوبرنتیز را با APIهای دیگری گسترش داد که جزو APIهای هستهٔ کوبرنتیز نیستند.



## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* باید [لایهٔ تجمیع را پیکربندی کنید](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) و فلگ‌های apiserver را فعال کنید.



<!-- steps -->

## راه‌اندازی یک سرور API افزونه برای کار با لایهٔ تجمیع

مراحل زیر *در سطحی کلی* نحوهٔ راه‌اندازی یک سرور API افزونه را شرح می‌دهند. این مراحل، چه از پیکربندی‌های YAML استفاده کنید و چه از APIها، یکسان‌اند و تلاش شده است هر تفاوتی میان این دو روش به‌طور مشخص بیان شود. برای دیدن نمونه‌ای عملی از پیاده‌سازی این مراحل با پیکربندی‌های YAML، می‌توانید به [sample-apiserver](https://github.com/kubernetes/sample-apiserver/blob/master/README.md) در مخزن کوبرنتیز مراجعه کنید.

همچنین می‌توانید از یک راه‌حل آمادهٔ شخص ثالث مانند [apiserver-builder](https://github.com/kubernetes-sigs/apiserver-builder-alpha/blob/master/README.md) استفاده کنید که اسکلت اولیه را تولید می‌کند و همهٔ مراحل زیر را برایتان خودکار انجام می‌دهد.

1. مطمئن شوید که API مربوط به APIService فعال است (`--runtime-config` را بررسی کنید). این API به‌طور پیش‌فرض فعال است، مگر آنکه در کلاستر شما عمداً غیرفعال شده باشد.
1. ممکن است لازم باشد یک قاعدهٔ RBAC بسازید که اجازهٔ افزودن آبجکت‌های APIService را به شما بدهد، یا از مدیر کلاستر بخواهید چنین قاعده‌ای بسازد. (از آنجا که افزونه‌های API بر کل کلاستر اثر می‌گذارند، توصیه نمی‌شود آزمایش، توسعه یا اشکال‌زدایی یک افزونهٔ API را در کلاستری عملیاتی انجام دهید.)
1. فضای نام (namespace) کوبرنتیزی را که می‌خواهید سرویس API افزونه در آن اجرا شود، ایجاد کنید.
1. یک گواهی CA ایجاد یا تهیه کنید تا با آن گواهی سروری امضا شود که سرور API افزونه برای HTTPS به کار می‌برد.
1. یک گواهی و کلید سرور برای استفادهٔ سرور API در HTTPS ایجاد کنید. این گواهی باید با CA بالا امضا شده باشد و مقدار CN آن نیز باید نام DNS کوبرنتیز باشد. این نام از Service کوبرنتیز به دست می‌آید و قالب آن `<service name>.<service name namespace>.svc` است.
1. یک Secret کوبرنتیز حاوی گواهی و کلید سرور در فضای نام خود ایجاد کنید.
1. یک Deployment کوبرنتیز برای سرور API افزونه ایجاد کنید و مطمئن شوید که Secret را به‌صورت یک حجم (volume) بارگذاری می‌کنید. این Deployment باید به یک ایمیج سالم از سرور API افزونهٔ شما ارجاع دهد و همچنین باید در فضای نام شما قرار داشته باشد.
1. مطمئن شوید که سرور API افزونه آن گواهی‌ها را از همان حجم بارگذاری می‌کند و از آن‌ها در دست‌دهی (handshake) HTTPS استفاده می‌شود.
1. یک ServiceAccount کوبرنتیز در فضای نام خود ایجاد کنید.
1. یک ClusterRole کوبرنتیز برای عملیاتی که می‌خواهید روی منابع خود مجاز کنید، ایجاد کنید.
1. یک ClusterRoleBinding کوبرنتیز از ServiceAccount موجود در فضای نام خود به ClusterRole ایجادشده بسازید.
1. یک ClusterRoleBinding کوبرنتیز از ServiceAccount موجود در فضای نام خود به ClusterRole با نام `system:auth-delegator` بسازید تا تصمیم‌های احراز هویت و مجوزدهی به سرور API هستهٔ کوبرنتیز واگذار شود.
1. یک RoleBinding کوبرنتیز از ServiceAccount موجود در فضای نام خود به Role با نام `extension-apiserver-authentication-reader` بسازید. با این کار، سرور API افزونه می‌تواند به ConfigMap با نام `extension-apiserver-authentication` دسترسی داشته باشد.
1. یک APIService کوبرنتیز ایجاد کنید. گواهی CA بالا باید با base64 کدگذاری شود، خطوط جدید آن حذف شود و به‌عنوان spec.caBundle در APIService به کار رود. این آبجکت نباید به فضای نام خاصی تعلق داشته باشد. اگر از [API مربوط به kube-aggregator](https://github.com/kubernetes/kube-aggregator/) استفاده می‌کنید، فقط بستهٔ CA با کدگذاری PEM را ارسال کنید، زیرا کدگذاری base64 به‌طور خودکار برایتان انجام می‌شود.
1. با kubectl منبع خود را دریافت کنید. در این حالت، kubectl باید پیام "No resources found." را برگرداند. این پیام نشان می‌دهد که همه‌چیز درست کار کرده است، اما در حال حاضر هیچ آبجکتی از آن نوع منبع ایجاد نکرده‌اید.


## {{% heading "whatsnext" %}}


* مراحل [پیکربندی لایهٔ تجمیع API](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) و فعال‌سازی فلگ‌های apiserver را دنبال کنید.
* برای مروری کلی، [گسترش API کوبرنتیز با لایهٔ تجمیع](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) را ببینید.
* با نحوهٔ [گسترش API کوبرنتیز با استفاده از Custom Resource Definitionها](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) آشنا شوید.

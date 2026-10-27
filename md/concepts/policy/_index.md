---
title: "سیاست‌ها"
weight: 90
no_list: true
description: >
  مدیریت امنیت و بهترین روش‌ها با استفاده از سیاست‌ها.
---

<!-- overview -->

سیاست‌های کوبرنتیز پیکربندی‌هایی هستند که پیکربندی‌های دیگر یا رفتارهای زمان اجرا را مدیریت می‌کنند. کوبرنتیز اشکال مختلفی از سیاست‌ها را ارائه می‌دهد که در ادامه شرح داده شده‌اند:

<!-- body -->

## اعمال سیاست‌ها با استفاده از آبجکت‌های API

 برخی آبجکت‌های API نقش سیاست را ایفا می‌کنند. در اینجا چند نمونه آمده است:
* از [NetworkPolicyها](/docs/concepts/services-networking/network-policies/) می‌توان برای محدودکردن ترافیک ورودی و خروجی یک بار کاری استفاده کرد.
* [LimitRangeها](/docs/concepts/policy/limit-range/) محدودیت‌های تخصیص منابع را در میان انواع مختلف آبجکت مدیریت می‌کنند.
* [ResourceQuotaها](/docs/concepts/policy/resource-quotas/) مصرف منابع را برای یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} محدود می‌کنند.

## اعمال سیاست‌ها با استفاده از admission controllerها

یک {{< glossary_tooltip text="admission controller" term_id="admission-controller" >}}
در سرور API اجرا می‌شود
و می‌تواند درخواست‌های API را اعتبارسنجی یا تغییر دهد. برخی admission controllerها برای اعمال سیاست‌ها عمل می‌کنند.
برای مثال، admission controller ‏[AlwaysPullImages](/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages) یک Pod جدید را تغییر می‌دهد تا سیاست دریافت ایمیج را روی `Always` تنظیم کند.

کوبرنتیز چند admission controller داخلی دارد که از طریق پرچم `--enable-admission-plugins` سرور API قابل پیکربندی هستند.

جزئیات admission controllerها، همراه با فهرست کامل admission controllerهای موجود، در بخشی اختصاصی مستند شده است:

* [Admission Controllerها](/docs/reference/access-authn-authz/admission-controllers/)

## اعمال سیاست‌ها با استفاده از ValidatingAdmissionPolicy

سیاست‌های validating admission اجازه می‌دهند بررسی‌های اعتبارسنجی قابل پیکربندی با استفاده از Common Expression Language (CEL) در سرور API اجرا شوند. برای مثال، از یک `ValidatingAdmissionPolicy` می‌توان برای ممنوع‌کردن استفاده از تگ ایمیج `latest` استفاده کرد.

یک `ValidatingAdmissionPolicy` روی یک درخواست API عمل می‌کند و می‌توان از آن برای مسدودکردن، ممیزی و هشداردادن به کاربران دربارهٔ پیکربندی‌های ناسازگار با قواعد استفاده کرد.

جزئیات API ‏`ValidatingAdmissionPolicy`، همراه با مثال‌ها، در بخشی اختصاصی مستند شده است:
* [Validating Admission Policy](/docs/reference/access-authn-authz/validating-admission-policy/)


## اعمال سیاست‌ها با استفاده از کنترل پذیرش پویا

admission controllerهای پویا (یا admission webhookها) بیرون از سرور API و به‌صورت برنامه‌های جداگانه اجرا می‌شوند که ثبت‌نام می‌کنند تا درخواست‌های webhook را برای انجام اعتبارسنجی یا تغییر درخواست‌های API دریافت کنند. 

از admission controllerهای پویا می‌توان برای اعمال سیاست‌ها روی درخواست‌های API و راه‌اندازی سایر گردش‌کارهای مبتنی بر سیاست استفاده کرد. یک admission controller پویا می‌تواند بررسی‌های پیچیده‌ای انجام دهد، از جمله بررسی‌هایی که به بازیابی سایر منابع کلاستر و داده‌های خارجی نیاز دارند. برای مثال، یک بررسی تأیید ایمیج می‌تواند داده‌ها را از رجیستری‌های OCI جست‌وجو کند تا امضاها و گواهی‌های (attestations) ایمیج کانتینر را اعتبارسنجی کند.

جزئیات کنترل پذیرش پویا در بخشی اختصاصی مستند شده است:
* [کنترل پذیرش پویا](/docs/reference/access-authn-authz/extensible-admission-controllers/)

### پیاده‌سازی‌ها {#implementations-admission-control}

{{% thirdparty-content %}}

admission controllerهای پویایی که به‌عنوان موتورهای سیاست انعطاف‌پذیر عمل می‌کنند در اکوسیستم کوبرنتیز در حال توسعه هستند، مانند:
- [Kubewarden](https://github.com/kubewarden)
- [Kyverno](https://kyverno.io)
- [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper)
- [Polaris](https://polaris.docs.fairwinds.com/admission-controller/)

## اعمال سیاست‌ها با استفاده از پیکربندی‌های Kubelet

کوبرنتیز امکان پیکربندی Kubelet را روی هر نود کارگر فراهم می‌کند. برخی پیکربندی‌های Kubelet نقش سیاست را ایفا می‌کنند:
* از [محدودیت‌ها و رزروهای شناسهٔ فرایند](/docs/concepts/policy/pid-limiting/) برای محدودکردن و رزرو PIDهای قابل تخصیص استفاده می‌شود.
* [مدیران منابع نود](/docs/concepts/policy/node-resource-managers/) می‌توانند منابع محاسباتی، حافظه و دستگاه را برای بارهای کاری حساس به تأخیر و با توان عملیاتی بالا مدیریت کنند.

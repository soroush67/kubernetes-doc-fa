---
title: فعال یا غیرفعال کردن یک API در کوبرنتیز
content_type: task
weight: 200
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توانید یک نسخهٔ API را در
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کلاستر خود فعال یا غیرفعال کنید.

<!-- steps -->


برای روشن یا خاموش کردن نسخه‌های مشخصی از API، کافی است `--runtime-config=api/<version>` را به‌عنوان
آرگومان خط فرمان به سرور API بدهید. مقدار این آرگومان فهرستی از نسخه‌های API است که با کاما از هم
جدا شده‌اند. مقدارهای بعدی، مقدارهای پیشین را بازنویسی می‌کنند.

آرگومان خط فرمان `runtime-config` از دو کلید ویژه نیز پشتیبانی می‌کند:

- کلید `api/all` که نمایانگر همهٔ APIهای شناخته‌شده است.
- کلید `api/legacy` که فقط نمایانگر APIهای قدیمی (legacy) است. APIهای قدیمی همهٔ APIهایی هستند که به‌طور
   صریح [منسوخ (deprecated)](/docs/reference/using-api/deprecation-policy/) شده‌اند.

برای نمونه، برای خاموش کردن همهٔ نسخه‌های API به‌جز v1، مقدار `--runtime-config=api/all=false,api/v1=true`
را به `kube-apiserver` بدهید.

## {{% heading "whatsnext" %}}

[مستندات کامل](/docs/reference/command-line-tools-reference/kube-apiserver/)
مؤلفهٔ `kube-apiserver` را مطالعه کنید.

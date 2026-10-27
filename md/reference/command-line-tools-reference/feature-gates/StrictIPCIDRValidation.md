---
title: StrictIPCIDRValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
از اعتبارسنجی سخت‌گیرانه‌تر برای فیلدهایی که شامل آدرس‌های IP و مقادیر CIDR هستند استفاده می‌کند.

به‌طور مشخص، با فعال بودن این feature gate، در اکتت‌های (octet) آدرس‌های IPv4 هیچ صفر پیشرو (leading `0`) مجاز نیست و مقادیر IPv6 از نوع IPv4-mapped (برای مثال
`::ffff:192.168.0.1`) ممنوع هستند. این‌گونه مقادیر می‌توانند به‌طور بالقوه مشکلات امنیتی ایجاد کنند، زیرا اجزای مختلف ممکن است یک رشته‌ی یکسان را به‌صورت آدرس‌های IP متفاوت تفسیر کنند (مانند CVE-2021-29923).

این سخت‌گیری فقط در مورد فیلدهای موجود در API kindهای درون‌ساخت (built-in) اعمال می‌شود و شامل custom resource kindها، مقادیر موجود در فایل‌های پیکربندی کوبرنتیز یا آرگومان‌های خط فرمان نمی‌شود.

---
title: ExperimentalHostUserNamespaceDefaulting
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.5"  
    toVersion: "1.27" 
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.28"  
    toVersion: "1.29" 
removed: true
---
فعال‌سازی تنظیم پیش‌فرض فضای نام کاربر (user namespace) روی میزبان. این قابلیت برای کانتینرهایی در نظر گرفته شده است که از سایر فضاهای نام میزبان یا mountهای میزبان استفاده می‌کنند، یا کانتینرهای دارای سطح دسترسی ویژه (privileged) و کانتینرهایی که از قابلیت‌های (capabilities) خاصِ غیر وابسته به فضای نام استفاده می‌کنند (برای نمونه `MKNODE`، `SYS_MODULE` و مانند آن‌ها). این قابلیت را فقط در صورتی فعال کنید که بازنگاشت فضای نام کاربر (user namespace remapping) در Docker daemon فعال باشد.

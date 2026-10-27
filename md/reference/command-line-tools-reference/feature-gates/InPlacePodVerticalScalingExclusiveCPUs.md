---
title: InPlacePodVerticalScalingExclusiveCPUs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
---
امکان تغییر اندازه‌ی منابع را برای کانتینرها در Podهای دارای کلاس Guaranteed که درخواست CPU آن‌ها عدد صحیح است فعال می‌کند.
این قابلیت فقط در نودهایی کاربرد دارد که ویژگی‌های `InPlacePodVerticalScaling` و `CPUManager` در آن‌ها فعال باشد
و سیاست CPUManager روی `static` تنظیم شده باشد.

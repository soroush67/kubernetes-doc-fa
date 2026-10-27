---
title: EmptyDirVolumeMode
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
امکان تنظیم بیت‌های مجوز یونیکس (Unix) روی دایرکتوری‌های حجم (volume) از نوع `emptyDir` را با استفاده از فیلد
`mode` در منابع حجم `emptyDir` فراهم می‌کند. هنگامی که این قابلیت فعال باشد، کاربران می‌توانند مقداری
بین `0000` و `01777` (در مبنای هشت‌هشتی) مشخص کنند تا مجوزهای دایرکتوری در زمان ایجاد آن کنترل شود.
اگر `mode` مشخص نشود، رفتار پیش‌فرض `0777` حفظ می‌شود.

---
title: AllowUnsafeMalformedObjectDeletion
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
به اپراتور کلاستر امکان می‌دهد منابع خراب را با استفاده از عملیات **list** شناسایی کند و گزینه‌ای با نام `ignoreStoreReadErrorWithClusterBreakingPotential` معرفی می‌کند که اپراتور می‌تواند آن را تنظیم کند تا با استفاده از API کوبرنتیز، عملیات **delete** ناایمن و اجباری را روی این منابع خراب انجام دهد.

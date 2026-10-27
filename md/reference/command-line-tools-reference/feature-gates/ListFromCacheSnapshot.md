---
title: ListFromCacheSnapshot
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"

--- 
به API server امکان می‌دهد برای ذخیره‌گاه watch cache اسنپ‌شات تولید کند و از آن‌ها برای پاسخ‌گویی به درخواست‌های LIST استفاده کند.

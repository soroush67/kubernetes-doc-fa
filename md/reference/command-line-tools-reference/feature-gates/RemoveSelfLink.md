---
title: RemoveSelfLink
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.19"
  - stage: beta
    defaultValue: true
    fromVersion: "1.20"  
    toVersion: "1.23" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"  
    toVersion: "1.29"

removed: true
---
فیلد `.metadata.selfLink` را برای همه‌ی آبجکت‌ها و مجموعه‌ها (collections) روی مقدار خالی (رشته‌ی تهی) تنظیم می‌کند. این فیلد از نسخه‌ی v1.16 کوبرنتیز منسوخ شده است. هنگامی که این قابلیت فعال باشد، فیلد `.metadata.selfLink` همچنان بخشی از API کوبرنتیز باقی می‌ماند، اما همواره بدون مقدار (unset) است.

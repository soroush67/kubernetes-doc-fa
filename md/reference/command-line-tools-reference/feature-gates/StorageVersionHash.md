---
title: StorageVersionHash
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.14"
  - stage: beta
    defaultValue: true
    fromVersion: "1.15"
---
به API serverها اجازه می‌دهد هش نسخه ذخیره‌سازی (storage version hash) را در
فرایند discovery در دسترس قرار دهند.

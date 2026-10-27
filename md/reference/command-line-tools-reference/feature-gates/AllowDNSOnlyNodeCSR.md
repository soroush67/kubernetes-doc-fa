---
title: AllowDNSOnlyNodeCSR
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.31"
---
به kubelet اجازه می‌دهد بدون نیاز به هیچ آدرس IP نود، و تنها با استفاده از نام‌های DNS، درخواست گواهی (certificate) ارسال کند.

---
title: DRADeviceTaints
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
    toVersion: "1.37"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
پشتیبانی از
[اعمال taint روی دستگاه‌ها و تحمل انتخابی آن taintها](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations)
را هنگام استفاده از تخصیص پویای منابع (dynamic resource allocation) برای مدیریت دستگاه‌ها فعال می‌کند.

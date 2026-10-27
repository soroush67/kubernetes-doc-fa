---
title: DRADeviceTaintRules
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.37"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
پشتیبانی از
[اعمال taint روی دستگاه‌ها از طریق آبجکت‌های DeviceTaintRule](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations)
را هنگام استفاده از تخصیص پویای منابع (dynamic resource allocation) برای مدیریت دستگاه‌ها فعال می‌کند.

این feature gate تا زمانی که feature gate با نام `DRADeviceTaints` را نیز فعال نکنید، هیچ تأثیری ندارد.

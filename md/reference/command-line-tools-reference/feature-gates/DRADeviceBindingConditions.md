---
title: DRADeviceBindingConditions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
پشتیبانی از DeviceBindingConditions را در فیلدهای مرتبط با DRA فعال می‌کند.
این قابلیت امکان بررسی‌های دقیق آمادگی دستگاه و انجام فرایندهای اتصال (attachment) را پیش از مرحلهٔ Bind فراهم می‌کند.

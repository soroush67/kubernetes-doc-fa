---
title: MaxUnavailableStatefulSet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.24"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35.0"
    toVersion: "1.35.3"
  - stage: beta
    defaultValue: false
    fromVersion: "1.35.4"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
امکان تنظیم فیلد `maxUnavailable` را برای
[راهبرد به‌روزرسانی تدریجی](/docs/concepts/workloads/controllers/statefulset/#rolling-updates)
در StatefulSet فعال می‌کند. این فیلد حداکثر تعداد Podهایی را مشخص می‌کند
که در طول به‌روزرسانی می‌توانند در دسترس نباشند.

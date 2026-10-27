---
title: SkipReadOnlyValidationGCE
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"

removed: true
---
اعتبارسنجی اینکه حجم‌های (volume) از نوع GCE PersistentDisk در حالت فقط‌خواندنی قرار دارند، نادیده گرفته می‌شود.

---
title: DRAPrioritizedList
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
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    locked: false
    fromVersion: "1.36"
---
امکان مشخص‌کردن یک فهرست اولویت‌بندی‌شده از دستگاه‌های جایگزین را فراهم می‌کند که در صورت در دسترس نبودن گزینهٔ ترجیحی، می‌توان آن‌ها را در یک claim به یک درخواست تخصیص داد.

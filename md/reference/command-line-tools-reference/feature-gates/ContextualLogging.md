---
title: ContextualLogging
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.24"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
---
جزئیات اضافی را در خروجی لاگ مؤلفه‌های کوبرنتیز که از
contextual logging پشتیبانی می‌کنند فعال می‌کند.

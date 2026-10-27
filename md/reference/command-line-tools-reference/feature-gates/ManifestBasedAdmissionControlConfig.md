---
title: ManifestBasedAdmissionControlConfig
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
امکان بارگذاری وب‌هوک‌های admission و سیاست‌های admission مبتنی بر CEL را از فایل‌های مانیفست ایستا روی دیسک فراهم می‌کند. این بارگذاری از طریق فیلد `staticManifestsDir` در `AdmissionConfiguration` انجام می‌شود. این سیاست‌ها از زمان راه‌اندازی API server فعال هستند، در صورت در دسترس نبودن etcd همچنان برقرار می‌مانند و می‌توانند از منابع admission مبتنی بر API در برابر تغییر محافظت کنند.

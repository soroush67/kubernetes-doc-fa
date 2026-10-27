---
# Removed from Kubernetes
title: AttachVolumeLimit
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.16"
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.21"

removed: true
---
امکان می‌دهد افزونه‌های حجم (volume) محدودیت تعداد حجم‌هایی را که می‌توان به یک نود متصل کرد گزارش کنند.
برای جزئیات بیشتر به [محدودیت‌های پویای حجم](/docs/concepts/storage/storage-limits/#dynamic-volume-limits) مراجعه کنید.

---
# Removed from Kubernetes
title: MountContainers
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.16"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.17"
    toVersion: "1.17"

removed: true
---
امکان استفاده از کانتینرهای کمکی (utility containers) روی میزبان را به‌عنوان ابزار مانت‌کننده‌ی حجم (volume) فعال می‌کند.

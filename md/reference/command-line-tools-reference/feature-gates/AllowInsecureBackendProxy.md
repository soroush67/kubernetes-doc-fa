---
# Removed from Kubernetes
title: AllowInsecureBackendProxy
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.20"
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.25"

removed: true
---
به کاربران امکان می‌دهد در درخواست‌های لاگ Pod، از اعتبارسنجی TLS مربوط به kubeletها صرف‌نظر کنند.

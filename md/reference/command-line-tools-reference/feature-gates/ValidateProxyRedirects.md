---
# Removed from Kubernetes
title: ValidateProxyRedirects
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.13"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.21"    
  - stage: deprecated 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.24"

removed: true
---
این پرچم کنترل می‌کند که آیا API server باید اعتبارسنجی کند که ریدایرکت‌ها
فقط به همان میزبان (host) دنبال شوند یا خیر. این پرچم تنها در صورتی استفاده می‌شود که پرچم `StreamingProxyRedirects` فعال باشد.

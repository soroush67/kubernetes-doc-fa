---
title: ProxyTerminatingEndpoints
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.25"
  - stage: beta
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.29" 
removed: true
---
فعال‌سازی امکان مدیریت endpointهای در حال خاتمه (terminating) توسط kube-proxy، زمانی که `ExternalTrafficPolicy=Local` تنظیم شده باشد.

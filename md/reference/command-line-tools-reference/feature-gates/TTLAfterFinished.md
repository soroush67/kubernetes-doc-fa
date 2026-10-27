---
# Removed from Kubernetes
title: TTLAfterFinished
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    

removed: true
---
به یک [کنترل‌کننده TTL](/docs/concepts/workloads/controllers/ttlafterfinished/) اجازه می‌دهد
منابع را پس از پایان اجرای آن‌ها پاک‌سازی کند.

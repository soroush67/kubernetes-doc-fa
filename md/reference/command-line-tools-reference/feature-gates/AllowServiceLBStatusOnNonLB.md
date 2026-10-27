---
title: AllowServiceLBStatusOnNonLB
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.29"    
    toVersion: "1.34"

removed: true
---
امکان تنظیم فیلد `.status.ingress.loadBalancer` را روی Service هایی با نوعی غیر از `LoadBalancer` فراهم می‌کند.

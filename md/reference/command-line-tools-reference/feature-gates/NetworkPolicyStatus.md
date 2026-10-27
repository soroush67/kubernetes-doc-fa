---
title: NetworkPolicyStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.24"
    toVersion: "1.27"

removed: true
---
فعال‌سازی زیرمنبع (subresource) با نام `status` برای آبجکت‌های NetworkPolicy.

---
# Removed from Kubernetes
title: CustomResourceSubresources
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.10"
    toVersion: "1.10"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.15"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.18"

removed: true  
---
فعال‌سازی زیرمنبع‌های (subresources) `/status` و `/scale`
روی منابعی که از روی [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) ایجاد می‌شوند.

---
# Removed from Kubernetes
title: CustomResourceWebhookConversion
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.13"
    toVersion: "1.14"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.15"
    toVersion: "1.15"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.18"

removed: true  
---
فعال‌سازی تبدیل مبتنی بر وب‌هوک (webhook) برای منابع ایجادشده از روی [CustomResourceDefinition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

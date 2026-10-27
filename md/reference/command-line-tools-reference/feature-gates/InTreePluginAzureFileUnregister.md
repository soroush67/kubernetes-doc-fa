---
title: InTreePluginAzureFileUnregister
content_type: feature_gate
_build:
  list: never
  render: false
 
stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.21" 
    toVersion: "1.30"

removed: true
---
ثبت نشدن افزونه درون‌درختی (in-tree) azurefile در kubelet و کنترل‌کننده‌های حجم (volume) را موجب می‌شود.

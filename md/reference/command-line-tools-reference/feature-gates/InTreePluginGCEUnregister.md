---
title: InTreePluginGCEUnregister
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
ثبت افزونه درون‌درختی (in-tree) مربوط به gce-pd را در kubelet
و کنترل‌کننده‌های حجم (volume) متوقف می‌کند.

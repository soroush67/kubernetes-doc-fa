---
title: InTreePluginvSphereUnregister
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
ثبت‌نام افزونه درون‌درختی (in-tree) vSphere را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند.

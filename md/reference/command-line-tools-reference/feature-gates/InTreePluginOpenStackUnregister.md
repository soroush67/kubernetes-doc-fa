---
title: InTreePluginOpenStackUnregister
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
ثبت‌نشدن افزونه درون‌درختی (in-tree) OpenStack Cinder را در kubelet
و کنترل‌کننده‌های حجم (volume) فعال می‌کند؛ به این ترتیب این افزونه دیگر ثبت نمی‌شود.

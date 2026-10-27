---
title: InTreePluginAWSUnregister
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
ثبت‌نشدن افزونه درون‌درختی (in-tree) aws-ebs در kubelet و کنترل‌کننده‌های حجم (volume) را موجب می‌شود؛ به عبارت دیگر، این افزونه دیگر در آن‌ها ثبت نمی‌شود.

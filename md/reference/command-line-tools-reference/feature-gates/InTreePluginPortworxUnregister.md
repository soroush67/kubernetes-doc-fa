---
title: InTreePluginPortworxUnregister
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.35"

removed: true
---
ثبت‌نشدن افزونه درون‌درخت (in-tree) Portworx را در kubelet
و کنترل‌کننده‌های حجم (volume) فعال می‌کند؛ به این ترتیب، این افزونه دیگر در آن‌ها ثبت نمی‌شود.

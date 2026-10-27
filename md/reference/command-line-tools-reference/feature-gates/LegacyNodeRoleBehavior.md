---
# Removed from Kubernetes
title: LegacyNodeRoleBehavior
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.20"
  - stage: stable
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.22"

removed: true
---
هنگامی که این قابلیت غیرفعال باشد، رفتار قدیمی (legacy) در متعادل‌کننده‌های بار سرویس (service load balancers) و در مدیریت اختلال نود (node disruption)، برچسب `node-role.kubernetes.io/master` را نادیده می‌گیرد و به‌جای آن از برچسب‌های اختصاصی هر قابلیت که توسط `NodeDisruptionExclusion` و `ServiceNodeExclusion` فراهم می‌شوند، استفاده می‌کند.

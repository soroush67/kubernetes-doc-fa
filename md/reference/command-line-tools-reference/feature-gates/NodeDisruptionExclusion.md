---
# Removed from Kubernetes
title: NodeDisruptionExclusion
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
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"

removed: true
---
استفاده از برچسب Node با نام `node.kubernetes.io/exclude-disruption` را فعال می‌کند؛ این برچسب از تخلیه شدن نودها در زمان بروز خرابی در zone جلوگیری می‌کند.

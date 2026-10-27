---
# Removed from Kubernetes
title: LocalStorageCapacityIsolation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.7"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.24"
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"

removed: true
---
امکان مصرف
[ذخیره‌سازی موقت محلی](/docs/concepts/configuration/manage-resources-containers/)
و همچنین ویژگی `sizeLimit` در یک
[حجم emptyDir](/docs/concepts/storage/volumes/#emptydir)
را فعال می‌کند.

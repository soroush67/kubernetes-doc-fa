---
# Removed from Kubernetes
title: VolumeScheduling
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.12"
  - stage: stable
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true
---
زمان‌بندی آگاه از توپولوژی حجم (volume) را فعال می‌کند و باعث می‌شود اتصال (binding) PersistentVolumeClaim (PVC) نسبت به تصمیم‌های زمان‌بندی آگاه باشد. همچنین در صورت استفاده همراه با feature gate با نام `PersistentLocalVolumes`، امکان استفاده از نوع حجم [`local`](/docs/concepts/storage/volumes/#local) را فراهم می‌کند.

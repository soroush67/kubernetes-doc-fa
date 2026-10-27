---
# Removed from Kubernetes
title: StorageObjectInUseProtection
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.10"
  - stage: stable
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.24"    

removed: true   
---
در صورتی که آبجکت‌های PersistentVolume یا
PersistentVolumeClaim همچنان در حال استفاده باشند، حذف آن‌ها به تعویق می‌افتد.

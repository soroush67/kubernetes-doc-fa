---
title: HonorPVReclaimPolicy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
    toVersion: "1.35"

removed: true
---
سیاست بازیابی (reclaim policy) حجم پایدار (PersistentVolume) را در صورتی که مقدار آن `Delete` باشد، صرف‌نظر از ترتیب حذف PV و PVC رعایت می‌کند.
برای جزئیات بیشتر، مستندات
[PersistentVolume deletion protection finalizer](/docs/concepts/storage/persistent-volumes/#persistentvolume-deletion-protection-finalizer)
را مطالعه کنید.

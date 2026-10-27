---
title: StatefulSetAutoDeletePVC
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
استفاده از فیلد اختیاری `.spec.persistentVolumeClaimRetentionPolicy` را امکان‌پذیر می‌کند
و کنترل حذف PVCها را در چرخه عمر یک StatefulSet فراهم می‌سازد.
برای جزئیات بیشتر به
[نگهداری PersistentVolumeClaim](/docs/concepts/workloads/controllers/statefulset/#persistentvolumeclaim-retention)
مراجعه کنید.

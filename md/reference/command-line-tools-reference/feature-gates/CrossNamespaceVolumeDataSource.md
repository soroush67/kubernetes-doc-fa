---
title: CrossNamespaceVolumeDataSource
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.26"
---
استفاده از منبع داده حجم (volume) میان‌فضای‌نامی (cross namespace) را فعال می‌کند تا بتوانید یک فضای نام (namespace) مبدأ را در فیلد `dataSourceRef` یک PersistentVolumeClaim مشخص کنید.

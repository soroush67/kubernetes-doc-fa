---
title: PersistentVolumeClaimUnusedSinceTime
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
هنگامی که این قابلیت فعال باشد، کنترل‌کننده PVC protection یک شرط (condition) با نام `Unused` به PersistentVolumeClaimها اضافه می‌کند که مشخص می‌کند آیا PVC در حال حاضر توسط هیچ Pod غیرپایانی (non-terminal) مورد ارجاع قرار گرفته است یا خیر. فیلد `lastTransitionTime` در این شرط، زمان آخرین گذار PVC میان وضعیت در حال استفاده و وضعیت بدون استفاده را ثبت می‌کند.

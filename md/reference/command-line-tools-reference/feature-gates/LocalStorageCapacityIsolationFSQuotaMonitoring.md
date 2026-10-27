---
title: LocalStorageCapacityIsolationFSQuotaMonitoring
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.30"
  - stage: beta 
    defaultValue: false
    fromVersion: "1.31"
---
هنگامی که `LocalStorageCapacityIsolation` برای
[ذخیره‌سازی موقت محلی](/docs/concepts/configuration/manage-resources-containers/) فعال باشد،
سیستم فایل پشتیبان [حجم‌های emptyDir](/docs/concepts/storage/volumes/#emptydir) از سهمیه‌های پروژه (project quotas) پشتیبانی کند،
و `UserNamespacesSupport` فعال باشد،
به‌جای پیمایش سیستم فایل (filesystem walk)، از سهمیه‌های پروژه برای پایش میزان مصرف ذخیره‌سازی حجم `emptyDir` استفاده می‌شود که عملکرد و دقت بهتری را تضمین می‌کند.

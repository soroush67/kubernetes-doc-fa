---
title: StorageCapacityScoring
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
فیچر گیت `VolumeCapacityPriority` در نسخه v1.32 برای پشتیبانی از ذخیره‌سازی‌ای که به‌صورت ایستا (statically) تأمین می‌شود، استفاده می‌شد. از نسخه v1.33 به بعد، feature gate جدید `StorageCapacityScoring` جایگزین گیت قدیمی `VolumeCapacityPriority` شده است و پشتیبانی از ذخیره‌سازی تأمین‌شده به‌صورت پویا (dynamically) را نیز به آن افزوده است.
هنگامی که `StorageCapacityScoring` فعال باشد، افزونه VolumeBinding در kube-scheduler گسترش می‌یابد تا نودها را بر اساس ظرفیت ذخیره‌سازی هر یک از آن‌ها امتیازدهی کند.
این قابلیت برای حجم‌های (volume) CSI که از [ظرفیت ذخیره‌سازی](/docs/concepts/storage/storage-capacity/) پشتیبانی می‌کنند، از جمله ذخیره‌سازی محلی مبتنی بر درایور CSI، قابل استفاده است.

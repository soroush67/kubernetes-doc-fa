---
title: VolumeLimitScaling
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
قابلیت مقیاس‌دهی محدودیت حجم (volume) را برای درایورهای CSI فعال می‌کند. این قابلیت به زمان‌بند امکان می‌دهد در مورد محدودیت‌های ذخیره‌سازی هماهنگی بهتری با cluster-autoscaler داشته باشد.
برای اطلاعات بیشتر به [محدودیت‌های ذخیره‌سازی](/docs/concepts/storage/storage-limits/) مراجعه کنید.

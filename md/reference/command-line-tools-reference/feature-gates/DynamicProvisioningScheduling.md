---
# Removed from Kubernetes
title: DynamicProvisioningScheduling
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: deprecated
    fromVersion: "1.12"

removed: true  
---
زمان‌بند پیش‌فرض را به‌گونه‌ای توسعه می‌دهد که از توپولوژی حجم (volume) آگاه باشد و تأمین PV را مدیریت کند.
این قابلیت در نسخه v1.12 با قابلیت `VolumeScheduling` جایگزین شد.

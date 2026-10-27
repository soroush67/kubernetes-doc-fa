---
title: DRAResourceClaimDeviceStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    fromVersion: "1.37"
---
پشتیبانی از فیلد `ResourceClaim.status.devices` و همچنین امکان تنظیم این
وضعیت از سوی درایورهای DRA را فعال می‌کند. این قابلیت مستلزم فعال بودن
feature gate با نام `DynamicResourceAllocation` است.

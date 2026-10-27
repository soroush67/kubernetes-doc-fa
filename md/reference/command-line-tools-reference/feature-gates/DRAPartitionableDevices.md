---
title: DRAPartitionableDevices
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
پشتیبانی از درخواست [دستگاه‌های قابل‌پارتیشن‌بندی (Partitionable Devices)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)
را برای DRA فعال می‌کند. این قابلیت به درایورها امکان می‌دهد چندین دستگاه را معرفی کنند که به منابع یکسانی از یک دستگاه فیزیکی نگاشت می‌شوند.

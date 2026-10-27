---
title: DRADeviceCompatibilityGroups
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
پشتیبانی از [گروه‌های سازگاری دستگاه](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#device-compatibility-groups)
را در DRA فعال می‌کند. درایورها می‌توانند گروه‌های سازگاری مبهم (opaque) را برای هر ورودی `consumesCounters` از یک دستگاه در ResourceSlice تعریف کنند، و زمان‌بند
تنها در صورتی دستگاه‌هایی را که از یک مجموعه شمارنده (counter set) مشترک استفاده می‌کنند هم‌زمان تخصیص می‌دهد که گروه‌های اعلام‌شده‌ی آن‌ها اشتراک داشته باشند. نیازمند فعال بودن `DRAPartitionableDevices` است.

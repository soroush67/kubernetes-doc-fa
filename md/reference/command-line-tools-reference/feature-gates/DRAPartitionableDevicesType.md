---
title: DRAPartitionableDevicesType
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
فیلد `PartitionTypeAttribute` را روی ResourceSliceها فعال می‌کند؛ این فیلد یک مخزن منبع (resource pool) [قابل‌پارتیشن‌بندی](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices) را در نمای خلاصه‌شدهٔ نوع‌دار پارتیشن‌ها در
[ResourcePoolStatusRequest](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#resource-pool-partition-summary)
مشارکت می‌دهد. این فیلد نام یک ویژگی دستگاه (device attribute) را مشخص می‌کند (مانند یک پروفایل MIG) که مقدار آن، هر نوع پارتیشن را گروه‌بندی می‌کند، تا یک ResourcePoolStatusRequest بتواند گزارش دهد که از هر نوع پارتیشن چه تعداد دستگاه هنوز قابل تخصیص است. این قابلیت بر پایهٔ feature gateهای
[`DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
و
[`DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
ساخته شده است و هر دوی آن‌ها نیز باید فعال باشند.

---
title: CompositePodGroup
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---

فعال‌سازی زمان‌بندی گروهی سلسله‌مراتبی (hierarchical gang scheduling) برای [CompositePodGroups](/docs/concepts/workloads/compositepodgroup-api/) و PodGroups.

فعال‌کردن feature gate با نام `CompositePodGroup` مستلزم آن است که feature gateهای `GenericWorkload` و `TopologyAwareWorkloadScheduling` نیز فعال باشند.

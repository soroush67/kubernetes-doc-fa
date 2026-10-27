---
title: PodGroupPreemptionPolicy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---

پشتیبانی از فیلد `PreemptionPolicy` را در [PodGroup API](/docs/concepts/workloads/podgroup-api/) و [Workload API](/docs/concepts/workloads/workload-api/) فعال می‌کند.

در صورت فعال بودن، اگر یک PodGroup دارای `PreemptionPolicy: Never` باشد، پیش‌دستی (preemption) آگاه از بار کاری را انجام نخواهد داد.

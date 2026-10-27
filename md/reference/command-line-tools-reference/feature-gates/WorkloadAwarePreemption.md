---
title: WorkloadAwarePreemption
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"

removed: true
---

پشتیبانی از [پیش‌دستی آگاه از بار کاری (Workload-aware preemption)](/docs/concepts/scheduling-eviction/workload-aware-preemption/) را فعال می‌کند. این feature gate در نسخه 1.37 حذف شد و با feature gate با نام `GenericWorkload` ادغام گردید.

هنگامی که این قابلیت فعال باشد، اگر زمان‌بندی یک PodGroup با شکست مواجه شود، زمان‌بند به‌جای الگوریتم پیش‌فرض پیش‌دستی Pod، از یک الگوریتم پیش‌دستی آگاه از بار کاری برای انتخاب قربانیان پیش‌دستی استفاده می‌کند.

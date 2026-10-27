---
title: GenericWorkload
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
    defaultValue: false
    fromVersion: "1.37"
---

پشتیبانی از [Workload API](/docs/concepts/workloads/workload-api/) و [PodGroup API](/docs/concepts/workloads/podgroup-api/) را فعال می‌کند تا بتوان الزامات زمان‌بندی را در سطح بار کاری بیان کرد.

وقتی این قابلیت فعال باشد، Podها می‌توانند به یک PodGroup مشخص ارجاع دهند تا بر نحوهٔ زمان‌بندی خود تأثیر بگذارند. از کوبرنتیز نسخهٔ v1.37 به بعد، این feature gate شامل [زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) و [پیش‌دستی آگاه از بار کاری (workload-aware preemption)](/docs/concepts/scheduling-eviction/workload-aware-preemption/) نیز می‌شود.

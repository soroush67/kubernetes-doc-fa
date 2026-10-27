---
title: DRAWorkloadResourceClaims
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
  - stage: beta
    defaultValue: false
    fromVersion: "1.37"
---

به منابع PodGroup از [Workload API](/docs/concepts/workloads/workload-api/) امکان می‌دهد
از طریق
[تخصیص پویای منابع (Dynamic Resource Allocation)](/docs/concepts/resource-management/dynamic-resource-allocation/)
درخواست‌هایی برای دستگاه‌ها ثبت کنند
که Podهای عضو آن‌ها می‌توانند از آن دستگاه‌ها به‌صورت مشترک استفاده کنند.

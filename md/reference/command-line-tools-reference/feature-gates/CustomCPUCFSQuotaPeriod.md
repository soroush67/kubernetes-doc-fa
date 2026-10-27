---
title: CustomCPUCFSQuotaPeriod
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.12"
---
به نودها امکان می‌دهد مقدار `cpuCFSQuotaPeriod` را در
[پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/)
تغییر دهند.

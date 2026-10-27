---
title: JobReadyPods
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.23"
  - stage: beta
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.28"
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"

removed: true
---
امکان ردیابی تعداد Podهایی را فراهم می‌کند که [شرط (condition)](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) برابر با `Ready` دارند.
تعداد Podهای `Ready` در [وضعیت (status)](/docs/reference/kubernetes-api/workload-resources/job-v1/#JobStatus)
یک [Job](/docs/concepts/workloads/controllers/job) ثبت می‌شود.

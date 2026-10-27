---
title: JobPodReplacementPolicy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
امکان تعیین سیاست جایگزینی Podها را برای Podهای در حال خاتمه (terminating) در یک [Job](/docs/concepts/workloads/controllers/job) فراهم می‌کند.

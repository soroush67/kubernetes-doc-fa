---
title: ElasticIndexedJob
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
---
امکان مقیاس‌دهی افزایشی یا کاهشی Indexed Jobها را فراهم می‌کند؛ این کار با تغییر هم‌زمان هر دو فیلد
`spec.completions` و `spec.parallelism` به‌گونه‌ای انجام می‌شود که `spec.completions == spec.parallelism` برقرار باشد.
برای جزئیات بیشتر، مستندات [Indexed Jobهای الاستیک](/docs/concepts/workloads/controllers/job#elastic-indexed-jobs) را ببینید.

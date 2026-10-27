---
title: StatefulSetStartOrdinal
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
---
امکان پیکربندی شماره ترتیبی شروع (start ordinal) را در یک
StatefulSet فراهم می‌کند. برای جزئیات بیشتر به
[شماره ترتیبی شروع](/docs/concepts/workloads/controllers/statefulset/#start-ordinal)
مراجعه کنید.

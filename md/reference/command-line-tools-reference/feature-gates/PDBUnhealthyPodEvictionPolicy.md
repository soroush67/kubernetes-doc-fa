---
title: PDBUnhealthyPodEvictionPolicy
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
    toVersion: "1.32"

removed: true
---
فیلد `unhealthyPodEvictionPolicy` را در `PodDisruptionBudget` فعال می‌کند. این فیلد مشخص می‌کند که Podهای ناسالم چه زمانی باید برای تخلیه (eviction) در نظر گرفته شوند. برای جزئیات بیشتر، لطفاً به [سیاست تخلیه Pod ناسالم](/docs/tasks/run-application/configure-pdb/#unhealthy-pod-eviction-policy) مراجعه کنید.

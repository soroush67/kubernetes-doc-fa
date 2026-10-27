---
title: PodHasNetworkCondition
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.27"

removed: true
---
به kubelet امکان می‌دهد شرط [PodHasNetwork](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network) را روی پادها علامت‌گذاری کند. این feature gate در نسخه 1.28 به `PodReadyToStartContainersCondition` تغییر نام داد.

---
title: PodReadyToStartContainersCondition
former_titles:
  - PodHasNetworkCondition
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
    toVersion: "1.36"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.37"
---
به kubelet امکان می‌دهد شرط (condition) با نام [PodReadyToStartContainers](/docs/concepts/workloads/pods/pod-lifecycle/#pod-has-network) را روی Podها علامت‌گذاری کند.

این feature gate پیش‌تر با نام `PodHasNetworkCondition` شناخته می‌شد و شرط مرتبط با آن
`PodHasNetwork` نام داشت.

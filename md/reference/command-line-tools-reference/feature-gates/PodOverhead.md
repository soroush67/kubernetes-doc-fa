---
# Removed from Kubernetes
title: PodOverhead
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.17"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.23"
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"

removed: true
---
قابلیت [PodOverhead](/docs/concepts/scheduling-eviction/pod-overhead/) را فعال می‌کند تا سربار (overhead) پادها در محاسبه منابع لحاظ شود.

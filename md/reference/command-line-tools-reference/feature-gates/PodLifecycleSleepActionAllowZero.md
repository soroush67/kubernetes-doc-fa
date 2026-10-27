---
title: PodLifecycleSleepActionAllowZero
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
امکان تنظیم مقدار صفر را برای اکشن `sleep` در
[هوک‌های چرخه عمر کانتینر](/docs/concepts/containers/container-lifecycle-hooks/)
فعال می‌کند.

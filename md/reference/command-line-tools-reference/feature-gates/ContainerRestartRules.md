---
title: ContainerRestartRules
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"

  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
امکان پیکربندی سیاست راه‌اندازی مجدد (restart policy) و قوانین راه‌اندازی مجدد را در سطح کانتینر فعال می‌کند.
برای جزئیات بیشتر، [سیاست و قوانین راه‌اندازی مجدد کانتینر](/docs/concepts/workloads/pods/pod-lifecycle/#container-restart-rules) را ببینید.

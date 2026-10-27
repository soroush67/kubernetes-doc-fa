---
title: GracefulNodeShutdownBasedOnPodPriority
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
---
به kubelet امکان می‌دهد هنگام خاموش‌سازی graceful (تدریجی و با مهلت مناسب) یک نود، اولویت Podها را بررسی کند.

---
title: HPAScaleToZero
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
امکان تنظیم `minReplicas` روی مقدار 0 را برای منابع `HorizontalPodAutoscaler` فراهم می‌کند، در صورتی که از متریک‌های سفارشی یا خارجی استفاده شود.

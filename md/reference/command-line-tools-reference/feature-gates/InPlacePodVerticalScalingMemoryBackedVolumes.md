---
title: InPlacePodVerticalScalingMemoryBackedVolumes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
مقیاس‌پذیری عمودی درجا (in-place) را برای محدودیت اندازه حجم‌های (volume) `emptyDir` مبتنی بر حافظه فعال می‌کند.

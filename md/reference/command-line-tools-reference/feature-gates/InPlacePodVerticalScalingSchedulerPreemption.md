---
title: InPlacePodVerticalScalingSchedulerPreemption
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
زمان‌بند را قادر می‌سازد تا برای برآورده کردن درخواست‌های به‌تعویق‌افتاده‌ی تغییر اندازه‌ی درجا (in-place) پادها، پادهای دارای اولویت پایین‌تر را پیش‌دستی (preempt) کند.

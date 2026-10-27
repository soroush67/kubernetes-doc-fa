---
title: TopologyManagerPolicyBetaOptions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.27"
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
---
امکان تنظیم دقیق سیاست‌های مدیر توپولوژی (topology manager) را فراهم می‌کند؛
این گزینه‌ها آزمایشی هستند و کیفیت آن‌ها در سطح بتا است.
این feature gate مجموعه‌ای از گزینه‌های مدیر توپولوژی را کنترل می‌کند که سطح کیفیت آن‌ها بتا است.
این feature gate هرگز به مرحله پایدار ارتقا نخواهد یافت.

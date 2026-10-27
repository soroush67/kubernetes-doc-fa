---
title: TopologyManagerPolicyAlphaOptions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
---
امکان تنظیم دقیق سیاست‌های topology manager را فراهم می‌کند؛
این گزینه‌ها آزمایشی و با کیفیت آلفا هستند.
این feature gate از *گروهی* از گزینه‌های topology manager محافظت می‌کند که سطح کیفیت آن‌ها آلفا است.
این feature gate هرگز به مرحله بتا یا پایدار ارتقا نخواهد یافت.

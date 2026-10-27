---
title: CPUManagerPolicyAlphaOptions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
---
این گزینه امکان تنظیم دقیق سیاست‌های CPUManager را فراهم می‌کند؛
گزینه‌هایی آزمایشی و با کیفیت آلفا.
این feature gate یک *گروه* از گزینه‌های CPUManager را کنترل می‌کند که سطح کیفیت آن‌ها آلفا است.
این feature gate هرگز به مرحله بتا یا پایدار ارتقا نخواهد یافت.

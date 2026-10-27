---
title: PodLogsQuerySplitStreams
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
---
امکان دریافت جریان‌های لاگ مشخص (یعنی stdout یا stderr) از میان جریان‌های لاگ یک کانتینر را با استفاده از API مربوط به Pod فراهم می‌کند.

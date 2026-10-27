---
title: GracefulNodeShutdown
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: beta
    defaultValue: true
    fromVersion: "1.21"
---
پشتیبانی از خاموش‌شدن مرتب (graceful shutdown) را در kubelet فعال می‌کند.
هنگام خاموش‌شدن سیستم، kubelet تلاش می‌کند رویداد خاموش‌شدن را شناسایی کند
و Podهای در حال اجرا روی نود را به‌صورت مرتب خاتمه دهد. برای جزئیات بیشتر به
[خاموش‌شدن مرتب نود](/docs/concepts/architecture/nodes/#graceful-node-shutdown)
مراجعه کنید.

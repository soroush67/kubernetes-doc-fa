---
title: ContainerStopSignals
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.33"
---
امکان استفاده از چرخه حیات StopSignal را برای کانتینرها فعال می‌کند تا بتوان سیگنال‌های توقف سفارشی را پیکربندی کرد که کانتینرها با استفاده از آن‌ها متوقف می‌شوند.

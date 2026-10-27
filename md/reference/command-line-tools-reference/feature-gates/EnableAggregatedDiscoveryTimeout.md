---
# Removed from Kubernetes
title: EnableAggregatedDiscoveryTimeout
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.16"
    toVersion: "1.17"

removed: true  

---
فعال‌سازی مهلت زمانی پنج‌ثانیه‌ای
برای فراخوانی‌های کشف تجمیعی (aggregated discovery).

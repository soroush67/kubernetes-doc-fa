---
title: TaintTolerationComparisonOperators
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
---
عملگرهای مقایسه‌ای عددی (`Lt` و `Gt`) را برای
[تحمل‌ها (tolerations)](/docs/concepts/scheduling-eviction/taint-and-toleration/)
فعال می‌کند.

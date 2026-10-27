---
title: MatchLabelKeysInPodTopologySpreadSelectorMerge
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
فعال‌سازی ادغام انتخابگرهای (selector) ساخته‌شده از `matchLabelKeys` در `labelSelector` مربوط به
[محدودیت‌های توزیع توپولوژی Pod](/docs/concepts/scheduling-eviction/topology-spread-constraints/).
این feature gate را می‌توان زمانی فعال کرد که قابلیت `matchLabelKeys` با feature flag با نام `MatchLabelKeysInPodTopologySpread` فعال شده باشد.

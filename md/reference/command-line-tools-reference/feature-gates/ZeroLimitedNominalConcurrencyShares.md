---
title: ZeroLimitedNominalConcurrencyShares
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"

removed: true
---
به [اولویت و انصاف (priority & fairness)](/docs/concepts/cluster-administration/flow-control/)
در API server اجازه می‌دهد که برای فیلد `nominalConcurrencyShares` در بخش `limited` از یک سطح اولویت (priority level)، مقدار صفر را به کار ببرد.

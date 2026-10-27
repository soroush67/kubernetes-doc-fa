---
title: PreventStaticPodAPIReferences
content_type: feature_gate

_build:
  list: never
  render: false

stages:
- stage: beta
  defaultValue: true
  fromVersion: "1.34"

---
در صورتی که Podهای ایستا (static Pod) به سایر آبجکت‌های API ارجاع دهند، پذیرش (admission) آن Podها رد می‌شود.

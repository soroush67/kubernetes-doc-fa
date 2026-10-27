---
title: CRDObservedGenerationTracking
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.35"
---
امکان ردیابی observed generation را در شرایط (conditions) مربوط به CRD فراهم می‌کند. تنظیم این مقدار به
false باعث می‌شود observed generation از شرایط CRD پاک شود.

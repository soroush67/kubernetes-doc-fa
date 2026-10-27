---
title: GangScheduling
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.36"

removed: true
---

افزونه GangScheduling را در kube-scheduler فعال می‌کند که الگوریتم زمان‌بندی «همه یا هیچ» (all-or-nothing) را پیاده‌سازی می‌کند. برای بیان الزامات، از [Workload API](/docs/concepts/workloads/workload-api/) استفاده می‌شود.

این feature gate در نسخه 1.37 حذف شد و با feature gate با نام `GenericWorkload` ادغام گردید.

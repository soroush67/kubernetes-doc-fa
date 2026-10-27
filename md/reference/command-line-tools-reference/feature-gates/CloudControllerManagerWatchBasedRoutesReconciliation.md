---
title: CloudControllerManagerWatchBasedRoutesReconciliation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
---
یک سازوکار هم‌سان‌سازی مسیرها (route) مبتنی بر watch را فعال می‌کند (به‌جای هم‌سان‌سازی در یک بازه زمانی ثابت)
در کتابخانه cloud-controller-manager.

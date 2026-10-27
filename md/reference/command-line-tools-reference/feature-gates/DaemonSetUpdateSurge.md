---
title: DaemonSetUpdateSurge
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"

removed: true  
---
به بارهای کاری DaemonSet امکان می‌دهد در طول به‌روزرسانی، در هر نود
دسترس‌پذیری خود را حفظ کنند.
به [انجام به‌روزرسانی تدریجی روی یک DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/) مراجعه کنید.

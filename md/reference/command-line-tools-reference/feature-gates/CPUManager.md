---
title: CPUManager
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: beta
    defaultValue: true
    fromVersion: "1.10"  
    toVersion: "1.25" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.32"

removed: true
---
فعال‌سازی پشتیبانی از تخصیص وابستگی CPU (CPU affinity) در سطح کانتینر؛ برای اطلاعات بیشتر به [سیاست‌های مدیریت CPU](/docs/tasks/administer-cluster/cpu-management-policies/) مراجعه کنید.

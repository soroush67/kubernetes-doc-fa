---
title: MutablePodResourcesForSuspendedJobs 
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
removed: false
---
امکان اعمال patch بر قالب‌های Pod در Jobهای معلق‌شده (suspended) را فعال می‌کند تا بتوان درخواست‌ها (requests) یا محدودیت‌های (limits) منابع زیرساختی را تغییر داد.

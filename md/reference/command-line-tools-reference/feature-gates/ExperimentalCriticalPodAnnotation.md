---
# Removed from Kubernetes
title: ExperimentalCriticalPodAnnotation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.5"
    toVersion: "1.12"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true  
---
امکان حاشیه‌نویسی (annotation) پادهای مشخص به‌عنوان پاد *حیاتی* (critical) را فراهم می‌کند، به‌طوری که [زمان‌بندی آن‌ها تضمین شود](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/).
این قابلیت از نسخه v1.13 به‌دلیل معرفی Pod Priority و Preemption منسوخ شده است.

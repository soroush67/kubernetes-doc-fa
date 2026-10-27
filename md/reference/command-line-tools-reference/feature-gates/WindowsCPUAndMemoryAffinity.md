---
title: WindowsCPUAndMemoryAffinity
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
---

افزودن پشتیبانی از وابستگی (affinity) پردازنده و حافظه به نودهای ویندوزی با استفاده از [CPUManager](/docs/tasks/administer-cluster/cpu-management-policies/#windows-support)،
[MemoryManager](/docs/tasks/administer-cluster/memory-manager/#windows-support)
و topology manager.

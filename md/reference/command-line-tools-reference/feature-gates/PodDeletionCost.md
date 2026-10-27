---
title: PodDeletionCost
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
---
قابلیت [هزینه حذف Pod](/docs/concepts/workloads/controllers/replicaset/#pod-deletion-cost) (Pod Deletion Cost) را فعال می‌کند؛ قابلیتی که به کاربران امکان می‌دهد بر ترتیب کاهش مقیاس (downscaling) یک ReplicaSet تأثیر بگذارند.

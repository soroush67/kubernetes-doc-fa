---
title: MutablePVNodeAffinity
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
---
امکان به‌روزرسانی فیلد `.spec.nodeAffinity` در یک PersistentVolume را فراهم می‌کند.
برای جزئیات بیشتر به [به‌روزرسانی‌های node affinity](/docs/concepts/storage/persistent-volumes/#updates-to-node-affinity) مراجعه کنید.

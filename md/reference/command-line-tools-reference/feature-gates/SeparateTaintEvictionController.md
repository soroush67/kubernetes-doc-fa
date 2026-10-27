---
title: SeparateTaintEvictionController
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
اجرای کنترل‌کننده _taint based eviction_ را که [Taint-based Evictions](/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions) را انجام می‌دهد، به‌صورت یک کنترل‌کننده مستقل (جدا از کنترل‌کننده _node lifecycle_) فعال می‌کند.

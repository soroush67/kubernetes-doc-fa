---
# Removed from Kubernetes
title: VolumeSubpath
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.24"

removed: true
---
امکان مانت کردن یک مسیر فرعی (subpath) از یک حجم (volume) را در یک کانتینر فراهم می‌کند.

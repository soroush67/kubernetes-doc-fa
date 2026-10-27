---
# Removed from Kubernetes
title: PreferNominatedNode
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
    toVersion: "1.23"
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"

removed: true
---
این پرچم به زمان‌بند مشخص می‌کند که آیا نودهای نامزدشده (nominated) پیش از پیمایش سایر نودهای کلاستر، ابتدا بررسی شوند یا خیر.

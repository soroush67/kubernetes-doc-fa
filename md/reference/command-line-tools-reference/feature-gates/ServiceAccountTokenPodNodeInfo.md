---
title: ServiceAccountTokenPodNodeInfo
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
مشخص می‌کند که آیا apiserver هنگام صدور توکن‌های service account که به آبجکت‌های Pod متصل (bound) شده‌اند، نام نود و uid نود مرتبط را در توکن درج کند یا خیر.

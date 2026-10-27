---
title: StreamingCollectionEncodingToJSON
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
به رمزگذار JSON در API server اجازه می‌دهد مجموعه‌ها (collections) را به‌جای رمزگذاری یکجا، آیتم به آیتم رمزگذاری کند.

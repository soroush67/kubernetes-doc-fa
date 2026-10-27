---
title: StreamingCollectionEncodingToProtobuf
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"

---
به رمزگذار (encoder) Protobuf در سرور API اجازه می‌دهد مجموعه‌ها (collections) را به‌جای رمزگذاری یکجا، مورد به مورد رمزگذاری کند.

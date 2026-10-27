---
title: JobSuccessPolicy
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
به کاربران اجازه می‌دهد مشخص کنند که یک Job در چه شرایطی، بر اساس مجموعه Podهای موفق‌شده، می‌تواند موفق‌شده اعلام شود.

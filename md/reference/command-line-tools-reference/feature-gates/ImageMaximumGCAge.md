---
title: ImageMaximumGCAge
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
    toVersion: "1.34"
  - stage: stable
    defaultValue: true
    fromVersion: "1.35"
---
فیلد پیکربندی `imageMaximumGCAge` در kubelet را فعال می‌کند و به مدیر کلاستر اجازه می‌دهد مشخص کند که یک ایمیج پس از گذشت چه مدت زمانی، جمع‌آوری زباله (garbage collection) شود.

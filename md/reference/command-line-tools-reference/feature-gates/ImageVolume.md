---
title: ImageVolume
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
امکان استفاده از منبع حجم (volume) از نوع [`image`](/docs/concepts/storage/volumes/) را در یک Pod فراهم می‌کند.
این منبع حجم به شما امکان می‌دهد یک ایمیج کانتینر را به‌صورت یک حجم (volume) فقط‌خواندنی مانت کنید.

---
title: NodeDeclaredFeatures
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.37"
---
به نودها امکان می‌دهد قابلیت‌های پشتیبانی‌شده را از طریق `.status` خود گزارش کنند. این امر به زمان‌بند و admission controller اجازه می‌دهد از اجرای عملیات روی نودهایی که فاقد قابلیت‌های موردنیاز Pod هستند جلوگیری کنند. به [قابلیت‌های اعلام‌شده توسط نود](/docs/concepts/scheduling-eviction/node-declared-features/) مراجعه کنید.

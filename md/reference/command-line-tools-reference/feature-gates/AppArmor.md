---
title: AppArmor
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.4"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
استفاده از کنترل دسترسی اجباری AppArmor را برای Podهایی که روی نودهای لینوکس اجرا می‌شوند فعال می‌کند.
برای جزئیات بیشتر، [آموزش AppArmor](/docs/tutorials/security/apparmor/) را ببینید.

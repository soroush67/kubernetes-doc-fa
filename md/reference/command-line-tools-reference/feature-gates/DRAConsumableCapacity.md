---
title: DRAConsumableCapacity
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
امکان اشتراک‌گذاری یک دستگاه میان چندین ResourceClaim یا چندین درخواست را فراهم می‌کند.

افزون بر این، اگر دستگاهی از اشتراک‌گذاری پشتیبانی کند، منبع (ظرفیت) آن را می‌توان از طریق یک سیاست اشتراک‌گذاری تعریف‌شده مدیریت کرد.

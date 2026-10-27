---
title: DynamicResourceAllocation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: beta
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    locked: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.35"

---
پشتیبانی از منابعی را فعال می‌کند که پارامترهای سفارشی دارند و چرخه عمر آن‌ها مستقل از Pod است. تخصیص منابع بر اساس «پارامترهای ساختاریافته» (structured parameters) توسط زمان‌بند کوبرنتیز انجام می‌شود.

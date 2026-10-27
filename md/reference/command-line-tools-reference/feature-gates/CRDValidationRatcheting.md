---
title: CRDValidationRatcheting
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    fromVersion: "1.33"
---
امکان به‌روزرسانی منابع سفارشی (custom resources) را فراهم می‌کند، به‌گونه‌ای که حتی اگر منبع شامل موارد نقض طرح‌واره OpenAPI خود باشد، به‌روزرسانی پذیرفته شود، مشروط بر اینکه بخش‌های دارای نقض در آن به‌روزرسانی تغییر نکرده باشند. برای جزئیات بیشتر به [Validation Ratcheting](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-ratcheting) مراجعه کنید.

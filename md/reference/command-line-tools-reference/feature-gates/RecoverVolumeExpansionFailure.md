---
title: RecoverVolumeExpansionFailure
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.31"
  - stage: beta
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34" 
---
به کاربران امکان می‌دهد PVCهای خود را به اندازه‌های کوچک‌تر ویرایش کنند تا بتوانند از شکست‌های قبلاً رخ‌داده در گسترش حجم (volume) بازیابی کنند.
برای جزئیات بیشتر به [بازیابی از شکست در هنگام گسترش حجم‌ها](/docs/concepts/storage/persistent-volumes/#recovering-from-failure-when-expanding-volumes) مراجعه کنید.

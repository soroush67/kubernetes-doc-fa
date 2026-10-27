---
title: RuntimeClassInImageCriApi
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
---
امکان دریافت (pull) ایمیج‌ها را بر اساس [کلاس زمان اجرا (runtime class)](/docs/concepts/containers/runtime-class/) پادهایی که به آن‌ها ارجاع می‌دهند فراهم می‌کند.

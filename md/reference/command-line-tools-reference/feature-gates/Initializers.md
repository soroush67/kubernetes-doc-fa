---
title: Initializers
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.7"
    toVersion: "1.13"
  - stage: deprecated
    fromVersion: "1.14"
    toVersion: "1.14"

removed: true
---
امکان هماهنگی ناهمگام (asynchronous) در ایجاد آبجکت‌ها را با استفاده از
افزونه admission با نام Initializers فراهم می‌کند.

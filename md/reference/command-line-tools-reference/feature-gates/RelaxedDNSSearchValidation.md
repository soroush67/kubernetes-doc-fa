---
title: RelaxedDNSSearchValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.36"

removed: true
---
اعتبارسنجی سمت سرور برای رشته‌ی جست‌وجوی DNS
(`.spec.dnsConfig.searches`) کانتینرها را تسهیل می‌کند. برای مثال،
با فعال بودن این gate، می‌توان نویسه‌ی `_` را
در رشته‌ی جست‌وجوی نام DNS گنجاند.

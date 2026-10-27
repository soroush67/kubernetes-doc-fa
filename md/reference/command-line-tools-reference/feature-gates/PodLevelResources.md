---
title: PodLevelResources
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
فعال‌سازی _منابع در سطح Pod_: امکان تعیین درخواست‌ها (requests) و محدودیت‌های (limits) منابع در سطح Pod، به‌جای تعیین آن‌ها فقط برای کانتینرهای مشخص.

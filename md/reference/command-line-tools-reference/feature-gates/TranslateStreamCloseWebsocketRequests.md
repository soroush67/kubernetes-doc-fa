---
title: TranslateStreamCloseWebsocketRequests
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
---
امکان استریم WebSocket برای زیرپروتکل دستور راه دور (`exec`، `cp`، `attach`) را برای کلاینت‌هایی فراهم می‌کند که نسخه ۵ (v5) این زیرپروتکل را درخواست می‌کنند.

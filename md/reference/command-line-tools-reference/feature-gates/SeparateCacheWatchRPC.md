---
title: SeparateCacheWatchRPC
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"

---
به watch cache در سرور API اجازه می‌دهد یک watch را روی یک RPC اختصاصی ایجاد کند.
این کار از گرسنگی منابع (starvation) در watch cache به‌دلیل سایر watchها جلوگیری می‌کند.

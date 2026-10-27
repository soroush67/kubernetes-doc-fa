---
title: ConcurrentWatchObjectDecode
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"

---
فعال‌سازی رمزگشایی هم‌زمان آبجکت‌های watch. این قابلیت برای جلوگیری از گرسنگی منابع (starvation) در watch cache سرور API در زمان نصب‌بودن یک conversion webhook در نظر گرفته شده است.

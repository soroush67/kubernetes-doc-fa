---
title: ReduceDefaultCrashLoopBackOffDecay
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
---
کاهش هم تأخیر اولیه و هم حداکثر تأخیری که میان راه‌اندازی مجدد کانتینرها برای یک نود انباشته می‌شود، برای کانتینرهایی که در وضعیت `CrashLoopBackOff` قرار دارند، در سراسر کلاستر فعال شده است؛ به‌طوری که تأخیر اولیه `1s` و حداکثر تأخیر `60s` خواهد بود.

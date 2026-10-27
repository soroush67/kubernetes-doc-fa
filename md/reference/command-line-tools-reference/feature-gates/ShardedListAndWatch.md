---
title: ShardedListAndWatch
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
پشتیبانی از پارامتر `shardSelector` را در درخواست‌های **list** و **watch** فعال می‌کند.
این قابلیت به کلاینت‌ها اجازه می‌دهد زیرمجموعه‌ای فیلترشده از آبجکت‌ها را بر پایه بازه‌های هش
فیلدهای فراداده (metadata) مانند UID دریافت کنند. برای جزئیات بیشتر، به
[List و watch شاردشده](/docs/reference/using-api/api-concepts/#sharded-list-and-watch)
مراجعه کنید.

---
title: WatchListClient
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
به یک کلاینت API اجازه می‌دهد به‌جای دریافت یک فهرست کامل، یک جریان (stream) از داده‌ها را درخواست کند.
این قابلیت در `client-go` در دسترس است و نیازمند آن است که قابلیت
[WatchList](/docs/reference/command-line-tools-reference/feature-gates/)
در سمت سرور فعال باشد.
اگر `WatchList` در سمت سرور پشتیبانی نشود، کلاینت به‌طور یکپارچه به یک درخواست list استاندارد بازمی‌گردد.

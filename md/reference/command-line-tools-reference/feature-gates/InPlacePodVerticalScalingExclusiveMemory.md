---
title: InPlacePodVerticalScalingExclusiveMemory
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
---
امکان تغییر اندازهٔ منابع را برای کانتینرها در Podهای Guaranteed فراهم می‌کند، زمانی که سیاست memory manager روی `"Static"` تنظیم شده باشد.
این قابلیت فقط برای نودهایی اعمال می‌شود که ویژگی‌های `InPlacePodVerticalScaling` و memory manager در آن‌ها فعال شده باشد.

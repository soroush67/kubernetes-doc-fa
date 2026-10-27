---
title: WatchListCompression
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
فشرده‌سازی پاسخ‌های
[_watch list_](/docs/reference/using-api/api-concepts/#streaming-lists)
را از سمت API server فعال می‌کند.
اگر `WatchList` غیرفعال باشد، این feature gate تأثیری ندارد.

---
title: CBORServingAndStorage
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
---
CBOR را به‌عنوان یک کدگذاری پشتیبانی‌شده برای درخواست‌ها و
پاسخ‌ها ([کدگذاری CBOR](/docs/reference/using-api/api-concepts/#cbor-encoding)) و همچنین به‌عنوان کدگذاری ترجیحی ذخیره‌سازی
برای منابع سفارشی (custom resources) فعال می‌کند.

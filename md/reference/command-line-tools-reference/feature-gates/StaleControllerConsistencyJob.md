---
title: StaleControllerConsistencyJob
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
رفتاری را در کنترل‌کننده Job فعال می‌کند که تضمین می‌کند نوشتن‌های قبلی روی
سرور API پیش از ادامهٔ هماهنگ‌سازی (reconciliation) بیشتر برای همان Job مشاهده شده‌اند.
هدف این است که از ایجاد به‌روزرسانی‌های نادرست یا ناخواسته در Job به‌دلیل کهنه‌بودن کش (cache) جلوگیری شود.

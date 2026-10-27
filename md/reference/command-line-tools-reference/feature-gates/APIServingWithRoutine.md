---
title: APIServingWithRoutine
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.30"
---
این feature gate یک بهبود عملکردی برای API server فعال می‌کند:
API server می‌تواند از goroutineهای جداگانه (رشته‌های سبک مدیریت‌شده توسط زمان‌اجرای Go)
برای پاسخ‌گویی به درخواست‌های [**watch**](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)
استفاده کند.

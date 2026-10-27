---
title: UnauthenticatedHTTP2DOSMitigation
content_type: feature_gate
_build:
  list: never
  render: false
 
stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29" 
---
اقدامات کاهش‌دهنده‌ی حمله‌ی منع سرویس (DoS) در HTTP/2 را برای کلاینت‌های احراززهویت‌نشده فعال می‌کند.
کوبرنتیز نسخه‌های v1.28.0 تا v1.28.2 این feature gate را شامل نمی‌شوند.

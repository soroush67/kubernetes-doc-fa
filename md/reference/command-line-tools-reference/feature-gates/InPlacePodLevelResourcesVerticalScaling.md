---
title: InPlacePodLevelResourcesVerticalScaling
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
امکان مقیاس‌دهی عمودی درجا (in-place) منابع را برای یک Pod فعال می‌کند (برای مثال، تغییر درخواست‌ها/محدودیت‌های CPU یا حافظه در سطح Pod برای یک Pod در حال اجرا، بدون نیاز به راه‌اندازی مجدد آن). برای جزئیات بیشتر، به مستندات [مقیاس‌دهی عمودی درجا منابع در سطح Pod](/docs/tasks/configure-pod-container/resize-pod-resources/) مراجعه کنید.

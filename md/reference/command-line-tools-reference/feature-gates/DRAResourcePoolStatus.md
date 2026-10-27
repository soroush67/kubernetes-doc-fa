---
title: DRAResourcePoolStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
API مربوط به ResourcePoolStatusRequest را فعال می‌کند که برای پرس‌وجو درباره‌ی
[در دسترس بودن دستگاه‌ها در استخرهای منابع DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#resource-pool-status) به کار می‌رود.
در صورت فعال بودن، کاربران می‌توانند آبجکت‌های ResourcePoolStatusRequest را ایجاد کنند تا
یک تصویر لحظه‌ای از وضعیت در دسترس بودن دستگاه‌ها (دستگاه‌های کل، تخصیص‌یافته، در دسترس و
غیرقابل‌دسترس) را برای یک درایور مشخص و در صورت نیاز برای یک استخر مشخص دریافت کنند.
یک کنترل‌کننده در kube-controller-manager این درخواست‌های یک‌باره را پردازش می‌کند و
وضعیت (status) را با اطلاعات استخر تکمیل می‌کند.

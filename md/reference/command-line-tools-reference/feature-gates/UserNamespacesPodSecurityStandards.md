---
title: UserNamespacesPodSecurityStandards
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.34"

removed: true
---
امکان تعدیل (شل‌سازی) سیاست‌های Pod Security Standards را برای پادهایی فراهم می‌کند
که با user namespace اجرا می‌شوند. باید مقدار این feature gate را در تمام نودهای
کلاستر خود به‌صورت یکسان تنظیم کنید و برای استفاده از این قابلیت، باید `UserNamespacesSupport` را نیز فعال نمایید.

این feature gate در کوبرنتیز نسخه v1.35 (و نسخه‌های پس از آن) وجود ندارد، زیرا
در این نسخه‌های کوبرنتیز، تمام نسخه‌های پشتیبانی‌شده‌ی kubelet در صورتی که یک Pod درخواست user namespace کند
ولی نود از آن پشتیبانی نکند، از ایجاد Pod ناموفق خواهند ماند.

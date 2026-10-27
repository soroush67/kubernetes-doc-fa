---
title: DRAAdminAccess
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
پشتیبانی از درخواست [دسترسی مدیریتی (admin access)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#admin-access)
در ResourceClaim یا ResourceClaimTemplate را فعال می‌کند. دسترسی مدیریتی، امکان دسترسی به
دستگاه‌های در حال استفاده را فراهم می‌کند و ممکن است هنگام در دسترس قرار دادن دستگاه
در یک کانتینر، مجوزهای اضافی نیز فعال شود. از کوبرنتیز نسخه 1.33 به بعد، فقط کاربرانی که مجاز به
ایجاد آبجکت‌های ResourceClaim یا ResourceClaimTemplate در فضاهای نام (namespace) دارای برچسب
`resource.kubernetes.io/admin-access: "true"` (حساس به حروف بزرگ و کوچک) هستند، می‌توانند از فیلد
`adminAccess` استفاده کنند. این امر تضمین می‌کند که کاربران غیرمدیر نتوانند از این
قابلیت سوءاستفاده کنند. از کوبرنتیز نسخه 1.34 به بعد، این برچسب به `resource.kubernetes.io/admin-access: "true"` به‌روزرسانی شده است.

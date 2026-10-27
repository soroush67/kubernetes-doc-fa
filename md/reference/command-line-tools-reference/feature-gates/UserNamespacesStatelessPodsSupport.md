---
title: UserNamespacesStatelessPodsSupport
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.27"

removed: true
---
پشتیبانی از user namespace را برای Podهای بدون حالت (stateless) فعال می‌کند. این feature gate در نسخه ۱.۲۸ کوبرنتیز با feature gate با نام `UserNamespacesSupport` جایگزین شد.

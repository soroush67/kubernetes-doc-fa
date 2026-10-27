---
# Removed from Kubernetes
title: APISelfSubjectReview
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.29"
removed: true
---
API با نام `SelfSubjectReview` را فعال می‌کند که به کاربران اجازه می‌دهد
اطلاعات احراز هویت سوژه درخواست‌دهنده را مشاهده کنند.
برای جزئیات بیشتر، به [دسترسی API به اطلاعات احراز هویت یک کلاینت](/docs/reference/access-authn-authz/authentication/#self-subject-review)
مراجعه کنید.

---
title: StructuredAuthorizationConfiguration
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
پیکربندی ساختاریافته مجوزدهی (authorization) را فعال می‌کند، به‌طوری که مدیران کلاستر
بتوانند بیش از یک [authorization webhook](/docs/reference/access-authn-authz/webhook/)
را در زنجیره پردازشگر (handler chain) سرور API مشخص کنند.

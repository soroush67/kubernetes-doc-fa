---
title: ServerSideFieldValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.24"
  - stage: beta
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.26" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.31"

removed: true
---
اعتبارسنجی فیلدها در سمت سرور را فعال می‌کند. این بدان معناست که اعتبارسنجی
طرح‌واره (schema) منبع در سمت API server انجام می‌شود، نه در سمت کلاینت
(برای مثال، در دستور `kubectl create` یا `kubectl apply`).

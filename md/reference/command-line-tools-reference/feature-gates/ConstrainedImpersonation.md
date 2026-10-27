---
title: ConstrainedImpersonation
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
امکان جعل هویت (impersonation) محدودشده به درخواست‌های مشخص را فراهم می‌کند، به‌جای آن‌که جعل هویت به‌صورت «همه یا هیچ» باشد.

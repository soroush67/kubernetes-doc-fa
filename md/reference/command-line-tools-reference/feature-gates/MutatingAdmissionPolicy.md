---
title: MutatingAdmissionPolicy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.33"
  - stage: beta
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---

پشتیبانی از [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/) را فعال می‌کند؛ این قابلیت امکان می‌دهد
جهش‌های (mutations) مبتنی بر [CEL](/docs/reference/using-api/cel/) در طول کنترل پذیرش (admission control) اعمال شوند.

در کوبرنتیز نسخه‌های v1.30 و v1.31، این feature gate وجود داشت اما هیچ تأثیری نداشت.

---
title: PodHostIPs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"
removed: true

---
فیلد `status.hostIPs` را برای Pod‌ها و {{< glossary_tooltip term_id="downward-api" text="downward API" >}} فعال می‌کند.
این فیلد به شما امکان می‌دهد نشانی‌های IP نود میزبان را در اختیار بارهای کاری قرار دهید.

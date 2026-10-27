---
title: ServiceAccountNodeAudienceRestriction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"  

---
این gate برای محدود کردن audience‌هایی به کار می‌رود که kubelet می‌تواند برای آن‌ها توکن service account درخواست کند.

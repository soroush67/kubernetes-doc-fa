---
title: KubeletServiceAccountTokenForCredentialProviders
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
فعال‌سازی قابلیت ارسال توکن حساب سرویس (service account) متصل به Pod‌ای که ایمیج آن در حال دریافت (pull) است، توسط kubelet به افزونه ارائه‌دهنده اعتبارنامه (credential provider plugin).

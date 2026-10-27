---
title: ExternalServiceAccountTokenSigner
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
با فعال‌سازی و تنظیم `--service-account-signing-endpoint`، کوبرنتیز kube-apiserver را قادر می‌سازد تا برای امضای توکن‌ها و مدیریت کلیدهای تأیید توکن از یک [امضاکننده خارجی (external signer)](/docs/reference/access-authn-authz/service-accounts-admin#external-serviceaccount-token-signing-and-key-management) استفاده کند.

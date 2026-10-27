---
# Removed from Kubernetes
title: ServiceAccountIssuerDiscovery
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.23"

removed: true
---
فعال‌سازی نقاط انتهایی کشف OIDC (نشانی‌های issuer و JWKS) برای issuer مربوط به service account در API server. برای جزئیات بیشتر، به
[پیکربندی Service Accountها برای Podها](/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery)
مراجعه کنید.

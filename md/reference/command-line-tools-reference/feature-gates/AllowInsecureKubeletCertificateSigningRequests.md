---
title: AllowInsecureKubeletCertificateSigningRequests
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.31"
---
اعتبارسنجی admission نود را برای
[CertificateSigningRequests](/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests)
مربوط به امضاکنندگان (signers) kubelet غیرفعال می‌کند. مگر اینکه این feature gate را غیرفعال کنید، کوبرنتیز اعمال می‌کند که گواهی‌های جدید kubelet دارای `commonName` منطبق با `system:node:$nodeName` باشند.

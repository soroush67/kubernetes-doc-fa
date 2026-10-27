---
title: ReloadKubeletServerCertificateFile
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"

---
در صورت تغییر فایل گواهی مشخص‌شده، به سرور TLS در kubelet امکان می‌دهد گواهی خود را به‌روزرسانی کند.

این قابلیت زمانی مفید است که `tlsCertFile` و `tlsPrivateKeyFile` در پیکربندی kubelet مشخص شده باشند.
این feature gate در سایر حالت‌ها، مانند استفاده از TLS bootstrap، تأثیری ندارد.

---
title: CSIServiceAccountTokenSecrets
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
به درایورهای CSI امکان می‌دهد تا با انتخاب خودشان، توکن‌های service account را از kubelet از طریق فیلد اختصاصی secrets در NodePublishVolumeRequest دریافت کنند، به‌جای آنکه این توکن‌ها را از فیلد volume_context دریافت کنند.

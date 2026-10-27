---
title: AllowServiceExternalIPs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.36"

---
در صورت فعال بودن، kube-proxy همچنان به فیلد منسوخ‌شدهٔ `externalIPs`
در Serviceها احترام می‌گذارد و آن را در نظر می‌گیرد.

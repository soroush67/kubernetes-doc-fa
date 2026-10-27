---
title: TokenRequestServiceAccountUIDValidation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.34"

---
این قابلیت برای اطمینان از این استفاده می‌شود که UID ارائه‌شده در TokenRequest با UID مربوط به ServiceAccount که توکن برای آن درخواست شده است مطابقت داشته باشد.
این کار با اطمینان از اینکه توکن‌ها فقط برای ServiceAccount صحیح صادر می‌شوند، از سوءاستفاده از API مربوط به TokenRequest جلوگیری می‌کند.

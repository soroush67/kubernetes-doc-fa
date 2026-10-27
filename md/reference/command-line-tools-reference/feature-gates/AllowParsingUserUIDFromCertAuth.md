---
title: AllowParsingUserUIDFromCertAuth
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
هنگامی که این قابلیت فعال باشد، صفت نام موضوع (subject name) با شناسه `1.3.6.1.4.1.57683.2`
در گواهی X.509 در طول احراز هویت مبتنی بر گواهی، به‌عنوان UID کاربر تجزیه (parse) می‌شود.

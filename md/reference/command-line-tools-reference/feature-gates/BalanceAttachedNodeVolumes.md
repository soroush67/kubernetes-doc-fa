---
# Removed from Kubernetes
title: BalanceAttachedNodeVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.21"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.22"

removed: true
---
تعداد حجم‌ها (volumes) روی نود را نیز در تخصیص متوازن منابع هنگام زمان‌بندی در نظر می‌گیرد. نودی که میزان مصرف CPU و حافظه و همچنین تعداد حجم‌های آن به هم نزدیک‌تر باشد، هنگام تصمیم‌گیری توسط زمان‌بند ترجیح داده می‌شود.

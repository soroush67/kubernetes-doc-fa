---
title: GitRepoVolumeDriver
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.33"

---
این feature gate مشخص می‌کند که افزونه حجم (volume) از نوع `gitRepo` پشتیبانی شود یا خیر.
افزونه حجم `gitRepo` از نسخه v1.33 به‌طور پیش‌فرض غیرفعال است.
این feature gate راهی برای کاربران فراهم می‌کند تا آن را فعال کنند.

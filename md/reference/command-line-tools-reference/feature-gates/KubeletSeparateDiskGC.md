---
title: KubeletSeparateDiskGC
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
---
قابلیت تفکیک فایل‌سیستم ایمیج، kubelet را قادر می‌سازد تا garbage collection مربوط به ایمیج‌ها (لایه‌های فقط‌خواندنی) و/یا کانتینرها (لایه‌های قابل‌نوشتن) را که روی فایل‌سیستم‌های جداگانه مستقر شده‌اند، انجام دهد.

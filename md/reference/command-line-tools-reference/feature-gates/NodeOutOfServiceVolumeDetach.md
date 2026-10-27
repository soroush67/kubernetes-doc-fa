---
title: NodeOutOfServiceVolumeDetach
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.24"
    toVersion: "1.25"
  - stage: beta
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.31"

removed: true
---
هنگامی که یک نود با استفاده از taint با نام `node.kubernetes.io/out-of-service` به‌عنوان خارج از سرویس (out-of-service) علامت‌گذاری شود، Podهای موجود روی آن نود که نتوانند این taint را تحمل کنند، به‌صورت اجباری حذف می‌شوند و عملیات جداسازی حجم (volume detach) برای Podهایی که روی آن نود در حال خاتمه یافتن هستند بلافاصله انجام خواهد شد. Podهای حذف‌شده می‌توانند به‌سرعت روی نودهای دیگر بازیابی شوند.

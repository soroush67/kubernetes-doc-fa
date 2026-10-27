---
title: QOSReserved
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
---
امکان رزرو منابع را در سطح QoS فراهم می‌کند و از افزایش ناگهانی مصرف (bursting) پادها در سطوح پایین‌تر QoS در منابعی که در سطوح بالاتر QoS درخواست شده‌اند جلوگیری می‌کند
(فعلاً فقط برای حافظه).

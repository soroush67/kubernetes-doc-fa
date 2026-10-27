---
title: MutableCSINodeAllocatableCount
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
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
فیلد `.spec.drivers[*].allocatable.count` در آبجکت CSINode را قابل تغییر (mutable) می‌کند.
همچنین فیلدی در CSIDriver با نام `nodeAllocatableUpdatePeriodSeconds` را فعال می‌کند.

این امر امکان به‌روزرسانی دوره‌ای ظرفیت حجم (volume) قابل تخصیصی را که نود گزارش می‌کند فراهم می‌سازد
و از گیر کردن پادهای حالت‌دار (stateful) به‌دلیل اطلاعات منسوخ‌شده جلوگیری می‌کند؛
اطلاعاتی که در غیر این صورت kube-scheduler به آن‌ها تکیه می‌کرد.

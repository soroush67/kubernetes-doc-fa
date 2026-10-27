---
title: JobTrackingWithFinalizers
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.22"
  - stage: beta
    defaultValue: false
    fromVersion: "1.23"  
    toVersion: "1.24" 
  - stage: beta
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.25" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"
    toVersion: "1.28"     

removed: true
---
امکان ردیابی تکمیل‌های [Job](/docs/concepts/workloads/controllers/job) را بدون اتکا به ماندگاری نامحدود Podها در کلاستر فراهم می‌کند.
کنترل‌کننده Job از finalizerهای Pod و یک فیلد در وضعیت Job (Job status) استفاده می‌کند تا Podهای پایان‌یافته‌ای را که باید در شمارش تکمیل Job لحاظ شوند، ردیابی کند.

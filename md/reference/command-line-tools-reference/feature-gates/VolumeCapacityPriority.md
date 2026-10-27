---
title: VolumeCapacityPriority
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.32"

removed: true
---
پشتیبانی از اولویت‌بندی نودها در توپولوژی‌های مختلف را بر اساس ظرفیت PV در دسترس فعال می‌کند.
این قابلیت در نسخه v1.33 به `StorageCapacityScoring` تغییر نام یافته است.

---
title: ServiceNodePortStaticSubrange
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.27"
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.28" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.29" 
    toVersion: "1.30" 

removed: true  
---
استفاده از راهبردهای مختلف تخصیص پورت را برای Serviceهای از نوع NodePort فعال می‌کند. برای جزئیات بیشتر، به [رزرو بازه‌های NodePort برای جلوگیری از تداخل](/docs/concepts/services-networking/service/#avoid-nodeport-collisions) مراجعه کنید.

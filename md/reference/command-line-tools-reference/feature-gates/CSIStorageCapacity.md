---
title: CSIStorageCapacity
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.27"

removed: true  
---
به درایورهای CSI امکان می‌دهد اطلاعات ظرفیت ذخیره‌سازی را منتشر کنند
و به زمان‌بند کوبرنتیز اجازه می‌دهد هنگام زمان‌بندی Podها از این اطلاعات استفاده کند. به
[ظرفیت ذخیره‌سازی](/docs/concepts/storage/storage-capacity/) مراجعه کنید.
برای جزئیات بیشتر، مستندات [نوع حجم (volume) `csi`](/docs/concepts/storage/volumes/#csi) را بررسی کنید.

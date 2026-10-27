---
title: ServiceIPStaticSubrange
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.24"
    toVersion: "1.24"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.25"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"
    toVersion: "1.27"    

removed: true  
---
راهبردی را برای تخصیص ClusterIP به Serviceها فعال می‌کند که در آن محدوده ClusterIP به زیرمحدوده‌ها تقسیم می‌شود. آدرس‌های ClusterIP که به‌صورت پویا تخصیص داده می‌شوند، ترجیحاً از محدوده بالایی تخصیص می‌یابند؛ این کار به کاربران امکان می‌دهد ClusterIPهای ثابت را از محدوده پایینی و با ریسک کم برخورد (collision) تخصیص دهند. برای جزئیات بیشتر به
[پرهیز از برخوردها](/docs/reference/networking/virtual-ips/#avoiding-collisions)
مراجعه کنید.

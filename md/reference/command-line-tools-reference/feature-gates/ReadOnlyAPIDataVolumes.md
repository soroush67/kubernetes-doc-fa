---
# Removed from Kubernetes
title: ReadOnlyAPIDataVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: stable
    fromVersion: "1.10"
    toVersion: "1.10"

removed: true  
---
حجم‌های (volumes) [`configMap`](/docs/concepts/storage/volumes/#configmap)،
[`secret`](/docs/concepts/storage/volumes/#secret)،
[`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi) و
[`projected`](/docs/concepts/storage/volumes/#projected)
را به‌صورت فقط‌خواندنی mount کنید. {{< glossary_tooltip term_id="volume" text="حجم‌ها" >}}

از کوبرنتیز نسخه ۱.۱۰ به بعد، این انواع حجم همواره فقط‌خواندنی هستند و امکان انصراف از این رفتار وجود ندارد.

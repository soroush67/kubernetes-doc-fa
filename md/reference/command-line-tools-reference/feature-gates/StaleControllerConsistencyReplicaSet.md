---
title: StaleControllerConsistencyReplicaSet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true  
    fromVersion: "1.36"
---
رفتاری را در کنترل‌کننده ReplicaSet فعال می‌کند که تضمین می‌کند نوشتن‌های قبلی روی
API server پیش از ادامه‌ی هرگونه تطبیق (reconciliation) بیشتر برای همان ReplicaSet مشاهده شده باشند.
هدف از این کار جلوگیری از آن است که کش قدیمی (stale cache) موجب به‌روزرسانی‌های نادرست یا ناخواسته در ReplicaSet شود.

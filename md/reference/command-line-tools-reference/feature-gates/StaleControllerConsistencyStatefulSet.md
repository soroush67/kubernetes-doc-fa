---
title: StaleControllerConsistencyStatefulSet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
رفتاری را در کنترل‌کننده StatefulSet فعال می‌کند که تضمین می‌کند نوشتن‌های قبلی روی
سرور API پیش از ادامه‌ی مصالحه (reconciliation) بیشتر برای همان StatefulSet مشاهده شده باشند.
هدف از این کار جلوگیری از آن است که کش قدیمی (stale cache) موجب به‌روزرسانی‌های نادرست یا ناخواسته در StatefulSet شود.

---
title: StaleControllerConsistencyDaemonSet
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
رفتاری را در کنترل‌کننده DaemonSet فعال می‌کند تا اطمینان حاصل شود که نوشتن‌های قبلی در API server پیش از ادامه‌ی تطبیق (reconciliation) بیشتر برای همان DaemonSet مشاهده شده‌اند.
هدف از این کار جلوگیری از آن است که کش قدیمی (stale cache) باعث به‌روزرسانی‌های نادرست یا ناخواسته در DaemonSet شود.

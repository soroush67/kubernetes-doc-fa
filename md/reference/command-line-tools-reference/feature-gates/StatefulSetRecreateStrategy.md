---
title: StatefulSetRecreateStrategy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
راهبرد به‌روزرسانی `Recreate` را برای StatefulSetها فعال می‌کند؛ این راهبرد پیش از ایجاد Podهای جدیدی که تغییرات اعمال‌شده در `.spec.template` مربوط به StatefulSet را منعکس می‌کنند، تمام Podهای آن StatefulSet را حذف می‌کند. برای جزئیات بیشتر به
[Recreate](/docs/concepts/workloads/controllers/statefulset/#recreate) مراجعه کنید.

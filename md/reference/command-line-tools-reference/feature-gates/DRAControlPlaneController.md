---
title: DRAControlPlaneController
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.31"

removed: true
---
پشتیبانی از منابعی را فعال می‌کند که پارامترهای سفارشی دارند و چرخه‌حیات آن‌ها مستقل از Pod است. تخصیص این منابع بر عهده‌ی کنترل‌کننده‌ی control plane مربوط به resource driver است.

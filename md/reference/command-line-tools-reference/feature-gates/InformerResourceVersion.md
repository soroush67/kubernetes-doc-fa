---
title: InformerResourceVersion
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.34"
  - stage: stable 
    defaultValue: true
    fromVersion: "1.35"
---
به کلاینت‌ها اجازه می‌دهد از فراخوانی `LastSyncResourceVersion()` روی informerها استفاده کنند و بر این اساس بتوانند اقدامات خود را بر پایه نسخه فعلی منبع (resource version) انجام دهند. زمانی که این قابلیت غیرفعال باشد، فراخوانی `LastSyncResourceVersion()` با موفقیت انجام می‌شود، اما یک رشته خالی برمی‌گرداند. این قابلیت توسط kube-controller-manager برای StorageVersionMigration استفاده می‌شود.

---
# Removed from Kubernetes
title: ResourceLimitsPriorityFunction
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.18"
  - stage: deprecated
    fromVersion: "1.19"
    toVersion: "1.19"

removed: true
---
یک تابع اولویت‌بندی (priority function) در زمان‌بند را فعال می‌کند که به نودی که دست‌کم یکی از محدودیت‌های cpu و حافظه‌ی Pod ورودی را برآورده کند، کمترین امتیاز ممکن، یعنی ۱، را اختصاص می‌دهد. هدف از این کار، شکستن تساوی میان نودهایی است که امتیاز یکسان دارند.

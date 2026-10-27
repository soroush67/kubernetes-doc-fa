---
title: HugepageAwareEviction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
ظرفیت hugepage را از `memory.available` کم می‌کند تا سیگنال اخراج (eviction) در kubelet، میزان واقعی حافظه‌ی معمولی در دسترس را منعکس کند. بدون این feature gate، رزروهای hugepage مقدار `AvailableBytes` را بیش از واقعیت نشان می‌دهند؛ این امر اخراج را به تأخیر می‌اندازد و در نودهایی که hugepage روی آن‌ها پیکربندی شده است، به OOM kill منجر می‌شود.

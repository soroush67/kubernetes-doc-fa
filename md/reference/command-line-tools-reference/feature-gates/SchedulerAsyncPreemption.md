---
title: SchedulerAsyncPreemption
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
---

اجرای برخی عملیات پرهزینه مرتبط با
[پیش‌دستی (preemption)](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
را درون زمان‌بند به‌صورت ناهمگام فعال می‌کند.
پردازش ناهمگام پیش‌دستی، تأخیر کلی زمان‌بندی Podها را بهبود می‌بخشد.

---
title: SchedulerAsyncAPICalls
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---

kube-scheduler را طوری تغییر می‌دهد که کل چرخه زمان‌بندی از درخواست‌های مسدودکننده به API server کوبرنتیز عاری باشد.
در عوض، تعامل با API کوبرنتیز با استفاده از کد ناهمگام (asynchronous) انجام می‌شود.

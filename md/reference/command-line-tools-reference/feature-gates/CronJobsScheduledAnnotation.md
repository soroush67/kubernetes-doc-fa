---
title: CronJobsScheduledAnnotation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"

---
زمان زمان‌بندی‌شدهٔ Job را به‌صورت یک
{{< glossary_tooltip text="حاشیه‌نویسی (annotation)" term_id="annotation" >}}
روی Jobهایی که از طرف یک CronJob ایجاد شده‌اند تنظیم می‌کند.

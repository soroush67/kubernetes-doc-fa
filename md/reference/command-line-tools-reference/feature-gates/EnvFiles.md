---
title: EnvFiles
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
پشتیبانی از تعریف مقادیر متغیرهای محیطی کانتینر از طریق فایل.
برای جزئیات بیشتر، [تعریف مقادیر متغیرهای محیطی با استفاده از یک init container](/docs/tasks/inject-data-application/define-environment-variable-via-file) را ببینید.

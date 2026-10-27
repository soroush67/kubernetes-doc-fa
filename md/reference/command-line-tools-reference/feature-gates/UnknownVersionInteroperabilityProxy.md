---
title: UnknownVersionInteroperabilityProxy
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
درخواست‌های مربوط به منابع را در شرایطی که چندین kube-apiserver با نسخه‌های متفاوت وجود دارند، به kube-apiserver همتای صحیح هدایت (proxy) می‌کند.
برای اطلاعات بیشتر به [پروکسی نسخه‌های ترکیبی](/docs/concepts/architecture/mixed-version-proxy/) مراجعه کنید.

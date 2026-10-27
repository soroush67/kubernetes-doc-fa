---
title: ComponentFlagz
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
endpoint مربوط به flagz در کامپوننت را فعال می‌کند.
برای اطلاعات بیشتر به [zpages](/docs/reference/instrumentation/zpages/) مراجعه کنید.

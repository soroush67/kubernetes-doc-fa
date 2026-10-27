---
title: ImageVolumeWithDigest
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
---
برای هر [حجم `image`](/docs/concepts/storage/volumes#image) در یک Pod،
digest ایمیج به‌عنوان بخشی از وضعیت (status) پاد ثبت می‌شود.

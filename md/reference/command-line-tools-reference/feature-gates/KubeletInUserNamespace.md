---
title: KubeletInUserNamespace
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
پشتیبانی از اجرای kubelet در یک
{{<glossary_tooltip text="فضای نام کاربر (user namespace)" term_id="userns">}}
را فعال می‌کند.
به [اجرای مؤلفه‌های نود کوبرنتیز به‌عنوان کاربر غیر root](/docs/tasks/administer-cluster/kubelet-in-userns/) مراجعه کنید.

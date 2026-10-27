---
title: KubeletEnsureSecretPulledImages
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
اطمینان حاصل می‌کند که Podهایی که یک ایمیج را درخواست می‌کنند، در صورتی که آن ایمیج از قبل روی نود وجود داشته باشد، با استفاده از اعتبارنامه‌های ارائه‌شده مجاز به دسترسی به آن ایمیج هستند.
به [اطمینان از تأیید اعتبارنامه‌های دریافت ایمیج](/docs/concepts/containers/images#ensureimagepullcredentialverification) مراجعه کنید.

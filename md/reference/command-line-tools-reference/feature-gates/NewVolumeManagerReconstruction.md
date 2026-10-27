---
title: NewVolumeManagerReconstruction
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"

removed: true
---
کشف بهبودیافته‌ی حجم‌های (volume) مانت‌شده را هنگام راه‌اندازی kubelet فعال می‌کند. از آنجا که کد مرتبط به‌طور قابل‌توجهی بازآرایی شده بود، نسخه‌های 1.25 تا 1.29 کوبرنتیز به شما امکان می‌دادند در صورتی که kubelet هنگام راه‌اندازی دچار گیر کردن می‌شد یا حجم‌های Podهای خاتمه‌یافته را unmount نمی‌کرد، این قابلیت را غیرفعال کنید.

این بازآرایی در نسخه‌های 1.25 و 1.26 کوبرنتیز پشت feature gate با نام `SELinuxMountReadWriteOncePod` قرار داشت.

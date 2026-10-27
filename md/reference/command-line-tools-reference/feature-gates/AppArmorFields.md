---
title: AppArmorFields
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
تنظیمات security context مرتبط با AppArmor را فعال می‌کند.

برای اطلاعات بیشتر درباره AppArmor و کوبرنتیز، بخش
[AppArmor](/docs/concepts/security/linux-kernel-security-constraints/#apparmor)
را در
[ویژگی‌های امنیتی در هسته لینوکس](/docs/concepts/security/linux-kernel-security-constraints/#linux-security-features)
مطالعه کنید.

---
title: VolumeBindMountOptions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
امکان تنظیم گزینه‌های bind mount (شامل `noexec`، `nodev` و `nosuid`) را برای هر نقطه اتصال حجم (volume mount) در کانتینر، از طریق فیلد `bindMountOptions` در `volumeMounts` فراهم می‌کند. در صورت فعال بودن، kubelet این گزینه‌ها را به container runtime ارسال می‌کند و container runtime آن‌ها را به‌صورت پرچم‌های bind mount لینوکس اعمال می‌کند. container runtime باید از فیلد `mount_options` در پیام `Mount` در CRI پشتیبانی کند. این فیلد بر نودهای ویندوز تأثیری ندارد.

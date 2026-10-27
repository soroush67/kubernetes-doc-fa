---
title: SELinuxMount
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    fromVersion: "1.37"

---
سرعت راه‌اندازی کانتینر را افزایش می‌دهد؛ به این صورت که به kubelet اجازه می‌دهد حجم‌های (volumes) یک Pod را مستقیماً با برچسب صحیح SELinux مونت کند، به‌جای آنکه برچسب تک‌تک فایل‌های موجود در حجم‌ها را به‌صورت بازگشتی تغییر دهد.
این قابلیت بهبودهای عملکردی‌ای را که فیچر گیت `SELinuxMountReadWriteOncePod` فراهم می‌کند، با گسترش پیاده‌سازی به همهٔ حجم‌ها توسعه می‌دهد.

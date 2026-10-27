---
title: ExecProbeTimeout
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"  
---
اطمینان حاصل می‌کند که kubelet محدودیت‌های زمانی (timeout) پروب‌های exec را رعایت کند.
این feature gate برای حالتی وجود دارد که بارهای کاری موجود شما به خطایی وابسته باشند که اکنون برطرف شده است و در آن کوبرنتیز timeout پروب‌های exec را نادیده می‌گرفت. به
[پروب‌های آمادگی (readiness probes)](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes)
مراجعه کنید.

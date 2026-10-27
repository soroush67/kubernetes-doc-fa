---
title: ChangeContainerStatusOnKubeletRestart
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.35"
---
فعال‌سازی نوشتن‌های قدیمی (legacy) برای به‌روزرسانی وضعیت `ready` کانتینر پس از آنکه kubelet یک
[راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#kubelet-restarts) را تشخیص می‌دهد.

این feature gate برای آن معرفی شد که بتوانید رفتار را به پیش‌فرضی که پیش‌تر استفاده می‌شد بازگردانید.
اگر از رفتار پیش‌فرض رضایت دارید، نیازی به فعال‌سازی این
feature gate ندارید.

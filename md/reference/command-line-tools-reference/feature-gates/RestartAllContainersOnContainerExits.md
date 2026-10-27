---
title: RestartAllContainersOnContainerExits
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.35"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
امکان تعیین `RestartAllContainers` به‌عنوان یک اقدام (action) در `restartPolicyRules` کانتینر را فعال می‌کند. هنگامی که خروج یک کانتینر با قاعده‌ای دارای این اقدام مطابقت پیدا کند، کل Pod خاتمه می‌یابد و به‌صورت درجا (in-place) دوباره راه‌اندازی می‌شود.

`RestartAllContainersOnContainerExits` به هر دو feature gate با نام‌های `ContainerRestartRules` و `NodeDeclaredFeatures` وابسته است. اگر feature gateهای وابسته فعال نباشند، ممکن است راه‌اندازی kubelet با شکست مواجه شود.

برای جزئیات بیشتر، [راه‌اندازی مجدد همه کانتینرها](/docs/concepts/workloads/pods/pod-lifecycle/#restart-all-containers) را ببینید.

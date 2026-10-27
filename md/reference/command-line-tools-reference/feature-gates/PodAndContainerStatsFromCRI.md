---
title: PodAndContainerStatsFromCRI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.36"
  - stage: beta
    defaultValue: false
    fromVersion: "1.37"
---
kubelet را به گونه‌ای پیکربندی می‌کند که آمار کانتینرها و Podها را به‌جای cAdvisor، از container runtime مبتنی بر CRI جمع‌آوری کند.
از نسخه 1.26 به بعد، این قابلیت شامل جمع‌آوری متریک‌ها از CRI و انتشار آن‌ها از طریق `/metrics/cadvisor` نیز می‌شود (به‌جای آنکه cAdvisor آن‌ها را مستقیماً منتشر کند).

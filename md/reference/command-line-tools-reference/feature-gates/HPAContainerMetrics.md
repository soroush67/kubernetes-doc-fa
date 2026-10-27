---
title: HPAContainerMetrics
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.20"
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
به {{< glossary_tooltip text="HorizontalPodAutoscalerها" term_id="horizontal-pod-autoscaler" >}}
اجازه می‌دهد بر اساس متریک‌های هر یک از کانتینرهای موجود در Podهای هدف، مقیاس‌دهی را انجام دهند.

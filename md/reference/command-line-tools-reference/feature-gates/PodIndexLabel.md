---
title: PodIndexLabel
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
به کنترل‌کننده Job و کنترل‌کننده StatefulSet امکان می‌دهد هنگام ایجاد Podهای جدید، شاخص (index) Pod را به‌صورت یک برچسب اضافه کنند. برای جزئیات بیشتر، [مستندات حالت تکمیل Job](/docs/concepts/workloads/controllers/job#completion-mode) و [مستندات برچسب شاخص Pod در StatefulSet](/docs/concepts/workloads/controllers/statefulset/#pod-index-label) را ببینید.

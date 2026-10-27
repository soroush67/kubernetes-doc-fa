---
title: ComponentSLIs
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.26"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.32"
    toVersion: "1.34"

removed: true
---
فعال‌سازی endpoint با مسیر `/metrics/slis` در اجزای کوبرنتیز مانند
kubelet، kube-scheduler، kube-proxy، kube-controller-manager و cloud-controller-manager
که به شما امکان می‌دهد متریک‌های بررسی سلامت (health check) را جمع‌آوری (scrape) کنید.

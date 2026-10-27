---
title: ConsistentHTTPGetHandlers
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.30"

removed: true
---
یکسان‌سازی نحوهٔ ارسال URL و هدرهای درخواست HTTP GET برای 
handlerهای چرخهٔ حیات (lifecycle) به همراه probeها.

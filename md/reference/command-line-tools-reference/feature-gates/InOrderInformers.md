---
title: InOrderInformers
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
---
اینفورمرها (informers) را وادار می‌کند رویدادهای جریان watch را به‌ترتیب تحویل دهند، نه به‌صورت نامرتب.

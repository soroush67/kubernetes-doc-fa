---
# Removed from Kubernetes
title: EphemeralContainers
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.16"
    toVersion: "1.22"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"    

removed: true  
---
امکان افزودن
{{< glossary_tooltip text="کانتینرهای زودگذر" term_id="ephemeral-container" >}}
به Podهای در حال اجرا را فعال می‌کند.

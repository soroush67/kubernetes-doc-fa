---
title: RemoteRequestHeaderUID
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
---
امکان پذیرش UIDها (شناسه‌های کاربر) از طریق احراز هویت مبتنی بر هدر درخواست را برای API server فعال می‌کند.
این قابلیت همچنین باعث می‌شود API aggregator در `kube-apiserver` هنگام هدایت درخواست‌ها به سرورهایی که API تجمیع‌شده (aggregated API) را ارائه می‌دهند، UIDها را از طریق هدرهای استاندارد اضافه کند.

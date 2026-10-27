---
title: EtcdRangeStream
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"

---
این قابلیت به kube-apiserver امکان می‌دهد از فراخوان RPC با نام `RangeStream` در etcd استفاده کند تا پاسخ‌های بزرگ درخواست‌های list را به‌صورت جریانی (stream) از etcd دریافت کند، به‌جای آنکه آن‌ها را در یک پاسخ واحد `Range` واکشی کند. این کار هنگام پاسخ‌گویی به درخواست‌های بزرگ `LIST`، جهش‌های مصرف حافظه را هم در etcd و هم در kube-apiserver کاهش می‌دهد.

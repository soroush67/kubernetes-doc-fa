---
title: GRPCContainerProbeTLS
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
پشتیبانی از TLS را برای پروب‌های gRPC کانتینر فعال می‌کند. در صورت فعال بودن،
می‌توانید فیلد `mode` را به فیلد `grpc` در پروب‌های gRPC اضافه کنید. تنظیم
`mode: TLS` در یک پروب liveness، readiness یا startup باعث می‌شود kubelet
از طریق TLS (با `InsecureSkipVerify`) متصل شود.
به [پیکربندی پروب‌های Liveness، Readiness و Startup](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#grpc-probe-tls) مراجعه کنید.

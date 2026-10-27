---
title: H2CContainerProbe
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
پشتیبانی از HTTP/2 cleartext (h2c) را برای probeهای HTTP کانتینر فعال می‌کند. در صورت فعال بودن،
می‌توانید فیلد `protocol` را به فیلد `httpGet` در probeهای HTTP اضافه کنید. تنظیم
`protocol: HTTP2` در یک liveness probe، readiness probe یا startup probe باعث می‌شود `kubelet`
به‌جای HTTP/1.1، probe را از طریق h2c انجام دهد.
به [پیکربندی probeهای Liveness، Readiness و Startup](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#use-h2c-with-http-probes) مراجعه کنید.

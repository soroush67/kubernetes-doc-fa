---
title: SystemdWatchdog
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.32"
---
امکان استفاده از watchdog سیستم‌دی (systemd) را برای پایش وضعیت سلامت kubelet فراهم می‌کند.
برای جزئیات بیشتر به [Watchdog سیستم‌دی در kubelet](/docs/reference/node/systemd-watchdog/) مراجعه کنید.

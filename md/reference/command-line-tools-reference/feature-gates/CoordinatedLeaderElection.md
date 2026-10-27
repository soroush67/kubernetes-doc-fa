---
title: CoordinatedLeaderElection
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
---
رفتارهای پشتیبانی‌کننده از API مربوط به LeaseCandidate را فعال می‌کند و همچنین انتخاب رهبر هماهنگ‌شده (coordinated leader election) را برای control plane کوبرنتیز به‌صورت قطعی (deterministic) فعال می‌سازد.

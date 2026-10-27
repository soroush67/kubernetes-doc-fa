---
title: ControllerManagerReleaseLeaderElectionLockOnExit
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
باعث می‌شود `kube-controller-manager` هنگام جابه‌جایی رهبر (leader)، قفل انتخابات رهبر (leader election lock) خود را به‌طور فعال آزاد کند، به‌جای اینکه منتظر بماند تا TTL آن قفل منقضی شود.
این کار امکان می‌دهد رهبر جدید سریع‌تر انتخاب شود.

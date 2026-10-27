---
# Removed from Kubernetes
title: ControllerManagerLeaderMigration
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.26"

removed: true  
---
مهاجرت رهبر (Leader Migration) را برای
[kube-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#initial-leader-migration-configuration) و
[cloud-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#deploy-cloud-controller-manager)
فعال می‌کند؛ قابلیتی که به اپراتور کلاستر اجازه می‌دهد کنترل‌کننده‌ها را بدون توقف سرویس و به‌صورت زنده (live) از kube-controller-manager به یک controller-manager خارجی
(برای مثال cloud-controller-manager) در یک کلاستر با دسترس‌پذیری بالا (HA) منتقل کند.

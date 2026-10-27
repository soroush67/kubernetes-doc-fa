---
title: DefaultHostNetworkHostPortsInPodTemplates
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"

removed: true
---
این feature gate مشخص می‌کند که مقدار پیش‌فرض فیلد
`.spec.containers[*].ports[*].hostPort`
در چه مرحله‌ای برای Podهایی که از `hostNetwork: true` استفاده می‌کنند تعیین شود. از نسخه v1.28 کوبرنتیز به بعد، رفتار پیش‌فرض این است که مقدار پیش‌فرض فقط در خود Podها تنظیم شود.

فعال‌سازی این گیت به این معناست که مقدار پیش‌فرض حتی برای `.spec` یک
[PodTemplate](/docs/concepts/workloads/pods/#pod-templates) تعبیه‌شده (برای مثال در یک Deployment) نیز تعیین می‌شود؛
این همان روشی است که نسخه‌های قدیمی‌تر کوبرنتیز بر اساس آن کار می‌کردند.
شما باید کد خود را به‌گونه‌ای مهاجرت دهید که به این رفتار قدیمی وابسته نباشد.

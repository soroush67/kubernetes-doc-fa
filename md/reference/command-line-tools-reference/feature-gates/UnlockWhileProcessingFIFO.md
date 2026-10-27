---
title: UnlockWhileProcessingFIFO
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---

استفاده از یک صف FIFO در client-go را فعال می‌کند که هنگام پردازش رویدادها قفل را آزاد می‌کند. اگر این قابلیت فعال نباشد،
صف در تمام مدت پردازش رویدادها قفل را نگه می‌دارد، که ممکن است در سناریوهای با توان عملیاتی بالا
به مشکلات عملکردی منجر شود. این feature gate را می‌توان در
kube-controller-manager و هر کنترل‌کننده مبتنی بر client-go فعال یا غیرفعال کرد.

فعال‌سازی این feature gate تنها در صورتی امکان‌پذیر است که feature gate
[AtomicFIFO](/docs/reference/command-line-tools-reference/feature-gates/#AtomicFIFO) نیز فعال باشد.

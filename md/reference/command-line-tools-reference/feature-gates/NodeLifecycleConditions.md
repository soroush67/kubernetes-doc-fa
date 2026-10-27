---
title: NodeLifecycleConditions
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
شرط‌های (condition) شناخته‌شده‌ی Node را فعال می‌کند که وضعیت چرخه‌ی حیات مربوط به تخلیه (drain)، نگهداری (maintenance) و
[خاموش‌شدن مرحله‌ای نود (Graceful Node Shutdown)](/docs/concepts/cluster-administration/node-shutdown/)
را گزارش می‌کنند. برای اطلاعات بیشتر به
[شرط‌های چرخه‌ی حیات نود](/docs/reference/node/node-lifecycle-conditions/)
مراجعه کنید.

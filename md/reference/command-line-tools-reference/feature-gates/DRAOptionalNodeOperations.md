---
title: DRAOptionalNodeOperations
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
پشتیبانی از عملیات اختیاری محلی نود را در تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) فعال می‌کند. این قابلیت به درایورها اجازه می‌دهد اعلام کنند که عملیات مشخصی از نود (`NodePrepareResources` و/یا `NodeUnprepareResources`) برای دستگاه‌هایشان قابل صرف‌نظر کردن است؛ در نتیجه `kubelet` می‌تواند فراخوانی‌های غیرضروری gRPC را نادیده بگیرد.

برای اطلاعات بیشتر، به
[عملیات اختیاری نود](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#optional-node-operations)
در مستندات تخصیص پویای منابع (Dynamic Resource Allocation) مراجعه کنید.

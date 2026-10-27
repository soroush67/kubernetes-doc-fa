---
title: DRADerivedAttributes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
قابلیت `derivedAttributes` را در تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) فعال می‌کند. این قابلیت به نویسندگان ResourceClaim و ResourceClaimTemplate اجازه می‌دهد با استفاده از عبارت‌های CEL مخصوص هر دستگاه، ویژگی‌های مجازی دستگاه را محاسبه کنند تا در محدودیت‌های `matchAttribute` و `distinctAttribute` به کار روند.

برای اطلاعات بیشتر، بخش
[ویژگی‌های مشتق‌شده (Derived attributes)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#derived-attributes)
را در مستندات آبجکت‌های API مربوط به DRA ببینید.

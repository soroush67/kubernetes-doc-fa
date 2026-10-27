---
title: DRAListTypeAttributes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
فیلدهای ویژگی (attribute) از نوع لیست (`bools`، `ints`، `strings`، `versions`) را برای دستگاه‌ها
در `ResourceSlice` فعال می‌کند و به یک دستگاه اجازه می‌دهد برای یک ویژگی واحد چندین مقدار را اعلام کند.

هنگامی که این قابلیت فعال باشد، `matchAttribute` از معناشناسی اشتراک مجموعه‌ها (set-intersection) استفاده می‌کند
(مجموعه‌های مقادیر ویژگی در میان تمام دستگاه‌های انتخاب‌شده باید اشتراکی غیرتهی داشته باشند)، و
`distinctAttribute` از معناشناسی مجزای دوبه‌دو (pairwise-disjoint) استفاده می‌کند (مجموعه‌ها نباید هیچ مقدار مشترکی داشته باشند).
ویژگی‌های اسکالر با نسخه‌های قبلی سازگار باقی می‌مانند و به‌عنوان مجموعه‌های تک‌عضوی در نظر گرفته می‌شوند.

همچنین تابع کمکی `includes()` را به عبارت‌های انتخابگر دستگاه (device selector) در CEL اضافه می‌کند که
هم روی ویژگی‌های اسکالر و هم روی ویژگی‌های از نوع لیست کار می‌کند.

برای اطلاعات بیشتر، بخش
[List type attributes](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#list-type-attributes)
را در مستندات تخصیص پویای منابع (Dynamic Resource Allocation) ببینید.

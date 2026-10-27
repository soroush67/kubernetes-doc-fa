---
title: ResourceHealthStatus
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
فیلد `allocatedResourcesStatus` را در بخش `.status` یک Pod فعال می‌کند. این فیلد
جزئیات بیشتری را برای هر کانتینر در Pod گزارش می‌دهد
و شامل اطلاعات سلامت هر دستگاهی است که به Pod اختصاص داده شده است.

از نسخه v1.36 (بتا)، گزارش سلامت شامل یک فیلد اختیاری `message` است که
زمینه‌ی توضیحی بیشتری را به شکل متنی قابل‌خواندن برای انسان درباره‌ی وضعیت سلامت ارائه می‌دهد، مانند جزئیات خطا
یا دلایل شکست.

این قابلیت برای دستگاه‌هایی که هم توسط [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) و هم توسط [Dynamic Resource Allocation](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-health-monitoring) مدیریت می‌شوند اعمال می‌شود. برای جزئیات بیشتر، [Device plugin and unhealthy devices](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-and-unhealthy-devices) را ببینید.

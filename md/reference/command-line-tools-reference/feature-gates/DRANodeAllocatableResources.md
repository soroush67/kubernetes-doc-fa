---
title: DRANodeAllocatableResources
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
---
این قابلیت به `kube-scheduler` امکان می‌دهد منابع قابل تخصیص نود (Node Allocatable) مانند
CPU، حافظه و hugepages را که توسط تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) مدیریت می‌شوند، در حسابداری استاندارد منابع نود خود لحاظ کند.

هنگامی که این قابلیت فعال باشد، درایورهای DRA می‌توانند با استفاده از فیلد `nodeAllocatableResources` در دستگاه‌های `ResourceSlice` مشخص کنند که دستگاه‌هایشان چگونه منابع قابل تخصیص نود را مصرف می‌کنند. این فیلد از دو حالت کاربرد مختلف پشتیبانی می‌کند:
- `mapping`: برای درایورهایی که مستقیماً یک منبع بومی نود را فراهم می‌کنند (برای مثال درایور DRA مربوط به CPU یا حافظه). این حالت از مقیاس‌دهی ظرفیت‌ها یا تعداد دستگاه‌ها پشتیبانی می‌کند.
- `overhead`: برای دستگاه‌هایی که به وابستگی‌های کمکی روی نود نیاز دارند (برای مثال شتاب‌دهنده‌ای که حافظه میزبان را مصرف می‌کند). این حالت از هزینه‌های به‌ازای هر Pod یا به‌ازای هر کانتینر پشتیبانی می‌کند.

این امر به زمان‌بند اجازه می‌دهد این تخصیص‌های DRA را با درخواست‌های استاندارد Pod ترکیب کند تا از تخصیص بیش‌ازحد منابع نود در زمان پذیرش (admission) Pod جلوگیری شود.

همچنین فیلد `status.nodeAllocatableResourceClaimStatuses` را در API مربوط به Pod ارائه می‌کند تا تخصیص‌های منابعِ حاصل را ردیابی کند. `kubelet` از این فیلد برای به‌روزرسانی تنظیمات cgroup مربوط به Pod و کانتینر و همچنین تنظیم امتیازهای OOM استفاده می‌کند.

برای اطلاعات بیشتر، به
[منابع قابل تخصیص نود](/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/#node-allocatable-resources)
در مستندات تخصیص پویای منابع (Dynamic Resource Allocation) مراجعه کنید.

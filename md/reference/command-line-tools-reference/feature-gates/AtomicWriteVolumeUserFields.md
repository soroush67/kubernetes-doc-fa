---
title: AtomicWriteVolumeUserFields
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
این feature gate در kube-apiserver و kubelet کوبرنتیز وجود دارد.

زمانی که این قابلیت در kube-apiserver استفاده شود، به کاربران امکان می‌دهد فیلدهای `user` و `defaultUser` را
در حجم‌های (volume) از نوع `configMap`، `secret`، `downwardAPI` و `projected` تنظیم کنند.

در kubelet، اگر فیلدهای `user` یا `defaultUser` برای یک حجم (volume) مشخص شده باشند،
kubelet هنگام ایجاد فایل‌ها، UID مالک فایل‌های داده‌ی آن حجم را تنظیم می‌کند.

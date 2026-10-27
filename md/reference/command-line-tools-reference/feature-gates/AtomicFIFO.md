---
title: AtomicFIFO
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"

---
پیاده‌سازی‌ای در client-go از یک صف FIFO که با استفاده از عملیات اتمیک تضمین می‌کند رویدادهایی که به‌صورت دسته‌ای می‌رسند، مانند رویدادهای حاصل از یک فراخوانی ListAndWatch، در قالب یک بخش واحد پردازش شوند. این رویکرد در مقابل پیاده‌سازی پیشین است که این رویدادها را یکی‌یکی پردازش می‌کرد و ممکن بود موجب شود حافظه نهان (cache) داخلی به‌طور موقت با سرور API ناسازگار شود. این feature gate را می‌توان در kube-controller-manager و در هر کنترل‌کننده مبتنی بر client-go فعال یا غیرفعال کرد.

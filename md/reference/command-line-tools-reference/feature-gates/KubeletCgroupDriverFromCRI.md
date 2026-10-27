---
title: KubeletCgroupDriverFromCRI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"
---
فعال‌سازی تشخیص گزینه پیکربندی cgroup driver مربوط به kubelet
از طریق {{<glossary_tooltip term_id="cri" text="CRI">}}.
این feature gate اکنون برای همه کلاسترها فعال است. با این حال، فقط روی نودهایی کار می‌کند
که دارای یک container runtime مبتنی بر CRI باشند که از فراخوانی
CRI با نام `RuntimeConfig` پشتیبانی می‌کند. اگر CRI از این قابلیت پشتیبانی کند، kubelet
تنظیم پیکربندی `cgroupDriver` (یا آرگومان خط فرمان منسوخ‌شده `--cgroup-driver`) را نادیده می‌گیرد.
اگر container runtime از آن پشتیبانی نکند، kubelet به استفاده از درایوری بازمی‌گردد که با
تنظیم پیکربندی `cgroupDriver` مشخص شده است.
kubelet در کوبرنتیز 1.36 دیگر به این پیکربندی بازنخواهد گشت.
بنابراین، کاربران باید تا آن زمان container runtime مبتنی بر CRI خود را به نسخه‌ای ارتقا دهند که از
فراخوانی CRI با نام `RuntimeConfig` پشتیبانی می‌کند. مدیران می‌توانند با استفاده از متریک
`kubelet_cri_losing_support` بررسی کنند که آیا نودی در کلاستر آن‌ها وجود دارد که
در نسخه 1.36 پشتیبانی را از دست بدهد. نسخه‌های CRI زیر از این فراخوانی CRI پشتیبانی می‌کنند:

* containerd: پشتیبانی در نسخه v2.0.0 اضافه شد
* CRI-O: پشتیبانی در نسخه v1.28.0 اضافه شد

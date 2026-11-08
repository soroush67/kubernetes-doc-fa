---
content_type: "reference"
title: دیده‌بان systemd برای Kubelet
weight: 80
math: true # for a division by 2
---

{{< feature-state feature_gate_name="SystemdWatchdog" >}}

کوبرنتیز {{< skew currentVersion >}} در نودهای لینوکسی از یکپارچه‌سازی با [systemd](https://systemd.io/) پشتیبانی می‌کند تا ناظر سیستم‌عامل بتواند kubelet ازکارافتاده را بازیابی کند. این یکپارچه‌سازی به‌طور پیش‌فرض فعال نیست. می‌توان از آن به‌جای ارسال درخواست‌های دوره‌ای به نقطهٔ پایانی `/healthz` در kubelet برای بررسی سلامت استفاده کرد. اگر kubelet در مهلت زمانی تعیین‌شده به دیده‌بان (watchdog) پاسخ ندهد، دیده‌بان آن را از بین می‌برد.

سازوکار دیده‌بان systemd به این صورت است که سرویس باید به‌طور دوره‌ای سیگنال _زنده‌بودن_ (keep-alive) را برای فرایند systemd بفرستد. اگر این سیگنال در مهلت زمانی مشخص‌شده دریافت نشود، سرویس بدون پاسخ تلقی و خاتمه داده می‌شود. پس از آن می‌توان سرویس را طبق پیکربندی دوباره راه‌اندازی کرد.

## پیکربندی

برای استفاده از دیده‌بان systemd باید پارامتر `WatchdogSec` را در بخش `[Service]` از فایل یونیت سرویس kubelet پیکربندی کنید:
```
[Service]
WatchdogSec=30s
```

با تنظیم `WatchdogSec=30s`، مهلت زمانی دیده‌بان سرویس ۳۰ ثانیه تعیین می‌شود. در kubelet، تابع `sd_notify()` در بازه‌های \\( WatchdogSec \div 2\\) فراخوانی می‌شود تا `WATCHDOG=1` (پیام زنده‌بودن) را بفرستد. اگر این پیام در مهلت زمانی به دیده‌بان نرسد، kubelet از بین می‌رود. با تنظیم `Restart` روی "always"، "on-failure"، "on-watchdog" یا "on-abnormal"، سرویس به‌طور خودکار دوباره راه‌اندازی خواهد شد.

چند نکته دربارهٔ پیکربندی systemd:

1. اگر مقدار `WatchdogSec` را در systemd برابر 0 قرار دهید یا آن را تنظیم نکنید، دیده‌بان systemd برای این یونیت فعال نمی‌شود.
2. کمینهٔ دورهٔ دیده‌بانی که kubelet پشتیبانی می‌کند ۱٫۰ ثانیه است؛ این محدودیت از ازبین‌رفتن غیرمنتظرهٔ kubelet جلوگیری می‌کند. می‌توانید مقدار `WatchdogSec` را در تعریف یونیت systemd کمتر از ۱ ثانیه تنظیم کنید، اما کوبرنتیز از بازه‌های کوتاه‌تر از این مقدار پشتیبانی نمی‌کند. لازم نیست مهلت زمانی عددی صحیح بر حسب ثانیه باشد.
3. پروژهٔ کوبرنتیز پیشنهاد می‌کند `WatchdogSec` روی دوره‌ای در حدود ۱۵ ثانیه تنظیم شود. دوره‌های طولانی‌تر از ۱۰ دقیقه پشتیبانی می‌شوند، اما صراحتاً توصیه **نمی‌شوند**.

### نمونهٔ پیکربندی
```systemd
[Unit]
Description=kubelet: The Kubernetes Node Agent
Documentation=https://kubernetes.io/docs/home/
Wants=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/bin/kubelet
# Configures the watchdog timeout
WatchdogSec=30s
Restart=on-failure
StartLimitInterval=0
RestartSec=10

[Install]
WantedBy=multi-user.target
```
## {{% heading "whatsnext" %}}
برای آگاهی از جزئیات بیشتر دربارهٔ پیکربندی systemd، به [مستندات systemd](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#WatchdogSec=) مراجعه کنید.

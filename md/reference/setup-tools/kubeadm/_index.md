---
title: "Kubeadm"
weight: 10
no_list: true
content_type: concept
card:
  title: مرجع دستورهای kubeadm
  name: setup
  weight: 80
---

<img src="/images/kubeadm-stacked-color.png" align="right" width="150px">ابزار Kubeadm برای ارائهٔ دستورهای `kubeadm init` و `kubeadm join` ساخته شده است تا «مسیرهای سریعی» مطابق با بهترین شیوه‌ها برای ایجاد کلاسترهای کوبرنتیز فراهم کند.

این ابزار اقدامات لازم را برای راه‌اندازی و اجرای یک کلاستر حداقلی و کارآمد انجام می‌دهد. طراحی kubeadm به‌گونه‌ای است که فقط به راه‌اندازی اولیهٔ کلاستر می‌پردازد و تأمین ماشین‌ها در حوزهٔ کار آن نیست. همچنین نصب افزونه‌های گوناگونی که وجودشان مفید اما غیرضروری است، مانند داشبورد کوبرنتیز، راهکارهای پایش و افزونه‌های مختص هر ابر، در حوزهٔ کار این ابزار قرار ندارد.

در عوض، انتظار داریم ابزارهای سطح بالاتر و متناسب‌تر با نیازهای خاص بر پایهٔ kubeadm ساخته شوند. در حالت ایده‌آل، استفاده از kubeadm به‌عنوان پایهٔ همهٔ استقرارها، ایجاد کلاسترهای سازگار با استانداردهای کوبرنتیز را آسان‌تر می‌کند.

## روش نصب

برای نصب kubeadm، [راهنمای نصب](/docs/setup/production-environment/tools/kubeadm/install-kubeadm) را ببینید.

## {{% heading "whatsnext" %}}

* دستور [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init) برای راه‌اندازی اولیهٔ یک نود control plane کوبرنتیز
* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join) برای راه‌اندازی اولیهٔ یک نود کارگر کوبرنتیز و افزودن آن به کلاستر
* دستور [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade) برای ارتقای کلاستر کوبرنتیز به نسخه‌ای جدیدتر
* دستور [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config) برای پیکربندی کلاستر جهت استفاده از `kubeadm upgrade`، در صورتی که کلاستر را با kubeadm نسخهٔ v1.7.x یا پایین‌تر راه‌اندازی کرده باشید
* دستور [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token) برای مدیریت توکن‌های `kubeadm join`
* دستور [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset) برای بازگرداندن تغییراتی که `kubeadm init` یا `kubeadm join` روی این میزبان اعمال کرده‌اند
* دستور [kubeadm certs](/docs/reference/setup-tools/kubeadm/kubeadm-certs) برای مدیریت گواهی‌های کوبرنتیز
* دستور [kubeadm kubeconfig](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig) برای مدیریت فایل‌های kubeconfig
* دستور [kubeadm version](/docs/reference/setup-tools/kubeadm/kubeadm-version) برای نمایش نسخهٔ kubeadm
* دستور [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha) برای پیش‌نمایش مجموعه‌ای از قابلیت‌ها که برای دریافت بازخورد از جامعهٔ کاربری در دسترس قرار گرفته‌اند

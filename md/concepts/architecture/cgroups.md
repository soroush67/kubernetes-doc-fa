---
title: درباره‌ی cgroup v2
content_type: concept
weight: 50
---

<!-- overview -->

در لینوکس، {{< glossary_tooltip text="گروه‌های کنترلی" term_id="cgroup" >}}
منابع اختصاص‌یافته به پردازه‌ها را محدود می‌کنند.

{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و محیط اجرای کانتینر
زیرین آن باید با cgroupها تعامل داشته باشند تا
[مدیریت منابع برای پادها و کانتینرها](/docs/concepts/configuration/manage-resources-containers/)
را اعمال کنند. این مدیریت شامل درخواست‌ها (requests) و محدودیت‌های (limits) CPU و حافظه برای بارهای کاری کانتینری‌شده است.

لینوکس دو نسخه از cgroup دارد: cgroup v1 و cgroup v2. نسخه‌ی cgroup v2
نسل جدید API مربوط به `cgroup` است.

<!-- body -->


## نسخه‌ی cgroup v2 چیست؟ {#cgroup-v2}
{{< feature-state for_k8s_version="v1.25" state="stable" >}}

نسخه‌ی cgroup v2 نسخه‌ی بعدی API مربوط به `cgroup` در لینوکس است. این نسخه
یک سامانه‌ی کنترلی یکپارچه با قابلیت‌های پیشرفته‌تر برای مدیریت منابع فراهم می‌کند.

نسخه‌ی cgroup v2 چندین بهبود نسبت به cgroup v1 دارد که برخی از آن‌ها عبارت‌اند از:

- طراحی سلسله‌مراتبی واحد و یکپارچه در API
- واگذاری امن‌تر زیردرخت‌ها به کانتینرها
- قابلیت‌های جدیدتر مانند [Pressure Stall Information](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- مدیریت پیشرفته‌تر تخصیص منابع و جداسازی در میان چندین منبع
  - حسابداری یکپارچه برای انواع مختلف تخصیص حافظه (حافظه‌ی شبکه، حافظه‌ی کرنل و غیره)
  - حسابداری تغییرات غیرفوری منابع، مانند بازنویسی‌های حافظه‌ی نهان صفحه (page cache write backs)

برخی از قابلیت‌های کوبرنتیز برای مدیریت و جداسازی بهتر منابع منحصراً از cgroup v2
استفاده می‌کنند. برای نمونه، قابلیت
[MemoryQoS](/docs/concepts/workloads/pods/pod-qos/#memory-qos-with-cgroup-v2) کیفیت سرویس (QoS) حافظه را بهبود می‌دهد
و به سازوکارهای پایه‌ی cgroup v2 متکی است.


## استفاده از cgroup v2 {#using-cgroupv2}

روش توصیه‌شده برای استفاده از cgroup v2، به‌کارگیری یک توزیع لینوکس است که
cgroup v2 را به‌طور پیش‌فرض فعال کرده و از آن استفاده می‌کند.

برای اینکه بررسی کنید آیا توزیع شما از cgroup v2 استفاده می‌کند یا نه، به [شناسایی نسخه‌ی cgroup در نودهای لینوکسی](#check-cgroup-version) مراجعه کنید.

### پیش‌نیازها

نسخه‌ی cgroup v2 پیش‌نیازهای زیر را دارد:

* توزیع سیستم‌عامل، cgroup v2 را فعال کرده باشد.
* نسخه‌ی کرنل لینوکس 5.8 یا بالاتر باشد.
* محیط اجرای کانتینر از cgroup v2 پشتیبانی کند. برای نمونه:
  * محیط اجرای [containerd](https://containerd.io/) نسخه‌ی v1.4 و بالاتر
  * محیط اجرای [cri-o](https://cri-o.io/) نسخه‌ی v1.20 و بالاتر
* هم kubelet و هم محیط اجرای کانتینر برای استفاده از [درایور cgroup مربوط به systemd](/docs/setup/production-environment/container-runtimes#systemd-cgroup-driver) پیکربندی شده باشند.

### پشتیبانی توزیع‌های لینوکس از cgroup v2

برای مشاهده‌ی فهرست توزیع‌های لینوکسی که از cgroup v2 استفاده می‌کنند، به [مستندات cgroup v2](https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md) مراجعه کنید.

<!-- the list should be kept in sync with https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md -->
* سیستم‌عامل Container Optimized OS (از نسخه‌ی M97)
* توزیع Ubuntu (از نسخه‌ی 21.10؛ نسخه‌ی 22.04 و بالاتر توصیه می‌شود)
* توزیع Debian GNU/Linux (از Debian 11 bullseye)
* توزیع Fedora (از نسخه‌ی 31)
* توزیع Arch Linux (از آوریل ۲۰۲۱)
* توزیع RHEL و توزیع‌های مشابه آن (از نسخه‌ی 9)

برای اینکه بررسی کنید آیا توزیع شما از cgroup v2 استفاده می‌کند یا نه، به مستندات
توزیع خود مراجعه کنید یا دستورالعمل‌های بخش [شناسایی نسخه‌ی cgroup در نودهای لینوکسی](#check-cgroup-version) را دنبال کنید.

همچنین می‌توانید با تغییر آرگومان‌های راه‌اندازی خط فرمان کرنل (kernel cmdline)،
cgroup v2 را به‌صورت دستی در توزیع لینوکس خود فعال کنید. اگر توزیع شما از GRUB
استفاده می‌کند، باید `systemd.unified_cgroup_hierarchy=1` را به `GRUB_CMDLINE_LINUX`
در فایل `/etc/default/grub` اضافه کنید و سپس `sudo update-grub` را اجرا کنید. با این حال،
روش توصیه‌شده استفاده از توزیعی است که cgroup v2 را از پیش و به‌طور پیش‌فرض فعال کرده باشد.

### مهاجرت به cgroup v2 {#migrating-cgroupv2}

برای مهاجرت به cgroup v2، ابتدا مطمئن شوید که [پیش‌نیازها](#requirements) را برآورده می‌کنید و سپس
کرنل را به نسخه‌ای ارتقا دهید که cgroup v2 را به‌طور پیش‌فرض فعال می‌کند.

ابزار kubelet به‌طور خودکار تشخیص می‌دهد که سیستم‌عامل روی cgroup v2 اجرا می‌شود و
بدون نیاز به هیچ پیکربندی اضافه‌ای، متناسب با آن عمل می‌کند.

هنگام جابه‌جایی به cgroup v2 نباید تفاوت محسوسی در تجربه‌ی کاربری مشاهده شود،
مگر اینکه کاربران مستقیماً به سیستم فایل cgroup دسترسی داشته باشند؛ چه روی نود و چه از درون کانتینرها.

نسخه‌ی cgroup v2 از API متفاوتی نسبت به cgroup v1 استفاده می‌کند؛ بنابراین اگر برنامه‌هایی
وجود دارند که مستقیماً به سیستم فایل cgroup دسترسی دارند، باید به نسخه‌های جدیدتری
به‌روزرسانی شوند که از cgroup v2 پشتیبانی می‌کنند. برای نمونه:

* برخی از عامل‌های (agents) نظارتی و امنیتی شخص ثالث ممکن است به سیستم فایل cgroup وابسته باشند.
 این عامل‌ها را به نسخه‌هایی به‌روزرسانی کنید که از cgroup v2 پشتیبانی می‌کنند.
* اگر [cAdvisor](https://github.com/google/cadvisor) را به‌صورت یک DaemonSet مستقل
 برای نظارت بر پادها و کانتینرها اجرا می‌کنید، آن را به نسخه‌ی v0.43.0 یا بالاتر به‌روزرسانی کنید.
* اگر برنامه‌های جاوا را مستقر می‌کنید، ترجیحاً از نسخه‌هایی استفاده کنید که به‌طور کامل از cgroup v2 پشتیبانی می‌کنند:
    * نسخه‌های jdk8u372، 11.0.16، 15 و بالاتر از [OpenJDK / HotSpot](https://bugs.openjdk.org/browse/JDK-8230305)
    * نسخه‌های 8.0.382.0، 11.0.20.0، 17.0.8.0 و بالاتر از [IBM Semeru Runtimes](https://www.ibm.com/support/pages/apar/IJ46681)
    * نسخه‌ی 8.0.8.6 و بالاتر از [IBM Java](https://www.ibm.com/support/pages/apar/IJ46681)
* اگر از بسته‌ی [uber-go/automaxprocs](https://github.com/uber-go/automaxprocs) استفاده می‌کنید، مطمئن شوید
  نسخه‌ای که به کار می‌برید v1.5.1 یا بالاتر باشد.
* اگر برنامه‌های [Node.js](https://nodejs.org/) را مستقر می‌کنید، ترجیحاً از نسخه‌هایی استفاده کنید که محدودیت‌های
  حافظه‌ی cgroup v2 را تشخیص می‌دهند. محیط Node.js از نسخه‌ی v20.3.0 به بعد، محدودیت‌های حافظه‌ی cgroup v2 را
  (از طریق [libuv](https://libuv.org/)) می‌خواند. خط انتشار v18 محدودیت‌های حافظه‌ی cgroup v2 را به‌طور قابل‌اعتماد تشخیص نمی‌دهد.
  نسخه‌هایی که این پشتیبانی را ندارند ممکن است به‌جای محدودیت اعمال‌شده بر پاد، کل حافظه‌ی میزبان را بخوانند.
  این موضوع می‌تواند به تعیین نادرست اندازه‌ی heap و خاتمه‌ی پردازه به دلیل کمبود حافظه (OOM) منجر شود.
  در نسخه‌های آسیب‌پذیر، اندازه‌ی heap را به‌صراحت تنظیم کنید؛ برای مثال با فلگ
  `--max-old-space-size`.

## شناسایی نسخه‌ی cgroup در نودهای لینوکسی  {#check-cgroup-version}

نسخه‌ی cgroup به توزیع لینوکس مورد استفاده و نسخه‌ی پیش‌فرض cgroup که در سیستم‌عامل
پیکربندی شده است بستگی دارد. برای بررسی اینکه توزیع شما از کدام نسخه‌ی cgroup استفاده
می‌کند، دستور `stat -fc %T /sys/fs/cgroup/` را روی نود اجرا کنید:

```shell
stat -fc %T /sys/fs/cgroup/
```

برای cgroup v2، خروجی `cgroup2fs` است.

برای cgroup v1، خروجی `tmpfs.` است.

## منسوخ شدن cgroup v1

{{< feature-state for_k8s_version="v1.35" state="deprecated" >}}

کوبرنتیز پشتیبانی از cgroup v1 را منسوخ کرده است.
حذف آن مطابق [سیاست منسوخ‌سازی کوبرنتیز](/docs/reference/using-api/deprecation-policy/) انجام خواهد شد.

به‌طور پیش‌فرض، kubelet دیگر روی نودی که از cgroup v1 استفاده می‌کند اجرا نمی‌شود.
برای غیرفعال کردن این رفتار، مدیر کلاستر باید مقدار `failCgroupV1` را در [فایل پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) برابر false قرار دهد.

## {{% heading "whatsnext" %}}

- درباره‌ی [cgroupها](https://man7.org/linux/man-pages/man7/cgroups.7.html) بیشتر بیاموزید.
- درباره‌ی [محیط اجرای کانتینر](/docs/concepts/containers/cri/) بیشتر بیاموزید.
- درباره‌ی [درایورهای cgroup](/docs/setup/production-environment/container-runtimes#cgroup-drivers) بیشتر بیاموزید.

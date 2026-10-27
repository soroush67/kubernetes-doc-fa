---
title: دربارهٔ cgroup v2
content_type: concept
weight: 50
---

<!-- overview -->

در لینوکس، {{< glossary_tooltip text="گروه‌های کنترلی (control groups)" term_id="cgroup" >}}
منابعی را که به فرایندها تخصیص داده می‌شوند محدود می‌کنند.

{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و
محیط اجرای کانتینر زیربنایی باید با cgroupها تعامل داشته باشند تا
[مدیریت منابع برای پادها و کانتینرها](/docs/concepts/configuration/manage-resources-containers/) را اعمال کنند؛ این مدیریت
شامل درخواست‌ها (requests) و محدودیت‌های (limits) پردازنده و حافظه برای بارهای کاری کانتینری‌شده است.

در لینوکس دو نسخه از cgroupها وجود دارد: cgroup v1 و cgroup v2. cgroup v2
نسل جدید API مربوط به `cgroup` است.

<!-- body -->


## cgroup v2 چیست؟ {#cgroup-v2}
{{< feature-state for_k8s_version="v1.25" state="stable" >}}

cgroup v2 نسخهٔ بعدی API لینوکس `cgroup` است. cgroup v2 یک
سیستم کنترلی یکپارچه با قابلیت‌های پیشرفته‌تر مدیریت منابع
فراهم می‌کند.

cgroup v2 بهبودهای متعددی نسبت به cgroup v1 ارائه می‌دهد، از جمله موارد زیر:

- طراحی سلسله‌مراتب یکپارچهٔ واحد در API
- واگذاری امن‌تر زیردرخت‌ها به کانتینرها
- قابلیت‌های جدیدتر مانند [اطلاعات توقف ناشی از فشار (Pressure Stall Information)](https://www.kernel.org/doc/html/latest/accounting/psi.html)
- مدیریت پیشرفته‌تر تخصیص منابع و جداسازی در میان چندین منبع
  - حسابرسی یکپارچه برای انواع مختلف تخصیص حافظه (حافظهٔ شبکه، حافظهٔ هسته و غیره)
  - حسابرسی تغییرات غیرآنی منابع، مانند بازنویسی‌های حافظهٔ نهان صفحه (page cache write backs)

برخی از قابلیت‌های کوبرنتیز برای مدیریت و جداسازی پیشرفته‌تر منابع منحصراً از cgroup v2
استفاده می‌کنند. برای نمونه، قابلیت
[MemoryQoS](/docs/concepts/workloads/pods/pod-qos/#memory-qos-with-cgroup-v2) کیفیت خدمات (QoS) حافظه را بهبود می‌بخشد
و به سازه‌های پایه‌ای cgroup v2 متکی است.


## استفاده از cgroup v2 {#using-cgroupv2}

روش توصیه‌شده برای استفاده از cgroup v2، به‌کارگیری یک توزیع لینوکس است که
cgroup v2 را به‌طور پیش‌فرض فعال کرده و از آن استفاده می‌کند.

برای بررسی اینکه آیا توزیع شما از cgroup v2 استفاده می‌کند، به [شناسایی نسخهٔ cgroup روی نودهای لینوکسی](#check-cgroup-version) مراجعه کنید.

### نیازمندی‌ها

cgroup v2 نیازمندی‌های زیر را دارد:

* توزیع سیستم‌عامل، cgroup v2 را فعال کرده باشد
* نسخهٔ هستهٔ لینوکس 5.8 یا بالاتر باشد
* محیط اجرای کانتینر از cgroup v2 پشتیبانی کند. برای نمونه:
  * [containerd](https://containerd.io/) نسخهٔ v1.4 و بالاتر
  * [cri-o](https://cri-o.io/) نسخهٔ v1.20 و بالاتر
* kubelet و محیط اجرای کانتینر برای استفاده از [درایور cgroup مبتنی بر systemd](/docs/setup/production-environment/container-runtimes#systemd-cgroup-driver) پیکربندی شده باشند

### پشتیبانی توزیع‌های لینوکس از cgroup v2

برای فهرستی از توزیع‌های لینوکسی که از cgroup v2 استفاده می‌کنند، به [مستندات cgroup v2](https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md) مراجعه کنید

<!-- the list should be kept in sync with https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md -->
* Container Optimized OS (از M97 به بعد)
* Ubuntu (از 21.10 به بعد؛ 22.04 و بالاتر توصیه می‌شود)
* Debian GNU/Linux (از Debian 11 bullseye به بعد)
* Fedora (از 31 به بعد)
* Arch Linux (از آوریل ۲۰۲۱ به بعد)
* RHEL و توزیع‌های مشابه RHEL (از 9 به بعد)

برای بررسی اینکه آیا توزیع شما از cgroup v2 استفاده می‌کند، به مستندات توزیع خود مراجعه کنید
یا دستورالعمل‌های بخش [شناسایی نسخهٔ cgroup روی نودهای لینوکسی](#check-cgroup-version) را دنبال کنید.

همچنین می‌توانید cgroup v2 را با تغییر آرگومان‌های راه‌اندازی خط فرمان هسته (kernel cmdline)
به‌صورت دستی در توزیع لینوکس خود فعال کنید. اگر توزیع شما از GRUB استفاده می‌کند،
باید `systemd.unified_cgroup_hierarchy=1` را به `GRUB_CMDLINE_LINUX`
در فایل `/etc/default/grub` اضافه کنید و سپس `sudo update-grub` را اجرا کنید. با این حال،
رویکرد توصیه‌شده استفاده از توزیعی است که cgroup v2 را از پیش و به‌طور
پیش‌فرض فعال کرده باشد.

### مهاجرت به cgroup v2 {#migrating-cgroupv2}

برای مهاجرت به cgroup v2، اطمینان حاصل کنید که [نیازمندی‌ها](#requirements) را برآورده می‌کنید و سپس
به نسخه‌ای از هسته ارتقا دهید که cgroup v2 را به‌طور پیش‌فرض فعال می‌کند.

kubelet به‌طور خودکار تشخیص می‌دهد که سیستم‌عامل روی cgroup v2 اجرا می‌شود و
بدون نیاز به هیچ پیکربندی اضافه‌ای بر همین اساس عمل می‌کند.

هنگام تغییر به cgroup v2 نباید تفاوت محسوسی در تجربهٔ کاربری وجود داشته باشد،
مگر اینکه کاربران مستقیماً، چه روی نود و چه از درون کانتینرها، به سیستم فایل cgroup
دسترسی داشته باشند.

cgroup v2 از API متفاوتی نسبت به cgroup v1 استفاده می‌کند؛ بنابراین اگر برنامه‌هایی
وجود دارند که مستقیماً به سیستم فایل cgroup دسترسی دارند، باید به
نسخه‌های جدیدتری که از cgroup v2 پشتیبانی می‌کنند به‌روزرسانی شوند. برای نمونه:

* برخی از عامل‌های پایش و امنیتی شخص ثالث ممکن است به سیستم فایل cgroup وابسته باشند.
 این عامل‌ها را به نسخه‌هایی به‌روزرسانی کنید که از cgroup v2 پشتیبانی می‌کنند.
* اگر [cAdvisor](https://github.com/google/cadvisor) را به‌صورت یک DaemonSet مستقل
 برای پایش پادها و کانتینرها اجرا می‌کنید، آن را به نسخهٔ v0.43.0 یا بالاتر به‌روزرسانی کنید.
* اگر برنامه‌های Java مستقر می‌کنید، ترجیحاً از نسخه‌هایی استفاده کنید که به‌طور کامل از cgroup v2 پشتیبانی می‌کنند:
    * [OpenJDK / HotSpot](https://bugs.openjdk.org/browse/JDK-8230305): نسخه‌های jdk8u372، 11.0.16، 15 و بالاتر
    * [IBM Semeru Runtimes](https://www.ibm.com/support/pages/apar/IJ46681): نسخه‌های 8.0.382.0، 11.0.20.0، 17.0.8.0 و بالاتر
    * [IBM Java](https://www.ibm.com/support/pages/apar/IJ46681): نسخهٔ 8.0.8.6 و بالاتر
* اگر از بستهٔ [uber-go/automaxprocs](https://github.com/uber-go/automaxprocs) استفاده می‌کنید، اطمینان حاصل کنید
  که نسخهٔ مورد استفادهٔ شما v1.5.1 یا بالاتر است.
* اگر برنامه‌های [Node.js](https://nodejs.org/) مستقر می‌کنید، ترجیحاً از نسخه‌هایی استفاده کنید که محدودیت‌های حافظهٔ cgroup v2
  را تشخیص می‌دهند. Node.js از نسخهٔ v20.3.0 به بعد، محدودیت‌های حافظهٔ cgroup v2 را (از طریق [libuv](https://libuv.org/))
  می‌خواند. شاخهٔ انتشار v18 محدودیت‌های حافظهٔ cgroup v2 را به‌طور قابل‌اطمینانی تشخیص نمی‌دهد.
  نسخه‌های فاقد این پشتیبانی ممکن است به‌جای محدودیت اعمال‌شده بر پاد، کل حافظهٔ میزبان را بخوانند
  که می‌تواند به اندازهٔ نادرست heap و خاتمه‌های ناشی از کمبود حافظه (OOM)
  منجر شود. در نسخه‌های متأثر، اندازهٔ heap را به‌طور صریح تنظیم کنید؛ برای نمونه با
  پرچم `--max-old-space-size`.

## شناسایی نسخهٔ cgroup روی نودهای لینوکسی  {#check-cgroup-version}

نسخهٔ cgroup به توزیع لینوکس مورد استفاده و
نسخهٔ پیش‌فرض cgroup پیکربندی‌شده در سیستم‌عامل بستگی دارد. برای بررسی اینکه توزیع شما از کدام نسخهٔ cgroup
استفاده می‌کند، فرمان `stat -fc %T /sys/fs/cgroup/` را روی
نود اجرا کنید:

```shell
stat -fc %T /sys/fs/cgroup/
```

برای cgroup v2، خروجی `cgroup2fs` است.

برای cgroup v1، خروجی `tmpfs.` است.

## منسوخ‌شدن cgroup v1

{{< feature-state for_k8s_version="v1.35" state="deprecated" >}}

کوبرنتیز cgroup v1 را منسوخ کرده است.
حذف آن مطابق با [سیاست منسوخ‌سازی کوبرنتیز](/docs/reference/using-api/deprecation-policy/) انجام خواهد شد.

kubelet به‌طور پیش‌فرض دیگر روی نودی با cgroup v1 راه‌اندازی نخواهد شد.
برای غیرفعال‌کردن این تنظیم، مدیر کلاستر باید `failCgroupV1` را در [فایل پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) برابر با false قرار دهد.

## {{% heading "whatsnext" %}}

- دربارهٔ [cgroupها](https://man7.org/linux/man-pages/man7/cgroups.7.html) بیشتر بیاموزید
- دربارهٔ [محیط اجرای کانتینر](/docs/concepts/architecture/cri) بیشتر بیاموزید
- دربارهٔ [درایورهای cgroup](/docs/setup/production-environment/container-runtimes#cgroup-drivers) بیشتر بیاموزید

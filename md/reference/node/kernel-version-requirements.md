---
content_type: "reference"
title: الزامات نسخه کرنل لینوکس
weight: 10
---

{{% thirdparty-content %}}

بسیاری از قابلیت‌ها به امکانات مشخصی از کرنل وابسته‌اند و به حداقل نسخه‌ای از کرنل نیاز دارند. با این حال، اتکای صرف به شماره نسخه کرنل در برخی توزیع‌های سیستم‌عامل کافی نیست، زیرا نگهدارندگان توزیع‌هایی مانند RHEL، Ubuntu و SUSE اغلب قابلیت‌های منتخب را به نسخه‌های قدیمی‌تر کرنل پس‌انتقال (backport) می‌دهند و شماره نسخه قدیمی کرنل را حفظ می‌کنند.

## پارامترهای sysctl در Pod

در لینوکس، فراخوانی سیستمی `sysctl()` پارامترهای کرنل را در زمان اجرا پیکربندی می‌کند. برای پیکربندی این پارامترها می‌توانید از ابزار خط فرمانی به نام `sysctl` نیز استفاده کنید. بسیاری از این پارامترها از طریق فایل‌سیستم `proc` نیز در دسترس هستند.

برخی از پارامترهای sysctl فقط در کرنل‌های به‌اندازه کافی جدید در دسترس‌اند.

پارامترهای sysctl زیر به حداقل نسخه‌ای از کرنل نیاز دارند و در [مجموعه امن](/docs/tasks/administer-cluster/sysctl-cluster/#safe-and-unsafe-sysctls) پشتیبانی می‌شوند:

<!--
Code: https://github.com/kubernetes/kubernetes/blob/00236ae0d73d2455a2470469ed1005674f8ed61f/pkg/util/kernel/constants.go#L19-L45
-->
- پارامتر `net.ipv4.ip_local_reserved_ports` (از کوبرنتیز 1.27، نیازمند کرنل 3.16 یا بالاتر)؛
- پارامتر `net.ipv4.tcp_keepalive_time` (از کوبرنتیز 1.29، نیازمند کرنل 4.5 یا بالاتر)؛
- پارامتر `net.ipv4.tcp_fin_timeout` (از کوبرنتیز 1.29، نیازمند کرنل 4.6 یا بالاتر)؛
- پارامتر `net.ipv4.tcp_keepalive_intvl` (از کوبرنتیز 1.29، نیازمند کرنل 4.5 یا بالاتر)؛
- پارامتر `net.ipv4.tcp_keepalive_probes` (از کوبرنتیز 1.29، نیازمند کرنل 4.5 یا بالاتر)؛
- پارامتر `net.ipv4.tcp_syncookies` (از کرنل 4.6 به بعد در سطح فضای نام (namespace) تنظیم می‌شود).
- پارامتر `net.ipv4.tcp_rmem` (از کوبرنتیز 1.32، نیازمند کرنل 4.15 یا بالاتر).
- پارامتر `net.ipv4.tcp_wmem` (از کوبرنتیز 1.32، نیازمند کرنل 4.15 یا بالاتر).
- پارامتر `net.ipv4.tcp_slow_start_after_idle` (از کوبرنتیز 1.37، نیازمند کرنل 4.15 یا بالاتر).
- پارامتر `net.ipv4.tcp_notsent_lowat` (از کوبرنتیز 1.37، نیازمند کرنل 4.6 یا بالاتر).
- پارامتر `net.ipv4.vs.conn_reuse_mode` (در حالت پراکسی `ipvs` استفاده می‌شود، نیازمند کرنل 4.1 یا بالاتر)؛

### حالت پراکسی `nftables` در kube-proxy

<!--
Code: https://github.com/kubernetes/kubernetes/blob/00236ae0d73d2455a2470469ed1005674f8ed61f/pkg/util/kernel/constants.go#L53-L56
-->
در کوبرنتیز {{< skew currentVersion >}}، [حالت `nftables`](/docs/reference/networking/virtual-ips/#proxy-mode-nftables) در kube-proxy به ابزار خط فرمان nft با نسخه 1.0.1 یا بالاتر و همچنین کرنل 5.13 یا بالاتر نیاز دارد.

برای آزمایش و توسعه می‌توانید با تنظیم گزینه `nftables.skipKernelVersionCheck` در پیکربندی kube-proxy از کرنل‌های قدیمی‌تر، حداکثر تا نسخه 5.4، استفاده کنید. با این حال، این کار در محیط عملیاتی توصیه نمی‌شود، زیرا ممکن است برای سایر کاربران nftables در سیستم مشکل ایجاد کند.

## گروه‌های کنترلی نسخه ۲

پشتیبانی کوبرنتیز از cgroup v1 از نسخه v1.31 در حالت نگهداری قرار دارد و استفاده از cgroup v2 توصیه می‌شود. در [لینوکس 5.8](https://github.com/torvalds/linux/commit/4a7e89c5ec0238017a757131eb9ab8dc111f961c)، برای سهولت کار، فایل `cpu.stat` در سطح سیستم به cgroup ریشه اضافه شد.

در مستندات runc، استفاده از کرنل‌های قدیمی‌تر از 5.2 به دلیل نبود freezer توصیه نشده است.

## اطلاعات توقف ناشی از فشار (Pressure Stall Information یا PSI) {#requirements-psi}

[اطلاعات توقف ناشی از فشار](/docs/reference/instrumentation/understand-psi-metrics/) در کرنل لینوکس نسخه 4.20 و بالاتر پشتیبانی می‌شود، اما به پیکربندی زیر نیاز دارد:

- کرنل باید با گزینه `CONFIG_PSI=y` کامپایل شده باشد. بیشتر توزیع‌های جدید این گزینه را به‌طور پیش‌فرض فعال می‌کنند. برای بررسی پیکربندی کرنل خود می‌توانید دستور `zgrep CONFIG_PSI /proc/config.gz` را اجرا کنید.
- برخی از توزیع‌های لینوکس ممکن است PSI را در کرنل کامپایل کنند، اما آن را به‌طور پیش‌فرض غیرفعال نگه دارند. در این صورت باید با افزودن پارامتر `psi=1` به خط فرمان کرنل، آن را در زمان راه‌اندازی سیستم فعال کنید.

## سایر الزامات کرنل {#requirements-other}

برخی از قابلیت‌ها ممکن است به امکانات جدید کرنل وابسته باشند و الزامات مشخصی برای کرنل داشته باشند:

<!--
Code(recursive read only mount): https://github.com/kubernetes/kubernetes/blob/00236ae0d73d2455a2470469ed1005674f8ed61f/staging/src/k8s.io/cri-api/pkg/apis/runtime/v1/api.proto#L1605-L1609
Code(user namespace and swap): https://github.com/kubernetes/kubernetes/blob/00236ae0d73d2455a2470469ed1005674f8ed61f/pkg/util/kernel/constants.go#L47-L51
-->
1. [اتصال (mount) فقط‌خواندنی بازگشتی](/docs/concepts/storage/volumes/#recursive-read-only-mounts):
    این قابلیت با اعمال ویژگی `MOUNT_ATTR_RDONLY` همراه با پرچم `AT_RECURSIVE` از طریق `mount_setattr`(2) پیاده‌سازی شده است که در کرنل لینوکس v5.12 اضافه شد.
2. بر اساس [KEP-127](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/127-user-namespaces/README.md)، پشتیبانی از فضای نام کاربری در Pod به کرنل نسخه 6.5 یا بالاتر نیاز دارد.
3. در [swap سیستمی نود](/docs/concepts/architecture/nodes/#swap-memory)، تنظیم tmpfs روی `noswap` تا پیش از کرنل 6.3 پشتیبانی نمی‌شود.

## نگهداری بلندمدت کرنل لینوکس

فهرست نسخه‌های فعال کرنل را می‌توانید در [kernel.org](https://www.kernel.org/category/releases.html) ببینید.

معمولاً چند نسخه کرنل با _نگهداری بلندمدت_ ارائه می‌شود تا رفع اشکال‌ها به شاخه‌های قدیمی‌تر کرنل پس‌انتقال داده شوند. در این کرنل‌ها فقط اشکال‌های مهم برطرف می‌شوند و نسخه‌های جدید آن‌ها، به‌ویژه در شاخه‌های قدیمی‌تر، معمولاً با فاصله زیاد منتشر می‌شوند. برای دیدن [فهرست نسخه‌ها](https://www.kernel.org/category/releases.html) در دسته _Longterm_ به وب‌سایت کرنل لینوکس مراجعه کنید.

## {{% heading "whatsnext" %}}

- برای جزئیات بیشتر، صفحه [پارامترهای sysctl](/docs/tasks/administer-cluster/sysctl-cluster/) را ببینید.
- اجرای kube-proxy را در [حالت nftables](/docs/reference/networking/virtual-ips/#proxy-mode-nftables) فعال کنید.
- اطلاعات بیشتر را در [cgroups v2](/docs/concepts/architecture/cgroups/) بخوانید.

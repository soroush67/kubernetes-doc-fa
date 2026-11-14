---
reviewers:
- derekwaynecarr
title: مدیریت HugePages
content_type: task
description: پیکربندی و مدیریت صفحه‌های بزرگ (huge pages) به‌عنوان منبعی قابل زمان‌بندی در کلاستر.
---

<!-- overview -->
{{< feature-state feature_gate_name="HugePages" >}}

کوبرنتیز از تخصیص و مصرف صفحه‌های بزرگ (huge pages) ازپیش‌تخصیص‌یافته توسط برنامه‌های درون یک Pod پشتیبانی می‌کند. این صفحه توضیح می‌دهد که کاربران چگونه می‌توانند از صفحه‌های بزرگ استفاده کنند.

## {{% heading "prerequisites" %}}

نودهای کوبرنتیز باید
[صفحه‌های بزرگ را از پیش تخصیص دهند](https://www.kernel.org/doc/html/latest/admin-guide/mm/hugetlbpage.html)
تا نود بتواند ظرفیت صفحه‌های بزرگ خود را گزارش کند.

هر نود می‌تواند صفحه‌های بزرگ را در چند اندازه از پیش تخصیص دهد. برای نمونه، خط زیر در فایل `/etc/default/grub` تعداد `2*1GiB` صفحه از نوع ۱ GiB و `512*2 MiB` صفحه از نوع ۲ MiB تخصیص می‌دهد:

```
GRUB_CMDLINE_LINUX="hugepagesz=1G hugepages=2 hugepagesz=2M hugepages=512"
```

نودها به‌طور خودکار همهٔ منابع صفحه‌های بزرگ را شناسایی می‌کنند و آن‌ها را به‌عنوان منابع قابل زمان‌بندی گزارش می‌دهند.

هنگامی که Node را توصیف (describe) می‌کنید، باید در بخش‌های `Capacity` و `Allocatable` خروجی‌ای مشابه زیر ببینید:

```
Capacity:
  cpu:                ...
  ephemeral-storage:  ...
  hugepages-1Gi:      2Gi
  hugepages-2Mi:      1Gi
  memory:             ...
  pods:               ...
Allocatable:
  cpu:                ...
  ephemeral-storage:  ...
  hugepages-1Gi:      2Gi
  hugepages-2Mi:      1Gi
  memory:             ...
  pods:               ...
```

{{< note >}}
برای صفحه‌هایی که به‌صورت پویا (پس از راه‌اندازی سیستم) تخصیص داده می‌شوند، باید kubelet را دوباره راه‌اندازی کنید تا تخصیص‌های جدید در آن منعکس شوند.
{{< /note >}}

<!-- steps -->

## API

صفحه‌های بزرگ را می‌توان از طریق الزامات منابع در سطح کانتینر و با نام منبع `hugepages-<size>` مصرف کرد. در این نام، `<size>` فشرده‌ترین نمایش دودویی با مقادیر صحیح است که روی یک نود مشخص پشتیبانی می‌شود. برای مثال، اگر نودی از اندازه‌های صفحهٔ 2048KiB و 1048576KiB پشتیبانی کند، منابع قابل زمان‌بندی `hugepages-2Mi` و `hugepages-1Gi` را ارائه می‌دهد. برخلاف CPU یا حافظه، صفحه‌های بزرگ از تخصیص بیش از ظرفیت (overcommit) پشتیبانی نمی‌کنند. توجه کنید که هنگام درخواست منابع صفحه‌های بزرگ، باید منابع حافظه یا CPU را نیز درخواست کنید.

یک پاد می‌تواند در یک مشخصهٔ پاد (pod spec) از چند اندازهٔ صفحهٔ بزرگ استفاده کند. در این حالت، باید برای همهٔ اتصال‌های حجم (volume mount) از نشانه‌گذاری `medium: HugePages-<hugepagesize>` استفاده کند.


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: huge-pages-example
spec:
  containers:
  - name: example
    image: fedora:latest
    command:
    - sleep
    - inf
    volumeMounts:
    - mountPath: /hugepages-2Mi
      name: hugepage-2mi
    - mountPath: /hugepages-1Gi
      name: hugepage-1gi
    resources:
      limits:
        hugepages-2Mi: 100Mi
        hugepages-1Gi: 2Gi
        memory: 100Mi
      requests:
        memory: 100Mi
  volumes:
  - name: hugepage-2mi
    emptyDir:
      medium: HugePages-2Mi
  - name: hugepage-1gi
    emptyDir:
      medium: HugePages-1Gi
```

یک پاد تنها در صورتی می‌تواند از `medium: HugePages` استفاده کند که صفحه‌های بزرگ را فقط در یک اندازه درخواست کند.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: huge-pages-example
spec:
  containers:
  - name: example
    image: fedora:latest
    command:
    - sleep
    - inf
    volumeMounts:
    - mountPath: /hugepages
      name: hugepage
    resources:
      limits:
        hugepages-2Mi: 100Mi
        memory: 100Mi
      requests:
        memory: 100Mi
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

- درخواست‌های صفحه‌های بزرگ باید با محدودیت‌ها (limits) برابر باشند. اگر محدودیت‌ها مشخص شده باشند اما درخواست‌ها مشخص نشده باشند، همین حالت به‌طور پیش‌فرض اعمال می‌شود.
- صفحه‌های بزرگ در سطح کانتینر ایزوله می‌شوند؛ بنابراین هر کانتینر، مطابق آنچه در مشخصهٔ کانتینر درخواست شده است، محدودیت مخصوص به خود را روی محیط ایزولهٔ cgroup خود دارد.
- حجم‌های EmptyDir که بر پایهٔ صفحه‌های بزرگ ایجاد شده‌اند، نمی‌توانند بیش از مقدار درخواست‌شده توسط پاد از حافظهٔ صفحه‌های بزرگ مصرف کنند.
- برنامه‌هایی که از طریق `shmget()` همراه با `SHM_HUGETLB` صفحه‌های بزرگ را مصرف می‌کنند، باید با یک گروه تکمیلی (supplemental group) اجرا شوند که با مقدار `proc/sys/vm/hugetlb_shm_group` مطابقت داشته باشد.
- میزان استفاده از صفحه‌های بزرگ در یک فضای نام (namespace) را می‌توان، مانند سایر منابع محاسباتی نظیر `cpu` یا `memory`، با استفاده از ResourceQuota و توکن `hugepages-<size>` کنترل کرد.

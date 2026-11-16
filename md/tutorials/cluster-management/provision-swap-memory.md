---
reviewers:
- lmktfy
title: پیکربندی حافظهٔ swap روی نودهای کوبرنتیز
content_type: tutorial
weight: 35
min-kubernetes-server-version: "1.33"
---

<!-- overview -->

این صفحه نمونه‌ای از تأمین و پیکربندی حافظهٔ swap روی یک نود کوبرنتیز با استفاده از kubeadm را ارائه می‌کند.

<!-- lessoncontent -->

## {{% heading "objectives" %}}

* حافظهٔ swap را با استفاده از kubeadm روی یک نود کوبرنتیز تأمین کنید.
* با پیکربندی swap رمزگذاری‌شده و رمزگذاری‌نشده آشنا شوید.
* با فعال‌سازی swap هنگام راه‌اندازی سیستم آشنا شوید.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

کلاستر شما باید دست‌کم یک نود کارگر (worker node) داشته باشد که سیستم‌عامل لینوکس روی آن اجرا شود.
برای این نمایش لازم است ابزار kubeadm را طبق مراحل شرح‌داده‌شده در
[راهنمای نصب kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm) نصب کرده باشید.

روی هر نود کارگری که قرار است استفاده از swap را در آن پیکربندی کنید، به این ابزارها نیاز دارید:
* `fallocate`
* `mkswap`
* `swapon`

* برای فضای swap رمزگذاری‌شده (توصیه‌شده)، به این ابزار نیز نیاز دارید:
* `cryptsetup`

<!-- lessoncontent -->


## نصب کلاستری با قابلیت swap به کمک kubeadm

### ایجاد فایل swap و روشن کردن swap

اگر swap فعال نیست، باید آن را روی نود تأمین کنید.
بخش‌های زیر نحوهٔ ایجاد ۴ گیبی‌بایت (GiB) فضای swap را در هر دو حالت رمزگذاری‌شده و رمزگذاری‌نشده نشان می‌دهند.

{{< tabs name="ایجاد فایل swap و روشن کردن swap" >}}

{{% tab name="راه‌اندازی swap رمزگذاری‌شده" %}}
می‌توانید یک فایل swap رمزگذاری‌شده را به روش زیر راه‌اندازی کنید.
توجه داشته باشید که این مثال از فایل اجرایی `cryptsetup` استفاده می‌کند (که در بیشتر
توزیع‌های لینوکس در دسترس است).

```bash
# Allocate storage and restrict access
fallocate --length 4GiB /swapfile
chmod 600 /swapfile

# Create an encrypted device backed by the allocated storage
cryptsetup --type plain --cipher aes-xts-plain64 --key-size 256 -d /dev/urandom open /swapfile cryptswap

# Format the swap space
mkswap /dev/mapper/cryptswap

# Activate the swap space for paging
swapon /dev/mapper/cryptswap
```

{{% /tab %}}

{{% tab name="راه‌اندازی swap رمزگذاری‌نشده" %}}
می‌توانید یک فایل swap رمزگذاری‌نشده را به روش زیر راه‌اندازی کنید.

```bash
# Allocate storage and restrict access
fallocate --length 4GiB /swapfile
chmod 600 /swapfile

# Format the swap space
mkswap /swapfile

# Activate the swap space for paging
swapon /swapfile
```

{{% /tab %}}

{{< /tabs >}}

#### بررسی فعال بودن swap

برای اطمینان از فعال بودن swap می‌توانید از دستور `swapon -s` یا دستور `free` استفاده کنید.

با استفاده از `swapon -s`:
```
Filename       Type		Size		Used		Priority
/dev/dm-0      partition 	4194300		0		-2
```

با استفاده از `free -h`:
```
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       1.3Gi       249Mi        25Mi       2.5Gi       2.5Gi
Swap:          4.0Gi          0B       4.0Gi
```

#### فعال‌سازی swap هنگام راه‌اندازی سیستم

پس از راه‌اندازی swap، برای اینکه فایل swap هنگام بوت سیستم فعال شود،
معمولاً یا یک یونیت systemd برای فعال‌سازی swap (رمزگذاری‌شده) تعریف می‌کنید، یا
خطی مشابه `/swapfile swap swap defaults 0 0` را به فایل `/etc/fstab` اضافه می‌کنید.

اگر بخواهید اطمینان یابید که kubelet پیش از در دسترس بودن swap اجرا نمی‌شود، می‌توانید
فعال‌سازی swap را با systemd انجام دهید؛ در این صورت سیستم شروع به کار kubelet را تا آماده شدن swap به تأخیر می‌اندازد.
به همین ترتیب، استفاده از systemd باعث می‌شود سرور شما swap را تا زمان خاموش شدن kubelet
(و معمولاً محیط اجرای کانتینر) فعال نگه دارد.

### تنظیم پیکربندی kubelet

پس از فعال‌سازی swap روی نود، باید kubelet را برای استفاده از آن پیکربندی کنید.
لازم است یک [رفتار swap](/docs/reference/node/swap-behavior/)
برای این نود انتخاب کنید. در این آموزش، رفتار _LimitedSwap_ را پیکربندی خواهید کرد.

فایل پیکربندی kubelet را پیدا و ویرایش کنید و:

- مقدار `failSwapOn` را برابر false قرار دهید
- مقدار `memorySwap.swapBehavior` را برابر LimitedSwap قرار دهید

```yaml
 # this fragment goes into the kubelet's configuration file
 failSwapOn: false
 memorySwap:
     swapBehavior: LimitedSwap
```

برای اعمال شدن این پیکربندی‌ها، باید kubelet را دوباره راه‌اندازی کنید.
معمولاً این کار را با اجرای دستور زیر انجام می‌دهید:
```shell
systemctl restart kubelet.service
```

اکنون باید ببینید که kubelet در وضعیت سالم قرار دارد و می‌توانید Podهایی را اجرا کنید
که در صورت نیاز از حافظهٔ swap استفاده می‌کنند.

---
title: پیدا کردن محیط اجرای کانتینر مورد استفاده در یک نود
content_type: task
reviewers:
- SergeyKanzhelev
weight: 30
---

<!-- overview -->

این صفحه مراحل پیدا کردن [محیط اجرای کانتینری](/docs/setup/production-environment/container-runtimes/)
را شرح می‌دهد که نودهای کلاستر شما از آن استفاده می‌کنند.

بسته به روشی که کلاستر خود را اجرا می‌کنید، ممکن است محیط اجرای کانتینر نودها
از پیش پیکربندی شده باشد یا لازم باشد خودتان آن را پیکربندی کنید. اگر از یک سرویس
مدیریت‌شدهٔ کوبرنتیز استفاده می‌کنید، ممکن است ارائه‌دهنده روش‌های مخصوص خود را برای
بررسی محیط اجرای کانتینر پیکربندی‌شده روی نودها داشته باشد. روش شرح‌داده‌شده در این صفحه
در هر جایی که اجرای `kubectl` مجاز باشد، باید کار کند.

## {{% heading "prerequisites" %}}

ابزار `kubectl` را نصب و پیکربندی کنید. برای جزئیات بیشتر، بخش [نصب ابزارها](/docs/tasks/tools/#kubectl) را ببینید.

## پیدا کردن محیط اجرای کانتینر مورد استفاده در یک نود

با استفاده از `kubectl` اطلاعات نودها را دریافت و نمایش دهید:

```shell
kubectl get nodes -o wide
```

خروجی مشابه نمونهٔ زیر است. ستون `CONTAINER-RUNTIME` محیط اجرا و نسخهٔ آن را
نشان می‌دهد.

برای Docker Engine، خروجی مشابه این است:

```none
NAME         STATUS   VERSION    CONTAINER-RUNTIME
node-1       Ready    v1.16.15   docker://19.3.1
node-2       Ready    v1.16.15   docker://19.3.1
node-3       Ready    v1.16.15   docker://19.3.1
```
اگر محیط اجرای شما Docker Engine نشان داده می‌شود، باز هم ممکن است حذف dockershim
در کوبرنتیز نسخهٔ v1.24 روی شما تأثیری نداشته باشد.
برای اینکه بفهمید از dockershim استفاده می‌کنید یا نه، [نقطهٔ پایانی محیط اجرا را بررسی کنید](#which-endpoint).
اگر از dockershim استفاده نمی‌کنید، این تغییر روی شما تأثیری ندارد.

برای containerd، خروجی مشابه این است:

```none
NAME         STATUS   VERSION   CONTAINER-RUNTIME
node-1       Ready    v1.19.6   containerd://1.4.1
node-2       Ready    v1.19.6   containerd://1.4.1
node-3       Ready    v1.19.6   containerd://1.4.1
```

برای اطلاعات بیشتر دربارهٔ محیط‌های اجرای کانتینر، صفحهٔ
[محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/)
را ببینید.

## پیدا کردن نقطهٔ پایانی محیط اجرای کانتینر مورد استفاده {#which-endpoint}

محیط اجرای کانتینر از طریق یک سوکت یونیکس و با استفاده از [پروتکل
CRI](/docs/concepts/architecture/cri/) که بر پایهٔ چارچوب gRPC ساخته شده است، با kubelet
ارتباط برقرار می‌کند. در این ارتباط، kubelet نقش کلاینت و محیط اجرا نقش سرور را دارد.
در برخی موارد، دانستن اینکه نودهای شما از کدام سوکت استفاده می‌کنند مفید است. برای
نمونه، با حذف dockershim در کوبرنتیز نسخهٔ v1.24 و نسخه‌های بعدی، ممکن است بخواهید
بدانید که آیا از Docker Engine همراه با dockershim استفاده می‌کنید یا نه.

{{<note>}}
اگر در حال حاضر روی نودهای خود از Docker Engine همراه با `cri-dockerd` استفاده می‌کنید،
حذف dockershim روی شما تأثیری ندارد.
{{</note>}}

با بررسی پیکربندی kubelet روی نودها می‌توانید بفهمید از کدام سوکت استفاده می‌کنید.

1.  دستورهای راه‌اندازی فرایند kubelet را بخوانید:

    ```
    tr \\0 ' ' < /proc/"$(pgrep kubelet)"/cmdline
    ```
    اگر ابزارهای `tr` یا `pgrep` را در اختیار ندارید، خط فرمان فرایند kubelet را
    به‌صورت دستی بررسی کنید.

1.  در خروجی، به دنبال فلگ‌های `--container-runtime` و
    `--container-runtime-endpoint` بگردید.

    *   اگر نودهای شما از کوبرنتیز نسخهٔ v1.23 یا نسخه‌های قدیمی‌تر استفاده می‌کنند و این فلگ‌ها
        وجود ندارند، یا مقدار فلگ `--container-runtime` برابر `remote` نیست،
        از سوکت dockershim همراه با Docker Engine استفاده می‌کنید. آرگومان خط فرمان
        `--container-runtime` در کوبرنتیز نسخهٔ v1.27 و نسخه‌های بعدی در دسترس نیست.
    *   اگر فلگ `--container-runtime-endpoint` وجود دارد، نام سوکت را بررسی کنید
        تا بفهمید از کدام محیط اجرا استفاده می‌کنید. برای نمونه،
        `unix:///run/containerd/containerd.sock` نقطهٔ پایانی containerd است.

اگر می‌خواهید محیط اجرای کانتینر یک نود را از Docker Engine به containerd تغییر دهید،
اطلاعات بیشتر را در [مهاجرت از Docker Engine به containerd](/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/)
بیابید. اگر هم می‌خواهید در کوبرنتیز نسخهٔ v1.24 و نسخه‌های بعدی همچنان از Docker Engine
استفاده کنید، به یک آداپتور سازگار با CRI مانند [`cri-dockerd`](https://github.com/Mirantis/cri-dockerd) مهاجرت کنید.

---
title: اشتراک فضای نام پردازه بین کانتینرهای یک Pod
reviewers:
- verb
- yujuhong
- dchen1107
content_type: task
weight: 200
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه اشتراک فضای نام پردازه (process namespace) را برای یک Pod پیکربندی کنید. وقتی اشتراک فضای نام پردازه فعال باشد، پردازه‌های هر کانتینر برای همهٔ کانتینرهای دیگرِ همان Pod قابل مشاهده هستند.

با این قابلیت می‌توانید کانتینرهایی را پیکربندی کنید که با یکدیگر همکاری می‌کنند، مانند یک کانتینر کناری (sidecar) برای مدیریت لاگ‌ها. همچنین می‌توانید از آن برای عیب‌یابی ایمیج‌های کانتینری استفاده کنید که ابزارهای اشکال‌زدایی مانند شل (shell) را ندارند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## پیکربندی یک Pod

اشتراک فضای نام پردازه با فیلد `shareProcessNamespace` در بخش `.spec` یک Pod فعال می‌شود. برای مثال:

{{% code_sample file="pods/share-process-namespace.yaml" %}}

1. پاد `nginx` را در کلاستر خود ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/share-process-namespace.yaml
   ```

1. به کانتینر `shell` متصل شوید و دستور `ps` را اجرا کنید:

   ```shell
   kubectl exec -it nginx -c shell -- /bin/sh
   ```

   اگر خط فرمان را نمی‌بینید، کلید Enter را فشار دهید. در شل کانتینر دستور زیر را اجرا کنید:

   ```shell
   # run this inside the "shell" container
   ps ax
   ```

   خروجی مشابه زیر است:

   ```none
   PID   USER     TIME  COMMAND
       1 root      0:00 /pause
       8 root      0:00 nginx: master process nginx -g daemon off;
      14 101       0:00 nginx: worker process
      15 root      0:00 sh
      21 root      0:00 ps ax
   ```

می‌توانید به پردازه‌های کانتینرهای دیگر سیگنال بفرستید. برای مثال، با فرستادن سیگنال `SIGHUP` به `nginx`، پردازهٔ worker آن را دوباره راه‌اندازی کنید. این کار به قابلیت `SYS_PTRACE` نیاز دارد.

```shell
# run this inside the "shell" container
kill -HUP 8   # change "8" to match the PID of the nginx leader process, if necessary
ps ax
```

خروجی مشابه زیر است:

```none
PID   USER     TIME  COMMAND
    1 root      0:00 /pause
    8 root      0:00 nginx: master process nginx -g daemon off;
   15 root      0:00 sh
   22 101       0:00 nginx: worker process
   23 root      0:00 ps ax
```

حتی می‌توان با استفاده از پیوند `/proc/$pid/root` به سیستم فایل کانتینری دیگر دسترسی داشت.

```shell
# run this inside the "shell" container
# change "8" to the PID of the Nginx process, if necessary
head /proc/8/root/etc/nginx/nginx.conf
```

خروجی مشابه زیر است:

```none
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
```

<!-- discussion -->

## آشنایی با اشتراک فضای نام پردازه

پادها منابع زیادی را با هم به اشتراک می‌گذارند، پس منطقی است که فضای نام پردازه را نیز به اشتراک بگذارند. با این حال، برخی کانتینرها انتظار دارند از کانتینرهای دیگر جدا باشند؛ بنابراین درک تفاوت‌های زیر اهمیت دارد:

1. **پردازهٔ کانتینر دیگر شناسهٔ پردازهٔ ۱ (PID 1) را ندارد.** برخی کانتینرها بدون PID 1 راه‌اندازی نمی‌شوند (برای مثال، کانتینرهایی که از `systemd` استفاده می‌کنند) یا برای فرستادن سیگنال به پردازهٔ کانتینر، دستورهایی مانند `kill -HUP 1` را اجرا می‌کنند. در پادهایی که فضای نام پردازهٔ مشترک دارند، دستور `kill -HUP 1` به محیط ایزولهٔ (sandbox) پاد سیگنال می‌فرستد (در مثال بالا، `/pause`).

1. **پردازه‌ها برای کانتینرهای دیگرِ پاد قابل مشاهده هستند.** این موضوع شامل همهٔ اطلاعاتی است که در `/proc` دیده می‌شود، مانند گذرواژه‌هایی که به‌صورت آرگومان یا متغیر محیطی ارسال شده‌اند. این اطلاعات فقط با مجوزهای معمول یونیکس محافظت می‌شوند.

1. **سیستم فایل هر کانتینر از طریق پیوند `/proc/$pid/root` برای کانتینرهای دیگرِ پاد قابل مشاهده است.** این ویژگی اشکال‌زدایی را آسان‌تر می‌کند، اما به این معناست که اطلاعات محرمانهٔ موجود در سیستم فایل فقط با مجوزهای سیستم فایل محافظت می‌شوند.

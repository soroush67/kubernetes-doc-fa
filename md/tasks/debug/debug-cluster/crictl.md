---
reviewers:
- Random-Liu
- feiskyer
- mrunalp
title: اشکال‌زدایی نودهای کوبرنتیز با crictl
content_type: task
weight: 30
---


<!-- overview -->

{{< feature-state for_k8s_version="v1.11" state="stable" >}}

ابزار `crictl` یک رابط خط فرمان برای محیط‌های اجرای کانتینر سازگار با CRI است. با این ابزار می‌توانید محیط‌های اجرای کانتینر و برنامه‌های روی یک نود کوبرنتیز را بررسی و اشکال‌زدایی کنید. ابزار `crictl` و کد منبع آن در مخزن [cri-tools](https://github.com/kubernetes-sigs/cri-tools) نگهداری می‌شوند.

## {{% heading "prerequisites" %}}

ابزار `crictl` به یک سیستم‌عامل لینوکس با یک محیط اجرای CRI نیاز دارد.

<!-- steps -->

## نصب crictl

می‌توانید بایگانی فشرده‌ی `crictl` را برای چندین معماری مختلف از [صفحه‌ی انتشارها](https://github.com/kubernetes-sigs/cri-tools/releases)ی cri-tools دانلود کنید. نسخه‌ای را دانلود کنید که با نسخه‌ی کوبرنتیز شما مطابقت دارد. سپس آن را از حالت فشرده خارج کنید و به مسیری در مسیرهای سیستمی خود، مانند `/usr/local/bin/`، منتقل کنید.

## کاربرد عمومی

فرمان `crictl` چندین زیرفرمان و فلگ زمان اجرا دارد. برای جزئیات بیشتر از `crictl help` یا `crictl <subcommand> help` استفاده کنید.

برای تنظیم نقطه‌ی پایانی (endpoint) `crictl` می‌توانید یکی از کارهای زیر را انجام دهید:

* فلگ‌های `--runtime-endpoint` و `--image-endpoint` را تنظیم کنید.
* متغیرهای محیطی `CONTAINER_RUNTIME_ENDPOINT` و `IMAGE_SERVICE_ENDPOINT` را تنظیم کنید.
* نقطه‌ی پایانی را در فایل پیکربندی `/etc/crictl.yaml` تنظیم کنید. برای مشخص کردن فایلی دیگر، هنگام اجرای `crictl` از فلگ `--config=PATH_TO_FILE` استفاده کنید.

{{<note>}}
اگر نقطه‌ی پایانی را تنظیم نکنید، `crictl` تلاش می‌کند به فهرستی از نقطه‌های پایانی شناخته‌شده متصل شود که ممکن است بر کارایی اثر بگذارد.
{{</note>}}

همچنین می‌توانید با مشخص کردن مقادیر `timeout` یا `debug` در فایل پیکربندی، یا با استفاده از فلگ‌های خط فرمان `--timeout` و `--debug`، مقدار مهلت زمانی اتصال به سرور را تعیین کنید و اشکال‌زدایی را فعال یا غیرفعال کنید.

برای مشاهده یا ویرایش پیکربندی فعلی، محتوای `/etc/crictl.yaml` را مشاهده یا ویرایش کنید. برای نمونه، پیکربندی هنگام استفاده از محیط اجرای کانتینر `containerd` مشابه زیر است:

```
runtime-endpoint: unix:///var/run/containerd/containerd.sock
image-endpoint: unix:///var/run/containerd/containerd.sock
timeout: 10
debug: true
```

برای آشنایی بیشتر با `crictl`، به [مستندات `crictl`](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md) مراجعه کنید.

## نمونه‌هایی از فرمان‌های crictl

نمونه‌های زیر برخی از فرمان‌های `crictl` و خروجی نمونه‌ی آن‌ها را نشان می‌دهند.

### فهرست کردن پادها

فهرست همه‌ی پادها:

```shell
crictl pods
```

خروجی مشابه زیر است:

```
POD ID              CREATED              STATE               NAME                         NAMESPACE           ATTEMPT
926f1b5a1d33a       About a minute ago   Ready               sh-84d7dcf559-4r2gq          default             0
4dccb216c4adb       About a minute ago   Ready               nginx-65899c769f-wv2gp       default             0
a86316e96fa89       17 hours ago         Ready               kube-proxy-gblk4             kube-system         0
919630b8f81f1       17 hours ago         Ready               nvidia-device-plugin-zgbbv   kube-system         0
```

فهرست پادها بر اساس نام:

```shell
crictl pods --name nginx-65899c769f-wv2gp
```

خروجی مشابه زیر است:

```
POD ID              CREATED             STATE               NAME                     NAMESPACE           ATTEMPT
4dccb216c4adb       2 minutes ago       Ready               nginx-65899c769f-wv2gp   default             0
```

فهرست پادها بر اساس برچسب:

```shell
crictl pods --label run=nginx
```

خروجی مشابه زیر است:

```
POD ID              CREATED             STATE               NAME                     NAMESPACE           ATTEMPT
4dccb216c4adb       2 minutes ago       Ready               nginx-65899c769f-wv2gp   default             0
```

### فهرست کردن ایمیج‌ها

فهرست همه‌ی ایمیج‌ها:

```shell
crictl images
```

خروجی مشابه زیر است:

```
IMAGE                                     TAG                 IMAGE ID            SIZE
busybox                                   latest              8c811b4aec35f       1.15MB
k8s-gcrio.azureedge.net/hyperkube-amd64   v1.10.3             e179bbfe5d238       665MB
k8s-gcrio.azureedge.net/pause-amd64       3.1                 da86e6ba6ca19       742kB
nginx                                     latest              cd5239a0906a6       109MB
```

فهرست ایمیج‌ها بر اساس مخزن:

```shell
crictl images nginx
```

خروجی مشابه زیر است:

```
IMAGE               TAG                 IMAGE ID            SIZE
nginx               latest              cd5239a0906a6       109MB
```

فهرست کردن فقط شناسه‌های ایمیج:

```shell
crictl images -q
```

خروجی مشابه زیر است:

```
sha256:8c811b4aec35f259572d0f79207bc0678df4c736eeec50bc9fec37ed936a472a
sha256:e179bbfe5d238de6069f3b03fccbecc3fb4f2019af741bfff1233c4d7b2970c5
sha256:da86e6ba6ca197bf6bc5e9d900febd906b133eaa4750e6bed647b0fbe50ed43e
sha256:cd5239a0906a6ccf0562354852fae04bc5b52d72a2aff9a871ddb6bd57553569
```

### فهرست کردن کانتینرها

فهرست همه‌ی کانتینرها:

```shell
crictl ps -a
```

خروجی مشابه زیر است:

```
CONTAINER ID        IMAGE                                                                                                             CREATED             STATE               NAME                       ATTEMPT
1f73f2d81bf98       busybox@sha256:141c253bc4c3fd0a201d32dc1f493bcf3fff003b6df416dea4f41046e0f37d47                                   7 minutes ago       Running             sh                         1
9c5951df22c78       busybox@sha256:141c253bc4c3fd0a201d32dc1f493bcf3fff003b6df416dea4f41046e0f37d47                                   8 minutes ago       Exited              sh                         0
87d3992f84f74       nginx@sha256:d0a8828cccb73397acb0073bf34f4d7d8aa315263f1e7806bf8c55d8ac139d5f                                     8 minutes ago       Running             nginx                      0
1941fb4da154f       k8s-gcrio.azureedge.net/hyperkube-amd64@sha256:00d814b1f7763f4ab5be80c58e98140dfc69df107f253d7fdd714b30a714260a   18 hours ago        Running             kube-proxy                 0
```

فهرست کانتینرهای در حال اجرا:

```shell
crictl ps
```

خروجی مشابه زیر است:

```
CONTAINER ID        IMAGE                                                                                                             CREATED             STATE               NAME                       ATTEMPT
1f73f2d81bf98       busybox@sha256:141c253bc4c3fd0a201d32dc1f493bcf3fff003b6df416dea4f41046e0f37d47                                   6 minutes ago       Running             sh                         1
87d3992f84f74       nginx@sha256:d0a8828cccb73397acb0073bf34f4d7d8aa315263f1e7806bf8c55d8ac139d5f                                     7 minutes ago       Running             nginx                      0
1941fb4da154f       k8s-gcrio.azureedge.net/hyperkube-amd64@sha256:00d814b1f7763f4ab5be80c58e98140dfc69df107f253d7fdd714b30a714260a   17 hours ago        Running             kube-proxy                 0
```

### اجرای یک فرمان در کانتینر در حال اجرا

```shell
crictl exec -i -t 1f73f2d81bf98 ls
```

خروجی مشابه زیر است:

```
bin   dev   etc   home  proc  root  sys   tmp   usr   var
```

### دریافت لاگ‌های یک کانتینر

دریافت همه‌ی لاگ‌های کانتینر:

```shell
crictl logs 87d3992f84f74
```

خروجی مشابه زیر است:

```
10.240.0.96 - - [06/Jun/2018:02:45:49 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.96 - - [06/Jun/2018:02:45:50 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.96 - - [06/Jun/2018:02:45:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
```

دریافت فقط `N` خط آخر لاگ‌ها:

```shell
crictl logs --tail=1 87d3992f84f74
```

خروجی مشابه زیر است:

```
10.240.0.96 - - [06/Jun/2018:02:45:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
```

## {{% heading "whatsnext" %}}

* [درباره‌ی `crictl` بیشتر بدانید](https://github.com/kubernetes-sigs/cri-tools).

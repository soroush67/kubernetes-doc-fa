---
title: اجرای Pod‌ها فقط روی برخی از نودها
content_type: task
weight: 30
---
<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید {{<glossary_tooltip term_id="pod" text="Pod‌ها">}} را به‌عنوان بخشی از یک {{<glossary_tooltip term_id="daemonset" text="DaemonSet">}} فقط روی برخی از {{<glossary_tooltip term_id="node" text="نودها">}} اجرا کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

## اجرای Pod‌ها فقط روی برخی از نودها

فرض کنید می‌خواهید یک {{<glossary_tooltip term_id="daemonset" text="DaemonSet">}} اجرا کنید، اما لازم است Pod‌های daemon آن فقط روی نودهایی اجرا شوند که ذخیره‌سازی محلی حالت جامد (SSD) دارند. برای مثال، ممکن است این Pod سرویس کش را برای نود فراهم کند و این کش فقط زمانی سودمند باشد که ذخیره‌سازی محلی با تأخیر کم در دسترس باشد.

### گام ۱: افزودن برچسب به نودها

برچسب `ssd=true` را به نودهایی که SSD دارند اضافه کنید.

```shell
kubectl label nodes example-node-1 example-node-2 ssd=true
```

### گام ۲: ایجاد مانیفست

اکنون یک {{<glossary_tooltip term_id="daemonset" text="DaemonSet">}} ایجاد می‌کنیم که Pod‌های daemon را فقط روی {{<glossary_tooltip term_id="node" text="نودهایی">}} که برچسب SSD دارند مستقر می‌کند.


سپس با استفاده از یک `nodeSelector` اطمینان حاصل کنید که DaemonSet فقط روی نودهایی Pod اجرا می‌کند که مقدار برچسب `ssd` در آن‌ها برابر `"true"` است.

{{% code_sample file="controllers/daemonset-label-selector.yaml" %}}

### گام ۳: ایجاد DaemonSet

با استفاده از `kubectl create` یا `kubectl apply`، آبجکت DaemonSet را از روی مانیفست ایجاد کنید.

اکنون یک نود دیگر را با `ssd=true` برچسب‌گذاری می‌کنیم.

```shell
kubectl label nodes example-node-3 ssd=true
```

برچسب‌گذاری نود به‌طور خودکار باعث می‌شود control plane (به‌طور مشخص، کنترل‌کننده DaemonSet) یک Pod daemon جدید روی آن نود اجرا کند.

```shell
kubectl get pods -o wide
```
خروجی مشابه زیر است:

```
NAME                              READY     STATUS    RESTARTS   AGE    IP      NODE
<daemonset-name><some-hash-01>    1/1       Running   0          13s    .....   example-node-1
<daemonset-name><some-hash-02>    1/1       Running   0          13s    .....   example-node-2
<daemonset-name><some-hash-03>    1/1       Running   0          5s     .....   example-node-3
```

---
title: پیکربندی مقداردهی اولیهٔ Pod
content_type: task
weight: 170
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از یک کانتینر init (Init Container)، پیش از اجرای کانتینر برنامه، یک Pod را مقداردهی اولیه کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## ایجاد یک Pod دارای کانتینر init

در این تمرین، یک Pod می‌سازید که یک کانتینر برنامه و یک کانتینر init دارد. کانتینر init پیش از شروع کانتینر برنامه اجرا می‌شود و تا پایان کارش ادامه می‌یابد.

فایل پیکربندی این Pod به شرح زیر است:

{{% code_sample file="pods/init-containers.yaml" %}}

در فایل پیکربندی می‌بینید که Pod یک حجم (volume) دارد که کانتینر init و کانتینر برنامه آن را به‌طور مشترک استفاده می‌کنند.

کانتینر init حجم مشترک را در مسیر `/work-dir` و کانتینر برنامه همان حجم را در مسیر `/usr/share/nginx/html` سوار (mount) می‌کند. کانتینر init فرمان زیر را اجرا می‌کند و سپس خاتمه می‌یابد:

```shell
wget -O /work-dir/index.html http://info.cern.ch
```

توجه کنید که کانتینر init فایل `index.html` را در دایرکتوری ریشهٔ سرور nginx می‌نویسد.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/init-containers.yaml
```

بررسی کنید که کانتینر nginx در حال اجرا باشد:

```shell
kubectl get pod init-demo
```

خروجی نشان می‌دهد که کانتینر nginx در حال اجرا است:

```
NAME        READY     STATUS    RESTARTS   AGE
init-demo   1/1       Running   0          1m
```

یک پوستهٔ (shell) تعاملی در کانتینر nginx که در Pod به نام init-demo اجرا می‌شود باز کنید:

```shell
kubectl exec -it init-demo -- /bin/bash
```

در این پوسته، یک درخواست GET به سرور nginx بفرستید:

```
root@nginx:~# apt-get update
root@nginx:~# apt-get install curl
root@nginx:~# curl localhost
```

خروجی نشان می‌دهد که nginx همان صفحهٔ وبی را ارائه می‌کند که کانتینر init نوشته است:

```html
<html><head></head><body><header>
<title>http://info.cern.ch</title>
</header>

<h1>http://info.cern.ch - home of the first website</h1>
  ...
  <li><a href="http://info.cern.ch/hypertext/WWW/TheProject.html">Browse the first website</a></li>
  ...
```

## {{% heading "whatsnext" %}}

* دربارهٔ
  [ارتباط میان کانتینرهایی که در یک Pod اجرا می‌شوند](/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/) بیشتر بیاموزید.
* دربارهٔ [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/) بیشتر بیاموزید.
* دربارهٔ [حجم‌ها](/docs/concepts/storage/volumes/) بیشتر بیاموزید.
* دربارهٔ [اشکال‌زدایی کانتینرهای init](/docs/tasks/debug/debug-application/debug-init-containers/) بیشتر بیاموزید.

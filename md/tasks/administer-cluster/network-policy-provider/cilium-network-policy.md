---
reviewers:
- danwent
- aanm
title: استفاده از Cilium برای NetworkPolicy
content_type: task
weight: 30
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان از Cilium برای NetworkPolicy استفاده کرد.

برای آشنایی با پیش‌زمینهٔ Cilium، [مقدمه‌ای بر Cilium](https://docs.cilium.io/en/stable/overview/intro) را بخوانید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## استقرار Cilium روی Minikube برای آزمایش‌های پایه

برای آشنایی آسان با Cilium می‌توانید از
[راهنمای شروع به کار Cilium در کوبرنتیز](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/)
پیروی کنید و یک نصب پایهٔ Cilium به‌صورت DaemonSet را در minikube انجام دهید.

برای راه‌اندازی minikube، که به نسخهٔ v1.5.2 یا بالاتر نیاز دارد، آن را با
آرگومان‌های زیر اجرا کنید:

```shell
minikube version
```

```
minikube version: v1.5.2
```

```shell
minikube start --network-plugin=cni
```

در minikube می‌توانید Cilium را با ابزار خط فرمان (CLI) آن نصب کنید. برای این کار، ابتدا آخرین
نسخهٔ این ابزار را با فرمان زیر دانلود کنید:

```shell
curl -LO https://github.com/cilium/cilium-cli/releases/latest/download/cilium-linux-amd64.tar.gz
```

سپس فایل دانلودشده را با فرمان زیر در پوشهٔ `/usr/local/bin` استخراج کنید:

```shell
sudo tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin
rm cilium-linux-amd64.tar.gz
```

پس از اجرای فرمان‌های بالا، اکنون می‌توانید Cilium را با فرمان زیر نصب کنید:

```shell
cilium install
```

در ادامه، Cilium پیکربندی کلاستر را به‌طور خودکار تشخیص می‌دهد و مؤلفه‌های مناسب را
برای یک نصب موفق ایجاد و نصب می‌کند.
این مؤلفه‌ها عبارت‌اند از:

- مرجع صدور گواهی (Certificate Authority یا CA) در Secret `cilium-ca` و گواهی‌های مربوط به Hubble (لایهٔ مشاهده‌پذیری Cilium).
- حساب‌های سرویس (Service account).
- نقش‌های کلاستر (Cluster role).
- ConfigMap.
- یک DaemonSet برای عامل (Agent) و یک Deployment برای اپراتور (Operator).

پس از نصب، می‌توانید وضعیت کلی استقرار Cilium را با فرمان `cilium status` مشاهده کنید.
خروجی مورد انتظار فرمان `status` را
[اینجا](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/#validate-the-installation) ببینید.

بخش‌های باقی‌ماندهٔ راهنمای شروع به کار، با استفاده از یک برنامهٔ نمونه توضیح می‌دهد که چگونه
هم سیاست‌های امنیتی لایهٔ L3/L4 (یعنی نشانی IP و پورت) و هم سیاست‌های امنیتی لایهٔ L7
(برای نمونه HTTP) را اعمال کنید.

## استقرار Cilium برای محیط عملیاتی

برای دستورالعمل‌های مفصل دربارهٔ استقرار Cilium در محیط عملیاتی، به
[راهنمای نصب Cilium در کوبرنتیز](https://docs.cilium.io/en/stable/network/kubernetes/concepts/)
مراجعه کنید. این مستندات شامل الزامات و دستورالعمل‌های مفصل و نمونه‌فایل‌های
DaemonSet برای محیط عملیاتی است.

<!-- discussion -->

##  آشنایی با مؤلفه‌های Cilium

با استقرار یک کلاستر همراه با Cilium، تعدادی Pod به فضای نام (namespace) `kube-system` افزوده می‌شود. برای دیدن
فهرست این Podها فرمان زیر را اجرا کنید:

```shell
kubectl get pods --namespace=kube-system -l k8s-app=cilium
```

فهرستی از Podها مشابه نمونهٔ زیر خواهید دید:

```console
NAME           READY   STATUS    RESTARTS   AGE
cilium-kkdhz   1/1     Running   0          3m23s
...
```

روی هر نود از کلاستر شما یک Pod به نام `cilium` اجرا می‌شود که با استفاده از Linux BPF،
سیاست شبکه را بر ترافیک ورودی و خروجی Podهای آن نود اعمال می‌کند.

## {{% heading "whatsnext" %}}

پس از راه‌اندازی کلاستر، می‌توانید با دنبال کردن
[تعریف سیاست شبکه](/docs/tasks/administer-cluster/declare-network-policy/)،
NetworkPolicy کوبرنتیز را همراه با Cilium امتحان کنید.
از کار با آن لذت ببرید و اگر پرسشی داشتید، از طریق
[کانال Slack مربوط به Cilium](https://slack.cilium.io/) با ما در تماس باشید.

---
title: "بررسی نصب kubectl"
description: "چگونه نصب kubectl را بررسی کنیم."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

ابزار kubectl برای یافتن یک کلاستر کوبرنتیز و دسترسی به آن به یک
[فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
نیاز دارد. این فایل هنگام ایجاد کلاستر با
[kube-up.sh](https://github.com/kubernetes/kubernetes/blob/master/cluster/kube-up.sh)
یا پس از استقرار موفق یک کلاستر Minikube به‌طور خودکار ساخته می‌شود.
پیکربندی kubectl به‌طور پیش‌فرض در مسیر `~/.kube/config` قرار دارد.

با دریافت وضعیت کلاستر، بررسی کنید که kubectl به‌درستی پیکربندی شده باشد:

```shell
kubectl cluster-info
```

اگر در پاسخ یک URL مشاهده کردید، kubectl برای دسترسی به کلاستر شما به‌درستی پیکربندی شده است.

اگر پیامی مشابه پیام زیر مشاهده کردید، kubectl به‌درستی پیکربندی نشده است
یا نمی‌تواند به کلاستر کوبرنتیز متصل شود.

```
The connection to the server <server-name:port> was refused - did you specify the right host or port?
```

برای مثال، اگر قصد دارید یک کلاستر کوبرنتیز را روی لپ‌تاپ خود (به‌صورت محلی) اجرا کنید،
ابتدا باید ابزاری مانند [Minikube](https://minikube.sigs.k8s.io/docs/start/) را نصب کنید
و سپس دستورهای بالا را دوباره اجرا کنید.

اگر دستور `kubectl cluster-info` پاسخی حاوی URL برمی‌گرداند اما نمی‌توانید به کلاستر خود دسترسی پیدا کنید،
با دستور زیر بررسی کنید که کلاستر به‌درستی پیکربندی شده باشد:

```shell
kubectl cluster-info dump
```

### عیب‌یابی پیام خطای 'No Auth Provider Found' {#no-auth-provider-found}

در کوبرنتیز نسخهٔ 1.26، سازوکار احراز هویت داخلی kubectl برای سرویس‌های کوبرنتیز مدیریت‌شدهٔ
ارائه‌دهندگان ابری زیر حذف شد. این ارائه‌دهندگان افزونه‌هایی (plugin) برای kubectl منتشر کرده‌اند
که احراز هویت مخصوص هر ابر را فراهم می‌کنند. برای دستورالعمل‌ها، به مستندات ارائه‌دهندهٔ مربوط مراجعه کنید:

* Azure AKS: [افزونهٔ kubelogin](https://azure.github.io/kubelogin/)
* Google Kubernetes Engine: [gke-gcloud-auth-plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin)

همین پیام خطا ممکن است دلایل دیگری نیز داشته باشد که به این تغییر
ارتباطی ندارند.

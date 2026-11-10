---
reviewers:
- caseydavenport
- danwinship
title: اعلان سیاست شبکه
min-kubernetes-server-version: v1.8
content_type: task
weight: 180
---
<!-- overview -->
این سند به شما کمک می‌کند تا کار با [API مربوط به NetworkPolicy](/docs/concepts/services-networking/network-policies/) در کوبرنتیز را آغاز کنید و سیاست‌های شبکه‌ای را اعلان کنید که نحوهٔ ارتباط پادها با یکدیگر را کنترل می‌کنند.

{{% thirdparty-content %}}

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

مطمئن شوید که یک ارائه‌دهندهٔ شبکه (network provider) با پشتیبانی از سیاست شبکه پیکربندی کرده‌اید. ارائه‌دهندگان شبکهٔ متعددی از NetworkPolicy پشتیبانی می‌کنند، از جمله:

* [Antrea](/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/)
* [Calico](/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
* [Cilium](/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
* [Kube-router](/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)

<!-- steps -->

## ایجاد یک Deployment برای `nginx` و در دسترس قرار دادن آن از طریق یک Service

برای مشاهدهٔ نحوهٔ عملکرد سیاست شبکه در کوبرنتیز، ابتدا یک Deployment برای `nginx` ایجاد کنید.

```console
kubectl create deployment nginx --image=nginx
```
```none
deployment.apps/nginx created
```

این Deployment را از طریق یک Service با نام `nginx` در دسترس قرار دهید.

```console
kubectl expose deployment nginx --port=80
```

```none
service/nginx exposed
```

دستورهای بالا یک Deployment با یک Pod از nginx ایجاد می‌کنند و این Deployment را از طریق یک Service با نام `nginx` در دسترس قرار می‌دهند. Pod و Deployment مربوط به `nginx` در فضای نام (namespace) `default` قرار دارند.

```console
kubectl get svc,pod
```

```none
NAME                        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/kubernetes          10.100.0.1    <none>        443/TCP    46m
service/nginx               10.100.0.16   <none>        80/TCP     33s

NAME                        READY         STATUS        RESTARTS   AGE
pod/nginx-701339712-e0qfq   1/1           Running       0          35s
```

## آزمایش سرویس با دسترسی به آن از یک Pod دیگر

باید بتوانید از Podهای دیگر به سرویس جدید `nginx` دسترسی داشته باشید. برای دسترسی به Service `nginx` از یک Pod دیگر در فضای نام `default`، یک کانتینر busybox اجرا کنید:

```console
kubectl run busybox --rm -ti --image=busybox -- /bin/sh
```

در پوستهٔ (shell) خود، دستور زیر را اجرا کنید:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
remote file exists
```

## محدود کردن دسترسی به سرویس `nginx`

برای محدود کردن دسترسی به سرویس `nginx`، به‌طوری که فقط Podهای دارای برچسب `access: true` بتوانند به آن درخواست بفرستند، یک آبجکت NetworkPolicy به شکل زیر ایجاد کنید:

{{% code_sample file="service/networking/nginx-policy.yaml" %}}

نام هر آبجکت NetworkPolicy باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

{{< note >}}
هر NetworkPolicy یک `podSelector` دارد که گروهی از Podها را انتخاب می‌کند که سیاست بر آن‌ها اعمال می‌شود. همان‌طور که می‌بینید، این سیاست Podهای دارای برچسب `app=nginx` را انتخاب می‌کند. این برچسب به‌طور خودکار به Pod موجود در Deployment `nginx` افزوده شده است. یک `podSelector` خالی همهٔ پادهای موجود در فضای نام را انتخاب می‌کند.
{{< /note >}}

## اختصاص سیاست به سرویس

با استفاده از kubectl، یک NetworkPolicy از فایل `nginx-policy.yaml` بالا ایجاد کنید:

```console
kubectl apply -f https://k8s.io/examples/service/networking/nginx-policy.yaml
```

```none
networkpolicy.networking.k8s.io/access-nginx created
```

## آزمایش دسترسی به سرویس در حالتی که برچسب دسترسی تعریف نشده است
وقتی تلاش می‌کنید از یک Pod فاقد برچسب‌های درست به Service `nginx` دسترسی پیدا کنید، مهلت درخواست به پایان می‌رسد:

```console
kubectl run busybox --rm -ti --image=busybox -- /bin/sh
```

در پوستهٔ خود، این دستور را اجرا کنید:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
wget: download timed out
```

## تعریف برچسب دسترسی و آزمایش دوباره

می‌توانید یک Pod با برچسب‌های درست ایجاد کنید تا ببینید که درخواست مجاز شمرده می‌شود:

```console
kubectl run busybox --rm -ti --labels="access=true" --image=busybox -- /bin/sh
```

در پوستهٔ خود، این دستور را اجرا کنید:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
remote file exists
```

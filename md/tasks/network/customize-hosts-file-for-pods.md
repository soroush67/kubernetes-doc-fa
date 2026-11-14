---
reviewers:
- rickypai
- thockin
title: افزودن ورودی به فایل /etc/hosts پاد با HostAliases
content_type: task
weight: 60
min-kubernetes-server-version: 1.7
---


<!-- overview -->

هنگامی که DNS و گزینه‌های دیگر کارساز نیستند، می‌توان با افزودن ورودی به فایل `/etc/hosts` یک Pod، تفکیک نام میزبان (hostname resolution) را در سطح Pod بازنویسی کرد. این ورودی‌های سفارشی را می‌توانید با فیلد HostAliases در PodSpec اضافه کنید.

پروژهٔ کوبرنتیز توصیه می‌کند پیکربندی DNS را با فیلد `hostAliases` (که بخشی از `.spec` یک Pod است) تغییر دهید، نه با استفاده از یک init container یا روش‌های دیگری که `/etc/hosts` را مستقیماً ویرایش می‌کنند.
ممکن است kubelet تغییراتی را که به روش‌های دیگر اعمال شده‌اند، هنگام ایجاد یا راه‌اندازی مجدد Pod بازنویسی کند.

<!-- steps -->

## محتوای پیش‌فرض فایل hosts

یک Pod مبتنی بر Nginx اجرا کنید که یک IP پاد به آن اختصاص داده می‌شود:

```shell
kubectl run nginx --image nginx
```

```
pod/nginx created
```

آدرس IP پاد را بررسی کنید:

```shell
kubectl get pods --output=wide
```

```
NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
nginx    1/1       Running   0          13s    10.200.0.4   worker0
```

محتوای فایل hosts به این شکل خواهد بود:

```shell
kubectl exec nginx -- cat /etc/hosts
```

```
# Kubernetes-managed hosts file.
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
fe00::0	ip6-mcastprefix
fe00::1	ip6-allnodes
fe00::2	ip6-allrouters
10.200.0.4	nginx
```

به‌طور پیش‌فرض، فایل `hosts` فقط شامل ورودی‌های استاندارد IPv4 و IPv6، مانند `localhost` و نام میزبان خود Pod است.

## افزودن ورودی‌های بیشتر با hostAliases

علاوه بر ورودی‌های استاندارد پیش‌فرض، می‌توانید ورودی‌های دیگری نیز به فایل `hosts` اضافه کنید.
برای مثال، برای اینکه `foo.local` و `bar.local` به `127.0.0.1` و `foo.remote` و `bar.remote` به `10.1.2.3` تفکیک شوند، می‌توانید HostAliases را برای یک Pod در `.spec.hostAliases` پیکربندی کنید:

{{% code_sample file="service/networking/hostaliases-pod.yaml" %}}

برای اجرای یک Pod با این پیکربندی، دستور زیر را اجرا کنید:

```shell
kubectl apply -f https://k8s.io/examples/service/networking/hostaliases-pod.yaml
```

```
pod/hostaliases-pod created
```

جزئیات Pod را بررسی کنید تا آدرس IPv4 و وضعیت آن را ببینید:

```shell
kubectl get pod --output=wide
```

```
NAME                           READY     STATUS      RESTARTS   AGE       IP              NODE
hostaliases-pod                0/1       Completed   0          6s        10.200.0.5      worker0
```

محتوای فایل `hosts` به این شکل است:

```shell
kubectl logs hostaliases-pod
```

```
# Kubernetes-managed hosts file.
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
fe00::0	ip6-mcastprefix
fe00::1	ip6-allnodes
fe00::2	ip6-allrouters
10.200.0.5	hostaliases-pod

# Entries added by HostAliases.
127.0.0.1	foo.local	bar.local
10.1.2.3	foo.remote	bar.remote
```

همان‌طور که می‌بینید، ورودی‌های اضافه‌شده در انتهای فایل قرار گرفته‌اند.

## چرا kubelet فایل hosts را مدیریت می‌کند؟ {#why-does-kubelet-manage-the-hosts-file}

kubelet فایل `hosts` را برای هر کانتینر Pod مدیریت می‌کند تا محیط اجرای کانتینر (container runtime) نتواند پس از راه‌اندازی کانتینرها این فایل را تغییر دهد.
در گذشته، کوبرنتیز همیشه از Docker Engine به‌عنوان محیط اجرای کانتینر استفاده می‌کرد و Docker Engine پس از راه‌اندازی هر کانتینر، فایل `/etc/hosts` را تغییر می‌داد.

نسخه‌های کنونی کوبرنتیز می‌توانند از محیط‌های اجرای کانتینر گوناگونی استفاده کنند. با این حال، kubelet فایل hosts را درون هر کانتینر مدیریت می‌کند تا صرف‌نظر از محیط اجرای کانتینری که استفاده می‌کنید، نتیجه همان چیزی باشد که انتظار می‌رود.

{{< caution >}}
از اعمال تغییرات دستی در فایل hosts درون کانتینر خودداری کنید.

اگر فایل hosts را به‌صورت دستی تغییر دهید، این تغییرات با خروج کانتینر از بین می‌روند.
{{< /caution >}}

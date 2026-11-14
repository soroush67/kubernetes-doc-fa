---
reviewers:
- jsafrane
title: ایجاد Podهای ایستا
weight: 220
content_type: task
---

<!-- overview -->
 
این صفحه نحوهٔ ایجاد _Podهای ایستا_ (static Pods) را روی یک نود نشان می‌دهد.
برای آشنایی کلی با چیستی Podهای ایستا و موارد استفاده از آن‌ها، به
[Podهای ایستا](/docs/concepts/workloads/pods/static-pods/) مراجعه کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

در این صفحه فرض بر این است که برای اجرای Podها از {{< glossary_tooltip term_id="cri-o" >}} استفاده می‌کنید
و نودهای شما سیستم‌عامل Fedora را اجرا می‌کنند.
دستورالعمل‌ها برای توزیع‌های دیگر یا نصب‌های دیگر کوبرنتیز ممکن است متفاوت باشد.

<!-- steps -->

## ایجاد یک Pod ایستا {#static-pod-creation}

می‌توانید یک Pod ایستا را با یک [فایل پیکربندی میزبانی‌شده در سیستم فایل](#configuration-files)
یا یک [فایل پیکربندی میزبانی‌شده در وب](#pods-created-via-http) پیکربندی کنید.

### مانیفست Pod ایستای میزبانی‌شده در سیستم فایل {#configuration-files}

مانیفست‌ها تعریف‌های استاندارد Pod در قالب JSON یا YAML هستند که در یک دایرکتوری مشخص قرار می‌گیرند.
از فیلد `staticPodPath: <the directory>` در
[فایل پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/) استفاده کنید.
kubelet این دایرکتوری را به‌طور دوره‌ای بررسی می‌کند و با ظاهر یا حذف شدن فایل‌های YAML/JSON در آن، Podهای ایستا را ایجاد یا حذف می‌کند.
توجه کنید که kubelet هنگام بررسی دایرکتوری مشخص‌شده، فایل‌هایی را که با نقطه شروع می‌شوند نادیده می‌گیرد.

{{< caution >}}
kubelet **همهٔ فایل‌هایی را که با نقطه شروع نمی‌شوند** در دایرکتوری Podهای ایستا پردازش می‌کند
و هیچ فیلتری بر اساس پسوند فایل اعمال نمی‌شود. برای مثال، اگر با اجرای
`cp kube-apiserver.yaml kube-apiserver.yaml.backup` از یک مانیفست نسخهٔ پشتیبان بگیرید، kubelet
**هر دو** فایل را می‌خواند و تلاش می‌کند از هر کدام یک Pod ایستا ایجاد کند. وقتی دو فایل
Podی با نام یکسان تعریف کنند، رفتار حاصل تعریف‌نشده است و ممکن است باعث شود مشخصات
قدیمی نسخهٔ پشتیبان، بی‌سروصدا به‌جای مانیفست فعلی اعمال شود. اگر نسخهٔ پشتیبان
می‌گیرید، آن را **بیرون** از دایرکتوری Podهای ایستا نگه دارید (برای مثال، در
`/etc/kubernetes/backup/`).
{{< /caution >}}

برای مثال، روش راه‌اندازی یک وب‌سرور ساده به‌صورت Pod ایستا چنین است:

1. نودی را که می‌خواهید Pod ایستا روی آن اجرا شود انتخاب کنید. در این مثال، این نود `my-node1` است.

   ```shell
   ssh my-node1
   ```

1. یک دایرکتوری، مثلاً `/etc/kubernetes/manifests`، انتخاب کنید و تعریف Pod یک وب‌سرور را
   در آن قرار دهید، برای مثال `/etc/kubernetes/manifests/static-web.yaml`:
 
   ```shell
   # Run this command on the node where kubelet is running
   mkdir -p /etc/kubernetes/manifests/
   cat <<EOF >/etc/kubernetes/manifests/static-web.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   EOF
   ```

1. kubelet را روی آن نود طوری پیکربندی کنید که مقدار `staticPodPath` در
   [فایل پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/) تنظیم شود.  
   برای اطلاعات بیشتر، به [تنظیم پارامترهای Kubelet از طریق فایل پیکربندی](/docs/tasks/administer-cluster/kubelet-config-file/)
   مراجعه کنید.

   روش جایگزین و منسوخ‌شده این است که kubelet روی آن نود را طوری پیکربندی کنید
   که با استفاده از یک آرگومان خط فرمان، مانیفست‌های Pod ایستا را به‌صورت محلی جست‌وجو کند.
   برای استفاده از این روش منسوخ‌شده، kubelet را با آرگومان
   `--pod-manifest-path=/etc/kubernetes/manifests/` اجرا کنید.
   
1. kubelet را دوباره راه‌اندازی کنید. در Fedora باید این دستور را اجرا کنید:

   ```shell
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```

### مانیفست Pod ایستای میزبانی‌شده در وب {#pods-created-via-http}

kubelet به‌طور دوره‌ای فایلی را که با آرگومان `--manifest-url=<URL>` مشخص شده است دانلود می‌کند
و آن را به‌عنوان یک فایل JSON/YAML حاوی تعریف‌های Pod تفسیر می‌کند.
همانند عملکرد [مانیفست‌های میزبانی‌شده در سیستم فایل](#configuration-files)، kubelet
مانیفست را طبق یک زمان‌بندی دوباره دریافت می‌کند. اگر فهرست Podهای ایستا
تغییر کرده باشد، kubelet این تغییرات را اعمال می‌کند.

برای استفاده از این روش:

1. یک فایل YAML ایجاد کنید و آن را روی یک وب‌سرور ذخیره کنید تا بتوانید نشانی URL آن فایل را به kubelet بدهید.

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: static-web
     labels:
       role: myrole
   spec:
     containers:
       - name: web
         image: nginx
         ports:
           - name: web
             containerPort: 80
             protocol: TCP
   ```

1. با به‌روزرسانی فایل پیکربندی kubelet و افزودن فیلد `staticPodURL` به آن،
   kubelet را روی نود انتخابی خود طوری پیکربندی کنید که از این مانیفست وب استفاده کند:

   ```yaml
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   staticPodURL: "<manifest-url>"
   ```

1. kubelet را دوباره راه‌اندازی کنید. در Fedora باید این دستور را اجرا کنید:

   ```shell
   # Run this command on the node where the kubelet is running
   systemctl restart kubelet
   ```

## مشاهدهٔ رفتار Pod ایستا {#behavior-of-static-pods}

هنگامی که kubelet شروع به کار می‌کند، همهٔ Podهای ایستای تعریف‌شده را به‌طور خودکار اجرا می‌کند. از آنجا که
یک Pod ایستا تعریف کرده‌اید و kubelet را دوباره راه‌اندازی کرده‌اید، Pod ایستای جدید باید
اکنون در حال اجرا باشد.

می‌توانید با اجرای دستور زیر (روی نود)، کانتینرهای در حال اجرا (از جمله Podهای ایستا) را مشاهده کنید:
```shell
# Run this command on the node where the kubelet is running
crictl ps
```

خروجی ممکن است چیزی شبیه این باشد:

```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
129fd7d382018   docker.io/library/nginx@sha256:...    11 minutes ago    Running    web     0          34533c6729106
```

{{< note >}}
خروجی `crictl` شامل URI ایمیج و checksum از نوع SHA-256 است. مقدار `NAME` بیشتر به این شکل خواهد بود:
`docker.io/library/nginx@sha256:0d17b565c37bcbd895e9d92315a05c1c3c9a29f762b011a10c54a66cd53c9b31`.
{{< /note >}}

می‌توانید Pod آینه‌ای (mirror Pod) را روی سرور API ببینید:

```shell
kubectl get pods
```
```console
NAME                  READY   STATUS    RESTARTS        AGE
static-web-my-node1   1/1     Running   0               2m
```

{{< note >}}
مطمئن شوید که kubelet مجوز ایجاد Pod آینه‌ای در سرور API را دارد.
در غیر این صورت، سرور API درخواست ایجاد را رد می‌کند.
{{< /note >}}

{{< glossary_tooltip term_id="label" text="برچسب‌های" >}} Pod ایستا به
Pod آینه‌ای منتقل می‌شوند. می‌توانید از این برچسب‌ها به‌طور معمول از طریق
{{< glossary_tooltip term_id="selector" text="انتخابگرها" >}} و موارد مشابه استفاده کنید.

اگر بخواهید با `kubectl` Pod آینه‌ای را از سرور API حذف کنید،
kubelet Pod ایستا را حذف _نمی‌کند_:

```shell
kubectl delete pod static-web-my-node1
```
```console
pod "static-web-my-node1" deleted
```
می‌بینید که Pod همچنان در حال اجراست:
```shell
kubectl get pods
```
```console
NAME                  READY   STATUS    RESTARTS   AGE
static-web-my-node1   1/1     Running   0          4s
```

اکنون به نودی که kubelet روی آن اجرا می‌شود برگردید و کانتینر را به‌صورت دستی متوقف کنید.
خواهید دید که پس از مدتی، kubelet متوجه این موضوع می‌شود و Pod را
به‌طور خودکار دوباره راه‌اندازی می‌کند:

```shell
# Run these commands on the node where the kubelet is running
crictl stop 129fd7d382018 # replace with the ID of your container
sleep 20
crictl ps
```

```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
89db4553e1eeb   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```
پس از شناسایی کانتینر مورد نظر، می‌توانید لاگ‌های آن کانتینر را با `crictl` دریافت کنید:

```shell
# Run these commands on the node where the container is running
crictl logs <container_id>
```

```console
10.240.0.48 - - [16/Nov/2022:12:45:49 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nov/2022:12:45:50 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nove/2022:12:45:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
```

برای آشنایی بیشتر با اشکال‌زدایی به کمک `crictl`، به
[_اشکال‌زدایی نودهای کوبرنتیز با crictl_](/docs/tasks/debug/debug-cluster/crictl/) مراجعه کنید.

## افزودن و حذف پویای Podهای ایستا

kubelet در حال اجرا، دایرکتوری پیکربندی‌شده
(در مثال ما `/etc/kubernetes/manifests`) را به‌طور دوره‌ای برای یافتن تغییرات بررسی می‌کند و
با ظاهر یا حذف شدن فایل‌ها در این دایرکتوری، Podها را اضافه یا حذف می‌کند.

```shell
# This assumes you are using filesystem-hosted static Pod configuration
# Run these commands on the node where the container is running
mv /etc/kubernetes/manifests/static-web.yaml /tmp
sleep 20
crictl ps
# You see that no nginx container is running
mv /tmp/static-web.yaml  /etc/kubernetes/manifests/
sleep 20
crictl ps
```
```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
f427638871c35   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```
## {{% heading "whatsnext" %}}

* [Podهای ایستا](/docs/concepts/workloads/pods/static-pods/)
* [تولید مانیفست‌های Pod ایستا برای مؤلفه‌های control plane](/docs/reference/setup-tools/kubeadm/implementation-details/#generate-static-pod-manifests-for-control-plane-components)
* [تولید مانیفست Pod ایستا برای etcd محلی](/docs/reference/setup-tools/kubeadm/implementation-details/#generate-static-pod-manifest-for-local-etcd)
* [اشکال‌زدایی نودهای کوبرنتیز با `crictl`](/docs/tasks/debug/debug-cluster/crictl/)
* [آشنایی بیشتر با `crictl`](https://github.com/kubernetes-sigs/cri-tools)
* [راه‌اندازی نمونه‌های etcd به‌صورت Podهای ایستای مدیریت‌شده توسط kubelet](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)

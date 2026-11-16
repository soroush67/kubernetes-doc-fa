---
title: پیکربندی یک Pod برای استفاده از PersistentVolume به‌عنوان فضای ذخیره‌سازی
content_type: tutorial
weight: 90
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک Pod را پیکربندی کنید تا از یک
{{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}}
برای ذخیره‌سازی استفاده کند.
خلاصهٔ این فرایند به شرح زیر است:

1. شما در نقش مدیر کلاستر، یک PersistentVolume ایجاد می‌کنید که بر پایهٔ یک
   ذخیره‌ساز فیزیکی است. این حجم (volume) را به هیچ Podی مرتبط نمی‌کنید.

1. سپس در نقش یک توسعه‌دهنده یا کاربر کلاستر، یک PersistentVolumeClaim ایجاد
   می‌کنید که به‌طور خودکار به یک PersistentVolume مناسب متصل (bind) می‌شود.

1. یک Pod ایجاد می‌کنید که از PersistentVolumeClaim بالا برای ذخیره‌سازی استفاده می‌کند.

## {{% heading "prerequisites" %}}

* به یک کلاستر کوبرنتیز نیاز دارید که فقط یک نود داشته باشد، و ابزار خط فرمان
  {{< glossary_tooltip text="kubectl" term_id="kubectl" >}}
  نیز باید برای برقراری ارتباط با کلاستر شما پیکربندی شده باشد. اگر هنوز یک
  کلاستر تک‌نودی ندارید، می‌توانید با استفاده از
  [Minikube](https://minikube.sigs.k8s.io/docs/) یکی ایجاد کنید.

* با مطالب صفحهٔ
  [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) آشنا شوید.

<!-- steps -->

## ایجاد یک فایل index.html روی نود

یک پوسته (shell) روی تنها نود کلاستر خود باز کنید. نحوهٔ باز کردن پوسته به
شیوهٔ راه‌اندازی کلاستر شما بستگی دارد. برای مثال، اگر از Minikube استفاده
می‌کنید، می‌توانید با وارد کردن `minikube ssh` یک پوسته روی نود خود باز کنید.

در پوستهٔ آن نود، دایرکتوری `/mnt/data` را ایجاد کنید:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data
```

در دایرکتوری `/mnt/data` یک فایل `index.html` ایجاد کنید:

```shell
# This again assumes that your Node uses "sudo" to run commands
# as the superuser
sudo sh -c "echo 'Hello from Kubernetes storage' > /mnt/data/index.html"
```

{{< note >}}
اگر نود شما برای دسترسی ابرکاربر (superuser) از ابزاری غیر از `sudo` استفاده
می‌کند، معمولاً با جایگزین کردن `sudo` با نام آن ابزار می‌توانید این دستورها را اجرا کنید.
{{< /note >}}

بررسی کنید که فایل `index.html` وجود دارد:

```shell
cat /mnt/data/index.html
```

خروجی باید به این صورت باشد:

```
Hello from Kubernetes storage
```

اکنون می‌توانید پوستهٔ نود را ببندید.

## ایجاد یک PersistentVolume

در این تمرین، یک PersistentVolume از نوع *hostPath* ایجاد می‌کنید. کوبرنتیز از
نوع hostPath برای توسعه و آزمایش روی کلاستر تک‌نودی پشتیبانی می‌کند. یک
PersistentVolume از نوع hostPath از یک فایل یا دایرکتوری روی نود برای شبیه‌سازی
ذخیره‌سازی متصل به شبکه استفاده می‌کند.

در کلاستر عملیاتی (production) از hostPath استفاده نمی‌شود. در عوض، مدیر کلاستر
یک منبع شبکه‌ای مانند دیسک پایدار Google Compute Engine، یک اشتراک NFS یا یک
حجم Amazon Elastic Block Store را فراهم می‌کند. مدیران کلاستر همچنین می‌توانند از
[StorageClassها](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#storageclass-v1-storage-k8s-io)
برای راه‌اندازی
[تأمین پویا](/docs/concepts/storage/dynamic-provisioning/) استفاده کنند.

فایل پیکربندی PersistentVolume از نوع hostPath به این صورت است:

{{% code_sample file="pods/storage/pv-volume.yaml" %}}

این فایل پیکربندی مشخص می‌کند که حجم در مسیر `/mnt/data` روی نود کلاستر قرار
دارد. همچنین اندازهٔ ۱۰ گیبی‌بایت و حالت دسترسی `ReadWriteOnce` را تعیین می‌کند؛
این حالت یعنی حجم را فقط یک نود می‌تواند به‌صورت خواندنی-نوشتنی mount کند. این
پیکربندی [نام StorageClass](/docs/concepts/storage/persistent-volumes/#class)
را برای این PersistentVolume برابر `manual` تعریف می‌کند؛ از این نام برای اتصال
درخواست‌های PersistentVolumeClaim به این PersistentVolume استفاده می‌شود.

{{< note >}}
این مثال برای سادگی از حالت دسترسی `ReadWriteOnce` استفاده می‌کند. برای استفادهٔ
عملیاتی، پروژهٔ کوبرنتیز توصیه می‌کند به‌جای آن از حالت دسترسی `ReadWriteOncePod`
استفاده کنید.
{{< /note >}}

‏PersistentVolume را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-volume.yaml
```

اطلاعات PersistentVolume را مشاهده کنید:

```shell
kubectl get pv task-pv-volume
```

خروجی نشان می‌دهد که مقدار `STATUS` این PersistentVolume برابر `Available` است.
این یعنی هنوز به هیچ PersistentVolumeClaimی متصل نشده است.

```
NAME             CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS      CLAIM     STORAGECLASS   REASON    AGE
task-pv-volume   10Gi       RWO           Retain          Available             manual                   4s
```

## ایجاد یک PersistentVolumeClaim

گام بعدی ایجاد یک PersistentVolumeClaim است. Podها از PersistentVolumeClaimها
برای درخواست ذخیره‌ساز فیزیکی استفاده می‌کنند. در این تمرین، یک
PersistentVolumeClaim ایجاد می‌کنید که حجمی با دست‌کم سه گیبی‌بایت درخواست
می‌کند؛ حجمی که بتواند در هر لحظه حداکثر برای یک نود دسترسی خواندنی-نوشتنی فراهم کند.

فایل پیکربندی PersistentVolumeClaim به این صورت است:

{{% code_sample file="pods/storage/pv-claim.yaml" %}}

‏PersistentVolumeClaim را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-claim.yaml
```

پس از ایجاد PersistentVolumeClaim، control plane کوبرنتیز به‌دنبال یک
PersistentVolume می‌گردد که الزامات این درخواست را برآورده کند. اگر control plane
یک PersistentVolume مناسب با همان StorageClass پیدا کند، درخواست را به آن حجم متصل می‌کند.

دوباره PersistentVolume را بررسی کنید:

```shell
kubectl get pv task-pv-volume
```

اکنون خروجی مقدار `STATUS` را برابر `Bound` نشان می‌دهد.

```
NAME             CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM                   STORAGECLASS   REASON    AGE
task-pv-volume   10Gi       RWO           Retain          Bound     default/task-pv-claim   manual                   2m
```

‏PersistentVolumeClaim را بررسی کنید:

```shell
kubectl get pvc task-pv-claim
```

خروجی نشان می‌دهد که PersistentVolumeClaim به PersistentVolume شما، یعنی
`task-pv-volume`، متصل شده است.

```
NAME            STATUS    VOLUME           CAPACITY   ACCESSMODES   STORAGECLASS   AGE
task-pv-claim   Bound     task-pv-volume   10Gi       RWO           manual         30s
```

## ایجاد یک Pod

گام بعدی ایجاد یک Pod است که از PersistentVolumeClaim شما به‌عنوان حجم استفاده می‌کند.

فایل پیکربندی Pod به این صورت است:

{{% code_sample file="pods/storage/pv-pod.yaml" %}}

توجه کنید که فایل پیکربندی Pod یک PersistentVolumeClaim را مشخص می‌کند، اما
PersistentVolume را مشخص نمی‌کند. از دید Pod، این درخواست (claim) یک حجم است.

‏Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-pod.yaml
```

بررسی کنید که کانتینر درون Pod در حال اجرا است:

```shell
kubectl get pod task-pv-pod
```

یک پوسته در کانتینری که در Pod شما اجرا می‌شود باز کنید:

```shell
kubectl exec -it task-pv-pod -- /bin/bash
```

در پوستهٔ خود بررسی کنید که nginx فایل `index.html` را از حجم hostPath ارائه می‌دهد:

```shell
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

خروجی، متنی را نشان می‌دهد که در فایل `index.html` روی حجم hostPath نوشته بودید:

```
Hello from Kubernetes storage
```

اگر این پیام را می‌بینید، یک Pod را با موفقیت پیکربندی کرده‌اید تا از ذخیره‌سازی
یک PersistentVolumeClaim استفاده کند.

## پاک‌سازی

‏Pod را حذف کنید:

```shell
kubectl delete pod task-pv-pod
```

## mount کردن یک PersistentVolume در دو مکان

تاکنون با نحوهٔ ایجاد PersistentVolume و PersistentVolumeClaim و همچنین mount
کردن حجم در یک مکان درون کانتینر آشنا شدید. اکنون بررسی می‌کنیم که چگونه می‌توان
یک PersistentVolume را در دو مکان متفاوت درون کانتینر mount کرد. در ادامه یک مثال آمده است:

{{% code_sample file="pods/storage/pv-duplicate.yaml" %}}

در اینجا:

- فیلد `subPath`: با این فیلد می‌توان فایل‌ها یا دایرکتوری‌های مشخصی از
  PersistentVolume mountشده را در مکان‌های مختلفی درون کانتینر در دسترس قرار داد. در این مثال:
  - مقدار `subPath: html` دایرکتوری html را mount می‌کند.
  - مقدار `subPath: nginx.conf` یک فایل مشخص، یعنی nginx.conf، را mount می‌کند.

از آنجا که مقدار اولین subPath برابر `html` است، باید یک دایرکتوری `html` درون
`/mnt/data/` روی نود ایجاد شود.

دومین subPath، یعنی `nginx.conf`، به این معناست که از فایلی درون دایرکتوری
`/mnt/data/` استفاده می‌شود. نیازی به ایجاد دایرکتوری دیگری نیست.

دو mount حجم روی کانتینر nginx شما ایجاد می‌شود:

- مسیر `/usr/share/nginx/html` برای وب‌سایت ایستا
- مسیر `/etc/nginx/nginx.conf` برای پیکربندی پیش‌فرض

### انتقال فایل index.html روی نود به یک پوشهٔ جدید

منظور از فایل `index.html` در اینجا همان فایلی است که در بخش «[ایجاد یک فایل index.html روی نود](#create-an-index-html-file-on-your-node)» ایجاد کردید.

یک پوسته روی تنها نود کلاستر خود باز کنید. نحوهٔ باز کردن پوسته به شیوهٔ
راه‌اندازی کلاستر شما بستگی دارد. برای مثال، اگر از Minikube استفاده می‌کنید،
می‌توانید با وارد کردن `minikube ssh` یک پوسته روی نود خود باز کنید.

دایرکتوری `/mnt/data/html` را ایجاد کنید:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo mkdir /mnt/data/html
```

فایل index.html را به این دایرکتوری منتقل کنید:

```shell
# Move index.html from its current location to the html sub-directory
sudo mv /mnt/data/index.html /mnt/data/html/index.html
```

### ایجاد یک فایل nginx.conf جدید

{{% code_sample file="pods/storage/nginx.conf" %}}

این نسخهٔ تغییریافتهٔ فایل پیش‌فرض `nginx.conf` است. در اینجا مقدار پیش‌فرض
`keepalive_timeout` به `60` تغییر یافته است.

فایل nginx.conf را ایجاد کنید:

```shell
cat <<EOF > /mnt/data/nginx.conf
user  nginx;
worker_processes  auto;
error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '\$remote_addr - \$remote_user [\$time_local] "\$request" '
                      '\$status \$body_bytes_sent "\$http_referer" '
                      '"\$http_user_agent" "\$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  60;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
EOF
```

### ایجاد یک Pod

در اینجا یک Pod ایجاد می‌کنیم که از PersistentVolume و PersistentVolumeClaim
موجود استفاده می‌کند. با این حال، این Pod فقط یک فایل مشخص (`nginx.conf`) و یک
دایرکتوری مشخص (`html`) را در کانتینر mount می‌کند.

‏Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-duplicate.yaml
```

بررسی کنید که کانتینر درون Pod در حال اجرا است:

```shell
kubectl get pod test
```

یک پوسته در کانتینری که در Pod شما اجرا می‌شود باز کنید:

```shell
kubectl exec -it test -- /bin/bash
```

در پوستهٔ خود بررسی کنید که nginx فایل `index.html` را از حجم hostPath ارائه می‌دهد:

```shell
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

خروجی، متنی را نشان می‌دهد که در فایل `index.html` روی حجم hostPath نوشته بودید:

```
Hello from Kubernetes storage
```

همچنین در پوستهٔ خود بررسی کنید که nginx فایل `nginx.conf` را از حجم hostPath ارائه می‌دهد:

```shell
# Be sure to run these commands inside the root shell that comes from
# running "kubectl exec" in the previous step
cat /etc/nginx/nginx.conf | grep keepalive_timeout
```

خروجی، متن تغییریافته‌ای را نشان می‌دهد که در فایل `nginx.conf` روی حجم hostPath نوشته بودید:

```
keepalive_timeout  60;
```

اگر این پیام‌ها را می‌بینید، یک Pod را با موفقیت پیکربندی کرده‌اید تا از یک فایل
و یک دایرکتوری مشخص در ذخیره‌سازی یک PersistentVolumeClaim استفاده کند.

## پاک‌سازی

‏Pod را حذف کنید:

```shell
kubectl delete pod test
kubectl delete pvc task-pv-claim
kubectl delete pv task-pv-volume
```

اگر هنوز پوسته‌ای روی نود کلاستر خود باز نکرده‌اید، به همان روشی که پیش‌تر انجام
دادید یک پوستهٔ جدید باز کنید.

در پوستهٔ نود، فایل‌ها و دایرکتوری‌هایی را که ایجاد کرده بودید حذف کنید:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo rm /mnt/data/html/index.html
sudo rm /mnt/data/nginx.conf
sudo rmdir /mnt/data/html
sudo rmdir /mnt/data
```

اکنون می‌توانید پوستهٔ نود را ببندید.

<!-- discussion -->

## کنترل دسترسی

در ذخیره‌سازی‌ای که با یک شناسهٔ گروه (GID) پیکربندی شده باشد، فقط Podهایی که از
همان GID استفاده می‌کنند اجازهٔ نوشتن دارند. نبودِ GID یا ناهمخوانی آن به خطای
عدم مجوز (permission denied) منجر می‌شود. برای کاهش نیاز به هماهنگی با کاربران،
مدیر می‌تواند یک PersistentVolume را با یک GID حاشیه‌نویسی (annotation) کند. در
این صورت، آن GID به‌طور خودکار به هر Podی که از آن PersistentVolume استفاده
می‌کند افزوده می‌شود.

از حاشیه‌نویسی `pv.beta.kubernetes.io/gid` به این صورت استفاده کنید:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv1
  annotations:
    pv.beta.kubernetes.io/gid: "1234"
```

وقتی یک Pod از PersistentVolumeای استفاده می‌کند که حاشیه‌نویسی GID دارد، آن GID
به همان شیوه‌ای بر همهٔ کانتینرهای Pod اعمال می‌شود که GIDهای مشخص‌شده در
security context خود Pod اعمال می‌شوند. هر GID، چه از حاشیه‌نویسی PersistentVolume
آمده باشد و چه از مشخصات Pod، بر نخستین پردازه‌ای که در هر کانتینر اجرا می‌شود اعمال می‌شود.

{{< note >}}
وقتی یک Pod از یک PersistentVolume استفاده می‌کند، GIDهای مرتبط با آن
PersistentVolume در خود منبع Pod دیده نمی‌شوند.
{{< /note >}}

## {{% heading "whatsnext" %}}

* دربارهٔ [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) بیشتر بیاموزید.
* [سند طراحی ذخیره‌سازی پایدار](https://git.k8s.io/design-proposals-archive/storage/persistent-storage.md) را بخوانید.

### مرجع

* [PersistentVolume](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#persistentvolume-v1-core)
* [PersistentVolumeSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#persistentvolumespec-v1-core)
* [PersistentVolumeClaim](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#persistentvolumeclaim-v1-core)
* [PersistentVolumeClaimSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#persistentvolumeclaimspec-v1-core)

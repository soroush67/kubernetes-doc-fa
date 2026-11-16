---
title: اجرای kubelet در حالت مستقل
content_type: tutorial
weight: 10
---

<!-- overview -->

این آموزش نشان می‌دهد که چگونه یک نمونهٔ مستقل از kubelet را اجرا کنید.

ممکن است انگیزه‌های گوناگونی برای اجرای kubelet به‌صورت مستقل داشته باشید.
هدف این آموزش آشنا کردن شما با کوبرنتیز است، حتی اگر تجربهٔ چندانی با آن نداشته باشید.
با دنبال کردن این آموزش، با راه‌اندازی نود، Podهای پایه (ایستا) و شیوهٔ مدیریت کانتینرها در کوبرنتیز آشنا می‌شوید.

پس از پایان این آموزش، می‌توانید استفاده از کلاستری را امتحان کنید که یک
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} برای مدیریت Podها،
نودها و انواع دیگر آبجکت‌ها دارد؛ برای نمونه،
[سلام، minikube](/docs/tutorials/hello-minikube/).

همچنین می‌توانید kubelet را برای موارد استفادهٔ محیط عملیاتی (production) در حالت مستقل اجرا کنید؛ برای نمونه،
برای اجرای control plane یک کلاستر با دسترس‌پذیری بالا که به‌صورت مقاوم در برابر خطا مستقر شده است. این
آموزش به جزئیات لازم برای اجرای یک control plane مقاوم در برابر خطا نمی‌پردازد.

## {{% heading "objectives" %}}

* نصب `cri-o` و `kubelet` روی یک سیستم لینوکسی و اجرای آن‌ها به‌صورت سرویس‌های `systemd`.
* راه‌اندازی یک Pod که `nginx` را اجرا می‌کند و روی پورت TCP شمارهٔ ۸۰ نشانی IP همان Pod به درخواست‌ها گوش می‌دهد.
* آشنایی با نحوهٔ تعامل اجزای مختلف این راهکار با یکدیگر.

{{< alert color="caution" title="هشدار" >}}
پیکربندی kubelet در این آموزش عمداً ناامن طراحی شده است و _نباید_ در محیط عملیاتی
از آن استفاده شود.
{{< /alert >}}

## {{% heading "prerequisites" %}}

* دسترسی مدیر (`root`) به یک سیستم لینوکسی که از `systemd` و `iptables`
  (یا nftables همراه با شبیه‌سازی `iptables`) استفاده می‌کند.
* دسترسی به اینترنت برای دریافت اجزای لازم برای این آموزش، از جمله:
  * یک {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}}
    که {{< glossary_tooltip term_id="cri" text="(CRI)">}} کوبرنتیز را پیاده‌سازی کند.
  * افزونه‌های شبکه (که اغلب با نام
    {{< glossary_tooltip text="رابط شبکهٔ کانتینر (CNI)" term_id="cni" >}} شناخته می‌شوند)
  * ابزارهای خط فرمان لازم: `curl`، `tar` و `jq`.

<!-- lessoncontent -->

## آماده‌سازی سیستم

### پیکربندی swap

به‌طور پیش‌فرض، اگر kubelet روی یک نود حافظهٔ swap را تشخیص دهد، راه‌اندازی نمی‌شود.
بنابراین یا باید swap را غیرفعال کنید یا kubelet را طوری پیکربندی کنید که وجود آن را تحمل کند.

{{< alert color="info" title="نکته" >}}
اگر kubelet را طوری پیکربندی کنید که swap را تحمل کند، kubelet همچنان Podها (و
کانتینرهای درون آن Podها) را طوری پیکربندی می‌کند که از فضای swap استفاده نکنند. برای اینکه بدانید Podها چگونه
می‌توانند واقعاً از swap موجود استفاده کنند، می‌توانید دربارهٔ
[مدیریت حافظهٔ swap](/docs/concepts/architecture/nodes/#swap-memory) روی نودهای لینوکسی بیشتر بخوانید.
{{< /alert >}}

اگر حافظهٔ swap فعال است، یا آن را غیرفعال کنید یا `failSwapOn: false` را به
فایل پیکربندی kubelet اضافه کنید.

برای بررسی فعال بودن swap:

```shell
sudo swapon --show
```

اگر این دستور خروجی‌ای نداشته باشد، حافظهٔ swap از قبل غیرفعال است.

برای غیرفعال کردن موقت swap:

```shell
sudo swapoff -a
```

برای اینکه این تغییر پس از راه‌اندازی مجدد سیستم نیز باقی بماند:

بسته به اینکه swap روی سیستم شما چگونه پیکربندی شده است، مطمئن شوید که در `/etc/fstab` یا
`systemd.swap` غیرفعال شده باشد.

### فعال کردن هدایت بسته‌های IPv4

برای بررسی فعال بودن هدایت بسته‌های IPv4:

```shell
cat /proc/sys/net/ipv4/ip_forward
```

اگر خروجی `1` باشد، این قابلیت از قبل فعال است. اگر خروجی `0` باشد، مراحل بعدی را دنبال کنید.

برای فعال کردن هدایت بسته‌های IPv4، یک فایل پیکربندی بسازید که پارامتر
`net.ipv4.ip_forward` را برابر `1` قرار دهد:

```shell
sudo tee /etc/sysctl.d/k8s.conf <<EOF
net.ipv4.ip_forward = 1
EOF
```

تغییرات را روی سیستم اعمال کنید:

```shell
sudo sysctl --system
```

خروجی مشابه زیر است:

```
...
* Applying /etc/sysctl.d/k8s.conf ...
net.ipv4.ip_forward = 1
* Applying /etc/sysctl.conf ...
```

## دریافت، نصب و پیکربندی اجزا

{{% thirdparty-content %}}

### نصب محیط اجرای کانتینر {#container-runtime}

جدیدترین نسخه‌های موجود از بسته‌های لازم را دریافت کنید (توصیه می‌شود).

این آموزش نصب [محیط اجرای کانتینر CRI-O](https://github.com/cri-o/cri-o)
(پیوند خارجی) را پیشنهاد می‌کند.

بسته به توزیع لینوکسی که استفاده می‌کنید، [روش‌های مختلفی برای نصب](https://github.com/cri-o/cri-o/blob/main/install.md)
محیط اجرای کانتینر CRI-O وجود دارد. با اینکه
CRI-O استفاده از بسته‌های `deb` یا `rpm` را توصیه می‌کند، این آموزش از اسکریپت
_بستهٔ باینری ایستا_ (static binary bundle) در
[پروژهٔ CRI-O Packaging](https://github.com/cri-o/packaging/blob/main/README.md)
استفاده می‌کند تا هم کل فرایند ساده‌تر شود و هم به توزیع خاصی وابسته نباشد.

این اسکریپت نرم‌افزارهای لازم دیگری را نیز نصب و پیکربندی می‌کند؛ از جمله
[`cni-plugins`](https://github.com/containernetworking/cni) برای شبکه‌بندی
کانتینرها، و [`crun`](https://github.com/containers/crun) و
[`runc`](https://github.com/opencontainers/runc) برای اجرای کانتینرها.

این اسکریپت معماری پردازندهٔ سیستم شما (`amd64` یا `arm64`) را به‌طور خودکار
تشخیص می‌دهد و جدیدترین نسخه‌های بسته‌های نرم‌افزاری را انتخاب و نصب می‌کند.

### راه‌اندازی CRI-O {#cri-o-setup}

به صفحهٔ [انتشارها](https://github.com/cri-o/cri-o/releases) (پیوند خارجی) بروید.

اسکریپت بستهٔ باینری ایستا را دریافت کنید:

```shell
curl https://raw.githubusercontent.com/cri-o/packaging/main/get > crio-install
```

اسکریپت نصب را اجرا کنید:

```shell
sudo bash crio-install
```

سرویس `crio` را فعال و اجرا کنید:

```shell
sudo systemctl daemon-reload
sudo systemctl enable --now crio.service
```

آزمون سریع:

```shell
sudo systemctl is-active crio.service
```

خروجی مشابه زیر است:

```
active
```

بررسی دقیق سرویس:

```shell
sudo journalctl -f -u crio.service
```

### نصب افزونه‌های شبکه

نصب‌کنندهٔ `cri-o` بستهٔ `cni-plugins` را نصب و پیکربندی می‌کند. می‌توانید
با اجرای دستور زیر از درستی نصب مطمئن شوید:

```shell
/opt/cni/bin/bridge --version
```

خروجی مشابه زیر است:

```
CNI bridge plugin v1.5.1
CNI protocol versions supported: 0.1.0, 0.2.0, 0.3.0, 0.3.1, 0.4.0, 1.0.0
```

برای بررسی پیکربندی پیش‌فرض:

```shell
cat /etc/cni/net.d/11-crio-ipv4-bridge.conflist
```

خروجی مشابه زیر است:

```json
{
  "cniVersion": "1.0.0",
  "name": "crio",
  "plugins": [
    {
      "type": "bridge",
      "bridge": "cni0",
      "isGateway": true,
      "ipMasq": true,
      "hairpinMode": true,
      "ipam": {
        "type": "host-local",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ],
        "ranges": [
            [{ "subnet": "10.85.0.0/16" }]
        ]
      }
    }
  ]
}
```

{{< alert color="info" title="نکته" >}}
مطمئن شوید که محدودهٔ پیش‌فرض `subnet` (`10.85.0.0/16`) با هیچ‌یک از شبکه‌های فعال شما
هم‌پوشانی نداشته باشد. اگر هم‌پوشانی وجود دارد، می‌توانید فایل را ویرایش و این محدوده را
متناسب با آن تغییر دهید. پس از اعمال تغییر، سرویس را دوباره راه‌اندازی کنید.
{{< /alert >}}

### دریافت و راه‌اندازی kubelet

[جدیدترین نسخهٔ پایدار](/releases/download/) kubelet را دریافت کنید.

{{< tabs name="download_kubelet" >}}
{{< tab name="x86-64" codelang="bash" >}}
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubelet"
{{< /tab >}}
{{< tab name="ARM64" codelang="bash" >}}
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubelet"
{{< /tab >}}
{{< /tabs >}}

پیکربندی:

```shell
sudo mkdir -p /etc/kubernetes/manifests
```

```shell
sudo tee /etc/kubernetes/kubelet.yaml <<EOF
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
authentication:
  webhook:
    enabled: false # Do NOT use in production clusters!
authorization:
  mode: AlwaysAllow # Do NOT use in production clusters!
enableServer: false
logging:
  format: text
address: 127.0.0.1 # Restrict access to localhost
readOnlyPort: 10255 # Do NOT use in production clusters!
staticPodPath: /etc/kubernetes/manifests
containerRuntimeEndpoint: unix:///var/run/crio/crio.sock
EOF
```

{{< alert color="info" title="نکته" >}}
از آنجا که کلاستری برای محیط عملیاتی راه‌اندازی نمی‌کنید، برای پرس‌وجوهای بدون احراز هویت
به API کلاینت kubelet از HTTP ساده (`readOnlyPort: 10255`) استفاده می‌کنید.

در این آموزش، _وب‌هوک احراز هویت_ غیرفعال شده و _حالت مجوزدهی_ روی `AlwaysAllow`
تنظیم شده است. برای پیکربندی درست kubelet در حالت مستقل در محیط خودتان، می‌توانید دربارهٔ
[حالت‌های مجوزدهی](/docs/reference/access-authn-authz/authorization/#authorization-modules)
و [احراز هویت با وب‌هوک](/docs/reference/access-authn-authz/webhook/) بیشتر بخوانید.

برای اینکه بدانید اجزای کوبرنتیز از چه پورت‌هایی استفاده می‌کنند، صفحهٔ
[پورت‌ها و پروتکل‌ها](/docs/reference/networking/ports-and-protocols/) را ببینید.
{{< /alert >}}

نصب:

```shell
chmod +x kubelet
sudo cp kubelet /usr/bin/
```

یک فایل واحد سرویس `systemd` بسازید:

```shell
sudo tee /etc/systemd/system/kubelet.service <<EOF
[Unit]
Description=Kubelet

[Service]
ExecStart=/usr/bin/kubelet \
 --config=/etc/kubernetes/kubelet.yaml
Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

آرگومان خط فرمان `--kubeconfig` عمداً در فایل پیکربندی سرویس حذف شده است.
این آرگومان مسیر یک فایل
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
را تعیین می‌کند که نحوهٔ اتصال به API server را مشخص می‌کند و حالت API server را فعال می‌سازد.
با حذف آن، حالت مستقل فعال می‌شود.

سرویس `kubelet` را فعال و اجرا کنید:

```shell
sudo systemctl daemon-reload
sudo systemctl enable --now kubelet.service
```

آزمون سریع:

```shell
sudo systemctl is-active kubelet.service
```

خروجی مشابه زیر است:

```
active
```

بررسی دقیق سرویس:

```shell
sudo journalctl -u kubelet.service
```

نقطهٔ پایانی `/healthz` در API کلاینت kubelet را بررسی کنید:

```shell
curl http://localhost:10255/healthz?verbose
```

خروجی مشابه زیر است:

```
[+]ping ok
[+]log ok
[+]syncloop ok
healthz check passed
```

از نقطهٔ پایانی `/pods` در API کلاینت kubelet پرس‌وجو کنید:

```shell
curl http://localhost:10255/pods | jq '.'
```

خروجی مشابه زیر است:

```json
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {},
  "items": null
}
```

## اجرای یک Pod در kubelet

در حالت مستقل، می‌توانید Podها را با استفاده از مانیفست‌های Pod اجرا کنید. این مانیفست‌ها
می‌توانند روی سیستم فایل محلی باشند یا از طریق HTTP از یک منبع پیکربندی دریافت شوند.

یک مانیفست برای Pod بسازید:

```shell
cat <<EOF > static-web.yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-web
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

فایل مانیفست `static-web.yaml` را در پوشهٔ `/etc/kubernetes/manifests` کپی کنید.

```shell
sudo cp static-web.yaml /etc/kubernetes/manifests/
```

### به‌دست آوردن اطلاعات دربارهٔ kubelet و Pod {#find-out-information}

افزونهٔ شبکهٔ Pod یک پل شبکه (`cni0`) و برای هر Pod یک جفت رابط `veth` ایجاد می‌کند
(یکی از این جفت درون Pod تازه‌ساخته‌شده و دیگری در سطح میزبان قرار دارد).

از نقطهٔ پایانی API کلاینت kubelet در نشانی `http://localhost:10255/pods` پرس‌وجو کنید:

```shell
curl http://localhost:10255/pods | jq '.'
```

برای به‌دست آوردن نشانی IP مربوط به Pod با نام `static-web`:

```shell
curl http://localhost:10255/pods | jq '.items[].status.podIP'
```

خروجی مشابه زیر است:

```
"10.85.0.4"
```

به Pod سرور `nginx` در نشانی `http://<IP>:<Port>` متصل شوید (پورت پیش‌فرض ۸۰ است)؛ در این مثال:

```shell
curl http://10.85.0.4
```

خروجی مشابه زیر است:

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

## جزئیات بیشتر را کجا پیدا کنیم

اگر برای اجرای درست این آموزش نیاز به عیب‌یابی دارید، می‌توانید
برای پایش و رفع اشکال، پوشه‌های زیر را بررسی کنید:

```
/var/lib/cni
/var/lib/containers
/var/lib/kubelet

/var/log/containers
/var/log/pods
```

## پاک‌سازی

### kubelet

```shell
sudo systemctl disable --now kubelet.service
sudo systemctl daemon-reload
sudo rm /etc/systemd/system/kubelet.service
sudo rm /usr/bin/kubelet
sudo rm -rf /etc/kubernetes
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/log/containers
sudo rm -rf /var/log/pods
```

### محیط اجرای کانتینر

```shell
sudo systemctl disable --now crio.service
sudo systemctl daemon-reload
sudo rm -rf /usr/local/bin
sudo rm -rf /usr/local/lib
sudo rm -rf /usr/local/share
sudo rm -rf /usr/libexec/crio
sudo rm -rf /etc/crio
sudo rm -rf /etc/containers
```

### افزونه‌های شبکه

```shell
sudo rm -rf /opt/cni
sudo rm -rf /etc/cni
sudo rm -rf /var/lib/cni
```

## جمع‌بندی

این صفحه جنبه‌های پایه‌ای استقرار kubelet در حالت مستقل را پوشش داد.
اکنون آماده‌اید که Podها را مستقر کنید و قابلیت‌های دیگر را بیازمایید.

توجه کنید که در حالت مستقل، kubelet از دریافت پیکربندی Podها از control plane
پشتیبانی *نمی‌کند* (زیرا هیچ اتصالی به control plane وجود ندارد).

همچنین نمی‌توانید از {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} یا
{{< glossary_tooltip text="Secret" term_id="secret" >}} برای پیکربندی کانتینرهای
یک Pod ایستا استفاده کنید.

## {{% heading "whatsnext" %}}

* آموزش [سلام، minikube](/docs/tutorials/hello-minikube/) را دنبال کنید تا با اجرای کوبرنتیز
  _همراه با_ control plane آشنا شوید. ابزار minikube به شما کمک می‌کند یک کلاستر تمرینی روی رایانهٔ خودتان راه‌اندازی کنید.
* دربارهٔ [افزونه‌های شبکه](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) بیشتر بیاموزید.
* دربارهٔ [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/) بیشتر بیاموزید.
* دربارهٔ [kubelet](/docs/reference/command-line-tools-reference/kubelet/) بیشتر بیاموزید.
* دربارهٔ [Podهای ایستا](/docs/tasks/configure-pod-container/static-pod/) بیشتر بیاموزید.

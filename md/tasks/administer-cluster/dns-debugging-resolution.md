---
reviewers:
- bowei
- zihongz
title:  اشکال‌زدایی تفکیک نام DNS
content_type: task
min-kubernetes-server-version: v1.6
weight: 170
---

<!-- overview -->
این صفحه راهنمایی‌هایی برای تشخیص مشکلات DNS ارائه می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}  
کلاستر شما باید طوری پیکربندی شده باشد که از
{{< glossary_tooltip text="افزونه" term_id="addons" >}}ی CoreDNS استفاده کند.

{{% version-check %}}

<!-- steps -->

### یک Pod ساده به‌عنوان محیط آزمایشی بسازید

{{% code_sample file="admin/dns/dnsutils.yaml" %}}

{{< note >}}
این مثال یک Pod در فضای نام (namespace) `default` می‌سازد. تفکیک نام DNS برای
سرویس‌ها به فضای نام Pod بستگی دارد. برای اطلاعات بیشتر، صفحهٔ
[DNS برای سرویس‌ها و Podها](/docs/concepts/services-networking/dns-pod-service/#what-things-get-dns-names) را ببینید.
{{< /note >}}

با استفاده از این مانیفست یک Pod بسازید:

```shell
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
```
```
pod/dnsutils created
```
…و وضعیت آن را بررسی کنید:
```shell
kubectl get pods dnsutils
```
```
NAME       READY     STATUS    RESTARTS   AGE
dnsutils   1/1       Running   0          <some-time>
```

پس از اجرای این Pod، می‌توانید دستور `nslookup` را در این محیط اجرا کنید.
اگر خروجی‌ای مشابه نمونهٔ زیر می‌بینید، DNS به‌درستی کار می‌کند.

```shell
kubectl exec -i -t dnsutils -- nslookup kubernetes.default
```
```
Server:    10.0.0.10
Address 1: 10.0.0.10

Name:      kubernetes.default
Address 1: 10.0.0.1
```

اگر دستور `nslookup` با شکست مواجه شد، موارد زیر را بررسی کنید:

### ابتدا پیکربندی محلی DNS را بررسی کنید

محتوای فایل resolv.conf را بررسی کنید.
(برای اطلاعات بیشتر، [سفارشی‌سازی سرویس DNS](/docs/tasks/administer-cluster/dns-custom-nameservers) و
بخش [مشکلات شناخته‌شده](#known-issues) را در ادامه ببینید.)

```shell
kubectl exec -ti dnsutils -- cat /etc/resolv.conf
```

بررسی کنید که مسیر جست‌وجو (search path) و سرور نام (name server) مانند نمونهٔ زیر تنظیم شده باشند
(توجه کنید که مسیر جست‌وجو ممکن است در ارائه‌دهندگان ابری مختلف متفاوت باشد):

```
search default.svc.cluster.local svc.cluster.local cluster.local google.internal c.gce_project_id.internal
nameserver 10.0.0.10
options ndots:5
```

خطاهایی مانند نمونه‌های زیر نشان‌دهندهٔ مشکلی در افزونهٔ CoreDNS
یا سرویس‌های مرتبط با آن هستند:

```shell
kubectl exec -i -t dnsutils -- nslookup kubernetes.default
```
```
Server:    10.0.0.10
Address 1: 10.0.0.10

nslookup: can't resolve 'kubernetes.default'
```

یا

```shell
kubectl exec -i -t dnsutils -- nslookup kubernetes.default
```
```
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

nslookup: can't resolve 'kubernetes.default'
```

### بررسی کنید که Pod مربوط به DNS در حال اجرا باشد

با دستور `kubectl get pods` بررسی کنید که Pod مربوط به DNS در حال اجرا باشد.

```shell
kubectl get pods --namespace=kube-system -l k8s-app=kube-dns
```
```
NAME                       READY     STATUS    RESTARTS   AGE
...
coredns-7b96bf9f76-5hsxb   1/1       Running   0           1h
coredns-7b96bf9f76-mvmmt   1/1       Running   0           1h
...
```

{{< note >}}
مقدار برچسب `k8s-app` برای CoreDNS، به‌منظور سازگاری با نسخه‌های قبلی و kube-dns اصلی،
برابر با `kube-dns` است.
{{< /note >}}


اگر می‌بینید که هیچ Pod مربوط به CoreDNS در حال اجرا نیست یا وضعیت Pod شکست‌خورده یا تکمیل‌شده است،
احتمالاً افزونهٔ DNS به‌طور پیش‌فرض در محیط فعلی شما مستقر نشده است و
باید آن را به‌صورت دستی مستقر کنید.

### خطاهای Pod مربوط به DNS را بررسی کنید

با دستور `kubectl logs` لاگ‌های کانتینرهای DNS را ببینید.

برای CoreDNS:
```shell
kubectl logs --namespace=kube-system -l k8s-app=kube-dns
```

نمونه‌ای از لاگ یک CoreDNS سالم در ادامه آمده است:

```
.:53
2018/08/15 14:37:17 [INFO] CoreDNS-1.2.2
2018/08/15 14:37:17 [INFO] linux/amd64, go1.10.3, 2e322f6
CoreDNS-1.2.2
linux/amd64, go1.10.3, 2e322f6
2018/08/15 14:37:17 [INFO] plugin/reload: Running configuration MD5 = 24e6c59e83ce706f07bcc82c31b1ea1c
```

بررسی کنید که آیا پیام مشکوک یا غیرمنتظره‌ای در لاگ‌ها وجود دارد یا نه.

### آیا سرویس DNS فعال است؟

با دستور `kubectl get service` بررسی کنید که سرویس DNS فعال باشد.

```shell
kubectl get svc --namespace=kube-system
```
```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)             AGE
...
kube-dns     ClusterIP   10.0.0.10      <none>        53/UDP,53/TCP        1h
...
```

{{< note >}}
نام Service مربوط به CoreDNS، به‌منظور سازگاری با نسخه‌های قبلی و kube-dns اصلی،
`kube-dns` است.
{{< /note >}}



اگر Service را ساخته‌اید، یا قرار بوده به‌طور پیش‌فرض ساخته شود
اما نمایش داده نمی‌شود، برای اطلاعات بیشتر صفحهٔ
[اشکال‌زدایی سرویس‌ها](/docs/tasks/debug/debug-application/debug-service/) را ببینید.

### آیا endpointهای DNS در دسترس قرار گرفته‌اند؟

با دستور `kubectl get endpointslice` می‌توانید بررسی کنید که
endpointهای DNS در دسترس قرار گرفته باشند.

```shell
kubectl get endpointslice -l kubernetes.io/service-name=kube-dns --namespace=kube-system
```
```
NAME             ADDRESSTYPE   PORTS   ENDPOINTS                  AGE
coredns-zxoja    IPv4          53      10.180.3.17,10.180.3.17    1h
```

اگر endpointها را نمی‌بینید، بخش endpointها را در مستندات
[اشکال‌زدایی سرویس‌ها](/docs/tasks/debug/debug-application/debug-service/) ببینید.

### آیا پرس‌وجوهای DNS دریافت و پردازش می‌شوند؟

برای بررسی اینکه CoreDNS پرس‌وجوها را دریافت می‌کند یا نه، می‌توانید افزونهٔ `log` را به پیکربندی CoreDNS (که Corefile نیز نامیده می‌شود) اضافه کنید.
فایل Corefile مربوط به CoreDNS در یک {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} با نام `coredns` نگهداری می‌شود. برای ویرایش آن از دستور زیر استفاده کنید:

```
kubectl -n kube-system edit configmap coredns
```

سپس مطابق نمونهٔ زیر، `log` را به بخش Corefile اضافه کنید:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        log
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          upstream
          fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

پس از ذخیرهٔ تغییرات، ممکن است یک تا دو دقیقه طول بکشد تا کوبرنتیز این تغییرات را به Podهای CoreDNS منتقل کند.

سپس چند پرس‌وجو انجام دهید و مطابق بخش‌های قبلی این سند، لاگ‌ها را ببینید. اگر Podهای CoreDNS پرس‌وجوها را دریافت کنند، باید آن‌ها را در لاگ‌ها ببینید.

نمونه‌ای از یک پرس‌وجو در لاگ در ادامه آمده است:

```
.:53
2018/08/15 14:37:15 [INFO] CoreDNS-1.2.0
2018/08/15 14:37:15 [INFO] linux/amd64, go1.10.3, 2e322f6
CoreDNS-1.2.0
linux/amd64, go1.10.3, 2e322f6
2018/09/07 15:29:04 [INFO] plugin/reload: Running configuration MD5 = 162475cdf272d8aa601e6fe67a6ad42f
2018/09/07 15:29:04 [INFO] Reloading complete
172.17.0.18:41675 - [07/Sep/2018:15:29:11 +0000] 59925 "A IN kubernetes.default.svc.cluster.local. udp 54 false 512" NOERROR qr,aa,rd,ra 106 0.000066649s
```
### آیا CoreDNS مجوزهای کافی دارد؟

برای تفکیک درست نام سرویس‌ها، CoreDNS باید بتواند منابع مرتبط با {{< glossary_tooltip text="سرویس"
term_id="service" >}} و {{< glossary_tooltip text="endpointslice"
term_id="endpoint-slice" >}} را فهرست کند.

نمونهٔ پیام خطا:
```
2022-03-18T07:12:15.699431183Z [INFO] 10.96.144.227:52299 - 3686 "A IN serverproxy.contoso.net.cluster.local. udp 52 false 512" SERVFAIL qr,aa,rd 145 0.000091221s
```

ابتدا ClusterRole فعلی `system:coredns` را دریافت کنید:

```shell
kubectl describe clusterrole system:coredns -n kube-system
```

خروجی مورد انتظار:
```
PolicyRule:
  Resources                        Non-Resource URLs  Resource Names  Verbs
  ---------                        -----------------  --------------  -----
  endpoints                        []                 []              [list watch]
  namespaces                       []                 []              [list watch]
  pods                             []                 []              [list watch]
  services                         []                 []              [list watch]
  endpointslices.discovery.k8s.io  []                 []              [list watch]
```

اگر مجوزی وجود ندارد، ClusterRole را ویرایش کنید و آن را اضافه کنید:

```shell
kubectl edit clusterrole system:coredns -n kube-system
```

نمونه‌ای از افزودن مجوزهای EndpointSlice:
```
...
- apiGroups:
  - discovery.k8s.io
  resources:
  - endpointslices
  verbs:
  - list
  - watch
...
```

### آیا در فضای نام درست سرویس هستید؟

دامنهٔ پرس‌وجوهای DNS که فضای نامی در آن‌ها مشخص نشده است، به فضای نام Pod
محدود می‌شود.

اگر فضای نام Pod و سرویس متفاوت باشد، پرس‌وجوی DNS باید فضای نام
سرویس را نیز در بر داشته باشد.

این پرس‌وجو به فضای نام Pod محدود است:
```shell
kubectl exec -i -t dnsutils -- nslookup <service-name>
```

این پرس‌وجو فضای نام را مشخص می‌کند:
```shell
kubectl exec -i -t dnsutils -- nslookup <service-name>.<namespace>
```

برای آشنایی بیشتر با تفکیک نام، صفحهٔ
[DNS برای سرویس‌ها و Podها](/docs/concepts/services-networking/dns-pod-service/#what-things-get-dns-names) را ببینید.

## مشکلات شناخته‌شده

برخی توزیع‌های لینوکس (مانند Ubuntu) به‌طور پیش‌فرض از یک تفکیک‌کنندهٔ DNS محلی (systemd-resolved) استفاده می‌کنند.
سرویس systemd-resolved فایل `/etc/resolv.conf` را جابه‌جا می‌کند و یک فایل stub را جایگزین آن می‌کند که ممکن است هنگام تفکیک نام‌ها در سرورهای بالادستی،
یک حلقهٔ ارسال (forwarding loop) مخرب ایجاد کند. می‌توان این مشکل را به‌صورت دستی برطرف کرد؛ کافی است با فلگ `--resolv-conf` در kubelet
به فایل `resolv.conf` درست اشاره کنید (در صورت استفاده از `systemd-resolved`، این فایل `/run/systemd/resolve/resolv.conf` است).
ابزار kubeadm وجود `systemd-resolved` را به‌طور خودکار تشخیص می‌دهد و فلگ‌های kubelet را متناسب با آن تنظیم می‌کند.

نصب‌های کوبرنتیز به‌طور پیش‌فرض فایل‌های `resolv.conf` نودها را برای استفاده از
DNS کلاستر پیکربندی نمی‌کنند، زیرا این فرایند ذاتاً به توزیع وابسته است.
احتمالاً این قابلیت در آینده پیاده‌سازی خواهد شد.

کتابخانهٔ libc لینوکس (یا همان glibc) به‌طور پیش‌فرض تعداد رکوردهای `nameserver` در DNS را به ۳ محدود می‌کند
و کوبرنتیز به یک رکورد `nameserver` نیاز دارد. بنابراین اگر
یک نصب محلی از قبل از ۳ رکورد `nameserver` استفاده کند، برخی از این مدخل‌ها
از دست می‌روند. برای دور زدن این محدودیت، نود می‌تواند `dnsmasq` را اجرا کند که
مدخل‌های `nameserver` بیشتری فراهم می‌کند. همچنین می‌توانید از فلگ `--resolv-conf`
در kubelet استفاده کنید.

اگر از نسخهٔ 3.17 یا قدیمی‌تر Alpine به‌عنوان ایمیج پایه استفاده می‌کنید، ممکن است به‌دلیل یک مشکل طراحی در Alpine،
DNS به‌درستی کار نکند.
تا پیش از نسخهٔ 1.24 کتابخانهٔ musl، امکان بازگشت به TCP (TCP fallback) در تفکیک‌کنندهٔ stub مربوط به DNS وجود نداشت؛ به این معنا که هر فراخوانی DNS بزرگ‌تر از ۵۱۲ بایت با شکست مواجه می‌شد.
لطفاً ایمیج‌های خود را به نسخهٔ 3.18 یا بالاتر Alpine ارتقا دهید.

## {{% heading "whatsnext" %}}

- صفحهٔ [مقیاس‌دهی خودکار سرویس DNS در یک کلاستر](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/) را ببینید.
- صفحهٔ [DNS برای سرویس‌ها و Podها](/docs/concepts/services-networking/dns-pod-service/) را بخوانید.

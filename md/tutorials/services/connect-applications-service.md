---
reviewers:
- caesarxuchao
- lavalamp
- thockin
title: اتصال برنامه‌ها با Serviceها
content_type: tutorial
weight: 20
---


<!-- overview -->

## مدل کوبرنتیز برای اتصال کانتینرها

اکنون یک برنامهٔ تکثیرشده دارید که به‌طور پیوسته اجرا می‌شود و می‌توانید آن را در شبکه در دسترس قرار دهید.

کوبرنتیز فرض می‌کند که پادها، صرف‌نظر از اینکه روی کدام میزبان قرار بگیرند، می‌توانند با پادهای دیگر ارتباط برقرار کنند.
کوبرنتیز به هر پاد یک نشانی IP خصوصی و اختصاصی در سطح کلاستر می‌دهد. بنابراین لازم نیست به‌صراحت میان پادها پیوند
ایجاد کنید یا پورت‌های کانتینر را به پورت‌های میزبان نگاشت کنید. به این ترتیب، همهٔ کانتینرهای درون یک Pod می‌توانند
از طریق localhost به پورت‌های یکدیگر دسترسی داشته باشند و همهٔ پادهای یک کلاستر نیز بدون NAT یکدیگر را می‌بینند.
ادامهٔ این سند توضیح می‌دهد که چگونه می‌توانید سرویس‌های قابل‌اعتمادی را روی چنین مدل شبکه‌ای اجرا کنید.

این آموزش برای نشان دادن این مفهوم از یک وب‌سرور سادهٔ nginx استفاده می‌کند.

<!-- body -->

## در دسترس قرار دادن پادها در کلاستر

این کار را در یکی از مثال‌های قبلی انجام دادیم، اما بیایید یک بار دیگر آن را تکرار کنیم و این بار بر جنبهٔ شبکه تمرکز کنیم.
یک Pod برای nginx ایجاد کنید و توجه داشته باشید که این Pod مشخصهٔ پورت کانتینر دارد:

{{% code_sample file="service/networking/run-my-nginx.yaml" %}}

با این کار، این Pod از هر نودی در کلاستر شما قابل دسترسی می‌شود. نودهایی را که Pod روی آن‌ها اجرا می‌شود بررسی کنید:

```shell
kubectl apply -f ./run-my-nginx.yaml
kubectl get pods -l run=my-nginx -o wide
```
```
NAME                        READY     STATUS    RESTARTS   AGE       IP            NODE
my-nginx-3800858182-jr4a2   1/1       Running   0          13s       10.244.3.4    kubernetes-minion-905m
my-nginx-3800858182-kna2y   1/1       Running   0          13s       10.244.2.5    kubernetes-minion-ljyd
```

نشانی‌های IP پادهای خود را بررسی کنید:

```shell
kubectl get pods -l run=my-nginx -o custom-columns=POD_IP:.status.podIPs
    POD_IP
    [map[ip:10.244.3.4]]
    [map[ip:10.244.2.5]]
```

باید بتوانید با ssh به هر نودی از کلاستر خود وارد شوید و با ابزاری مانند `curl`
به هر دو نشانی IP درخواست بفرستید. توجه کنید که کانتینرها از پورت 80 روی نود
استفاده *نمی‌کنند* و هیچ قاعدهٔ NAT خاصی هم برای مسیریابی ترافیک به پاد وجود ندارد. این یعنی
می‌توانید چند پاد nginx را روی یک نود اجرا کنید که همگی از `containerPort` یکسانی استفاده می‌کنند،
و از هر پاد یا نود دیگری در کلاستر، با استفاده از نشانی IP اختصاص‌یافته به هر پاد، به آن‌ها
دسترسی داشته باشید. اگر بخواهید پورت مشخصی روی نود میزبان به پادهای پشتیبان هدایت شود،
این کار ممکن است؛ اما مدل شبکه طوری طراحی شده است که نیازی به این کار نداشته باشید.

اگر کنجکاو هستید، می‌توانید دربارهٔ
[مدل شبکهٔ کوبرنتیز](/docs/concepts/cluster-administration/networking/#the-kubernetes-network-model)
بیشتر بخوانید.

## ایجاد یک Service

اکنون پادهایی داریم که nginx را در یک فضای نشانی تخت و سراسری در سطح کلاستر اجرا می‌کنند. در تئوری
می‌توانید مستقیماً با این پادها ارتباط برقرار کنید، اما اگر یک نود از کار بیفتد چه اتفاقی می‌افتد؟ پادها نیز
همراه آن از بین می‌روند و ReplicaSet درون Deployment پادهای جدیدی با نشانی‌های IP متفاوت ایجاد می‌کند.
این همان مشکلی است که Service حل می‌کند.

هر Service در کوبرنتیز یک انتزاع است که مجموعه‌ای منطقی از پادها را تعریف می‌کند؛ پادهایی که در جایی از
کلاستر شما اجرا می‌شوند و همگی کارکرد یکسانی ارائه می‌دهند. هنگام ایجاد هر Service، یک نشانی IP یکتا
(که clusterIP نیز نامیده می‌شود) به آن اختصاص داده می‌شود. این نشانی به طول عمر Service وابسته است
و تا زمانی که Service وجود دارد تغییر نمی‌کند. می‌توان پادها را طوری پیکربندی کرد که با Service ارتباط
برقرار کنند، با این اطمینان که ارتباط با Service به‌طور خودکار میان پادهای عضو آن Service توزیع بار (load-balance) می‌شود.

می‌توانید با دستور `kubectl expose` یک Service برای دو رونوشت (replica) nginx خود ایجاد کنید:

```shell
kubectl expose deployment/my-nginx
```
```
service/my-nginx exposed
```

این کار معادل اجرای `kubectl apply -f` روی فایل YAML زیر است:

{{% code_sample file="service/networking/nginx-svc.yaml" %}}

این مشخصه یک Service ایجاد می‌کند که پورت TCP شمارهٔ 80 را روی هر Pod دارای برچسب
`run: my-nginx` هدف قرار می‌دهد و آن را روی یک پورت انتزاعی Service در دسترس قرار می‌دهد
(`targetPort` پورتی است که کانتینر ترافیک را روی آن می‌پذیرد و `port` پورت انتزاعی Service است
که می‌تواند هر پورتی باشد که پادهای دیگر برای دسترسی به Service از آن استفاده می‌کنند).
برای دیدن فهرست فیلدهای پشتیبانی‌شده در تعریف Service، آبجکت API
[Service](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#service-v1-core) را ببینید.
وضعیت Service خود را بررسی کنید:

```shell
kubectl get svc my-nginx
```
```
NAME       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
my-nginx   ClusterIP   10.0.162.149   <none>        80/TCP    21s
```

همان‌طور که پیش‌تر گفته شد، پشتوانهٔ هر Service گروهی از پادهاست. این پادها از طریق
{{<glossary_tooltip term_id="endpoint-slice" text="EndpointSliceها">}} در دسترس قرار می‌گیرند.
انتخابگر (selector) Service به‌طور پیوسته ارزیابی می‌شود و نتایج آن با درخواست POST به یک EndpointSlice
ارسال می‌شود که با استفاده از {{< glossary_tooltip text="برچسب‌ها" term_id="label" >}} به Service متصل است.
وقتی یک Pod از بین می‌رود، به‌طور خودکار از EndpointSliceهایی که آن را به‌عنوان نقطهٔ پایانی (endpoint)
در بر دارند حذف می‌شود. پادهای جدیدی که با انتخابگر Service مطابقت داشته باشند، به‌طور خودکار به یکی از
EndpointSliceهای آن Service افزوده می‌شوند.
نقاط پایانی را بررسی کنید و توجه کنید که نشانی‌های IP همان نشانی‌های پادهایی هستند که در گام اول ایجاد شدند:

```shell
kubectl describe svc my-nginx
```
```
Name:                my-nginx
Namespace:           default
Labels:              run=my-nginx
Annotations:         <none>
Selector:            run=my-nginx
Type:                ClusterIP
IP Family Policy:    SingleStack
IP Families:         IPv4
IP:                  10.0.162.149
IPs:                 10.0.162.149
Port:                <unset> 80/TCP
TargetPort:          80/TCP
Endpoints:           10.244.2.5:80,10.244.3.4:80
Session Affinity:    None
Events:              <none>
```
```shell
kubectl get endpointslices -l kubernetes.io/service-name=my-nginx
```
```
NAME             ADDRESSTYPE   PORTS   ENDPOINTS               AGE
my-nginx-7vzhx   IPv4          80      10.244.2.5,10.244.3.4   21s
```

اکنون باید بتوانید از هر نودی در کلاستر خود با curl به Service مربوط به nginx در نشانی
`<CLUSTER-IP>:<PORT>` درخواست بفرستید. توجه کنید که IP سرویس کاملاً مجازی است و
هرگز روی سیم شبکه منتقل نمی‌شود. اگر کنجکاوید بدانید این سازوکار چگونه کار می‌کند،
می‌توانید دربارهٔ [پراکسی سرویس](/docs/reference/networking/virtual-ips/) بیشتر بخوانید.

## دسترسی به Service

کوبرنتیز از دو روش اصلی برای یافتن یک Service پشتیبانی می‌کند: متغیرهای محیطی
و DNS. روش اول بدون هیچ پیکربندی اضافه‌ای کار می‌کند، در حالی که روش دوم به
[افزونهٔ کلاستر CoreDNS](https://releases.k8s.io/v{{< skew currentPatchVersion >}}/cluster/addons/dns/coredns) نیاز دارد.

{{< alert color="info" title="Note" >}}
اگر متغیرهای محیطی سرویس را نمی‌خواهید (مثلاً به دلیل احتمال تداخل با متغیرهای مورد انتظار
برنامه، تعداد زیاد متغیرها برای پردازش، استفادهٔ صرف از DNS و مانند آن)، می‌توانید این حالت را
با تنظیم فلگ `enableServiceLinks` روی `false` در
[مشخصات پاد](/docs/reference/generated/kubernetes-api/v{{< skew latestVersion >}}/#pod-v1-core) غیرفعال کنید.
{{< /alert >}}


### متغیرهای محیطی

وقتی یک Pod روی یک نود اجرا می‌شود، kubelet برای هر Service فعال مجموعه‌ای از متغیرهای محیطی
را اضافه می‌کند. این موضوع مشکلی در ترتیب ایجاد پیش می‌آورد. برای اینکه دلیلش را ببینید،
محیط پادهای nginx در حال اجرای خود را بررسی کنید (نام Pod شما متفاوت خواهد بود):

```shell
kubectl exec my-nginx-3800858182-jr4a2 -- printenv | grep SERVICE
```
```
KUBERNETES_SERVICE_HOST=10.0.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
```

توجه کنید که هیچ اشاره‌ای به Service شما نشده است. دلیلش این است که رونوشت‌ها را پیش از
Service ایجاد کردید. عیب دیگر این کار آن است که زمان‌بند ممکن است هر دو Pod را روی یک ماشین
قرار دهد و اگر آن ماشین از کار بیفتد، کل Service شما از دسترس خارج می‌شود. می‌توانیم این کار را
به روش درست انجام دهیم: دو Pod را از بین می‌بریم و منتظر می‌مانیم تا Deployment دوباره آن‌ها را
ایجاد کند. این بار Service *پیش از* رونوشت‌ها وجود دارد. با این کار، پادهای شما در سطح زمان‌بند
بر اساس Service پخش می‌شوند (به شرط آنکه همهٔ نودهایتان ظرفیت یکسانی داشته باشند) و متغیرهای
محیطی درست نیز تنظیم می‌شوند:

```shell
kubectl scale deployment my-nginx --replicas=0; kubectl scale deployment my-nginx --replicas=2;

kubectl get pods -l run=my-nginx -o wide
```
```
NAME                        READY     STATUS    RESTARTS   AGE     IP            NODE
my-nginx-3800858182-e9ihh   1/1       Running   0          5s      10.244.2.7    kubernetes-minion-ljyd
my-nginx-3800858182-j4rm4   1/1       Running   0          5s      10.244.3.8    kubernetes-minion-905m
```

ممکن است متوجه شوید که نام پادها تغییر کرده است، زیرا آن‌ها از بین رفته و دوباره ایجاد شده‌اند.

```shell
kubectl exec my-nginx-3800858182-e9ihh -- printenv | grep SERVICE
```
```
KUBERNETES_SERVICE_PORT=443
MY_NGINX_SERVICE_HOST=10.0.162.149
KUBERNETES_SERVICE_HOST=10.0.0.1
MY_NGINX_SERVICE_PORT=80
KUBERNETES_SERVICE_PORT_HTTPS=443
```

### DNS

کوبرنتیز یک Service افزونهٔ کلاستر برای DNS ارائه می‌دهد که به‌طور خودکار به Serviceهای دیگر
نام DNS اختصاص می‌دهد. می‌توانید بررسی کنید که آیا این سرویس روی کلاستر شما در حال اجراست:

```shell
kubectl get services kube-dns --namespace=kube-system
```
```
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)         AGE
kube-dns   ClusterIP   10.0.0.10    <none>        53/UDP,53/TCP   8m
```

در ادامهٔ این بخش فرض می‌کنیم که یک Service با IP بلندمدت (my-nginx) و یک سرور DNS دارید
که به آن IP نامی اختصاص داده است. در اینجا از افزونهٔ کلاستر CoreDNS (با نام برنامهٔ `kube-dns`)
استفاده می‌کنیم، بنابراین می‌توانید از هر پادی در کلاستر خود و با روش‌های استاندارد
(مثلاً `gethostbyname()`) با Service ارتباط برقرار کنید.
اگر CoreDNS در حال اجرا نیست، می‌توانید با مراجعه به
[README پروژهٔ CoreDNS](https://github.com/coredns/deployment/tree/master/kubernetes)
یا [نصب CoreDNS](/docs/tasks/administer-cluster/coredns/#installing-coredns) آن را فعال کنید.
بیایید برای آزمودن این موضوع، یک برنامهٔ curl دیگر اجرا کنیم:

```shell
kubectl run curl --image=radial/busyboxplus:curl -i --tty --rm
```
```
Waiting for pod default/curl-131556218-9fnch to be running, status is Pending, pod ready: false
Hit enter for command prompt
```

سپس کلید Enter را بزنید و دستور `nslookup my-nginx` را اجرا کنید:

```shell
[ root@curl-131556218-9fnch:/ ]$ nslookup my-nginx
Server:    10.0.0.10
Address 1: 10.0.0.10

Name:      my-nginx
Address 1: 10.0.162.149
```

## ایمن‌سازی Service

تا اینجا فقط از درون کلاستر به سرور nginx دسترسی داشته‌ایم. پیش از آنکه Service را در اینترنت
در دسترس قرار دهید، باید مطمئن شوید که کانال ارتباطی امن است. برای این کار به موارد زیر نیاز دارید:

* گواهی‌های خودامضا (self-signed) برای https (مگر آنکه از قبل گواهی هویت داشته باشید)
* یک سرور nginx که برای استفاده از این گواهی‌ها پیکربندی شده باشد
* یک [Secret](/docs/concepts/configuration/secret/) که گواهی‌ها را در دسترس پادها قرار دهد

همهٔ این موارد را می‌توانید از
[مثال https برای nginx](https://github.com/kubernetes/examples/tree/master/_archived/https-nginx/) به دست آورید.
این کار به نصب ابزارهای go و make نیاز دارد. اگر نمی‌خواهید این ابزارها را نصب کنید،
مراحل دستی را که در ادامه آمده است دنبال کنید. به‌طور خلاصه:

```shell
make keys KEY=/tmp/nginx.key CERT=/tmp/nginx.crt
kubectl create secret tls nginxsecret --key /tmp/nginx.key --cert /tmp/nginx.crt
```
```
secret/nginxsecret created
```
```shell
kubectl get secrets
```
```
NAME                  TYPE                                  DATA      AGE
nginxsecret           kubernetes.io/tls                     2         1m
```
و همچنین ConfigMap را ایجاد کنید:
```shell
kubectl create configmap nginxconfigmap --from-file=default.conf
```

نمونه‌ای از فایل `default.conf` را می‌توانید در
[مخزن پروژهٔ مثال‌های کوبرنتیز](https://github.com/kubernetes/examples/tree/bc9ca4ca32bb28762ef216386934bef20f1f9930/staging/https-nginx/) پیدا کنید.

```
configmap/nginxconfigmap created
```
```shell
kubectl get configmaps
```
```
NAME             DATA   AGE
nginxconfigmap   1      114s
```

با دستور زیر می‌توانید جزئیات ConfigMap با نام `nginxconfigmap` را ببینید:

```shell
kubectl describe configmap  nginxconfigmap
```

خروجی مشابه زیر است:

```console
Name:         nginxconfigmap
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
default.conf:
----
server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        listen 443 ssl;

        root /usr/share/nginx/html;
        index index.html;

        server_name localhost;
        ssl_certificate /etc/nginx/ssl/tls.crt;
        ssl_certificate_key /etc/nginx/ssl/tls.key;

        location / {
                try_files $uri $uri/ =404;
        }
}

BinaryData
====

Events:  <none>
```

اگر در اجرای make با مشکل مواجه شدید (برای مثال در ویندوز)، مراحل دستی زیر را دنبال کنید:

```shell
# Create a public private key pair
openssl req -x509 -noenc -days 365 -newkey rsa:2048 -keyout /d/tmp/nginx.key -out /d/tmp/nginx.crt -subj "/CN=my-nginx/O=my-nginx"
# Convert the keys to base64 encoding
cat /d/tmp/nginx.crt | base64 | tr -d '\n'
cat /d/tmp/nginx.key | base64 | tr -d '\n'
```
 
از خروجی دستورهای قبلی برای ایجاد یک فایل YAML به شکل زیر استفاده کنید.
مقدار کدگذاری‌شده با base64 باید به‌طور کامل در یک خط باشد.

```yaml
apiVersion: "v1"
kind: "Secret"
metadata:
  name: "nginxsecret"
  namespace: "default"
type: kubernetes.io/tls
data:
 # NOTE: Replace the following values with your own base64-encoded certificate and key.
  tls.crt: "REPLACE_WITH_BASE64_CERT" 
  tls.key: "REPLACE_WITH_BASE64_KEY"
```
اکنون با استفاده از این فایل، Secretها را ایجاد کنید:

```shell
kubectl apply -f nginxsecrets.yaml
kubectl get secrets
```
```
NAME                  TYPE                                  DATA      AGE
nginxsecret           kubernetes.io/tls                     2         1m
```

اکنون رونوشت‌های nginx خود را طوری تغییر دهید که با استفاده از گواهی موجود در Secret یک سرور https
راه‌اندازی کنند، و Service را نیز طوری تغییر دهید که هر دو پورت (80 و 443) را در دسترس قرار دهد:

{{% code_sample file="service/networking/nginx-secure-app.yaml" %}}

نکات قابل‌توجه دربارهٔ مانیفست nginx-secure-app:

- این فایل مشخصات Deployment و Service را با هم در بر دارد.
- [سرور nginx](https://github.com/kubernetes/examples/blob/master/_archived/https-nginx/default.conf)
  ترافیک HTTP را روی پورت 80 و ترافیک HTTPS را روی پورت 443 سرویس می‌دهد و Service مربوط به nginx
  هر دو پورت را در دسترس قرار می‌دهد.
- هر کانتینر از طریق یک حجم (volume) که در مسیر `/etc/nginx/ssl` سوار (mount) شده است به کلیدها دسترسی دارد.
  این حجم *پیش از* راه‌اندازی سرور nginx آماده می‌شود.

```shell
kubectl delete deployments,svc my-nginx; kubectl create -f ./nginx-secure-app.yaml
```

اکنون می‌توانید از هر نودی به سرور nginx دسترسی داشته باشید.

```shell
kubectl get pods -l run=my-nginx -o custom-columns=POD_IP:.status.podIPs
    POD_IP
    [map[ip:10.244.3.5]]
```

```shell
node $ curl -k https://10.244.3.5
...
<h1>Welcome to nginx!</h1>
```

توجه کنید که در گام آخر پارامتر `-k` را به curl دادیم. دلیلش این است که هنگام تولید گواهی
هیچ اطلاعاتی دربارهٔ پادهایی که nginx را اجرا می‌کنند نداریم، پس باید به curl بگوییم عدم تطابق
CName را نادیده بگیرد. با ایجاد یک Service، مقدار CName به‌کاررفته در گواهی را به نام DNS واقعی‌ای
پیوند دادیم که پادها هنگام جست‌وجوی Service از آن استفاده می‌کنند. بیایید این را از درون یک پاد
بیازماییم (برای سادگی از همان Secret دوباره استفاده می‌شود؛ پاد برای دسترسی به Service فقط به
nginx.crt نیاز دارد):

{{% code_sample file="service/networking/curlpod.yaml" %}}

```shell
kubectl apply -f ./curlpod.yaml
kubectl get pods -l app=curlpod
```
```
NAME                               READY     STATUS    RESTARTS   AGE
curl-deployment-1515033274-1410r   1/1       Running   0          1m
```
```shell
kubectl exec curl-deployment-1515033274-1410r -- curl https://my-nginx --cacert /etc/nginx/ssl/tls.crt
...
<title>Welcome to nginx!</title>
...
```

## در دسترس قرار دادن Service

ممکن است بخواهید برای برخی بخش‌های برنامه‌هایتان، یک Service را روی یک نشانی IP خارجی
در دسترس قرار دهید. کوبرنتیز از دو روش برای این کار پشتیبانی می‌کند: NodePort و
LoadBalancer. سرویسی که در بخش قبل ایجاد شد از قبل از نوع `NodePort` استفاده می‌کرد،
بنابراین اگر نود شما IP عمومی داشته باشد، رونوشت HTTPS مربوط به nginx آمادهٔ سرویس‌دهی
به ترافیک اینترنت است.

```shell
kubectl get svc my-nginx -o yaml | grep nodePort -C 5
  uid: 07191fb3-f61a-11e5-8ae5-42010af00002
spec:
  clusterIP: 10.0.162.149
  ports:
  - name: http
    nodePort: 31704
    port: 8080
    protocol: TCP
    targetPort: 80
  - name: https
    nodePort: 32453
    port: 443
    protocol: TCP
    targetPort: 443
  selector:
    run: my-nginx
```
```shell
kubectl get nodes -o yaml | grep ExternalIP -C 1
    - address: 104.197.41.11
      type: ExternalIP
    allocatable:
--
    - address: 23.251.152.56
      type: ExternalIP
    allocatable:
...

$ curl https://<EXTERNAL-IP>:<NODE-PORT> -k
...
<h1>Welcome to nginx!</h1>
```

اکنون Service را دوباره طوری ایجاد کنیم که از یک متعادل‌کنندهٔ بار (load balancer) ابری استفاده کند.
مقدار `Type` در Service با نام `my-nginx` را از `NodePort` به `LoadBalancer` تغییر دهید:

```shell
kubectl edit svc my-nginx
kubectl get svc my-nginx
```
```
NAME       TYPE           CLUSTER-IP     EXTERNAL-IP        PORT(S)               AGE
my-nginx   LoadBalancer   10.0.162.149     xx.xxx.xxx.xxx     8080:30163/TCP        21s
```
```
curl https://<EXTERNAL-IP> -k
...
<title>Welcome to nginx!</title>
```

نشانی IP موجود در ستون `EXTERNAL-IP` همان نشانی‌ای است که در اینترنت عمومی در دسترس است.
مقدار `CLUSTER-IP` فقط درون کلاستر یا شبکهٔ ابر خصوصی شما در دسترس است.

توجه کنید که در AWS، نوع `LoadBalancer` یک ELB ایجاد می‌کند که به‌جای IP از یک نام میزبان
(طولانی) استفاده می‌کند. این نام در واقع آن‌قدر طولانی است که در خروجی استاندارد `kubectl get svc`
جا نمی‌شود، بنابراین برای دیدن آن باید دستور `kubectl describe service my-nginx` را اجرا کنید.
چیزی شبیه به این خواهید دید:

```shell
kubectl describe service my-nginx
...
LoadBalancer Ingress:   a320587ffd19711e5a37606cf4a74574-1142138393.us-east-1.elb.amazonaws.com
...
```



## {{% heading "whatsnext" %}}


* دربارهٔ [استفاده از Service برای دسترسی به یک برنامه در کلاستر](/docs/tasks/access-application-cluster/service-access-application-cluster/) بیشتر بیاموزید
* دربارهٔ [اتصال فرانت‌اند به بک‌اند با استفاده از Service](/docs/tasks/access-application-cluster/connecting-frontend-backend/) بیشتر بیاموزید
* دربارهٔ [ایجاد یک متعادل‌کنندهٔ بار خارجی](/docs/tasks/access-application-cluster/create-external-load-balancer/) بیشتر بیاموزید

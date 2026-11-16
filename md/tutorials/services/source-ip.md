---
title: استفاده از آی‌پی مبدأ
content_type: tutorial
min-kubernetes-server-version: v1.5
weight: 40
---

<!-- overview -->

برنامه‌هایی که در یک کلاستر کوبرنتیز اجرا می‌شوند، از طریق انتزاع Service یکدیگر و دنیای بیرون را پیدا می‌کنند و با آن‌ها ارتباط برقرار می‌کنند. این سند توضیح می‌دهد که چه اتفاقی برای آی‌پی مبدأ (source IP) بسته‌هایی می‌افتد که به انواع مختلف Serviceها ارسال می‌شوند. همچنین نشان می‌دهد چگونه می‌توانید این رفتار را بر اساس نیازهای خود تغییر دهید.



## {{% heading "prerequisites" %}}


### اصطلاحات

در این سند از اصطلاحات زیر استفاده می‌شود:

{{< comment >}}
اگر این بخش را بومی‌سازی می‌کنید، به صفحه‌های معادل ویکی‌پدیا در زبان مقصد پیوند دهید.
{{< /comment >}}

[ترجمهٔ نشانی شبکه (NAT)](https://en.wikipedia.org/wiki/Network_address_translation)
: ترجمهٔ نشانی شبکه (Network address translation)

[ترجمهٔ نشانی مبدأ (Source NAT)](https://en.wikipedia.org/wiki/Network_address_translation#SNAT)
: جایگزین کردن آی‌پی مبدأ یک بسته؛ در این صفحه، معمولاً به معنای جایگزین کردن آن با نشانی آی‌پی یک نود است.

[ترجمهٔ نشانی مقصد (Destination NAT)](https://en.wikipedia.org/wiki/Network_address_translation#DNAT)
: جایگزین کردن آی‌پی مقصد یک بسته؛ در این صفحه، معمولاً به معنای جایگزین کردن آن با نشانی آی‌پی یک {{< glossary_tooltip term_id="pod" >}} است.

[آی‌پی مجازی (VIP)](/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)
: یک نشانی آی‌پی مجازی، مانند نشانی‌ای که به هر {{< glossary_tooltip text="Service" term_id="service" >}} در کوبرنتیز اختصاص داده می‌شود.

[کامپوننت kube-proxy](/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies)
: یک دیمن شبکه که مدیریت آی‌پی‌های مجازی Serviceها را روی هر نود هماهنگ می‌کند.

### پیش‌نیازها

{{< include "task-tutorial-prereqs.md" >}}

در مثال‌ها از یک وب‌سرور کوچک nginx استفاده می‌شود که آی‌پی مبدأ درخواست‌های دریافتی را از طریق یک هدر HTTP بازمی‌گرداند. می‌توانید آن را به این صورت ایجاد کنید:

{{< alert color="info" title="Note" >}}
ایمیج به‌کاررفته در فرمان زیر فقط روی معماری‌های AMD64 اجرا می‌شود.
{{< /alert >}}

```shell
kubectl create deployment source-ip-app --image=registry.k8s.io/echoserver:1.10
```
خروجی به این صورت است:
```
deployment.apps/source-ip-app created
```


## {{% heading "objectives" %}}


* در دسترس قرار دادن یک برنامهٔ ساده از طریق انواع مختلف Serviceها
* درک نحوهٔ برخورد هر نوع Service با ترجمهٔ نشانی آی‌پی مبدأ
* درک مصالحه‌های مربوط به حفظ آی‌پی مبدأ




<!-- lessoncontent -->

## آی‌پی مبدأ برای Serviceهایی با `Type=ClusterIP`

اگر kube-proxy را در [حالت iptables](/docs/reference/networking/virtual-ips/#proxy-mode-iptables) (حالت پیش‌فرض) اجرا کنید، روی بسته‌هایی که از داخل کلاستر به ClusterIP ارسال می‌شوند هرگز ترجمهٔ نشانی مبدأ انجام نمی‌شود. برای اطلاع از حالت kube-proxy، می‌توانید نشانی `http://localhost:10249/proxyMode` را روی نودی که kube-proxy در آن اجرا می‌شود دریافت کنید.

```console
kubectl get nodes
```
خروجی مشابه زیر است:
```
NAME                           STATUS     ROLES    AGE     VERSION
kubernetes-node-6jst   Ready      <none>   2h      v1.13.0
kubernetes-node-cx31   Ready      <none>   2h      v1.13.0
kubernetes-node-jj1t   Ready      <none>   2h      v1.13.0
```

حالت پراکسی را روی یکی از نودها به دست آورید (kube-proxy روی پورت 10249 گوش می‌دهد):
```shell
# Run this in a shell on the node you want to query.
curl http://localhost:10249/proxyMode
```
خروجی به این صورت است:
```
iptables
```

برای آزمودن حفظ آی‌پی مبدأ، می‌توانید یک Service روی برنامهٔ source IP ایجاد کنید:

```shell
kubectl expose deployment source-ip-app --name=clusterip --port=80 --target-port=8080
```
خروجی به این صورت است:
```
service/clusterip exposed
```
```shell
kubectl get svc clusterip
```
خروجی مشابه زیر است:
```
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
clusterip    ClusterIP   10.0.170.92   <none>        80/TCP    51s
```

سپس از یک پاد در همان کلاستر به `ClusterIP` درخواست بفرستید:

```shell
kubectl run busybox -it --image=busybox:1.28 --restart=Never --rm
```
خروجی مشابه زیر است:
```
Waiting for pod default/busybox to be running, status is Pending, pod ready: false
If you don't see a command prompt, try pressing enter.

```
پس از آن می‌توانید یک فرمان را درون آن Pod اجرا کنید:

```shell
# Run this inside the terminal from "kubectl run"
ip addr
```
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc noqueue
    link/ether 0a:58:0a:f4:03:08 brd ff:ff:ff:ff:ff:ff
    inet 10.244.3.8/24 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::188a:84ff:feb0:26a5/64 scope link
       valid_lft forever preferred_lft forever
```

…سپس با `wget` از وب‌سرور محلی پرس‌وجو کنید:
```shell
# Replace "10.0.170.92" with the IPv4 address of the Service named "clusterip"
wget -qO - 10.0.170.92
```
```
CLIENT VALUES:
client_address=10.244.3.8
command=GET
...
```
مقدار `client_address` همیشه نشانی آی‌پی پاد کلاینت است، چه پاد کلاینت و پاد سرور روی یک نود باشند و چه روی نودهای متفاوت.

## آی‌پی مبدأ برای Serviceهایی با `Type=NodePort`

روی بسته‌هایی که به Serviceهایی با [`Type=NodePort`](/docs/concepts/services-networking/service/#type-nodeport) ارسال می‌شوند، به‌طور پیش‌فرض ترجمهٔ نشانی مبدأ انجام می‌شود. برای آزمودن این موضوع، یک Service از نوع `NodePort` ایجاد کنید:

```shell
kubectl expose deployment source-ip-app --name=nodeport --port=80 --target-port=8080 --type=NodePort
```
خروجی به این صورت است:
```
service/nodeport exposed
```

```shell
NODEPORT=$(kubectl get -o jsonpath="{.spec.ports[0].nodePort}" services nodeport)
NODES=$(kubectl get nodes -o jsonpath='{ $.items[*].status.addresses[?(@.type=="InternalIP")].address }')
```

اگر روی یک ارائه‌دهندهٔ ابری کار می‌کنید، ممکن است لازم باشد یک قاعدهٔ فایروال برای `nodes:nodeport` گزارش‌شده در بالا باز کنید.
اکنون می‌توانید از بیرون کلاستر و از طریق پورت نودی که در بالا تخصیص یافت، به Service دسترسی پیدا کنید.

```shell
for node in $NODES; do curl -s $node:$NODEPORT | grep -i client_address; done
```
خروجی مشابه زیر است:
```
client_address=10.180.1.1
client_address=10.240.0.5
client_address=10.240.0.3
```

توجه کنید که این‌ها آی‌پی‌های درست کلاینت نیستند، بلکه آی‌پی‌های داخلی کلاستر هستند. روند کار به این صورت است:

* کلاینت بسته را به `node2:nodePort` می‌فرستد
* نود `node2` نشانی آی‌پی مبدأ بسته را با نشانی آی‌پی خودش جایگزین می‌کند (SNAT)
* نود `node2` آی‌پی مقصد بسته را با آی‌پی پاد جایگزین می‌کند
* بسته به نود ۱ و سپس به نقطهٔ پایانی (endpoint) مسیریابی می‌شود
* پاسخ پاد دوباره به node2 مسیریابی می‌شود
* پاسخ پاد به کلاینت بازگردانده می‌شود

به‌صورت تصویری:

{{< figure src="/docs/images/tutor-service-nodePort-fig01.svg" alt="source IP nodeport figure 01" class="diagram-large" caption="Figure. Source IP Type=NodePort using SNAT" link="https://mermaid.live/edit#pako:eNqNkV9rwyAUxb-K3LysYEqS_WFYKAzat9GHdW9zDxKvi9RoMIZtlH732ZjSbE970cu5v3s86hFqJxEYfHjRNeT5ZcUtIbXRaMNN2hZ5vrYRqt52cSXV-4iMSuwkZiYtyX739EqWaahMQ-V1qPxDVLNOvkYrO6fj2dupWMR2iiT6foOKdEZoS5Q2hmVSStoH7w7IMqXUVOefWoaG3XVftHbGeZYVRbH6ZXJ47CeL2-qhxvt_ucTe1SUlpuMN6CX12XeGpLdJiaMMFFr0rdAyvvfxjHEIDbbIgcVSohKDCRy4PUV06KQIuJU6OA9MCdMjBTEEt_-2NbDgB7xAGy3i97VJPP0ABRmcqg" >}}


برای جلوگیری از این وضعیت، کوبرنتیز قابلیتی برای [حفظ آی‌پی مبدأ کلاینت](/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip) دارد. اگر مقدار `service.spec.externalTrafficPolicy` را برابر `Local` قرار دهید، آنگاه kube-proxy درخواست‌ها را فقط به نقطه‌های پایانی محلی پراکسی می‌کند و ترافیک را به نودهای دیگر هدایت نمی‌کند. این روش نشانی آی‌پی مبدأ اصلی را حفظ می‌کند. اگر هیچ نقطهٔ پایانی محلی وجود نداشته باشد، بسته‌های ارسال‌شده به نود دور ریخته می‌شوند؛ بنابراین در هر قاعدهٔ پردازش بسته‌ای که روی بسته‌های رسیده به نقطهٔ پایانی اعمال می‌کنید، می‌توانید به درستی آی‌پی مبدأ اتکا کنید.

فیلد `service.spec.externalTrafficPolicy` را به این صورت تنظیم کنید:

```shell
kubectl patch svc nodeport -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```
خروجی به این صورت است:
```
service/nodeport patched
```

اکنون آزمون را دوباره اجرا کنید:

```shell
for node in $NODES; do curl --connect-timeout 1 -s $node:$NODEPORT | grep -i client_address; done
```
خروجی مشابه زیر است:
```
client_address=198.51.100.79
```

توجه کنید که فقط یک پاسخ، آن هم با آی‌پی *درست* کلاینت، دریافت کردید؛ پاسخی که از تنها نودی آمده است که پاد نقطهٔ پایانی روی آن اجرا می‌شود.

روند کار به این صورت است:

* کلاینت بسته را به `node2:nodePort` می‌فرستد که هیچ نقطهٔ پایانی ندارد
* بسته دور ریخته می‌شود
* کلاینت بسته را به `node1:nodePort` می‌فرستد که نقطهٔ پایانی *دارد*
* نود node1 بسته را با آی‌پی مبدأ درست به نقطهٔ پایانی مسیریابی می‌کند

به‌صورت تصویری:


{{< figure src="/docs/images/tutor-service-nodePort-fig02.svg" alt="source IP nodeport figure 02" class="diagram-large" caption="Figure. Source IP Type=NodePort preserves client source IP address" link="" >}}

## آی‌پی مبدأ برای Serviceهایی با `Type=LoadBalancer`

روی بسته‌هایی که به Serviceهایی با [`Type=LoadBalancer`](/docs/concepts/services-networking/service/#loadbalancer) ارسال می‌شوند، به‌طور پیش‌فرض ترجمهٔ نشانی مبدأ انجام می‌شود؛ زیرا همهٔ نودهای قابل زمان‌بندی کوبرنتیز که در وضعیت `Ready` هستند، برای دریافت ترافیک متوازن‌شده واجد شرایط‌اند. بنابراین اگر بسته‌ها به نودی بدون نقطهٔ پایانی برسند، سیستم آن‌ها را به نودی *دارای* نقطهٔ پایانی پراکسی می‌کند و آی‌پی مبدأ بسته را با آی‌پی نود جایگزین می‌کند (همان‌طور که در بخش قبل توضیح داده شد).

برای آزمودن این موضوع، برنامهٔ source-ip-app را از طریق یک متوازن‌کنندهٔ بار (load balancer) در دسترس قرار دهید:

```shell
kubectl expose deployment source-ip-app --name=loadbalancer --port=80 --target-port=8080 --type=LoadBalancer
```
خروجی به این صورت است:
```
service/loadbalancer exposed
```

نشانی‌های آی‌پی Service را چاپ کنید:
```console
kubectl get svc loadbalancer
```
خروجی مشابه زیر است:
```
NAME           TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)   AGE
loadbalancer   LoadBalancer   10.0.65.118   203.0.113.140     80/TCP    5m
```

سپس یک درخواست به آی‌پی خارجی این Service بفرستید:

```shell
curl 203.0.113.140
```
خروجی مشابه زیر است:
```
CLIENT VALUES:
client_address=10.240.0.5
...
```

با این حال، اگر روی Google Kubernetes Engine/GCE کار می‌کنید، تنظیم همان فیلد `service.spec.externalTrafficPolicy` روی `Local` باعث می‌شود نودهای *بدون* نقطهٔ پایانی Service، با ناموفق کردن عمدی بررسی‌های سلامت، خود را از فهرست نودهای واجد شرایط برای دریافت ترافیک متوازن‌شده حذف کنند.

به‌صورت تصویری:

![آی‌پی مبدأ با externalTrafficPolicy](/images/docs/sourceip-externaltrafficpolicy.svg)

می‌توانید این موضوع را با تنظیم این حاشیه‌نویسی (annotation) بیازمایید:

```shell
kubectl patch svc loadbalancer -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```

باید بلافاصله ببینید که کوبرنتیز فیلد `service.spec.healthCheckNodePort` را تخصیص داده است:

```shell
kubectl get svc loadbalancer -o yaml | grep -i healthCheckNodePort
```
خروجی مشابه زیر است:
```yaml
  healthCheckNodePort: 32122
```

فیلد `service.spec.healthCheckNodePort` به پورتی روی هر نود اشاره می‌کند که بررسی سلامت را در مسیر `/healthz` ارائه می‌دهد. می‌توانید این را بیازمایید:

```shell
kubectl get pod -o wide -l app=source-ip-app
```
خروجی مشابه زیر است:
```
NAME                            READY     STATUS    RESTARTS   AGE       IP             NODE
source-ip-app-826191075-qehz4   1/1       Running   0          20h       10.180.1.136   kubernetes-node-6jst
```

با `curl` نقطهٔ پایانی `/healthz` را روی نودهای مختلف دریافت کنید:
```shell
# Run this locally on a node you choose
curl localhost:32122/healthz
```
```
1 Service Endpoints found
```

ممکن است روی نود دیگری نتیجهٔ متفاوتی بگیرید:
```shell
# Run this locally on a node you choose
curl localhost:32122/healthz
```
```
No Service Endpoints Found
```

یک کنترل‌کننده که روی {{< glossary_tooltip text="control plane" term_id="control-plane" >}} اجرا می‌شود، مسئول تخصیص متوازن‌کنندهٔ بار ابری است. همین کنترل‌کننده بررسی‌های سلامت HTTP را نیز تخصیص می‌دهد که به این پورت و مسیر روی هر نود اشاره می‌کنند. حدود ۱۰ ثانیه صبر کنید تا بررسی سلامت دو نودِ بدون نقطهٔ پایانی ناموفق شود، سپس با `curl` از نشانی IPv4 متوازن‌کنندهٔ بار پرس‌وجو کنید:

```shell
curl 203.0.113.140
```
خروجی مشابه زیر است:
```
CLIENT VALUES:
client_address=198.51.100.79
...
```

## پشتیبانی میان‌سکویی

فقط برخی از ارائه‌دهندگان ابری از حفظ آی‌پی مبدأ از طریق Serviceهایی با `Type=LoadBalancer` پشتیبانی می‌کنند.
ارائه‌دهندهٔ ابری‌ای که از آن استفاده می‌کنید ممکن است درخواست ایجاد متوازن‌کنندهٔ بار را به چند روش مختلف برآورده کند:

1. با یک پراکسی که اتصال کلاینت را خاتمه می‌دهد و اتصال جدیدی به نودها یا نقطه‌های پایانی شما باز می‌کند. در چنین مواردی، آی‌پی مبدأ همیشه آی‌پی متوازن‌کنندهٔ بار ابری خواهد بود، نه آی‌پی کلاینت.

2. با یک هدایت‌کنندهٔ بسته، به‌گونه‌ای که درخواست‌های کلاینت که به آی‌پی مجازی متوازن‌کنندهٔ بار فرستاده می‌شوند، با آی‌پی مبدأ کلاینت به نود برسند، نه با آی‌پی یک پراکسی میانی.

متوازن‌کننده‌های بار دستهٔ اول باید برای انتقال آی‌پی واقعی کلاینت، از پروتکلی توافق‌شده میان متوازن‌کنندهٔ بار و بک‌اند استفاده کنند؛ مانند هدرهای HTTP [Forwarded](https://tools.ietf.org/html/rfc7239#section-5.2) یا [X-FORWARDED-FOR](https://en.wikipedia.org/wiki/X-Forwarded-For)، یا [پروتکل proxy](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt).
متوازن‌کننده‌های بار دستهٔ دوم می‌توانند با ایجاد یک بررسی سلامت HTTP که به پورت ذخیره‌شده در فیلد `service.spec.healthCheckNodePort` آن Service اشاره می‌کند، از قابلیتی که در بالا توضیح داده شد بهره ببرند.



## {{% heading "cleanup" %}}


Serviceها را حذف کنید:

```shell
kubectl delete svc -l app=source-ip-app
```

آبجکت‌های Deployment، ReplicaSet و Pod را حذف کنید:

```shell
kubectl delete deployment source-ip-app
```



## {{% heading "whatsnext" %}}

* دربارهٔ [اتصال برنامه‌ها از طریق Serviceها](/docs/tutorials/services/connect-applications-service/) بیشتر بیاموزید
* نحوهٔ [ایجاد یک متوازن‌کنندهٔ بار خارجی](/docs/tasks/access-application-cluster/create-external-load-balancer/) را بخوانید

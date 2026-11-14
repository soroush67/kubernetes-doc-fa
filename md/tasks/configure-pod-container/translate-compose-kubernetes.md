---
reviewers:
- cdrage
title: تبدیل یک فایل Docker Compose به منابع کوبرنتیز
content_type: task
weight: 230
---

<!-- overview -->

ابزار Kompose چیست؟ این ابزار هر چیزی را که با Compose (یعنی Docker Compose) نوشته شده باشد، برای هماهنگ‌کننده‌های کانتینر (کوبرنتیز یا OpenShift) تبدیل می‌کند.

اطلاعات بیشتر را می‌توانید در وب‌سایت Kompose به نشانی [https://kompose.io/](https://kompose.io/) بیابید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## نصب Kompose

برای نصب Kompose چند روش وجود دارد. روش پیشنهادی ما دانلود فایل باینری از آخرین انتشار در GitHub است.

{{< tabs name="install_ways" >}}
{{% tab name="دانلود از GitHub" %}}

نسخه‌های Kompose در چرخه‌های سه‌هفته‌ای از طریق GitHub منتشر می‌شوند. همه انتشارهای فعلی را می‌توانید در [صفحه انتشارهای GitHub](https://github.com/kubernetes/kompose/releases) ببینید.

```sh
# Linux
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-linux-amd64 -o kompose

# macOS
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-darwin-amd64 -o kompose

# Windows
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-windows-amd64.exe -o kompose.exe

chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

به‌عنوان راه دیگر، می‌توانید [فایل فشرده tarball](https://github.com/kubernetes/kompose/releases) را دانلود کنید.

{{% /tab %}}
{{% tab name="ساخت از کد منبع" %}}

نصب با `go get` کد را از شاخه master، همراه با آخرین تغییرات در حال توسعه، دریافت می‌کند.

```sh
go get -u github.com/kubernetes/kompose
```

{{% /tab %}}
{{% tab name="Homebrew (macOS)" %}}

در macOS می‌توانید آخرین نسخه را با [Homebrew](https://brew.sh) نصب کنید:

```bash
brew install kompose
```

{{% /tab %}}
{{< /tabs >}}

## استفاده از Kompose

در چند گام، شما را از Docker Compose به کوبرنتیز می‌رسانیم. تنها چیزی که
نیاز دارید یک فایل `docker-compose.yml` موجود است.

1. به پوشه‌ای بروید که فایل `docker-compose.yml` شما در آن قرار دارد. اگر چنین فایلی ندارید، می‌توانید با فایل زیر آزمایش کنید.

   ```yaml

   services:

     redis-leader:
       container_name: redis-leader
       image: redis
       ports:
         - "6379"

     redis-replica:
       container_name: redis-replica
       image: redis
       ports:
         - "6379"
       command: redis-server --replicaof redis-leader 6379 --dir /tmp

     web:
       container_name: web
       image: quay.io/kompose/web
       ports:
         - "8080:8080"
       environment:
         - GET_HOSTS_FROM=dns
       labels:
         kompose.service.type: LoadBalancer
   ```

2. برای تبدیل فایل `docker-compose.yml` به فایل‌هایی که با `kubectl` قابل استفاده
   باشند، دستور `kompose convert` و سپس `kubectl apply -f <output file>` را اجرا کنید.

   ```bash
   kompose convert
   ```

   خروجی مشابه زیر است:

   ```none
   INFO Kubernetes file "redis-leader-service.yaml" created
   INFO Kubernetes file "redis-replica-service.yaml" created
   INFO Kubernetes file "web-tcp-service.yaml" created
   INFO Kubernetes file "redis-leader-deployment.yaml" created
   INFO Kubernetes file "redis-replica-deployment.yaml" created
   INFO Kubernetes file "web-deployment.yaml" created
   ```

   ```bash
    kubectl apply -f web-tcp-service.yaml,redis-leader-service.yaml,redis-replica-service.yaml,web-deployment.yaml,redis-leader-deployment.yaml,redis-replica-deployment.yaml
   ```

   خروجی مشابه زیر است:

   ```none
   deployment.apps/redis-leader created
   deployment.apps/redis-replica created
   deployment.apps/web created
   service/redis-leader created
   service/redis-replica created
   service/web-tcp created
   ```

    اکنون Deploymentهای شما در کوبرنتیز در حال اجرا هستند.

3. به برنامه خود دسترسی پیدا کنید.

   اگر در فرایند توسعه از `minikube` استفاده می‌کنید:

   ```bash
   minikube service web-tcp
   ```

   در غیر این صورت، بیایید ببینیم سرویس شما از چه IPای استفاده می‌کند!

   ```sh
   kubectl describe svc web-tcp
   ```

   ```none
    Name:                     web-tcp
    Namespace:                default
    Labels:                   io.kompose.service=web-tcp
    Annotations:              kompose.cmd: kompose convert
                              kompose.service.type: LoadBalancer
                              kompose.version: 1.33.0 (3ce457399)
    Selector:                 io.kompose.service=web
    Type:                     LoadBalancer
    IP Family Policy:         SingleStack
    IP Families:              IPv4
    IP:                       10.102.30.3
    IPs:                      10.102.30.3
    Port:                     8080  8080/TCP
    TargetPort:               8080/TCP
    NodePort:                 8080  31624/TCP
    Endpoints:                10.244.0.5:8080
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>
   ```

   اگر از یک ارائه‌دهنده ابری استفاده می‌کنید، IP شما در کنار `LoadBalancer Ingress` نمایش داده می‌شود.

   ```sh
   curl http://192.0.2.89
   ```
   
4. پاک‌سازی.

   پس از پایان آزمایش استقرار برنامه نمونه، کافی است دستور زیر را در پوسته خود اجرا کنید تا
   منابع استفاده‌شده حذف شوند.
   
   ```sh
   kubectl delete -f web-tcp-service.yaml,redis-leader-service.yaml,redis-replica-service.yaml,web-deployment.yaml,redis-leader-deployment.yaml,redis-replica-deployment.yaml
   ```

<!-- discussion -->

## راهنمای کاربر

- رابط خط فرمان (CLI)
  - [`kompose convert`](#kompose-convert)
- مستندات
  - [تبدیل‌های جایگزین](#alternative-conversions)
  - [برچسب‌ها](#labels)
  - [راه‌اندازی مجدد](#restart)
  - [نسخه‌های Docker Compose](#docker-compose-versions)

ابزار Kompose از دو ارائه‌دهنده پشتیبانی می‌کند: OpenShift و کوبرنتیز.
می‌توانید ارائه‌دهنده موردنظر را با گزینه سراسری `--provider` انتخاب کنید. اگر ارائه‌دهنده‌ای مشخص نشود، کوبرنتیز به‌طور پیش‌فرض انتخاب می‌شود.

## دستور `kompose convert`

ابزار Kompose از تبدیل فایل‌های Docker Compose نسخه‌های V1، V2 و V3 به آبجکت‌های کوبرنتیز و OpenShift پشتیبانی می‌کند.

### مثال `kompose convert` برای کوبرنتیز

```shell
kompose --file docker-voting.yml convert
```

```none
WARN Unsupported key networks - ignoring
WARN Unsupported key build - ignoring
INFO Kubernetes file "worker-svc.yaml" created
INFO Kubernetes file "db-svc.yaml" created
INFO Kubernetes file "redis-svc.yaml" created
INFO Kubernetes file "result-svc.yaml" created
INFO Kubernetes file "vote-svc.yaml" created
INFO Kubernetes file "redis-deployment.yaml" created
INFO Kubernetes file "result-deployment.yaml" created
INFO Kubernetes file "vote-deployment.yaml" created
INFO Kubernetes file "worker-deployment.yaml" created
INFO Kubernetes file "db-deployment.yaml" created
```

```shell
ls
```

```none
db-deployment.yaml  docker-compose.yml         docker-gitlab.yml  redis-deployment.yaml  result-deployment.yaml  vote-deployment.yaml  worker-deployment.yaml
db-svc.yaml         docker-voting.yml          redis-svc.yaml     result-svc.yaml        vote-svc.yaml           worker-svc.yaml
```

همچنین می‌توانید چند فایل docker-compose را هم‌زمان ارائه دهید:

```shell
kompose -f docker-compose.yml -f docker-guestbook.yml convert
```

```none
INFO Kubernetes file "frontend-service.yaml" created         
INFO Kubernetes file "mlbparks-service.yaml" created         
INFO Kubernetes file "mongodb-service.yaml" created          
INFO Kubernetes file "redis-master-service.yaml" created     
INFO Kubernetes file "redis-slave-service.yaml" created      
INFO Kubernetes file "frontend-deployment.yaml" created      
INFO Kubernetes file "mlbparks-deployment.yaml" created      
INFO Kubernetes file "mongodb-deployment.yaml" created       
INFO Kubernetes file "mongodb-claim0-persistentvolumeclaim.yaml" created
INFO Kubernetes file "redis-master-deployment.yaml" created  
INFO Kubernetes file "redis-slave-deployment.yaml" created   
```

```shell
ls
```

```none
mlbparks-deployment.yaml  mongodb-service.yaml                       redis-slave-service.jsonmlbparks-service.yaml  
frontend-deployment.yaml  mongodb-claim0-persistentvolumeclaim.yaml  redis-master-service.yaml
frontend-service.yaml     mongodb-deployment.yaml                    redis-slave-deployment.yaml
redis-master-deployment.yaml
```

وقتی چند فایل docker-compose ارائه شود، پیکربندی آن‌ها با هم ادغام می‌شود. هر پیکربندی مشترک با مقدار فایل بعدی بازنویسی می‌شود.

### مثال `kompose convert` برای OpenShift

```sh
kompose --provider openshift --file docker-voting.yml convert
```

```none
WARN [worker] Service cannot be created because of missing port.
INFO OpenShift file "vote-service.yaml" created             
INFO OpenShift file "db-service.yaml" created               
INFO OpenShift file "redis-service.yaml" created            
INFO OpenShift file "result-service.yaml" created           
INFO OpenShift file "vote-deploymentconfig.yaml" created    
INFO OpenShift file "vote-imagestream.yaml" created         
INFO OpenShift file "worker-deploymentconfig.yaml" created  
INFO OpenShift file "worker-imagestream.yaml" created       
INFO OpenShift file "db-deploymentconfig.yaml" created      
INFO OpenShift file "db-imagestream.yaml" created           
INFO OpenShift file "redis-deploymentconfig.yaml" created   
INFO OpenShift file "redis-imagestream.yaml" created        
INFO OpenShift file "result-deploymentconfig.yaml" created  
INFO OpenShift file "result-imagestream.yaml" created  
```

این ابزار همچنین از ایجاد buildconfig برای دستور build در یک سرویس پشتیبانی می‌کند. به‌طور پیش‌فرض، مخزن راه دور شاخه فعلی git به‌عنوان مخزن منبع و شاخه فعلی به‌عنوان شاخه منبع برای ساخت استفاده می‌شود. می‌توانید به‌ترتیب با گزینه‌های ``--build-repo`` و ``--build-branch`` مخزن و شاخه منبع دیگری را مشخص کنید.

```sh
kompose --provider openshift --file buildconfig/docker-compose.yml convert
```

```none
WARN [foo] Service cannot be created because of missing port.
INFO OpenShift Buildconfig using git@github.com:rtnpro/kompose.git::master as source.
INFO OpenShift file "foo-deploymentconfig.yaml" created     
INFO OpenShift file "foo-imagestream.yaml" created          
INFO OpenShift file "foo-buildconfig.yaml" created
```

{{< note >}}
اگر مصنوعات OpenShift را به‌صورت دستی با ``oc create -f`` ارسال می‌کنید، برای دور زدن این مشکل OpenShift باید مطمئن شوید که مصنوع imagestream را پیش از مصنوع buildconfig ارسال می‌کنید: https://github.com/openshift/origin/issues/4518 .
{{< /note >}}

## تبدیل‌های جایگزین

تبدیل پیش‌فرض `kompose`، آبجکت‌های [Deployment](/docs/concepts/workloads/controllers/deployment/) و [Service](/docs/concepts/services-networking/service/) کوبرنتیز را در قالب yaml تولید می‌کند. به‌عنوان گزینه جایگزین، می‌توانید با `-j` خروجی json تولید کنید. همچنین می‌توانید به‌جای آن‌ها آبجکت‌های [Replication Controller](/docs/concepts/workloads/controllers/replicationcontroller/)، [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) یا چارت‌های [Helm](https://github.com/helm/helm) تولید کنید.

```sh
kompose convert -j
INFO Kubernetes file "redis-svc.json" created
INFO Kubernetes file "web-svc.json" created
INFO Kubernetes file "redis-deployment.json" created
INFO Kubernetes file "web-deployment.json" created
```

فایل‌های `*-deployment.json` شامل آبجکت‌های Deployment هستند.

```sh
kompose convert --replication-controller
INFO Kubernetes file "redis-svc.yaml" created
INFO Kubernetes file "web-svc.yaml" created
INFO Kubernetes file "redis-replicationcontroller.yaml" created
INFO Kubernetes file "web-replicationcontroller.yaml" created
```

فایل‌های `*-replicationcontroller.yaml` شامل آبجکت‌های Replication Controller هستند. اگر می‌خواهید تعداد نسخه‌های تکثیری (replicas) را مشخص کنید (مقدار پیش‌فرض ۱ است)، از فلگ `--replicas` استفاده کنید: `kompose convert --replication-controller --replicas 3`.

```shell
kompose convert --daemon-set
INFO Kubernetes file "redis-svc.yaml" created
INFO Kubernetes file "web-svc.yaml" created
INFO Kubernetes file "redis-daemonset.yaml" created
INFO Kubernetes file "web-daemonset.yaml" created
```

فایل‌های `*-daemonset.yaml` شامل آبجکت‌های DaemonSet هستند.

اگر می‌خواهید چارتی برای استفاده با [Helm](https://github.com/kubernetes/helm) تولید کنید، دستور زیر را اجرا کنید:

```shell
kompose convert -c
```

```none
INFO Kubernetes file "web-svc.yaml" created
INFO Kubernetes file "redis-svc.yaml" created
INFO Kubernetes file "web-deployment.yaml" created
INFO Kubernetes file "redis-deployment.yaml" created
chart created in "./docker-compose/"
```

```shell
tree docker-compose/
```

```none
docker-compose
├── Chart.yaml
├── README.md
└── templates
    ├── redis-deployment.yaml
    ├── redis-svc.yaml
    ├── web-deployment.yaml
    └── web-svc.yaml
```

هدف از این ساختار چارت، فراهم کردن اسکلتی برای ساختن چارت‌های Helm شماست.

## برچسب‌ها

ابزار `kompose` از برچسب‌های مخصوص Kompose در فایل `docker-compose.yml` پشتیبانی می‌کند تا بتوانید رفتار یک سرویس را هنگام تبدیل به‌صراحت تعریف کنید.

- برچسب `kompose.service.type` نوع سرویسی را که باید ایجاد شود تعیین می‌کند.

  برای مثال:

  ```yaml
  version: "2"
  services:
    nginx:
      image: nginx
      dockerfile: foobar
      build: ./foobar
      cap_add:
        - ALL
      container_name: foobar
      labels:
        kompose.service.type: nodeport
  ```

- برچسب `kompose.service.expose` تعیین می‌کند که آیا سرویس باید از بیرون کلاستر در دسترس باشد یا نه. اگر مقدار آن "true" باشد، ارائه‌دهنده نقطه پایانی (endpoint) را به‌طور خودکار تنظیم می‌کند و هر مقدار دیگری به‌عنوان نام میزبان (hostname) در نظر گرفته می‌شود. اگر چند پورت در یک سرویس تعریف شده باشد، نخستین پورت برای در دسترس قرار گرفتن انتخاب می‌شود.
  - برای ارائه‌دهنده کوبرنتیز، یک منبع ingress ایجاد می‌شود و فرض بر این است که یک کنترل‌کننده ingress از قبل پیکربندی شده است.
  - برای ارائه‌دهنده OpenShift، یک route ایجاد می‌شود.

  برای مثال:

  ```yaml
  version: "2"
  services:
    web:
      image: tuna/docker-counter23
      ports:
      - "5000:5000"
      links:
      - redis
      labels:
        kompose.service.expose: "counter.example.com"
    redis:
      image: redis:3.0
      ports:
      - "6379"
  ```

گزینه‌هایی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از:

| کلید                  | مقدار                               |
|----------------------|-------------------------------------|
| kompose.service.type | nodeport / clusterip / loadbalancer |
| kompose.service.expose| true / hostname |

{{< note >}}
برچسب `kompose.service.type` فقط باید همراه با `ports` تعریف شود؛ در غیر این صورت `kompose` با خطا مواجه می‌شود.
{{< /note >}}

## راه‌اندازی مجدد

اگر می‌خواهید Podهای معمولی و بدون کنترل‌کننده ایجاد کنید، می‌توانید این کار را با ساختار `restart` در docker-compose تعریف کنید. در جدول زیر می‌بینید که با هر مقدار `restart` چه اتفاقی می‌افتد.

| `docker-compose` `restart` | آبجکت ایجادشده    | `restartPolicy` در Pod |
|----------------------------|-------------------|---------------------|
| `""`                       | آبجکت کنترل‌کننده | `Always`            |
| `always`                   | آبجکت کنترل‌کننده | `Always`            |
| `on-failure`               | Pod               | `OnFailure`         |
| `no`                       | Pod               | `Never`             |

{{< note >}}
آبجکت کنترل‌کننده می‌تواند `deployment` یا `replicationcontroller` باشد.
{{< /note >}}

برای مثال، سرویس `pival` در نمونه زیر به یک Pod تبدیل می‌شود. این کانتینر مقدار `pi` را محاسبه می‌کند.

```yaml
version: '2'

services:
  pival:
    image: perl
    command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
    restart: "on-failure"
```

### هشدار درباره پیکربندی‌های Deployment

اگر در فایل Docker Compose برای یک سرویس حجم (volume) مشخص شده باشد، راهبرد Deployment (در کوبرنتیز) یا DeploymentConfig (در OpenShift) به‌جای "RollingUpdate" (پیش‌فرض) به "Recreate" تغییر می‌کند. این کار برای جلوگیری از دسترسی هم‌زمان چند نمونه از یک سرویس به یک حجم انجام می‌شود.

اگر نام سرویس در فایل Docker Compose شامل `_` باشد (برای مثال `web_service`)، این نویسه با `-` جایگزین می‌شود و نام سرویس متناسب با آن تغییر می‌کند (برای مثال `web-service`). دلیل این کار Kompose آن است که کوبرنتیز اجازه استفاده از `_` را در نام آبجکت‌ها نمی‌دهد.

توجه داشته باشید که تغییر نام سرویس ممکن است برخی از فایل‌های `docker-compose` را از کار بیندازد.

## نسخه‌های Docker Compose

ابزار Kompose از نسخه‌های ۱، ۲ و ۳ Docker Compose پشتیبانی می‌کند. پشتیبانی ما از نسخه‌های 2.1 و 3.2 به دلیل ماهیت آزمایشی آن‌ها محدود است.

فهرست کامل سازگاری میان هر سه نسخه، همراه با فهرست همه کلیدهای ناسازگار Docker Compose، در [سند تبدیل](https://github.com/kubernetes/kompose/blob/master/docs/conversion.md) ما آمده است.

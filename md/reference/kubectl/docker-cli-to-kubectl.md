---
title: kubectl برای کاربران Docker
content_type: concept
reviewers:
- brendandburns
- thockin
weight: 50
---

<!-- overview -->
می‌توانید از ابزار خط فرمان کوبرنتیز، یعنی `kubectl`، برای تعامل با API Server استفاده کنید. اگر با ابزار خط فرمان Docker آشنا باشید، استفاده از kubectl ساده است. با این حال، میان دستورهای Docker و دستورهای kubectl چند تفاوت وجود دارد. در بخش‌های زیر یک زیردستور Docker نشان داده می‌شود و دستور معادل آن در `kubectl` شرح داده می‌شود.


<!-- body -->
## docker run

برای اجرای یک Deployment از nginx و در دسترس قرار دادن آن، به [kubectl create deployment](/docs/reference/generated/kubectl/kubectl-commands#-em-deployment-em-) مراجعه کنید.

docker:

```shell
docker run -d --restart=always -e DOMAIN=cluster --name nginx-app -p 80:80 nginx
```
```
55c103fa129692154a7652490236fee9be47d70a8dd562281ae7d2f9a339a6db
```

```shell
docker ps
```
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
55c103fa1296        nginx               "nginx -g 'daemon of…"   9 seconds ago       Up 9 seconds        0.0.0.0:80->80/tcp   nginx-app
```

kubectl:

```shell
# start the pod running nginx
kubectl create deployment --image=nginx nginx-app
```
```
deployment.apps/nginx-app created
```

```shell
# add env to nginx-app
kubectl set env deployment/nginx-app  DOMAIN=cluster
```
```
deployment.apps/nginx-app env updated
```

{{< note >}}
دستورهای `kubectl` نوع و نام منبعی را که ایجاد یا تغییر داده‌اند چاپ می‌کنند و می‌توان از آن‌ها در دستورهای بعدی استفاده کرد. پس از ایجاد یک Deployment می‌توانید یک Service جدید را در دسترس قرار دهید.
{{< /note >}}

```shell
# expose a port through with a service
kubectl expose deployment nginx-app --port=80 --name=nginx-http
```
```
service "nginx-http" exposed
```

با استفاده از kubectl می‌توانید یک [Deployment](/docs/concepts/workloads/controllers/deployment/) ایجاد کنید تا اطمینان حاصل شود که N پاد nginx را اجرا می‌کنند؛ در اینجا N تعداد replicaهایی است که در spec مشخص شده است و مقدار پیش‌فرض آن 1 است. همچنین می‌توانید یک [service](/docs/concepts/services-networking/service/) با یک انتخابگر (selector) ایجاد کنید که با برچسب‌های پادها مطابقت داشته باشد. برای اطلاعات بیشتر، به [استفاده از Service برای دسترسی به یک برنامه در کلاستر](/docs/tasks/access-application-cluster/service-access-application-cluster) مراجعه کنید.

به‌طور پیش‌فرض، ایمیج‌ها در پس‌زمینه اجرا می‌شوند، مشابه `docker run -d ...`. برای اجرای آن‌ها در پیش‌زمینه، از [`kubectl run`](/docs/reference/generated/kubectl/kubectl-commands/#run) برای ایجاد پاد استفاده کنید:
```shell
kubectl run [-i] [--tty] --attach <name> --image=<image>
```

برخلاف `docker run ...`، اگر `--attach` را مشخص کنید، `stdin`، `stdout` و `stderr` متصل می‌شوند. نمی‌توانید کنترل کنید که کدام جریان‌ها متصل شوند (`docker -a ...`).
برای جدا شدن از کانتینر، می‌توانید دنباله escape یعنی Ctrl+P و سپس Ctrl+Q را وارد کنید.

## docker ps

برای فهرست کردن آنچه در حال حاضر در حال اجراست، به [kubectl get](/docs/reference/generated/kubectl/kubectl-commands/#get) مراجعه کنید.

docker:

```shell
docker ps -a
```
```
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                     PORTS                NAMES
14636241935f        ubuntu:16.04        "echo test"              5 seconds ago        Exited (0) 5 seconds ago                        cocky_fermi
55c103fa1296        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute          0.0.0.0:80->80/tcp   nginx-app
```

kubectl:

```shell
kubectl get po
```
```
NAME                        READY     STATUS      RESTARTS   AGE
nginx-app-8df569cb7-4gd89   1/1       Running     0          3m
ubuntu                      0/1       Completed   0          20s
```

## docker attach

برای اتصال به فرایندی که از قبل در یک کانتینر در حال اجراست، به [kubectl attach](/docs/reference/generated/kubectl/kubectl-commands/#attach) مراجعه کنید.

docker:

```shell
docker ps
```
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
55c103fa1296        nginx               "nginx -g 'daemon of…"   5 minutes ago       Up 5 minutes        0.0.0.0:80->80/tcp   nginx-app
```

```shell
docker attach 55c103fa1296
...
```

kubectl:

```shell
kubectl get pods
```
```
NAME              READY     STATUS    RESTARTS   AGE
nginx-app-5jyvm   1/1       Running   0          10m
```

```shell
kubectl attach -it nginx-app-5jyvm
...
```

برای جدا شدن از کانتینر، می‌توانید دنباله escape یعنی Ctrl+P و سپس Ctrl+Q را وارد کنید.

## docker exec

برای اجرای یک دستور در یک کانتینر، به [kubectl exec](/docs/reference/generated/kubectl/kubectl-commands/#exec) مراجعه کنید.

docker:

```shell
docker ps
```
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
55c103fa1296        nginx               "nginx -g 'daemon of…"   6 minutes ago       Up 6 minutes        0.0.0.0:80->80/tcp   nginx-app
```
```shell
docker exec 55c103fa1296 cat /etc/hostname
```
```
55c103fa1296
```

kubectl:

```shell
kubectl get po
```
```
NAME              READY     STATUS    RESTARTS   AGE
nginx-app-5jyvm   1/1       Running   0          10m
```

```shell
kubectl exec nginx-app-5jyvm -- cat /etc/hostname
```
```
nginx-app-5jyvm
```

برای استفاده از دستورهای تعاملی:


docker:

```shell
docker exec -ti 55c103fa1296 /bin/sh
# exit
```

kubectl:

```shell
kubectl exec -ti nginx-app-5jyvm -- /bin/sh
# exit
```

برای اطلاعات بیشتر، به [دریافت یک شل در کانتینر در حال اجرا](/docs/tasks/debug/debug-application/get-shell-running-container/) مراجعه کنید.

## docker logs

برای دنبال کردن stdout/stderr یک فرایند در حال اجرا، به [kubectl logs](/docs/reference/generated/kubectl/kubectl-commands/#logs) مراجعه کنید.


docker:

```shell
docker logs -f a9e
```
```
192.168.9.1 - - [14/Jul/2015:01:04:02 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.35.0" "-"
192.168.9.1 - - [14/Jul/2015:01:04:03 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.35.0" "-"
```

kubectl:

```shell
kubectl logs -f nginx-app-zibvs
```
```
10.240.63.110 - - [14/Jul/2015:01:09:01 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.26.0" "-"
10.240.63.110 - - [14/Jul/2015:01:09:02 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.26.0" "-"
```

میان پادها و کانتینرها تفاوت اندکی وجود دارد؛ به‌طور پیش‌فرض، پادها در صورت خروج فرایندهایشان خاتمه نمی‌یابند. در عوض، پادها فرایند را دوباره راه‌اندازی می‌کنند. این رفتار مشابه گزینه `--restart=always` در docker run است، با یک تفاوت عمده: در docker، خروجی هر بار اجرای فرایند به خروجی قبلی افزوده می‌شود، اما در کوبرنتیز هر بار اجرا جداگانه است. برای مشاهده خروجی اجرای قبلی در کوبرنتیز، به این صورت عمل کنید:

```shell
kubectl logs --previous nginx-app-zibvs
```
```
10.240.63.110 - - [14/Jul/2015:01:09:01 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.26.0" "-"
10.240.63.110 - - [14/Jul/2015:01:09:02 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.26.0" "-"
```

برای اطلاعات بیشتر، به [معماری ثبت لاگ](/docs/concepts/cluster-administration/logging/) مراجعه کنید.

## docker stop and docker rm

برای متوقف کردن و حذف یک فرایند در حال اجرا، به [kubectl delete](/docs/reference/generated/kubectl/kubectl-commands/#delete) مراجعه کنید.

docker:

```shell
docker ps
```
```
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS              PORTS                         NAMES
a9ec34d98787        nginx               "nginx -g 'daemon of"  22 hours ago        Up 22 hours         0.0.0.0:80->80/tcp, 443/tcp   nginx-app
```

```shell
docker stop a9ec34d98787
```
```
a9ec34d98787
```

```shell
docker rm a9ec34d98787
```
```
a9ec34d98787
```

kubectl:

```shell
kubectl get deployment nginx-app
```
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
nginx-app    1/1     1            1           2m
```

```shell
kubectl get po -l app=nginx-app
```
```
NAME                         READY     STATUS    RESTARTS   AGE
nginx-app-2883164633-aklf7   1/1       Running   0          2m
```
```shell
kubectl delete deployment nginx-app
```
```
deployment "nginx-app" deleted
```

```shell
kubectl get po -l app=nginx-app
# Return nothing
```

{{< note >}}
هنگام استفاده از kubectl، پاد را مستقیماً حذف نمی‌کنید. ابتدا باید Deployment مالک آن پاد را حذف کنید. اگر پاد را مستقیماً حذف کنید، Deployment آن را دوباره ایجاد می‌کند.
{{< /note >}}

## docker login

در kubectl معادل مستقیمی برای `docker login` وجود ندارد. اگر می‌خواهید کوبرنتیز را با یک رجیستری خصوصی به کار ببرید، به [استفاده از رجیستری خصوصی](/docs/concepts/containers/images/#using-a-private-registry) مراجعه کنید.

## docker version

برای دریافت نسخه کلاینت و سرور، به [kubectl version](/docs/reference/generated/kubectl/kubectl-commands/#version) مراجعه کنید.

docker:

```shell
docker version
```
```
Client version: 1.7.0
Client API version: 1.19
Go version (client): go1.4.2
Git commit (client): 0baf609
OS/Arch (client): linux/amd64
Server version: 1.7.0
Server API version: 1.19
Go version (server): go1.4.2
Git commit (server): 0baf609
OS/Arch (server): linux/amd64
```

kubectl:

```shell
kubectl version
```
```
Client Version: version.Info{Major:"1", Minor:"6", GitVersion:"v1.6.9+a3d1dfa6f4335", GitCommit:"9b77fed11a9843ce3780f70dd251e92901c43072", GitTreeState:"dirty", BuildDate:"2017-08-29T20:32:58Z", OpenPaasKubernetesVersion:"v1.03.02", GoVersion:"go1.7.5", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"6", GitVersion:"v1.6.9+a3d1dfa6f4335", GitCommit:"9b77fed11a9843ce3780f70dd251e92901c43072", GitTreeState:"dirty", BuildDate:"2017-08-29T20:32:58Z", OpenPaasKubernetesVersion:"v1.03.02", GoVersion:"go1.7.5", Compiler:"gc", Platform:"linux/amd64"}
```

## docker info

برای دریافت اطلاعات متفرقه درباره محیط و پیکربندی، به [kubectl cluster-info](/docs/reference/generated/kubectl/kubectl-commands/#cluster-info) مراجعه کنید.

docker:

```shell
docker info
```
```
Containers: 40
Images: 168
Storage Driver: aufs
 Root Dir: /usr/local/google/docker/aufs
 Backing Filesystem: extfs
 Dirs: 248
 Dirperm1 Supported: false
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 3.13.0-53-generic
Operating System: Ubuntu 14.04.2 LTS
CPUs: 12
Total Memory: 31.32 GiB
Name: k8s-is-fun.mtv.corp.google.com
ID: ADUV:GCYR:B3VJ:HMPO:LNPQ:KD5S:YKFQ:76VN:IANZ:7TFV:ZBF4:BYJO
WARNING: No swap limit support
```

kubectl:

```shell
kubectl cluster-info
```
```
Kubernetes master is running at https://203.0.113.141
CoreDNS is running at https://203.0.113.141/api/v1/namespaces/kube-system/services/kube-dns/proxy
kubernetes-dashboard is running at https://203.0.113.141/api/v1/namespaces/kube-system/services/kubernetes-dashboard/proxy
Grafana is running at https://203.0.113.141/api/v1/namespaces/kube-system/services/monitoring-grafana/proxy
Heapster is running at https://203.0.113.141/api/v1/namespaces/kube-system/services/monitoring-heapster/proxy
InfluxDB is running at https://203.0.113.141/api/v1/namespaces/kube-system/services/monitoring-influxdb/proxy
```

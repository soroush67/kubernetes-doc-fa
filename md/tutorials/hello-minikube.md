---
title: سلام Minikube
content_type: tutorial
weight: 5
card:
  name: tutorials
  weight: 10
---

<!-- overview -->

این آموزش نشان می‌دهد که چگونه یک برنامهٔ نمونه را با استفاده از minikube روی کوبرنتیز اجرا کنید.
در این آموزش یک ایمیج کانتینر در اختیار شما قرار می‌گیرد که با استفاده از NGINX همهٔ درخواست‌ها را عیناً بازمی‌گرداند.

## {{% heading "objectives" %}}

* استقرار یک برنامهٔ نمونه روی minikube.
* اجرای برنامه.
* مشاهدهٔ لاگ‌های برنامه.

## {{% heading "prerequisites" %}}


در این آموزش فرض بر این است که `minikube` را از قبل راه‌اندازی کرده‌اید.
برای دستورالعمل‌های نصب، __گام ۱__ را در [شروع کار با minikube](https://minikube.sigs.k8s.io/docs/start/) ببینید.
{{< alert color="info" title="Note" >}}
فقط دستورالعمل‌های __گام ۱، نصب__ را اجرا کنید. باقی مراحل در همین صفحه پوشش داده شده است.
{{< /alert >}}

همچنین باید `kubectl` را نصب کنید.
برای دستورالعمل‌های نصب، [نصب ابزارها](/docs/tasks/tools/#kubectl) را ببینید.


<!-- lessoncontent -->

## ایجاد یک کلاستر minikube

```shell
minikube start
```

{{< alert color="info" title="Note" >}}
دستور `minikube start` یک کلاستر تک‌نودی ایجاد می‌کند. این نود هم نقش control plane و هم نقش نود کارگر (worker) را بر عهده دارد. این وضعیت با بسیاری از کلاسترهای عملیاتی (production) کوبرنتیز متفاوت است؛ در آن کلاسترها نودهای control plane معمولاً با استفاده از
[taintها](/docs/concepts/scheduling-eviction/taint-and-toleration/) از نودهای کارگر جدا می‌شوند یا اصلاً برای کاربر قابل مشاهده نیستند.
{{< /alert >}}

## بررسی وضعیت کلاستر minikube

وضعیت کلاستر minikube را بررسی کنید تا مطمئن شوید همهٔ مؤلفه‌ها در حال اجرا هستند.

```shell
minikube status
```
خروجی دستور بالا باید همهٔ مؤلفه‌ها را در وضعیت Running یا Configured نشان دهد، مانند نمونه خروجی زیر:

```
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

## باز کردن داشبورد

داشبورد کوبرنتیز را باز کنید. این کار را به دو روش می‌توانید انجام دهید:

{{< tabs name="dashboard" >}}
{{% tab name="اجرای مرورگر" %}}
یک ترمینال **جدید** باز کنید و دستور زیر را اجرا کنید:
```shell
# Start a new terminal, and leave this running.
minikube dashboard
```

اکنون به ترمینالی برگردید که دستور `minikube start` را در آن اجرا کردید.

{{< alert color="info" title="Note" >}}
دستور `dashboard` افزونهٔ داشبورد را فعال می‌کند و پراکسی را در مرورگر وب پیش‌فرض باز می‌کند.
در داشبورد می‌توانید منابع کوبرنتیز مانند Deployment و Service ایجاد کنید.

برای اینکه بدانید چگونه می‌توان از باز شدن مستقیم مرورگر از طریق ترمینال جلوگیری کرد و یک URL برای داشبورد وب به دست آورد، زبانهٔ «کپی و جای‌گذاری URL» را ببینید.

داشبورد به‌طور پیش‌فرض فقط از داخل شبکهٔ مجازی داخلی کوبرنتیز در دسترس است.
دستور `dashboard` یک پراکسی موقت ایجاد می‌کند تا داشبورد از بیرون شبکهٔ مجازی کوبرنتیز نیز در دسترس باشد.

برای متوقف کردن پراکسی، با زدن `Ctrl+C` از فرایند خارج شوید.
پس از خروج دستور، داشبورد همچنان در کلاستر کوبرنتیز در حال اجرا باقی می‌ماند.
می‌توانید دستور `dashboard` را دوباره اجرا کنید تا پراکسی دیگری برای دسترسی به داشبورد ایجاد شود.
{{< /alert >}}

{{% /tab %}}
{{% tab name="کپی و جای‌گذاری URL" %}}

اگر نمی‌خواهید minikube مرورگر وب را برایتان باز کند، زیرفرمان `dashboard` را همراه با فلگ
`--url` اجرا کنید. در این حالت، `minikube` یک URL در خروجی نمایش می‌دهد که می‌توانید آن را در مرورگر دلخواه خود باز کنید.

یک ترمینال **جدید** باز کنید و دستور زیر را اجرا کنید:
```shell
# Start a new terminal, and leave this running.
minikube dashboard --url
```

اکنون می‌توانید از این URL استفاده کنید و به ترمینالی برگردید که دستور `minikube start` را در آن اجرا کردید.

{{% /tab %}}
{{< /tabs >}}

## ایجاد یک Deployment

هر [*Pod*](/docs/concepts/workloads/pods/) در کوبرنتیز گروهی از یک یا چند کانتینر است
که برای اهداف مدیریتی و شبکه‌ای به هم پیوند خورده‌اند. Pod این آموزش
فقط یک کانتینر دارد. هر
[*Deployment*](/docs/concepts/workloads/controllers/deployment/) در کوبرنتیز سلامت
Pod شما را بررسی می‌کند و در صورت خاتمه یافتن کانتینر Pod، آن را دوباره راه‌اندازی می‌کند. استفاده از Deploymentها
روش توصیه‌شده برای مدیریت ایجاد و مقیاس‌دهی Podها است.

1. با استفاده از دستور `kubectl create` یک Deployment ایجاد کنید که یک Pod را مدیریت می‌کند. این
   Pod یک کانتینر را بر پایهٔ ایمیج Docker ارائه‌شده اجرا می‌کند.

    ```shell
    # Run a test container image that includes a webserver
    kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.53 -- /agnhost netexec --http-port=8080
    ```

1. Deployment را مشاهده کنید:

    ```shell
    kubectl get deployments
    ```

    خروجی مشابه زیر است:

    ```
    NAME         READY   UP-TO-DATE   AVAILABLE   AGE
    hello-node   1/1     1            1           1m
    ```

    (ممکن است مدتی طول بکشد تا Pod در دسترس قرار گیرد. اگر مقدار «0/1» را می‌بینید، چند ثانیه بعد دوباره امتحان کنید.)

1. Pod را مشاهده کنید:

    ```shell
    kubectl get pods
    ```

    خروجی مشابه زیر است:

    ```
    NAME                          READY     STATUS    RESTARTS   AGE
    hello-node-5f76cf6ccf-br9b5   1/1       Running   0          1m
    ```

1. رویدادهای کلاستر را مشاهده کنید:

    ```shell
    kubectl get events
    ```

1. پیکربندی `kubectl` را مشاهده کنید:

    ```shell
    kubectl config view
    ```

1. لاگ‌های برنامهٔ یک کانتینر را در یک Pod مشاهده کنید (نام Pod را با نامی که از `kubectl get pods` به دست آوردید جایگزین کنید).

   {{< alert color="info" title="Note" >}}
   در دستور `kubectl logs`، عبارت `hello-node-5f76cf6ccf-br9b5` را با نام Pod در خروجی دستور `kubectl get pods` جایگزین کنید.
   {{< /alert >}}

   ```shell
   kubectl logs hello-node-5f76cf6ccf-br9b5
   ```

   خروجی مشابه زیر است:

   ```
   I0911 09:19:26.677397       1 log.go:195] Started HTTP server on port 8080
   I0911 09:19:26.677586       1 log.go:195] Started UDP server on port  8081
   ```


{{< alert color="info" title="Note" >}}
برای اطلاعات بیشتر دربارهٔ دستورهای `kubectl`، [مروری بر kubectl](/docs/reference/kubectl/) را ببینید.
{{< /alert >}}

## ایجاد یک Service

به‌طور پیش‌فرض، Pod فقط از طریق نشانی IP داخلی خود و از درون
کلاستر کوبرنتیز در دسترس است. برای اینکه کانتینر `hello-node` از بیرون
شبکهٔ مجازی کوبرنتیز در دسترس باشد، باید Pod را در قالب یک
[*Service*](/docs/concepts/services-networking/service/) کوبرنتیز در معرض دسترسی قرار دهید.

{{< alert color="danger" title="Warning" >}}
کانتینر agnhost یک endpoint با مسیر `/shell` دارد که برای
اشکال‌زدایی مفید است، اما قرار دادن آن در معرض اینترنت عمومی خطرناک است. این کانتینر را روی
کلاستری که به اینترنت دسترسی دارد یا روی کلاستر عملیاتی اجرا نکنید.
{{< /alert >}}

1. با استفاده از دستور `kubectl expose`، Pod را در معرض اینترنت عمومی قرار دهید:

    ```shell
    kubectl expose deployment hello-node --type=LoadBalancer --port=8080
    ```

    فلگ `--type=LoadBalancer` نشان می‌دهد که می‌خواهید Service خود را
    بیرون از کلاستر در دسترس قرار دهید.

    کد برنامه در ایمیج آزمایشی فقط به پورت TCP شمارهٔ 8080 گوش می‌دهد. اگر با
    `kubectl expose` پورت دیگری را در معرض دسترسی قرار دهید، کلاینت‌ها نمی‌توانند به آن پورت متصل شوند.

2. Service ایجادشده را مشاهده کنید:

    ```shell
    kubectl get services
    ```

    خروجی مشابه زیر است:

    ```
    NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    hello-node   LoadBalancer   10.108.144.78   <pending>     8080:30369/TCP   21s
    kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          23m
    ```

    در ارائه‌دهندگان ابری که از متعادل‌کننده‌های بار (load balancer) پشتیبانی می‌کنند،
    یک نشانی IP خارجی برای دسترسی به Service تخصیص داده می‌شود. در minikube،
    نوع `LoadBalancer` باعث می‌شود Service از طریق دستور `minikube service`
    در دسترس باشد.

3. دستور زیر را اجرا کنید:

    ```shell
    minikube service hello-node
    ```

    با این دستور، یک پنجرهٔ مرورگر باز می‌شود که برنامهٔ شما را ارائه می‌دهد و پاسخ برنامه را نشان می‌دهد.

## فعال کردن افزونه‌ها

ابزار minikube شامل مجموعه‌ای از {{< glossary_tooltip text="افزونه‌های" term_id="addons" >}} داخلی است که می‌توان آن‌ها را در محیط محلی کوبرنتیز فعال، غیرفعال و باز کرد.

1. افزونه‌هایی را که در حال حاضر پشتیبانی می‌شوند فهرست کنید:

    ```shell
    minikube addons list
    ```

    خروجی مشابه زیر است:

    ```
    addon-manager: enabled
    dashboard: enabled
    default-storageclass: enabled
    efk: disabled
    freshpod: disabled
    gvisor: disabled
    helm-tiller: disabled
    ingress: disabled
    ingress-dns: disabled
    logviewer: disabled
    metrics-server: disabled
    nvidia-driver-installer: disabled
    nvidia-gpu-device-plugin: disabled
    registry: disabled
    registry-creds: disabled
    storage-provisioner: enabled
    storage-provisioner-gluster: disabled
    ```

1. یک افزونه، برای مثال `metrics-server`، را فعال کنید:

    ```shell
    minikube addons enable metrics-server
    ```

    خروجی مشابه زیر است:

    ```
    The 'metrics-server' addon is enabled
    ```

1. Pod و Serviceای را که با نصب این افزونه ایجاد شده‌اند مشاهده کنید:

    ```shell
    kubectl get pod,svc -n kube-system
    ```

    خروجی مشابه زیر است:

    ```
    NAME                                        READY     STATUS    RESTARTS   AGE
    pod/coredns-5644d7b6d9-mh9ll                1/1       Running   0          34m
    pod/coredns-5644d7b6d9-pqd2t                1/1       Running   0          34m
    pod/metrics-server-67fb648c5                1/1       Running   0          26s
    pod/etcd-minikube                           1/1       Running   0          34m
    pod/influxdb-grafana-b29w8                  2/2       Running   0          26s
    pod/kube-addon-manager-minikube             1/1       Running   0          34m
    pod/kube-apiserver-minikube                 1/1       Running   0          34m
    pod/kube-controller-manager-minikube        1/1       Running   0          34m
    pod/kube-proxy-rnlps                        1/1       Running   0          34m
    pod/kube-scheduler-minikube                 1/1       Running   0          34m
    pod/storage-provisioner                     1/1       Running   0          34m

    NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
    service/metrics-server         ClusterIP   10.96.241.45    <none>        80/TCP              26s
    service/kube-dns               ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP       34m
    service/monitoring-grafana     NodePort    10.99.24.54     <none>        80:30002/TCP        26s
    service/monitoring-influxdb    ClusterIP   10.111.169.94   <none>        8083/TCP,8086/TCP   26s
    ```

1. خروجی `metrics-server` را بررسی کنید:

    ```shell
    kubectl top pods
    ```

    خروجی مشابه زیر است:

    ```
    NAME                         CPU(cores)   MEMORY(bytes)
    hello-node-ccf4b9788-4jn97   1m           6Mi
    ```

    اگر پیام زیر را می‌بینید، کمی صبر کنید و دوباره امتحان کنید:

    ```
    error: Metrics API not available
    ```

1. افزونهٔ `metrics-server` را غیرفعال کنید:

    ```shell
    minikube addons disable metrics-server
    ```

    خروجی مشابه زیر است:

    ```
    metrics-server was successfully disabled
    ```

## پاک‌سازی

اکنون می‌توانید منابعی را که در کلاستر خود ایجاد کرده‌اید پاک کنید:

```shell
kubectl delete service hello-node
kubectl delete deployment hello-node
```

کلاستر Minikube را متوقف کنید:

```shell
minikube stop
```

در صورت تمایل، ماشین مجازی Minikube را حذف کنید:

```shell
# Optional
minikube delete
```

اگر می‌خواهید برای یادگیری بیشتر دربارهٔ کوبرنتیز دوباره از minikube استفاده کنید، نیازی به حذف آن ندارید.

## جمع‌بندی

در این صفحه، جنبه‌های اصلی راه‌اندازی و اجرای یک کلاستر minikube پوشش داده شد. اکنون آماده‌اید که برنامه‌ها را مستقر کنید.

## {{% heading "whatsnext" %}}


* آموزش _[استقرار نخستین برنامهٔ خود روی کوبرنتیز با kubectl](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)_.
* دربارهٔ [آبجکت‌های Deployment](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.
* دربارهٔ [استقرار برنامه‌ها](/docs/tasks/run-application/run-stateless-application-deployment/) بیشتر بیاموزید.
* دربارهٔ [آبجکت‌های Service](/docs/concepts/services-networking/service/) بیشتر بیاموزید.

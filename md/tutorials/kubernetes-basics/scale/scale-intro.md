---
title: اجرای چندین نمونه از برنامه‌تان
weight: 10
---

## {{% heading "objectives" %}}

* مقیاس‌دهی دستی یک برنامهٔ موجود با استفاده از kubectl.

## {{% heading "prerequisites" %}}

دستورهای پوسته در این آموزش از نحو پوستهٔ POSIX استفاده می‌کنند که پوسته‌های پیش‌فرض بیشتر سیستم‌های لینوکس و macOS (برای مثال bash، zsh یا sh) از آن پشتیبانی می‌کنند. کاربران ویندوز برای اجرای دستورها به همان شکلی که نوشته شده‌اند، باید از یک پوستهٔ سازگار با POSIX مانند [زیرسیستم ویندوز برای لینوکس (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) یا [Git Bash](https://gitforwindows.org/) استفاده کنند. دستورهایی که از `export`، `$()` و ساختارهای مشابه استفاده می‌کنند، با PowerShell یا Command Prompt ویندوز سازگار **نیستند**.



## مقیاس‌دهی یک برنامه

{{% alert %}}
_می‌توانید از همان ابتدا با استفاده از پارامتر ‎--replicas در دستور kubectl create deployment، یک Deployment با چندین نمونه ایجاد کنید._
{{% /alert %}}

پیش‌تر یک [Deployment](/docs/concepts/workloads/controllers/deployment/) ایجاد کردیم و سپس آن را از طریق یک [Service](/docs/concepts/services-networking/service/) به‌صورت عمومی در دسترس قرار دادیم. آن Deployment تنها یک Pod برای اجرای برنامهٔ ما ایجاد کرد. هنگامی که ترافیک افزایش می‌یابد، باید برنامه را مقیاس‌دهی کنیم تا پاسخگوی تقاضای کاربران باشد.

اگر بخش‌های قبلی را انجام نداده‌اید، از [استفاده از minikube برای ایجاد یک کلاستر](/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/) شروع کنید.

_مقیاس‌دهی_ با تغییر تعداد رونوشت‌ها (replicas) در یک Deployment انجام می‌شود.

{{< alert color="info" title="Note" >}}
اگر این بخش را پس از [بخش قبلی](/docs/tutorials/kubernetes-basics/expose/expose-intro/) امتحان می‌کنید، ممکن است سرویسی را که ایجاد کرده بودید حذف کرده باشید یا یک Service از نوع `type: NodePort` ایجاد کرده باشید. در این بخش فرض بر این است که یک سرویس با `type: LoadBalancer` برای Deployment با نام kubernetes-bootcamp ایجاد شده است.

اگر Service ایجادشده در [بخش قبلی](/docs/tutorials/kubernetes-basics/expose/expose-intro) را حذف _نکرده‌اید_، ابتدا آن Service را حذف کنید و سپس دستور زیر را اجرا کنید تا یک Service جدید با `type` برابر با `LoadBalancer` ایجاد شود:

```shell
kubectl expose deployment/kubernetes-bootcamp --type="LoadBalancer" --port 8080
```
{{< /alert >}}

## نمای کلی مقیاس‌دهی

<!-- animation -->
{{< tutorials/carousel id="myCarousel" interval="3000" >}}
  {{< tutorials/carousel-item
      image="/docs/tutorials/kubernetes-basics/public/images/module_05_scaling1.svg"
      active="true" >}}

  {{< tutorials/carousel-item
      image="/docs/tutorials/kubernetes-basics/public/images/module_05_scaling2.svg" >}}
{{< /tutorials/carousel >}}

{{% alert %}}
_مقیاس‌دهی با تغییر تعداد رونوشت‌ها در یک Deployment انجام می‌شود._
{{% /alert %}}

با افزایش مقیاس یک Deployment، اطمینان حاصل می‌شود که Podهای جدید ایجاد شده و روی نودهایی با منابع در دسترس زمان‌بندی می‌شوند. مقیاس‌دهی، تعداد Podها را به وضعیت مطلوب جدید می‌رساند. کوبرنتیز از [مقیاس‌دهی خودکار](/docs/concepts/workloads/autoscaling/) Podها نیز پشتیبانی می‌کند، اما این موضوع خارج از محدودهٔ این آموزش است. مقیاس‌دهی تا صفر نیز امکان‌پذیر است و در این حالت همهٔ Podهای Deployment مشخص‌شده خاتمه می‌یابند.

اجرای چندین نمونه از یک برنامه نیازمند روشی برای توزیع ترافیک میان همهٔ آن‌ها است. هر Service یک متعادل‌کنندهٔ بار (load-balancer) یکپارچه دارد که ترافیک شبکه را میان همهٔ Podهای یک Deployment در دسترس قرارگرفته توزیع می‌کند. سرویس‌ها با استفاده از endpointها به‌طور پیوسته Podهای در حال اجرا را پایش می‌کنند تا اطمینان حاصل شود که ترافیک فقط به Podهای در دسترس ارسال می‌شود.

هنگامی که چندین نمونه از یک برنامه در حال اجرا باشد، می‌توانید به‌روزرسانی‌های تدریجی (Rolling updates) را بدون توقف سرویس انجام دهید. این موضوع را در بخش بعدی آموزش پوشش خواهیم داد. اکنون به ترمینال برویم و برنامه‌مان را مقیاس‌دهی کنیم.

### مقیاس‌دهی یک Deployment

برای فهرست کردن Deploymentهای خود، از زیردستور `get deployments` استفاده کنید:

```shell
kubectl get deployments
```

خروجی باید مشابه زیر باشد:

```
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   1/1     1            1           11m
```

باید ۱ Pod داشته باشیم. در غیر این صورت، دستور را دوباره اجرا کنید. این خروجی موارد زیر را نشان می‌دهد:

* ستون _NAME_ نام Deploymentهای موجود در کلاستر را فهرست می‌کند.
* ستون _READY_ نسبت رونوشت‌های CURRENT/DESIRED (فعلی/مطلوب) را نشان می‌دهد.
* ستون _UP-TO-DATE_ تعداد رونوشت‌هایی را نشان می‌دهد که برای رسیدن به وضعیت مطلوب به‌روزرسانی شده‌اند.
* ستون _AVAILABLE_ نشان می‌دهد چه تعداد رونوشت از برنامه در دسترس کاربران شما است.
* ستون _AGE_ مدت زمانی را نشان می‌دهد که برنامه در حال اجرا بوده است.

برای مشاهدهٔ ReplicaSet ایجادشده توسط Deployment، دستور زیر را اجرا کنید:

```shell
kubectl get rs
```

توجه کنید که نام ReplicaSet همیشه به قالب <nobr>[DEPLOYMENT-NAME]-[RANDOM-STRING]</nobr> است. رشتهٔ تصادفی به‌صورت تصادفی تولید می‌شود و از pod-template-hash به‌عنوان بذر (seed) استفاده می‌کند.

دو ستون مهم این خروجی عبارت‌اند از:

* ستون _DESIRED_ تعداد مطلوب رونوشت‌های برنامه را نشان می‌دهد که هنگام ایجاد Deployment تعریف می‌کنید. این همان وضعیت مطلوب است.
* ستون _CURRENT_ نشان می‌دهد در حال حاضر چه تعداد رونوشت در حال اجرا است.

در ادامه، Deployment را به ۴ رونوشت مقیاس‌دهی می‌کنیم. از دستور `kubectl scale` استفاده می‌کنیم و پس از آن نوع Deployment، نام آن و تعداد مطلوب نمونه‌ها را می‌آوریم:

```shell
kubectl scale deployments/kubernetes-bootcamp --replicas=4
```

برای فهرست کردن دوبارهٔ Deploymentهای خود، از `get deployments` استفاده کنید:

```shell
kubectl get deployments
```

تغییر اعمال شد و اکنون ۴ نمونه از برنامه در دسترس داریم. در ادامه بررسی می‌کنیم که آیا تعداد Podها تغییر کرده است یا نه:

```shell
kubectl get pods -o wide
```

اکنون ۴ Pod با نشانی‌های IP متفاوت وجود دارد. این تغییر در لاگ رویدادهای Deployment ثبت شده است. برای بررسی آن، از زیردستور `describe` استفاده کنید:

```shell
kubectl describe deployments/kubernetes-bootcamp
```

در خروجی این دستور نیز می‌توانید ببینید که اکنون ۴ رونوشت وجود دارد.

### متعادل‌سازی بار

بیایید بررسی کنیم که آیا Service ترافیک را متعادل‌سازی می‌کند یا نه. برای یافتن IP و پورت در دسترس قرارگرفته، می‌توانیم همان‌طور که در بخش قبلی آموزش یاد گرفتیم از `describe service` استفاده کنیم:

```shell
kubectl describe services/kubernetes-bootcamp
```

یک متغیر محیطی با نام NODE_PORT ایجاد کنید که مقدار آن برابر با پورت نود باشد:

```shell
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo NODE_PORT=$NODE_PORT
```

در ادامه، با `curl` به نشانی IP و پورت در دسترس قرارگرفته درخواست می‌فرستیم. دستور را چندین بار اجرا کنید:

```shell
curl http://"$(minikube ip):$NODE_PORT"
```

هر درخواست به یک Pod متفاوت می‌رسد. این نشان می‌دهد که متعادل‌سازی بار کار می‌کند.

خروجی باید مشابه زیر باشد:

```
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-644c5687f4-wp67j | v=1
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-644c5687f4-hs9dj | v=1
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-644c5687f4-4hjvf | v=1
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-644c5687f4-wp67j | v=1
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-644c5687f4-4hjvf | v=1
```

{{< alert color="info" title="Note" >}}
اگر minikube را با Docker Desktop به‌عنوان درایور کانتینر اجرا می‌کنید، به یک تونل minikube نیاز است. دلیل این امر آن است که کانتینرهای درون Docker Desktop از رایانهٔ میزبان شما جدا هستند.

در یک پنجرهٔ ترمینال جداگانه، دستور زیر را اجرا کنید:

```shell
minikube service kubernetes-bootcamp --url
```

خروجی به این شکل است:

```
http://127.0.0.1:51082
!  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

سپس با استفاده از URL داده‌شده به برنامه دسترسی پیدا کنید:

```shell
curl 127.0.0.1:51082
```
{{< /alert >}}

### کاهش مقیاس

برای کاهش مقیاس Deployment به ۲ رونوشت، دوباره زیردستور `scale` را اجرا کنید:

```shell
kubectl scale deployments/kubernetes-bootcamp --replicas=2
```

برای بررسی اعمال شدن تغییر، Deploymentها را با زیردستور `get deployments` فهرست کنید:

```shell
kubectl get deployments
```

تعداد رونوشت‌ها به ۲ کاهش یافت. Podها را با `get pods` فهرست کنید:

```shell
kubectl get pods -o wide
```

این خروجی تأیید می‌کند که ۲ Pod خاتمه یافته‌اند.

## {{% heading "whatsnext" %}}

* آموزش [انجام یک به‌روزرسانی تدریجی](/docs/tutorials/kubernetes-basics/update/update-intro/).
* دربارهٔ [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/) بیشتر بیاموزید.
* دربارهٔ [مقیاس‌دهی خودکار](/docs/concepts/workloads/autoscaling/) بیشتر بیاموزید.

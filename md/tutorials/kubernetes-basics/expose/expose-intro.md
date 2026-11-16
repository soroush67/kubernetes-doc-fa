---
title: استفاده از Service برای در دسترس قرار دادن برنامه
weight: 10
---

## {{% heading "objectives" %}}

* با Service در کوبرنتیز آشنا شوید.
* رابطهٔ برچسب‌ها و انتخابگرها (selector) با Service را درک کنید.
* یک برنامه را خارج از کلاستر کوبرنتیز در دسترس قرار دهید.

## {{% heading "prerequisites" %}}

دستورهای پوسته در این آموزش از نحو پوستهٔ POSIX استفاده می‌کنند که پوسته‌های پیش‌فرض
بیشتر سیستم‌های Linux و macOS (برای نمونه bash، zsh یا sh) از آن پشتیبانی می‌کنند.
کاربران ویندوز برای اجرای دستورها به همان شکلی که نوشته شده‌اند، باید از یک پوستهٔ
سازگار با POSIX مانند
[Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
یا [Git Bash](https://gitforwindows.org/) استفاده کنند.
دستورهایی که از `export`، `$()` و ساختارهای مشابه استفاده می‌کنند، با PowerShell یا
Command Prompt ویندوز سازگار **نیستند**.


## مروری بر Serviceهای کوبرنتیز

[Podهای](/docs/concepts/workloads/pods/) کوبرنتیز فناپذیرند و
[چرخهٔ حیات](/docs/concepts/workloads/pods/pod-lifecycle/) مشخصی دارند. وقتی یک نود
کارگر از کار می‌افتد، Podهایی که روی آن نود اجرا می‌شوند نیز از دست می‌روند. در این
حالت یک [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/) ممکن است با
ایجاد Podهای جدید، کلاستر را به‌صورت پویا به وضعیت مطلوب بازگرداند تا برنامهٔ شما
همچنان در حال اجرا بماند. به‌عنوان نمونه‌ای دیگر، یک بک‌اند پردازش تصویر با ۳ نسخهٔ
تکراری (replica) را در نظر بگیرید. این نسخه‌ها جایگزین‌پذیرند؛ سیستم فرانت‌اند نباید
به نسخه‌های بک‌اند اهمیت دهد، حتی اگر یک Pod از دست برود و دوباره ایجاد شود. با این
حال، هر Pod در کلاستر کوبرنتیز نشانی IP منحصربه‌فردی دارد، حتی Podهایی که روی یک نود
قرار دارند. بنابراین باید راهی برای هماهنگ‌سازی خودکار تغییرات میان Podها وجود داشته
باشد تا برنامه‌های شما به کار خود ادامه دهند.

{{% alert %}}
_هر Service در کوبرنتیز یک لایهٔ انتزاعی است که مجموعه‌ای منطقی از Podها را تعریف
می‌کند و امکان در دسترس قرار دادن آن‌ها برای ترافیک خارجی، توزیع بار و کشف سرویس را
برای این Podها فراهم می‌کند._
{{% /alert %}}

[Service](/docs/concepts/services-networking/service/) در کوبرنتیز یک انتزاع است که
مجموعه‌ای منطقی از Podها و سیاستی برای دسترسی به آن‌ها را تعریف می‌کند. Serviceها
امکان اتصال سست (loose coupling) میان Podهای وابسته به یکدیگر را فراهم می‌کنند. هر
Service، مانند همهٔ مانیفست‌های آبجکت‌های کوبرنتیز، با YAML یا JSON تعریف می‌شود.
مجموعهٔ Podهایی که یک Service هدف می‌گیرد، معمولاً با یک _انتخابگر برچسب_ (label
selector) تعیین می‌شود (در ادامه توضیح داده شده است که چرا ممکن است بخواهید Serviceی
بدون `selector` در spec داشته باشید).

اگرچه هر Pod نشانی IP منحصربه‌فردی دارد، این نشانی‌ها بدون Service خارج از کلاستر در
دسترس نیستند. Serviceها به برنامه‌های شما امکان دریافت ترافیک را می‌دهند. با تعیین
`type` در `spec` یک Service، می‌توان آن را به روش‌های مختلفی در دسترس قرار داد:

* _ClusterIP_ (پیش‌فرض) - Service را روی یک IP داخلی در کلاستر در دسترس قرار می‌دهد.
با این نوع، Service فقط از درون کلاستر قابل دسترسی است.

* _NodePort_ - Service را با استفاده از NAT روی پورتی یکسان در هر نود انتخاب‌شده از
کلاستر در دسترس قرار می‌دهد. با این نوع، Service از بیرون کلاستر از طریق
`NodeIP:NodePort` قابل دسترسی می‌شود. این نوع، ابرمجموعهٔ ClusterIP است.

* _LoadBalancer_ - در ابر فعلی (در صورت پشتیبانی) یک توزیع‌کنندهٔ بار خارجی ایجاد
می‌کند و یک IP خارجی ثابت به Service اختصاص می‌دهد. این نوع، ابرمجموعهٔ NodePort است.

* _ExternalName_ - با برگرداندن یک رکورد `CNAME` حاوی مقدار فیلد `externalName`
(برای نمونه `foo.bar.example.com`)، Service را به محتوای این فیلد نگاشت می‌کند.
هیچ نوع پراکسی‌ای راه‌اندازی نمی‌شود.

اطلاعات بیشتر دربارهٔ انواع مختلف Serviceها را می‌توانید در آموزش
[استفاده از Source IP](/docs/tutorials/services/source-ip/) بیابید. همچنین
[اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/)
را ببینید.

افزون بر این، توجه کنید که در برخی موارد استفاده از Serviceها، `selector` در spec
تعریف نمی‌شود. Serviceی که بدون `selector` ایجاد شود، آبجکت Endpoints متناظر را نیز
ایجاد نمی‌کند. به این ترتیب کاربران می‌توانند یک Service را به‌صورت دستی به
endpointهای مشخصی نگاشت کنند. دلیل احتمالی دیگر برای نبودن انتخابگر این است که فقط از
`type: ExternalName` استفاده می‌کنید.

## Serviceها و برچسب‌ها

هر Service ترافیک را میان مجموعه‌ای از Podها مسیریابی می‌کند. Serviceها انتزاعی هستند
که به Podها اجازه می‌دهند در کوبرنتیز از بین بروند و تکثیر شوند، بی‌آنکه بر برنامهٔ
شما اثری بگذارند. کشف و مسیریابی میان Podهای وابسته به یکدیگر (مانند مؤلفه‌های
فرانت‌اند و بک‌اند یک برنامه) را Serviceهای کوبرنتیز انجام می‌دهند.

Serviceها با استفاده از
[برچسب‌ها و انتخابگرها](/docs/concepts/overview/working-with-objects/labels) با
مجموعه‌ای از Podها تطبیق داده می‌شوند. برچسب‌ها و انتخابگرها یک سازوکار پایه‌ای
گروه‌بندی هستند که امکان انجام عملیات منطقی روی آبجکت‌های کوبرنتیز را فراهم می‌کنند.
برچسب‌ها زوج‌های کلید/مقداری هستند که به آبجکت‌ها متصل می‌شوند و به شیوه‌های گوناگونی
می‌توان از آن‌ها استفاده کرد:

* مشخص کردن آبجکت‌ها برای محیط‌های توسعه، آزمون و تولید
* درج برچسب‌های نسخه
* دسته‌بندی یک آبجکت با استفاده از برچسب‌ها

{{< figure src="/docs/tutorials/kubernetes-basics/public/images/module_04_labels.svg" class="diagram-medium" >}}

برچسب‌ها را می‌توان هنگام ایجاد آبجکت‌ها یا پس از آن به آن‌ها متصل کرد و در هر زمانی
تغییر داد. اکنون برنامهٔ خود را با استفاده از یک Service در دسترس قرار می‌دهیم و چند
برچسب اعمال می‌کنیم.

### گام ۱: ایجاد یک Service جدید

ابتدا بررسی می‌کنیم که برنامهٔ ما در حال اجرا باشد. از دستور `kubectl get` استفاده
می‌کنیم و به دنبال Podهای موجود می‌گردیم:

```shell
kubectl get pods
```

اگر هیچ Podی در حال اجرا نباشد، یعنی آبجکت‌های آموزش‌های قبلی پاک شده‌اند. در این
صورت، به آموزش
[استفاده از kubectl برای ایجاد یک Deployment](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro#deploy-an-app)
برگردید و Deployment را دوباره ایجاد کنید. چند ثانیه صبر کنید و دوباره فهرست Podها را
بگیرید. وقتی دیدید آن یک Pod در حال اجراست، می‌توانید ادامه دهید.

سپس فهرست Serviceهای فعلی کلاستر را می‌گیریم:

```shell
kubectl get services
```

برای در دسترس قرار دادن Deployment برای ترافیک خارجی، از دستور kubectl expose با
گزینهٔ --type=NodePort استفاده می‌کنیم:

```shell
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```

اکنون Serviceی با نام kubernetes-bootcamp در حال اجرا داریم. در اینجا می‌بینیم که این
Service یک cluster-IP منحصربه‌فرد، یک پورت داخلی و یک external-IP (نشانی IP نود)
دریافت کرده است.

برای اینکه بفهمیم کدام پورت به‌صورت خارجی باز شده است (برای Service از نوع
`type: NodePort`)، زیردستور `describe service` را اجرا می‌کنیم:

```shell
kubectl describe services/kubernetes-bootcamp
```

یک متغیر محیطی با نام `NODE_PORT` ایجاد کنید که مقدار پورت اختصاص‌یافته به نود را در
خود نگه دارد:

```shell
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"
```

اکنون می‌توانیم با استفاده از `curl`، نشانی IP نود و پورتی که به‌صورت خارجی در دسترس
قرار گرفته است، بررسی کنیم که برنامه خارج از کلاستر در دسترس است:

```shell
curl http://"$(minikube ip):$NODE_PORT"
```
{{< alert color="info" title="یادداشت" >}}
اگر minikube را با Docker Desktop به‌عنوان درایور کانتینر اجرا می‌کنید، به یک تونل
minikube نیاز دارید. دلیل این است که کانتینرهای درون Docker Desktop از رایانهٔ میزبان
شما جدا هستند.

در یک پنجرهٔ ترمینال جداگانه، این دستور را اجرا کنید:

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

و پاسخی از سرور دریافت می‌کنیم. Service در دسترس قرار گرفته است.

### گام ۲: استفاده از برچسب‌ها

Deployment به‌صورت خودکار یک برچسب برای Pod ما ایجاد کرده است. با زیردستور
`describe deployment` می‌توانید نام (_کلید_) آن برچسب را ببینید:

```shell
kubectl describe deployment
```

از این برچسب برای پرس‌وجو در فهرست Podها استفاده می‌کنیم. دستور `kubectl get pods`
را با پارامتر `-l` و پس از آن مقادیر برچسب به کار می‌بریم:

```shell
kubectl get pods -l app=kubernetes-bootcamp
```
همین کار را برای فهرست کردن Serviceهای موجود نیز می‌توانید انجام دهید:

```shell
kubectl get services -l app=kubernetes-bootcamp
```

نام Pod را به دست آورید و آن را در متغیر محیطی POD_NAME ذخیره کنید:

```shell
export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
echo "Name of the Pod: $POD_NAME"
```

برای اعمال یک برچسب جدید، از زیردستور label و پس از آن نوع آبجکت، نام آبجکت و برچسب
جدید استفاده می‌کنیم:

```shell
kubectl label pods "$POD_NAME" version=v1
```

با این کار برچسب جدیدی به Pod ما اعمال می‌شود (نسخهٔ برنامه را به Pod سنجاق کرده‌ایم)
و می‌توانیم آن را با دستور `describe pod` بررسی کنیم:

```shell
kubectl describe pods "$POD_NAME"
```

در اینجا می‌بینیم که برچسب اکنون به Pod ما متصل شده است. اکنون می‌توانیم با استفاده از
برچسب جدید در فهرست Podها پرس‌وجو کنیم:

```shell
kubectl get pods -l version=v1
```
و Pod را می‌بینیم.

### گام ۳: حذف یک Service

برای حذف Serviceها می‌توانید از زیردستور `delete service` استفاده کنید. در اینجا هم
می‌توان از برچسب‌ها استفاده کرد:

```shell
kubectl delete service -l app=kubernetes-bootcamp
```

بررسی کنید که Service حذف شده باشد:

```shell
kubectl get services
```

این خروجی تأیید می‌کند که Service ما حذف شده است. برای اطمینان از اینکه این مسیر دیگر
در دسترس نیست، می‌توانید با `curl` به IP و پورتی که پیش‌تر در دسترس بود درخواست
بفرستید:

```shell
curl http://"$(minikube ip):$NODE_PORT"
```

این نشان می‌دهد که برنامه دیگر از بیرون کلاستر قابل دسترسی نیست. با اجرای `curl` از
درون Pod می‌توانید تأیید کنید که برنامه همچنان در حال اجراست:

```shell
kubectl exec -ti $POD_NAME -- curl http://localhost:8080
```

در اینجا می‌بینیم که برنامه در حال اجراست، زیرا Deployment مدیریت برنامه را بر عهده
دارد. برای خاموش کردن برنامه، باید Deployment را نیز حذف کنید.

## {{% heading "whatsnext" %}}

* آموزش
[اجرای چند نمونه از برنامه](/docs/tutorials/kubernetes-basics/scale/scale-intro/).
* دربارهٔ [Service](/docs/concepts/services-networking/service/) بیشتر بیاموزید.

---
title: تخصیص منابع CPU به کانتینرها و Podها
content_type: task
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک *درخواست* (request) CPU و یک *محدودیت* (limit) CPU را به یک
کانتینر تخصیص دهید. کانتینرها نمی‌توانند بیش از محدودیت پیکربندی‌شده از CPU استفاده کنند.
به شرط آنکه سیستم زمان آزاد CPU داشته باشد، تخصیص مقدار CPU درخواستی هر کانتینر به آن تضمین می‌شود.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

برای اجرای مثال‌های این تمرین، کلاستر شما باید دست‌کم ۱ CPU در دسترس داشته باشد.

برای انجام چند گام از این صفحه باید سرویس
[metrics-server](https://github.com/kubernetes-sigs/metrics-server)
را در کلاستر خود اجرا کنید. اگر metrics-server از قبل
در حال اجراست، می‌توانید از این گام‌ها بگذرید.

اگر از {{< glossary_tooltip term_id="minikube" >}} استفاده می‌کنید، برای فعال‌کردن
metrics-server دستور زیر را اجرا کنید:

```shell
minikube addons enable metrics-server
```

برای اینکه ببینید metrics-server (یا فراهم‌کننده‌ی دیگری از API معیارهای منابع،
یعنی `metrics.k8s.io`) در حال اجراست یا نه، دستور زیر را وارد کنید:

```shell
kubectl get apiservices
```

اگر API معیارهای منابع در دسترس باشد، خروجی شامل
ارجاعی به `metrics.k8s.io` خواهد بود.


```
NAME
v1beta1.metrics.k8s.io
```




<!-- steps -->

## ایجاد یک فضای نام

یک {{< glossary_tooltip term_id="namespace" text="فضای نام" >}} ایجاد کنید تا منابعی که
در این تمرین می‌سازید از بقیه‌ی کلاستر جدا بمانند.

```shell
kubectl create namespace cpu-example
```

## تعیین یک درخواست CPU و یک محدودیت CPU

برای تعیین درخواست CPU یک کانتینر، فیلد `resources.requests.cpu` را
در مانیفست منبع کانتینر قرار دهید. برای تعیین محدودیت CPU، فیلد `resources.limits.cpu` را قرار دهید.

در این تمرین، یک Pod با یک کانتینر ایجاد می‌کنید. درخواست این کانتینر
۰٫۵ CPU و محدودیت آن ۱ CPU است. فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/resource/cpu-request-limit.yaml" options="hl_lines=10-14" %}}

بخش `args` در فایل پیکربندی، آرگومان‌هایی را برای هنگام شروع کانتینر فراهم می‌کند.
آرگومان `-cpus "2"` به کانتینر می‌گوید که تلاش کند از ۲ CPU استفاده کند.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/cpu-request-limit.yaml --namespace=cpu-example
```

بررسی کنید که Pod در حال اجرا باشد:

```shell
kubectl get pod cpu-demo --namespace=cpu-example
```

اطلاعات کامل Pod را مشاهده کنید:

```shell
kubectl get pod cpu-demo --output=yaml --namespace=cpu-example
```

خروجی نشان می‌دهد که تنها کانتینر این Pod درخواست CPU برابر ۵۰۰ میلی‌CPU
و محدودیت CPU برابر ۱ CPU دارد.

```yaml
resources:
  limits:
    cpu: "1"
  requests:
    cpu: 500m
```

برای دریافت معیارهای Pod از `kubectl top` استفاده کنید:

```shell
kubectl top pod cpu-demo --namespace=cpu-example
```

این خروجی نمونه نشان می‌دهد که Pod در حال استفاده از ۹۷۴ میلی‌CPU است که
اندکی کمتر از محدودیت ۱ CPU تعیین‌شده در پیکربندی Pod است.

```
NAME                        CPU(cores)   MEMORY(bytes)
cpu-demo                    974m         <something>
```

به یاد داشته باشید که با تنظیم `-cpu "2"`، کانتینر را طوری پیکربندی کردید که تلاش کند از ۲ CPU استفاده کند، اما کانتینر تنها اجازه دارد حدود ۱ CPU مصرف کند. مصرف CPU کانتینر محدود (throttle) می‌شود، زیرا کانتینر می‌کوشد بیش از محدودیت خود از منابع CPU استفاده کند.

{{< note >}}
توضیح احتمالی دیگر برای کمتر بودن مصرف CPU از ۱٫۰ این است که نود ممکن است
منابع CPU کافی در دسترس نداشته باشد. به یاد داشته باشید که پیش‌نیازهای این تمرین ایجاب می‌کند کلاستر شما دست‌کم ۱ CPU در دسترس داشته باشد. اگر کانتینر شما روی نودی اجرا شود که تنها ۱ CPU دارد، کانتینر صرف‌نظر از محدودیت CPU تعیین‌شده برای آن نمی‌تواند بیش از ۱ CPU مصرف کند.
{{< /note >}}

## واحدهای CPU

منبع CPU با واحد *CPU* اندازه‌گیری می‌شود. در کوبرنتیز، یک CPU معادل موارد زیر است:

* ۱ vCPU در AWS
* ۱ هسته (Core) در GCP
* ۱ vCore در Azure
* ۱ هایپرترد (Hyperthread) روی یک پردازنده‌ی Intel بدون مجازی‌سازی (bare-metal) دارای فناوری Hyperthreading

مقادیر کسری مجاز هستند. برای کانتینری که ۰٫۵ CPU درخواست می‌کند، نصف مقدار CPU
کانتینری که ۱ CPU درخواست می‌کند تضمین می‌شود. می‌توانید از پسوند m به معنای میلی استفاده کنید. برای نمونه،
100m CPU، ۱۰۰ میلی‌CPU و ۰٫۱ CPU همگی یکسان هستند. دقتی ریزتر از 1m مجاز نیست.

درخواست CPU همیشه به‌صورت مقداری مطلق بیان می‌شود و هرگز نسبی نیست؛ مقدار ۰٫۱ روی ماشینی
تک‌هسته‌ای، دوهسته‌ای یا ۴۸ هسته‌ای، مقدار یکسانی از CPU است.

Pod خود را حذف کنید:

```shell
kubectl delete pod cpu-demo --namespace=cpu-example
```

## تعیین درخواست CPU بزرگ‌تر از ظرفیت نودها

درخواست‌ها و محدودیت‌های CPU به کانتینرها مربوط می‌شوند، اما مفید است که
Pod را نیز دارای درخواست و محدودیت CPU در نظر بگیرید. درخواست CPU یک Pod برابر با مجموع
درخواست‌های CPU همه‌ی کانتینرهای آن Pod است. به همین ترتیب، محدودیت CPU
یک Pod برابر با مجموع محدودیت‌های CPU همه‌ی کانتینرهای آن Pod است.

زمان‌بندی Podها بر پایه‌ی درخواست‌ها انجام می‌شود. یک Pod تنها زمانی برای اجرا روی یک نود زمان‌بندی می‌شود که
آن نود منابع CPU کافی برای برآوردن درخواست CPU آن Pod در دسترس داشته باشد.

در این تمرین، Podای ایجاد می‌کنید که درخواست CPU آن چنان بزرگ است که از
ظرفیت هر نود در کلاستر شما فراتر می‌رود. فایل پیکربندی زیر مربوط به Podای
با یک کانتینر است. این کانتینر ۱۰۰ CPU درخواست می‌کند که به احتمال زیاد از
ظرفیت هر نود در کلاستر شما بیشتر است.

{{% code_sample file="pods/resource/cpu-request-limit-2.yaml" options="hl_lines=10-14" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/cpu-request-limit-2.yaml --namespace=cpu-example
```

وضعیت Pod را مشاهده کنید:

```shell
kubectl get pod cpu-demo-2 --namespace=cpu-example
```

خروجی نشان می‌دهد که وضعیت Pod در حالت Pending است. یعنی Pod برای اجرا
روی هیچ نودی زمان‌بندی نشده است و برای مدتی نامحدود در وضعیت Pending باقی می‌ماند:


```
NAME         READY     STATUS    RESTARTS   AGE
cpu-demo-2   0/1       Pending   0          7m
```

اطلاعات کامل Pod، از جمله رویدادها را مشاهده کنید:


```shell
kubectl describe pod cpu-demo-2 --namespace=cpu-example
```

خروجی نشان می‌دهد که کانتینر به دلیل کمبود منابع CPU روی نودها
قابل زمان‌بندی نیست:


```
Events:
  Reason                        Message
  ------                        -------
  FailedScheduling      No nodes are available that match all of the following predicates:: Insufficient cpu (3).
```

Pod خود را حذف کنید:

```shell
kubectl delete pod cpu-demo-2 --namespace=cpu-example
```

## اگر محدودیت CPU تعیین نکنید

اگر برای یک کانتینر محدودیت CPU تعیین نکنید، یکی از حالت‌های زیر پیش می‌آید:

* کانتینر هیچ سقفی برای منابع CPU قابل استفاده ندارد. کانتینر
می‌تواند از همه‌ی منابع CPU در دسترس روی نودی که در آن اجرا می‌شود استفاده کند.

* کانتینر در فضای نامی اجرا می‌شود که محدودیت CPU پیش‌فرض دارد و
محدودیت پیش‌فرض به‌طور خودکار به کانتینر تخصیص داده می‌شود. مدیران کلاستر می‌توانند با استفاده از یک
[LimitRange](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#limitrange-v1-core/)
مقدار پیش‌فرضی برای محدودیت CPU تعیین کنند.

## اگر محدودیت CPU را تعیین کنید ولی درخواست CPU را تعیین نکنید

اگر برای یک کانتینر محدودیت CPU تعیین کنید اما درخواست CPU تعیین نکنید، کوبرنتیز به‌طور خودکار
درخواست CPUای برابر با محدودیت تخصیص می‌دهد. به همین ترتیب، اگر یک کانتینر محدودیت حافظه‌ی خود را تعیین کند
ولی درخواست حافظه را تعیین نکند، کوبرنتیز به‌طور خودکار درخواست حافظه‌ای برابر با
محدودیت تخصیص می‌دهد.

## انگیزه‌ی استفاده از درخواست‌ها و محدودیت‌های CPU

با پیکربندی درخواست‌ها و محدودیت‌های CPU کانتینرهایی که در
کلاستر شما اجرا می‌شوند، می‌توانید از منابع CPU در دسترس روی نودهای کلاستر
به‌طور کارآمد استفاده کنید. با پایین نگه‌داشتن درخواست CPU یک Pod، شانس خوبی برای
زمان‌بندی آن فراهم می‌کنید. با داشتن محدودیت CPU بزرگ‌تر از درخواست CPU، دو هدف را محقق می‌کنید:

* Pod می‌تواند دوره‌هایی از فعالیت شدید (burst) داشته باشد که در آن از منابع CPU که در آن لحظه در دسترس هستند استفاده کند.
* مقدار منابع CPU که یک Pod می‌تواند در طول این دوره‌ها استفاده کند به مقداری معقول محدود می‌شود.

## پاک‌سازی

فضای نام خود را حذف کنید:

```shell
kubectl delete namespace cpu-example
```



## {{% heading "whatsnext" %}}



### برای توسعه‌دهندگان برنامه

* [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

* [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)

* [پیکربندی کیفیت سرویس (Quality of Service) برای Podها](/docs/tasks/configure-pod-container/quality-service-pod/)

* [تغییر اندازه‌ی منابع CPU و حافظه‌ی تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/)

* [تغییر اندازه‌ی منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/resize-pod-resources/)

### برای مدیران کلاستر

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)

* [پیکربندی درخواست‌ها و محدودیت‌های پیش‌فرض CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)

* [پیکربندی حداقل و حداکثر محدودیت‌های حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)

* [پیکربندی حداقل و حداکثر محدودیت‌های CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)

* [پیکربندی سهمیه‌های حافظه و CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)

* [پیکربندی سهمیه‌ی Pod برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)

* [پیکربندی سهمیه‌ها برای آبجکت‌های API](/docs/tasks/administer-cluster/quota-api-object/)

* [تغییر اندازه‌ی منابع CPU و حافظه‌ی تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/)

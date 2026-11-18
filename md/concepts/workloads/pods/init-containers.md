---
reviewers:
- erictune
title: کانتینرهای Init
content_type: concept
weight: 40
---

<!-- overview -->
این صفحه مروری بر کانتینرهای init ارائه می‌دهد. کانتینرهای init کانتینرهای ویژه‌ای هستند که پیش از کانتینرهای برنامه در یک {{< glossary_tooltip text="Pod" term_id="pod" >}} اجرا می‌شوند. این کانتینرها می‌توانند ابزارها یا اسکریپت‌های راه‌اندازی‌ای را در خود داشته باشند که در ایمیج برنامه وجود ندارند.

می‌توانید کانتینرهای init را در مشخصات Pod، در کنار آرایهٔ `containers` (که کانتینرهای برنامه را توصیف می‌کند) تعریف کنید.

در کوبرنتیز، [کانتینر کناری (sidecar container)](/docs/concepts/workloads/pods/sidecar-containers/) کانتینری است که پیش از کانتینر اصلی برنامه آغاز می‌شود و _به اجرای خود ادامه می‌دهد_. موضوع این سند کانتینرهای init است؛ یعنی کانتینرهایی که در طول مقداردهی اولیهٔ Pod تا پایان کار خود اجرا می‌شوند.

<!-- body -->

## آشنایی با کانتینرهای init

یک {{< glossary_tooltip text="Pod" term_id="pod" >}} می‌تواند چندین کانتینر داشته باشد که برنامه‌ها را درون آن اجرا می‌کنند، اما می‌تواند یک یا چند کانتینر init نیز داشته باشد که پیش از آغاز کانتینرهای برنامه اجرا می‌شوند.

کانتینرهای init دقیقاً مانند کانتینرهای معمولی هستند، با این تفاوت‌ها:

* کانتینرهای init همیشه تا پایان کار خود اجرا می‌شوند.
* هر کانتینر init باید پیش از آغاز کانتینر بعدی با موفقیت به پایان برسد.

اگر کانتینر init یک Pod با شکست مواجه شود، kubelet آن کانتینر init را آن‌قدر دوباره راه‌اندازی می‌کند تا با موفقیت اجرا شود. با این حال، اگر مقدار `restartPolicy` آن Pod برابر Never باشد و یک کانتینر init در هنگام راه‌اندازی Pod شکست بخورد، کوبرنتیز کل Pod را شکست‌خورده در نظر می‌گیرد.

برای تعریف یک کانتینر init برای یک Pod، فیلد `initContainers` را به‌صورت آرایه‌ای از آیتم‌های `container` (مشابه فیلد `containers` برنامه و محتوای آن) به [مشخصات Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec) اضافه کنید. برای جزئیات بیشتر، بخش [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) را در مرجع API ببینید.

وضعیت کانتینرهای init در فیلد `.status.initContainerStatuses` و به‌صورت آرایه‌ای از وضعیت‌های کانتینر (مشابه فیلد `.status.containerStatuses`) بازگردانده می‌شود.

### تفاوت با کانتینرهای معمولی

کانتینرهای init از همهٔ فیلدها و قابلیت‌های کانتینرهای برنامه، از جمله محدودیت‌های منابع، [حجم‌ها (volumes)](/docs/concepts/storage/volumes/) و تنظیمات امنیتی پشتیبانی می‌کنند. با این حال، درخواست‌ها و محدودیت‌های منابع برای یک کانتینر init به شیوهٔ متفاوتی مدیریت می‌شوند؛ این موضوع در بخش [اشتراک منابع میان کانتینرها](#resource-sharing-within-containers) توضیح داده شده است.

کانتینرهای init معمولی (به عبارت دیگر، به‌جز کانتینرهای کناری) از فیلدهای `lifecycle`، `livenessProbe`، `readinessProbe` یا `startupProbe` پشتیبانی نمی‌کنند. کانتینرهای init باید پیش از آماده‌شدن Pod تا پایان کار خود اجرا شوند؛ در حالی که کانتینرهای کناری در طول عمر Pod به اجرای خود ادامه می‌دهند و از برخی کاوشگرها (probe) _پشتیبانی می‌کنند_. برای جزئیات بیشتر دربارهٔ کانتینرهای کناری، صفحهٔ [کانتینر کناری](/docs/concepts/workloads/pods/sidecar-containers/) را ببینید.

اگر چند کانتینر init برای یک Pod تعریف کنید، kubelet هر کانتینر init را به‌ترتیب اجرا می‌کند. هر کانتینر init باید پیش از اجرای کانتینر بعدی با موفقیت به پایان برسد. هنگامی که همهٔ کانتینرهای init تا پایان اجرا شدند، kubelet کانتینرهای برنامهٔ Pod را مقداردهی اولیه می‌کند و آن‌ها را به روال معمول اجرا می‌کند.

### تفاوت با کانتینرهای کناری

کانتینرهای init پیش از آغاز کانتینر اصلی برنامه اجرا می‌شوند و وظایف خود را به پایان می‌رسانند. برخلاف [کانتینرهای کناری](/docs/concepts/workloads/pods/sidecar-containers)، کانتینرهای init به‌طور پیوسته در کنار کانتینرهای اصلی اجرا نمی‌شوند.

کانتینرهای init به‌ترتیب و تا پایان کار خود اجرا می‌شوند و کانتینر اصلی تا زمانی که همهٔ کانتینرهای init با موفقیت به پایان نرسیده باشند، آغاز نمی‌شود.

کانتینرهای init از `lifecycle`، `livenessProbe`، `readinessProbe` یا `startupProbe` پشتیبانی نمی‌کنند، در حالی که کانتینرهای کناری برای کنترل چرخهٔ عمر خود از همهٔ این [کاوشگرها](/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe) پشتیبانی می‌کنند.

کانتینرهای init منابع یکسانی (CPU، حافظه، شبکه) را با کانتینرهای اصلی برنامه به اشتراک می‌گذارند، اما به‌طور مستقیم با آن‌ها تعامل ندارند. با این حال، می‌توانند برای تبادل داده از حجم‌های مشترک استفاده کنند.

## استفاده از کانتینرهای init

از آنجا که ایمیج کانتینرهای init از ایمیج کانتینرهای برنامه جداست، این کانتینرها برای کدهای مربوط به راه‌اندازی مزایایی دارند:

* کانتینرهای init می‌توانند ابزارها یا کدهای سفارشی راه‌اندازی را در خود داشته باشند که در ایمیج برنامه وجود ندارند. برای مثال، نیازی نیست فقط برای استفاده از ابزاری مانند `sed`، `awk`، `python` یا `dig` در هنگام راه‌اندازی، ایمیجی را با `FROM` بر پایهٔ ایمیج دیگری بسازید.
* نقش‌های سازندهٔ ایمیج برنامه و مستقرکنندهٔ آن می‌توانند به‌طور مستقل کار کنند، بدون اینکه لازم باشد به‌طور مشترک یک ایمیج واحد برای برنامه بسازند.
* کانتینرهای init می‌توانند با نمایی متفاوت از سیستم فایل نسبت به کانتینرهای برنامه در همان Pod اجرا شوند. در نتیجه، می‌توان به آن‌ها دسترسی به {{< glossary_tooltip text="Secretها" term_id="secret" >}}یی داد که کانتینرهای برنامه به آن‌ها دسترسی ندارند.
* از آنجا که کانتینرهای init پیش از آغاز هر کانتینر برنامه‌ای تا پایان اجرا می‌شوند، سازوکاری برای مسدودکردن یا به تأخیر انداختن آغاز کانتینرهای برنامه تا زمان برآورده‌شدن مجموعه‌ای از پیش‌شرط‌ها فراهم می‌کنند. پس از برآورده‌شدن پیش‌شرط‌ها، همهٔ کانتینرهای برنامه در یک Pod می‌توانند به‌صورت موازی آغاز شوند.
* کانتینرهای init می‌توانند ابزارها یا کدهای سفارشی‌ای را به‌صورت ایمن اجرا کنند که در غیر این صورت امنیت ایمیج کانتینر برنامه را کاهش می‌دادند. با جدا نگه‌داشتن ابزارهای غیرضروری، می‌توانید سطح حملهٔ ایمیج کانتینر برنامهٔ خود را محدود کنید.


### مثال‌ها
در ادامه چند ایده برای استفاده از کانتینرهای init آمده است:

* منتظر ماندن برای ایجاد یک {{< glossary_tooltip text="Service" term_id="service">}}، با استفاده از یک دستور تک‌خطی شل مانند:
  ```shell
  for i in {1..100}; do sleep 1; if nslookup myservice; then exit 0; fi; done; exit 1
  ```

* ثبت این Pod در یک سرور راه دور با استفاده از downward API، با دستوری مانند:
  ```shell
  curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d 'instance=$(<POD_NAME>)&ip=$(<POD_IP>)'
  ```

* منتظر ماندن برای مدتی پیش از آغاز کانتینر برنامه، با دستوری مانند
  ```shell
  sleep 60
  ```

* کلون‌کردن یک مخزن Git در یک {{< glossary_tooltip text="حجم" term_id="volume" >}}

* قرار دادن مقادیر در یک فایل پیکربندی و اجرای یک ابزار قالب‌سازی برای تولید پویای فایل پیکربندی کانتینر اصلی برنامه. برای مثال، مقدار `POD_IP` را در یک پیکربندی قرار دهید و فایل پیکربندی اصلی برنامه را با Jinja تولید کنید.

#### نمونهٔ کاربردی کانتینرهای init

این مثال یک Pod ساده با دو کانتینر init تعریف می‌کند. کانتینر اول منتظر `myservice` و کانتینر دوم منتظر `mydb` می‌ماند. پس از پایان هر دو کانتینر init، این Pod کانتینر برنامه را از بخش `spec` خود اجرا می‌کند.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app.kubernetes.io/name: MyApp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup myservice.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for myservice; sleep 2; done"]
  - name: init-mydb
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup mydb.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for mydb; sleep 2; done"]
```

می‌توانید این Pod را با اجرای دستور زیر آغاز کنید:

```shell
kubectl apply -f myapp.yaml
```
خروجی مشابه زیر است:
```
pod/myapp-pod created
```

و وضعیت آن را با دستور زیر بررسی کنید:
```shell
kubectl get -f myapp.yaml
```
خروجی مشابه زیر است:
```
NAME        READY     STATUS     RESTARTS   AGE
myapp-pod   0/1       Init:0/2   0          6m
```

یا برای جزئیات بیشتر:
```shell
kubectl describe -f myapp.yaml
```
خروجی مشابه زیر است:
```
Name:          myapp-pod
Namespace:     default
[...]
Labels:        app.kubernetes.io/name=MyApp
Status:        Pending
[...]
Init Containers:
  init-myservice:
[...]
    State:         Running
[...]
  init-mydb:
[...]
    State:         Waiting
      Reason:      PodInitializing
    Ready:         False
[...]
Containers:
  myapp-container:
[...]
    State:         Waiting
      Reason:      PodInitializing
    Ready:         False
[...]
Events:
  FirstSeen    LastSeen    Count    From                      SubObjectPath                           Type          Reason        Message
  ---------    --------    -----    ----                      -------------                           --------      ------        -------
  16s          16s         1        {default-scheduler }                                              Normal        Scheduled     Successfully assigned myapp-pod to 172.17.4.201
  16s          16s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Pulling       pulling image "busybox"
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Pulled        Successfully pulled image "busybox"
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Created       Created container init-myservice
  13s          13s         1        {kubelet 172.17.4.201}    spec.initContainers{init-myservice}     Normal        Started       Started container init-myservice
```

برای دیدن لاگ‌های کانتینرهای init در این Pod، دستور زیر را اجرا کنید:
```shell
kubectl logs myapp-pod -c init-myservice # Inspect the first init container
kubectl logs myapp-pod -c init-mydb      # Inspect the second init container
```

در این مرحله، آن کانتینرهای init منتظر شناسایی {{< glossary_tooltip text="Serviceهای" term_id="service" >}} با نام‌های `mydb` و `myservice` هستند.

در ادامه پیکربندی‌ای آمده است که می‌توانید برای ایجاد آن Serviceها از آن استفاده کنید:

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: myservice
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
---
apiVersion: v1
kind: Service
metadata:
  name: mydb
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9377
```

برای ایجاد سرویس‌های `mydb` و `myservice`:

```shell
kubectl apply -f services.yaml
```
خروجی مشابه زیر است:
```
service/myservice created
service/mydb created
```

سپس خواهید دید که آن کانتینرهای init به پایان می‌رسند و Pod با نام `myapp-pod` به وضعیت Running می‌رود:

```shell
kubectl get -f myapp.yaml
```
خروجی مشابه زیر است:
```
NAME        READY     STATUS    RESTARTS   AGE
myapp-pod   1/1       Running   0          9m
```

این مثال ساده باید ایده‌هایی برای ساخت کانتینرهای init خودتان به شما بدهد. بخش [قدم‌های بعدی](#what-s-next) پیوندی به یک مثال مفصل‌تر دارد.

## رفتار تفصیلی

در هنگام راه‌اندازی Pod، kubelet اجرای کانتینرهای init را تا آماده‌شدن شبکه و ذخیره‌سازی به تأخیر می‌اندازد. سپس kubelet کانتینرهای init آن Pod را به ترتیبی که در مشخصات Pod آمده‌اند اجرا می‌کند.

هر کانتینر init باید پیش از آغاز کانتینر بعدی با موفقیت خارج شود. اگر کانتینری به دلیل محیط اجرا نتواند آغاز شود یا با شکست خارج شود، بر اساس `restartPolicy` آن Pod دوباره تلاش می‌شود. با این حال، اگر `restartPolicy` آن Pod روی Always تنظیم شده باشد، کانتینرهای init از `restartPolicy` با مقدار OnFailure استفاده می‌کنند.

یک Pod تا زمانی که همهٔ کانتینرهای init با موفقیت اجرا نشده باشند، نمی‌تواند در وضعیت `Ready` قرار بگیرد. درگاه‌های (port) یک کانتینر init زیر یک Service تجمیع نمی‌شوند. Podی که در حال مقداردهی اولیه است در وضعیت `Pending` قرار دارد، اما باید شرط `Initialized` آن روی false تنظیم شده باشد.

اگر Pod [دوباره راه‌اندازی شود](#pod-restart-reasons) یا دوباره راه‌اندازی گردد، همهٔ کانتینرهای init باید دوباره اجرا شوند.

تغییرات در مشخصات کانتینر init به فیلد ایمیج کانتینر محدود است. تغییر مستقیم فیلد `image` یک کانتینر init باعث راه‌اندازی دوبارهٔ Pod یا ایجاد دوبارهٔ آن _نمی‌شود_. اگر Pod هنوز آغاز نشده باشد، این تغییر ممکن است بر نحوهٔ بالا آمدن Pod اثر بگذارد.

در یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) معمولاً می‌توانید هر فیلدی از یک کانتینر init را تغییر دهید؛ تأثیر این تغییر به محل استفاده از آن قالب Pod بستگی دارد.

از آنجا که کانتینرهای init ممکن است دوباره راه‌اندازی شوند، دوباره امتحان شوند یا دوباره اجرا شوند، کد کانتینر init باید خودتوان (idempotent) باشد. به‌ویژه، کدی که در هر حجم `emptyDir` می‌نویسد باید برای این احتمال آماده باشد که فایل خروجی از قبل وجود داشته باشد.

کانتینرهای init همهٔ فیلدهای یک کانتینر برنامه را دارند. با این حال، کوبرنتیز استفاده از `readinessProbe` را ممنوع می‌کند، زیرا کانتینرهای init نمی‌توانند آمادگی را جدا از پایان کار تعریف کنند. این محدودیت در هنگام اعتبارسنجی اعمال می‌شود.

برای جلوگیری از شکست بی‌پایان کانتینرهای init، از `activeDeadlineSeconds` روی Pod استفاده کنید. این مهلت فعال شامل کانتینرهای init نیز می‌شود. با این حال، توصیه می‌شود فقط در صورتی از `activeDeadlineSeconds` استفاده کنید که تیم‌ها برنامهٔ خود را به‌صورت Job مستقر می‌کنند، زیرا `activeDeadlineSeconds` حتی پس از پایان initContainer نیز اثر دارد. در صورت تنظیم `activeDeadlineSeconds`، Podی که از قبل به‌درستی در حال اجراست نیز از بین برده می‌شود.

نام هر کانتینر برنامه و کانتینر init در یک Pod باید یکتا باشد؛ برای هر کانتینری که نامش با کانتینر دیگری یکسان باشد، خطای اعتبارسنجی صادر می‌شود.

### اشتراک منابع میان کانتینرها

با توجه به ترتیب اجرای کانتینرهای init، کناری و برنامه، قواعد زیر برای مصرف منابع اعمال می‌شوند:

* بالاترین مقدار درخواست یا محدودیت هر منبع خاص که در همهٔ کانتینرهای init تعریف شده باشد، *درخواست/محدودیت مؤثر init* است. اگر برای منبعی هیچ محدودیتی تعیین نشده باشد، همین به‌عنوان بالاترین محدودیت در نظر گرفته می‌شود.
* *درخواست/محدودیت مؤثر* Pod برای یک منبع، بزرگ‌ترِ این دو مقدار است:
  * مجموع درخواست/محدودیت همهٔ کانتینرهای برنامه برای آن منبع
  * درخواست/محدودیت مؤثر init برای آن منبع
* زمان‌بندی بر اساس درخواست‌ها/محدودیت‌های مؤثر انجام می‌شود؛ یعنی کانتینرهای init می‌توانند منابعی را برای مقداردهی اولیه رزرو کنند که در طول عمر Pod استفاده نمی‌شوند.
* ردهٔ QoS (کیفیت سرویس) مربوط به *ردهٔ QoS مؤثر* Pod، ردهٔ QoS هم برای کانتینرهای init و هم برای کانتینرهای برنامه است.

سهمیه‌ها و محدودیت‌ها بر اساس درخواست و محدودیت مؤثر Pod اعمال می‌شوند.

### کانتینرهای init و cgroupهای لینوکس {#cgroups}

در لینوکس، تخصیص منابع برای گروه‌های کنترل (cgroups) در سطح Pod، همانند زمان‌بند، بر اساس درخواست و محدودیت مؤثر Pod انجام می‌شود.

{{< comment >}}
This section also present under [sidecar containers](/docs/concepts/workloads/pods/sidecar-containers/) page.
If you're editing this section, change both places.
{{< /comment >}}

### دلایل راه‌اندازی دوبارهٔ Pod

یک Pod ممکن است به دلایل زیر دوباره راه‌اندازی شود و در نتیجه کانتینرهای init دوباره اجرا شوند:

* کانتینر زیرساخت Pod دوباره راه‌اندازی شود. این اتفاق نادر است و باید توسط کسی انجام شود که به نودها دسترسی root دارد.
* همهٔ کانتینرهای یک Pod در حالی خاتمه یابند که `restartPolicy` روی Always تنظیم شده است و این امر راه‌اندازی دوباره را الزامی کند، و سابقهٔ پایان کانتینر init به دلیل {{< glossary_tooltip text="جمع‌آوری زباله" term_id="garbage-collection" >}} از دست رفته باشد.

هنگامی که ایمیج کانتینر init تغییر کند، یا سابقهٔ پایان کانتینر init به دلیل جمع‌آوری زباله از دست برود، Pod دوباره راه‌اندازی نمی‌شود. این رفتار برای کوبرنتیز نسخهٔ 1.20 و بالاتر صدق می‌کند. اگر از نسخهٔ قدیمی‌تری از کوبرنتیز استفاده می‌کنید، به مستندات نسخهٔ مورد استفادهٔ خود مراجعه کنید.

## {{% heading "whatsnext" %}}

دربارهٔ موارد زیر بیشتر بیاموزید:
* [ایجاد یک Pod دارای کانتینر init](/docs/tasks/configure-pod-container/configure-pod-initialization/#create-a-pod-that-has-an-init-container).
* [اشکال‌زدایی کانتینرهای init](/docs/tasks/debug/debug-application/debug-init-containers/).
* مروری بر [kubelet](/docs/reference/command-line-tools-reference/kubelet/) و [kubectl](/docs/reference/kubectl/).
* [انواع کاوشگرها](/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe): کاوشگرهای liveness، readiness و startup.
* [کانتینرهای کناری](/docs/concepts/workloads/pods/sidecar-containers).

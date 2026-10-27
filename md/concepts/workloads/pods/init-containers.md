---
reviewers:
- erictune
title: کانتینرهای مقداردهی اولیه (Init Containers)
content_type: concept
weight: 40
---

<!-- overview -->
این صفحه یک نمای کلی از init containerها ارائه می‌دهد: کانتینرهای تخصصی که پیش از کانتینرهای برنامه در یک {{< glossary_tooltip text="Pod" term_id="pod" >}} اجرا می‌شوند.
Init containerها می‌توانند شامل ابزارها یا اسکریپت‌های راه‌اندازی باشند که در ایمیج برنامه وجود ندارند.

می‌توانید init containerها را در مشخصات Pod و در کنار آرایه `containers` (که کانتینرهای برنامه را توصیف می‌کند) تعریف کنید.

در کوبرنتیز، [کانتینر سایدکار (sidecar)](/docs/concepts/workloads/pods/sidecar-containers/) کانتینری است که پیش از کانتینر اصلی برنامه شروع به کار می‌کند و _به اجرای خود ادامه می‌دهد_. این سند درباره init containerهاست: کانتینرهایی که در طول مقداردهی اولیه Pod تا پایان کار اجرا می‌شوند.

<!-- body -->

## شناخت init containerها {#understanding-init-containers}

یک {{< glossary_tooltip text="Pod" term_id="pod" >}} می‌تواند چندین کانتینر داشته باشد که برنامه‌ها را درون آن اجرا می‌کنند، اما می‌تواند یک یا چند init container نیز داشته باشد که پیش از شروع کانتینرهای برنامه اجرا می‌شوند.

Init containerها دقیقاً مانند کانتینرهای معمولی هستند، با این تفاوت‌ها:

* Init containerها همیشه تا پایان کار اجرا می‌شوند.
* هر init container باید پیش از شروع init container بعدی با موفقیت به پایان برسد.

اگر init container یک Pod با شکست مواجه شود، kubelet آن init container را پیوسته راه‌اندازی مجدد می‌کند تا موفق شود.
با این حال، اگر مقدار `restartPolicy` در Pod برابر Never باشد و یک init container در طول راه‌اندازی آن Pod شکست بخورد، کوبرنتیز کل Pod را ناموفق در نظر می‌گیرد.

برای تعیین یک init container برای Pod، فیلد `initContainers` را به [مشخصات Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec) اضافه کنید، به‌صورت آرایه‌ای از آیتم‌های `container` (مشابه فیلد `containers` برنامه و محتویات آن).
برای جزئیات بیشتر، بخش [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) را در مرجع API ببینید.

وضعیت init containerها در فیلد `.status.initContainerStatuses` به‌صورت آرایه‌ای از وضعیت کانتینرها بازگردانده می‌شود (مشابه فیلد `.status.containerStatuses`).

### تفاوت‌ها با کانتینرهای معمولی {#differences-from-regular-containers}

Init containerها از همه فیلدها و ویژگی‌های کانتینرهای برنامه پشتیبانی می‌کنند، از جمله محدودیت‌های منابع، [حجم‌ها (volumes)](/docs/concepts/storage/volumes/) و تنظیمات امنیتی. با این حال، درخواست‌ها و محدودیت‌های منابع برای init container به شکل متفاوتی مدیریت می‌شوند، همان‌طور که در [اشتراک منابع میان کانتینرها](#resource-sharing-within-containers) توضیح داده شده است.

Init containerهای معمولی (به عبارت دیگر: به‌جز کانتینرهای سایدکار) از فیلدهای `lifecycle`، `livenessProbe`، `readinessProbe` و `startupProbe` پشتیبانی نمی‌کنند. Init containerها باید پیش از آماده شدن Pod تا پایان کار اجرا شوند؛ کانتینرهای سایدکار در طول عمر Pod به اجرا ادامه می‌دهند و از برخی probeها _پشتیبانی می‌کنند_. برای جزئیات بیشتر درباره کانتینرهای سایدکار، [کانتینر سایدکار](/docs/concepts/workloads/pods/sidecar-containers/) را ببینید.

اگر چند init container برای یک Pod تعریف کنید، kubelet هر init container را به‌صورت ترتیبی اجرا می‌کند. هر init container باید پیش از اجرای بعدی با موفقیت به پایان برسد.
هنگامی که همه init containerها تا پایان کار اجرا شدند، kubelet کانتینرهای برنامه Pod را مقداردهی اولیه می‌کند و آن‌ها را به‌طور معمول اجرا می‌کند.

### تفاوت‌ها با کانتینرهای سایدکار {#differences-from-sidecar-containers}

Init containerها پیش از شروع کانتینر اصلی برنامه اجرا می‌شوند و کار خود را کامل می‌کنند.
برخلاف [کانتینرهای سایدکار](/docs/concepts/workloads/pods/sidecar-containers)، init containerها به‌طور پیوسته در کنار کانتینرهای اصلی اجرا نمی‌شوند.

Init containerها به‌صورت ترتیبی تا پایان کار اجرا می‌شوند و کانتینر اصلی تا زمانی که همه init containerها با موفقیت به پایان نرسیده باشند، شروع نمی‌شود.

Init containerها از `lifecycle`، `livenessProbe`، `readinessProbe` و `startupProbe` پشتیبانی نمی‌کنند، در حالی که کانتینرهای سایدکار از همه این [probeها](/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe) برای کنترل چرخه عمر خود پشتیبانی می‌کنند.

Init containerها منابع یکسانی (CPU، حافظه، شبکه) را با کانتینرهای اصلی برنامه به اشتراک می‌گذارند، اما به‌طور مستقیم با آن‌ها تعامل ندارند. با این حال، می‌توانند برای تبادل داده از حجم‌های (volumes) مشترک استفاده کنند.

## استفاده از init containerها {#using-init-containers}

از آنجا که init containerها ایمیج‌هایی جدا از کانتینرهای برنامه دارند، برای کدهای مربوط به راه‌اندازی چند مزیت دارند:

* Init containerها می‌توانند شامل ابزارها یا کد سفارشی برای راه‌اندازی باشند که در ایمیج برنامه وجود ندارند. برای مثال، لازم نیست فقط برای استفاده از ابزارهایی مانند `sed`، `awk`، `python` یا `dig` در زمان راه‌اندازی، یک ایمیج را با `FROM` از ایمیج دیگری بسازید.
* نقش‌های سازنده ایمیج برنامه و مستقرکننده آن می‌توانند به‌طور مستقل کار کنند، بدون اینکه نیازی به ساخت مشترک یک ایمیج واحد برای برنامه باشد.
* Init containerها می‌توانند با دیدی متفاوت از سیستم فایل نسبت به کانتینرهای برنامه در همان Pod اجرا شوند. در نتیجه، می‌توان به آن‌ها دسترسی به {{< glossary_tooltip text="Secretها" term_id="secret" >}} داد که کانتینرهای برنامه به آن‌ها دسترسی ندارند.
* از آنجا که init containerها پیش از شروع هر یک از کانتینرهای برنامه تا پایان کار اجرا می‌شوند، سازوکاری فراهم می‌کنند تا شروع کانتینرهای برنامه تا برآورده شدن مجموعه‌ای از پیش‌شرط‌ها مسدود یا به تأخیر انداخته شود. پس از برآورده شدن پیش‌شرط‌ها، همه کانتینرهای برنامه در یک Pod می‌توانند به‌طور موازی شروع شوند.
* Init containerها می‌توانند ابزارها یا کد سفارشی را که در غیر این صورت ایمیج کانتینر برنامه را کم‌امن‌تر می‌کردند، به‌صورت ایمن اجرا کنند. با جدا نگه داشتن ابزارهای غیرضروری، می‌توانید سطح حمله ایمیج کانتینر برنامه خود را محدود کنید.


### مثال‌ها {#examples}
در اینجا چند ایده برای استفاده از init containerها آمده است:

* منتظر ماندن تا یک {{< glossary_tooltip text="Service" term_id="service">}} ایجاد شود، با استفاده از یک فرمان تک‌خطی شل مانند:
  ```shell
  for i in {1..100}; do sleep 1; if nslookup myservice; then exit 0; fi; done; exit 1
  ```

* ثبت این Pod در یک سرور راه دور از طریق downward API با فرمانی مانند:
  ```shell
  curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d 'instance=$(<POD_NAME>)&ip=$(<POD_IP>)'
  ```

* منتظر ماندن برای مدتی پیش از شروع کانتینر برنامه با فرمانی مانند
  ```shell
  sleep 60
  ```

* کلون کردن یک مخزن Git در یک {{< glossary_tooltip text="Volume" term_id="volume" >}}

* قرار دادن مقادیر در یک فایل پیکربندی و اجرای یک ابزار قالب‌ساز برای تولید پویای فایل پیکربندی کانتینر اصلی برنامه. برای مثال، مقدار `POD_IP` را در یک پیکربندی قرار دهید و فایل پیکربندی اصلی برنامه را با استفاده از Jinja تولید کنید.

#### Init containerها در عمل {#init-containers-in-use}

این مثال یک Pod ساده با دو init container تعریف می‌کند.
اولی منتظر `myservice` می‌ماند و دومی منتظر `mydb`. پس از اینکه هر دو init container به پایان رسیدند، Pod کانتینر برنامه را از بخش `spec` خود اجرا می‌کند.

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

می‌توانید این Pod را با اجرای دستور زیر شروع کنید:

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

برای مشاهده لاگ‌های init containerهای این Pod، دستورهای زیر را اجرا کنید:
```shell
kubectl logs myapp-pod -c init-myservice # Inspect the first init container
kubectl logs myapp-pod -c init-mydb      # Inspect the second init container
```

در این مرحله، این init containerها منتظر کشف {{< glossary_tooltip text="Serviceهایی" term_id="service" >}} با نام‌های `mydb` و `myservice` خواهند بود.

در اینجا پیکربندی‌ای آمده است که می‌توانید برای ظاهر شدن این Serviceها از آن استفاده کنید:

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

برای ایجاد Serviceهای `mydb` و `myservice`:

```shell
kubectl apply -f services.yaml
```
خروجی مشابه زیر است:
```
service/myservice created
service/mydb created
```

سپس خواهید دید که این init containerها به پایان می‌رسند و Pod با نام `myapp-pod` به وضعیت Running می‌رود:

```shell
kubectl get -f myapp.yaml
```
خروجی مشابه زیر است:
```
NAME        READY     STATUS    RESTARTS   AGE
myapp-pod   1/1       Running   0          9m
```

این مثال ساده باید الهام‌بخش شما برای ایجاد init containerهای خودتان باشد. بخش [گام بعدی](#what-s-next) شامل پیوندی به یک مثال دقیق‌تر است.

## رفتار دقیق {#detailed-behavior}

در طول راه‌اندازی Pod، kubelet اجرای init containerها را تا آماده شدن شبکه و ذخیره‌سازی به تأخیر می‌اندازد. سپس kubelet init containerهای Pod را به همان ترتیبی که در مشخصات Pod ظاهر شده‌اند اجرا می‌کند.

هر init container باید پیش از شروع کانتینر بعدی با موفقیت خارج شود. اگر کانتینری به دلیل runtime نتواند شروع شود یا با شکست خارج شود، بر اساس `restartPolicy` مربوط به Pod دوباره تلاش می‌شود. با این حال، اگر `restartPolicy` در Pod روی Always تنظیم شده باشد، init containerها از `restartPolicy` برابر OnFailure استفاده می‌کنند.

یک Pod تا زمانی که همه init containerها موفق نشده باشند نمی‌تواند `Ready` شود. پورت‌های یک init container زیر یک Service تجمیع نمی‌شوند. Podی که در حال مقداردهی اولیه است در وضعیت `Pending` قرار دارد، اما باید شرط `Initialized` آن روی false تنظیم شده باشد.

اگر Pod [راه‌اندازی مجدد شود](#pod-restart-reasons) یا مجدداً راه‌اندازی شود، همه init containerها باید دوباره اجرا شوند.

تغییرات در مشخصات init container به فیلد ایمیج کانتینر محدود است.
تغییر مستقیم فیلد `image` در یک init container، Pod را راه‌اندازی مجدد نمی‌کند و باعث ایجاد مجدد آن نمی‌شود. اگر Pod هنوز شروع نشده باشد، این تغییر ممکن است بر نحوه بالا آمدن Pod تأثیر بگذارد.

برای یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) معمولاً می‌توانید هر فیلدی را برای یک init container تغییر دهید؛ تأثیر این تغییر به محلی که قالب Pod در آن استفاده می‌شود بستگی دارد.

از آنجا که init containerها می‌توانند راه‌اندازی مجدد، دوباره‌تلاش یا دوباره‌اجرا شوند، کد init container باید خنثی‌توان (idempotent) باشد. به‌ویژه، کدی که در هر حجم `emptyDir` می‌نویسد باید برای این احتمال آماده باشد که فایل خروجی از قبل وجود داشته باشد.

Init containerها همه فیلدهای یک کانتینر برنامه را دارند. با این حال، کوبرنتیز استفاده از `readinessProbe` را ممنوع می‌کند، زیرا init containerها نمی‌توانند آمادگی‌ای جدا از تکمیل شدن تعریف کنند. این موضوع در طول اعتبارسنجی اعمال می‌شود.

برای جلوگیری از شکست دائمی init containerها، از `activeDeadlineSeconds` در Pod استفاده کنید.
مهلت فعال (active deadline) شامل init containerها نیز می‌شود.
با این حال، توصیه می‌شود `activeDeadlineSeconds` را فقط زمانی استفاده کنید که تیم‌ها برنامه خود را به‌صورت Job مستقر می‌کنند، زیرا `activeDeadlineSeconds` حتی پس از پایان کار initContainer نیز اثر دارد.
در صورت تنظیم این فیلد، Podی که از قبل به‌درستی در حال اجراست نیز توسط `activeDeadlineSeconds` متوقف خواهد شد.

نام هر کانتینر برنامه و init container در یک Pod باید یکتا باشد؛ برای هر کانتینری که نام خود را با کانتینر دیگری به اشتراک بگذارد، خطای اعتبارسنجی صادر می‌شود.

### اشتراک منابع میان کانتینرها {#resource-sharing-within-containers}

با توجه به ترتیب اجرای init containerها، کانتینرهای سایدکار و کانتینرهای برنامه، قوانین زیر برای استفاده از منابع اعمال می‌شود:

* بالاترین درخواست یا محدودیت هر منبع مشخص که روی همه init containerها تعریف شده باشد، *درخواست/محدودیت مؤثر init* است. اگر برای هر منبعی محدودیتی تعیین نشده باشد، این مورد به‌عنوان بالاترین محدودیت در نظر گرفته می‌شود.
* *درخواست/محدودیت مؤثر* Pod برای یک منبع، مقدار بزرگ‌تر از میان موارد زیر است:
  * مجموع درخواست/محدودیت همه کانتینرهای برنامه برای آن منبع
  * درخواست/محدودیت مؤثر init برای آن منبع
* زمان‌بندی بر اساس درخواست‌ها/محدودیت‌های مؤثر انجام می‌شود، به این معنا که init containerها می‌توانند منابعی را برای مقداردهی اولیه رزرو کنند که در طول عمر Pod استفاده نمی‌شوند.
* سطح QoS (کیفیت خدمات) مؤثر Pod، همان سطح QoS برای init containerها و کانتینرهای برنامه به‌طور یکسان است.

سهمیه (quota) و محدودیت‌ها بر اساس درخواست و محدودیت مؤثر Pod اعمال می‌شوند.

### Init containerها و cgroupهای لینوکس {#cgroups}

در لینوکس، تخصیص منابع برای گروه‌های کنترل (cgroups) در سطح Pod بر اساس درخواست و محدودیت مؤثر Pod انجام می‌شود، همانند زمان‌بند.

{{< comment >}}
This section also present under [sidecar containers](/docs/concepts/workloads/pods/sidecar-containers/) page.
If you're editing this section, change both places.
{{< /comment >}}

### دلایل راه‌اندازی مجدد Pod {#pod-restart-reasons}

یک Pod می‌تواند راه‌اندازی مجدد شود و موجب اجرای دوباره init containerها گردد، به دلایل زیر:

* کانتینر زیرساختی Pod راه‌اندازی مجدد شود. این حالت نادر است و باید توسط کسی انجام شود که به نودها دسترسی root دارد.
* همه کانتینرهای یک Pod در حالی که `restartPolicy` روی Always تنظیم شده است خاتمه یابند و راه‌اندازی مجدد اجباری شود، و رکورد تکمیل init container به دلیل {{< glossary_tooltip text="garbage collection" term_id="garbage-collection" >}} از بین رفته باشد.

با تغییر ایمیج init container، یا از بین رفتن رکورد تکمیل init container به دلیل garbage collection، Pod راه‌اندازی مجدد نخواهد شد. این موضوع برای کوبرنتیز نسخه v1.20 و بعد از آن صدق می‌کند. اگر از نسخه قدیمی‌تری از کوبرنتیز استفاده می‌کنید، مستندات نسخه مورد استفاده خود را مطالعه کنید.

## {{% heading "whatsnext" %}}

درباره موارد زیر بیشتر بیاموزید:
* [ایجاد یک Pod که دارای init container است](/docs/tasks/configure-pod-container/configure-pod-initialization/#create-a-pod-that-has-an-init-container).
* [اشکال‌زدایی init containerها](/docs/tasks/debug/debug-application/debug-init-containers/).
* نمای کلی [kubelet](/docs/reference/command-line-tools-reference/kubelet/) و [kubectl](/docs/reference/kubectl/).
* [انواع probeها](/docs/concepts/workloads/pods/pod-lifecycle/#types-of-probe): probeهای liveness، readiness و startup.
* [کانتینرهای سایدکار](/docs/concepts/workloads/pods/sidecar-containers).

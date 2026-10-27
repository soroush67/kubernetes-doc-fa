---
reviewers:
- bprashanth
- janetkuo
title: ReplicationController
api_metadata:
- apiVersion: "v1"
  kind: "ReplicationController"
content_type: concept
weight: 90
description: >-
  API قدیمی برای مدیریت بارهای کاری که می‌توانند به‌صورت افقی مقیاس‌پذیر باشند.
  این API با APIهای Deployment و ReplicaSet جایگزین شده است.
---

<!-- overview -->

{{< note >}}
اکنون روش توصیه‌شده برای راه‌اندازی تکثیر (replication)، استفاده از یک [`Deployment`](/docs/concepts/workloads/controllers/deployment/) است که یک [`ReplicaSet`](/docs/concepts/workloads/controllers/replicaset/) را پیکربندی می‌کند.
{{< /note >}}

یک _ReplicationController_ تضمین می‌کند که در هر لحظه تعداد مشخصی از replicaهای Pod در حال اجرا
باشند. به بیان دیگر، ReplicationController اطمینان حاصل می‌کند که یک Pod یا مجموعه‌ای همگن از Podها
همواره فعال و در دسترس باشد.

<!-- body -->

## یک ReplicationController چگونه کار می‌کند

اگر تعداد Podها بیش از حد باشد، ReplicationController Podهای اضافی را خاتمه می‌دهد. اگر تعداد آن‌ها کمتر از حد لازم باشد،
ReplicationController Podهای بیشتری راه‌اندازی می‌کند. برخلاف Podهایی که به‌صورت دستی ایجاد می‌شوند، Podهایی که توسط
ReplicationController نگهداری می‌شوند، در صورت از کار افتادن، حذف شدن یا خاتمه یافتن به‌طور خودکار جایگزین می‌شوند.
برای مثال، Podهای شما پس از یک نگهداری مخرب مانند ارتقای کرنل، روی یک نود دوباره ایجاد می‌شوند.
به همین دلیل، حتی اگر برنامه شما تنها به یک Pod نیاز دارد، باید از یک ReplicationController
استفاده کنید. ReplicationController شبیه یک ناظر فرایند (process supervisor) است،
اما به‌جای نظارت بر فرایندهای منفرد روی یک نود، چندین Pod را در
چندین نود نظارت می‌کند.

ReplicationController در گفت‌وگوها اغلب به‌صورت «rc» خلاصه می‌شود و همین عبارت به‌عنوان میان‌بر در
فرمان‌های kubectl نیز به کار می‌رود.

یک حالت ساده این است که یک آبجکت ReplicationController ایجاد کنید تا یک نمونه از
یک Pod را به‌طور قابل اتکا و برای مدت نامحدود اجرا کند. یک کاربرد پیچیده‌تر، اجرای چندین replica یکسان از یک
سرویس تکثیرشده، مانند وب‌سرورها، است.

## اجرای یک ReplicationController نمونه

این پیکربندی نمونه ReplicationController سه نسخه از وب‌سرور nginx را اجرا می‌کند.

{{% code_sample file="controllers/replication.yaml" %}}

کار نمونه را با دانلود فایل نمونه و سپس اجرای این فرمان اجرا کنید:

```shell
kubectl apply -f https://k8s.io/examples/controllers/replication.yaml
```

خروجی مشابه زیر است:

```
replicationcontroller/nginx created
```

وضعیت ReplicationController را با استفاده از این فرمان بررسی کنید:

```shell
kubectl describe replicationcontrollers/nginx
```

خروجی مشابه زیر است:

```
Name:        nginx
Namespace:   default
Selector:    app=nginx
Labels:      app=nginx
Annotations:    <none>
Replicas:    3 current / 3 desired
Pods Status: 0 Running / 3 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:       app=nginx
  Containers:
   nginx:
    Image:              nginx
    Port:               80/TCP
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Events:
  FirstSeen       LastSeen     Count    From                        SubobjectPath    Type      Reason              Message
  ---------       --------     -----    ----                        -------------    ----      ------              -------
  20s             20s          1        {replication-controller }                    Normal    SuccessfulCreate    Created pod: nginx-qrm3m
  20s             20s          1        {replication-controller }                    Normal    SuccessfulCreate    Created pod: nginx-3ntk0
  20s             20s          1        {replication-controller }                    Normal    SuccessfulCreate    Created pod: nginx-4ok8v
```

در اینجا سه Pod ایجاد شده‌اند، اما هیچ‌کدام هنوز در حال اجرا نیستند؛ احتمالاً به این دلیل که ایمیج در حال دریافت (pull) است.
کمی بعد، همین فرمان ممکن است چنین چیزی نشان دهد:

```shell
Pods Status:    3 Running / 0 Waiting / 0 Succeeded / 0 Failed
```

برای فهرست کردن همه Podهای متعلق به ReplicationController به شکلی قابل خواندن برای ماشین، می‌توانید از فرمانی مانند این استفاده کنید:

```shell
pods=$(kubectl get pods --selector=app=nginx --output=jsonpath={.items..metadata.name})
echo $pods
```

خروجی مشابه زیر است:

```
nginx-3ntk0 nginx-4ok8v nginx-qrm3m
```

در اینجا، انتخابگر همان انتخابگر ReplicationController است (که در خروجی
`kubectl describe` دیده می‌شود) و به شکلی دیگر در `replication.yaml` آمده است. گزینه `--output=jsonpath`
عبارتی را مشخص می‌کند که نام هر Pod را در فهرست بازگردانده‌شده استخراج می‌کند.

## نوشتن مانیفست ReplicationController

مانند همه پیکربندی‌های دیگر کوبرنتیز، یک ReplicationController به فیلدهای `apiVersion`، `kind` و `metadata` نیاز دارد.

هنگامی که control plane برای یک ReplicationController، Podهای جدید ایجاد می‌کند، `.metadata.name` آن
ReplicationController بخشی از مبنای نام‌گذاری آن Podها است. نام یک ReplicationController باید یک مقدار معتبر
[زیردامنه DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)
باشد، اما این ممکن است برای نام میزبان (hostname) Podها نتایج غیرمنتظره‌ای ایجاد کند. برای بهترین سازگاری،
نام باید از قواعد سخت‌گیرانه‌تر یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) پیروی کند.

برای اطلاعات کلی درباره کار با فایل‌های پیکربندی، به [مدیریت آبجکت‌ها](/docs/concepts/overview/working-with-objects/object-management/) مراجعه کنید.

یک ReplicationController همچنین به یک [بخش `.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) نیاز دارد.

### قالب Pod

`.spec.template` تنها فیلد الزامی `.spec` است.

`.spec.template` یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) است. این قالب دقیقاً همان طرح‌واره (schema) یک {{< glossary_tooltip text="Pod" term_id="pod" >}} را دارد، با این تفاوت که تودرتو است و `apiVersion` یا `kind` ندارد.

افزون بر فیلدهای الزامی یک Pod، قالب Pod در یک ReplicationController باید برچسب‌های مناسب
و یک سیاست راه‌اندازی مجدد مناسب را مشخص کند. در مورد برچسب‌ها، مطمئن شوید که با کنترل‌کننده‌های دیگر هم‌پوشانی ندارند. به [انتخابگر Pod](#pod-selector) مراجعه کنید.

تنها مقدار مجاز برای [`.spec.template.spec.restartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) برابر با `Always` است که در صورت مشخص نشدن، مقدار پیش‌فرض نیز هست.

برای راه‌اندازی مجدد کانتینرهای محلی، ReplicationControllerها این کار را به عاملی روی نود،
برای مثال [Kubelet](/docs/reference/command-line-tools-reference/kubelet/)، واگذار می‌کنند.

### برچسب‌های روی ReplicationController

خود ReplicationController می‌تواند برچسب‌هایی (`.metadata.labels`) داشته باشد. معمولاً
این برچسب‌ها را همانند `.spec.template.metadata.labels` تنظیم می‌کنید؛ اگر `.metadata.labels` مشخص نشود،
مقدار پیش‌فرض آن `.spec.template.metadata.labels` خواهد بود. با این حال، متفاوت بودن آن‌ها مجاز است
و `.metadata.labels` بر رفتار ReplicationController تأثیری ندارد.

### انتخابگر Pod

فیلد `.spec.selector` یک [انتخابگر برچسب](/docs/concepts/overview/working-with-objects/labels/#label-selectors) است. یک ReplicationController
همه Podهایی را مدیریت می‌کند که برچسب‌هایشان با این انتخابگر مطابقت دارد. این کنترل‌کننده میان Podهایی که خودش ایجاد یا حذف کرده
و Podهایی که شخص یا فرایند دیگری ایجاد یا حذف کرده است، تمایزی قائل نمی‌شود.
این ویژگی امکان جایگزینی ReplicationController را بدون تأثیر بر Podهای در حال اجرا فراهم می‌کند.

در صورت مشخص شدن، `.spec.template.metadata.labels` باید برابر با `.spec.selector` باشد، در غیر این صورت
توسط API رد خواهد شد. اگر `.spec.selector` مشخص نشود، مقدار پیش‌فرض آن
`.spec.template.metadata.labels` خواهد بود.

همچنین در حالت عادی نباید هیچ Podای ایجاد کنید که برچسب‌هایش با این انتخابگر مطابقت داشته باشد؛ چه به‌طور مستقیم، چه با
یک ReplicationController دیگر و چه با کنترل‌کننده‌ای دیگر مانند Job. اگر چنین کنید،
ReplicationController تصور می‌کند که آن Podهای دیگر را خودش ایجاد کرده است. کوبرنتیز مانع
انجام این کار نمی‌شود.

اگر در نهایت چندین کنترل‌کننده با انتخابگرهای هم‌پوشان داشته باشید،
باید حذف را خودتان مدیریت کنید (به [بخش زیر](#working-with-replicationcontrollers) مراجعه کنید).

### چندین Replica

می‌توانید با تنظیم `.spec.replicas` روی تعداد Podهایی که می‌خواهید به‌طور هم‌زمان اجرا شوند،
مشخص کنید چند Pod باید به‌طور هم‌زمان اجرا شوند. تعداد Podهای در حال اجرا در هر لحظه ممکن است بیشتر
یا کمتر باشد؛ برای مثال، اگر تعداد replicaها تازه افزایش یا کاهش یافته باشد، یا اگر یک Pod به‌صورت مسالمت‌آمیز (graceful)
خاموش شود و جایگزین آن زودتر شروع به کار کند.

اگر `.spec.replicas` را مشخص نکنید، مقدار پیش‌فرض آن 1 است.

## کار با ReplicationControllerها

### حذف یک ReplicationController و Podهای آن

برای حذف یک ReplicationController و همه Podهای آن، از [`kubectl
delete`](/docs/reference/generated/kubectl/kubectl-commands#delete) استفاده کنید. Kubectl مقیاس ReplicationController را به صفر می‌رساند و
منتظر می‌ماند تا هر Pod حذف شود و سپس خود ReplicationController را حذف می‌کند. اگر این فرمان kubectl
قطع شود، می‌توان آن را دوباره اجرا کرد.

هنگام استفاده از REST API یا [کتابخانه کلاینت](/docs/reference/using-api/client-libraries)، باید این مراحل را به‌طور صریح انجام دهید (کاهش مقیاس replicaها به
0، انتظار برای حذف Podها و سپس حذف ReplicationController).

### حذف فقط یک ReplicationController

می‌توانید یک ReplicationController را بدون تأثیر بر هیچ‌یک از Podهای آن حذف کنید.

با استفاده از kubectl، گزینه `--cascade=orphan` را به [`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands#delete) بدهید.

هنگام استفاده از REST API یا [کتابخانه کلاینت](/docs/reference/using-api/client-libraries)، می‌توانید آبجکت ReplicationController را حذف کنید.

پس از حذف ReplicationController اصلی، می‌توانید یک ReplicationController جدید برای جایگزینی آن ایجاد کنید. تا زمانی که
`.spec.selector` قدیمی و جدید یکسان باشند، ReplicationController جدید Podهای قدیمی را به فرزندی می‌پذیرد.
با این حال، هیچ تلاشی برای منطبق کردن Podهای موجود با یک قالب Pod جدید و متفاوت انجام نمی‌دهد.
برای به‌روزرسانی کنترل‌شده Podها به یک spec جدید، از [به‌روزرسانی غلتان](#rolling-updates) استفاده کنید.

### جدا کردن Podها از یک ReplicationController

Podها را می‌توان با تغییر برچسب‌هایشان از مجموعه هدف یک ReplicationController خارج کرد. از این روش می‌توان برای خارج کردن Podها از سرویس به منظور اشکال‌زدایی و بازیابی داده استفاده کرد. Podهایی که به این روش جدا می‌شوند به‌طور خودکار جایگزین خواهند شد (با فرض اینکه تعداد replicaها نیز تغییر نکرده باشد).

## الگوهای رایج استفاده

### زمان‌بندی مجدد

همان‌طور که در بالا اشاره شد، چه 1 Pod داشته باشید که می‌خواهید در حال اجرا بماند و چه 1000 Pod، ReplicationController تضمین می‌کند که تعداد مشخص‌شده Pod وجود داشته باشد، حتی در صورت خرابی نود یا خاتمه یافتن Pod (برای مثال، به دلیل اقدامی از سوی یک عامل کنترلی دیگر).

### مقیاس‌دهی

ReplicationController امکان افزایش یا کاهش تعداد replicaها را، چه به‌صورت دستی و چه توسط یک عامل کنترلی مقیاس‌دهی خودکار، از طریق به‌روزرسانی فیلد `replicas` فراهم می‌کند.

### به‌روزرسانی‌های غلتان

ReplicationController به گونه‌ای طراحی شده است که با جایگزینی Podها به‌صورت یک‌به‌یک، به‌روزرسانی غلتان یک سرویس را تسهیل کند.

همان‌طور که در [#1353](https://issue.k8s.io/1353) توضیح داده شده است، رویکرد توصیه‌شده این است که یک ReplicationController جدید با 1 replica ایجاد کنید، مقیاس کنترل‌کننده جدید (+1) و قدیمی (-1) را یکی‌یکی تغییر دهید و سپس کنترل‌کننده قدیمی را پس از رسیدن به 0 replica حذف کنید. این روش مجموعه Podها را صرف‌نظر از خرابی‌های غیرمنتظره، به شکلی قابل پیش‌بینی به‌روزرسانی می‌کند.

در حالت ایده‌آل، کنترل‌کننده به‌روزرسانی غلتان آمادگی (readiness) برنامه را در نظر می‌گیرد و تضمین می‌کند که در هر لحظه تعداد کافی از Podها به‌طور مؤثر در حال سرویس‌دهی باشند.

دو ReplicationController باید Podهایی با دست‌کم یک برچسب متمایزکننده ایجاد کنند، مانند تگ ایمیج کانتینر اصلی Pod؛ زیرا معمولاً به‌روزرسانی ایمیج‌ها است که انگیزه انجام به‌روزرسانی‌های غلتان را ایجاد می‌کند.

### چندین مسیر انتشار

افزون بر اجرای چندین نسخه انتشار از یک برنامه در حین انجام یک به‌روزرسانی غلتان، رایج است که چندین نسخه انتشار برای مدتی طولانی یا حتی به‌طور پیوسته، با استفاده از چندین مسیر انتشار (release track) اجرا شوند. این مسیرها با برچسب‌ها از یکدیگر متمایز می‌شوند.

برای نمونه، یک سرویس ممکن است همه Podهای دارای `tier in (frontend), environment in (prod)` را هدف قرار دهد. حال فرض کنید 10 Pod تکثیرشده دارید که این لایه را تشکیل می‌دهند. اما می‌خواهید بتوانید نسخه جدیدی از این مؤلفه را به‌صورت «canary» آزمایش کنید. می‌توانید یک ReplicationController با مقدار `replicas` برابر 9 برای بخش عمده replicaها و با برچسب‌های `tier=frontend, environment=prod, track=stable` راه‌اندازی کنید و یک ReplicationController دیگر با مقدار `replicas` برابر 1 برای canary و با برچسب‌های `tier=frontend, environment=prod, track=canary` ایجاد کنید. اکنون سرویس هم Podهای canary و هم Podهای غیر canary را پوشش می‌دهد. اما می‌توانید ReplicationControllerها را جداگانه دست‌کاری کنید تا موارد را آزمایش کنید، نتایج را پایش کنید و غیره.

### استفاده از ReplicationControllerها همراه با Serviceها

چندین ReplicationController می‌توانند پشت یک سرویس واحد قرار گیرند تا برای مثال بخشی از ترافیک
به نسخه قدیمی و بخشی به نسخه جدید برود.

یک ReplicationController هرگز به‌خودی‌خود خاتمه نمی‌یابد، اما انتظار نمی‌رود به اندازه سرویس‌ها طول عمر داشته باشد. سرویس‌ها ممکن است از Podهایی تشکیل شوند که توسط چندین ReplicationController کنترل می‌شوند و انتظار می‌رود در طول عمر یک سرویس، ReplicationControllerهای زیادی ایجاد و نابود شوند (برای نمونه، برای انجام به‌روزرسانی Podهایی که سرویس را اجرا می‌کنند). هم خود سرویس‌ها و هم کلاینت‌هایشان باید از ReplicationControllerهایی که Podهای سرویس‌ها را نگهداری می‌کنند بی‌اطلاع بمانند.

## نوشتن برنامه برای تکثیر

Podهایی که توسط یک ReplicationController ایجاد می‌شوند قرار است جایگزین‌پذیر و از نظر معنایی یکسان باشند، هرچند پیکربندی‌های آن‌ها ممکن است به مرور زمان ناهمگن شود. این ویژگی آشکارا برای سرورهای بدون حالت تکثیرشده مناسب است، اما ReplicationControllerها را می‌توان برای حفظ در دسترس بودن برنامه‌های مبتنی بر انتخاب master، شارد‌شده (sharded) و مبتنی بر مخزن کارگر (worker-pool) نیز به کار برد. چنین برنامه‌هایی باید از سازوکارهای تخصیص پویای کار، مانند [صف‌های کاری RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)، استفاده کنند، نه از سفارشی‌سازی ایستا یا یک‌باره پیکربندی هر Pod که یک ضدالگو (anti-pattern) به شمار می‌رود. هرگونه سفارشی‌سازی Pod، مانند تعیین خودکار عمودی اندازه منابع (برای مثال cpu یا حافظه)، باید توسط یک فرایند کنترل‌کننده برخط دیگر انجام شود، فرایندی نه چندان متفاوت از خود ReplicationController.

## مسئولیت‌های ReplicationController

ReplicationController تضمین می‌کند که تعداد مطلوب Podها با انتخابگر برچسب آن مطابقت داشته باشند و عملیاتی باشند. در حال حاضر، تنها Podهای خاتمه‌یافته از شمارش آن کنار گذاشته می‌شوند. در آینده ممکن است [آمادگی (readiness)](https://issue.k8s.io/620) و سایر اطلاعات موجود در سیستم نیز در نظر گرفته شوند، ممکن است کنترل‌های بیشتری بر سیاست جایگزینی اضافه کنیم، و قصد داریم رویدادهایی منتشر کنیم که کلاینت‌های خارجی بتوانند از آن‌ها برای پیاده‌سازی سیاست‌های جایگزینی و/یا کاهش مقیاس با هر درجه از پیچیدگی استفاده کنند.

ReplicationController برای همیشه به همین مسئولیت محدود، مقید است. این کنترل‌کننده خودش بررسی‌های آمادگی (readiness probe) یا زنده بودن (liveness probe) را انجام نمی‌دهد. به‌جای انجام مقیاس‌دهی خودکار، قرار است توسط یک مقیاس‌دهنده خودکار خارجی کنترل شود (همان‌طور که در [#492](https://issue.k8s.io/492) بحث شده است) که فیلد `replicas` آن را تغییر می‌دهد. ما سیاست‌های زمان‌بندی (برای مثال [توزیع (spreading)](https://issue.k8s.io/367#issuecomment-48428019)) را به ReplicationController اضافه نخواهیم کرد. همچنین این کنترل‌کننده نباید بررسی کند که Podهای تحت کنترل با قالبی که در حال حاضر مشخص شده است مطابقت دارند یا نه، زیرا این کار مانع تعیین خودکار اندازه و سایر فرایندهای خودکار می‌شود. به همین ترتیب، مهلت‌های تکمیل، وابستگی‌های ترتیبی، بسط پیکربندی و سایر قابلیت‌ها به جای دیگری تعلق دارند. حتی قصد داریم سازوکار ایجاد انبوه Podها را نیز جدا کنیم ([#170](https://issue.k8s.io/170)).

ReplicationController قرار است یک بلوک سازنده ابتدایی و قابل ترکیب باشد. انتظار داریم در آینده APIها و/یا ابزارهای سطح بالاتری برای راحتی کاربران بر پایه آن و سایر عناصر ابتدایی مکمل ساخته شوند. عملیات «کلان» (macro) که در حال حاضر توسط kubectl پشتیبانی می‌شوند (run، scale) نمونه‌هایی اثبات مفهومی از این موضوع هستند. برای نمونه، می‌توان چیزی مانند [Asgard](https://netflixtechblog.com/asgard-web-based-cloud-management-and-deployment-2c9fc4e4d3a1) را تصور کرد که ReplicationControllerها، مقیاس‌دهنده‌های خودکار، سرویس‌ها، سیاست‌های زمان‌بندی، canaryها و غیره را مدیریت می‌کند.

## آبجکت API

Replication controller یک منبع سطح بالا در REST API کوبرنتیز است. جزئیات بیشتر درباره
آبجکت API را می‌توانید در اینجا بیابید:
[آبجکت API مربوط به ReplicationController](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#replicationcontroller-v1-core).

## جایگزین‌های ReplicationController

### ReplicaSet

[`ReplicaSet`](/docs/concepts/workloads/controllers/replicaset/) نسل بعدی ReplicationController است که از [انتخابگر برچسب مبتنی بر مجموعه](/docs/concepts/overview/working-with-objects/labels/#set-based-requirement) جدید پشتیبانی می‌کند.
این آبجکت عمدتاً توسط [Deployment](/docs/concepts/workloads/controllers/deployment/) به‌عنوان سازوکاری برای هماهنگ‌سازی ایجاد، حذف و به‌روزرسانی Podها استفاده می‌شود.
توجه داشته باشید که توصیه می‌کنیم به‌جای استفاده مستقیم از Replica Setها از Deploymentها استفاده کنید، مگر اینکه به هماهنگ‌سازی سفارشی به‌روزرسانی نیاز داشته باشید یا اصلاً به به‌روزرسانی نیازی نداشته باشید.

### Deployment (توصیه‌شده)

[`Deployment`](/docs/concepts/workloads/controllers/deployment/) یک آبجکت API سطح بالاتر است که Replica Setهای زیرین خود و Podهای آن‌ها را به‌روزرسانی می‌کند. اگر قابلیت به‌روزرسانی غلتان را می‌خواهید، استفاده از Deploymentها توصیه می‌شود، زیرا اعلانی و سمت سرور هستند و قابلیت‌های بیشتری دارند.

### Podهای مستقل (Bare Pods)

برخلاف حالتی که کاربر مستقیماً Podها را ایجاد کرده است، یک ReplicationController Podهایی را که به هر دلیلی حذف شده یا خاتمه یافته‌اند جایگزین می‌کند؛ برای مثال در صورت خرابی نود یا نگهداری مخرب نود، مانند ارتقای کرنل. به همین دلیل، توصیه می‌کنیم حتی اگر برنامه شما تنها به یک Pod نیاز دارد، از یک ReplicationController استفاده کنید. آن را مشابه یک ناظر فرایند در نظر بگیرید، با این تفاوت که به‌جای فرایندهای منفرد روی یک نود، چندین Pod را در چندین نود نظارت می‌کند. یک ReplicationController راه‌اندازی مجدد کانتینرهای محلی را به عاملی روی نود، مانند kubelet، واگذار می‌کند.

### Job

برای Podهایی که انتظار می‌رود خودشان خاتمه یابند (یعنی کارهای دسته‌ای یا batch jobs)، به‌جای ReplicationController از یک [`Job`](/docs/concepts/workloads/controllers/job/)
استفاده کنید.

### DaemonSet

برای Podهایی که یک عملکرد در سطح ماشین ارائه می‌دهند، مانند پایش ماشین یا ثبت لاگ ماشین، به‌جای ReplicationController از یک [`DaemonSet`](/docs/concepts/workloads/controllers/daemonset/)
استفاده کنید. طول عمر این Podها به طول عمر ماشین گره خورده است: Pod باید پیش از شروع سایر Podها روی ماشین در حال اجرا باشد و
خاتمه دادن به آن زمانی که ماشین برای راه‌اندازی مجدد یا خاموش شدن آماده است، بی‌خطر است.

## {{% heading "whatsnext" %}}

* درباره [Podها](/docs/concepts/workloads/pods) بیاموزید.
* درباره [Deployment](/docs/concepts/workloads/controllers/deployment/)، جایگزین
  ReplicationController، بیاموزید.
* `ReplicationController` بخشی از REST API کوبرنتیز است.
  تعریف آبجکت {{< api-reference page="core/replication-controller-v1" >}}
  را بخوانید تا API مربوط به replication controllerها را درک کنید.

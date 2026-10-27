---
reviewers:
- mikedanese
title: برچسب‌ها و انتخابگرها
content_type: concept
weight: 40
---

<!-- overview -->

_برچسب‌ها_ (labels) جفت‌های کلید/مقداری هستند که به
{{< glossary_tooltip text="آبجکت‌ها" term_id="object" >}} مانند پادها پیوست می‌شوند.
برچسب‌ها برای مشخص‌کردن ویژگی‌های شناسایی آبجکت‌ها در نظر گرفته شده‌اند
که برای کاربران معنادار و مرتبط هستند، اما به‌طور مستقیم معنایی برای
سیستم اصلی ندارند. از برچسب‌ها می‌توان برای سازمان‌دهی و انتخاب زیرمجموعه‌هایی از
آبجکت‌ها استفاده کرد. برچسب‌ها را می‌توان هنگام ایجاد به آبجکت‌ها پیوست کرد و سپس
در هر زمان آن‌ها را افزود یا تغییر داد. هر آبجکت می‌تواند مجموعه‌ای از برچسب‌های کلید/مقدار
تعریف‌شده داشته باشد. هر کلید باید برای یک آبجکت مشخص یکتا باشد.

```json
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

برچسب‌ها امکان پرس‌وجوها و watchهای کارآمد را فراهم می‌کنند و برای استفاده در رابط‌های کاربری
و CLIها ایده‌آل هستند. اطلاعات غیرشناسایی باید با استفاده از
[حاشیه‌نویسی‌ها](/docs/concepts/overview/working-with-objects/annotations/) ثبت شوند.

<!-- body -->

## انگیزه

برچسب‌ها به کاربران امکان می‌دهند ساختارهای سازمانی خود را به شیوه‌ای با وابستگی سست
بر آبجکت‌های سیستم نگاشت کنند، بدون آنکه کلاینت‌ها ملزم به ذخیرهٔ این نگاشت‌ها باشند.

استقرارهای سرویس و خطوط پردازش دسته‌ای اغلب موجودیت‌هایی چندبعدی هستند
(برای مثال، چند پارتیشن یا استقرار، چند مسیر انتشار، چند لایه،
چند میکروسرویس در هر لایه). مدیریت اغلب به عملیات‌هایی نیاز دارد که چند بخش را هم‌زمان در بر می‌گیرند،
و این امر کپسوله‌سازی بازنمایی‌های کاملاً سلسله‌مراتبی را می‌شکند، به‌ویژه سلسله‌مراتب‌های
انعطاف‌ناپذیری که توسط زیرساخت تعیین می‌شوند و نه توسط کاربران.

نمونه برچسب‌ها:

* `"release" : "stable"`، `"release" : "canary"`
* `"environment" : "dev"`، `"environment" : "qa"`، `"environment" : "production"`
* `"tier" : "frontend"`، `"tier" : "backend"`، `"tier" : "cache"`
* `"partition" : "customerA"`، `"partition" : "customerB"`
* `"track" : "daily"`، `"track" : "weekly"`

این‌ها نمونه‌هایی از
[برچسب‌های رایج](/docs/concepts/overview/working-with-objects/common-labels/) هستند؛
شما آزادید قراردادهای خود را ایجاد کنید.
به خاطر داشته باشید که کلید برچسب باید برای یک آبجکت مشخص یکتا باشد.

## نحو و مجموعهٔ نویسه‌ها

_برچسب‌ها_ جفت‌های کلید/مقدار هستند. کلیدهای معتبر برچسب دو بخش دارند: یک
پیشوند اختیاری و یک نام که با یک اسلش (`/`) از هم جدا می‌شوند. بخش نام الزامی است و
باید حداکثر ۶۳ نویسه باشد، با یک نویسهٔ الفبایی-عددی
(`[a-z0-9A-Z]`) آغاز و پایان یابد و در میان آن خط تیره (`-`)، زیرخط (`_`)، نقطه (`.`)
و نویسه‌های الفبایی-عددی قرار گیرند. پیشوند اختیاری است. در صورت تعیین، پیشوند
باید یک زیردامنهٔ DNS باشد: مجموعه‌ای از برچسب‌های DNS که با نقطه (`.`) از هم جدا شده‌اند،
در مجموع حداکثر ۲۵۳ نویسه، و پس از آن یک اسلش (`/`).

اگر پیشوند حذف شود، فرض می‌شود کلید برچسب مختص کاربر است.
اجزای خودکار سیستم (برای مثال `kube-scheduler`، `kube-controller-manager`،
`kube-apiserver`، `kubectl` یا سایر خودکارسازی‌های شخص ثالث) که برچسب‌هایی
به آبجکت‌های کاربر نهایی اضافه می‌کنند، باید یک پیشوند مشخص کنند.

پیشوندهای `kubernetes.io/` و `k8s.io/` برای اجزای اصلی کوبرنتیز
[رزرو شده‌اند](/docs/reference/labels-annotations-taints/).

مقدار معتبر برچسب:

* باید حداکثر ۶۳ نویسه باشد (می‌تواند خالی باشد)،
* در صورتی که خالی نباشد، باید با یک نویسهٔ الفبایی-عددی (`[a-z0-9A-Z]`) آغاز و پایان یابد،
* می‌تواند در میان خود شامل خط تیره (`-`)، زیرخط (`_`)، نقطه (`.`) و نویسه‌های الفبایی-عددی باشد.

برای مثال، در اینجا مانیفستی برای یک Pod آمده است که دو برچسب
`environment: production` و `app: nginx` دارد:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: label-demo
  labels:
    environment: production
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

## انتخابگرهای برچسب

برخلاف [نام‌ها و UIDها](/docs/concepts/overview/working-with-objects/names/)، برچسب‌ها
یکتایی فراهم نمی‌کنند. به‌طور کلی، انتظار داریم آبجکت‌های بسیاری برچسب(های) یکسانی داشته باشند.

از طریق یک _انتخابگر برچسب_ (label selector)، کلاینت/کاربر می‌تواند مجموعه‌ای از آبجکت‌ها را شناسایی کند.
انتخابگر برچسب ابزار اصلی گروه‌بندی در کوبرنتیز است.

API در حال حاضر از دو نوع انتخابگر پشتیبانی می‌کند: _مبتنی بر برابری_ (equality-based) و _مبتنی بر مجموعه_ (set-based).
یک انتخابگر برچسب می‌تواند از چند _الزام_ (requirement) تشکیل شود که با ویرگول از هم جدا می‌شوند.
در صورت وجود چند الزام، همهٔ آن‌ها باید برآورده شوند؛ بنابراین جداکنندهٔ ویرگول
مانند عملگر منطقی _AND_ (`&&`) عمل می‌کند.

معنای انتخابگرهای خالی یا تعیین‌نشده به زمینه بستگی دارد،
و انواع APIای که از انتخابگرها استفاده می‌کنند باید اعتبار و معنای
آن‌ها را مستند کنند.

{{< note >}}
برای برخی انواع API، مانند ReplicaSetها، انتخابگرهای برچسب دو نمونه نباید
درون یک فضای نام با هم هم‌پوشانی داشته باشند؛ در غیر این صورت کنترل‌کننده ممکن است آن را دستورالعمل‌های
متناقض تلقی کند و نتواند تعیین کند چه تعداد replica باید وجود داشته باشد.
{{< /note >}}

{{< caution >}}
هم برای شرط‌های مبتنی بر برابری و هم برای شرط‌های مبتنی بر مجموعه، هیچ عملگر منطقی _OR_ (`||`) وجود ندارد.
اطمینان حاصل کنید که عبارت‌های فیلتر شما متناسب با این موضوع ساختاربندی شده‌اند.
{{< /caution >}}

### الزام _مبتنی بر برابری_

الزام‌های _مبتنی بر برابری_ یا _مبتنی بر نابرابری_ امکان فیلترکردن بر اساس کلیدها و مقادیر برچسب را فراهم می‌کنند.
آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسب تعیین‌شده را برآورده کنند، هرچند ممکن است
برچسب‌های اضافی نیز داشته باشند. سه نوع عملگر پذیرفته می‌شود: `=`،`==`،`!=`.
دو عملگر نخست نشان‌دهندهٔ _برابری_ هستند (و مترادف‌اند)، در حالی که عملگر آخر نشان‌دهندهٔ _نابرابری_ است.
برای مثال:

```
environment = production
tier != frontend
```

اولی همهٔ منابعی را انتخاب می‌کند که کلید آن‌ها برابر `environment` و مقدارشان برابر `production` است.
دومی همهٔ منابعی را انتخاب می‌کند که کلید آن‌ها برابر `tier` و مقدارشان متفاوت از `frontend` است،
و نیز همهٔ منابعی که هیچ برچسبی با کلید `tier` ندارند. می‌توان منابع موجود در `production`
را به‌جز `frontend` با استفاده از عملگر ویرگول فیلتر کرد: `environment=production,tier!=frontend`

یکی از سناریوهای استفاده از الزام برچسب مبتنی بر برابری، تعیین معیارهای انتخاب نود
توسط پادهاست. برای مثال، Pod نمونهٔ زیر نودهایی را انتخاب می‌کند که
برچسب `accelerator` در آن‌ها وجود دارد و مقدار آن `nvidia-tesla-p100` است.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
    - name: cuda-test
      image: "registry.k8s.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1
  nodeSelector:
    accelerator: nvidia-tesla-p100
```

### الزام _مبتنی بر مجموعه_

الزام‌های برچسب _مبتنی بر مجموعه_ امکان فیلترکردن کلیدها بر اساس مجموعه‌ای از مقادیر را فراهم می‌کنند.
سه نوع عملگر پشتیبانی می‌شود: `in`،`notin` و `exists` (فقط شناسهٔ کلید).
برای مثال:

```
environment in (production, qa)
tier notin (frontend, backend)
partition
!partition
```

- مثال اول همهٔ منابعی را انتخاب می‌کند که کلید آن‌ها برابر `environment` و مقدارشان
  برابر `production` یا `qa` است.
- مثال دوم همهٔ منابعی را انتخاب می‌کند که کلید آن‌ها برابر `tier` و مقدارشان چیزی غیر
  از `frontend` و `backend` است، و نیز همهٔ منابعی که هیچ برچسبی با کلید `tier` ندارند.
- مثال سوم همهٔ منابعی را انتخاب می‌کند که برچسبی با کلید `partition` دارند؛
  هیچ مقداری بررسی نمی‌شود.
- مثال چهارم همهٔ منابعی را انتخاب می‌کند که برچسبی با کلید `partition` ندارند؛
  هیچ مقداری بررسی نمی‌شود.

به همین ترتیب، جداکنندهٔ ویرگول مانند عملگر _AND_ عمل می‌کند. بنابراین فیلترکردن منابعی
که کلید `partition` دارند (صرف‌نظر از مقدار) و مقدار `environment` آن‌ها متفاوت
از `qa` است، با استفاده از `partition,environment notin (qa)` امکان‌پذیر است.
انتخابگر برچسب _مبتنی بر مجموعه_ شکل کلی‌تری از برابری است، زیرا
`environment=production` معادل `environment in (production)` است؛
همین موضوع دربارهٔ `!=` و `notin` نیز صدق می‌کند.

الزام‌های _مبتنی بر مجموعه_ را می‌توان با الزام‌های _مبتنی بر برابری_ ترکیب کرد.
برای مثال: `partition in (customerA, customerB),environment!=qa`.

## API

### فیلترکردن LIST و WATCH

برای عملیات **list** و **watch**، می‌توانید انتخابگرهای برچسب را برای فیلترکردن مجموعه‌های آبجکت
بازگردانده‌شده مشخص کنید؛ فیلتر را با استفاده از یک پارامتر پرس‌وجو تعیین می‌کنید.
(برای آشنایی دقیق با watchها در کوبرنتیز،
[تشخیص کارآمد تغییرات](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) را بخوانید.)
هر دو نوع الزام مجاز هستند
(در اینجا به همان شکلی نمایش داده شده‌اند که در رشتهٔ پرس‌وجوی یک URL ظاهر می‌شوند):

* الزام‌های _مبتنی بر برابری_: `?labelSelector=environment%3Dproduction,tier%3Dfrontend`
* الزام‌های _مبتنی بر مجموعه_: `?labelSelector=environment+in+%28production%2Cqa%29%2Ctier+in+%28frontend%29`

از هر دو سبک انتخابگر برچسب می‌توان برای فهرست‌کردن یا watch کردن منابع از طریق یک کلاینت REST استفاده کرد.
برای مثال، با هدف قراردادن `apiserver` توسط `kubectl` و با استفاده از الزام _مبتنی بر برابری_ می‌توان نوشت:

```shell
kubectl get pods -l environment=production,tier=frontend
```

یا با استفاده از الزام‌های _مبتنی بر مجموعه_:

```shell
kubectl get pods -l 'environment in (production),tier in (frontend)'
```

همان‌طور که پیش‌تر اشاره شد، الزام‌های _مبتنی بر مجموعه_ بیان‌پذیری بیشتری دارند.
برای نمونه، می‌توانند عملگر _OR_ را روی مقادیر پیاده‌سازی کنند:

```shell
kubectl get pods -l 'environment in (production, qa)'
```

یا تطبیق منفی را از طریق عملگر _notin_ محدود کنند:

```shell
kubectl get pods -l 'environment,environment notin (frontend)'
```

### ارجاع به مجموعه‌ها در آبجکت‌های API

برخی آبجکت‌های کوبرنتیز، مانند [`services`](/docs/concepts/services-networking/service/)
و [`replicationcontrollers`](/docs/concepts/workloads/controllers/replicationcontroller/)،
نیز از انتخابگرهای برچسب برای مشخص‌کردن مجموعه‌هایی از منابع دیگر، مانند
[پادها](/docs/concepts/workloads/pods/)، استفاده می‌کنند.

#### Service و ReplicationController

مجموعهٔ پادهایی که یک `service` هدف قرار می‌دهد با یک انتخابگر برچسب تعریف می‌شود.
به همین ترتیب، جمعیت پادهایی که یک `replicationcontroller` باید
مدیریت کند نیز با یک انتخابگر برچسب تعریف می‌شود.

انتخابگرهای برچسب برای هر دو آبجکت در فایل‌های `json` یا `yaml` با استفاده از نگاشت‌ها (maps) تعریف می‌شوند،
و فقط انتخابگرهای الزام _مبتنی بر برابری_ پشتیبانی می‌شوند:

```json
"selector": {
    "component" : "redis",
}
```

یا

```yaml
selector:
  component: redis
```

این انتخابگر (به ترتیب در قالب `json` یا `yaml`) معادل
`component=redis` یا `component in (redis)` است.

#### منابعی که از الزام‌های مبتنی بر مجموعه پشتیبانی می‌کنند

منابع جدیدتر، مانند [`Job`](/docs/concepts/workloads/controllers/job/)،
[`Deployment`](/docs/concepts/workloads/controllers/deployment/)،
[`ReplicaSet`](/docs/concepts/workloads/controllers/replicaset/) و
[`DaemonSet`](/docs/concepts/workloads/controllers/daemonset/)،
از الزام‌های _مبتنی بر مجموعه_ نیز پشتیبانی می‌کنند.

```yaml
selector:
  matchLabels:
    component: redis
  matchExpressions:
    - { key: tier, operator: In, values: [cache] }
    - { key: environment, operator: NotIn, values: [dev] }
```

`matchLabels` نگاشتی از جفت‌های `{key,value}` است. یک `{key,value}` منفرد در
نگاشت `matchLabels` معادل عنصری از `matchExpressions` است که فیلد `key` آن
برابر «key»، `operator` آن برابر «In» و آرایهٔ `values` آن فقط شامل «value» است.
`matchExpressions` فهرستی از الزام‌های انتخابگر پاد است. عملگرهای معتبر عبارت‌اند از
In، NotIn، Exists و DoesNotExist. در مورد In و NotIn، مجموعهٔ مقادیر نباید خالی باشد.
همهٔ الزام‌ها، چه از `matchLabels` و چه از `matchExpressions`،
با AND با هم ترکیب می‌شوند -- برای تطبیق، همهٔ آن‌ها باید برآورده شوند.

#### انتخاب مجموعه‌هایی از نودها

یکی از موارد استفادهٔ انتخاب بر اساس برچسب‌ها، محدودکردن مجموعهٔ نودهایی است که
یک پاد می‌تواند روی آن‌ها زمان‌بندی شود. برای اطلاعات بیشتر به مستندات
[انتخاب نود](/docs/concepts/scheduling-eviction/assign-pod-node/) مراجعه کنید.

## استفادهٔ مؤثر از برچسب‌ها

می‌توانید یک برچسب واحد را روی هر منبعی اعمال کنید، اما این همیشه
بهترین روش نیست. سناریوهای بسیاری وجود دارد که در آن‌ها باید از چند برچسب برای
متمایزکردن مجموعه‌های منابع از یکدیگر استفاده کرد.

برای نمونه، برنامه‌های مختلف از مقادیر متفاوتی برای برچسب `app` استفاده می‌کنند، اما یک
برنامهٔ چندلایه، مانند [نمونهٔ guestbook](https://github.com/kubernetes/examples/tree/master/web/guestbook/)،
علاوه بر این باید هر لایه را نیز متمایز کند. 

در مثال‌های زیر، برچسب `app` برای سهولت در پرس‌وجوهای دستی
و استفادهٔ ساده از CLI گنجانده شده است. برچسب `app.kubernetes.io/name` از قراردادهای
برچسب‌گذاری توصیه‌شدهٔ کوبرنتیز پیروی می‌کند و برای ابزارها و خودکارسازی مناسب‌تر است.

لایهٔ frontend می‌تواند برچسب‌های زیر را داشته باشد:

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: frontend
```

در حالی که master و replica مربوط به Redis برچسب‌های `tier` متفاوتی خواهند داشت و شاید حتی یک
برچسب `role` اضافی نیز داشته باشند:

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: master
```

و

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: replica
```

برچسب‌ها امکان تفکیک و دسته‌بندی منابع را در امتداد هر بعدی که با یک برچسب مشخص شده باشد فراهم می‌کنند:

```shell
kubectl apply -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
kubectl get pods -Lapp -Ltier -Lrole
```

```none
NAME                           READY  STATUS    RESTARTS   AGE   APP         TIER       ROLE
guestbook-fe-4nlpb             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-ght6d             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-jpy62             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-redis-master-5pg3b   1/1    Running   0          1m    guestbook   backend    master
guestbook-redis-replica-2q2yf  1/1    Running   0          1m    guestbook   backend    replica
guestbook-redis-replica-qgazl  1/1    Running   0          1m    guestbook   backend    replica
my-nginx-divi2                 1/1    Running   0          29m   nginx       <none>     <none>
my-nginx-o0ef1                 1/1    Running   0          29m   nginx       <none>     <none>
```

```shell
kubectl get pods -lapp=guestbook,role=replica
```

```none
NAME                           READY  STATUS   RESTARTS  AGE
guestbook-redis-replica-2q2yf  1/1    Running  0         3m
guestbook-redis-replica-qgazl  1/1    Running  0         3m
```

## به‌روزرسانی برچسب‌ها

گاهی ممکن است بخواهید پیش از ایجاد منابع جدید، پادها و سایر منابع موجود را
دوباره برچسب‌گذاری کنید. این کار را می‌توان با `kubectl label` انجام داد.
برای مثال، اگر می‌خواهید همهٔ پادهای NGINX خود را به‌عنوان لایهٔ frontend برچسب‌گذاری کنید، دستور زیر را اجرا کنید:

```shell
kubectl label pods -l app=nginx tier=fe
```

```none
pod/my-nginx-2035384211-j5fhi labeled
pod/my-nginx-2035384211-u2c7e labeled
pod/my-nginx-2035384211-u3t6x labeled
```

این دستور ابتدا همهٔ پادهای دارای برچسب «app=nginx» را فیلتر می‌کند و سپس آن‌ها را با «tier=fe» برچسب‌گذاری می‌کند.
برای مشاهدهٔ پادهایی که برچسب‌گذاری کرده‌اید، دستور زیر را اجرا کنید:

```shell
kubectl get pods -l app=nginx -L tier
```

```none
NAME                        READY     STATUS    RESTARTS   AGE       TIER
my-nginx-2035384211-j5fhi   1/1       Running   0          23m       fe
my-nginx-2035384211-u2c7e   1/1       Running   0          23m       fe
my-nginx-2035384211-u3t6x   1/1       Running   0          23m       fe
```

این دستور همهٔ پادهای «app=nginx» را همراه با یک ستون برچسب اضافی برای لایهٔ پادها
(که با `-L` یا `--label-columns` مشخص شده است) نمایش می‌دهد.

برای اطلاعات بیشتر، لطفاً به [kubectl label](/docs/reference/generated/kubectl/kubectl-commands/#label) مراجعه کنید.

## {{% heading "whatsnext" %}}

- نحوهٔ [افزودن برچسب به یک نود](/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node) را بیاموزید
- [برچسب‌ها، حاشیه‌نویسی‌ها و Taintهای شناخته‌شده](/docs/reference/labels-annotations-taints/) را بیابید
- [برچسب‌های توصیه‌شده](/docs/concepts/overview/working-with-objects/common-labels/) را ببینید
- [اعمال استانداردهای امنیتی Pod با برچسب‌های Namespace](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
- یک پست وبلاگ دربارهٔ [نوشتن یک کنترل‌کننده برای برچسب‌های Pod](/blog/2021/06/21/writing-a-controller-for-pod-labels/) بخوانید

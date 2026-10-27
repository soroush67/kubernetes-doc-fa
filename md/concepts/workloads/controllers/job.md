---
reviewers:
- erictune
- mimowo
- soltysh
title: Jobs
api_metadata:
- apiVersion: "batch/v1"
  kind: "Job"
content_type: concept
description: >-
  Jobها نمایانگر وظایف یک‌باره‌ای هستند که تا پایان اجرا می‌شوند و سپس متوقف می‌گردند.
feature:
  title: اجرای دسته‌ای
  description: >
    علاوه بر سرویس‌ها، کوبرنتیز می‌تواند بارهای کاری دسته‌ای (batch) و CI شما را نیز مدیریت کند و در صورت نیاز، کانتینرهای ناموفق را جایگزین نماید.
weight: 50
hide_summary: true # Listed separately in section index
---

<!-- overview -->

یک Job یک یا چند Pod ایجاد می‌کند و تا زمانی که تعداد مشخصی از آن‌ها با موفقیت خاتمه یابند، به تلاش مجدد برای اجرای Podها ادامه می‌دهد.
با تکمیل موفقیت‌آمیز Podها، Job تعداد تکمیل‌های موفق را ردیابی می‌کند. هنگامی که تعداد مشخصی
از تکمیل‌های موفق حاصل شود، وظیفه (یعنی Job) کامل شده است. حذف یک Job، Podهایی را که ایجاد کرده است پاک‌سازی می‌کند.
تعلیق (suspend) یک Job، Podهای فعال آن را حذف می‌کند تا زمانی که Job
دوباره از سر گرفته شود.

ساده‌ترین حالت این است که یک آبجکت Job ایجاد شود تا یک Pod به‌صورت قابل‌اعتماد تا پایان اجرا شود.
اگر Pod اول با شکست مواجه شود یا حذف گردد (برای مثال
به دلیل خرابی سخت‌افزاری نود یا راه‌اندازی مجدد نود)، آبجکت Job یک Pod جدید راه‌اندازی می‌کند.

همچنین می‌توانید از Job برای اجرای موازی چند Pod استفاده کنید.

اگر می‌خواهید یک Job (چه یک وظیفه‌ی واحد و چه چند وظیفه‌ی موازی) را بر اساس یک زمان‌بندی اجرا کنید،
به [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) مراجعه کنید.

<!-- body -->

## اجرای یک Job نمونه {#running-an-example-job}

در اینجا یک پیکربندی نمونه‌ی Job آمده است. این Job عدد π را تا ۲۰۰۰ رقم اعشار محاسبه و چاپ می‌کند.
اجرای آن حدود ۱۰ ثانیه طول می‌کشد.

{{% code_sample file="controllers/job.yaml" %}}

می‌توانید نمونه را با این دستور اجرا کنید:

```shell
kubectl apply -f https://kubernetes.io/examples/controllers/job.yaml
```

خروجی مشابه زیر است:

```
job.batch/pi created
```

وضعیت Job را با `kubectl` بررسی کنید:

{{< tabs name="Check status of Job" >}}
{{< tab name="kubectl describe job pi" codelang="bash" >}}
Name:           pi
Namespace:      default
Selector:       batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
Labels:         batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
                batch.kubernetes.io/job-name=pi
                ...
Annotations:    batch.kubernetes.io/job-tracking: ""
Parallelism:    1
Completions:    1
Start Time:     Mon, 02 Dec 2019 15:20:11 +0200
Completed At:   Mon, 02 Dec 2019 15:21:16 +0200
Duration:       65s
Pods Statuses:  0 Running / 1 Succeeded / 0 Failed
Pod Template:
  Labels:  batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
           batch.kubernetes.io/job-name=pi
  Containers:
   pi:
    Image:      perl:5.34.0
    Port:       <none>
    Host Port:  <none>
    Command:
      perl
      -Mbignum=bpi
      -wle
      print bpi(2000)
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From            Message
  ----    ------            ----  ----            -------
  Normal  SuccessfulCreate  21s   job-controller  Created pod: pi-xf9p4
  Normal  Completed         18s   job-controller  Job completed
{{< /tab >}}
{{< tab name="kubectl get job pi -o yaml" codelang="bash" >}}
apiVersion: batch/v1
kind: Job
metadata:
  annotations: batch.kubernetes.io/job-tracking: ""
             ...  
  creationTimestamp: "2022-11-10T17:53:53Z"
  generation: 1
  labels:
    batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
    batch.kubernetes.io/job-name: pi
  name: pi
  namespace: default
  resourceVersion: "4751"
  uid: 204fb678-040b-497f-9266-35ffa8716d14
spec:
  backoffLimit: 4
  completionMode: NonIndexed
  completions: 1
  parallelism: 1
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
  suspend: false
  template:
    metadata:
      creationTimestamp: null
      labels:
        batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
        batch.kubernetes.io/job-name: pi
    spec:
      containers:
      - command:
        - perl
        - -Mbignum=bpi
        - -wle
        - print bpi(2000)
        image: perl:5.34.0
        imagePullPolicy: IfNotPresent
        name: pi
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Never
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  active: 1
  ready: 0
  startTime: "2022-11-10T17:53:57Z"
  uncountedTerminatedPods: {}
{{< /tab >}}
{{< /tabs >}}

برای مشاهده‌ی Podهای تکمیل‌شده‌ی یک Job از `kubectl get pods` استفاده کنید.

برای فهرست کردن همه‌ی Podهایی که به یک Job تعلق دارند، به شکلی که برای ماشین قابل خواندن باشد، می‌توانید از دستوری مانند زیر استفاده کنید:

```shell
pods=$(kubectl get pods --selector=batch.kubernetes.io/job-name=pi --output=jsonpath='{.items[*].metadata.name}')
echo $pods
```

خروجی مشابه زیر است:

```
pi-5rwd7
```

در اینجا، انتخابگر (selector) همان انتخابگر Job است. گزینه‌ی `--output=jsonpath` عبارتی را مشخص می‌کند
که نام هر Pod را از فهرست بازگردانده‌شده استخراج می‌کند.

خروجی استاندارد یکی از Podها را مشاهده کنید:

```shell
kubectl logs $pods
```

روش دیگر برای مشاهده‌ی لاگ‌های یک Job:

```shell
kubectl logs jobs/pi
```

خروجی مشابه زیر است:

```
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275901
```

## نوشتن مشخصات (spec) یک Job {#writing-a-job-spec}

همانند همه‌ی پیکربندی‌های دیگر کوبرنتیز، یک Job به فیلدهای `apiVersion`، `kind` و `metadata` نیاز دارد.

هنگامی که control plane برای یک Job، Podهای جدید ایجاد می‌کند، مقدار `.metadata.name` مربوط به
Job بخشی از مبنای نام‌گذاری آن Podها است. نام یک Job باید یک مقدار معتبر
[زیردامنه‌ی DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)
باشد، اما این موضوع ممکن است برای نام میزبان (hostname) Podها نتایج غیرمنتظره‌ای ایجاد کند. برای بیشترین سازگاری،
نام باید از قواعد سخت‌گیرانه‌تر
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) پیروی کند.
حتی اگر نام یک زیردامنه‌ی DNS باشد، طول آن نباید از ۶۳
نویسه بیشتر شود.

یک Job همچنین به یک [بخش `.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) نیاز دارد.

### برچسب‌های Job {#job-labels}

برچسب‌های Job برای `job-name` و `controller-uid` پیشوند `batch.kubernetes.io/` دارند.

### قالب Pod {#pod-template}

`.spec.template` تنها فیلد الزامی در `.spec` است.

`.spec.template` یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) است.
این قالب دقیقاً همان طرح‌واره‌ی (schema) یک {{< glossary_tooltip text="Pod" term_id="pod" >}} را دارد،
با این تفاوت که تو در تو است و `apiVersion` یا `kind` ندارد.

علاوه بر فیلدهای الزامی برای یک Pod، قالب Pod در یک Job باید
برچسب‌های مناسب (به [انتخابگر Pod](#pod-selector) مراجعه کنید) و یک سیاست راه‌اندازی مجدد مناسب مشخص کند.

تنها [`RestartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)
برابر با `Never` یا `OnFailure` مجاز است.

### انتخابگر Pod {#pod-selector}

فیلد `.spec.selector` اختیاری است. در تقریباً همه‌ی موارد نباید آن را مشخص کنید.
به بخش [مشخص کردن انتخابگر Pod اختصاصی خودتان](#specifying-your-own-pod-selector) مراجعه کنید.

### اجرای موازی برای Jobها {#parallel-jobs}

سه نوع اصلی وظیفه وجود دارد که برای اجرا به‌صورت Job مناسب هستند:

1. Jobهای غیرموازی
   - معمولاً فقط یک Pod راه‌اندازی می‌شود، مگر اینکه Pod با شکست مواجه شود.
   - Job به محض اینکه Pod آن با موفقیت خاتمه یابد، کامل می‌شود.
1. Jobهای موازی با *تعداد تکمیل ثابت*:
   - یک مقدار مثبت و غیرصفر برای `.spec.completions` مشخص کنید.
   - Job نمایانگر کل وظیفه است و زمانی کامل می‌شود که به تعداد `.spec.completions` Pod موفق وجود داشته باشد.
   - هنگام استفاده از `.spec.completionMode="Indexed"`، به هر Pod یک ایندکس متفاوت در بازه‌ی ۰ تا `.spec.completions-1` اختصاص داده می‌شود.
1. Jobهای موازی با *صف کار (work queue)*:
   - `.spec.completions` را مشخص نکنید؛ مقدار پیش‌فرض آن برابر `.spec.parallelism` است.
   - Podها باید با یکدیگر یا با یک سرویس خارجی هماهنگ شوند تا مشخص کنند
     هرکدام باید روی چه کاری کار کند. برای مثال، یک Pod ممکن است دسته‌ای شامل حداکثر N آیتم را از صف کار دریافت کند.
   - هر Pod به‌طور مستقل می‌تواند تشخیص دهد که آیا همه‌ی همتایان آن کار خود را تمام کرده‌اند یا خیر،
     و در نتیجه کل Job به پایان رسیده است.
   - هنگامی که _هر_ Pod از Job با موفقیت خاتمه یابد، هیچ Pod جدیدی ایجاد نمی‌شود.
   - هنگامی که دست‌کم یک Pod با موفقیت خاتمه یافته و همه‌ی Podها پایان یافته باشند،
     Job با موفقیت کامل می‌شود.
   - به محض اینکه هر Pod با موفقیت خارج شود، هیچ Pod دیگری نباید همچنان برای این وظیفه کار کند
     یا خروجی بنویسد. همه‌ی آن‌ها باید در حال خروج باشند.

برای یک Job _غیرموازی_، می‌توانید هر دو فیلد `.spec.completions` و `.spec.parallelism` را تنظیم‌نشده رها کنید.
وقتی هر دو تنظیم‌نشده باشند، مقدار پیش‌فرض هر دو برابر ۱ است.

برای یک Job با _تعداد تکمیل ثابت_، باید `.spec.completions` را برابر با تعداد تکمیل‌های موردنیاز تنظیم کنید.
می‌توانید `.spec.parallelism` را تنظیم کنید یا آن را تنظیم‌نشده رها کنید که در این صورت مقدار پیش‌فرض آن ۱ خواهد بود.

برای یک Job از نوع _صف کار_، باید `.spec.completions` را تنظیم‌نشده رها کنید و `.spec.parallelism` را روی
یک عدد صحیح نامنفی تنظیم کنید.

برای اطلاعات بیشتر درباره‌ی نحوه‌ی استفاده از انواع مختلف Job،
به بخش [الگوهای Job](#job-patterns) مراجعه کنید.

#### کنترل میزان موازی‌سازی {#controlling-parallelism}

میزان موازی‌سازی درخواستی (`.spec.parallelism`) را می‌توان روی هر مقدار نامنفی تنظیم کرد.
اگر مشخص نشود، مقدار پیش‌فرض آن ۱ است.
اگر روی ۰ تنظیم شود، Job عملاً متوقف می‌ماند تا زمانی که این مقدار افزایش یابد.

میزان موازی‌سازی واقعی (تعداد Podهای در حال اجرا در هر لحظه) ممکن است به دلایل گوناگون بیشتر یا کمتر از
میزان موازی‌سازی درخواستی باشد:

- برای Jobهای با _تعداد تکمیل ثابت_، تعداد واقعی Podهایی که به‌صورت موازی اجرا می‌شوند از تعداد
  تکمیل‌های باقی‌مانده بیشتر نخواهد شد. مقادیر بزرگ‌تر `.spec.parallelism` عملاً نادیده گرفته می‌شوند.
- برای Jobهای از نوع _صف کار_، پس از موفقیت هر Pod هیچ Pod جدیدی راه‌اندازی نمی‌شود؛ با این حال، به Podهای باقی‌مانده اجازه داده می‌شود تا کار خود را کامل کنند.
- اگر {{< glossary_tooltip term_id="controller" text="کنترل‌کننده" >}} Job فرصت واکنش نداشته باشد.
- اگر کنترل‌کننده‌ی Job به هر دلیلی (نبود `ResourceQuota`، نبود مجوز و غیره) در ایجاد Podها ناموفق باشد،
  ممکن است تعداد Podها کمتر از مقدار درخواستی باشد.
- کنترل‌کننده‌ی Job ممکن است به دلیل شکست‌های بیش از حد Podهای قبلی در همان Job، ایجاد Podهای جدید را محدود (throttle) کند.
- هنگامی که یک Pod به‌صورت مؤدبانه (gracefully) خاموش می‌شود، توقف آن زمان می‌برد.

### حالت تکمیل (Completion mode) {#completion-mode}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

Jobهای با _تعداد تکمیل ثابت_ - یعنی Jobهایی که مقدار `.spec.completions` آن‌ها null نیست -
می‌توانند یک حالت تکمیل داشته باشند که در `.spec.completionMode` مشخص می‌شود:

- `NonIndexed` (پیش‌فرض): Job زمانی کامل در نظر گرفته می‌شود که
  `.spec.completions` Pod با موفقیت تکمیل شده باشد. به بیان دیگر، تکمیل هر Pod
  با تکمیل Podهای دیگر هم‌ارز است. توجه داشته باشید که Jobهایی که مقدار
  `.spec.completions` آن‌ها null است، به‌طور ضمنی `NonIndexed` هستند.
- `Indexed`: به Podهای یک Job یک ایندکس تکمیل از ۰ تا
  `.spec.completions-1` اختصاص داده می‌شود. این ایندکس از چهار طریق در دسترس است:
  - حاشیه‌نویسی (annotation) Pod با نام `batch.kubernetes.io/job-completion-index`.
  - برچسب Pod با نام `batch.kubernetes.io/job-completion-index` (برای نسخه‌ی v1.28 و بالاتر). توجه کنید
    که برای استفاده از این برچسب باید feature gate با نام `PodIndexLabel` فعال باشد، که به‌طور پیش‌فرض
    فعال است.
  - به‌عنوان بخشی از نام میزبان (hostname) Pod، مطابق الگوی `$(job-name)-$(index)`.
    وقتی از یک Job از نوع Indexed همراه با یک
    {{< glossary_tooltip term_id="Service" text="Service" >}} استفاده می‌کنید، Podهای درون Job می‌توانند
    با استفاده از نام‌های میزبان قطعی (deterministic) از طریق DNS یکدیگر را آدرس‌دهی کنند. برای اطلاعات بیشتر درباره‌ی
    نحوه‌ی پیکربندی این قابلیت، به [Job با ارتباط Pod به Pod](/docs/tasks/job/job-with-pod-to-pod-communication/) مراجعه کنید.
  - از درون وظیفه‌ی کانتینری‌شده، در متغیر محیطی `JOB_COMPLETION_INDEX`.

  Job زمانی کامل در نظر گرفته می‌شود که برای هر ایندکس یک Pod
  با موفقیت تکمیل شده باشد. برای اطلاعات بیشتر درباره‌ی نحوه‌ی استفاده از این حالت، به
  [Indexed Job برای پردازش موازی با تخصیص ایستای کار](/docs/tasks/job/indexed-parallel-processing-static/) مراجعه کنید.

{{< note >}}
اگرچه به‌ندرت رخ می‌دهد، ممکن است به دلایل مختلف مانند خرابی نود،
راه‌اندازی مجدد kubelet یا حذف (eviction) Pod، بیش از یک Pod برای یک ایندکس یکسان راه‌اندازی شود. در این حالت، تنها اولین Podی که با موفقیت تکمیل شود
در شمارش تکمیل‌ها لحاظ می‌شود و وضعیت Job را به‌روزرسانی می‌کند. سایر Podهایی که برای همان ایندکس در حال اجرا
یا تکمیل‌شده هستند، پس از شناسایی توسط کنترل‌کننده‌ی Job حذف خواهند شد.
{{< /note >}}

## یکپارچه‌سازی با APIهای Workload {#integrate-with-workload-apis}

{{< feature-state feature_gate_name="WorkloadWithJob" >}}

هنگامی که feature gate با نام [`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/)
فعال باشد، کنترل‌کننده‌ی Job پیکربندی `.spec.scheduling` یک Job را پیش از ایجاد هر Pod به آبجکت‌های
[Workload](/docs/concepts/workloads/workload-api/) و
[PodGroup](/docs/concepts/workloads/podgroup-api/) (با نسخه‌ی `scheduling.k8s.io/v1beta1`) کامپایل می‌کند.
این کار به شما امکان می‌دهد نیت زمان‌بندی صریح را برای یک Job بیان کنید،
مانند [زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) (زمان‌بندی همه‌ی Podها
با هم یا هیچ‌کدام)، هم‌مکانی توپولوژیک و رفتار در برابر اختلال (disruption).

وقتی `.spec.scheduling` را حذف کنید، Job به سیاست زمان‌بندی `Basic` پیش‌فرض می‌شود که
نتیجه‌ی استاندارد زمان‌بندی Pod به Pod یک Job معمولی را حفظ می‌کند. کنترل‌کننده همچنان برای هر
Job واجد شرایط (از جمله Jobهای `Basic`) یک `Workload` و یک `PodGroup` ایجاد می‌کند، بنابراین آبجکت‌های قابل مشاهده
فارغ از سیاست، یکسان و سازگار هستند.

### پیکربندی زمان‌بندی {#scheduling-configuration}

فیلد `.spec.scheduling` فیلدهای زیر را می‌پذیرد:

- `schedulingPolicy`: دقیقاً یکی از `basic` یا `gang` باید مشخص شود. با `gang`،
  همه‌ی Podها باید پیش از آنکه هرکدام متصل (bind) شوند، با هم قابل زمان‌بندی باشند. اگر `gang.minCount` حذف شود،
  مقدار پیش‌فرض آن برابر `.spec.parallelism` مربوط به Job است. به
  [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) مراجعه کنید.
- `schedulingConstraints`:
  محدودیت‌های هم‌مکانی [توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
  برای Podهای Job.
- `disruptionMode`: اینکه Podها به‌صورت جداگانه (`single`) یا به‌صورت گروهی (`all`)
  دچار اختلال شوند. به
  [اختلال و اولویت](/docs/concepts/workloads/workload-api/disruption-and-priority/) مراجعه کنید.
- `resourceClaims`: درخواست‌های منبع پویا که میان Podهای Job به اشتراک گذاشته می‌شوند.

همه‌ی فیلدهای `.spec.scheduling` پس از ایجاد Job تغییرناپذیر (immutable) هستند، به‌جز
`schedulingPolicy.gang.minCount` که می‌توانید برای
[مقیاس‌دهی کشسان یک gang](#elastic-indexed-jobs) آن را تغییر دهید.

### زمان‌بندی گروهی (Gang scheduling) {#gang-scheduling}

Job زیر زمان‌بندی گروهی را برای ۸ Pod خود درخواست می‌کند، به‌طوری که Podها در یک
zone واحد هم‌مکان باشند و به‌صورت گروهی دچار اختلال شوند:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: distributed-training
  namespace: training
spec:
  parallelism: 8
  completions: 8
  completionMode: Indexed
  scheduling:
    schedulingPolicy:
      gang: {}                # minCount omitted -> defaults to parallelism (8)
    schedulingConstraints:
      key:
      - level: topology.kubernetes.io/zone
    disruptionMode:
      all: {}                 # the entire group is disrupted together
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: trainer
        image: training-image:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

هنگامی که کنترل‌کننده‌ی Job این Job را پردازش می‌کند، مراحل زیر را انجام می‌دهد:

1. یک آبجکت [Workload](/docs/concepts/workloads/workload-api/) در همان
   فضای نام (namespace) ایجاد می‌کند که شامل یک `podGroupTemplate` کامپایل‌شده از `.spec.scheduling` است
   (در اینجا، یک [سیاست gang](/docs/concepts/workloads/workload-api/policies/) با
   `minCount: 8`).
1. یک آبجکت PodGroup از روی آن قالب ایجاد می‌کند. PodGroup واحد زمان‌بندی زمان اجرا است
   و یک نسخه‌ی درون‌خطی از سیاست را به همراه دارد.
1. Podها را با تنظیم `.spec.schedulingGroup.podGroupName` روی نام
   PodGroup ایجاد می‌کند و بدین ترتیب هر Pod را به گروه زمان‌بندی خود پیوند می‌دهد.

کنترل‌کننده این آبجکت‌ها را از طریق ارجاعات درون spec
(`Workload.spec.controllerRef` و `PodGroup.spec.workloadRef`) پیدا می‌کند، نه از طریق
نام. آبجکت‌هایی که کنترل‌کننده ایجاد می‌کند دارای یک ورودی `ownerReferences` هستند که به
Job اشاره می‌کند، بنابراین با حذف Job، توسط garbage collector جمع‌آوری می‌شوند.

### زمان‌بندی پیش‌فرض (Basic) {#default-basic-scheduling}

یک Job که `.spec.scheduling` را حذف کند، به‌طور پیش‌فرض `Basic` خواهد بود که به‌منزله‌ی انصراف ضمنی
از زمان‌بندی گروهی است. Podهای آن مانند یک Job معمولی زمان‌بندی می‌شوند،
در حالی که همچنان یک `Workload` و `PodGroup` از نوع `Basic` ایجاد می‌شود:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-processor
  namespace: batch
spec:
  parallelism: 10
  completions: 10
  # .spec.scheduling omitted -> defaults to Basic scheduling.
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: processor
        image: processor-image:v1
```

### کنترل‌کننده‌های سطح بالاتر {#higher-level-controllers}

برای یک Job مستقل، کنترل‌کننده‌ی Job مالک هر دو آبجکت `Workload` و
`PodGroup` است. اما وقتی یک Job دارای `ownerReference` به یک کنترل‌کننده‌ی والد باشد
که `Workload` را کامپایل می‌کند (برای مثال `JobSet`)، کنترل‌کننده‌ی Job مالکیت
`Workload` را به آن والد واگذار می‌کند. اینکه کنترل‌کننده‌ی Job همچنان
`PodGroup` زمان اجرا را ایجاد کند یا نه، به آنچه والد واگذار می‌کند بستگی دارد:

- اگر والد حاشیه‌نویسی (annotation) با نام `scheduling.k8s.io/group-template-name` را روی
  Job تنظیم کند، کنترل‌کننده‌ی Job، `PodGroup` را ایجاد می‌کند و مالک آن می‌شود و آن را به
  `PodGroupTemplate` نام‌برده‌شده‌ی والد نگاشت می‌کند.
- در غیر این صورت، والد مالک هر دو آبجکت است و کنترل‌کننده‌ی Job هیچ‌کدام را ایجاد نمی‌کند؛
  بلکه آبجکت‌های موجود را شناسایی می‌کند و هنگام ایجاد Podها از آن‌ها استفاده می‌کند.

اگر قالب Pod یک Job از قبل `.spec.template.spec.schedulingGroup` را تنظیم کرده باشد،
کنترل‌کننده‌ی Job هیچ‌یک از دو آبجکت را ایجاد نمی‌کند و به شما (یا یک کنترل‌کننده‌ی سطح بالاتر) اجازه می‌دهد
چرخه‌ی عمر `Workload`/`PodGroup` را خودتان مدیریت کنید.

### رفتار CronJob {#cronjob-behavior}

Jobهایی که توسط یک `CronJob` ایجاد می‌شوند مستقل هستند؛ `CronJob` آبجکت‌های `Workload` را
ایجاد یا مدیریت نمی‌کند. اگر `jobTemplate` یک `CronJob` مقدار `.spec.scheduling` را تنظیم کند،
کنترل‌کننده‌ی Job برای هر نمونه‌ی Job یک `Workload` و `PodGroup` جداگانه ایجاد می‌کند
که از `.spec.scheduling` همان Job کامپایل می‌شوند (در صورت حذف، پیش‌فرض `Basic` است).
این آبجکت‌ها با تکمیل یا حذف هر Job توسط garbage collector جمع‌آوری می‌شوند.

### محدودیت‌ها در نسخه‌ی آلفا {#workload-integration-limitations}

- هر Job دقیقاً به یک `PodGroup` نگاشت می‌شود؛ همه‌ی Podهای درون Job یک
  سیاست زمان‌بندی واحد را به اشتراک می‌گذارند.
- تنها `schedulingPolicy.gang.minCount` قابل تغییر (mutable) است؛ همه‌ی فیلدهای دیگر `.spec.scheduling`
  پس از ایجاد تغییرناپذیر هستند.
- Jobهای تعلیق‌شده (suspended) آبجکت‌های `Workload` و `PodGroup` خود را حفظ می‌کنند؛ این آبجکت‌ها
  هنگام تعلیق حذف نمی‌شوند و هنگام از سرگیری دوباره ایجاد نمی‌شوند.

## مدیریت خطاهای Pod و کانتینر

یک کانتینر در یک Pod ممکن است به دلایل مختلفی با شکست مواجه شود؛ برای مثال به این دلیل که پردازش درون آن با کد خروج غیرصفر پایان یافته است، یا کانتینر به علت فراتر رفتن از محدودیت حافظه متوقف (kill) شده است و موارد مشابه. اگر چنین اتفاقی بیفتد و مقدار `.spec.template.spec.restartPolicy = "OnFailure"` باشد، Pod روی نود باقی می‌ماند، اما کانتینر دوباره اجرا می‌شود. بنابراین برنامه شما باید حالتی را که به‌صورت محلی دوباره راه‌اندازی می‌شود مدیریت کند، یا در غیر این صورت مقدار `.spec.template.spec.restartPolicy = "Never"` را مشخص کنید.
برای اطلاعات بیشتر درباره `restartPolicy` به [چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) مراجعه کنید.

یک Pod به‌طور کامل نیز ممکن است به دلایل مختلفی با شکست مواجه شود؛ برای مثال زمانی که Pod از روی نود بیرون رانده می‌شود (نود ارتقا می‌یابد، راه‌اندازی مجدد می‌شود، حذف می‌شود و غیره)، یا زمانی که یکی از کانتینرهای Pod با شکست مواجه می‌شود و مقدار `.spec.template.spec.restartPolicy = "Never"` است. هنگامی که یک Pod با شکست مواجه می‌شود، کنترل‌کننده Job یک Pod جدید راه‌اندازی می‌کند. این بدان معناست که برنامه شما باید حالتی را که در یک Pod جدید دوباره راه‌اندازی می‌شود مدیریت کند. به‌طور خاص، برنامه باید فایل‌های موقت، قفل‌ها، خروجی ناقص و موارد مشابهی را که در اجراهای قبلی ایجاد شده‌اند مدیریت کند.

به‌طور پیش‌فرض، هر شکست Pod در حد مجاز `.spec.backoffLimit` شمارش می‌شود؛
به [سیاست شکست backoff در Pod](#pod-backoff-failure-policy) مراجعه کنید. با این حال، می‌توانید با تنظیم [سیاست شکست Pod](#pod-failure-policy) برای Job، نحوه مدیریت شکست‌های Pod را سفارشی کنید.

علاوه بر این، می‌توانید با تنظیم فیلد `.spec.backoffLimitPerIndex`، شکست‌های Pod را برای هر ایندکس از یک Job از نوع [Indexed](#completion-mode) به‌صورت مستقل شمارش کنید
(برای اطلاعات بیشتر به [محدودیت backoff به‌ازای هر ایندکس](#backoff-limit-per-index) مراجعه کنید).

توجه داشته باشید که حتی اگر `.spec.parallelism = 1`، `.spec.completions = 1` و
`.spec.template.spec.restartPolicy = "Never"` را مشخص کنید، ممکن است گاهی یک برنامه
دو بار راه‌اندازی شود.

اگر هر دو مقدار `.spec.parallelism` و `.spec.completions` را بزرگ‌تر از 1 مشخص کنید، ممکن است چندین Pod به‌طور هم‌زمان در حال اجرا باشند. بنابراین Podهای شما باید نسبت به هم‌روندی (concurrency) نیز تحمل‌پذیر باشند.

اگر فیلد `.spec.podFailurePolicy` را مشخص کنید، کنترل‌کننده Job یک Pod در حال خاتمه (Pod ای که فیلد `.metadata.deletionTimestamp` آن تنظیم شده است) را تا زمانی که آن Pod به وضعیت پایانی نرسد (یعنی `.status.phase` آن `Failed` یا `Succeeded` شود) شکست محسوب نمی‌کند. با این حال، کنترل‌کننده Job به محض آشکار شدن خاتمه، یک Pod جایگزین ایجاد می‌کند. پس از آنکه Pod خاتمه یافت، کنترل‌کننده Job مقادیر `.backoffLimit` و `.podFailurePolicy` را برای Job مربوطه ارزیابی می‌کند و این Pod خاتمه‌یافته را نیز در نظر می‌گیرد.

اگر هر یک از این الزامات برقرار نباشد، کنترل‌کننده Job یک Pod در حال خاتمه را بلافاصله شکست محسوب می‌کند، حتی اگر آن Pod بعداً با `phase: "Succeeded"` خاتمه یابد.

### سیاست شکست backoff در Pod {#pod-backoff-failure-policy}

شرایطی وجود دارد که می‌خواهید پس از تعدادی تلاش مجدد، به دلیل یک خطای منطقی در پیکربندی و مانند آن، یک Job را ناموفق اعلام کنید.
برای این کار، مقدار `.spec.backoffLimit` را تنظیم کنید تا تعداد تلاش‌های مجدد پیش از ناموفق در نظر گرفتن Job مشخص شود.

مقدار پیش‌فرض `.spec.backoffLimit` برابر 6 است، مگر آنکه
[محدودیت backoff به‌ازای هر ایندکس](#backoff-limit-per-index) (فقط برای Job از نوع Indexed) مشخص شده باشد.
هنگامی که `.spec.backoffLimitPerIndex` مشخص شود، مقدار پیش‌فرض `.spec.backoffLimit`
برابر 2147483647 (MaxInt32) خواهد بود.

Podهای ناموفق مرتبط با Job توسط کنترل‌کننده Job با تأخیر backoff نمایی (10 ثانیه، 20 ثانیه، 40 ثانیه و ...) که حداکثر به ده دقیقه محدود می‌شود، دوباره ایجاد می‌شوند.

تعداد تلاش‌های مجدد به دو شیوه محاسبه می‌شود:

- تعداد Podهایی که `.status.phase = "Failed"` دارند.
- هنگام استفاده از `restartPolicy = "OnFailure"`، تعداد تلاش‌های مجدد در همه کانتینرهای Podهایی که `.status.phase` آن‌ها برابر `Pending` یا `Running` است.

اگر هر یک از این دو محاسبه به `.spec.backoffLimit` برسد، Job ناموفق در نظر گرفته می‌شود.

{{< note >}}
اگر Job شما `restartPolicy = "OnFailure"` دارد، به یاد داشته باشید که Pod اجراکننده Job پس از رسیدن به محدودیت backoff خاتمه داده می‌شود. این موضوع می‌تواند اشکال‌زدایی فایل اجرایی Job را دشوارتر کند. پیشنهاد می‌کنیم هنگام اشکال‌زدایی Job، مقدار `restartPolicy = "Never"` را تنظیم کنید یا از یک سامانه ثبت لاگ استفاده کنید تا اطمینان یابید خروجی Jobهای ناموفق به‌طور ناخواسته از دست نمی‌رود.
{{< /note >}}

### محدودیت backoff به‌ازای هر ایندکس {#backoff-limit-per-index}

{{< feature-state feature_gate_name="JobBackoffLimitPerIndex" >}}

هنگامی که یک Job از نوع [indexed](#completion-mode) را اجرا می‌کنید، می‌توانید تلاش‌های مجدد ناشی از شکست Pod را برای هر ایندکس به‌صورت مستقل مدیریت کنید. برای این کار، مقدار `.spec.backoffLimitPerIndex` را تنظیم کنید تا حداکثر تعداد شکست‌های Pod به‌ازای هر ایندکس مشخص شود.

هنگامی که محدودیت backoff به‌ازای هر ایندکس برای یک ایندکس فراتر رود، کوبرنتیز آن ایندکس را ناموفق در نظر می‌گیرد و آن را به فیلد `.status.failedIndexes` اضافه می‌کند. ایندکس‌های موفق، یعنی ایندکس‌هایی که Podهای آن‌ها با موفقیت اجرا شده‌اند، صرف‌نظر از اینکه فیلد `backoffLimitPerIndex` را تنظیم کرده باشید یا نه، در فیلد `.status.completedIndexes` ثبت می‌شوند.

توجه داشته باشید که ناموفق بودن یک ایندکس، اجرای ایندکس‌های دیگر را متوقف نمی‌کند.
هنگامی که اجرای همه ایندکس‌ها برای Jobی که در آن محدودیت backoff به‌ازای هر ایندکس را مشخص کرده‌اید به پایان برسد، اگر دست‌کم یکی از آن ایندکس‌ها ناموفق بوده باشد، کنترل‌کننده Job با تنظیم شرط Failed در status، کل Job را ناموفق علامت‌گذاری می‌کند. Job حتی در صورتی که برخی از ایندکس‌ها، و بالقوه تقریباً همه آن‌ها، با موفقیت پردازش شده باشند نیز ناموفق علامت‌گذاری می‌شود.

علاوه بر این، می‌توانید با تنظیم فیلد `.spec.maxFailedIndexes` حداکثر تعداد ایندکس‌هایی را که ناموفق علامت‌گذاری می‌شوند محدود کنید.
هنگامی که تعداد ایندکس‌های ناموفق از مقدار فیلد `maxFailedIndexes` فراتر رود، کنترل‌کننده Job خاتمه همه Podهای در حال اجرای باقی‌مانده آن Job را آغاز می‌کند.
پس از آنکه همه Podها خاتمه یافتند، کنترل‌کننده Job با تنظیم شرط Failed در status مربوط به Job، کل Job را ناموفق علامت‌گذاری می‌کند.

در اینجا یک مانیفست نمونه برای Jobی که `backoffLimitPerIndex` را تعریف می‌کند آمده است:

{{< code_sample file="/controllers/job-backoff-limit-per-index-example.yaml" >}}

در مثال بالا، کنترل‌کننده Job برای هر یک از ایندکس‌ها یک بار راه‌اندازی مجدد را مجاز می‌داند. هنگامی که تعداد کل ایندکس‌های ناموفق از 5 فراتر رود، کل Job خاتمه می‌یابد.

پس از پایان Job، status آن به شکل زیر خواهد بود:

```sh
kubectl get -o yaml job job-backoff-limit-per-index-example
```

```yaml
  status:
    completedIndexes: 1,3,5,7,9
    failedIndexes: 0,2,4,6,8
    succeeded: 5          # 1 succeeded pod for each of 5 succeeded indexes
    failed: 10            # 2 failed pods (1 retry) for each of 5 failed indexes
    conditions:
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: FailureTarget
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: Failed
```

کنترل‌کننده Job شرط `FailureTarget` را به Job اضافه می‌کند تا [خاتمه و پاک‌سازی Job](#job-termination-and-cleanup) آغاز شود. هنگامی که همه Podهای Job خاتمه یافتند، کنترل‌کننده Job شرط `Failed` را با همان مقادیر `reason` و `message` شرط `FailureTarget` اضافه می‌کند. برای جزئیات بیشتر به [خاتمه Podهای Job](#termination-of-job-pods) مراجعه کنید.

علاوه بر این، ممکن است بخواهید backoff به‌ازای هر ایندکس را همراه با [سیاست شکست Pod](#pod-failure-policy) به کار ببرید. هنگام استفاده از backoff به‌ازای هر ایندکس، اکشن جدیدی به نام `FailIndex` در دسترس است که به شما امکان می‌دهد از تلاش‌های مجدد غیرضروری درون یک ایندکس جلوگیری کنید.

### سیاست شکست Pod {#pod-failure-policy}

{{< feature-state feature_gate_name="JobPodFailurePolicy" >}}

سیاست شکست Pod که با فیلد `.spec.podFailurePolicy` تعریف می‌شود، کلاستر شما را قادر می‌سازد شکست‌های Pod را بر اساس کدهای خروج کانتینر و شرایط (conditions) Pod مدیریت کند.

در برخی موقعیت‌ها ممکن است بخواهید هنگام مدیریت شکست‌های Pod کنترل بهتری نسبت به کنترل ارائه‌شده توسط [سیاست شکست backoff در Pod](#pod-backoff-failure-policy) داشته باشید، که بر پایه `.spec.backoffLimit` در Job است. در ادامه چند نمونه از موارد استفاده آمده است:

* برای بهینه‌سازی هزینه‌های اجرای بارهای کاری با اجتناب از راه‌اندازی مجدد غیرضروری Podها، می‌توانید به محض آنکه یکی از Podهای Job با کد خروجی که نشان‌دهنده یک باگ نرم‌افزاری است شکست بخورد، Job را خاتمه دهید.
* برای تضمین اینکه Job حتی در صورت وجود اختلال‌ها (disruptions) به پایان می‌رسد، می‌توانید شکست‌های Pod ناشی از اختلال‌ها (مانند {{< glossary_tooltip text="preemption" term_id="preemption" >}}، {{< glossary_tooltip text="API-initiated eviction" term_id="api-eviction" >}} یا شروع تخلیه مبتنی بر {{< glossary_tooltip text="taint" term_id="taint" >}}) را نادیده بگیرید تا این شکست‌ها در محدودیت `.spec.backoffLimit` برای تلاش‌های مجدد شمارش نشوند.

می‌توانید برای پاسخ به موارد استفاده بالا، یک سیاست شکست Pod را در فیلد `.spec.podFailurePolicy` پیکربندی کنید. این سیاست می‌تواند شکست‌های Pod را بر اساس کدهای خروج کانتینر و شرایط Pod مدیریت کند.

در اینجا یک مانیفست برای Jobی که `podFailurePolicy` را تعریف می‌کند آمده است:

{{% code_sample file="/controllers/job-pod-failure-policy-example.yaml" %}}

در مثال بالا، نخستین قاعده سیاست شکست Pod مشخص می‌کند که اگر کانتینر `main` با کد خروج 42 شکست بخورد، Job باید ناموفق علامت‌گذاری شود. قواعد زیر به‌طور خاص برای کانتینر `main` هستند:

- کد خروج 0 به این معناست که کانتینر موفق بوده است
- کد خروج 42 به این معناست که **کل Job** ناموفق بوده است
- هر کد خروج دیگری نشان می‌دهد که کانتینر و در نتیجه کل Pod ناموفق بوده است. اگر تعداد کل راه‌اندازی‌های مجدد کمتر از `backoffLimit` باشد، Pod دوباره ایجاد می‌شود. اگر به `backoffLimit` برسیم، **کل Job** ناموفق است.

{{< note >}}
از آنجا که قالب Pod مقدار `restartPolicy: Never` را مشخص کرده است،
kubelet کانتینر `main` را در آن Pod خاص دوباره راه‌اندازی نمی‌کند.
{{< /note >}}

قاعده دوم سیاست شکست Pod، که اکشن `Ignore` را برای Podهای ناموفق دارای شرط `DisruptionTarget` مشخص می‌کند، باعث می‌شود اختلال‌های Pod در محدودیت `.spec.backoffLimit` برای تلاش‌های مجدد شمارش نشوند.

{{< note >}}
اگر Job به‌دلیل سیاست شکست Pod یا سیاست شکست backoff در Pod ناموفق شود و Job چندین Pod را اجرا کند، کوبرنتیز همه Podهای آن Job را که هنوز در وضعیت Pending یا Running هستند خاتمه می‌دهد.
{{< /note >}}

در ادامه برخی الزامات و معناشناسی این API آمده است:

- اگر می‌خواهید از فیلد `.spec.podFailurePolicy` برای یک Job استفاده کنید، باید قالب Pod آن Job را نیز با `.spec.restartPolicy` برابر `Never` تعریف کنید.
- قواعد سیاست شکست Pod که در `spec.podFailurePolicy.rules` مشخص می‌کنید به ترتیب ارزیابی می‌شوند. هنگامی که یک قاعده با شکست Pod مطابقت پیدا کند، قواعد باقی‌مانده نادیده گرفته می‌شوند. اگر هیچ قاعده‌ای با شکست Pod مطابقت نداشته باشد، مدیریت پیش‌فرض اعمال می‌شود.
- ممکن است بخواهید یک قاعده را با مشخص کردن نام کانتینر در `spec.podFailurePolicy.rules[*].onExitCodes.containerName` به یک کانتینر خاص محدود کنید. اگر مشخص نشود، قاعده برای همه کانتینرها اعمال می‌شود. اگر مشخص شود، باید با یکی از نام‌های کانتینر یا `initContainer` در قالب Pod مطابقت داشته باشد.
- می‌توانید اکشنی را که هنگام تطابق با سیاست شکست Pod انجام می‌شود با `spec.podFailurePolicy.rules[*].action` مشخص کنید. مقادیر ممکن عبارت‌اند از:
  - `FailJob`: برای نشان دادن اینکه Job مربوط به Pod باید ناموفق (Failed) علامت‌گذاری شود و همه Podهای در حال اجرا باید خاتمه یابند.
  - `Ignore`: برای نشان دادن اینکه شمارنده مربوط به `.spec.backoffLimit` نباید افزایش یابد و یک Pod جایگزین باید ایجاد شود.
  - `Count`: برای نشان دادن اینکه Pod باید به شیوه پیش‌فرض مدیریت شود. شمارنده مربوط به `.spec.backoffLimit` باید افزایش یابد.
  - `FailIndex`: از این اکشن همراه با [محدودیت backoff به‌ازای هر ایندکس](#backoff-limit-per-index) استفاده کنید تا از تلاش‌های مجدد غیرضروری در ایندکس یک Pod ناموفق جلوگیری شود.

{{< note >}}
هنگامی که از `podFailurePolicy` استفاده می‌کنید، کنترل‌کننده Job فقط Podهای در فاز `Failed` را مطابقت می‌دهد. Podهایی که دارای زمان حذف (deletion timestamp) هستند و در فاز پایانی (`Failed` یا `Succeeded`) نیستند، همچنان در حال خاتمه در نظر گرفته می‌شوند. این بدان معناست که Podهای در حال خاتمه تا رسیدن به فاز پایانی یک [finalizer ردیابی](#job-tracking-with-finalizers) را حفظ می‌کنند.
از کوبرنتیز 1.27 به بعد، Kubelet Podهای حذف‌شده را به فاز پایانی منتقل می‌کند
(ر.ک. [فاز Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)). این امر تضمین می‌کند که finalizerهای Podهای حذف‌شده توسط کنترل‌کننده Job برداشته شوند.
{{< /note >}}

{{< note >}}
از کوبرنتیز v1.28 به بعد، هنگامی که سیاست شکست Pod استفاده می‌شود، کنترل‌کننده Job Podهای در حال خاتمه را تنها پس از رسیدن آن‌ها به فاز پایانی `Failed` دوباره ایجاد می‌کند. این رفتار مشابه `podReplacementPolicy: Failed` است. برای اطلاعات بیشتر به [سیاست جایگزینی Pod](#pod-replacement-policy) مراجعه کنید.
{{< /note >}}

هنگامی که از `podFailurePolicy` استفاده می‌کنید و Job به دلیل مطابقت Pod با قاعده‌ای که اکشن `FailJob` دارد ناموفق می‌شود، کنترل‌کننده Job با افزودن شرط `FailureTarget` فرایند خاتمه Job را آغاز می‌کند.
برای جزئیات بیشتر به [خاتمه و پاک‌سازی Job](#job-termination-and-cleanup) مراجعه کنید.

## سیاست موفقیت {#success-policy}

هنگام ایجاد یک Job از نوع Indexed، می‌توانید با استفاده از `.spec.successPolicy` و بر اساس Podهای موفق، مشخص کنید که چه زمانی یک Job موفق اعلام شود.

به‌طور پیش‌فرض، یک Job زمانی موفق می‌شود که تعداد Podهای موفق برابر `.spec.completions` باشد.
در ادامه چند موقعیت آمده است که ممکن است در آن‌ها بخواهید کنترل بیشتری برای اعلام موفقیت Job داشته باشید:

* هنگام اجرای شبیه‌سازی‌ها با پارامترهای مختلف، ممکن است برای موفقیت کلی Job نیازی نباشد که همه شبیه‌سازی‌ها موفق شوند.
* هنگام پیروی از الگوی leader-worker، تنها موفقیت leader تعیین می‌کند که Job موفق شده است یا ناموفق. نمونه‌هایی از این حالت، فریم‌ورک‌هایی مانند MPI و PyTorch و مانند آن‌ها هستند.

می‌توانید برای پاسخ به موارد استفاده بالا، یک سیاست موفقیت را در فیلد `.spec.successPolicy` پیکربندی کنید. این سیاست می‌تواند موفقیت Job را بر اساس Podهای موفق مدیریت کند. پس از آنکه Job سیاست موفقیت را برآورده کرد، کنترل‌کننده Job Podهای باقی‌مانده را خاتمه می‌دهد.
سیاست موفقیت با قواعد تعریف می‌شود. هر قاعده می‌تواند یکی از اشکال زیر را داشته باشد:

* هنگامی که فقط `succeededIndexes` را مشخص می‌کنید، به محض آنکه همه ایندکس‌های مشخص‌شده در `succeededIndexes` موفق شوند، کنترل‌کننده Job آن Job را موفق علامت‌گذاری می‌کند. `succeededIndexes` باید فهرستی از بازه‌ها بین 0 و `.spec.completions-1` باشد.
* هنگامی که فقط `succeededCount` را مشخص می‌کنید، به محض آنکه تعداد ایندکس‌های موفق به `succeededCount` برسد، کنترل‌کننده Job آن Job را موفق علامت‌گذاری می‌کند.
* هنگامی که هم `succeededIndexes` و هم `succeededCount` را مشخص می‌کنید، به محض آنکه تعداد ایندکس‌های موفق از زیرمجموعه ایندکس‌های مشخص‌شده در `succeededIndexes` به `succeededCount` برسد، کنترل‌کننده Job آن Job را موفق علامت‌گذاری می‌کند.

توجه داشته باشید که هنگامی که چندین قاعده را در `.spec.successPolicy.rules` مشخص می‌کنید، کنترل‌کننده Job قواعد را به ترتیب ارزیابی می‌کند. به محض آنکه Job یک قاعده را برآورده کند، کنترل‌کننده Job قواعد باقی‌مانده را نادیده می‌گیرد.

در اینجا یک مانیفست برای Job دارای `successPolicy` آمده است:

{{% code_sample file="/controllers/job-success-policy.yaml" %}}

در مثال بالا، هر دو مقدار `succeededIndexes` و `succeededCount` مشخص شده‌اند.
بنابراین، کنترل‌کننده Job زمانی که هر یک از ایندکس‌های مشخص‌شده، یعنی 0، 2 یا 3، موفق شود، Job را موفق علامت‌گذاری می‌کند و Podهای باقی‌مانده را خاتمه می‌دهد.
Jobی که سیاست موفقیت را برآورده می‌کند، شرط `SuccessCriteriaMet` را با دلیل (reason) برابر `SuccessPolicy` دریافت می‌کند.
پس از صدور دستور حذف Podهای باقی‌مانده، Job شرط `Complete` را دریافت می‌کند.

توجه داشته باشید که `succeededIndexes` به‌صورت بازه‌هایی که با خط تیره از هم جدا شده‌اند نمایش داده می‌شود.
اعداد با نخستین و واپسین عنصر دنباله نمایش داده می‌شوند که با خط تیره از هم جدا شده‌اند.

{{< note >}}
هنگامی که هم سیاست موفقیت و هم برخی سیاست‌های خاتمه‌دهنده مانند `.spec.backoffLimit` و `.spec.podFailurePolicy` را مشخص می‌کنید، به محض آنکه Job یکی از این سیاست‌ها را برآورده کند، کنترل‌کننده Job سیاست خاتمه را رعایت می‌کند و سیاست موفقیت را نادیده می‌گیرد.
{{< /note >}}

## خاتمه و پاک‌سازی Job

هنگامی که یک Job کامل می‌شود، Podهای جدیدی ایجاد نمی‌شوند، اما Podها [معمولاً](#pod-backoff-failure-policy) حذف هم نمی‌شوند.
نگه‌داشتن آن‌ها به شما امکان می‌دهد همچنان لاگ‌های Podهای تکمیل‌شده را برای بررسی خطاها، هشدارها یا سایر خروجی‌های تشخیصی مشاهده کنید.
آبجکت Job نیز پس از تکمیل باقی می‌ماند تا بتوانید وضعیت آن را مشاهده کنید. حذف Jobهای قدیمی پس از ثبت وضعیت آن‌ها بر عهده کاربر است. Job را با `kubectl` حذف کنید (برای مثال `kubectl delete jobs/pi` یا `kubectl delete -f ./job.yaml`).
هنگامی که Job را با `kubectl` حذف می‌کنید، تمام Podهایی که ایجاد کرده است نیز حذف می‌شوند.

به‌طور پیش‌فرض، یک Job بدون وقفه اجرا می‌شود، مگر اینکه یک Pod با شکست مواجه شود (`restartPolicy=Never`)
یا یک کانتینر با خطا خارج شود (`restartPolicy=OnFailure`)؛ در این نقطه Job به
`.spec.backoffLimit` که در بالا توضیح داده شد رجوع می‌کند. پس از رسیدن به `.spec.backoffLimit`، Job
به‌عنوان ناموفق علامت‌گذاری می‌شود و تمام Podهای در حال اجرا خاتمه می‌یابند.

راه دیگر برای خاتمه‌دادن به یک Job، تعیین یک مهلت فعال (active deadline) است.
برای این کار، فیلد `.spec.activeDeadlineSeconds` در Job را روی تعدادی ثانیه تنظیم کنید.
مقدار `activeDeadlineSeconds` بر مدت زمان اجرای Job اعمال می‌شود، صرف‌نظر از اینکه چند Pod ایجاد شده باشد.
هنگامی که Job به `activeDeadlineSeconds` برسد، تمام Podهای در حال اجرای آن خاتمه می‌یابند و وضعیت Job
به `type: Failed` با `reason: DeadlineExceeded` تبدیل می‌شود.

توجه کنید که `.spec.activeDeadlineSeconds` در یک Job بر `.spec.backoffLimit` آن اولویت دارد.
بنابراین، Jobی که در حال تلاش مجدد برای یک یا چند Pod ناموفق است، پس از رسیدن به محدودیت زمانی تعیین‌شده توسط `activeDeadlineSeconds`، هیچ Pod اضافه‌ای را مستقر نمی‌کند، حتی اگر `backoffLimit` هنوز به حد خود نرسیده باشد.

مثال:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi-with-timeout
spec:
  backoffLimit: 5
  activeDeadlineSeconds: 100
  template:
    spec:
      containers:
      - name: pi
        image: perl:5.34.0
        command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
```

توجه کنید که هم spec مربوط به Job و هم [spec قالب Pod](/docs/concepts/workloads/pods/init-containers/#detailed-behavior)
درون Job دارای فیلد `activeDeadlineSeconds` هستند. مطمئن شوید که این فیلد را در سطح مناسب تنظیم می‌کنید.

به یاد داشته باشید که `restartPolicy` بر Pod اعمال می‌شود و نه بر خود Job:
هنگامی که وضعیت Job برابر `type: Failed` شود، راه‌اندازی مجدد خودکار Job وجود ندارد.
به عبارت دیگر، سازوکارهای خاتمه‌دادن به Job که با `.spec.activeDeadlineSeconds`
و `.spec.backoffLimit` فعال می‌شوند، به شکست دائمی Job منجر می‌شوند که برای رفع آن مداخله دستی لازم است.

### شرایط پایانی Job {#terminal-job-conditions}

یک Job دو حالت پایانی ممکن دارد که هر کدام شرط (condition) متناظری در Job دارند:
* موفق: شرط Job با نام `Complete`
* ناموفق: شرط Job با نام `Failed`

Jobها به دلایل زیر ناموفق می‌شوند:
- تعداد شکست‌های Pod از `.spec.backoffLimit` تعیین‌شده در مشخصات Job فراتر رفته است.
  برای جزئیات، [سیاست backoff شکست Pod](#pod-backoff-failure-policy) را ببینید.
- زمان اجرای Job از `.spec.activeDeadlineSeconds` تعیین‌شده فراتر رفته است.
- یک Job اندیس‌دار (indexed) که از `.spec.backoffLimitPerIndex` استفاده کرده است، اندیس‌های ناموفق دارد.
  برای جزئیات، [محدودیت backoff به ازای هر اندیس](#backoff-limit-per-index) را ببینید.
- تعداد اندیس‌های ناموفق در Job از `spec.maxFailedIndexes` تعیین‌شده فراتر رفته است.
  برای جزئیات، [محدودیت backoff به ازای هر اندیس](#backoff-limit-per-index) را ببینید.
- یک Pod ناموفق با یکی از قواعد `.spec.podFailurePolicy` که دارای اقدام `FailJob` است مطابقت دارد.
  برای جزئیات اینکه قواعد سیاست شکست Pod چگونه ممکن است بر ارزیابی شکست تأثیر بگذارند، [سیاست شکست Pod](#pod-failure-policy) را ببینید.

Jobها به دلایل زیر موفق می‌شوند:
- تعداد Podهای موفق به `.spec.completions` تعیین‌شده رسیده است.
- معیارهای تعیین‌شده در `.spec.successPolicy` برآورده شده‌اند. برای جزئیات،
  [سیاست موفقیت](#success-policy) را ببینید.

در کوبرنتیز نسخه v1.31 و بالاتر، کنترل‌کننده Job افزودن شرایط پایانی `Failed` یا `Complete` را
تا زمانی که تمام Podهای Job خاتمه یابند به تأخیر می‌اندازد.

در کوبرنتیز نسخه v1.30 و پایین‌تر، کنترل‌کننده Job شرایط پایانی `Complete` یا
`Failed` را به محض آغاز فرایند خاتمه Job و حذف تمام finalizerهای Pod اضافه می‌کرد. با این حال، برخی Podها
در لحظه افزوده‌شدن شرط پایانی همچنان در حال اجرا یا در حال خاتمه بودند.

در کوبرنتیز نسخه v1.31 و بالاتر، کنترل‌کننده شرایط پایانی Job را فقط
_پس از_ خاتمه یافتن تمام Podها اضافه می‌کند. می‌توانید این رفتار را با استفاده از
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)های
`JobManagedBy` و `JobPodReplacementPolicy` (که هر دو به‌طور پیش‌فرض فعال هستند) کنترل کنید.

### خاتمه Podهای Job

کنترل‌کننده Job پس از اینکه Job معیارهای موفقیت یا شکست را برآورده کرد، شرط `FailureTarget` یا شرط `SuccessCriteriaMet`
را به Job اضافه می‌کند تا خاتمه Podها را آغاز کند.

عواملی مانند `terminationGracePeriodSeconds` ممکن است مدت زمان بین لحظه‌ای که کنترل‌کننده Job
شرط `FailureTarget` یا شرط `SuccessCriteriaMet` را اضافه می‌کند تا لحظه‌ای که تمام Podهای Job خاتمه می‌یابند
و کنترل‌کننده Job یک [شرط پایانی](#terminal-job-conditions)
(`Failed` یا `Complete`) اضافه می‌کند، افزایش دهند.

می‌توانید از شرط `FailureTarget` یا `SuccessCriteriaMet` استفاده کنید تا بدون نیاز به انتظار برای
افزوده‌شدن شرط پایانی توسط کنترل‌کننده، ارزیابی کنید که Job ناموفق بوده یا موفق شده است.

برای مثال، ممکن است بخواهید تصمیم بگیرید که چه زمانی یک Job جایگزین ایجاد شود که جایگزین Job ناموفق می‌شود. اگر Job ناموفق را هنگام ظاهرشدن شرط `FailureTarget` جایگزین کنید، Job جایگزین شما زودتر اجرا می‌شود، اما ممکن است باعث شود Podهای Job ناموفق و Job جایگزین هم‌زمان اجرا شوند و از منابع محاسباتی اضافی استفاده کنند.

در عوض، اگر کلاستر شما ظرفیت منابع محدودی دارد، می‌توانید منتظر بمانید تا شرط `Failed` روی Job ظاهر شود؛ این کار Job جایگزین شما را به تأخیر می‌اندازد، اما با انتظار تا حذف تمام Podهای ناموفق، اطمینان می‌دهد که در منابع صرفه‌جویی می‌کنید.

## پاک‌سازی خودکار Jobهای پایان‌یافته

Jobهای پایان‌یافته معمولاً دیگر در سیستم مورد نیاز نیستند. نگه‌داشتن آن‌ها در
سیستم به API server فشار وارد می‌کند. اگر Jobها مستقیماً توسط یک کنترل‌کننده سطح بالاتر مانند
[CronJobs](/docs/concepts/workloads/controllers/cron-jobs/) مدیریت شوند، Jobها می‌توانند
توسط CronJobها بر اساس سیاست پاک‌سازی مبتنی بر ظرفیت تعیین‌شده پاک‌سازی شوند.

### سازوکار TTL برای Jobهای پایان‌یافته

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

راه دیگر برای پاک‌سازی خودکار Jobهای پایان‌یافته (چه `Complete` و چه `Failed`)،
استفاده از سازوکار TTL است که توسط
[کنترل‌کننده TTL](/docs/concepts/workloads/controllers/ttlafterfinished/) برای
منابع پایان‌یافته فراهم شده است و با تعیین فیلد `.spec.ttlSecondsAfterFinished` در
Job به کار می‌رود.

هنگامی که کنترل‌کننده TTL، Job را پاک‌سازی می‌کند، آن را به‌صورت آبشاری حذف می‌کند؛
یعنی آبجکت‌های وابسته، مانند Podها، را همراه با Job حذف می‌کند. توجه کنید
که هنگام حذف Job، تضمین‌های چرخه عمر آن، مانند finalizerها،
رعایت خواهند شد.

برای مثال:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi-with-ttl
spec:
  ttlSecondsAfterFinished: 100
  template:
    spec:
      containers:
      - name: pi
        image: perl:5.34.0
        command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
```

Job با نام `pi-with-ttl` پس از گذشت `100`
ثانیه از پایان کار، واجد شرایط حذف خودکار خواهد بود.

اگر مقدار این فیلد `0` باشد، Job بلافاصله پس از پایان کار واجد شرایط حذف خودکار خواهد بود. اگر فیلد تنظیم نشده باشد، این Job پس از پایان کار توسط کنترل‌کننده TTL پاک‌سازی نخواهد شد.

{{< note >}}
توصیه می‌شود فیلد `ttlSecondsAfterFinished` تنظیم شود، زیرا Jobهای مدیریت‌نشده
(Jobهایی که مستقیماً ایجاد کرده‌اید و نه به‌طور غیرمستقیم از طریق سایر APIهای بار کاری
مانند CronJob) سیاست حذف پیش‌فرض
`orphanDependents` دارند که باعث می‌شود Podهای ایجادشده توسط یک Job مدیریت‌نشده
پس از حذف کامل آن Job باقی بمانند.
اگرچه {{< glossary_tooltip text="control plane" term_id="control-plane" >}} در نهایت
Podهای یک Job حذف‌شده را پس از ناموفق‌شدن یا تکمیل‌شدن،
[پاک‌سازی (garbage collection)](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)
می‌کند، گاهی این Podهای باقی‌مانده ممکن است باعث کاهش کارایی کلاستر شوند یا در بدترین حالت
موجب از دسترس خارج‌شدن کلاستر در اثر این کاهش کارایی گردند.

می‌توانید از [LimitRanges](/docs/concepts/policy/limit-range/) و
[ResourceQuotas](/docs/concepts/policy/resource-quotas/) برای اعمال
سقف بر میزان منابعی که یک فضای نام (namespace) مشخص
می‌تواند مصرف کند، استفاده کنید.
{{< /note >}}

## الگوهای Job

آبجکت Job را می‌توان برای پردازش مجموعه‌ای از *آیتم‌های کاری* مستقل اما مرتبط به کار برد.
این آیتم‌ها می‌توانند ایمیل‌هایی برای ارسال، فریم‌هایی برای رندر، فایل‌هایی برای تبدیل کدگذاری (transcode)،
بازه‌هایی از کلیدها در یک پایگاه داده NoSQL برای اسکن و موارد مشابه باشند.

در یک سیستم پیچیده ممکن است چندین مجموعه متفاوت از آیتم‌های کاری وجود داشته باشد. در اینجا فقط
یک مجموعه از آیتم‌های کاری را در نظر می‌گیریم که کاربر می‌خواهد آن‌ها را با هم مدیریت کند &mdash; یک *batch job*.

الگوهای متفاوتی برای محاسبات موازی وجود دارد که هر کدام نقاط قوت و ضعفی دارند.
بدهبستان‌ها عبارت‌اند از:

- یک آبجکت Job برای هر آیتم کاری، در مقابل یک آبجکت Job واحد برای همه آیتم‌های کاری.
  یک Job به ازای هر آیتم کاری، سربار (overhead) مدیریت تعداد زیادی آبجکت Job را
  برای کاربر و سیستم ایجاد می‌کند.
  یک Job واحد برای همه آیتم‌ها برای تعداد زیاد آیتم‌ها بهتر است.
- تعداد Podهای ایجادشده برابر با تعداد آیتم‌های کاری است، در مقابل اینکه هر Pod بتواند چندین آیتم کاری را پردازش کند.
  هنگامی که تعداد Podها برابر با تعداد آیتم‌های کاری است، Podها معمولاً
  به تغییرات کمتری در کد و کانتینرهای موجود نیاز دارند. پردازش چندین آیتم کاری توسط هر Pod
  برای تعداد زیاد آیتم‌ها بهتر است.
- چند رویکرد از یک صف کار (work queue) استفاده می‌کنند. این رویکرد نیازمند اجرای یک سرویس صف
  و اعمال تغییراتی در برنامه یا کانتینر موجود است تا از صف کار استفاده کند.
  رویکردهای دیگر راحت‌تر با یک برنامه کانتینری‌شده موجود سازگار می‌شوند.
- هنگامی که Job با یک
  [headless Service](/docs/concepts/services-networking/service/#headless-services)
  مرتبط باشد، می‌توانید به Podهای درون یک Job امکان دهید برای همکاری در یک محاسبه
  با یکدیگر ارتباط برقرار کنند.

بدهبستان‌ها در اینجا خلاصه شده‌اند و ستون‌های ۲ تا ۴ با بدهبستان‌های بالا متناظرند.
نام الگوها نیز پیوند به مثال‌ها و توضیحات دقیق‌تر است.

|                  الگو                        | آبجکت Job واحد | Pod کمتر از آیتم‌های کاری؟ | استفاده از برنامه بدون تغییر؟ |
| ----------------------------------------------- |:-----------------:|:---------------------------:|:-------------------:|
| [Queue with Pod Per Work Item]                  |         ✓         |                             |      گاهی      |
| [Queue with Variable Pod Count]                 |         ✓         |             ✓               |                     |
| [Indexed Job with Static Work Assignment]       |         ✓         |                             |          ✓          |
| [Job with Pod-to-Pod Communication]             |         ✓         |         گاهی           |      گاهی      |
| [Job Template Expansion]                        |                   |                             |          ✓          |

هنگامی که تعداد تکمیل‌ها را با `.spec.completions` مشخص می‌کنید، هر Pod ایجادشده توسط کنترل‌کننده Job
دارای [`spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) یکسانی است.
این بدان معناست که تمام Podهای یک وظیفه، خط فرمان یکسان، ایمیج یکسان،
حجم‌های (volumes) یکسان و (تقریباً) متغیرهای محیطی یکسانی خواهند داشت. این الگوها
روش‌های مختلفی برای ترتیب‌دادن به کار Podها روی چیزهای متفاوت هستند.

این جدول تنظیمات لازم برای `.spec.parallelism` و `.spec.completions` را برای هر یک از الگوها نشان می‌دهد.
در اینجا `W` تعداد آیتم‌های کاری است.

|             الگو                             | `.spec.completions` |  `.spec.parallelism` |
| ----------------------------------------------- |:-------------------:|:--------------------:|
| [Queue with Pod Per Work Item]                  |          W          |        هر مقدار           |
| [Queue with Variable Pod Count]                 |         null        |        هر مقدار           |
| [Indexed Job with Static Work Assignment]       |          W          |        هر مقدار           |
| [Job with Pod-to-Pod Communication]             |          W          |         W            |
| [Job Template Expansion]                        |          1          |     باید 1 باشد      |

## استفاده پیشرفته

### تعلیق یک Job {#suspending-a-job}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

هنگامی که یک Job ایجاد می‌شود، کنترل‌کننده Job بلافاصله شروع به ایجاد Podها
برای برآورده‌کردن نیازمندی‌های Job می‌کند و تا زمانی که Job
کامل نشود به این کار ادامه می‌دهد. با این حال، ممکن است بخواهید اجرای یک Job را موقتاً به حالت تعلیق درآورید و
بعداً از سر بگیرید، یا Jobها را در حالت تعلیق آغاز کنید و بگذارید یک کنترل‌کننده سفارشی
بعداً تصمیم بگیرد که چه زمانی آن‌ها را شروع کند.

برای تعلیق یک Job، می‌توانید فیلد `.spec.suspend` در
Job را به true به‌روزرسانی کنید؛ سپس، هنگامی که می‌خواهید دوباره آن را از سر بگیرید، آن را به false به‌روزرسانی کنید.
ایجاد یک Job با `.spec.suspend` برابر true، آن را در حالت تعلیق
ایجاد می‌کند.

در کوبرنتیز نسخه 1.35 یا بالاتر، هنگامی که feature gate با نام
[MutableSchedulingDirectivesForSuspendedJobs](#mutable-scheduling-directives-for-suspended-jobs)
فعال باشد، فیلد `.status.startTime` هنگام تعلیق Job پاک می‌شود.

هنگامی که یک Job از تعلیق خارج و از سر گرفته می‌شود، فیلد `.status.startTime` آن
روی زمان فعلی بازنشانی می‌شود. این بدان معناست که زمان‌سنج `.spec.activeDeadlineSeconds`
هنگام تعلیق و از سرگیری Job متوقف و بازنشانی می‌شود.

هنگامی که یک Job را تعلیق می‌کنید، هر Pod در حال اجرا که وضعیت `Completed` ندارد
با سیگنال SIGTERM [خاتمه داده می‌شود](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).
دوره خاتمه ملایم (graceful termination) Pod رعایت می‌شود و
Pod شما باید این سیگنال را در این بازه مدیریت کند. این کار ممکن است شامل ذخیره
پیشرفت برای استفاده بعدی یا بازگرداندن تغییرات باشد. Podهایی که به این روش خاتمه داده می‌شوند
در شمارش `completions` مربوط به Job به حساب نمی‌آیند.

نمونه‌ای از تعریف Job در حالت تعلیق می‌تواند به این صورت باشد:

```shell
kubectl get job myjob -o yaml
```

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: myjob
spec:
  suspend: true
  parallelism: 1
  completions: 5
  template:
    spec:
      ...
```

همچنین می‌توانید با اعمال patch روی Job از طریق خط فرمان، وضعیت تعلیق Job را تغییر دهید.

تعلیق یک Job فعال:

```shell
kubectl patch job/myjob --type=strategic --patch '{"spec":{"suspend":true}}'
```

از سرگیری یک Job معلق:

```shell
kubectl patch job/myjob --type=strategic --patch '{"spec":{"suspend":false}}'
```

از وضعیت Job می‌توان برای تعیین اینکه آیا یک Job معلق است یا در گذشته
معلق شده است استفاده کرد:

```shell
kubectl get jobs/myjob -o yaml
```

```yaml
apiVersion: batch/v1
kind: Job
# .metadata and .spec omitted
status:
  conditions:
  - lastProbeTime: "2021-02-05T13:14:33Z"
    lastTransitionTime: "2021-02-05T13:14:33Z"
    status: "True"
    type: Suspended
  startTime: "2021-02-05T13:13:48Z"
```

شرط Job از نوع "Suspended" با وضعیت "True" به این معناست که Job
معلق است؛ از فیلد `lastTransitionTime` می‌توان برای تعیین مدت زمانی که
Job معلق بوده است استفاده کرد. اگر وضعیت آن شرط "False" باشد، Job
قبلاً معلق شده بوده و اکنون در حال اجراست. اگر چنین شرطی در وضعیت Job
وجود نداشته باشد، Job هرگز متوقف نشده است.

هنگام تعلیق و از سرگیری Job، رویدادهایی (Events) نیز ایجاد می‌شوند:

```shell
kubectl describe jobs/myjob
```

```
Name:           myjob
...
Events:
  Type    Reason            Age   From            Message
  ----    ------            ----  ----            -------
  Normal  SuccessfulCreate  12m   job-controller  Created pod: myjob-hlrpl
  Normal  SuccessfulDelete  11m   job-controller  Deleted pod: myjob-hlrpl
  Normal  Suspended         11m   job-controller  Job suspended
  Normal  SuccessfulCreate  3s    job-controller  Created pod: myjob-jvb44
  Normal  Resumed           3s    job-controller  Job resumed
```

چهار رویداد آخر، به‌ویژه رویدادهای "Suspended" و "Resumed"،
مستقیماً نتیجه تغییر فیلد `.spec.suspend` هستند. در بازه زمانی بین
این دو رویداد، می‌بینیم که هیچ Podی ایجاد نشده است، اما ایجاد Pod
به محض از سرگیری Job دوباره آغاز شد.

### دستورالعمل‌های زمان‌بندی قابل تغییر

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

در بیشتر موارد، یک Job موازی می‌خواهد Podها با محدودیت‌هایی اجرا شوند،
مانند اینکه همگی در یک zone باشند، یا همگی روی GPU مدل x یا y باشند اما ترکیبی از هر دو نباشند.

فیلد [suspend](#suspending-a-job) نخستین گام برای دستیابی به این معناشناسی است. Suspend به یک
کنترل‌کننده صف سفارشی اجازه می‌دهد تصمیم بگیرد که یک Job چه زمانی باید شروع شود؛ با این حال، پس از اینکه Job از تعلیق خارج شد،
کنترل‌کننده صف سفارشی هیچ تأثیری بر اینکه Podهای Job واقعاً کجا قرار می‌گیرند ندارد.

این قابلیت امکان به‌روزرسانی دستورالعمل‌های زمان‌بندی یک Job را پیش از شروع آن فراهم می‌کند، که به کنترل‌کننده‌های
صف سفارشی توانایی تأثیرگذاری بر جایگذاری Pod را می‌دهد و در عین حال
تخصیص واقعی Pod به نود را به kube-scheduler واگذار می‌کند.

فیلدهایی در قالب Pod یک Job که می‌توانند به‌روزرسانی شوند عبارت‌اند از node affinity، node selector،
tolerations، برچسب‌ها، حاشیه‌نویسی‌ها (annotations) و [scheduling gates](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/).

#### دستورالعمل‌های زمان‌بندی قابل تغییر برای Jobهای معلق {#mutable-scheduling-directives-for-suspended-jobs}

{{< feature-state feature_gate_name="MutableSchedulingDirectivesForSuspendedJobs" >}}

در کوبرنتیز 1.34 یا پایین‌تر، تغییر دستورالعمل‌های زمان‌بندی Pod فقط برای
Jobهای معلقی مجاز است که پیش‌تر هرگز از تعلیق خارج نشده‌اند. در کوبرنتیز 1.35، هنگامی که feature gate با نام `MutableSchedulingDirectivesForSuspendedJobs` فعال باشد، این کار
برای هر Job معلقی مجاز است.

علاوه بر این، این feature gate پاک‌شدن فیلد `.status.startTime` را هنگام [تعلیق Job](#suspending-a-job) فعال می‌کند.

### منابع قابل تغییر Pod برای Jobهای معلق‌شده

{{< feature-state feature_gate_name="MutablePodResourcesForSuspendedJobs" >}}

مدیر کلاستر می‌تواند در کوبرنتیز کنترل‌های پذیرش (admission controls) تعریف کند که بر اساس قواعد سیاستی، درخواست‌ها (requests) یا محدودیت‌های (limits) منابع یک Job را تغییر دهند.

با این قابلیت، کوبرنتیز همچنین به شما اجازه می‌دهد قالب Pod مربوط به یک [Job معلق‌شده](#suspending-a-job) را تغییر دهید تا نیازمندی‌های منابع Podهای آن Job تغییر کند.
این موضوع با _تغییر اندازه درجا (in-place) برای Pod_ متفاوت است؛ قابلیتی که به شما امکان می‌دهد منابع Podهایی را که هم‌اکنون در حال اجرا هستند، هر بار برای یک Pod به‌روزرسانی کنید.

کلاینتی که درخواست‌ها یا محدودیت‌های جدید منابع را تنظیم می‌کند می‌تواند با کلاینتی که در ابتدا Job را ایجاد کرده است متفاوت باشد و لازم نیست مدیر کلاستر باشد.

### مشخص کردن انتخابگر (selector) Pod به‌صورت دلخواه

به‌طور معمول، هنگام ایجاد یک آبجکت Job، مقدار `.spec.selector` را مشخص نمی‌کنید.
منطق مقداردهی پیش‌فرض سیستم، این فیلد را هنگام ایجاد Job اضافه می‌کند.
این منطق مقداری برای انتخابگر برمی‌گزیند که با هیچ Job دیگری هم‌پوشانی نداشته باشد.

با این حال، در برخی موارد ممکن است لازم باشد این انتخابگر را که به‌صورت خودکار تنظیم شده است، بازنویسی کنید.
برای این کار می‌توانید مقدار `.spec.selector` را در Job مشخص کنید.

در این کار بسیار دقت کنید. اگر انتخابگر برچسبی (label selector) تعیین کنید که برای Podهای آن Job منحصربه‌فرد نباشد و با Podهای نامرتبط تطبیق پیدا کند، ممکن است Podهای Job نامرتبط حذف شوند، یا این Job سایر Podها را به‌عنوان Podهای تکمیل‌کننده خود بشمارد، یا یکی از Jobها یا هر دوی آن‌ها از ایجاد Pod یا اجرا تا مرحله تکمیل خودداری کنند. اگر انتخابگر غیرمنحصربه‌فرد انتخاب شود، سایر کنترل‌کننده‌ها (مثلاً ReplicationController) و Podهای آن‌ها نیز ممکن است به شیوه‌ای غیرقابل‌پیش‌بینی رفتار کنند. کوبرنتیز هنگام مشخص کردن `.spec.selector` مانع اشتباه شما نمی‌شود.

در ادامه نمونه‌ای از موردی آورده شده است که ممکن است بخواهید از این قابلیت استفاده کنید.

فرض کنید Job با نام `old` از قبل در حال اجراست. می‌خواهید Podهای موجود به اجرای خود ادامه دهند، اما می‌خواهید بقیه Podهایی که این Job ایجاد می‌کند از قالب Pod متفاوتی استفاده کنند و Job نام جدیدی داشته باشد.
شما نمی‌توانید Job را به‌روزرسانی کنید، زیرا این فیلدها قابل به‌روزرسانی نیستند.
بنابراین، Job با نام `old` را حذف می‌کنید اما _Podهای آن را در حال اجرا باقی می‌گذارید_؛ این کار با دستور `kubectl delete jobs/old --cascade=orphan` انجام می‌شود.
پیش از حذف، انتخابگری را که این Job استفاده می‌کند یادداشت می‌کنید:

```shell
kubectl get job old -o yaml
```

خروجی مشابه زیر است:

```yaml
kind: Job
metadata:
  name: old
  ...
spec:
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: a8f3d00d-c6d2-11e5-9f87-42010af00002
  ...
```

سپس یک Job جدید با نام `new` ایجاد می‌کنید و همان انتخابگر را به‌صورت صریح مشخص می‌کنید.
از آنجا که Podهای موجود دارای برچسب `batch.kubernetes.io/controller-uid=a8f3d00d-c6d2-11e5-9f87-42010af00002` هستند، Job با نام `new` نیز آن‌ها را کنترل می‌کند.

باید در Job جدید `manualSelector: true` را مشخص کنید، زیرا از انتخابگری که سیستم معمولاً به‌طور خودکار برای شما تولید می‌کند استفاده نمی‌کنید.

```yaml
kind: Job
metadata:
  name: new
  ...
spec:
  manualSelector: true
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: a8f3d00d-c6d2-11e5-9f87-42010af00002
  ...
```

خود Job جدید uid متفاوتی با `a8f3d00d-c6d2-11e5-9f87-42010af00002` خواهد داشت. تنظیم `manualSelector: true` به سیستم می‌گوید که می‌دانید چه کار می‌کنید و به این ناهماهنگی اجازه بدهد.

### ردیابی Job با finalizerها

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

control plane Podهایی را که به هر Job تعلق دارند ردیابی می‌کند و متوجه می‌شود اگر چنین Podی از API server حذف شود. برای این کار، کنترل‌کننده Job، Podها را با finalizer به نام `batch.kubernetes.io/job-tracking` ایجاد می‌کند. کنترل‌کننده این finalizer را تنها پس از آن حذف می‌کند که Pod در وضعیت (status) Job به حساب آمده باشد؛ این امر به سایر کنترل‌کننده‌ها یا کاربران اجازه می‌دهد Pod را حذف کنند.

{{< note >}}
اگر مشاهده کردید Podهای یک Job با finalizer ردیابی گیر کرده‌اند، به [Pod من در وضعیت terminating باقی می‌ماند](/docs/tasks/debug/debug-application/debug-pods/) مراجعه کنید.
{{< /note >}}

### Jobهای Indexed الاستیک {#elastic-indexed-jobs}

{{< feature-state feature_gate_name="ElasticIndexedJob" >}}

می‌توانید با تغییر هم‌زمان `.spec.parallelism` و `.spec.completions` به‌گونه‌ای که `.spec.parallelism == .spec.completions` برقرار باشد، Jobهای Indexed را افزایش یا کاهش مقیاس دهید.
هنگام کاهش مقیاس، کوبرنتیز Podهایی را که اندیس بالاتری دارند حذف می‌کند.

موارد استفاده از Jobهای Indexed الاستیک شامل بارهای کاری دسته‌ای (batch) است که نیاز به تغییر مقیاس یک Job از نوع Indexed دارند، مانند Jobهای آموزش MPI، Horovod، Ray و PyTorch.

{{< note >}}
هنگامی که feature gate با نام [`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/) فعال باشد و یک Job از [gang scheduling](#integrate-with-workload-apis) استفاده کند، اندازه gang از مقدار قابل تغییر `schedulingPolicy.gang.minCount` پیروی می‌کند (یا در صورت تنظیم‌نشدن `minCount`، از `.spec.parallelism`).
می‌توانید gang را به یکی از دو روش زیر تغییر مقیاس دهید:

- مقدار `.spec.scheduling.schedulingPolicy.gang.minCount` را مستقیماً تنظیم کنید، یا
- در صورت تنظیم‌نشدن `minCount`، مقدار `.spec.parallelism` را تغییر دهید.

در هر یک از این دو تغییر، کنترل‌کننده `Workload` را دوباره کامپایل می‌کند و اندازه `PodGroup` را دوباره همگام‌سازی می‌کند و gang را بدون ایجاد مجدد Job، در همان جا تغییر مقیاس می‌دهد. به‌روزرسانی‌ها فقط بر Podهایی اعمال می‌شوند که در چرخه‌های زمان‌بندی آینده ارزیابی می‌شوند و بر Podهایی که از قبل زمان‌بندی شده‌اند تأثیری ندارند. مقدار `gang.minCount` بزرگ‌تر از `.spec.parallelism` رد می‌شود، زیرا چنین gangای هرگز نمی‌تواند برآورده شود.
{{< /note >}}

### ایجاد با تأخیر Podهای جایگزین {#pod-replacement-policy}

{{< feature-state feature_gate_name="JobPodReplacementPolicy" >}}

به‌طور پیش‌فرض، کنترل‌کننده Job به محض اینکه Podها شکست بخورند یا در حال خاتمه یافتن (terminating) باشند (یعنی زمان‌مهر حذف داشته باشند)، آن‌ها را دوباره ایجاد می‌کند.
این بدان معناست که در یک زمان مشخص، هنگامی که برخی از Podها در حال خاتمه یافتن هستند، تعداد Podهای در حال اجرای یک Job می‌تواند بیشتر از `parallelism` یا بیشتر از یک Pod به ازای هر اندیس باشد (اگر از Job از نوع Indexed استفاده می‌کنید).

می‌توانید انتخاب کنید که Podهای جایگزین تنها زمانی ایجاد شوند که Pod در حال خاتمه یافتن کاملاً به وضعیت نهایی رسیده باشد (یعنی `status.phase: Failed` داشته باشد).
برای این کار، `.spec.podReplacementPolicy: Failed` را تنظیم کنید.
سیاست جایگزینی پیش‌فرض به این بستگی دارد که آیا Job دارای `podFailurePolicy` است یا خیر.
اگر برای یک Job هیچ سیاست شکست Pod تعریف نشده باشد، حذف فیلد `podReplacementPolicy` سیاست جایگزینی `TerminatingOrFailed` را انتخاب می‌کند:
control plane بلافاصله پس از حذف Pod، Podهای جایگزین را ایجاد می‌کند
(به محض اینکه control plane ببیند Podی از این Job مقدار `deletionTimestamp` را دارد).
برای Jobهایی که سیاست شکست Pod دارند، مقدار پیش‌فرض `podReplacementPolicy` برابر `Failed` است و هیچ مقدار دیگری مجاز نیست.
برای آگاهی بیشتر درباره سیاست‌های شکست Pod برای Jobها به [سیاست شکست Pod](#pod-failure-policy) مراجعه کنید.

```yaml
kind: Job
metadata:
  name: new
  ...
spec:
  podReplacementPolicy: Failed
  ...
```

مشروط بر اینکه feature gate در کلاستر شما فعال باشد، می‌توانید فیلد `.status.terminating` را در یک Job بررسی کنید.
مقدار این فیلد تعداد Podهای متعلق به Job است که در حال حاضر در حال خاتمه یافتن هستند.

```shell
kubectl get jobs/myjob -o yaml
```

```yaml
apiVersion: batch/v1
kind: Job
# .metadata and .spec omitted
status:
  terminating: 3 # three Pods are terminating and have not yet reached the Failed phase
```

### واگذاری مدیریت یک آبجکت Job به کنترل‌کننده خارجی

{{< feature-state feature_gate_name="JobManagedBy" >}}

این قابلیت به شما امکان می‌دهد کنترل‌کننده داخلی Job را برای یک Job مشخص غیرفعال کنید و تطبیق (reconciliation) آن Job را به یک کنترل‌کننده خارجی واگذار کنید.

کنترل‌کننده‌ای را که Job را تطبیق می‌دهد با تنظیم یک مقدار سفارشی برای فیلد `spec.managedBy` مشخص می‌کنید؛ هر مقداری به‌جز `kubernetes.io/job-controller`. مقدار این فیلد تغییرناپذیر (immutable) است.

{{< note >}}
هنگام استفاده از این قابلیت، مطمئن شوید کنترل‌کننده‌ای که در این فیلد مشخص شده است نصب شده باشد، در غیر این صورت ممکن است Job اصلاً تطبیق داده نشود.
{{< /note >}}

{{< note >}}
هنگام توسعه یک کنترل‌کننده خارجی Job توجه داشته باشید که کنترل‌کننده شما باید به شیوه‌ای مطابق با تعاریف فیلدهای spec و status در API آبجکت Job عمل کند.

لطفاً این موارد را به‌طور دقیق در [Job API](/docs/reference/kubernetes-api/workload-resources/job-v1/) بررسی کنید.
همچنین توصیه می‌کنیم برای راستی‌آزمایی پیاده‌سازی خود، آزمون‌های انطباق e2e را برای آبجکت Job اجرا کنید.

در نهایت، هنگام توسعه یک کنترل‌کننده خارجی Job مطمئن شوید که از finalizer با نام `batch.kubernetes.io/job-tracking` که برای کنترل‌کننده داخلی رزرو شده است، استفاده نمی‌کند.
{{< /note >}}

## جایگزین‌ها {#alternatives}

### Podهای مستقل (Bare Pods)

هنگامی که نودی که یک Pod روی آن اجرا می‌شود راه‌اندازی مجدد شود یا از کار بیفتد، آن Pod خاتمه می‌یابد و دوباره راه‌اندازی نخواهد شد. با این حال، یک Job برای جایگزینی Podهای خاتمه‌یافته، Podهای جدید ایجاد می‌کند.
به همین دلیل توصیه می‌کنیم حتی اگر برنامه شما فقط به یک Pod نیاز دارد، به‌جای Pod مستقل از Job استفاده کنید.

### Replication Controller

Jobها مکمل [Replication Controllerها](/docs/concepts/workloads/controllers/replicationcontroller/) هستند.
یک Replication Controller Podهایی را مدیریت می‌کند که انتظار نمی‌رود خاتمه یابند (مثلاً وب‌سرورها)، و یک Job Podهایی را مدیریت می‌کند که انتظار می‌رود خاتمه یابند (مثلاً وظایف دسته‌ای).

همان‌طور که در [چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/) بحث شده است، `Job` *فقط* برای Podهایی مناسب است که `RestartPolicy` آن‌ها برابر `OnFailure` یا `Never` باشد.

{{< note >}}
اگر `RestartPolicy` تنظیم نشده باشد، مقدار پیش‌فرض آن `Always` است.
{{< /note >}}

### یک Job واحد، Pod کنترل‌کننده را راه‌اندازی می‌کند

الگوی دیگر این است که یک Job واحد یک Pod ایجاد کند و آن Pod نیز Podهای دیگری ایجاد کند و به نوعی نقش یک کنترل‌کننده سفارشی را برای آن Podها ایفا کند. این روش بیشترین انعطاف‌پذیری را فراهم می‌کند، اما ممکن است شروع کار با آن تا حدی پیچیده باشد و یکپارچگی کمتری با کوبرنتیز ارائه دهد.

یکی از مزایای این رویکرد این است که کل فرایند از تضمین تکمیل یک آبجکت Job بهره می‌برد، اما کنترل کامل بر اینکه چه Podهایی ایجاد شوند و کار چگونه به آن‌ها اختصاص یابد، حفظ می‌شود.

## {{% heading "whatsnext" %}}

* درباره [Podها](/docs/concepts/workloads/pods) بیاموزید.
* درباره روش‌های مختلف اجرای Jobها بخوانید:
  * [پردازش موازی درشت‌دانه با استفاده از صف کار](/docs/tasks/job/coarse-parallel-processing-work-queue/)
  * [پردازش موازی ریزدانه با استفاده از صف کار](/docs/tasks/job/fine-parallel-processing-work-queue/)
  * از یک [Job از نوع Indexed برای پردازش موازی با تخصیص ایستای کار](/docs/tasks/job/indexed-parallel-processing-static/) استفاده کنید
  * ایجاد چندین Job بر پایه یک قالب: [پردازش موازی با استفاده از بسط (Expansion)](/docs/tasks/job/parallel-processing-expansion/)
* پیوندهای موجود در [پاک‌سازی خودکار Jobهای پایان‌یافته](#clean-up-finished-jobs-automatically) را دنبال کنید
  تا درباره نحوه پاک‌سازی وظایف تکمیل‌شده و/یا ناموفق توسط کلاستر خود بیشتر بیاموزید.
* `Job` بخشی از REST API کوبرنتیز است.
  برای درک API مربوط به Jobها، تعریف آبجکت {{< api-reference page="batch/job-v1" >}} را بخوانید.
* درباره [`CronJob`](/docs/concepts/workloads/controllers/cron-jobs/) بخوانید که می‌توانید
  با آن مجموعه‌ای از Jobها را تعریف کنید که بر اساس یک زمان‌بندی اجرا می‌شوند، مشابه
  ابزار یونیکس `cron`.
* با استفاده از `podFailurePolicy` و بر پایه [مثال‌های](/docs/tasks/job/pod-failure-policy/) گام‌به‌گام، نحوه پیکربندی مدیریت شکست‌های Pod قابل‌تکرار و غیرقابل‌تکرار را تمرین کنید.
* درباره [gang scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/)
  برای زمان‌بندی «همه یا هیچ» Jobهای موازی بیاموزید.

[Indexed Job with Static Work Assignment]: /docs/tasks/job/indexed-parallel-processing-static/
[Job Template Expansion]: /docs/tasks/job/parallel-processing-expansion/
[Job with Pod-to-Pod Communication]: /docs/tasks/job/job-with-pod-to-pod-communication/
[Queue with Pod Per Work Item]: /docs/tasks/job/coarse-parallel-processing-work-queue/
[Queue with Variable Pod Count]: /docs/tasks/job/fine-parallel-processing-work-queue/

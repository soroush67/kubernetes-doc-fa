---
reviewers:
- erictune
- mimowo
- soltysh
title: Jobها
api_metadata:
- apiVersion: "batch/v1"
  kind: "Job"
content_type: concept
description: >-
  هر Job نمایانگر یک کار یک‌باره است که تا پایان اجرا می‌شود و سپس متوقف می‌شود.
feature:
  title: اجرای دسته‌ای
  description: >
    کوبرنتیز علاوه بر سرویس‌ها می‌تواند بارهای کاری دسته‌ای و CI شما را نیز مدیریت کند و در صورت تمایل، کانتینرهایی را که با شکست مواجه می‌شوند جایگزین کند.
weight: 50
hide_summary: true # Listed separately in section index
---

<!-- overview -->

هر Job یک یا چند Pod ایجاد می‌کند و اجرای Podها را تا زمانی که تعداد مشخصی از آن‌ها با موفقیت خاتمه یابند، دوباره امتحان می‌کند.
با پایان موفقیت‌آمیز هر Pod، شمار تکمیل‌های موفق در Job ثبت می‌شود. وقتی تعداد تکمیل‌های موفق به عدد
مشخص‌شده برسد، کار (یعنی Job) کامل شده است. با حذف یک Job، Podهایی که ایجاد کرده نیز پاک می‌شوند.
معلق کردن یک Job باعث حذف Podهای فعال آن می‌شود تا زمانی که Job دوباره از سر گرفته شود.

یک حالت ساده این است که یک آبجکت Job ایجاد کنید تا یک Pod به‌طور قابل‌اعتماد تا پایان اجرا شود.
اگر نخستین Pod با شکست مواجه شود یا حذف شود (برای مثال به دلیل خرابی سخت‌افزاری نود یا راه‌اندازی مجدد نود)،
آبجکت Job یک Pod جدید راه‌اندازی می‌کند.

همچنین می‌توانید از یک Job برای اجرای موازی چند Pod استفاده کنید.

اگر می‌خواهید یک Job را (چه یک کار منفرد و چه چند کار موازی) طبق یک زمان‌بندی اجرا کنید،
به [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) مراجعه کنید.

<!-- body -->

## اجرای یک Job نمونه

در ادامه یک پیکربندی نمونه برای Job آمده است. این Job عدد π را تا ۲۰۰۰ رقم اعشار محاسبه و چاپ می‌کند.
تکمیل آن حدود ۱۰ ثانیه طول می‌کشد.

{{% code_sample file="controllers/job.yaml" %}}

می‌توانید این نمونه را با دستور زیر اجرا کنید:

```shell
kubectl apply -f https://kubernetes.io/examples/controllers/job.yaml
```

خروجی مشابه زیر است:

```
job.batch/pi created
```

وضعیت Job را با `kubectl` بررسی کنید:

{{< tabs name="بررسی وضعیت Job" >}}
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

برای مشاهدهٔ Podهای تکمیل‌شدهٔ یک Job، از `kubectl get pods` استفاده کنید.

برای فهرست کردن همهٔ Podهای متعلق به یک Job در قالبی قابل‌خواندن برای ماشین، می‌توانید از دستوری مانند زیر استفاده کنید:

```shell
pods=$(kubectl get pods --selector=batch.kubernetes.io/job-name=pi --output=jsonpath='{.items[*].metadata.name}')
echo $pods
```

خروجی مشابه زیر است:

```
pi-5rwd7
```

در اینجا، انتخابگر (selector) همان انتخابگر Job است. گزینهٔ `--output=jsonpath` عبارتی را مشخص می‌کند
که نام هر Pod را از فهرست بازگردانده‌شده استخراج می‌کند.

خروجی استاندارد یکی از Podها را مشاهده کنید:

```shell
kubectl logs $pods
```

روش دیگری برای مشاهدهٔ لاگ‌های یک Job:

```shell
kubectl logs jobs/pi
```

خروجی مشابه زیر است:

```
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076601047101819429555961989467678374494482553797747268471040475346462080466842590694912933136770289891521047521620569660240580381501935112533824300355876402474964732639141992726042699227967823547816360093417216412199245863150302861829745557067498385054945885869269956909272107975093029553211653449872027559602364806654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275901
```

## نوشتن مشخصات Job

مانند همهٔ پیکربندی‌های دیگر کوبرنتیز، هر Job به فیلدهای `apiVersion`، `kind` و `metadata` نیاز دارد.

وقتی control plane برای یک Job، Podهای جدید ایجاد می‌کند، مقدار `.metadata.name` آن
Job بخشی از مبنای نام‌گذاری آن Podها است. نام یک Job باید یک مقدار معتبر
[زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)
باشد، اما این ممکن است برای نام میزبان (hostname) Podها نتایج غیرمنتظره‌ای ایجاد کند. برای بهترین سازگاری،
نام باید از قواعد سخت‌گیرانه‌تر
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) پیروی کند.
حتی وقتی نام یک زیردامنهٔ DNS است، طول آن نباید از ۶۳ نویسه بیشتر باشد.

هر Job همچنین به یک [بخش `.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) نیاز دارد.

### برچسب‌های Job

برچسب‌های Job برای `job-name` و `controller-uid` پیشوند `batch.kubernetes.io/` خواهند داشت.

### الگوی Pod

فیلد `.spec.template` تنها فیلد الزامی `.spec` است.

فیلد `.spec.template` یک [الگوی Pod](/docs/concepts/workloads/pods/#pod-templates) است.
طرح‌واره (schema) آن دقیقاً همانند یک {{< glossary_tooltip text="Pod" term_id="pod" >}} است،
با این تفاوت که تودرتو است و `apiVersion` یا `kind` ندارد.

الگوی Pod در یک Job، علاوه بر فیلدهای الزامی یک Pod، باید برچسب‌های مناسب
(به [انتخابگر Pod](#pod-selector) مراجعه کنید) و سیاست راه‌اندازی مجدد مناسبی را مشخص کند.

فقط [`RestartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)
با مقدار `Never` یا `OnFailure` مجاز است.

### انتخابگر Pod

فیلد `.spec.selector` اختیاری است. تقریباً در همهٔ موارد نباید آن را مشخص کنید.
به بخش [مشخص کردن انتخابگر Pod دلخواه](#specifying-your-own-pod-selector) مراجعه کنید.

### اجرای موازی Jobها {#parallel-jobs}

سه نوع اصلی از کارها برای اجرا به‌صورت Job مناسب هستند:

1. Jobهای غیرموازی
   - معمولاً فقط یک Pod راه‌اندازی می‌شود، مگر اینکه آن Pod با شکست مواجه شود.
   - به محض اینکه Pod آن با موفقیت خاتمه یابد، Job کامل می‌شود.
1. Jobهای موازی با *تعداد تکمیل ثابت*:
   - برای `.spec.completions` یک مقدار مثبت غیرصفر مشخص کنید.
   - در این حالت Job نمایانگر کل کار است و وقتی کامل می‌شود که به تعداد `.spec.completions` Pod موفق وجود داشته باشد.
   - هنگام استفاده از `.spec.completionMode="Indexed"`، هر Pod یک اندیس متفاوت در بازهٔ ۰ تا `.spec.completions-1` دریافت می‌کند.
1. Jobهای موازی با *صف کار*:
   - مقدار `.spec.completions` را مشخص نکنید؛ مقدار پیش‌فرض آن برابر `.spec.parallelism` است.
   - Podها باید میان خود یا با یک سرویس خارجی هماهنگ شوند تا مشخص کنند
     هر کدام روی چه چیزی کار کند. برای مثال، یک Pod ممکن است دسته‌ای حداکثر شامل N آیتم را از صف کار دریافت کند.
   - هر Pod به‌طور مستقل می‌تواند تشخیص دهد که آیا همهٔ همتایانش کار خود را تمام کرده‌اند یا نه،
     و در نتیجه آیا کل Job تمام شده است یا خیر.
   - وقتی _هر یک_ از Podهای Job با موفقیت خاتمه یابد، هیچ Pod جدیدی ایجاد نمی‌شود.
   - هنگامی که دست‌کم یک Pod با موفقیت خاتمه یافته باشد و همهٔ Podها خاتمه یافته باشند،
     Job با موفقیت کامل می‌شود.
   - هنگامی که هر یک از Podها با موفقیت خارج شد، هیچ Pod دیگری نباید همچنان روی این کار
     مشغول باشد یا خروجی بنویسد. همهٔ آن‌ها باید در حال خروج باشند.

برای یک Job _غیرموازی_، می‌توانید هر دو فیلد `.spec.completions` و `.spec.parallelism` را تنظیم‌نشده رها کنید.
وقتی هر دو تنظیم نشده باشند، مقدار پیش‌فرض هر دو ۱ است.

برای یک Job با _تعداد تکمیل ثابت_، باید `.spec.completions` را برابر تعداد تکمیل‌های لازم قرار دهید.
می‌توانید `.spec.parallelism` را تنظیم کنید یا آن را تنظیم‌نشده رها کنید تا مقدار پیش‌فرض ۱ بگیرد.

برای یک Job از نوع _صف کار_، باید `.spec.completions` را تنظیم‌نشده رها کنید و `.spec.parallelism` را
برابر یک عدد صحیح نامنفی قرار دهید.

برای اطلاعات بیشتر دربارهٔ نحوهٔ استفاده از انواع مختلف Job،
به بخش [الگوهای Job](#job-patterns) مراجعه کنید.

#### کنترل موازی‌سازی

موازی‌سازی درخواستی (`.spec.parallelism`) را می‌توان روی هر مقدار نامنفی تنظیم کرد.
اگر مشخص نشود، مقدار پیش‌فرض آن ۱ است.
اگر برابر ۰ تعیین شود، Job در عمل تا زمانی که این مقدار افزایش یابد متوقف می‌ماند.

موازی‌سازی واقعی (تعداد Podهایی که در هر لحظه در حال اجرا هستند) ممکن است به دلایل مختلف
بیشتر یا کمتر از موازی‌سازی درخواستی باشد:

- در Jobهای با _تعداد تکمیل ثابت_، تعداد واقعی Podهایی که به‌صورت موازی اجرا می‌شوند از تعداد
  تکمیل‌های باقی‌مانده بیشتر نمی‌شود. مقادیر بالاتر `.spec.parallelism` در عمل نادیده گرفته می‌شوند.
- در Jobهای از نوع _صف کار_، پس از موفقیت هر یک از Podها هیچ Pod جدیدی راه‌اندازی نمی‌شود؛ با این حال، Podهای باقی‌مانده اجازه دارند کار خود را کامل کنند.
- اگر {{< glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller" >}} Job هنوز فرصت واکنش نشان دادن نداشته باشد.
- اگر کنترل‌کنندهٔ Job به هر دلیلی (کمبود `ResourceQuota`، نبود مجوز و غیره) نتواند Podها را ایجاد کند،
  ممکن است تعداد Podها کمتر از مقدار درخواستی باشد.
- کنترل‌کنندهٔ Job ممکن است به دلیل شکست‌های بیش از حد Podهای قبلی در همان Job، سرعت ایجاد Podهای جدید را محدود کند.
- وقتی یک Pod به‌صورت مؤدبانه (graceful) خاموش می‌شود، توقف آن زمان می‌برد.

### حالت تکمیل

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

Jobهای با _تعداد تکمیل ثابت_، یعنی Jobهایی که مقدار `.spec.completions` آن‌ها null نیست،
می‌توانند یک حالت تکمیل داشته باشند که در `.spec.completionMode` مشخص می‌شود:

- حالت `NonIndexed` (پیش‌فرض): Job زمانی کامل در نظر گرفته می‌شود که به تعداد
  `.spec.completions` Pod با موفقیت تکمیل شده باشند. به عبارت دیگر، تکمیل همهٔ Podها
  هم‌ارز یکدیگر است. توجه کنید که Jobهایی که مقدار `.spec.completions` آن‌ها null است،
  به‌طور ضمنی `NonIndexed` هستند.
- حالت `Indexed`: هر یک از Podهای Job یک اندیس تکمیل متناظر از ۰ تا
  `.spec.completions-1` دریافت می‌کند. این اندیس از چهار راه در دسترس است:
  - حاشیه‌نویسی (annotation) `batch.kubernetes.io/job-completion-index` روی Pod.
  - برچسب `batch.kubernetes.io/job-completion-index` روی Pod (برای نسخهٔ v1.28 و بعد از آن). توجه کنید
    که برای استفاده از این برچسب، feature gate با نام `PodIndexLabel` باید فعال باشد؛ این feature gate
    به‌طور پیش‌فرض فعال است.
  - به‌عنوان بخشی از نام میزبان Pod، طبق الگوی `$(job-name)-$(index)`.
    وقتی از یک Job از نوع Indexed همراه با یک
    {{< glossary_tooltip term_id="Service" >}} استفاده می‌کنید، Podهای داخل Job می‌توانند
    با استفاده از نام‌های میزبان قطعی، از طریق DNS یکدیگر را آدرس‌دهی کنند. برای اطلاعات بیشتر دربارهٔ
    نحوهٔ پیکربندی این قابلیت، به [Job با ارتباط Pod به Pod](/docs/tasks/job/job-with-pod-to-pod-communication/) مراجعه کنید.
  - از درون کار کانتینری‌شده، در متغیر محیطی `JOB_COMPLETION_INDEX`.
  
  Job زمانی کامل در نظر گرفته می‌شود که برای هر اندیس یک Pod با موفقیت تکمیل شده باشد.
  برای اطلاعات بیشتر دربارهٔ نحوهٔ استفاده از این حالت، به
  [Job اندیس‌دار برای پردازش موازی با تخصیص ایستای کار](/docs/tasks/job/indexed-parallel-processing-static/) مراجعه کنید.

{{< note >}}
هرچند به‌ندرت پیش می‌آید، ممکن است بیش از یک Pod برای یک اندیس راه‌اندازی شود (به دلایل مختلفی مانند خرابی نود،
راه‌اندازی مجدد kubelet یا بیرون‌رانی (eviction) Podها). در این حالت، فقط نخستین Pod که با موفقیت تکمیل شود
در شمار تکمیل‌ها محسوب می‌شود و وضعیت Job را به‌روزرسانی می‌کند. کنترل‌کنندهٔ Job سایر Podهایی را که
برای همان اندیس در حال اجرا هستند یا تکمیل شده‌اند، به محض شناسایی حذف می‌کند.
{{< /note >}}

## یکپارچه‌سازی با APIهای Workload

{{< feature-state feature_gate_name="WorkloadWithJob" >}}

وقتی feature gate با نام [`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/)
فعال باشد، کنترل‌کنندهٔ Job پیش از ایجاد هر Pod، پیکربندی `.spec.scheduling` آن Job را
به آبجکت‌های [Workload](/docs/concepts/workloads/workload-api/) و
[PodGroup](/docs/concepts/workloads/podgroup-api/) (`scheduling.k8s.io/v1beta1`) تبدیل می‌کند.
با این کار می‌توانید قصد زمان‌بندی خود را برای یک Job به‌صراحت بیان کنید؛ برای مثال
[زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) (همهٔ Podها
با هم زمان‌بندی شوند یا هیچ‌کدام)، هم‌مکانی در توپولوژی و رفتار هنگام اختلال.

وقتی `.spec.scheduling` را حذف کنید، Job به‌طور پیش‌فرض از سیاست زمان‌بندی `Basic` استفاده می‌کند
که همان نتیجهٔ زمان‌بندی استاندارد Pod به Pod یک Job معمولی را حفظ می‌کند. کنترل‌کننده
همچنان برای هر Job واجد شرایط (از جمله Jobهای `Basic`) یک `Workload` و یک `PodGroup` ایجاد می‌کند،
بنابراین آبجکت‌های قابل‌مشاهده صرف‌نظر از سیاست، یکسان هستند.

### پیکربندی زمان‌بندی

فیلد `.spec.scheduling` فیلدهای زیر را می‌پذیرد:

- فیلد `schedulingPolicy`: دقیقاً یکی از `basic` یا `gang` باید مشخص شود. با `gang`،
  همهٔ Podها باید پیش از اتصال (bind) هر یک از آن‌ها، با هم قابل‌زمان‌بندی باشند. اگر
  `gang.minCount` مشخص نشود، مقدار پیش‌فرض آن برابر `.spec.parallelism` آن Job است. به
  [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) مراجعه کنید.
- فیلد `schedulingConstraints`: قیدهای هم‌مکانی
  [توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
  برای Podهای Job.
- فیلد `disruptionMode`: اینکه Podها به‌صورت جداگانه (`single`) دچار اختلال شوند یا به‌صورت
  گروهی (`all`). به
  [اختلال و اولویت](/docs/concepts/workloads/workload-api/disruption-and-priority/) مراجعه کنید.
- فیلد `resourceClaims`: درخواست‌های منبع پویا که میان Podهای Job به اشتراک گذاشته می‌شوند.

همهٔ فیلدهای `.spec.scheduling` پس از ایجاد Job تغییرناپذیر هستند، به جز
`schedulingPolicy.gang.minCount` که می‌توانید آن را برای
[مقیاس‌دهی کشسان یک گروه](#elastic-indexed-jobs) تغییر دهید.

### زمان‌بندی گروهی

Job زیر برای ۸ Pod خود زمان‌بندی گروهی درخواست می‌کند؛ این Podها در یک
ناحیهٔ (zone) واحد هم‌مکان می‌شوند و با هم دچار اختلال می‌شوند:

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

کنترل‌کنندهٔ Job هنگام پردازش این Job، کارهای زیر را انجام می‌دهد:

1. یک آبجکت [Workload](/docs/concepts/workloads/workload-api/) در همان
   فضای نام (namespace) ایجاد می‌کند که شامل یک `podGroupTemplate` تولیدشده از `.spec.scheduling` است
   (در اینجا، یک [سیاست gang](/docs/concepts/workloads/workload-api/policies/) با
   `minCount: 8`).
1. یک آبجکت PodGroup از روی آن الگو ایجاد می‌کند. این PodGroup واحد زمان‌بندی در زمان اجرا است
   و یک نسخهٔ درون‌خطی از سیاست را در خود دارد.
1. Podهایی ایجاد می‌کند که فیلد `.spec.schedulingGroup.podGroupName` آن‌ها برابر نام PodGroup
   تنظیم شده است و به این ترتیب هر Pod را به گروه زمان‌بندی‌اش پیوند می‌دهد.

کنترل‌کننده این آبجکت‌ها را از طریق ارجاع‌های موجود در spec
(`Workload.spec.controllerRef` و `PodGroup.spec.workloadRef`) پیدا می‌کند، نه از روی
نام. آبجکت‌هایی که کنترل‌کننده ایجاد می‌کند یک ورودی `ownerReferences` دارند که به
Job اشاره می‌کند، بنابراین هنگام حذف Job، زباله‌روبی (garbage collection) می‌شوند.

### زمان‌بندی پیش‌فرض (Basic)

هر Job که `.spec.scheduling` را مشخص نکند، به‌طور پیش‌فرض از `Basic` استفاده می‌کند که در عمل
به معنای کنار گذاشتن ضمنی زمان‌بندی گروهی است. Podهای آن به همان شیوهٔ یک Job معمولی زمان‌بندی می‌شوند،
در حالی که یک `Workload` و یک `PodGroup` از نوع `Basic` همچنان ایجاد می‌شوند:

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

### کنترل‌کننده‌های سطح بالاتر

در یک Job مستقل، کنترل‌کنندهٔ Job مالک هر دو آبجکت `Workload` و
`PodGroup` است. اما وقتی یک Job دارای یک `ownerReference` به یک کنترل‌کنندهٔ والد باشد
که خود `Workload` را تولید می‌کند (برای مثال `JobSet`)، کنترل‌کنندهٔ Job مالکیت
`Workload` را به آن والد واگذار می‌کند. اینکه کنترل‌کنندهٔ Job همچنان
`PodGroup` زمان اجرا را ایجاد کند یا نه، به چیزی بستگی دارد که والد به آن واگذار می‌کند:

- اگر والد حاشیه‌نویسی `scheduling.k8s.io/group-template-name` را روی
  Job تنظیم کند، کنترل‌کنندهٔ Job آبجکت `PodGroup` را ایجاد می‌کند و مالک آن می‌شود و آن را به
  `PodGroupTemplate` نام‌گذاری‌شدهٔ والد نگاشت می‌کند.
- در غیر این صورت، والد مالک هر دو آبجکت است و کنترل‌کنندهٔ Job هیچ‌یک را ایجاد نمی‌کند؛
  بلکه آبجکت‌های موجود را پیدا می‌کند و هنگام ایجاد Podها از آن‌ها استفاده می‌کند.

اگر الگوی Pod یک Job از قبل دارای فیلد `.spec.template.spec.schedulingGroup` باشد،
کنترل‌کنندهٔ Job هیچ‌یک از این دو آبجکت را ایجاد نمی‌کند تا شما (یا یک کنترل‌کنندهٔ سطح بالاتر)
خودتان چرخهٔ حیات `Workload`/`PodGroup` را مدیریت کنید.

### رفتار CronJob

Jobهایی که یک `CronJob` ایجاد می‌کند مستقل هستند؛ `CronJob` هیچ آبجکت `Workload` ایجاد
یا مدیریت نمی‌کند. اگر `jobTemplate` یک `CronJob` فیلد `.spec.scheduling` را تنظیم کند، کنترل‌کنندهٔ
Job برای هر نمونهٔ Job یک `Workload` و یک `PodGroup` جداگانه ایجاد می‌کند
که از `.spec.scheduling` همان Job تولید می‌شوند (و در صورت مشخص نبودن، پیش‌فرض `Basic` است).
این آبجکت‌ها هنگام تکمیل یا حذف هر Job، زباله‌روبی می‌شوند.

### محدودیت‌های نسخهٔ آلفا {#workload-integration-limitations}

- هر Job دقیقاً به یک `PodGroup` نگاشت می‌شود؛ همهٔ Podهای Job یک سیاست زمان‌بندی
  واحد را به اشتراک می‌گذارند.
- فقط `schedulingPolicy.gang.minCount` قابل‌تغییر است؛ همهٔ فیلدهای دیگر `.spec.scheduling`
  پس از ایجاد تغییرناپذیر هستند.
- Jobهای معلق‌شده آبجکت‌های `Workload` و `PodGroup` خود را حفظ می‌کنند؛ این آبجکت‌ها
  هنگام تعلیق حذف نمی‌شوند و هنگام از سرگیری دوباره ایجاد نمی‌شوند.

## مدیریت خرابی‌های Pod و کانتینر

کانتینری که درون یک Pod اجرا می‌شود ممکن است به دلایل مختلفی با خرابی روبه‌رو شود. برای نمونه، فرایند درون آن با کد خروج غیرصفر پایان یابد، یا کانتینر به‌دلیل فراتر رفتن از محدودیت حافظه متوقف شود. اگر چنین اتفاقی بیفتد و `.spec.template.spec.restartPolicy = "OnFailure"` تنظیم شده باشد، Pod روی نود باقی می‌ماند و کانتینر دوباره اجرا می‌شود. بنابراین برنامهٔ شما باید بتواند حالتی را که به‌صورت محلی دوباره راه‌اندازی می‌شود مدیریت کند. در غیر این صورت، مقدار `.spec.template.spec.restartPolicy = "Never"` را مشخص کنید. برای اطلاعات بیشتر دربارهٔ `restartPolicy` به [چرخهٔ حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) مراجعه کنید.

کل یک Pod نیز ممکن است به دلایل مختلفی خراب شود. برای نمونه، Pod از نود بیرون رانده شود (چون نود ارتقا یافته، راه‌اندازی مجدد شده، حذف شده و مانند آن)، یا یکی از کانتینرهای Pod خراب شود و `.spec.template.spec.restartPolicy = "Never"` تنظیم شده باشد. هنگامی که یک Pod خراب می‌شود، کنترل‌کنندهٔ Job یک Pod جدید راه‌اندازی می‌کند. بنابراین برنامهٔ شما باید بتواند حالتی را که در یک Pod جدید دوباره راه‌اندازی می‌شود مدیریت کند. به‌ویژه، باید فایل‌های موقت، قفل‌ها، خروجی‌های ناقص و موارد مشابهی را که از اجراهای قبلی باقی مانده‌اند مدیریت کند.

به‌طور پیش‌فرض، هر خرابی Pod در محدودیت `.spec.backoffLimit` شمرده می‌شود؛ به [سیاست خرابی backoff برای Pod](#pod-backoff-failure-policy) مراجعه کنید. با این حال، می‌توانید با تنظیم [سیاست خرابی Pod](#pod-failure-policy) برای Job، نحوهٔ مدیریت خرابی‌های Pod را سفارشی کنید.

افزون بر این، می‌توانید با تنظیم فیلد `.spec.backoffLimitPerIndex` خرابی‌های Pod را برای هر اندیس از یک Job از نوع [Indexed](#completion-mode) به‌طور مستقل بشمارید (برای اطلاعات بیشتر، به [محدودیت backoff برای هر اندیس](#backoff-limit-per-index) مراجعه کنید).

توجه داشته باشید که حتی اگر `.spec.parallelism = 1`، `.spec.completions = 1` و `.spec.template.spec.restartPolicy = "Never"` را مشخص کنید، ممکن است یک برنامه گاهی دو بار اجرا شود.

اگر مقدار هر دو فیلد `.spec.parallelism` و `.spec.completions` را بزرگ‌تر از ۱ تعیین کنید، ممکن است چند Pod به‌طور هم‌زمان در حال اجرا باشند. بنابراین Podهای شما باید اجرای هم‌زمان را نیز تحمل کنند.

اگر فیلد `.spec.podFailurePolicy` را مشخص کنید، کنترل‌کنندهٔ Job یک Pod در حال خاتمه (Podی که فیلد `.metadata.deletionTimestamp` آن تنظیم شده است) را تا زمانی که به وضعیت پایانی نرسیده باشد (یعنی مقدار `.status.phase` آن `Failed` یا `Succeeded` نباشد) خرابی به حساب نمی‌آورد. با این حال، کنترل‌کنندهٔ Job به محض آشکار شدن خاتمه، یک Pod جایگزین ایجاد می‌کند. پس از خاتمهٔ Pod، کنترل‌کنندهٔ Job با در نظر گرفتن این Pod خاتمه‌یافته، مقادیر `.backoffLimit` و `.podFailurePolicy` را برای Job مربوطه ارزیابی می‌کند.

اگر هر یک از این الزامات برآورده نشود، کنترل‌کنندهٔ Job یک Pod در حال خاتمه را بی‌درنگ خرابی به حساب می‌آورد، حتی اگر آن Pod بعداً با `phase: "Succeeded"` خاتمه یابد.

### سیاست خرابی backoff برای Pod

در برخی موقعیت‌ها می‌خواهید یک Job پس از تعداد معینی تلاش مجدد، به‌دلیل یک خطای منطقی در پیکربندی یا موارد مشابه، ناموفق اعلام شود. برای این کار، با تنظیم `.spec.backoffLimit` تعداد تلاش‌های مجدد پیش از ناموفق در نظر گرفتن Job را مشخص کنید.

مقدار پیش‌فرض `.spec.backoffLimit` برابر ۶ است، مگر اینکه [محدودیت backoff برای هر اندیس](#backoff-limit-per-index) (فقط برای Job از نوع Indexed) مشخص شده باشد. هنگامی که `.spec.backoffLimitPerIndex` مشخص شده باشد، مقدار پیش‌فرض `.spec.backoffLimit` برابر 2147483647 (MaxInt32) است.

کنترل‌کنندهٔ Job، Podهای خراب‌شدهٔ مرتبط با Job را با تأخیر backoff نمایی (۱۰ ثانیه، ۲۰ ثانیه، ۴۰ ثانیه و ...) که حداکثر به ده دقیقه محدود است، دوباره ایجاد می‌کند.

تعداد تلاش‌های مجدد به دو روش محاسبه می‌شود:

- تعداد Podهایی که `.status.phase = "Failed"` دارند.
- هنگام استفاده از `restartPolicy = "OnFailure"`، تعداد تلاش‌های مجدد در همهٔ کانتینرهای Podهایی که مقدار `.status.phase` آن‌ها `Pending` یا `Running` است.

اگر هر یک از این دو محاسبه به `.spec.backoffLimit` برسد، Job ناموفق در نظر گرفته می‌شود.

{{< note >}}
اگر Job شما `restartPolicy = "OnFailure"` داشته باشد، به یاد داشته باشید که پس از رسیدن به محدودیت backoff، Podی که Job را اجرا می‌کند خاتمه می‌یابد. این موضوع می‌تواند اشکال‌زدایی برنامهٔ اجرایی Job را دشوارتر کند. پیشنهاد می‌کنیم هنگام اشکال‌زدایی Job، مقدار `restartPolicy = "Never"` را تنظیم کنید یا از یک سامانهٔ ثبت لاگ استفاده کنید تا خروجی Jobهای ناموفق ناخواسته از دست نرود.
{{< /note >}}

### محدودیت backoff برای هر اندیس {#backoff-limit-per-index}

{{< feature-state feature_gate_name="JobBackoffLimitPerIndex" >}}

هنگامی که یک Job از نوع [indexed](#completion-mode) را اجرا می‌کنید، می‌توانید تلاش‌های مجدد ناشی از خرابی Podها را برای هر اندیس به‌طور مستقل مدیریت کنید. برای این کار، با تنظیم `.spec.backoffLimitPerIndex` حداکثر تعداد خرابی‌های Pod برای هر اندیس را مشخص کنید.

هنگامی که محدودیت backoff یک اندیس از حد مجاز فراتر رود، کوبرنتیز آن اندیس را ناموفق در نظر می‌گیرد و آن را به فیلد `.status.failedIndexes` اضافه می‌کند. اندیس‌های موفق، یعنی اندیس‌هایی که Podهای آن‌ها با موفقیت اجرا شده‌اند، صرف‌نظر از اینکه فیلد `backoffLimitPerIndex` را تنظیم کرده باشید یا نه، در فیلد `.status.completedIndexes` ثبت می‌شوند.

توجه داشته باشید که ناموفق بودن یک اندیس، اجرای اندیس‌های دیگر را متوقف نمی‌کند. در Jobی که برای آن محدودیت backoff برای هر اندیس مشخص کرده‌اید، پس از پایان همهٔ اندیس‌ها، اگر دست‌کم یکی از آن‌ها ناموفق شده باشد، کنترل‌کنندهٔ Job با تنظیم شرط Failed در وضعیت، کل Job را ناموفق علامت‌گذاری می‌کند. Job حتی اگر برخی از اندیس‌ها، و شاید تقریباً همهٔ آن‌ها، با موفقیت پردازش شده باشند، ناموفق علامت‌گذاری می‌شود.

افزون بر این، می‌توانید با تنظیم فیلد `.spec.maxFailedIndexes` حداکثر تعداد اندیس‌هایی را که ناموفق علامت‌گذاری می‌شوند محدود کنید. هنگامی که تعداد اندیس‌های ناموفق از مقدار فیلد `maxFailedIndexes` فراتر رود، کنترل‌کنندهٔ Job خاتمهٔ همهٔ Podهای باقی‌ماندهٔ در حال اجرای آن Job را آغاز می‌کند. پس از خاتمهٔ همهٔ Podها، کنترل‌کنندهٔ Job با تنظیم شرط Failed در وضعیت Job، کل Job را ناموفق علامت‌گذاری می‌کند.

در ادامه، نمونه‌ای از مانیفست یک Job آمده است که `backoffLimitPerIndex` را تعریف می‌کند:

{{< code_sample file="/controllers/job-backoff-limit-per-index-example.yaml" >}}

در نمونهٔ بالا، کنترل‌کنندهٔ Job برای هر اندیس یک بار راه‌اندازی مجدد را مجاز می‌داند. هنگامی که تعداد کل اندیس‌های ناموفق از ۵ فراتر رود، کل Job خاتمه می‌یابد.

پس از پایان Job، وضعیت آن به این شکل است:

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

کنترل‌کنندهٔ Job شرط `FailureTarget` را به Job اضافه می‌کند تا [خاتمه و پاک‌سازی Job](#job-termination-and-cleanup) را آغاز کند. هنگامی که همهٔ Podهای Job خاتمه یافتند، کنترل‌کنندهٔ Job شرط `Failed` را با همان مقادیر `reason` و `message` شرط `FailureTarget` اضافه می‌کند. برای جزئیات بیشتر، به [خاتمهٔ Podهای Job](#termination-of-job-pods) مراجعه کنید.

افزون بر این، ممکن است بخواهید backoff برای هر اندیس را همراه با یک [سیاست خرابی Pod](#pod-failure-policy) به کار ببرید. هنگام استفاده از backoff برای هر اندیس، کنش جدیدی به نام `FailIndex` در دسترس است که با آن می‌توانید از تلاش‌های مجدد غیرضروری درون یک اندیس جلوگیری کنید.

### سیاست خرابی Pod {#pod-failure-policy}

{{< feature-state feature_gate_name="JobPodFailurePolicy" >}}

سیاست خرابی Pod که با فیلد `.spec.podFailurePolicy` تعریف می‌شود، به کلاستر شما امکان می‌دهد خرابی‌های Pod را بر اساس کدهای خروج کانتینرها و شرط‌های Pod مدیریت کند.

در برخی موقعیت‌ها ممکن است بخواهید هنگام مدیریت خرابی‌های Pod، کنترل بیشتری نسبت به [سیاست خرابی backoff برای Pod](#pod-backoff-failure-policy) داشته باشید که بر پایهٔ `.spec.backoffLimit` در Job است. چند نمونه از این موارد کاربرد عبارت‌اند از:

* برای بهینه‌سازی هزینه‌های اجرای بارهای کاری با جلوگیری از راه‌اندازی‌های مجدد غیرضروری Pod، می‌توانید به محض اینکه یکی از Podهای یک Job با کد خروجی که نشان‌دهندهٔ یک باگ نرم‌افزاری است ناموفق شود، آن Job را خاتمه دهید.
* برای اطمینان از اینکه Job شما حتی در صورت وقوع اختلال به پایان می‌رسد، می‌توانید خرابی‌های Pod ناشی از اختلال‌ها (مانند {{< glossary_tooltip text="پیش‌دستی" term_id="preemption" >}}، {{< glossary_tooltip text="بیرون‌رانی آغازشده از طریق API" term_id="api-eviction" >}} یا بیرون‌رانی مبتنی بر {{< glossary_tooltip text="taint" term_id="taint" >}}) را نادیده بگیرید تا در محدودیت تلاش‌های مجدد `.spec.backoffLimit` شمرده نشوند.

برای پاسخ به موارد کاربرد بالا، می‌توانید یک سیاست خرابی Pod را در فیلد `.spec.podFailurePolicy` پیکربندی کنید. این سیاست می‌تواند خرابی‌های Pod را بر اساس کدهای خروج کانتینرها و شرط‌های Pod مدیریت کند.

در ادامه، مانیفست یک Job آمده است که `podFailurePolicy` را تعریف می‌کند:

{{% code_sample file="/controllers/job-pod-failure-policy-example.yaml" %}}

در نمونهٔ بالا، نخستین قاعدهٔ سیاست خرابی Pod مشخص می‌کند که اگر کانتینر `main` با کد خروج ۴۲ ناموفق شود، Job باید ناموفق علامت‌گذاری شود. قواعد زیر به‌طور خاص به کانتینر `main` مربوط‌اند:

- کد خروج ۰ به این معناست که کانتینر با موفقیت اجرا شده است
- کد خروج ۴۲ به این معناست که **کل Job** ناموفق شده است
- هر کد خروج دیگر نشان می‌دهد که کانتینر و در نتیجه کل Pod ناموفق شده است. اگر تعداد کل راه‌اندازی‌های مجدد کمتر از `backoffLimit` باشد، Pod دوباره ایجاد می‌شود. اگر به `backoffLimit` برسد، **کل Job** ناموفق می‌شود.

{{< note >}}
از آنجا که قالب Pod مقدار `restartPolicy: Never` را مشخص می‌کند، kubelet کانتینر `main` را در آن Pod خاص دوباره راه‌اندازی نمی‌کند.
{{< /note >}}

دومین قاعدهٔ سیاست خرابی Pod که کنش `Ignore` را برای Podهای ناموفق دارای شرط `DisruptionTarget` مشخص می‌کند، اختلال‌های Pod را از شمارش در محدودیت تلاش‌های مجدد `.spec.backoffLimit` مستثنا می‌کند.

{{< note >}}
اگر Job، چه بر اثر سیاست خرابی Pod و چه بر اثر سیاست خرابی backoff برای Pod، ناموفق شود و چند Pod را اجرا کند، کوبرنتیز همهٔ Podهای آن Job را که هنوز در وضعیت Pending یا Running هستند خاتمه می‌دهد.
{{< /note >}}

برخی از الزامات و معناشناسی این API عبارت‌اند از:

- اگر می‌خواهید از فیلد `.spec.podFailurePolicy` برای یک Job استفاده کنید، باید قالب Pod آن Job را نیز با مقدار `Never` برای `.spec.restartPolicy` تعریف کنید.
- قواعد سیاست خرابی Pod که در `spec.podFailurePolicy.rules` مشخص می‌کنید، به ترتیب ارزیابی می‌شوند. به محض اینکه یک قاعده با خرابی Pod مطابقت یابد، قواعد باقی‌مانده نادیده گرفته می‌شوند. اگر هیچ قاعده‌ای با خرابی Pod مطابقت نداشته باشد، مدیریت پیش‌فرض اعمال می‌شود.
- ممکن است بخواهید یک قاعده را با مشخص کردن نام یک کانتینر در `spec.podFailurePolicy.rules[*].onExitCodes.containerName` به آن کانتینر محدود کنید. اگر نام مشخص نشود، قاعده بر همهٔ کانتینرها اعمال می‌شود. اگر مشخص شود، باید با نام یکی از کانتینرها یا `initContainer`ها در قالب Pod مطابقت داشته باشد.
- می‌توانید کنشی را که هنگام مطابقت یک سیاست خرابی Pod انجام می‌شود، با `spec.podFailurePolicy.rules[*].action` مشخص کنید. مقادیر ممکن عبارت‌اند از:
  - کنش `FailJob`: برای نشان دادن اینکه Job مربوط به Pod باید Failed علامت‌گذاری شود و همهٔ Podهای در حال اجرا خاتمه یابند.
  - کنش `Ignore`: برای نشان دادن اینکه شمارندهٔ مربوط به `.spec.backoffLimit` نباید افزایش یابد و باید یک Pod جایگزین ایجاد شود.
  - کنش `Count`: برای نشان دادن اینکه Pod باید به روش پیش‌فرض مدیریت شود. شمارندهٔ مربوط به `.spec.backoffLimit` باید افزایش یابد.
  - کنش `FailIndex`: این کنش را همراه با [محدودیت backoff برای هر اندیس](#backoff-limit-per-index) به کار ببرید تا از تلاش‌های مجدد غیرضروری درون اندیس یک Pod ناموفق جلوگیری شود.

{{< note >}}
هنگامی که از `podFailurePolicy` استفاده می‌کنید، کنترل‌کنندهٔ Job فقط Podهایی را که در فاز `Failed` هستند مطابقت می‌دهد. Podهایی که برچسب زمانی حذف دارند ولی در فاز پایانی (`Failed` یا `Succeeded`) نیستند، همچنان در حال خاتمه در نظر گرفته می‌شوند. این یعنی Podهای در حال خاتمه تا رسیدن به فاز پایانی، یک [finalizer ردیابی](#job-tracking-with-finalizers) را حفظ می‌کنند. از کوبرنتیز 1.27 به بعد، kubelet Podهای حذف‌شده را به فاز پایانی منتقل می‌کند (به [فاز Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) مراجعه کنید). این کار تضمین می‌کند که کنترل‌کنندهٔ Job، finalizerهای Podهای حذف‌شده را بردارد.
{{< /note >}}

{{< note >}}
از کوبرنتیز v1.28 به بعد، هنگامی که از سیاست خرابی Pod استفاده می‌شود، کنترل‌کنندهٔ Job، Podهای در حال خاتمه را تنها پس از رسیدن آن‌ها به فاز پایانی `Failed` دوباره ایجاد می‌کند. این رفتار مشابه `podReplacementPolicy: Failed` است. برای اطلاعات بیشتر، به [سیاست جایگزینی Pod](#pod-replacement-policy) مراجعه کنید.
{{< /note >}}

هنگامی که از `podFailurePolicy` استفاده می‌کنید و Job به‌دلیل مطابقت Pod با قاعده‌ای دارای کنش `FailJob` ناموفق می‌شود، کنترل‌کنندهٔ Job با افزودن شرط `FailureTarget` فرایند خاتمهٔ Job را آغاز می‌کند. برای جزئیات بیشتر، به [خاتمه و پاک‌سازی Job](#job-termination-and-cleanup) مراجعه کنید.

## سیاست موفقیت {#success-policy}

هنگام ایجاد یک Job از نوع Indexed، می‌توانید با استفاده از `.spec.successPolicy` و بر اساس Podهای موفق، مشخص کنید که Job چه زمانی موفق اعلام شود.

به‌طور پیش‌فرض، یک Job زمانی موفق می‌شود که تعداد Podهای موفق با `.spec.completions` برابر شود. در موقعیت‌های زیر ممکن است برای موفق اعلام کردن یک Job به کنترل بیشتری نیاز داشته باشید:

* هنگام اجرای شبیه‌سازی‌ها با پارامترهای مختلف، ممکن است برای موفقیت کل Job لازم نباشد همهٔ شبیه‌سازی‌ها موفق شوند.
* هنگام پیروی از الگوی رهبر-کارگر (leader-worker)، تنها موفقیت رهبر است که موفقیت یا ناموفق بودن Job را تعیین می‌کند. چارچوب‌هایی مانند MPI و PyTorch نمونه‌هایی از این الگو هستند.

برای پاسخ به موارد کاربرد بالا، می‌توانید یک سیاست موفقیت را در فیلد `.spec.successPolicy` پیکربندی کنید. این سیاست می‌تواند موفقیت Job را بر اساس Podهای موفق مدیریت کند. پس از اینکه Job سیاست موفقیت را برآورده کرد، کنترل‌کنندهٔ Job، Podهای باقی‌مانده را خاتمه می‌دهد. سیاست موفقیت با قواعدی تعریف می‌شود. هر قاعده می‌تواند یکی از شکل‌های زیر را داشته باشد:

* هنگامی که فقط `succeededIndexes` را مشخص می‌کنید، به محض موفقیت همهٔ اندیس‌های مشخص‌شده در `succeededIndexes`، کنترل‌کنندهٔ Job آن Job را موفق علامت‌گذاری می‌کند. مقدار `succeededIndexes` باید فهرستی از بازه‌ها بین ۰ و `.spec.completions-1` باشد.
* هنگامی که فقط `succeededCount` را مشخص می‌کنید، به محض اینکه تعداد اندیس‌های موفق به `succeededCount` برسد، کنترل‌کنندهٔ Job آن Job را موفق علامت‌گذاری می‌کند.
* هنگامی که هر دو فیلد `succeededIndexes` و `succeededCount` را مشخص می‌کنید، به محض اینکه تعداد اندیس‌های موفق از زیرمجموعهٔ اندیس‌های مشخص‌شده در `succeededIndexes` به `succeededCount` برسد، کنترل‌کنندهٔ Job آن Job را موفق علامت‌گذاری می‌کند.

توجه داشته باشید که هنگامی که چند قاعده را در `.spec.successPolicy.rules` مشخص می‌کنید، کنترل‌کنندهٔ Job قواعد را به ترتیب ارزیابی می‌کند. به محض اینکه Job یک قاعده را برآورده کند، کنترل‌کنندهٔ Job قواعد باقی‌مانده را نادیده می‌گیرد.

در ادامه، مانیفست یک Job دارای `successPolicy` آمده است:

{{% code_sample file="/controllers/job-success-policy.yaml" %}}

در نمونهٔ بالا، هر دو فیلد `succeededIndexes` و `succeededCount` مشخص شده‌اند. بنابراین، هنگامی که هر یک از اندیس‌های مشخص‌شده، یعنی ۰، ۲ یا ۳، موفق شود، کنترل‌کنندهٔ Job آن Job را موفق علامت‌گذاری می‌کند و Podهای باقی‌مانده را خاتمه می‌دهد. Jobی که سیاست موفقیت را برآورده کند، شرط `SuccessCriteriaMet` را با دلیل `SuccessPolicy` دریافت می‌کند. پس از صدور دستور حذف Podهای باقی‌مانده، Job شرط `Complete` را دریافت می‌کند.

توجه داشته باشید که مقدار `succeededIndexes` به‌صورت بازه‌هایی نمایش داده می‌شود که با خط تیره از هم جدا شده‌اند. هر بازه با نخستین و آخرین عضو دنباله نمایش داده می‌شود که با خط تیره از هم جدا شده‌اند.

{{< note >}}
هنگامی که هم یک سیاست موفقیت و هم برخی سیاست‌های خاتمه مانند `.spec.backoffLimit` و `.spec.podFailurePolicy` را مشخص می‌کنید، به محض اینکه Job هر یک از این سیاست‌ها را برآورده کند، کنترل‌کنندهٔ Job سیاست خاتمه را رعایت می‌کند و سیاست موفقیت را نادیده می‌گیرد.
{{< /note >}}

## خاتمه و پاک‌سازی Job

وقتی یک Job کامل می‌شود، Pod جدیدی ایجاد نمی‌شود، اما Podهای موجود نیز [معمولاً](#pod-backoff-failure-policy) حذف نمی‌شوند. با نگه‌داشتن این Podها همچنان می‌توانید لاگ‌های Podهای کامل‌شده را ببینید و خطاها، هشدارها یا دیگر خروجی‌های عیب‌یابی را بررسی کنید. آبجکت Job نیز پس از کامل شدن باقی می‌ماند تا بتوانید وضعیت آن را مشاهده کنید. حذف Jobهای قدیمی پس از بررسی وضعیتشان بر عهدهٔ کاربر است. برای حذف Job از `kubectl` استفاده کنید (برای مثال `kubectl delete jobs/pi` یا `kubectl delete -f ./job.yaml`). وقتی Job را با `kubectl` حذف می‌کنید، همهٔ Podهایی که ایجاد کرده است نیز حذف می‌شوند.

به‌طور پیش‌فرض، یک Job بدون وقفه اجرا می‌شود، مگر اینکه یک Pod شکست بخورد (`restartPolicy=Never`) یا یک کانتینر با خطا خارج شود (`restartPolicy=OnFailure`). در این حالت، Job از مقدار `.spec.backoffLimit` که پیش‌تر توضیح داده شد پیروی می‌کند. وقتی به `.spec.backoffLimit` برسد، Job شکست‌خورده علامت‌گذاری می‌شود و همهٔ Podهای در حال اجرا خاتمه می‌یابند.

راه دیگر برای خاتمه دادن به یک Job، تعیین یک مهلت فعال (active deadline) است. برای این کار، فیلد `.spec.activeDeadlineSeconds` در Job را برابر تعدادی ثانیه قرار دهید. مقدار `activeDeadlineSeconds` بر کل مدت اجرای Job اعمال می‌شود، صرف‌نظر از اینکه چند Pod ایجاد شده باشد. وقتی Job به `activeDeadlineSeconds` برسد، همهٔ Podهای در حال اجرای آن خاتمه می‌یابند و وضعیت Job به `type: Failed` با `reason: DeadlineExceeded` تغییر می‌کند.

توجه کنید که `.spec.activeDeadlineSeconds` یک Job بر `.spec.backoffLimit` آن اولویت دارد. بنابراین، Jobی که در حال تلاش مجدد برای یک یا چند Pod شکست‌خورده است، پس از رسیدن به محدودیت زمانی تعیین‌شده در `activeDeadlineSeconds` دیگر Pod جدیدی مستقر نمی‌کند، حتی اگر هنوز به `backoffLimit` نرسیده باشد.

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

توجه کنید که هم مشخصات Job و هم [مشخصات قالب Pod](/docs/concepts/workloads/pods/init-containers/#detailed-behavior) درون Job، هر دو فیلدی به نام `activeDeadlineSeconds` دارند. مطمئن شوید که این فیلد را در سطح درست تنظیم می‌کنید.

به خاطر داشته باشید که `restartPolicy` بر Pod اعمال می‌شود و نه بر خود Job؛ یعنی وقتی وضعیت Job به `type: Failed` برسد، Job به‌طور خودکار دوباره راه‌اندازی نمی‌شود. به بیان دیگر، سازوکارهای خاتمهٔ Job که با `.spec.activeDeadlineSeconds` و `.spec.backoffLimit` فعال می‌شوند، به شکست دائمی Job می‌انجامند که رفع آن به مداخلهٔ دستی نیاز دارد.

### شرایط پایانی Job

هر Job دو حالت پایانی ممکن دارد که هر کدام با یک شرط (condition) متناظر در Job مشخص می‌شود:
* موفق (Succeeded): شرط `Complete` در Job
* شکست‌خورده (Failed): شرط `Failed` در Job

یک Job به دلایل زیر شکست می‌خورد:
- تعداد شکست‌های Pod از مقدار `.spec.backoffLimit` تعیین‌شده در مشخصات Job فراتر رفته است. برای جزئیات، به [سیاست شکست backoff برای Pod](#pod-backoff-failure-policy) مراجعه کنید.
- زمان اجرای Job از مقدار تعیین‌شدهٔ `.spec.activeDeadlineSeconds` فراتر رفته است.
- یک Job اندیس‌دار که از `.spec.backoffLimitPerIndex` استفاده کرده، اندیس‌های شکست‌خورده دارد. برای جزئیات، به [محدودیت backoff برای هر اندیس](#backoff-limit-per-index) مراجعه کنید.
- تعداد اندیس‌های شکست‌خورده در Job از مقدار تعیین‌شدهٔ `spec.maxFailedIndexes` فراتر رفته است. برای جزئیات، به [محدودیت backoff برای هر اندیس](#backoff-limit-per-index) مراجعه کنید.
- یک Pod شکست‌خورده با قاعده‌ای در `.spec.podFailurePolicy` که کنش `FailJob` دارد مطابقت می‌کند. برای جزئیات اینکه قواعد سیاست شکست Pod چگونه ممکن است بر ارزیابی شکست اثر بگذارند، به [سیاست شکست Pod](#pod-failure-policy) مراجعه کنید.

یک Job به دلایل زیر موفق می‌شود:
- تعداد Podهای موفق به مقدار تعیین‌شدهٔ `.spec.completions` رسیده است.
- معیارهای تعیین‌شده در `.spec.successPolicy` برآورده شده‌اند. برای جزئیات، به [سیاست موفقیت](#success-policy) مراجعه کنید.

در کوبرنتیز نسخهٔ 1.31 و بعد از آن، کنترل‌کنندهٔ Job افزودن شرایط پایانی، یعنی `Failed` یا `Complete`، را تا زمانی که همهٔ Podهای Job خاتمه یابند به تأخیر می‌اندازد.

در کوبرنتیز نسخهٔ 1.30 و پیش از آن، کنترل‌کنندهٔ Job شرط پایانی `Complete` یا `Failed` را بلافاصله پس از آغاز فرایند خاتمهٔ Job و حذف همهٔ finalizerهای Pod اضافه می‌کرد. با این حال، در لحظهٔ افزودن شرط پایانی، برخی Podها هنوز در حال اجرا یا در حال خاتمه بودند.

در کوبرنتیز نسخهٔ 1.31 و بعد از آن، کنترل‌کننده شرایط پایانی Job را تنها _پس از_ خاتمهٔ همهٔ Podها اضافه می‌کند. می‌توانید این رفتار را با [feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/) `JobManagedBy` و `JobPodReplacementPolicy` (که هر دو به‌طور پیش‌فرض فعال‌اند) کنترل کنید.

### خاتمهٔ Podهای Job

پس از آنکه Job معیارهای موفقیت یا شکست را برآورده کرد، کنترل‌کنندهٔ Job شرط `FailureTarget` یا شرط `SuccessCriteriaMet` را به Job اضافه می‌کند تا خاتمهٔ Podها را آغاز کند.

عواملی مانند `terminationGracePeriodSeconds` ممکن است فاصلهٔ زمانی میان لحظه‌ای که کنترل‌کنندهٔ Job شرط `FailureTarget` یا `SuccessCriteriaMet` را اضافه می‌کند تا لحظه‌ای که همهٔ Podهای Job خاتمه می‌یابند و کنترل‌کنندهٔ Job یک [شرط پایانی](#terminal-job-conditions) (`Failed` یا `Complete`) اضافه می‌کند را افزایش دهند.

می‌توانید از شرط `FailureTarget` یا `SuccessCriteriaMet` استفاده کنید تا بدون انتظار برای افزودن شرط پایانی توسط کنترل‌کننده، شکست یا موفقیت Job را ارزیابی کنید.

برای مثال، ممکن است بخواهید تصمیم بگیرید چه زمانی یک Job جایگزین برای Job شکست‌خورده ایجاد کنید. اگر Job شکست‌خورده را همزمان با ظاهر شدن شرط `FailureTarget` جایگزین کنید، Job جایگزین زودتر اجرا می‌شود، اما ممکن است Podهای Job شکست‌خورده و Job جایگزین همزمان اجرا شوند و منابع محاسباتی اضافی مصرف کنند.

در مقابل، اگر ظرفیت منابع کلاستر شما محدود است، می‌توانید صبر کنید تا شرط `Failed` روی Job ظاهر شود. این کار Job جایگزین را به تأخیر می‌اندازد، اما با انتظار تا حذف همهٔ Podهای شکست‌خورده، در مصرف منابع صرفه‌جویی می‌شود.

## پاک‌سازی خودکار Jobهای پایان‌یافته

معمولاً Jobهای پایان‌یافته دیگر در سیستم مورد نیاز نیستند. نگه‌داشتن آن‌ها در سیستم بار اضافی بر سرور API وارد می‌کند. اگر Jobها مستقیماً با یک کنترل‌کنندهٔ سطح بالاتر مانند [CronJobها](/docs/concepts/workloads/controllers/cron-jobs/) مدیریت شوند، CronJobها می‌توانند Jobها را بر اساس سیاست پاک‌سازی مبتنی بر ظرفیتِ تعیین‌شده پاک کنند.

### سازوکار TTL برای Jobهای پایان‌یافته

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

راه دیگر برای پاک‌سازی خودکار Jobهای پایان‌یافته (چه `Complete` و چه `Failed`)، استفاده از سازوکار TTL است که [کنترل‌کنندهٔ TTL](/docs/concepts/workloads/controllers/ttlafterfinished/) برای منابع پایان‌یافته فراهم می‌کند. برای این کار، فیلد `.spec.ttlSecondsAfterFinished` را در Job تعیین کنید.

وقتی کنترل‌کنندهٔ TTL یک Job را پاک‌سازی می‌کند، آن را به‌صورت آبشاری حذف می‌کند؛ یعنی آبجکت‌های وابسته به آن، مانند Podها، را همراه با Job حذف می‌کند. توجه کنید که هنگام حذف Job، تضمین‌های چرخهٔ عمر آن، مانند finalizerها، رعایت می‌شوند.

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

Job با نام `pi-with-ttl`، `100` ثانیه پس از پایان یافتن، واجد شرایط حذف خودکار می‌شود.

اگر این فیلد روی `0` تنظیم شود، Job بلافاصله پس از پایان یافتن واجد شرایط حذف خودکار می‌شود. اگر این فیلد تنظیم نشده باشد، کنترل‌کنندهٔ TTL این Job را پس از پایان یافتن پاک‌سازی نمی‌کند.

{{< note >}}
توصیه می‌شود فیلد `ttlSecondsAfterFinished` را تنظیم کنید، زیرا Jobهای مدیریت‌نشده (Jobهایی که مستقیماً ایجاد کرده‌اید و نه به‌طور غیرمستقیم از طریق دیگر APIهای بار کاری مانند CronJob) سیاست حذف پیش‌فرض `orphanDependents` دارند. در نتیجه، Podهایی که یک Job مدیریت‌نشده ایجاد کرده است، پس از حذف کامل آن Job باقی می‌مانند.
اگرچه {{< glossary_tooltip text="control plane" term_id="control-plane" >}} سرانجام Podهای یک Job حذف‌شده را پس از شکست یا کامل شدن [جمع‌آوری زباله](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection) می‌کند، گاهی این Podهای باقی‌مانده ممکن است باعث افت کارایی کلاستر شوند یا در بدترین حالت، به دلیل همین افت کارایی، کلاستر را از دسترس خارج کنند.

می‌توانید از [LimitRangeها](/docs/concepts/policy/limit-range/) و [ResourceQuotaها](/docs/concepts/policy/resource-quotas/) استفاده کنید تا برای میزان منابعی که یک فضای نام (namespace) مشخص می‌تواند مصرف کند سقفی تعیین کنید.
{{< /note >}}

## الگوهای Job

از آبجکت Job می‌توان برای پردازش مجموعه‌ای از *آیتم‌های کاری* مستقل اما مرتبط استفاده کرد. این آیتم‌ها ممکن است ایمیل‌هایی برای ارسال، فریم‌هایی برای رندر، فایل‌هایی برای تبدیل قالب (transcode)، بازه‌هایی از کلیدها در یک پایگاه دادهٔ NoSQL برای پیمایش و مانند آن باشند.

در یک سیستم پیچیده ممکن است چندین مجموعهٔ متفاوت از آیتم‌های کاری وجود داشته باشد. در اینجا فقط یک مجموعه از آیتم‌های کاری را در نظر می‌گیریم که کاربر می‌خواهد آن‌ها را با هم مدیریت کند؛ یعنی یک *کار دسته‌ای* (batch job).

چند الگوی متفاوت برای محاسبات موازی وجود دارد که هر کدام نقاط قوت و ضعف خود را دارند. موازنه‌ها (tradeoffs) عبارت‌اند از:

- یک آبجکت Job برای هر آیتم کاری، در برابر یک آبجکت Job واحد برای همهٔ آیتم‌های کاری. داشتن یک Job برای هر آیتم کاری، سربار مدیریت تعداد زیادی آبجکت Job را بر کاربر و سیستم تحمیل می‌کند. برای تعداد زیاد آیتم‌ها، یک Job واحد برای همهٔ آیتم‌های کاری بهتر است.
- برابر بودن تعداد Podهای ایجادشده با تعداد آیتم‌های کاری، در برابر اینکه هر Pod بتواند چند آیتم کاری را پردازش کند. وقتی تعداد Podها با تعداد آیتم‌های کاری برابر است، معمولاً Podها به تغییرات کمتری در کد و کانتینرهای موجود نیاز دارند. برای تعداد زیاد آیتم‌ها، اینکه هر Pod چند آیتم کاری را پردازش کند بهتر است.
- چند رویکرد از یک صف کاری استفاده می‌کنند. این کار به اجرای یک سرویس صف و ایجاد تغییراتی در برنامه یا کانتینر موجود برای استفاده از صف کاری نیاز دارد. سازگار کردن رویکردهای دیگر با یک برنامهٔ کانتینری‌شدهٔ موجود آسان‌تر است.
- وقتی Job با یک [Service بدون سر (headless)](/docs/concepts/services-networking/service/#headless-services) مرتبط باشد، می‌توانید امکان ارتباط Podهای درون Job با یکدیگر را فراهم کنید تا در یک محاسبه همکاری کنند.

این موازنه‌ها در جدول زیر خلاصه شده‌اند؛ ستون‌های ۲ تا ۴ با موازنه‌های بالا متناظرند. نام الگوها پیوندهایی به مثال‌ها و توضیحات مفصل‌تر نیز هستند.

|                  الگو                        | آبجکت Job واحد | Podهای کمتر از آیتم‌های کاری؟ | استفاده از برنامه بدون تغییر؟ |
| ----------------------------------------------- |:-----------------:|:---------------------------:|:-------------------:|
| [صف با یک Pod برای هر آیتم کاری][Queue with Pod Per Work Item]                  |         ✓         |                             |      گاهی      |
| [صف با تعداد متغیر Pod][Queue with Variable Pod Count]                 |         ✓         |             ✓               |                     |
| [Job اندیس‌دار با تخصیص ایستای کار][Indexed Job with Static Work Assignment]       |         ✓         |                             |          ✓          |
| [Job با ارتباط Pod به Pod][Job with Pod-to-Pod Communication]             |         ✓         |         گاهی           |      گاهی      |
| [بسط قالب Job][Job Template Expansion]                        |                   |                             |          ✓          |

وقتی تعداد تکمیل‌ها را با `.spec.completions` تعیین می‌کنید، هر Podی که کنترل‌کنندهٔ Job ایجاد می‌کند [`spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) یکسانی دارد. یعنی همهٔ Podهای یک وظیفه خط فرمان یکسان، ایمیج یکسان، حجم‌های (volume) یکسان و متغیرهای محیطی (تقریباً) یکسانی خواهند داشت. این الگوها روش‌های مختلفی هستند برای اینکه Podها روی کارهای متفاوت کار کنند.

جدول زیر تنظیمات لازم برای `.spec.parallelism` و `.spec.completions` را برای هر یک از الگوها نشان می‌دهد. در اینجا، `W` تعداد آیتم‌های کاری است.

|             الگو                             | `.spec.completions` |  `.spec.parallelism` |
| ----------------------------------------------- |:-------------------:|:--------------------:|
| [صف با یک Pod برای هر آیتم کاری][Queue with Pod Per Work Item]                  |          W          |        هر مقدار           |
| [صف با تعداد متغیر Pod][Queue with Variable Pod Count]                 |         null        |        هر مقدار           |
| [Job اندیس‌دار با تخصیص ایستای کار][Indexed Job with Static Work Assignment]       |          W          |        هر مقدار           |
| [Job با ارتباط Pod به Pod][Job with Pod-to-Pod Communication]             |          W          |         W            |
| [بسط قالب Job][Job Template Expansion]                        |          1          |     باید 1 باشد      |



## استفادهٔ پیشرفته

### تعلیق یک Job

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

وقتی یک Job ایجاد می‌شود، کنترل‌کنندهٔ Job بلافاصله ایجاد Podها را برای برآوردن نیازهای Job آغاز می‌کند و تا کامل شدن Job به این کار ادامه می‌دهد. با این حال، ممکن است بخواهید اجرای یک Job را موقتاً معلق کنید و بعداً از سر بگیرید، یا Jobها را در حالت معلق آغاز کنید و تصمیم دربارهٔ زمان شروع آن‌ها را بعداً به یک کنترل‌کنندهٔ سفارشی بسپارید.

برای تعلیق یک Job، می‌توانید فیلد `.spec.suspend` آن را به true تغییر دهید و بعداً، هر وقت خواستید آن را از سر بگیرید، مقدار آن را به false برگردانید. اگر Job را با مقدار true برای `.spec.suspend` ایجاد کنید، Job در حالت معلق ایجاد می‌شود.

در کوبرنتیز نسخهٔ 1.35 یا بعد از آن، اگر feature gate با نام [MutableSchedulingDirectivesForSuspendedJobs](#mutable-scheduling-directives-for-suspended-jobs) فعال باشد، فیلد `.status.startTime` هنگام تعلیق Job پاک می‌شود.

وقتی یک Job از حالت تعلیق خارج می‌شود، فیلد `.status.startTime` آن به زمان فعلی بازنشانی می‌شود. یعنی زمان‌سنج `.spec.activeDeadlineSeconds` هنگام تعلیق و ازسرگیری Job متوقف و بازنشانی می‌شود.

وقتی یک Job را معلق می‌کنید، همهٔ Podهای در حال اجرا که وضعیت `Completed` ندارند، با سیگنال SIGTERM [خاتمه می‌یابند](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination). دورهٔ خاتمهٔ آرام (graceful termination) Pod رعایت می‌شود و Pod شما باید در این دوره این سیگنال را مدیریت کند. این کار ممکن است شامل ذخیرهٔ پیشرفت کار برای ادامه در آینده یا بازگرداندن تغییرات باشد. Podهایی که به این شکل خاتمه می‌یابند، در شمارش `completions` در Job محاسبه نمی‌شوند.

تعریف یک Job نمونه در حالت معلق می‌تواند به این شکل باشد:

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

همچنین می‌توانید با patch کردن Job از طریق خط فرمان، وضعیت تعلیق آن را تغییر دهید.

معلق کردن یک Job فعال:

```shell
kubectl patch job/myjob --type=strategic --patch '{"spec":{"suspend":true}}'
```

ازسرگیری یک Job معلق:

```shell
kubectl patch job/myjob --type=strategic --patch '{"spec":{"suspend":false}}'
```

با استفاده از وضعیت Job می‌توان تعیین کرد که آیا Job معلق است یا در گذشته معلق شده است:

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

وجود شرطی از نوع "Suspended" با وضعیت "True" در Job به این معناست که Job معلق است؛ از فیلد `lastTransitionTime` می‌توان برای تعیین مدت زمان تعلیق Job استفاده کرد. اگر وضعیت این شرط "False" باشد، Job قبلاً معلق بوده و اکنون در حال اجراست. اگر چنین شرطی در وضعیت Job وجود نداشته باشد، Job هرگز متوقف نشده است.

هنگام تعلیق و ازسرگیری Job، رویدادهایی نیز ایجاد می‌شوند:

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

چهار رویداد آخر، به‌ویژه رویدادهای "Suspended" و "Resumed"، نتیجهٔ مستقیم تغییر فیلد `.spec.suspend` هستند. همان‌طور که می‌بینیم، در فاصلهٔ میان این دو رویداد هیچ Podی ایجاد نشده است، اما به محض ازسرگیری Job، ایجاد Podها دوباره آغاز شده است.

### دستورالعمل‌های زمان‌بندی قابل‌تغییر

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

در بیشتر موارد، یک Job موازی می‌خواهد Podهایش با محدودیت‌هایی اجرا شوند؛ مثلاً همه در یک zone، یا همه یا روی مدل GPU x یا روی مدل y، اما نه ترکیبی از هر دو.

فیلد [suspend](#suspending-a-job) نخستین گام برای دستیابی به این رفتار است. تعلیق به یک کنترل‌کنندهٔ صف سفارشی امکان می‌دهد تصمیم بگیرد یک Job چه زمانی شروع شود؛ اما وقتی Job از حالت تعلیق خارج شد، کنترل‌کنندهٔ صف سفارشی هیچ تأثیری بر اینکه Podهای Job در عمل روی کدام نودها قرار می‌گیرند ندارد.

این قابلیت امکان به‌روزرسانی دستورالعمل‌های زمان‌بندی یک Job را پیش از شروع آن فراهم می‌کند. با این کار، کنترل‌کننده‌های صف سفارشی می‌توانند بر محل قرارگیری Podها اثر بگذارند و در عین حال، تخصیص واقعی Pod به نود را به kube-scheduler بسپارند.

فیلدهایی از قالب Pod در Job که می‌توان آن‌ها را به‌روزرسانی کرد عبارت‌اند از: node affinity، انتخابگر (selector) نود، tolerationها، برچسب‌ها، حاشیه‌نویسی‌ها (annotation) و [دروازه‌های زمان‌بندی](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/).

#### دستورالعمل‌های زمان‌بندی قابل‌تغییر برای Jobهای معلق

{{< feature-state feature_gate_name="MutableSchedulingDirectivesForSuspendedJobs" >}}

در کوبرنتیز نسخهٔ 1.34 یا پیش از آن، تغییر دستورالعمل‌های زمان‌بندی Pod فقط برای Jobهای معلقی مجاز است که پیش‌تر هرگز از حالت تعلیق خارج نشده‌اند. در کوبرنتیز نسخهٔ 1.35، اگر feature gate با نام `MutableSchedulingDirectivesForSuspendedJobs` فعال باشد، این کار برای همهٔ Jobهای معلق مجاز است.

افزون بر این، این feature gate پاک شدن فیلد `.status.startTime` را هنگام [تعلیق Job](#suspending-a-job) فعال می‌کند.

### منابع قابل‌تغییر Pod برای Jobهای معلق

{{< feature-state feature_gate_name="MutablePodResourcesForSuspendedJobs" >}}

مدیر کلاستر می‌تواند در کوبرنتیز کنترل‌های پذیرش (admission control) تعریف کند تا درخواست‌ها (requests) یا محدودیت‌های (limits) منابع یک Job را بر اساس قواعد سیاستی تغییر دهد.

با این قابلیت، کوبرنتیز به شما نیز اجازه می‌دهد قالب Pod یک [Job معلق](#suspending-a-job) را تغییر دهید تا نیازمندی‌های منابع Podهای آن Job عوض شود.
این قابلیت با _تغییر اندازهٔ درجای Pod_ (in-place Pod resize) تفاوت دارد؛ آن قابلیت امکان به‌روزرسانی منابع Podهایی را فراهم می‌کند که از قبل در حال اجرا هستند، آن هم هر بار برای یک Pod.

کلاینتی که درخواست‌ها یا محدودیت‌های جدید منابع را تنظیم می‌کند می‌تواند با کلاینتی که Job را در ابتدا ایجاد کرده متفاوت باشد و لازم نیست مدیر کلاستر باشد.

### تعیین انتخابگر Pod دلخواه

معمولاً هنگام ایجاد یک آبجکت Job، فیلد `.spec.selector` را تعیین نمی‌کنید.
منطق مقداردهی پیش‌فرض سیستم این فیلد را هنگام ایجاد Job اضافه می‌کند.
این منطق مقداری برای انتخابگر (selector) برمی‌گزیند که با هیچ Job دیگری هم‌پوشانی نداشته باشد.

با این حال، ممکن است در برخی موارد لازم باشد این انتخابگرِ خودکار را بازنویسی کنید.
برای این کار می‌توانید `.spec.selector` را در Job تعیین کنید.

در انجام این کار بسیار محتاط باشید. اگر انتخابگر برچسبی تعیین کنید که مختص Podهای همان Job نباشد و با Podهای نامرتبط نیز مطابقت داشته باشد، ممکن است Podهای Job نامرتبط حذف شوند، یا این Job، Podهای دیگر را جزو تکمیل‌کنندگان خود به شمار آورد، یا یکی از Jobها یا هر دو از ایجاد Pod یا اجرا تا پایان سر باز بزنند. اگر انتخابگری غیریکتا انتخاب شود، کنترل‌کننده‌های دیگر (مثلاً ReplicationController) و Podهای آن‌ها نیز ممکن است رفتاری پیش‌بینی‌ناپذیر داشته باشند. کوبرنتیز هنگام تعیین `.spec.selector` جلوی اشتباه شما را نمی‌گیرد.

در ادامه نمونه‌ای از موقعیتی آمده است که ممکن است بخواهید از این قابلیت استفاده کنید.

فرض کنید Job با نام `old` از قبل در حال اجراست. می‌خواهید Podهای موجود به اجرای خود ادامه دهند، اما بقیهٔ Podهایی که ایجاد می‌شوند از قالب Pod دیگری استفاده کنند و Job نیز نام جدیدی داشته باشد.
نمی‌توانید Job را به‌روزرسانی کنید، زیرا این فیلدها قابل‌به‌روزرسانی نیستند.
بنابراین Job با نام `old` را با دستور `kubectl delete jobs/old --cascade=orphan` حذف می‌کنید، اما _Podهای آن را در حال اجرا نگه می‌دارید_.
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

سپس Job جدیدی با نام `new` ایجاد می‌کنید و همان انتخابگر را به‌صراحت در آن تعیین می‌کنید.
از آنجا که Podهای موجود برچسب `batch.kubernetes.io/controller-uid=a8f3d00d-c6d2-11e5-9f87-42010af00002` را دارند، Job با نام `new` نیز آن‌ها را کنترل می‌کند.

باید در Job جدید مقدار `manualSelector: true` را تعیین کنید، زیرا از انتخابگری که سیستم معمولاً به‌طور خودکار برایتان تولید می‌کند استفاده نمی‌کنید.

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

خود Job جدید uid متفاوتی با `a8f3d00d-c6d2-11e5-9f87-42010af00002` خواهد داشت. با تنظیم `manualSelector: true` به سیستم اعلام می‌کنید که می‌دانید چه می‌کنید و این ناهمخوانی باید مجاز شمرده شود.

### ردیابی Job با finalizerها

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

control plane، Podهای متعلق به هر Job را ردیابی می‌کند و متوجه می‌شود که آیا چنین Podای از API server حذف شده است یا نه. برای این کار، کنترل‌کنندهٔ Job، Podها را با finalizer `batch.kubernetes.io/job-tracking` ایجاد می‌کند. کنترل‌کننده تنها پس از آنکه Pod در وضعیت Job به حساب آمد، finalizer را حذف می‌کند و از آن پس کنترل‌کننده‌های دیگر یا کاربران می‌توانند Pod را حذف کنند.

{{< note >}}
اگر مشاهده کردید که Podهای یک Job با finalizer ردیابی گیر کرده‌اند، به [Pod من در وضعیت terminating باقی می‌ماند](/docs/tasks/debug/debug-application/debug-pods/) مراجعه کنید.
{{< /note >}}

### Jobهای Indexed کشسان {#elastic-indexed-jobs}

{{< feature-state feature_gate_name="ElasticIndexedJob" >}}

می‌توانید با تغییر هم‌زمان `.spec.parallelism` و `.spec.completions`، به‌گونه‌ای که `.spec.parallelism == .spec.completions` برقرار باشد، مقیاس Jobهای Indexed را افزایش یا کاهش دهید.
هنگام کاهش مقیاس، کوبرنتیز Podهایی را که اندیس بالاتری دارند حذف می‌کند.

از موارد کاربرد Jobهای Indexed کشسان می‌توان به بارهای کاری دسته‌ای (batch) اشاره کرد که به تغییر مقیاس یک Job Indexed نیاز دارند، مانند Jobهای آموزشی MPI، Horovod، Ray و PyTorch.

{{< note >}}
وقتی feature gate [`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/) فعال باشد و یک Job از [زمان‌بندی گروهی (gang scheduling)](#integrate-with-workload-apis) استفاده کند، اندازهٔ گروه از مقدار قابل‌تغییر `schedulingPolicy.gang.minCount` (یا در صورت تنظیم‌نشدن `minCount`، از `.spec.parallelism`) پیروی می‌کند.
مقیاس گروه را به یکی از دو روش زیر می‌توانید تغییر دهید:

- تنظیم مستقیم `.spec.scheduling.schedulingPolicy.gang.minCount`، یا
- تغییر `.spec.parallelism` در صورتی که `minCount` تنظیم نشده باشد.

با هر یک از این تغییرات، کنترل‌کننده `Workload` را دوباره کامپایل می‌کند و اندازهٔ `PodGroup` را دوباره همگام‌سازی می‌کند و بدین ترتیب مقیاس گروه را بدون ایجاد دوبارهٔ Job، درجا تغییر می‌دهد. به‌روزرسانی‌ها فقط بر Podهایی اعمال می‌شوند که در چرخه‌های زمان‌بندی آینده ارزیابی شوند و بر Podهایی که از قبل زمان‌بندی شده‌اند اثری ندارند. مقدار `gang.minCount` بزرگ‌تر از `.spec.parallelism` پذیرفته نمی‌شود، زیرا چنین گروهی هرگز برآورده نخواهد شد.
{{< /note >}}

### ایجاد با تأخیر Podهای جایگزین {#pod-replacement-policy}

{{< feature-state feature_gate_name="JobPodReplacementPolicy" >}}

به‌طور پیش‌فرض، کنترل‌کنندهٔ Job به‌محض اینکه Podها شکست بخورند یا در حال خاتمه باشند (مُهر زمانی حذف داشته باشند)، آن‌ها را دوباره ایجاد می‌کند.
این یعنی در یک لحظهٔ مشخص، وقتی برخی از Podها در حال خاتمه هستند، تعداد Podهای در حال اجرای یک Job ممکن است از `parallelism` بیشتر شود یا (اگر از Job Indexed استفاده می‌کنید) از یک Pod به ازای هر اندیس فراتر رود.

می‌توانید تصمیم بگیرید Podهای جایگزین فقط زمانی ایجاد شوند که Pod در حال خاتمه کاملاً به وضعیت پایانی رسیده باشد (`status.phase: Failed` داشته باشد).
برای این کار، `.spec.podReplacementPolicy: Failed` را تنظیم کنید.
سیاست جایگزینی پیش‌فرض به این بستگی دارد که آیا `podFailurePolicy` برای Job تنظیم شده است یا نه.
اگر هیچ سیاست شکست Pod برای Job تعریف نشده باشد، حذف فیلد `podReplacementPolicy` سیاست جایگزینی `TerminatingOrFailed` را برمی‌گزیند؛ در این حالت control plane بلافاصله پس از حذف Pod، Podهای جایگزین را ایجاد می‌کند (به‌محض اینکه control plane ببیند فیلد `deletionTimestamp` برای یکی از Podهای این Job تنظیم شده است).
برای Jobهایی که سیاست شکست Pod دارند، مقدار پیش‌فرض `podReplacementPolicy` برابر `Failed` است و هیچ مقدار دیگری مجاز نیست.
برای آشنایی بیشتر با سیاست‌های شکست Pod برای Jobها، به [سیاست شکست Pod](#pod-failure-policy) مراجعه کنید.

```yaml
kind: Job
metadata:
  name: new
  ...
spec:
  podReplacementPolicy: Failed
  ...
```

به شرط آنکه این feature gate در کلاستر شما فعال باشد، می‌توانید فیلد `.status.terminating` یک Job را بررسی کنید.
مقدار این فیلد برابر تعداد Podهای متعلق به Job است که در حال حاضر در حال خاتمه هستند.

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

### واگذاری مدیریت آبجکت Job به کنترل‌کنندهٔ خارجی

{{< feature-state feature_gate_name="JobManagedBy" >}}

این قابلیت به شما امکان می‌دهد کنترل‌کنندهٔ داخلی Job را برای یک Job مشخص غیرفعال کنید و هماهنگ‌سازی (reconciliation) آن Job را به یک کنترل‌کنندهٔ خارجی بسپارید.

کنترل‌کننده‌ای را که Job را هماهنگ می‌کند، با تنظیم یک مقدار سفارشی برای فیلد `spec.managedBy` مشخص می‌کنید؛ این مقدار می‌تواند هر چیزی جز `kubernetes.io/job-controller` باشد. مقدار این فیلد تغییرناپذیر است.

{{< note >}}
هنگام استفاده از این قابلیت، مطمئن شوید کنترل‌کننده‌ای که این فیلد به آن اشاره می‌کند نصب شده باشد؛ در غیر این صورت ممکن است Job اصلاً هماهنگ نشود.
{{< /note >}}

{{< note >}}
هنگام توسعهٔ یک کنترل‌کنندهٔ خارجی Job، توجه داشته باشید که کنترل‌کنندهٔ شما باید مطابق با تعاریف فیلدهای spec و status آبجکت Job در API عمل کند.

لطفاً این تعاریف را با جزئیات در [API مربوط به Job](/docs/reference/kubernetes-api/workload-resources/job-v1/) بررسی کنید.
همچنین توصیه می‌کنیم برای راستی‌آزمایی پیاده‌سازی خود، آزمون‌های انطباق e2e مربوط به آبجکت Job را اجرا کنید.

در پایان، هنگام توسعهٔ یک کنترل‌کنندهٔ خارجی Job، مطمئن شوید که از finalizer `batch.kubernetes.io/job-tracking` استفاده نمی‌کند؛ این finalizer برای کنترل‌کنندهٔ داخلی رزرو شده است.
{{< /note >}}

## جایگزین‌ها

### Podهای مستقل

وقتی نودی که یک Pod روی آن اجرا می‌شود راه‌اندازی مجدد شود یا از کار بیفتد، آن Pod خاتمه می‌یابد و دوباره راه‌اندازی نمی‌شود. اما یک Job برای جایگزینی Podهای خاتمه‌یافته، Podهای جدید ایجاد می‌کند.
به همین دلیل توصیه می‌کنیم به‌جای Pod مستقل از Job استفاده کنید، حتی اگر برنامهٔ شما فقط به یک Pod نیاز داشته باشد.

### Replication Controller

Jobها مکمل [Replication Controllerها](/docs/concepts/workloads/controllers/replicationcontroller/) هستند.
یک Replication Controller، Podهایی را مدیریت می‌کند که انتظار نمی‌رود خاتمه یابند (مثلاً وب‌سرورها)، و یک Job، Podهایی را مدیریت می‌کند که انتظار می‌رود خاتمه یابند (مثلاً وظایف دسته‌ای).

همان‌طور که در [چرخهٔ عمر Pod](/docs/concepts/workloads/pods/pod-lifecycle/) توضیح داده شد، `Job` *فقط* برای Podهایی مناسب است که `RestartPolicy` آن‌ها برابر `OnFailure` یا `Never` باشد.

{{< note >}}
اگر `RestartPolicy` تنظیم نشده باشد، مقدار پیش‌فرض آن `Always` است.
{{< /note >}}

### Job واحد که Pod کنترل‌کننده را راه‌اندازی می‌کند

الگوی دیگر این است که یک Job واحد، Podای ایجاد کند که آن Pod سپس Podهای دیگری ایجاد می‌کند و در نقش نوعی کنترل‌کنندهٔ سفارشی برای آن Podها عمل می‌کند. این روش بیشترین انعطاف‌پذیری را فراهم می‌کند، اما شروع کار با آن ممکن است تا حدی پیچیده باشد و یکپارچگی کمتری با کوبرنتیز دارد.

یکی از مزایای این رویکرد این است که کل فرایند از تضمین تکمیلِ آبجکت Job برخوردار می‌شود، در حالی که کنترل کامل بر اینکه چه Podهایی ایجاد شوند و کار چگونه میان آن‌ها تقسیم شود همچنان حفظ می‌شود.

## {{% heading "whatsnext" %}}

* با [Podها](/docs/concepts/workloads/pods) آشنا شوید.
* دربارهٔ روش‌های مختلف اجرای Jobها بخوانید:
  * [پردازش موازی درشت‌دانه با استفاده از صف کار](/docs/tasks/job/coarse-parallel-processing-work-queue/)
  * [پردازش موازی ریزدانه با استفاده از صف کار](/docs/tasks/job/fine-parallel-processing-work-queue/)
  * از یک [Job Indexed برای پردازش موازی با تخصیص ایستای کار](/docs/tasks/job/indexed-parallel-processing-static/) استفاده کنید
  * چند Job را بر اساس یک قالب ایجاد کنید: [پردازش موازی با استفاده از بسط قالب](/docs/tasks/job/parallel-processing-expansion/)
* برای آشنایی بیشتر با نحوهٔ پاک‌سازی وظایف تکمیل‌شده و/یا شکست‌خورده در کلاستر، پیوندهای موجود در بخش [پاک‌سازی خودکار Jobهای پایان‌یافته](#clean-up-finished-jobs-automatically) را دنبال کنید.
* `Job` بخشی از REST API کوبرنتیز است.
  برای درک API مربوط به Jobها، تعریف آبجکت {{< api-reference page="batch/job-v1" >}} را بخوانید.
* دربارهٔ [`CronJob`](/docs/concepts/workloads/controllers/cron-jobs/) بخوانید؛ با آن می‌توانید مجموعه‌ای از Jobها را تعریف کنید که بر اساس یک زمان‌بندی، مشابه ابزار `cron` در UNIX، اجرا می‌شوند.
* با کمک [مثال‌های](/docs/tasks/job/pod-failure-policy/) گام‌به‌گام، پیکربندی نحوهٔ رسیدگی به شکست‌های قابل‌تکرار و غیرقابل‌تکرار Pod را با استفاده از `podFailurePolicy` تمرین کنید.
* با [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) برای زمان‌بندی همه‌یا‌هیچ Jobهای موازی آشنا شوید.

[Indexed Job with Static Work Assignment]: /docs/tasks/job/indexed-parallel-processing-static/
[Job Template Expansion]: /docs/tasks/job/parallel-processing-expansion/
[Job with Pod-to-Pod Communication]: /docs/tasks/job/job-with-pod-to-pod-communication/
[Queue with Pod Per Work Item]: /docs/tasks/job/coarse-parallel-processing-work-queue/
[Queue with Variable Pod Count]: /docs/tasks/job/fine-parallel-processing-work-queue/

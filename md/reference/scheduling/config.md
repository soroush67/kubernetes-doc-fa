---
title: پیکربندی زمان‌بند
content_type: concept
weight: 20
---

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

با نوشتن یک فایل پیکربندی و ارسال مسیر آن به‌عنوان آرگومان خط فرمان، می‌توانید رفتار `kube-scheduler` را سفارشی کنید.

<!-- overview -->

<!-- body -->

با یک پروفایل زمان‌بندی (scheduling profile) می‌توانید مراحل مختلف زمان‌بندی را در {{< glossary_tooltip text="kube-scheduler" term_id="kube-scheduler" >}} پیکربندی کنید. هر مرحله در قالب یک نقطهٔ توسعه (extension point) در دسترس قرار می‌گیرد. افزونه‌ها (plugins) با پیاده‌سازی یک یا چند نقطه از این نقاط توسعه، رفتارهای زمان‌بندی را فراهم می‌کنند.

برای تعیین پروفایل‌های زمان‌بندی می‌توانید دستور `kube-scheduler --config <filename>` را اجرا کنید و از ساختار KubeSchedulerConfiguration نسخهٔ [v1](/docs/reference/config-api/kube-scheduler-config.v1/) بهره بگیرید.

یک پیکربندی حداقلی به شکل زیر است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
clientConnection:
  kubeconfig: /etc/srv/kubernetes/kube-scheduler/kubeconfig
```

{{< note >}}
نسخهٔ v1beta3 از KubeSchedulerConfiguration در v1.26 منسوخ شده و در v1.29 حذف شده است. لطفاً KubeSchedulerConfiguration را به نسخهٔ [v1](/docs/reference/config-api/kube-scheduler-config.v1/) مهاجرت دهید.
{{< /note >}}

## پروفایل‌ها

با یک پروفایل زمان‌بندی می‌توانید مراحل مختلف زمان‌بندی را در {{< glossary_tooltip text="kube-scheduler" term_id="kube-scheduler" >}} پیکربندی کنید. هر مرحله در قالب یک [نقطهٔ توسعه](#extension-points) در دسترس قرار می‌گیرد. [افزونه‌ها](#scheduling-plugins) با پیاده‌سازی یک یا چند نقطه از این نقاط توسعه، رفتارهای زمان‌بندی را فراهم می‌کنند.

می‌توانید یک نمونه از `kube-scheduler` را طوری پیکربندی کنید که [چند پروفایل](#multiple-profiles) را اجرا کند.

### نقاط توسعه

زمان‌بندی در مجموعه‌ای از مراحل انجام می‌شود که از طریق نقاط توسعهٔ زیر در دسترس هستند:

1. نقطهٔ `queueSort`: این افزونه‌ها تابعی برای تعیین ترتیب فراهم می‌کنند که برای مرتب‌سازی Podهای در انتظار در صف زمان‌بندی به کار می‌رود. در هر زمان دقیقاً یک افزونهٔ مرتب‌سازی صف می‌تواند فعال باشد.
1. نقطهٔ `placementGenerate`: این افزونه‌ها جایگذاری‌های ممکن (مجموعه‌هایی از نودها) را تولید می‌کنند که PodGroup موردنظر می‌تواند در آن‌ها زمان‌بندی شود. این نقطهٔ توسعه فقط در زمان‌بندی PodGroup کاربرد دارد و برای استفاده از آن باید زمان‌بندی Workload فعال باشد.
1. نقطهٔ `placementScore`: این افزونه‌ها به جایگذاری‌های پیشنهادی `placementGenerate` امتیاز می‌دهند تا بهترین جایگذاری برای PodGroup موردنظر انتخاب شود.
1. نقطهٔ `preFilter`: این افزونه‌ها پیش از فیلترکردن، اطلاعات مربوط به یک Pod یا کلاستر را پیش‌پردازش یا بررسی می‌کنند. این افزونه‌ها می‌توانند یک Pod را غیرقابل‌زمان‌بندی علامت‌گذاری کنند.
1. نقطهٔ `filter`: این افزونه‌ها معادل Predicates در Policy زمان‌بندی هستند و نودهایی را که نمی‌توانند Pod را اجرا کنند کنار می‌گذارند. فیلترها به ترتیب پیکربندی‌شده فراخوانی می‌شوند. اگر هیچ نودی از همهٔ فیلترها عبور نکند، Pod غیرقابل‌زمان‌بندی علامت‌گذاری می‌شود.
1. نقطهٔ `postFilter`: اگر هیچ نود مناسبی برای Pod پیدا نشود، این افزونه‌ها به ترتیب پیکربندی‌شده فراخوانی می‌شوند. اگر هر یک از افزونه‌های `postFilter` آن Pod را _قابل‌زمان‌بندی_ علامت‌گذاری کند، افزونه‌های باقی‌مانده فراخوانی نمی‌شوند. این افزونه‌ها برای Podهایی که در چارچوب زمان‌بندی PodGroup زمان‌بندی می‌شوند کاربرد ندارند.
1. نقطهٔ `podGroupPostFilter`: اگر هیچ جایگذاری مناسبی برای گروه Pod پیدا نشود، این افزونه‌ها به ترتیب پیکربندی‌شده فراخوانی می‌شوند. اگر هر یک از افزونه‌های `podGroupPostFilter` گروه Pod را _قابل‌زمان‌بندی_ علامت‌گذاری کند، افزونه‌های باقی‌مانده فراخوانی نمی‌شوند. این نقطهٔ توسعه فقط در زمان‌بندی PodGroup کاربرد دارد و برای استفاده از آن باید زمان‌بندی Workload فعال باشد.
1. نقطهٔ `preScore`: این نقطهٔ توسعه جنبهٔ اطلاع‌رسانی دارد و می‌توان از آن برای انجام کارهای پیش از امتیازدهی استفاده کرد.
1. نقطهٔ `score`: این افزونه‌ها به هر نودی که از مرحلهٔ فیلترکردن گذشته باشد امتیاز می‌دهند. سپس زمان‌بند نودی را انتخاب می‌کند که بیشترین مجموع وزن‌دار امتیازها را داشته باشد.
1. نقطهٔ `reserve`: این نقطهٔ توسعه جنبهٔ اطلاع‌رسانی دارد و هنگامی که منابع برای یک Pod مشخص رزرو شده باشند، افزونه‌ها را آگاه می‌کند. افزونه‌ها فراخوانی `Unreserve` را نیز پیاده‌سازی می‌کنند که در صورت بروز خطا در حین `Reserve` یا پس از آن اجرا می‌شود.
1. نقطهٔ `permit`: این افزونه‌ها می‌توانند از اتصال (binding) یک Pod جلوگیری کنند یا آن را به تأخیر بیندازند.
1. نقطهٔ `preBind`: این افزونه‌ها هر کاری را که پیش از اتصال یک Pod لازم باشد انجام می‌دهند.
1. نقطهٔ `bind`: این افزونه‌ها یک Pod را به یک Node متصل می‌کنند. افزونه‌های `bind` به ترتیب فراخوانی می‌شوند و همین که یکی از آن‌ها اتصال را انجام دهد، از افزونه‌های باقی‌مانده صرف‌نظر می‌شود. وجود دست‌کم یک افزونهٔ bind الزامی است.
1. نقطهٔ `postBind`: این نقطهٔ توسعه جنبهٔ اطلاع‌رسانی دارد و پس از اتصال یک Pod فراخوانی می‌شود.
1. نقطهٔ `multiPoint`: این فیلد فقط در پیکربندی وجود دارد و با آن می‌توان افزونه‌ها را به‌طور هم‌زمان برای همهٔ نقاط توسعهٔ قابل‌اعمال آن‌ها فعال یا غیرفعال کرد.

برای هر نقطهٔ توسعه می‌توانید [افزونه‌های پیش‌فرض](#scheduling-plugins) مشخصی را غیرفعال کنید یا افزونه‌های خود را فعال کنید. برای مثال:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - plugins:
      score:
        disabled:
        - name: PodTopologySpread
        enabled:
        - name: MyCustomPluginA
          weight: 2
        - name: MyCustomPluginB
          weight: 1
```

برای غیرفعال‌کردن همهٔ افزونه‌های پیش‌فرض یک نقطهٔ توسعه، می‌توانید از `*` به‌عنوان نام در آرایهٔ disabled استفاده کنید. در صورت نیاز، از این روش برای تغییر ترتیب افزونه‌ها نیز می‌توان بهره گرفت.

### افزونه‌های زمان‌بندی

افزونه‌های زیر به‌طور پیش‌فرض فعال هستند و یک یا چند نقطه از این نقاط توسعه را پیاده‌سازی می‌کنند:

- افزونهٔ `ImageLocality`: نودهایی را ترجیح می‌دهد که ایمیج‌های کانتینری که Pod اجرا می‌کند از قبل روی آن‌ها موجود باشد.
  نقاط توسعه: `score`.
- افزونهٔ `TaintToleration`: [taintها و tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration/) را پیاده‌سازی می‌کند.
  نقاط توسعهٔ پیاده‌سازی‌شده: `filter`، `preScore`، `score`.
- افزونهٔ `NodeName`: بررسی می‌کند که نام نود در مشخصات Pod با نود فعلی مطابقت داشته باشد.
  نقاط توسعه: `filter`.
- افزونهٔ `NodePorts`: بررسی می‌کند که نود، پورت‌های آزاد برای پورت‌های درخواستی Pod داشته باشد.
  نقاط توسعه: `preFilter`، `filter`.
- افزونهٔ `NodeAffinity`: [انتخابگرهای (selector) نود](/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) و [وابستگی نود (node affinity)](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) را پیاده‌سازی می‌کند.
  نقاط توسعه: `filter`، `score`.
- افزونهٔ `PodTopologySpread`: [توزیع توپولوژیک Pod](/docs/concepts/scheduling-eviction/topology-spread-constraints/) را پیاده‌سازی می‌کند.
  نقاط توسعه: `preFilter`، `filter`، `preScore`، `score`.
- افزونهٔ `NodeUnschedulable`: نودهایی را که مقدار `.spec.unschedulable` آن‌ها true است کنار می‌گذارد.
  نقاط توسعه: `filter`.
- افزونهٔ `NodeResourcesFit`: در زمان‌بندی تک‌به‌تک Podها، بررسی می‌کند که نود همهٔ منابع درخواستی Pod را داشته باشد. امتیازدهی می‌تواند از یکی از سه راهبرد `LeastAllocated` (پیش‌فرض)، `MostAllocated` و `RequestedToCapacityRatio` استفاده کند.
  در زمان‌بندی PodGroup، میزان بهره‌برداری از منابع را در کل جایگذاری ارزیابی‌شده محاسبه می‌کند.
  در این حالت، امتیازدهی از راهبرد `MostAllocated` استفاده می‌کند.
  نقاط توسعه: `preFilter`، `filter`، `score`، `placementScore`.
- افزونهٔ `NodeResourcesBalancedAllocation`: نودهایی را ترجیح می‌دهد که در صورت زمان‌بندی Pod روی آن‌ها، مصرف منابعشان متوازن‌تر شود.
  نقاط توسعه: `score`.
- افزونهٔ `VolumeBinding`: بررسی می‌کند که نود {{< glossary_tooltip text="حجم‌های (volume)" term_id="volume" >}} درخواستی را داشته باشد یا بتواند آن‌ها را متصل کند.
  نقاط توسعه: `preFilter`، `filter`، `reserve`، `preBind`، `score`.
  {{< note >}}
  نقطهٔ توسعهٔ `score` زمانی فعال می‌شود که قابلیت `StorageCapacityScoring` فعال باشد. این نقطهٔ توسعه کوچک‌ترین PVهایی را که اندازهٔ حجم درخواستی در آن‌ها جا می‌شود در اولویت قرار می‌دهد.
  {{< /note >}}
- افزونهٔ `VolumeRestrictions`: بررسی می‌کند که حجم‌های متصل‌شده به نود، محدودیت‌های خاص ارائه‌دهندهٔ حجم را رعایت کنند.
  نقاط توسعه: `filter`.
- افزونهٔ `VolumeZone`: بررسی می‌کند که حجم‌های درخواستی، الزامات مربوط به zone خود را در صورت وجود برآورده کنند.
  نقاط توسعه: `filter`.
- افزونهٔ `NodeVolumeLimits`: بررسی می‌کند که محدودیت‌های حجم CSI برای نود قابل‌رعایت باشند. اگر هیچ درایور CSI روی نود نصب نشده باشد، این افزونه می‌تواند از قرارگرفتن Pod روی آن نود نیز جلوگیری کند؛ این قابلیت مستلزم فعال‌بودن feature gate با نام `VolumeLimitScaling` است. افزون بر این، cluster-autoscaler به کمک این افزونه می‌تواند تعداد نودهای لازم برای زمان‌بندی Podهای در انتظار دارای حجم‌های CSI قابل‌اتصال را دقیق محاسبه کند.
  نقاط توسعه: `filter`.
- افزونهٔ `EBSLimits`: بررسی می‌کند که محدودیت‌های حجم AWS EBS برای نود قابل‌رعایت باشند.
  نقاط توسعه: `filter`.
- افزونهٔ `GCEPDLimits`: بررسی می‌کند که محدودیت‌های حجم GCP-PD برای نود قابل‌رعایت باشند.
  نقاط توسعه: `filter`.
- افزونهٔ `AzureDiskLimits`: بررسی می‌کند که محدودیت‌های حجم دیسک Azure برای نود قابل‌رعایت باشند.
  نقاط توسعه: `filter`.
- افزونهٔ `InterPodAffinity`: [وابستگی و ضدوابستگی بین Podها](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) را پیاده‌سازی می‌کند.
  نقاط توسعه: `preFilter`، `filter`، `preScore`، `score`.
- افزونهٔ `PrioritySort`: مرتب‌سازی پیش‌فرض مبتنی بر اولویت را فراهم می‌کند.
  نقاط توسعه: `queueSort`.
- افزونهٔ `DefaultBinder`: سازوکار پیش‌فرض اتصال را فراهم می‌کند.
  نقاط توسعه: `bind`.
- افزونهٔ `DefaultPreemption`: سازوکار پیش‌فرض پس‌گیری منابع (preemption) را فراهم می‌کند.
  نقاط توسعه: `postFilter`، `podGroupPostFilter`.
- افزونهٔ `TopologyPlacement`: سازوکار پیش‌فرض تولید جایگذاری را برای محدودیت‌های توپولوژی PodGroup فراهم می‌کند.
  نقاط توسعه: `placementGenerate`.
- افزونهٔ `PodGroupPodsCount`: الگوریتم امتیازدهی جایگذاری را بر اساس تعداد Podهایی که می‌توانند در جایگذاری موردنظر زمان‌بندی شوند فراهم می‌کند.
  نقاط توسعه: `placementScore`.

افزونه‌های زیر به‌طور پیش‌فرض فعال نیستند، اما می‌توانید آن‌ها را از طریق APIهای پیکربندی مؤلفه فعال کنید:

- افزونهٔ `CinderLimits`: بررسی می‌کند که محدودیت‌های حجم [OpenStack Cinder](https://docs.openstack.org/cinder/) برای نود قابل‌رعایت باشند.
  نقاط توسعه: `filter`.

### چند پروفایل

می‌توانید `kube-scheduler` را طوری پیکربندی کنید که بیش از یک پروفایل را اجرا کند. هر پروفایل نام زمان‌بند مخصوص به خود را دارد و می‌تواند مجموعهٔ متفاوتی از افزونه‌ها را در [نقاط توسعهٔ](#extension-points) خود پیکربندی کند.

با پیکربندی نمونهٔ زیر، زمان‌بند با دو پروفایل اجرا می‌شود: یکی با افزونه‌های پیش‌فرض و دیگری با همهٔ افزونه‌های امتیازدهی در حالت غیرفعال.

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: default-scheduler
  - schedulerName: no-scoring-scheduler
    plugins:
      preScore:
        disabled:
        - name: '*'
      score:
        disabled:
        - name: '*'
```

هر Pod که باید بر اساس پروفایل مشخصی زمان‌بندی شود، می‌تواند نام زمان‌بند متناظر را در فیلد `.spec.schedulerName` خود قرار دهد.

به‌طور پیش‌فرض، یک پروفایل با نام زمان‌بند `default-scheduler` ایجاد می‌شود. این پروفایل شامل افزونه‌های پیش‌فرضی است که در بالا شرح داده شدند. هنگام تعریف بیش از یک پروفایل، هر پروفایل باید نام زمان‌بند یکتایی داشته باشد.

اگر Pod نام زمان‌بندی را مشخص نکند، kube-apiserver مقدار آن را `default-scheduler` قرار می‌دهد. بنابراین برای زمان‌بندی چنین Podهایی باید پروفایلی با این نام زمان‌بند وجود داشته باشد.

{{< note >}}
رویدادهای زمان‌بندی Pod مقدار `.spec.schedulerName` را به‌عنوان `reportingController` خود دارند. رویدادهای انتخاب رهبر از نام زمان‌بند نخستین پروفایل فهرست استفاده می‌کنند.

برای اطلاعات بیشتر، به بخش `reportingController` در [مرجع Event API](/docs/reference/kubernetes-api/cluster-resources/event-v1/) مراجعه کنید.
{{< /note >}}

{{< note >}}
همهٔ پروفایل‌ها باید در نقطهٔ توسعهٔ `queueSort` از افزونهٔ یکسانی استفاده کنند و پارامترهای پیکربندی یکسانی (در صورت وجود) داشته باشند، زیرا زمان‌بند فقط یک صف برای Podهای در انتظار دارد.
{{< /note >}}

### افزونه‌هایی که بر چند نقطهٔ توسعه اعمال می‌شوند {#multipoint}

از نسخهٔ `kubescheduler.config.k8s.io/v1beta3` به بعد، پیکربندی پروفایل فیلد دیگری با نام `multiPoint` دارد که با آن می‌توان یک افزونه را به‌آسانی در چند نقطهٔ توسعه فعال یا غیرفعال کرد. هدف از پیکربندی `multiPoint` ساده‌کردن تنظیماتی است که کاربران و مدیران هنگام استفاده از پروفایل‌های سفارشی به آن نیاز دارند.

افزونه‌ای با نام `MyPlugin` را در نظر بگیرید که نقاط توسعهٔ `preScore`، `score`، `preFilter` و `filter` را پیاده‌سازی می‌کند. برای فعال‌کردن `MyPlugin` در همهٔ نقاط توسعهٔ موجود آن، پیکربندی پروفایل به شکل زیر است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: multipoint-scheduler
    plugins:
      multiPoint:
        enabled:
        - name: MyPlugin
```

این پیکربندی معادل آن است که `MyPlugin` را به‌صورت دستی برای همهٔ نقاط توسعه‌اش فعال کنید:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: non-multipoint-scheduler
    plugins:
      preScore:
        enabled:
        - name: MyPlugin
      score:
        enabled:
        - name: MyPlugin
      preFilter:
        enabled:
        - name: MyPlugin
      filter:
        enabled:
        - name: MyPlugin
```

یکی از مزایای استفاده از `multiPoint` در اینجا آن است که اگر `MyPlugin` در آینده نقطهٔ توسعهٔ دیگری را پیاده‌سازی کند، پیکربندی `multiPoint` آن را به‌طور خودکار برای نقطهٔ توسعهٔ جدید نیز فعال می‌کند.

با استفاده از فیلد `disabled` هر نقطهٔ توسعه می‌توان آن نقطه را از گسترش `MultiPoint` مستثنا کرد. این روش برای غیرفعال‌کردن افزونه‌های پیش‌فرض و غیرپیش‌فرض کار می‌کند و با نویسهٔ عام (`'*'`) نیز می‌توان همهٔ افزونه‌ها را غیرفعال کرد. نمونه‌ای از این کار، با غیرفعال‌کردن `Score` و `PreScore`، به شکل زیر است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: non-multipoint-scheduler
    plugins:
      multiPoint:
        enabled:
        - name: 'MyPlugin'
      preScore:
        disabled:
        - name: '*'
      score:
        disabled:
        - name: '*'
```

از نسخهٔ `kubescheduler.config.k8s.io/v1beta3` به بعد، همهٔ [افزونه‌های پیش‌فرض](#scheduling-plugins) به‌صورت داخلی از طریق `MultiPoint` فعال می‌شوند. با این حال، نقاط توسعهٔ جداگانه همچنان در دسترس هستند تا بتوان مقادیر پیش‌فرض (مانند ترتیب و وزن‌های Score) را به‌صورت انعطاف‌پذیر بازپیکربندی کرد. برای مثال، دو افزونهٔ Score با نام‌های `DefaultScore1` و `DefaultScore2` را در نظر بگیرید که وزن هر یک `1` است. می‌توان ترتیب آن‌ها را با وزن‌های متفاوت به شکل زیر تغییر داد:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: multipoint-scheduler
    plugins:
      score:
        enabled:
        - name: 'DefaultScore2'
          weight: 5
```

در این مثال، نیازی به ذکر صریح افزونه‌ها در `MultiPoint` نیست، زیرا این‌ها افزونه‌های پیش‌فرض هستند. همچنین تنها افزونه‌ای که در `Score` مشخص شده `DefaultScore2` است، زیرا افزونه‌هایی که از طریق نقاط توسعهٔ مشخص تنظیم می‌شوند همیشه بر افزونه‌های `MultiPoint` اولویت دارند. بنابراین این قطعه در عمل ترتیب دو افزونه را تغییر می‌دهد، بی‌آنکه نیازی به ذکر هر دوی آن‌ها باشد.

سلسله‌مراتب کلی اولویت هنگام پیکربندی افزونه‌های `MultiPoint` به شرح زیر است:
1. نقاط توسعهٔ مشخص ابتدا اجرا می‌شوند و تنظیمات آن‌ها بر هر تنظیمی که در جای دیگر تعیین شده باشد غلبه می‌کند
2. افزونه‌هایی که به‌صورت دستی از طریق `MultiPoint` پیکربندی شده‌اند و تنظیمات آن‌ها
3. افزونه‌های پیش‌فرض و تنظیمات پیش‌فرض آن‌ها

برای نشان‌دادن سلسله‌مراتب بالا، مثال زیر بر پایهٔ این افزونه‌ها است:
| افزونه             | نقاط توسعه        |
| ------------------ | ----------------- |
| `DefaultQueueSort` | `QueueSort`       |
| `CustomQueueSort`  | `QueueSort`       |
| `DefaultPlugin1`   | `Score`, `Filter` |
| `DefaultPlugin2`   | `Score`           |
| `CustomPlugin1`    | `Score`, `Filter` |
| `CustomPlugin2`    | `Score`, `Filter` |

یک پیکربندی نمونهٔ معتبر برای این افزونه‌ها به شکل زیر است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: multipoint-scheduler
    plugins:
      multiPoint:
        enabled:
        - name: 'CustomQueueSort'
        - name: 'CustomPlugin1'
          weight: 3
        - name: 'CustomPlugin2'
        disabled:
        - name: 'DefaultQueueSort'
      filter:
        disabled:
        - name: 'DefaultPlugin1'
      score:
        enabled:
        - name: 'DefaultPlugin2'
```

توجه کنید که تعریف دوبارهٔ یک افزونهٔ `MultiPoint` در یک نقطهٔ توسعهٔ مشخص خطا ایجاد نمی‌کند. این تعریف دوباره نادیده گرفته می‌شود (و در لاگ ثبت می‌شود)، زیرا نقاط توسعهٔ مشخص اولویت دارند.

این نمونه علاوه بر نگه‌داشتن بیشتر پیکربندی در یک محل، چند کار دیگر نیز انجام می‌دهد:
* افزونهٔ سفارشی `queueSort` را فعال و افزونهٔ پیش‌فرض را غیرفعال می‌کند
* افزونه‌های `CustomPlugin1` و `CustomPlugin2` را فعال می‌کند که در همهٔ نقاط توسعهٔ خود ابتدا اجرا می‌شوند
* افزونهٔ `DefaultPlugin1` را فقط برای `filter` غیرفعال می‌کند
* ترتیب `DefaultPlugin2` را طوری تغییر می‌دهد که در `score` ابتدا اجرا شود (حتی پیش از افزونه‌های سفارشی)

در نسخه‌های پیکربندی پیش از `v1beta3`، که `multiPoint` وجود نداشت، قطعهٔ بالا معادل پیکربندی زیر است:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1beta2
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: multipoint-scheduler
    plugins:

      # Disable the default QueueSort plugin
      queueSort:
        enabled:
        - name: 'CustomQueueSort'
        disabled:
        - name: 'DefaultQueueSort'

      # Enable custom Filter plugins
      filter:
        enabled:
        - name: 'CustomPlugin1'
        - name: 'CustomPlugin2'
        disabled:
        - name: 'DefaultPlugin1'

      # Enable and reorder custom score plugins
      score:
        enabled:
        - name: 'DefaultPlugin2'
          weight: 1
        - name: 'DefaultPlugin1'
          weight: 1
        - name: 'CustomPlugin1'
          weight: 3
        - name: 'CustomPlugin2'
          weight: 1
```

این مثال پیچیده است، اما هم انعطاف‌پذیری پیکربندی `MultiPoint` را نشان می‌دهد و هم یکپارچگی روان آن را با روش‌های موجود برای پیکربندی نقاط توسعه.

## {{% heading "whatsnext" %}}

* [مرجع kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/) را بخوانید
* دربارهٔ [زمان‌بندی](/docs/concepts/scheduling-eviction/kube-scheduler/) بیاموزید
* مرجع [پیکربندی kube-scheduler (v1)](/docs/reference/config-api/kube-scheduler-config.v1/) را بخوانید

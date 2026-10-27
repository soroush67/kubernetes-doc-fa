---
reviewers:
- davidopp
- dom4ha
- kevin-wangzefeng
- macsko
- sanposhiho
title: اختصاص Podها به نودها
content_type: concept
weight: 20
---

<!-- overview -->

می‌توانید یک {{< glossary_tooltip text="Pod" term_id="pod" >}} را طوری محدود کنید که
تنها روی {{< glossary_tooltip text="نود(های)" term_id="node" >}} مشخصی _اجازهٔ_ اجرا داشته باشد،
یا اجرا روی نودهای مشخصی را _ترجیح_ دهد.
چند روش برای انجام این کار وجود دارد و همهٔ رویکردهای توصیه‌شده از
[انتخابگرهای برچسب (label selectors)](/docs/concepts/overview/working-with-objects/labels/) برای تسهیل انتخاب استفاده می‌کنند.
اغلب نیازی به تعیین چنین محدودیت‌هایی ندارید؛
{{< glossary_tooltip text="زمان‌بند" term_id="kube-scheduler" >}} به‌طور خودکار جای‌گذاری معقولی انجام می‌دهد
(برای مثال، Podهای شما را در میان نودها پخش می‌کند تا Podها را روی نودی که منابع آزاد کافی ندارد قرار ندهد).
با این حال، در برخی شرایط ممکن است بخواهید کنترل کنید که
Pod روی کدام نود مستقر شود؛ برای مثال، برای اطمینان از اینکه یک Pod در نهایت روی نودی قرار گیرد که یک SSD به آن متصل است،
یا برای قرار دادن Podهای دو سرویس متفاوت که ارتباط زیادی با هم دارند در یک ناحیهٔ دسترس‌پذیری (availability zone) یکسان.

<!-- body -->

می‌توانید از هر یک از روش‌های زیر برای انتخاب محلی که کوبرنتیز
Podهای مشخص را در آن زمان‌بندی می‌کند، استفاده کنید:

- فیلد [nodeSelector](#nodeselector) که با [برچسب‌های نود](#built-in-node-labels) تطبیق داده می‌شود
- [وابستگی و ضدوابستگی (Affinity and anti-affinity)](#affinity-and-anti-affinity)
- فیلد [nodeName](#nodename)
- [قیدهای پخش توپولوژی Pod](#pod-topology-spread-constraints)

## برچسب‌های نود {#built-in-node-labels}

مانند بسیاری دیگر از آبجکت‌های کوبرنتیز، نودها نیز
[برچسب](/docs/concepts/overview/working-with-objects/labels/) دارند. می‌توانید
[برچسب‌ها را به‌صورت دستی اضافه کنید](/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node).
کوبرنتیز همچنین یک [مجموعهٔ استاندارد از برچسب‌ها](/docs/reference/node/node-labels/)
را روی همهٔ نودهای کلاستر مقداردهی می‌کند.

{{<note>}}
مقدار این برچسب‌ها وابسته به ارائه‌دهندهٔ ابری است و قابل اتکا بودن آن تضمین نمی‌شود.
برای مثال، مقدار `kubernetes.io/hostname` ممکن است در برخی محیط‌ها با نام نود یکسان باشد
و در محیط‌های دیگر مقدار متفاوتی داشته باشد.
{{</note>}}

### ایزوله‌سازی/محدودسازی نود

افزودن برچسب به نودها به شما اجازه می‌دهد Podها را برای زمان‌بندی روی نودها یا
گروه‌هایی از نودهای مشخص هدف بگیرید. می‌توانید از این قابلیت برای اطمینان از اینکه Podهای
مشخص تنها روی نودهایی با ویژگی‌های ایزوله‌سازی، امنیتی یا مقرراتی معین اجرا شوند،
استفاده کنید.

اگر از برچسب‌ها برای ایزوله‌سازی نود استفاده می‌کنید، کلیدهای برچسبی را انتخاب کنید که {{<glossary_tooltip text="kubelet" term_id="kubelet">}}
نتواند آن‌ها را تغییر دهد. این کار از اینکه یک نود آسیب‌دیده (compromised) آن برچسب‌ها را روی
خودش تنظیم کند و زمان‌بند بارهای کاری را روی آن نود آسیب‌دیده زمان‌بندی کند، جلوگیری می‌کند.

[افزونهٔ پذیرش `NodeRestriction`](/docs/reference/access-authn-authz/admission-controllers/#noderestriction)
از تنظیم یا تغییر برچسب‌هایی که پیشوند
`node-restriction.kubernetes.io/` دارند توسط kubelet جلوگیری می‌کند.

برای استفاده از این پیشوند برچسب برای ایزوله‌سازی نود:

1. اطمینان حاصل کنید که از [Node authorizer](/docs/reference/access-authn-authz/node/) استفاده می‌کنید و افزونهٔ پذیرش `NodeRestriction` را _فعال_ کرده‌اید.
2. برچسب‌هایی با پیشوند `node-restriction.kubernetes.io/` به نودهای خود اضافه کنید و از آن برچسب‌ها در [انتخابگرهای نود](#nodeselector) خود استفاده کنید.
   برای مثال، `example.com.node-restriction.kubernetes.io/fips=true` یا `example.com.node-restriction.kubernetes.io/pci-dss=true`.

## nodeSelector

`nodeSelector` ساده‌ترین شکل توصیه‌شدهٔ قید انتخاب نود است.
می‌توانید فیلد `nodeSelector` را به مشخصات Pod خود اضافه کنید و
[برچسب‌های نودی](#built-in-node-labels) را که می‌خواهید نود مقصد داشته باشد، مشخص کنید.
کوبرنتیز Pod را تنها روی نودهایی زمان‌بندی می‌کند که همهٔ برچسب‌هایی را که
مشخص کرده‌اید، داشته باشند.

برای اطلاعات بیشتر، [اختصاص Podها به نودها](/docs/tasks/configure-pod-container/assign-pods-nodes) را
ببینید.

## وابستگی و ضدوابستگی (Affinity and anti-affinity)

`nodeSelector` ساده‌ترین راه برای محدود کردن Podها به نودهایی با برچسب‌های
مشخص است. وابستگی و ضدوابستگی انواع قیدهایی را که می‌توانید
تعریف کنید، گسترش می‌دهند. برخی از مزایای وابستگی و ضدوابستگی عبارت‌اند از:

- زبان وابستگی/ضدوابستگی بیانگرتر است. `nodeSelector` تنها
  نودهایی را انتخاب می‌کند که همهٔ برچسب‌های مشخص‌شده را داشته باشند. وابستگی/ضدوابستگی به شما
  کنترل بیشتری بر منطق انتخاب می‌دهد.
- می‌توانید مشخص کنید که یک قاعده *نرم* یا *ترجیحی* است، تا زمان‌بند
  حتی اگر نتواند نود منطبقی پیدا کند، همچنان Pod را زمان‌بندی کند.
- می‌توانید یک Pod را به‌جای استفادهٔ صرف از برچسب‌های نود، با استفاده از برچسب‌های Podهای دیگری که روی نود (یا دامنهٔ توپولوژیک دیگر) در حال اجرا هستند، محدود کنید،
  که به شما اجازه می‌دهد قواعدی تعریف کنید که مشخص می‌کنند کدام Podها
  می‌توانند در کنار هم روی یک نود قرار گیرند.

قابلیت وابستگی از دو نوع وابستگی تشکیل شده است:

- *وابستگی نود (Node affinity)* مانند فیلد `nodeSelector` عمل می‌کند، اما بیانگرتر است و
  به شما اجازه می‌دهد قواعد نرم تعریف کنید.
- *وابستگی/ضدوابستگی بین Podها (Inter-pod affinity/anti-affinity)* به شما اجازه می‌دهد Podها را بر اساس برچسب‌های
  Podهای دیگر محدود کنید.

### وابستگی نود

وابستگی نود از نظر مفهومی مشابه `nodeSelector` است و به شما اجازه می‌دهد محدود کنید که
Pod شما بر اساس برچسب‌های نود روی کدام نودها قابل زمان‌بندی باشد. دو نوع وابستگی
نود وجود دارد:

- `requiredDuringSchedulingIgnoredDuringExecution`: زمان‌بند نمی‌تواند
  Pod را زمان‌بندی کند، مگر اینکه قاعده برآورده شود. این نوع مانند `nodeSelector` عمل می‌کند،
  اما با نحوی (syntax) بیانگرتر.
- `preferredDuringSchedulingIgnoredDuringExecution`: زمان‌بند می‌کوشد
  نودی را بیابد که قاعده را برآورده کند. اگر نود منطبقی در دسترس نباشد،
  زمان‌بند همچنان Pod را زمان‌بندی می‌کند.

{{<note>}}
در انواع بالا، `IgnoredDuringExecution` به این معناست که اگر برچسب‌های نود
پس از زمان‌بندی Pod توسط کوبرنتیز تغییر کنند، Pod به اجرای خود ادامه می‌دهد.
{{</note>}}

می‌توانید وابستگی‌های نود را با استفاده از فیلد `.spec.affinity.nodeAffinity` در
مشخصات Pod خود تعیین کنید.

برای مثال، مشخصات Pod زیر را در نظر بگیرید:

{{% code_sample file="pods/pod-with-node-affinity.yaml" %}}

در این مثال، قواعد زیر اعمال می‌شوند:

- نود *باید* برچسبی با کلید `topology.kubernetes.io/zone` داشته باشد و
  مقدار آن برچسب *باید* یا `antarctica-east1` یا `antarctica-west1` باشد.
- *ترجیحاً* نود برچسبی با کلید `another-node-label-key` و
  مقدار `another-node-label-value` داشته باشد.

می‌توانید از فیلد `operator` برای تعیین یک عملگر منطقی استفاده کنید که کوبرنتیز هنگام
تفسیر قواعد از آن استفاده کند. می‌توانید از `In`، `NotIn`، `Exists`، `DoesNotExist`،
`Gt` و `Lt` استفاده کنید.

برای آگاهی بیشتر از نحوهٔ کار این عملگرها،
[عملگرها](#operators) را بخوانید.

`NotIn` و `DoesNotExist` به شما اجازه می‌دهند رفتار ضدوابستگی نود را تعریف کنید.
به‌عنوان راه دیگر، می‌توانید از [taintهای نود](/docs/concepts/scheduling-eviction/taint-and-toleration/)
برای دور نگه داشتن Podها از نودهای مشخص استفاده کنید.

{{<note>}}
اگر هم `nodeSelector` و هم `nodeAffinity` را مشخص کنید، برای زمان‌بندی Pod روی یک نود
*هر دو* باید برآورده شوند.

اگر چند عبارت (term) را در `nodeSelectorTerms` مرتبط با انواع `nodeAffinity`
مشخص کنید، Pod در صورتی می‌تواند روی یک نود زمان‌بندی شود که یکی از عبارت‌های مشخص‌شده
برآورده شود (عبارت‌ها با OR ترکیب می‌شوند).

اگر چند عبارت (expression) را در یک فیلد `matchExpressions` واحد مرتبط با یک
term در `nodeSelectorTerms` مشخص کنید، Pod تنها در صورتی می‌تواند روی یک نود زمان‌بندی شود
که همهٔ عبارت‌ها برآورده شوند (عبارت‌ها با AND ترکیب می‌شوند).
{{</note>}}

برای اطلاعات بیشتر، [اختصاص Podها به نودها با استفاده از وابستگی نود](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
را ببینید.

#### وزن وابستگی نود

می‌توانید برای هر نمونه از نوع وابستگی
`preferredDuringSchedulingIgnoredDuringExecution` یک `weight` بین ۱ و ۱۰۰ تعیین کنید. هنگامی که
زمان‌بند نودهایی را می‌یابد که همهٔ الزامات زمان‌بندی دیگر Pod را برآورده می‌کنند،
زمان‌بند روی هر قاعدهٔ ترجیحی که نود برآورده می‌کند پیمایش می‌کند و
مقدار `weight` آن عبارت را به یک مجموع اضافه می‌کند.

مجموع نهایی به امتیاز سایر توابع اولویت برای آن نود افزوده می‌شود.
هنگامی که زمان‌بند برای Pod تصمیم زمان‌بندی می‌گیرد، نودهایی که بالاترین امتیاز کل را دارند
در اولویت قرار می‌گیرند.

برای مثال، مشخصات Pod زیر را در نظر بگیرید:

{{% code_sample file="pods/pod-with-affinity-preferred-weight.yaml" %}}

اگر دو نود ممکن وجود داشته باشد که با قاعدهٔ
`preferredDuringSchedulingIgnoredDuringExecution` مطابقت کنند، یکی با برچسب
`label-1:key-1` و دیگری با برچسب `label-2:key-2`، زمان‌بند
`weight` هر نود را در نظر می‌گیرد و وزن را به سایر امتیازهای
آن نود اضافه می‌کند و Pod را روی نودی با بالاترین امتیاز نهایی زمان‌بندی می‌کند.

{{<note>}}
اگر می‌خواهید کوبرنتیز Podهای این مثال را با موفقیت زمان‌بندی کند،
باید نودهایی با برچسب `kubernetes.io/os=linux` در کلاستر داشته باشید.
{{</note>}}

#### وابستگی نود به‌ازای هر پروفایل زمان‌بندی

{{< feature-state for_k8s_version="v1.20" state="beta" >}}

هنگام پیکربندی چند [پروفایل زمان‌بندی](/docs/reference/scheduling/config/#multiple-profiles)، می‌توانید
یک پروفایل را با یک وابستگی نود مرتبط کنید؛ این کار زمانی مفید است که یک پروفایل تنها برای مجموعهٔ مشخصی از نودها اعمال شود.
برای این کار، یک `addedAffinity` به فیلد `args` مربوط به [افزونهٔ `NodeAffinity`](/docs/reference/scheduling/config/#scheduling-plugins)
در [پیکربندی زمان‌بند](/docs/reference/scheduling/config/) اضافه کنید. برای مثال:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration

profiles:
  - schedulerName: default-scheduler
  - schedulerName: foo-scheduler
    pluginConfig:
      - name: NodeAffinity
        args:
          addedAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: scheduler-profile
                  operator: In
                  values:
                  - foo
```

`addedAffinity` علاوه بر NodeAffinity مشخص‌شده در PodSpec، روی همهٔ Podهایی اعمال می‌شود که `.spec.schedulerName` را روی `foo-scheduler` تنظیم کرده‌اند.
یعنی برای تطابق با Pod، نودها باید هم `addedAffinity` و هم
`.spec.NodeAffinity` مربوط به Pod را برآورده کنند.

از آنجا که `addedAffinity` برای کاربران نهایی قابل مشاهده نیست، رفتار آن ممکن است
برایشان غیرمنتظره باشد. از برچسب‌های نودی استفاده کنید که ارتباط روشنی با
نام پروفایل زمان‌بند دارند.

{{< note >}}
کنترل‌کنندهٔ DaemonSet که [Podها را برای DaemonSetها ایجاد می‌کند](/docs/concepts/workloads/controllers/daemonset/#how-daemon-pods-are-scheduled)،
از پروفایل‌های زمان‌بندی پشتیبانی نمی‌کند. هنگامی که کنترل‌کنندهٔ DaemonSet
Podها را ایجاد می‌کند، زمان‌بند پیش‌فرض کوبرنتیز آن Podها را جای‌گذاری می‌کند و همهٔ
قواعد `nodeAffinity` موجود در کنترل‌کنندهٔ DaemonSet را رعایت می‌کند.
{{< /note >}}

### وابستگی و ضدوابستگی بین Podها

وابستگی و ضدوابستگی بین Podها به شما اجازه می‌دهند محدود کنید که Podهای شما
روی کدام نودها قابل زمان‌بندی باشند، آن هم بر اساس برچسب‌های Podهایی که از قبل روی آن
نود در حال اجرا هستند، به‌جای برچسب‌های نود.

#### انواع وابستگی و ضدوابستگی بین Podها

وابستگی و ضدوابستگی بین Podها به این شکل بیان می‌شوند: «این
Pod باید (یا در مورد ضدوابستگی، نباید) در X اجرا شود، اگر آن X
از قبل یک یا چند Pod را اجرا می‌کند که قاعدهٔ Y را برآورده می‌کنند»، که در آن X یک دامنهٔ
توپولوژی مانند نود، رک، ناحیه (zone) یا منطقهٔ (region) ارائه‌دهندهٔ ابری یا موارد مشابه است و Y
قاعده‌ای است که کوبرنتیز می‌کوشد آن را برآورده کند.

این قواعد (Y) را به‌صورت [انتخابگرهای برچسب](/docs/concepts/overview/working-with-objects/labels/#label-selectors)
همراه با فهرستی اختیاری از فضاهای نام مرتبط بیان می‌کنید. Podها در کوبرنتیز آبجکت‌هایی
وابسته به فضای نام هستند، بنابراین برچسب‌های Pod نیز به‌طور ضمنی فضای نام دارند. هر انتخابگر برچسب
برای برچسب‌های Pod باید فضاهای نامی را که کوبرنتیز باید در آن‌ها به دنبال آن
برچسب‌ها بگردد، مشخص کند.

دامنهٔ توپولوژی (X) را با استفاده از `topologyKey` بیان می‌کنید که کلید
برچسب نودی است که سیستم برای مشخص کردن دامنه از آن استفاده می‌کند. برای نمونه‌ها،
[برچسب‌ها، حاشیه‌نویسی‌ها و Taintهای شناخته‌شده](/docs/reference/labels-annotations-taints/) را ببینید.

{{< note >}}
وابستگی و ضدوابستگی بین Podها به پردازش قابل‌توجهی نیاز دارند
که می‌تواند زمان‌بندی را در کلاسترهای بزرگ به‌طور چشمگیری کند کند. ما
استفاده از آن‌ها را در کلاسترهای بزرگ‌تر از چند صد نود توصیه نمی‌کنیم.
{{</note>}}

{{< note >}}
ضدوابستگی Pod نیازمند آن است که نودها به‌طور یکنواخت برچسب‌گذاری شده باشند؛ به عبارت دیگر،
هر نود در کلاستر باید برچسب مناسبی منطبق با `topologyKey` داشته باشد.
اگر برخی یا همهٔ نودها برچسب `topologyKey` مشخص‌شده را نداشته باشند، ممکن است
به رفتار ناخواسته‌ای منجر شود.
{{</note>}}

مشابه [وابستگی نود](#node-affinity)، دو نوع وابستگی و
ضدوابستگی Pod به شرح زیر وجود دارد:

- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`

برای مثال، می‌توانید از وابستگی
`requiredDuringSchedulingIgnoredDuringExecution` استفاده کنید تا به زمان‌بند بگویید
Podهای دو سرویس را در یک ناحیهٔ ارائه‌دهندهٔ ابری یکسان قرار دهد، زیرا آن‌ها
ارتباط زیادی با یکدیگر دارند. به همین ترتیب، می‌توانید از ضدوابستگی
`preferredDuringSchedulingIgnoredDuringExecution` برای پخش کردن Podهای
یک سرویس در میان چند ناحیهٔ ارائه‌دهندهٔ ابری استفاده کنید.

برای استفاده از وابستگی بین Podها، از فیلد `affinity.podAffinity` در مشخصات Pod استفاده کنید.
برای ضدوابستگی بین Podها، از فیلد `affinity.podAntiAffinity` در مشخصات
Pod استفاده کنید.

#### رفتار زمان‌بندی

هنگام زمان‌بندی یک Pod جدید، زمان‌بند کوبرنتیز قواعد وابستگی/ضدوابستگی Pod را در بستر وضعیت فعلی کلاستر ارزیابی می‌کند:

1. قیدهای سخت (فیلتر کردن نودها):
   - `podAffinity.requiredDuringSchedulingIgnoredDuringExecution` و `podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution`:
     - زمان‌بند اطمینان حاصل می‌کند که Pod جدید به نودهایی اختصاص یابد که این قواعد الزامی وابستگی و ضدوابستگی را بر اساس Podهای موجود برآورده می‌کنند.

2. قیدهای نرم (امتیازدهی):
   - `podAffinity.preferredDuringSchedulingIgnoredDuringExecution` و `podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`:
     - زمان‌بند نودها را بر اساس میزان برآورده کردن این قواعد ترجیحی وابستگی و ضدوابستگی امتیاز می‌دهد تا جای‌گذاری Pod بهینه شود.

3. فیلدهای نادیده‌گرفته‌شده:
   - `podAffinity.preferredDuringSchedulingIgnoredDuringExecution` مربوط به Podهای موجود:
     - این قواعد ترجیحی وابستگی در تصمیم زمان‌بندی برای Podهای جدید در نظر گرفته نمی‌شوند.
   - `podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution` مربوط به Podهای موجود:
     - به همین ترتیب، قواعد ترجیحی ضدوابستگی Podهای موجود در طول زمان‌بندی نادیده گرفته می‌شوند.

#### زمان‌بندی گروهی از Podها با وابستگی بین Podها نسبت به خودشان

اگر Pod فعلی که در حال زمان‌بندی است، نخستین Pod از مجموعه‌ای باشد که نسبت به خودشان وابستگی دارند،
در صورتی که از همهٔ بررسی‌های وابستگی دیگر عبور کند، اجازهٔ زمان‌بندی دارد. این موضوع با
بررسی این موارد تعیین می‌شود: هیچ Pod دیگری در کلاستر با فضای نام و انتخابگر این Pod منطبق نباشد،
Pod با عبارت‌های خودش منطبق باشد، و نود انتخاب‌شده با همهٔ توپولوژی‌های درخواست‌شده منطبق باشد.
این کار تضمین می‌کند که حتی اگر همهٔ Podها وابستگی بین Podها را مشخص کرده باشند،
بن‌بست (deadlock) رخ ندهد.

#### مثال وابستگی Pod {#an-example-of-a-pod-that-uses-pod-affinity}

مشخصات Pod زیر را در نظر بگیرید:

{{% code_sample file="pods/pod-with-pod-affinity.yaml" %}}

این مثال یک قاعدهٔ وابستگی Pod و یک قاعدهٔ ضدوابستگی Pod تعریف می‌کند.
قاعدهٔ وابستگی Pod از نوع «سخت»
`requiredDuringSchedulingIgnoredDuringExecution` استفاده می‌کند، در حالی که قاعدهٔ ضدوابستگی
از نوع «نرم» `preferredDuringSchedulingIgnoredDuringExecution` استفاده می‌کند.

قاعدهٔ وابستگی مشخص می‌کند که زمان‌بند تنها در صورتی مجاز است Pod نمونه را
روی یک نود قرار دهد که آن نود به یک [ناحیهٔ](/docs/concepts/scheduling-eviction/topology-spread-constraints/) مشخص تعلق داشته باشد
که در آن Podهای دیگری با `security=S1` برچسب‌گذاری شده باشند.
برای نمونه، اگر کلاستری با یک ناحیهٔ تعیین‌شده داشته باشیم که آن را «Zone V» می‌نامیم
و از نودهایی با برچسب `topology.kubernetes.io/zone=V` تشکیل شده است، زمان‌بند می‌تواند
Pod را به هر نودی درون Zone V اختصاص دهد، به شرط آنکه دست‌کم یک Pod درون
Zone V از قبل برچسب `security=S1` داشته باشد. در مقابل، اگر هیچ Podی با برچسب‌های `security=S1`
در Zone V وجود نداشته باشد، زمان‌بند Pod نمونه را به هیچ نودی در آن ناحیه اختصاص نمی‌دهد.

قاعدهٔ ضدوابستگی مشخص می‌کند که زمان‌بند باید بکوشد از زمان‌بندی Pod
روی یک نود پرهیز کند، اگر آن نود به یک [ناحیهٔ](/docs/concepts/scheduling-eviction/topology-spread-constraints/) مشخص تعلق داشته باشد
که در آن Podهای دیگری با `security=S2` برچسب‌گذاری شده باشند.
برای نمونه، اگر کلاستری با یک ناحیهٔ تعیین‌شده داشته باشیم که آن را «Zone R» می‌نامیم
و از نودهایی با برچسب `topology.kubernetes.io/zone=R` تشکیل شده است، زمان‌بند باید از
اختصاص Pod به هر نودی درون Zone R پرهیز کند، به شرط آنکه دست‌کم یک Pod درون
Zone R از قبل برچسب `security=S2` داشته باشد. در مقابل، اگر هیچ Podی با برچسب‌های `security=S2` وجود نداشته باشد،
قاعدهٔ ضدوابستگی بر زمان‌بندی در Zone R اثری ندارد.

برای آشنایی بیشتر با نمونه‌های وابستگی و ضدوابستگی Pod،
به [پیشنهاد طراحی](https://git.k8s.io/design-proposals-archive/scheduling/podaffinity.md) مراجعه کنید.

می‌توانید از مقادیر `In`، `NotIn`، `Exists` و `DoesNotExist` در
فیلد `operator` برای وابستگی و ضدوابستگی Pod استفاده کنید.

برای آگاهی بیشتر از نحوهٔ کار این عملگرها،
[عملگرها](#operators) را بخوانید.

در اصل، `topologyKey` می‌تواند هر کلید برچسب مجازی باشد، به‌جز
استثناهای زیر که به دلایل کارایی و امنیتی وجود دارند:

- برای وابستگی و ضدوابستگی Pod، فیلد `topologyKey` خالی در هیچ‌یک از
  `requiredDuringSchedulingIgnoredDuringExecution`
  و `preferredDuringSchedulingIgnoredDuringExecution` مجاز نیست.
- برای قواعد ضدوابستگی Pod از نوع `requiredDuringSchedulingIgnoredDuringExecution`،
  کنترل‌کنندهٔ پذیرش `LimitPodHardAntiAffinityTopology`،
  `topologyKey` را به `kubernetes.io/hostname` محدود می‌کند. اگر می‌خواهید توپولوژی‌های سفارشی را مجاز کنید،
  می‌توانید این کنترل‌کنندهٔ پذیرش را تغییر دهید یا غیرفعال کنید.

علاوه بر `labelSelector` و `topologyKey`، می‌توانید به‌طور اختیاری فهرستی
از فضاهای نام را که `labelSelector` باید با آن‌ها تطبیق داده شود، با استفاده از
فیلد `namespaces` در همان سطح `labelSelector` و `topologyKey` مشخص کنید.
اگر `namespaces` حذف شود یا خالی باشد، مقدار پیش‌فرض آن فضای نام Podی است که
تعریف وابستگی/ضدوابستگی در آن آمده است.

#### انتخابگر فضای نام

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

همچنین می‌توانید فضاهای نام منطبق را با استفاده از `namespaceSelector` انتخاب کنید که یک پرس‌وجوی برچسب روی مجموعهٔ فضاهای نام است.
عبارت وابستگی روی فضاهای نامی اعمال می‌شود که هم توسط `namespaceSelector` و هم توسط فیلد `namespaces` انتخاب شده باشند.
توجه داشته باشید که یک `namespaceSelector` خالی ({}) با همهٔ فضاهای نام منطبق است، در حالی که یک فهرست `namespaces` تهی (null) یا خالی همراه با
`namespaceSelector` تهی، با فضای نام Podی منطبق است که قاعده در آن تعریف شده است.

#### matchLabelKeys

{{< feature-state feature_gate_name="MatchLabelKeysInPodAffinity" >}}

{{< note >}}
<!-- UPDATE THIS WHEN PROMOTING TO STABLE -->
فیلد `matchLabelKeys` یک فیلد در سطح بتا است و به‌طور پیش‌فرض در
کوبرنتیز {{< skew currentVersion >}} فعال است.
اگر بخواهید آن را غیرفعال کنید، باید این کار را به‌طور صریح از طریق
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `MatchLabelKeysInPodAffinity` انجام دهید.
{{< /note >}}

کوبرنتیز یک فیلد اختیاری `matchLabelKeys` برای وابستگی
یا ضدوابستگی Pod دارد. این فیلد کلیدهای برچسب‌هایی را مشخص می‌کند که هنگام برآورده کردن (ضد)وابستگی Pod
باید با برچسب‌های Pod ورودی منطبق باشند.

این کلیدها برای جست‌وجوی مقادیر در برچسب‌های Pod استفاده می‌شوند؛ آن برچسب‌های کلید-مقدار
(با استفاده از `AND`) با محدودیت‌های تطبیقی که با فیلد `labelSelector` تعریف شده‌اند ترکیب می‌شوند. فیلتر
ترکیبی، مجموعه‌ای از Podهای موجود را انتخاب می‌کند که در محاسبهٔ (ضد)وابستگی Pod در نظر گرفته می‌شوند.

{{< caution >}}
استفاده از `matchLabelKeys` با برچسب‌هایی که ممکن است مستقیماً روی Podها به‌روزرسانی شوند، توصیه نمی‌شود.
حتی اگر برچسب Pod را که در `matchLabelKeys` مشخص شده است **مستقیماً** ویرایش کنید (یعنی نه از طریق یک Deployment)،
kube-apiserver به‌روزرسانی برچسب را در `labelSelector` ادغام‌شده منعکس نمی‌کند.
{{< /caution >}}

یک مورد استفادهٔ رایج، استفاده از `matchLabelKeys` همراه با `pod-template-hash` است (که روی Podهایی تنظیم می‌شود
که به‌عنوان بخشی از یک Deployment مدیریت می‌شوند و مقدار آن برای هر نسخه (revision) یکتاست).
استفاده از `pod-template-hash` در `matchLabelKeys` به شما اجازه می‌دهد Podهایی را هدف بگیرید که
به همان نسخهٔ Pod ورودی تعلق دارند، تا ارتقای تدریجی (rolling upgrade) وابستگی را نشکند.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: application-server
...
spec:
  template:
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - database
            topologyKey: topology.kubernetes.io/zone
            # Only Pods from a given rollout are taken into consideration when calculating pod affinity.
            # If you update the Deployment, the replacement Pods follow their own affinity rules
            # (if there are any defined in the new Pod template)
            matchLabelKeys:
            - pod-template-hash
```

#### mismatchLabelKeys

{{< feature-state feature_gate_name="MatchLabelKeysInPodAffinity" >}}

{{< note >}}
<!-- UPDATE THIS WHEN PROMOTING TO STABLE -->
فیلد `mismatchLabelKeys` یک فیلد در سطح بتا است و به‌طور پیش‌فرض در
کوبرنتیز {{< skew currentVersion >}} فعال است.
اگر بخواهید آن را غیرفعال کنید، باید این کار را به‌طور صریح از طریق
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `MatchLabelKeysInPodAffinity` انجام دهید.
{{< /note >}}

کوبرنتیز یک فیلد اختیاری `mismatchLabelKeys` برای وابستگی
یا ضدوابستگی Pod دارد. این فیلد کلیدهای برچسب‌هایی را مشخص می‌کند که هنگام برآورده کردن (ضد)وابستگی Pod
نباید با برچسب‌های Pod ورودی منطبق باشند.

{{< caution >}}
استفاده از `mismatchLabelKeys` با برچسب‌هایی که ممکن است مستقیماً روی Podها به‌روزرسانی شوند، توصیه نمی‌شود.
حتی اگر برچسب Pod را که در `mismatchLabelKeys` مشخص شده است **مستقیماً** ویرایش کنید (یعنی نه از طریق یک Deployment)،
kube-apiserver به‌روزرسانی برچسب را در `labelSelector` ادغام‌شده منعکس نمی‌کند.
{{< /caution >}}

یک نمونه مورد استفاده، اطمینان از این است که Podها به دامنهٔ توپولوژی‌ای (نود، ناحیه و غیره) بروند که تنها Podهای متعلق به همان مستأجر (tenant) یا تیم در آن زمان‌بندی می‌شوند.
به عبارت دیگر، می‌خواهید از اجرای همزمان Podهای دو مستأجر متفاوت در یک دامنهٔ توپولوژی یکسان پرهیز کنید.

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    # Assume that all relevant Pods have a "tenant" label set
    tenant: tenant-a
...
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      # ensure that Pods associated with this tenant land on the correct node pool
      - matchLabelKeys:
          - tenant
        labelSelector: {}
        topologyKey: node-pool
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      # ensure that Pods associated with this tenant can't schedule to nodes used for another tenant
      - mismatchLabelKeys:
        - tenant # whatever the value of the "tenant" label for this Pod, prevent
                 # scheduling to nodes in any pool where any Pod from a different
                 # tenant is running.
        labelSelector:
          # We have to have the labelSelector which selects only Pods with the tenant label,
          # otherwise this Pod would have anti-affinity against Pods from daemonsets as well, for example,
          # which aren't supposed to have the tenant label.
          matchExpressions:
          - key: tenant
            operator: Exists
        topologyKey: node-pool
```

#### موارد استفادهٔ کاربردی‌تر

وابستگی و ضدوابستگی بین Podها هنگامی که همراه با مجموعه‌های سطح بالاتری
مانند ReplicaSetها، StatefulSetها، Deploymentها و غیره به کار روند، می‌توانند حتی مفیدتر باشند. این
قواعد به شما اجازه می‌دهند پیکربندی کنید که مجموعه‌ای از بارهای کاری باید
در یک توپولوژی تعریف‌شدهٔ یکسان در کنار هم قرار گیرند؛ برای مثال، ترجیح قرار دادن دو Pod
مرتبط روی یک نود یکسان.

برای مثال: کلاستری سه‌نودی را تصور کنید. از این کلاستر برای اجرای یک برنامهٔ وب
و همچنین یک حافظهٔ نهان درون‌حافظه‌ای (مانند Redis) استفاده می‌کنید. در این مثال، همچنین فرض کنید که تأخیر بین
برنامهٔ وب و حافظهٔ نهان باید تا حد امکان پایین باشد. می‌توانید از وابستگی و ضدوابستگی
بین Podها استفاده کنید تا سرورهای وب را تا حد امکان در کنار حافظهٔ نهان قرار دهید.

در Deployment نمونهٔ زیر برای حافظهٔ نهان Redis، replicaها برچسب `app=store` می‌گیرند. قاعدهٔ
`podAntiAffinity` به زمان‌بند می‌گوید از قرار دادن چند replica
با برچسب `app=store` روی یک نود واحد پرهیز کند. این کار هر حافظهٔ نهان را روی یک
نود جداگانه ایجاد می‌کند.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-cache
spec:
  selector:
    matchLabels:
      app: store
  replicas: 3
  template:
    metadata:
      labels:
        app: store
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - store
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: redis-server
        image: redis:3.2-alpine
```

Deployment نمونهٔ زیر برای سرورهای وب، replicaهایی با برچسب `app=web-store` ایجاد می‌کند.
قاعدهٔ وابستگی Pod به زمان‌بند می‌گوید هر replica را روی نودی قرار دهد که یک Pod
با برچسب `app=store` دارد. قاعدهٔ ضدوابستگی Pod به زمان‌بند می‌گوید هرگز
چند سرور `app=web-store` را روی یک نود واحد قرار ندهد.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-server
spec:
  selector:
    matchLabels:
      app: web-store
  replicas: 3
  template:
    metadata:
      labels:
        app: web-store
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - web-store
            topologyKey: "kubernetes.io/hostname"
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - store
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: web-app
        image: nginx:1.16-alpine
```

ایجاد دو Deployment بالا به چیدمان کلاستر زیر منجر می‌شود
که در آن هر سرور وب در کنار یک حافظهٔ نهان، روی سه نود جداگانه قرار دارد.

|    node-1     |    node-2     |    node-3     |
| :-----------: | :-----------: | :-----------: |
| *webserver-1* | *webserver-2* | *webserver-3* |
|   *cache-1*   |   *cache-2*   |   *cache-3*   |

اثر کلی این است که احتمالاً هر نمونهٔ حافظهٔ نهان توسط یک کلاینت واحد که
روی همان نود در حال اجراست، مورد دسترسی قرار می‌گیرد. هدف این رویکرد به حداقل رساندن هم ناهمگونی (skew، یعنی بار نامتوازن) و هم تأخیر است.

ممکن است دلایل دیگری برای استفاده از ضدوابستگی Pod داشته باشید.
برای نمونه‌ای از یک StatefulSet که با ضدوابستگی برای دسترس‌پذیری بالا
پیکربندی شده و از همان تکنیک این مثال استفاده می‌کند،
[آموزش ZooKeeper](/docs/tutorials/stateful-application/zookeeper/#tolerating-node-failure) را ببینید.

## nodeName

`nodeName` شکل مستقیم‌تری از انتخاب نود نسبت به وابستگی یا
`nodeSelector` است. `nodeName` فیلدی در مشخصات Pod است. اگر فیلد `nodeName`
خالی نباشد، زمان‌بند Pod را نادیده می‌گیرد و kubelet روی نود نام‌برده‌شده
می‌کوشد Pod را روی آن نود قرار دهد. استفاده از `nodeName` بر استفاده از
`nodeSelector` یا قواعد وابستگی و ضدوابستگی ارجحیت دارد.

برخی از محدودیت‌های استفاده از `nodeName` برای انتخاب نودها عبارت‌اند از:

- اگر نود نام‌برده‌شده وجود نداشته باشد، Pod اجرا نمی‌شود و در
  برخی موارد ممکن است به‌طور خودکار حذف شود.
- اگر نود نام‌برده‌شده منابع کافی برای جای دادن
  Pod نداشته باشد، Pod با شکست مواجه می‌شود و دلیل آن مشخص می‌کند چرا؛
  برای مثال OutOfmemory یا OutOfcpu.
- نام نودها در محیط‌های ابری همیشه قابل پیش‌بینی یا پایدار نیستند.

{{< warning >}}
`nodeName` برای استفاده توسط زمان‌بندهای سفارشی یا موارد استفادهٔ پیشرفته‌ای در نظر گرفته شده است که
در آن‌ها باید هرگونه زمان‌بند پیکربندی‌شده را دور بزنید. دور زدن زمان‌بندها ممکن است
در صورتی که نودهای اختصاص‌یافته بیش از ظرفیت بارگذاری شوند، به Podهای ناموفق منجر شود. می‌توانید از [وابستگی نود](#node-affinity)
یا [فیلد `nodeSelector`](#nodeselector) برای اختصاص یک Pod به یک نود مشخص بدون دور زدن زمان‌بندها استفاده کنید.
{{</ warning >}}

در اینجا نمونه‌ای از مشخصات Pod با استفاده از فیلد `nodeName` آمده است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01
```

Pod بالا تنها روی نود `kube-01` اجرا می‌شود.

## nominatedNodeName

{{< feature-state feature_gate_name="NominatedNodeNameForExpectation" >}}

اجزای خارجی می‌توانند از `nominatedNodeName` برای نامزد کردن یک نود برای یک Pod در انتظار (pending) استفاده کنند.
این نامزدسازی به شیوهٔ بهترین تلاش است: اگر زمان‌بند تشخیص دهد که Pod نمی‌تواند به نود نامزدشده برود، ممکن است نادیده گرفته شود.

همچنین، این فیلد ممکن است توسط زمان‌بند نوشته (یا بازنویسی) شود:
- اگر زمان‌بند از طریق پس‌گیری (preemption) نودی برای نامزد کردن بیابد.
- اگر زمان‌بند تصمیم بگیرد Pod به کجا می‌رود و آن را به چرخهٔ اتصال (binding cycle) منتقل کند.
  - توجه داشته باشید که در این حالت، `nominatedNodeName` تنها زمانی تنظیم می‌شود که Pod باید از نقاط توسعهٔ `WaitOnPermit` یا `PreBind` عبور کند.

در اینجا نمونه‌ای از وضعیت یک Pod با استفاده از فیلد `nominatedNodeName` آمده است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
...
status:
  nominatedNodeName: kube-01
```

## قیدهای پخش توپولوژی Pod

می‌توانید از _قیدهای پخش توپولوژی_ برای کنترل نحوهٔ پخش شدن {{< glossary_tooltip text="Podها" term_id="Pod" >}}
در کلاستر خود در میان دامنه‌های خرابی (failure-domains) مانند منطقه‌ها، ناحیه‌ها، نودها یا در میان هر
دامنهٔ توپولوژی دیگری که تعریف می‌کنید، استفاده کنید. ممکن است این کار را برای بهبود کارایی، دسترس‌پذیری مورد انتظار یا
بهره‌وری کلی انجام دهید.

برای آگاهی بیشتر از نحوهٔ کار آن‌ها،
[قیدهای پخش توپولوژی Pod](/docs/concepts/scheduling-eviction/topology-spread-constraints/) را بخوانید.

## برچسب‌های توپولوژی Pod

{{< feature-state feature_gate_name="PodTopologyLabelsAdmission" >}}

Podها برچسب‌های توپولوژی (`topology.kubernetes.io/zone` و `topology.kubernetes.io/region`) را در صورت وجود از نود اختصاص‌یافتهٔ خود به ارث می‌برند. سپس می‌توان از این برچسب‌ها از طریق Downward API استفاده کرد تا بار کاری از توپولوژی نود آگاه شود.

در اینجا نمونه‌ای از یک Pod آمده است که از Downward API برای ناحیه و منطقهٔ خود استفاده می‌کند:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-topology-labels
spec:
  containers:
    - name: app
      image: alpine
      command: ["sh", "-c", "env"]
      env:
        - name: MY_ZONE
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/zone']
        - name: MY_REGION
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/region']
```

## عملگرها

در ادامه همهٔ عملگرهای منطقی آمده‌اند که می‌توانید در فیلد `operator` برای `nodeAffinity` و `podAffinity` که در بالا ذکر شدند، استفاده کنید.

|    عملگر    |    رفتار     |
| :------------: | :-------------: |
| `In` | مقدار برچسب در مجموعهٔ رشته‌های ارائه‌شده وجود دارد |
|   `NotIn`   | مقدار برچسب در مجموعهٔ رشته‌های ارائه‌شده وجود ندارد |
| `Exists` | برچسبی با این کلید روی آبجکت وجود دارد |
| `DoesNotExist` | هیچ برچسبی با این کلید روی آبجکت وجود ندارد |

عملگرهای زیر تنها با `nodeAffinity` قابل استفاده‌اند.

|    عملگر    |    رفتار    |
| :------------: | :-------------: |
| `Gt` | مقدار فیلد به‌صورت یک عدد صحیح تجزیه می‌شود و عدد صحیحی که از تجزیهٔ مقدار برچسبِ نام‌برده‌شده توسط این انتخابگر به دست می‌آید، از این عدد صحیح بزرگ‌تر است |
| `Lt` | مقدار فیلد به‌صورت یک عدد صحیح تجزیه می‌شود و عدد صحیحی که از تجزیهٔ مقدار برچسبِ نام‌برده‌شده توسط این انتخابگر به دست می‌آید، از این عدد صحیح کوچک‌تر است |

{{<note>}}

عملگرهای `Gt` و `Lt` با مقادیر غیرصحیح کار نمی‌کنند. اگر مقدار داده‌شده
به‌صورت یک عدد صحیح تجزیه نشود، زمان‌بندی Pod با شکست مواجه می‌شود. همچنین، `Gt` و `Lt`
برای `podAffinity` در دسترس نیستند.
{{</note>}}

## {{% heading "whatsnext" %}}

- دربارهٔ [taintها و tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration/) بیشتر بخوانید.
- اسناد طراحی [وابستگی نود](https://git.k8s.io/design-proposals-archive/scheduling/nodeaffinity.md)
  و [وابستگی/ضدوابستگی بین Podها](https://git.k8s.io/design-proposals-archive/scheduling/podaffinity.md) را بخوانید.
- بیاموزید که [topology manager](/docs/tasks/administer-cluster/topology-manager/) چگونه در تصمیم‌های تخصیص منابع
  در سطح نود مشارکت می‌کند.
- بیاموزید که چگونه از [nodeSelector](/docs/tasks/configure-pod-container/assign-pods-nodes/) استفاده کنید.
- بیاموزید که چگونه از [وابستگی و ضدوابستگی](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/) استفاده کنید.

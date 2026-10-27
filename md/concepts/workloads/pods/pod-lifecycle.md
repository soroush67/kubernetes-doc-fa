---
title: چرخه حیات Pod
content_type: concept
weight: 30
math: true
---

<!-- overview -->

این صفحه چرخه حیات یک Pod را توضیح می‌دهد. Podها از یک چرخه حیات تعریف‌شده پیروی می‌کنند؛ از [فاز](#pod-phase) `Pending` آغاز می‌شوند، در صورتی که دست‌کم یکی از کانتینرهای اصلی آن‌ها به‌درستی شروع به کار کند به فاز `Running` می‌روند، و سپس بسته به اینکه آیا هر کانتینری در Pod با شکست پایان یافته است یا خیر، به فاز `Succeeded` یا `Failed` منتقل می‌شوند.

در زمانی که یک Pod در حال اجراست، kubelet کانتینرها را مدیریت می‌کند و مشخصات (spec) Pod را برای container runtime ترجمه می‌کند. kubelet همچنین اجرای [probeها](#container-probes) را که سلامت برنامه شما را پایش می‌کنند، مدیریت می‌کند.

Podها نیز مانند کانتینرهای برنامه‌ی منفرد، موجودیت‌هایی نسبتاً زودگذر (و نه پایدار) به شمار می‌روند. Podها ایجاد می‌شوند، یک شناسه‌ی یکتا ([UID](/docs/concepts/overview/working-with-objects/names/#uids)) به آن‌ها اختصاص می‌یابد و برای اجرا روی نودهایی زمان‌بندی می‌شوند که تا زمان خاتمه (مطابق با سیاست راه‌اندازی مجدد) یا حذف، در آن‌ها باقی می‌مانند.
اگر یک {{< glossary_tooltip term_id="node" text="نود" >}} از کار بیفتد، Podهایی که روی آن نود در حال اجرا هستند (یا برای اجرا روی آن زمان‌بندی شده‌اند) [برای حذف علامت‌گذاری می‌شوند](#pod-garbage-collection). control plane پس از یک بازه‌ی زمانی انتظار (timeout)، Podها را برای حذف علامت‌گذاری می‌کند.

<!-- body -->

## طول عمر Pod {#pod-lifetime}

در حالی که یک Pod در حال اجراست، kubelet می‌تواند برای مدیریت برخی انواع خطاها، کانتینرها را مجدداً راه‌اندازی کند. کوبرنتیز در داخل یک Pod، [وضعیت‌های](#container-states) مختلف کانتینرها را پیگیری می‌کند و تعیین می‌کند چه اقدامی باید انجام دهد تا Pod دوباره سالم شود. این کار در یک [حلقه‌ی polling](/docs/reference/node/kubelet-sync-loop/) انجام می‌شود که به‌صورت دوره‌ای حالت مطلوب (spec یک Pod) را با حالت واقعی کانتینرهای در حال اجرا هم‌سو می‌کند.

در API کوبرنتیز، Podها هم مشخصات (specification) و هم وضعیت (status) واقعی دارند. وضعیت یک آبجکت Pod از مجموعه‌ای از [شرایط Pod (Pod conditions)](#pod-conditions) تشکیل شده است. همچنین، اگر برای برنامه‌ی شما مفید باشد، می‌توانید [اطلاعات آمادگی سفارشی](#pod-readiness-gate) را به داده‌های condition یک Pod اضافه کنید.

Podها در طول عمر خود تنها یک بار [زمان‌بندی](/docs/concepts/scheduling-eviction/) می‌شوند؛ اختصاص یک Pod به یک نود مشخص _binding_ نامیده می‌شود و فرایند انتخاب نودی که باید استفاده شود _scheduling_ نام دارد.
پس از آنکه یک Pod زمان‌بندی شد و به یک نود متصل (bound) گردید، کوبرنتیز تلاش می‌کند آن Pod را روی آن نود اجرا کند. Pod روی آن نود اجرا می‌شود تا زمانی که متوقف شود یا تا زمانی که Pod [خاتمه داده شود](#pod-termination)؛ اگر کوبرنتیز نتواند Pod را روی نود انتخاب‌شده راه‌اندازی کند (برای مثال، اگر نود پیش از شروع Pod از کار بیفتد)، آن Pod خاص هرگز شروع نخواهد شد.

می‌توانید از [آمادگی زمان‌بندی Pod (Pod Scheduling Readiness)](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/) برای به تعویق انداختن زمان‌بندی یک Pod تا زمانی که همه‌ی _scheduling gateهای_ آن برداشته شوند استفاده کنید. برای مثال، ممکن است بخواهید مجموعه‌ای از Podها را تعریف کنید، اما زمان‌بندی را فقط پس از ایجاد همه‌ی Podها آغاز کنید.

### Podها و بازیابی از خطا {#pod-fault-recovery}

اگر یکی از کانتینرهای Pod با شکست مواجه شود، کوبرنتیز ممکن است سعی کند همان کانتینر را مجدداً راه‌اندازی کند.
برای اطلاعات بیشتر، [نحوه‌ی برخورد Podها با مشکلات کانتینرها](#container-restarts) را بخوانید.

با این حال، Podها می‌توانند به شیوه‌ای دچار خطا شوند که کلاستر قادر به بازیابی آن نباشد، و در آن صورت کوبرنتیز تلاش بیشتری برای ترمیم Pod نمی‌کند؛ در عوض، کوبرنتیز Pod را حذف می‌کند و برای ترمیم خودکار به سایر مؤلفه‌ها متکی است.

اگر یک Pod روی یک {{< glossary_tooltip text="نود" term_id="node" >}} زمان‌بندی شده باشد و سپس آن نود از کار بیفتد، Pod ناسالم تلقی می‌شود و کوبرنتیز در نهایت آن Pod را حذف می‌کند.
یک Pod در برابر {{< glossary_tooltip text="تخلیه (eviction)" term_id="eviction" >}} ناشی از کمبود منابع یا نگهداری نود دوام نمی‌آورد.

کوبرنتیز از یک انتزاع سطح بالاتر به نام {{< glossary_tooltip term_id="controller" text="کنترل‌کننده" >}} استفاده می‌کند که کار مدیریت نمونه‌های نسبتاً یک‌بارمصرف Pod را بر عهده دارد.

یک Pod مشخص (که با یک UID تعریف می‌شود) هرگز به نود دیگری «زمان‌بندی مجدد» نمی‌شود؛ در عوض، آن Pod می‌تواند با یک Pod جدید و تقریباً یکسان جایگزین شود. اگر یک Pod جایگزین بسازید، می‌تواند حتی همان نامی (مانند `.metadata.name`) را داشته باشد که Pod قدیمی داشت، اما Pod جایگزین `.metadata.uid` متفاوتی نسبت به Pod قدیمی خواهد داشت.

کوبرنتیز تضمین نمی‌کند که جایگزین یک Pod موجود روی همان نودی زمان‌بندی شود که Pod قدیمیِ جایگزین‌شده روی آن بود.

### طول عمرهای وابسته {#associated-lifetimes}

وقتی گفته می‌شود چیزی، مانند یک {{< glossary_tooltip term_id="volume" text="حجم (volume)" >}}، طول عمری برابر با یک Pod دارد، به این معناست که آن چیز تا زمانی وجود دارد که آن Pod مشخص (با همان UID دقیق) وجود داشته باشد. اگر آن Pod به هر دلیلی حذف شود، و حتی اگر یک جایگزین یکسان ایجاد شود، چیز مرتبط (در این مثال، یک حجم) نیز از بین می‌رود و از نو ساخته می‌شود.

{{< figure src="/images/docs/pod.svg" title="Figure 1." class="diagram-medium" caption="A multi-container Pod that contains a file puller [sidecar](/docs/concepts/workloads/pods/sidecar-containers/) and a web server. The Pod uses an [ephemeral `emptyDir` volume](/docs/concepts/storage/volumes/#emptydir) for shared storage between the containers." >}}

## فاز Pod {#pod-phase}

فیلد `status` یک Pod یک آبجکت [PodStatus](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) است که دارای یک فیلد `phase` می‌باشد.

فاز یک Pod خلاصه‌ای ساده و سطح بالا از جایگاه Pod در چرخه حیات آن است. فاز قرار نیست جمع‌بندی جامعی از مشاهدات وضعیت کانتینر یا Pod باشد، و همچنین قرار نیست یک ماشین حالت (state machine) جامع باشد.

تعداد و معانی مقادیر فاز Pod به‌دقت حفظ می‌شوند.
جز آنچه در اینجا مستند شده است، نباید درباره‌ی Podهایی که مقدار مشخصی برای `phase` دارند فرضی در نظر گرفته شود.

مقادیر ممکن برای `phase` به شرح زیر است:

مقدار       | توضیح
:-----------|:-----------
`Pending`   | Pod توسط کلاستر کوبرنتیز پذیرفته شده است، اما یک یا چند کانتینر آن هنوز راه‌اندازی نشده و آماده‌ی اجرا نشده‌اند. این شامل زمانی است که Pod در انتظار زمان‌بندی می‌گذراند و همچنین زمان صرف‌شده برای دانلود ایمیج‌های کانتینر از طریق شبکه.
`Running`   | Pod به یک نود متصل شده است و همه‌ی کانتینرها ایجاد شده‌اند. دست‌کم یک کانتینر همچنان در حال اجراست، یا در حال شروع یا راه‌اندازی مجدد است.
`Succeeded` | همه‌ی کانتینرهای Pod با موفقیت خاتمه یافته‌اند و دوباره راه‌اندازی نخواهند شد.
`Failed`    | همه‌ی کانتینرهای Pod خاتمه یافته‌اند و دست‌کم یک کانتینر با شکست خاتمه یافته است. یعنی کانتینر یا با وضعیت غیرصفر خارج شده یا توسط سیستم خاتمه داده شده است، و برای راه‌اندازی مجدد خودکار تنظیم نشده است.
`Unknown`   | به دلایلی وضعیت Pod قابل دریافت نبوده است. این فاز معمولاً به‌دلیل خطا در ارتباط با نودی رخ می‌دهد که Pod باید روی آن در حال اجرا باشد.

{{< note >}}

وقتی یک Pod به‌طور مکرر در شروع شدن با شکست مواجه می‌شود، ممکن است `CrashLoopBackOff` در فیلد `Status` برخی از دستورات kubectl نمایش داده شود.
به‌طور مشابه، وقتی یک Pod در حال حذف شدن است، ممکن است `Terminating` در فیلد `Status` برخی از دستورات kubectl نمایش داده شود.

مراقب باشید _Status_ را که یک فیلد نمایشی kubectl برای درک شهودی کاربر است، با `phase` مربوط به Pod اشتباه نگیرید.
فاز Pod بخشی صریح از مدل داده‌ی کوبرنتیز و [API مربوط به Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/) است.

```
  NAMESPACE               NAME               READY   STATUS             RESTARTS   AGE
  alessandras-namespace   alessandras-pod    0/1     CrashLoopBackOff   200        2d9h
```

به یک Pod مهلتی برای خاتمه‌ی آرام (graceful) داده می‌شود که به‌طور پیش‌فرض ۳۰ ثانیه است.
می‌توانید از فلگ `--force` برای [خاتمه‌ی اجباری یک Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced) استفاده کنید.
{{< /note >}}

از کوبرنتیز نسخه‌ی ۱.۲۷ به بعد، kubelet پیش از حذف Podهای حذف‌شده از API server، آن‌ها را به یک فاز نهایی (`Failed` یا `Succeeded`، بسته به وضعیت‌های خروج کانتینرهای Pod) منتقل می‌کند، به‌جز دو استثنا:

* [Podهای ایستا (static Pods)](/docs/tasks/configure-pod-container/static-pod/) (که مستقیماً توسط kubelet مدیریت می‌شوند و توسط {{< glossary_tooltip text="mirror Podها" term_id="mirror-pod" >}} نمایش داده می‌شوند)
* [Podهایی که به‌صورت اجباری حذف شده‌اند](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced) و finalizer ندارند

اگر یک نود از کار بیفتد یا از بقیه‌ی کلاستر قطع شود، کوبرنتیز سیاستی را برای تنظیم `phase` همه‌ی Podهای روی نود ازدست‌رفته به Failed اعمال می‌کند.

## وضعیت‌های کانتینر {#container-states}

علاوه بر [فاز](#pod-phase) کلی Pod، کوبرنتیز وضعیت هر کانتینر داخل یک Pod را نیز پیگیری می‌کند. می‌توانید از [hookهای چرخه حیات کانتینر](/docs/concepts/containers/container-lifecycle-hooks/) برای راه‌اندازی رویدادهایی استفاده کنید که در نقاط مشخصی از چرخه حیات کانتینر اجرا شوند.

هنگامی که {{< glossary_tooltip text="زمان‌بند" term_id="kube-scheduler" >}} یک Pod را به یک نود اختصاص می‌دهد، kubelet با استفاده از یک {{< glossary_tooltip text="container runtime" term_id="container-runtime" >}} شروع به ایجاد کانتینرها برای آن Pod می‌کند.
سه وضعیت ممکن برای کانتینر وجود دارد: `Waiting`، `Running` و `Terminated`.

برای بررسی وضعیت کانتینرهای یک Pod می‌توانید از `kubectl describe pod <name-of-pod>` استفاده کنید. خروجی، وضعیت هر کانتینر داخل آن Pod را نشان می‌دهد.

هر وضعیت معنای مشخصی دارد:

### `Waiting` {#container-state-waiting}

اگر کانتینری نه در وضعیت `Running` باشد و نه در وضعیت `Terminated`، در وضعیت `Waiting` است.
کانتینری که در وضعیت `Waiting` است، هنوز در حال انجام عملیاتی است که برای تکمیل راه‌اندازی به آن نیاز دارد: برای مثال، دریافت ایمیج کانتینر از یک registry ایمیج کانتینر، یا اعمال داده‌های {{< glossary_tooltip text="Secret" term_id="secret" >}}.
هنگامی که از `kubectl` برای پرس‌وجو درباره‌ی Podی استفاده می‌کنید که کانتینری در وضعیت `Waiting` دارد، یک فیلد Reason نیز می‌بینید که دلیل قرار داشتن کانتینر در آن وضعیت را خلاصه می‌کند.

### `Running` {#container-state-running}

وضعیت `Running` نشان می‌دهد که کانتینر بدون مشکل در حال اجراست. اگر یک hook از نوع `postStart` پیکربندی شده بوده باشد، پیش‌تر اجرا و تمام شده است. هنگامی که از `kubectl` برای پرس‌وجو درباره‌ی Podی استفاده می‌کنید که کانتینری در وضعیت `Running` دارد، اطلاعاتی درباره‌ی زمان ورود کانتینر به وضعیت `Running` نیز می‌بینید.

### `Terminated` {#container-state-terminated}

کانتینری که در وضعیت `Terminated` است، اجرا را آغاز کرده و سپس یا تا پایان اجرا شده یا به دلیلی با شکست مواجه شده است. هنگامی که از `kubectl` برای پرس‌وجو درباره‌ی Podی استفاده می‌کنید که کانتینری در وضعیت `Terminated` دارد، یک دلیل (reason)، یک کد خروج (exit code) و زمان شروع و پایان دوره‌ی اجرای آن کانتینر را می‌بینید.

اگر برای یک کانتینر hook از نوع `preStop` پیکربندی شده باشد، این hook پیش از ورود کانتینر به وضعیت `Terminated` اجرا می‌شود.

## نحوه‌ی برخورد Podها با مشکلات کانتینرها {#container-restarts}

کوبرنتیز خطاهای کانتینر در Podها را با استفاده از [`restartPolicy`](#restart-policy) که در `spec` مربوط به Pod تعریف شده است مدیریت می‌کند. این سیاست تعیین می‌کند کوبرنتیز چگونه به خروج کانتینرها به‌دلیل خطا یا دلایل دیگر واکنش نشان دهد، که مطابق توالی زیر است:

1. **خرابی اولیه**: کوبرنتیز بر اساس `restartPolicy` مربوط به Pod، بلافاصله تلاش می‌کند کانتینر را مجدداً راه‌اندازی کند.
1. **خرابی‌های مکرر**: پس از خرابی اولیه، کوبرنتیز برای راه‌اندازی‌های مجدد بعدی یک تأخیر backoff نمایی اعمال می‌کند که در [`restartPolicy`](#restart-policy) شرح داده شده است.
   این کار از بارگذاری بیش‌ازحد سیستم در اثر تلاش‌های سریع و مکرر برای راه‌اندازی مجدد جلوگیری می‌کند.
1. **وضعیت CrashLoopBackOff**: این وضعیت نشان می‌دهد که سازوکار تأخیر backoff در حال حاضر برای کانتینر مشخصی که در یک حلقه‌ی خرابی (crash loop) قرار دارد و به‌طور مکرر شکست می‌خورد و دوباره راه‌اندازی می‌شود، در حال اعمال است.
1. **بازنشانی backoff**: اگر یک کانتینر برای مدت زمان مشخصی (مثلاً ۱۰ دقیقه) با موفقیت اجرا شود، کوبرنتیز تأخیر backoff را بازنشانی می‌کند و هر خرابی جدید را همانند اولین خرابی در نظر می‌گیرد.

در عمل، `CrashLoopBackOff` وضعیت یا رویدادی است که ممکن است در خروجی دستور `kubectl` هنگام توصیف یا فهرست کردن Podها دیده شود، زمانی که کانتینری در Pod به‌درستی شروع نمی‌شود و سپس پیوسته در یک حلقه تلاش می‌کند و شکست می‌خورد.

به عبارت دیگر، هنگامی که یک کانتینر وارد حلقه‌ی خرابی می‌شود، کوبرنتیز تأخیر backoff نمایی را که در [سیاست راه‌اندازی مجدد کانتینر](#restart-policy) ذکر شد اعمال می‌کند. این سازوکار از آن جلوگیری می‌کند که یک کانتینر معیوب با تلاش‌های ناموفق و پیوسته‌ی راه‌اندازی، سیستم را تحت فشار قرار دهد.

`CrashLoopBackOff` می‌تواند ناشی از مشکلاتی مانند موارد زیر باشد:

* خطاهای برنامه که باعث خروج کانتینر می‌شوند.
* خطاهای پیکربندی، مانند متغیرهای محیطی نادرست یا فایل‌های پیکربندی گم‌شده.
* محدودیت‌های منابع، که در آن‌ها ممکن است کانتینر حافظه یا CPU کافی برای شروع صحیح نداشته باشد.
* شکست بررسی‌های سلامت (health checks) در صورتی که برنامه در زمان مورد انتظار شروع به سرویس‌دهی نکند.
* برگرداندن نتیجه‌ی `Failure` توسط liveness probeها یا startup probeهای کانتینر، همان‌طور که در [بخش probeها](#container-probes) ذکر شده است.

برای بررسی علت ریشه‌ای مشکل `CrashLoopBackOff`، کاربر می‌تواند:

1. **لاگ‌ها را بررسی کند**: از `kubectl logs <name-of-pod>` برای بررسی لاگ‌های کانتینر استفاده کند.
   این اغلب مستقیم‌ترین راه برای تشخیص مشکلی است که باعث خرابی‌ها می‌شود.
1. **رویدادها را بررسی کند**: از `kubectl describe pod <name-of-pod>` برای مشاهده‌ی رویدادهای Pod استفاده کند، که می‌تواند سرنخ‌هایی درباره‌ی مشکلات پیکربندی یا منابع ارائه دهد.
1. **پیکربندی را مرور کند**: اطمینان حاصل کند که پیکربندی Pod، از جمله متغیرهای محیطی و حجم‌های mount‌شده، درست است و همه‌ی منابع خارجی مورد نیاز در دسترس هستند.
1. **محدودیت‌های منابع را بررسی کند**: مطمئن شود که به کانتینر CPU و حافظه‌ی کافی اختصاص داده شده است. گاهی افزایش منابع در تعریف Pod می‌تواند مشکل را حل کند.
1. **برنامه را اشکال‌زدایی کند**: ممکن است باگ‌ها یا پیکربندی‌های نادرستی در کد برنامه وجود داشته باشد. اجرای این ایمیج کانتینر به‌صورت محلی یا در یک محیط توسعه می‌تواند به تشخیص مشکلات خاص برنامه کمک کند.

### راه‌اندازی مجدد کانتینرها {#restart-policy}

وقتی یک کانتینر در Pod شما متوقف می‌شود یا با خطا مواجه می‌شود، کوبرنتیز می‌تواند آن را دوباره راه‌اندازی کند.
راه‌اندازی مجدد همیشه مناسب نیست؛ برای مثال،
{{< glossary_tooltip text="کانتینرهای init" term_id="init-container" >}} فقط یک بار (در صورت موفقیت)
در زمان راه‌اندازی Pod اجرا می‌شوند.
می‌توانید راه‌اندازی مجدد را به‌صورت سیاستی که برای همه Podها اعمال می‌شود پیکربندی کنید، یا از پیکربندی در سطح کانتینر استفاده کنید (برای مثال: هنگامی که یک
{{< glossary_tooltip text="کانتینر sidecar" term_id="sidecar-container" >}} تعریف می‌کنید) یا یک بازنویسی (override) در سطح کانتینر تعریف کنید.

#### راه‌اندازی مجدد کانتینر و تاب‌آوری {#container-restart-resilience}

پروژه کوبرنتیز پیروی از اصول بومی ابری (cloud-native) را توصیه می‌کند، از جمله طراحی تاب‌آور
که راه‌اندازی‌های مجدد اعلام‌نشده یا دلخواه را در نظر می‌گیرد. می‌توانید این هدف را یا
با شکست‌دادن Pod و اتکا به
[جایگزینی](/docs/concepts/workloads/controllers/) خودکار آن محقق کنید، یا می‌توانید برای تاب‌آوری در سطح کانتینر طراحی کنید.
هر دو رویکرد به این امر کمک می‌کنند که بار کاری شما در مجموع، با وجود
خرابی جزئی، در دسترس باقی بماند.

#### سیاست راه‌اندازی مجدد کانتینر در سطح Pod

فیلد `spec` یک Pod دارای فیلدی به نام `restartPolicy` است که مقادیر ممکن آن Always، OnFailure
و Never است. مقدار پیش‌فرض Always است.

`restartPolicy` یک Pod برای {{< glossary_tooltip text="کانتینرهای برنامه" term_id="app-container" >}}
در Pod و برای [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/) معمولی اعمال می‌شود.
[کانتینرهای sidecar](/docs/concepts/workloads/pods/sidecar-containers/)
فیلد `restartPolicy` در سطح Pod را نادیده می‌گیرند: در کوبرنتیز، sidecar به‌صورت
یک عنصر درون `initContainers` تعریف می‌شود که `restartPolicy` در سطح کانتینر آن روی `Always` تنظیم شده است.
برای کانتینرهای init که با خطا خارج می‌شوند، kubelet کانتینر init را دوباره راه‌اندازی می‌کند اگر
`restartPolicy` در سطح Pod برابر `OnFailure` یا `Always` باشد:

* `Always`: کانتینر را پس از هر نوع خاتمه به‌طور خودکار دوباره راه‌اندازی می‌کند.
* `OnFailure`: کانتینر را تنها در صورتی دوباره راه‌اندازی می‌کند که با خطا خارج شود (کد خروج غیرصفر).
* `Never`: کانتینر خاتمه‌یافته را به‌طور خودکار دوباره راه‌اندازی نمی‌کند.

##### مقایسه رفتار راه‌اندازی مجدد

جدول زیر نشان می‌دهد کانتینرها تحت سیاست‌های راه‌اندازی مجدد و کدهای خروج مختلف چگونه رفتار می‌کنند:

| کد خروج | `restartPolicy: Always` | `restartPolicy: OnFailure` | `restartPolicy: Never` | کانتینرهای Sidecar |
|-----------|-------------------------|---------------------------|------------------------|-------------------|
| 0 (موفقیت) | راه‌اندازی مجدد می‌شود | راه‌اندازی مجدد نمی‌شود | راه‌اندازی مجدد نمی‌شود | همیشه راه‌اندازی مجدد می‌شود |
| غیرصفر (شکست) | راه‌اندازی مجدد می‌شود | راه‌اندازی مجدد می‌شود | راه‌اندازی مجدد نمی‌شود | همیشه راه‌اندازی مجدد می‌شود |

{{< note >}}
رفتار راه‌اندازی مجدد هنگام انتخاب بین Deploymentها و Jobها اهمیت ویژه‌ای دارد:
- **Deploymentها** معمولاً از `restartPolicy: Always` (تنها مقدار مجاز) استفاده می‌کنند تا برنامه‌ها به‌طور پیوسته در حال اجرا بمانند
- **Jobها** معمولاً از `restartPolicy: OnFailure` یا `restartPolicy: Never` استفاده می‌کنند تا وظایف پردازش دسته‌ای را به‌درستی مدیریت کنند
- **کانتینرهای sidecar** کانتینرهای init هستند که صرف‌نظر از `restartPolicy` مربوط به Pod همیشه دوباره راه‌اندازی می‌شوند، زیرا `restartPolicy: Always` مختص خودشان را در سطح کانتینر دارند
{{< /note >}}

##### سناریوهای نمونه

در اینجا مثال‌های عینی برای نمایش رفتارهای مختلف راه‌اندازی مجدد آمده است:

**مثال ۱: وب‌سرور با `restartPolicy: Always` (معمول برای Deploymentها)**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-server
spec:
  restartPolicy: Always  # Container restarts regardless of exit code
  containers:
  - name: nginx
    image: nginx:1.14.2
    # If this container crashes or exits for any reason, it will be restarted
```

**مثال ۲: Job دسته‌ای با `restartPolicy: OnFailure`**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: data-processor
spec:
  template:
    spec:
      restartPolicy: OnFailure  # Only restart on non-zero exit codes
      containers:
      - name: processor
        image: busybox:1.28
        command: ['sh', '-c', 'echo "Processing data..."; exit 0']
        # Exit code 0: Job completes successfully, no restart
        # Exit code 1+: Container restarts to retry the task
```

**مثال ۳: وظیفه یک‌باره با `restartPolicy: Never`**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: migration-task
spec:
  restartPolicy: Never  # Never restart, regardless of exit code
  containers:
  - name: migrate
    image: busybox:1.28
    command: ['sh', '-c', 'echo "Running migration..."; exit 1']
    # Even with exit code 1 (failure), the container will not restart
    # The Pod will remain in Failed state
```

##### کانتینرهای sidecar و سیاست‌های راه‌اندازی مجدد

[کانتینرهای sidecar](/docs/concepts/workloads/pods/sidecar-containers/) رفتار راه‌اندازی مجدد ویژه‌ای دارند که با کانتینرهای برنامه معمولی متفاوت است:

- **کانتینرهای sidecar فیلد `restartPolicy` در سطح Pod را نادیده می‌گیرند**: آن‌ها از فیلد `restartPolicy` در سطح کانتینر مختص خود استفاده می‌کنند که همیشه روی `Always` تنظیم شده است
- **چرخه حیات مستقل**: کانتینرهای sidecar می‌توانند مستقل از کانتینر اصلی برنامه دوباره راه‌اندازی شوند
- **عملکرد پایدار**: کانتینرهای sidecar در تمام طول عمر Pod در حال اجرا باقی می‌مانند تا خدمات پشتیبان را فراهم کنند

**مثال: Pod دارای کانتینر sidecar**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  restartPolicy: OnFailure  # Applies to main container only
  initContainers:
  - name: logging-sidecar    # This is a sidecar container
    image: fluent/fluent-bit:1.8
    restartPolicy: Always    # Sidecar always restarts regardless of exit code
    # Provides logging services throughout Pod lifetime
  containers:
  - name: main-app          # This follows Pod-level restartPolicy
    image: nginx:1.14.2
    # Will only restart on failure (non-zero exit) due to Pod's OnFailure policy
```

{{< note >}}
در حالی که کانتینر اصلی برنامه از `restartPolicy: OnFailure` مربوط به Pod پیروی می‌کند، کانتینر sidecar صرف‌نظر از کد خروج خود دوباره راه‌اندازی می‌شود، زیرا کانتینرهای sidecar در سطح کانتینر همیشه `restartPolicy: Always` دارند.
{{< /note >}}

هنگامی که kubelet راه‌اندازی مجدد کانتینرها را بر اساس سیاست راه‌اندازی مجدد پیکربندی‌شده مدیریت می‌کند،
این موضوع فقط شامل راه‌اندازی‌هایی می‌شود که کانتینرهای جایگزین را درون همان
Pod و روی همان نود ایجاد می‌کنند. پس از خروج کانتینرهای یک Pod، kubelet
آن‌ها را با تأخیر عقب‌نشینی نمایی (exponential backoff) (۱۰ ثانیه، ۲۰ ثانیه، ۴۰ ثانیه، …) که حداکثر
به ۳۰۰ ثانیه (۵ دقیقه) محدود می‌شود، دوباره راه‌اندازی می‌کند. هنگامی که یک کانتینر به مدت ۱۰ دقیقه بدون هیچ
مشکلی اجرا شده باشد، kubelet زمان‌سنج عقب‌نشینی راه‌اندازی مجدد را برای آن کانتینر بازنشانی می‌کند.
[کانتینرهای sidecar و چرخه حیات Pod](/docs/concepts/workloads/pods/sidecar-containers/#sidecar-containers-and-pod-lifecycle)
رفتار `init containers` را هنگام تعیین فیلد `restartPolicy` روی آن‌ها توضیح می‌دهد.

#### سیاست و قواعد راه‌اندازی مجدد برای هر کانتینر به‌صورت جداگانه {#container-restart-rules}

{{< feature-state feature_gate_name="ContainerRestartRules" >}}

اگر feature gate با نام `ContainerRestartRules` در کلاستر شما فعال باشد، می‌توانید
`restartPolicy` و `restartPolicyRules` را روی _هر کانتینر به‌صورت جداگانه_ مشخص کنید تا سیاست
راه‌اندازی مجدد Pod را بازنویسی کنند. سیاست و قواعد راه‌اندازی مجدد کانتینر برای {{< glossary_tooltip text="کانتینرهای برنامه" term_id="app-container" >}}
در Pod و برای [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/) معمولی اعمال می‌شود.

یک [کانتینر sidecar](/docs/concepts/workloads/pods/sidecar-containers/) بومی کوبرنتیز
فیلد `restartPolicy` سطح کانتینر خود را روی `Always` تنظیم‌شده دارد.

راه‌اندازی مجدد کانتینرها از همان عقب‌نشینی نمایی سیاست راه‌اندازی مجدد Pod که در بالا توضیح داده شد پیروی می‌کند.
سیاست‌های راه‌اندازی مجدد پشتیبانی‌شده برای کانتینر عبارت‌اند از:

* `Always`: کانتینر را پس از هر نوع خاتمه به‌طور خودکار دوباره راه‌اندازی می‌کند.
* `OnFailure`: کانتینر را تنها در صورتی دوباره راه‌اندازی می‌کند که با خطا خارج شود (کد خروج غیرصفر).
* `Never`: کانتینر خاتمه‌یافته را به‌طور خودکار دوباره راه‌اندازی نمی‌کند.

علاوه بر این، _هر کانتینر به‌صورت جداگانه_ می‌تواند `restartPolicyRules` را مشخص کند. اگر فیلد `restartPolicyRules`
مشخص شود، آنگاه `restartPolicy` کانتینر نیز **باید** مشخص شود. `restartPolicyRules`
فهرستی از قواعد را تعریف می‌کند که هنگام خروج کانتینر اعمال می‌شوند. هر قاعده شامل یک شرط
و یک عمل است. شرط پشتیبانی‌شده `exitCodes` است که کد خروج کانتینر را
با فهرستی از مقادیر داده‌شده مقایسه می‌کند. عمل پشتیبانی‌شده `Restart` است، به این معنا که کانتینر
دوباره راه‌اندازی خواهد شد. قواعد به‌ترتیب ارزیابی می‌شوند. در نخستین تطابق، عمل مربوطه اعمال می‌شود.
اگر شرط هیچ‌یک از قواعد برقرار نباشد، کوبرنتیز به `restartPolicy` پیکربندی‌شده‌ی کانتینر بازمی‌گردد.

برای مثال، یک Pod با سیاست راه‌اندازی مجدد OnFailure که دارای یک کانتینر `try-once` است. این امکان را می‌دهد
که Pod فقط برخی کانتینرها را دوباره راه‌اندازی کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: on-failure-pod
spec:
  restartPolicy: OnFailure
  containers:
  - name: try-once-container    # This container will run only once because the restartPolicy is Never.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Only running once" && sleep 10 && exit 1']
    restartPolicy: Never     
  - name: on-failure-container  # This container will be restarted on failure.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Keep restarting" && sleep 1800 && exit 1']
```

یک Pod با سیاست راه‌اندازی مجدد `Always` که دارای یک کانتینر init است که فقط یک بار اجرا می‌شود. اگر کانتینر
init شکست بخورد، Pod شکست می‌خورد. این امکان را می‌دهد که Pod در صورت شکست مقداردهی اولیه شکست بخورد،
اما پس از موفقیت مقداردهی اولیه همچنان در حال اجرا بماند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: fail-pod-if-init-fails
spec:
  restartPolicy: Always
  initContainers:
  - name: init-once      # This init container will only try once. If it fails, the pod will fail.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Failing initialization" && sleep 10 && exit 1']
    restartPolicy: Never
  containers:
  - name: main-container # This container will always be restarted once initialization succeeds.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 1800 && exit 0']
```

یک Pod با سیاست راه‌اندازی مجدد Never که دارای کانتینری است که برخی کدهای خروج مشخص را نادیده می‌گیرد و برای برخی دیگر راه‌اندازی مجدد می‌شود.
این برای تمایز میان خطاهای قابل راه‌اندازی مجدد و خطاهای غیرقابل راه‌اندازی مجدد مفید است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: restart-on-exit-codes
spec:
  restartPolicy: Never
  containers:
  - name: restart-on-exit-codes
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 60 && exit 0']
    restartPolicy: Never     # Container restart policy must be specified if rules are specified
    restartPolicyRules:      # Only restart the container if it exits with code 42
    - action: Restart
      exitCodes:
        operator: In
        values: [42]
```

قواعد راه‌اندازی مجدد را می‌توان برای بسیاری از سناریوهای پیشرفته‌تر مدیریت چرخه حیات به کار برد. توجه داشته باشید که قواعد راه‌اندازی مجدد
نیز تحت تأثیر همان ناسازگاری‌هایی هستند که سیاست راه‌اندازی مجدد معمولی دارد. راه‌اندازی‌های مجدد kubelet، جمع‌آوری زباله (garbage collection) در
container runtime و مشکلات اتصال مقطعی با control plane ممکن است باعث
از دست رفتن وضعیت شوند و کانتینرها حتی زمانی که انتظار دارید دوباره راه‌اندازی نشوند، ممکن است دوباره اجرا شوند.

#### راه‌اندازی مجدد همه کانتینرها {#restart-all-containers}

{{< feature-state feature_gate_name="RestartAllContainersOnContainerExits" >}}

اگر feature gate با نام `RestartAllContainersOnContainerExits` در کلاستر شما فعال باشد، می‌توانید
`RestartAllContainers` را به‌عنوان یک عمل در `restartPolicyRules` در سطح کانتینر مشخص کنید. هنگامی که خروج یک کانتینر
با قاعده‌ای که این عمل را دارد مطابقت پیدا کند، کل Pod خاتمه می‌یابد و به‌صورت درجا (in-place) دوباره راه‌اندازی می‌شود.

این راه‌اندازی مجدد «درجا» در مقایسه با حذف کامل و ایجاد مجدد، روشی کارآمدتر برای بازنشانی وضعیت Pod ارائه می‌دهد.
این موضوع به‌ویژه برای بارهای کاری ارزشمند است که زمان‌بندی مجدد آن‌ها پرهزینه است، مانند
Jobهای دسته‌ای یا وظایف آموزش هوش مصنوعی/یادگیری ماشین.

##### راه‌اندازی مجدد درجای Pod چگونه کار می‌کند

هنگامی که عمل `RestartAllContainers` فعال می‌شود، kubelet مراحل زیر را انجام می‌دهد:

1. **خاتمه سریع**: همه کانتینرهای در حال اجرا در Pod خاتمه می‌یابند.
   مقدار پیکربندی‌شده `terminationGracePeriodSeconds` رعایت نمی‌شود و هیچ hook از نوع `preStop` که پیکربندی شده باشد
   اجرا نمی‌شود. این امر خاموش‌شدن سریع را تضمین می‌کند.
1. **حفظ منابع Pod**: منابع ضروری Pod حفظ می‌شوند:

   * UID، آدرس IP و network namespace مربوط به Pod
   * Pod sandbox و هر دستگاه متصل‌شده
   * همه حجم‌ها (volumeها)، از جمله `emptyDir` و حجم‌های مونت‌شده

1. **به‌روزرسانی وضعیت Pod**: وضعیت Pod با شرط `PodRestartInPlace` که روی `True` تنظیم شده به‌روزرسانی می‌شود.
   این کار فرایند راه‌اندازی مجدد را قابل مشاهده می‌کند.
1. **توالی کامل راه‌اندازی مجدد**: پس از خاتمه همه کانتینرها، شرط `PodRestartInPlace`
   روی `False` تنظیم می‌شود و Pod فرایند استاندارد راه‌اندازی را آغاز می‌کند:

   * **کانتینرهای init به‌ترتیب دوباره اجرا می‌شوند.**
   * کانتینرهای sidecar و کانتینرهای معمولی راه‌اندازی می‌شوند.

یکی از جنبه‌های کلیدی این قابلیت آن است که **همه** کانتینرها دوباره راه‌اندازی می‌شوند، از جمله کانتینرهایی که
پیش‌تر با موفقیت تکمیل شده یا شکست خورده بودند. عمل `RestartAllContainers` هر
`restartPolicy` پیکربندی‌شده در سطح کانتینر یا سطح Pod را بازنویسی می‌کند.

این سازوکار در سناریوهایی مفید است که به یک شروع پاک برای همه کانتینرها نیاز است، مانند:

- هنگامی که یک کانتینر `init` محیطی را آماده می‌کند که ممکن است خراب شود، این قابلیت تضمین می‌کند
  که فرایند آماده‌سازی دوباره اجرا می‌شود.
- یک کانتینر sidecar می‌تواند سلامت برنامه اصلی را پایش کند و در صورتی که برنامه وارد وضعیت غیرقابل بازیابی شود،
  راه‌اندازی مجدد کامل Pod را فعال کند.

بار کاری را در نظر بگیرید که در آن یک sidecar ناظر (watcher) مسئول راه‌اندازی مجدد برنامه اصلی
از یک وضعیت سالم شناخته‌شده است، در صورتی که با خطا مواجه شود. ناظر می‌تواند با یک کد مشخص خارج شود
تا راه‌اندازی مجدد کامل و درجای Pod کارگر را فعال کند.

{{% code_sample file="pods/restart-policy/restart-all-containers.yaml" %}}

در این مثال:

- مقدار کلی `restartPolicy` برای Pod برابر `Never` است.
- کانتینر `watcher-sidecar` یک فرمان را اجرا می‌کند و سپس با کد `88` خارج می‌شود.
- کد خروج با قاعده مطابقت دارد و عمل `RestartAllContainers` را فعال می‌کند.
- کل Pod، شامل کانتینر init با نام `setup-environment` و کانتینر `main-application`،
  سپس به‌صورت درجا دوباره راه‌اندازی می‌شود. Pod همچنان UID، sandbox، IP و حجم‌های (volumeهای) خود را حفظ می‌کند.

### کاهش تأخیر راه‌اندازی مجدد کانتینر

{{< feature-state
feature_gate_name="ReduceDefaultCrashLoopBackOffDecay" >}}

با فعال بودن feature gate آلفای `ReduceDefaultCrashLoopBackOffDecay`،
تلاش‌های مجدد برای راه‌اندازی کانتینر در سراسر کلاستر شما کاهش می‌یابد و از ۱ ثانیه
(به‌جای ۱۰ ثانیه) آغاز می‌شود و در هر راه‌اندازی مجدد به‌صورت نمایی با ضریب ۲ افزایش می‌یابد تا به حداکثر
تأخیر ۶۰ ثانیه (به‌جای ۳۰۰ ثانیه، یعنی ۵ دقیقه) برسد.

اگر از این قابلیت همراه با قابلیت آلفای
`KubeletCrashLoopBackOffMax` (که در ادامه توضیح داده می‌شود) استفاده کنید، نودهای مختلف ممکن است
حداکثر تأخیرهای متفاوتی داشته باشند.

### تأخیر راه‌اندازی مجدد کانتینر قابل پیکربندی

{{< feature-state feature_gate_name="KubeletCrashLoopBackOffMax" >}}

با فعال بودن feature gate با نام `KubeletCrashLoopBackOffMax`، می‌توانید
حداکثر تأخیر بین تلاش‌های مجدد راه‌اندازی کانتینر را که به‌طور پیش‌فرض
۳۰۰ ثانیه (۵ دقیقه) است، دوباره پیکربندی کنید. این پیکربندی برای هر نود و با استفاده از پیکربندی kubelet تنظیم می‌شود. در
[پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) خود،
زیر `crashLoopBackOff` فیلد `maxContainerRestartPeriod` را بین `"1s"` و
`"300s"` تنظیم کنید. همان‌طور که در بالا در [سیاست راه‌اندازی مجدد کانتینر](#restart-policy) توضیح داده شد،
تأخیرها روی آن نود همچنان از ۱۰ ثانیه شروع می‌شوند و در هر راه‌اندازی مجدد به‌صورت نمایی با ضریب ۲ افزایش می‌یابند،
اما اکنون به حداکثر پیکربندی‌شده‌ی شما محدود می‌شوند. اگر
مقدار `maxContainerRestartPeriod` که پیکربندی می‌کنید کمتر از مقدار اولیه پیش‌فرض
۱۰ ثانیه باشد، تأخیر اولیه به‌جای آن روی حداکثر پیکربندی‌شده تنظیم خواهد شد.

نمونه‌های پیکربندی kubelet زیر را ببینید:

```yaml
# container restart delays will start at 10s, increasing
# 2x each time they are restarted, to a maximum of 100s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "100s"
```

```yaml
# delays between container restarts will always be 2s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "2s"
```

اگر از این قابلیت همراه با قابلیت آلفای
`ReduceDefaultCrashLoopBackOffDecay` (که در بالا توضیح داده شد) استفاده کنید، مقادیر پیش‌فرض کلاستر شما
برای عقب‌نشینی اولیه و حداکثر عقب‌نشینی دیگر ۱۰ ثانیه و ۳۰۰ ثانیه نخواهند بود، بلکه ۱ ثانیه
و ۶۰ ثانیه خواهند بود. پیکربندی هر نود بر مقادیر پیش‌فرض تعیین‌شده توسط
`ReduceDefaultCrashLoopBackOffDecay` اولویت دارد، حتی اگر این امر باعث شود یک نود
حداکثر عقب‌نشینی بلندتری نسبت به سایر نودهای کلاستر داشته باشد.

## شرایط Pod (Pod conditions) {#pod-conditions}

یک Pod دارای PodStatus است که شامل آرایه‌ای از
[PodConditions](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podcondition-v1-core)
است که Pod از آن‌ها عبور کرده یا نکرده است. kubelet
PodConditionهای زیر را مدیریت می‌کند:

* `PodScheduled`: Pod به یک نود زمان‌بندی شده است.
* `PodReadyToStartContainers`: sandbox مربوط به Pod با موفقیت ایجاد شده،
  شبکه پیکربندی شده، حجم‌های ذخیره‌سازی مونت شده‌اند و هر منبع پویا (در صورت درخواست) تخصیص یافته است.
* `ContainersReady`: همه کانتینرهای Pod آماده هستند.
* `Initialized`: همه [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/)
  با موفقیت تکمیل شده‌اند.
* `Ready`: Pod قادر به پاسخ‌گویی به درخواست‌ها است و باید به مجموعه‌های توزیع بار
  همه Serviceهای منطبق افزوده شود.
* `DisruptionTarget`: Pod در آستانه خاتمه‌یافتن به‌دلیل یک اختلال (مانند preemption، eviction یا garbage-collection) است.
* `PodResizePending`: تغییر اندازه Pod درخواست شده اما قابل اعمال نیست. [وضعیت تغییر اندازه Pod](/docs/tasks/configure-pod-container/resize-container-resources#pod-resize-status) را ببینید.
* `PodResizeInProgress`: Pod در حال تغییر اندازه است. [وضعیت تغییر اندازه Pod](/docs/tasks/configure-pod-container/resize-container-resources#pod-resize-status) را ببینید.

نام فیلد             | توضیح
:--------------------|:-----------
`type`               | نام این شرط Pod.
`status`             | نشان می‌دهد که آیا آن شرط قابل اعمال است یا خیر؛ مقادیر ممکن "`True`"، "`False`" یا "`Unknown`" هستند.
`lastProbeTime`      | مهر زمانی آخرین باری که شرط Pod بررسی (probe) شده است.
`lastTransitionTime` | مهر زمانی آخرین باری که Pod از یک وضعیت به وضعیت دیگر گذار کرده است.
`reason`             | متن قابل‌خواندن برای ماشین، با قالب UpperCamelCase، که دلیل آخرین گذار شرط را نشان می‌دهد.
`message`            | پیام قابل‌خواندن برای انسان که جزئیات آخرین گذار وضعیت را نشان می‌دهد.

### آمادگی Pod {#pod-readiness-gate}

{{< feature-state for_k8s_version="v1.14" state="stable" >}}

برنامه شما می‌تواند بازخورد یا سیگنال‌های اضافی را به PodStatus تزریق کند:
_آمادگی Pod_. برای استفاده از این قابلیت، `readinessGates` را در `spec` مربوط به Pod تنظیم کنید تا
فهرستی از شرایط اضافی را که kubelet برای آمادگی Pod ارزیابی می‌کند مشخص نمایید.

readiness gateها بر اساس وضعیت فعلی فیلدهای `status.condition`
مربوط به Pod تعیین می‌شوند. اگر کوبرنتیز نتواند چنین شرطی را در فیلد
`status.conditions` یک Pod پیدا کند، وضعیت آن شرط
به‌طور پیش‌فرض "`False`" در نظر گرفته می‌شود.

در اینجا یک مثال آمده است:

```yaml
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

شرایط Podی که اضافه می‌کنید باید نام‌هایی داشته باشند که با
[قالب کلید برچسب](/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set) کوبرنتیز سازگار باشد.

### وضعیت آمادگی Pod {#pod-readiness-status}

دستور `kubectl patch` از اعمال patch بر روی وضعیت (status) آبجکت پشتیبانی نمی‌کند.
برای تنظیم این `status.conditions` در Pod، برنامه‌ها و
{{< glossary_tooltip term_id="operator-pattern" text="اپراتورها">}} باید از
عملیات `PATCH` استفاده کنند.
می‌توانید از یک [کتابخانه کلاینت کوبرنتیز](/docs/reference/using-api/client-libraries/) برای
نوشتن کدی استفاده کنید که شرط‌های سفارشی Pod را برای آمادگی Pod تنظیم می‌کند.

برای Podی که از شرط‌های سفارشی استفاده می‌کند، آن Pod **تنها** زمانی آماده ارزیابی می‌شود
که هر دو گزارهٔ زیر برقرار باشند:

* همهٔ کانتینرهای Pod آماده باشند.
* همهٔ شرط‌های مشخص‌شده در `readinessGates` برابر `True` باشند.

هنگامی که کانتینرهای یک Pod در وضعیت Ready هستند اما دست‌کم یک شرط سفارشی وجود ندارد یا
مقدار آن `False` است، kubelet [شرط](#pod-conditions) Pod را روی `ContainersReady` تنظیم می‌کند.

### آمادگی Pod برای شروع کانتینرها {#pod-ready-to-start-containers}

{{< feature-state for_k8s_version="v1.37" state="stable" >}}

{{< note >}}
در مراحل اولیهٔ توسعه، این شرط `PodHasNetwork` نام داشت.
{{< /note >}}

پس از آنکه یک Pod روی یک نود زمان‌بندی شد، لازم است kubelet آن را بپذیرد (admit کند) و
حجم‌های ذخیره‌سازی مورد نیاز آن مونت شوند. پس از تکمیل این مراحل،
kubelet با یک
container runtime (با استفاده از {{< glossary_tooltip term_id="cri" >}}) همکاری می‌کند تا یک
sandbox زمان اجرا راه‌اندازی کند و شبکه را برای Pod پیکربندی کند. اگر Pod از
[تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/) استفاده کند،
آن منابع نیز در همین مرحله تخصیص داده می‌شوند.
شرط `PodReadyToStartContainers` به فیلد `status.conditions` یک Pod افزوده می‌شود.

kubelet این شرط را زمانی روی `False` تنظیم می‌کند که تشخیص دهد
Pod فاقد یک sandbox زمان اجرا با شبکهٔ پیکربندی‌شده است. این وضعیت در
سناریوهای زیر رخ می‌دهد:

- در اوایل چرخهٔ حیات Pod، زمانی که kubelet هنوز با استفاده از container runtime شروع به راه‌اندازی sandbox
  برای Pod نکرده است.
- در مراحل بعدی چرخهٔ حیات Pod، زمانی که sandbox مربوط به Pod به یکی از دو دلیل زیر از بین رفته باشد:
  - راه‌اندازی مجدد نود، بدون آنکه Pod اخراج (evict) شود
  - برای container runtimeهایی که از ماشین‌های مجازی برای ایزولاسیون استفاده می‌کنند، راه‌اندازی مجدد ماشین مجازی
    sandbox مربوط به Pod، که در نتیجه نیازمند ایجاد یک sandbox جدید و
    پیکربندی تازهٔ شبکهٔ کانتینر است.

پس از اتمام ایجاد sandbox، پیکربندی شبکه، مونت حجم‌ها و (در صورت درخواست) تخصیص پویای منابع،
kubelet شرط `PodReadyToStartContainers` را روی `True` تنظیم می‌کند.
دریافت ایمیج و ایجاد کانتینر پس از این نقطه انجام می‌شوند.

برای Podی که init container دارد، kubelet شرط `Initialized` را پس از
تکمیل موفق init containerها روی `True` تنظیم می‌کند (که پس از
ایجاد موفق sandbox و پیکربندی شبکه توسط افزونهٔ runtime رخ می‌دهد). برای Podی که init container ندارد،
kubelet شرط `Initialized` را پیش از آغاز ایجاد sandbox و پیکربندی شبکه
روی `True` تنظیم می‌کند.

## تغییر اندازهٔ Podها {#pod-resize}

{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}
{{< feature-state feature_gate_name="InPlacePodLevelResourcesVerticalScaling" >}}

کوبرنتیز از تغییر منابع CPU و حافظهٔ تخصیص‌یافته به Podها پس از ایجاد آن‌ها پشتیبانی می‌کند.
(برای سایر منابع زیرساختی، باید از روش‌های متفاوتی که مختص همان منابع است استفاده کنید.)
دو رویکرد اصلی برای تغییر اندازهٔ CPU و حافظه وجود دارد:

### تغییر اندازهٔ درجای Pod {#pod-resize-inplace}

می‌توانید منابع CPU و حافظهٔ سطح کانتینر یک Pod را بدون ایجاد مجدد Pod تغییر دهید.
این روش _مقیاس‌دهی عمودی درجای Pod_ نیز نامیده می‌شود. این قابلیت به شما اجازه می‌دهد تخصیص منابع
کانتینرهای در حال اجرا را تنظیم کنید و در عین حال احتمالاً از اختلال در برنامه جلوگیری شود.

اگر منابع را در سطح Pod مشخص کرده باشید، می‌توانید آن‌ها را نیز به‌صورت درجا تغییر دهید.
برای جزئیات بیشتر، [تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به Podها](/docs/tasks/configure-pod-container/resize-pod-resources/) را ببینید.

برای انجام تغییر اندازهٔ درجا، وضعیت مطلوب Pod را با استفاده از زیرمنبع (subresource) `/resize`
به‌روزرسانی می‌کنید. سپس kubelet تلاش می‌کند مقادیر جدید منابع را بر کانتینرهای
در حال اجرا اعمال کند. {{< glossary_tooltip text="شرط‌های" term_id="condition" >}} Pod
یعنی `PodResizePending` و `PodResizeInProgress` (که در [شرط‌های Pod](#pod-conditions) توضیح داده شده‌اند)
وضعیت عملیات تغییر اندازه را نشان می‌دهند. برای جزئیات بیشتر دربارهٔ وضعیت تغییر اندازه، به
[وضعیت تغییر اندازهٔ کانتینر](/docs/tasks/configure-pod-container/resize-container-resources/#container-resize-status) مراجعه کنید.

نکات کلیدی دربارهٔ تغییر اندازهٔ درجا:
- تنها منابع CPU و حافظه را می‌توان به‌صورت درجا تغییر اندازه داد.
- [کلاس کیفیت سرویس (QoS)](/docs/concepts/workloads/pods/pod-qos/) مربوط به Pod
  هنگام ایجاد تعیین می‌شود و با تغییر اندازه قابل تغییر نیست.
- می‌توانید با استفاده از `resizePolicy` در مشخصات کانتینر پیکربندی کنید که آیا برای تغییر اندازه
  راه‌اندازی مجدد کانتینر لازم است یا خیر.

برای دستورالعمل‌های دقیق دربارهٔ انجام تغییر اندازهٔ درجا، به
[تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/) مراجعه کنید.

### تغییر اندازه با راه‌اندازی Podهای جایگزین

رویکرد بومی‌تر در فضای ابری (cloud native) برای تغییر منابع یک Pod، استفاده از
منبع بار کاری است که آن را مدیریت می‌کند (مانند Deployment یا StatefulSet).
وقتی مشخصات منابع را در قالب Pod (Pod template) به‌روزرسانی می‌کنید،
کنترل‌کنندهٔ بار کاری Podهای جدیدی با منابع به‌روزشده ایجاد می‌کند و
Podهای قدیمی را مطابق راهبرد به‌روزرسانی خود خاتمه می‌دهد.

این رویکرد:
- با هر نسخهٔ کوبرنتیز کار می‌کند.
- می‌تواند هر بخشی از مشخصات Pod را تغییر دهد، نه فقط منابع را.
- منجر به جایگزینی Pod می‌شود، بنابراین باید بار کاری خود را طوری طراحی کنید که بتواند
  [اختلالات برنامه‌ریزی‌شده](/docs/concepts/workloads/pods/disruptions/) را مدیریت کند. برای کنترل دسترس‌پذیری، استفاده از
  [PodDisruptionBudget](/docs/tasks/run-application/configure-pdb/) را در نظر بگیرید.
- مستلزم آن است که Podهای شما توسط یک منبع بار کاری مدیریت شوند.

همچنین می‌توانید از
[VerticalPodAutoscaler](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
برای مدیریت خودکار پیشنهادها و به‌روزرسانی‌های منابع Pod استفاده کنید.

## پروب‌های کانتینر {#container-probes}

کوبرنتیز به شما اجازه می‌دهد _پروب‌هایی_ (probes) تعریف کنید تا سلامت کانتینرهای یک Pod
به‌طور مداوم پایش شود. پروب یک بررسی تشخیصی است که به‌صورت دوره‌ای
توسط {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} روی یک کانتینر انجام می‌شود.
برای انجام این بررسی، kubelet یا کدی را درون
کانتینر اجرا می‌کند یا یک درخواست شبکه‌ای ارسال می‌کند.

بر اساس نتایج پروب، کوبرنتیز می‌تواند کانتینرهای ناسالم را راه‌اندازی مجدد کند
یا ارسال ترافیک به کانتینرهایی را که آماده نیستند متوقف کند.

kubelet می‌تواند به‌صورت اختیاری سه نوع پروب را روی کانتینرهای در حال اجرا اجرا کند و به نتایج آن‌ها واکنش نشان دهد،
که هر کدام هدف متفاوتی را دنبال می‌کنند. برای آگاهی از سازوکارهای پروب (`exec`،
`grpc`، `httpGet`، `tcpSocket`)، فیلدهای پیکربندی و راهنمای کاربردی تفصیلی،
[پروب‌های Liveness، Readiness و Startup](/docs/concepts/workloads/pods/probes/) را ببینید.

### پروب Startup {#startup-probe}

پروب‌های Startup بررسی می‌کنند که آیا برنامهٔ درون یک کانتینر راه‌اندازی شده است یا خیر.
اگر یک پروب Startup پیکربندی شده باشد، کوبرنتیز تا زمانی که پروب Startup موفق نشود، پروب‌های Liveness یا
Readiness را اجرا نمی‌کند، و به این ترتیب به برنامه فرصت می‌دهد
مقداردهی اولیهٔ خود را به پایان برساند.

برخلاف پروب‌های Liveness و Readiness که به‌صورت دوره‌ای اجرا می‌شوند،
این نوع پروب تنها در زمان راه‌اندازی اجرا می‌شود.

اگر پروب Startup شکست بخورد، kubelet کانتینر را متوقف (kill) می‌کند و کانتینر
تابع [سیاست راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) خود قرار می‌گیرد.

### پروب Liveness {#liveness-probe}

پروب‌های Liveness تعیین می‌کنند که چه زمانی یک کانتینر باید راه‌اندازی مجدد شود.
برای مثال، پروب‌های Liveness می‌توانند deadlock را تشخیص دهند، یعنی وضعیتی که در آن برنامه
در حال اجراست اما قادر به پیشرفت نیست. راه‌اندازی مجدد کانتینر در چنین وضعیتی
می‌تواند با وجود باگ‌ها به دسترس‌پذیری بیشتر برنامه کمک کند.

اگر یک کانتینر بیش از حد تحمل پیکربندی‌شده در پروب Liveness شکست بخورد،
kubelet آن کانتینر را راه‌اندازی مجدد می‌کند.
پروب‌های Liveness منتظر موفقیت پروب‌های Readiness نمی‌مانند. اگر می‌خواهید پیش از اجرای پروب Liveness
مدتی صبر شود، می‌توانید یا `initialDelaySeconds` را تعریف کنید یا از یک پروب Startup استفاده کنید.

### پروب Readiness {#readiness-probe}

پروب‌های Readiness تعیین می‌کنند که چه زمانی یک کانتینر برای پذیرش ترافیک آماده است.
این پروب‌ها زمانی مفیدند که باید منتظر ماند تا برنامه کارهای اولیهٔ زمان‌بر خود را انجام دهد،
مانند برقراری اتصال‌های شبکه، بارگذاری فایل‌ها و گرم کردن
کش‌ها (cache).
پروب‌های Readiness در مراحل بعدی چرخهٔ حیات کانتینر نیز می‌توانند مفید باشند،
برای مثال هنگام بازیابی از خطاهای موقت یا بار بیش از حد.

اگر پروب Readiness وضعیت ناموفق برگرداند،
کنترل‌کنندهٔ {{< glossary_tooltip text="EndpointSlice" term_id="endpoint-slice" >}}
نشانی IP مربوط به Pod را از EndpointSliceهای همهٔ Serviceهایی که
با آن Pod مطابقت دارند حذف می‌کند.

پروب‌های Readiness در تمام طول چرخهٔ حیات کانتینر روی آن اجرا می‌شوند.

## خاتمه یافتن Podها {#pod-termination}

از آنجا که Podها نمایانگر فرایندهایی هستند که روی نودهای کلاستر اجرا می‌شوند، مهم است که
به آن فرایندها اجازه داده شود وقتی دیگر لازم نیستند به‌صورت آرام (graceful) خاتمه یابند (به‌جای
آنکه ناگهان با سیگنال `KILL` متوقف شوند و فرصتی برای پاک‌سازی نداشته باشند).

هدف طراحی این است که بتوانید درخواست حذف بدهید و بدانید فرایندها چه زمانی
خاتمه می‌یابند، و همچنین بتوانید اطمینان حاصل کنید که حذف‌ها در نهایت کامل می‌شوند.
وقتی حذف یک Pod را درخواست می‌کنید، کلاستر مهلت آرام‌سازی (grace period) موردنظر را پیش از آنکه اجازهٔ
kill اجباری Pod داده شود ثبت و پیگیری می‌کند. با وجود این پیگیری خاتمهٔ اجباری،
{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} تلاش می‌کند
خاموشی آرام را انجام دهد.

معمولاً در این خاتمهٔ آرامِ Pod، kubelet از container runtime درخواست می‌کند
که با ارسال سیگنال TERM (که SIGTERM هم نامیده می‌شود) همراه با یک مهلت زمانی آرام‌سازی
به فرایند اصلی هر کانتینر، تلاش کند کانتینرهای Pod را متوقف کند.
درخواست‌های توقف کانتینرها توسط container runtime به‌صورت ناهمگام (asynchronous) پردازش می‌شوند.
هیچ تضمینی برای ترتیب پردازش این درخواست‌ها وجود ندارد.
بسیاری از container runtimeها مقدار `STOPSIGNAL` تعریف‌شده در ایمیج کانتینر را رعایت می‌کنند و
در صورت متفاوت بودن، به‌جای TERM سیگنال STOPSIGNAL پیکربندی‌شده در ایمیج کانتینر را ارسال می‌کنند.
پس از سپری شدن مهلت آرام‌سازی، سیگنال KILL به هر فرایند باقی‌مانده ارسال می‌شود
و سپس Pod از
{{< glossary_tooltip text="API Server" term_id="kube-apiserver" >}} حذف می‌شود. اگر kubelet یا
سرویس مدیریتی container runtime هنگام انتظار برای خاتمهٔ فرایندها راه‌اندازی مجدد شود،
کلاستر از ابتدا و با در نظر گرفتن کل مهلت آرام‌سازی اولیه دوباره تلاش می‌کند.

### سیگنال‌های توقف {#pod-termination-stop-signals}

سیگنال توقفی که برای kill کردن کانتینر استفاده می‌شود را می‌توان در ایمیج کانتینر با دستور `STOPSIGNAL` تعریف کرد.
اگر هیچ سیگنال توقفی در ایمیج تعریف نشده باشد، از سیگنال پیش‌فرض container runtime
(SIGTERM برای هر دوی containerd و CRI-O) برای kill کردن کانتینر استفاده می‌شود.

### تعریف سیگنال‌های توقف سفارشی {#defining-custom-stop-signals}

{{< feature-state feature_gate_name="ContainerStopSignals" >}}

اگر feature gate با نام `ContainerStopSignals` فعال باشد، می‌توانید یک سیگنال توقف سفارشی
برای کانتینرهای خود از طریق Lifecycle کانتینر پیکربندی کنید. برای تعریف سیگنال‌های توقف در lifecycle کانتینر،
لازم است فیلد `spec.os.name` در Pod وجود داشته باشد.
فهرست سیگنال‌های معتبر به سیستم‌عاملی بستگی دارد که Pod روی آن زمان‌بندی می‌شود.
برای Podهایی که روی نودهای Windows زمان‌بندی می‌شوند، تنها SIGTERM و SIGKILL به‌عنوان سیگنال معتبر پشتیبانی می‌شوند.

در اینجا نمونه‌ای از مشخصات Pod با تعریف یک سیگنال توقف سفارشی آمده است:

```yaml
spec:
  os:
    name: linux
  containers:
    - name: my-container
      image: container-image:latest
      lifecycle:
        stopSignal: SIGUSR1
```

اگر یک سیگنال توقف در lifecycle تعریف شده باشد، این سیگنال بر سیگنال تعریف‌شده در ایمیج کانتینر اولویت خواهد داشت.
اگر هیچ سیگنال توقفی در مشخصات کانتینر تعریف نشده باشد، کانتینر به رفتار پیش‌فرض بازمی‌گردد.

### جریان خاتمهٔ Pod {#pod-termination-flow}

جریان خاتمهٔ Pod، با یک مثال:

1. با استفاده از ابزار `kubectl` یک Pod مشخص را به‌صورت دستی و با مهلت آرام‌سازی پیش‌فرض
   (۳۰ ثانیه) حذف می‌کنید.

1. Pod در API server با زمانی که پس از آن Pod «مرده» در نظر گرفته می‌شود
   به‌همراه مهلت آرام‌سازی به‌روزرسانی می‌شود.
   اگر برای بررسی Podی که در حال حذف آن هستید از `kubectl describe` استفاده کنید، آن Pod با وضعیت «Terminating» نمایش داده می‌شود.
   روی نودی که Pod در آن اجرا می‌شود: به‌محض آنکه kubelet می‌بیند Pod به‌عنوان
   در حال خاتمه علامت‌گذاری شده است (مدت خاموشی آرام تعیین شده است)، kubelet فرایند محلی
   خاموشی Pod را آغاز می‌کند.

   1. اگر یکی از کانتینرهای Pod یک `preStop`
      [hook](/docs/concepts/containers/container-lifecycle-hooks) تعریف کرده باشد و مقدار `terminationGracePeriodSeconds`
      در مشخصات Pod روی 0 تنظیم نشده باشد، kubelet آن hook را درون کانتینر اجرا می‌کند.
      مقدار پیش‌فرض تنظیم `terminationGracePeriodSeconds` برابر ۳۰ ثانیه است.

      اگر hook از نوع `preStop` پس از انقضای مهلت آرام‌سازی همچنان در حال اجرا باشد، kubelet
      یک تمدید کوچک و یک‌باره ۲ ثانیه‌ای برای مهلت آرام‌سازی درخواست می‌کند.

   {{% note %}}
   اگر hook از نوع `preStop` برای تکمیل به زمانی بیش از مهلت آرام‌سازی پیش‌فرض نیاز دارد،
   باید `terminationGracePeriodSeconds` را متناسب با آن تغییر دهید.
   {{% /note %}}

   1. kubelet container runtime را وادار می‌کند که سیگنال TERM را به فرایند شمارهٔ ۱ درون هر
      کانتینر ارسال کند.

      اگر Pod دارای {{< glossary_tooltip text="کانتینرهای sidecar" term_id="sidecar-container" >}} تعریف‌شده باشد،
      یک [ترتیب ویژه](#termination-with-sidecars) اعمال می‌شود.
      در غیر این صورت، کانتینرهای Pod سیگنال TERM را در زمان‌های متفاوت و با
      ترتیبی دلخواه دریافت می‌کنند. اگر ترتیب خاموش شدن اهمیت دارد، استفاده از یک hook از نوع `preStop`
      برای همگام‌سازی را در نظر بگیرید (یا به استفاده از کانتینرهای sidecar روی آورید).

1. همزمان با آغاز خاموشی آرام Pod توسط kubelet، control plane
   ارزیابی می‌کند که آیا Podِ در حال خاموش شدن باید از آبجکت‌های EndpointSlice حذف شود،
   آبجکت‌هایی که نمایانگر یک {{< glossary_tooltip term_id="service" text="Service" >}}
   دارای {{< glossary_tooltip text="انتخابگر (selector)" term_id="selector" >}} پیکربندی‌شده هستند.
   {{< glossary_tooltip text="ReplicaSetها" term_id="replica-set" >}} و سایر منابع بار کاری
   دیگر Podِ در حال خاموش شدن را به‌عنوان یک replica معتبر و در حال سرویس‌دهی در نظر نمی‌گیرند.

   Podهایی که به‌کندی خاموش می‌شوند نباید به سرویس‌دهی به ترافیک عادی ادامه دهند و باید شروع به
   خاتمه کنند و پردازش اتصال‌های باز را به پایان برسانند. برخی برنامه‌ها فراتر از
   تکمیل اتصال‌های باز به خاتمهٔ آرام‌تری نیاز دارند، برای مثال تخلیه و
   تکمیل نشست‌ها (session draining and completion).

   هر endpoint که نمایانگر Podهای در حال خاتمه باشد بلافاصله از
   EndpointSliceها حذف نمی‌شود، و وضعیتی که نشان‌دهندهٔ [حالت در حال خاتمه](/docs/concepts/services-networking/endpoint-slices/#conditions)
   است از طریق API مربوط به EndpointSlice در دسترس قرار می‌گیرد.
   Endpointهای در حال خاتمه همیشه وضعیت `ready` خود را `false` دارند (برای سازگاری با نسخه‌های
   قبل از 1.26)، بنابراین load balancerها از آن‌ها برای ترافیک عادی استفاده نخواهند کرد.

   اگر تخلیهٔ ترافیک روی Podِ در حال خاتمه لازم باشد، آمادگی واقعی را می‌توان از طریق شرط
   `serving` بررسی کرد. جزئیات بیشتر دربارهٔ نحوهٔ پیاده‌سازی تخلیهٔ اتصال‌ها را می‌توانید در
   آموزش [جریان خاتمهٔ Podها و Endpointها](/docs/tutorials/services/pods-and-endpoint-termination-flow/) بیابید.

   <a id="pod-termination-beyond-grace-period" />

1. kubelet اطمینان حاصل می‌کند که Pod خاموش و خاتمه یافته است

   1. هنگامی که مهلت آرام‌سازی به پایان می‌رسد، اگر هنوز کانتینری در Pod در حال اجرا باشد،
      kubelet خاموشی اجباری را آغاز می‌کند.
      container runtime سیگنال `SIGKILL` را به همهٔ فرایندهایی که هنوز در هر کانتینر Pod در حال اجرا هستند ارسال می‌کند.
      kubelet همچنین در صورتی که container runtime از یک کانتینر پنهان `pause` استفاده کند، آن را پاک‌سازی می‌کند.
   1. kubelet، Pod را به یک فاز نهایی (`Failed` یا `Succeeded` بسته به
      وضعیت پایانی کانتینرهای آن) منتقل می‌کند.
   1. kubelet با تنظیم مهلت آرام‌سازی روی 0 (حذف فوری)، حذف اجباری آبجکت Pod را از API server آغاز می‌کند.
   1. API server آبجکت API مربوط به Pod را حذف می‌کند و دیگر از هیچ کلاینتی قابل مشاهده نیست.

### حذف اجباری Pod {#pod-termination-forced}

{{< caution >}}
حذف اجباری می‌تواند برای برخی بارهای کاری و Podهای آن‌ها مخرب باشد.
{{< /caution >}}

به‌صورت پیش‌فرض، تمام عملیات حذف ظرف ۳۰ ثانیه و به‌صورت graceful انجام می‌شود. دستور `kubectl delete`
از گزینه `--grace-period=<seconds>` پشتیبانی می‌کند که به شما امکان می‌دهد مقدار پیش‌فرض را
نادیده بگیرید و مقدار دلخواه خود را مشخص کنید.

تنظیم مهلت graceful روی `0` باعث می‌شود Pod به‌صورت اجباری و بلافاصله از API server حذف شود.
اگر Pod هنوز روی یک نود در حال اجرا باشد، این حذف اجباری باعث می‌شود kubelet
پاک‌سازی فوری را آغاز کند.

هنگام استفاده از kubectl، برای انجام حذف اجباری باید علاوه بر `--grace-period=0`،
فلگ `--force` را نیز مشخص کنید.

هنگامی که حذف اجباری انجام می‌شود، API server منتظر تأیید kubelet مبنی بر خاتمه یافتن Pod
روی نودی که در آن اجرا می‌شد نمی‌ماند. API server بلافاصله Pod را از API حذف می‌کند تا بتوان
Pod جدیدی با همان نام ایجاد کرد. روی نود، Podهایی که قرار است بلافاصله خاتمه یابند
همچنان پیش از کشته‌شدن اجباری، یک مهلت graceful کوتاه دریافت می‌کنند.

{{< caution >}}
حذف فوری منتظر تأیید خاتمه یافتن منبع در حال اجرا نمی‌ماند.
ممکن است منبع مذکور برای مدت نامحدود در کلاستر به اجرا ادامه دهد.
{{< /caution >}}

اگر نیاز دارید Podهایی را که بخشی از یک StatefulSet هستند به‌صورت اجباری حذف کنید، به مستندات وظیفه
[حذف Podها از یک StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/)
مراجعه کنید.

### خاموش شدن Pod و کانتینرهای sidecar {#termination-with-sidecars}

اگر Pod شما شامل یک یا چند
[کانتینر sidecar](/docs/concepts/workloads/pods/sidecar-containers/)
(کانتینرهای init با سیاست راه‌اندازی مجدد `Always`) باشد، kubelet ارسال سیگنال TERM به این کانتینرهای sidecar را
تا زمانی که آخرین کانتینر اصلی به‌طور کامل خاتمه نیافته است به تأخیر می‌اندازد.
کانتینرهای sidecar به ترتیب معکوسِ تعریف‌شدنشان در spec مربوط به Pod خاتمه داده می‌شوند.
این کار تضمین می‌کند که کانتینرهای sidecar تا زمانی که دیگر به آن‌ها نیازی نیست، به سرویس‌دهی به سایر کانتینرهای Pod ادامه دهند.

این بدان معناست که کند بودن خاتمه یک کانتینر اصلی، خاتمه کانتینرهای sidecar را نیز به تأخیر می‌اندازد.
اگر مهلت graceful پیش از تکمیل فرایند خاتمه به پایان برسد، ممکن است Pod وارد [خاتمه اجباری](#pod-termination-beyond-grace-period) شود.
در این حالت، تمام کانتینرهای باقی‌مانده در Pod به‌طور هم‌زمان و با یک مهلت graceful کوتاه خاتمه داده می‌شوند.

به‌طور مشابه، اگر Pod دارای یک hook از نوع `preStop` باشد که از مهلت graceful خاتمه فراتر رود، ممکن است خاتمه اضطراری رخ دهد.
به‌طور کلی، اگر پیش‌تر برای کنترل ترتیب خاتمه بدون کانتینرهای sidecar از hookهای `preStop` استفاده کرده‌اید، اکنون می‌توانید
آن‌ها را حذف کنید و اجازه دهید kubelet خاتمه sidecarها را به‌طور خودکار مدیریت کند.

### پاک‌سازی (Garbage collection) Podها {#pod-garbage-collection}

برای Podهای ناموفق، آبجکت‌های API تا زمانی که یک انسان یا یک فرایند
{{< glossary_tooltip term_id="controller" text="کنترل‌کننده" >}}
آن‌ها را به‌صراحت حذف نکند، در API کلاستر باقی می‌مانند.

پاک‌سازی‌کننده Pod (PodGC) که یک کنترل‌کننده در control plane است، Podهای خاتمه‌یافته
(با فاز `Succeeded` یا `Failed`) را زمانی که تعداد Podها از آستانه پیکربندی‌شده
(که با `terminated-pod-gc-threshold` در kube-controller-manager تعیین می‌شود) فراتر رود، پاک‌سازی می‌کند.
این کار از نشت منابع در حین ایجاد و خاتمه Podها در طول زمان جلوگیری می‌کند.

علاوه بر این، PodGC هر Podی را که یکی از شرایط زیر را داشته باشد پاک‌سازی می‌کند:

1. Podهای یتیم (orphan) باشند؛ یعنی به نودی متصل باشند که دیگر وجود ندارد،
1. Podهای در حال خاتمه‌ای باشند که زمان‌بندی نشده‌اند،
1. Podهای در حال خاتمه‌ای باشند که به یک نود غیرآماده با taint
   [`node.kubernetes.io/out-of-service`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-out-of-service) متصل هستند.

PodGC همراه با پاک‌سازی Podها، آن‌ها را در صورتی که در فاز غیرنهایی باشند، به‌عنوان ناموفق (failed) علامت‌گذاری می‌کند.
همچنین PodGC هنگام پاک‌سازی یک Pod یتیم، یک condition اختلال Pod اضافه می‌کند.
برای جزئیات بیشتر به [Pod disruption conditions](/docs/concepts/workloads/pods/disruptions#pod-disruption-conditions) مراجعه کنید.

## رفتار Pod هنگام راه‌اندازی مجدد kubelet {#kubelet-restarts}

اگر kubelet را راه‌اندازی مجدد کنید، Podها (و کانتینرهای آن‌ها) حتی در طول راه‌اندازی مجدد
به اجرا ادامه می‌دهند.
هنگامی که Podهایی در حال اجرا روی یک نود وجود دارند، متوقف کردن یا راه‌اندازی مجدد kubelet
روی آن نود باعث **نمی‌شود** که kubelet پیش از متوقف شدن خودش، تمام Podهای محلی را متوقف کند.
برای متوقف کردن Podهای یک نود می‌توانید از `kubectl drain` استفاده کنید.

### تشخیص راه‌اندازی مجدد kubelet

{{< feature-state feature_gate_name="ChangeContainerStatusOnKubeletRestart" >}}

هنگامی که kubelet شروع به کار می‌کند، بررسی می‌کند که آیا از قبل Nodeی با Podهای متصل وجود دارد یا خیر.
اگر [condition با نام `Ready`](/docs/reference/node/node-status/#condition) مربوط به نود بدون تغییر بماند،
به عبارت دیگر از true به false تغییر وضعیت نداده باشد، کوبرنتیز آن را به‌عنوان _راه‌اندازی مجدد kubelet_ تشخیص می‌دهد.
(امکان راه‌اندازی مجدد kubelet به روش‌های دیگر نیز وجود دارد، برای مثال برای رفع یک اشکال نود،
اما در این موارد کوبرنتیز گزینه ایمن را انتخاب می‌کند و با آن مانند حالتی رفتار می‌کند که
kubelet را متوقف کرده‌اید و سپس بعداً آن را راه‌اندازی کرده‌اید).

هنگامی که kubelet راه‌اندازی مجدد می‌شود، وضعیت کانتینرها بسته به تنظیم feature gate به شکل متفاوتی مدیریت می‌شود:

* به‌صورت پیش‌فرض، kubelet پس از راه‌اندازی مجدد، وضعیت کانتینرها را تغییر نمی‌دهد.
  کانتینرهایی که روی حالت `ready: true` تنظیم شده بودند، آماده باقی می‌مانند.

  اگر kubelet را آن‌قدر متوقف نگه دارید که یک سری بررسی
  [ضربان قلب نود](/docs/concepts/architecture/leases/#node-heart-beats) ناموفق شود،
  و سپس پیش از راه‌اندازی دوباره kubelet صبر کنید، ممکن است کوبرنتیز شروع به تخلیه (evict) کردن Podها از آن Node کند.
  با این حال، حتی با آغاز شدن تخلیه Podها، کوبرنتیز کانتینرهای منفرد آن Podها را با `ready: false` علامت‌گذاری نمی‌کند.
  تخلیه در سطح Pod پس از آن رخ می‌دهد که control plane نود را (به دلیل ناموفق بودن ضربان‌های قلب) با taint
  `node.kubernetes.io/not-ready` علامت‌گذاری کند.

* در کوبرنتیز {{< skew currentVersion >}} می‌توانید رفتار قدیمی را فعال کنید که در آن kubelet پس از هر راه‌اندازی مجدد،
  مقدار `ready` کانتینرها را همواره false قرار می‌دهد.

  این رفتار قدیمی برای مدت طولانی رفتار پیش‌فرض بود، اما برای کاربران کوبرنتیز، به‌ویژه در استقرارهای بزرگ‌مقیاس، مشکل ایجاد می‌کرد.
  اگرچه feature gate امکان بازگشت موقت به این رفتار قدیمی را فراهم می‌کند، پروژه کوبرنتیز توصیه می‌کند در صورت مواجهه با مشکل،
  گزارش اشکال (bug report) ثبت کنید.
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ChangeContainerStatusOnKubeletRestart)
  با نام `ChangeContainerStatusOnKubeletRestart` در آینده حذف خواهد شد.

## {{% heading "whatsnext" %}}

* تجربه عملی کسب کنید در زمینه
  [متصل کردن handlerها به رویدادهای چرخه عمر کانتینر](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/).

* تجربه عملی کسب کنید در زمینه
  [پیکربندی probeهای Liveness، Readiness و Startup](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

* درباره [hookهای چرخه عمر کانتینر](/docs/concepts/containers/container-lifecycle-hooks/) بیشتر بیاموزید.

* درباره [کانتینرهای sidecar](/docs/concepts/workloads/pods/sidecar-containers/) بیشتر بیاموزید.

* برای اطلاعات دقیق درباره وضعیت Pod و کانتینر در API، به مستندات مرجع API
  که [`status`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodStatus) مربوط به Pod را پوشش می‌دهد، مراجعه کنید.

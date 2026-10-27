---
title: پروب‌های Liveness، Readiness و Startup
content_type: concept
weight: 65
math: true
---

<!-- overview -->

کوبرنتیز به شما اجازه می‌دهد _پروب‌هایی_ (probes) تعریف کنید تا سلامت
کانتینرهای یک Pod را به‌طور پیوسته پایش کنید. پروب یک بررسی تشخیصی است که به‌صورت دوره‌ای
توسط {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} روی یک کانتینر انجام می‌شود.
kubelet برای انجام این بررسی تشخیصی یا کدی را درون
کانتینر اجرا می‌کند یا یک درخواست شبکه‌ای ارسال می‌کند.

کوبرنتیز بر اساس نتایج پروب می‌تواند کانتینرهای ناسالم را دوباره راه‌اندازی کند
یا ارسال ترافیک به کانتینرهایی را که آماده نیستند متوقف کند.

<!-- body -->

## انواع پروب {#types-of-probe}

kubelet می‌تواند به‌صورت اختیاری سه نوع پروب را روی کانتینرهای در حال اجرا انجام دهد و
به نتایج آن‌ها واکنش نشان دهد که هر کدام هدف متفاوتی دارند:

- [پروب Startup](#startup-probe)
- [پروب Liveness](#liveness-probe)
- [پروب Readiness](#readiness-probe)

### پروب Startup {#startup-probe}

پروب‌های Startup بررسی می‌کنند که آیا برنامه‌ی درون یک کانتینر راه‌اندازی شده است یا خیر.
اگر یک پروب Startup پیکربندی شده باشد، کوبرنتیز تا زمانی که پروب Startup موفق نشود، پروب‌های Liveness یا
Readiness را اجرا نمی‌کند و بدین ترتیب به برنامه
فرصت می‌دهد مقداردهی اولیه‌ی خود را به پایان برساند.

این نوع پروب برخلاف پروب‌های Liveness و Readiness که به‌صورت دوره‌ای اجرا می‌شوند،
تنها در هنگام راه‌اندازی اجرا می‌شود.
اگر پروب Startup شکست بخورد، kubelet کانتینر را از بین می‌برد و کانتینر
تابع [سیاست راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) خود می‌شود.

### پروب Liveness {#liveness-probe}

پروب‌های Liveness تعیین می‌کنند که چه زمانی یک کانتینر باید دوباره راه‌اندازی شود.
برای مثال، پروب‌های Liveness می‌توانند بن‌بست (deadlock) را تشخیص دهند؛ وضعیتی که در آن برنامه
در حال اجراست اما نمی‌تواند پیشرفتی داشته باشد. راه‌اندازی مجدد کانتینر در چنین وضعیتی
می‌تواند با وجود باگ‌ها به افزایش دسترس‌پذیری برنامه کمک کند.

اگر یک کانتینر بیش از حد تحمل پیکربندی‌شده در پروب Liveness خود شکست بخورد،
kubelet آن کانتینر را دوباره راه‌اندازی می‌کند.
پروب‌های Liveness منتظر موفقیت پروب‌های Readiness نمی‌مانند. اگر می‌خواهید
پیش از اجرای پروب Liveness صبر شود، می‌توانید یا
`initialDelaySeconds` را تعریف کنید یا از یک [پروب Startup](#startup-probe) استفاده کنید.

{{< caution >}}
پروب‌های Liveness می‌توانند روشی قدرتمند برای بازیابی از خرابی‌های برنامه باشند،
اما باید با احتیاط به کار روند.
پروب‌های Liveness باید با دقت پیکربندی شوند تا اطمینان حاصل شود که واقعاً نشان‌دهنده‌ی
خرابی غیرقابل‌بازیابی برنامه، برای مثال یک بن‌بست، هستند.

پیاده‌سازی نادرست پروب‌های Liveness می‌تواند به خرابی‌های زنجیره‌ای منجر شود.
نتیجه‌ی این امر، راه‌اندازی مجدد کانتینر تحت بار زیاد، شکست درخواست‌های کلاینت
به دلیل کاهش مقیاس‌پذیری برنامه، و افزایش بار کاری روی Podهای باقی‌مانده
به دلیل شکست برخی Podها است. تفاوت میان پروب‌های Liveness و
Readiness و زمان مناسب برای به‌کارگیری هر یک در برنامه‌ی خود را درک کنید.
{{< /caution >}}

### پروب Readiness {#readiness-probe}

پروب‌های Readiness تعیین می‌کنند که چه زمانی یک کانتینر آماده‌ی پذیرش ترافیک است.
این کار هنگامی مفید است که منتظر می‌مانید برنامه وظایف اولیه‌ی زمان‌بری
مانند برقراری اتصال‌های شبکه، بارگذاری فایل‌ها و گرم‌کردن
حافظه‌های نهان (cache) را انجام دهد.
پروب‌های Readiness می‌توانند در مراحل بعدی چرخه‌ی عمر کانتینر نیز مفید باشند،
برای مثال هنگام بازیابی از خطاهای موقت یا بار بیش از حد.

اگر پروب Readiness وضعیت شکست را برگرداند، کنترل‌کننده‌ی
{{< glossary_tooltip text="EndpointSlice" term_id="endpoint-slice" >}}
نشانی IP آن Pod را از EndpointSliceهای همه‌ی Serviceهایی که
با Pod منطبق هستند حذف می‌کند.

پروب‌های Readiness در تمام چرخه‌ی عمر کانتینر روی آن اجرا می‌شوند.

{{< note >}}
اگر می‌خواهید هنگام حذف Pod بتوانید درخواست‌ها را تخلیه (drain) کنید،
لزوماً به پروب Readiness نیاز ندارید؛ هنگامی که Pod حذف می‌شود، endpoint متناظر
در EndpointSlice [شرایط](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/#conditions) خود را به‌روزرسانی می‌کند: شرط ready
آن endpoint روی false تنظیم می‌شود، بنابراین متعادل‌کننده‌های بار از آن Pod برای
ترافیک عادی استفاده نمی‌کنند. برای اطلاعات بیشتر درباره‌ی نحوه‌ی رسیدگی kubelet به حذف Pod،
[خاتمه‌ی Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) را ببینید.
{{< /note >}}

## زمان استفاده از هر پروب {#when-to-use-each-probe}

### چه زمانی باید از پروب Startup استفاده کرد؟ {#when-should-you-use-a-startup-probe}

پروب‌های Startup برای Podهایی مفید هستند که کانتینرهایشان زمان زیادی برای
آماده‌شدن به خدمت‌رسانی نیاز دارند. به جای تعیین یک بازه‌ی Liveness طولانی، می‌توانید
پیکربندی جداگانه‌ای برای پروب‌کردن کانتینر در هنگام راه‌اندازی تعیین کنید و
زمانی طولانی‌تر از آنچه بازه‌ی Liveness اجازه می‌دهد در نظر بگیرید.

<!-- ensure front matter contains math: true -->
اگر کانتینر شما معمولاً در زمانی بیش از
\\( initialDelaySeconds + failureThreshold \times  periodSeconds \\) راه‌اندازی می‌شود، باید یک
پروب Startup تعیین کنید که همان endpoint پروب Liveness را بررسی کند. مقدار پیش‌فرض
`periodSeconds` برابر 10s است. سپس باید `failureThreshold` آن را به اندازه‌ی کافی
بزرگ تنظیم کنید تا کانتینر بتواند راه‌اندازی شود، بدون آنکه مقادیر پیش‌فرض
پروب Liveness را تغییر دهید. این کار به محافظت در برابر بن‌بست‌ها کمک می‌کند.

### چه زمانی باید از پروب Liveness استفاده کرد؟ {#when-should-you-use-a-liveness-probe}

اگر فرایند درون کانتینر شما می‌تواند هر زمان که با مشکلی مواجه شد یا
ناسالم شد خودبه‌خود از کار بیفتد، لزوماً به پروب Liveness نیاز ندارید؛
kubelet به‌طور خودکار اقدام درست را مطابق با
`restartPolicy` آن Pod انجام می‌دهد.

اگر می‌خواهید در صورت شکست یک پروب، کانتینر شما از بین برود و دوباره راه‌اندازی شود،
یک پروب Liveness تعیین کنید و `restartPolicy` را روی `Always` یا
`OnFailure` تنظیم کنید.

یک الگوی رایج برای پروب‌های Liveness، استفاده از همان endpoint کم‌هزینه‌ی HTTP
پروب‌های Readiness است، اما با `failureThreshold` بالاتر. این کار تضمین می‌کند
که Pod پیش از آنکه به‌طور قطعی از بین برده شود، برای مدتی در وضعیت not-ready
مشاهده شود.

### چه زمانی باید از پروب Readiness استفاده کرد؟ {#when-should-you-use-a-readiness-probe}

برای اینکه ارسال ترافیک به یک Pod تنها پس از موفقیت یک پروب آغاز شود، یک
پروب Readiness تعیین کنید. پروب Readiness ممکن است با پروب Liveness یکسان باشد،
اما وجود پروب Readiness در spec به این معناست که Pod بدون دریافت هیچ ترافیکی
راه‌اندازی می‌شود و تنها پس از آنکه پروب موفق شد، دریافت ترافیک را آغاز می‌کند.

همچنین می‌توانید از پروب Readiness استفاده کنید تا یک کانتینر بتواند خود را برای
نگهداری از سرویس خارج کند؛ این کار با بررسی endpoint ویژه‌ی Readiness انجام می‌شود که با
endpoint پروب Liveness متفاوت است.

هنگامی که برنامه‌ی شما وابستگی سختی به سرویس‌های پشتیبان (back-end) دارد، می‌توانید
هم پروب Liveness و هم پروب Readiness پیاده‌سازی کنید. پروب Liveness زمانی موفق می‌شود که خود برنامه
سالم باشد، اما پروب Readiness علاوه بر آن بررسی می‌کند که هر
سرویس پشتیبان موردنیاز در دسترس باشد. این کار به شما کمک می‌کند از هدایت ترافیک
به Podهایی که تنها می‌توانند با پیام‌های خطا پاسخ دهند پرهیز کنید.

برای کانتینرهایی که باید در هنگام راه‌اندازی داده‌های حجیم، فایل‌های پیکربندی یا
مهاجرت‌ها (migrations) را بارگذاری کنند، استفاده از یک [پروب Startup](#startup-probe) را در نظر بگیرید.
با این حال، اگر می‌خواهید تفاوت میان برنامه‌ای که شکست خورده
و برنامه‌ای که هنوز در حال پردازش داده‌های راه‌اندازی خود است را تشخیص دهید، ممکن است پروب Readiness را ترجیح دهید.

## سازوکارهای بررسی {#check-mechanisms}

چهار روش مختلف برای بررسی یک کانتینر با استفاده از پروب وجود دارد. هر پروب
باید دقیقاً یکی از این چهار سازوکار را تعریف کند:

`exec`
: یک فرمان مشخص را درون کانتینر اجرا می‌کند. بررسی تشخیصی در صورتی
  موفق در نظر گرفته می‌شود که فرمان با کد وضعیت 0 خاتمه یابد.

`grpc`
: یک فراخوانی رویه‌ی راه دور با استفاده از [gRPC](https://grpc.io/) انجام می‌دهد. هدف
  باید [بررسی‌های سلامت gRPC](https://grpc.io/grpc/core/md_doc_health-checking.html) را پیاده‌سازی کرده باشد.
  بررسی تشخیصی در صورتی موفق در نظر گرفته می‌شود که `status` پاسخ برابر
  `SERVING` باشد. برای جزئیات بیشتر، [پروب‌های gRPC](#grpc-probes) را ببینید.

`httpGet`
: یک درخواست HTTP `GET` به نشانی IP آن Pod روی درگاه (port) و مسیر مشخص‌شده
  ارسال می‌کند. بررسی تشخیصی در صورتی موفق در نظر گرفته می‌شود که پاسخ
  کد وضعیتی بزرگ‌تر یا مساوی 200 و کوچک‌تر از 400 داشته باشد.
  برای جزئیات بیشتر، [پروب‌های HTTP](#http-probes) را ببینید.

`tcpSocket`
: یک بررسی TCP روی نشانی IP آن Pod و درگاه مشخص‌شده انجام می‌دهد.
  بررسی تشخیصی در صورتی موفق در نظر گرفته می‌شود که درگاه باز باشد. اگر سیستم راه دور
  (کانتینر) اتصال را بلافاصله پس از باز شدن ببندد، این وضعیت نیز
  سالم به شمار می‌آید.
  برای جزئیات بیشتر، [پروب‌های TCP](#tcp-probes) را ببینید.

{{< caution >}}
برخلاف سایر سازوکارها، پیاده‌سازی پروب `exec` هر بار که اجرا می‌شود
شامل ایجاد/انشعاب (fork) چندین فرایند است. در نتیجه، در
کلاسترهایی با تراکم Pod بالاتر و بازه‌های کوتاه‌تر
`initialDelaySeconds` و `periodSeconds`، پیکربندی هر پروبی با سازوکار exec
ممکن است سربار قابل‌توجهی بر مصرف CPU نود تحمیل کند. در چنین
سناریوهایی، استفاده از سازوکارهای جایگزین پروب را برای پرهیز از این سربار در نظر بگیرید.
{{< /caution >}}

## نتایج پروب {#probe-results}

kubelet نتیجه‌ی هر اجرای پروب را ارزیابی می‌کند و بر اساس آن
اقدام می‌کند. هر پروب یکی از سه نتیجه‌ی زیر را دارد:

`Success`
: کانتینر بررسی تشخیصی را با موفقیت پشت سر گذاشت.

`Failure`
: کانتینر در بررسی تشخیصی شکست خورد. برای پروب‌های Liveness و Startup،
  kubelet کانتینر را از بین می‌برد و کانتینر تابع
  [سیاست راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) خود می‌شود.
  برای پروب‌های Readiness، kubelet کانتینر را به‌عنوان آماده‌نبودن علامت‌گذاری می‌کند و
  Pod دیگر از Serviceهای منطبق ترافیکی دریافت نمی‌کند.

`Unknown`
: خود بررسی تشخیصی شکست خورد (نباید اقدامی انجام شود و kubelet
  بررسی‌های بیشتری انجام خواهد داد).

اگر یک کانتینر پروب خاصی را ارائه نکند، kubelet همواره
نتیجه را `Success` در نظر می‌گیرد. به‌طور خاص برای پروب‌های Readiness،
نتیجه پیش از سپری‌شدن تأخیر اولیه `Failure` در نظر گرفته می‌شود.

## فیلدهای پیکربندی {#configure-probes}

[پروب‌ها](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#probe-v1-core)
فیلدهای متعددی دارند که می‌توانید با استفاده از آن‌ها رفتار بررسی‌های Startup،
Liveness و Readiness را دقیق‌تر کنترل کنید. برای مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probe-example
spec:
  containers:
  - name: app
    image: registry.k8s.io/e2e-test-images/agnhost:2.40
    ports:
    - containerPort: 8080
    startupProbe:
      httpGet:
        path: /healthz
        port: 8080
      failureThreshold: 30
      periodSeconds: 10
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 5
      timeoutSeconds: 3
      failureThreshold: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      periodSeconds: 5
```

`initialDelaySeconds`
: تعداد ثانیه‌هایی که پس از شروع کانتینر سپری می‌شود تا پروب‌های Startup، Liveness یا Readiness آغاز شوند. اگر یک پروب Startup تعریف شده باشد، تأخیرهای پروب‌های Liveness و Readiness تا زمان موفقیت پروب Startup آغاز نمی‌شوند. در برخی نسخه‌های قدیمی‌تر کوبرنتیز، اگر periodSeconds روی مقداری بزرگ‌تر از initialDelaySeconds تنظیم می‌شد، ممکن بود initialDelaySeconds نادیده گرفته شود. با این حال، در نسخه‌های کنونی، initialDelaySeconds همواره رعایت می‌شود و پروب تا پس از این تأخیر اولیه آغاز نمی‌شود. مقدار پیش‌فرض 0 ثانیه است. حداقل مقدار 0 است.

`periodSeconds`
: فاصله‌ی زمانی (بر حسب ثانیه) میان اجراهای پروب. مقدار پیش‌فرض 10 ثانیه است. حداقل مقدار 1 است. تا زمانی که یک کانتینر Ready نیست، پروب Readiness ممکن است در زمان‌هایی غیر از بازه‌ی پیکربندی‌شده‌ی `periodSeconds` اجرا شود. این کار برای آن است که Pod سریع‌تر آماده شود.

`timeoutSeconds`
: تعداد ثانیه‌هایی که پس از آن مهلت پروب به پایان می‌رسد. مقدار پیش‌فرض 1 ثانیه است. حداقل مقدار 1 است.

`successThreshold`
: حداقل تعداد موفقیت‌های متوالی لازم برای آنکه پروب پس از شکست، موفق در نظر گرفته شود. مقدار پیش‌فرض 1 است. برای پروب‌های Liveness و Startup باید 1 باشد. حداقل مقدار 1 است.

`failureThreshold`
: پس از آنکه یک پروب `failureThreshold` بار پشت سر هم شکست بخورد، کوبرنتیز کل بررسی را شکست‌خورده در نظر می‌گیرد: کانتینر آماده/سالم/زنده _نیست_. مقدار پیش‌فرض 3 است. حداقل مقدار 1 است. در مورد پروب Startup یا Liveness، اگر دست‌کم `failureThreshold` پروب شکست خورده باشند، کوبرنتیز کانتینر را ناسالم تلقی می‌کند و راه‌اندازی مجدد همان کانتینر خاص را آغاز می‌کند. kubelet تنظیم `terminationGracePeriodSeconds` آن کانتینر را رعایت می‌کند. برای یک پروب Readiness شکست‌خورده، kubelet به اجرای کانتینری که در بررسی‌ها شکست خورده ادامه می‌دهد و همچنین به اجرای پروب‌های بیشتر ادامه می‌دهد؛ از آنجا که بررسی شکست خورده است، kubelet [شرط](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) `Ready` را روی Pod برابر `false` تنظیم می‌کند.

`terminationGracePeriodSeconds`
: یک مهلت ملایم (grace period) پیکربندی می‌کند که kubelet میان آغاز خاموش‌کردن کانتینر شکست‌خورده و سپس وادارکردن محیط اجرای کانتینر به متوقف‌کردن آن کانتینر صبر کند. پیش‌فرض این است که مقدار سطح Pod برای `terminationGracePeriodSeconds` به ارث برده شود (در صورت تعیین‌نشدن، 30 ثانیه) و حداقل مقدار 1 است. برای جزئیات بیشتر، [`terminationGracePeriodSeconds` در سطح پروب](#probe-level-terminationgraceperiodseconds) را ببینید.

{{< caution >}}
پیاده‌سازی نادرست پروب‌های Readiness ممکن است به افزایش پیوسته‌ی
تعداد فرایندها در کانتینر و در صورت رسیدگی‌نکردن، به کمبود منابع منجر شود.
{{< /caution >}}

### `terminationGracePeriodSeconds` در سطح پروب {#probe-level-terminationgraceperiodseconds}

{{< feature-state for_k8s_version="v1.28" state="stable" >}}

در نسخه‌ی 1.25 و بالاتر، کاربران می‌توانند `terminationGracePeriodSeconds` را در سطح پروب
به‌عنوان بخشی از مشخصات پروب تعیین کنند. هنگامی که `terminationGracePeriodSeconds`
هم در سطح Pod و هم در سطح پروب تنظیم شده باشد، kubelet از مقدار سطح پروب
استفاده می‌کند.

هنگام تنظیم `terminationGracePeriodSeconds`، به نکات زیر توجه کنید:

* kubelet همواره فیلد `terminationGracePeriodSeconds` در سطح پروب را
  در صورت وجود در یک Pod رعایت می‌کند.
* اگر Podهای موجودی دارید که فیلد `terminationGracePeriodSeconds` در آن‌ها
  تنظیم شده است و دیگر نمی‌خواهید از مهلت‌های ملایم خاتمه به ازای هر پروب استفاده کنید،
  باید آن Podهای موجود را حذف کنید.

برای مثال:

```yaml
spec:
  terminationGracePeriodSeconds: 3600  # pod-level
  containers:
  - name: test
    image: ...

    ports:
    - name: liveness-port
      containerPort: 8080

    livenessProbe:
      httpGet:
        path: /healthz
        port: liveness-port
      failureThreshold: 1
      periodSeconds: 60
      # Override pod-level terminationGracePeriodSeconds
      terminationGracePeriodSeconds: 60
```

`terminationGracePeriodSeconds` در سطح پروب را **نمی‌توان** برای پروب‌های Readiness تنظیم کرد.
API server آن را رد می‌کند.

## جزئیات سازوکارهای پروب {#probe-mechanism-details}

### پروب‌های HTTP {#http-probes}

[پروب‌های HTTP](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#httpgetaction-v1-core)
فیلدهای دیگری نیز دارند که می‌توان روی `httpGet` تنظیم کرد:

* `host`: نام میزبانی که باید به آن متصل شد؛ مقدار پیش‌فرض آن IP آن Pod است. احتمالاً بهتر است
  به جای آن، "Host" را در `httpHeaders` تنظیم کنید.
* `scheme`: طرحی (scheme) که برای اتصال به میزبان استفاده می‌شود (HTTP یا HTTPS). مقدار پیش‌فرض
  "HTTP" است.
* `path`: مسیری که باید روی سرور HTTP به آن دسترسی یافت. مقدار پیش‌فرض "/" است.
* `httpHeaders`: هدرهای سفارشی برای تنظیم در درخواست. HTTP اجازه‌ی تکرار
  هدرها را می‌دهد.
* `port`: نام یا شماره‌ی درگاهی از کانتینر که باید به آن دسترسی یافت. شماره باید
  در بازه‌ی 1 تا 65535 باشد.
* `protocol`: پروتکلی که برای درخواست پروب استفاده می‌شود. مقدار پیش‌فرض `HTTP1` است.
  برای پروب‌کردن از طریق HTTP/2 بدون رمزنگاری (h2c) آن را روی `HTTP2` تنظیم کنید. این کار مستلزم
  فعال‌بودن [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `H2CContainerProbe`
  است.

برای یک پروب HTTP، kubelet برای انجام بررسی یک درخواست HTTP به درگاه و
مسیر مشخص‌شده ارسال می‌کند. kubelet پروب را به نشانی IP آن Pod ارسال می‌کند،
مگر آنکه این نشانی با فیلد اختیاری `host` در `httpGet` جایگزین شده باشد. اگر
فیلد `scheme` روی `HTTPS` تنظیم شده باشد، kubelet یک درخواست HTTPS ارسال می‌کند و
راستی‌آزمایی گواهی را نادیده می‌گیرد. در بیشتر سناریوها، نیازی به تنظیم فیلد
`host` ندارید. در اینجا سناریویی را می‌بینید که در آن باید آن را تنظیم کنید. فرض کنید کانتینر
روی 127.0.0.1 گوش می‌دهد و فیلد `hostNetwork` آن Pod برابر true است. در این صورت `host`
در زیر `httpGet` باید روی 127.0.0.1 تنظیم شود. اگر Pod شما به میزبان‌های
مجازی (virtual hosts) متکی است، که احتمالاً حالت رایج‌تری است، نباید از `host` استفاده کنید، بلکه
باید هدر `Host` را در `httpHeaders` تنظیم کنید.

برای یک پروب HTTP، kubelet علاوه بر هدر الزامی `Host`، دو هدر درخواست دیگر
نیز ارسال می‌کند:

- `User-Agent` که مقدار پیش‌فرض آن `kube-probe/{{< skew currentVersion >}}` است؛
  که در آن `{{< skew currentVersion >}}` نسخه‌ی kubelet است.
- `Accept` که مقدار پیش‌فرض آن `*/*` است.

می‌توانید با تعریف `httpHeaders` برای پروب، این هدرها را بازنویسی کنید.
برای مثال:

```yaml
livenessProbe:
  httpGet:
    httpHeaders:
      - name: Accept
        value: application/json

startupProbe:
  httpGet:
    httpHeaders:
      - name: User-Agent
        value: MyUserAgent
```

همچنین می‌توانید با تعریف این دو هدر با مقدار خالی، آن‌ها را حذف کنید.

```yaml
livenessProbe:
  httpGet:
    httpHeaders:
      - name: Accept
        value: ""

startupProbe:
  httpGet:
    httpHeaders:
      - name: User-Agent
        value: ""
```

{{< feature-state feature_gate_name="H2CContainerProbe" >}}

می‌توانید با تنظیم فیلد `protocol` روی `HTTP2`، یک پروب HTTP را برای استفاده از HTTP/2 بدون رمزنگاری (h2c)
پیکربندی کنید. هنگامی که `protocol` روی `HTTP2` تنظیم شده باشد، kubelet
به جای HTTP/1.1 از h2c (HTTP/2 روی TCP ساده) استفاده می‌کند. مقدار پیش‌فرض `protocol`
برابر `HTTP1` است. تنظیم `protocol: HTTP2` مستلزم `scheme: HTTP` (مقدار پیش‌فرض) است؛
API server ترکیب `protocol: HTTP2` با
`scheme: HTTPS` را رد می‌کند. برای جزئیات بیشتر،
[استفاده از HTTP/2 بدون رمزنگاری (h2c) با پروب‌های HTTP](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#use-h2c-with-http-probes) را ببینید.

#### رسیدگی به تغییر مسیرها {#http-probes-redirects}

هنگامی که kubelet یک کانتینر را با استفاده از HTTP پروب می‌کند، تنها در صورتی تغییر مسیرها (redirects) را دنبال می‌کند که
تغییر مسیر به همان میزبان باشد. این شامل تغییر مسیرهایی نیز می‌شود که
پروتکل را از HTTP به HTTPS تغییر می‌دهند، حتی اگر پروب با
`scheme: HTTP` پیکربندی شده باشد.

اگر تغییر مسیر به نام میزبان دیگری باشد، kubelet آن را دنبال نمی‌کند.
در عوض، kubelet پروب را موفق تلقی می‌کند و یک رویداد
`ProbeWarning` ثبت می‌کند.

اگر kubelet یک تغییر مسیر را دنبال کند و در مجموع 11 تغییر مسیر یا بیشتر دریافت کند، پروب
موفق در نظر گرفته می‌شود و یک رویداد `ProbeWarning` ثبت می‌کند. برای مثال:

```none
Events:
  Type     Reason        Age                     From               Message
  ----     ------        ----                    ----               -------
  Normal   Scheduled     29m                     default-scheduler  Successfully assigned default/httpbin-7b8bc9cb85-bjzwn to daocloud
  Normal   Pulling       29m                     kubelet            Pulling image "docker.io/kennethreitz/httpbin"
  Normal   Pulled        24m                     kubelet            Successfully pulled image "docker.io/kennethreitz/httpbin" in 5m12.402735213s
  Normal   Created       24m                     kubelet            Created container httpbin
  Normal   Started       24m                     kubelet            Started container httpbin
 Warning  ProbeWarning  4m11s (x1197 over 24m)  kubelet            Readiness probe warning: Probe terminated redirects
```

{{< caution >}}
هنگام پردازش یک پروب `httpGet`، kubelet پس از 10KiB خواندن بدنه‌ی پاسخ را متوقف می‌کند.
موفقیت پروب تنها بر اساس کد وضعیت پاسخ تعیین می‌شود که در هدرهای پاسخ قرار دارد.

اگر endpointی را پروب کنید که بدنه‌ی پاسخی بزرگ‌تر از **10KiB** برمی‌گرداند،
kubelet همچنان پروب را بر اساس کد وضعیت موفق علامت‌گذاری می‌کند،
اما پس از رسیدن به حد 10KiB اتصال را می‌بندد.
این بسته‌شدن ناگهانی می‌تواند باعث شود خطاهای **connection reset by peer** یا **broken pipe** در لاگ‌های برنامه‌ی شما ظاهر شوند
که تشخیص آن‌ها از مشکلات واقعی شبکه می‌تواند دشوار باشد.

برای داشتن پروب‌های `httpGet` قابل‌اعتماد، اکیداً توصیه می‌شود از endpointهای اختصاصی بررسی سلامت
استفاده کنید که بدنه‌ی پاسخ حداقلی برمی‌گردانند. اگر ناچارید از endpoint موجودی با محتوای حجیم استفاده کنید،
به جای آن استفاده از یک پروب `exec` را برای انجام یک درخواست HEAD در نظر بگیرید.
{{< /caution >}}

### پروب‌های TCP {#tcp-probes}

برای یک پروب TCP، kubelet اتصال پروب را در سطح نود برقرار می‌کند، نه درون
Pod؛ این بدان معناست که نمی‌توانید از نام یک سرویس در پارامتر `host` استفاده کنید،
زیرا kubelet قادر به تفکیک (resolve) آن نیست.

### پروب‌های gRPC {#grpc-probes}

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

اگر برنامه‌ی شما
[پروتکل بررسی سلامت gRPC](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) را پیاده‌سازی کرده باشد،
می‌توانید کوبرنتیز را طوری پیکربندی کنید که از آن برای بررسی‌های Startup، Liveness یا Readiness برنامه استفاده کند.

در اینجا یک مانیفست نمونه آمده است:

{{% code_sample file="pods/probe/grpc-liveness.yaml" %}}

برای استفاده از پروب gRPC، باید `port` پیکربندی شود. اگر می‌خواهید
پروب‌های انواع مختلف و پروب‌های قابلیت‌های مختلف را از یکدیگر متمایز کنید، می‌توانید
از فیلد `service` استفاده کنید. می‌توانید `service` را روی مقدار `liveness` تنظیم کنید و
endpoint بررسی سلامت gRPC خود را طوری بسازید که به این درخواست پاسخی متفاوت از حالتی بدهد که
`service` را روی `readiness` تنظیم کرده‌اید. این کار به شما امکان می‌دهد از یک endpoint برای
انواع مختلف بررسی سلامت کانتینر استفاده کنید، به جای آنکه روی دو درگاه مختلف
گوش دهید. اگر می‌خواهید نام سرویس سفارشی خود را تعیین کنید و نوع
پروب را نیز مشخص کنید، پروژه‌ی کوبرنتیز توصیه می‌کند از نامی استفاده کنید که
این دو را به هم پیوند می‌دهد. برای مثال: `myservice-liveness` (با استفاده از `-` به‌عنوان جداکننده).

{{< note >}}
برخلاف پروب‌های HTTP یا TCP، نمی‌توانید درگاه بررسی سلامت را با نام آن تعیین کنید
و نمی‌توانید نام میزبان سفارشی پیکربندی کنید.
{{< /note >}}

مشکلات پیکربندی (برای مثال: درگاه یا سرویس نادرست، یا پیاده‌سازی‌نشدن
پروتکل بررسی سلامت)، مشابه پروب‌های HTTP و
TCP، شکست پروب در نظر گرفته می‌شوند.

{{< feature-state feature_gate_name="GRPCContainerProbeTLS" >}}

می‌توانید با تنظیم فیلد `mode` روی `TLS`، یک پروب gRPC را برای اتصال از طریق TLS
پیکربندی کنید. هنگامی که `mode` روی `TLS` تنظیم شده باشد، kubelet از TLS با
`InsecureSkipVerify` استفاده می‌کند (یعنی گواهی سرور را راستی‌آزمایی نمی‌کند). مقدار پیش‌فرض
`mode` برابر `Plaintext` است. برای جزئیات بیشتر،
[استفاده از TLS با پروب‌های gRPC](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#grpc-probe-tls) را ببینید.

## {{% heading "whatsnext" %}}

* بیاموزید چگونه
  [پروب‌های Liveness، Readiness و Startup را پیکربندی کنید](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).
* برای مشخصات کامل فیلدهای مرتبط با پروب، مرجع API را ببینید:
  [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)،
  [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)،
  [Probe](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Probe)

---
reviewers:
- bprashanth
title: Service
api_metadata:
- apiVersion: "v1"
  kind: "Service"
feature:
  title: کشف سرویس و توزیع بار
  description: >
    برای استفاده از یک سازوکار ناآشنای کشف سرویس، نیازی به تغییر برنامهٔ خود ندارید. کوبرنتیز به Podها نشانی‌های IP مخصوص به خودشان و یک نام DNS واحد برای مجموعه‌ای از Podها می‌دهد و می‌تواند بار را میان آن‌ها توزیع کند.
description: >-
  برنامه‌ای را که در کلاستر شما اجرا می‌شود، پشت یک endpoint واحدِ رو به بیرون
  در دسترس قرار دهید، حتی زمانی که بار کاری میان چندین backend تقسیم شده است.
content_type: concept
weight: 10
---


<!-- overview -->

{{< glossary_definition term_id="service" length="short" prepend="In Kubernetes, a Service is" >}}

یکی از اهداف کلیدی Serviceها در کوبرنتیز این است که برای استفاده از یک سازوکار ناآشنای کشف سرویس،
نیازی به تغییر برنامهٔ موجود خود نداشته باشید.
می‌توانید کد را در Podها اجرا کنید، چه این کد برای دنیای cloud-native طراحی شده باشد و چه
برنامه‌ای قدیمی‌تر باشد که آن را کانتینری کرده‌اید. از یک Service استفاده می‌کنید تا آن مجموعه از Podها را
در شبکه در دسترس قرار دهید تا کلاینت‌ها بتوانند با آن تعامل داشته باشند.

اگر برای اجرای برنامهٔ خود از یک {{< glossary_tooltip term_id="deployment" >}} استفاده کنید،
آن Deployment می‌تواند Podها را به‌صورت پویا ایجاد و نابود کند. از لحظه‌ای به لحظهٔ دیگر،
نمی‌دانید چه تعداد از آن Podها در حال کار و سالم هستند؛ حتی ممکن است ندانید
آن Podهای سالم چه نامی دارند.
{{< glossary_tooltip term_id="pod" text="Podهای" >}} کوبرنتیز ایجاد و نابود می‌شوند
تا با وضعیت مطلوب کلاستر شما مطابقت داشته باشند. Podها منابعی گذرا هستند (نباید
انتظار داشته باشید که یک Pod منفرد قابل اعتماد و ماندگار باشد).

هر Pod نشانی IP مخصوص به خود را دریافت می‌کند (کوبرنتیز از افزونه‌های شبکه انتظار دارد این را تضمین کنند).
برای یک Deployment مشخص در کلاستر شما، مجموعهٔ Podهایی که در یک لحظه در حال اجرا هستند
ممکن است با مجموعهٔ Podهایی که لحظه‌ای بعد آن برنامه را اجرا می‌کنند، متفاوت باشد.

این امر به یک مشکل منجر می‌شود: اگر مجموعه‌ای از Podها (آن‌ها را «backendها» بنامیم)
قابلیتی را برای Podهای دیگر (آن‌ها را «frontendها» بنامیم) درون کلاستر شما فراهم کنند،
frontendها چگونه بفهمند و پیگیری کنند که به کدام نشانی IP متصل شوند
تا frontend بتواند از بخش backend بار کاری استفاده کند؟

اینجاست که _Serviceها_ وارد میدان می‌شوند.

<!-- body -->

## Serviceها در کوبرنتیز

API مربوط به Service، که بخشی از کوبرنتیز است، یک انتزاع است که به شما کمک می‌کند گروه‌هایی از
Podها را از طریق شبکه در دسترس قرار دهید. هر آبجکت Service مجموعه‌ای منطقی از endpointها (معمولاً
این endpointها Podها هستند) را همراه با سیاستی دربارهٔ نحوهٔ در دسترس قرار دادن آن Podها تعریف می‌کند.

برای مثال، یک backend پردازش تصویر بدون حالت (stateless) را در نظر بگیرید که با
۳ replica اجرا می‌شود. این replicaها جایگزین‌پذیر هستند&mdash;برای frontendها اهمیتی ندارد که از کدام backend
استفاده می‌کنند. در حالی که Podهای واقعی تشکیل‌دهندهٔ مجموعهٔ backend ممکن است تغییر کنند،
کلاینت‌های frontend نباید نیازی به آگاهی از این موضوع داشته باشند و نباید نیازی داشته باشند که
خودشان مجموعهٔ backendها را پیگیری کنند.

انتزاع Service این جداسازی را ممکن می‌سازد.

استقرارهای canary یکی از موارد استفادهٔ رایج Serviceها هستند. برای آشنایی با جزئیات آن، آموزش [استقرار یک نسخه با استفاده از استقرار Canary](/docs/tutorials/stateless-application/canary-deployment/) را دنبال کنید.

مجموعهٔ Podهایی که یک Service هدف قرار می‌دهد، معمولاً با
یک {{< glossary_tooltip text="انتخابگر" term_id="selector" >}} تعیین می‌شود که
شما تعریف می‌کنید.
برای آشنایی با روش‌های دیگر تعریف endpointهای Service،
[Serviceهای _بدون_ انتخابگر](#services-without-selectors) را ببینید.

اگر بار کاری شما با HTTP ارتباط برقرار می‌کند، ممکن است تصمیم بگیرید از یک
[Ingress](/docs/concepts/services-networking/ingress/) برای کنترل نحوهٔ رسیدن ترافیک وب
به آن بار کاری استفاده کنید.
Ingress یک نوع Service نیست، اما به‌عنوان نقطهٔ ورود به کلاستر شما
عمل می‌کند. Ingress به شما امکان می‌دهد قواعد مسیریابی خود را در یک منبع واحد یکپارچه کنید تا
بتوانید چند مؤلفه از بار کاری خود را که به‌طور جداگانه در کلاستر شما اجرا می‌شوند،
پشت یک listener واحد در دسترس قرار دهید.

API ‏[Gateway](https://gateway-api.sigs.k8s.io/#what-is-the-gateway-api) برای کوبرنتیز
قابلیت‌هایی فراتر از Ingress و Service فراهم می‌کند. می‌توانید Gateway را به کلاستر خود اضافه کنید -
این خانواده‌ای از APIهای افزونه است که با استفاده از
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitionها" >}} پیاده‌سازی شده است -
و سپس از آن‌ها برای پیکربندی دسترسی به سرویس‌های شبکه‌ای که در کلاستر شما اجرا می‌شوند، استفاده کنید.

### کشف سرویس به‌شیوهٔ cloud-native

اگر می‌توانید در برنامهٔ خود از APIهای کوبرنتیز برای کشف سرویس استفاده کنید،
می‌توانید از {{< glossary_tooltip text="API server" term_id="kube-apiserver" >}}
EndpointSliceهای منطبق را پرس‌وجو کنید. کوبرنتیز هر زمان که مجموعهٔ Podهای یک Service تغییر کند،
EndpointSliceهای آن Service را به‌روزرسانی می‌کند.

برای برنامه‌های غیربومی، کوبرنتیز روش‌هایی برای قرار دادن یک پورت شبکه یا توزیع‌کنندهٔ
بار میان برنامهٔ شما و Podهای backend ارائه می‌کند.

در هر دو حالت، بار کاری شما می‌تواند از این سازوکارهای [کشف سرویس](#discovering-services)
برای یافتن مقصدی که می‌خواهد به آن متصل شود، استفاده کند.

## تعریف یک Service

یک Service یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} است
(همان‌طور که یک Pod یا یک ConfigMap آبجکت است). می‌توانید تعاریف Service را
با استفاده از API کوبرنتیز ایجاد، مشاهده یا تغییر دهید. معمولاً
از ابزاری مانند `kubectl` استفاده می‌کنید تا این فراخوانی‌های API را برای شما انجام دهد.

برای مثال، فرض کنید مجموعه‌ای از Podها دارید که هر کدام روی پورت TCP ‏9376 گوش می‌دهند
و با `app.kubernetes.io/name=MyApp` برچسب‌گذاری شده‌اند. می‌توانید یک Service برای
منتشر کردن آن listener از نوع TCP تعریف کنید:

{{% code_sample file="service/simple-service.yaml" %}}

اعمال این مانیفست یک Service جدید با نام «my-service» و با [نوع سرویس](#publishing-services-service-types)
پیش‌فرض ClusterIP ایجاد می‌کند. این Service
پورت TCP ‏9376 را روی هر Pod دارای برچسب `app.kubernetes.io/name: MyApp` هدف قرار می‌دهد.

کوبرنتیز یک نشانی IP (همان _cluster IP_) به این Service اختصاص می‌دهد
که سازوکار نشانی IP مجازی از آن استفاده می‌کند. برای جزئیات بیشتر دربارهٔ این سازوکار،
[IPهای مجازی و پراکسی‌های Service](/docs/reference/networking/virtual-ips/) را بخوانید.

کنترل‌کنندهٔ آن Service به‌طور پیوسته Podهایی را که با انتخابگر آن
مطابقت دارند جست‌وجو می‌کند و سپس هرگونه به‌روزرسانی لازم را در مجموعهٔ
EndpointSliceهای آن Service انجام می‌دهد.

نام یک آبجکت Service باید یک
[نام برچسب معتبر طبق RFC 1123](/docs/concepts/overview/working-with-objects/names#rfc-1123-label-names) باشد.


{{< note >}}
یک Service می‌تواند _هر_ `port` ورودی را به یک `targetPort` نگاشت کند. به‌طور پیش‌فرض و
برای سهولت، `targetPort` روی همان مقدار فیلد `port`
تنظیم می‌شود.
{{< /note >}}

### تعاریف پورت {#field-spec-ports}

تعاریف پورت در Podها نام دارند و می‌توانید در ویژگی
`targetPort` یک Service به این نام‌ها ارجاع دهید. برای مثال، می‌توانیم `targetPort`
مربوط به Service را به روش زیر به پورت Pod متصل کنیم:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc

---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
        name: http-web-svc
```

این روش حتی زمانی کار می‌کند که ترکیبی از Podها در Service وجود داشته باشد که از یک
نام پیکربندی‌شدهٔ واحد استفاده می‌کنند و همان پروتکل شبکه از طریق شماره‌های پورت
متفاوت در دسترس است. این امر انعطاف‌پذیری زیادی برای استقرار و تکامل
Serviceهای شما فراهم می‌کند. برای مثال، می‌توانید شماره‌های پورتی را که Podها در نسخهٔ بعدی
نرم‌افزار backend شما در دسترس قرار می‌دهند تغییر دهید، بدون آنکه کلاینت‌ها دچار مشکل شوند.

پروتکل پیش‌فرض برای Serviceها
[TCP](/docs/reference/networking/service-protocols/#protocol-tcp) است؛ همچنین می‌توانید
از هر [پروتکل پشتیبانی‌شدهٔ](/docs/reference/networking/service-protocols/) دیگری استفاده کنید.

از آنجا که بسیاری از Serviceها باید بیش از یک پورت را در دسترس قرار دهند، کوبرنتیز از
[تعاریف چند پورت](#multi-port-services) برای یک Service واحد پشتیبانی می‌کند.
هر تعریف پورت می‌تواند `protocol` یکسان یا متفاوتی داشته باشد.

### Serviceهای بدون انتخابگر

Serviceها معمولاً به لطف انتخابگر، دسترسی به Podهای کوبرنتیز را انتزاعی می‌کنند،
اما هنگامی که همراه با مجموعه‌ای متناظر از آبجکت‌های
{{<glossary_tooltip term_id="endpoint-slice" text="EndpointSlice">}}
و بدون انتخابگر استفاده شوند، Service می‌تواند انواع دیگری از backendها را،
از جمله backendهایی که بیرون از کلاستر اجرا می‌شوند، انتزاعی کند.

برای مثال:

* می‌خواهید در محیط عملیاتی یک کلاستر پایگاه دادهٔ خارجی داشته باشید، اما در
  محیط آزمایشی از پایگاه‌های دادهٔ خودتان استفاده می‌کنید.
* می‌خواهید Service خود را به یک Service در یک
  {{< glossary_tooltip term_id="namespace" >}} دیگر یا در کلاستری دیگر هدایت کنید.
* در حال مهاجرت یک بار کاری به کوبرنتیز هستید. در حین ارزیابی این رویکرد،
  تنها بخشی از backendهای خود را در کوبرنتیز اجرا می‌کنید.

در هر یک از این سناریوها می‌توانید یک Service را _بدون_ تعیین
انتخابگری برای تطبیق Podها تعریف کنید. برای مثال:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
```

از آنجا که این Service انتخابگری ندارد، آبجکت‌های EndpointSlice متناظر
به‌طور خودکار ایجاد نمی‌شوند. می‌توانید با افزودن دستی یک آبجکت EndpointSlice،
Service را به نشانی شبکه و پورتی که در آن اجرا می‌شود نگاشت کنید.
برای مثال:

```yaml
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: my-service-1 # by convention, use the name of the Service
                     # as a prefix for the name of the EndpointSlice
  labels:
    # You should set the "kubernetes.io/service-name" label.
    # Set its value to match the name of the Service
    kubernetes.io/service-name: my-service
addressType: IPv4
ports:
  - name: http # should match with the name of the service port defined above
    appProtocol: http
    protocol: TCP
    port: 9376
endpoints:
  - addresses:
      - "10.4.5.6"
  - addresses:
      - "10.1.2.3"
```

#### EndpointSliceهای سفارشی

هنگامی که یک آبجکت [EndpointSlice](#endpointslices) برای یک Service ایجاد می‌کنید، می‌توانید
از هر نامی برای EndpointSlice استفاده کنید. هر EndpointSlice در یک فضای نام باید
نام یکتایی داشته باشد. با تنظیم {{< glossary_tooltip text="برچسب" term_id="label" >}}
`kubernetes.io/service-name` روی یک EndpointSlice، آن را به یک Service پیوند می‌دهید.

{{< note >}}
IPهای endpoint _نباید_ از این انواع باشند: loopback ‏(127.0.0.0/8 برای IPv4، ‏::1/128 برای IPv6) یا
link-local ‏(169.254.0.0/16 و 224.0.0.0/24 برای IPv4، ‏fe80::/64 برای IPv6).

نشانی‌های IP مربوط به endpoint نمی‌توانند cluster IPهای سایر Serviceهای کوبرنتیز باشند،
زیرا {{< glossary_tooltip term_id="kube-proxy" >}} از IPهای مجازی
به‌عنوان مقصد پشتیبانی نمی‌کند.
{{< /note >}}

برای EndpointSliceای که خودتان یا در کد خودتان ایجاد می‌کنید،
باید مقداری نیز برای برچسب
[`endpointslice.kubernetes.io/managed-by`](/docs/reference/labels-annotations-taints/#endpointslicekubernetesiomanaged-by) انتخاب کنید.
اگر کد کنترل‌کنندهٔ خود را برای مدیریت EndpointSliceها می‌نویسید، استفاده از
مقداری مشابه `"my-domain.example/name-of-controller"` را در نظر بگیرید. اگر از یک ابزار
شخص ثالث استفاده می‌کنید، نام ابزار را با حروف کاملاً کوچک به کار ببرید و فاصله‌ها و سایر
علائم نگارشی را به خط تیره (`-`) تبدیل کنید.
اگر افراد مستقیماً از ابزاری مانند `kubectl` برای مدیریت EndpointSliceها استفاده می‌کنند،
از نامی استفاده کنید که این مدیریت دستی را توصیف کند، مانند `"staff"` یا
`"cluster-admins"`. باید
از به کار بردن مقدار رزروشدهٔ `"controller"` خودداری کنید؛ این مقدار EndpointSliceهایی را مشخص می‌کند که
توسط control plane خود کوبرنتیز مدیریت می‌شوند.

#### دسترسی به یک Service بدون انتخابگر {#service-no-selector-access}

دسترسی به یک Service بدون انتخابگر همانند حالتی است که انتخابگر داشته باشد.
در [مثال](#services-without-selectors) مربوط به Service بدون انتخابگر،
ترافیک به یکی از دو endpoint تعریف‌شده در
مانیفست EndpointSlice هدایت می‌شود: یک اتصال TCP به 10.1.2.3 یا 10.4.5.6 روی پورت 9376.

{{< note >}}
API server کوبرنتیز اجازهٔ پراکسی کردن به endpointهایی را که به
Podها نگاشت نشده‌اند، نمی‌دهد. اقداماتی مانند `kubectl port-forward service/<service-name> forwardedPort:servicePort` برای سرویسی که
انتخابگر ندارد، به دلیل همین محدودیت با شکست مواجه می‌شوند. این کار از استفاده از API server کوبرنتیز
به‌عنوان پراکسی به endpointهایی که فراخواننده ممکن است مجوز دسترسی به آن‌ها را نداشته باشد، جلوگیری می‌کند.
{{< /note >}}

یک Service از نوع `ExternalName` حالت خاصی از Service است که
انتخابگر ندارد و به‌جای آن از نام‌های DNS استفاده می‌کند. برای اطلاعات بیشتر، بخش
[ExternalName](#externalname) را ببینید.

### EndpointSliceها

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

[EndpointSliceها](/docs/concepts/services-networking/endpoint-slices/) آبجکت‌هایی هستند که
زیرمجموعه‌ای (یک _برش_) از endpointهای شبکهٔ پشتیبان یک Service را نمایش می‌دهند.

کلاستر کوبرنتیز شما پیگیری می‌کند که هر EndpointSlice نمایانگر چه تعداد endpoint است.
اگر تعداد endpointهای یک Service به حدی برسد که از یک آستانه فراتر رود،
کوبرنتیز یک EndpointSlice خالی دیگر اضافه می‌کند و اطلاعات endpointهای جدید را
در آن ذخیره می‌کند.
به‌طور پیش‌فرض، کوبرنتیز زمانی یک EndpointSlice جدید می‌سازد که همهٔ EndpointSliceهای موجود
دست‌کم ۱۰۰ endpoint داشته باشند. کوبرنتیز EndpointSlice جدید را
تا زمانی که نیاز به افزودن یک endpoint اضافی نباشد، نمی‌سازد.

برای اطلاعات بیشتر دربارهٔ این API، [EndpointSliceها](/docs/concepts/services-networking/endpoint-slices/)
را ببینید.

### Endpoints (منسوخ‌شده) {#endpoints}

{{< feature-state for_k8s_version="v1.33" state="deprecated" >}}

API مربوط به EndpointSlice شکل تکامل‌یافتهٔ API قدیمی‌تر
[Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
است. API منسوخ‌شدهٔ Endpoints در مقایسه با
EndpointSlice چند مشکل دارد:

  - از کلاسترهای دوپشته‌ای پشتیبانی نمی‌کند.
  - اطلاعات لازم برای پشتیبانی از قابلیت‌های جدیدتر، مانند
    [trafficDistribution](/docs/concepts/services-networking/service/#traffic-distribution)، را در بر ندارد.
  - اگر فهرست endpointها بیش از حدی طولانی باشد که در یک آبجکت واحد جای گیرد، آن را کوتاه می‌کند.

به همین دلیل، توصیه می‌شود همهٔ کلاینت‌ها به‌جای Endpoints از
API مربوط به EndpointSlice استفاده کنند.

#### endpointهای بیش از ظرفیت

کوبرنتیز تعداد endpointهایی را که می‌توانند در یک آبجکت Endpoints واحد جای گیرند، محدود می‌کند.
هنگامی که بیش از ۱۰۰۰ endpoint پشتیبان برای یک Service وجود داشته باشد، کوبرنتیز
داده‌های آبجکت Endpoints را کوتاه می‌کند. از آنجا که یک Service می‌تواند با
بیش از یک EndpointSlice پیوند داشته باشد، محدودیت ۱۰۰۰ endpoint پشتیبان تنها
بر API قدیمی Endpoints اثر می‌گذارد.

در این حالت، کوبرنتیز حداکثر ۱۰۰۰ endpoint ممکن از backendها را برای ذخیره
در آبجکت Endpoints انتخاب می‌کند و یک
{{< glossary_tooltip text="حاشیه‌نویسی" term_id="annotation" >}} روی Endpoints تنظیم می‌کند:
[`endpoints.kubernetes.io/over-capacity: truncated`](/docs/reference/labels-annotations-taints/#endpoints-kubernetes-io-over-capacity).
control plane همچنین در صورتی که تعداد Podهای backend به کمتر از ۱۰۰۰ برسد، آن حاشیه‌نویسی را حذف می‌کند.

ترافیک همچنان به backendها ارسال می‌شود، اما هر سازوکار توزیع باری که به
API قدیمی Endpoints متکی است، ترافیک را تنها به حداکثر ۱۰۰۰ endpoint از endpointهای پشتیبان موجود ارسال می‌کند.

همین محدودیت API به این معناست که نمی‌توانید یک Endpoints را به‌صورت دستی طوری به‌روزرسانی کنید که بیش از ۱۰۰۰ endpoint داشته باشد.

### پروتکل برنامه

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

فیلد `appProtocol` راهی برای تعیین یک پروتکل برنامه برای
هر پورت Service فراهم می‌کند. پیاده‌سازی‌ها از این فیلد به‌عنوان راهنمایی استفاده می‌کنند تا
برای پروتکل‌هایی که می‌شناسند، رفتار غنی‌تری ارائه دهند.
مقدار این فیلد در آبجکت‌های Endpoints و EndpointSlice متناظر
بازتاب داده می‌شود.

این فیلد از نحو استاندارد برچسب در کوبرنتیز پیروی می‌کند. مقادیر معتبر یکی از موارد زیر است:

* [نام‌های استاندارد سرویس IANA](https://www.iana.org/assignments/service-names).

* نام‌های پیشونددار تعریف‌شده توسط پیاده‌سازی، مانند `mycompany.com/my-custom-protocol`.

* نام‌های پیشونددار تعریف‌شده توسط کوبرنتیز:

| پروتکل | توضیح |
|----------|-------------|
| `kubernetes.io/h2c` | HTTP/2 روی متن ساده (cleartext)، همان‌گونه که در [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113) توصیف شده است |
| `kubernetes.io/ws`  | WebSocket روی متن ساده (cleartext)، همان‌گونه که در [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) توصیف شده است |
| `kubernetes.io/wss` | WebSocket روی TLS، همان‌گونه که در [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) توصیف شده است |

### Serviceهای چندپورتی

برای برخی Serviceها، باید بیش از یک پورت را در دسترس قرار دهید.
کوبرنتیز به شما امکان می‌دهد چند تعریف پورت را روی یک آبجکت Service پیکربندی کنید.
هنگام استفاده از چند پورت برای یک Service، باید به همهٔ پورت‌های خود نام بدهید
تا ابهامی وجود نداشته باشد.
برای مثال:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377
```

{{< note >}}
همانند {{< glossary_tooltip term_id="name" text="نام‌های">}} کوبرنتیز به‌طور کلی، نام پورت‌ها
باید تنها شامل نویسه‌های الفبایی‌عددی کوچک و `-` باشد. نام پورت‌ها
همچنین باید با یک نویسهٔ الفبایی‌عددی آغاز شوند و پایان یابند.

برای مثال، نام‌های `123-abc` و `web` معتبر هستند، اما `123_abc` و `-web` معتبر نیستند.
{{< /note >}}

## نوع Service  {#publishing-services-service-types}

برای برخی بخش‌های برنامهٔ خود (برای مثال frontendها) ممکن است بخواهید یک
Service را روی یک نشانی IP خارجی در دسترس قرار دهید؛ نشانی‌ای که از بیرون
کلاستر شما قابل دسترسی باشد.

انواع Service در کوبرنتیز به شما امکان می‌دهند نوع Service مورد نظر خود را تعیین کنید.

مقادیر موجود برای `type` و رفتار آن‌ها به این شرح است:

[`ClusterIP`](#type-clusterip)
: Service را روی یک IP داخلی کلاستر در دسترس قرار می‌دهد. انتخاب این مقدار
  باعث می‌شود Service تنها از درون کلاستر قابل دسترسی باشد. اگر `type` را برای یک Service
  صراحتاً تعیین نکنید، همین مقدار پیش‌فرض استفاده می‌شود.
  می‌توانید Service را با استفاده از یک
  [Ingress](/docs/concepts/services-networking/ingress/) یا یک
  [Gateway](https://gateway-api.sigs.k8s.io/) در اینترنت عمومی در دسترس قرار دهید.

[`NodePort`](#type-nodeport)
: Service را روی IP هر نود و در یک پورت ثابت (همان `NodePort`) در دسترس قرار می‌دهد.
  برای در دسترس قرار دادن پورت نود، کوبرنتیز یک نشانی cluster IP راه‌اندازی می‌کند،
  درست مانند زمانی که یک Service از نوع `type: ClusterIP` درخواست کرده باشید.

[`LoadBalancer`](#loadbalancer)
: Service را با استفاده از یک توزیع‌کنندهٔ بار خارجی، به‌صورت خارجی در دسترس قرار می‌دهد. کوبرنتیز
  مستقیماً یک مؤلفهٔ توزیع بار ارائه نمی‌کند؛ باید خودتان یکی فراهم کنید یا
  می‌توانید کلاستر کوبرنتیز خود را با یک ارائه‌دهندهٔ ابری یکپارچه کنید.

[`ExternalName`](#externalname)
: Service را به محتوای فیلد `externalName` نگاشت می‌کند (برای مثال،
  به hostname ‏`api.foo.bar.example`). این نگاشت، سرور DNS کلاستر شما را طوری
  پیکربندی می‌کند که یک رکورد `CNAME` با همان مقدار hostname خارجی برگرداند.
  هیچ نوع پراکسی‌ای راه‌اندازی نمی‌شود.

فیلد `type` در API مربوط به Service به‌صورت قابلیتی تودرتو طراحی شده است - هر سطح
چیزی به سطح قبلی اضافه می‌کند. با این حال، این طراحی تودرتو یک استثنا دارد. می‌توانید
یک Service از نوع `LoadBalancer` را با
[غیرفعال کردن تخصیص `NodePort` برای توزیع‌کنندهٔ بار](/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) تعریف کنید.

### `type: ClusterIP` {#type-clusterip}

این نوع پیش‌فرض Service، یک نشانی IP را از مخزنی از نشانی‌های IP که
کلاستر شما برای این منظور رزرو کرده است، اختصاص می‌دهد.

چند نوع دیگر Service بر پایهٔ نوع `ClusterIP`
ساخته می‌شوند.

اگر Serviceای تعریف کنید که `.spec.clusterIP` آن روی `"None"` تنظیم شده باشد،
کوبرنتیز هیچ نشانی IPای اختصاص نمی‌دهد. برای اطلاعات بیشتر، [Serviceهای headless](#headless-services)
را ببینید.

#### انتخاب نشانی IP دلخواه

می‌توانید نشانی cluster IP دلخواه خود را به‌عنوان بخشی از درخواست ایجاد یک `Service`
تعیین کنید. برای این کار، فیلد `.spec.clusterIP` را تنظیم کنید. برای مثال، زمانی که
یک ورودی DNS موجود دارید که می‌خواهید دوباره از آن استفاده کنید، یا سامانه‌های قدیمی‌ای
که برای یک نشانی IP مشخص پیکربندی شده‌اند و پیکربندی دوبارهٔ آن‌ها دشوار است.

نشانی IPای که انتخاب می‌کنید باید یک نشانی IPv4 یا IPv6 معتبر از درون
بازهٔ CIDR ‏`service-cluster-ip-range` باشد که برای API server پیکربندی شده است.
اگر تلاش کنید یک Service با مقدار نشانی `clusterIP` نامعتبر ایجاد کنید، API
server کد وضعیت HTTP ‏422 را برمی‌گرداند تا نشان دهد مشکلی وجود دارد.

برای آشنایی با اینکه کوبرنتیز چگونه به کاهش خطر و اثر تلاش دو Service متفاوت
برای استفاده از یک نشانی IP یکسان کمک می‌کند، [پرهیز از برخوردها](/docs/reference/networking/virtual-ips/#avoiding-collisions)
را بخوانید.

### `type: NodePort` {#type-nodeport}

اگر فیلد `type` را روی `NodePort` تنظیم کنید، control plane کوبرنتیز
یک پورت را از بازه‌ای که با فلگ `--service-node-port-range` تعیین می‌شود (پیش‌فرض: 30000-32767) تخصیص می‌دهد.
هر نود آن پورت (همان شمارهٔ پورت روی همهٔ نودها) را به Service شما پراکسی می‌کند.
Service شما پورت تخصیص‌یافته را در فیلد `.spec.ports[*].nodePort` خود گزارش می‌کند.

استفاده از NodePort به شما آزادی می‌دهد تا راهکار توزیع بار خود را راه‌اندازی کنید،
محیط‌هایی را که به‌طور کامل توسط کوبرنتیز پشتیبانی نمی‌شوند پیکربندی کنید، یا حتی
نشانی‌های IP یک یا چند نود را مستقیماً در دسترس قرار دهید.

برای یک Service از نوع node port، کوبرنتیز علاوه بر این یک پورت (TCP، UDP یا
SCTP، مطابق با پروتکل Service) تخصیص می‌دهد. هر نود در کلاستر خود را طوری
پیکربندی می‌کند که روی آن پورت تخصیص‌یافته گوش دهد و ترافیک را به یکی از endpointهای آماده‌ای
که با آن Service مرتبط هستند، ارسال کند. می‌توانید از بیرون کلاستر، با اتصال به هر نود با استفاده از
پروتکل مناسب (برای مثال: TCP) و پورت مناسب (همان پورتی که به آن Service اختصاص داده شده است)،
با Service از نوع `type: NodePort` ارتباط برقرار کنید.

#### انتخاب پورت دلخواه {#nodeport-custom-port}

اگر یک شمارهٔ پورت مشخص می‌خواهید، می‌توانید مقداری را در فیلد `nodePort`
تعیین کنید. control plane یا آن پورت را به شما تخصیص می‌دهد یا گزارش می‌دهد
که تراکنش API با شکست مواجه شد.
این به آن معناست که باید خودتان مراقب برخوردهای احتمالی پورت باشید.
همچنین باید از یک شمارهٔ پورت معتبر استفاده کنید؛ پورتی که درون بازهٔ پیکربندی‌شده
برای استفادهٔ NodePort باشد.

در اینجا یک مانیفست نمونه برای یک Service از نوع `type: NodePort` آمده است که
یک مقدار NodePort (در این مثال 30007) تعیین می‌کند:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - port: 80
      # By default and for convenience, the `targetPort` is set to
      # the same value as the `port` field.
      targetPort: 80
      # Optional field
      # By default and for convenience, the Kubernetes control plane
      # will allocate a port from a range (default: 30000-32767)
      nodePort: 30007
```

#### رزرو بازه‌های Nodeport برای پرهیز از برخورد  {#avoid-nodeport-collisions}

سیاست تخصیص پورت به سرویس‌های NodePort هم بر سناریوی تخصیص خودکار و هم بر
سناریوی تخصیص دستی اعمال می‌شود. هنگامی که کاربری می‌خواهد یک سرویس NodePort ایجاد کند که
از یک پورت مشخص استفاده می‌کند، ممکن است پورت مقصد با پورت دیگری که پیش‌تر تخصیص داده شده است، تعارض داشته باشد.

برای پرهیز از این مشکل، بازهٔ پورت سرویس‌های NodePort به دو باند تقسیم می‌شود.
تخصیص پویای پورت به‌طور پیش‌فرض از باند بالایی استفاده می‌کند و پس از پر شدن
باند بالایی، ممکن است از باند پایینی استفاده کند. در این صورت کاربران می‌توانند با خطر کمتر برخورد پورت، از باند پایینی تخصیص دهند.

هنگام استفاده از بازهٔ پیش‌فرض NodePort یعنی 30000-32767، باندها به این صورت تقسیم می‌شوند: 

- باند ایستا: 30000-30085
- باند پویا: 30086-32767

برای جزئیات بیشتر دربارهٔ نحوهٔ محاسبهٔ باندهای ایستا و پویا،
[پرهیز از برخورد در تخصیص پورت به سرویس‌های NodePort](/blog/2023/05/11/nodeport-dynamic-and-static-allocation/) را ببینید.

#### پیکربندی نشانی IP برای Serviceهای `type: NodePort` {#service-nodeport-custom-listen-address}

هنگام استفاده از kube-proxy در [حالت
`iptables`](/docs/reference/networking/virtual-ips/#proxy-mode-iptables)، سرویس‌های NodePort به‌طور پیش‌فرض
روی همهٔ IPهای نود در دسترس هستند. هنگام استفاده از [حالت
`nftables`](/docs/reference/networking/virtual-ips/#proxy-mode-nftables)، این سرویس‌ها به‌طور پیش‌فرض تنها
روی IP اصلی نود (یا IPهای اصلی دوپشته‌ای) در دسترس هستند.

می‌توانید مجموعهٔ IPهای نودی را که سرویس‌های NodePort روی آن‌ها در دسترس هستند، با
فلگ `--nodeport-addresses` در kube-proxy یا فیلد معادل `nodePortAddresses`
در [فایل پیکربندی kube-proxy](/docs/reference/config-api/kube-proxy-config.v1alpha1/) تغییر دهید.
این گزینه فهرستی از بلوک‌های IP جداشده با کاما (مانند `10.0.0.0/8` و `192.0.2.0/25`) یا یک
یا چند مورد از کلیدواژه‌های زیر را می‌پذیرد:

- `primary` - نشانی IPv4 و/یا IPv6 اصلی نود، بر اساس آبجکت Node.
  (این مقدار پیش‌فرض برای حالت `nftables` است.)
- `localhost` - نشانی‌های loopback نود (`127.0.0.0/8`، `::1/128`).
- `all` - همهٔ نشانی‌ها. (این مقدار پیش‌فرض برای حالت‌های `iptables` و `ipvs` است.)

برای مثال، اگر kube-proxy را با فلگ `--nodeport-addresses=192.168.0.0/24` راه‌اندازی کنید،
kube-proxy تلاش می‌کند روی هر نود یک نشانی IP محلی در آن زیرشبکه بیابد و
سرویس‌های NodePort را تنها از طریق همان IP ارائه کند.

#### Serviceهای `type: NodePort` از طریق localhost {#localhost-nodeports}

سازوکارهایی که پراکسی‌های سرویس برای پیاده‌سازی سرویس‌های NodePort به کار می‌برند، همیشه
از ارائهٔ سرویس‌های NodePort روی localhost پشتیبانی نمی‌کنند. برای kube-proxy:

  - هنگام استفاده از حالت `iptables` با مقداری برای `--nodeport-addresses` که شامل
    `127.0.0.1` باشد، سرویس‌های NodePort روی `127.0.0.1` در دسترس خواهند بود. با این حال، این کار
    مستلزم فعال کردن یک sysctl کرنل (`route_localnet`) است که ممکن است در برخی کلاسترها
    عوارض جانبی ناامنی داشته باشد. NodePortهای localhost در IPTables را می‌توان با ارسال
    `--iptables-localhost-nodeports false` به kube-proxy، یا با تنظیم
    `--nodeport-addresses` روی بازه‌ای که شامل `127.0.0.1` نباشد، غیرفعال کرد.

  - هنگام استفاده از حالت `ipvs`، یا حالت `iptables` در کلاسترهای تک‌پشته‌ای IPv6، سرویس‌های
    NodePort روی localhost در دسترس نیستند.

{{< feature-state feature_gate_name="KubeProxyNFTablesLocalhostNodePorts" >}}

  - هنگام استفاده از حالت `nftables`، سرویس‌های NodePort زمانی روی localhost در دسترس خواهند بود که
    feature gate ‏`KubeProxyNFTablesLocalhostNodePorts` فعال باشد و
    `--nodeport-addresses` روی مقداری تنظیم شده باشد که صراحتاً شامل `localhost` باشد.
    (تنظیم آن تنها روی `all`، سرویس‌های NodePort روی localhost را فعال _نمی‌کند_.) این قابلیت
    با هدایت اتصال‌های NodePort روی localhost از طریق یک پراکسی در فضای کاربر پیاده‌سازی شده است،
    بنابراین به اندازهٔ پراکسی معمول سرویس کارآمد نیست.

افزونه‌های شبکهٔ شخص ثالثی که پیاده‌سازی پراکسی سرویس مخصوص به خود را دارند، ممکن است
از NodePortهای localhost پشتیبانی کنند یا نکنند؛ به مستندات آن افزونه‌ها مراجعه کنید.

### `type: LoadBalancer` {#loadbalancer}

در ارائه‌دهندگان ابری‌ای که از توزیع‌کننده‌های بار خارجی پشتیبانی می‌کنند، تنظیم فیلد `type`
روی `LoadBalancer` یک توزیع‌کنندهٔ بار برای Service شما فراهم می‌کند.
ایجاد واقعی توزیع‌کنندهٔ بار به‌صورت ناهمگام انجام می‌شود و
اطلاعات مربوط به توزیع‌کنندهٔ فراهم‌شده در فیلد
`.status.loadBalancer` مربوط به Service منتشر می‌شود.
برای مثال:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  clusterIP: 10.0.171.239
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - ip: 192.0.2.127
```

ترافیک از توزیع‌کنندهٔ بار خارجی به Podهای backend هدایت می‌شود. ارائه‌دهندهٔ
ابری تصمیم می‌گیرد که بار آن چگونه توزیع شود.

برای پیاده‌سازی یک Service از نوع `type: LoadBalancer`، کوبرنتیز معمولاً کار را
با اعمال تغییراتی آغاز می‌کند که معادل درخواست یک Service از نوع
`type: NodePort` است. سپس مؤلفهٔ cloud-controller-manager توزیع‌کنندهٔ بار خارجی را
طوری پیکربندی می‌کند که ترافیک را به همان پورت نود تخصیص‌یافته ارسال کند.

می‌توانید یک Service با توزیع بار را طوری پیکربندی کنید که تخصیص پورت نود را
[حذف کند](#load-balancer-nodeport-allocation)، به شرط آنکه
پیاده‌سازی ارائه‌دهندهٔ ابری از این کار پشتیبانی کند.

برخی ارائه‌دهندگان ابری به شما امکان می‌دهند `loadBalancerIP` را تعیین کنید. در این موارد، توزیع‌کنندهٔ بار
با `loadBalancerIP` تعیین‌شده توسط کاربر ایجاد می‌شود. اگر فیلد `loadBalancerIP` تعیین نشده باشد،
توزیع‌کنندهٔ بار با یک نشانی IP گذرا راه‌اندازی می‌شود. اگر یک `loadBalancerIP` تعیین کنید
اما ارائه‌دهندهٔ ابری شما از این قابلیت پشتیبانی نکند، فیلد `loadbalancerIP` که
تنظیم کرده‌اید نادیده گرفته می‌شود.


{{< note >}}
فیلد `.spec.loadBalancerIP` برای Service در کوبرنتیز v1.24 منسوخ شد.

این فیلد به‌طور ناکافی تعریف شده بود و معنای آن در پیاده‌سازی‌های مختلف متفاوت است.
همچنین نمی‌تواند از شبکهٔ دوپشته‌ای پشتیبانی کند. این فیلد ممکن است در نسخه‌ای آینده از API حذف شود.

اگر با ارائه‌دهنده‌ای یکپارچه می‌شوید که از تعیین نشانی(های) IP توزیع‌کنندهٔ بار
برای یک Service از طریق یک حاشیه‌نویسی (مختص ارائه‌دهنده) پشتیبانی می‌کند، باید به همان روش روی بیاورید.

اگر برای یکپارچه‌سازی یک توزیع‌کنندهٔ بار با کوبرنتیز کد می‌نویسید، از استفاده از این فیلد خودداری کنید.
می‌توانید به‌جای Service با [Gateway](https://gateway-api.sigs.k8s.io/) یکپارچه شوید، یا
می‌توانید حاشیه‌نویسی‌های (مختص ارائه‌دهندهٔ) خود را روی Service تعریف کنید که جزئیات معادل را تعیین کنند.
{{< /note >}}

#### اثر زنده بودن نود بر ترافیک توزیع‌کنندهٔ بار

بررسی‌های سلامت توزیع‌کنندهٔ بار برای برنامه‌های مدرن حیاتی هستند. از آن‌ها برای
تعیین اینکه توزیع‌کنندهٔ بار باید ترافیک را به کدام سرور (ماشین مجازی یا نشانی IP)
ارسال کند، استفاده می‌شود. APIهای کوبرنتیز تعریف نمی‌کنند که بررسی‌های سلامت برای
توزیع‌کننده‌های بار مدیریت‌شده توسط کوبرنتیز چگونه باید پیاده‌سازی شوند؛ بلکه این ارائه‌دهندگان ابری
(و افرادی که کد یکپارچه‌سازی را پیاده‌سازی می‌کنند) هستند که دربارهٔ رفتار تصمیم می‌گیرند. بررسی‌های سلامت
توزیع‌کنندهٔ بار به‌طور گسترده در زمینهٔ پشتیبانی از فیلد
`externalTrafficPolicy` برای Serviceها استفاده می‌شوند.

#### توزیع‌کننده‌های بار با انواع پروتکل ترکیبی

{{< feature-state feature_gate_name="MixedProtocolLBService" >}}

به‌طور پیش‌فرض، برای Serviceهای از نوع LoadBalancer، هنگامی که بیش از یک پورت تعریف شده باشد، همهٔ
پورت‌ها باید پروتکل یکسانی داشته باشند و این پروتکل باید از پروتکل‌هایی باشد که
ارائه‌دهندهٔ ابری از آن پشتیبانی می‌کند.

feature gate ‏`MixedProtocolLBService` (که از v1.24 به‌طور پیش‌فرض برای kube-apiserver فعال است) امکان استفاده از
پروتکل‌های مختلف را برای Serviceهای از نوع LoadBalancer، هنگامی که بیش از یک پورت تعریف شده باشد، فراهم می‌کند.

{{< note >}}
مجموعهٔ پروتکل‌هایی که می‌توان برای Serviceهای دارای توزیع بار استفاده کرد، توسط
ارائه‌دهندهٔ ابری شما تعیین می‌شود؛ ممکن است آن‌ها محدودیت‌هایی فراتر از آنچه API کوبرنتیز اعمال می‌کند، تحمیل کنند.
{{< /note >}}

#### غیرفعال کردن تخصیص NodePort برای توزیع‌کنندهٔ بار {#load-balancer-nodeport-allocation}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

می‌توانید به‌صورت اختیاری تخصیص پورت نود را برای یک Service از نوع `type: LoadBalancer`، با تنظیم
فیلد `spec.allocateLoadBalancerNodePorts` روی `false` غیرفعال کنید. این کار تنها باید برای پیاده‌سازی‌هایی از توزیع‌کنندهٔ بار
استفاده شود که ترافیک را به‌جای استفاده از پورت‌های نود، مستقیماً به Podها هدایت می‌کنند. به‌طور پیش‌فرض، `spec.allocateLoadBalancerNodePorts`
برابر با `true` است و Serviceهای از نوع LoadBalancer همچنان پورت‌های نود تخصیص خواهند داد. اگر `spec.allocateLoadBalancerNodePorts`
روی یک Service موجود که پورت‌های نود تخصیص‌یافته دارد به `false` تنظیم شود، آن پورت‌های نود به‌طور خودکار آزاد **نخواهند** شد.
برای آزاد کردن آن پورت‌های نود، باید ورودی `nodePorts` را در هر پورت Service صراحتاً حذف کنید.

#### تعیین کلاس پیاده‌سازی توزیع‌کنندهٔ بار {#load-balancer-class}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

برای Serviceای که `type` آن روی `LoadBalancer` تنظیم شده است، فیلد `.spec.loadBalancerClass`
به شما امکان می‌دهد از پیاده‌سازی‌ای از توزیع‌کنندهٔ بار غیر از پیاده‌سازی پیش‌فرض ارائه‌دهندهٔ ابری استفاده کنید.

به‌طور پیش‌فرض، `.spec.loadBalancerClass` تنظیم نشده است و یک Service از نوع `LoadBalancer`
در صورتی که کلاستر با یک ارائه‌دهندهٔ ابری و با استفاده از فلگ مؤلفهٔ `--cloud-provider` پیکربندی شده باشد،
از پیاده‌سازی پیش‌فرض توزیع‌کنندهٔ بار ارائه‌دهندهٔ ابری استفاده می‌کند.

اگر `.spec.loadBalancerClass` را تعیین کنید، فرض بر این است که یک پیاده‌سازی توزیع‌کنندهٔ بار
که با کلاس تعیین‌شده مطابقت دارد، Serviceها را زیر نظر دارد.
هر پیاده‌سازی پیش‌فرض توزیع‌کنندهٔ بار (برای مثال، پیاده‌سازی‌ای که
ارائه‌دهندهٔ ابری فراهم می‌کند) Serviceهایی را که این فیلد برای آن‌ها تنظیم شده است، نادیده می‌گیرد.
`spec.loadBalancerClass` تنها روی Serviceای از نوع `LoadBalancer` قابل تنظیم است.
پس از تنظیم، نمی‌توان آن را تغییر داد.
مقدار `spec.loadBalancerClass` باید یک شناسه به سبک برچسب باشد،
با پیشوندی اختیاری مانند «`internal-vip`» یا «`example.com/internal-vip`».
نام‌های بدون پیشوند برای کاربران نهایی رزرو شده‌اند.

#### حالت نشانی IP توزیع‌کنندهٔ بار {#load-balancer-ip-mode}

برای یک Service از نوع `type: LoadBalancer`، یک کنترل‌کننده می‌تواند `.status.loadBalancer.ingress.ipMode` را تنظیم کند.
`.status.loadBalancer.ingress.ipMode` مشخص می‌کند که IP توزیع‌کنندهٔ بار چگونه رفتار می‌کند.
این فیلد تنها زمانی قابل تعیین است که فیلد `.status.loadBalancer.ingress.ip` نیز تعیین شده باشد.

دو مقدار ممکن برای `.status.loadBalancer.ingress.ipMode` وجود دارد: «VIP» و «Proxy».
مقدار پیش‌فرض «VIP» است؛ به این معنا که ترافیک با مقصدی برابر با IP و پورت توزیع‌کنندهٔ بار
به نود تحویل داده می‌شود.
هنگام تنظیم این فیلد روی «Proxy»، بسته به اینکه توزیع‌کنندهٔ بار
ارائه‌دهندهٔ ابری ترافیک را چگونه تحویل می‌دهد، دو حالت وجود دارد:

- اگر ترافیک به نود تحویل داده شود و سپس با DNAT به Pod برسد، مقصد روی IP و پورت نودِ نود تنظیم می‌شود؛
- اگر ترافیک مستقیماً به Pod تحویل داده شود، مقصد روی IP و پورت Pod تنظیم می‌شود.

پیاده‌سازی‌های Service ممکن است از این اطلاعات برای تنظیم مسیریابی ترافیک استفاده کنند.

#### توزیع‌کنندهٔ بار داخلی

در یک محیط ترکیبی، گاهی لازم است ترافیک از Serviceهای درون همان
بلوک نشانی شبکهٔ (مجازی) مسیریابی شود.

در یک محیط DNS از نوع split-horizon، به دو Service نیاز دارید تا بتوانید هم ترافیک خارجی
و هم ترافیک داخلی را به endpointهای خود مسیریابی کنید.

برای تنظیم یک توزیع‌کنندهٔ بار داخلی، بسته به ارائه‌دهندهٔ سرویس ابری‌ای که استفاده می‌کنید،
یکی از حاشیه‌نویسی‌های زیر را به Service خود اضافه کنید:

{{< tabs name="service_tabs" >}}
{{% tab name="پیش‌فرض" %}}
یکی از زبانه‌ها را انتخاب کنید.
{{% /tab %}}

{{% tab name="GCP" %}}

```yaml
metadata:
  name: my-service
  annotations:
    networking.gke.io/load-balancer-type: "Internal"
```
{{% /tab %}}
{{% tab name="AWS" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
```

{{% /tab %}}
{{% tab name="Azure" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
```

{{% /tab %}}
{{% tab name="IBM Cloud" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.kubernetes.io/ibm-load-balancer-cloud-provider-ip-type: "private"
```

{{% /tab %}}
{{% tab name="OpenStack" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/openstack-internal-load-balancer: "true"
```

{{% /tab %}}
{{% tab name="Baidu Cloud" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/cce-load-balancer-internal-vpc: "true"
```

{{% /tab %}}
{{% tab name="Tencent Cloud" %}}

```yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxx
```

{{% /tab %}}
{{% tab name="Alibaba Cloud" %}}

```yaml
metadata:
  annotations:
    service.beta.kubernetes.io/alibaba-cloud-loadbalancer-address-type: "intranet"
```

{{% /tab %}}
{{% tab name="OCI" %}}

```yaml
metadata:
  name: my-service
  annotations:
    service.beta.kubernetes.io/oci-load-balancer-internal: true
```
{{% /tab %}}
{{< /tabs >}}

### `type: ExternalName` {#externalname}

Serviceهای از نوع ExternalName یک Service را به یک نام DNS نگاشت می‌کنند، نه به یک انتخابگر معمول مانند
`my-service` یا `cassandra`. این Serviceها را با پارامتر `spec.externalName` تعیین می‌کنید.

برای مثال، این تعریف Service،
Service ‏`my-service` در فضای نام `prod` را به `my.database.example.com` نگاشت می‌کند:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

{{< note >}}
یک Service از نوع `type: ExternalName` یک رشتهٔ نشانی IPv4 را می‌پذیرد،
اما با آن رشته به‌عنوان یک نام DNS متشکل از ارقام رفتار می‌کند،
نه به‌عنوان یک نشانی IP (با این حال، اینترنت چنین نام‌هایی را در DNS مجاز نمی‌داند).
Serviceهایی با نام‌های خارجی که شبیه نشانی‌های IPv4 هستند،
توسط سرورهای DNS ‏resolve نمی‌شوند.

اگر می‌خواهید یک Service را مستقیماً به یک نشانی IP مشخص نگاشت کنید، استفاده از
[Serviceهای headless](#headless-services) را در نظر بگیرید.
{{< /note >}}

هنگام جست‌وجوی host ‏`my-service.prod.svc.cluster.local`، سرویس DNS کلاستر
یک رکورد `CNAME` با مقدار `my.database.example.com` برمی‌گرداند. دسترسی به
`my-service` همانند سایر Serviceها کار می‌کند، اما با این تفاوت
اساسی که هدایت مجدد در سطح DNS انجام می‌شود، نه از طریق پراکسی یا
ارسال (forwarding). اگر بعدها تصمیم بگیرید پایگاه دادهٔ خود را به درون کلاستر منتقل کنید،
می‌توانید Podهای آن را راه‌اندازی کنید، انتخابگرها یا endpointهای مناسب را اضافه کنید و
`type` مربوط به Service را تغییر دهید.

{{< caution >}}
ممکن است در استفاده از ExternalName برای برخی پروتکل‌های رایج، از جمله HTTP و HTTPS، با مشکل مواجه شوید.
اگر از ExternalName استفاده کنید، hostnameی که کلاینت‌های درون کلاستر شما به کار می‌برند با
نامی که ExternalName به آن ارجاع می‌دهد، متفاوت است.

برای پروتکل‌هایی که از hostname استفاده می‌کنند، این تفاوت ممکن است به خطاها یا پاسخ‌های غیرمنتظره منجر شود.
درخواست‌های HTTP هدر `Host:` خواهند داشت که سرور مبدأ آن را نمی‌شناسد؛
سرورهای TLS نمی‌توانند گواهی‌ای منطبق با hostnameی که کلاینت به آن متصل شده است، ارائه کنند.
{{< /caution >}}

## Serviceهای headless

گاهی به توزیع بار و یک IP واحد برای Service نیاز ندارید. در
این حالت، می‌توانید با تعیین صریح مقدار `"None"` برای نشانی cluster IP ‏(`.spec.clusterIP`)،
آنچه را _Serviceهای headless_ نامیده می‌شود، ایجاد کنید.

می‌توانید از یک Service از نوع headless برای ارتباط با سایر سازوکارهای کشف سرویس استفاده کنید،
بدون آنکه به پیاده‌سازی کوبرنتیز وابسته باشید.

برای Serviceهای headless، هیچ cluster IPای تخصیص داده نمی‌شود، kube-proxy به این Serviceها
رسیدگی نمی‌کند و هیچ توزیع بار یا پراکسی‌ای توسط پلتفرم برای آن‌ها انجام نمی‌شود.

یک Service از نوع headless به کلاینت اجازه می‌دهد مستقیماً به هر Podی که ترجیح می‌دهد متصل شود. Serviceهای headless
مسیرها و ارسال بسته‌ها را با استفاده از
[نشانی‌های IP مجازی و پراکسی‌ها](/docs/reference/networking/virtual-ips/) پیکربندی نمی‌کنند؛ در عوض، Serviceهای headless
نشانی‌های IP مربوط به endpointهای Podهای منفرد را از طریق رکوردهای DNS داخلی گزارش می‌کنند که از طریق
[سرویس DNS](/docs/concepts/services-networking/dns-pod-service/) کلاستر ارائه می‌شوند.
برای تعریف یک Service از نوع headless، Serviceای می‌سازید که `.spec.type` آن روی ClusterIP تنظیم شده است (که مقدار پیش‌فرض `type` نیز هست)
و علاوه بر آن `.spec.clusterIP` را روی None تنظیم می‌کنید.

مقدار رشته‌ای None حالتی خاص است و با تنظیم نکردن فیلد `.spec.clusterIP` یکسان نیست.

نحوهٔ پیکربندی خودکار DNS به این بستگی دارد که آیا Service انتخابگر تعریف‌شده دارد یا خیر:

### با انتخابگر

برای Serviceهای headless که انتخابگر تعریف می‌کنند، کنترل‌کنندهٔ endpointها
EndpointSliceهایی را در API کوبرنتیز ایجاد می‌کند و پیکربندی DNS را طوری تغییر می‌دهد که
رکوردهای A یا AAAA (نشانی‌های IPv4 یا IPv6) را برگرداند که مستقیماً به Podهای پشتیبان Service اشاره دارند.

### بدون انتخابگر

برای Serviceهای headless که انتخابگر تعریف نمی‌کنند، control plane
آبجکت‌های EndpointSlice ایجاد نمی‌کند. با این حال، سامانهٔ DNS یکی از موارد زیر را
جست‌وجو و پیکربندی می‌کند:

* رکوردهای DNS از نوع CNAME برای Serviceهای [`type: ExternalName`](#externalname).
* رکوردهای DNS از نوع A / AAAA برای همهٔ نشانی‌های IP مربوط به endpointهای آمادهٔ Service،
  برای همهٔ انواع Service به‌جز `ExternalName`.
  * برای endpointهای IPv4، سامانهٔ DNS رکوردهای A ایجاد می‌کند.
  * برای endpointهای IPv6، سامانهٔ DNS رکوردهای AAAA ایجاد می‌کند.

هنگامی که یک Service از نوع headless را بدون انتخابگر تعریف می‌کنید، `port` باید
با `targetPort` مطابقت داشته باشد.

## کشف سرویس‌ها

برای کلاینت‌هایی که درون کلاستر شما اجرا می‌شوند، کوبرنتیز از دو حالت اصلی برای
یافتن یک Service پشتیبانی می‌کند: متغیرهای محیطی و DNS.

### متغیرهای محیطی

هنگامی که یک Pod روی یک نود اجرا می‌شود، kubelet مجموعه‌ای از متغیرهای محیطی را
برای هر Service فعال اضافه می‌کند. این متغیرها شامل `{SVCNAME}_SERVICE_HOST` و `{SVCNAME}_SERVICE_PORT` هستند
که در آن‌ها نام Service با حروف بزرگ نوشته می‌شود و خط تیره‌ها به زیرخط تبدیل می‌شوند.


برای مثال، Service ‏`redis-primary` که پورت TCP ‏6379 را در دسترس قرار می‌دهد و
نشانی cluster IP ‏10.0.0.11 به آن تخصیص داده شده است، متغیرهای محیطی
زیر را تولید می‌کند:

```shell
REDIS_PRIMARY_SERVICE_HOST=10.0.0.11
REDIS_PRIMARY_SERVICE_PORT=6379
REDIS_PRIMARY_PORT=tcp://10.0.0.11:6379
REDIS_PRIMARY_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_PRIMARY_PORT_6379_TCP_PROTO=tcp
REDIS_PRIMARY_PORT_6379_TCP_PORT=6379
REDIS_PRIMARY_PORT_6379_TCP_ADDR=10.0.0.11
```

{{< note >}}
هنگامی که Podی دارید که باید به یک Service دسترسی داشته باشد و از
روش متغیر محیطی برای انتشار پورت و cluster IP به Podهای
کلاینت استفاده می‌کنید، باید Service را *پیش از* به وجود آمدن Podهای کلاینت ایجاد کنید.
در غیر این صورت، متغیرهای محیطی آن Podهای کلاینت مقداردهی نخواهند شد.

اگر تنها از DNS برای کشف cluster IP یک Service استفاده می‌کنید، لازم نیست
نگران این مسئلهٔ ترتیب باشید.
{{< /note >}}

کوبرنتیز همچنین از متغیرهایی پشتیبانی می‌کند و آن‌ها را فراهم می‌کند که با قابلیت
«_[legacy container links](https://docs.docker.com/network/links/)_» در Docker Engine سازگار هستند.
می‌توانید [`makeLinkVariables`](https://github.com/kubernetes/kubernetes/blob/dd2d12f6dc0e654c15d5db57a5f9f6ba61192726/pkg/kubelet/envvars/envvars.go#L72)
را بخوانید تا ببینید این قابلیت در کوبرنتیز چگونه پیاده‌سازی شده است.

### DNS

می‌توانید (و تقریباً همیشه باید) با استفاده از یک [افزونه (add-on)](/docs/concepts/cluster-administration/addons/)،
یک سرویس DNS برای کلاستر کوبرنتیز خود راه‌اندازی کنید.

یک سرور DNS آگاه از کلاستر، مانند CoreDNS، API کوبرنتیز را برای Serviceهای جدید
زیر نظر دارد و برای هر کدام مجموعه‌ای از رکوردهای DNS ایجاد می‌کند. اگر DNS در
سراسر کلاستر شما فعال شده باشد، همهٔ Podها باید به‌طور خودکار بتوانند
Serviceها را با نام DNS آن‌ها resolve کنند.

برای مثال، اگر Serviceای به نام `my-service` در فضای نام
`my-ns` کوبرنتیز داشته باشید، control plane و سرویس DNS با همکاری یکدیگر
یک رکورد DNS برای `my-service.my-ns` ایجاد می‌کنند. Podهای فضای نام `my-ns`
باید بتوانند با جست‌وجوی نام `my-service` سرویس را بیابند
(`my-service.my-ns` نیز کار می‌کند).

Podهای فضاهای نام دیگر باید نام را به‌صورت `my-service.my-ns` کامل کنند. این نام‌ها
به cluster IP تخصیص‌یافته به Service ‏resolve می‌شوند.

کوبرنتیز همچنین از رکوردهای DNS از نوع SRV (Service) برای پورت‌های نام‌دار پشتیبانی می‌کند. اگر
Service ‏`my-service.my-ns` پورتی با نام `http` و پروتکل
`TCP` داشته باشد، می‌توانید یک پرس‌وجوی DNS SRV برای `_http._tcp.my-service.my-ns` انجام دهید تا
شمارهٔ پورت `http` و همچنین نشانی IP را کشف کنید.

سرور DNS کوبرنتیز تنها راه دسترسی به Serviceهای `ExternalName` است.
می‌توانید اطلاعات بیشتری دربارهٔ resolve کردن `ExternalName` را در
[DNS برای Serviceها و Podها](/docs/concepts/services-networking/dns-pod-service/) بیابید.

<!-- preserve existing hyperlinks -->
<a id="shortcomings" />
<a id="the-gory-details-of-virtual-ips" />
<a id="proxy-modes" />
<a id="proxy-mode-userspace" />
<a id="proxy-mode-iptables" />
<a id="proxy-mode-ipvs" />
<a id="ips-and-vips" />

## سازوکار نشانی‌دهی IP مجازی

[IPهای مجازی و پراکسی‌های Service](/docs/reference/networking/virtual-ips/) را بخوانید؛ این صفحه
سازوکاری را توضیح می‌دهد که کوبرنتیز برای در دسترس قرار دادن یک Service با یک نشانی IP مجازی فراهم می‌کند.

### سیاست‌های ترافیک

می‌توانید فیلدهای `.spec.internalTrafficPolicy` و `.spec.externalTrafficPolicy` را تنظیم کنید
تا کنترل کنید کوبرنتیز چگونه ترافیک را به backendهای سالم («آماده») مسیریابی می‌کند.

برای جزئیات بیشتر، [سیاست‌های ترافیک](/docs/reference/networking/virtual-ips/#traffic-policies) را ببینید.

### کنترل توزیع ترافیک {#traffic-distribution}

فیلد `.spec.trafficDistribution` راه دیگری برای اثرگذاری بر مسیریابی ترافیک
درون یک Service کوبرنتیز فراهم می‌کند. در حالی که سیاست‌های ترافیک بر تضمین‌های
معنایی سخت‌گیرانه تمرکز دارند، توزیع ترافیک به شما امکان می‌دهد _ترجیحات_ خود را بیان کنید
(مانند مسیریابی به endpointهایی که از نظر توپولوژی نزدیک‌تر هستند). این کار می‌تواند به بهینه‌سازی
کارایی، هزینه یا قابلیت اطمینان کمک کند. در کوبرنتیز {{< skew currentVersion >}}،
مقادیر زیر پشتیبانی می‌شوند:

`PreferSameZone`
: ترجیح برای مسیریابی ترافیک به endpointهایی را نشان می‌دهد که در همان
  ناحیه (zone)ای قرار دارند که کلاینت در آن است.

`PreferSameNode`
: ترجیح برای مسیریابی ترافیک به endpointهایی را نشان می‌دهد که روی همان
  نودی قرار دارند که کلاینت روی آن است.

`PreferClose` (منسوخ‌شده)
: این نام مستعار قدیمی‌تری برای `PreferSameZone` است که معنای آن
  کمتر روشن است.

اگر این فیلد تنظیم نشده باشد، پیاده‌سازی راهبرد مسیریابی پیش‌فرض خود را اعمال خواهد کرد.

برای جزئیات بیشتر، [توزیع
ترافیک](/docs/reference/networking/virtual-ips/#traffic-distribution) را
ببینید

### چسبندگی نشست (Session stickiness)

اگر می‌خواهید اطمینان حاصل کنید که اتصال‌های یک کلاینت مشخص هر بار به
همان Pod ارسال می‌شوند، می‌توانید وابستگی نشست (session affinity) را بر اساس
نشانی IP کلاینت پیکربندی کنید. برای آشنایی بیشتر، [وابستگی نشست](/docs/reference/networking/virtual-ips/#session-affinity)
را بخوانید.

## IPهای خارجی

{{< feature-state for_k8s_version="v1.36" state="deprecated" >}}

همهٔ کاربران باید مهاجرت از `externalIPs` را آغاز کنند.
به‌جای آن، استفاده از یک کنترل‌کنندهٔ توزیع‌کنندهٔ بار خارجی یا یک پیاده‌سازی Gateway API
را در نظر بگیرید.

اگر IPهای خارجی‌ای وجود داشته باشند که به یک یا چند نود کلاستر مسیریابی می‌شوند، Serviceهای کوبرنتیز
می‌توانند روی آن `externalIPs` در دسترس قرار گیرند. هنگامی که ترافیک شبکه با
IP خارجی (به‌عنوان IP مقصد) و پورتی منطبق با آن Service وارد کلاستر می‌شود، قواعد و مسیرهایی
که کوبرنتیز پیکربندی کرده است تضمین می‌کنند که ترافیک به یکی از endpointهای
آن Service هدایت شود.

هنگام تعریف یک Service، می‌توانید `externalIPs` را برای هر
[نوع سرویس](#publishing-services-service-types) تعیین کنید.
در مثال زیر، کلاینت‌ها می‌توانند با استفاده از TCP و روی
`"198.51.100.32:80"` (که از `.spec.externalIPs[]` و `.spec.ports[].port` محاسبه می‌شود) به Service با نام `"my-service"` دسترسی داشته باشند.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 49152
  externalIPs:
    - 198.51.100.32
```

{{< note >}}
کوبرنتیز تخصیص `externalIPs` را مدیریت نمی‌کند؛ این مسئولیت
بر عهدهٔ مدیر کلاستر است.
{{< /note >}}

## آبجکت API

Service یک منبع سطح بالا در REST API کوبرنتیز است. می‌توانید جزئیات بیشتری
دربارهٔ [آبجکت API مربوط به Service](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#service-v1-core) بیابید.

## {{% heading "whatsnext" %}}

دربارهٔ Serviceها و جایگاه آن‌ها در کوبرنتیز بیشتر بیاموزید:

* آموزش [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/)
  را دنبال کنید.
* دربارهٔ [Ingress](/docs/concepts/services-networking/ingress/) بخوانید که
  مسیرهای HTTP و HTTPS را از بیرون کلاستر به Serviceهای درون
  کلاستر شما در دسترس قرار می‌دهد.
* دربارهٔ [Gateway](/docs/concepts/services-networking/gateway/) بخوانید؛ افزونه‌ای برای
  کوبرنتیز که انعطاف‌پذیری بیشتری نسبت به Ingress فراهم می‌کند.

برای آشنایی بیشتر با زمینهٔ موضوع، موارد زیر را بخوانید:

* [IPهای مجازی و پراکسی‌های Service](/docs/reference/networking/virtual-ips/)
* [EndpointSliceها](/docs/concepts/services-networking/endpoint-slices/)
* [مرجع API مربوط به Service](/docs/reference/kubernetes-api/service-resources/service-v1/)
* [مرجع API مربوط به EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/)
* [مرجع API مربوط به Endpoint (قدیمی)](/docs/reference/kubernetes-api/service-resources/endpoints-v1/)

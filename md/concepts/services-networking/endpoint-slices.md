---
reviewers:
- freehan
title: EndpointSliceها
api_metadata:
- apiVersion: "discovery.k8s.io/v1"
  kind: "EndpointSlice"
content_type: concept
weight: 60
description: >-
  API مربوط به EndpointSlice سازوکاری است که کوبرنتیز به کمک آن به Service شما اجازه می‌دهد
  برای رسیدگی به تعداد زیادی backend مقیاس‌پذیر باشد و به کلاستر امکان می‌دهد فهرست
  backendهای سالم خود را به‌طور کارآمد به‌روزرسانی کند.
---


<!-- overview -->

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

{{< glossary_definition term_id="endpoint-slice" length="short" >}}

<!-- body -->

## API مربوط به EndpointSlice {#endpointslice-resource}

در کوبرنتیز، یک EndpointSlice ارجاع‌هایی به مجموعه‌ای از endpointهای شبکه
را در بر دارد. control plane به‌طور خودکار برای هر Service کوبرنتیز که یک
{{< glossary_tooltip text="انتخابگر"
term_id="selector" >}} برای آن تعیین شده باشد، EndpointSliceهایی ایجاد می‌کند. این EndpointSliceها
ارجاع‌هایی به همهٔ Podهایی را که با انتخابگر Service مطابقت دارند، در بر دارند. EndpointSliceها
endpointهای شبکه را بر اساس ترکیب‌های یکتای خانوادهٔ IP، پروتکل،
شمارهٔ پورت و نام Service گروه‌بندی می‌کنند.
نام یک آبجکت EndpointSlice باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

به‌عنوان نمونه، در اینجا یک آبجکت EndpointSlice نمونه آمده است که مالک آن Service کوبرنتیزِ
`example` است.

```yaml
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-abc
  labels:
    kubernetes.io/service-name: example
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 80
endpoints:
  - addresses:
      - "10.1.2.3"
    conditions:
      ready: true
    hostname: pod-1
    nodeName: node-1
    zone: us-west2-a
```

به‌طور پیش‌فرض، control plane، EndpointSliceها را طوری ایجاد و مدیریت می‌کند که هر کدام
بیش از ۱۰۰ endpoint نداشته باشند. می‌توانید این مقدار را با فلگ
`--max-endpoints-per-slice` در
{{< glossary_tooltip text="kube-controller-manager" term_id="kube-controller-manager" >}}
پیکربندی کنید که حداکثر تا ۱۰۰۰ امکان‌پذیر است.

EndpointSliceها در خصوص نحوهٔ مسیریابی ترافیک داخلی،
به‌عنوان منبع مرجع (source of truth) برای {{< glossary_tooltip term_id="kube-proxy" text="kube-proxy" >}}
عمل می‌کنند.

### انواع نشانی

EndpointSliceها از دو نوع نشانی پشتیبانی می‌کنند:

* IPv4
* IPv6

هر آبجکت `EndpointSlice` نمایندهٔ یک نوع نشانی IP مشخص است. اگر
Serviceای داشته باشید که از طریق IPv4 و IPv6 در دسترس است، دست‌کم دو آبجکت
`EndpointSlice` وجود خواهد داشت (یکی برای IPv4 و یکی برای IPv6).

### وضعیت‌ها (Conditions)

API مربوط به EndpointSlice وضعیت‌هایی دربارهٔ endpointها ذخیره می‌کند که ممکن است برای مصرف‌کنندگان مفید باشند.
این سه وضعیت عبارت‌اند از `serving`، `terminating` و `ready`.

#### Serving

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

وضعیت `serving` نشان می‌دهد که endpoint در حال حاضر در حال ارائهٔ پاسخ است و
بنابراین باید به‌عنوان مقصدی برای ترافیک Service استفاده شود. برای endpointهایی که پشتوانهٔ آن‌ها یک Pod است،
این وضعیت با وضعیت `Ready` مربوط به Pod متناظر است.

#### Terminating

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

وضعیت `terminating` نشان می‌دهد که endpoint در حال
خاتمه یافتن است. برای endpointهایی که پشتوانهٔ آن‌ها یک Pod است، این وضعیت زمانی تنظیم می‌شود که
Pod برای نخستین بار حذف می‌شود (یعنی هنگامی که یک برچسب زمانی حذف (deletion
timestamp) دریافت می‌کند، اما به احتمال زیاد پیش از آنکه کانتینرهای Pod خارج شوند).

پراکسی‌های Service معمولاً endpointهایی را که در وضعیت `terminating` هستند نادیده می‌گیرند،
اما اگر همهٔ endpointهای موجود در وضعیت `terminating` باشند، ممکن است ترافیک را به endpointهایی که هم `serving` و هم
`terminating` هستند هدایت کنند. (این کار
کمک می‌کند تا اطمینان حاصل شود که هیچ ترافیکی از Service در طول به‌روزرسانی‌های تدریجی (rolling update)
Podهای زیرین از دست نمی‌رود.)

#### Ready

وضعیت `ready` در اصل میان‌بری برای بررسی
«`serving` و نه `terminating`» است (هرچند برای Serviceهایی که `spec.publishNotReadyAddresses` آن‌ها روی
`true` تنظیم شده است، همواره مقدار `true` خواهد داشت).

### اطلاعات توپولوژی {#topology}

هر endpoint درون یک EndpointSlice می‌تواند اطلاعات توپولوژی مرتبط را در بر داشته باشد.
اطلاعات توپولوژی شامل مکان endpoint و اطلاعاتی
دربارهٔ Node و ناحیه (zone) متناظر است. این اطلاعات در فیلدهای زیر که برای هر endpoint
در EndpointSliceها وجود دارند، در دسترس است:

* `nodeName` - نام Nodeی که این endpoint روی آن قرار دارد.
* `zone` - ناحیه‌ای که این endpoint در آن قرار دارد.

### مدیریت

در بیشتر موارد، control plane (به‌طور مشخص، {{< glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller" >}}
endpoint slice) آبجکت‌های EndpointSlice را ایجاد و
مدیریت می‌کند. موارد استفادهٔ گوناگون دیگری نیز برای
EndpointSliceها وجود دارد، مانند پیاده‌سازی‌های service mesh، که ممکن است منجر به آن شوند که موجودیت‌ها
یا کنترل‌کننده‌های دیگری مجموعه‌های بیشتری از EndpointSliceها را مدیریت کنند.

برای اطمینان از اینکه چند موجودیت می‌توانند بدون تداخل با یکدیگر EndpointSliceها را مدیریت کنند،
کوبرنتیز {{< glossary_tooltip term_id="label" text="برچسب" >}}
`endpointslice.kubernetes.io/managed-by` را تعریف می‌کند که موجودیتِ مدیریت‌کنندهٔ
یک EndpointSlice را نشان می‌دهد.
کنترل‌کنندهٔ endpoint slice مقدار `endpointslice-controller.k8s.io` را به‌عنوان مقدار
این برچسب روی همهٔ EndpointSliceهایی که مدیریت می‌کند، تنظیم می‌کند. سایر موجودیت‌هایی که
EndpointSliceها را مدیریت می‌کنند نیز باید مقدار یکتایی برای این برچسب تنظیم کنند.

### مالکیت

در بیشتر موارد استفاده، مالک EndpointSliceها همان Serviceای است که آبجکت endpoint
slice، endpointهای آن را ردیابی می‌کند. این مالکیت با یک ارجاع مالک (owner
reference) روی هر EndpointSlice و همچنین یک برچسب `kubernetes.io/service-name`
نشان داده می‌شود که جست‌وجوی ساده‌ی همهٔ EndpointSliceهای متعلق به یک Service را ممکن می‌سازد.

### توزیع EndpointSliceها

هر EndpointSlice مجموعه‌ای از پورت‌ها دارد که بر همهٔ endpointهای درون آن
منبع اعمال می‌شود. هنگامی که برای یک Service از پورت‌های نام‌دار استفاده می‌شود، ممکن است Podها
برای یک پورت نام‌دار یکسان، شماره‌های پورت مقصد متفاوتی داشته باشند که در این صورت به
EndpointSliceهای متفاوتی نیاز است.

control plane تلاش می‌کند EndpointSliceها را تا حد امکان پر کند، اما
به‌طور فعال آن‌ها را دوباره متوازن نمی‌کند. منطق این کار نسبتاً ساده است:

1. EndpointSliceهای موجود را پیمایش می‌کند، endpointهایی را که دیگر
   مورد نیاز نیستند حذف می‌کند و endpointهای منطبقی را که تغییر کرده‌اند به‌روزرسانی می‌کند.
2. EndpointSliceهایی را که در گام نخست تغییر کرده‌اند پیمایش می‌کند و
   آن‌ها را با هر endpoint جدید مورد نیاز پر می‌کند.
3. اگر هنوز endpointهای جدیدی برای افزودن باقی مانده باشد، تلاش می‌کند آن‌ها را در sliceای که پیش‌تر
   تغییر نکرده است جای دهد و/یا sliceهای جدیدی ایجاد می‌کند.

نکتهٔ مهم این است که گام سوم، محدود کردن به‌روزرسانی‌های EndpointSlice را بر
توزیع کاملاً پر EndpointSliceها اولویت می‌دهد. برای مثال، اگر ۱۰
endpoint جدید برای افزودن وجود داشته باشد و ۲ EndpointSlice که هر کدام جای ۵ endpoint دیگر را دارند،
این رویکرد به‌جای پر کردن ۲ EndpointSlice موجود، یک EndpointSlice جدید
ایجاد می‌کند. به بیان دیگر، ایجاد یک EndpointSlice واحد
بر چندین به‌روزرسانی EndpointSlice ترجیح دارد.

از آنجا که kube-proxy روی هر Node اجرا می‌شود و EndpointSliceها را زیر نظر دارد، هر تغییر
در یک EndpointSlice نسبتاً پرهزینه است، زیرا به
همهٔ Nodeهای کلاستر منتقل می‌شود. هدف این رویکرد محدود کردن تعداد
تغییراتی است که باید به هر Node ارسال شوند، حتی اگر به ایجاد چندین
EndpointSlice ناپر منجر شود.

در عمل، چنین توزیع نه‌چندان ایدئالی باید نادر باشد. بیشتر تغییراتی
که کنترل‌کنندهٔ EndpointSlice پردازش می‌کند به اندازه‌ای کوچک هستند که در یک
EndpointSlice موجود جای بگیرند و اگر چنین نباشد، احتمالاً به‌زودی به یک EndpointSlice جدید
در هر صورت نیاز خواهد بود. به‌روزرسانی‌های تدریجی Deploymentها نیز با جایگزین شدن همهٔ Podها و
endpointهای متناظرشان، به‌طور طبیعی EndpointSliceها را دوباره بسته‌بندی می‌کنند.

### endpointهای تکراری

به دلیل ماهیت تغییرات EndpointSlice، ممکن است endpointها هم‌زمان در بیش از
یک EndpointSlice نمایش داده شوند. این امر به‌طور طبیعی رخ می‌دهد، زیرا تغییرات
آبجکت‌های EndpointSlice مختلف ممکن است در زمان‌های متفاوتی به watch / cache کلاینت کوبرنتیز
برسند.

{{< note >}}
کلاینت‌های API مربوط به EndpointSlice باید همهٔ EndpointSliceهای موجودِ
مرتبط با یک Service را پیمایش کنند و فهرست کاملی از endpointهای شبکهٔ یکتا بسازند.
ذکر این نکته اهمیت دارد که endpointها ممکن است در EndpointSliceهای مختلف تکرار شوند.

می‌توانید یک پیاده‌سازی مرجع برای نحوهٔ انجام این تجمیع endpointها
و حذف موارد تکراری را در بخشی از کد `EndpointSliceCache` درون `kube-proxy` بیابید.
{{< /note >}}

### بازتاب (mirroring) EndpointSlice

{{< feature-state for_k8s_version="v1.33" state="deprecated" >}}

API مربوط به EndpointSlice جایگزینی برای API قدیمی‌تر Endpoints است. برای
حفظ سازگاری با کنترل‌کننده‌های قدیمی‌تر و بارهای کاری کاربران که
انتظار دارند {{<glossary_tooltip term_id="kube-proxy" text="kube-proxy">}}
ترافیک را بر اساس منابع Endpoints مسیریابی کند، control plane
کلاستر بیشتر منابع Endpoints ایجادشده توسط کاربر را در
EndpointSliceهای متناظر بازتاب می‌دهد.

(با این حال، این قابلیت، مانند بقیهٔ API مربوط به Endpoints،
منسوخ شده است. کاربرانی که endpointها را برای Serviceهای بدون انتخابگر به‌صورت دستی تعیین می‌کنند،
باید این کار را با ایجاد مستقیم منابع EndpointSlice انجام دهند،
نه با ایجاد منابع Endpoints و اجازه دادن به بازتاب
آن‌ها.)

control plane منابع Endpoints را بازتاب می‌دهد، مگر اینکه:

* منبع Endpoints برچسب `endpointslice.kubernetes.io/skip-mirror`
  را با مقدار `true` داشته باشد.
* منبع Endpoints حاشیه‌نویسی (annotation) `control-plane.alpha.kubernetes.io/leader`
  را داشته باشد.
* منبع Service متناظر وجود نداشته باشد.
* منبع Service متناظر انتخابگری غیرتهی (non-nil) داشته باشد.

هر منبع Endpoints ممکن است به چند EndpointSlice تبدیل شود. این امر
زمانی رخ می‌دهد که یک منبع Endpoints چند زیرمجموعه (subset) داشته باشد یا endpointهایی
با چند خانوادهٔ IP (IPv4 و IPv6) را در بر داشته باشد. حداکثر ۱۰۰۰ نشانی از هر
زیرمجموعه در EndpointSliceها بازتاب داده می‌شود.

## {{% heading "whatsnext" %}}

* آموزش [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/) را دنبال کنید
* [مرجع API](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/) مربوط به API ‏EndpointSlice را بخوانید
* [مرجع API](/docs/reference/kubernetes-api/service-resources/endpoints-v1/) مربوط به API ‏Endpoints را بخوانید

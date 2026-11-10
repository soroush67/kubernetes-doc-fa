---
title: مفاهیم API کوبرنتیز
reviewers:
- smarterclayton
- lavalamp
- liggitt
content_type: concept
weight: 20
---

<!-- overview -->
رابط برنامه‌نویسی (API) کوبرنتیز یک رابط برنامه‌نویسی مبتنی بر منبع (RESTful) است که از طریق HTTP ارائه می‌شود. این API از بازیابی، ایجاد، به‌روزرسانی و حذف منابع اصلی با فعل‌های استاندارد HTTP (POST، PUT، PATCH، DELETE، GET) پشتیبانی می‌کند.

برای برخی منابع، API زیرمنابع (subresource) دیگری نیز دارد که امکان مجوزدهی دقیق‌تر را فراهم می‌کنند (مانند نماهای جداگانه برای جزئیات Pod و بازیابی لاگ‌ها). همچنین API می‌تواند برای سهولت یا کارایی بیشتر، این منابع را در بازنمایی‌های مختلف بپذیرد و ارائه کند.

کوبرنتیز اعلان کارآمد تغییرات منابع را از طریق _watch_ (پایش) پشتیبانی می‌کند:
{{< glossary_definition prepend="in the Kubernetes API, watch is" term_id="watch" length="short" >}}
کوبرنتیز همچنین عملیات list سازگار (consistent) فراهم می‌کند تا کلاینت‌های API بتوانند وضعیت منابع را به‌طور مؤثر کش، ردیابی و همگام‌سازی کنند.

می‌توانید [مرجع API](/docs/reference/kubernetes-api/) را به‌صورت آنلاین ببینید، یا برای آشنایی کلی با API به خواندن ادامه دهید.

<!-- body -->
## اصطلاحات API کوبرنتیز {#standard-api-terminology}

کوبرنتیز معمولاً برای توصیف مفاهیم API از اصطلاحات رایج RESTful استفاده می‌کند:

* *نوع منبع* (resource type) نامی است که در URL به کار می‌رود (`pods`، `namespaces`، `services`)
* هر نوع منبع یک بازنمایی مشخص (شِمای آبجکت آن) دارد که *kind* نامیده می‌شود
* فهرستی از نمونه‌های یک نوع منبع، *مجموعه* (collection) نامیده می‌شود
* یک نمونهٔ واحد از یک نوع منبع، *منبع* (resource) نامیده می‌شود و معمولاً نمایانگر یک *آبجکت* نیز هست
* برای برخی انواع منبع، API یک یا چند *زیرمنبع* دارد که به‌صورت مسیرهای URI زیر آن منبع نمایش داده می‌شوند

بیشتر انواع منبع در API کوبرنتیز {{< glossary_tooltip text="آبجکت" term_id="object" >}} هستند؛ یعنی نمونه‌ای مشخص از یک مفهوم در کلاستر را نمایش می‌دهند، مانند یک پاد یا یک فضای نام. تعداد کمتری از انواع منبع API *مجازی* هستند، به این معنا که اغلب به‌جای خود آبجکت‌ها، عملیاتی روی آبجکت‌ها را نمایش می‌دهند؛ مانند بررسی مجوز (یک درخواست POST با بدنه‌ای از نوع `SubjectAccessReview` که با JSON کدگذاری شده است به منبع `subjectaccessreviews` بفرستید)، یا زیرمنبع `eviction` یک Pod (که برای راه‌اندازی [بیرون‌رانی آغازشده از طریق API](/docs/concepts/scheduling-eviction/api-eviction/) استفاده می‌شود).

### نام آبجکت‌ها

همهٔ آبجکت‌هایی که می‌توانید از طریق API ایجاد کنید یک {{< glossary_tooltip text="نام" term_id="name" >}} یکتا دارند تا ایجاد و بازیابی آن‌ها به‌صورت خودتوان (idempotent) ممکن باشد؛ با این استثنا که انواع منبع مجازی، اگر قابل بازیابی نباشند یا به خودتوانی وابسته نباشند، ممکن است نام یکتا نداشته باشند.

در یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}}، هویت یکتای هر آبجکت با چندتایی **گروه API**، **منبع**، **فضای نام** و **نام** آن تعیین می‌شود.

* **میان‌گروهی (Cross-Group):** اگر دو آبجکت به گروه‌های API متفاوتی تعلق داشته باشند (برای مثال `apps` در برابر `example.com`)، می‌توانند نام یکسانی داشته باشند.
* **میان‌نسخه‌ای (Cross-Version):** نسخه‌های مختلف API (مانند `v1` و `v1beta1`) از یک گروه و منبع یکسان، داده‌های زیربنایی یکسانی را نمایش می‌دهند. ایجاد آبجکتی با نام یکسان در نسخهٔ دیگری از همان گروه به تداخل نام می‌انجامد، زیرا این آبجکت‌ها در ذخیره‌سازی هویت یکسانی دارند.

برخی آبجکت‌ها به فضای نام تعلق ندارند (برای مثال Nodeها)، بنابراین نام آن‌ها باید در کل کلاستر یکتا باشد.

### فعل‌های API

تقریباً همهٔ انواع منبعِ آبجکت از فعل‌های استاندارد HTTP، یعنی GET، POST، PUT، PATCH و DELETE، پشتیبانی می‌کنند. کوبرنتیز فعل‌های مخصوص به خود را نیز به کار می‌برد که اغلب با حروف کوچک نوشته می‌شوند تا از فعل‌های HTTP متمایز شوند.

کوبرنتیز برای توصیف عمل بازگرداندن یک [مجموعه](#collections) از منابع، اصطلاح **list** را به کار می‌برد تا آن را از بازیابی یک منبع واحد، که معمولاً **get** نامیده می‌شود، متمایز کند. اگر یک درخواست HTTP GET با پارامتر پرس‌وجوی `?watch` بفرستید، کوبرنتیز آن را **watch** می‌نامد و نه **get** (برای جزئیات بیشتر، [تشخیص کارآمد تغییرات](#efficient-detection-of-changes) را ببینید).

کوبرنتیز درخواست‌های PUT را بر اساس وضعیت آبجکت موجود، به‌طور داخلی در یکی از دو دستهٔ **create** یا **update** قرار می‌دهد. عمل **update** با **patch** تفاوت دارد؛ فعل HTTP مربوط به **patch**، PATCH است.

## مسیرهای URI منابع

دامنهٔ هر نوع منبع یا کل کلاستر است (`/apis/GROUP/VERSION/*`) یا یک فضای نام (`/apis/GROUP/VERSION/namespaces/NAMESPACE/*`). منابعی که دامنهٔ آن‌ها فضای نام است، با حذف فضای نام مربوط حذف می‌شوند و دسترسی به آن نوع منبع با بررسی‌های مجوز در سطح فضای نام کنترل می‌شود.

توجه: منابع هسته (core) به‌جای `/apis` از `/api` استفاده می‌کنند و بخش GROUP را در مسیر ندارند.

نمونه‌ها:

* `/api/v1/namespaces`
* `/api/v1/pods`
* `/api/v1/namespaces/my-namespace/pods`
* `/apis/apps/v1/deployments`
* `/apis/apps/v1/namespaces/my-namespace/deployments`
* `/apis/apps/v1/namespaces/my-namespace/deployments/my-deployment`

همچنین می‌توانید به مجموعه‌هایی از منابع دسترسی داشته باشید (برای مثال، فهرست‌کردن همهٔ Nodeها). مسیرهای زیر برای بازیابی مجموعه‌ها و منابع استفاده می‌شوند:

* منابع با دامنهٔ کلاستر:

  * مسیر `GET /apis/GROUP/VERSION/RESOURCETYPE`: مجموعهٔ منابعِ آن نوع منبع را برمی‌گرداند
  * مسیر `GET /apis/GROUP/VERSION/RESOURCETYPE/NAME`: منبعی با نام NAME از آن نوع منبع را برمی‌گرداند

* منابع با دامنهٔ فضای نام:

  * مسیر `GET /apis/GROUP/VERSION/RESOURCETYPE`: مجموعهٔ همهٔ نمونه‌های آن نوع منبع را در همهٔ فضاهای نام برمی‌گرداند
  * مسیر `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE`: مجموعهٔ همهٔ نمونه‌های آن نوع منبع را در فضای نام NAMESPACE برمی‌گرداند
  * مسیر `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE/NAME`: نمونه‌ای از آن نوع منبع را که نامش NAME است، در فضای نام NAMESPACE برمی‌گرداند

از آنجا که فضای نام خود یک نوع منبع با دامنهٔ کلاستر است، می‌توانید فهرست («مجموعهٔ») همهٔ فضاهای نام را با `GET /api/v1/namespaces` و جزئیات یک فضای نام خاص را با `GET /api/v1/namespaces/NAME` بازیابی کنید.

* زیرمنبع با دامنهٔ کلاستر: `GET /apis/GROUP/VERSION/RESOURCETYPE/NAME/SUBRESOURCE`
* زیرمنبع با دامنهٔ فضای نام: `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE/NAME/SUBRESOURCE`

فعل‌هایی که هر زیرمنبع پشتیبانی می‌کند به آبجکت بستگی دارد؛ برای اطلاعات بیشتر [مرجع API](/docs/reference/kubernetes-api/) را ببینید. دسترسی هم‌زمان به زیرمنابعِ چند منبع ممکن نیست؛ اگر چنین نیازی پیش بیاید، معمولاً از یک نوع منبع مجازی جدید استفاده می‌شود.

## نوع‌های رسانهٔ HTTP {#alternate-representations-of-resources}

کوبرنتیز روی HTTP از کدگذاری‌های انتقال JSON، YAML، CBOR و Protobuf پشتیبانی می‌کند.

کوبرنتیز به‌طور پیش‌فرض آبجکت‌ها را با [سریال‌سازی JSON](#json-encoding) و نوع رسانهٔ (media type) `application/json` برمی‌گرداند. با اینکه JSON پیش‌فرض است، کلاینت‌ها می‌توانند پاسخ را با قالب YAML درخواست کنند، یا برای کارایی بهتر در مقیاس بزرگ از [بازنمایی Protobuf](#protobuf-encoding) که باینری و کارآمدتر است استفاده کنند.

رابط API کوبرنتیز سازوکار استاندارد مذاکرهٔ نوع محتوا (content type negotiation) در HTTP را پیاده‌سازی می‌کند: با ارسال سرآیند `Accept` همراه یک فراخوانی `GET`، از سرور می‌خواهید که تلاش کند پاسخ را با نوع رسانهٔ دلخواه شما برگرداند. اگر می‌خواهید در یک درخواست `PUT` یا `POST` آبجکتی را با قالب Protobuf به سرور بفرستید، باید سرآیند `Content-Type` درخواست را به‌درستی تنظیم کنید.

اگر نوع رسانهٔ موجودی را درخواست کنید، سرور API پاسخی با `Content-Type` مناسب برمی‌گرداند؛ اگر هیچ‌یک از نوع‌های رسانهٔ درخواستی شما پشتیبانی نشود، سرور API پیام خطای `406 Not acceptable` را برمی‌گرداند.
همهٔ انواع منبع داخلی از نوع رسانهٔ `application/json` پشتیبانی می‌کنند.

#### کدگذاری تکه‌تکهٔ مجموعه‌ها

کوبرنتیز برای کدگذاری‌های JSON و Protobuf، کدگذارهای سفارشی‌ای پیاده‌سازی می‌کند که خروجی را آیتم‌به‌آیتم می‌نویسند. این قابلیت خروجی را تغییر نمی‌دهد، اما باعث می‌شود سرور API مجبور نباشد کل پاسخ LIST را در حافظه بارگذاری کند. برای مجموعه‌های بزرگ منابع (بیش از 100MB) باید از به‌کارگیری انواع دیگر کدگذاری (از جمله نمایش خوانای JSON) پرهیز کرد، زیرا ممکن است بر کارایی اثر منفی بگذارد.

### کدگذاری JSON منابع {#json-encoding}

رابط API کوبرنتیز به‌طور پیش‌فرض برای کدگذاری بدنهٔ پیام‌های HTTP از [JSON](https://www.json.org/json-en.html) استفاده می‌کند.

برای مثال:

1. همهٔ پادهای یک کلاستر را بدون تعیین قالب ترجیحی فهرست کنید

   ```
   GET /api/v1/pods
   ```

   ```
   200 OK
   Content-Type: application/json

   … JSON encoded collection of Pods (PodList object)
   ```

1. با ارسال JSON به سرور و درخواست پاسخ JSON، یک پاد ایجاد کنید.

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/json
   Accept: application/json
   … JSON encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/json

   {
     "kind": "Pod",
     "apiVersion": "v1",
     …
   }
   ```

همچنین می‌توانید بازنمایی‌های [جدولی](#table-fetches) و [فقط فراداده](#metadata-only-fetches) را با این کدگذاری درخواست کنید.

### کدگذاری YAML منابع {#yaml-encoding}

کوبرنتیز از نوع رسانهٔ [`application/yaml`](https://www.rfc-editor.org/rfc/rfc9512.html) نیز، هم برای درخواست‌ها و هم برای پاسخ‌ها، پشتیبانی می‌کند. از [`YAML`](https://yaml.org/) می‌توان برای تعریف مانیفست‌های کوبرنتیز و تعامل با API استفاده کرد.

برای مثال:

1. همهٔ پادهای یک کلاستر را با قالب YAML فهرست کنید

   ```
   GET /api/v1/pods
   Accept: application/yaml
   ```
   
   ```
   200 OK
   Content-Type: application/yaml

   … YAML encoded collection of Pods (PodList object)
   ```

1. با ارسال داده‌های کدگذاری‌شده با YAML به سرور و درخواست پاسخ YAML، یک پاد ایجاد کنید:

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/yaml
   Accept: application/yaml
   … YAML encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/yaml

   apiVersion: v1
   kind: Pod
   metadata:
     name: my-pod
     …
   ```

همچنین می‌توانید بازنمایی‌های [جدولی](#table-fetches) و [فقط فراداده](#metadata-only-fetches) را با این کدگذاری درخواست کنید.

### کدگذاری Protobuf کوبرنتیز {#protobuf-encoding}

کوبرنتیز برای کدگذاری پاسخ‌های [Protobuf](https://protobuf.dev/) از یک پوشش (envelope wrapper) استفاده می‌کند. این پوشش با یک عدد جادویی ۴ بایتی آغاز می‌شود که کمک می‌کند محتوای ذخیره‌شده روی دیسک یا در etcd به‌عنوان Protobuf (و نه JSON) شناسایی شود. پس از داده‌های عدد جادویی ۴ بایتی، یک پیام پوششی کدگذاری‌شده با Protobuf قرار می‌گیرد که کدگذاری و نوع آبجکت زیربنایی را توصیف می‌کند. درون این پیام پوششی Protobuf، داده‌های آبجکت درونی در فیلد `raw` از Unknown ثبت می‌شوند (برای جزئیات بیشتر، [IDL](#protobuf-encoding-idl) را ببینید).

برای مثال:

1. همهٔ پادهای یک کلاستر را با قالب Protobuf فهرست کنید.

   ```
   GET /api/v1/pods
   Accept: application/vnd.kubernetes.protobuf
   ```

   ```
   200 OK
   Content-Type: application/vnd.kubernetes.protobuf

   … binary encoded collection of Pods (PodList object)
   ```

1. با ارسال داده‌های کدگذاری‌شده با Protobuf به سرور یک پاد ایجاد کنید، اما پاسخ را با قالب JSON درخواست کنید.

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/vnd.kubernetes.protobuf
   Accept: application/json
   … binary encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/json

   {
     "kind": "Pod",
     "apiVersion": "v1",
     ...
   }
   ```

می‌توانید هر دو روش را با هم به کار ببرید و از کدگذاری Protobuf کوبرنتیز برای تعامل با هر APIای که از آن پشتیبانی می‌کند، هم برای خواندن و هم برای نوشتن، استفاده کنید. تنها برخی از انواع منبع API با Protobuf [سازگار](#protobuf-encoding-compatibility) هستند.

<a id="protobuf-encoding-idl" />

قالب این پوشش به این صورت است:

```
A four byte magic number prefix:
  Bytes 0-3: "k8s\x00" [0x6b, 0x38, 0x73, 0x00]

An encoded Protobuf message with the following IDL:
  message Unknown {
    // typeMeta should have the string values for "kind" and "apiVersion" as set on the JSON object
    optional TypeMeta typeMeta = 1;

    // raw will hold the complete serialized object in protobuf. See the protobuf definitions in the client libraries for a given kind.
    optional bytes raw = 2;

    // contentEncoding is encoding used for the raw data. Unspecified means no encoding.
    optional string contentEncoding = 3;

    // contentType is the serialization method used to serialize 'raw'. Unspecified means application/vnd.kubernetes.protobuf and is usually
    // omitted.
    optional string contentType = 4;
  }

  message TypeMeta {
    // apiVersion is the group/version for this type
    optional string apiVersion = 1;
    // kind is the name of the object schema. A protobuf definition should exist for this object.
    optional string kind = 2;
  }
```

{{< note >}}
کلاینت‌هایی که پاسخی با نوع `application/vnd.kubernetes.protobuf` دریافت می‌کنند که با پیشوند مورد انتظار مطابقت ندارد، باید آن پاسخ را رد کنند؛ زیرا ممکن است در نسخه‌های آینده لازم شود قالب سریال‌سازی به شکلی ناسازگار تغییر کند و این تغییر با عوض‌کردن پیشوند انجام خواهد شد.
{{< /note >}}

همچنین می‌توانید بازنمایی‌های [جدولی](#table-fetches) و [فقط فراداده](#metadata-only-fetches) را با این کدگذاری درخواست کنید.

#### سازگاری با Protobuf کوبرنتیز {#protobuf-encoding-compatibility}

همهٔ انواع منبع API از کدگذاری Protobuf کوبرنتیز پشتیبانی نمی‌کنند؛ به‌طور مشخص، Protobuf برای منابعی که به‌صورت {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitions" >}} تعریف شده‌اند یا از طریق {{< glossary_tooltip text="لایهٔ تجمیع" term_id="aggregation-layer" >}} ارائه می‌شوند، در دسترس نیست.

اگر به‌عنوان کلاینت ممکن است با انواع افزونه (extension) کار کنید، باید چند نوع محتوا را در سرآیند `Accept` درخواست مشخص کنید تا امکان بازگشت به JSON فراهم باشد.
برای مثال:

```
Accept: application/vnd.kubernetes.protobuf, application/json
```

### کدگذاری CBOR منابع {#cbor-encoding}

{{< feature-state feature_gate_name="CBORServingAndStorage" >}}

با فعال بودن [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `CBORServingAndStorage`، بدنهٔ درخواست‌ها و پاسخ‌ها برای همهٔ انواع منبع داخلی و همهٔ منابعی که با یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} تعریف شده‌اند، می‌تواند با قالب دادهٔ باینری [CBOR](https://www.rfc-editor.org/rfc/rfc8949) کدگذاری شود. {{< glossary_tooltip text="لایهٔ تجمیع" term_id="aggregation-layer" >}} نیز از CBOR پشتیبانی می‌کند، به شرطی که این قابلیت در هر یک از سرورهای API تجمیع‌شده فعال باشد.

وقتی بدنهٔ درخواست شامل یک [آیتم دادهٔ کدگذاری‌شده](https://www.rfc-editor.org/rfc/rfc8949.html#section-1.2-4.2) واحد با CBOR است، کلاینت‌ها باید نوع رسانهٔ IANA یعنی `application/cbor` را در سرآیند `Content-Type` درخواست HTTP مشخص کنند؛ و هنگامی که آماده‌اند در پاسخ یک آیتم دادهٔ کدگذاری‌شده با CBOR دریافت کنند، باید آن را در سرآیند `Accept` درخواست HTTP مشخص کنند. هرگاه بدنهٔ پاسخ شامل آبجکتی کدگذاری‌شده با CBOR باشد، سرورهای API در سرآیند `Content-Type` پاسخ HTTP از `application/cbor` استفاده می‌کنند.

اگر یک سرور API پاسخ خود به یک [درخواست watch](#efficient-detection-of-changes) را با CBOR کدگذاری کند، بدنهٔ پاسخ یک [دنبالهٔ CBOR](https://www.rfc-editor.org/rfc/rfc8742) خواهد بود و سرآیند `Content-Type` پاسخ HTTP از نوع رسانهٔ IANA یعنی `application/cbor-seq` استفاده می‌کند. هر ورودی این دنباله (در صورت وجود) یک رویداد watch واحد است که با CBOR کدگذاری شده است.

افزون بر نوع رسانهٔ موجود `application/apply-patch+yaml` برای [پیکربندی‌های اعمال سمت سرور (server-side apply)](#patch-and-apply) که با YAML کدگذاری شده‌اند، سرورهای APIای که CBOR را فعال کرده‌اند نوع رسانهٔ `application/apply-patch+cbor` را برای پیکربندی‌های اعمال سمت سرورِ کدگذاری‌شده با CBOR می‌پذیرند. برای `application/json-patch+json`، `application/merge-patch+json` یا `application/strategic-merge-patch+json` هیچ معادل CBOR پشتیبانی‌شده‌ای وجود ندارد.

همچنین می‌توانید بازنمایی‌های [جدولی](#table-fetches) و [فقط فراداده](#metadata-only-fetches) را با این کدگذاری درخواست کنید.

## تشخیص کارآمد تغییرات

در API کوبرنتیز، کلاینت‌ها می‌توانند ابتدا یک درخواست اولیه برای یک آبجکت یا یک مجموعه (collection) ارسال کنند و سپس تغییراتی را که پس از آن درخواست رخ داده است دنبال کنند. به این سازوکار **watch** گفته می‌شود. کلاینت‌ها می‌توانند یک درخواست **list** یا **get** بفرستند و پس از آن یک درخواست **watch** ارسال کنند.

برای اینکه ردیابی تغییرات ممکن شود، هر آبجکت کوبرنتیز یک فیلد `resourceVersion` دارد. این فیلد نسخهٔ آن منبع را، همان‌طور که در لایهٔ ماندگاری (persistence layer) زیرین ذخیره شده است، نشان می‌دهد. هنگام بازیابی مجموعه‌ای از منابع (چه در محدودهٔ فضای نام (namespace) و چه در محدودهٔ کلاستر)، پاسخ سرور API یک مقدار `resourceVersion` دارد. کلاینت می‌تواند با همین `resourceVersion` یک **watch** را روی سرور API آغاز کند.

وقتی یک درخواست **watch** ارسال می‌کنید، سرور API با جریانی (stream) از تغییرات پاسخ می‌دهد. این تغییرات نتیجهٔ عملیاتی (مانند **create**، **delete** و **update**) را فهرست می‌کنند که پس از `resourceVersion` تعیین‌شده در پارامتر درخواست **watch** رخ داده‌اند. سازوکار **watch** در مجموع به کلاینت امکان می‌دهد وضعیت فعلی را دریافت کند و سپس، بدون از دست دادن هیچ رویدادی، تغییرات بعدی را دنبال کند.

اگر اتصال **watch** یک کلاینت قطع شود، کلاینت می‌تواند یک **watch** جدید را از آخرین `resourceVersion` بازگردانده‌شده آغاز کند. همچنین می‌تواند یک درخواست **get** / **list** تازه بفرستد و از نو شروع کند. برای جزئیات بیشتر، [معناشناسی نسخهٔ منبع](#resource-versions) را ببینید.

برای مثال:

1. همهٔ پادهای یک فضای نام مشخص را فهرست کنید.

   ```http
   GET /api/v1/namespaces/test/pods
   ---
   200 OK
   Content-Type: application/json

   {
     "kind": "PodList",
     "apiVersion": "v1",
     "metadata": {"resourceVersion":"10245"},
     "items": [...]
   }
   ```

2. از نسخهٔ منبع 10245 به بعد، برای هر عملیات API (مانند **create**، **delete**، **patch** یا **update**) که بر Podهای فضای نام _test_ اثر می‌گذارد، اعلان دریافت کنید. هر اعلان تغییر یک سند JSON است. بدنهٔ پاسخ HTTP (که با نوع `application/json` ارائه می‌شود) از مجموعه‌ای از سندهای JSON تشکیل شده است.

   ```http
   GET /api/v1/namespaces/test/pods?watch=1&resourceVersion=10245
   ---
   200 OK
   Transfer-Encoding: chunked
   Content-Type: application/json

   {
     "type": "ADDED",
     "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "10596", ...}, ...}
   }
   {
     "type": "MODIFIED",
     "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "11020", ...}, ...}
   }
   ...
   ```

هر سرور کوبرنتیز سابقهٔ تغییرات را فقط برای مدت محدودی نگه می‌دارد. کلاسترهایی که از etcd 3 استفاده می‌کنند، به‌طور پیش‌فرض تغییرات ۵ دقیقهٔ اخیر را نگه می‌دارند. اگر عملیات **watch** درخواستی به این دلیل شکست بخورد که نسخهٔ تاریخی آن منبع دیگر در دسترس نیست، کلاینت‌ها باید این وضعیت را مدیریت کنند. یعنی باید کد وضعیت `410 Gone` را تشخیص دهند، کش محلی خود را پاک کنند، یک عملیات **get** یا **list** جدید انجام دهند و **watch** را از `resourceVersion` بازگردانده‌شده آغاز کنند.

کتابخانه‌های کلاینت کوبرنتیز معمولاً برای دنبال کردن مجموعه‌ها، ابزاری استاندارد برای این منطق «ابتدا **list** و سپس **watch**» ارائه می‌کنند. (در کتابخانهٔ کلاینت Go، این ابزار `Reflector` نام دارد و در بستهٔ `k8s.io/client-go/tools/cache` قرار دارد.)

### نشانک‌های watch {#watch-bookmarks}

برای کاهش اثر کوتاه بودن بازهٔ سابقه، API کوبرنتیز یک رویداد watch به نام `BOOKMARK` فراهم می‌کند. این رویداد نوع خاصی از رویداد است و نشان می‌دهد که همهٔ تغییرات تا یک `resourceVersion` مشخصِ درخواستیِ کلاینت پیش‌تر ارسال شده‌اند. سندی که رویداد `BOOKMARK` را نمایش می‌دهد از همان نوعی است که در درخواست خواسته شده است، اما فقط فیلد `.metadata.resourceVersion` را دارد. برای مثال:

```http
GET /api/v1/namespaces/test/pods?watch=1&resourceVersion=10245&allowWatchBookmarks=true
---
200 OK
Transfer-Encoding: chunked
Content-Type: application/json

{
  "type": "ADDED",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "10596", ...}, ...}
}
...
{
  "type": "BOOKMARK",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "12746"} }
}
```

شما به‌عنوان کلاینت می‌توانید با افزودن پارامتر کوئری `allowWatchBookmarks=true` به درخواست **watch**، رویدادهای `BOOKMARK` را درخواست کنید. با این حال، نباید فرض کنید که نشانک‌ها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند. کلاینت‌ها حتی در صورت درخواست نیز نمی‌توانند فرض کنند که سرور API رویداد `BOOKMARK` ارسال خواهد کرد.

## فهرست‌های جریانی

{{< feature-state feature_gate_name="WatchList" >}}

در کلاسترهای بزرگ، بازیابی مجموعهٔ برخی انواع منابع ممکن است مصرف منابع (عمدتاً RAM) را در control plane به‌طور چشمگیری افزایش دهد. کوبرنتیز v1.32 برای کاهش این اثر و ساده‌تر کردن تجربهٔ کاربری الگوی **list** + **watch**، قابلیتی را به مرحلهٔ بتا ارتقا می‌دهد. با این قابلیت می‌توان وضعیت اولیه را (که پیش‌تر با درخواست **list** دریافت می‌شد) به‌عنوان بخشی از درخواست **watch** درخواست کرد.

در سمت کلاینت، می‌توان وضعیت اولیه را با قرار دادن `sendInitialEvents=true` به‌عنوان پارامتر رشتهٔ کوئری در درخواست **watch** درخواست کرد. در این صورت، سرور API جریان watch را با رویدادهای اولیهٔ مصنوعی (از نوع `ADDED`) آغاز می‌کند تا کل وضعیت همهٔ آبجکت‌های موجود ساخته شود. پس از آن، یک [رویداد `BOOKMARK`](/docs/reference/using-api/api-concepts/#watch-bookmarks) ارسال می‌شود (اگر با گزینهٔ `allowWatchBookmarks=true` درخواست شده باشد). رویداد نشانک، نسخهٔ منبعی را که همگام‌سازی تا آن انجام شده است در خود دارد. سرور API پس از ارسال رویداد نشانک، مانند هر درخواست **watch** دیگری به کار خود ادامه می‌دهد.

وقتی `sendInitialEvents=true` را در رشتهٔ کوئری قرار می‌دهید، کوبرنتیز همچنین الزام می‌کند که `resourceVersionMatch` را روی مقدار `NotOlderThan` تنظیم کنید.
اگر `resourceVersion` را بدون مقدار در رشتهٔ کوئری قرار دهید یا اصلاً آن را ارائه نکنید، این کار به‌عنوان درخواست _خواندن سازگار_ (consistent read) تفسیر می‌شود. در این حالت، رویداد نشانک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ یک خواندن سازگار، از زمان آغاز پردازش درخواست، همگام شده باشد. اگر `resourceVersion` را (در رشتهٔ کوئری) مشخص کنید، رویداد نشانک زمانی ارسال می‌شود که وضعیت دست‌کم تا نسخهٔ منبع ارائه‌شده همگام شده باشد.

### مثال {#example-streaming-lists}

فرض کنید می‌خواهید مجموعه‌ای از Podها را watch کنید. نسخهٔ منبع فعلی این مجموعه 10245 است و دو پاد به نام‌های `foo` و `bar` در آن وجود دارد. در این صورت، ارسال درخواست زیر (که با تعیین نسخهٔ منبع خالی از طریق `resourceVersion=`، به‌صراحت _خواندن سازگار_ را درخواست می‌کند) ممکن است به دنبالهٔ رویدادهای زیر منجر شود:

```http
GET /api/v1/namespaces/test/pods?watch=1&sendInitialEvents=true&allowWatchBookmarks=true&resourceVersion=&resourceVersionMatch=NotOlderThan
---
200 OK
Transfer-Encoding: chunked
Content-Type: application/json

{
  "type": "ADDED",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "8467", "name": "foo"}, ...}
}
{
  "type": "ADDED",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "5726", "name": "bar"}, ...}
}
{
  "type": "BOOKMARK",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "10245"} }
}
...
<followed by regular watch stream starting from resourceVersion="10245">
```

## فهرست و watch بخش‌بندی‌شده {#sharded-list-and-watch}

{{< feature-state feature_gate_name="ShardedListAndWatch" >}}

در کلاسترهای بزرگ، کنترل‌کننده‌هایی که انواع منابع پرتعداد (مانند Podها یا Endpointها) را watch می‌کنند، ممکن است برای دریافت و واسریال‌سازی (deserialize) کل جریان رویدادها، پهنای باند شبکه و CPU قابل‌توجهی مصرف کنند؛ حتی اگر فقط به زیرمجموعه‌ای از آبجکت‌ها نیاز داشته باشند. فهرست و watch بخش‌بندی‌شده (sharded) به کنترل‌کننده‌هایی که به‌صورت افقی مقیاس‌دهی شده‌اند امکان می‌دهد بار کاری را میان خود تقسیم کنند تا هر رپلیکا فقط رویدادهای مربوط به سهم خود را دریافت کند.

کوبرنتیز {{< skew currentVersion >}} قابلیتی آلفا معرفی می‌کند که به کلاینت‌ها امکان می‌دهد با بخش‌بندی مبتنی بر هش روی فیلدهای metadata، یک **بخش (shard) فیلترشده** از آبجکت‌ها را از سرور API درخواست کنند. برای استفاده از این قابلیت، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ShardedListAndWatch` را روی سرور API فعال کنید. در صورت فعال بودن این قابلیت، سرور API هم پاسخ‌های list و هم جریان‌های رویداد watch را در سمت سرور فیلتر می‌کند. در نتیجه، فقط آبجکت‌ها و رویدادهایی تحویل داده می‌شوند که مقدار هش‌شدهٔ metadata آن‌ها در بازهٔ درخواستی قرار دارد.

### فیلد shardSelector

فیلد `ShardSelector` در
[`ListOptions`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#listoptions-v1-meta)
یک عبارت مبتنی بر CEL را می‌پذیرد که از تابع `shardRange()` استفاده می‌کند:

```
shardRange(<field-path>, '<hex-start>', '<hex-end>')
```

در این عبارت:

- پارامتر **`<field-path>`** فیلدی از metadata است که هش می‌شود و با نحو CEL و با ریشهٔ object نوشته می‌شود.
  مسیرهایی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از:
  - `object.metadata.uid`
  - `object.metadata.namespace`
- پارامتر **`<hex-start>`** کران پایین بازهٔ هش است و خودش نیز در بازه قرار می‌گیرد. این مقدار به‌صورت رشته‌ای هگزادسیمال ۱۶ رقمی با حروف کوچک و پیشوند `0x` نوشته می‌شود (برای مثال `'0x0000000000000000'`).
- پارامتر **`<hex-end>`** کران بالای بازه است و خودش در بازه قرار نمی‌گیرد. این مقدار به‌صورت رشته‌ای هگزادسیمال با پیشوند `0x` نوشته می‌شود و بیشینهٔ آن `'0x10000000000000000'` (2^64) است.

سرور API یک هش قطعی ۶۴ بیتی از نوع
[FNV-1a](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
از مقدار فیلد مشخص‌شده محاسبه می‌کند و فقط آبجکت‌هایی را بازمی‌گرداند که هش آن‌ها در بازهٔ `[start, end)` قرار دارد. این تابع هش برای ورودی یکسان در همهٔ نمونه‌های سرور API نتیجهٔ یکسانی تولید می‌کند؛ بنابراین استفاده از درخواست‌های بخش‌بندی‌شده با چند رپلیکای سرور API ایمن است.

می‌توانید چند بازه را با `||` (عملگر OR منطقی) ترکیب کنید تا بخش‌های ناپیوستهٔ فضای هش را پوشش دهید. همهٔ بازه‌های یک عبارت باید از مسیر فیلد یکسانی استفاده کنند.

### استفاده از فهرست و watch بخش‌بندی‌شده در کنترل‌کننده‌ها {#sharded-list-and-watch-controllers}

کنترل‌کننده‌ها معمولاً برای list و watch کردن منابع از [informerها](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) استفاده می‌کنند. برای تقسیم بار کاری میان رپلیکاها، هر رپلیکا فیلد `ShardSelector` را در `ListOptions`ای که informerهایش استفاده می‌کنند قرار می‌دهد.

روش استاندارد برای این کار، استفاده از `WithTweakListOptions` هنگام ساختن یک کارخانهٔ informer مشترک (shared informer factory) است. تابع tweak پیش از هر فراخوانی list و watch که informer انجام می‌دهد اجرا می‌شود؛ به همین دلیل انتخابگر (selector) بخش همواره به‌طور یکسان اعمال می‌شود:

```go
import (
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/informers"
)

// shardSelector is determined by the replica's identity (e.g. from a
// StatefulSet ordinal or lease-based assignment). Each replica claims a
// non-overlapping range of the hash space.
shardSelector := "shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"

factory := informers.NewSharedInformerFactoryWithOptions(client, resyncPeriod,
    informers.WithTweakListOptions(func(opts *metav1.ListOptions) {
        opts.ShardSelector = shardSelector
    }),
)
```

با این پیکربندی، هر informer ساخته‌شده از این کارخانه فقط آبجکت‌هایی را list و watch می‌کند که UID هش‌شدهٔ آن‌ها در بازهٔ تخصیص‌یافته قرار دارد. هر رپلیکا زیرمجموعه‌ای از کل مجموعه را دریافت می‌کند که با زیرمجموعهٔ دیگر رپلیکاها هم‌پوشانی ندارد. در نتیجه، ترافیک شبکه و مصرف حافظهٔ هر رپلیکا کاهش می‌یابد.

برای یک استقرار دورپلیکایی، انتخابگرها به این صورت خواهند بود:

```go
// Replica 0: lower half of the hash space
"shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"

// Replica 1: upper half of the hash space
"shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')"
```

یک رپلیکا به‌تنهایی نیز می‌تواند با استفاده از `||` چند بازهٔ ناپیوسته را پوشش دهد:

```go
"shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000') || " +
    "shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')"
```

### اطلاعات بخش در پاسخ‌ها

وقتی سرور API یک `ShardSelector` را اعمال می‌کند، پاسخ list در `metadata` خود یک فیلد `shardInfo` دارد. این فیلد همان انتخابگر را بازمی‌گرداند تا کلاینت‌ها بتوانند بررسی کنند کدام بخش را دریافت کرده‌اند. انتخابگر بخش برای جریان‌های watch نیز به همین شکل اعمال می‌شود: سرور API فقط رویدادهای آبجکت‌هایی را ارسال می‌کند که هش آن‌ها در بازهٔ درخواستی قرار دارد.

```json
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {
    "resourceVersion": "10245",
    "shardInfo": {
      "selector": "shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"
    }
  },
  "items": [...]
}
```

{{< note >}}
پاسخ listای که فیلد `shardInfo` دارد، زیرمجموعه‌ای فیلترشده از کل مجموعه است. کلاینت‌ها نباید پاسخ‌های list بخش‌بندی‌شده را نمایش کاملی از آن نوع منبع در نظر بگیرند.
{{< /note >}}

### تشخیص پشتیبانی سرور

اگر سرور API از فهرست و watch بخش‌بندی‌شده پشتیبانی نکند (چون feature gate فعال نیست یا نسخهٔ سرور قدیمی‌تر است)، فیلد `ShardSelector` نادیده گرفته می‌شود و سرور کل نتایج را بدون فیلتر بازمی‌گرداند. کلاینت‌ها می‌توانند این وضعیت را با بررسی وجود `shardInfo` در metadata پاسخ list تشخیص دهند. اگر `shardInfo` وجود نداشته باشد، یعنی سرور انتخابگر بخش را اعمال نکرده و کلاینت کل مجموعه را بدون فیلتر دریافت کرده است. در این حالت، کلاینت باید برای مدیریت کل نتایج آماده باشد؛ برای مثال، با فیلتر کردن در سمت کلاینت، آبجکت‌هایی را که خارج از بازهٔ بخش تخصیص‌یافته به آن هستند کنار بگذارد.

## فشرده‌سازی پاسخ

{{< feature-state feature_gate_name="APIResponseCompression" >}}

گزینهٔ `APIResponseCompression` به سرور API امکان می‌دهد پاسخ‌های درخواست‌های **get** و **list** را فشرده کند. این کار پهنای باند شبکه را کاهش می‌دهد و کارایی کلاسترهای بزرگ را بهبود می‌بخشد. این گزینه از کوبرنتیز 1.16 به‌طور پیش‌فرض فعال است و می‌توان آن را با افزودن `APIResponseCompression=false` به فلگ `--feature-gates` در سرور API غیرفعال کرد.

فشرده‌سازی پاسخ API می‌تواند اندازهٔ پاسخ را به‌طور چشمگیری کاهش دهد، به‌ویژه برای منابع بزرگ یا [مجموعه‌ها](/docs/reference/using-api/api-concepts/#collections).
برای مثال، یک درخواست **list** برای پادها، بسته به تعداد پادها و ویژگی‌هایشان، می‌تواند صدها کیلوبایت یا حتی چند مگابایت داده بازگرداند. با فشرده‌سازی پاسخ، می‌توان در پهنای باند شبکه صرفه‌جویی کرد و تأخیر را کاهش داد.

برای بررسی کارکرد `APIResponseCompression`، می‌توانید یک درخواست **get** یا **list** همراه با سرآیند `Accept-Encoding` به سرور API بفرستید و اندازه و سرآیندهای پاسخ را بررسی کنید. برای مثال:

```http
GET /api/v1/pods
Accept-Encoding: gzip
---
200 OK
Content-Type: application/json
content-encoding: gzip
...
```

سرآیند `content-encoding` نشان می‌دهد که پاسخ با `gzip` فشرده شده است.

## بازیابی مجموعه‌نتایج بزرگ در قالب تکه‌ها

{{< feature-state feature_gate_name="APIListChunking" >}}

در کلاسترهای بزرگ، بازیابی مجموعهٔ برخی انواع منابع ممکن است به پاسخ‌های بسیار بزرگی منجر شود که بر سرور و کلاینت اثر می‌گذارند. برای نمونه، یک کلاستر ممکن است ده‌ها هزار Pod داشته باشد که هر کدام تقریباً معادل 2 KiB داده JSON کدگذاری‌شده است. بازیابی همهٔ پادها در همهٔ فضاهای نام ممکن است پاسخی بسیار بزرگ (10 تا 20 مگابایت) ایجاد کند و مقدار زیادی از منابع سرور را مصرف کند.

سرور API کوبرنتیز می‌تواند یک درخواست بزرگ برای یک مجموعه را به تکه‌های کوچک‌تر متعددی تقسیم کند و در عین حال سازگاری کل درخواست را حفظ کند. هر تکه را می‌توان به‌ترتیب بازگرداند. این کار هم اندازهٔ کل درخواست را کاهش می‌دهد و هم به کلاینت‌هایی که با کاربر سروکار دارند امکان می‌دهد نتایج را به‌تدریج نمایش دهند تا پاسخ‌گویی بهتر شود.

می‌توانید از سرور API بخواهید پاسخ یک **list** را به‌صورت صفحه‌بندی‌شده (که کوبرنتیز هر صفحه را یک _تکه_ (chunk) می‌نامد) ارائه کند. برای بازیابی یک مجموعه در قالب تکه‌ها، درخواست‌های مربوط به مجموعه‌ها از دو پارامتر کوئری `limit` و `continue` پشتیبانی می‌کنند. همچنین همهٔ عملیات **list** یک فیلد پاسخ به نام `continue` را در فیلد `metadata` مجموعه بازمی‌گردانند. کلاینت باید با `limit` بیشینهٔ تعداد نتایجی را که می‌خواهد در هر تکه دریافت کند مشخص کند. سرور حداکثر به تعداد `limit` منبع در نتیجه بازمی‌گرداند و اگر منابع بیشتری در مجموعه باقی مانده باشد، یک مقدار `continue` نیز در پاسخ قرار می‌دهد.

سپس شما به‌عنوان کلاینت API می‌توانید این مقدار `continue` را در درخواست بعدی به سرور API بفرستید تا سرور صفحهٔ (_تکهٔ_) بعدی نتایج را بازگرداند. اگر این کار را تا زمانی که سرور مقدار `continue` خالی بازگرداند ادامه دهید، کل مجموعه را بازیابی خواهید کرد.

توکن `continue` نیز مانند عملیات **watch** پس از مدت کوتاهی (به‌طور پیش‌فرض ۵ دقیقه) منقضی می‌شود و اگر بازگرداندن نتایج بیشتر ممکن نباشد، پاسخ `410 Gone` بازگردانده می‌شود. در این حالت، کلاینت باید از ابتدا شروع کند یا پارامتر `limit` را حذف کند.

برای مثال، اگر ۱٬۲۵۳ پاد در کلاستر وجود داشته باشد و بخواهید آن‌ها را در تکه‌های ۵۰۰تایی دریافت کنید، این تکه‌ها را به این صورت درخواست کنید:

1. همهٔ پادهای کلاستر را فهرست کنید و هر بار حداکثر ۵۰۰ پاد را بازیابی کنید.

   ```http
   GET /api/v1/pods?limit=500
   ---
   200 OK
   Content-Type: application/json

   {
     "kind": "PodList",
     "apiVersion": "v1",
     "metadata": {
       "resourceVersion":"10245",
       "continue": "ENCODED_CONTINUE_TOKEN",
       "remainingItemCount": 753,
       ...
     },
     "items": [...] // returns pods 1-500
   }
   ```

1. فراخوانی قبلی را ادامه دهید و ۵۰۰ پاد بعدی را بازیابی کنید.

   ```http
   GET /api/v1/pods?limit=500&continue=ENCODED_CONTINUE_TOKEN
   ---
   200 OK
   Content-Type: application/json

   {
     "kind": "PodList",
     "apiVersion": "v1",
     "metadata": {
       "resourceVersion":"10245",
       "continue": "ENCODED_CONTINUE_TOKEN_2",
       "remainingItemCount": 253,
       ...
     },
     "items": [...] // returns pods 501-1000
   }
   ```

1. فراخوانی قبلی را ادامه دهید و ۲۵۳ پاد باقی‌مانده را بازیابی کنید.

   ```http
   GET /api/v1/pods?limit=500&continue=ENCODED_CONTINUE_TOKEN_2
   ---
   200 OK
   Content-Type: application/json

   {
     "kind": "PodList",
     "apiVersion": "v1",
     "metadata": {
       "resourceVersion":"10245",
       "continue": "", // continue token is empty because we have reached the end of the list
       ...
     },
     "items": [...] // returns pods 1001-1253
   }
   ```

توجه کنید که `resourceVersion` مجموعه در همهٔ درخواست‌ها ثابت می‌ماند. این یعنی سرور یک تصویر لحظه‌ای (snapshot) سازگار از پادها را به شما نشان می‌دهد. پادهایی که پس از نسخهٔ `10245` ایجاد، به‌روزرسانی یا حذف شوند نمایش داده نمی‌شوند، مگر اینکه یک درخواست **list** جداگانه بدون توکن `continue` ارسال کنید. به این ترتیب می‌توانید درخواست‌های بزرگ را به تکه‌های کوچک‌تر تقسیم کنید و سپس، بدون از دست دادن هیچ به‌روزرسانی، یک عملیات **watch** روی کل مجموعه انجام دهید.

فیلد `remainingItemCount` تعداد آیتم‌های بعدی مجموعه را نشان می‌دهد که در این پاسخ گنجانده نشده‌اند. اگر درخواست **list** شامل
{{< glossary_tooltip text="انتخابگرهای" term_id="selector">}} برچسب یا فیلد باشد، تعداد آیتم‌های باقی‌مانده مشخص نیست و سرور API فیلد `remainingItemCount` را در پاسخ خود قرار نمی‌دهد.
اگر **list** کامل باشد (چه به این دلیل که تکه‌بندی انجام نمی‌شود و چه به این دلیل که این آخرین تکه است)، آیتمی باقی نمانده است و سرور API فیلد `remainingItemCount` را در پاسخ خود قرار نمی‌دهد. هدف از `remainingItemCount` تخمین اندازهٔ یک مجموعه است.

## مجموعه‌ها

در اصطلاحات کوبرنتیز، پاسخی که از یک عملیات **list** دریافت می‌کنید یک _مجموعه_ (collection) است. با این حال، کوبرنتیز برای مجموعه‌های هر نوع منبع، kindهای مشخصی تعریف می‌کند. نام kind هر مجموعه از نام kind منبع به‌همراه پسوند `List` تشکیل می‌شود.

هنگامی که API را برای نوع خاصی پرس‌وجو می‌کنید، همهٔ آیتم‌هایی که آن پرس‌وجو برمی‌گرداند از همان نوع هستند. برای مثال، وقتی Serviceها را **list** می‌کنید، مقدار `kind` در پاسخِ مجموعه برابر با
[`ServiceList`](/docs/reference/kubernetes-api/service-resources/service-v1/#ServiceList)
است و هر آیتم در آن مجموعه نمایانگر یک Service است. برای مثال:

```http
GET /api/v1/services
```

```yaml
{
  "kind": "ServiceList",
  "apiVersion": "v1",
  "metadata": {
    "resourceVersion": "2947301"
  },
  "items": [
    {
      "metadata": {
        "name": "kubernetes",
        "namespace": "default",
...
      "metadata": {
        "name": "kube-dns",
        "namespace": "kube-system",
...
```

ده‌ها نوع مجموعه (مانند `PodList`، `ServiceList` و `NodeList`) در API کوبرنتیز تعریف شده است. اطلاعات بیشتر دربارهٔ هر نوع مجموعه را می‌توانید در مستندات [API کوبرنتیز](/docs/reference/kubernetes-api/) بیابید.

برخی ابزارها، مانند `kubectl`، سازوکار مجموعه‌های کوبرنتیز را کمی متفاوت از خود API کوبرنتیز نمایش می‌دهند. از آنجا که خروجی `kubectl` ممکن است شامل پاسخ چندین عملیات **list** در سطح API باشد، `kubectl` فهرست آیتم‌ها را با `kind: List` نمایش می‌دهد. برای مثال:

```shell
kubectl get services -A -o yaml
```
```yaml
apiVersion: v1
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
items:
- apiVersion: v1
  kind: Service
  metadata:
    creationTimestamp: "2021-06-03T14:54:12Z"
    labels:
      component: apiserver
      provider: kubernetes
    name: kubernetes
    namespace: default
...
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      prometheus.io/port: "9153"
      prometheus.io/scrape: "true"
    creationTimestamp: "2021-06-03T14:54:14Z"
    labels:
      k8s-app: kube-dns
      kubernetes.io/cluster-service: "true"
      kubernetes.io/name: CoreDNS
    name: kube-dns
    namespace: kube-system
```

{{< note >}}
به خاطر داشته باشید که API کوبرنتیز هیچ `kind`ی با نام `List` ندارد.

مقدار `kind: List` جزئیاتی از پیاده‌سازی داخلی در سمت کلاینت است که برای پردازش مجموعه‌هایی به کار می‌رود که ممکن است آبجکت‌هایی از انواع مختلف را در بر داشته باشند. در خودکارسازی‌ها یا سایر کدها به `kind: List` وابسته نشوید.
{{< /note >}}

## دریافت به‌صورت جدول

هنگامی که `kubectl get` را اجرا می‌کنید، قالب پیش‌فرض خروجی، نمایشی ساده و جدولی از یک یا چند نمونه از یک نوع منبع خاص است. در گذشته، کلاینت‌ها برای فهرست‌کردن سادهٔ آبجکت‌ها ناچار بودند خروجی جدولی و خروجی describe پیاده‌سازی‌شده در `kubectl` را بازتولید کنند. از جمله محدودیت‌های این رویکرد، منطق پیچیده‌ای بود که هنگام کار با برخی آبجکت‌ها لازم می‌شد. افزون بر این، انواعی که از طریق تجمیع API (API aggregation) یا منابع شخص ثالث ارائه می‌شوند، در زمان کامپایل شناخته‌شده نیستند. به همین دلیل، برای انواعی که کلاینت آن‌ها را نمی‌شناخت، باید پیاده‌سازی‌های عمومی وجود می‌داشت.

برای پرهیز از محدودیت‌های احتمالی که در بالا شرح داده شد، کلاینت‌ها می‌توانند نمایش Table آبجکت‌ها را درخواست کنند و جزئیات مربوط به چاپ را به سرور واگذار کنند. API کوبرنتیز مذاکرهٔ استاندارد نوع محتوا (content type negotiation) در HTTP را پیاده‌سازی می‌کند: اگر در یک فراخوانی `GET` سرآیند `Accept` را با مقدار `application/json;as=Table;g=meta.k8s.io;v=v1` ارسال کنید، از سرور درخواست می‌شود که آبجکت‌ها را با نوع محتوای Table برگرداند.

برای مثال، همهٔ پادهای یک کلاستر را در قالب Table فهرست کنید.

```http
GET /api/v1/pods
Accept: application/json;as=Table;g=meta.k8s.io;v=v1
---
200 OK
Content-Type: application/json

{
    "kind": "Table",
    "apiVersion": "meta.k8s.io/v1",
    ...
    "columnDefinitions": [
        ...
    ]
}
```

برای آن دسته از انواع منابع API که control plane هیچ تعریف Table سفارشی‌ای برایشان نمی‌شناسد، سرور API یک پاسخ Table پیش‌فرض برمی‌گرداند که از فیلدهای `name` و `creationTimestamp` منبع تشکیل شده است.

```http
GET /apis/crd.example.com/v1alpha1/namespaces/default/resources
---
200 OK
Content-Type: application/json
...

{
    "kind": "Table",
    "apiVersion": "meta.k8s.io/v1",
    ...
    "columnDefinitions": [
        {
            "name": "Name",
            "type": "string",
            ...
        },
        {
            "name": "Created At",
            "type": "date",
            ...
        }
    ]
}
```

همهٔ انواع منابع API از پاسخ Table پشتیبانی نمی‌کنند؛ برای مثال، ممکن است
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitionها" >}}
نگاشت فیلد به جدول را تعریف نکنند، و یک APIService که
[API هستهٔ کوبرنتیز را گسترش می‌دهد](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
ممکن است اصلاً پاسخ Table ارائه ندهد. اگر کلاینتی پیاده‌سازی می‌کنید که از اطلاعات Table استفاده می‌کند و باید با همهٔ انواع منابع، از جمله افزونه‌ها، کار کند، باید درخواست‌هایی ارسال کنید که چند نوع محتوا را در سرآیند `Accept` مشخص می‌کنند. برای مثال:

```
Accept: application/json;as=Table;g=meta.k8s.io;v=v1, application/json
```

اگر کلاینت اعلام کند که فقط `...;as=Table;g=meta.k8s.io;v=v1` را می‌پذیرد، سرورهایی که از پاسخ‌های جدولی پشتیبانی نمی‌کنند کد خطای 406 برمی‌گردانند.

اگر در چنین حالتی بازگشت به آبجکت‌های کامل مطلوب باشد، کلاینت‌ها می‌توانند `,application/json` (یا هر کدگذاری پشتیبانی‌شدهٔ دیگری) را به سرآیند Accept خود اضافه کنند و در پاسخ، هم جدول و هم آبجکت‌های کامل را مدیریت کنند:

```http
Accept: application/json;as=Table;g=meta.k8s.io;v=v1,application/json`
```

برای اطلاعات بیشتر دربارهٔ مذاکرهٔ نوع محتوا، به
[MDN Content Negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) مراجعه کنید.

## دریافت فقط فراداده

برای درخواست بخشی از فرادادهٔ آبجکت، می‌توانید در سرآیند `Accept` پاسخ‌هایی را درخواست کنید که فقط فراداده دارند. API کوبرنتیز گونه‌ای از مذاکرهٔ نوع محتوا در HTTP را پیاده‌سازی می‌کند. شما به‌عنوان کلاینت می‌توانید سرآیند `Accept` را با نوع رسانهٔ موردنظر، به‌همراه پارامترهایی که نشان می‌دهند فقط فراداده را می‌خواهید، ارسال کنید. برای مثال، `Accept: application/json;as=PartialObjectMetadata;g=meta.k8s.io;v=v1` برای دریافت JSON یک آبجکت مشخص و
`Accept: application/json;as=PartialObjectMetadataList;g=meta.k8s.io;v=v1` برای یک فهرست.

{{< note >}}
مقدار `as=PartialObjectMetadata` باید در درخواست‌های مربوط به یک منبع مشخص و مقدار `as=PartialObjectMetadataList` باید برای فهرست‌ها استفاده شود.
{{< /note >}}

برای مثال، برای فهرست‌کردن همهٔ پادهای یک کلاستر در تمام فضاهای نام، به‌گونه‌ای که فقط فرادادهٔ هر پاد برگردانده شود:

```http
GET /api/v1/pods
Accept: application/json;as=PartialObjectMetadataList;g=meta.k8s.io;v=v1
---
200 OK
Content-Type: application/json

{
    "kind": "PartialObjectMetadataList",
    "apiVersion": "meta.k8s.io/v1",
    "metadata": {
        "resourceVersion": "...",
    },
    "items": [
        {
            "apiVersion": "meta.k8s.io/v1",
            "kind": "PartialObjectMetadata",
            "metadata": {
                "name": "pod-1",
                ...
            }
        },
        {
            "apiVersion": "meta.k8s.io/v1",
            "kind": "PartialObjectMetadata",
            "metadata": {
                "name": "pod-2",
                ...
            }
        }
    ]
}
```

در پاسخ به درخواستِ یک مجموعه، سرور API یک PartialObjectMetadataList برمی‌گرداند. در پاسخ به درخواستِ یک آبجکت منفرد، سرور API نمایش PartialObjectMetadata آن آبجکت را برمی‌گرداند. در هر دو حالت، آبجکت‌های برگردانده‌شده فقط فیلد `metadata` را دارند و فیلدهای `spec` و `status` حذف می‌شوند.

این قابلیت برای کلاینت‌هایی مفید است که فقط باید وجود یک آبجکت را بررسی کنند یا فقط به خواندن فرادادهٔ آن نیاز دارند. این قابلیت می‌تواند اندازهٔ پاسخ سرور API را به‌طور چشمگیری کاهش دهد.

دریافت فقط‌فراداده را می‌توانید برای همهٔ انواع رسانهٔ موجود (JSON، YAML، CBOR و Kubernetes Protobuf) درخواست کنید. برای Protobuf، مقدار سرآیند `Accept` به این صورت خواهد بود:
`application/vnd.kubernetes.protobuf;as=PartialObjectMetadata;g=meta.k8s.io;v=v1`.

سرور API کوبرنتیز تقریباً برای همهٔ APIهای داخلی خود از دریافت جزئی پشتیبانی می‌کند. با این حال، می‌توانید از کوبرنتیز برای دسترسی به سرورهای API دیگر از طریق
{{< glossary_tooltip text="لایهٔ تجمیع" term_id="aggregation-layer" >}} استفاده کنید و ممکن است آن APIها از دریافت جزئی پشتیبانی نکنند.

اگر کلاینتی با سرآیند `Accept` **فقط** پاسخ `...;as=PartialObjectMetadata;g=meta.k8s.io;v=v1` را درخواست کند و به APIای دسترسی پیدا کند که از پاسخ‌های جزئی پشتیبانی نمی‌کند، کوبرنتیز با خطای HTTP 406 پاسخ می‌دهد.


اگر در چنین حالتی بازگشت به آبجکت‌های کامل مطلوب باشد، کلاینت‌ها می‌توانند `,application/json` (یا هر کدگذاری پشتیبانی‌شدهٔ دیگری) را به سرآیند Accept خود اضافه کنند و در پاسخ، هم PartialObjectMetadata و هم آبجکت‌های کامل را مدیریت کنند. بهتر است با استفاده از پارامتر `q` (_کیفیت_) مشخص کنید که پاسخ جزئی ترجیح داده می‌شود. برای مثال:

```http
Accept: application/json;as=PartialObjectMetadata;g=meta.k8s.io;v=v1, application/json;q=0.9
```

برای اطلاعات بیشتر دربارهٔ مذاکرهٔ نوع محتوا، به
[MDN Content Negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) مراجعه کنید.

## حذف منبع

هنگامی که منبعی را **delete** می‌کنید، این کار در دو مرحله انجام می‌شود.

1. _نهایی‌سازی_ (finalization)
1. برداشتن (removal)

```yaml
{
  "kind": "ConfigMap",
  "apiVersion": "v1",
  "metadata": {
    "finalizers": ["url.io/neat-finalization", "other-url.io/my-finalizer"],
    "deletionTimestamp": nil,
  }
}
```

هنگامی که یک کلاینت برای نخستین بار درخواست **delete** را برای حذف یک منبع ارسال می‌کند، مقدار `.metadata.deletionTimestamp` برابر با زمان کنونی تنظیم می‌شود. پس از تنظیم `.metadata.deletionTimestamp`، کنترل‌کننده‌های خارجی که روی finalizerها عمل می‌کنند ممکن است در هر زمان و با هر ترتیبی کار پاک‌سازی خود را آغاز کنند.

میان finalizerها هیچ ترتیبی اعمال **نمی‌شود**، زیرا این کار خطر جدیِ گیرکردن `.metadata.finalizers` را به همراه دارد.

فیلد `.metadata.finalizers` مشترک است: هر عاملی که مجوز لازم را داشته باشد می‌تواند ترتیب آن را تغییر دهد. اگر فهرست finalizerها به‌ترتیب پردازش می‌شد، ممکن بود وضعیتی پیش آید که در آن، مؤلفهٔ مسئولِ نخستین finalizer فهرست منتظر سیگنالی (مقدار یک فیلد، یک سامانهٔ خارجی یا چیزی دیگر) بماند که مؤلفهٔ مسئولِ یکی از finalizerهای بعدی فهرست تولید می‌کند و در نتیجه بن‌بست (deadlock) رخ دهد.

بدون اعمال ترتیب، finalizerها آزادند ترتیب خود را میان خودشان تعیین کنند و در برابر تغییر ترتیب در فهرست آسیب‌پذیر نیستند.

پس از حذف آخرین finalizer، منبع واقعاً از etcd حذف می‌شود.

### حذف اجباری

{{< feature-state feature_gate_name="AllowUnsafeMalformedObjectDeletion" >}}

{{< caution >}}
اگر بار کاری مرتبط با منبعی که به‌اجبار حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است آن بار کاری را از کار بیندازد؛ بنابراین ممکن است پیامدهایی در حد از کار افتادن کلاستر به دنبال داشته باشد.
{{< /caution >}}

با فعال‌کردن گزینهٔ حذف `ignoreStoreReadErrorWithClusterBreakingPotential`، کاربر می‌تواند عملیات **delete** اجباری و ناامن را روی منبعی رمزگشایی‌ناپذیر یا خراب انجام دهد. این گزینه زمانی در دسترس است که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `AllowUnsafeMalformedObjectDeletion` فعال باشد؛ این feature gate از کوبرنتیز v1.37 به‌طور پیش‌فرض فعال است. اپراتور کلاستر می‌تواند با تنظیم گزینهٔ خط فرمان
`--feature-gates=AllowUnsafeMalformedObjectDeletion=false` این رفتار را غیرفعال کند.

{{< note >}}
کاربری که عملیات **delete** اجباری را انجام می‌دهد باید روی منبع موردنظر، مجوز هر دو فعل **delete** و **unsafe-delete-ignore-read-errors** را داشته باشد.
{{< /note >}}

یک منبع زمانی خراب در نظر گرفته می‌شود که به یکی از دلایل زیر نتوان آن را با موفقیت از ذخیره‌سازی بازیابی کرد:

- خطای تبدیل (برای مثال: شکست در رمزگشایی)، یا
- شکست در دیکدکردن (decode) آبجکت.

سرور API ابتدا حذف عادی را امتحان می‌کند و اگر این کار با خطای _منبع خراب_ شکست بخورد، حذف اجباری را آغاز می‌کند. عملیات **delete** اجباری ناامن است، زیرا محدودیت‌های finalizer را نادیده می‌گیرد و بررسی پیش‌شرط‌ها را انجام نمی‌دهد.

مقدار پیش‌فرض این گزینه `false` است تا سازگاری با نسخه‌های پیشین حفظ شود. در درخواست **delete**ی که در آن `ignoreStoreReadErrorWithClusterBreakingPotential` برابر با `true` باشد، فیلدهای `dryRun`، `gracePeriodSeconds`، `orphanDependents`، `preconditions` و `propagationPolicy` باید بدون مقدار باقی بمانند.

{{< note >}}
اگر کاربر درخواست **delete**ی را با مقدار `true` برای `ignoreStoreReadErrorWithClusterBreakingPotential` روی منبعی ارسال کند که در واقع قابل خواندن است، سرور API درخواست را با خطا لغو می‌کند.
{{< /note >}}

## رابط API برای منابع منفرد

فعل‌های **get**، **create**، **update**، **patch**، **delete** و **proxy** در API کوبرنتیز فقط از منابع منفرد پشتیبانی می‌کنند. این فعل‌ها امکان ارسال هم‌زمان چند منبع را در قالب یک فهرست یا تراکنش، چه مرتب و چه نامرتب، فراهم نمی‌کنند.

هنگامی که کلاینت‌ها (از جمله kubectl) روی مجموعه‌ای از منابع عمل می‌کنند، کلاینت مجموعه‌ای از درخواست‌های API تک‌منبعی ارسال می‌کند و سپس در صورت نیاز پاسخ‌ها را تجمیع می‌کند.

در مقابل، فعل‌های **list** و **watch** در API کوبرنتیز امکان دریافت چند منبع را فراهم می‌کنند و فعل **deletecollection** امکان حذف چند منبع را می‌دهد.

## اعتبارسنجی فیلد

کوبرنتیز همیشه نوع فیلدها را اعتبارسنجی می‌کند. برای مثال، اگر فیلدی در API به‌صورت عدد تعریف شده باشد، نمی‌توانید مقدار متنی به آن بدهید. اگر فیلدی به‌صورت آرایه‌ای از رشته‌ها تعریف شده باشد، فقط می‌توانید یک آرایه ارائه دهید. برخی فیلدها را می‌توان حذف کرد و برخی دیگر الزامی هستند. حذف یک فیلد الزامی از درخواست API خطا محسوب می‌شود.

اگر درخواستی با یک فیلد اضافی ارسال کنید، یعنی فیلدی که control plane کلاستر آن را نمی‌شناسد، رفتار سرور API پیچیده‌تر است.

به‌طور پیش‌فرض، سرور API فیلدهایی را که نمی‌شناسد از ورودی دریافتی (برای مثال، بدنهٔ JSON یک درخواست `PUT`) حذف می‌کند.

در دو حالت، سرور API فیلدهایی را که در یک درخواست HTTP ارائه کرده‌اید حذف می‌کند.

این حالت‌ها عبارت‌اند از:

1. فیلد ناشناخته است، زیرا در شِمای OpenAPI منبع وجود ندارد. (یک استثنا در این مورد، آن دسته از {{< glossary_tooltip term_id="CustomResourceDefinition" text="CRDها" >}}
   است که صراحتاً با استفاده از `x-kubernetes-preserve-unknown-fields` تعیین می‌کنند فیلدهای ناشناخته هرس نشوند.)
1. فیلد در آبجکت تکراری است.

### اعتبارسنجی فیلدهای ناشناخته یا تکراری {#setting-the-field-validation-level}

{{< feature-state feature_gate_name="ServerSideFieldValidation" >}}

از نسخهٔ 1.25 به بعد، هنگامی که از فعل‌های HTTPای استفاده می‌کنید که می‌توانند داده ارسال کنند (`POST`، `PUT` و `PATCH`)، فیلدهای ناشناخته یا تکراری در یک آبجکت از طریق اعتبارسنجی در سمت سرور شناسایی می‌شوند. سطوح ممکن اعتبارسنجی عبارت‌اند از `Ignore`، `Warn` (پیش‌فرض) و `Strict`.

`Ignore`
: سرور API درخواست را با موفقیت پردازش می‌کند، درست همان‌طور که اگر فیلدهای نادرست تنظیم نشده بودند پردازش می‌کرد؛ همهٔ فیلدهای ناشناخته و تکراری را حذف می‌کند و هیچ نشانه‌ای از انجام این کار ارائه نمی‌دهد.

`Warn`
: (پیش‌فرض) سرور API درخواست را با موفقیت پردازش می‌کند و یک هشدار به کلاینت گزارش می‌دهد. این هشدار با استفاده از سرآیند پاسخ `Warning:` ارسال می‌شود و به‌ازای هر فیلد ناشناخته یا تکراری یک مورد هشدار به آن اضافه می‌شود. برای اطلاعات بیشتر دربارهٔ هشدارها و API کوبرنتیز، مقالهٔ وبلاگ
  [Warning: Helpful Warnings Ahead](/blog/2020/09/03/warnings/) را ببینید.

`Strict`
: سرور API هنگامی که هر فیلد ناشناخته یا تکراری را تشخیص دهد، درخواست را با خطای 400 Bad Request رد می‌کند. پیام پاسخ سرور API همهٔ فیلدهای ناشناخته یا تکراری‌ای را که تشخیص داده است مشخص می‌کند.

سطح اعتبارسنجی فیلد با پارامتر پرس‌وجوی `fieldValidation` تنظیم می‌شود.

{{< note >}}
اگر درخواستی ارسال کنید که فیلدی ناشناخته را مشخص می‌کند و به دلیل دیگری نیز نامعتبر است (برای مثال، درخواست برای یک فیلد شناخته‌شده که API برای آن عدد صحیح انتظار دارد، مقداری رشته‌ای ارائه می‌دهد)، سرور API با خطای 400 Bad Request پاسخ می‌دهد، اما هیچ اطلاعاتی دربارهٔ فیلدهای ناشناخته یا تکراری ارائه نمی‌کند (و فقط نخستین خطای مهلکی را که با آن مواجه شده است گزارش می‌دهد).

در این حالت، صرف‌نظر از سطح اعتبارسنجی فیلدی که درخواست کرده‌اید، همیشه پاسخ خطا دریافت می‌کنید.
{{< /note >}}

ابزارهایی که به سرور درخواست ارسال می‌کنند (مانند `kubectl`) ممکن است پیش‌فرض‌های خود را تعیین کنند که با سطح اعتبارسنجی `Warn`، یعنی سطح پیش‌فرض سرور API، متفاوت است.

ابزار `kubectl` برای تنظیم سطح اعتبارسنجی فیلد از فلگ `--validate` استفاده می‌کند. این فلگ مقادیر `ignore`، `warn` و `strict` را می‌پذیرد و همچنین مقادیر `true` (معادل `strict`) و `false` (معادل `ignore`) را نیز قبول می‌کند. تنظیم پیش‌فرض اعتبارسنجی در kubectl برابر با `--validate=true` است که به معنای اعتبارسنجی سخت‌گیرانهٔ فیلد در سمت سرور است.

هنگامی که kubectl نتواند به سرور APIای متصل شود که از اعتبارسنجی فیلد پشتیبانی می‌کند (سرورهای API پیش از کوبرنتیز 1.27)، به اعتبارسنجی سمت کلاینت بازمی‌گردد. اعتبارسنجی سمت کلاینت در نسخه‌ای آینده از kubectl به‌طور کامل حذف خواهد شد.

{{< note >}}

پیش از کوبرنتیز 1.25، از `kubectl --validate` به‌عنوان یک فلگ بولی برای روشن یا خاموش‌کردن اعتبارسنجی سمت کلاینت استفاده می‌شد.

{{< /note >}}

از نسخهٔ v1.33 به بعد، کوبرنتیز (از جمله v{{< skew currentVersion>}}) روشی برای تعریف اعتبارسنجی فیلدها با استفاده از _تگ‌های اعلانی_ (declarative tags) ارائه می‌دهد. این قابلیت برای کسانی که در توسعهٔ خود کوبرنتیز مشارکت می‌کنند مفید است و اگر API خود را با کتابخانه‌های کوبرنتیز می‌نویسید نیز به کار شما می‌آید. برای آشنایی بیشتر، [اعتبارسنجی اعلانی API](/docs/reference/using-api/declarative-validation/) را ببینید.

## اجرای آزمایشی (Dry-run)

{{< feature-state feature_gate_name="DryRun" >}}

هنگامی که از فعل‌های HTTPای استفاده می‌کنید که می‌توانند منابع را تغییر دهند (`POST`، `PUT`، `PATCH` و `DELETE`)، می‌توانید درخواست خود را در حالت _اجرای آزمایشی_ ارسال کنید. حالت اجرای آزمایشی کمک می‌کند درخواست، تا پیش از مرحلهٔ ذخیرهٔ آبجکت‌ها در ذخیره‌سازی، از مراحل معمول پردازش درخواست (زنجیرهٔ پذیرش، اعتبارسنجی، تعارض‌های ادغام) عبور کند و ارزیابی شود. بدنهٔ پاسخ این درخواست تا حد امکان به پاسخ یک درخواست عادی (غیرآزمایشی) نزدیک است. کوبرنتیز تضمین می‌کند که درخواست‌های اجرای آزمایشی در ذخیره‌سازی ثبت نمی‌شوند و هیچ اثر جانبی دیگری ندارند.

### ارسال درخواست dry-run

حالت dry-run با تنظیم پارامتر پرس‌وجوی `dryRun` فعال می‌شود. این پارامتر یک رشته است که مانند یک enum عمل می‌کند و تنها مقدارهای پذیرفتنی آن عبارت‌اند از:

[بدون مقدار]
: اثرات جانبی مجاز است. این حالت را با رشتهٔ پرس‌وجویی مانند `?dryRun` یا `?dryRun&pretty=true` درخواست می‌کنید. پاسخ، آبجکت نهایی‌ای است که ذخیره می‌شد، یا اگر درخواست قابل انجام نباشد، یک خطا است.

`All`
: همهٔ مراحل به‌طور عادی اجرا می‌شوند، به‌جز مرحلهٔ نهایی ذخیره‌سازی که در آن از بروز اثرات جانبی جلوگیری می‌شود.

وقتی `?dryRun=All` را تنظیم می‌کنید، همهٔ
{{< glossary_tooltip text="کنترل‌کننده‌های پذیرش" term_id="admission-controller" >}}
مرتبط اجرا می‌شوند، کنترل‌کننده‌های پذیرشِ اعتبارسنج درخواست را پس از تغییر بررسی می‌کنند، در `PATCH` عمل ادغام انجام می‌شود، فیلدها مقدار پیش‌فرض می‌گیرند و اعتبارسنجی schema صورت می‌گیرد. تغییرات در ذخیره‌سازی زیرین ذخیره نمی‌شوند، اما آبجکت نهایی‌ای که ذخیره می‌شد همچنان همراه با کد وضعیت عادی به کاربر بازگردانده می‌شود.

اگر نسخهٔ غیر dry-run یک درخواست، کنترل‌کنندهٔ پذیرشی را فعال کند که اثرات جانبی دارد، درخواست به‌جای پذیرفتن خطر یک اثر جانبی ناخواسته، با شکست مواجه می‌شود. همهٔ افزونه‌های داخلی کنترل پذیرش از dry-run پشتیبانی می‌کنند. افزون بر این، webhookهای پذیرش می‌توانند در
[آبجکت پیکربندی](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#validatingwebhook-v1-admissionregistration-k8s-io)
خود با تنظیم فیلد `sideEffects` روی `None` اعلام کنند که اثر جانبی ندارند.

{{< note >}}
اگر یک webhook واقعاً اثرات جانبی داشته باشد، باید فیلد `sideEffects` را روی "NoneOnDryRun" تنظیم کرد. این تغییر تنها در صورتی مناسب است که webhook نیز طوری اصلاح شود که فیلد `DryRun` را در AdmissionReview درک کند و از بروز اثرات جانبی در هر درخواستی که به‌عنوان dry-run علامت‌گذاری شده است جلوگیری کند.
{{< /note >}}

در اینجا نمونه‌ای از یک درخواست dry-run را می‌بینید که از `?dryRun=All` استفاده می‌کند:

```http
POST /api/v1/namespaces/test/pods?dryRun=All
Content-Type: application/json
Accept: application/json
```

پاسخ مشابه پاسخ درخواست غیر dry-run خواهد بود، اما ممکن است مقدار برخی از فیلدهای تولیدشده متفاوت باشد.

### مقدارهای تولیدشده

برخی از مقدارهای یک آبجکت معمولاً پیش از ذخیره‌شدن آبجکت تولید می‌شوند. مهم است که به مقدار این فیلدها در پاسخ یک درخواست dry-run تکیه نکنید، زیرا این مقدارها در حالت dry-run به احتمال زیاد با مقدارهایی که هنگام ارسال درخواست واقعی تولید می‌شوند متفاوت خواهند بود. برخی از این فیلدها عبارت‌اند از:

* فیلد `name`: اگر `generateName` تنظیم شده باشد، `name` یک نام تصادفی یکتا خواهد داشت
* فیلدهای `creationTimestamp` / `deletionTimestamp`: زمان ایجاد/حذف را ثبت می‌کنند
* فیلد `UID`: آبجکت را [به‌طور یکتا شناسایی می‌کند](/docs/concepts/overview/working-with-objects/names/#uids)
  و به‌صورت تصادفی (غیرقطعی) تولید می‌شود
* فیلد `resourceVersion`: نسخهٔ ذخیره‌شدهٔ آبجکت را دنبال می‌کند
* هر فیلدی که یک کنترل‌کنندهٔ پذیرشِ تغییردهنده (mutating) تنظیم کند
* برای منبع `Service`: پورت‌ها یا نشانی‌های IP که kube-apiserver به آبجکت‌های Service اختصاص می‌دهد

### مجوزدهی dry-run

مجوزدهی برای درخواست‌های dry-run و غیر dry-run یکسان است. بنابراین، برای ارسال یک درخواست dry-run باید مجوز ارسال همان درخواست به‌صورت غیر dry-run را داشته باشید.

برای نمونه، برای اجرای یک **patch** به‌صورت dry-run روی یک Deployment، باید مجوز انجام همان **patch** را داشته باشید. در اینجا نمونه‌ای از یک قانون
{{< glossary_tooltip text="RBAC" term_id="rbac">}} در کوبرنتیز را می‌بینید که اجازهٔ patch کردن Deploymentها را می‌دهد:

```yaml
rules:
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["patch"]
```

به [مروری بر مجوزدهی](/docs/reference/access-authn-authz/authorization/) مراجعه کنید.

## به‌روزرسانی منابع موجود {#patch-and-apply}

کوبرنتیز چندین روش برای به‌روزرسانی آبجکت‌های موجود فراهم می‌کند. برای آشنایی با اینکه کدام رویکرد برای مورد استفادهٔ شما مناسب‌تر است، می‌توانید بخش [انتخاب سازوکار به‌روزرسانی](#update-mechanism-choose) را بخوانید.

می‌توانید یک منبع موجود، مثلاً یک ConfigMap، را با یک درخواست HTTP PUT بازنویسی (**update**) کنید. در درخواست PUT، مشخص‌کردن `resourceVersion` (که از آبجکتِ در حال به‌روزرسانی گرفته می‌شود) بر عهدهٔ کلاینت است. کوبرنتیز از این اطلاعات `resourceVersion` استفاده می‌کند تا سرور API بتواند به‌روزرسانی‌های ازدست‌رفته را تشخیص دهد و درخواست‌های کلاینتی را که نسبت به وضعیت کلاستر قدیمی است رد کند. اگر منبع تغییر کرده باشد (یعنی `resourceVersion` ارائه‌شده از سوی کلاینت کهنه باشد)، سرور API پاسخ خطای `409 Conflict` برمی‌گرداند.

کلاینت می‌تواند به‌جای ارسال درخواست PUT، دستوری به سرور API بفرستد تا یک منبع موجود را **patch** کند. **patch** معمولاً زمانی مناسب است که تغییری که کلاینت می‌خواهد اعمال کند به داده‌های موجود وابسته نباشد. کلاینت‌هایی که به تشخیص مؤثر به‌روزرسانی‌های ازدست‌رفته نیاز دارند، بهتر است درخواست خود را (چه HTTP PUT و چه HTTP PATCH) به `resourceVersion` موجود مشروط کنند و سپس در صورت بروز تعارض، تلاش‌های مجدد لازم را مدیریت کنند.

API کوبرنتیز از چهار عملیات PATCH مختلف پشتیبانی می‌کند که با سرآیند HTTP `Content-Type` متناظرشان تعیین می‌شوند:

`application/apply-patch+yaml`
: ‏Server Side Apply YAML (یک افزونهٔ ویژهٔ کوبرنتیز مبتنی بر YAML).
  همهٔ اسناد JSON، YAML معتبر هستند، بنابراین می‌توانید با این نوع رسانه JSON نیز ارسال کنید. برای جزئیات بیشتر به [سریال‌سازی در Server Side Apply](/docs/reference/using-api/server-side-apply/#serialization) مراجعه کنید.
  از دید کوبرنتیز، اگر آبجکت وجود نداشته باشد این یک عملیات **create** و اگر آبجکت از قبل وجود داشته باشد یک عملیات **patch** است.

`application/json-patch+json`
: ‏JSON Patch، همان‌گونه که در [RFC6902](https://tools.ietf.org/html/rfc6902) تعریف شده است.
  هر JSON patch دنباله‌ای از عملیات‌هاست که روی منبع اجرا می‌شوند؛ برای نمونه `{"op": "add", "path": "/a/b/c", "value": [ "foo", "bar" ]}`.
  از دید کوبرنتیز، این یک عملیات **patch** است.

  یک **patch** با `application/json-patch+json` می‌تواند شرط‌هایی برای اعتبارسنجی سازگاری داشته باشد تا در صورت برآورده‌نشدن آن شرط‌ها، عملیات با شکست مواجه شود (برای نمونه، برای جلوگیری از یک به‌روزرسانی ازدست‌رفته).

`application/merge-patch+json`
: ‏JSON Merge Patch، همان‌گونه که در [RFC7386](https://tools.ietf.org/html/rfc7386) تعریف شده است.
  هر JSON Merge Patch در اصل بازنمایی جزئی‌ای از منبع است. JSON ارسال‌شده با منبع فعلی ترکیب می‌شود تا منبع جدیدی ساخته شود و سپس منبع جدید ذخیره می‌شود.
  از دید کوبرنتیز، این یک عملیات **patch** است.

`application/strategic-merge-patch+json`
: ‏Strategic Merge Patch (یک افزونهٔ ویژهٔ کوبرنتیز مبتنی بر JSON).
  این روش یک پیاده‌سازی سفارشی از JSON Merge Patch است. از Strategic Merge Patch تنها می‌توانید با APIهای داخلی یا با سرورهای API تجمیعی (aggregated) که پشتیبانی ویژه‌ای از آن دارند استفاده کنید. نمی‌توانید از
  `application/strategic-merge-patch+json` با هیچ APIای که با یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} تعریف شده است استفاده کنید.

  {{< note >}}
  سازوکار _server side apply_ کوبرنتیز جایگزین Strategic Merge Patch شده است.
  {{< /note >}}

قابلیت [Server Side Apply](/docs/reference/using-api/server-side-apply/) در کوبرنتیز به control plane امکان می‌دهد فیلدهای مدیریت‌شده را برای آبجکت‌های تازه ایجادشده دنبال کند. این قابلیت الگوی روشنی برای مدیریت تعارض فیلدها فراهم می‌کند، عملیات‌های **apply** و **update** سمت سرور را ارائه می‌دهد و جایگزین کارکرد سمت کلاینتِ `kubectl apply` می‌شود.

در Server-Side Apply، اگر آبجکت هنوز وجود نداشته باشد کوبرنتیز درخواست را یک **create** و در غیر این صورت یک **patch** در نظر می‌گیرد. برای سایر درخواست‌هایی که در سطح HTTP از PATCH استفاده می‌کنند، عملیات منطقی کوبرنتیز همیشه **patch** است.

برای جزئیات بیشتر به [Server Side Apply](/docs/reference/using-api/server-side-apply/) مراجعه کنید.

### انتخاب سازوکار به‌روزرسانی {#update-mechanism-choose}

#### استفاده از HTTP PUT برای جایگزینی منبع موجود {#update-mechanism-update}

پیاده‌سازی عملیات **update** (HTTP `PUT`) ساده و انعطاف‌پذیر است، اما معایبی دارد:

* باید تعارض‌هایی را مدیریت کنید که در آن‌ها `resourceVersion` آبجکت در فاصلهٔ میان خواندن آن توسط کلاینت و تلاش برای بازنویسی‌اش تغییر می‌کند. کوبرنتیز همیشه این تعارض را تشخیص می‌دهد، اما شما به‌عنوان نویسندهٔ کلاینت باید تلاش مجدد را پیاده‌سازی کنید.
* اگر آبجکتی را به‌صورت محلی رمزگشایی کنید، ممکن است ناخواسته برخی فیلدها را از دست بدهید (برای نمونه، با استفاده از client-go ممکن است فیلدهایی دریافت کنید که کلاینت شما نمی‌داند چگونه با آن‌ها کار کند و سپس آن‌ها را در جریان به‌روزرسانی حذف کند).
* اگر رقابت زیادی بر سر آبجکت وجود داشته باشد (حتی روی فیلد یا مجموعه‌ای از فیلدها که قصد ویرایش آن‌ها را ندارید)، ممکن است در ارسال به‌روزرسانی با مشکل روبه‌رو شوید. این مشکل برای آبجکت‌های بزرگ‌تر و آبجکت‌هایی با فیلدهای زیاد شدیدتر است.

#### استفاده از HTTP PATCH با JSON Patch {#update-mechanism-json-patch}

به‌روزرسانی از نوع **patch** سودمند است، زیرا:

* از آنجا که تنها تفاوت‌ها را ارسال می‌کنید، دادهٔ کمتری در درخواست `PATCH` فرستاده می‌شود.
* می‌توانید تغییراتی اعمال کنید که به مقدارهای موجود وابسته‌اند، مانند کپی‌کردن مقدار یک فیلد خاص در یک حاشیه‌نویسی (annotation).
* برخلاف **update** (HTTP `PUT`)، تغییر شما می‌تواند فوراً اعمال شود، حتی اگر فیلدهای نامرتبط مرتباً تغییر کنند؛ معمولاً نیازی به تلاش مجدد نخواهید داشت.
  * اگر بخواهید برای جلوگیری از به‌روزرسانی‌های ازدست‌رفته احتیاط بیشتری به خرج دهید، ممکن است همچنان لازم باشد `resourceVersion` را (برای تطابق با یک آبجکت موجود) مشخص کنید
  * همچنان بهتر است منطقی برای تلاش مجدد در صورت بروز خطا بنویسید.
* می‌توانید با استفاده از شرط‌های آزمون (test)، شرایط به‌روزرسانی مشخصی را با دقت طراحی کنید. برای نمونه، می‌توانید بدون خواندن یک شمارنده، در صورتی که مقدار موجود با مقدار مورد انتظارتان مطابقت داشته باشد، آن را افزایش دهید. این کار را می‌توانید بدون خطر از دست رفتن به‌روزرسانی انجام دهید، حتی اگر آبجکت از آخرین باری که در آن نوشته‌اید به شکل‌های دیگری تغییر کرده باشد. (اگر شرط آزمون برقرار نباشد، می‌توانید به خواندن مقدار فعلی بازگردید و سپس عدد تغییریافته را بازنویسی کنید.)

با این حال:

* برای ساختن patch به منطق محلی (سمت کلاینت) بیشتری نیاز دارید؛ داشتن یک کتابخانه با پیاده‌سازی JSON Patch، یا حتی کتابخانه‌ای برای ساخت JSON Patch به‌طور خاص برای کوبرنتیز، کمک زیادی می‌کند.
* به‌عنوان نویسندهٔ نرم‌افزار کلاینت، هنگام ساختن patch (بدنهٔ درخواست HTTP) باید مراقب باشید که فیلدی از دست نرود (ترتیب عملیات‌ها اهمیت دارد).

#### استفاده از HTTP PATCH با Server-Side Apply {#update-mechanism-server-side-apply}

روش Server-Side Apply مزایای روشنی دارد:

* تنها یک رفت‌وبرگشت: به‌ندرت لازم است ابتدا یک درخواست `GET` ارسال کنید.
  * و همچنان می‌توانید تعارض‌های ناشی از تغییرات غیرمنتظره را تشخیص دهید
  * در صورت لزوم، می‌توانید یک تعارض را به‌اجبار نادیده بگیرید و مقدار خود را اعمال کنید
* ساخت پیاده‌سازی‌های کلاینت آسان است.
* بدون تلاش اضافه، یک عملیات اتمی ایجاد-یا-به‌روزرسانی در اختیار دارید (مشابه `UPSERT` در برخی گویش‌های SQL).

با این حال:

* روش Server-Side Apply برای تغییر فیلدهایی که به مقدار فعلی آبجکت وابسته‌اند اصلاً کار نمی‌کند.
* تنها می‌توانید به‌روزرسانی‌ها را روی آبجکت‌ها اعمال کنید. برخی از منابع در HTTP API کوبرنتیز آبجکت نیستند (فیلد `.metadata` ندارند) و Server-Side Apply تنها برای آبجکت‌های کوبرنتیز کاربرد دارد.

## نسخه‌های منبع

نسخه‌های منبع (resource versions) رشته‌هایی هستند که نسخهٔ داخلی یک آبجکت را در سرور مشخص می‌کنند. کلاینت‌ها می‌توانند از نسخه‌های منبع برای تشخیص زمان تغییر آبجکت‌ها یا برای بیان الزامات سازگاری داده هنگام get، list و watch کردن منابع استفاده کنند. نسخه‌های منبع باید بدون تغییر به سرور بازگردانده شوند.

رشته‌های نسخهٔ منبع، در یک نوع منبع یکسان و برای همهٔ نوع‌هایی که kube-apiserver ارائه می‌کند، مانند اعداد صحیحِ یکنواخت صعودی قابل مرتب‌سازی هستند. این موضوع شامل نوع‌های داخلی API و نوع‌های مبتنی بر custom resource definitionها نیز می‌شود. هر دو نسخهٔ منبع باید متعلق به آبجکت‌هایی از یک گروه API و نوع منبع یکسان باشند. برای نمونه، می‌توان نسخه‌های منبع دو Deployment از گروه API ‏apps را با هم مقایسه کرد، اما یک Pod و یک Deployment را نمی‌توان. به شرط آنکه دو آبجکت از یک نوع منبع API یکسان بازیابی شده باشند، می‌توانید آن‌ها را حتی اگر در فضاهای نام متفاوتی باشند با هم مقایسه کنید.

اگر از منابع APIای استفاده می‌کنید که یک سرور API افزونه (extension API server) ارائه می‌کند، کلاینت باید بررسی کند که آیا رشتهٔ نسخهٔ منبع به‌عنوان یک عدد دهدهی تجزیه می‌شود یا نه (جزئیات بیشتر در چند پاراگراف بعدی آمده است). اگر هر یک از دو رشتهٔ نسخهٔ منبع به‌عنوان عدد دهدهی تجزیه نشود، می‌توان برابری دو رشته را بررسی کرد، اما **نمی‌توان** برای تعیین ترتیب به مقایسهٔ آن‌ها تکیه کرد.

از کوبرنتیز نسخهٔ 1.35 به بعد، قابلیت مرتب‌سازی نسخه‌های منبع برای همهٔ نوع‌های کوبرنتیز جزو الزامات [Certified
Kubernetes](https://www.cncf.io/training/certification/software-conformance/) است. آبجکت‌های پایهٔ API و منابع سفارشی در هر پیاده‌سازی APIServer نسخهٔ 1.35 به بعد **باید** مانند یک عدد صحیح یکنواخت صعودی قابل مرتب‌سازی باشند تا آزمون‌های انطباق (conformance) را با موفقیت بگذرانند.

برای مقایسهٔ دو رشتهٔ نسخهٔ منبع:

مطمئن شوید که الزامات زیر برآورده شده‌اند:
* هر دو نسخهٔ منبع، همان‌طور که در بالا توضیح داده شد، باید از یک نوع منبع یکسان باشند
* هر دو باید با یکی از ارقام 1 تا 9 شروع شوند و تنها شامل ارقام 0 تا 9 باشند
* نسخه‌های منبع به‌صورت اعداد صحیح دهدهی با اندازهٔ بیتی دلخواه مقایسه می‌شوند

برای مقایسهٔ آن‌ها بدون تکیه بر اندازهٔ بیتی ثابت، می‌توان آن‌ها را به‌صورت رشته مقایسه کرد. نباید فرض کرد که اندازهٔ بیتی مقدار ثابتی است.

به‌جای آن، می‌توان از مقایسهٔ واژگانی (lexicographical) به شکل زیر استفاده کرد:
* اگر طول آن‌ها برابر نباشد، رشتهٔ بلندتر بزرگ‌تر است (برای نمونه، "123" > "23")
* اگر طول آن‌ها برابر باشد، رشته‌ای که از نظر واژگانی بزرگ‌تر است بزرگ‌تر است (برای نمونه، "234" > "123")

چند نمونه از مقایسه‌های نسخهٔ منبع که باید درست کار کنند:
* ‏"2345678901234567890123456789012345678901" > "345678901234567890123456789012345678901"
* ‏"345678901234567890123456789012345678901" == "345678901234567890123456789012345678901"
* ‏"345678901234567890123456789012345678900" < "345678901234567890123456789012345678901"

برای انجام این مقایسه، یک متد کمکی در
[client-go](https://pkg.go.dev/k8s.io/apimachinery/pkg/util/resourceversion#CompareResourceVersion)
در دسترس است.

### فیلدهای `resourceVersion` در metadata {#resourceversion-in-metadata}

کلاینت‌ها نسخه‌های منبع را در خود منابع پیدا می‌کنند، از جمله در منابعی که از جریان پاسخ یک **watch** دریافت می‌شوند یا هنگام استفاده از **list** برای فهرست‌کردن منابع.

در [v1.meta/ObjectMeta](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#objectmeta-v1-meta)، فیلد `metadata.resourceVersion` یک نمونهٔ منبع، نسخهٔ منبعی را مشخص می‌کند که آن نمونه آخرین بار در آن تغییر کرده است.

در [v1.meta/ListMeta](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#listmeta-v1-meta)، فیلد `metadata.resourceVersion` یک مجموعه از منابع (پاسخ یک **list**)، نسخهٔ منبعی را مشخص می‌کند که مجموعه در آن ساخته شده است.

### پارامترهای `resourceVersion` در رشته‌های پرس‌وجو {#the-resourceversion-parameter}

عملیات‌های **get**، **list** و **watch** از پارامتر `resourceVersion` پشتیبانی می‌کنند. از نسخهٔ v1.19، سرورهای API کوبرنتیز از پارامتر `resourceVersionMatch` نیز در درخواست‌های _list_ پشتیبانی می‌کنند.

سرور API پارامتر `resourceVersion` را بسته به عملیاتی که درخواست می‌کنید و مقدار `resourceVersion` به شکل‌های متفاوتی تفسیر می‌کند. اگر `resourceVersionMatch` را تنظیم کنید، این پارامتر نیز بر نحوهٔ انجام تطابق اثر می‌گذارد.

### معناشناسی **get** و **list**

برای **get** و **list**، معنای `resourceVersion` به این صورت است:

**get:**

| بدون تنظیم resourceVersion | مقدار resourceVersion="0" | مقدار resourceVersion="{مقداری غیر از 0}" |
|-----------------------|---------------------|----------------------------------------|
| جدیدترین           | هر نسخه                 | نه قدیمی‌تر از                         |

**list:**

از نسخهٔ v1.19، سرورهای API کوبرنتیز از پارامتر `resourceVersionMatch` در درخواست‌های _list_ پشتیبانی می‌کنند. اگر هم `resourceVersion` و هم `resourceVersionMatch` را تنظیم کنید، پارامتر `resourceVersionMatch` تعیین می‌کند که سرور API مقدار `resourceVersion` را چگونه تفسیر کند.

هر بار که `resourceVersion` را در یک درخواست **list** تنظیم می‌کنید، پارامتر `resourceVersionMatch` را نیز تنظیم کنید. با این حال، برای حالتی آماده باشید که سرور API پاسخ‌دهنده از `resourceVersionMatch` اطلاعی ندارد و آن را نادیده می‌گیرد.

اگر به سازگاری قوی (strong consistency) نیاز ندارید، بهتر است از `resourceVersionMatch=NotOlderThan` همراه با یک `resourceVersion` معلوم استفاده کنید. حالت دیگر، یعنی تنظیم‌نکردن `resourceVersion` و `resourceVersionMatch`، برای پاسخ‌دادن به خواندن مبتنی بر حد نصاب (quorum read) نیاز دارد. روش اول در مقایسه با این حالت کارایی و مقیاس‌پذیری بهتری برای کلاستر شما فراهم می‌کند.

تنظیم پارامتر `resourceVersionMatch` بدون تنظیم `resourceVersion` معتبر نیست.

جدول زیر رفتار درخواست‌های **list** را با ترکیب‌های مختلف `resourceVersion` و `resourceVersionMatch` توضیح می‌دهد:

{{< table caption="resourceVersionMatch and paging parameters for list" >}}

| پارامتر resourceVersionMatch          | پارامترهای صفحه‌بندی                  | بدون تنظیم resourceVersion | مقدار resourceVersion="0" | مقدار resourceVersion="{مقداری غیر از 0}" |
|-------------------------------------|--------------------------------|-------------------------|---------------------|----------------------------------------|
| _تنظیم‌نشده_                             | _بدون limit_                  | جدیدترین             | هر نسخه                 | نه قدیمی‌تر از                         |
| _تنظیم‌نشده_                             | مقدار limit=\<n\>، _بدون continue_  | جدیدترین             | هر نسخه                 | دقیق                                  |
| _تنظیم‌نشده_                             | مقدار limit=\<n\>، continue=\<token\>| ادامه            | ادامه        | نامعتبر، HTTP `400 Bad Request`        |
| `resourceVersionMatch=Exact`        | _بدون limit_                  | نامعتبر                 | نامعتبر             | دقیق                                  |
| `resourceVersionMatch=Exact`        | مقدار limit=\<n\>، _بدون continue_  | نامعتبر                 | نامعتبر             | دقیق                                  |
| `resourceVersionMatch=NotOlderThan` | _بدون limit_                  | نامعتبر                 | هر نسخه                 | نه قدیمی‌تر از                         |
| `resourceVersionMatch=NotOlderThan` | مقدار limit=\<n\>، _بدون continue_  | نامعتبر                 | هر نسخه                 | نه قدیمی‌تر از                         |

{{< /table >}}

{{< note >}}
اگر سرور API کلاستر شما پارامتر `resourceVersionMatch` را رعایت نکند، رفتار آن مانند حالتی است که این پارامتر را تنظیم نکرده باشید.
{{< /note >}}

معنای هر یک از این حالت‌ها برای **get** و **list** به شرح زیر است:

هر نسخه
: داده‌ها را در هر نسخه‌ای از منبع بازمی‌گرداند. جدیدترین نسخهٔ موجودِ منبع ترجیح داده می‌شود، اما سازگاری قوی الزامی نیست و ممکن است داده‌ها در هر نسخه‌ای ارائه شوند. ممکن است درخواست، داده‌ها را در نسخه‌ای بسیار قدیمی‌تر از نسخه‌ای بازگرداند که کلاینت پیش‌تر مشاهده کرده است. این وضعیت به‌ویژه در پیکربندی‌های با دسترس‌پذیری بالا (high availability) و به‌دلیل پارتیشن‌بندی شبکه یا کش‌های کهنه رخ می‌دهد. کلاینت‌هایی که این وضعیت را تحمل نمی‌کنند نباید از این حالت استفاده کنند. پاسخ همیشه از _کش watch_ (watch cache) ارائه می‌شود که کارایی را بهبود می‌دهد و بار etcd را کاهش می‌دهد.

جدیدترین
: داده‌ها را در جدیدترین نسخهٔ منبع بازمی‌گرداند. داده‌های بازگردانده‌شده باید سازگار باشند (به‌طور دقیق: از etcd و از طریق خواندن مبتنی بر حد نصاب ارائه شوند). برای etcd نسخهٔ v3.4.31 به بعد و v3.5.13 به بعد، کوبرنتیز {{< skew currentVersion >}} خواندن‌های «جدیدترین» را از _کش watch_ ارائه می‌کند. این کش یک مخزن داخلی و درون‌حافظه‌ای در سرور API است که وضعیت داده‌های ذخیره‌شده در etcd را کش و بازتاب می‌کند. کوبرنتیز برای حفظ سازگاری کش با لایهٔ ماندگاری etcd، اعلان پیشرفت (progress notification) درخواست می‌کند. نسخه‌های v1.28 تا v1.30 کوبرنتیز نیز از این قابلیت پشتیبانی می‌کردند، اما چون قابلیت در وضعیت آلفا بود، تا انتشار نسخهٔ v1.31 برای محیط عملیاتی توصیه نمی‌شد و به‌طور پیش‌فرض فعال نبود.

نه قدیمی‌تر از
: داده‌هایی را بازمی‌گرداند که دست‌کم به اندازهٔ `resourceVersion` ارائه‌شده جدید باشند. جدیدترین داده‌های موجود ترجیح داده می‌شوند، اما ممکن است هر داده‌ای که قدیمی‌تر از `resourceVersion` ارائه‌شده نباشد ارائه شود. در درخواست‌های **list** به سرورهایی که پارامتر `resourceVersionMatch` را رعایت می‌کنند، این حالت تضمین می‌کند که مقدار `.metadata.resourceVersion` مجموعه قدیمی‌تر از `resourceVersion` درخواست‌شده نباشد، اما هیچ تضمینی دربارهٔ `.metadata.resourceVersion` آیتم‌های آن مجموعه نمی‌دهد. پاسخ همیشه از _کش watch_ ارائه می‌شود که کارایی را بهبود می‌دهد و بار etcd را کاهش می‌دهد.

دقیق
: داده‌ها را دقیقاً در نسخهٔ منبعِ ارائه‌شده بازمی‌گرداند. اگر `resourceVersion` ارائه‌شده در دسترس نباشد، سرور با HTTP `410 Gone` پاسخ می‌دهد. در درخواست‌های **list** به سرورهایی که پارامتر `resourceVersionMatch` را رعایت می‌کنند، این حالت تضمین می‌کند که مقدار `.metadata.resourceVersion` مجموعه با `resourceVersion`ی که در رشتهٔ پرس‌وجو درخواست کرده‌اید یکسان باشد. این تضمین شامل `.metadata.resourceVersion` آیتم‌های درون آن مجموعه نمی‌شود. وقتی feature gate `ListFromCacheSnapshot` فعال باشد (که به‌طور پیش‌فرض فعال است)، سرور API تلاش می‌کند پاسخ را از اسنپ‌شات‌ها ارائه کند، به شرط آنکه اسنپ‌شاتی با `resourceVersion` قدیمی‌تر از نسخهٔ درخواست‌شده موجود باشد. این کار کارایی را بهبود می‌دهد و بار etcd را کاهش می‌دهد. سرور API بدون هیچ اسنپ‌شاتی شروع به کار می‌کند و با هر رویداد watch یک اسنپ‌شات جدید می‌سازد. سرور اسنپ‌شات‌ها را تا زمانی نگه می‌دارد که تشخیص دهد etcd فشرده‌سازی (compaction) شده است یا کش از رویدادهای قدیمی‌تر از ۷۵ ثانیه پر شده است. اگر `resourceVersion` ارائه‌شده در دسترس نباشد، سرور به etcd بازمی‌گردد.

ادامه
: صفحهٔ بعدی داده‌ها را برای یک درخواست list صفحه‌بندی‌شده بازمی‌گرداند و سازگاری با همان `resourceVersion` دقیقی را تضمین می‌کند که درخواست اولیهٔ این دنباله تعیین کرده است. پاسخ درخواست‌های **list** که limit دارند شامل یک _توکن ادامه_ (continue token) است. این توکن `resourceVersion` و آخرین موقعیت مشاهده‌شده را رمزگذاری می‌کند تا فهرست از همان نقطه ادامه یابد. اگر `resourceVersion` موجود در _توکن ادامه_ ارائه‌شده در دسترس نباشد، سرور با HTTP `410 Gone` پاسخ می‌دهد. وقتی feature gate `ListFromCacheSnapshot` فعال باشد (که به‌طور پیش‌فرض فعال است)، سرور API تلاش می‌کند پاسخ را از اسنپ‌شات‌ها ارائه کند، به شرط آنکه اسنپ‌شاتی با `resourceVersion` قدیمی‌تر از نسخهٔ درخواست‌شده موجود باشد. این کار کارایی را بهبود می‌دهد و بار etcd را کاهش می‌دهد. سرور API بدون هیچ اسنپ‌شاتی شروع به کار می‌کند و با هر رویداد watch یک اسنپ‌شات جدید می‌سازد. سرور اسنپ‌شات‌ها را تا زمانی نگه می‌دارد که تشخیص دهد etcd فشرده‌سازی شده است یا کش از رویدادهای قدیمی‌تر از ۷۵ ثانیه پر شده است. اگر `resourceVersion` موجود در _توکن ادامه_ ارائه‌شده در دسترس نباشد، سرور به etcd بازمی‌گردد.

{{< note >}}
وقتی منابع را **list** می‌کنید و پاسخی از نوع مجموعه دریافت می‌کنید، این پاسخ هم
[فراداده‌های فهرست](/docs/reference/generated/kubernetes-api/v{{<skew currentVersion >}}/#listmeta-v1-meta)
مجموعه و هم
[فراداده‌های آبجکت](/docs/reference/generated/kubernetes-api/v{{<skew currentVersion >}}/#objectmeta-v1-meta)
هر آیتم آن مجموعه را در بر دارد. برای آبجکت‌های منفردی که در پاسخ مجموعه قرار دارند، مقدار `.metadata.resourceVersion` نشان می‌دهد آن آبجکت آخرین بار چه زمانی به‌روزرسانی شده است، نه اینکه آبجکت در زمان ارائه تا چه اندازه به‌روز است.
{{< /note >}}

هنگام استفاده از `resourceVersionMatch=NotOlderThan` در حالتی که limit تنظیم شده است، کلاینت‌ها باید پاسخ‌های HTTP `410 Gone` را مدیریت کنند. برای مثال، کلاینت می‌تواند با یک `resourceVersion` جدیدتر دوباره تلاش کند یا به `resourceVersion=""` بازگردد.

هنگام استفاده از `resourceVersionMatch=Exact` در حالتی که `limit` تنظیم نشده است، کلاینت‌ها باید بررسی کنند که مقدار `.metadata.resourceVersion` مجموعه با `resourceVersion` درخواست‌شده مطابقت داشته باشد و حالت عدم مطابقت را مدیریت کنند. برای مثال، کلاینت می‌تواند به ارسال درخواستی با `limit` تنظیم‌شده بازگردد.

### معناشناسی **watch**

برای **watch**، معنای نسخهٔ منبع به این صورت است:

**watch:**

{{< table caption="resourceVersion for watch" >}}

| بدون تنظیم resourceVersion               | مقدار resourceVersion="0"        | مقدار resourceVersion="{مقداری غیر از 0}" |
|-------------------------------------|----------------------------|----------------------------------------|
| دریافت وضعیت و شروع از جدیدترین  | دریافت وضعیت و شروع از هر نسخه | شروع از نسخهٔ دقیق                         |

{{< /table >}}

معنای هر یک از این حالت‌های **watch** به شرح زیر است:

دریافت وضعیت و شروع از هر نسخه
: یک **watch** را از هر نسخه‌ای از منبع شروع می‌کند. جدیدترین نسخهٔ موجودِ منبع ترجیح داده می‌شود، اما الزامی نیست و شروع از هر نسخه‌ای مجاز است. ممکن است **watch** از نسخه‌ای بسیار قدیمی‌تر از نسخه‌ای شروع شود که کلاینت پیش‌تر مشاهده کرده است. این وضعیت به‌ویژه در پیکربندی‌های با دسترس‌پذیری بالا و به‌دلیل پارتیشن‌بندی شبکه یا کش‌های کهنه رخ می‌دهد. کلاینت‌هایی که این عقب‌گردِ ظاهری را تحمل نمی‌کنند نباید **watch** را با این حالت شروع کنند. برای برقراری وضعیت اولیه، **watch** با رویدادهای مصنوعی "Added" برای همهٔ نمونه‌های منبعی آغاز می‌شود که در نسخهٔ شروع وجود دارند. همهٔ رویدادهای watch بعدی مربوط به تغییراتی هستند که پس از نسخهٔ منبعِ شروعِ **watch** رخ داده‌اند.

  {{< caution >}}
  ممکن است **watch**هایی که به این روش راه‌اندازی می‌شوند داده‌هایی با هر میزان کهنگی بازگردانند. پیش از استفاده از این حالت آن را به‌دقت بررسی کنید و در صورت امکان حالت‌های دیگر را ترجیح دهید.
  {{< /caution >}}

دریافت وضعیت و شروع از جدیدترین
: یک **watch** را از جدیدترین نسخهٔ منبع شروع می‌کند که باید سازگار باشد (به‌طور دقیق: از etcd و از طریق خواندن مبتنی بر حد نصاب ارائه شود). برای برقراری وضعیت اولیه، **watch** با رویدادهای مصنوعی "Added" برای همهٔ نمونه‌های منبعی آغاز می‌شود که در نسخهٔ شروع وجود دارند. همهٔ رویدادهای watch بعدی مربوط به تغییراتی هستند که پس از نسخهٔ منبعِ شروعِ **watch** رخ داده‌اند.

شروع از نسخهٔ دقیق
: یک **watch** را دقیقاً از نسخهٔ مشخصی از منبع شروع می‌کند. رویدادهای watch مربوط به همهٔ تغییراتی هستند که پس از نسخهٔ منبعِ ارائه‌شده رخ داده‌اند. برخلاف «دریافت وضعیت و شروع از جدیدترین» و «دریافت وضعیت و شروع از هر نسخه»، در این حالت **watch** با رویدادهای مصنوعی "Added" برای نسخهٔ منبعِ ارائه‌شده شروع نمی‌شود. فرض بر این است که کلاینت وضعیت اولیه را در نسخهٔ شروع از قبل در اختیار دارد، زیرا خودِ کلاینت این نسخه را ارائه کرده است.

### پاسخ‌های "410 Gone"

سرورها ملزم نیستند همهٔ نسخه‌های قدیمی‌تر منابع را ارائه کنند. اگر کلاینت `resourceVersion`ی قدیمی‌تر از نسخه‌هایی درخواست کند که سرور نگه داشته است، ممکن است سرور کد وضعیت HTTP `410 (Gone)` را بازگرداند. کلاینت‌ها باید بتوانند پاسخ‌های `410 (Gone)` را تحمل کنند. برای جزئیات نحوهٔ مدیریت پاسخ‌های `410 (Gone)` هنگام watch کردن منابع، به [تشخیص کارآمد تغییرات](#efficient-detection-of-changes) مراجعه کنید.

اگر `resourceVersion`ی خارج از محدودهٔ مجاز درخواست کنید، ممکن است سرور API، بسته به اینکه درخواست از کش ارائه می‌شود یا نه، با یک پاسخ HTTP `410 Gone` پاسخ دهد.

### نسخه‌های منبعِ در دسترس نبوده

سرورها ملزم نیستند نسخه‌های ناشناختهٔ منابع را ارائه کنند. اگر **list** یا **get** را برای نسخه‌ای از منبع درخواست کنید که سرور API آن را نمی‌شناسد، سرور API ممکن است یکی از این دو کار را انجام دهد:

* مدت کوتاهی منتظر بماند تا آن نسخهٔ منبع در دسترس قرار گیرد و اگر نسخه‌های منبعِ ارائه‌شده در مدت زمان معقولی در دسترس قرار نگیرند، با خطای `504 (Gateway Timeout)` به پایان مهلت برسد؛
* با سرآیند پاسخ `Retry-After` پاسخ دهد که نشان می‌دهد کلاینت پیش از تلاش دوباره باید چند ثانیه صبر کند.

اگر نسخه‌ای از منبع را درخواست کنید که سرور API آن را نمی‌شناسد، kube-apiserver افزون بر این، پاسخ‌های خطای خود را با پیام `Too large resource version` مشخص می‌کند.

اگر یک درخواست **watch** برای نسخهٔ ناشناخته‌ای از منبع ارسال کنید، ممکن است سرور API به‌طور نامحدود (تا پایان مهلت درخواست) منتظر بماند تا آن نسخه در دسترس قرار گیرد.

### راه‌اندازی اولیهٔ کش watch {#watch-cache-initialization}

سرور API کوبرنتیز دو سازوکار محافظتی به کار می‌گیرد تا در هنگام راه‌اندازی اولیه یا راه‌اندازی مجدد کش watch، از اضافه‌بار control plane و گرسنگی (starvation) در API Priority and Fairness (APF) جلوگیری کند:

* **محافظت از آمادگی در زمان راه‌اندازی**: سرور API هنگام راه‌اندازی، گزارش آمادگی (`/readyz`) را تا زمانی به تعویق می‌اندازد که همهٔ کش‌های watch ثبت‌شده همگام‌سازی اولیهٔ خود با etcd را کامل کنند. این کار مانع می‌شود که متعادل‌کننده‌های بار (load balancer) ترافیک کلاینت‌ها را زودهنگام به سرور API هدایت کنند. به این ترتیب، هجوم هم‌زمان خواندن‌ها در زمان راه‌اندازی (thundering herd) از بین می‌رود؛ خواندن‌هایی که در غیر این صورت کشِ آماده‌نشده را دور می‌زدند و مستقیماً به etcd می‌رسیدند.
* **رد درخواست‌ها در حین راه‌اندازی اولیهٔ کش**: ممکن است درخواست‌هایی در زمانی برسند که کش watch برای یک نوع منبع هنوز راه‌اندازی نشده است؛ برای مثال هنگام بوت سرور (پیش از اعلام آمادگی) یا پس از همگام‌سازی مجدد یا قطع اتصال کش در زمان اجرا. در این وضعیت، سرور API نمی‌گذارد پرس‌وجوهای پرهزینه بار سنگینی بر etcd وارد کنند یا به‌طور نامحدود معلق بمانند:
  * **درخواست‌های `WATCH`** و **درخواست‌های `LIST` بدون صفحه‌بندی یا دارای فیلتر** (هر پرس‌وجوی list که `limit` صفحه‌بندی ندارد یا یک انتخابگر (selector) برچسب یا فیلد مشخص می‌کند) بی‌درنگ با کد وضعیت HTTP `429 Too Many Requests` و یک سرآیند `Retry-After` پویا رد می‌شوند. این کار از goroutineهای معلق، کمبود جایگاه (seat) در APF و تمام‌شدن حافظهٔ etcd جلوگیری می‌کند.
  * **خواندن‌های صفحه‌بندی‌شدهٔ ایمن**: فقط **درخواست‌های `GET`** و **درخواست‌های `LIST` صفحه‌بندی‌شده و بدون فیلتر** (`limit` > 0 بدون انتخابگر برچسب یا فیلد) به‌عنوان راه‌حل جایگزین ایمن، مستقیماً به etcd سپرده می‌شوند.

کلاینت‌ها (از جمله کنترل‌کننده‌ها و اپراتورهای سفارشی) باید طوری طراحی شوند که پاسخ‌های HTTP `429 Too Many Requests` را به‌درستی مدیریت کنند؛ یعنی سرآیندهای `Retry-After` را رعایت کنند و عقب‌نشینی نمایی (exponential backoff) را پیاده‌سازی کنند.

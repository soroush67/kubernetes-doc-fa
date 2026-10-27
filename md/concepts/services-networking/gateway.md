---
title: Gateway API
content_type: concept
description: >-
  Gateway API خانواده‌ای از انواع API است که فراهم‌سازی پویای زیرساخت
  و مسیریابی پیشرفتهٔ ترافیک را ارائه می‌کند.
weight: 55
---

<!-- overview -->

سرویس‌های شبکه را با استفاده از یک سازوکار پیکربندی توسعه‌پذیر، نقش‌محور و آگاه از پروتکل
در دسترس قرار دهید. [Gateway API](https://gateway-api.sigs.k8s.io/) یک {{<glossary_tooltip text="افزونه (add-on)" term_id="addons">}}
است که شامل [انواع](https://gateway-api.sigs.k8s.io/references/spec/) API است که فراهم‌سازی پویای زیرساخت
و مسیریابی پیشرفتهٔ ترافیک را ارائه می‌کنند.

<!-- body -->

## اصول طراحی

اصول زیر طراحی و معماری Gateway API را شکل داده‌اند:

* __نقش‌محور:__ انواع Gateway API بر اساس نقش‌های سازمانی‌ای مدل‌سازی شده‌اند که
  مسئول مدیریت شبکهٔ سرویس‌ها در کوبرنتیز هستند:
  * __ارائه‌دهندهٔ زیرساخت:__ زیرساختی را مدیریت می‌کند که به چندین کلاستر ایزوله اجازه می‌دهد
    به چندین مستأجر (tenant) خدمت‌رسانی کنند؛ برای مثال یک ارائه‌دهندهٔ ابری.
  * __اپراتور کلاستر:__ کلاسترها را مدیریت می‌کند و معمولاً با سیاست‌ها، دسترسی
    شبکه، مجوزهای برنامه و مواردی از این دست سروکار دارد.
  * __توسعه‌دهندهٔ برنامه:__ برنامه‌ای را که در یک کلاستر اجرا می‌شود مدیریت می‌کند و معمولاً
    با پیکربندی در سطح برنامه و ترکیب [Service](/docs/concepts/services-networking/service/)
    سروکار دارد.
* __قابل حمل:__ مشخصات Gateway API به‌صورت [منابع سفارشی (custom resources)](/docs/concepts/extend-kubernetes/api-extension/custom-resources)
  تعریف شده‌اند و [پیاده‌سازی‌های](https://gateway-api.sigs.k8s.io/implementations/) بسیاری از آن‌ها پشتیبانی می‌کنند.
* __بیانگر:__ انواع Gateway API از قابلیت‌هایی برای موارد استفادهٔ رایج مسیریابی ترافیک
  پشتیبانی می‌کنند، مانند تطبیق مبتنی بر هدر، وزن‌دهی ترافیک و موارد دیگری که پیش‌تر تنها در
  [Ingress](/docs/concepts/services-networking/ingress/) و با استفاده از حاشیه‌نویسی‌های سفارشی امکان‌پذیر بودند.
* __توسعه‌پذیر:__ Gateway اجازه می‌دهد منابع سفارشی در لایه‌های مختلف API پیوند داده شوند.
  این امر سفارشی‌سازی جزئی را در جاهای مناسب درون ساختار API ممکن می‌سازد.

## مدل منابع

Gateway API چهار نوع API پایدار دارد:

* __GatewayClass:__ مجموعه‌ای از gatewayها را با پیکربندی مشترک تعریف می‌کند که توسط کنترل‌کننده‌ای
  که این کلاس را پیاده‌سازی می‌کند، مدیریت می‌شوند.

* __Gateway:__ نمونه‌ای از زیرساخت رسیدگی به ترافیک، مانند توزیع‌کنندهٔ بار ابری، را تعریف می‌کند.

* __HTTPRoute:__ قواعد مختص HTTP را برای نگاشت ترافیک از یک listener در Gateway به
  نمایشی از endpointهای شبکهٔ backend تعریف می‌کند. این endpointها اغلب به‌صورت یک
  {{<glossary_tooltip text="Service" term_id="service">}} نمایش داده می‌شوند.

* __GRPCRoute:__ قواعد مختص gRPC را برای نگاشت ترافیک از یک listener در Gateway به
نمایشی از endpointهای شبکهٔ backend تعریف می‌کند. این endpointها اغلب به‌صورت یک
  {{<glossary_tooltip text="Service" term_id="service">}} نمایش داده می‌شوند.

Gateway API در قالب انواع API مختلفی سازمان‌دهی شده است که برای پشتیبانی از
ماهیت نقش‌محور سازمان‌ها، روابط وابسته به هم دارند. هر آبجکت Gateway دقیقاً با یک GatewayClass مرتبط است؛
GatewayClass کنترل‌کنندهٔ gateway مسئول مدیریت Gatewayهای این کلاس را توصیف می‌کند.
سپس یک یا چند نوع route، مانند HTTPRoute، با Gatewayها مرتبط می‌شوند. یک Gateway می‌تواند routeهایی را
که ممکن است به `listeners` آن متصل شوند فیلتر کند و بدین ترتیب یک مدل اعتماد دوسویه با routeها شکل دهد.

شکل زیر روابط سه نوع پایدار Gateway API را نشان می‌دهد:

{{< figure src="/docs/images/gateway-kind-relationships.svg" alt="شکلی که روابط سه نوع پایدار Gateway API را نشان می‌دهد" class="diagram-medium" >}}

### GatewayClass {#api-kind-gateway-class}

Gatewayها را می‌توان با کنترل‌کننده‌های مختلف و اغلب با پیکربندی‌های متفاوت پیاده‌سازی کرد. یک Gateway
باید به GatewayClassای ارجاع دهد که نام کنترل‌کنندهٔ پیاده‌سازی‌کنندهٔ آن
کلاس را در بر دارد.

یک نمونهٔ حداقلی از GatewayClass:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: example-class
spec:
  controllerName: example.com/gateway-controller
```

در این نمونه، کنترل‌کننده‌ای که Gateway API را پیاده‌سازی کرده است، برای مدیریت GatewayClassهایی
با نام کنترل‌کنندهٔ `example.com/gateway-controller` پیکربندی شده است. Gatewayهای این کلاس توسط
کنترل‌کنندهٔ آن پیاده‌سازی مدیریت خواهند شد.

برای تعریف کامل این نوع API، مرجع [GatewayClass](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.GatewayClass)
را ببینید.

### Gateway {#api-kind-gateway}

یک Gateway نمونه‌ای از زیرساخت رسیدگی به ترافیک را توصیف می‌کند. این آبجکت یک endpoint شبکه تعریف می‌کند
که می‌توان از آن برای پردازش ترافیک، یعنی فیلتر کردن، توزیع بار، تقسیم و غیره، برای backendهایی
مانند یک Service استفاده کرد. برای مثال، یک Gateway ممکن است نمایانگر یک توزیع‌کنندهٔ بار ابری یا یک سرور پراکسی
درون کلاستر باشد که برای پذیرش ترافیک HTTP پیکربندی شده است.

یک نمونهٔ معمول از منبع Gateway:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: example-namespace
spec:
  gatewayClassName: example-class
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    hostname: "www.example.com"
    allowedRoutes:
      namespaces:
        from: Same
```

در این نمونه، یک نمونه از زیرساخت رسیدگی به ترافیک طوری برنامه‌ریزی شده است که به ترافیک HTTP
روی پورت 80 گوش دهد. از آنجا که فیلد `addresses` تعیین نشده است، یک نشانی یا hostname
توسط کنترل‌کنندهٔ پیاده‌سازی به Gateway اختصاص داده می‌شود. این نشانی به‌عنوان endpoint شبکه برای
پردازش ترافیک endpointهای شبکهٔ backend که در routeها تعریف شده‌اند، استفاده می‌شود.

برای تعریف کامل این نوع API، مرجع [Gateway](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.Gateway)
را ببینید. برای راهنمایی دربارهٔ پیکربندی listenerهای HTTPS/TLS،
[راهنمای TLS در Gateway API](https://gateway-api.sigs.k8s.io/guides/tls/) را ببینید.

{{< note >}}
به‌طور پیش‌فرض، یک Gateway تنها Routeهایی را از همان فضای نام می‌پذیرد. Routeهای میان‌فضای‌نامی نیازمند پیکربندی `allowedRoutes` هستند.
{{< /note >}}

### HTTPRoute {#api-kind-httproute}

نوع HTTPRoute رفتار مسیریابی درخواست‌های HTTP را از یک listener در Gateway به endpointهای شبکهٔ
backend مشخص می‌کند. برای یک backend از نوع Service، یک پیاده‌سازی ممکن است endpoint شبکهٔ backend را به‌صورت IP
مربوط به Service یا EndpointSliceهای پشتیبان Service نمایش دهد. یک HTTPRoute نمایانگر پیکربندی‌ای است که بر
پیاده‌سازی زیرین Gateway اعمال می‌شود. برای مثال، تعریف یک HTTPRoute جدید ممکن است به پیکربندی routeهای
ترافیکی اضافی در یک توزیع‌کنندهٔ بار ابری یا سرور پراکسی درون کلاستر منجر شود.

یک نمونهٔ معمول از HTTPRoute:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-httproute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "www.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /login
    backendRefs:
    - name: example-svc
      port: 8080
```

در این نمونه، ترافیک HTTP از Gateway ‏`example-gateway` که هدر Host: آن روی `www.example.com`
تنظیم شده و مسیر درخواست آن `/login` باشد، به Service ‏`example-svc` روی پورت `8080` هدایت می‌شود.

برای تعریف کامل این نوع API، مرجع [HTTPRoute](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.HTTPRoute)
را ببینید.


### GRPCRoute {#api-kind-grpcroute}

نوع GRPCRoute رفتار مسیریابی درخواست‌های gRPC را از یک listener در Gateway به endpointهای شبکهٔ
backend مشخص می‌کند. برای یک backend از نوع Service، یک پیاده‌سازی ممکن است endpoint شبکهٔ backend را به‌صورت IP
مربوط به Service یا EndpointSliceهای پشتیبان Service نمایش دهد. یک GRPCRoute نمایانگر پیکربندی‌ای است که بر
پیاده‌سازی زیرین Gateway اعمال می‌شود. برای مثال، تعریف یک GRPCRoute جدید ممکن است به پیکربندی routeهای
ترافیکی اضافی در یک توزیع‌کنندهٔ بار ابری یا سرور پراکسی درون کلاستر منجر شود.

Gatewayهایی که از GRPCRoute پشتیبانی می‌کنند، ملزم‌اند بدون ارتقای اولیه از HTTP/1 از HTTP/2 پشتیبانی کنند
تا جریان صحیح ترافیک gRPC تضمین شود.

یک نمونهٔ معمول از GRPCRoute:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - backendRefs:
    - name: example-svc
      port: 50051
```

در این نمونه، ترافیک gRPC از Gateway ‏`example-gateway` که host آن روی `svc.example.com` تنظیم شده باشد،
به سرویس `example-svc` روی پورت `50051` در همان فضای نام هدایت می‌شود.

GRPCRoute امکان تطبیق سرویس‌های gRPC مشخص را فراهم می‌کند، مطابق نمونهٔ زیر:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - matches:
    - method:
        service: com.example
        method: Login
    backendRefs:
    - name: foo-svc
      port: 50051
```

در این حالت، GRPCRoute با هر ترافیکی برای svc.example.com مطابقت پیدا می‌کند و قواعد مسیریابی خود را
برای ارسال ترافیک به backend درست اعمال می‌کند. از آنجا که تنها یک تطبیق تعیین شده است، تنها درخواست‌های
مربوط به متد com.example.User.Login به svc.example.com ارسال خواهند شد.
RPCهای مربوط به هر متد دیگری با این Route مطابقت پیدا نخواهند کرد.

برای تعریف کامل این نوع API، مرجع [GRPCRoute](https://gateway-api.sigs.k8s.io/references/spec/#grpcroute)
را ببینید.

## جریان درخواست

در اینجا یک نمونهٔ ساده از ترافیک HTTP آمده است که با استفاده از یک Gateway و یک HTTPRoute به یک Service هدایت می‌شود:

{{< figure src="/docs/images/gateway-request-flow.svg" alt="نموداری که نمونه‌ای از هدایت ترافیک HTTP به یک Service با استفاده از یک Gateway و یک HTTPRoute را نشان می‌دهد" class="diagram-medium" >}}

در این نمونه، جریان درخواست برای Gatewayای که به‌صورت reverse proxy پیاده‌سازی شده، به این شرح است:

1. کلاینت شروع به آماده‌سازی یک درخواست HTTP برای URL ‏`http://www.example.com` می‌کند
2. resolver مربوط به DNS در کلاینت، نام مقصد را پرس‌وجو می‌کند و نگاشتی به
   یک یا چند نشانی IP مرتبط با Gateway به دست می‌آورد.
3. کلاینت درخواستی به نشانی IP مربوط به Gateway ارسال می‌کند؛ reverse proxy درخواست HTTP را
   دریافت می‌کند و با استفاده از هدر Host: آن را با پیکربندی‌ای تطبیق می‌دهد که از Gateway
   و HTTPRoute متصل‌شده به دست آمده است.
4. به‌صورت اختیاری، reverse proxy می‌تواند بر اساس قواعد تطبیق HTTPRoute،
   تطبیق هدر درخواست و/یا مسیر را انجام دهد.
5. به‌صورت اختیاری، reverse proxy می‌تواند درخواست را بر اساس قواعد فیلتر HTTPRoute تغییر دهد؛
   برای مثال، هدرهایی را اضافه یا حذف کند.
6. در پایان، reverse proxy درخواست را به یک یا چند backend ارسال می‌کند.

## انطباق (Conformance)

Gateway API مجموعهٔ گسترده‌ای از قابلیت‌ها را پوشش می‌دهد و به‌طور گسترده پیاده‌سازی شده است. این ترکیب
نیازمند تعاریف و آزمون‌های انطباق روشنی است تا اطمینان حاصل شود که API در هر جایی که استفاده می‌شود،
تجربه‌ای یکسان ارائه می‌کند.

برای درک جزئیاتی مانند کانال‌های انتشار، سطوح پشتیبانی و اجرای آزمون‌های انطباق، مستندات
[انطباق](https://gateway-api.sigs.k8s.io/docs/concepts/conformance/) را ببینید.

## مهاجرت از Ingress

Gateway API جانشین API مربوط به [Ingress](/docs/concepts/services-networking/ingress/) است.
با این حال، نوع Ingress را در بر ندارد. در نتیجه، یک تبدیل یک‌باره از منابع Ingress موجود شما
به منابع Gateway API ضروری است.

برای جزئیات مهاجرت منابع Ingress به منابع Gateway API، به راهنمای
[مهاجرت از ingress](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress) مراجعه کنید.

## {{% heading "whatsnext" %}}

به‌جای آنکه منابع Gateway API به‌صورت بومی توسط کوبرنتیز پیاده‌سازی شوند، مشخصات آن‌ها
به‌صورت [منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
تعریف شده‌اند که طیف گسترده‌ای از [پیاده‌سازی‌ها](https://gateway-api.sigs.k8s.io/implementations/) از آن‌ها پشتیبانی می‌کنند.
CRDهای Gateway API را [نصب کنید](https://gateway-api.sigs.k8s.io/guides/#installing-gateway-api) یا
دستورالعمل‌های نصب پیاده‌سازی انتخابی خود را دنبال کنید. پس از نصب یک
پیاده‌سازی، از راهنمای [شروع به کار](https://gateway-api.sigs.k8s.io/guides/) استفاده کنید تا
به‌سرعت کار با Gateway API را آغاز کنید.

{{< note >}}
حتماً مستندات پیاده‌سازی انتخابی خود را مرور کنید تا از هرگونه نکتهٔ احتیاطی آگاه شوید.
{{< /note >}}

برای جزئیات بیشتر دربارهٔ همهٔ انواع Gateway API، به [مشخصات API](https://gateway-api.sigs.k8s.io/reference/api-spec/main/spec/)
مراجعه کنید.

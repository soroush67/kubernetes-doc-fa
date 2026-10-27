---
reviewers:
- robscott
- rikatz
title: Ingress
api_metadata:
- apiVersion: "networking.k8s.io/v1"
  kind: "Ingress"
- apiVersion: "networking.k8s.io/v1"
  kind: "IngressClass"
content_type: concept
description: >-
  سرویس شبکهٔ HTTP (یا HTTPS) خود را با استفاده از یک سازوکار پیکربندی آگاه از پروتکل
  در دسترس قرار دهید که مفاهیم وب مانند URIها، hostnameها، مسیرها و موارد دیگر را درک می‌کند.
  مفهوم Ingress به شما امکان می‌دهد ترافیک را بر اساس قواعدی که از طریق API کوبرنتیز
  تعریف می‌کنید، به backendهای مختلف نگاشت کنید.
weight: 30
---

<!-- overview -->
{{< feature-state for_k8s_version="v1.19" state="stable" >}}
{{< glossary_definition term_id="ingress" length="all" >}}

{{< note >}}
پروژهٔ کوبرنتیز استفاده از [Gateway](https://gateway-api.sigs.k8s.io/) را به‌جای
[Ingress](/docs/concepts/services-networking/ingress/) توصیه می‌کند.
API مربوط به Ingress منجمد شده است.

این به آن معناست که:
* API مربوط به Ingress به‌طور عمومی در دسترس (GA) است و مشمول [تضمین‌های پایداری](/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api) مربوط به APIهای عمومی در دسترس است.
  پروژهٔ کوبرنتیز هیچ برنامه‌ای برای حذف Ingress از کوبرنتیز ندارد.
* API مربوط به Ingress دیگر توسعه داده نمی‌شود و هیچ تغییر
  یا به‌روزرسانی دیگری در آن اعمال نخواهد شد.
{{< /note >}}

<!-- body -->


## اصطلاحات

برای روشن‌تر شدن مطلب، این راهنما اصطلاحات زیر را تعریف می‌کند:

* نود (Node): یک ماشین کارگر در کوبرنتیز که بخشی از یک کلاستر است.
* کلاستر (Cluster): مجموعه‌ای از نودها که برنامه‌های کانتینری‌شدهٔ مدیریت‌شده توسط کوبرنتیز را اجرا می‌کنند.
  در این مثال و در بیشتر استقرارهای رایج کوبرنتیز، نودهای کلاستر
  بخشی از اینترنت عمومی نیستند.
* مسیریاب لبه (Edge router): مسیریابی که سیاست دیوارهٔ آتش کلاستر شما را اعمال می‌کند. این
  می‌تواند یک gateway مدیریت‌شده توسط یک ارائه‌دهندهٔ ابری یا یک قطعه سخت‌افزار فیزیکی باشد.
* شبکهٔ کلاستر (Cluster network): مجموعه‌ای از پیوندهای منطقی یا فیزیکی که ارتباط
  درون یک کلاستر را مطابق با [مدل شبکه](/docs/concepts/cluster-administration/networking/) کوبرنتیز ممکن می‌سازند.
* سرویس (Service): یک {{< glossary_tooltip term_id="service" >}} کوبرنتیز که
  مجموعه‌ای از Podها را با استفاده از انتخابگرهای {{< glossary_tooltip text="برچسب" term_id="label" >}} شناسایی می‌کند.
  جز در مواردی که خلاف آن ذکر شود، فرض بر این است که Serviceها IPهای مجازی دارند که تنها درون شبکهٔ کلاستر قابل مسیریابی هستند.

## Ingress چیست؟

[Ingress](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#ingress-v1-networking-k8s-io)
مسیرهای HTTP و HTTPS را از بیرون کلاستر به
{{< link text="سرویس‌های" url="/docs/concepts/services-networking/service/" >}} درون کلاستر در دسترس قرار می‌دهد.
مسیریابی ترافیک با قواعدی که روی منبع Ingress تعریف می‌شوند، کنترل می‌شود.

در اینجا یک نمونهٔ ساده آمده است که در آن یک Ingress تمام ترافیک خود را به یک Service ارسال می‌کند:

{{< figure src="/docs/images/ingress.svg" alt="ingress-diagram" class="diagram-large" caption="شکل. Ingress" link="https://mermaid.live/edit#pako:eNqNkstuwyAQRX8F4U0r2VHqPlSRKqt0UamLqlnaWWAYJygYLB59KMm_Fxcix-qmGwbuXA7DwAEzzQETXKutof0Ovb4vaoUQkwKUu6pi3FwXM_QSHGBt0VFFt8DRU2OWSGrKUUMlVQwMmhVLEV1Vcm9-aUksiuXRaO_CEhkv4WjBfAgG1TrGaLa-iaUw6a0DcwGI-WgOsF7zm-pN881fvRx1UDzeiFq7ghb1kgqFWiElyTjnuXVG74FkbdumefEpuNuRu_4rZ1pqQ7L5fL6YQPaPNiFuywcG9_-ihNyUkm6YSONWkjVNM8WUIyaeOJLO3clTB_KhL8NQDmVe-OJjxgZM5FhFiiFTK5zjDkxHBQ9_4zB4a-x20EGNSZhyaKmXrg7f5hSsvufUwTMXThtMWiot5Jh6p9ffimHijIezaSVoeN0uiqcfMJvf7w" >}}

یک Ingress را می‌توان طوری پیکربندی کرد که به Serviceها URLهای قابل دسترس از بیرون بدهد،
ترافیک را توزیع بار کند، SSL / TLS را خاتمه دهد و میزبانی مجازی مبتنی بر نام ارائه کند.
یک [کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers)
مسئول تحقق بخشیدن به Ingress است که معمولاً این کار را با یک توزیع‌کنندهٔ بار انجام می‌دهد، هرچند
ممکن است مسیریاب لبه یا frontendهای اضافی شما را نیز برای کمک به رسیدگی به ترافیک پیکربندی کند.

یک Ingress پورت‌ها یا پروتکل‌های دلخواه را در دسترس قرار نمی‌دهد. در دسترس قرار دادن سرویس‌هایی غیر از HTTP و HTTPS در اینترنت معمولاً
با استفاده از سرویسی از نوع [Service.Type=NodePort](/docs/concepts/services-networking/service/#type-nodeport) یا
[Service.Type=LoadBalancer](/docs/concepts/services-networking/service/#loadbalancer) انجام می‌شود.

## پیش‌نیازها

برای تحقق بخشیدن به یک Ingress، باید یک [کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers)
داشته باشید. صرفاً ایجاد یک منبع Ingress هیچ اثری ندارد.

می‌توانید از میان چندین [کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers) انتخاب کنید.

در حالت ایدئال، همهٔ کنترل‌کننده‌های Ingress باید با مشخصات مرجع منطبق باشند. در واقعیت، کنترل‌کننده‌های Ingress
مختلف اندکی متفاوت عمل می‌کنند.

{{< note >}}
حتماً مستندات کنترل‌کنندهٔ Ingress خود را مرور کنید تا از نکات احتیاطی انتخاب آن آگاه شوید.
{{< /note >}}

## منبع Ingress

یک نمونهٔ حداقلی از منبع Ingress:

{{% code_sample file="service/networking/minimal-ingress.yaml" %}}

یک Ingress به فیلدهای `apiVersion`، `kind`، `metadata` و `spec` نیاز دارد.
نام یک آبجکت Ingress باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.
برای اطلاعات کلی دربارهٔ کار با فایل‌های پیکربندی، بخش‌های
[استقرار برنامه‌ها](/docs/tasks/run-application/run-stateless-application-deployment/)،
[پیکربندی کانتینرها](/docs/tasks/configure-pod-container/configure-pod-configmap/) و
[مدیریت منابع](/docs/concepts/workloads/management/) را ببینید.
کنترل‌کننده‌های Ingress اغلب از [حاشیه‌نویسی‌ها](/docs/concepts/overview/working-with-objects/annotations/) برای پیکربندی رفتار استفاده می‌کنند.
مستندات کنترل‌کنندهٔ ingress انتخابی خود را مرور کنید تا بدانید کدام حاشیه‌نویسی‌ها مورد انتظار و / یا پشتیبانی‌شده هستند.

[مشخصات Ingress](/docs/reference/kubernetes-api/service-resources/ingress-v1/#IngressSpec)
همهٔ اطلاعات لازم برای پیکربندی یک توزیع‌کنندهٔ بار یا سرور پراکسی را در بر دارد. مهم‌تر از همه، این مشخصات
فهرستی از قواعد را در بر دارد که با همهٔ درخواست‌های ورودی تطبیق داده می‌شوند. منبع Ingress تنها از قواعدی
برای هدایت ترافیک HTTP(S) پشتیبانی می‌کند.

اگر `ingressClassName` حذف شده باشد، باید یک [کلاس Ingress پیش‌فرض](#default-ingress-class)
تعریف شده باشد.

برخی کنترل‌کننده‌های ingress حتی بدون تعریف یک
IngressClass پیش‌فرض نیز کار می‌کنند. حتی اگر از کنترل‌کنندهٔ ingressای استفاده کنید که می‌تواند
بدون هیچ IngressClassای کار کند، پروژهٔ کوبرنتیز همچنان توصیه می‌کند
که یک IngressClass پیش‌فرض تعریف کنید.

### قواعد Ingress

هر قاعدهٔ HTTP اطلاعات زیر را در بر دارد:

* یک host اختیاری. در این مثال هیچ hostی تعیین نشده است، بنابراین قاعده بر همهٔ ترافیک HTTP ورودی
  از طریق نشانی IP تعیین‌شده اعمال می‌شود. اگر یک host ارائه شود (برای مثال
  foo.bar.com)، قواعد بر همان host اعمال می‌شوند.
* فهرستی از مسیرها (برای مثال `/testpath`) که هر یک backend مرتبطی دارد
  که با یک `service.name` و یک `service.port.name` یا
  `service.port.number` تعریف می‌شود. پیش از آنکه توزیع‌کنندهٔ بار ترافیک را به
  Service ارجاع‌شده هدایت کند، هم host و هم مسیر باید با محتوای
  درخواست ورودی مطابقت داشته باشند.
* یک backend ترکیبی از نام‌های Service و پورت است، همان‌گونه که در
  [مستندات Service](/docs/concepts/services-networking/service/) توضیح داده شده است، یا یک [backend منبع سفارشی](#resource-backend)
  از طریق یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CRD" >}}. درخواست‌های HTTP (و HTTPS) به
  Ingress که با host و مسیر قاعده مطابقت دارند، به backend فهرست‌شده ارسال می‌شوند.

یک `defaultBackend` اغلب در کنترل‌کنندهٔ Ingress پیکربندی می‌شود تا به هر درخواستی که با
هیچ مسیری در مشخصات مطابقت ندارد، رسیدگی کند.

### DefaultBackend {#default-backend}

یک Ingress بدون قاعده، همهٔ ترافیک را به یک backend پیش‌فرض واحد ارسال می‌کند و `.spec.defaultBackend`
همان backendی است که باید در این حالت به درخواست‌ها رسیدگی کند.
`defaultBackend` طبق عرف یک گزینهٔ پیکربندی در
[کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers) است و
در منابع Ingress شما تعیین نمی‌شود.
اگر هیچ `.spec.rules`ای تعیین نشده باشد، `.spec.defaultBackend` باید تعیین شود.
اگر `defaultBackend` تنظیم نشده باشد، نحوهٔ رسیدگی به درخواست‌هایی که با هیچ یک از قواعد مطابقت ندارند، بر عهدهٔ
کنترل‌کنندهٔ ingress خواهد بود (برای اطلاع از نحوهٔ رسیدگی کنترل‌کنندهٔ ingress خود به این حالت، به مستندات آن مراجعه کنید).

اگر هیچ یک از hostها یا مسیرهای موجود در آبجکت‌های Ingress با درخواست HTTP مطابقت نداشته باشند، ترافیک
به backend پیش‌فرض شما هدایت می‌شود.

### backendهای منبع {#resource-backend}

یک backend از نوع `Resource` یک ObjectRef به منبع دیگری از کوبرنتیز در
همان فضای نامِ آبجکت Ingress است. `Resource` تنظیمی است که با Service
مانعةالجمع است و اگر هر دو تعیین شوند، اعتبارسنجی با شکست مواجه می‌شود. یکی از کاربردهای
رایج backend از نوع `Resource`، هدایت داده‌های ورودی به یک backend ذخیره‌سازی آبجکت
حاوی دارایی‌های ایستا است.

{{% code_sample file="service/networking/ingress-resource-backend.yaml" %}}

پس از ایجاد Ingress بالا، می‌توانید آن را با فرمان زیر مشاهده کنید:

```bash
kubectl describe ingress ingress-resource-backend
```

```
Name:             ingress-resource-backend
Namespace:        default
Address:
Default backend:  APIGroup: k8s.example.com, Kind: StorageBucket, Name: static-assets
Rules:
  Host        Path  Backends
  ----        ----  --------
  *
              /icons   APIGroup: k8s.example.com, Kind: StorageBucket, Name: icon-assets
Annotations:  <none>
Events:       <none>
```

### انواع مسیر

هر مسیر در یک Ingress باید نوع مسیر متناظری داشته باشد. مسیرهایی
که `pathType` صریحی ندارند، در اعتبارسنجی رد می‌شوند. سه
نوع مسیر پشتیبانی‌شده وجود دارد:

* `ImplementationSpecific`: با این نوع مسیر، نحوهٔ تطبیق بر عهدهٔ
  IngressClass است. پیاده‌سازی‌ها می‌توانند این را یک `pathType` جداگانه در نظر بگیرند یا
  با آن دقیقاً مانند انواع مسیر `Prefix` یا `Exact` رفتار کنند.

* `Exact`: با مسیر URL به‌طور دقیق و با حساسیت به بزرگی و کوچکی حروف تطبیق می‌دهد.

* `Prefix`: بر اساس پیشوند مسیر URL که با `/` تقسیم شده است، تطبیق می‌دهد. تطبیق به بزرگی و کوچکی حروف
  حساس است و عنصر به عنصر روی مسیر انجام می‌شود. منظور از عنصر مسیر،
  فهرست برچسب‌هایی است که از تقسیم مسیر با جداکنندهٔ `/` به دست می‌آیند. یک درخواست
  با مسیر _p_ مطابقت دارد، اگر هر _p_ پیشوندی عنصر به عنصر از _p_ در
  مسیر درخواست باشد.

  {{< note >}}
  اگر آخرین عنصر مسیر زیررشته‌ای از آخرین
  عنصر مسیر درخواست باشد، تطبیقی وجود ندارد (برای مثال: `/foo/bar`
  با `/foo/bar/baz` مطابقت دارد، اما با `/foo/barbaz` مطابقت ندارد).
  {{< /note >}}

### نمونه‌ها

| نوع   | مسیر(ها)                         | مسیر(های) درخواست               | مطابقت دارد؟                           |
|--------|---------------------------------|-------------------------------|------------------------------------|
| Prefix | `/`                             | (همهٔ مسیرها)                   | بله                                |
| Exact  | `/foo`                          | `/foo`                        | بله                                |
| Exact  | `/foo`                          | `/bar`                        | خیر                                 |
| Exact  | `/foo`                          | `/foo/`                       | خیر                                 |
| Exact  | `/foo/`                         | `/foo`                        | خیر                                 |
| Prefix | `/foo`                          | `/foo`, `/foo/`               | بله                                |
| Prefix | `/foo/`                         | `/foo`, `/foo/`               | بله                                |
| Prefix | `/aaa/bb`                       | `/aaa/bbb`                    | خیر                                 |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb`                    | بله                                |
| Prefix | `/aaa/bbb/`                     | `/aaa/bbb`                    | بله، اسلش پایانی را نادیده می‌گیرد        |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb/`                   | بله، با اسلش پایانی مطابقت دارد       |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb/ccc`                | بله، با زیرمسیر مطابقت دارد               |
| Prefix | `/aaa/bbb`                      | `/aaa/bbbxyz`                 | خیر، با پیشوند رشته‌ای مطابقت ندارد   |
| Prefix | `/`, `/aaa`                     | `/aaa/ccc`                    | بله، با پیشوند `/aaa` مطابقت دارد         |
| Prefix | `/`, `/aaa`, `/aaa/bbb`         | `/aaa/bbb`                    | بله، با پیشوند `/aaa/bbb` مطابقت دارد     |
| Prefix | `/`, `/aaa`, `/aaa/bbb`         | `/ccc`                        | بله، با پیشوند `/` مطابقت دارد            |
| Prefix | `/aaa`                          | `/ccc`                        | خیر، از backend پیش‌فرض استفاده می‌کند           |
| ترکیبی  | `/foo` (Prefix), `/foo` (Exact) | `/foo`                        | بله، Exact را ترجیح می‌دهد                 |

#### چند تطبیق هم‌زمان

در برخی موارد، چند مسیر درون یک Ingress با یک درخواست مطابقت دارند. در این
موارد، اولویت ابتدا به طولانی‌ترین مسیر منطبق داده می‌شود. اگر دو مسیر
همچنان به یک اندازه منطبق باشند، اولویت به مسیرهایی با نوع مسیر exact
نسبت به نوع مسیر prefix داده می‌شود.

## Wildcardهای hostname

hostها می‌توانند تطبیق‌های دقیق (برای مثال «`foo.bar.com`») یا wildcard (برای
مثال «`*.foo.com`») باشند. تطبیق‌های دقیق مستلزم آن‌اند که هدر `host` در HTTP
با فیلد `host` مطابقت داشته باشد. تطبیق‌های wildcard مستلزم آن‌اند که هدر `host` در HTTP
با پسوند قاعدهٔ wildcard برابر باشد.

| Host        | هدر Host       | مطابقت دارد؟                                            |
| ----------- |-------------------| --------------------------------------------------|
| `*.foo.com` | `bar.foo.com`     | بر اساس پسوند مشترک مطابقت دارد                    |
| `*.foo.com` | `baz.bar.foo.com` | مطابقت ندارد؛ wildcard تنها یک برچسب DNS را پوشش می‌دهد |
| `*.foo.com` | `foo.com`         | مطابقت ندارد؛ wildcard تنها یک برچسب DNS را پوشش می‌دهد |

{{% code_sample file="service/networking/ingress-wildcard-host.yaml" %}}

## کلاس Ingress

Ingressها را می‌توان با کنترل‌کننده‌های مختلف و اغلب با پیکربندی‌های متفاوت
پیاده‌سازی کرد. هر Ingress باید یک کلاس تعیین کند؛ یعنی ارجاعی به یک
منبع IngressClass که پیکربندی اضافی، از جمله نام
کنترل‌کننده‌ای را که باید این کلاس را پیاده‌سازی کند، در بر دارد.

{{% code_sample file="service/networking/external-lb.yaml" %}}

فیلد `.spec.parameters` در یک IngressClass به شما امکان می‌دهد به منبع دیگری
ارجاع دهید که پیکربندی مرتبط با آن IngressClass را فراهم می‌کند.

نوع مشخص پارامترهایی که باید استفاده شود، به کنترل‌کنندهٔ ingressای بستگی دارد
که در فیلد `.spec.controller` در IngressClass تعیین می‌کنید.

### دامنهٔ IngressClass

بسته به کنترل‌کنندهٔ ingress شما، ممکن است بتوانید از پارامترهایی استفاده کنید
که در سطح کل کلاستر یا تنها برای یک فضای نام تنظیم می‌کنید.

{{< tabs name="tabs_ingressclass_parameter_scope" >}}
{{% tab name="کلاستر" %}}
دامنهٔ پیش‌فرض برای پارامترهای IngressClass، کل کلاستر است.

اگر فیلد `.spec.parameters` را تنظیم کنید و `.spec.parameters.scope` را تنظیم نکنید،
یا اگر `.spec.parameters.scope` را روی
`Cluster` تنظیم کنید، آنگاه IngressClass به یک منبع با دامنهٔ کلاستر ارجاع می‌دهد.
`kind` (در ترکیب با `apiGroup`) پارامترها
به یک API با دامنهٔ کلاستر (احتمالاً یک منبع سفارشی) اشاره دارد و
`name` پارامترها یک منبع مشخص با دامنهٔ کلاستر را
برای آن API شناسایی می‌کند.

برای مثال:

```yaml
---
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-1
spec:
  controller: example.com/ingress-controller
  parameters:
    # The parameters for this IngressClass are specified in a
    # ClusterIngressParameter (API group k8s.example.net) named
    # "external-config-1". This definition tells Kubernetes to
    # look for a cluster-scoped parameter resource.
    scope: Cluster
    apiGroup: k8s.example.net
    kind: ClusterIngressParameter
    name: external-config-1
```

{{% /tab %}}
{{% tab name="فضای نام" %}}
{{< feature-state for_k8s_version="v1.23" state="stable" >}}

اگر فیلد `.spec.parameters` را تنظیم کنید و
`.spec.parameters.scope` را روی `Namespace` تنظیم کنید، آنگاه IngressClass به
یک منبع با دامنهٔ فضای نام ارجاع می‌دهد. همچنین باید فیلد `namespace`
درون `.spec.parameters` را روی فضای نامی تنظیم کنید که
پارامترهای مورد نظر شما را در بر دارد.

`kind` (در ترکیب با `apiGroup`) پارامترها
به یک API با دامنهٔ فضای نام (برای مثال: ConfigMap) اشاره دارد و
`name` پارامترها یک منبع مشخص را
در فضای نامی که در `namespace` تعیین کرده‌اید، شناسایی می‌کند.

پارامترهای با دامنهٔ فضای نام به اپراتور کلاستر کمک می‌کنند کنترل بر
پیکربندی‌ای را که برای یک بار کاری استفاده می‌شود (برای مثال: تنظیمات توزیع‌کنندهٔ بار، تعریف API gateway)
واگذار کند. اگر از یک پارامتر با دامنهٔ کلاستر استفاده می‌کردید، آنگاه یا:

- تیم اپراتور کلاستر باید هر بار که یک تغییر پیکربندی جدید اعمال می‌شود،
  تغییرات تیم دیگری را تأیید کند؛
- یا اپراتور کلاستر باید کنترل‌های دسترسی مشخصی، مانند
  نقش‌ها و اتصال‌های (bindings) [RBAC](/docs/reference/access-authn-authz/rbac/)، تعریف کند که به
  تیم برنامه اجازه دهد در منبع پارامترهای با دامنهٔ کلاستر تغییر ایجاد کند.

خود API مربوط به IngressClass همواره دامنهٔ کلاستر دارد.

در اینجا نمونه‌ای از یک IngressClass آمده است که به پارامترهایی با دامنهٔ فضای نام
ارجاع می‌دهد:

```yaml
---
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-2
spec:
  controller: example.com/ingress-controller
  parameters:
    # The parameters for this IngressClass are specified in an
    # IngressParameter (API group k8s.example.com) named "external-config",
    # that's in the "external-configuration" namespace.
    scope: Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter
    namespace: external-configuration
    name: external-config
```

{{% /tab %}}
{{< /tabs >}}

### حاشیه‌نویسی منسوخ‌شده

پیش از آنکه منبع IngressClass و فیلد `ingressClassName` در
کوبرنتیز 1.18 افزوده شوند، کلاس‌های Ingress با یک
حاشیه‌نویسی `kubernetes.io/ingress.class` روی Ingress تعیین می‌شدند. این حاشیه‌نویسی
هرگز به‌طور رسمی تعریف نشد، اما کنترل‌کننده‌های Ingress به‌طور گسترده از آن پشتیبانی می‌کردند.

فیلد جدیدتر `ingressClassName` روی Ingressها جایگزین آن
حاشیه‌نویسی است، اما معادل مستقیم آن نیست. در حالی که حاشیه‌نویسی معمولاً
برای ارجاع به نام کنترل‌کنندهٔ Ingressای به کار می‌رفت که باید Ingress را پیاده‌سازی کند،
این فیلد ارجاعی به یک منبع IngressClass است که پیکربندی اضافی
Ingress، از جمله نام کنترل‌کنندهٔ Ingress، را در بر دارد.

### IngressClass پیش‌فرض {#default-ingress-class}

می‌توانید یک IngressClass مشخص را به‌عنوان پیش‌فرض کلاستر خود علامت‌گذاری کنید. تنظیم
حاشیه‌نویسی `ingressclass.kubernetes.io/is-default-class` روی `true` در یک
منبع IngressClass تضمین می‌کند که این IngressClass پیش‌فرض به Ingressهای جدیدی که
فیلد `ingressClassName` برای آن‌ها تعیین نشده است، اختصاص داده شود.

{{< caution >}}
اگر بیش از یک IngressClass به‌عنوان پیش‌فرض کلاستر شما علامت‌گذاری شده باشد،
کنترل‌کنندهٔ admission از ایجاد آبجکت‌های Ingress جدیدی که
`ingressClassName` برای آن‌ها تعیین نشده است، جلوگیری می‌کند. می‌توانید با اطمینان از اینکه حداکثر ۱
IngressClass در کلاستر شما به‌عنوان پیش‌فرض علامت‌گذاری شده است، این مشکل را برطرف کنید.
{{< /caution >}}

کار را با تعریف یک
IngressClass پیش‌فرض آغاز کنید. با این حال، توصیه می‌شود IngressClass
پیش‌فرض را تعیین کنید:

{{% code_sample file="service/networking/default-ingressclass.yaml" %}}

## انواع Ingress

### Ingress با پشتوانهٔ یک Service واحد {#single-service-ingress}

مفاهیمی در کوبرنتیز وجود دارند که به شما امکان می‌دهند یک Service واحد را در دسترس قرار دهید
([جایگزین‌ها](#alternatives) را ببینید). همچنین می‌توانید این کار را با یک Ingress و با تعیین یک
*backend پیش‌فرض* بدون هیچ قاعده‌ای انجام دهید.

{{% code_sample file="service/networking/test-ingress.yaml" %}}

اگر آن را با استفاده از `kubectl apply -f` ایجاد کنید، باید بتوانید وضعیت
Ingressی را که افزوده‌اید مشاهده کنید:

```bash
kubectl get ingress test-ingress
```

```
NAME           CLASS         HOSTS   ADDRESS         PORTS   AGE
test-ingress   external-lb   *       203.0.113.123   80      59s
```

که در آن `203.0.113.123` همان IPای است که کنترل‌کنندهٔ Ingress برای تحقق بخشیدن به
این Ingress تخصیص داده است.

{{< note >}}
ممکن است تخصیص یک نشانی IP توسط کنترل‌کننده‌های Ingress و توزیع‌کننده‌های بار یکی دو دقیقه طول بکشد.
تا آن زمان، اغلب نشانی را به‌صورت `<pending>` فهرست‌شده می‌بینید.
{{< /note >}}

### انشعاب ساده (Simple fanout)

پیکربندی fanout ترافیک را بر اساس URI درخواستی HTTP، از یک نشانی IP واحد به بیش از یک Service
هدایت می‌کند. یک Ingress به شما امکان می‌دهد تعداد توزیع‌کننده‌های بار را
در حداقل نگه دارید. برای مثال، چیدمانی مانند:

{{< figure src="/docs/images/ingressFanOut.svg" alt="ingress-fanout-diagram" class="diagram-large" caption="شکل. انشعاب Ingress (Fan Out)" link="https://mermaid.live/edit#pako:eNqNUslOwzAQ_RXLvYCUhMQpUFzUUzkgcUBwbHpw4klr4diR7bCo8O8k2FFbFomLPZq3jP00O1xpDpjijWHtFt09zAuFUCUFKHey8vf6NE7QrdoYsDZumGIb4Oi6NAskNeOoZJKpCgxK4oXwrFVgRyi7nCVXWZKRPMlysv5yD6Q4Xryf1Vq_WzDPooJs9egLNDbolKTpT03JzKgh3zWEztJZ0Niu9L-qZGcdmAMfj4cxvWmreba613z9C0B-AMQD-V_AdA-A4j5QZu0SatRKJhSqhZR0wjmPrDP6CeikrutQxy-Cuy2dtq9RpaU2dJKm6fzI5Glmg0VOLio4_5dLjx27hFSC015KJ2VZHtuQvY2fuHcaE43G0MaCREOow_FV5cMxHZ5-oPX75UM5avuXhXuOI9yAaZjg_aLuBl6B3RYaKDDtSw4166QrcKE-emrXcubghgunDaY1kxYizDqnH99UhakzHYykpWD9hjS--fEJoIELqQ" >}}

به Ingressی مانند زیر نیاز دارد:

{{% code_sample file="service/networking/simple-fanout-example.yaml" %}}

هنگامی که Ingress را با `kubectl apply -f` ایجاد می‌کنید:

```shell
kubectl describe ingress simple-fanout-example
```

```
Name:             simple-fanout-example
Namespace:        default
Address:          178.91.123.132
Default backend:  default-http-backend:80 (10.8.2.3:8080)
Rules:
  Host         Path  Backends
  ----         ----  --------
  foo.bar.com
               /foo   service1:4200 (10.8.0.90:4200)
               /bar   service2:8080 (10.8.0.91:8080)
Events:
  Type     Reason  Age                From                     Message
  ----     ------  ----               ----                     -------
  Normal   ADD     22s                loadbalancer-controller  default/test
```

تا زمانی که Serviceها (`service1`، `service2`) وجود داشته باشند، کنترل‌کنندهٔ Ingress
یک توزیع‌کنندهٔ بارِ مختص پیاده‌سازی فراهم می‌کند که Ingress را تحقق می‌بخشد.
پس از انجام این کار، می‌توانید نشانی توزیع‌کنندهٔ بار را در
فیلد Address ببینید.

{{< note >}}
بسته به [کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers/)ای
که استفاده می‌کنید، ممکن است لازم باشد یک
[Service](/docs/concepts/services-networking/service/) به نام default-http-backend ایجاد کنید.
{{< /note >}}

### میزبانی مجازی مبتنی بر نام

میزبان‌های مجازی مبتنی بر نام از مسیریابی ترافیک HTTP به چند نام host روی یک نشانی IP یکسان پشتیبانی می‌کنند.

{{< figure src="/docs/images/ingressNameBased.svg" alt="ingress-namebase-diagram" class="diagram-large" caption="شکل. میزبانی مجازی مبتنی بر نام در Ingress" link="https://mermaid.live/edit#pako:eNqNkl9PwyAUxb8KYS-atM1Kp05m9qSJJj4Y97jugcLtRqTQAPVPdN_dVlq3qUt8gZt7zvkBN7xjbgRgiteW1Rt0_zjLNUJcSdD-ZBn21WmcoDu9tuBcXDHN1iDQVWHnSBkmUMEU0xwsSuK5DK5l745QejFNLtMkJVmSZmT1Re9NcTz_uDXOU1QakxTMJtxUHw7ss-SQLhehQEODTsdH4l20Q-zFyc84-Y67pghv5apxHuweMuj9eS2_NiJdPhix-kMgvwQShOyYMNkJoEUYM3PuGkpUKyY1KqVSdCSEiJy35gnoqCzLvo5fpPAbOqlfI26UsXQ0Ho9nB5CnqesRGTnncPYvSqsdUvqp9KRdlI6KojjEkB0mnLgjDRONhqENBYm6oXbLV5V1y6S7-l42_LowlIN2uFm_twqOcAW2YlK0H_i9c-bYb6CCHNO2FFCyRvkc53rbWptaMA83QnpjMS2ZchBh1nizeNMcU28bGEzXkrV_pArN7Sc0rBTu" >}}

Ingress زیر به توزیع‌کنندهٔ بار پشتیبان می‌گوید که درخواست‌ها را بر اساس
[هدر Host](https://tools.ietf.org/html/rfc7230#section-5.4) مسیریابی کند.

{{% code_sample file="service/networking/name-virtual-host-ingress.yaml" %}}

اگر یک منبع Ingress بدون تعریف هیچ hostی در قواعد ایجاد کنید، آنگاه هر
ترافیک وبی به نشانی IP کنترل‌کنندهٔ Ingress شما می‌تواند بدون نیاز به
میزبان مجازی مبتنی بر نام تطبیق داده شود.

برای مثال، Ingress زیر ترافیک
درخواستی برای `first.bar.com` را به `service1`، ترافیک `second.bar.com` را به `service2`
و هر ترافیکی را که هدر host درخواست آن با `first.bar.com`
و `second.bar.com` مطابقت ندارد، به `service3` هدایت می‌کند.

{{% code_sample file="service/networking/name-virtual-host-ingress-no-third-host.yaml" %}}

### TLS

می‌توانید با تعیین یک {{< glossary_tooltip term_id="secret" >}}
که یک کلید خصوصی و گواهی TLS را در بر دارد، یک Ingress را امن کنید. منبع Ingress تنها
از یک پورت TLS واحد، یعنی 443، پشتیبانی می‌کند و فرض می‌کند خاتمهٔ TLS در نقطهٔ ingress انجام می‌شود
(ترافیک به Service و Podهای آن به‌صورت متن ساده است).
اگر بخش پیکربندی TLS در یک Ingress hostهای متفاوتی را تعیین کند، این hostها
بر اساس hostnameی که از طریق افزونهٔ SNI در TLS تعیین می‌شود، روی همان پورت multiplex می‌شوند
(به شرط آنکه کنترل‌کنندهٔ Ingress از SNI پشتیبانی کند). Secret مربوط به TLS
باید کلیدهایی با نام‌های `tls.crt` و `tls.key` داشته باشد که گواهی
و کلید خصوصی مورد استفاده برای TLS را در بر دارند. برای مثال:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: testsecret-tls
  namespace: default
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
type: kubernetes.io/tls
```

ارجاع به این Secret در یک Ingress به کنترل‌کنندهٔ Ingress می‌گوید که
کانال میان کلاینت و توزیع‌کنندهٔ بار را با استفاده از TLS امن کند. باید اطمینان
حاصل کنید که Secret مربوط به TLS که ایجاد کرده‌اید، از گواهی‌ای به دست آمده است که یک Common
Name (CN)، که با نام Fully Qualified Domain Name (FQDN) نیز شناخته می‌شود، برای `https-example.foo.com` در بر دارد.

{{< note >}}
به خاطر داشته باشید که TLS روی قاعدهٔ پیش‌فرض کار نخواهد کرد، زیرا
گواهی‌ها باید برای همهٔ زیردامنه‌های ممکن صادر شوند. بنابراین،
`hosts` در بخش `tls` باید صراحتاً با `host` در بخش `rules`
مطابقت داشته باشد.
{{< /note >}}

{{% code_sample file="service/networking/tls-example-ingress.yaml" %}}

{{< note >}}
میان قابلیت‌های TLS که کنترل‌کننده‌های ingress مختلف پشتیبانی می‌کنند، تفاوت‌هایی وجود دارد.
برای درک نحوهٔ کارکرد TLS در محیط خود، باید به مستندات کنترل‌کننده(های) ingress انتخابی خود
مراجعه کنید.
{{< /note >}}

### توزیع بار {#load-balancing}

یک کنترل‌کنندهٔ Ingress با برخی تنظیمات سیاست توزیع بار راه‌اندازی می‌شود
که آن‌ها را بر همهٔ Ingressها اعمال می‌کند، مانند الگوریتم توزیع بار، طرح وزن‌دهی
backendها و موارد دیگر. مفاهیم پیشرفته‌تر توزیع بار
(مانند نشست‌های پایدار یا وزن‌های پویا) هنوز از طریق
Ingress در دسترس قرار نگرفته‌اند. در عوض می‌توانید این قابلیت‌ها را از طریق توزیع‌کنندهٔ باری که برای
یک Service استفاده می‌شود، به دست آورید.

همچنین شایان ذکر است که اگرچه بررسی‌های سلامت (health checks) مستقیماً
از طریق Ingress در دسترس قرار نگرفته‌اند، مفاهیم موازی‌ای در کوبرنتیز وجود دارند، مانند
[readiness probeها](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)،
که به شما امکان می‌دهند به همان نتیجهٔ نهایی برسید. لطفاً مستندات مختص
کنترل‌کننده را مرور کنید تا ببینید آن‌ها چگونه به بررسی‌های سلامت رسیدگی می‌کنند.

## به‌روزرسانی یک Ingress

برای به‌روزرسانی یک Ingress موجود به‌منظور افزودن یک Host جدید، می‌توانید منبع را ویرایش کنید:

```shell
kubectl describe ingress test
```

```
Name:             test
Namespace:        default
Address:          178.91.123.132
Default backend:  default-http-backend:80 (10.8.2.3:8080)
Rules:
  Host         Path  Backends
  ----         ----  --------
  foo.bar.com
               /foo   service1:80 (10.8.0.90:80)
Events:
  Type     Reason  Age                From                     Message
  ----     ------  ----               ----                     -------
  Normal   ADD     35s                loadbalancer-controller  default/test
```

```shell
kubectl edit ingress test
```

این فرمان یک ویرایشگر با پیکربندی موجود در قالب YAML باز می‌کند.
آن را طوری تغییر دهید که Host جدید را در بر بگیرد:

```yaml
spec:
  rules:
  - host: foo.bar.com
    http:
      paths:
      - backend:
          service:
            name: service1
            port:
              number: 80
        path: /foo
        pathType: Prefix
  - host: bar.baz.com
    http:
      paths:
      - backend:
          service:
            name: service2
            port:
              number: 80
        path: /foo
        pathType: Prefix
..
```

پس از ذخیرهٔ تغییرات، kubectl منبع را در API server به‌روزرسانی می‌کند و این کار به
کنترل‌کنندهٔ Ingress می‌گوید توزیع‌کنندهٔ بار را دوباره پیکربندی کند.

این موضوع را تأیید کنید:

```shell
kubectl describe ingress test
```

```
Name:             test
Namespace:        default
Address:          178.91.123.132
Default backend:  default-http-backend:80 (10.8.2.3:8080)
Rules:
  Host         Path  Backends
  ----         ----  --------
  foo.bar.com
               /foo   service1:80 (10.8.0.90:80)
  bar.baz.com
               /foo   service2:80 (10.8.0.91:80)
Events:
  Type     Reason  Age                From                     Message
  ----     ------  ----               ----                     -------
  Normal   ADD     45s                loadbalancer-controller  default/test
```

می‌توانید با اجرای `kubectl replace -f` روی یک فایل YAML تغییریافتهٔ Ingress نیز به همین نتیجه برسید.

## تحمل خرابی در میان ناحیه‌های دسترس‌پذیری

روش‌های پخش ترافیک در میان دامنه‌های خرابی (failure domains) در ارائه‌دهندگان ابری مختلف متفاوت است.
لطفاً برای جزئیات، مستندات [کنترل‌کنندهٔ Ingress](/docs/concepts/services-networking/ingress-controllers) مربوط را بررسی کنید.

## جایگزین‌ها

می‌توانید یک Service را به روش‌های متعددی در دسترس قرار دهید که مستقیماً به منبع Ingress مربوط نیستند:

* از [Service.Type=LoadBalancer](/docs/concepts/services-networking/service/#loadbalancer) استفاده کنید
* از [Service.Type=NodePort](/docs/concepts/services-networking/service/#type-nodeport) استفاده کنید

## {{% heading "whatsnext" %}}

* دربارهٔ API مربوط به [Ingress](/docs/reference/kubernetes-api/service-resources/ingress-v1/) بیاموزید
* دربارهٔ [کنترل‌کننده‌های Ingress](/docs/concepts/services-networking/ingress-controllers/) بیاموزید

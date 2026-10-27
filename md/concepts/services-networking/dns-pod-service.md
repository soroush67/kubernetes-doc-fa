---
reviewers:
- jbelamaric
- bowei
- thockin
title: DNS برای Serviceها و Podها
content_type: concept
weight: 80
description: >-
  بار کاری شما می‌تواند Serviceهای درون کلاستر را با استفاده از DNS کشف کند؛
  این صفحه توضیح می‌دهد که این کار چگونه انجام می‌شود.
---
<!-- overview -->

کوبرنتیز برای Serviceها و Podها رکوردهای DNS ایجاد می‌کند. شما می‌توانید به‌جای نشانی‌های IP،
با استفاده از نام‌های DNS ثابت با Serviceها ارتباط برقرار کنید.

<!-- body -->

کوبرنتیز اطلاعاتی دربارهٔ Podها و Serviceها منتشر می‌کند که برای
برنامه‌ریزی DNS به کار می‌رود. kubelet تنظیمات DNS مربوط به Podها را پیکربندی می‌کند تا کانتینرهای در حال اجرا
بتوانند Serviceها را به‌جای IP با نام جست‌وجو کنند.

به Serviceهایی که در کلاستر تعریف می‌شوند، نام‌های DNS اختصاص داده می‌شود. به‌طور پیش‌فرض،
فهرست جست‌وجوی DNS یک Pod کلاینت شامل فضای نام (namespace) خود Pod و
دامنهٔ پیش‌فرض کلاستر است.

### فضاهای نام Serviceها

یک پرس‌وجوی DNS ممکن است بسته به فضای نام Podی که آن را ارسال می‌کند، نتایج متفاوتی
برگرداند. پرس‌وجوهای DNS که فضای نامی را مشخص نمی‌کنند، به فضای نام خود Pod
محدود می‌شوند. برای دسترسی به Serviceهای موجود در فضاهای نام دیگر، فضای نام را در پرس‌وجوی DNS مشخص کنید.

برای مثال، Podی را در فضای نام `test` در نظر بگیرید. یک Service به نام `data` در
فضای نام `prod` قرار دارد.

پرس‌وجو برای `data` هیچ نتیجه‌ای برنمی‌گرداند، زیرا از فضای نام `test` مربوط به Pod استفاده می‌کند.

پرس‌وجو برای `data.prod` نتیجهٔ مورد نظر را برمی‌گرداند، زیرا
فضای نام را مشخص می‌کند.

پرس‌وجوهای DNS ممکن است با استفاده از فایل `/etc/resolv.conf` مربوط به Pod گسترش یابند. kubelet
این فایل را برای هر Pod پیکربندی می‌کند. برای مثال، پرس‌وجو برای تنها `data` ممکن است به
`data.test.svc.cluster.local` گسترش یابد. مقادیر گزینهٔ `search`
برای گسترش پرس‌وجوها به کار می‌روند. برای آشنایی بیشتر با پرس‌وجوهای DNS،
[صفحهٔ راهنمای `resolv.conf`](https://www.man7.org/linux/man-pages/man5/resolv.conf.5.html) را ببینید.

```
nameserver 10.32.0.10
search <namespace>.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```

به‌طور خلاصه، یک Pod در فضای نام _test_ می‌تواند هر یک از نام‌های
`data.prod` یا `data.prod.svc.cluster.local` را با موفقیت resolve کند.

### رکوردهای DNS

چه آبجکت‌هایی رکورد DNS دریافت می‌کنند؟

1. Serviceها
1. Podها

بخش‌های زیر انواع رکوردهای DNS پشتیبانی‌شده و ساختار پشتیبانی‌شده را
به‌تفصیل شرح می‌دهند. هر ساختار، نام یا پرس‌وجوی دیگری که به‌طور اتفاقی کار کند،
جزئیات پیاده‌سازی محسوب می‌شود و ممکن است بدون هشدار تغییر کند.
برای مشخصات به‌روزتر، به
[کشف سرویس مبتنی بر DNS در کوبرنتیز](https://github.com/kubernetes/dns/blob/master/docs/specification.md) مراجعه کنید.

## Serviceها

### رکوردهای A/AAAA

به Serviceهای «عادی» (غیر headless)، بسته به خانواده یا خانواده‌های IP مربوط به Service،
رکوردهای DNS از نوع A و/یا AAAA با نامی به شکل
`my-svc.my-namespace.svc.cluster-domain.example` اختصاص داده می‌شود. این نام به cluster IP
مربوط به Service resolve می‌شود.

به [Serviceهای headless](/docs/concepts/services-networking/service/#headless-services)
(بدون cluster IP) نیز رکوردهای DNS از نوع A و/یا AAAA
با نامی به شکل `my-svc.my-namespace.svc.cluster-domain.example` اختصاص داده می‌شود. برخلاف
Serviceهای عادی، این نام به مجموعهٔ IPهای همهٔ Podهایی که Service انتخاب کرده است، resolve می‌شود.
انتظار می‌رود کلاینت‌ها از کل این مجموعه استفاده کنند یا در غیر این صورت، به‌روش استاندارد round-robin
از میان این مجموعه انتخاب کنند.

### رکوردهای SRV

رکوردهای SRV برای پورت‌های نام‌داری ایجاد می‌شوند که بخشی از Serviceهای عادی یا
headless هستند.

- برای هر پورت نام‌دار، رکورد SRV به شکل
  `_port-name._port-protocol.my-svc.my-namespace.svc.cluster-domain.example` است.
- برای یک Service معمولی، این رکورد به شمارهٔ پورت و نام دامنهٔ
  `my-svc.my-namespace.svc.cluster-domain.example` resolve می‌شود.
- برای یک Service از نوع headless، این رکورد به چند پاسخ resolve می‌شود؛ یک پاسخ برای هر Pod
  که پشتیبان Service است. هر پاسخ شامل شمارهٔ پورت و نام دامنهٔ Pod
  به شکل `hostname.my-svc.my-namespace.svc.cluster-domain.example` است.

## Podها

### رکوردهای A/AAAA

نسخه‌های Kube-DNS، پیش از پیاده‌سازی
[مشخصات DNS](https://github.com/kubernetes/dns/blob/master/docs/specification.md)،
شیوهٔ resolve کردن DNS زیر را داشتند:

```
<pod-IPv4-address>.<namespace>.pod.<cluster-domain>
```

برای مثال، اگر یک Pod در فضای نام `default` نشانی IP ‏172.17.0.3 داشته باشد
و نام دامنهٔ کلاستر شما `cluster.local` باشد، آنگاه Pod این نام DNS را دارد:

```
172-17-0-3.default.pod.cluster.local
```

برخی سازوکارهای DNS کلاستر، مانند [CoreDNS](https://coredns.io/)، رکوردهای `A` را برای الگوی زیر نیز فراهم می‌کنند:

```
<pod-ipv4-address>.<service-name>.<my-namespace>.svc.<cluster-domain.example>
```

برای مثال، اگر یک Pod در فضای نام `cafe` نشانی IP ‏172.17.0.3 داشته باشد،
یک endpoint از Serviceای به نام `barista` باشد و نام دامنهٔ کلاستر شما
`cluster.local` باشد، آنگاه Pod این رکورد DNS از نوع `A` را در دامنهٔ Service خواهد داشت.

```
172-17-0-3.barista.cafe.svc.cluster.local
```

### فیلدهای hostname و subdomain در Pod {#pod-hostname-and-subdomain-field}

در حال حاضر، هنگامی که یک Pod ایجاد می‌شود، hostname آن (آن‌گونه که از درون Pod دیده می‌شود)
همان مقدار `metadata.name` مربوط به Pod است.

مشخصات (spec) Pod یک فیلد اختیاری `hostname` دارد که می‌توان از آن برای تعیین
hostname متفاوتی استفاده کرد. در صورت تعیین شدن، این فیلد بر نام Pod اولویت دارد و
hostname آن Pod می‌شود (باز هم، آن‌گونه که از درون Pod دیده می‌شود). برای مثال،
اگر `spec.hostname` یک Pod روی `"my-host"` تنظیم شده باشد، hostname آن Pod
`"my-host"` خواهد بود.

مشخصات Pod همچنین یک فیلد اختیاری `subdomain` دارد که می‌توان از آن برای نشان دادن
اینکه Pod بخشی از یک زیرگروه از فضای نام است، استفاده کرد. برای مثال، Podی که `spec.hostname`
آن روی `"foo"` و `spec.subdomain` آن روی `"bar"` تنظیم شده و در فضای نام `"my-namespace"` قرار دارد،
hostname برابر با `"foo"` و نام دامنهٔ کاملاً مشخص (FQDN) برابر با
`"foo.bar.my-namespace.svc.cluster.local"` خواهد داشت (باز هم، آن‌گونه که از درون
Pod دیده می‌شود).

اگر در همان فضای نامِ Pod، یک Service از نوع headless با
نامی برابر با subdomain وجود داشته باشد، سرور DNS کلاستر برای hostname کاملاً مشخص Pod
نیز رکوردهای A و/یا AAAA برمی‌گرداند.

مثال:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: busybox-subdomain
spec:
  selector:
    name: busybox
  clusterIP: None
  ports:
  - name: foo # name is not required for single-port Services
    port: 1234
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox1
  labels:
    name: busybox
spec:
  hostname: busybox-1
  subdomain: busybox-subdomain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox2
  labels:
    name: busybox
spec:
  hostname: busybox-2
  subdomain: busybox-subdomain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```

با وجود Service بالا با نام `"busybox-subdomain"` و Podهایی که `spec.subdomain` را
روی `"busybox-subdomain"` تنظیم کرده‌اند، Pod نخست FQDN خود را به‌صورت
`"busybox-1.busybox-subdomain.my-namespace.svc.cluster-domain.example"` خواهد دید. DNS
در این نام رکوردهای A و/یا AAAA ارائه می‌کند که به IP مربوط به Pod اشاره دارند. هر دو Pod ‏«`busybox1`» و
«`busybox2`» رکوردهای نشانی مخصوص به خود را خواهند داشت.

یک {{<glossary_tooltip term_id="endpoint-slice" text="EndpointSlice">}} می‌تواند
hostname مربوط به DNS را برای هر نشانی endpoint، همراه با IP آن، مشخص کند.

{{< note >}}
رکوردهای A و AAAA برای نام Podها ایجاد نمی‌شوند، زیرا `hostname` برای Pod تعیین نشده است.
Podی که `hostname` ندارد اما `subdomain` دارد، تنها رکورد
A یا AAAA را برای Service از نوع headless (`busybox-subdomain.my-namespace.svc.cluster-domain.example`) ایجاد می‌کند
که به نشانی‌های IP مربوط به Podها اشاره دارد. همچنین Pod برای داشتن رکورد باید آماده (ready)
باشد، مگر اینکه `publishNotReadyAddresses=True` روی Service تنظیم شده باشد.
{{< /note >}}

### فیلد setHostnameAsFQDN در Pod {#pod-sethostnameasfqdn-field}

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

هنگامی که یک Pod طوری پیکربندی شده باشد که نام دامنهٔ کاملاً مشخص (FQDN) داشته باشد،
hostname آن همان hostname کوتاه است. برای مثال، اگر Podی با نام دامنهٔ کاملاً مشخص
`busybox-1.busybox-subdomain.my-namespace.svc.cluster-domain.example` داشته باشید،
به‌طور پیش‌فرض فرمان `hostname` درون آن Pod مقدار `busybox-1` را برمی‌گرداند و
فرمان `hostname --fqdn` مقدار FQDN را برمی‌گرداند.

هنگامی که `setHostnameAsFQDN: true` را در مشخصات Pod تنظیم می‌کنید، kubelet مقدار FQDN مربوط به Pod
را به‌عنوان hostname در فضای نام (namespace) آن Pod می‌نویسد. در این حالت، هر دو فرمان `hostname` و `hostname --fqdn`
مقدار FQDN مربوط به Pod را برمی‌گردانند.

{{< note >}}
در لینوکس، فیلد hostname کرنل (فیلد `nodename` در `struct utsname`) به ۶۴ نویسه محدود است.

اگر یک Pod این قابلیت را فعال کند و FQDN آن بیش از ۶۴ نویسه باشد، راه‌اندازی آن با شکست مواجه می‌شود.
Pod در وضعیت `Pending` باقی می‌ماند (در `kubectl` به‌صورت `ContainerCreating` دیده می‌شود) و
رویدادهای خطایی تولید می‌کند، مانند Failed to construct FQDN from Pod hostname and cluster domain,
FQDN `long-FQDN` is too long (64 characters is the max, 70 characters requested).
یکی از راه‌های بهبود تجربهٔ کاربری در این سناریو، ایجاد یک
[کنترل‌کنندهٔ admission webhook](/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks)
است تا هنگام ایجاد آبجکت‌های سطح بالا (برای مثال Deployment) توسط کاربران، اندازهٔ FQDN را کنترل کند.
{{< /note >}}

### سیاست DNS در Pod

سیاست‌های DNS را می‌توان برای هر Pod به‌طور جداگانه تنظیم کرد. در حال حاضر کوبرنتیز از
سیاست‌های DNS مختص Pod زیر پشتیبانی می‌کند. این سیاست‌ها در
فیلد `dnsPolicy` از مشخصات Pod تعیین می‌شوند.

- «`Default`»: Pod پیکربندی resolve کردن نام را از نودی که
  Podها روی آن اجرا می‌شوند، به ارث می‌برد.
  برای جزئیات بیشتر، [بحث مرتبط](/docs/tasks/administer-cluster/dns-custom-nameservers)
  را ببینید.
- «`ClusterFirst`»: هر پرس‌وجوی DNS که با پسوند دامنهٔ پیکربندی‌شدهٔ کلاستر
  مطابقت نداشته باشد، مانند «`www.kubernetes.io`»، توسط سرور DNS به یک nameserver
  بالادستی ارسال می‌شود. مدیران کلاستر ممکن است stub-domainها و سرورهای DNS بالادستی
  اضافی پیکربندی کرده باشند.
  برای جزئیات نحوهٔ رسیدگی به پرس‌وجوهای DNS در این موارد، [بحث مرتبط](/docs/tasks/administer-cluster/dns-custom-nameservers)
  را ببینید.
- «`ClusterFirstWithHostNet`»: برای Podهایی که با hostNetwork اجرا می‌شوند، باید
  سیاست DNS آن‌ها را صراحتاً روی «`ClusterFirstWithHostNet`» تنظیم کنید. در غیر این صورت، Podهایی
  که با hostNetwork و `"ClusterFirst"` اجرا می‌شوند، به رفتار
  سیاست `"Default"` بازمی‌گردند.

  {{< note >}}
  این گزینه در ویندوز پشتیبانی نمی‌شود. برای جزئیات، [بخش زیر](#dns-windows) را ببینید.
  {{< /note >}}

- «`None`»: این گزینه به Pod اجازه می‌دهد تنظیمات DNS محیط کوبرنتیز را نادیده بگیرد.
  همهٔ تنظیمات DNS باید با استفاده از
  فیلد `dnsConfig` در مشخصات Pod ارائه شوند.
  زیربخش [پیکربندی DNS در Pod](#pod-dns-config) را در ادامه ببینید.

{{< note >}}
«Default» سیاست DNS پیش‌فرض نیست. اگر `dnsPolicy`
صراحتاً تعیین نشده باشد، از «ClusterFirst» استفاده می‌شود.
{{< /note >}}

مثال زیر Podی را نشان می‌دهد که سیاست DNS آن روی
«`ClusterFirstWithHostNet`» تنظیم شده است، زیرا `hostNetwork` آن روی `true` تنظیم شده است.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: default
spec:
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    imagePullPolicy: IfNotPresent
    name: busybox
  restartPolicy: Always
  hostNetwork: true
  dnsPolicy: ClusterFirstWithHostNet
```

### پیکربندی DNS در Pod {#pod-dns-config}

{{< feature-state for_k8s_version="v1.14" state="stable" >}}

پیکربندی DNS در Pod به کاربران امکان کنترل بیشتری بر تنظیمات DNS یک Pod می‌دهد.

فیلد `dnsConfig` اختیاری است و می‌تواند با هر تنظیمی از `dnsPolicy` کار کند.
با این حال، هنگامی که `dnsPolicy` یک Pod روی «`None`» تنظیم شده باشد، فیلد `dnsConfig`
باید تعیین شود.

در ادامه ویژگی‌هایی آمده است که کاربر می‌تواند در فیلد `dnsConfig` تعیین کند:

- `nameservers`: فهرستی از نشانی‌های IP که به‌عنوان سرورهای DNS برای
  Pod استفاده خواهند شد. حداکثر ۳ نشانی IP را می‌توان تعیین کرد. هنگامی که `dnsPolicy` مربوط به Pod
  روی «`None`» تنظیم شده باشد، این فهرست باید دست‌کم شامل یک نشانی IP باشد؛ در غیر این صورت،
  این ویژگی اختیاری است.
  سرورهای فهرست‌شده با nameserverهای پایه‌ای که از
  سیاست DNS تعیین‌شده تولید می‌شوند، ترکیب می‌شوند و نشانی‌های تکراری حذف می‌شوند.
- `searches`: فهرستی از دامنه‌های جست‌وجوی DNS برای جست‌وجوی hostname در Pod.
  این ویژگی اختیاری است. در صورت تعیین شدن، فهرست ارائه‌شده با
  نام‌های دامنهٔ جست‌وجوی پایه‌ای که از سیاست DNS انتخاب‌شده تولید می‌شوند، ادغام می‌شود.
  نام‌های دامنهٔ تکراری حذف می‌شوند.
  کوبرنتیز حداکثر ۳۲ دامنهٔ جست‌وجو را مجاز می‌داند.
- `options`: فهرستی اختیاری از آبجکت‌ها که هر آبجکت می‌تواند یک ویژگی `name`
  (الزامی) و یک ویژگی `value` (اختیاری) داشته باشد. محتوای این
  ویژگی با گزینه‌هایی که از سیاست DNS تعیین‌شده تولید می‌شوند، ادغام می‌شود.
  ورودی‌های تکراری حذف می‌شوند.

در ادامه نمونه‌ای از یک Pod با تنظیمات DNS سفارشی آمده است:

{{% code_sample file="service/networking/custom-dns.yaml" %}}

هنگامی که Pod بالا ایجاد شود، کانتینر `test` محتوای زیر را
در فایل `/etc/resolv.conf` خود دریافت می‌کند:

```
nameserver 192.0.2.1
search ns1.svc.cluster-domain.example my.dns.search.suffix
options ndots:2 edns0
```

برای راه‌اندازی IPv6، مسیر جست‌وجو و name server باید به این صورت تنظیم شوند:

```shell
kubectl exec -it dns-example -- cat /etc/resolv.conf
```

خروجی مشابه زیر است:

```
nameserver 2001:db8:30::a
search default.svc.cluster-domain.example svc.cluster-domain.example cluster-domain.example
options ndots:5
```

## محدودیت‌های فهرست دامنه‌های جست‌وجوی DNS

{{< feature-state for_k8s_version="1.28" state="stable" >}}

خود کوبرنتیز پیکربندی DNS را محدود نمی‌کند، مگر اینکه طول فهرست دامنه‌های
جست‌وجو از ۳۲ بیشتر شود یا مجموع طول همهٔ دامنه‌های جست‌وجو از ۲۰۴۸ فراتر رود.
این محدودیت به‌ترتیب بر فایل پیکربندی resolver نود، پیکربندی DNS در Pod
و پیکربندی DNS ادغام‌شده اعمال می‌شود.

{{< note >}}
برخی از container runtimeهای نسخه‌های قدیمی‌تر ممکن است محدودیت‌های خاص خود را دربارهٔ
تعداد دامنه‌های جست‌وجوی DNS داشته باشند. بسته به محیط container runtime،
Podهایی که تعداد زیادی دامنهٔ جست‌وجوی DNS دارند ممکن است در
وضعیت pending گیر کنند.

مشخص شده است که containerd نسخهٔ v1.5.5 یا قدیمی‌تر و CRI-O نسخهٔ v1.21 یا قدیمی‌تر
این مشکل را دارند.
{{< /note >}}

## resolve کردن DNS در نودهای ویندوزی {#dns-windows}

- `ClusterFirstWithHostNet` برای Podهایی که روی نودهای ویندوزی اجرا می‌شوند، پشتیبانی نمی‌شود.
  ویندوز همهٔ نام‌هایی را که شامل `.` هستند FQDN در نظر می‌گیرد و از resolve کردن FQDN صرف‌نظر می‌کند.
- در ویندوز، چندین resolver برای DNS وجود دارد که می‌توان از آن‌ها استفاده کرد. از آنجا که این resolverها
  رفتارهای اندکی متفاوت دارند، استفاده از cmdlet پاورشل
  [`Resolve-DNSName`](https://docs.microsoft.com/powershell/module/dnsclient/resolve-dnsname)
  برای resolve کردن پرس‌وجوهای نام توصیه می‌شود.
- در لینوکس، یک فهرست پسوند DNS دارید که پس از ناموفق بودن resolve کردن یک نام به‌عنوان نام
  کاملاً مشخص، به کار می‌رود.
  در ویندوز، تنها می‌توانید ۱ پسوند DNS داشته باشید که همان پسوند DNS مرتبط با
  فضای نام آن Pod است (مثال: `mydns.svc.cluster.local`). ویندوز می‌تواند FQDNها، Serviceها
  یا نام‌های شبکه‌ای را که با همین یک پسوند قابل resolve شدن هستند، resolve کند. برای مثال، Podی که
  در فضای نام `default` ایجاد شده باشد، پسوند DNS ‏`default.svc.cluster.local` را خواهد داشت.
  درون یک Pod ویندوزی، می‌توانید هم `kubernetes.default.svc.cluster.local`
  و هم `kubernetes` را resolve کنید، اما نام‌های تا حدی مشخص (`kubernetes.default` یا
  `kubernetes.default.svc`) را نمی‌توانید.

## {{% heading "whatsnext" %}}

برای راهنمایی دربارهٔ مدیریت پیکربندی‌های DNS، بخش
[پیکربندی سرویس DNS](/docs/tasks/administer-cluster/dns-custom-nameservers/) را ببینید.

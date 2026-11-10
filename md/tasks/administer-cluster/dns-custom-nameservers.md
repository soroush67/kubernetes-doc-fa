---
reviewers:
- bowei
- zihongz
title: سفارشی‌سازی سرویس DNS
content_type: task
min-kubernetes-server-version: v1.12
weight: 160
---

<!-- overview -->
این صفحه توضیح می‌دهد که چگونه
{{< glossary_tooltip text="Pod(های)" term_id="pod" >}} مربوط به DNS را پیکربندی کنید و
فرایند تفکیک نام DNS (DNS resolution) را در کلاستر خود سفارشی کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

افزونهٔ CoreDNS باید در کلاستر شما در حال اجرا باشد.

{{% version-check %}}

<!-- steps -->

## مقدمه

DNS یک سرویس داخلی کوبرنتیز است که به‌طور خودکار با استفاده از
[افزونهٔ کلاستر](https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/addon-manager/README.md) _مدیر افزونه‌ها_ (addon manager) راه‌اندازی می‌شود.

{{< note >}}
نام Service مربوط به CoreDNS در فیلد `metadata.name` برابر با `kube-dns` است.
هدف از این کار، تضمین سازگاری بیشتر با بارهای کاری‌ای است که برای تفکیک
آدرس‌های داخلی کلاستر به نام قدیمی Service یعنی `kube-dns` وابسته بودند.
استفاده از یک Service با نام `kube-dns` جزئیات پیاده‌سازی را پنهان می‌کند؛
یعنی مشخص نمی‌شود کدام ارائه‌دهندهٔ DNS پشت این نام مشترک در حال اجراست.
{{< /note >}}

اگر CoreDNS را به‌صورت یک Deployment اجرا کنید، معمولاً به‌شکل یک Service
کوبرنتیز با یک نشانی IP ثابت در دسترس قرار می‌گیرد.
kubelet اطلاعات حل‌کنندهٔ DNS (DNS resolver) را با فلگ
`--cluster-dns=<dns-service-ip>` به هر کانتینر منتقل می‌کند.

نام‌های DNS به دامنه نیز نیاز دارند. دامنهٔ محلی را با فلگ
`--cluster-domain=<default-local-domain>` در kubelet پیکربندی می‌کنید.

سرور DNS از جست‌وجوهای مستقیم (رکوردهای A و AAAA)، جست‌وجوی پورت (رکوردهای SRV)،
جست‌وجوی معکوس نشانی IP (رکوردهای PTR) و موارد دیگر پشتیبانی می‌کند. برای اطلاعات بیشتر،
[DNS برای Serviceها و Podها](/docs/concepts/services-networking/dns-pod-service/) را ببینید.

اگر مقدار `dnsPolicy` یک Pod برابر با `default` باشد، Pod پیکربندی تفکیک نام را
از نودی که روی آن اجرا می‌شود به ارث می‌برد. رفتار تفکیک نام DNS در Pod باید
همانند نود باشد. با این حال،
[مشکلات شناخته‌شده](/docs/tasks/administer-cluster/dns-debugging-resolution/#known-issues) را نیز ببینید.

اگر این رفتار را نمی‌خواهید یا پیکربندی DNS متفاوتی برای Podها می‌خواهید،
می‌توانید از فلگ `--resolv-conf` در kubelet استفاده کنید. برای جلوگیری از به ارث بردن
DNS توسط Podها، مقدار این فلگ را "" قرار دهید. برای تعیین فایلی غیر از
`/etc/resolv.conf` جهت به ارث بردن DNS، مقدار آن را یک مسیر فایل معتبر قرار دهید.

## CoreDNS

سرور CoreDNS یک سرور DNS مرجع (authoritative) و همه‌منظوره است که می‌تواند در نقش
DNS کلاستر عمل کند و با [مشخصات DNS](https://github.com/kubernetes/dns/blob/master/docs/specification.md) سازگار است.

### گزینه‌های ConfigMap در CoreDNS

سرور CoreDNS یک سرور DNS ماژولار و افزونه‌پذیر است که افزونه‌ها (plugins) قابلیت‌های جدیدی به آن اضافه می‌کنند.
سرور CoreDNS را می‌توان با نگهداری یک [Corefile](https://coredns.io/2017/07/23/corefile-explained/)،
که همان فایل پیکربندی CoreDNS است، پیکربندی کرد. شما به‌عنوان مدیر کلاستر می‌توانید
{{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} مربوط به Corefile در CoreDNS را
تغییر دهید تا نحوهٔ رفتار کشف سرویس DNS را در آن کلاستر تغییر دهید.

در کوبرنتیز، CoreDNS با پیکربندی پیش‌فرض زیر برای Corefile نصب می‌شود:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health {
            lameduck 5s
        }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
            pods insecure
            fallthrough in-addr.arpa ip6.arpa
            ttl 30
        }
        prometheus :9153
        forward . /etc/resolv.conf
        cache 30
        loop
        reload
        loadbalance
    }
```

پیکربندی Corefile شامل [افزونه‌های](https://coredns.io/plugins/) زیر از CoreDNS است:

* [errors](https://coredns.io/plugins/errors/): خطاها در stdout ثبت می‌شوند.
* [health](https://coredns.io/plugins/health/): وضعیت سلامت CoreDNS در
  `http://localhost:8080/health` گزارش می‌شود. در این نحو توسعه‌یافته، `lameduck` فرایند را
  ناسالم اعلام می‌کند و سپس ۵ ثانیه پیش از خاموش شدن فرایند صبر می‌کند.
* [ready](https://coredns.io/plugins/ready/): یک نقطهٔ پایانی HTTP روی پورت 8181 زمانی پاسخ 200 OK
  برمی‌گرداند که همهٔ افزونه‌هایی که می‌توانند آمادگی را اعلام کنند، این کار را انجام داده باشند.
* [kubernetes](https://coredns.io/plugins/kubernetes/): سرور CoreDNS بر اساس IP مربوط به
  Serviceها و Podها به پرس‌وجوهای DNS پاسخ می‌دهد. می‌توانید [جزئیات بیشتر](https://coredns.io/plugins/kubernetes/)
  دربارهٔ این افزونه را در وب‌سایت CoreDNS بیابید.
  - با `ttl` می‌توانید یک TTL سفارشی برای پاسخ‌ها تعیین کنید. مقدار پیش‌فرض ۵ ثانیه است.
    کمترین TTL مجاز ۰ ثانیه و بیشترین مقدار آن ۳۶۰۰ ثانیه است.
    تنظیم TTL روی ۰ از کش شدن رکوردها جلوگیری می‌کند.
  - گزینهٔ `pods insecure` برای سازگاری با نسخه‌های قبلی `kube-dns` ارائه شده است.
  - می‌توانید از گزینهٔ `pods verified` استفاده کنید که تنها در صورتی یک رکورد A برمی‌گرداند
    که یک Pod با IP منطبق در همان فضای نام وجود داشته باشد.
  - اگر از رکوردهای Pod استفاده نمی‌کنید، می‌توانید از گزینهٔ `pods disabled` استفاده کنید.
* [prometheus](https://coredns.io/plugins/metrics/): متریک‌های CoreDNS در
  `http://localhost:9153/metrics` با قالب [Prometheus](https://prometheus.io/)
  (که OpenMetrics نیز نامیده می‌شود) در دسترس هستند.
* [forward](https://coredns.io/plugins/forward/): هر پرس‌وجویی که در دامنهٔ کلاستر کوبرنتیز
  نباشد، به حل‌کننده‌های از پیش تعریف‌شده (/etc/resolv.conf) ارسال می‌شود.
* [cache](https://coredns.io/plugins/cache/): این افزونه یک کش در لایهٔ جلویی (frontend) فعال می‌کند.
* [loop](https://coredns.io/plugins/loop/): حلقه‌های ساده در ارسال را تشخیص می‌دهد و
  در صورت یافتن حلقه، فرایند CoreDNS را متوقف می‌کند.
* [reload](https://coredns.io/plugins/reload): امکان بارگذاری مجدد خودکار Corefile تغییریافته را فراهم می‌کند.
  پس از ویرایش پیکربندی ConfigMap، دو دقیقه زمان دهید تا تغییرات شما اعمال شوند.
* [loadbalance](https://coredns.io/plugins/loadbalance): این افزونه یک متعادل‌کنندهٔ بار DNS از نوع round-robin است
  که ترتیب رکوردهای A، AAAA و MX را در پاسخ به‌صورت تصادفی تغییر می‌دهد.

با تغییر ConfigMap می‌توانید رفتار پیش‌فرض CoreDNS را تغییر دهید.

### پیکربندی دامنهٔ فرعی (Stub-domain) و سرور نام بالادستی با استفاده از CoreDNS

سرور CoreDNS می‌تواند با استفاده از [افزونهٔ forward](https://coredns.io/plugins/forward/)،
دامنه‌های فرعی و سرورهای نام بالادستی (upstream nameservers) را پیکربندی کند.

#### مثال

فرض کنید اپراتور کلاستر یک سرور دامنهٔ [Consul](https://www.consul.io/) در نشانی "10.150.0.1" دارد
و همهٔ نام‌های Consul پسوند ".consul.local" دارند. برای پیکربندی آن در CoreDNS،
مدیر کلاستر بخش زیر را در ConfigMap مربوط به CoreDNS ایجاد می‌کند.

```
consul.local:53 {
    errors
    cache 30
    forward . 10.150.0.1
}
```

برای اینکه همهٔ جست‌وجوهای DNS خارج از کلاستر صراحتاً از یک سرور نام مشخص در 172.16.0.1 عبور کنند،
به‌جای `/etc/resolv.conf`، مقصد `forward` را به آن سرور نام اشاره دهید:

```
forward .  172.16.0.1
```

ConfigMap نهایی همراه با پیکربندی پیش‌فرض `Corefile` به این شکل است:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        forward . 172.16.0.1
        cache 30
        loop
        reload
        loadbalance
    }
    consul.local:53 {
        errors
        cache 30
        forward . 10.150.0.1
    }
```

{{< note >}}
سرور CoreDNS از نام‌های دامنهٔ کاملاً مشخص (FQDN) برای دامنه‌های فرعی و سرورهای نام (مثلاً "ns.foo.com") پشتیبانی نمی‌کند.
هنگام تبدیل، همهٔ سرورهای نامی که به‌صورت FQDN تعریف شده‌اند از پیکربندی CoreDNS حذف می‌شوند.
{{< /note >}}

## {{% heading "whatsnext" %}}

- [اشکال‌زدایی تفکیک نام DNS](/docs/tasks/administer-cluster/dns-debugging-resolution/) را بخوانید.

---
reviewers:
- bowei
- zihongz
- sftim
title: استفاده از NodeLocal DNSCache در کلاسترهای کوبرنتیز
content_type: task
weight: 390
---
 
<!-- overview -->

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

این صفحه نمای کلی از قابلیت NodeLocal DNSCache در کوبرنتیز ارائه می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

 <!-- steps -->

## مقدمه

قابلیت NodeLocal DNSCache با اجرای یک عامل کش DNS به‌صورت DaemonSet روی نودهای کلاستر،
کارایی DNS کلاستر را بهبود می‌دهد. در معماری فعلی، Podهایی که در حالت DNS از نوع 'ClusterFirst' هستند
معمولاً برای پرس‌وجوهای DNS به `clusterIP` مربوط به CoreDNS مراجعه می‌کنند. kube-proxy این آدرس را
به یک endpoint از CoreDNS ترجمه می‌کند.
در این معماری جدید، Podها به عامل کش DNS که روی همان نود اجرا می‌شود مراجعه می‌کنند و به این ترتیب
از قواعد DNAT و ردیابی اتصال (connection tracking) پرهیز می‌شود.
عامل کش محلی، در صورت نبودِ نام‌های میزبان کلاستر در کش (که به‌طور پیش‌فرض پسوند "`cluster.local`" دارند)،
از سرویس CoreDNS پرس‌وجو می‌کند.

## انگیزه

* در معماری فعلی DNS، اگر هیچ نمونهٔ محلی از CoreDNS وجود نداشته باشد، ممکن است Podهایی که
  بیشترین QPS مربوط به DNS را دارند ناچار شوند به نود دیگری مراجعه کنند.
  وجود یک کش محلی به کاهش تأخیر در چنین سناریوهایی کمک می‌کند.

* دور زدن DNAT در iptables و ردیابی اتصال به کاهش
  [شرایط رقابتی conntrack](https://github.com/kubernetes/kubernetes/issues/56903)
  کمک می‌کند و از پر شدن جدول conntrack با ورودی‌های DNS مبتنی بر UDP جلوگیری می‌کند.

* اتصال‌های عامل کش محلی به سرویس CoreDNS را می‌توان به TCP ارتقا داد.
  ورودی‌های conntrack مربوط به TCP هنگام بسته شدن اتصال حذف می‌شوند، در حالی که
  ورودی‌های UDP باید منتظر پایان مهلت زمانی (timeout) بمانند
  (مقدار [پیش‌فرض](https://www.kernel.org/doc/Documentation/networking/nf_conntrack-sysctl.txt)
  `nf_conntrack_udp_timeout` برابر ۳۰ ثانیه است).

* ارتقای پرس‌وجوهای DNS از UDP به TCP، تأخیر انتهایی (tail latency) ناشی از بسته‌های UDP
  ازدست‌رفته و پایان مهلت‌های DNS را که معمولاً تا ۳۰ ثانیه (۳ تلاش مجدد + مهلت ۱۰ ثانیه) طول می‌کشد، کاهش می‌دهد.
  از آنجا که کش nodelocal به پرس‌وجوهای DNS مبتنی بر UDP گوش می‌دهد، نیازی به تغییر برنامه‌ها نیست.

* معیارها (metrics) و دیدپذیری درخواست‌های DNS در سطح نود.

* می‌توان کش منفی (negative caching) را دوباره فعال کرد و به این ترتیب تعداد پرس‌وجوها از سرویس CoreDNS را کاهش داد.

## نمودار معماری

مسیری که پرس‌وجوهای DNS پس از فعال‌سازی NodeLocal DNSCache طی می‌کنند به این صورت است:


{{< figure src="/images/docs/nodelocaldns.svg" alt="جریان NodeLocal DNSCache" title="جریان Nodelocal DNSCache" caption="این تصویر نشان می‌دهد NodeLocal DNSCache چگونه پرس‌وجوهای DNS را مدیریت می‌کند." class="diagram-medium" >}}

## پیکربندی

{{< note >}}
نشانی IP محلی‌ای که NodeLocal DNSCache روی آن گوش می‌دهد می‌تواند هر نشانی‌ای باشد که
بتوان تضمین کرد با هیچ IP موجود در کلاستر شما تداخل ندارد.
توصیه می‌شود از نشانی‌ای با دامنهٔ محلی استفاده کنید؛ برای مثال،
از بازهٔ 'link-local' یعنی '169.254.0.0/16' برای IPv4 یا از بازهٔ
'Unique Local Address' در IPv6 یعنی 'fd00::/8'.
{{< /note >}}

این قابلیت را می‌توان با مراحل زیر فعال کرد:

* مانیفستی مشابه نمونهٔ
  [`nodelocaldns.yaml`](https://github.com/kubernetes/kubernetes/blob/master/cluster/addons/dns/nodelocaldns/nodelocaldns.yaml)
  آماده کنید و آن را با نام `nodelocaldns.yaml` ذخیره کنید.

* اگر از IPv6 استفاده می‌کنید، در فایل پیکربندی CoreDNS باید همهٔ نشانی‌های IPv6 را،
  در صورتی که در قالب 'IP:Port' به کار رفته‌اند، داخل کروشه قرار دهید.
  اگر از مانیفست نمونهٔ مرحلهٔ قبل استفاده می‌کنید، لازم است
  [خط پیکربندی L70](https://github.com/kubernetes/kubernetes/blob/b2ecd1b3a3192fbbe2b9e348e095326f51dc43dd/cluster/addons/dns/nodelocaldns/nodelocaldns.yaml#L70)
  را به این شکل تغییر دهید: "`health [__PILLAR__LOCAL__DNS__]:8080`"

* متغیرهای موجود در مانیفست را با مقادیر درست جایگزین کنید:

  ```shell
  # For historical reasons, the Service for CoreDNS is called "kube-dns"
  coredns=`kubectl get svc kube-dns -n kube-system -o jsonpath={.spec.clusterIP}`
  domain=<cluster-domain>
  localdns=<node-local-address>
  ```

  مقدار `<cluster-domain>` به‌طور پیش‌فرض "`cluster.local`" است. مقدار `<node-local-address>`
  نشانی IP محلی‌ای است که برای گوش دادن NodeLocal DNSCache انتخاب شده است.

  * اگر kube-proxy در حالت IPTABLES اجرا می‌شود:

    ``` bash
    sed -i "s/__PILLAR__LOCAL__DNS__/$localdns/g; s/__PILLAR__DNS__DOMAIN__/$domain/g; s/__PILLAR__DNS__SERVER__/$coredns/g" nodelocaldns.yaml
    ```

    مقادیر `__PILLAR__CLUSTER__DNS__` و `__PILLAR__UPSTREAM__SERVERS__` را
    Podهای `node-local-dns` پر می‌کنند.
    در این حالت، Podهای `node-local-dns` هم روی IP سرویس CoreDNS و هم روی
    `<node-local-address>` گوش می‌دهند، بنابراین Podها می‌توانند با هر یک از این دو نشانی IP رکوردهای DNS را جست‌وجو کنند.

  * اگر kube-proxy در حالت IPVS اجرا می‌شود:

    ``` bash
    sed -i "s/__PILLAR__LOCAL__DNS__/$localdns/g; s/__PILLAR__DNS__DOMAIN__/$domain/g; s/,__PILLAR__DNS__SERVER__//g; s/__PILLAR__CLUSTER__DNS__/$coredns/g" nodelocaldns.yaml
    ```

    در این حالت، Podهای `node-local-dns` فقط روی `<node-local-address>` گوش می‌دهند.
    رابط `node-local-dns` نمی‌تواند به IP کلاستری CoreDNS متصل (bind) شود، زیرا
    رابطی که برای توزیع بار IPVS استفاده می‌شود از قبل این نشانی را در اختیار دارد.
    مقدار `__PILLAR__UPSTREAM__SERVERS__` را Podهای node-local-dns پر می‌کنند.

* دستور `kubectl create -f nodelocaldns.yaml` را اجرا کنید.

* اگر kube-proxy را در حالت IPVS استفاده می‌کنید، باید فلگ `--cluster-dns` در kubelet را تغییر دهید
  تا از `<node-local-address>` که NodeLocal DNSCache روی آن گوش می‌دهد استفاده کند.
  در غیر این صورت، نیازی به تغییر مقدار فلگ `--cluster-dns` نیست،
  زیرا NodeLocal DNSCache هم روی IP سرویس CoreDNS و هم روی
  `<node-local-address>` گوش می‌دهد.

پس از فعال‌سازی، Podهای `node-local-dns` در فضای نام `kube-system`
روی هر یک از نودهای کلاستر اجرا می‌شوند. این Pod، [CoreDNS](https://github.com/coredns/coredns)
را در حالت کش اجرا می‌کند؛ بنابراین همهٔ معیارهای CoreDNS که افزونه‌های مختلف ارائه می‌کنند
به‌تفکیک هر نود در دسترس خواهند بود.

برای غیرفعال کردن این قابلیت، می‌توانید DaemonSet را با دستور `kubectl delete -f <manifest>` حذف کنید.
همچنین باید هر تغییری را که در پیکربندی kubelet داده‌اید به حالت قبل برگردانید.

## پیکربندی دامنه‌های stub

فایل Corefile در ConfigMap مربوط به `node-local-dns` را می‌توان با پیکربندی
stubDomain تغییر داد. برخی ارائه‌دهندگان ابری ممکن است اجازهٔ تغییر مستقیم
ConfigMap مربوط به `node-local-dns` را ندهند؛ در این صورت می‌توان به‌جای آن از یک ConfigMap با نام `kube-dns`
در قالبی که به‌طور سنتی در `kube-dns` استفاده می‌شود بهره گرفت:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: kube-system
  name: kube-dns
data:
  stubDomains: |
    {"abc.com" : ["1.2.3.4"], "my.cluster.local" : ["2.3.4.5"]}
```

## تنظیم محدودیت‌های حافظه

Podهای `node-local-dns` از حافظه برای ذخیرهٔ ورودی‌های کش و پردازش پرس‌وجوها استفاده می‌کنند.
از آنجا که این Podها آبجکت‌های کوبرنتیز را پایش نمی‌کنند، اندازهٔ کلاستر یا تعداد Serviceها / EndpointSliceها مستقیماً بر مصرف حافظه اثری ندارد. مصرف حافظه تحت تأثیر الگوی پرس‌وجوهای DNS است.
بر اساس [مستندات CoreDNS](https://github.com/coredns/deployment/blob/master/kubernetes/Scaling_CoreDNS.md):
> اندازهٔ پیش‌فرض کش ۱۰۰۰۰ ورودی است که در صورت پر شدن کامل حدود ۳۰ مگابایت حافظه مصرف می‌کند.

این مقدار، مصرف حافظه برای هر بلوک سرور است (در صورتی که کش کاملاً پر شود).
با تعیین اندازه‌های کوچک‌تر برای کش می‌توان مصرف حافظه را کاهش داد.

تعداد پرس‌وجوهای هم‌زمان با نیاز به حافظه مرتبط است، زیرا هر goroutine اضافی که برای
رسیدگی به یک پرس‌وجو استفاده می‌شود به مقداری حافظه نیاز دارد. می‌توانید با گزینهٔ
`max_concurrent` در افزونهٔ forward یک حد بالا برای آن تعیین کنید.

اگر یک Pod از نوع `node-local-dns` بخواهد بیش از حافظهٔ دردسترس مصرف کند (به دلیل محدودیت
کل منابع سیستم، یا به دلیل یک
[محدودیت منبع](/docs/concepts/configuration/manage-resources-containers/) پیکربندی‌شده)، سیستم‌عامل
ممکن است کانتینر آن Pod را متوقف کند.
در این صورت، کانتینرِ خاتمه‌یافته («OOMKilled») قواعد سفارشی فیلتر بسته را که پیش‌تر
هنگام راه‌اندازی اضافه کرده بود پاک نمی‌کند.
کانتینر `node-local-dns` باید دوباره راه‌اندازی شود (زیرا به‌عنوان بخشی از یک DaemonSet مدیریت می‌شود)، اما این
وضعیت هر بار که کانتینر از کار بیفتد به قطعی کوتاه‌مدت DNS منجر می‌شود: قواعد فیلتر بسته،
پرس‌وجوهای DNS را به یک Pod محلی ناسالم هدایت می‌کنند.

برای تعیین محدودیت حافظهٔ مناسب، می‌توانید Podهای node-local-dns را بدون محدودیت اجرا کنید و
اوج مصرف را اندازه بگیرید. همچنین می‌توانید یک
[VerticalPodAutoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler)
را در _حالت توصیه‌گر (recommender mode)_ راه‌اندازی و استفاده کنید و سپس توصیه‌های آن را بررسی کنید.

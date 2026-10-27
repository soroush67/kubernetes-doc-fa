---
reviewers:
- jpbetz
title: پراکسی نسخه‌های ترکیبی
content_type: concept
weight: 220
---

<!-- overview -->

{{< feature-state feature_gate_name="UnknownVersionInteroperabilityProxy" >}}

کوبرنتیز {{< skew currentVersion >}} شامل یک قابلیت بتا است که به یک
{{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
اجازه می‌دهد درخواست‌های منابع را به سرورهای API _همتای_ دیگر پراکسی کند. همچنین به کلاینت‌ها امکان می‌دهد
از طریق کشف (discovery)، دیدی جامع از منابعی که در سراسر کلاستر ارائه می‌شوند به دست آورند.
این قابلیت زمانی سودمند است که چندین
سرور API با نسخه‌های مختلف کوبرنتیز در یک کلاستر اجرا می‌شوند
(برای نمونه، در طول یک فرایند استقرار طولانی‌مدت به یک انتشار جدید کوبرنتیز).

این قابلیت به مدیران کلاستر امکان می‌دهد کلاسترهایی با دسترس‌پذیری بالا پیکربندی کنند که بتوان آن‌ها را
با ایمنی بیشتری ارتقا داد، از این راه‌ها:

1. اطمینان از اینکه کنترل‌کننده‌هایی که برای وظایف مهم به کشف (discovery) جهت نمایش فهرستی جامع از منابع
متکی هستند، همواره دید کاملی از همهٔ منابع دریافت کنند. ما این کشف کامل در سطح کل کلاستر را
_کشف تجمیع‌شده از همتایان_ (Peer-aggregated discovery) می‌نامیم.
1. هدایت درخواست‌های منابع (که در طول ارتقا ارسال می‌شوند) به kube-apiserver درست.
این پراکسی‌کردن مانع از آن می‌شود که کاربران خطاهای غیرمنتظرهٔ 404 Not Found ناشی از
فرایند ارتقا را ببینند. این سازوکار _پراکسی نسخه‌های ترکیبی_ (Mixed Version Proxy) نام دارد.

## فعال‌سازی کشف تجمیع‌شده از همتایان و پراکسی نسخه‌های ترکیبی

هنگام راه‌اندازی {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}، اطمینان حاصل کنید که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#UnknownVersionInteroperabilityProxy) با نام `UnknownVersionInteroperabilityProxy` فعال است:

```shell
kube-apiserver \
--feature-gates=UnknownVersionInteroperabilityProxy=true \
# required command line arguments for this feature
--peer-ca-file=<path to kube-apiserver CA cert>
--proxy-client-cert-file=<path to aggregator proxy cert>,
--proxy-client-key-file=<path to aggregator proxy key>,
--requestheader-client-ca-file=<path to aggregator CA cert>,
# requestheader-allowed-names can be set to blank to allow any Common Name
--requestheader-allowed-names=<valid Common Names to verify proxy client cert against>,

# optional flags for this feature
--peer-advertise-ip=`IP of this kube-apiserver that should be used by peers to proxy requests`
--peer-advertise-port=`port of this kube-apiserver that should be used by peers to proxy requests`

# …and other flags as usual
```

### انتقال و احراز هویت پراکسی میان سرورهای API {#transport-and-authn}

* kube-apiserver مبدأ از
  [پرچم‌های موجود احراز هویت کلاینت APIserver](/docs/tasks/extend-kubernetes/configure-aggregation-layer/#kubernetes-apiserver-client-authentication)،
  یعنی `--proxy-client-cert-file` و `--proxy-client-key-file`، دوباره استفاده می‌کند تا هویت خود را ارائه دهد؛ هویتی که
  همتای آن (kube-apiserver مقصد) تأییدش خواهد کرد. سرور API مقصد
  آن اتصال همتا را بر اساس پیکربندی‌ای که با آرگومان خط فرمان
  `--requestheader-client-ca-file` تعیین می‌کنید، تأیید می‌کند.

* برای احراز هویت گواهی‌های سرویس‌دهی سرور مقصد، باید یک بستهٔ مرجع صدور گواهی
  را با تعیین آرگومان خط فرمان `--peer-ca-file` برای سرور API **مبدأ** پیکربندی کنید.

### پیکربندی اتصال سرورهای API همتا

برای تعیین موقعیت شبکه‌ای یک kube-apiserver که همتایان برای پراکسی‌کردن درخواست‌ها از آن استفاده خواهند کرد، از
آرگومان‌های خط فرمان `--peer-advertise-ip` و `--peer-advertise-port` برای kube-apiserver استفاده کنید یا
این فیلدها را در فایل پیکربندی سرور API مشخص کنید.
اگر این پرچم‌ها مشخص نشده باشند، همتایان از مقدار یکی از آرگومان‌های خط فرمان `--advertise-address` یا
`--bind-address` مربوط به kube-apiserver استفاده خواهند کرد.
اگر آن‌ها نیز تنظیم نشده باشند، از رابط پیش‌فرض میزبان استفاده می‌شود.

## کشف تجمیع‌شده از همتایان

هنگامی که این قابلیت را فعال می‌کنید، درخواست‌های کشف به‌طور خودکار فعال می‌شوند تا به‌طور پیش‌فرض
یک سند کشف جامع (که همهٔ منابع ارائه‌شده توسط هر apiserver در کلاستر را فهرست می‌کند)
ارائه دهند.

اگر می‌خواهید
یک سند کشف غیرتجمیع‌شده از همتایان درخواست کنید، می‌توانید این را با افزودن سرآیند Accept زیر به درخواست کشف مشخص کنید:

```
application/json;g=apidiscovery.k8s.io;v=v2;as=APIGroupDiscoveryList;profile=nopeer
```

{{< note >}}
کشف تجمیع‌شده از همتایان تنها برای
درخواست‌های [کشف تجمیع‌شده (Aggregated Discovery)](/docs/concepts/overview/kubernetes-api/#aggregated-discovery)
به نقطهٔ پایانی `/apis` پشتیبانی می‌شود و برای درخواست‌های [کشف غیرتجمیع‌شده (قدیمی)](/docs/concepts/overview/kubernetes-api/#unaggregated-discovery) پشتیبانی نمی‌شود.
{{< /note >}}

## پراکسی‌کردن نسخه‌های ترکیبی

هنگامی که پراکسی‌کردن نسخه‌های ترکیبی را فعال می‌کنید، [لایهٔ تجمیع](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
فیلتر ویژه‌ای را بارگذاری می‌کند که کارهای زیر را انجام می‌دهد:

* هنگامی که یک درخواست منبع به سرور API‌ای می‌رسد که نمی‌تواند آن API را ارائه دهد
  (یا به این دلیل که نسخهٔ آن سرور پیش از معرفی آن API است، یا به این دلیل که آن API روی سرور API خاموش است)،
  سرور API تلاش می‌کند درخواست را به یک سرور API همتا که می‌تواند API درخواستی را ارائه دهد ارسال کند.
  این کار با شناسایی گروه‌ها / نسخه‌ها / منابع API که سرور محلی آن‌ها را نمی‌شناسد انجام می‌شود
  و سرور تلاش می‌کند آن درخواست‌ها را به یک سرور API همتا که قادر به رسیدگی به درخواست است پراکسی کند.
* اگر سرور API همتا پاسخ ندهد، سرور API _مبدأ_ با خطای 503 ("Service Unavailable") پاسخ می‌دهد.

### سازوکار درونی

هنگامی که یک سرور API درخواست منبعی را دریافت می‌کند، ابتدا بررسی می‌کند کدام سرورهای API می‌توانند
منبع درخواستی را ارائه دهند. این بررسی با استفاده از سند کشف غیرتجمیع‌شده از همتایان انجام می‌شود.

* اگر منبع در سند کشف غیرتجمیع‌شده از همتایان که از سرور API دریافت‌کنندهٔ درخواست بازیابی شده فهرست شده باشد (برای نمونه، `GET /api/v1/pods/some-pod`)، درخواست به‌صورت محلی رسیدگی می‌شود.

* اگر منبع موجود در یک درخواست (برای نمونه، `GET /apis/resource.k8s.io/v1beta1/resourceclaims`) در سند کشف غیرتجمیع‌شده از همتایان که از سرور API در حال رسیدگی به درخواست (_سرور API رسیدگی‌کننده_) بازیابی شده یافت نشود، که احتمالاً به این دلیل است که API مربوط به `resource.k8s.io/v1beta1` در نسخهٔ جدیدتری از کوبرنتیز معرفی شده و _سرور API رسیدگی‌کننده_ نسخهٔ قدیمی‌تری را اجرا می‌کند که از آن پشتیبانی نمی‌کند، آنگاه _سرور API رسیدگی‌کننده_ با بررسی اسناد کشف غیرتجمیع‌شده از همتایانِ همهٔ سرورهای API همتا، سرورهای API همتایی را که گروه / نسخه / منبع API مربوط (در این مورد `resource.k8s.io/v1beta1/resourceclaims`) را ارائه می‌دهند پیدا می‌کند. سپس _سرور API رسیدگی‌کننده_ درخواست را به یکی از kube-apiserverهای همتای منطبق که از منبع درخواستی آگاه هستند پراکسی می‌کند.

* اگر هیچ همتای شناخته‌شده‌ای برای آن گروه / نسخه / منبع API وجود نداشته باشد، سرور API رسیدگی‌کننده
درخواست را به زنجیرهٔ رسیدگی‌کنندهٔ خود می‌سپارد که در نهایت باید پاسخ 404 ("Not Found") برگرداند.

* اگر سرور API رسیدگی‌کننده یک سرور API همتا را شناسایی و انتخاب کرده باشد، اما آن همتا
پاسخ ندهد (به دلایلی مانند مشکلات اتصال شبکه، یا رقابت داده‌ای (data race) میان دریافت
درخواست و ثبت اطلاعات همتا در control plane توسط یک کنترل‌کننده)، آنگاه سرور API
رسیدگی‌کننده با خطای 503 ("Service Unavailable") پاسخ می‌دهد.

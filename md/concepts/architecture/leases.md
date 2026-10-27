---
title: Leaseها
api_metadata:
- apiVersion: "coordination.k8s.io/v1"
  kind: "Lease"
content_type: concept
weight: 30
---

<!-- overview -->

سیستم‌های توزیع‌شده اغلب به _اجاره‌ها_ (leases) نیاز دارند؛ اجاره‌ها سازوکاری برای قفل‌کردن منابع مشترک
و هماهنگ‌سازی فعالیت میان اعضای یک مجموعه فراهم می‌کنند.
در کوبرنتیز، مفهوم اجاره با آبجکت‌های [Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/)
در {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `coordination.k8s.io` بازنمایی می‌شود
که برای قابلیت‌های حیاتی سیستم، مانند ضربان‌های نود (node heartbeats) و انتخاب رهبر در سطح مؤلفه، به کار می‌روند.

<!-- body -->

## ضربان‌های نود {#node-heart-beats}

کوبرنتیز از API مربوط به Lease برای ارسال ضربان‌های نود kubelet به سرور API کوبرنتیز استفاده می‌کند.
برای هر `Node`، یک آبجکت `Lease` با نام متناظر در فضای نام `kube-node-lease`
وجود دارد. در پشت صحنه، هر ضربان kubelet یک درخواست **update** به این آبجکت `Lease` است که
فیلد `spec.renewTime` آن Lease را به‌روزرسانی می‌کند. control plane کوبرنتیز از مُهر زمانی این فیلد
برای تعیین در دسترس بودن این `Node` استفاده می‌کند.

برای جزئیات بیشتر، به [آبجکت‌های Lease نود](/docs/concepts/architecture/nodes/#node-heartbeats) مراجعه کنید.

## انتخاب رهبر

کوبرنتیز همچنین از Leaseها استفاده می‌کند تا اطمینان حاصل کند که در هر لحظه تنها یک نمونه از یک مؤلفه در حال اجراست.
اجزای control plane مانند `kube-controller-manager` و `kube-scheduler` در
پیکربندی‌های با دسترس‌پذیری بالا (HA) از این سازوکار استفاده می‌کنند؛ در این پیکربندی‌ها تنها یک نمونه از مؤلفه باید به‌طور فعال اجرا شود و
سایر نمونه‌ها در حالت آماده‌به‌کار قرار دارند.

برای آشنایی با اینکه کوبرنتیز چگونه بر پایهٔ API مربوط به Lease تعیین می‌کند کدام نمونهٔ مؤلفه
نقش رهبر را ایفا کند، [انتخاب رهبر هماهنگ](/docs/concepts/cluster-administration/coordinated-leader-election) را بخوانید.

### آزادسازی قفل kube-controller-manager هنگام خروج

{{< feature-state feature_gate_name="ControllerManagerReleaseLeaderElectionLockOnExit" >}}

هنگامی که feature gate با نام `ControllerManagerReleaseLeaderElectionLockOnExit` فعال باشد،
`kube-controller-manager` در جریان جابه‌جایی رهبر، قفل انتخاب رهبر خود را به‌طور فعال
آزاد می‌کند، به‌جای آنکه منتظر انقضای TTL قفل بماند. این کار امکان می‌دهد
رهبر جدید سریع‌تر انتخاب شود و تأخیر جابه‌جایی رهبر کاهش یابد.

## هویت سرور API

{{< feature-state feature_gate_name="APIServerIdentity" >}}

از کوبرنتیز v1.26 به بعد، هر `kube-apiserver` از API مربوط به Lease برای انتشار هویت خود به
بقیهٔ سیستم استفاده می‌کند. اگرچه این قابلیت به‌تنهایی چندان سودمند نیست، سازوکاری برای کلاینت‌ها فراهم می‌کند تا
دریابند چه تعداد نمونه از `kube-apiserver` در حال اداره کردن control plane کوبرنتیز هستند.
وجود Leaseهای kube-apiserver، قابلیت‌های آینده‌ای را ممکن می‌سازد که ممکن است به هماهنگی میان
نمونه‌های kube-apiserver نیاز داشته باشند.

می‌توانید Leaseهای متعلق به هر kube-apiserver را با بررسی آبجکت‌های lease در فضای نام `kube-system`
با نام `apiserver-<sha256-hash>` بازرسی کنید. به‌عنوان راه دیگر، می‌توانید از انتخابگر برچسب `apiserver.kubernetes.io/identity=kube-apiserver` استفاده کنید:

```shell
kubectl -n kube-system get lease -l apiserver.kubernetes.io/identity=kube-apiserver
```
```
NAME                                        HOLDER                                                                           AGE
apiserver-07a5ea9b9b072c4a5f3d1c3702        apiserver-07a5ea9b9b072c4a5f3d1c3702_0c8914f7-0f35-440e-8676-7844977d3a05        5m33s
apiserver-7be9e061c59d368b3ddaf1376e        apiserver-7be9e061c59d368b3ddaf1376e_84f2a85d-37c1-4b14-b6b9-603e62e4896f        4m23s
apiserver-1dfef752bcb36637d2763d1868        apiserver-1dfef752bcb36637d2763d1868_c5ffa286-8a9a-45d4-91e7-61118ed58d2e        4m43s

```

درهم‌سازی SHA256 که در نام lease به کار می‌رود، بر پایهٔ نام میزبان سیستم‌عامل از دید آن سرور API است. هر kube-apiserver باید
طوری پیکربندی شود که از نام میزبانی یکتا در سطح کلاستر استفاده کند. نمونه‌های جدید kube-apiserver که از نام میزبان یکسانی استفاده می‌کنند،
به‌جای ایجاد آبجکت‌های Lease جدید، Leaseهای موجود را با یک هویت نگه‌دارندهٔ جدید در اختیار می‌گیرند. می‌توانید
نام میزبانی را که kube-apiserver استفاده می‌کند با بررسی مقدار برچسب `kubernetes.io/hostname` ببینید:

```shell
kubectl -n kube-system get lease apiserver-07a5ea9b9b072c4a5f3d1c3702 -o yaml
```
```yaml
apiVersion: coordination.k8s.io/v1
kind: Lease
metadata:
  creationTimestamp: "2023-07-02T13:16:48Z"
  labels:
    apiserver.kubernetes.io/identity: kube-apiserver
    kubernetes.io/hostname: master-1
  name: apiserver-07a5ea9b9b072c4a5f3d1c3702
  namespace: kube-system
  resourceVersion: "334899"
  uid: 90870ab5-1ba9-4523-b215-e4d4e662acb1
spec:
  holderIdentity: apiserver-07a5ea9b9b072c4a5f3d1c3702_0c8914f7-0f35-440e-8676-7844977d3a05
  leaseDurationSeconds: 3600
  renewTime: "2023-07-04T21:58:48.065888Z"
```

Leaseهای منقضی‌شدهٔ مربوط به kube-apiserverهایی که دیگر وجود ندارند، پس از ۱ ساعت توسط kube-apiserverهای جدید در جمع‌آوری زباله حذف می‌شوند.

می‌توانید Leaseهای هویت سرور API را با غیرفعال‌کردن
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `APIServerIdentity` غیرفعال کنید.

## بارهای کاری {#custom-workload}

بار کاری شما می‌تواند کاربرد خاص خود را برای Leaseها تعریف کند. برای نمونه، ممکن است یک
{{< glossary_tooltip term_id="controller" text="کنترل‌کنندهٔ" >}} سفارشی اجرا کنید که در آن یک عضو اصلی یا رهبر
عملیاتی را انجام می‌دهد که همتایانش انجام نمی‌دهند. شما یک Lease تعریف می‌کنید تا نسخه‌های تکثیرشدهٔ کنترل‌کننده بتوانند
با استفاده از API کوبرنتیز برای هماهنگی، یک رهبر را برگزینند یا انتخاب کنند.
اگر از Lease استفاده می‌کنید، روش خوبی است که برای Lease نامی تعریف کنید که به‌روشنی با
محصول یا مؤلفه مرتبط باشد. برای نمونه، اگر مؤلفه‌ای با نام Example Foo دارید، از Leaseای با نام
`example-foo` استفاده کنید.

اگر یک گردانندهٔ کلاستر یا کاربر نهایی دیگری ممکن است چندین نمونه از یک مؤلفه را مستقر کند، یک
پیشوند نام برگزینید و سازوکاری (مانند درهم‌سازی نام Deployment) انتخاب کنید تا از تداخل نام
Leaseها جلوگیری شود.

می‌توانید از رویکرد دیگری نیز استفاده کنید، به شرط آنکه به همان نتیجه برسد: محصولات نرم‌افزاری مختلف
با یکدیگر تداخل نداشته باشند.

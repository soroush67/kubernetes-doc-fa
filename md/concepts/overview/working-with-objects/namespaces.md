---
reviewers:
- derekwaynecarr
- mikedanese
- thockin
title: فضاهای نام
api_metadata:
- apiVersion: "v1"
  kind: "Namespace"
content_type: concept
weight: 45
---

<!-- overview -->

در کوبرنتیز، _فضاهای نام_ (namespaces) سازوکاری برای جداسازی گروه‌هایی از منابع درون یک کلاستر واحد فراهم می‌کنند. نام منابع باید درون یک فضای نام یکتا باشد، اما لازم نیست در میان فضاهای نام مختلف یکتا باشد. محدوده‌بندی مبتنی بر فضای نام فقط برای {{< glossary_tooltip text="آبجکت‌های" term_id="object" >}} وابسته به فضای نام _(مانند Deploymentها، Serviceها و غیره)_ کاربرد دارد و برای آبجکت‌های سطح کلاستر _(مانند StorageClass، Nodeها، PersistentVolumeها و غیره)_ کاربرد ندارد.

<!-- body -->

## چه زمانی از چند فضای نام استفاده کنیم

فضاهای نام برای استفاده در محیط‌هایی با کاربران بسیار که در چند
تیم یا پروژه پراکنده‌اند در نظر گرفته شده‌اند. برای کلاسترهایی با چند تا چند ده کاربر، اصلاً
نیازی نیست فضاهای نام ایجاد کنید یا به آن‌ها فکر کنید. هنگامی استفاده از فضاهای نام را آغاز کنید که
به قابلیت‌هایی که فراهم می‌کنند نیاز دارید.

فضاهای نام محدوده‌ای برای نام‌ها فراهم می‌کنند. نام منابع باید درون یک فضای نام یکتا باشد،
اما لازم نیست در میان فضاهای نام مختلف یکتا باشد. فضاهای نام را نمی‌توان درون یکدیگر قرار داد و هر منبع
کوبرنتیز فقط می‌تواند در یک فضای نام باشد.

فضاهای نام راهی برای تقسیم منابع کلاستر میان چند کاربر هستند (از طریق [سهمیهٔ منابع](/docs/concepts/policy/resource-quotas/)).

برای جداکردن منابعی که تفاوت اندکی با هم دارند، مانند نسخه‌های مختلف یک نرم‌افزار،
لازم نیست از چند فضای نام استفاده کنید: برای متمایزکردن
منابع درون یک فضای نام از {{< glossary_tooltip text="برچسب‌ها" term_id="label" >}} استفاده کنید.

{{< note >}}
برای یک کلاستر عملیاتی (production)، در نظر داشته باشید که از فضای نام `default` استفاده _نکنید_. به‌جای آن، فضاهای نام دیگری بسازید و از آن‌ها استفاده کنید.
{{< /note >}}

## فضاهای نام اولیه

کوبرنتیز با چهار فضای نام اولیه آغاز به کار می‌کند:

`default`
: کوبرنتیز این فضای نام را در بر دارد تا بتوانید بدون ایجاد یک فضای نام، استفاده از کلاستر جدید خود را آغاز کنید.

`kube-node-lease`
: این فضای نام آبجکت‌های [Lease](/docs/concepts/architecture/leases/) مرتبط با هر نود را نگه می‌دارد. Leaseهای نود به kubelet اجازه می‌دهند [ضربان‌های حیات (heartbeats)](/docs/concepts/architecture/nodes/#node-heartbeats) ارسال کند تا control plane بتواند خرابی نود را تشخیص دهد.

`kube-public`
: این فضای نام برای *همهٔ* کلاینت‌ها (از جمله کلاینت‌های احراز هویت‌نشده) قابل خواندن است. این فضای نام بیشتر برای استفادهٔ کلاستر رزرو شده است، برای مواردی که برخی منابع باید در سراسر کلاستر به‌صورت عمومی قابل مشاهده و خواندن باشند. جنبهٔ عمومی این فضای نام فقط یک قرارداد است و الزام نیست.

`kube-system`
: فضای نام آبجکت‌هایی که سیستم کوبرنتیز ایجاد می‌کند.

## کار با فضاهای نام

ایجاد و حذف فضاهای نام در
[مستندات راهنمای مدیر دربارهٔ فضاهای نام](/docs/tasks/administer-cluster/namespaces) شرح داده شده است.

{{< note >}}
از ایجاد فضاهای نام با پیشوند `kube-` خودداری کنید، زیرا این پیشوند برای فضاهای نام سیستمی کوبرنتیز رزرو شده است.
{{< /note >}}

### مشاهدهٔ فضاهای نام

می‌توانید فضاهای نام فعلی یک کلاستر را با استفاده از دستور زیر فهرست کنید:

```shell
kubectl get namespace
```
```
NAME              STATUS   AGE
default           Active   1d
kube-node-lease   Active   1d
kube-public       Active   1d
kube-system       Active   1d
```


### تنظیم فضای نام برای یک درخواست

برای تنظیم فضای نام برای درخواست فعلی، از پرچم `--namespace` استفاده کنید.

برای مثال:

```shell
kubectl run nginx --image=nginx --namespace=<insert-namespace-name-here>
kubectl get pods --namespace=<insert-namespace-name-here>
```

### تنظیم ترجیح فضای نام

می‌توانید فضای نام را برای همهٔ دستورهای kubectl بعدی در آن context
به‌طور دائمی ذخیره کنید.

```shell
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:
```

## فضاهای نام و DNS

هنگامی که یک [Service](/docs/concepts/services-networking/service/) ایجاد می‌کنید،
یک [ورودی DNS](/docs/concepts/services-networking/dns-pod-service/) متناظر ایجاد می‌شود.
این ورودی به شکل `<service-name>.<namespace-name>.svc.cluster.local` است، به این معنا
که اگر یک کانتینر فقط از `<service-name>` استفاده کند، به سرویسی resolve می‌شود که
در همان فضای نام محلی قرار دارد. این ویژگی برای استفاده از پیکربندی یکسان در
چند فضای نام مانند Development، Staging و Production مفید است. اگر می‌خواهید به
فضاهای نام دیگر دسترسی پیدا کنید، باید از نام دامنهٔ کاملاً مشخص (FQDN) استفاده کنید.

در نتیجه، نام همهٔ فضاهای نام باید
[برچسب‌های DNS معتبر مطابق RFC 1123](/docs/concepts/overview/working-with-objects/names/#dns-label-names) باشد.

{{< warning >}}
با ایجاد فضاهای نامی هم‌نام با [دامنه‌های سطح بالای
عمومی](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)، Serviceهای موجود در این
فضاهای نام می‌توانند نام‌های DNS کوتاهی داشته باشند که با رکوردهای DNS عمومی هم‌پوشانی دارند.
بارهای کاری هر فضای نامی که بدون [نقطهٔ انتهایی](https://datatracker.ietf.org/doc/html/rfc1034#page-8) جست‌وجوی DNS انجام دهند،
به آن سرویس‌ها هدایت خواهند شد و این سرویس‌ها بر DNS عمومی اولویت خواهند داشت.

برای کاهش این خطر، امتیاز ایجاد فضاهای نام را به کاربران مورد اعتماد محدود کنید. در صورت
نیاز، می‌توانید علاوه بر این، کنترل‌های امنیتی شخص ثالث، مانند
[admission
webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/)،
را پیکربندی کنید تا از ایجاد هر فضای نامی با نام [TLDهای
عمومی](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) جلوگیری شود.
{{< /warning >}}

## همهٔ آبجکت‌ها در یک فضای نام نیستند

بیشتر منابع کوبرنتیز (مانند Podها، Serviceها، Deploymentها و غیره) در فضاهای نامی قرار دارند. با این حال، خود منابع فضای نام در یک فضای نام قرار ندارند. منابع سطح پایین، مانند
[Nodeها](/docs/concepts/architecture/nodes/) و
[PersistentVolumeها](/docs/concepts/storage/persistent-volumes/)، نیز در هیچ فضای نامی قرار ندارند.

برای مشاهدهٔ اینکه کدام منابع کوبرنتیز در یک فضای نام هستند و کدام نیستند:

```shell
# In a namespace
kubectl api-resources --namespaced=true

# Not in a namespace
kubectl api-resources --namespaced=false
```

## برچسب‌گذاری خودکار

{{< feature-state for_k8s_version="1.22" state="stable" >}}

control plane کوبرنتیز یک {{< glossary_tooltip text="برچسب" term_id="label" >}} تغییرناپذیر
با نام `kubernetes.io/metadata.name` را روی همهٔ فضاهای نام تنظیم می‌کند.
مقدار این برچسب، نام فضای نام است.


## {{% heading "whatsnext" %}}

* دربارهٔ [ایجاد یک فضای نام جدید](/docs/tasks/administer-cluster/namespaces/#creating-a-new-namespace) بیشتر بیاموزید.
* دربارهٔ [حذف یک فضای نام](/docs/tasks/administer-cluster/namespaces/#deleting-a-namespace) بیشتر بیاموزید.

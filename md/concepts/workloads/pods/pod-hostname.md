---
title: نام میزبان Pod
content_type: concept
weight: 85
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه نام میزبان (hostname) یک Pod را تنظیم کنید، این پیکربندی چه پیامدهای جانبی احتمالی‌ای دارد و سازوکار زیربنایی آن چگونه است.

<!-- body -->

## نام میزبان پیش‌فرض Pod

هنگامی که یک Pod ایجاد می‌شود، نام میزبان آن (آن‌گونه که از درون Pod دیده می‌شود) از مقدار metadata.name آن Pod گرفته می‌شود. از دید Pod، هم نام میزبان و هم نام دامنهٔ کاملاً مشخص (FQDN) متناظر با آن برابر با مقدار metadata.name تنظیم می‌شوند.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-1
spec:
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```
نام میزبان و نام دامنهٔ کاملاً مشخص Pod ایجادشده با این مانیفست برابر با `busybox-1` تنظیم می‌شود.

## نام میزبان با فیلدهای hostname و subdomain در Pod
مشخصات (spec) Pod یک فیلد اختیاری به نام `hostname` دارد. اگر این فیلد تنظیم شود، مقدار آن برای تعیین نام میزبان (آن‌گونه که از درون Pod دیده می‌شود) بر `metadata.name` آن Pod اولویت دارد. برای مثال، نام میزبان Podای که فیلد spec.hostname آن برابر با `my-host` باشد، `my-host` خواهد بود.

مشخصات Pod همچنین یک فیلد اختیاری به نام `subdomain` دارد که نشان می‌دهد Pod به یک زیردامنه در فضای نام (namespace) خود تعلق دارد. اگر در فضای نام `my-namespace`، فیلد `spec.hostname` یک Pod برابر با "foo" و فیلد spec.subdomain آن برابر با "bar" باشد، نام میزبان آن `foo` و نام دامنهٔ کاملاً مشخص آن (از درون Pod) `foo.bar.my-namespace.svc.cluster-domain.example` خواهد بود.

هنگامی که هر دو فیلد hostname و subdomain تنظیم شده باشند، سرور DNS کلاستر بر اساس این فیلدها رکوردهای A و/یا AAAA ایجاد می‌کند. برای اطلاعات بیشتر به [فیلدهای hostname و subdomain در Pod](/docs/concepts/services-networking/dns-pod-service/#pod-hostname-and-subdomain-field) مراجعه کنید.

## نام میزبان با فیلد setHostnameAsFQDN در Pod

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

هنگامی که یک Pod برای داشتن نام دامنهٔ کاملاً مشخص پیکربندی شده باشد، نام میزبان آن همان نام میزبان کوتاه است. برای مثال، اگر Podای با نام دامنهٔ کاملاً مشخص `busybox-1.busybox-subdomain.my-namespace.svc.cluster-domain.example` داشته باشید، به‌طور پیش‌فرض دستور `hostname` در درون آن Pod مقدار `busybox-1` را برمی‌گرداند و دستور `hostname --fqdn` نام دامنهٔ کاملاً مشخص را برمی‌گرداند.

هنگامی که در مشخصات Pod هم `setHostnameAsFQDN: true` و هم فیلد subdomain تنظیم شده باشد، kubelet نام دامنهٔ کاملاً مشخص Pod را به‌عنوان نام میزبان در فضای نام آن Pod می‌نویسد. در این حالت، هر دو دستور `hostname` و `hostname --fqdn` نام دامنهٔ کاملاً مشخص Pod را برمی‌گردانند.

نام دامنهٔ کاملاً مشخص Pod به همان روشی ساخته می‌شود که پیش‌تر توضیح داده شد. این نام از فیلد `spec.hostname` Pod (در صورت تعیین) یا فیلد `metadata.name`، فیلد `spec.subdomain`، نام `namespace` و پسوند دامنهٔ کلاستر تشکیل می‌شود.

{{< note >}}
در لینوکس، فیلد نام میزبان در هسته (فیلد `nodename` در `struct utsname`) به ۶۴ نویسه محدود است.

اگر یک Pod این قابلیت را فعال کند و طول نام دامنهٔ کاملاً مشخص آن بیش از ۶۴ نویسه باشد، راه‌اندازی آن با شکست مواجه می‌شود. در این حالت، Pod در وضعیت `Pending` باقی می‌ماند (و `kubectl` آن را در وضعیت `ContainerCreating` نشان می‌دهد) و رویدادهای خطایی مانند "Failed to construct FQDN from Pod hostname and cluster domain" تولید می‌کند.

بنابراین هنگام استفاده از این فیلد، باید مطمئن شوید که مجموع طول فیلدهای `metadata.name` (یا `spec.hostname`) و `spec.subdomain` در Pod، نام دامنهٔ کاملاً مشخصی با طول بیش از ۶۴ نویسه ایجاد نکند.
{{< /note >}}

## نام میزبان با فیلد hostnameOverride در Pod
{{< feature-state feature_gate_name="HostnameOverride" >}}

اگر در مشخصات Pod مقداری برای `hostnameOverride` تعیین کنید، kubelet بدون هیچ شرطی هم نام میزبان و هم نام دامنهٔ کاملاً مشخص Pod را برابر با مقدار `hostnameOverride` تنظیم می‌کند.

طول فیلد `hostnameOverride` به ۶۴ نویسه محدود است و مقدار آن باید با استاندارد نام‌های زیردامنهٔ DNS که در [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123) تعریف شده است مطابقت داشته باشد.

مثال:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-2-busybox-example-domain
spec:
  hostnameOverride: busybox-2.busybox.example.domain
  containers:
  - image: busybox:1.28
    command:
      - sleep
      - "3600"
    name: busybox
```
{{< note >}}
این تنظیم فقط بر نام میزبان درون Pod اثر می‌گذارد و بر رکوردهای A یا AAAA مربوط به Pod در سرور DNS کلاستر تأثیری ندارد.
{{< /note >}}

اگر `hostnameOverride` همراه با فیلدهای `hostname` و `subdomain` تنظیم شود:
* نام میزبان درون Pod با مقدار `hostnameOverride` جایگزین می‌شود.
  
* رکوردهای A و/یا AAAA مربوط به Pod در سرور DNS کلاستر همچنان بر اساس فیلدهای `hostname` و `subdomain` ایجاد می‌شوند.

نکته: اگر `hostnameOverride` تنظیم شده باشد، نمی‌توانید هم‌زمان فیلدهای `hostNetwork` و `setHostnameAsFQDN` را تنظیم کنید. سرور API هر درخواست ایجادی را که چنین ترکیبی داشته باشد، صراحتاً رد می‌کند.

برای آشنایی با جزئیات رفتار سیستم هنگامی که `hostnameOverride` همراه با فیلدهای دیگر (hostname، subdomain، setHostnameAsFQDN، hostNetwork) تنظیم می‌شود، جدول موجود در [جزئیات طراحی KEP-4762](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/4762-allow-arbitrary-fqdn-as-pod-hostname/README.md#design-details ) را ببینید.

---
title: نام میزبان Pod
content_type: concept
weight: 85
---

<!-- overview -->

این صفحه نحوه تنظیم نام میزبان (hostname) یک Pod، عوارض جانبی احتمالی پس از اعمال این پیکربندی و سازوکارهای زیربنایی آن را توضیح می‌دهد.

<!-- body -->

## نام میزبان پیش‌فرض Pod

هنگامی که یک Pod ایجاد می‌شود، نام میزبان آن (آنگونه که از درون Pod مشاهده می‌شود)
از مقدار metadata.name مربوط به Pod گرفته می‌شود.
هم نام میزبان و هم نام دامنه کاملاً معتبر (FQDN) متناظر با آن
(از دیدگاه Pod) برابر با مقدار metadata.name تنظیم می‌شوند.

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
نام میزبان و نام دامنه کاملاً معتبر (FQDN) در Pod ایجادشده با این مانیفست برابر با `busybox-1` خواهد بود.

## نام میزبان با فیلدهای hostname و subdomain در Pod
مشخصات Pod (Pod spec) شامل یک فیلد اختیاری `hostname` است.
در صورت تنظیم، این مقدار به‌عنوان نام میزبان (آنگونه که از درون Pod مشاهده می‌شود)
بر `metadata.name` در Pod اولویت دارد.
برای مثال، نام میزبان در Pod ای که spec.hostname آن روی `my-host` تنظیم شده باشد، `my-host` خواهد بود.

مشخصات Pod همچنین شامل یک فیلد اختیاری `subdomain` است
که نشان می‌دهد Pod به یک زیردامنه در فضای نام (namespace) خود تعلق دارد.
اگر در فضای نام `my-namespace`، مقدار `spec.hostname` برابر با "foo" و مقدار spec.subdomain
برابر با "bar" باشد، نام میزبان Pod برابر با `foo` و نام دامنه کاملاً معتبر (FQDN) آن
برابر با `foo.bar.my-namespace.svc.cluster-domain.example` خواهد بود (آنگونه که از درون Pod مشاهده می‌شود).

هنگامی که هم hostname و هم subdomain تنظیم شده باشند، سرور DNS کلاستر
بر اساس این فیلدها رکوردهای A و/یا AAAA ایجاد می‌کند.
به این بخش مراجعه کنید: [فیلدهای hostname و subdomain در Pod](/docs/concepts/services-networking/dns-pod-service/#pod-hostname-and-subdomain-field).

## نام میزبان با فیلد setHostnameAsFQDN در Pod

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

هنگامی که یک Pod طوری پیکربندی شده باشد که نام دامنه کاملاً معتبر (FQDN) داشته باشد،
نام میزبان آن همان نام میزبان کوتاه است. برای مثال، اگر Pod ای با نام دامنه
کاملاً معتبر `busybox-1.busybox-subdomain.my-namespace.svc.cluster-domain.example` داشته باشید،
به‌طور پیش‌فرض دستور `hostname` درون آن Pod مقدار `busybox-1` را برمی‌گرداند و
دستور `hostname --fqdn` نام FQDN را برمی‌گرداند.

هنگامی که هم `setHostnameAsFQDN: true` و هم فیلد subdomain در مشخصات Pod تنظیم شده باشند،
kubelet نام FQDN مربوط به Pod را
در نام میزبان برای فضای نام آن Pod می‌نویسد. در این حالت، هر دو دستور `hostname` و `hostname --fqdn`
نام FQDN مربوط به Pod را برمی‌گردانند.

نام FQDN مربوط به Pod به همان شیوه‌ای که پیش‌تر تعریف شد ساخته می‌شود.
این نام از فیلد `spec.hostname` در Pod (در صورت مشخص‌شدن) یا `metadata.name`،
همراه با `spec.subdomain`، نام `namespace` و پسوند دامنه کلاستر تشکیل می‌شود.

{{< note >}}
در لینوکس، فیلد نام میزبان در هسته (فیلد `nodename` در `struct utsname`) به ۶۴ کاراکتر محدود است.

اگر Pod ای این قابلیت را فعال کند و طول FQDN آن بیشتر از ۶۴ کاراکتر باشد، شروع به کار نخواهد کرد.
این Pod در وضعیت `Pending` باقی می‌ماند (که در `kubectl` به‌صورت `ContainerCreating` دیده می‌شود)
و رویدادهای خطایی تولید می‌کند، مانند "Failed to construct FQDN from Pod hostname and cluster domain".

این بدان معناست که هنگام استفاده از این فیلد،
باید اطمینان حاصل کنید که مجموع طول فیلدهای `metadata.name` (یا `spec.hostname`)
و `spec.subdomain` در Pod به یک FQDN منجر شود که از ۶۴ کاراکتر بیشتر نباشد.
{{< /note >}}

## نام میزبان با فیلد hostnameOverride در Pod
{{< feature-state feature_gate_name="HostnameOverride" >}}

تنظیم مقدار برای `hostnameOverride` در مشخصات Pod باعث می‌شود kubelet
هم نام میزبان و هم نام دامنه کاملاً معتبر (FQDN) مربوط به Pod را
بدون هیچ قید و شرطی روی مقدار `hostnameOverride` تنظیم کند.

فیلد `hostnameOverride` محدودیت طول ۶۴ کاراکتر دارد
و باید از استاندارد نام‌های زیردامنه DNS که در [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123) تعریف شده است پیروی کند.

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
این تنظیم فقط بر نام میزبان درون Pod تأثیر می‌گذارد؛ بر رکوردهای A یا AAAA مربوط به Pod در سرور DNS کلاستر تأثیری ندارد.
{{< /note >}}

اگر `hostnameOverride` همراه با فیلدهای `hostname` و `subdomain` تنظیم شود:
* نام میزبان درون Pod با مقدار `hostnameOverride` جایگزین می‌شود.
  
* رکوردهای A و/یا AAAA مربوط به Pod در سرور DNS کلاستر همچنان بر اساس فیلدهای `hostname` و `subdomain` تولید می‌شوند.

توجه: اگر `hostnameOverride` تنظیم شده باشد، نمی‌توانید هم‌زمان فیلدهای `hostNetwork` و `setHostnameAsFQDN` را تنظیم کنید.
API server هر درخواست ایجادی را که چنین ترکیبی داشته باشد صراحتاً رد می‌کند.

برای جزئیات مربوط به رفتار هنگامی که `hostnameOverride` همراه با
سایر فیلدها (hostname، subdomain، setHostnameAsFQDN، hostNetwork) تنظیم می‌شود،
جدول موجود در [جزئیات طراحی KEP-4762](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/4762-allow-arbitrary-fqdn-as-pod-hostname/README.md#design-details ) را ببینید.

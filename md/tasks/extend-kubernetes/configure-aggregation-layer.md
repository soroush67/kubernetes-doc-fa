---
title: پیکربندی لایه تجمیع
reviewers:
- lavalamp
- cheftako
- chenopis
content_type: task
weight: 10
---

<!-- overview -->

با پیکربندی [لایه تجمیع](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
می‌توان apiserver کوبرنتیز را با APIهای دیگری گسترش داد که جزو APIهای اصلی کوبرنتیز نیستند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

{{< note >}}
برای اینکه لایه تجمیع در محیط شما کار کند و از احراز هویت TLS متقابل (mutual TLS) میان پراکسی و
apiserverهای افزونه پشتیبانی کند، باید چند پیش‌نیاز را فراهم کنید. کوبرنتیز و kube-apiserver چندین CA دارند؛
بنابراین مطمئن شوید که پراکسی را CA لایه تجمیع امضا کرده است، نه CA دیگری مانند CA عمومی کوبرنتیز.
{{< /note >}}

{{< caution >}}
استفادهٔ دوباره از یک CA برای انواع مختلف کلاینت می‌تواند بر عملکرد کلاستر اثر منفی بگذارد.
برای اطلاعات بیشتر، [استفادهٔ دوباره از CA و تعارض‌ها](#ca-reusage-and-conflicts) را ببینید.
{{< /caution >}}

<!-- steps -->

## جریان احراز هویت

برخلاف تعریف‌های منبع سفارشی (Custom Resource Definitions یا CRDs)، در API تجمیع (Aggregation API)
علاوه بر apiserver استاندارد کوبرنتیز، سرور دیگری نیز دخیل است: apiserver افزونهٔ شما.
لازم است apiserver کوبرنتیز با apiserver افزونهٔ شما ارتباط برقرار کند و apiserver افزونه نیز
با apiserver کوبرنتیز ارتباط داشته باشد. برای ایمن‌سازی این ارتباط، apiserver کوبرنتیز از گواهی‌های x509
برای احراز هویت خود نزد apiserver افزونه استفاده می‌کند.

این بخش توضیح می‌دهد که جریان‌های احراز هویت و مجوزدهی چگونه کار می‌کنند
و چگونه می‌توان آن‌ها را پیکربندی کرد.

جریان کلی به این صورت است:

1. در apiserver کوبرنتیز: احراز هویت کاربر درخواست‌کننده و بررسی مجوز او برای دسترسی به
   مسیر API درخواست‌شده.
2. در apiserver کوبرنتیز: پراکسی کردن درخواست به apiserver افزونه
3. در apiserver افزونه: احراز هویت درخواستی که از apiserver کوبرنتیز رسیده است
4. در apiserver افزونه: مجوزدهی درخواست کاربر اصلی
5. در apiserver افزونه: اجرا

ادامهٔ این بخش این مراحل را با جزئیات شرح می‌دهد.

این جریان را می‌توانید در نمودار زیر ببینید.

![جریان‌های احراز هویت تجمیع](/images/docs/aggregation-api-auth-flow.png)

کد منبع نمودار بالا (swimlanes) در منبع همین سند قرار دارد.

<!--
Swimlanes generated at https://swimlanes.io with the source as follows:

-----BEGIN-----
title: Aggregation API request flow


User -> kube-apiserver / aggregator:

note:
1. The user makes a request to the Kube API server using any recognized credential (e.g. OIDC or client certs)

kube-apiserver / aggregator -> kube-apiserver / aggregator: authentication

note:
2. The Kube API server authenticates the incoming request using any configured
   authentication methods (e.g. OIDC or client certs)

kube-apiserver / aggregator -> kube-apiserver / aggregator: authorization

note:
3. The Kube API server authorizes the requested URL using any configured authorization method (e.g. RBAC)

kube-apiserver / aggregator -> aggregated apiserver:

note:
4. The aggregator opens a connection to the aggregated API server using
   `--proxy-client-cert-file`/`--proxy-client-key-file` client certificate/key to secure the channel
5. The aggregator sends the user info from step 1 to the aggregated API server as
   http headers, as defined by the following flags:
  * `--requestheader-username-headers`
  * `--requestheader-group-headers`
  * `--requestheader-extra-headers-prefix`

aggregated apiserver -> aggregated apiserver: authentication

note:
6. The aggregated apiserver authenticates the incoming request using the auth proxy authentication method:
  * verifies the request has a recognized auth proxy client certificate
  * pulls user info from the incoming request's http headers

By default, it pulls the configuration information for this from a configmap
in the kube-system namespace that is published by the kube-apiserver,
containing the info from the `--requestheader-...` flags provided to the
kube-apiserver (CA bundle to use, auth proxy client certificate names to allow,
http header names to use, etc)

aggregated apiserver -> kube-apiserver / aggregator: authorization

note:
7. The aggregated apiserver authorizes the incoming request by making a
   SubjectAccessReview call to the kube-apiserver

aggregated apiserver -> aggregated apiserver: admission

note:
8. For mutating requests, the aggregated apiserver runs admission checks.
   by default, the namespace lifecycle admission plugin ensures namespaced
   resources are created in a namespace that exists in the kube-apiserver
-----END-----
-->

### احراز هویت و مجوزدهی در apiserver کوبرنتیز

درخواست به مسیری از API که apiserver افزونه به آن سرویس می‌دهد، مانند همهٔ درخواست‌های API
آغاز می‌شود: با برقراری ارتباط با apiserver کوبرنتیز. این مسیر پیش‌تر از سوی apiserver افزونه
در apiserver کوبرنتیز ثبت شده است.

کاربر با apiserver کوبرنتیز ارتباط برقرار می‌کند و درخواست دسترسی به این مسیر را می‌دهد.
سپس apiserver کوبرنتیز با استفاده از سازوکارهای استاندارد احراز هویت و مجوزدهی که برای آن
پیکربندی شده است، هویت کاربر را احراز می‌کند و مجوز دسترسی او به آن مسیر خاص را بررسی می‌کند.

برای مروری بر احراز هویت در یک کلاستر کوبرنتیز،
[«احراز هویت در کلاستر»](/docs/reference/access-authn-authz/authentication/) را ببینید.
برای مروری بر مجوزدهی دسترسی به منابع کلاستر کوبرنتیز،
[«مروری بر مجوزدهی»](/docs/reference/access-authn-authz/authorization/) را ببینید.

تا این مرحله، همه‌چیز همان درخواست‌ها، احراز هویت و مجوزدهی استاندارد API کوبرنتیز بوده است.

اکنون apiserver کوبرنتیز آمادهٔ ارسال درخواست به apiserver افزونه است.

### پراکسی کردن درخواست از سوی apiserver کوبرنتیز

اکنون apiserver کوبرنتیز درخواست را به apiserver افزونه‌ای که برای رسیدگی به آن ثبت شده است
ارسال، یا به بیان دیگر پراکسی (proxy)، می‌کند. برای این کار باید چند چیز را بداند:

1. چگونه apiserver کوبرنتیز باید هویت خود را نزد apiserver افزونه احراز کند و به آن اطلاع دهد
   که درخواستی که از طریق شبکه می‌رسد، از یک apiserver معتبر کوبرنتیز آمده است؟
2. چگونه apiserver کوبرنتیز باید نام کاربری و گروهی را که درخواست اصلی با آن‌ها احراز هویت شده است،
   به apiserver افزونه اطلاع دهد؟

برای فراهم کردن این دو مورد، باید apiserver کوبرنتیز را با چند فلگ پیکربندی کنید.

#### احراز هویت کلاینت در apiserver کوبرنتیز

اتصال apiserver کوبرنتیز به apiserver افزونه از طریق TLS برقرار می‌شود و apiserver کوبرنتیز
با یک گواهی کلاینت هویت خود را احراز می‌کند. هنگام راه‌اندازی apiserver کوبرنتیز باید موارد زیر را
با فلگ‌های مربوط در اختیار آن قرار دهید:

* فایل کلید خصوصی از طریق `--proxy-client-key-file`
* فایل گواهی کلاینت امضاشده از طریق `--proxy-client-cert-file`
* گواهی CA‌ای که فایل گواهی کلاینت را امضا کرده است، از طریق `--requestheader-client-ca-file`
* مقادیر معتبر Common Name (CN) در گواهی کلاینت امضاشده، از طریق `--requestheader-allowed-names`

برای احراز هویت نزد apiserver افزونه، apiserver کوبرنتیز از فایل‌هایی استفاده می‌کند که با
`--proxy-client-*-file` مشخص شده‌اند. برای اینکه یک apiserver افزونهٔ سازگار درخواست را معتبر بداند،
باید شرایط زیر برقرار باشد:

1. اتصال باید با گواهی کلاینتی برقرار شود که CA‌ای آن را امضا کرده باشد که گواهی‌اش
   در `--requestheader-client-ca-file` قرار دارد.
2. اتصال باید با گواهی کلاینتی برقرار شود که CN آن یکی از نام‌های فهرست‌شده
   در `--requestheader-allowed-names` باشد.

{{< note >}}
می‌توانید این گزینه را به‌صورت `--requestheader-allowed-names=""` خالی بگذارید.
با این کار به apiserver افزونه اعلام می‌شود که _هر_ CN‌ای پذیرفتنی است.
{{< /note >}}

وقتی apiserver کوبرنتیز با این گزینه‌ها راه‌اندازی شود:

1. از آن‌ها برای احراز هویت نزد apiserver افزونه استفاده می‌کند.
2. یک configmap با نام `extension-apiserver-authentication` در فضای نام `kube-system` ایجاد می‌کند
   و گواهی CA و CNهای مجاز را در آن قرار می‌دهد. apiserverهای افزونه نیز می‌توانند این اطلاعات را
   بازیابی کنند و برای اعتبارسنجی درخواست‌ها به کار ببرند.

توجه داشته باشید که apiserver کوبرنتیز برای احراز هویت نزد _همهٔ_ apiserverهای افزونه
از یک گواهی کلاینت یکسان استفاده می‌کند. این سرور برای هر apiserver افزونه گواهی کلاینت جداگانه‌ای
نمی‌سازد، بلکه تنها یک گواهی برای احراز هویت در نقش apiserver کوبرنتیز دارد.
همین گواهی برای همهٔ درخواست‌ها به apiserverهای افزونه دوباره استفاده می‌شود.

#### نام کاربری و گروه درخواست اصلی

هنگامی که apiserver کوبرنتیز درخواست را به apiserver افزونه پراکسی می‌کند، نام کاربری و گروهی را
که درخواست اصلی با آن‌ها با موفقیت احراز هویت شده است، به apiserver افزونه اطلاع می‌دهد.
این اطلاعات در هدرهای http درخواست پراکسی‌شده قرار می‌گیرد. شما باید نام هدرهایی را که
باید استفاده شوند به apiserver کوبرنتیز اعلام کنید.

* هدری که نام کاربری در آن ذخیره می‌شود، از طریق `--requestheader-username-headers`
* هدری که گروه در آن ذخیره می‌شود، از طریق `--requestheader-group-headers`
* پیشوندی که به همهٔ هدرهای اضافی افزوده می‌شود، از طریق `--requestheader-extra-headers-prefix`

نام این هدرها نیز در configmap `extension-apiserver-authentication` قرار می‌گیرد
تا apiserverهای افزونه بتوانند آن‌ها را بازیابی و استفاده کنند.

### احراز هویت درخواست در apiserver افزونه

پس از دریافت درخواست پراکسی‌شده از apiserver کوبرنتیز، apiserver افزونه باید اطمینان یابد
که درخواست واقعاً از یک پراکسی احراز هویت معتبر آمده است؛ نقشی که apiserver کوبرنتیز ایفا می‌کند.
اعتبارسنجی در apiserver افزونه به این صورت انجام می‌شود:

1. موارد زیر را، همان‌طور که در بالا توضیح داده شد، از configmap موجود در `kube-system` بازیابی می‌کند:
    * گواهی CA کلاینت
    * فهرست نام‌های مجاز (CNها)
    * نام هدرهای مربوط به نام کاربری، گروه و اطلاعات اضافی
2. بررسی می‌کند که اتصال TLS با گواهی کلاینتی احراز هویت شده باشد که:
    * با CA‌ای امضا شده باشد که گواهی آن با گواهی CA بازیابی‌شده مطابقت دارد.
    * CN آن در فهرست CNهای مجاز باشد، مگر آنکه فهرست خالی باشد؛ در این صورت همهٔ CNها مجازند.
    * نام کاربری و گروه را از هدرهای مربوط استخراج می‌کند.

اگر این بررسی‌ها با موفقیت انجام شوند، درخواست یک درخواست پراکسی‌شدهٔ معتبر از یک پراکسی
احراز هویت مشروع است که در این مورد همان apiserver کوبرنتیز است.

توجه داشته باشید که فراهم کردن موارد بالا بر عهدهٔ پیاده‌سازی apiserver افزونه است.
بسیاری از پیاده‌سازی‌ها با بهره‌گیری از بستهٔ `k8s.io/apiserver/` این کار را به‌طور پیش‌فرض انجام می‌دهند.
برخی دیگر نیز ممکن است گزینه‌هایی در خط فرمان برای بازنویسی آن ارائه دهند.

برای داشتن مجوز بازیابی configmap، apiserver افزونه به نقش (role) مناسب نیاز دارد.
نقشی پیش‌فرض با نام `extension-apiserver-authentication-reader` در فضای نام `kube-system`
وجود دارد که می‌توان آن را تخصیص داد.

### مجوزدهی درخواست در apiserver افزونه

اکنون apiserver افزونه می‌تواند بررسی کند که آیا کاربر/گروهی که از هدرها بازیابی شده است،
مجاز به اجرای درخواست مورد نظر است یا نه. این کار با ارسال یک درخواست استاندارد
[SubjectAccessReview](/docs/reference/access-authn-authz/authorization/)
به apiserver کوبرنتیز انجام می‌شود.

برای اینکه خود apiserver افزونه مجاز به ارسال درخواست `SubjectAccessReview` به apiserver کوبرنتیز باشد،
به مجوزهای درست نیاز دارد. کوبرنتیز یک `ClusterRole` پیش‌فرض با نام `system:auth-delegator` دارد
که مجوزهای لازم را در بر می‌گیرد. می‌توان این نقش را به حساب سرویس (service account) apiserver افزونه اعطا کرد.

### اجرای درخواست در apiserver افزونه

اگر `SubjectAccessReview` با موفقیت انجام شود، apiserver افزونه درخواست را اجرا می‌کند.


## فعال‌سازی فلگ‌های apiserver کوبرنتیز

لایه تجمیع را با فلگ‌های زیر در `kube-apiserver` فعال کنید.
ممکن است ارائه‌دهندهٔ شما پیش‌تر این کار را انجام داده باشد.

    --requestheader-client-ca-file=<path to aggregator CA cert>
    --requestheader-allowed-names=front-proxy-client
    --requestheader-extra-headers-prefix=X-Remote-Extra-
    --requestheader-group-headers=X-Remote-Group
    --requestheader-username-headers=X-Remote-User
    --proxy-client-cert-file=<path to aggregator proxy cert>
    --proxy-client-key-file=<path to aggregator proxy key>

### استفادهٔ دوباره از CA و تعارض‌ها

در apiserver کوبرنتیز دو گزینه برای CA کلاینت وجود دارد:

* گزینهٔ `--client-ca-file`
* گزینهٔ `--requestheader-client-ca-file`

هر یک از این گزینه‌ها مستقل عمل می‌کند و اگر به‌درستی استفاده نشوند،
ممکن است با یکدیگر تعارض پیدا کنند.

* گزینهٔ `--client-ca-file`: وقتی درخواستی به apiserver کوبرنتیز می‌رسد و این گزینه فعال است،
  apiserver کوبرنتیز گواهی درخواست را بررسی می‌کند. اگر گواهی با یکی از گواهی‌های CA موجود
  در فایلی که `--client-ca-file` به آن اشاره دارد امضا شده باشد، درخواست مشروع در نظر گرفته می‌شود؛
  در این حالت کاربر برابر مقدار نام عمومی (common name) `CN=` و گروه برابر سازمان `O=` است.
  [مستندات احراز هویت TLS](/docs/reference/access-authn-authz/authentication/#x509-client-certificates) را ببینید.
* گزینهٔ `--requestheader-client-ca-file`: وقتی درخواستی به apiserver کوبرنتیز می‌رسد و این گزینه فعال است،
  apiserver کوبرنتیز گواهی درخواست را بررسی می‌کند. اگر گواهی با یکی از گواهی‌های CA موجود
  در فایلی که `--requestheader-client-ca-file` به آن اشاره دارد امضا شده باشد، درخواست به‌عنوان
  درخواستی بالقوه مشروع در نظر گرفته می‌شود. سپس apiserver کوبرنتیز بررسی می‌کند که آیا نام عمومی `CN=`
  یکی از نام‌های فهرست ارائه‌شده در `--requestheader-allowed-names` است یا نه.
  اگر نام مجاز باشد، درخواست تأیید می‌شود و در غیر این صورت، تأیید نمی‌شود.

اگر _هر دو_ گزینهٔ `--client-ca-file` و `--requestheader-client-ca-file` ارائه شده باشند،
درخواست ابتدا با CA مربوط به `--requestheader-client-ca-file` و سپس با `--client-ca-file` بررسی می‌شود.
معمولاً برای هر یک از این گزینه‌ها CAهای متفاوتی، چه CA ریشه و چه CA میانی، به کار می‌رود؛
درخواست‌های عادی کلاینت با `--client-ca-file` تطبیق داده می‌شوند و درخواست‌های تجمیع با
`--requestheader-client-ca-file`. اما اگر هر دو از CA _یکسانی_ استفاده کنند، درخواست‌های کلاینتی
که در حالت عادی از طریق `--client-ca-file` پذیرفته می‌شدند، رد خواهند شد؛ زیرا CA با CA موجود در
`--requestheader-client-ca-file` مطابقت دارد، اما نام عمومی `CN=` با هیچ‌یک از نام‌های عمومی پذیرفتنی در
`--requestheader-allowed-names` مطابقت **ندارد**. در نتیجه ممکن است kubeletها و سایر مؤلفه‌های control plane،
و همچنین کاربران نهایی، نتوانند نزد apiserver کوبرنتیز احراز هویت کنند.

به همین دلیل، برای گزینهٔ `--client-ca-file` (برای مجوزدهی به مؤلفه‌های control plane و کاربران نهایی)
و گزینهٔ `--requestheader-client-ca-file` (برای مجوزدهی به درخواست‌های apiserver تجمیع) از گواهی‌های CA متفاوت استفاده کنید.

{{< warning >}}
از CA‌ای که در زمینهٔ دیگری استفاده می‌شود دوباره استفاده **نکنید**، مگر آنکه خطرات آن و
سازوکارهای محافظت از نحوهٔ استفاده از آن CA را به‌خوبی درک کرده باشید.
{{< /warning >}}

اگر kube-proxy را روی میزبانی که API server روی آن اجرا می‌شود اجرا نمی‌کنید،
باید مطمئن شوید که فلگ زیر در `kube-apiserver` فعال شده است:

    --enable-aggregator-routing=true



### ثبت آبجکت‌های APIService

می‌توانید به‌صورت پویا تعیین کنید که کدام درخواست‌های کلاینت به apiserver افزونه پراکسی شوند.
نمونه‌ای از یک ثبت در ادامه آمده است:

```yaml

apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  name: <name of the registration object>
spec:
  group: <API group name this extension apiserver hosts>
  version: <API version this extension apiserver hosts>
  groupPriorityMinimum: <priority this APIService for this group, see API documentation>
  versionPriority: <prioritizes ordering of this version within a group, see API documentation>
  service:
    namespace: <namespace of the extension apiserver service>
    name: <name of the extension apiserver service>
  caBundle: <pem encoded ca cert that signs the server cert used by the webhook>
```

نام هر آبجکت APIService باید یک
[نام بخش مسیر](/docs/concepts/overview/working-with-objects/names#path-segment-names) معتبر باشد.

#### برقراری ارتباط با apiserver افزونه

پس از اینکه apiserver کوبرنتیز تشخیص داد که درخواستی باید به یک apiserver افزونه ارسال شود،
باید بداند چگونه با آن ارتباط برقرار کند.

بخش `service` ارجاعی به سرویس مربوط به apiserver افزونه است.
فضای نام و نام سرویس الزامی هستند. پورت اختیاری است و مقدار پیش‌فرض آن 443 است.

در اینجا نمونه‌ای از یک apiserver افزونه آمده است که طوری پیکربندی شده که روی پورت "1234" فراخوانی شود
و اتصال TLS را با استفاده از یک بستهٔ CA سفارشی در برابر ServerName با مقدار
`my-service-name.my-service-namespace.svc` اعتبارسنجی کند.

```yaml
apiVersion: apiregistration.k8s.io/v1
kind: APIService
...
spec:
  ...
  service:
    namespace: my-service-namespace
    name: my-service-name
    port: 1234
  caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
...
```

## {{% heading "whatsnext" %}}

* [یک api-server افزونه راه‌اندازی کنید](/docs/tasks/extend-kubernetes/setup-extension-api-server/)
  تا با لایه تجمیع کار کند.
* برای مروری کلی،
  [گسترش API کوبرنتیز با لایه تجمیع](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) را ببینید.
* یاد بگیرید چگونه [API کوبرنتیز را با استفاده از Custom Resource Definitions گسترش دهید](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/).

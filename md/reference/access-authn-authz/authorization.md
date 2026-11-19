---
reviewers:
- erictune
- lavalamp
- deads2k
- liggitt
title: مجوزدهی
content_type: concept
weight: 30
description: >
  جزئیات سازوکارهای مجوزدهی در کوبرنتیز و حالت‌های مجوزدهی پشتیبانی‌شده.
---

<!-- overview -->

مجوزدهی (authorization) در کوبرنتیز پس از
[احراز هویت](/docs/reference/access-authn-authz/authentication/) انجام می‌شود.
معمولاً کلاینتی که درخواستی ارسال می‌کند باید پیش از پذیرفته‌شدن درخواستش احراز هویت شده باشد (وارد سیستم شده باشد)؛
با این حال، کوبرنتیز در برخی شرایط درخواست‌های ناشناس را نیز می‌پذیرد.

برای آشنایی کلی با جایگاه مجوزدهی در چارچوب گسترده‌تر کنترل دسترسی به API، صفحهٔ
[کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را بخوانید.

<!-- body -->

## نتیجهٔ مجوزدهی {#determine-whether-a-request-is-allowed-or-denied}

مجوزدهی درخواست‌های API در کوبرنتیز درون سرور API انجام می‌شود.
سرور API همهٔ ویژگی‌های درخواست را با همهٔ سیاست‌ها می‌سنجد، در صورت لزوم با سرویس‌های خارجی نیز مشورت می‌کند
و سپس درخواست را می‌پذیرد یا رد می‌کند.

برای ادامهٔ پردازش، همهٔ بخش‌های یک درخواست API باید به‌وسیلهٔ یکی از سازوکارهای مجوزدهی مجاز شمرده شوند.
به بیان دیگر، دسترسی به‌طور پیش‌فرض ممنوع است.

{{% note %}}
کنترل‌ها و سیاست‌های دسترسی‌ای که به فیلدهای مشخصی از انواع مشخصی از آبجکت‌ها وابسته‌اند،
به‌وسیلهٔ {{< glossary_tooltip text="کنترل‌کننده‌های پذیرش" term_id="admission-controller" >}} اعمال می‌شوند.

کنترل پذیرش در کوبرنتیز پس از پایان مجوزدهی انجام می‌شود (و بنابراین فقط زمانی اجرا می‌شود
که تصمیم مجوزدهی، پذیرفتن درخواست بوده باشد).
{{% /note %}}

وقتی چند [ماژول مجوزدهی](#authorization-modules) پیکربندی شده باشد،
هر کدام به‌ترتیب بررسی می‌شوند.
اگر یکی از مجوزدهنده‌ها درخواست را _تأیید_ یا _رد_ کند، همان تصمیم بی‌درنگ برگردانده می‌شود
و با هیچ مجوزدهندهٔ دیگری مشورت نمی‌شود. اگر هیچ‌یک از ماژول‌ها دربارهٔ درخواست _نظری نداشته باشند_،
درخواست رد می‌شود. نتیجهٔ نهایی «رد» به این معناست که سرور API درخواست را نمی‌پذیرد
و با وضعیت HTTP 403 (Forbidden) پاسخ می‌دهد.

## ویژگی‌های درخواست که در مجوزدهی به کار می‌روند

کوبرنتیز فقط ویژگی‌های زیر را از درخواست API بررسی می‌کند:

 * **کاربر (user)** - رشتهٔ `user` که هنگام احراز هویت ارائه می‌شود.
 * **گروه (group)** - فهرست نام گروه‌هایی که کاربر احراز هویت‌شده عضو آن‌هاست.
 * **اطلاعات اضافی (extra)** - نگاشتی از کلیدهای رشته‌ای دلخواه به مقادیر رشته‌ای که لایهٔ احراز هویت فراهم می‌کند.
 * **‏API** - نشان می‌دهد که آیا درخواست مربوط به یک منبع API است یا نه.
 * **مسیر درخواست** - مسیر نقاط پایانی متفرقه‌ای که منبع نیستند، مانند `/api` یا `/healthz`.
 * **فعل درخواست API** - فعل‌های API مانند `get`، `list`، `create`، `update`، `patch`، `watch`، `delete` و `deletecollection` برای درخواست‌های منبع به کار می‌روند. برای تعیین فعل درخواست در یک نقطهٔ پایانی API منبع، به [فعل‌های درخواست و مجوزدهی](/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) مراجعه کنید.
 * **فعل درخواست HTTP** - متدهای HTTP با حروف کوچک، مانند `get`، `post`، `put` و `delete`، برای درخواست‌هایی به کار می‌روند که به منبع مربوط نیستند.
 * **منبع (Resource)** - شناسه یا نام منبعی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع). برای درخواست‌های منبع با فعل‌های `get`، `update`، `patch` و `delete` باید نام منبع را مشخص کنید.
 * **زیرمنبع (Subresource)** - زیرمنبعی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع). این زیرمنبع می‌تواند یک زیرمنبع استاندارد (مثلاً `status` یا `scale`) یا یک زیرمنبع مصنوعی باشد که برای مجوزدهی دقیق و جزئی به کار می‌رود.
 * **فضای نام (Namespace)** - فضای نام آبجکتی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبعِ وابسته به فضای نام).
 * **گروه API** - {{< glossary_tooltip text="گروه API" term_id="api-group" >}} که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع). رشتهٔ خالی نشان‌دهندهٔ [گروه API](/docs/reference/using-api/#api-groups) _هسته_ (core) است.

### فعل‌های درخواست و مجوزدهی {#determine-the-request-verb}

#### درخواست‌های غیرمنبع {#request-verb-non-resource}

درخواست‌هایی که به نقاط پایانی‌ای غیر از `/api/v1/...` یا `/apis/<group>/<version>/...` ارسال می‌شوند،
_درخواست‌های غیرمنبع_ به شمار می‌آیند و متد HTTP درخواست را با حروف کوچک به‌عنوان فعل به کار می‌برند.
برای نمونه، ارسال درخواست `GET` از طریق HTTP به نقاط پایانی‌ای مانند `/api` یا `/healthz` از فعل **get** استفاده می‌کند.

#### درخواست‌های منبع {#request-verb-resource}

کوبرنتیز برای تعیین فعل درخواست در یک نقطهٔ پایانی API منبع، فعل HTTP به‌کاررفته را نگاشت می‌کند
و در نظر می‌گیرد که آیا درخواست روی یک منبع منفرد عمل می‌کند یا روی مجموعه‌ای از منابع:

فعل HTTP     | فعل درخواست
--------------|---------------
`POST`        | **create**
`GET`، `HEAD` | **get** (برای منابع منفرد)، **list** (برای مجموعه‌ها، شامل محتوای کامل آبجکت)، **watch** (برای پایش یک منبع منفرد یا مجموعه‌ای از منابع)
`PUT`         | **update**
`PATCH`       | **patch**
`DELETE`      | **delete** (برای منابع منفرد)، **deletecollection** (برای مجموعه‌ها)

{{< caution >}}
+فعل‌های **get**، **list** و **watch** همگی می‌توانند جزئیات کامل یک منبع را برگردانند. این فعل‌ها
از نظر دسترسی به داده‌های برگردانده‌شده با هم برابرند. برای نمونه، فعل **list** روی `secrets`
ویژگی‌های **data** همهٔ منابع برگردانده‌شده را آشکار می‌کند.
{{< /caution >}}

کوبرنتیز گاهی مجوزهای اضافی را با فعل‌های ویژه‌ای بررسی می‌کند. برای نمونه:

* حالت‌های خاص [احراز هویت](/docs/reference/access-authn-authz/authentication/)
  * فعل **impersonate** روی `users`، `groups` و `serviceaccounts` در گروه API هسته، و روی `userextras` در گروه API `authentication.k8s.io`.
* [مجوزدهی CertificateSigningRequestها](/docs/reference/access-authn-authz/certificate-signing-requests/#authorization)
  * فعل **approve** برای CertificateSigningRequestها و فعل **update** برای بازنگری در تأییدهای موجود
* [‏RBAC](/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping)
  * فعل‌های **bind** و **escalate** روی منابع `roles` و `clusterroles` در گروه API `rbac.authorization.k8s.io`.
* [تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
  * زیرمنبع‌های مصنوعی مانند `resourceclaims/binding` و `resourceclaims/driver` در گروه API `resource.k8s.io`.
  * فعل‌های آگاه از نود مانند `associated-node:update`، `associated-node:patch`، `arbitrary-node:update` و `arbitrary-node:patch` برای به‌روزرسانی‌های `resourceclaims/status` به‌وسیلهٔ درایور DRA.
* [حذف اجباری منابع خراب](/docs/reference/using-api/api-concepts/#force-deletion)
  * فعل **unsafe-delete-ignore-read-errors** روی منبع، که افزون بر فعل **delete** بررسی می‌شود.

## بستر مجوزدهی

کوبرنتیز انتظار دارد درخواست‌ها ویژگی‌هایی داشته باشند که در درخواست‌های REST API مشترک‌اند. به همین دلیل،
مجوزدهی کوبرنتیز با سامانه‌های کنترل دسترسی موجود در سطح سازمان یا ارائه‌دهندهٔ ابری سازگار است؛
سامانه‌هایی که ممکن است افزون بر API کوبرنتیز، APIهای دیگری را نیز مدیریت کنند.

## حالت‌های مجوزدهی {#authorization-modules}

سرور API کوبرنتیز می‌تواند با یکی از چند حالت مجوزدهی زیر به یک درخواست مجوز بدهد:

`AlwaysAllow`
: این حالت همهٔ درخواست‌ها را می‌پذیرد و همین امر [خطرهای امنیتی](#warning-always-allow) به همراه دارد. فقط زمانی از این حالت مجوزدهی استفاده کنید که به مجوزدهی برای درخواست‌های API خود نیازی ندارید (مثلاً برای آزمایش).

`AlwaysDeny`
: این حالت همهٔ درخواست‌ها را مسدود می‌کند. از این حالت مجوزدهی فقط برای آزمایش استفاده کنید.

`ABAC` ([کنترل دسترسی مبتنی بر ویژگی](/docs/reference/access-authn-authz/abac/))
: حالت ABAC در کوبرنتیز الگویی برای کنترل دسترسی تعریف می‌کند که در آن حقوق دسترسی از طریق سیاست‌هایی به کاربران داده می‌شود که چند ویژگی را با هم ترکیب می‌کنند. این سیاست‌ها می‌توانند از هر نوع ویژگی استفاده کنند (ویژگی‌های کاربر، ویژگی‌های منبع، آبجکت، ویژگی‌های محیط و غیره).

`RBAC` ([کنترل دسترسی مبتنی بر نقش](/docs/reference/access-authn-authz/rbac/))
: ‏RBAC در کوبرنتیز روشی برای تنظیم دسترسی به منابع رایانه‌ای یا شبکه‌ای بر پایهٔ نقش هر کاربر در یک سازمان است. در این بستر، دسترسی یعنی توانایی یک کاربر برای انجام یک کار مشخص، مانند مشاهده، ایجاد یا تغییر یک فایل.  
  در این حالت، کوبرنتیز تصمیم‌های مجوزدهی را بر پایهٔ گروه API `rbac.authorization.k8s.io` می‌گیرد و به این ترتیب می‌توانید سیاست‌های مجوز را به‌صورت پویا و از طریق API کوبرنتیز پیکربندی کنید.

`Node`
: حالت مجوزدهی ویژه‌ای که بر پایهٔ Podهایی که برای اجرا روی هر kubelet زمان‌بندی شده‌اند، به kubeletها مجوز می‌دهد. برای آشنایی بیشتر با حالت مجوزدهی Node، به [مجوزدهی Node](/docs/reference/access-authn-authz/node/) مراجعه کنید.

`Webhook`
: [حالت webhook](/docs/reference/access-authn-authz/webhook/) برای مجوزدهی در کوبرنتیز، یک فراخوانی همگام HTTP انجام می‌دهد و درخواست را تا زمانی که سرویس HTTP راه‌دور به پرس‌وجو پاسخ دهد، معطل نگه می‌دارد. می‌توانید نرم‌افزار خودتان را برای رسیدگی به این فراخوانی بنویسید یا از راهکارهای موجود در اکوسیستم استفاده کنید.

<a id="warning-always-allow" />

{{< warning >}}
فعال‌کردن حالت `AlwaysAllow` مجوزدهی را دور می‌زند؛ از این حالت در کلاستری که به **همهٔ** کلاینت‌های
احتمالی API، از جمله بارهای کاری که خودتان اجرا می‌کنید، اعتماد ندارید استفاده نکنید.

سازوکارهای مجوزدهی معمولاً نتیجهٔ _رد_ یا _بی‌نظر_ برمی‌گردانند؛ برای اطلاعات بیشتر به
[نتیجهٔ مجوزدهی](#determine-whether-a-request-is-allowed-or-denied) مراجعه کنید.
فعال‌کردن `AlwaysAllow` به این معناست که اگر همهٔ مجوزدهنده‌های دیگر نتیجهٔ «بی‌نظر» برگردانند،
درخواست پذیرفته می‌شود. برای نمونه، `--authorization-mode=AlwaysAllow,RBAC` همان اثر
`--authorization-mode=AlwaysAllow` را دارد، زیرا RBAC در کوبرنتیز قاعدهٔ دسترسی منفی (رد) ارائه نمی‌دهد.

در کلاستر کوبرنتیزی که سرور API آن از اینترنت عمومی در دسترس است، نباید از حالت `AlwaysAllow` استفاده کنید.
{{< /warning >}}

### گروه system:masters

گروه `system:masters` یک گروه داخلی کوبرنتیز است که دسترسی نامحدود به سرور API می‌دهد.
هر کاربری که به این گروه افزوده شود، از همهٔ امتیازهای مدیر کلاستر برخوردار است و همهٔ محدودیت‌های مجوزدهی
اعمال‌شده به‌وسیلهٔ سازوکارهای RBAC یا Webhook را دور می‌زند.
[از افزودن کاربران](/docs/concepts/security/rbac-good-practices/#least-privilege)
به این گروه خودداری کنید. اگر واقعاً لازم است حقوق cluster-admin را به کاربری بدهید، می‌توانید یک
[ClusterRoleBinding](/docs/reference/access-authn-authz/rbac/#user-facing-roles)
به ClusterRole داخلی `cluster-admin` ایجاد کنید.

### پیکربندی حالت مجوزدهی {#choice-of-authz-config}

زنجیرهٔ مجوزدهنده‌های سرور API کوبرنتیز را می‌توانید یا فقط با
یک [فایل پیکربندی](#using-configuration-file-for-authorization) یا با
[آرگومان‌های خط فرمان](#using-flags-for-your-authorization-module) پیکربندی کنید.

باید یکی از این دو روش پیکربندی را برگزینید؛ تعیین مسیر `--authorization-config`
و هم‌زمان پیکربندی یک webhook مجوزدهی با آرگومان‌های خط فرمان `--authorization-mode` و
`--authorization-webhook-*` مجاز نیست.
اگر چنین کنید، سرور API هنگام راه‌اندازی پیام خطا گزارش می‌دهد و بی‌درنگ خارج می‌شود.

<!-- keep legacy hyperlinks working -->
<a id="configuring-the-api-server-using-an-authorization-config-file" />

### پیکربندی سرور API با فایل پیکربندی مجوزدهی {#using-configuration-file-for-authorization}

{{< feature-state feature_gate_name="StructuredAuthorizationConfiguration" >}}

کوبرنتیز به شما امکان می‌دهد زنجیره‌های مجوزدهی‌ای پیکربندی کنید که می‌توانند چند webhook را دربر گیرند.
اجزای مجوزدهی در این زنجیره می‌توانند پارامترهای کاملاً تعریف‌شده‌ای داشته باشند که درخواست‌ها را
با ترتیبی مشخص اعتبارسنجی می‌کنند و کنترل دقیق و جزئی، مانند رد صریح در صورت بروز خطا، در اختیارتان می‌گذارند.

روش فایل پیکربندی حتی امکان تعریف قواعد [CEL](/docs/reference/using-api/cel/) را فراهم می‌کند
تا درخواست‌ها پیش از ارسال به webhookها پیش‌پالایش شوند و از فراخوانی‌های غیرضروری جلوگیری شود.
افزون بر این، هرگاه فایل پیکربندی تغییر کند، سرور API زنجیرهٔ مجوزدهنده‌ها را به‌طور خودکار دوباره بارگذاری می‌کند.

مسیر فایل پیکربندی مجوزدهی را با آرگومان خط فرمان
`--authorization-config` مشخص می‌کنید.

اگر بخواهید به‌جای فایل پیکربندی از آرگومان‌های خط فرمان استفاده کنید، این نیز روشی معتبر و پشتیبانی‌شده است.
برخی از قابلیت‌های مجوزدهی (مانند چند webhook، سیاست خطای webhook و قواعد پیش‌پالایش)
فقط در صورت استفاده از فایل پیکربندی مجوزدهی در دسترس‌اند.

#### نمونهٔ پیکربندی {#authz-config-example}

{{< highlight yaml "linenos=false,hl_lines=2-4" >}}
---
#
# این پیکربندی را بدون تغییر استفاده نکنید. این فقط یک نمونه است.
#
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  - type: Webhook
    # نامی که برای توصیف مجوزدهنده به کار می‌رود
    # این نام به‌طور صریح در سازوکار پایش برای معیارها (metrics) استفاده می‌شود
    # نکته:
    #   - اعتبارسنجی این فیلد مشابه شیوهٔ کنونی اعتبارسنجی برچسب‌های کوبرنتیز است.
    # الزامی، بدون مقدار پیش‌فرض
    name: webhook
    webhook:
      # مدت زمان نگهداری پاسخ‌های «مجاز» مجوزدهندهٔ webhook
      # در حافظهٔ نهان.
      # معادل تنظیم پرچم `--authorization-webhook-cache-authorized-ttl`
      # پیش‌فرض: 5m0s
      authorizedTTL: 30s
      # اگر false باشد، پاسخ‌های «مجاز» webhook در حافظهٔ نهان نگه داشته نمی‌شوند
      # و مقدار authorizedTTL تعیین‌شده نادیده گرفته می‌شود و اثری ندارد.
      # معادل تنظیم پرچم `--authorization-webhook-cache-authorized-ttl` روی `0`.
      # نکته: تنظیم authorizedTTL روی `0` باعث می‌شود مقدار پیش‌فرض آن به کار رود.
      # پیش‌فرض: true
      cacheAuthorizedRequests: true
      # مدت زمان نگهداری پاسخ‌های «غیرمجاز» مجوزدهندهٔ webhook
      # در حافظهٔ نهان.
      # معادل تنظیم پرچم `--authorization-webhook-cache-unauthorized-ttl`
      # پیش‌فرض: 30s
      unauthorizedTTL: 30s
      # اگر false باشد، پاسخ‌های «غیرمجاز» webhook در حافظهٔ نهان نگه داشته نمی‌شوند
      # و مقدار unauthorizedTTL تعیین‌شده نادیده گرفته می‌شود و اثری ندارد.
      # معادل تنظیم پرچم `--authorization-webhook-cache-unauthorized-ttl` روی `0`.
      # نکته: تنظیم unauthorizedTTL روی `0` باعث می‌شود مقدار پیش‌فرض آن به کار رود.
      # پیش‌فرض: true
      cacheUnauthorizedRequests: true
      # مهلت زمانی درخواست webhook
      # حداکثر مقدار مجاز 30s است.
      # الزامی، بدون مقدار پیش‌فرض.
      timeout: 3s
      # نسخهٔ API منبع SubjectAccessReview از گروه authorization.k8s.io که
      # به webhook ارسال می‌شود و از آن انتظار می‌رود.
      # معادل تنظیم پرچم `--authorization-webhook-version`
      # الزامی، بدون مقدار پیش‌فرض
      # مقادیر معتبر: v1beta1، v1
      subjectAccessReviewVersion: v1
      # فیلد MatchConditionSubjectAccessReviewVersion نسخه‌ای از SubjectAccessReview را
      # مشخص می‌کند که عبارت‌های CEL بر پایهٔ آن ارزیابی می‌شوند
      # مقادیر معتبر: v1
      # الزامی، بدون مقدار پیش‌فرض
      matchConditionSubjectAccessReviewVersion: v1
      # تصمیم مجوزدهی را در زمانی کنترل می‌کند که درخواست webhook کامل نشود،
      # پاسخی نادرست برگرداند یا ارزیابی matchConditions
      # با خطا روبه‌رو شود.
      # مقادیر معتبر:
      #   - NoOpinion: به مجوزدهنده‌های بعدی برو تا ببینی آیا یکی از
      #     آن‌ها درخواست را می‌پذیرد یا نه
      #   - Deny: درخواست را بدون مشورت با مجوزدهنده‌های بعدی رد کن
      # الزامی، بدون مقدار پیش‌فرض.
      failurePolicy: Deny
      connectionInfo:
        # شیوهٔ ارتباط webhook با سرور را کنترل می‌کند.
        # مقادیر معتبر:
        # - KubeConfigFile: از فایل مشخص‌شده در kubeConfigFile برای یافتن
        #   سرور استفاده کن.
        # - InClusterConfig: از پیکربندی درون‌کلاستری برای فراخوانی
        #   API ‏SubjectAccessReview که kube-apiserver میزبان آن است استفاده کن. این حالت
        #   برای kube-apiserver مجاز نیست.
        type: KubeConfigFile
        # مسیر KubeConfigFile برای اطلاعات اتصال
        # در صورتی که connectionInfo.Type برابر KubeConfigFile باشد، الزامی است
        kubeConfigFile: /kube-system-authz-webhook.yaml
        # فیلد matchConditions فهرستی از شرط‌هاست که برای ارسال یک درخواست به این
        # webhook باید برقرار باشند. فهرست خالی matchConditions با همهٔ درخواست‌ها مطابقت دارد.
        # حداکثر ۶۴ شرط تطبیق مجاز است.
        #
        # منطق دقیق تطبیق (به‌ترتیب) چنین است:
        #   1. اگر دست‌کم یکی از matchConditionها به FALSE ارزیابی شود، webhook نادیده گرفته می‌شود.
        #   2. اگر همهٔ matchConditionها به TRUE ارزیابی شوند، webhook فراخوانی می‌شود.
        #   3. اگر دست‌کم یکی از matchConditionها به خطا ارزیابی شود (اما هیچ‌کدام FALSE نباشد):
        #      - اگر failurePolicy=Deny باشد، webhook درخواست را رد می‌کند
        #      - اگر failurePolicy=NoOpinion باشد، خطا نادیده گرفته می‌شود و webhook کنار گذاشته می‌شود
      matchConditions:
      # فیلد expression عبارتی است که CEL آن را ارزیابی می‌کند. نتیجهٔ ارزیابی باید bool باشد.
      # عبارت‌های CEL به محتوای SubjectAccessReview در نسخهٔ v1 دسترسی دارند.
      # اگر نسخهٔ تعیین‌شده در subjectAccessReviewVersion برای متغیر request برابر v1beta1 باشد،
      # محتوا پیش از ارزیابی عبارت CEL به نسخهٔ v1 تبدیل می‌شود.
      #
      # مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/
      #
      # فقط درخواست‌های منبع را به webhook بفرست
      - expression: has(request.resourceAttributes)
      # فقط درخواست‌های مربوط به kube-system را رهگیری کن
      - expression: request.resourceAttributes.namespace == 'kube-system'
      # درخواست‌های حساب‌های سرویس kube-system را رهگیری نکن
      - expression: "!('system:serviceaccounts:kube-system' in request.groups)"
  - type: Node
    name: node
  - type: RBAC
    name: rbac
  - type: Webhook
    name: in-cluster-authorizer
    webhook:
      authorizedTTL: 5m
      unauthorizedTTL: 30s
      timeout: 3s
      subjectAccessReviewVersion: v1
      failurePolicy: NoOpinion
      connectionInfo:
        type: InClusterConfig
{{< /highlight >}}

هنگام پیکربندی زنجیرهٔ مجوزدهنده‌ها با فایل پیکربندی، مطمئن شوید که محتوای این فایل
در همهٔ نودهای control plane یکسان است. هنگام ارتقا یا بازگشت به نسخهٔ قبلی کلاسترها،
به پیکربندی سرور API توجه کنید. برای نمونه، اگر از کوبرنتیز {{< skew currentVersionAddMinor -1 >}}
به کوبرنتیز {{< skew currentVersion >}} ارتقا می‌دهید، باید پیش از ارتقای کلاستر مطمئن شوید که فایل پیکربندی
در قالبی است که کوبرنتیز {{< skew currentVersion >}} آن را می‌فهمد. اگر به نسخهٔ {{< skew currentVersionAddMinor -1 >}}
بازمی‌گردید، باید پیکربندی را متناسب با آن تنظیم کنید.

#### پیکربندی مجوزدهی و بارگذاری مجدد

هرگاه سرور API تغییری در فایل پیکربندی مجوزدهی مشاهده کند، کوبرنتیز آن را دوباره بارگذاری می‌کند؛
اگر هیچ رویداد تغییری مشاهده نشود نیز این کار هر ۶۰ ثانیه یک‌بار انجام می‌شود.

{{< note >}}
باید اطمینان حاصل کنید که همهٔ انواع مجوزدهنده‌های غیر webhook در فایل، هنگام بارگذاری مجدد بدون تغییر باقی می‌مانند.

بارگذاری مجدد **نباید** مجوزدهنده‌های Node یا RBAC را اضافه یا حذف کند (می‌توان ترتیب آن‌ها را تغییر داد،
اما نمی‌توان آن‌ها را اضافه یا حذف کرد).
{{< /note >}}

### پیکربندی حالت مجوزدهی از طریق خط فرمان {#using-flags-for-your-authorization-module}

می‌توانید از حالت‌های زیر استفاده کنید:

* `--authorization-mode=ABAC` (حالت کنترل دسترسی مبتنی بر ویژگی (Attribute-based access control))
* `--authorization-mode=RBAC` (حالت کنترل دسترسی مبتنی بر نقش (Role-based access control))
* `--authorization-mode=Node` (مجوزدهندهٔ نود)
* `--authorization-mode=Webhook` (حالت مجوزدهی Webhook)
* `--authorization-mode=AlwaysAllow` (درخواست‌ها را همیشه مجاز می‌کند و [خطرات امنیتی](#warning-always-allow) به همراه دارد)
* `--authorization-mode=AlwaysDeny` (درخواست‌ها را همیشه رد می‌کند)

می‌توانید بیش از یک حالت مجوزدهی انتخاب کنید؛ برای مثال:
`--authorization-mode=Node,RBAC,Webhook`

کوبرنتیز ماژول‌های مجوزدهی را به همان ترتیبی بررسی می‌کند که آن‌ها را در خط فرمان سرور API مشخص کرده‌اید؛ بنابراین ماژولی که زودتر آمده باشد، برای مجاز کردن یا رد کردن یک درخواست اولویت بالاتری دارد.

نمی‌توانید آرگومان خط فرمان `--authorization-mode` را با آرگومان خط فرمان `--authorization-config` ترکیب کنید؛ این آرگومان برای [پیکربندی مجوزدهی با استفاده از یک فایل محلی](#using-configuration-file-for-authorization) به کار می‌رود.

برای اطلاعات بیشتر دربارهٔ آرگومان‌های خط فرمان سرور API، [مرجع `kube-apiserver`](/docs/reference/command-line-tools-reference/kube-apiserver/) را بخوانید.

## افزایش سطح دسترسی از طریق ایجاد یا ویرایش بار کاری {#privilege-escalation-via-pod-creation}

کاربرانی که می‌توانند در یک فضای نام (namespace) پادها را ایجاد یا ویرایش کنند، چه به‌طور مستقیم و چه از طریق آبجکتی که [مدیریت بار کاری](/docs/concepts/architecture/controller/) را به‌صورت غیرمستقیم ممکن می‌سازد، ممکن است بتوانند سطح دسترسی خود را در آن فضای نام افزایش دهند. از جمله مسیرهای احتمالی افزایش سطح دسترسی، [افزونه‌های API](/docs/concepts/extend-kubernetes/#api-extensions) کوبرنتیز و {{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌های" >}} مرتبط با آن‌ها هستند.

{{< caution >}}
اگر مدیر کلاستر هستید، در اعطای دسترسی برای ایجاد یا ویرایش بارهای کاری احتیاط کنید.
برخی از جزئیات مربوط به نحوهٔ سوءاستفاده از این دسترسی‌ها در
[مسیرهای افزایش سطح دسترسی](/docs/reference/access-authn-authz/authorization/#escalation-paths) مستند شده است.
{{< /caution >}}

### مسیرهای افزایش سطح دسترسی {#escalation-paths}

اگر به یک مهاجم یا کاربر غیرقابل‌اعتماد اجازه دهید پادهای دلخواه را در یک فضای نام اجرا کند، او از راه‌های مختلفی می‌تواند دسترسی بیشتری در آن فضای نام به دست آورد:

- سوار کردن (mount) Secretهای دلخواه در آن فضای نام
  - می‌توان از آن برای دسترسی به اطلاعات محرمانه‌ای استفاده کرد که برای بارهای کاری دیگر در نظر گرفته شده است
  - می‌توان از آن برای به دست آوردن توکن حساب سرویسِ یک ServiceAccount با سطح دسترسی بالاتر استفاده کرد
- استفاده از ServiceAccountهای دلخواه در آن فضای نام
  - می‌توان عملیات API کوبرنتیز را به‌جای یک بار کاری دیگر انجام داد (جعل هویت)
  - می‌توان هر عملیات دارای امتیاز ویژه‌ای را که آن ServiceAccount مجاز به انجامش است، انجام داد
- سوار کردن یا استفاده از ConfigMapهایی که برای بارهای کاری دیگر در آن فضای نام در نظر گرفته شده‌اند
  - می‌توان از آن برای به دست آوردن اطلاعاتی مانند نام میزبان پایگاه داده استفاده کرد که برای بارهای کاری دیگر در نظر گرفته شده است.
- سوار کردن حجم‌هایی (volume) که برای بارهای کاری دیگر در آن فضای نام در نظر گرفته شده‌اند
  - می‌توان از آن برای به دست آوردن اطلاعات متعلق به بارهای کاری دیگر و تغییر آن استفاده کرد.

{{< caution >}}
اگر مدیر سیستم هستید، هنگام استقرار CustomResourceDefinitionهایی که به کاربران اجازهٔ ایجاد تغییر در موارد بالا را می‌دهند، باید محتاط باشید. این کار ممکن است مسیرهایی برای افزایش سطح دسترسی باز کند.
هنگام تصمیم‌گیری دربارهٔ کنترل‌های مجوزدهی، پیامدهای این نوع تغییرات را بسنجید.
{{< /caution >}}

## بررسی دسترسی به API

ابزار `kubectl` زیرفرمان `auth can-i` را برای پرس‌وجوی سریع از لایهٔ مجوزدهی API فراهم می‌کند.
این فرمان با استفاده از API `SelfSubjectAccessReview` تعیین می‌کند که آیا کاربر فعلی می‌تواند عمل مشخصی را انجام دهد یا نه، و صرف‌نظر از حالت مجوزدهی مورد استفاده کار می‌کند.


```bash
kubectl auth can-i create deployments --namespace dev
```

خروجی مشابه زیر است:

```
yes
```

```shell
kubectl auth can-i create deployments --namespace prod
```

خروجی مشابه زیر است:

```
no
```

مدیران می‌توانند این فرمان را با [جعل هویت کاربر](/docs/reference/access-authn-authz/authentication/#user-impersonation) ترکیب کنند تا مشخص شود کاربران دیگر چه اعمالی را می‌توانند انجام دهند.

```bash
kubectl auth can-i list secrets --namespace dev --as dave
```

خروجی مشابه زیر است:

```
no
```

به همین ترتیب، برای بررسی اینکه آیا یک ServiceAccount با نام `dev-sa` در فضای نام `dev` می‌تواند پادهای فضای نام `target` را فهرست کند یا نه:

```bash
kubectl auth can-i list pods \
    --namespace target \
    --as system:serviceaccount:dev:dev-sa
```

خروجی مشابه زیر است:

```
yes
```

منبع SelfSubjectAccessReview بخشی از گروه API `authorization.k8s.io` است که مجوزدهی سرور API را در اختیار سرویس‌های خارجی قرار می‌دهد. منابع دیگر این گروه عبارت‌اند از:

SubjectAccessReview
: بررسی دسترسی برای هر کاربری، نه فقط کاربر فعلی. این منبع برای واگذاری تصمیم‌های مجوزدهی به سرور API مفید است. برای مثال، kubelet و سرورهای API افزونه از آن برای تعیین دسترسی کاربر به APIهای خود استفاده می‌کنند.

LocalSubjectAccessReview
: مانند SubjectAccessReview است، اما به یک فضای نام مشخص محدود می‌شود.

SelfSubjectRulesReview
: بررسی‌ای که مجموعهٔ اعمالی را که یک کاربر می‌تواند در یک فضای نام انجام دهد، برمی‌گرداند. این منبع به کاربران کمک می‌کند تا خلاصه‌ای سریع از دسترسی‌های خود به دست آورند، و به رابط‌های کاربری امکان می‌دهد اعمال را پنهان یا نمایش دهند.

برای پرس‌وجو از این APIها کافی است منابع عادی کوبرنتیز را ایجاد کنید؛ در این حالت، فیلد `status` در پاسخِ آبجکت برگشتی، نتیجهٔ پرس‌وجو است. برای مثال:

```bash
kubectl create -f - -o yaml << EOF
apiVersion: authorization.k8s.io/v1
kind: SelfSubjectAccessReview
spec:
  resourceAttributes:
    group: apps
    resource: deployments
    verb: create
    namespace: dev
EOF
```

آبجکت SelfSubjectAccessReview تولیدشده مشابه زیر است:

{{< highlight yaml "linenos=false,hl_lines=11-13" >}}
apiVersion: authorization.k8s.io/v1
kind: SelfSubjectAccessReview
metadata:
  creationTimestamp: null
spec:
  resourceAttributes:
    group: apps
    resource: deployments
    namespace: dev
    verb: create
status:
  allowed: true
  denied: false
{{< /highlight >}}

## {{% heading "whatsnext" %}}

* برای آشنایی بیشتر با احراز هویت، [احراز هویت](/docs/reference/access-authn-authz/authentication/) را ببینید.
* برای یک نمای کلی، [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را بخوانید.
* برای آشنایی بیشتر با کنترل پذیرش (Admission Control)، [استفاده از کنترل‌کننده‌های پذیرش](/docs/reference/access-authn-authz/admission-controllers/) را ببینید.
* دربارهٔ [زبان عبارت مشترک (CEL) در کوبرنتیز](/docs/reference/using-api/cel/) بیشتر بخوانید.

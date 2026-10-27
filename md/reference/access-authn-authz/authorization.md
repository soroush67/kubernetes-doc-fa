---
reviewers:
- erictune
- lavalamp
- deads2k
- liggitt
title: احراز مجوز (Authorization)
content_type: concept
weight: 30
description: >
  جزئیات سازوکارهای احراز مجوز در کوبرنتیز و حالت‌های پشتیبانی‌شده‌ی احراز مجوز.
---

<!-- overview -->

احراز مجوز (authorization) در کوبرنتیز پس از
[احراز هویت](/docs/reference/access-authn-authz/authentication/) انجام می‌شود.
معمولاً کلاینتی که درخواستی ارسال می‌کند باید پیش از پذیرفته‌شدن درخواستش
احراز هویت شده (وارد سامانه شده) باشد؛ با این حال، کوبرنتیز در برخی شرایط
درخواست‌های ناشناس را نیز مجاز می‌داند.

برای مشاهده‌ی نمای کلی از جایگاه احراز مجوز در چارچوب گسترده‌تر کنترل دسترسی به API،
[کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را مطالعه کنید.

<!-- body -->

## نتایج احراز مجوز {#determine-whether-a-request-is-allowed-or-denied}

احراز مجوز درخواست‌های API در کوبرنتیز درون API server انجام می‌شود.
API server تمام ویژگی‌های درخواست را با تمام سیاست‌ها ارزیابی می‌کند،
در صورت لزوم از سرویس‌های خارجی نیز استعلام می‌گیرد، و سپس درخواست را مجاز یا ردشده اعلام می‌کند.

برای آنکه یک درخواست API ادامه یابد، تمام بخش‌های آن باید توسط
یک سازوکار احراز مجوز مجاز شمرده شوند. به بیان دیگر: دسترسی به‌طور پیش‌فرض ممنوع است.

{{% note %}}
کنترل‌های دسترسی و سیاست‌هایی که
به فیلدهای مشخصی از انواع مشخصی از آبجکت‌ها وابسته‌اند، توسط
{{< glossary_tooltip text="admission controllerها" term_id="admission-controller" >}}
مدیریت می‌شوند.

کنترل پذیرش (admission control) در کوبرنتیز پس از تکمیل احراز مجوز انجام می‌شود
(و بنابراین فقط زمانی که تصمیم احراز مجوز، اجازه‌ی درخواست بوده باشد).
{{% /note %}}

وقتی چندین [ماژول احراز مجوز](#authorization-modules) پیکربندی شده باشند،
هر یک به‌ترتیب بررسی می‌شود.
اگر هر یک از authorizerها درخواستی را _تأیید_ یا _رد_ کند، آن تصمیم بلافاصله
بازگردانده می‌شود و از هیچ authorizer دیگری استعلام نمی‌شود. اگر همه‌ی ماژول‌ها
درباره‌ی درخواست _نظری نداشته باشند_ (no opinion)، درخواست رد می‌شود. نتیجه‌ی کلی رد به این معناست که
API server درخواست را نمی‌پذیرد و با وضعیت HTTP 403 (Forbidden) پاسخ می‌دهد.

## ویژگی‌های درخواست که در احراز مجوز استفاده می‌شوند

کوبرنتیز فقط ویژگی‌های زیر از درخواست API را بررسی می‌کند:

 * **user** - رشته‌ی `user` که هنگام احراز هویت ارائه شده است.
 * **group** - فهرست نام گروه‌هایی که کاربر احراز هویت‌شده به آن‌ها تعلق دارد.
 * **extra** - نگاشتی از کلیدهای رشته‌ای دلخواه به مقادیر رشته‌ای که توسط لایه‌ی احراز هویت ارائه می‌شود.
 * **API** - مشخص می‌کند که آیا درخواست برای یک منبع API است یا خیر.
 * **Request path** - مسیر نقاط پایانی متفرقه‌ی غیر منبعی مانند `/api` یا `/healthz`.
 * **API request verb** - فعل‌های API مانند `get`، `list`، `create`، `update`، `patch`، `watch`، `delete` و `deletecollection` برای درخواست‌های منبع استفاده می‌شوند. برای تعیین فعل درخواست برای یک نقطه‌ی پایانی API منبع، [فعل‌های درخواست و احراز مجوز](/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) را ببینید.
 * **HTTP request verb** - متدهای HTTP با حروف کوچک مانند `get`، `post`، `put` و `delete` برای درخواست‌های غیر منبعی استفاده می‌شوند.
 * **Resource** - شناسه یا نام منبعی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع) -- برای درخواست‌های منبع که از فعل‌های `get`، `update`، `patch` و `delete` استفاده می‌کنند، باید نام منبع را مشخص کنید.
 * **Subresource** - زیرمنبعی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع). این می‌تواند یک زیرمنبع استاندارد (برای مثال `status` یا `scale`) یا یک زیرمنبع مصنوعی (synthetic) باشد که برای احراز مجوز با دقت بالا استفاده می‌شود.
 * **Namespace** - فضای نام آبجکتی که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منابعِ دارای namespace).
 * **API group** - {{< glossary_tooltip text="گروه API" term_id="api-group" >}} که به آن دسترسی پیدا می‌شود (فقط برای درخواست‌های منبع). رشته‌ی خالی نشان‌دهنده‌ی [گروه API](/docs/reference/using-api/#api-groups) _core_ است.

### فعل‌های درخواست و احراز مجوز {#determine-the-request-verb}

#### درخواست‌های غیر منبعی {#request-verb-non-resource}

درخواست‌ها به نقاط پایانی غیر از `/api/v1/...` یا `/apis/<group>/<version>/...`
_درخواست غیر منبعی_ محسوب می‌شوند و از متد HTTP درخواست، با حروف کوچک، به‌عنوان فعل استفاده می‌کنند.
برای مثال، ارسال یک درخواست `GET` با HTTP به نقاط پایانی‌ای مانند `/api` یا `/healthz`، فعل **get** را به کار می‌برد.

#### درخواست‌های منبع {#request-verb-resource}

برای تعیین فعل درخواست برای یک نقطه‌ی پایانی API منبع، کوبرنتیز فعل HTTP به‌کاررفته را نگاشت می‌کند
و بررسی می‌کند که درخواست روی یک منبع منفرد عمل می‌کند یا روی
مجموعه‌ای از منابع:

فعل HTTP     | فعل درخواست
--------------|---------------
`POST`        | **create**
`GET`, `HEAD` | **get** (برای منابع منفرد)، **list** (برای مجموعه‌ها، شامل محتوای کامل آبجکت)، **watch** (برای مشاهده‌ی یک منبع منفرد یا مجموعه‌ای از منابع)
`PUT`         | **update**
`PATCH`       | **patch**
`DELETE`      | **delete** (برای منابع منفرد)، **deletecollection** (برای مجموعه‌ها)

{{< caution >}}
+فعل‌های **get**، **list** و **watch** همگی می‌توانند جزئیات کامل یک منبع را بازگردانند. از نظر
دسترسی به داده‌های بازگردانده‌شده، این فعل‌ها معادل یکدیگرند. برای مثال، **list** روی `secrets`
ویژگی‌های **data** هر یک از منابع بازگردانده‌شده را آشکار می‌کند.
{{< /caution >}}

کوبرنتیز گاهی احراز مجوز را برای مجوزهای اضافی با استفاده از فعل‌های تخصصی بررسی می‌کند. برای مثال:

* موارد خاص [احراز هویت](/docs/reference/access-authn-authz/authentication/)
  * فعل **impersonate** روی `users`، `groups` و `serviceaccounts` در گروه API هسته (core)، و `userextras` در گروه API با نام `authentication.k8s.io`.
* [احراز مجوز CertificateSigningRequests](/docs/reference/access-authn-authz/certificate-signing-requests/#authorization)
  * فعل **approve** برای CertificateSigningRequests، و **update** برای بازنگری‌ها در تأییدهای موجود
* [RBAC](/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping)
  * فعل‌های **bind** و **escalate** روی منابع `roles` و `clusterroles` در گروه API با نام `rbac.authorization.k8s.io`.
* [تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
  * زیرمنابع مصنوعی مانند `resourceclaims/binding` و `resourceclaims/driver` در گروه API با نام `resource.k8s.io`.
  * فعل‌های آگاه از نود مانند `associated-node:update`، `associated-node:patch`، `arbitrary-node:update` و `arbitrary-node:patch` برای به‌روزرسانی‌های `resourceclaims/status` توسط درایور DRA.
* [حذف اجباری منابع معیوب](/docs/reference/using-api/api-concepts/#force-deletion)
  * فعل **unsafe-delete-ignore-read-errors** روی منبع، که علاوه بر فعل **delete** بررسی می‌شود.

## بافت احراز مجوز

کوبرنتیز ویژگی‌هایی را انتظار دارد که میان درخواست‌های REST API مشترک هستند. این بدان معناست
که احراز مجوز در کوبرنتیز با سامانه‌های کنترل دسترسیِ موجود در سطح سازمان یا
ارائه‌دهنده‌ی ابری کار می‌کند؛ سامانه‌هایی که ممکن است علاوه بر API کوبرنتیز،
APIهای دیگری را نیز مدیریت کنند.

## حالت‌های احراز مجوز {#authorization-modules}

API server کوبرنتیز می‌تواند یک درخواست را با یکی از چند حالت احراز مجوز، مجاز اعلام کند:

`AlwaysAllow`
: این حالت تمام درخواست‌ها را مجاز می‌کند که [ریسک‌های امنیتی](#warning-always-allow) به همراه دارد. این حالت احراز مجوز را فقط زمانی استفاده کنید که برای درخواست‌های API خود به احراز مجوز نیاز ندارید (برای مثال، برای آزمایش).

`AlwaysDeny`
: این حالت تمام درخواست‌ها را مسدود می‌کند. این حالت احراز مجوز را فقط برای آزمایش استفاده کنید.

`ABAC` ([کنترل دسترسی مبتنی بر ویژگی](/docs/reference/access-authn-authz/abac/))
: حالت ABAC در کوبرنتیز یک الگوی کنترل دسترسی را تعریف می‌کند که در آن حقوق دسترسی از طریق سیاست‌هایی که ویژگی‌ها را با هم ترکیب می‌کنند به کاربران اعطا می‌شود. سیاست‌ها می‌توانند از هر نوع ویژگی (ویژگی‌های کاربر، ویژگی‌های منبع، آبجکت، ویژگی‌های محیطی و غیره) استفاده کنند.

`RBAC` ([کنترل دسترسی مبتنی بر نقش](/docs/reference/access-authn-authz/rbac/))
: RBAC در کوبرنتیز روشی برای تنظیم دسترسی به منابع رایانه‌ای یا شبکه‌ای بر اساس نقش‌های کاربران منفرد در یک سازمان است. در این بافت، دسترسی به معنای توانایی یک کاربر منفرد برای انجام یک کار مشخص است، مانند مشاهده، ایجاد یا تغییر یک فایل.  
  در این حالت، کوبرنتیز از گروه API با نام `rbac.authorization.k8s.io` برای هدایت تصمیم‌های احراز مجوز استفاده می‌کند و به شما اجازه می‌دهد سیاست‌های مجوز را به‌صورت پویا از طریق API کوبرنتیز پیکربندی کنید.

`Node`
: یک حالت احراز مجوز با هدف ویژه که بر اساس Podهایی که قرار است روی kubeletها اجرا شوند، مجوزهایی را به آن‌ها اعطا می‌کند. برای کسب اطلاعات بیشتر درباره‌ی حالت احراز مجوز Node، [احراز مجوز Node](/docs/reference/access-authn-authz/node/) را ببینید.

`Webhook`
: [حالت webhook](/docs/reference/access-authn-authz/webhook/) در کوبرنتیز برای احراز مجوز، یک فراخوانی همگام (synchronous) HTTP انجام می‌دهد و درخواست را تا زمانی که سرویس HTTP راه دور به استعلام پاسخ دهد مسدود می‌کند. می‌توانید نرم‌افزار خودتان را برای مدیریت این فراخوانی بنویسید یا از راه‌حل‌های موجود در اکوسیستم استفاده کنید.

<a id="warning-always-allow" />

{{< warning >}}
فعال‌سازی حالت `AlwaysAllow` احراز مجوز را دور می‌زند؛ از آن در کلاستری که
به **همه‌ی** کلاینت‌های بالقوه‌ی API، از جمله بارهای کاری‌ای که خودتان اجرا می‌کنید، اعتماد ندارید استفاده نکنید.

سازوکارهای احراز مجوز معمولاً نتیجه‌ی _deny_ (رد) یا _no opinion_ (بدون نظر) را بازمی‌گردانند؛
برای اطلاعات بیشتر در این باره به
[نتایج احراز مجوز](#determine-whether-a-request-is-allowed-or-denied) مراجعه کنید.
فعال‌سازی `AlwaysAllow` به این معناست که اگر همه‌ی authorizerهای دیگر «no opinion» بازگردانند،
درخواست مجاز شمرده می‌شود. برای مثال، `--authorization-mode=AlwaysAllow,RBAC`
همان اثر `--authorization-mode=AlwaysAllow` را دارد، زیرا RBAC در کوبرنتیز
قواعد دسترسی منفی (deny) ارائه نمی‌دهد.

حالت `AlwaysAllow` را در کلاستر کوبرنتیزی که API server آن
از اینترنت عمومی در دسترس است استفاده نکنید.
{{< /warning >}}

### گروه system:masters

گروه `system:masters` یک گروه داخلی کوبرنتیز است که دسترسی نامحدود
به API server را اعطا می‌کند. هر کاربری که به این گروه اختصاص داده شود، دارای
همه‌ی امتیازات مدیر کلاستر است و هرگونه محدودیت احراز مجوز اعمال‌شده توسط سازوکارهای RBAC یا Webhook را دور می‌زند.
[از افزودن کاربران](/docs/concepts/security/rbac-good-practices/#least-privilege)
به این گروه پرهیز کنید. اگر نیاز دارید به کاربری حقوق cluster-admin بدهید، می‌توانید یک
[ClusterRoleBinding](/docs/reference/access-authn-authz/rbac/#user-facing-roles)
به ClusterRole داخلی `cluster-admin` ایجاد کنید.

### پیکربندی حالت احراز مجوز {#choice-of-authz-config}

می‌توانید زنجیره‌ی authorizer در API server کوبرنتیز را یا فقط با یک
[فایل پیکربندی](#using-configuration-file-for-authorization) یا با
[آرگومان‌های خط فرمان](#using-flags-for-your-authorization-module) پیکربندی کنید.

باید یکی از این دو رویکرد پیکربندی را انتخاب کنید؛ تنظیم همزمان مسیر `--authorization-config`
و پیکربندی یک authorization webhook با استفاده از آرگومان‌های خط فرمان `--authorization-mode` و
`--authorization-webhook-*` مجاز نیست.
اگر چنین کنید، API server هنگام راه‌اندازی پیام خطا گزارش می‌دهد و بلافاصله خارج می‌شود.

<!-- keep legacy hyperlinks working -->
<a id="configuring-the-api-server-using-an-authorization-config-file" />

### پیکربندی API Server با استفاده از فایل پیکربندی احراز مجوز {#using-configuration-file-for-authorization}

{{< feature-state feature_gate_name="StructuredAuthorizationConfiguration" >}}

کوبرنتیز به شما امکان می‌دهد زنجیره‌های احراز مجوزی پیکربندی کنید که می‌توانند شامل چندین
webhook باشند. آیتم‌های احراز مجوز در آن زنجیره می‌توانند پارامترهای کاملاً تعریف‌شده‌ای داشته باشند که
درخواست‌ها را به ترتیب مشخصی اعتبارسنجی می‌کنند و کنترل دقیقی در اختیار شما می‌گذارند، مانند Deny صریح در صورت بروز خطا.

رویکرد فایل پیکربندی حتی به شما امکان می‌دهد
قواعد [CEL](/docs/reference/using-api/cel/) را برای پیش‌فیلتر کردن درخواست‌ها پیش از ارسال آن‌ها
به webhookها مشخص کنید و به جلوگیری از فراخوانی‌های غیرضروری کمک کنید. همچنین API server به‌طور خودکار
زنجیره‌ی authorizer را هنگام تغییر فایل پیکربندی بازبارگذاری می‌کند.

مسیر پیکربندی احراز مجوز را با استفاده از آرگومان خط فرمان
`--authorization-config` مشخص می‌کنید.

اگر می‌خواهید به‌جای فایل پیکربندی از آرگومان‌های خط فرمان استفاده کنید، این نیز رویکردی معتبر و پشتیبانی‌شده است.
برخی قابلیت‌های احراز مجوز (برای مثال: چندین webhook، سیاست شکست webhook و قواعد پیش‌فیلتر)
فقط در صورتی در دسترس هستند که از فایل پیکربندی احراز مجوز استفاده کنید.

#### نمونه‌ی پیکربندی {#authz-config-example}

{{< highlight yaml "linenos=false,hl_lines=2-4" >}}
---
#
# این پیکربندی را به همین شکل استفاده نکنید. این فقط یک نمونه است.
#
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  - type: Webhook
    # نامی که برای توصیف authorizer استفاده می‌شود
    # این نام به‌صراحت در سازوکار پایش برای متریک‌ها استفاده می‌شود
    # توجه:
    #   - اعتبارسنجی این فیلد مشابه اعتبارسنجی برچسب‌ها (labels) در K8s است.
    # الزامی، بدون مقدار پیش‌فرض
    name: webhook
    webhook:
      # مدت زمان نگهداری پاسخ‌های «authorized» از authorizer مبتنی بر webhook
      # در حافظه‌ی نهان.
      # معادل تنظیم فلگ `--authorization-webhook-cache-authorized-ttl`
      # پیش‌فرض: 5m0s
      authorizedTTL: 30s
      # اگر روی false تنظیم شود، پاسخ‌های «authorized» از webhook در حافظه‌ی نهان
      # ذخیره نمی‌شوند و authorizedTTL مشخص‌شده نادیده گرفته می‌شود/تأثیری ندارد.
      # معادل تنظیم فلگ `--authorization-webhook-cache-authorized-ttl` روی `0`.
      # توجه: تنظیم authorizedTTL روی `0` باعث می‌شود مقدار پیش‌فرض آن استفاده شود.
      # پیش‌فرض: true
      cacheAuthorizedRequests: true
      # مدت زمان نگهداری پاسخ‌های «unauthorized» از authorizer مبتنی بر webhook
      # در حافظه‌ی نهان.
      # معادل تنظیم فلگ `--authorization-webhook-cache-unauthorized-ttl`
      # پیش‌فرض: 30s
      unauthorizedTTL: 30s
      # اگر روی false تنظیم شود، پاسخ‌های «unauthorized» از webhook در حافظه‌ی نهان
      # ذخیره نمی‌شوند و unauthorizedTTL مشخص‌شده نادیده گرفته می‌شود/تأثیری ندارد.
      # معادل تنظیم فلگ `--authorization-webhook-cache-unauthorized-ttl` روی `0`.
      # توجه: تنظیم unauthorizedTTL روی `0` باعث می‌شود مقدار پیش‌فرض آن استفاده شود.
      # پیش‌فرض: true
      cacheUnauthorizedRequests: true
      # مهلت زمانی (timeout) درخواست webhook
      # حداکثر مقدار مجاز 30s است.
      # الزامی، بدون مقدار پیش‌فرض.
      timeout: 3s
      # نسخه‌ی API از SubjectAccessReview در authorization.k8s.io که باید
      # به webhook ارسال شود و از آن انتظار می‌رود.
      # معادل تنظیم فلگ `--authorization-webhook-version`
      # الزامی، بدون مقدار پیش‌فرض
      # مقادیر معتبر: v1beta1, v1
      subjectAccessReviewVersion: v1
      # MatchConditionSubjectAccessReviewVersion نسخه‌ی SubjectAccessReview را مشخص می‌کند
      # که عبارت‌های CEL بر اساس آن ارزیابی می‌شوند
      # مقادیر معتبر: v1
      # الزامی، بدون مقدار پیش‌فرض
      matchConditionSubjectAccessReviewVersion: v1
      # تصمیم احراز مجوز را زمانی کنترل می‌کند که درخواست webhook
      # کامل نشود، پاسخ نامعتبر بازگرداند یا
      # ارزیابی matchConditions با خطا مواجه شود.
      # مقادیر معتبر:
      #   - NoOpinion: ادامه به authorizerهای بعدی تا بررسی شود آیا یکی از
      #     آن‌ها درخواست را مجاز می‌کند
      #   - Deny: رد درخواست بدون استعلام از authorizerهای بعدی
      # الزامی، بدون مقدار پیش‌فرض.
      failurePolicy: Deny
      connectionInfo:
        # نحوه‌ی ارتباط webhook با سرور را کنترل می‌کند.
        # مقادیر معتبر:
        # - KubeConfigFile: از فایل مشخص‌شده در kubeConfigFile برای یافتن
        #   سرور استفاده می‌کند.
        # - InClusterConfig: از پیکربندی درون‌کلاستری برای فراخوانی
        #   API با نام SubjectAccessReview که توسط kube-apiserver ارائه می‌شود استفاده می‌کند.
        #   این حالت برای kube-apiserver مجاز نیست.
        type: KubeConfigFile
        # مسیر KubeConfigFile برای اطلاعات اتصال
        # الزامی، اگر connectionInfo.Type برابر KubeConfigFile باشد
        kubeConfigFile: /kube-system-authz-webhook.yaml
        # matchConditions فهرستی از شرایطی است که برای ارسال یک درخواست به این
        # webhook باید برقرار باشند. فهرست خالی matchConditions با همه‌ی درخواست‌ها مطابقت دارد.
        # حداکثر 64 شرط تطبیق مجاز است.
        #
        # منطق دقیق تطبیق (به ترتیب) چنین است:
        #   1. اگر دست‌کم یک matchCondition به FALSE ارزیابی شود، webhook نادیده گرفته می‌شود.
        #   2. اگر همه‌ی matchConditions به TRUE ارزیابی شوند، webhook فراخوانی می‌شود.
        #   3. اگر دست‌کم یک matchCondition به خطا ارزیابی شود (اما هیچ‌کدام FALSE نباشند):
        #      - اگر failurePolicy=Deny باشد، webhook درخواست را رد می‌کند
        #      - اگر failurePolicy=NoOpinion باشد، خطا نادیده گرفته می‌شود و webhook رد می‌شود
      matchConditions:
      # expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد. باید به bool ارزیابی شود.
      # عبارت‌های CEL به محتوای SubjectAccessReview در نسخه‌ی v1 دسترسی دارند.
      # اگر نسخه‌ی مشخص‌شده توسط subjectAccessReviewVersion در متغیر request برابر v1beta1 باشد،
      # محتوا پیش از ارزیابی عبارت CEL به نسخه‌ی v1 تبدیل می‌شود.
      #
      # مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/
      #
      # فقط درخواست‌های منبع را به webhook ارسال کن
      - expression: has(request.resourceAttributes)
      # فقط درخواست‌ها به kube-system را رهگیری کن
      - expression: request.resourceAttributes.namespace == 'kube-system'
      # درخواست‌های service accountهای kube-system را رهگیری نکن
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

هنگام پیکربندی زنجیره‌ی authorizer با استفاده از فایل پیکربندی، مطمئن شوید که محتوای فایل در تمام
نودهای control plane یکسان است. هنگام ارتقا یا کاهش نسخه‌ی کلاسترها، پیکربندی
API server را در نظر داشته باشید. برای مثال، اگر از
کوبرنتیز {{< skew currentVersionAddMinor -1 >}} به کوبرنتیز {{< skew currentVersion >}} ارتقا می‌دهید،
پیش از ارتقای کلاستر باید مطمئن شوید که فایل پیکربندی در قالبی است که کوبرنتیز {{< skew currentVersion >}}
می‌تواند آن را درک کند. اگر به {{< skew currentVersionAddMinor -1 >}} کاهش نسخه می‌دهید،
باید پیکربندی را به‌طور مناسب تنظیم کنید.

#### پیکربندی احراز مجوز و بازبارگذاری‌ها

کوبرنتیز فایل پیکربندی احراز مجوز را زمانی که API server تغییری در
فایل مشاهده کند، و همچنین در یک زمان‌بندی ۶۰ ثانیه‌ای در صورت عدم مشاهده‌ی رویداد تغییر، بازبارگذاری می‌کند.

{{< note >}}
باید مطمئن شوید که تمام انواع authorizer غیر webhook هنگام بازبارگذاری در فایل بدون تغییر باقی می‌مانند.

یک بازبارگذاری **نباید** authorizerهای Node یا RBAC را اضافه یا حذف کند (می‌توان ترتیب آن‌ها را تغییر داد،
اما نمی‌توان آن‌ها را اضافه یا حذف کرد).
{{< /note >}}

### پیکربندی حالت مجوزدهی از طریق خط فرمان {#using-flags-for-your-authorization-module}

می‌توانید از حالت‌های زیر استفاده کنید:

* `--authorization-mode=ABAC` (حالت کنترل دسترسی مبتنی بر ویژگی)
* `--authorization-mode=RBAC` (حالت کنترل دسترسی مبتنی بر نقش)
* `--authorization-mode=Node` (مجوزدهنده Node)
* `--authorization-mode=Webhook` (حالت مجوزدهی Webhook)
* `--authorization-mode=AlwaysAllow` (همیشه درخواست‌ها را مجاز می‌کند؛ دارای [ریسک‌های امنیتی](#warning-always-allow) است)
* `--authorization-mode=AlwaysDeny` (همیشه درخواست‌ها را رد می‌کند)

می‌توانید بیش از یک حالت مجوزدهی را انتخاب کنید؛ برای مثال:
`--authorization-mode=Node,RBAC,Webhook`

کوبرنتیز ماژول‌های مجوزدهی را بر اساس ترتیبی که در خط فرمان API server مشخص کرده‌اید بررسی می‌کند؛ بنابراین ماژولی که زودتر آمده باشد، برای مجاز کردن یا رد کردن یک درخواست اولویت بالاتری دارد.

نمی‌توانید آرگومان خط فرمان `--authorization-mode` را با آرگومان خط فرمان `--authorization-config` که برای [پیکربندی مجوزدهی با استفاده از یک فایل محلی](#using-configuration-file-for-authorization-mode) به کار می‌رود، ترکیب کنید.

برای اطلاعات بیشتر درباره آرگومان‌های خط فرمان API server، [مرجع `kube-apiserver`](/docs/reference/command-line-tools-reference/kube-apiserver/) را مطالعه کنید.

## افزایش سطح دسترسی از طریق ایجاد یا ویرایش بارهای کاری {#privilege-escalation-via-pod-creation}

کاربرانی که می‌توانند در یک فضای نام (namespace) پادها را ایجاد یا ویرایش کنند، چه به‌صورت مستقیم و چه از طریق آبجکتی که امکان [مدیریت بار کاری](/docs/concepts/architecture/controller/) را به‌صورت غیرمستقیم فراهم می‌کند، ممکن است بتوانند سطح دسترسی خود را در آن فضای نام افزایش دهند. مسیرهای بالقوه افزایش سطح دسترسی شامل [افزونه‌های API](/docs/concepts/extend-kubernetes/#api-extensions) کوبرنتیز و {{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌های" >}} مرتبط با آن‌ها می‌شود.

{{< caution >}}
به‌عنوان مدیر کلاستر، هنگام اعطای دسترسی برای ایجاد یا ویرایش بارهای کاری احتیاط کنید. برخی جزئیات درباره چگونگی سوءاستفاده از این دسترسی‌ها در [مسیرهای افزایش سطح دسترسی](/docs/reference/access-authn-authz/authorization/#escalation-paths) مستند شده است.
{{< /caution >}}

### مسیرهای افزایش سطح دسترسی {#escalation-paths}

اگر به یک مهاجم یا کاربر غیرقابل‌اعتماد اجازه دهید در یک فضای نام Podهای دلخواه اجرا کند، راه‌های مختلفی وجود دارد که او می‌تواند سطح دسترسی بیشتری در آن فضای نام به دست آورد:

- مونت کردن Secretهای دلخواه در آن فضای نام
  - می‌تواند برای دسترسی به اطلاعات محرمانه‌ای که برای سایر بارهای کاری در نظر گرفته شده‌اند، استفاده شود
  - می‌تواند برای به دست آوردن توکن حساب سرویس (service account token) یک ServiceAccount با سطح دسترسی بالاتر استفاده شود
- استفاده از ServiceAccountهای دلخواه در آن فضای نام
  - می‌تواند اقدامات API کوبرنتیز را به‌جای یک بار کاری دیگر انجام دهد (جعل هویت)
  - می‌تواند هر اقدام دارای سطح دسترسی بالا را که آن ServiceAccount مجاز به انجام آن است، انجام دهد
- مونت کردن یا استفاده از ConfigMapهایی که برای سایر بارهای کاری در آن فضای نام در نظر گرفته شده‌اند
  - می‌تواند برای به دست آوردن اطلاعاتی که برای سایر بارهای کاری در نظر گرفته شده‌اند، مانند نام میزبان پایگاه داده، استفاده شود.
- مونت کردن حجم‌هایی (volume) که برای سایر بارهای کاری در آن فضای نام در نظر گرفته شده‌اند
  - می‌تواند برای به دست آوردن اطلاعاتی که برای سایر بارهای کاری در نظر گرفته شده‌اند و تغییر دادن آن‌ها استفاده شود.

{{< caution >}}
به‌عنوان مدیر سیستم، هنگام استقرار CustomResourceDefinitionهایی که به کاربران اجازه می‌دهند در حوزه‌های بالا تغییراتی ایجاد کنند، باید احتیاط کنید. این موارد ممکن است مسیرهای افزایش سطح دسترسی را باز کنند. هنگام تصمیم‌گیری درباره کنترل‌های مجوزدهی، پیامدهای این نوع تغییر را در نظر بگیرید.
{{< /caution >}}

## بررسی دسترسی به API

`kubectl` زیردستور `auth can-i` را برای پرس‌وجوی سریع از لایه مجوزدهی API فراهم می‌کند. این دستور از API با نام `SelfSubjectAccessReview` استفاده می‌کند تا مشخص کند آیا کاربر فعلی می‌تواند اقدام مشخصی را انجام دهد یا خیر، و بدون توجه به حالت مجوزدهی مورد استفاده کار می‌کند.


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

مدیران می‌توانند این دستور را با [جعل هویت کاربر](/docs/reference/access-authn-authz/authentication/#user-impersonation) ترکیب کنند تا مشخص شود سایر کاربران چه اقداماتی را می‌توانند انجام دهند.

```bash
kubectl auth can-i list secrets --namespace dev --as dave
```

خروجی مشابه زیر است:

```
no
```

به‌طور مشابه، برای بررسی اینکه آیا یک ServiceAccount با نام `dev-sa` در Namespace با نام `dev` می‌تواند Podها را در Namespace با نام `target` فهرست کند:

```bash
kubectl auth can-i list pods \
    --namespace target \
    --as system:serviceaccount:dev:dev-sa
```

خروجی مشابه زیر است:

```
yes
```

SelfSubjectAccessReview بخشی از گروه API با نام `authorization.k8s.io` است که مجوزدهی API server را در اختیار سرویس‌های خارجی قرار می‌دهد. سایر منابع این گروه عبارتند از:

SubjectAccessReview
: بررسی دسترسی برای هر کاربر، نه فقط کاربر فعلی. برای واگذاری تصمیم‌های مجوزدهی به API server مفید است. برای مثال، kubelet و API serverهای افزونه از این منبع برای تعیین دسترسی کاربر به APIهای خود استفاده می‌کنند.

LocalSubjectAccessReview
: مانند SubjectAccessReview است، اما به یک فضای نام (namespace) مشخص محدود می‌شود.

SelfSubjectRulesReview
: بررسی‌ای که مجموعه اقداماتی را که یک کاربر می‌تواند در یک فضای نام انجام دهد، برمی‌گرداند. برای اینکه کاربران بتوانند به‌سرعت دسترسی خود را خلاصه کنند، یا برای اینکه رابط‌های کاربری بتوانند اقدامات را پنهان یا نمایش دهند، مفید است.

این APIها را می‌توان با ایجاد منابع معمولی کوبرنتیز پرس‌وجو کرد، به‌طوری که فیلد `status` در پاسخ آبجکت بازگشتی، نتیجه پرس‌وجو است. برای مثال:

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

SelfSubjectAccessReview تولیدشده مشابه زیر است:

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

* برای کسب اطلاعات بیشتر درباره احراز هویت، [احراز هویت](/docs/reference/access-authn-authz/authentication/) را ببینید.
* برای دریافت یک نمای کلی، [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را مطالعه کنید.
* برای کسب اطلاعات بیشتر درباره Admission Control، [استفاده از Admission Controllerها](/docs/reference/access-authn-authz/admission-controllers/) را ببینید.
* درباره [Common Expression Language در کوبرنتیز](/docs/reference/using-api/cel/) بیشتر بخوانید.

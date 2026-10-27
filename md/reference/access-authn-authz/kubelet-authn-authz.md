---
reviewers:
- liggitt
title: احراز هویت و مجوزدهی Kubelet
weight: 110
---


## نمای کلی {#overview}

نقطه پایانی HTTPS مربوط به kubelet، APIهایی را در اختیار می‌گذارد که به داده‌هایی با سطوح حساسیت متفاوت دسترسی می‌دهند
و امکان انجام عملیاتی با سطوح قدرت متفاوت را روی نود و درون کانتینرها فراهم می‌کنند.

این سند توضیح می‌دهد که چگونه دسترسی به نقطه پایانی HTTPS مربوط به kubelet را احراز هویت و مجوزدهی کنید.

## احراز هویت Kubelet

به‌طور پیش‌فرض، درخواست‌هایی که به نقطه پایانی HTTPS مربوط به kubelet ارسال می‌شوند و توسط سایر روش‌های احراز هویت پیکربندی‌شده رد نمی‌شوند،
به‌عنوان درخواست ناشناس (anonymous) در نظر گرفته می‌شوند و نام کاربری `system:anonymous`
و گروه `system:unauthenticated` به آن‌ها داده می‌شود.

برای غیرفعال کردن دسترسی ناشناس و ارسال پاسخ `401 Unauthorized` به درخواست‌های فاقد احراز هویت:

* kubelet را با فلگ `--anonymous-auth=false` راه‌اندازی کنید

برای فعال‌سازی احراز هویت با گواهی کلاینت X509 در نقطه پایانی HTTPS مربوط به kubelet:

* kubelet را با فلگ `--client-ca-file` راه‌اندازی کنید و یک بسته CA برای اعتبارسنجی گواهی‌های کلاینت در اختیار آن بگذارید
* apiserver را با فلگ‌های `--kubelet-client-certificate` و `--kubelet-client-key` راه‌اندازی کنید
* برای جزئیات بیشتر، [مستندات احراز هویت apiserver](/docs/reference/access-authn-authz/authentication/#x509-client-certificates) را ببینید

برای فعال‌سازی استفاده از توکن‌های bearer در API (از جمله توکن‌های service account) جهت احراز هویت در نقطه پایانی HTTPS مربوط به kubelet:

* مطمئن شوید گروه API با نام `authentication.k8s.io/v1` در API server فعال است
* kubelet را با فلگ‌های `--authentication-token-webhook` و `--kubeconfig` راه‌اندازی کنید
* kubelet برای تعیین اطلاعات کاربر از روی توکن‌های bearer، API با نام `TokenReview` را روی API server پیکربندی‌شده فراخوانی می‌کند

## مجوزدهی Kubelet

هر درخواستی که با موفقیت احراز هویت شود (از جمله درخواست ناشناس)، سپس مجوزدهی می‌شود. حالت پیش‌فرض مجوزدهی `AlwaysAllow` است که همه درخواست‌ها را مجاز می‌کند.

دلایل متعددی برای تفکیک دسترسی به API مربوط به kubelet وجود دارد:

* احراز هویت ناشناس فعال است، اما توانایی کاربران ناشناس برای فراخوانی API مربوط به kubelet باید محدود شود
* احراز هویت با توکن bearer فعال است، اما توانایی کاربران دلخواه API (مانند service accountها) برای فراخوانی API مربوط به kubelet باید محدود شود
* احراز هویت با گواهی کلاینت فعال است، اما فقط برخی از گواهی‌های کلاینتی که توسط CA پیکربندی‌شده امضا شده‌اند باید اجازه استفاده از API مربوط به kubelet را داشته باشند

برای تفکیک دسترسی به API مربوط به kubelet، مجوزدهی را به API server واگذار کنید:

* مطمئن شوید گروه API با نام `authorization.k8s.io/v1` در API server فعال است
* kubelet را با فلگ‌های `--authorization-mode=Webhook` و `--kubeconfig` راه‌اندازی کنید
* kubelet برای تعیین اینکه هر درخواست مجاز است یا خیر، API با نام `SubjectAccessReview` را روی API server پیکربندی‌شده فراخوانی می‌کند

kubelet درخواست‌های API را با همان رویکرد [ویژگی‌های درخواست](/docs/reference/access-authn-authz/authorization/#review-your-request-attributes) که apiserver به کار می‌برد، مجوزدهی می‌کند.

فعل (verb) از روی فعل HTTP درخواست ورودی تعیین می‌شود:

فعل HTTP | فعل درخواست
----------|---------------
POST      | create
GET, HEAD | get
PUT       | update
PATCH     | patch
DELETE    | delete

منبع (resource) و زیرمنبع (subresource) از روی مسیر درخواست ورودی تعیین می‌شوند:

Kubelet API         | resource | subresource
--------------------|----------|------------
/stats/\*           | nodes    | stats
/metrics/\*         | nodes    | metrics
/logs/\*            | nodes    | log
/spec/\*            | nodes    | spec
/checkpoint/\*      | nodes    | checkpoint
*همه موارد دیگر*    | nodes    | proxy

<a name="get-nodes-proxy-warning"></a>
{{< warning >}}
مجوز `nodes/proxy` به همه APIهای دیگر kubelet دسترسی می‌دهد.
این شامل APIهایی است که می‌توان از آن‌ها برای اجرای دستورها در هر کانتینری که روی نود در حال اجراست استفاده کرد.

برخی از این نقاط پایانی از طریق درخواست‌های HTTP `GET` از پروتکل‌های Websocket پشتیبانی می‌کنند و با فعل **get** مجوزدهی می‌شوند.
این بدان معناست که مجوز **get** روی `nodes/proxy` یک مجوز فقط‌خواندنی نیست
و اجرای دستورها در هر کانتینری که روی نود در حال اجراست را مجاز می‌کند.
{{< /warning >}}

ویژگی‌های فضای نام (namespace) و گروه API همیشه رشته خالی هستند و
نام منبع همیشه نام آبجکت API از نوع `Node` مربوط به kubelet است.

هنگام اجرا در این حالت، مطمئن شوید کاربری که با فلگ‌های `--kubelet-client-certificate` و `--kubelet-client-key`
به apiserver داده شده است، برای ویژگی‌های زیر مجوز دارد:

* verb=\*, resource=nodes, subresource=proxy
* verb=\*, resource=nodes, subresource=stats
* verb=\*, resource=nodes, subresource=log
* verb=\*, resource=nodes, subresource=spec
* verb=\*, resource=nodes, subresource=metrics

### مجوزدهی ریزدانه {#fine-grained-authorization}

{{< feature-state feature_gate_name="KubeletFineGrainedAuthz" >}}

kubelet پیش از بازگشت به زیرمنبع `proxy` برای نقاط پایانی `/pods`، `/runningPods`، `/configz` و `/healthz`،
یک بررسی ریزدانه انجام می‌دهد. منبع و زیرمنبع از روی مسیر درخواست ورودی تعیین می‌شوند:

Kubelet API   | resource | subresource
--------------|----------|------------
/stats/\*     | nodes    | stats
/metrics/\*   | nodes    | metrics
/logs/\*      | nodes    | log
/pods         | nodes    | pods, proxy
/runningPods/ | nodes    | pods, proxy
/healthz      | nodes    | healthz, proxy
/configz      | nodes    | configz, proxy 
*همه موارد دیگر* | nodes    | proxy


هنگامی که feature gate با نام `KubeletFineGrainedAuthz` فعال است، مطمئن شوید کاربری که با فلگ‌های
`--kubelet-client-certificate` و `--kubelet-client-key`
به API server داده شده است، برای ویژگی‌های زیر مجوز دارد:

* verb=\*, resource=nodes, subresource=proxy
* verb=\*, resource=nodes, subresource=stats
* verb=\*, resource=nodes, subresource=log
* verb=\*, resource=nodes, subresource=metrics
* verb=\*, resource=nodes, subresource=configz
* verb=\*, resource=nodes, subresource=healthz
* verb=\*, resource=nodes, subresource=pods

اگر از [مجوزدهی RBAC](/docs/reference/access-authn-authz/rbac/) استفاده می‌شود،
فعال کردن این gate همچنین تضمین می‌کند که ClusterRole داخلی `system:kubelet-api-admin`
با مجوزهای دسترسی به همه زیرمنابع یادشده به‌روزرسانی می‌شود.

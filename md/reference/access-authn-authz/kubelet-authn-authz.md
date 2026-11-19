---
reviewers:
- liggitt
title: احراز هویت و مجوزدهی kubelet
weight: 110
---


## مرور کلی

نقطهٔ پایانی HTTPS هر kubelet مجموعه‌ای از APIها را در دسترس قرار می‌دهد که به داده‌هایی با سطوح حساسیت متفاوت دسترسی می‌دهند. این APIها همچنین امکان انجام عملیاتی با سطوح اختیار متفاوت را روی نود و درون کانتینرها فراهم می‌کنند.

این سند توضیح می‌دهد که چگونه دسترسی به نقطهٔ پایانی HTTPS مربوط به kubelet را احراز هویت (authentication) و مجوزدهی (authorization) کنید.

## احراز هویت kubelet

به‌طور پیش‌فرض، درخواست‌هایی به نقطهٔ پایانی HTTPS مربوط به kubelet که روش‌های احراز هویت پیکربندی‌شدهٔ دیگر آن‌ها را رد نکنند، درخواست ناشناس (anonymous) در نظر گرفته می‌شوند. به این درخواست‌ها نام کاربری `system:anonymous` و گروه `system:unauthenticated` اختصاص داده می‌شود.

برای غیرفعال کردن دسترسی ناشناس و ارسال پاسخ `401 Unauthorized` به درخواست‌های احراز هویت‌نشده:

* kubelet را با فلگ `--anonymous-auth=false` اجرا کنید

برای فعال کردن احراز هویت با گواهی کلاینت X509 در نقطهٔ پایانی HTTPS مربوط به kubelet:

* kubelet را با فلگ `--client-ca-file` اجرا کنید و یک بستهٔ CA برای اعتبارسنجی گواهی‌های کلاینت در اختیار آن قرار دهید
* apiserver را با فلگ‌های `--kubelet-client-certificate` و `--kubelet-client-key` اجرا کنید
* برای جزئیات بیشتر، [مستندات احراز هویت apiserver](/docs/reference/access-authn-authz/authentication/#x509-client-certificates) را ببینید

برای فعال کردن استفاده از توکن‌های حامل (bearer token) API، از جمله توکن‌های حساب سرویس، جهت احراز هویت در نقطهٔ پایانی HTTPS مربوط به kubelet:

* مطمئن شوید که گروه API ‏`authentication.k8s.io/v1` در سرور API فعال است
* kubelet را با فلگ‌های `--authentication-token-webhook` و `--kubeconfig` اجرا کنید
* ‏kubelet برای تعیین اطلاعات کاربر از روی توکن‌های حامل، API ‏`TokenReview` را روی سرور API پیکربندی‌شده فراخوانی می‌کند

## مجوزدهی kubelet

هر درخواستی که با موفقیت احراز هویت شود (از جمله درخواست ناشناس)، سپس مجوزدهی می‌شود. حالت پیش‌فرض مجوزدهی `AlwaysAllow` است که همهٔ درخواست‌ها را مجاز می‌داند.

دلایل زیادی برای تفکیک دسترسی به API مربوط به kubelet وجود دارد:

* احراز هویت ناشناس فعال است، اما توانایی کاربران ناشناس برای فراخوانی API مربوط به kubelet باید محدود شود
* احراز هویت با توکن حامل فعال است، اما توانایی کاربران دلخواه API (مانند حساب‌های سرویس) برای فراخوانی API مربوط به kubelet باید محدود شود
* احراز هویت با گواهی کلاینت فعال است، اما فقط برخی از گواهی‌های کلاینتِ امضاشده با CA پیکربندی‌شده باید اجازهٔ استفاده از API مربوط به kubelet را داشته باشند

برای تفکیک دسترسی به API مربوط به kubelet، مجوزدهی را به سرور API واگذار کنید:

* مطمئن شوید که گروه API ‏`authorization.k8s.io/v1` در سرور API فعال است
* kubelet را با فلگ‌های `--authorization-mode=Webhook` و `--kubeconfig` اجرا کنید
* ‏kubelet برای تعیین مجاز بودن هر درخواست، API ‏`SubjectAccessReview` را روی سرور API پیکربندی‌شده فراخوانی می‌کند

‏kubelet درخواست‌های API را با همان رویکرد [ویژگی‌های درخواست](/docs/reference/access-authn-authz/authorization/#review-your-request-attributes) که apiserver به کار می‌برد، مجوزدهی می‌کند.

فعل درخواست بر اساس فعل HTTP درخواست ورودی تعیین می‌شود:

فعل HTTP | فعل درخواست
----------|---------------
POST      | create
GET, HEAD | get
PUT       | update
PATCH     | patch
DELETE    | delete

منبع و زیرمنبع بر اساس مسیر درخواست ورودی تعیین می‌شوند:

API مربوط به kubelet | منبع | زیرمنبع
--------------------|----------|------------
/stats/\*           | nodes    | stats
/metrics/\*         | nodes    | metrics
/logs/\*            | nodes    | log
/spec/\*            | nodes    | spec
/checkpoint/\*      | nodes    | checkpoint
*سایر موارد*        | nodes    | proxy

<a name="get-nodes-proxy-warning"></a>
{{< warning >}}
مجوز `nodes/proxy` دسترسی به همهٔ APIهای دیگر kubelet را اعطا می‌کند. این شامل APIهایی است که می‌توان با آن‌ها در هر کانتینری که روی نود در حال اجراست، فرمان اجرا کرد.

برخی از این نقاط پایانی از پروتکل‌های Websocket از طریق درخواست‌های HTTP ‏`GET` پشتیبانی می‌کنند که با فعل **get** مجوزدهی می‌شوند. بنابراین مجوز **get** روی `nodes/proxy` یک مجوز فقط‌خواندنی نیست و اجرای فرمان در هر کانتینری را که روی نود در حال اجراست مجاز می‌کند.
{{< /warning >}}

ویژگی‌های فضای نام (namespace) و گروه API همیشه رشتهٔ خالی هستند و نام منبع همیشه نام آبجکت API ‏`Node` مربوط به همان kubelet است.

هنگام اجرا در این حالت، مطمئن شوید کاربری که با فلگ‌های `--kubelet-client-certificate` و `--kubelet-client-key` ارسال‌شده به apiserver شناسایی می‌شود، برای ویژگی‌های زیر مجوز دارد:

* verb=\*, resource=nodes, subresource=proxy
* verb=\*, resource=nodes, subresource=stats
* verb=\*, resource=nodes, subresource=log
* verb=\*, resource=nodes, subresource=spec
* verb=\*, resource=nodes, subresource=metrics

### مجوزدهی دقیق

{{< feature-state feature_gate_name="KubeletFineGrainedAuthz" >}}

‏kubelet برای نقاط پایانی `/pods`، `/runningPods`، `/configz` و `/healthz`، پیش از بازگشت به زیرمنبع `proxy`، یک بررسی دقیق انجام می‌دهد. منبع و زیرمنبع بر اساس مسیر درخواست ورودی تعیین می‌شوند:

API مربوط به kubelet | منبع | زیرمنبع
--------------|----------|------------
/stats/\*     | nodes    | stats
/metrics/\*   | nodes    | metrics
/logs/\*      | nodes    | log
/pods         | nodes    | pods, proxy
/runningPods/ | nodes    | pods, proxy
/healthz      | nodes    | healthz, proxy
/configz      | nodes    | configz, proxy 
*سایر موارد*  | nodes    | proxy


هنگامی که feature gate ‏`KubeletFineGrainedAuthz` فعال است، مطمئن شوید کاربری که با فلگ‌های `--kubelet-client-certificate` و `--kubelet-client-key` ارسال‌شده به سرور API شناسایی می‌شود، برای ویژگی‌های زیر مجوز دارد:

* verb=\*, resource=nodes, subresource=proxy
* verb=\*, resource=nodes, subresource=stats
* verb=\*, resource=nodes, subresource=log
* verb=\*, resource=nodes, subresource=metrics
* verb=\*, resource=nodes, subresource=configz
* verb=\*, resource=nodes, subresource=healthz
* verb=\*, resource=nodes, subresource=pods

اگر از [مجوزدهی RBAC](/docs/reference/access-authn-authz/rbac/) استفاده می‌شود، فعال کردن این gate همچنین تضمین می‌کند که ClusterRole داخلی `system:kubelet-api-admin` با مجوزهای لازم برای دسترسی به همهٔ زیرمنبع‌های ذکرشده در بالا به‌روزرسانی شود.

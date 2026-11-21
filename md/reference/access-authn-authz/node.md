---
reviewers:
- timstclair
- deads2k
- liggitt
title: استفاده از مجوزدهی نود
content_type: concept
weight: 34
---

<!-- overview -->
مجوزدهی نود (Node authorization) یک حالت مجوزدهی با کاربرد ویژه است که به‌طور خاص درخواست‌های API ارسال‌شده از سوی kubeletها را مجوزدهی می‌کند.


<!-- body -->
## مرور کلی

مجوزدهندهٔ Node به kubelet امکان می‌دهد عملیات API را انجام دهد. این عملیات عبارت‌اند از:

عملیات خواندن:

* سرویس‌ها (services)
* اندپوینت‌ها (endpoints)
* نودها
* پادها (pods)
* سکرت‌ها (secrets)، کانفیگ‌مپ‌ها (configmaps)، درخواست‌های حجم پایدار (persistent volume claims) و حجم‌های پایدار (persistent volumes) مرتبط با پادهایی که به نود kubelet متصل شده‌اند

{{< feature-state feature_gate_name="AuthorizeNodeWithSelectors" >}}

هر kubelet تنها می‌تواند آبجکت Node مربوط به خودش را بخواند و فقط پادهایی را بخواند که به نود خودش متصل شده‌اند.

عملیات نوشتن:

* نودها و وضعیت نود (برای محدود کردن kubelet به تغییر نود خودش، افزونهٔ پذیرش `NodeRestriction` را فعال کنید)
* پادها و وضعیت پاد (برای محدود کردن kubelet به تغییر پادهای متصل به خودش، افزونهٔ پذیرش `NodeRestriction` را فعال کنید)
* رویدادها (events)

عملیات مرتبط با احراز هویت و مجوزدهی:

* دسترسی خواندن/نوشتن به
  [API درخواست‌های امضای گواهی (CertificateSigningRequests)](/docs/reference/access-authn-authz/certificate-signing-requests/)
  برای راه‌اندازی اولیهٔ TLS (TLS bootstrapping)
* توانایی ایجاد TokenReviewها و SubjectAccessReviewها برای بررسی‌های واگذارشدهٔ احراز هویت و مجوزدهی

در نسخه‌های آینده، ممکن است مجوزدهندهٔ نود مجوزهایی را اضافه یا حذف کند تا اطمینان حاصل شود که kubeletها کمینهٔ مجوزهای لازم برای عملکرد درست را در اختیار دارند.

برای اینکه مجوزدهندهٔ Node به kubeletها مجوز بدهد، آن‌ها باید از اعتبارنامه‌ای استفاده کنند که آن‌ها را عضو گروه `system:nodes` و با نام کاربری `system:node:<nodeName>` معرفی کند.
این قالب گروه و نام کاربری با هویتی مطابقت دارد که در جریان
[راه‌اندازی اولیهٔ TLS برای kubelet](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
برای هر kubelet ایجاد می‌شود.

مقدار `<nodeName>` **باید** دقیقاً با نام نودی که kubelet ثبت کرده است مطابقت داشته باشد. به‌طور پیش‌فرض، این مقدار همان نام میزبانی است که دستور `hostname` ارائه می‌دهد، یا مقداری که با
[گزینهٔ kubelet](/docs/reference/command-line-tools-reference/kubelet/)
`--hostname-override` جایگزین آن شده است. با این حال، هنگام استفاده از گزینهٔ `--cloud-provider` در kubelet، ممکن است نام میزبان مشخص را ارائه‌دهندهٔ ابری تعیین کند و در این صورت `hostname` محلی و گزینهٔ `--hostname-override` نادیده گرفته می‌شوند.
برای جزئیات نحوهٔ تعیین نام میزبان توسط kubelet، به
[مرجع گزینه‌های kubelet](/docs/reference/command-line-tools-reference/kubelet/) مراجعه کنید.

برای فعال کردن مجوزدهندهٔ Node، {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
را با فلگ `--authorization-config` اجرا کنید و مقدار آن را فایلی قرار دهید که مجوزدهندهٔ `Node` را در بر دارد؛ برای مثال:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  ...
  - type: Node
  ...
```

یا {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} را با فلگ `--authorization-mode` اجرا کنید و مقدار آن را فهرستی جداشده با ویرگول قرار دهید که `Node` را در بر دارد؛
برای مثال:
```shell
kube-apiserver --authorization-mode=...,Node --other-options --more-options
```

برای محدود کردن آبجکت‌های API که kubeletها می‌توانند بنویسند، افزونهٔ پذیرش
[NodeRestriction](/docs/reference/access-authn-authz/admission-controllers#noderestriction)
را با اجرای apiserver همراه با
`--enable-admission-plugins=...,NodeRestriction,...` فعال کنید.

## محدودیت مخاطب توکن حساب سرویس {#service-account-token-audience-restriction}

{{< feature-state feature_gate_name="ServiceAccountNodeAudienceRestriction" >}}

هنگامی که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction`
فعال و افزونهٔ پذیرش `NodeRestriction` نیز فعال باشد، kubelet تنها می‌تواند برای مخاطبانی (audiences) توکن حساب سرویس درخواست کند که پادهای در حال اجرا روی آن نود از پیش به آن‌ها ارجاع داده‌اند. این کار مانع می‌شود که یک نود به‌خطرافتاده برای مخاطبان دلخواه توکن به دست آورد.

مخاطبان مجاز از روی مشخصات پاد (pod spec) تعیین می‌شوند:

- مخاطب پیش‌فرض سرور API (مقدار خالی یا مخاطب پیکربندی‌شدهٔ سرور API).
- مخاطبانی که در منابع حجم توکن حساب سرویس پروجکت‌شده (projected) تنظیم شده‌اند.
- مخاطبانی که در `spec.tokenRequests` درایور CSI برای هر درایور CSI مورد استفادهٔ پاد پیکربندی شده‌اند؛ چه از طریق حجم‌های CSI درون‌خطی، چه حجم‌های مبتنی بر PersistentVolumeClaim و چه حجم‌های موقت (ephemeral).

این موضوع به‌ویژه هنگام استفاده از [توکن‌های حساب سرویس برای ارائه‌دهندگان اعتبارنامهٔ ایمیج](/docs/tasks/administer-cluster/kubelet-credential-provider/#service-account-token-for-image-pulls) اهمیت دارد؛ در این حالت kubelet از طرف پادها توکن‌هایی با مخاطب مختص رجیستری درخواست می‌کند.

### مجاز کردن مخاطبان اضافی با RBAC {#allowing-additional-audiences}

می‌توانید به kubeletها اجازه دهید برای مخاطبانی فراتر از آنچه در مشخصات پاد ارجاع داده شده است توکن درخواست کنند. هنگامی که kubelet توکنی با مخاطبی درخواست می‌کند که در مشخصات پاد یافت نمی‌شود، افزونهٔ پذیرش NodeRestriction با انجام یک بررسی مجوزدهی با ویژگی‌های زیر، مجاز بودن kubelet را بررسی می‌کند:

| ویژگی  | مقدار |
| ---------- | ----- |
| فعل (Verb)       | `request-serviceaccounts-token-audience` |
| گروه API  | (رشتهٔ خالی، به معنای گروه API هسته) |
| منبع   | مقدار مخاطب درخواست‌شده |
| نام       | نام حساب سرویس |
| فضای نام (namespace)  | فضای نام حساب سرویس |

می‌توانید برای مجوزدهی به این بررسی‌ها از قواعد استاندارد RBAC استفاده کنید. فیلد `resources` تعیین می‌کند کدام مخاطبان مجاز هستند و فیلد `resourceNames` تعیین می‌کند قاعده روی کدام حساب‌های سرویس اعمال شود.

برای مثال، برای اینکه kubelet بتواند برای یک حساب سرویس مشخص، مخاطب `my-registry-audience` را درخواست کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-audience-my-registry
rules:
- verbs: ["request-serviceaccounts-token-audience"]
  apiGroups: [""]
  resources: ["my-registry-audience"]
  resourceNames: ["my-service-account"]
```

حذف `resourceNames` این مخاطب را برای همهٔ حساب‌های سرویس مجاز می‌کند. استفاده از نویسهٔ عام (`"*"`) برای `resources` هر مخاطبی را مجاز می‌کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-audience-unrestricted
rules:
- verbs: ["request-serviceaccounts-token-audience"]
  apiGroups: [""]
  resources: ["*"]  # any audience
  # no resourceNames: any service account
```

برای اعمال این ClusterRole روی همهٔ kubeletها، آن را به گروه `system:nodes` متصل کنید:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: node-audience-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: node-audience-my-registry
subjects:
- kind: Group
  name: system:nodes
  apiGroup: rbac.authorization.k8s.io
```

{{< note >}}
این محدودیت بخشی از افزونهٔ پذیرش NodeRestriction است و تنها برای هویت‌های نود (kubeletها) اعمال می‌شود. این محدودیت تعیین نمی‌کند که سایر فراخوانندگان API `TokenRequest` چه مخاطبانی را می‌توانند درخواست کنند. اگر لازم است سایر فراخوانندگان را محدود کنید، استفاده از [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) را بررسی کنید.
{{< /note >}}

## ملاحظات مهاجرت

### kubeletهای خارج از گروه `system:nodes`

حالت مجوزدهی `Node` به kubeletهایی که عضو گروه `system:nodes` نیستند مجوز نمی‌دهد و این kubeletها باید همچنان با هر سازوکاری که در حال حاضر به آن‌ها مجوز می‌دهد، مجوزدهی شوند.
افزونهٔ پذیرش نود درخواست‌های این kubeletها را محدود نمی‌کند.

### kubeletهایی با نام‌های کاربری غیرمتمایز

در برخی استقرارها، kubeletها اعتبارنامه‌هایی دارند که آن‌ها را در گروه `system:nodes` قرار می‌دهد، اما نود مشخصی را که به آن مرتبط هستند معرفی نمی‌کند، زیرا نام کاربری آن‌ها در قالب `system:node:...` نیست.
حالت مجوزدهی `Node` به این kubeletها مجوز نمی‌دهد و آن‌ها باید همچنان با هر سازوکاری که در حال حاضر به آن‌ها مجوز می‌دهد، مجوزدهی شوند.

افزونهٔ پذیرش `NodeRestriction` درخواست‌های این kubeletها را نادیده می‌گیرد، زیرا پیاده‌سازی پیش‌فرض شناسهٔ نود آن را هویت نود به شمار نمی‌آورد.

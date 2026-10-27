---
reviewers:
- timstclair
- deads2k
- liggitt
title: استفاده از Node Authorization
content_type: concept
weight: 34
---

<!-- overview -->
Node authorization یک حالت مجوزدهی با کاربرد ویژه است که به‌طور اختصاصی درخواست‌های API را که توسط kubeletها ارسال می‌شوند، مجاز می‌کند.


<!-- body -->
## مرور کلی {#overview}

Node authorizer به kubelet اجازه می‌دهد عملیات API را انجام دهد. این عملیات شامل موارد زیر است:

عملیات خواندن:

* services
* endpoints
* nodes
* pods
* secrets، configmaps، persistent volume claims و persistent volumeهای مرتبط
  با پادهایی که به نود kubelet متصل (bound) شده‌اند

{{< feature-state feature_gate_name="AuthorizeNodeWithSelectors" >}}

kubeletها فقط به خواندن آبجکت‌های Node مربوط به خودشان و فقط به خواندن پادهایی که به نود آن‌ها متصل شده‌اند محدود می‌شوند.

عملیات نوشتن:

* nodes و وضعیت node (افزونه admission با نام `NodeRestriction` را فعال کنید تا
  kubelet فقط بتواند نود خودش را تغییر دهد)
* pods و وضعیت pod (افزونه admission با نام `NodeRestriction` را فعال کنید تا
  kubelet فقط بتواند پادهای متصل به خودش را تغییر دهد)
* events

عملیات مرتبط با احراز هویت و مجوزدهی:

* دسترسی خواندن/نوشتن به
  [CertificateSigningRequests API](/docs/reference/access-authn-authz/certificate-signing-requests/)
  برای TLS bootstrapping
* قابلیت ایجاد TokenReview و SubjectAccessReview برای بررسی‌های احراز هویت/مجوزدهی تفویض‌شده

در نسخه‌های آینده، node authorizer ممکن است مجوزهایی را اضافه یا حذف کند تا اطمینان حاصل شود
kubeletها حداقل مجموعه مجوزهای لازم برای عملکرد صحیح را دارند.

برای آنکه kubeletها توسط Node authorizer مجاز شناخته شوند، باید از اعتبارنامه‌ای (credential) استفاده کنند
که آن‌ها را عضو گروه `system:nodes` با نام کاربری `system:node:<nodeName>` معرفی کند.
قالب این گروه و نام کاربری با هویتی که برای هر kubelet در جریان
[TLS bootstrapping مربوط به kubelet](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
ایجاد می‌شود، مطابقت دارد.

مقدار `<nodeName>` **باید** دقیقاً با نام نودی که توسط kubelet ثبت شده است مطابقت داشته باشد. به‌طور پیش‌فرض، این مقدار همان نام میزبان (host name) است که توسط `hostname` ارائه می‌شود، یا با
[گزینه kubelet](/docs/reference/command-line-tools-reference/kubelet/)
با نام `--hostname-override` بازنویسی می‌شود. با این حال، هنگام استفاده از گزینه
`--cloud-provider` در kubelet، ممکن است نام میزبان مشخص توسط ارائه‌دهنده ابر (cloud provider) تعیین شود و `hostname` محلی و گزینه `--hostname-override` نادیده گرفته شوند.
برای جزئیات بیشتر درباره نحوه تعیین نام میزبان توسط kubelet، به
[مرجع گزینه‌های kubelet](/docs/reference/command-line-tools-reference/kubelet/) مراجعه کنید.

برای فعال‌سازی Node authorizer، {{< glossary_tooltip text="API server" term_id="kube-apiserver" >}} را
با فلگ `--authorization-config` اجرا کنید و آن را روی فایلی تنظیم کنید که شامل authorizer با نوع `Node` باشد؛ برای مثال:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  ...
  - type: Node
  ...
```

یا {{< glossary_tooltip text="API server" term_id="kube-apiserver" >}} را با
فلگ `--authorization-mode` اجرا کنید و آن را روی فهرستی جداشده با ویرگول که شامل `Node` است تنظیم کنید؛
برای مثال:
```shell
kube-apiserver --authorization-mode=...,Node --other-options --more-options
```

برای محدود کردن آبجکت‌های API که kubeletها می‌توانند بنویسند، افزونه admission با نام
[NodeRestriction](/docs/reference/access-authn-authz/admission-controllers#noderestriction)
را با اجرای apiserver همراه با
`--enable-admission-plugins=...,NodeRestriction,...`
فعال کنید.

## محدودسازی audience توکن service account {#service-account-token-audience-restriction}

{{< feature-state feature_gate_name="ServiceAccountNodeAudienceRestriction" >}}

زمانی که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction`
فعال باشد و افزونه admission با نام `NodeRestriction` نیز فعال باشد، kubelet فقط می‌تواند
توکن‌های service account را برای audienceهایی درخواست کند که پیش‌تر توسط پادهای در حال اجرا
روی همان نود ارجاع داده شده‌اند. این کار از دریافت توکن برای audienceهای دلخواه توسط یک نود در معرض خطر (compromised) جلوگیری می‌کند.

audienceهای مجاز از روی مشخصات pod تعیین می‌شوند:

- audience پیش‌فرض API server (خالی یا audience پیکربندی‌شده در API server).
- audienceهای تعیین‌شده در منابع حجم توکن service account از نوع projected.
- audienceهای پیکربندی‌شده در `spec.tokenRequests` مربوط به درایور CSI برای هر درایور CSI که
  توسط pod استفاده می‌شود، چه از طریق حجم‌های CSI درون‌خطی (inline)، چه حجم‌های مبتنی بر PersistentVolumeClaim
  و چه حجم‌های ephemeral.

این موضوع به‌ویژه هنگام استفاده از [توکن‌های service account برای ارائه‌دهندگان اعتبارنامه ایمیج](/docs/tasks/administer-cluster/kubelet-credential-provider/#service-account-token-for-image-pulls)
اهمیت دارد، جایی که kubelet از طرف پادها توکن‌هایی را با audience مختص registry درخواست می‌کند.

### مجاز کردن audienceهای اضافی با RBAC {#allowing-additional-audiences}

می‌توانید به kubeletها اجازه دهید توکن‌هایی را برای audienceهایی فراتر از آنچه در
مشخصات pod ارجاع داده شده است درخواست کنند. هنگامی که kubelet توکنی را با audienceای درخواست می‌کند که
در مشخصات pod یافت نمی‌شود، افزونه admission با نام NodeRestriction با انجام یک بررسی مجوزدهی
با ویژگی‌های زیر بررسی می‌کند که آیا kubelet مجاز است یا خیر:

| ویژگی  | مقدار |
| ---------- | ----- |
| Verb       | `request-serviceaccounts-token-audience` |
| API Group  | (رشته خالی، به معنی API group هسته (core)) |
| Resource   | مقدار audience درخواست‌شده |
| Name       | نام service account |
| Namespace  | فضای نام (namespace) service account |

می‌توانید از قواعد استاندارد RBAC برای مجاز کردن این بررسی‌ها استفاده کنید. فیلد `resources`
مشخص می‌کند کدام audienceها مجاز هستند و فیلد `resourceNames` مشخص می‌کند
قاعده برای کدام service accountها اعمال می‌شود.

برای مثال، برای اینکه به kubelet اجازه دهید audience با نام `my-registry-audience` را برای
یک service account مشخص درخواست کند:

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

حذف `resourceNames` باعث می‌شود audience برای هر service account مجاز باشد. استفاده از
علامت wildcard (`"*"`) برای `resources` هر audience را مجاز می‌کند:

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

ClusterRole را به گروه `system:nodes` متصل (bind) کنید تا برای همه kubeletها اعمال شود:

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
این محدودیت بخشی از افزونه admission با نام NodeRestriction است و فقط برای
هویت‌های نود (kubeletها) اعمال می‌شود. این محدودیت، audienceهایی را که سایر فراخوان‌کنندگان
API با نام `TokenRequest` می‌توانند درخواست کنند، محدود نمی‌کند. اگر نیاز دارید سایر فراخوان‌کنندگان را محدود کنید، استفاده از [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) را در نظر بگیرید.
{{< /note >}}

## ملاحظات مهاجرت {#migration-considerations}

### kubeletهای خارج از گروه `system:nodes` {#kubelets-outside-the-system-nodes-group}

kubeletهای خارج از گروه `system:nodes` توسط حالت مجوزدهی `Node` مجاز شناخته نمی‌شوند
و باید همچنان از طریق هر سازوکاری که در حال حاضر آن‌ها را مجاز می‌کند، مجوز بگیرند.
افزونه admission مربوط به نود، درخواست‌های این kubeletها را محدود نمی‌کند.

### kubeletهای دارای نام کاربری غیرمتمایز {#kubelets-with-undifferentiated-usernames}

در برخی استقرارها، kubeletها اعتبارنامه‌هایی دارند که آن‌ها را در گروه `system:nodes` قرار می‌دهد،
اما نودی را که با آن مرتبط هستند مشخص نمی‌کند،
زیرا نام کاربری آن‌ها در قالب `system:node:...` نیست.
این kubeletها توسط حالت مجوزدهی `Node` مجاز شناخته نمی‌شوند
و باید همچنان از طریق هر سازوکاری که در حال حاضر آن‌ها را مجاز می‌کند، مجوز بگیرند.

افزونه admission با نام `NodeRestriction` درخواست‌های این kubeletها را نادیده می‌گیرد،
زیرا پیاده‌سازی پیش‌فرض شناسایی نود، آن را هویت نود در نظر نمی‌گیرد.

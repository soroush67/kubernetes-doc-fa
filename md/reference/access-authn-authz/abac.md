---
reviewers:
- erictune
- lavalamp
- deads2k
- liggitt
title: استفاده از مجوزدهی ABAC
content_type: concept
weight: 39
---

<!-- overview -->
کنترل دسترسی مبتنی بر ویژگی (Attribute-based access control یا ABAC) الگویی برای کنترل دسترسی تعریف می‌کند که در آن، حقوق دسترسی از طریق سیاست‌هایی به کاربران اعطا می‌شود که چند ویژگی را با هم ترکیب می‌کنند.

<!-- body -->
## قالب فایل سیاست

برای فعال‌سازی حالت `ABAC`، هنگام راه‌اندازی، `--authorization-policy-file=SOME_FILENAME` و `--authorization-mode=ABAC` را مشخص کنید.

قالب این فایل به صورت [یک آبجکت JSON در هر خط](https://jsonlines.org/) است. هیچ فهرست یا نگاشت دربرگیرنده‌ای نباید وجود داشته باشد و در هر خط فقط یک نگاشت قرار می‌گیرد.

هر خط یک «آبجکت سیاست» است و هر آبجکت از این نوع، نگاشتی با ویژگی‌های زیر است:

- ویژگی‌های نسخه‌بندی:
  - ویژگی `apiVersion` از نوع رشته؛ مقدار معتبر آن "abac.authorization.kubernetes.io/v1beta1" است. این ویژگی امکان نسخه‌بندی و تبدیل قالب سیاست را فراهم می‌کند.
  - ویژگی `kind` از نوع رشته؛ مقدار معتبر آن "Policy" است. این ویژگی امکان نسخه‌بندی و تبدیل قالب سیاست را فراهم می‌کند.
- ویژگی `spec` که مقدار آن نگاشتی با ویژگی‌های زیر است:
  - ویژگی‌های تطبیق موضوع:
    - ویژگی `user` از نوع رشته؛ رشتهٔ کاربر از `--token-auth-file`. اگر `user` را مشخص کنید، باید با نام کاربری کاربر احرازهویت‌شده مطابقت داشته باشد.
    - ویژگی `group` از نوع رشته؛ اگر `group` را مشخص کنید، باید با یکی از گروه‌های کاربر احرازهویت‌شده مطابقت داشته باشد. مقدار `system:authenticated` با همهٔ درخواست‌های احرازهویت‌شده و مقدار `system:unauthenticated` با همهٔ درخواست‌های احرازهویت‌نشده مطابقت دارد.
  - ویژگی‌های تطبیق منبع:
    - ویژگی `apiGroup` از نوع رشته؛ یک گروه API.
      - مثال: `apps`، `networking.k8s.io`
      - نویسهٔ عام: `*` با همهٔ گروه‌های API مطابقت دارد.
    - ویژگی `namespace` از نوع رشته؛ یک فضای نام (namespace).
      - مثال: `kube-system`
      - نویسهٔ عام: `*` با همهٔ درخواست‌های منبع مطابقت دارد.
    - ویژگی `resource` از نوع رشته؛ یک نوع منبع.
      - مثال: `pods`، `deployments`
      - نویسهٔ عام: `*` با همهٔ درخواست‌های منبع مطابقت دارد.
  - ویژگی‌های تطبیق غیرمنبع:
    - ویژگی `nonResourcePath` از نوع رشته؛ مسیرهای درخواست غیرمنبع.
      - مثال: `/version` یا `/apis`
      - نویسهٔ عام:
        - `*` با همهٔ درخواست‌های غیرمنبع مطابقت دارد.
        - `/foo/*` با همهٔ زیرمسیرهای `/foo/` مطابقت دارد.
  - ویژگی `readonly` از نوع بولی؛ اگر مقدار آن true باشد، سیاست تطبیق منبع فقط بر عملیات get، list و watch اعمال می‌شود و سیاست تطبیق غیرمنبع فقط بر عملیات get اعمال می‌شود.

{{< note >}}
ویژگیِ تنظیم‌نشده معادل ویژگی‌ای است که مقدار صفرِ نوع خود را دارد (مثلاً رشتهٔ خالی، 0، false). با این حال، برای خوانایی بهتر است ویژگی را تنظیم‌نشده باقی بگذارید.

در آینده ممکن است سیاست‌ها در قالب JSON بیان شوند و از طریق یک رابط REST مدیریت شوند.
{{< /note >}}

## الگوریتم مجوزدهی

هر درخواست ویژگی‌هایی دارد که با ویژگی‌های آبجکت سیاست متناظرند.

هنگام دریافت یک درخواست، ویژگی‌های آن تعیین می‌شوند. ویژگی‌های ناشناخته برابر با مقدار صفرِ نوع خود (مثلاً رشتهٔ خالی، 0، false) قرار می‌گیرند.

ویژگی‌ای که مقدار آن `"*"` باشد، با هر مقداری از ویژگی متناظر درخواست مطابقت دارد.

مجموعهٔ ویژگی‌های درخواست با تک‌تک سیاست‌های موجود در فایل سیاست مقایسه می‌شود. اگر دست‌کم یک خط با ویژگی‌های درخواست مطابقت داشته باشد، درخواست مجاز شمرده می‌شود (هرچند ممکن است در اعتبارسنجی‌های بعدی رد شود).

برای اینکه به هر کاربر احرازهویت‌شده اجازهٔ انجام کاری را بدهید، سیاستی بنویسید که ویژگی group آن برابر با `"system:authenticated"` باشد.

برای اینکه به هر کاربر احرازهویت‌نشده اجازهٔ انجام کاری را بدهید، سیاستی بنویسید که ویژگی group آن برابر با `"system:unauthenticated"` باشد.

برای اینکه به یک کاربر اجازهٔ انجام هر کاری را بدهید، سیاستی بنویسید که ویژگی‌های apiGroup، namespace، resource و nonResourcePath آن برابر با `"*"` باشند.

## Kubectl

ابزار kubectl از نقطه‌های پایانی `/api` و `/apis` در apiserver برای کشف انواع منابع ارائه‌شده استفاده می‌کند و آبجکت‌هایی را که با عملیات create/update به API فرستاده می‌شوند، با کمک اطلاعات طرح‌واره‌ای که در `/openapi/v2` قرار دارد، اعتبارسنجی می‌کند.

هنگام استفاده از مجوزدهی ABAC، این منابع ویژه باید به‌صراحت از طریق ویژگی `nonResourcePath` در یک سیاست در دسترس قرار گیرند (به [مثال‌های](#examples) زیر مراجعه کنید):

* مسیرهای `/api`، `/api/*`، `/apis` و `/apis/*` برای مذاکرهٔ نسخهٔ API.
* مسیر `/version` برای دریافت نسخهٔ سرور از طریق `kubectl version`.
* مسیر `/swaggerapi/*` برای عملیات create/update.

برای بررسی فراخوانی‌های HTTP که در یک عملیات خاص kubectl انجام می‌شوند، می‌توانید سطح جزئیات خروجی را افزایش دهید:

```shell
kubectl --v=8 version
```

## مثال‌ها

1. کاربر Alice می‌تواند هر کاری را روی همهٔ منابع انجام دهد:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "alice", "namespace": "*", "resource": "*", "apiGroup": "*"}}
   ```

1. کامپوننت kubelet می‌تواند همهٔ پادها را بخواند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "kubelet", "namespace": "*", "resource": "pods", "readonly": true}}
   ```

1. کامپوننت kubelet می‌تواند رویدادها را بخواند و بنویسد:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "kubelet", "namespace": "*", "resource": "events"}}
   ```

1. کاربر Bob فقط می‌تواند پادهای فضای نام "projectCaribou" را بخواند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "bob", "namespace": "projectCaribou", "resource": "pods", "readonly": true}}
   ```

1. همه می‌توانند درخواست‌های فقط‌خواندنی به همهٔ مسیرهای غیرمنبع بفرستند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"group": "system:authenticated", "readonly": true, "nonResourcePath": "*"}}
    {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"group": "system:unauthenticated", "readonly": true, "nonResourcePath": "*"}}
   ```

[نمونهٔ کامل فایل](https://releases.k8s.io/v{{< skew currentPatchVersion >}}/pkg/auth/authorizer/abac/example_policy_file.jsonl)

## نکته‌ای کوتاه دربارهٔ حساب‌های سرویس

هر حساب سرویس یک نام کاربری ABAC متناظر دارد و نام کاربری هر حساب سرویس طبق قرارداد نام‌گذاری زیر ساخته می‌شود:

```shell
system:serviceaccount:<namespace>:<serviceaccountname>
```

ایجاد یک فضای نام جدید به ایجاد یک حساب سرویس جدید با قالب زیر منجر می‌شود:

```shell
system:serviceaccount:<namespace>:default
```

برای مثال، اگر بخواهید با استفاده از ABAC به حساب سرویس پیش‌فرض (در فضای نام `kube-system`) دسترسی کامل به API بدهید، باید این خط را به فایل سیاست خود اضافه کنید:

```json
{"apiVersion":"abac.authorization.kubernetes.io/v1beta1","kind":"Policy","spec":{"user":"system:serviceaccount:kube-system:default","namespace":"*","resource":"*","apiGroup":"*"}}
```

برای اعمال خطوط جدید سیاست، باید apiserver را دوباره راه‌اندازی کنید.

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
کنترل دسترسی مبتنی بر ویژگی (Attribute-based access control یا ABAC) الگویی برای کنترل دسترسی تعریف می‌کند که در آن حقوق دسترسی از طریق سیاست‌هایی به کاربران اعطا می‌شود که ویژگی‌ها (attributes) را با یکدیگر ترکیب می‌کنند.

<!-- body -->
## قالب فایل سیاست {#policy-file-format}

برای فعال‌سازی حالت `ABAC`، هنگام راه‌اندازی، گزینه‌های `--authorization-policy-file=SOME_FILENAME` و `--authorization-mode=ABAC` را مشخص کنید.

قالب فایل، [یک آبجکت JSON در هر خط](https://jsonlines.org/) است. نباید هیچ لیست یا map فراگیری وجود داشته باشد؛ فقط یک map در هر خط.

هر خط یک «آبجکت سیاست» (policy object) است و هر یک از این آبجکت‌ها یک map با ویژگی‌های زیر است:

- ویژگی‌های نسخه‌بندی:
  - `apiVersion`، از نوع رشته؛ مقادیر معتبر عبارت است از "abac.authorization.kubernetes.io/v1beta1". این ویژگی امکان نسخه‌بندی و تبدیل قالب سیاست را فراهم می‌کند.
  - `kind`، از نوع رشته؛ مقادیر معتبر عبارت است از "Policy". این ویژگی امکان نسخه‌بندی و تبدیل قالب سیاست را فراهم می‌کند.
- ویژگی `spec` که روی یک map با ویژگی‌های زیر تنظیم می‌شود:
  - ویژگی‌های تطبیق سوژه (Subject):
    - `user`، از نوع رشته؛ رشته کاربر از `--token-auth-file`. اگر `user` را مشخص کنید، باید با نام کاربری کاربر احراز هویت‌شده مطابقت داشته باشد.
    - `group`، از نوع رشته؛ اگر `group` را مشخص کنید، باید با یکی از گروه‌های کاربر احراز هویت‌شده مطابقت داشته باشد. `system:authenticated` با همه درخواست‌های احراز هویت‌شده مطابقت دارد. `system:unauthenticated` با همه درخواست‌های احراز هویت‌نشده مطابقت دارد.
  - ویژگی‌های تطبیق منبع:
    - `apiGroup`، از نوع رشته؛ یک گروه API.
      - مثال: `apps`، `networking.k8s.io`
      - نویسه عام (Wildcard): `*` با همه گروه‌های API مطابقت دارد.
    - `namespace`، از نوع رشته؛ یک فضای نام (namespace).
      - مثال: `kube-system`
      - نویسه عام: `*` با همه درخواست‌های منبع مطابقت دارد.
    - `resource`، از نوع رشته؛ یک نوع منبع
      - مثال: `pods`، `deployments`
      - نویسه عام: `*` با همه درخواست‌های منبع مطابقت دارد.
  - ویژگی‌های تطبیق غیرمنبع:
    - `nonResourcePath`، از نوع رشته؛ مسیرهای درخواست‌های غیرمنبع.
      - مثال: `/version` یا `/apis`
      - نویسه عام:
        - `*` با همه درخواست‌های غیرمنبع مطابقت دارد.
        - `/foo/*` با همه زیرمسیرهای `/foo/` مطابقت دارد.
  - `readonly`، از نوع بولی؛ هنگامی که true باشد، به این معناست که سیاست تطبیق منبع فقط برای عملیات get، list و watch اعمال می‌شود و سیاست تطبیق غیرمنبع فقط برای عملیات get اعمال می‌شود.

{{< note >}}
ویژگی تنظیم‌نشده با ویژگی‌ای که روی مقدار صفر نوع خود تنظیم شده است (مثلاً رشته خالی، 0، false) یکسان است. با این حال، برای خوانایی بهتر است از تنظیم‌نکردن ویژگی استفاده شود.

در آینده ممکن است سیاست‌ها در قالب JSON بیان شوند و از طریق یک رابط REST مدیریت شوند.
{{< /note >}}

## الگوریتم مجوزدهی {#authorization-algorithm}

یک درخواست دارای ویژگی‌هایی است که با ویژگی‌های آبجکت سیاست متناظرند.

هنگامی که درخواستی دریافت می‌شود، ویژگی‌ها تعیین می‌گردند. ویژگی‌های ناشناخته روی مقدار صفر نوع خود تنظیم می‌شوند (مثلاً رشته خالی، 0، false).

ویژگی‌ای که روی `"*"` تنظیم شده باشد با هر مقداری از ویژگی متناظر مطابقت می‌کند.

چندتایی (tuple) ویژگی‌ها برای یافتن تطابق با تک‌تک سیاست‌های موجود در فایل سیاست بررسی می‌شود. اگر دست‌کم یک خط با ویژگی‌های درخواست مطابقت داشته باشد، درخواست مجاز شناخته می‌شود (اما ممکن است در اعتبارسنجی‌های بعدی ناموفق شود).

برای اینکه به هر کاربر احراز هویت‌شده اجازه انجام کاری را بدهید، سیاستی بنویسید که ویژگی group در آن روی `"system:authenticated"` تنظیم شده باشد.

برای اینکه به هر کاربر احراز هویت‌نشده اجازه انجام کاری را بدهید، سیاستی بنویسید که ویژگی group در آن روی `"system:unauthenticated"` تنظیم شده باشد.

برای اینکه به یک کاربر اجازه انجام هر کاری را بدهید، سیاستی بنویسید که ویژگی‌های apiGroup، namespace، resource و nonResourcePath در آن روی `"*"` تنظیم شده باشند.

## Kubectl {#kubectl}

Kubectl از نقاط پایانی `/api` و `/apis` در apiserver برای کشف انواع منابعی که ارائه می‌شوند استفاده می‌کند و آبجکت‌هایی را که در عملیات create/update به API ارسال می‌شوند، با استفاده از اطلاعات طرحواره (schema) موجود در `/openapi/v2` اعتبارسنجی می‌کند.

هنگام استفاده از مجوزدهی ABAC، این منابع ویژه باید به‌صراحت از طریق ویژگی `nonResourcePath` در یک سیاست در دسترس قرار گیرند (به [مثال‌ها](#examples) در ادامه مراجعه کنید):

* `/api`، `/api/*`، `/apis` و `/apis/*` برای مذاکره نسخه API.
* `/version` برای دریافت نسخه سرور از طریق `kubectl version`.
* `/swaggerapi/*` برای عملیات create/update.

برای بررسی فراخوانی‌های HTTP که در یک عملیات مشخص kubectl انجام می‌شوند، می‌توانید سطح جزئیات گزارش‌ها (verbosity) را افزایش دهید:

```shell
kubectl --v=8 version
```

## مثال‌ها {#examples}

1. Alice می‌تواند هر کاری را روی همه منابع انجام دهد:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "alice", "namespace": "*", "resource": "*", "apiGroup": "*"}}
   ```

1. kubelet می‌تواند هر Podی را بخواند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "kubelet", "namespace": "*", "resource": "pods", "readonly": true}}
   ```

1. kubelet می‌تواند رویدادها (events) را بخواند و بنویسد:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "kubelet", "namespace": "*", "resource": "events"}}
   ```

1. Bob فقط می‌تواند Podها را در فضای نام "projectCaribou" بخواند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"user": "bob", "namespace": "projectCaribou", "resource": "pods", "readonly": true}}
   ```

1. هر کسی می‌تواند درخواست‌های فقط‌خواندنی را به همه مسیرهای غیرمنبع ارسال کند:

   ```json
   {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"group": "system:authenticated", "readonly": true, "nonResourcePath": "*"}}
    {"apiVersion": "abac.authorization.kubernetes.io/v1beta1", "kind": "Policy", "spec": {"group": "system:unauthenticated", "readonly": true, "nonResourcePath": "*"}}
   ```

[نمونه فایل کامل](https://releases.k8s.io/v{{< skew currentPatchVersion >}}/pkg/auth/authorizer/abac/example_policy_file.jsonl)

## نکته‌ای کوتاه درباره حساب‌های سرویس (service account) {#a-quick-note-on-service-accounts}

هر حساب سرویس (service account) یک نام کاربری ABAC متناظر دارد و نام کاربری آن حساب سرویس طبق قرارداد نام‌گذاری زیر تولید می‌شود:

```shell
system:serviceaccount:<namespace>:<serviceaccountname>
```

ایجاد یک فضای نام جدید منجر به ایجاد یک حساب سرویس جدید با قالب زیر می‌شود:

```shell
system:serviceaccount:<namespace>:default
```

برای مثال، اگر بخواهید با استفاده از ABAC به حساب سرویس default (در فضای نام `kube-system`) دسترسی کامل به API بدهید، باید این خط را به فایل سیاست خود اضافه کنید:

```json
{"apiVersion":"abac.authorization.kubernetes.io/v1beta1","kind":"Policy","spec":{"user":"system:serviceaccount:kube-system:default","namespace":"*","resource":"*","apiGroup":"*"}}
```

برای اینکه خطوط جدید سیاست اعمال شوند، apiserver باید دوباره راه‌اندازی شود.

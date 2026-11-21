---
title: جعل هویت کاربر
content_type: reference
weight: 50
---

<!-- overview -->

_جعل هویت_ (impersonation) کاربر روشی است که به کاربران احراز هویت‌شده امکان می‌دهد از طریق سرآیندهای HTTP در نقش کاربر، گروه یا حساب سرویس (service account) دیگری عمل کنند.

<!-- body -->
هر کاربر می‌تواند با استفاده از سرآیندهای جعل هویت در نقش کاربر دیگری عمل کند. این سرآیندها اطلاعات کاربری‌ای را که درخواست با آن احراز هویت می‌شود، به‌صورت دستی بازنویسی می‌کنند. برای مثال، یک مدیر می‌تواند با استفاده از این قابلیت، به‌طور موقت هویت کاربر دیگری را جعل کند و ببیند آیا درخواست رد می‌شود یا نه، و به این ترتیب یک سیاست مجوزدهی را اشکال‌زدایی کند.

درخواست‌های جعل هویت ابتدا با هویت کاربر درخواست‌دهنده احراز هویت می‌شوند و سپس به اطلاعات کاربر جعل‌شده تغییر می‌یابند.

* کاربر با اعتبارنامه‌های خود _و_ سرآیندهای جعل هویت یک فراخوانی API انجام می‌دهد.
* سرور API کاربر را احراز هویت می‌کند.
* سرور API اطمینان حاصل می‌کند که کاربران احراز هویت‌شده دارای امتیاز جعل هویت هستند.
* اطلاعات کاربر درخواست با مقادیر جعل هویت جایگزین می‌شود.
* درخواست ارزیابی می‌شود و مجوزدهی بر اساس اطلاعات کاربر جعل‌شده انجام می‌گیرد.

برای انجام یک درخواست جعل هویت می‌توان از سرآیندهای HTTP زیر استفاده کرد:

* `Impersonate-User`: نام کاربری‌ای که باید در نقش آن عمل کرد.
* `Impersonate-Uid`: شناسه‌ای یکتا که نمایانگر کاربرِ جعل‌شده است. اختیاری است.
   به "Impersonate-User" نیاز دارد. کوبرنتیز هیچ الزامی دربارهٔ قالب این رشته تحمیل نمی‌کند.
* `Impersonate-Group`: نام گروهی که باید در نقش آن عمل کرد. برای تعیین چند گروه، می‌توان آن را چند بار ارائه کرد.
  اختیاری است. به "Impersonate-User" نیاز دارد.
* `Impersonate-Extra-( extra name )`: سرآیندی پویا که برای مرتبط کردن فیلدهای اضافی با کاربر استفاده می‌شود.
  اختیاری است. به "Impersonate-User" نیاز دارد. برای اینکه این مقدار به‌طور یکسان حفظ شود، `( extra name )`
  باید با حروف کوچک نوشته شود و هر نویسه‌ای که [در برچسب‌های سرآیند HTTP مجاز نیست](https://tools.ietf.org/html/rfc7230#section-3.2.6)
  باید حتماً به‌صورت utf8 و [کدگذاری درصدی](https://tools.ietf.org/html/rfc3986#section-2.1) باشد.

{{< note >}}
پیش از نسخهٔ 1.11.3 (و 1.10.7، 1.9.11)، `( extra name )` فقط می‌توانست شامل نویسه‌هایی باشد که
[در برچسب‌های سرآیند HTTP مجاز بودند](https://tools.ietf.org/html/rfc7230#section-3.2.6).
{{< /note >}}

{{< note >}}
سرآیند `Impersonate-Uid` فقط در نسخهٔ 1.22.0 و بالاتر در دسترس است.
{{< /note >}}

نمونه‌ای از سرآیندهای جعل هویت هنگام جعل هویت یک کاربر همراه با گروه‌ها:

```http
Impersonate-User: jane.doe@example.com
Impersonate-Group: developers
Impersonate-Group: admins
```

نمونه‌ای از سرآیندهای جعل هویت هنگام جعل هویت یک کاربر همراه با UID و فیلدهای اضافی:

```http
Impersonate-User: jane.doe@example.com
Impersonate-Uid: 06f6ce97-e2c5-4ab8-7ba5-7654dd08d52b
Impersonate-Extra-dn: cn=jane,ou=engineers,dc=example,dc=com
Impersonate-Extra-acme.com%2Fproject: some-project
Impersonate-Extra-scopes: view
Impersonate-Extra-scopes: development
```

هنگام استفاده از `kubectl`، برای پیکربندی سرآیند `Impersonate-User` آرگومان خط فرمان `--as` را تنظیم کنید. همچنین می‌توانید برای پیکربندی سرآیند `Impersonate-Group` پرچم `--as-group`، برای پیکربندی سرآیند `Impersonate-Uid` پرچم `--as-uid` (1.23) و برای پیکربندی سرآیند `Impersonate-Extra-( extra name )` پرچم `--as-user-extra` (1.35) را تنظیم کنید.

```bash
kubectl drain mynode
```

```none
Error from server (Forbidden): User "clark" cannot get nodes at the cluster scope. (get nodes mynode)
```

پرچم‌های `--as` و `--as-group` را تنظیم کنید:

```bash
kubectl drain mynode --as=superman --as-group=system:masters
```

```none
node/mynode cordoned
node/mynode drained
```

برای جعل هویت یک کاربر، شناسهٔ کاربر (UID)، گروه یا فیلدهای اضافی، کاربرِ جعل‌کننده باید توانایی اجرای فعل **impersonate** را روی نوع ویژگیِ مورد جعل ("user"، "uid"، "group" و غیره) داشته باشد. در کلاسترهایی که افزونهٔ مجوزدهی RBAC در آن‌ها فعال است، ClusterRole زیر قواعد لازم برای تنظیم سرآیندهای جعل هویت کاربر و گروه را در بر می‌گیرد:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonator
rules:
- apiGroups: [""]
  resources: ["users", "groups", "serviceaccounts"]
  verbs: ["impersonate"]
```

در جعل هویت، فیلدهای اضافی و UIDهای جعل‌شده هر دو زیر `apiGroup` با نام "authentication.k8s.io" قرار دارند.
فیلدهای اضافی به‌عنوان زیرمنبع‌های منبع "userextras" ارزیابی می‌شوند. برای اینکه کاربر بتواند از سرآیندهای جعل هویت برای فیلد اضافی `scopes` و برای UIDها استفاده کند، باید نقش زیر به او اعطا شود:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: scopes-and-uid-impersonator
rules:
# Can set "Impersonate-Extra-scopes" header and the "Impersonate-Uid" header.
- apiGroups: ["authentication.k8s.io"]
  resources: ["userextras/scopes", "uids"]
  verbs: ["impersonate"]
```

همچنین می‌توان مقادیر سرآیندهای جعل هویت را با محدود کردن مجموعهٔ `resourceNames` که یک منبع می‌تواند بپذیرد، محدود کرد.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: limited-impersonator
rules:
# Can impersonate the user "jane.doe@example.com"
- apiGroups: [""]
  resources: ["users"]
  verbs: ["impersonate"]
  resourceNames: ["jane.doe@example.com"]

# Can impersonate the groups "developers" and "admins"
- apiGroups: [""]
  resources: ["groups"]
  verbs: ["impersonate"]
  resourceNames: ["developers","admins"]

# Can impersonate the extras field "scopes" with the values "view" and "development"
- apiGroups: ["authentication.k8s.io"]
  resources: ["userextras/scopes"]
  verbs: ["impersonate"]
  resourceNames: ["view", "development"]

# Can impersonate the uid "06f6ce97-e2c5-4ab8-7ba5-7654dd08d52b"
- apiGroups: ["authentication.k8s.io"]
  resources: ["uids"]
  verbs: ["impersonate"]
  resourceNames: ["06f6ce97-e2c5-4ab8-7ba5-7654dd08d52b"]
```

{{< note >}}
جعل هویت یک کاربر یا گروه به شما امکان می‌دهد هر کاری را چنان انجام دهید که گویی همان کاربر یا گروه هستید؛
به همین دلیل، دامنهٔ جعل هویت به فضای نام (namespace) محدود نیست.
اگر می‌خواهید جعل هویت را با RBAC کوبرنتیز مجاز کنید،
باید از ClusterRole و ClusterRoleBinding استفاده کنید،
نه از Role و RoleBinding.

اعطای مجوز جعل هویت روی ServiceAccountها در محدودهٔ فضای نام است، اما ServiceAccount جعل‌شده
می‌تواند کارهایی خارج از آن فضای نام انجام دهد.
{{< /note >}}

## جعل هویت محدودشده

{{< feature-state feature_gate_name="ConstrainedImpersonation" >}}

با فعل **impersonate** نمی‌توان جعل هویت را محدود کرد یا دامنهٔ آن را مشخص کرد.
این فعل یا مجوز کامل جعل هویت را اعطا می‌کند یا هیچ مجوزی نمی‌دهد. پس از اینکه مجوز جعل هویت یک کاربر به شما اعطا شد، می‌توانید هر کاری را که آن کاربر قادر به انجامش است، روی همهٔ منابع و فضاهای نام انجام دهید.

با جعل هویت محدودشده، می‌توان جعل‌کننده را طوری محدود کرد که فقط برای کارهای مشخص روی منابع مشخص هویت کاربر دیگری را جعل کند، به‌جای اینکه بتواند همهٔ کارهایی را که کاربرِ جعل‌شده می‌تواند انجام دهد، اجرا کند.

این قابلیت با تنظیم
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ConstrainedImpersonation) با نام `ConstrainedImpersonation` فعال می‌شود.

### آشنایی با جعل هویت محدودشده

جعل هویت محدودشده به **دو مجوز جداگانه** نیاز دارد:

1. **مجوز جعل یک هویت مشخص** (کاربر، UID، گروه، حساب سرویس یا نود)
2. **مجوز انجام کارهای مشخص در یک دامنهٔ معین هنگام جعل هویت** (برای
   مثال، فقط `list` و `watch` روی پادها در فضای نام `default`)

بنابراین می‌توان جعل‌کننده را طوری محدود کرد که فقط برای عملیات مشخص هویت کاربر دیگری را جعل کند.

### حالت‌های جعل هویت

جعل هویت محدودشده سه حالت متمایز تعریف می‌کند که هر کدام مجموعه‌ای از فعل‌های مخصوص به خود را دارند:

#### حالت user-info

از این حالت برای جعل هویت کاربران عمومی (نه حساب‌های سرویس یا نودها) استفاده کنید. این حالت زمانی اعمال می‌شود که مقدار سرآیند `Impersonate-User`:
- با `system:serviceaccount:` شروع **نشود**
- با `system:node:` شروع **نشود**

**فعل‌ها:**
- `impersonate:user-info` - مجوز جعل هویت یک کاربر، گروه، UID یا فیلد اضافی مشخص
- `impersonate-on:user-info:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت یک کاربر عمومی

#### حالت ServiceAccount

از این حالت برای جعل هویت ServiceAccountها استفاده کنید.

**فعل‌ها:**
- `impersonate:serviceaccount` - مجوز جعل هویت یک حساب سرویس مشخص
- `impersonate-on:serviceaccount:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت یک حساب سرویس

#### حالت‌های arbitrary-node و associated-node

از این حالت‌ها برای جعل هویت نودها استفاده کنید. این حالت زمانی اعمال می‌شود که مقدار سرآیند `Impersonate-User` با `system:node:` شروع شود.

**فعل‌ها:**
- `impersonate:arbitrary-node` - مجوز جعل هویت هر نود مشخص‌شده
- `impersonate:associated-node` - مجوز جعل هویت فقط نودی که جعل‌کننده به آن متصل است
- `impersonate-on:arbitrary-node:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت هر نود
- `impersonate-on:associated-node:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت نود مرتبط

{{< note >}}
فعل `impersonate:associated-node` فقط زمانی اعمال می‌شود که جعل‌کننده یک حساب سرویس متصل به همان نودی باشد که قصد جعل هویت آن را دارد. این موضوع با بررسی این تعیین می‌شود که آیا اطلاعات کاربری حساب سرویس شامل یک فیلد اضافی با کلید `authentication.kubernetes.io/node-name` است که با نودِ مورد جعل مطابقت داشته باشد.
{{< /note >}}

### پیکربندی جعل هویت محدودشده با RBAC

همهٔ مجوزهای جعل هویت محدودشده از گروه API با نام `authentication.k8s.io` استفاده می‌کنند. در ادامه نحوهٔ پیکربندی حالت‌های مختلف آمده است.

#### مثال: جعل هویت یک کاربر برای کارهای مشخص

این مثال نشان می‌دهد چگونه می‌توان به یک حساب سرویس اجازه داد هویت کاربری با نام `jane.doe@example.com` را جعل کند، اما فقط برای `list` و `watch` روی پادها در فضای نام `default`. برای این کار هم به یک `ClusterRoleBinding` برای مجوز هویت و هم به یک `RoleBinding` برای مجوز انجام کار نیاز دارید.

**گام ۱: اعطای مجوز جعل هویت کاربر**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonate-jane-identity
rules:
- apiGroups: ["authentication.k8s.io"]
  resources: ["users"]
  resourceNames: ["jane.doe@example.com"]
  verbs: ["impersonate:user-info"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: impersonate-jane-identity
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: impersonate-jane-identity
subjects:
- kind: ServiceAccount
  name: my-controller
  namespace: default
```

**گام ۲: اعطای مجوز انجام کارهای مشخص هنگام جعل هویت**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: impersonate-list-watch-pods
  namespace: default
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs:
  - "impersonate-on:user-info:list"
  - "impersonate-on:user-info:watch"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: impersonate-list-watch-pods
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: impersonate-list-watch-pods
subjects:
- kind: ServiceAccount
  name: my-controller
  namespace: default
```

اکنون حساب سرویس `my-controller` می‌تواند با جعل هویت `jane.doe@example.com` پادهای فضای نام `default` را فهرست و رصد کند، اما **نمی‌تواند** کارهای دیگری مانند حذف پادها یا دسترسی به منابع سایر فضاهای نام را انجام دهد.

#### مثال: جعل هویت یک ServiceAccount

برای اینکه بتوان هویت حساب سرویسی با نام `app-sa` در فضای نام `production` را برای ایجاد و به‌روزرسانی Deploymentها جعل کرد:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: impersonate-app-sa
  namespace: default
rules:
- apiGroups: ["authentication.k8s.io"]
  resources: ["serviceaccounts"]
  resourceNames: ["app-sa"]
  # For service accounts, you must specify the namespace in the RoleBinding
  verbs: ["impersonate:serviceaccount"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: impersonate-manage-deployments
  namespace: production
rules:
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs:
  - "impersonate-on:serviceaccount:create"
  - "impersonate-on:serviceaccount:update"
  - "impersonate-on:serviceaccount:patch"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: impersonate-app-sa
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: impersonate-app-sa
subjects:
- kind: ServiceAccount
  name: deputy-controller
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: impersonate-manage-deployments
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: impersonate-manage-deployments
subjects:
- kind: ServiceAccount
  name: deputy-controller
  namespace: default
```

#### مثال: جعل هویت یک نود

برای اینکه ServiceAccount با نام `node-impersonator` در فضای نام `default` بتواند با جعل هویت نودی به نام `mynode` پادها را دریافت و فهرست کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonate-node-sa
rules:
- apiGroups: ["authentication.k8s.io"]
  resources: ["nodes"]
  resourceNames: ["mynode"]
  verbs: ["impersonate:arbitrary-node"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonate-list-pods
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs:
      - "impersonate-on:arbitrary-node:list"
      - "impersonate-on:arbitrary-node:get"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: impersonate-node-sa
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: impersonate-node-sa
subjects:
- kind: ServiceAccount
  name: node-impersonator
  namespace: default
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: impersonate-list-pods
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: impersonate-list-pods
subjects:
  - kind: ServiceAccount
    name: node-impersonator
    namespace: default
```

#### مثال: جعل هویت نود مرتبط توسط عامل نود

این الگو برای عامل‌های نود (مانند افزونه‌های CNI) رایج است که باید پادهای روی نود خود را بخوانند، بی‌آنکه به پادهای کل کلاستر دسترسی داشته باشند.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonate-associated-node-identity
rules:
- apiGroups: ["authentication.k8s.io"]
  resources: ["nodes"]
  verbs: ["impersonate:associated-node"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: impersonate-list-pods-on-node
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs:
  - "impersonate-on:associated-node:list"
  - "impersonate-on:associated-node:get"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: node-agent-impersonate-node
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: impersonate-associated-node-identity
subjects:
- kind: ServiceAccount
  name: node-agent
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: node-agent-impersonate-list-pods
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: impersonate-list-pods-on-node
subjects:
- kind: ServiceAccount
  name: node-agent
  namespace: kube-system
```

کنترل‌کننده نام نود را با استفاده از downward API به دست می‌آورد:

```yaml
env:
- name: MY_NODE_NAME
  valueFrom:
    fieldRef:
      fieldPath: spec.nodeName
```

سپس kubeconfig را برای جعل هویت پیکربندی کنید:

```go
kubeConfig, _ := clientcmd.BuildConfigFromFlags("", "")
kubeConfig.Impersonate = rest.ImpersonationConfig{
    UserName: "system:node:" + os.Getenv("MY_NODE_NAME"),
}
```

### استفاده از جعل هویت محدودشده

از دید کلاینت، استفاده از جعل هویت محدودشده دقیقاً مانند استفاده از جعل هویت سنتی است. همان سرآیندهای جعل هویت را به کار می‌برید:

```http
Impersonate-User: jane.doe@example.com
```

یا با kubectl:

```bash
kubectl get pods -n default --as=jane.doe@example.com
```

تفاوت به‌طور کامل در بررسی‌های مجوزدهی‌ای است که سرور API انجام می‌دهد.

### کار با فعل `impersonate`

- اگر قواعد RBAC موجودی دارید که از فعل `impersonate` استفاده می‌کنند، این قواعد پس از فعال شدن feature gate همچنان کار می‌کنند.

- هنگامی که یک درخواست جعل هویت ارسال می‌شود، سرور API ابتدا مجوزهای جعل هویت محدودشده را بررسی می‌کند. اگر این بررسی‌ها ناموفق باشند، به بررسی مجوز `impersonate` بازمی‌گردد.

## ممیزی

برای هر درخواست جعل هویت یک رویداد ممیزی (audit) ثبت می‌شود تا بتوان نحوهٔ استفاده از جعل هویت را ردیابی کرد.

هنگامی که درخواستی از جعل هویت محدودشده استفاده می‌کند، رویداد ممیزی شامل آبجکت `authenticationMetadata` با فیلد `impersonationConstraint` است که نشان می‌دهد کدام فعل جعل هویت محدودشده برای مجوزدهی به درخواست به کار رفته است.

برای درخواست‌های غیر از watch که بیش از 500ms طول می‌کشند، سرور API حاشیه‌نویسی (annotation) `apiserver.latency.k8s.io/impersonation` را نیز به رویداد ممیزی اضافه می‌کند. این حاشیه‌نویسی زمان صرف‌شده برای پردازش جعل هویت را (همراه با سایر handlerهایی که در مدت زمان کل سهم داشته‌اند) ثبت می‌کند.

نمونهٔ رویداد ممیزی:

```json
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "user": {
    "username": "system:serviceaccount:default:my-controller"
  },
  "impersonatedUser": {
    "username": "jane.doe@example.com"
  },
  "authenticationMetadata": {
    "impersonationConstraint": "impersonate:user-info"
  },
  "annotations": {
    "apiserver.latency.k8s.io/impersonation": "100ms"
  },
  "verb": "list",
  "objectRef": {
    "resource": "pods",
    "namespace": "default"
  }
}
```

مقدار `impersonationConstraint` نشان می‌دهد کدام حالت استفاده شده است (برای مثال، `impersonate:user-info` یا `impersonate:associated-node`). کار مشخص انجام‌شده (برای مثال، `list`) را می‌توان از فیلد `verb` در رویداد ممیزی تعیین کرد. برای درخواست‌های کند، حاشیه‌نویسی تأخیر، زمان صرف‌شده (برای مثال، `100ms`) برای پردازش جعل هویت درخواست را ثبت می‌کند.

## سنجه‌ها

مؤلفهٔ `kube-apiserver` سنجه‌های Prometheus زیر را برای جعل هویت محدودشده ارائه می‌کند:

- `apiserver_impersonation_attempts_total{mode, decision}`: شمارنده‌ای که با هر تلاش برای جعل هویت افزایش می‌یابد. مقدار `mode` یکی از `associated-node`، `arbitrary-node`، `serviceaccount`، `user-info` یا `legacy` است. مقدار `decision` برابر `allowed` یا `denied` است.
- `apiserver_impersonation_attempts_duration_seconds{mode, decision}`: هیستوگرامی که زمان صرف‌شده برای تعیین کاربر جعل‌شده را ردیابی می‌کند. برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند. به دلیل وجود حافظهٔ نهان در handler، این سنجه هزینهٔ تأخیر سرشکن‌شدهٔ درخواست‌های جعل هویت را نشان می‌دهد.
- `apiserver_impersonation_authorization_attempts_total{mode, decision}`: شمارنده‌ای که هر بار که یک تلاش برای جعل هویت، مجوزدهنده (authorizer) را فراخوانی می‌کند، افزایش می‌یابد. برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند.
- `apiserver_impersonation_authorization_attempts_duration_seconds{mode, decision}`: هیستوگرامی که زمان صرف‌شده توسط مجوزدهنده برای هر تلاش جعل هویت را ردیابی می‌کند.
  برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند.

در سنجه‌های `apiserver_impersonation_attempts_total{mode, decision}` و
`apiserver_impersonation_attempts_duration_seconds{mode, decision}`، هنگامی که `decision` برابر `denied` باشد، مقدار `mode` رشتهٔ خالی است.

## {{% heading "whatsnext" %}}

- دربارهٔ [مجوزدهی RBAC](/docs/reference/access-authn-authz/rbac/) بخوانید
- با [احراز هویت در کوبرنتیز](/docs/reference/access-authn-authz/authentication/) آشنا شوید

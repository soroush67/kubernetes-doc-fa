---
title: جعل هویت کاربر
content_type: reference
weight: 50
---

<!-- overview -->

_جعل هویت_ (impersonation) کاربر روشی است که به کاربران احراز هویت‌شده اجازه می‌دهد از طریق هدرهای HTTP به‌جای کاربر، گروه یا service account دیگری عمل کنند.

<!-- body -->
یک کاربر می‌تواند از طریق هدرهای جعل هویت به‌جای کاربر دیگری عمل کند. این هدرها امکان می‌دهند اطلاعات کاربری‌ای که درخواست با آن احراز هویت می‌شود، به‌صورت دستی بازنویسی شود. برای مثال، یک مدیر می‌تواند با استفاده از این قابلیت و با جعل موقت هویت کاربر دیگر، یک سیاست مجوزدهی را اشکال‌زدایی کند و ببیند آیا درخواستی رد شده است یا خیر.

درخواست‌های جعل هویت ابتدا با هویت کاربر درخواست‌دهنده احراز هویت می‌شوند و سپس به اطلاعات کاربری که هویتش جعل شده است تغییر می‌یابند.

* کاربر یک فراخوانی API را با اعتبارنامه‌های خود _و_ هدرهای جعل هویت ارسال می‌کند.
* سرور API کاربر را احراز هویت می‌کند.
* سرور API اطمینان حاصل می‌کند که کاربران احراز هویت‌شده دارای امتیاز جعل هویت هستند.
* اطلاعات کاربر درخواست با مقادیر جعل هویت جایگزین می‌شود.
* درخواست ارزیابی می‌شود و مجوزدهی بر اساس اطلاعات کاربرِ جعل‌شده انجام می‌گیرد.

از هدرهای HTTP زیر می‌توان برای ارسال درخواست جعل هویت استفاده کرد:

* `Impersonate-User`: نام کاربری که باید به‌جای آن عمل شود.
* `Impersonate-Uid`: شناسه‌ای یکتا که کاربرِ جعل‌شده را نشان می‌دهد. اختیاری است.
   به "Impersonate-User" نیاز دارد. کوبرنتیز هیچ الزامی برای قالب این رشته اعمال نمی‌کند.
* `Impersonate-Group`: نام گروهی که باید به‌جای آن عمل شود. برای تنظیم چند گروه می‌توان آن را چندین بار ارائه کرد.
  اختیاری است. به "Impersonate-User" نیاز دارد.
* `Impersonate-Extra-( extra name )`: هدری پویا که برای مرتبط کردن فیلدهای اضافی با کاربر به کار می‌رود.
  اختیاری است. به "Impersonate-User" نیاز دارد. برای اینکه مقدار به‌طور پایدار حفظ شود، `( extra name )`
  باید با حروف کوچک باشد و هر نویسه‌ای که [در برچسب‌های هدر HTTP مجاز نیست](https://tools.ietf.org/html/rfc7230#section-3.2.6)
  باید به‌صورت utf8 و [درصدکدگذاری‌شده (percent-encoded)](https://tools.ietf.org/html/rfc3986#section-2.1) باشد.

{{< note >}}
پیش از نسخه 1.11.3 (و 1.10.7 و 1.9.11)، `( extra name )` فقط می‌توانست شامل نویسه‌هایی باشد که
[در برچسب‌های هدر HTTP مجاز](https://tools.ietf.org/html/rfc7230#section-3.2.6) هستند.
{{< /note >}}

{{< note >}}
`Impersonate-Uid` فقط در نسخه 1.22.0 و بالاتر در دسترس است.
{{< /note >}}

نمونه‌ای از هدرهای جعل هویت که هنگام جعل هویت کاربر دارای گروه‌ها استفاده می‌شود:

```http
Impersonate-User: jane.doe@example.com
Impersonate-Group: developers
Impersonate-Group: admins
```

نمونه‌ای از هدرهای جعل هویت که هنگام جعل هویت کاربر دارای UID و فیلدهای اضافی استفاده می‌شود:

```http
Impersonate-User: jane.doe@example.com
Impersonate-Uid: 06f6ce97-e2c5-4ab8-7ba5-7654dd08d52b
Impersonate-Extra-dn: cn=jane,ou=engineers,dc=example,dc=com
Impersonate-Extra-acme.com%2Fproject: some-project
Impersonate-Extra-scopes: view
Impersonate-Extra-scopes: development
```

هنگام استفاده از `kubectl`، آرگومان خط فرمان `--as` را برای پیکربندی هدر `Impersonate-User` تنظیم کنید؛ همچنین می‌توانید فلگ `--as-group` را برای پیکربندی هدر `Impersonate-Group`، فلگ `--as-uid` (نسخه 1.23) را برای پیکربندی هدر `Impersonate-Uid` و فلگ `--as-user-extra` (نسخه 1.35) را برای پیکربندی هدر `Impersonate-Extra-( extra name )` تنظیم کنید.

```bash
kubectl drain mynode
```

```none
Error from server (Forbidden): User "clark" cannot get nodes at the cluster scope. (get nodes mynode)
```

فلگ‌های `--as` و `--as-group` را تنظیم کنید:

```bash
kubectl drain mynode --as=superman --as-group=system:masters
```

```none
node/mynode cordoned
node/mynode drained
```

برای جعل هویت یک کاربر، شناسه کاربر (UID)، گروه یا فیلدهای اضافی، کاربر جعل‌کننده باید توانایی انجام فعل **impersonate** را روی نوع ویژگی‌ای که هویتش جعل می‌شود ("user"، "uid"، "group" و غیره) داشته باشد. در کلاسترهایی که افزونه مجوزدهی RBAC را فعال کرده‌اند، ClusterRole زیر شامل قواعد لازم برای تنظیم هدرهای جعل هویت کاربر و گروه است:

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

برای جعل هویت، فیلدهای اضافی و UIDهای جعل‌شده هر دو در `apiGroup` با نام "authentication.k8s.io" قرار دارند. فیلدهای اضافی به‌عنوان زیرمنبع‌های منبع "userextras" ارزیابی می‌شوند. برای اینکه به یک کاربر اجازه داده شود از هدرهای جعل هویت برای فیلد اضافی `scopes` و برای UIDها استفاده کند، باید نقش زیر به او اعطا شود:

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

مقادیر هدرهای جعل هویت را می‌توان با محدود کردن مجموعه `resourceNames` که یک منبع می‌تواند بگیرد نیز محدود کرد.

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
جعل هویت یک کاربر یا گروه به شما اجازه می‌دهد هر اقدامی را به‌گونه‌ای انجام دهید که گویی همان کاربر یا گروه هستید؛
به همین دلیل، جعل هویت محدود به فضای نام (namespace) نیست.
اگر می‌خواهید جعل هویت را با RBAC کوبرنتیز مجاز کنید،
باید از ClusterRole و ClusterRoleBinding استفاده کنید،
نه Role و RoleBinding.

اعطای مجوز جعل هویت روی ServiceAccountها محدود به فضای نام است، اما ServiceAccountِ جعل‌شده
می‌تواند اقداماتی را خارج از آن فضای نام انجام دهد.
{{< /note >}}

## جعل هویت محدودشده (Constrained Impersonation) {#constrained-impersonation}

{{< feature-state feature_gate_name="ConstrainedImpersonation" >}}

با فعل **impersonate** نمی‌توان جعل هویت را محدود یا حوزه‌بندی کرد.
این فعل یا جعل هویت کامل را اعطا می‌کند یا هیچ چیز. پس از اعطای مجوز جعل هویت یک کاربر،
می‌توانید هر اقدامی را که آن کاربر می‌تواند در تمام منابع و فضاهای نام انجام دهد، انجام دهید.

با جعل هویت محدودشده، جعل‌کننده را می‌توان طوری محدود کرد که فقط برای اقدامات مشخص روی منابع مشخص هویت کاربر دیگر را جعل کند، به‌جای آنکه بتواند همه اقدامات قابل‌انجام توسط کاربر جعل‌شده را انجام دهد.

این قابلیت با تنظیم `ConstrainedImpersonation`
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ConstrainedImpersonation)
فعال می‌شود.

### شناخت جعل هویت محدودشده

جعل هویت محدودشده به **دو مجوز جداگانه** نیاز دارد:

1. **مجوز جعل هویت یک هویت مشخص** (کاربر، UID، گروه، service account یا نود)
2. **مجوز انجام اقدامات مشخص در یک حوزه معین هنگام جعل هویت** (برای
   مثال، فقط `list` و `watch` روی podها در فضای نام `default`)

این بدان معناست که یک جعل‌کننده را می‌توان طوری محدود کرد که فقط برای عملیات مشخص هویت کاربر دیگر را جعل کند.

### حالت‌های جعل هویت

جعل هویت محدودشده سه حالت متمایز تعریف می‌کند که هر کدام مجموعه افعال خاص خود را دارد:

#### حالت user-info

از این حالت برای جعل هویت کاربران عمومی (نه service accountها یا نودها) استفاده کنید. این حالت زمانی اعمال می‌شود که مقدار هدر `Impersonate-User`:
- با `system:serviceaccount:` شروع **نشده** باشد
- با `system:node:` شروع **نشده** باشد

**افعال:**
- `impersonate:user-info` - مجوز جعل هویت یک کاربر، گروه، UID یا فیلد اضافی مشخص
- `impersonate-on:user-info:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت یک کاربر عمومی

#### حالت ServiceAccount

از این حالت برای جعل هویت ServiceAccountها استفاده کنید.

**افعال:**
- `impersonate:serviceaccount` - مجوز جعل هویت یک service account مشخص
- `impersonate-on:serviceaccount:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت یک service account

#### حالت‌های arbitrary-node و associated-node

از این حالت‌ها برای جعل هویت نودها استفاده کنید. این حالت زمانی اعمال می‌شود که مقدار هدر `Impersonate-User` با `system:node:` شروع شود.

**افعال:**
- `impersonate:arbitrary-node` - مجوز جعل هویت هر نود مشخص‌شده
- `impersonate:associated-node` - مجوز جعل هویت فقط نودی که جعل‌کننده به آن متصل است
- `impersonate-on:arbitrary-node:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت هر نود
- `impersonate-on:associated-node:<verb>` - مجوز انجام `<verb>` هنگام جعل هویت نود مرتبط

{{< note >}}
فعل `impersonate:associated-node` فقط زمانی اعمال می‌شود که جعل‌کننده یک service account باشد که به نودی که قصد جعل هویت آن را دارد متصل است. این موضوع با بررسی اینکه آیا اطلاعات کاربری service account شامل یک فیلد اضافی با کلید `authentication.kubernetes.io/node-name` است که با نودِ جعل‌شده مطابقت دارد، تعیین می‌شود.
{{< /note >}}

### پیکربندی جعل هویت محدودشده با RBAC

تمام مجوزهای جعل هویت محدودشده از API group با نام `authentication.k8s.io` استفاده می‌کنند. در ادامه نحوه پیکربندی حالت‌های مختلف آمده است.

#### مثال: جعل هویت یک کاربر برای اقدامات مشخص

این مثال نشان می‌دهد چگونه می‌توان به یک service account اجازه داد هویت کاربری به نام `jane.doe@example.com` را جعل کند، اما فقط برای `list` و `watch` روی podها در فضای نام `default`. برای مجوز هویت به یک `ClusterRoleBinding` و برای مجوز اقدام به یک `RoleBinding` نیاز دارید.

**گام 1: اعطای مجوز جعل هویت کاربر**

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

**گام 2: اعطای مجوز انجام اقدامات مشخص هنگام جعل هویت**

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

اکنون service account با نام `my-controller` می‌تواند هویت `jane.doe@example.com` را جعل کند تا podها را در فضای نام `default` فهرست کند و تغییرات آن‌ها را دنبال (watch) کند، اما **نمی‌تواند** اقدامات دیگری مانند حذف podها یا دسترسی به منابع در فضاهای نام دیگر را انجام دهد.

#### مثال: جعل هویت یک ServiceAccount

برای اجازه دادن به جعل هویت یک service account به نام `app-sa` در فضای نام `production` به‌منظور ایجاد و به‌روزرسانی deploymentها:

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

برای اجازه دادن به ServiceAccount با نام `node-impersonator` در فضای نام `default` برای جعل هویت نودی به نام `mynode` به‌منظور get و list کردن podها:

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

#### مثال: عامل نود که هویت نود مرتبط را جعل می‌کند

این یک الگوی رایج برای عامل‌های نود (مانند افزونه‌های CNI) است که باید podهای روی نود خود را بخوانند، بدون آنکه به podهای سراسر کلاستر دسترسی داشته باشند.

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

کنترل‌کننده نام نود را با استفاده از downward API دریافت می‌کند:

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

از دیدگاه کلاینت، استفاده از جعل هویت محدودشده با استفاده از جعل هویت سنتی یکسان است. شما از همان هدرهای جعل هویت استفاده می‌کنید:

```http
Impersonate-User: jane.doe@example.com
```

یا با kubectl:

```bash
kubectl get pods -n default --as=jane.doe@example.com
```

تفاوت کاملاً در بررسی‌های مجوزدهی است که سرور API انجام می‌دهد.

### کار با فعل `impersonate`

- اگر قواعد RBAC موجودی دارید که از فعل `impersonate` استفاده می‌کنند، این قواعد
  با فعال بودن feature gate همچنان کار می‌کنند.

- هنگامی که یک درخواست جعل هویت ارسال می‌شود، سرور API ابتدا مجوزهای جعل هویت محدودشده را بررسی می‌کند. اگر این بررسی‌ها ناموفق باشند، به بررسی مجوز
  `impersonate` بازمی‌گردد.

## ممیزی (Auditing) {#auditing}

برای هر درخواست جعل هویت یک رویداد ممیزی ثبت می‌شود تا ردیابی نحوه استفاده از جعل هویت آسان‌تر شود.

وقتی درخواستی از جعل هویت محدودشده استفاده می‌کند، رویداد ممیزی شامل یک آبجکت `authenticationMetadata` با فیلد `impersonationConstraint` است که نشان می‌دهد کدام فعل جعل هویت محدودشده برای مجاز کردن درخواست به کار رفته است.

برای درخواست‌های غیر از watch که بیش از 500 میلی‌ثانیه طول می‌کشند، سرور API همچنین یک حاشیه‌نویسی (annotation) با نام `apiserver.latency.k8s.io/impersonation` به رویداد ممیزی اضافه می‌کند که زمان صرف‌شده برای پردازش جعل هویت (به‌همراه سایر handlerهایی که در مدت زمان کل مشارکت داشته‌اند) را ثبت می‌کند.

نمونه رویداد ممیزی:

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

مقدار `impersonationConstraint` نشان می‌دهد کدام حالت استفاده شده است (برای مثال `impersonate:user-info` یا `impersonate:associated-node`). اقدام مشخص (برای مثال `list`) را می‌توان از فیلد `verb` در رویداد ممیزی تشخیص داد. برای درخواست‌های کند، حاشیه‌نویسی تأخیر، زمان صرف‌شده (برای مثال `100ms`) برای پردازش جعل هویت آن درخواست را ثبت می‌کند.

## متریک‌ها (Metrics) {#metrics}

`kube-apiserver` متریک‌های Prometheus زیر را برای جعل هویت محدودشده ارائه می‌کند:

- `apiserver_impersonation_attempts_total{mode, decision}`: شمارنده‌ای که با هر تلاش برای جعل هویت افزایش می‌یابد. مقدار `mode` یکی از `associated-node`،
  `arbitrary-node`، `serviceaccount`، `user-info` یا `legacy` است. مقدار `decision` برابر `allowed` یا `denied` است.
- `apiserver_impersonation_attempts_duration_seconds{mode, decision}`: یک هیستوگرام که زمان صرف‌شده برای
  تعیین کاربر جعل‌شده را دنبال می‌کند. برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند. به‌دلیل
  کش‌کردن درون handler، این متریک هزینه تأخیر سرشکن‌شده درخواست‌های جعل هویت را نشان می‌دهد.
- `apiserver_impersonation_authorization_attempts_total{mode, decision}`: شمارنده‌ای که هر بار
  که یک تلاش برای جعل هویت authorizer را فراخوانی می‌کند افزایش می‌یابد. برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند.
- `apiserver_impersonation_authorization_attempts_duration_seconds{mode, decision}`: یک هیستوگرام
  که زمان صرف‌شده توسط authorizer را برای هر تلاش جعل هویت دنبال می‌کند.
  برچسب‌های `mode` و `decision` همان مقادیر بالا را دارند.

برای متریک‌های `apiserver_impersonation_attempts_total{mode, decision}` و
`apiserver_impersonation_attempts_duration_seconds{mode, decision}`، هنگامی که `decision` برابر `denied` باشد، مقدار `mode`
رشته خالی است.

## {{% heading "whatsnext" %}}

- درباره [مجوزدهی RBAC](/docs/reference/access-authn-authz/rbac/) بخوانید
- با [احراز هویت در کوبرنتیز](/docs/reference/access-authn-authz/authentication/) آشنا شوید

---
reviewers:
- erictune
- deads2k
- liggitt
title: استفاده از مجوزدهی RBAC
content_type: concept
aliases: [/rbac/]
weight: 33
---

<!-- overview -->
کنترل دسترسی مبتنی بر نقش (RBAC) روشی برای تنظیم و مدیریت دسترسی به منابع رایانه‌ای یا شبکه‌ای است که بر اساس نقش‌های کاربران منفرد در سازمان شما عمل می‌کند.


<!-- body -->
مجوزدهی RBAC از {{< glossary_tooltip text="گروه API" term_id="api-group" >}} با نام `rbac.authorization.k8s.io` برای هدایت تصمیم‌های مجوزدهی استفاده می‌کند و به شما امکان می‌دهد سیاست‌ها را به‌صورت پویا از طریق API کوبرنتیز پیکربندی کنید.

برای فعال‌سازی RBAC، {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} را با فلگ `--authorization-config` اجرا کنید و مقدار آن را فایلی قرار دهید که شامل authorizer با نوع `RBAC` باشد؛ برای مثال:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  ...
  - type: RBAC
  ...
```

یا {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} را با فلگ `--authorization-mode` اجرا کنید و مقدار آن را فهرستی جداشده با کاما قرار دهید که شامل `RBAC` باشد؛
برای مثال:
```shell
kube-apiserver --authorization-mode=...,RBAC --other-options --more-options
```

## آبجکت‌های API {#api-overview}

API مربوط به RBAC چهار نوع آبجکت کوبرنتیز را تعریف می‌کند: _Role_، _ClusterRole_،
_RoleBinding_ و _ClusterRoleBinding_. شما می‌توانید {{< glossary_tooltip text="آبجکت‌های" term_id="object" >}} RBAC را مانند هر آبجکت دیگر کوبرنتیز با ابزارهایی مانند `kubectl` توصیف یا اصلاح کنید.

{{< caution >}}
این آبجکت‌ها بنا به طراحی، محدودیت‌های دسترسی اعمال می‌کنند. اگر در حین یادگیری در یک کلاستر تغییراتی ایجاد می‌کنید، برای درک اینکه این محدودیت‌ها چگونه می‌توانند مانع انجام برخی تغییرات شوند، بخش
[پیشگیری از ارتقای سطح دسترسی و راه‌اندازی اولیه](#privilege-escalation-prevention-and-bootstrapping)
را مطالعه کنید.
{{< /caution >}}

### Role و ClusterRole

یک _Role_ یا _ClusterRole_ در RBAC شامل قواعدی است که مجموعه‌ای از مجوزها را نشان می‌دهند.
مجوزها صرفاً افزایشی هستند (قاعده‌ای از نوع «deny» وجود ندارد).

یک Role همیشه مجوزها را درون یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} مشخص تعیین می‌کند؛
هنگام ایجاد یک Role باید فضای نامی را که به آن تعلق دارد مشخص کنید.

در مقابل، ClusterRole یک منبع بدون فضای نام (non-namespaced) است. نام این منابع متفاوت است (Role
و ClusterRole)، زیرا یک آبجکت کوبرنتیز همیشه باید یا دارای فضای نام باشد یا نباشد؛
نمی‌تواند هر دو باشد.

ClusterRoleها کاربردهای متعددی دارند. شما می‌توانید از یک ClusterRole برای موارد زیر استفاده کنید:

1. تعریف مجوزها روی منابعی که دارای فضای نام هستند و اعطای دسترسی در یک یا چند فضای نام مشخص
1. تعریف مجوزها روی منابعی که دارای فضای نام هستند و اعطای دسترسی در تمام فضاهای نام
1. تعریف مجوزها روی منابعی که در سطح کلاستر تعریف می‌شوند

اگر می‌خواهید نقشی را درون یک فضای نام تعریف کنید، از Role استفاده کنید؛ اگر می‌خواهید
نقشی را در سطح کل کلاستر تعریف کنید، از ClusterRole استفاده کنید.

#### نمونه Role

در اینجا نمونه‌ای از یک Role در فضای نام «default» آورده شده است که می‌توان از آن برای اعطای دسترسی خواندن به
{{< glossary_tooltip text="پادها" term_id="pod" >}} استفاده کرد:

{{% code_sample file="access/simple-role.yaml" %}}

#### نمونه ClusterRole

از یک ClusterRole می‌توان برای اعطای همان مجوزهای یک Role استفاده کرد.
از آنجا که ClusterRoleها در سطح کلاستر تعریف می‌شوند، می‌توانید از آن‌ها برای اعطای دسترسی به موارد زیر نیز استفاده کنید:

* منابع در سطح کلاستر (مانند {{< glossary_tooltip text="نودها" term_id="node" >}})
* endpointهای غیرمنبعی (مانند `/healthz`)
* منابع دارای فضای نام (مانند Pod) در تمام فضاهای نام

  برای مثال: می‌توانید از یک ClusterRole استفاده کنید تا به یک کاربر مشخص اجازه دهید
  دستور `kubectl get pods --all-namespaces` را اجرا کند.

در ادامه نمونه‌ای از یک ClusterRole آورده شده است که می‌توان از آن برای اعطای دسترسی خواندن به
{{< glossary_tooltip text="Secretها" term_id="secret" >}} در هر فضای نام مشخص،
یا در تمام فضاهای نام استفاده کرد (بسته به اینکه چگونه [متصل](#rolebinding-and-clusterrolebinding) شود):

{{% code_sample file="access/simple-clusterrole.yaml" %}}

نام یک آبجکت Role یا ClusterRole باید یک
[نام معتبر برای path segment](/docs/concepts/overview/working-with-objects/names#path-segment-names) باشد.

### RoleBinding و ClusterRoleBinding

یک role binding مجوزهای تعریف‌شده در یک role را به یک کاربر یا مجموعه‌ای از کاربران اعطا می‌کند.
این آبجکت شامل فهرستی از *subjectها* (کاربران، گروه‌ها یا service accountها) و یک ارجاع به
role اعطاشده است.
یک RoleBinding مجوزها را درون یک فضای نام مشخص اعطا می‌کند، در حالی که یک ClusterRoleBinding
همان دسترسی را در سطح کل کلاستر اعطا می‌کند.

یک RoleBinding می‌تواند به هر Role موجود در همان فضای نام ارجاع دهد. همچنین یک RoleBinding
می‌تواند به یک ClusterRole ارجاع دهد و آن ClusterRole را به فضای نام خود RoleBinding متصل کند.
اگر می‌خواهید یک ClusterRole را به تمام فضاهای نام کلاستر خود متصل کنید، از یک
ClusterRoleBinding استفاده می‌کنید.

نام یک آبجکت RoleBinding یا ClusterRoleBinding باید یک
[نام معتبر برای path segment](/docs/concepts/overview/working-with-objects/names#path-segment-names) باشد.

#### نمونه‌های RoleBinding {#rolebinding-example}

در ادامه نمونه‌ای از یک RoleBinding آورده شده است که Role با نام «pod-reader» را به کاربر «jane»
درون فضای نام «default» اعطا می‌کند.
این کار به «jane» اجازه می‌دهد پادهای فضای نام «default» را بخواند.

{{% code_sample file="access/simple-rolebinding-with-role.yaml" %}}

یک RoleBinding همچنین می‌تواند به یک ClusterRole ارجاع دهد تا مجوزهای تعریف‌شده در آن ClusterRole را به منابع درون فضای نام همان RoleBinding اعطا کند. این نوع ارجاع
به شما امکان می‌دهد مجموعه‌ای از نقش‌های مشترک را در سراسر کلاستر تعریف کنید و سپس آن‌ها را در
چندین فضای نام دوباره به کار ببرید.

برای مثال، با اینکه RoleBinding زیر به یک ClusterRole ارجاع می‌دهد،
کاربر «dave» (subject، حساس به حروف بزرگ و کوچک) فقط می‌تواند Secretها را در فضای نام «development» بخواند،
زیرا فضای نام RoleBinding (در metadata آن) «development» است.

{{% code_sample file="access/simple-rolebinding-with-clusterrole.yaml" %}}

#### نمونه ClusterRoleBinding

برای اعطای مجوزها در سطح کل کلاستر می‌توانید از یک ClusterRoleBinding استفاده کنید.
ClusterRoleBinding زیر به هر کاربر عضو گروه «manager» اجازه می‌دهد
Secretها را در هر فضای نام بخواند.

{{% code_sample file="access/simple-clusterrolebinding.yaml" %}}

پس از ایجاد یک binding، دیگر نمی‌توانید Role یا ClusterRole ارجاع‌شده در آن را تغییر دهید.
اگر سعی کنید `roleRef` یک binding را تغییر دهید، با خطای اعتبارسنجی مواجه می‌شوید. اگر واقعاً می‌خواهید
`roleRef` یک binding را تغییر دهید، باید آبجکت binding را حذف کنید و یک جایگزین ایجاد کنید.

این محدودیت دو دلیل دارد:

1. تغییرناپذیر بودن `roleRef` این امکان را فراهم می‌کند که مجوز `update` روی یک آبجکت binding موجود به کسی اعطا شود تا بتواند فهرست subjectها را مدیریت کند، بدون اینکه بتواند
   نقشی را که به آن subjectها اعطا شده است تغییر دهد.
1. یک binding به نقشی متفاوت، در اصل یک binding کاملاً متفاوت است.
   الزام به حذف و ایجاد مجدد binding برای تغییر `roleRef`
   تضمین می‌کند که کل فهرست subjectهای موجود در binding واقعاً قرار است
   نقش جدید را دریافت کنند (برخلاف حالتی که فقط `roleRef` فعال یا به‌طور تصادفی تغییر داده شود،
   بدون اینکه بررسی شود آیا همه subjectهای موجود باید مجوزهای نقش جدید را دریافت کنند).

ابزار خط فرمان `kubectl auth reconcile` یک فایل مانیفست حاوی آبجکت‌های RBAC را ایجاد یا به‌روزرسانی می‌کند،
و در صورت نیاز برای تغییر نقش ارجاع‌شده، حذف و ایجاد مجدد آبجکت‌های binding را نیز انجام می‌دهد.
برای اطلاعات بیشتر به [نحوه استفاده از دستور و نمونه‌ها](#kubectl-auth-reconcile) مراجعه کنید.

### ارجاع به منابع {#referring-to-resources}

در API کوبرنتیز، بیشتر منابع با یک نمایش رشته‌ای از نام آبجکت خود نمایش داده می‌شوند و از همین طریق به آن‌ها دسترسی پیدا می‌شود، مانند `pods` برای یک Pod. RBAC دقیقاً با همان نامی به منابع ارجاع می‌دهد
که در URL مربوط به endpoint مرتبط API ظاهر می‌شود.
برخی از APIهای کوبرنتیز شامل یک
_زیرمنبع_ (subresource) هستند، مانند لاگ‌های یک Pod. درخواست دریافت لاگ‌های یک Pod به این شکل است:

```http
GET /api/v1/namespaces/{namespace}/pods/{name}/log
```

در این مثال، `pods` منبع دارای فضای نام برای منابع Pod است و `log` یک
زیرمنبع از `pods` است. برای نمایش این موضوع در یک role از نوع RBAC، از یک اسلش (`/`) برای
جدا کردن منبع و زیرمنبع استفاده کنید. برای اینکه به یک subject اجازه دهید `pods` را بخواند و
همچنین به زیرمنبع `log` هر یک از آن Podها دسترسی داشته باشد، به این صورت می‌نویسید:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-and-pod-logs-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list"]
```

همچنین می‌توانید برای برخی درخواست‌ها از طریق فهرست `resourceNames` بر اساس نام به منابع ارجاع دهید.
در صورت تعیین این فهرست، درخواست‌ها را می‌توان به نمونه‌های منفرد یک منبع محدود کرد.
در ادامه نمونه‌ای آورده شده است که subject را فقط به `get` یا `update` یک
{{< glossary_tooltip term_id="ConfigMap" >}} با نام `my-configmap` محدود می‌کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: configmap-updater
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing ConfigMap
  # objects is "configmaps"
  resources: ["configmaps"]
  resourceNames: ["my-configmap"]
  verbs: ["update", "get"]
```

{{< note >}}
شما نمی‌توانید درخواست‌های **deletecollection** یا درخواست‌های **create** سطح بالا را بر اساس نام منبع محدود کنید.
در مورد **create**، این محدودیت به این دلیل است که ممکن است نام آبجکت جدید در زمان مجوزدهی هنوز مشخص نباشد. با این حال، محدودیت **create** فقط برای منابع سطح بالا اعمال می‌شود، نه زیرمنابع. برای مثال، می‌توانید از فیلد `resourceNames` با `pods/exec` استفاده کنید.
اگر **list** یا **watch** را بر اساس `resourceName` محدود کنید، کلاینت‌ها باید برای مجاز شدن، یک انتخابگر فیلد (field selector) به نام `metadata.name` را در درخواست **list** یا **watch** خود قرار دهند (که با `resourceName` مشخص‌شده مطابقت داشته باشد).
برای مثال: `kubectl get configmaps --field-selector=metadata.name=my-configmap`
{{< /note >}}

به‌جای ارجاع به `resources`، `apiGroups` و `verbs` به‌صورت منفرد،
می‌توانید از نماد wildcard یعنی `*` برای ارجاع به همه این موارد استفاده کنید.
برای `nonResourceURLs` می‌توانید از wildcard با نماد `*` به‌عنوان تطبیق glob پسوندی استفاده کنید.
برای `resourceNames`، مجموعه خالی به این معناست که همه چیز مجاز است.
در ادامه نمونه‌ای آورده شده است که اجازه انجام هر اقدام فعلی و آینده را روی
تمام منابع فعلی و آینده در گروه API با نام `example.com` می‌دهد.
این مشابه نقش داخلی `cluster-admin` است.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: example.com-superuser # DO NOT USE THIS ROLE, IT IS JUST AN EXAMPLE
rules:
- apiGroups: ["example.com"]
  resources: ["*"]
  verbs: ["*"]
```

{{< caution >}}
استفاده از wildcard در ورودی‌های منبع و verb می‌تواند منجر به اعطای دسترسی بیش از حد به منابع حساس شود.
برای مثال، اگر نوع منبع جدیدی اضافه شود، یا زیرمنبع جدیدی افزوده شود،
یا یک verb سفارشی جدید بررسی شود، ورودی wildcard به‌طور خودکار دسترسی را اعطا می‌کند، که ممکن است مطلوب نباشد.
[اصل حداقل امتیاز](/docs/concepts/security/rbac-good-practices/#least-privilege)
باید رعایت شود و با استفاده از منابع و verbهای مشخص، تنها مجوزهای موردنیاز برای عملکرد صحیح
بار کاری اعمال شوند.
{{< /caution >}}

### ClusterRoleهای تجمیعی (Aggregated) {#aggregated-clusterroles}

شما می‌توانید چندین ClusterRole را در یک ClusterRole ترکیبی _تجمیع_ (aggregate) کنید.
یک کنترل‌کننده که به‌عنوان بخشی از control plane کلاستر اجرا می‌شود، آبجکت‌های ClusterRole
را که `aggregationRule` روی آن‌ها تنظیم شده است زیر نظر دارد. `aggregationRule` یک
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}} برچسب تعریف می‌کند که کنترل‌کننده
از آن برای یافتن سایر آبجکت‌های ClusterRole استفاده می‌کند که باید در فیلد `rules`
این ClusterRole ترکیب شوند.

{{< caution >}}
control plane هر مقداری را که به‌صورت دستی در فیلد `rules` یک ClusterRole تجمیعی مشخص کنید بازنویسی می‌کند. اگر می‌خواهید قواعد را تغییر دهید یا قاعده‌ای اضافه کنید، این کار را در آبجکت‌های `ClusterRole` انجام دهید
که توسط `aggregationRule` انتخاب می‌شوند.

فیلد `rules` را از مانیفست‌های ClusterRoleهای تجمیعی حذف کنید. تنظیم این فیلد، حتی با یک
فهرست خالی، هنگام اعمال مانیفست با
[server-side apply](/docs/reference/using-api/server-side-apply/) مالکیت فیلد را ادعا می‌کند. این مالکیت باعث
تعارض بین اعمال‌کننده و control plane می‌شود: اعمال‌های بعدی یا با تعارض field manager روی `.rules` شکست می‌خورند،
یا (اگر تعارض‌ها به‌اجبار حل شوند، همان‌طور که کنترل‌کننده‌های GitOps معمولاً چنین می‌کنند) قواعد تجمیعی را به‌طور مکرر پاک می‌کنند و control plane دوباره
آن‌ها را پر می‌کند.
{{< /caution >}}

در ادامه نمونه‌ای از یک ClusterRole تجمیعی آورده شده است:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: monitoring
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      rbac.example.com/aggregate-to-monitoring: "true"
# The control plane automatically fills in the rules
```

اگر یک ClusterRole جدید ایجاد کنید که با انتخابگر برچسب یک ClusterRole تجمیعی موجود مطابقت داشته باشد،
این تغییر باعث می‌شود قواعد جدید به ClusterRole تجمیعی اضافه شوند.
در ادامه نمونه‌ای آورده شده است که با ایجاد یک ClusterRole دیگر با برچسب `rbac.example.com/aggregate-to-monitoring: true`، قواعدی را به ClusterRole با نام «monitoring» اضافه می‌کند.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: monitoring-endpointslices
  labels:
    rbac.example.com/aggregate-to-monitoring: "true"
# When you create the "monitoring-endpointslices" ClusterRole,
# the rules below will be added to the "monitoring" ClusterRole.
rules:
- apiGroups: [""]
  resources: ["services", "pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["discovery.k8s.io"]
  resources: ["endpointslices"]
  verbs: ["get", "list", "watch"]
```

[نقش‌های پیش‌فرض کاربرمحور](#default-roles-and-role-bindings) از تجمیع ClusterRole استفاده می‌کنند. این امر به شما، به‌عنوان مدیر کلاستر، امکان می‌دهد
قواعدی را برای منابع سفارشی، مانند منابعی که توسط
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitionها" >}}
یا سرورهای API تجمیعی ارائه می‌شوند، بگنجانید تا نقش‌های پیش‌فرض را گسترش دهید.

برای مثال: ClusterRoleهای زیر به نقش‌های پیش‌فرض «admin» و «edit» اجازه می‌دهند منبع سفارشی
با نام CronTab را مدیریت کنند، در حالی که نقش «view» فقط می‌تواند عملیات خواندن را روی منابع CronTab انجام دهد.
می‌توانید فرض کنید آبجکت‌های CronTab در URLهایی که سرور API می‌بیند با نام `"crontabs"` شناخته می‌شوند.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: aggregate-cron-tabs-edit
  labels:
    # Add these permissions to the "admin" and "edit" default roles.
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
rules:
- apiGroups: ["stable.example.com"]
  resources: ["crontabs"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: aggregate-cron-tabs-view
  labels:
    # Add these permissions to the "view" default role.
    rbac.authorization.k8s.io/aggregate-to-view: "true"
rules:
- apiGroups: ["stable.example.com"]
  resources: ["crontabs"]
  verbs: ["get", "list", "watch"]
```

#### نمونه‌های Role

نمونه‌های زیر گزیده‌هایی از آبجکت‌های Role یا ClusterRole هستند که فقط
بخش `rules` را نشان می‌دهند.

اجازه خواندن منابع `"pods"` در
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} هسته (core):

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing Pod
  # objects is "pods"
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

اجازه خواندن/نوشتن Deploymentها (در سطح HTTP: آبجکت‌هایی که `"deployments"`
در بخش منبع URL آن‌ها وجود دارد) در گروه‌های API با نام `"apps"`:

```yaml
rules:
- apiGroups: ["apps"]
  #
  # at the HTTP level, the name of the resource for accessing Deployment
  # objects is "deployments"
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

اجازه خواندن Podها در گروه API هسته، و همچنین خواندن یا نوشتن منابع Job
در گروه API با نام `"batch"`:

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing Pod
  # objects is "pods"
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["batch"]
  #
  # at the HTTP level, the name of the resource for accessing Job
  # objects is "jobs"
  resources: ["jobs"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

اجازه خواندن یک ConfigMap با نام «my-config» (برای محدود کردن به یک ConfigMap واحد در یک فضای نام واحد،
باید با یک RoleBinding متصل شود):

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing ConfigMap
  # objects is "configmaps"
  resources: ["configmaps"]
  resourceNames: ["my-config"]
  verbs: ["get"]
```

اجازه خواندن منبع `"nodes"` در گروه هسته (از آنجا که Node
در سطح کلاستر تعریف می‌شود، برای مؤثر بودن باید در یک ClusterRole باشد که با یک
ClusterRoleBinding متصل شده است):

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing Node
  # objects is "nodes"
  resources: ["nodes"]
  verbs: ["get", "list", "watch"]
```

اجازه درخواست‌های GET و POST به endpoint غیرمنبعی `/healthz` و
تمام زیرمسیرهای آن (برای مؤثر بودن باید در یک ClusterRole باشد که با یک ClusterRoleBinding متصل شده است):

```yaml
rules:
- nonResourceURLs: ["/healthz", "/healthz/*"] # '*' in a nonResourceURL is a suffix glob match
  verbs: ["get", "post"]
```

### ارجاع به subjectها

یک RoleBinding یا ClusterRoleBinding یک نقش را به subjectها متصل می‌کند.
subjectها می‌توانند گروه، کاربر یا
{{< glossary_tooltip text="ServiceAccountها" term_id="service-account" >}} باشند.

کوبرنتیز نام‌های کاربری را به‌صورت رشته نمایش می‌دهد.
این نام‌ها می‌توانند نام‌های ساده مانند "alice"، نام‌هایی به سبک ایمیل مانند "bob@example.com"،
یا شناسه‌های کاربری عددی باشند که به‌صورت رشته نمایش داده می‌شوند. این بر عهده شما به‌عنوان مدیر کلاستر است
که [ماژول‌های احراز هویت](/docs/reference/access-authn-authz/authentication/) را طوری پیکربندی کنید
که احراز هویت، نام‌های کاربری را با قالب مورد نظر شما تولید کند.

{{< caution >}}
پیشوند `system:` برای استفاده سیستمی کوبرنتیز رزرو شده است، بنابراین باید مطمئن شوید
که به‌طور اتفاقی کاربر یا گروهی با نامی که با `system:` شروع می‌شود ندارید.
جدا از این پیشوند ویژه، سیستم مجوزدهی RBAC هیچ قالب خاصی را
برای نام‌های کاربری الزامی نمی‌کند.
{{< /caution >}}

در کوبرنتیز، ماژول‌های Authenticator اطلاعات گروه را فراهم می‌کنند.
گروه‌ها نیز مانند کاربران به‌صورت رشته نمایش داده می‌شوند و این رشته هیچ الزام قالبی ندارد،
جز اینکه پیشوند `system:` رزرو شده است.

[ServiceAccountها](/docs/tasks/configure-pod-container/configure-service-account/) نام‌هایی با پیشوند
`system:serviceaccount:` دارند و به گروه‌هایی تعلق دارند که نام آن‌ها با پیشوند `system:serviceaccounts:` شروع می‌شود.

{{< note >}}
- `system:serviceaccount:` (مفرد) پیشوند نام‌های کاربری service account است.
- `system:serviceaccounts:` (جمع) پیشوند گروه‌های service account است.
{{< /note >}}

#### نمونه‌های RoleBinding {#role-binding-examples}

نمونه‌های زیر بخش‌هایی از یک `RoleBinding` هستند که فقط
بخش `subjects` را نشان می‌دهند.

برای کاربری با نام `alice@example.com`:

```yaml
subjects:
- kind: User
  name: "alice@example.com"
  apiGroup: rbac.authorization.k8s.io
```

برای گروهی با نام `frontend-admins`:

```yaml
subjects:
- kind: Group
  name: "frontend-admins"
  apiGroup: rbac.authorization.k8s.io
```

برای service account پیش‌فرض در فضای نام (namespace) «kube-system»:

```yaml
subjects:
- kind: ServiceAccount
  name: default
  namespace: kube-system
```

برای همه service accountها در فضای نام «qa»:

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts:qa
  apiGroup: rbac.authorization.k8s.io
```

برای همه service accountها در هر فضای نام:

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts
  apiGroup: rbac.authorization.k8s.io
```

برای همه کاربران احراز هویت‌شده:

```yaml
subjects:
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
```

برای همه کاربران احراز هویت‌نشده:

```yaml
subjects:
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
```

برای همه کاربران:

```yaml
subjects:
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
```

## نقش‌ها و اتصال‌های نقش پیش‌فرض

API serverها مجموعه‌ای از آبجکت‌های ClusterRole و ClusterRoleBinding پیش‌فرض را ایجاد می‌کنند.
بسیاری از این آبجکت‌ها با پیشوند `system:` شروع می‌شوند که نشان می‌دهد منبع
مستقیماً توسط control plane کلاستر مدیریت می‌شود.
همه ClusterRoleها و ClusterRoleBindingهای پیش‌فرض با برچسب `kubernetes.io/bootstrapping=rbac-defaults` برچسب‌گذاری شده‌اند.

{{< caution >}}
هنگام تغییر ClusterRoleها و ClusterRoleBindingهایی که نام آن‌ها
پیشوند `system:` دارد، دقت کنید.
تغییر در این منابع می‌تواند باعث از کار افتادن کلاستر شود.
{{< /caution >}}

### تطبیق خودکار (Auto-reconciliation)

در هر بار راه‌اندازی، API server نقش‌های کلاستری پیش‌فرض را با مجوزهای ازدست‌رفته به‌روزرسانی می‌کند
و اتصال‌های نقش کلاستری پیش‌فرض را با subjectهای ازدست‌رفته به‌روزرسانی می‌کند.
این کار به کلاستر امکان می‌دهد تغییرات تصادفی را اصلاح کند و کمک می‌کند نقش‌ها و اتصال‌های نقش
با تغییر مجوزها و subjectها در نسخه‌های جدید کوبرنتیز به‌روز بمانند.

برای انصراف از این تطبیق، حاشیه‌نویسی (annotation) `rbac.authorization.kubernetes.io/autoupdate`
را روی یک نقش کلاستری پیش‌فرض یا یک RoleBinding کلاستری پیش‌فرض برابر `false` قرار دهید.
توجه داشته باشید که ازدست‌رفتن مجوزها و subjectهای پیش‌فرض می‌تواند باعث از کار افتادن کلاستر شود.

اگر RBAC authorizer فعال باشد، تطبیق خودکار به‌طور پیش‌فرض فعال است.

### نقش‌های کشف API {#discovery-roles}

اتصال‌های نقش کلاستری پیش‌فرض، کاربران احراز هویت‌نشده و احراز هویت‌شده را برای خواندن اطلاعات API
که امن و قابل دسترسی عمومی تلقی می‌شود (از جمله CustomResourceDefinitionها) مجاز می‌کنند.
برای غیرفعال‌سازی دسترسی ناشناس احراز هویت‌نشده، پرچم `--anonymous-auth=false` را به
پیکربندی API server اضافه کنید.

برای مشاهده پیکربندی این نقش‌ها از طریق `kubectl` دستور زیر را اجرا کنید:

```shell
kubectl get clusterroles system:discovery -o yaml
```

{{< note >}}
اگر این ClusterRole را ویرایش کنید، تغییرات شما هنگام راه‌اندازی مجدد API server
از طریق [تطبیق خودکار](#auto-reconciliation) بازنویسی خواهد شد. برای جلوگیری از این بازنویسی،
یا نقش را به‌صورت دستی ویرایش نکنید یا تطبیق خودکار را غیرفعال کنید.
{{< /note >}}

<table>
<caption>نقش‌های کشف API در RBAC کوبرنتیز</caption>
<colgroup><col style="width: 25%;" /><col style="width: 25%;" /><col /></colgroup>
<thead>
<tr>
<th>ClusterRole پیش‌فرض</th>
<th>ClusterRoleBinding پیش‌فرض</th>
<th>توضیحات</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>system:basic-user</b></td>
<td>گروه <b>system:authenticated</b></td>
<td>به کاربر اجازه می‌دهد به اطلاعات پایه درباره خودش دسترسی فقط‌خواندنی داشته باشد. پیش از v1.14، این نقش به‌طور پیش‌فرض به <tt>system:unauthenticated</tt> نیز متصل بود.</td>
</tr>
<tr>
<td><b>system:discovery</b></td>
<td>گروه <b>system:authenticated</b></td>
<td>دسترسی فقط‌خواندنی به endpointهای کشف API را که برای کشف و مذاکره سطح API لازم هستند، فراهم می‌کند. پیش از v1.14، این نقش به‌طور پیش‌فرض به <tt>system:unauthenticated</tt> نیز متصل بود.</td>
</tr>
<tr>
<td><b>system:public-info-viewer</b></td>
<td>گروه‌های <b>system:authenticated</b> و <b>system:unauthenticated</b></td>
<td>دسترسی فقط‌خواندنی به اطلاعات غیرحساس درباره کلاستر را فراهم می‌کند. در کوبرنتیز v1.14 معرفی شد.</td>
</tr>
</tbody>
</table>

### نقش‌های مخصوص کاربر

برخی از ClusterRoleهای پیش‌فرض پیشوند `system:` ندارند. این نقش‌ها برای استفاده مستقیم کاربران در نظر گرفته شده‌اند.
آن‌ها شامل نقش‌های سوپریوزر (`cluster-admin`)، نقش‌هایی که قرار است با استفاده از ClusterRoleBindingها
در سطح کل کلاستر اعطا شوند، و نقش‌هایی که قرار است با استفاده از RoleBindingها در فضاهای نام
مشخص اعطا شوند (`admin`، `edit`، `view`) هستند.

ClusterRoleهای مخصوص کاربر از [تجمیع ClusterRole](#aggregated-clusterroles) استفاده می‌کنند تا مدیران بتوانند
قواعد مربوط به منابع سفارشی را به این ClusterRoleها اضافه کنند. برای افزودن قواعد به نقش‌های `admin`، `edit` یا `view`،
یک ClusterRole با یک یا چند مورد از برچسب‌های زیر ایجاد کنید:

```yaml
metadata:
  labels:
    rbac.authorization.k8s.io/aggregate-to-admin: "true"
    rbac.authorization.k8s.io/aggregate-to-edit: "true"
    rbac.authorization.k8s.io/aggregate-to-view: "true"
```

<table>
<colgroup><col style="width: 25%;" /><col style="width: 25%;" /><col /></colgroup>
<thead>
<tr>
<th>ClusterRole پیش‌فرض</th>
<th>ClusterRoleBinding پیش‌فرض</th>
<th>توضیحات</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>cluster-admin</b></td>
<td>گروه <b>system:masters</b></td>
<td>دسترسی سوپریوزر را برای انجام هر عملی روی هر منبع فراهم می‌کند.
هنگامی که در یک <b>ClusterRoleBinding</b> استفاده شود، کنترل کامل بر هر منبع در کلاستر و در همه فضاهای نام را می‌دهد.
هنگامی که در یک <b>RoleBinding</b> استفاده شود، کنترل کامل بر هر منبع در فضای نام همان اتصال نقش، از جمله خود فضای نام، را می‌دهد.</td>
</tr>
<tr>
<td><b>admin</b></td>
<td>ندارد</td>
<td>دسترسی مدیریتی را فراهم می‌کند و قرار است با استفاده از یک <b>RoleBinding</b> در یک فضای نام اعطا شود.

اگر در یک <b>RoleBinding</b> استفاده شود، دسترسی خواندن/نوشتن به بیشتر منابع در یک فضای نام را می‌دهد،
از جمله توانایی ایجاد نقش‌ها و اتصال‌های نقش در همان فضای نام.
این نقش دسترسی نوشتن به resource quota یا به خود فضای نام را نمی‌دهد.
همچنین این نقش در کلاسترهای ایجادشده با کوبرنتیز v1.22 و بالاتر، دسترسی نوشتن به EndpointSlices را نمی‌دهد.
اطلاعات بیشتر در
[بخش «دسترسی نوشتن برای EndpointSlices»](#write-access-for-endpoints) موجود است.</td>
</tr>
<tr>
<td><b>edit</b></td>
<td>ندارد</td>
<td>دسترسی خواندن/نوشتن به بیشتر آبجکت‌ها در یک فضای نام را فراهم می‌کند.

این نقش اجازه مشاهده یا تغییر نقش‌ها یا اتصال‌های نقش را نمی‌دهد.
با این حال، این نقش امکان دسترسی به Secretها و اجرای Podها با هر ServiceAccount در
فضای نام را می‌دهد، بنابراین می‌توان از آن برای کسب سطوح دسترسی API هر ServiceAccount در
فضای نام استفاده کرد. همچنین این نقش در کلاسترهای ایجادشده با کوبرنتیز v1.22 و بالاتر،
دسترسی نوشتن به EndpointSlices را نمی‌دهد. اطلاعات بیشتر در
[بخش «دسترسی نوشتن برای EndpointSlices»](#write-access-for-endpoints) موجود است.</td>
</tr>
<tr>
<td><b>view</b></td>
<td>ندارد</td>
<td>دسترسی فقط‌خواندنی برای مشاهده بیشتر آبجکت‌ها در یک فضای نام را فراهم می‌کند.
این نقش اجازه مشاهده نقش‌ها یا اتصال‌های نقش را نمی‌دهد.

این نقش اجازه مشاهده Secretها را نمی‌دهد، زیرا خواندن
محتوای Secretها امکان دسترسی به اعتبارنامه‌های ServiceAccount
در فضای نام را فراهم می‌کند که به‌نوبه خود امکان دسترسی API با هویت هر ServiceAccount
در فضای نام را می‌دهد (نوعی ارتقای سطح دسترسی).</td>
</tr>
</tbody>
</table>

### نقش‌های مؤلفه‌های اصلی

<table>
<colgroup><col style="width: 25%;" /><col style="width: 25%;" /><col /></colgroup>
<thead>
<tr>
<th>ClusterRole پیش‌فرض</th>
<th>ClusterRoleBinding پیش‌فرض</th>
<th>توضیحات</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>system:kube-scheduler</b></td>
<td>کاربر <b>system:kube-scheduler</b></td>
<td>دسترسی به منابع موردنیاز مؤلفه {{< glossary_tooltip term_id="kube-scheduler" text="زمان‌بند" >}} را فراهم می‌کند.</td>
</tr>
<tr>
<td><b>system:volume-scheduler</b></td>
<td>کاربر <b>system:kube-scheduler</b></td>
<td>دسترسی به منابع حجم (volume) موردنیاز مؤلفه kube-scheduler را فراهم می‌کند.</td>
</tr>
<tr>
<td><b>system:kube-controller-manager</b></td>
<td>کاربر <b>system:kube-controller-manager</b></td>
<td>دسترسی به منابع موردنیاز مؤلفه {{< glossary_tooltip term_id="kube-controller-manager" text="controller manager" >}} را فراهم می‌کند.
مجوزهای موردنیاز کنترل‌کننده‌های جداگانه در <a href="#controller-roles">نقش‌های کنترل‌کننده</a> به‌تفصیل آمده است.</td>
</tr>
<tr>
<td><b>system:node</b></td>
<td>ندارد</td>
<td>دسترسی به منابع موردنیاز kubelet را فراهم می‌کند، <b>از جمله دسترسی خواندن به همه secretها و دسترسی نوشتن به همه آبجکت‌های وضعیت pod</b>.

به‌جای نقش <tt>system:node</tt> باید از <a href="/docs/reference/access-authn-authz/node/">Node authorizer</a> و <a href="/docs/reference/access-authn-authz/admission-controllers/#noderestriction">افزونه پذیرش NodeRestriction</a> استفاده کنید و اعطای دسترسی API به kubeletها را بر اساس Podهایی که زمان‌بندی شده‌اند تا روی آن‌ها اجرا شوند، مجاز کنید.

نقش <tt>system:node</tt> فقط برای سازگاری با کلاسترهای کوبرنتیز ارتقایافته از نسخه‌های قبل از v1.8 وجود دارد.
</td>
</tr>
<tr>
<td><b>system:node-proxier</b></td>
<td>کاربر <b>system:kube-proxy</b></td>
<td>دسترسی به منابع موردنیاز مؤلفه {{< glossary_tooltip term_id="kube-proxy" text="kube-proxy" >}} را فراهم می‌کند.</td>
</tr>
</tbody>
</table>

### نقش‌های سایر مؤلفه‌ها

<table>
<colgroup><col style="width: 25%;" /><col style="width: 25%;" /><col /></colgroup>
<thead>
<tr>
<th>ClusterRole پیش‌فرض</th>
<th>ClusterRoleBinding پیش‌فرض</th>
<th>توضیحات</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>system:auth-delegator</b></td>
<td>ندارد</td>
<td>بررسی‌های احراز هویت و مجوزدهی تفویض‌شده را مجاز می‌کند.
این نقش معمولاً توسط API serverهای افزونه برای احراز هویت و مجوزدهی یکپارچه استفاده می‌شود.</td>
</tr>
<tr>
<td><b>system:heapster</b></td>
<td>ندارد</td>
<td>نقش مربوط به مؤلفه <a href="https://github.com/kubernetes/heapster">Heapster</a> (منسوخ‌شده).</td>
</tr>
<tr>
<td><b>system:kube-aggregator</b></td>
<td>ندارد</td>
<td>نقش مربوط به مؤلفه <a href="https://github.com/kubernetes/kube-aggregator">kube-aggregator</a>.</td>
</tr>
<tr>
<td><b>system:kube-dns</b></td>
<td>service account با نام <b>kube-dns</b> در فضای نام <b>kube-system</b></td>
<td>نقش مربوط به مؤلفه منسوخ‌شده kube-dns. (<a href="/docs/concepts/services-networking/dns-pod-service/">CoreDNS</a> از این نقش استفاده نمی‌کند.)</td>
</tr>
<tr>
<td><b>system:kubelet-api-admin</b></td>
<td>ندارد</td>
<td>دسترسی کامل به API مربوط به kubelet را فراهم می‌کند.</td>
</tr>
<tr>
<td><b>system:node-bootstrapper</b></td>
<td>ندارد</td>
<td>دسترسی به منابع موردنیاز برای انجام
<a href="/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/">TLS bootstrapping مربوط به kubelet</a> را فراهم می‌کند.</td>
</tr>
<tr>
<td><b>system:node-problem-detector</b></td>
<td>ندارد</td>
<td>نقش مربوط به مؤلفه <a href="https://github.com/kubernetes/node-problem-detector">node-problem-detector</a>.</td>
</tr>
<tr>
<td><b>system:persistent-volume-provisioner</b></td>
<td>ندارد</td>
<td>دسترسی به منابع موردنیاز بیشتر <a href="/docs/concepts/storage/persistent-volumes/#dynamic">تأمین‌کننده‌های پویای حجم (dynamic volume provisioners)</a> را فراهم می‌کند.</td>
</tr>
<tr>
<td><b>system:monitoring</b></td>
<td>گروه <b>system:monitoring</b></td>
<td>دسترسی خواندن به endpointهای پایش control plane (یعنی endpointهای liveness و readiness مربوط به {{< glossary_tooltip term_id="kube-apiserver" text="kube-apiserver" >}} (<tt>/healthz</tt>، <tt>/livez</tt>، <tt>/readyz</tt>)، endpointهای بررسی سلامت جداگانه (<tt>/healthz/*</tt>، <tt>/livez/*</tt>، <tt>/readyz/*</tt>) و <tt>/metrics</tt>) را فراهم می‌کند و باعث می‌شود kube-apiserver هدر traceparent ارائه‌شده همراه درخواست‌ها را برای ردیابی (tracing) رعایت کند. توجه داشته باشید که endpointهای بررسی سلامت جداگانه و endpoint مربوط به متریک‌ها ممکن است اطلاعات حساس را افشا کنند.</td>
</tr>
</tbody>
</table>

### نقش‌ها برای کنترل‌کننده‌های داخلی {#controller-roles}

{{< glossary_tooltip term_id="kube-controller-manager" text="controller manager" >}} کوبرنتیز
{{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌هایی" >}} را اجرا می‌کند که در control plane
کوبرنتیز تعبیه شده‌اند.
هنگامی که با `--use-service-account-credentials` فراخوانی شود، kube-controller-manager هر کنترل‌کننده را
با یک service account جداگانه راه‌اندازی می‌کند.
برای هر کنترل‌کننده داخلی نقش متناظری با پیشوند `system:controller:` وجود دارد.
اگر controller manager با `--use-service-account-credentials` راه‌اندازی نشود، تمام حلقه‌های کنترل را
با اعتبارنامه خودش اجرا می‌کند و باید همه نقش‌های مرتبط به آن اعطا شده باشد.
این نقش‌ها عبارت‌اند از:

* `system:controller:attachdetach-controller`
* `system:controller:certificate-controller`
* `system:controller:clusterrole-aggregation-controller`
* `system:controller:cronjob-controller`
* `system:controller:daemon-set-controller`
* `system:controller:deployment-controller`
* `system:controller:disruption-controller`
* `system:controller:endpoint-controller`
* `system:controller:expand-controller`
* `system:controller:generic-garbage-collector`
* `system:controller:horizontal-pod-autoscaler`
* `system:controller:job-controller`
* `system:controller:namespace-controller`
* `system:controller:node-controller`
* `system:controller:persistent-volume-binder`
* `system:controller:pod-garbage-collector`
* `system:controller:pv-protection-controller`
* `system:controller:pvc-protection-controller`
* `system:controller:replicaset-controller`
* `system:controller:replication-controller`
* `system:controller:resourcequota-controller`
* `system:controller:root-ca-cert-publisher`
* `system:controller:route-controller`
* `system:controller:service-account-controller`
* `system:controller:service-controller`
* `system:controller:statefulset-controller`
* `system:controller:ttl-controller`

## پیشگیری از ارتقای سطح دسترسی و bootstrapping

RBAC API با ویرایش نقش‌ها یا اتصال‌های نقش، از ارتقای سطح دسترسی توسط کاربران جلوگیری می‌کند.
از آنجا که این محدودیت در سطح API اعمال می‌شود، حتی زمانی که RBAC authorizer استفاده نمی‌شود نیز برقرار است.

### محدودیت‌ها در ایجاد یا به‌روزرسانی نقش

شما فقط در صورتی می‌توانید یک نقش را ایجاد یا به‌روزرسانی کنید که دست‌کم یکی از شرایط زیر برقرار باشد:

1. شما از پیش همه مجوزهای موجود در نقش را در همان حوزه‌ای که آبجکت در حال تغییر قرار دارد در اختیار داشته باشید
   (برای ClusterRole در سطح کل کلاستر، برای Role در همان فضای نام یا در سطح کل کلاستر).
2. مجوز صریح برای انجام فعل `escalate` روی منبع `roles` یا
   `clusterroles` در گروه API با نام `rbac.authorization.k8s.io` به شما اعطا شده باشد.

برای مثال، اگر `user-1` توانایی فهرست‌کردن Secretها را در سطح کل کلاستر نداشته باشد، نمی‌تواند ClusterRole‌ای
شامل آن مجوز ایجاد کند. برای اینکه به کاربری اجازه دهید نقش‌ها را ایجاد/به‌روزرسانی کند:

1. نقشی به او اعطا کنید که به او اجازه می‌دهد آبجکت‌های Role یا ClusterRole را در صورت نیاز ایجاد/به‌روزرسانی کند.
2. به او مجوز دهید که مجوزهای مشخصی را در نقش‌هایی که ایجاد/به‌روزرسانی می‌کند بگنجاند:
   * به‌صورت ضمنی، با اعطای همان مجوزها به او (اگر او تلاش کند Role یا
     ClusterRole‌ای با مجوزهایی ایجاد یا تغییر دهد که خودش به آن‌ها دسترسی ندارد، درخواست API ممنوع خواهد شد)
   * یا با اعطای مجوز انجام فعل `escalate` روی منابع `roles` یا `clusterroles` در گروه API
     با نام `rbac.authorization.k8s.io`، به‌صورت صریح اجازه دهید هر مجوزی در یک `Role` یا `ClusterRole` مشخص شود

### محدودیت‌ها در ایجاد یا به‌روزرسانی role binding

شما فقط در صورتی می‌توانید یک role binding را ایجاد یا به‌روزرسانی کنید که همه مجوزهای موجود در نقش ارجاع‌شده را (در همان محدوده‌ای که role binding دارد) از قبل داشته باشید، *یا* مجاز شده باشید که فعل `bind` را روی نقش ارجاع‌شده اجرا کنید.
برای مثال، اگر `user-1` توانایی فهرست‌کردن Secretها را در سطح کل کلاستر نداشته باشد، نمی‌تواند یک ClusterRoleBinding به نقشی ایجاد کند که این مجوز را اعطا می‌کند. برای آنکه به یک کاربر اجازه دهید role bindingها را ایجاد یا به‌روزرسانی کند:

1. نقشی به او اعطا کنید که امکان ایجاد یا به‌روزرسانی آبجکت‌های RoleBinding یا ClusterRoleBinding را، بسته به نیاز، فراهم کند.
2. مجوزهای لازم برای bind کردن یک نقش مشخص را به او اعطا کنید:
   * به‌صورت ضمنی، با دادن مجوزهای موجود در آن نقش به او.
   * به‌صورت صریح، با دادن مجوز اجرای فعل `bind` روی Role (یا ClusterRole) مورد نظر.

برای مثال، این ClusterRole و RoleBinding به `user-1` اجازه می‌دهند نقش‌های `admin`، `edit` و `view` را در فضای نام (namespace) با نام `user-1-namespace` به کاربران دیگر اعطا کند:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: role-grantor
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["rolebindings"]
  verbs: ["create"]
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterroles"]
  verbs: ["bind"]
  # omit resourceNames to allow binding any ClusterRole
  resourceNames: ["admin","edit","view"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: role-grantor-binding
  namespace: user-1-namespace
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: role-grantor
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: user-1
```

هنگام راه‌اندازی اولیه (bootstrap) نخستین نقش‌ها و role bindingها، لازم است کاربر اولیه مجوزهایی را اعطا کند که خودش هنوز در اختیار ندارد.
برای راه‌اندازی اولیه نقش‌ها و role bindingها:

* از یک اعتبارنامه (credential) با گروه "system:masters" استفاده کنید؛ این گروه توسط bindingهای پیش‌فرض به نقش مدیر کل "cluster-admin" متصل شده است.

## ابزارهای خط فرمان {#command-line-utilities}

### `kubectl create role`

یک آبجکت Role ایجاد می‌کند که مجوزها را در یک فضای نام (namespace) واحد تعریف می‌کند. مثال‌ها:

* ایجاد یک Role با نام "pod-reader" که به کاربران اجازه می‌دهد روی podها `get`، `watch` و `list` انجام دهند:

  ```shell
  kubectl create role pod-reader --verb=get --verb=list --verb=watch --resource=pods
  ```

* ایجاد یک Role با نام "pod-reader" همراه با تعیین resourceNames:

  ```shell
  kubectl create role pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod
  ```

* ایجاد یک Role با نام "foo" همراه با تعیین apiGroups:

  ```shell
  kubectl create role foo --verb=get,list,watch --resource=replicasets.apps
  ```

* ایجاد یک Role با نام "foo" همراه با مجوزهای زیرمنبع (subresource):

  ```shell
  kubectl create role foo --verb=get,list,watch --resource=pods,pods/status
  ```

* ایجاد یک Role با نام "my-component-lease-holder" با مجوز get/update روی یک منبع با نام مشخص:

  ```shell
  kubectl create role my-component-lease-holder --verb=get,list,watch,update --resource=lease --resource-name=my-component
  ```

### `kubectl create clusterrole`

یک ClusterRole ایجاد می‌کند. مثال‌ها:

* ایجاد یک ClusterRole با نام "pod-reader" که به کاربر اجازه می‌دهد روی podها `get`، `watch` و `list` انجام دهد:

  ```shell
  kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
  ```

* ایجاد یک ClusterRole با نام "pod-reader" همراه با تعیین resourceNames:

  ```shell
  kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با تعیین apiGroups:

  ```shell
  kubectl create clusterrole foo --verb=get,list,watch --resource=replicasets.apps
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با مجوزهای زیرمنبع (subresource):

  ```shell
  kubectl create clusterrole foo --verb=get,list,watch --resource=pods,pods/status
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با تعیین nonResourceURL:

  ```shell
  kubectl create clusterrole "foo" --verb=get --non-resource-url=/logs/*
  ```

* ایجاد یک ClusterRole با نام "monitoring" همراه با تعیین aggregationRule:

  ```shell
  kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
  ```

### `kubectl create rolebinding`

یک Role یا ClusterRole را در یک فضای نام (namespace) مشخص اعطا می‌کند. مثال‌ها:

* در فضای نام "acme"، مجوزهای موجود در ClusterRole با نام "admin" را به کاربری با نام "bob" اعطا کنید:

  ```shell
  kubectl create rolebinding bob-admin-binding --clusterrole=admin --user=bob --namespace=acme
  ```

* در فضای نام "acme"، مجوزهای موجود در ClusterRole با نام "view" را به service account با نام "myapp" در فضای نام "acme" اعطا کنید:

  ```shell
  kubectl create rolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp --namespace=acme
  ```

* در فضای نام "acme"، مجوزهای موجود در ClusterRole با نام "view" را به service account با نام "myapp" در فضای نام "myappnamespace" اعطا کنید:

  ```shell
  kubectl create rolebinding myappnamespace-myapp-view-binding --clusterrole=view --serviceaccount=myappnamespace:myapp --namespace=acme
  ```

### `kubectl create clusterrolebinding`

یک ClusterRole را در سراسر کلاستر (همه فضاهای نام) اعطا می‌کند. مثال‌ها:

* در سراسر کلاستر، مجوزهای موجود در ClusterRole با نام "cluster-admin" را به کاربری با نام "root" اعطا کنید:

  ```shell
  kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root
  ```

* در سراسر کلاستر، مجوزهای موجود در ClusterRole با نام "system:node-proxier" را به کاربری با نام "system:kube-proxy" اعطا کنید:

  ```shell
  kubectl create clusterrolebinding kube-proxy-binding --clusterrole=system:node-proxier --user=system:kube-proxy
  ```

* در سراسر کلاستر، مجوزهای موجود در ClusterRole با نام "view" را به service account با نام "myapp" در فضای نام "acme" اعطا کنید:

  ```shell
  kubectl create clusterrolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp
  ```

### `kubectl auth reconcile` {#kubectl-auth-reconcile}

آبجکت‌های API از نوع `rbac.authorization.k8s.io/v1` را از روی یک فایل مانیفست ایجاد یا به‌روزرسانی می‌کند.

آبجکت‌های ناموجود ایجاد می‌شوند و در صورت لزوم، فضای نام حاوی آن‌ها نیز برای آبجکت‌های دارای فضای نام ایجاد می‌شود.

نقش‌های موجود به‌روزرسانی می‌شوند تا مجوزهای موجود در آبجکت‌های ورودی را شامل شوند،
و در صورتی که `--remove-extra-permissions` مشخص شده باشد، مجوزهای اضافی حذف می‌شوند.

bindingهای موجود به‌روزرسانی می‌شوند تا subjectهای موجود در آبجکت‌های ورودی را شامل شوند،
و در صورتی که `--remove-extra-subjects` مشخص شده باشد، subjectهای اضافی حذف می‌شوند.

مثال‌ها:

* آزمایش اعمال یک فایل مانیفست از آبجکت‌های RBAC و نمایش تغییراتی که اعمال خواهند شد:

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml --dry-run=client
  ```

* اعمال یک فایل مانیفست از آبجکت‌های RBAC با حفظ هرگونه مجوز اضافی (در نقش‌ها) و هر subject اضافی (در bindingها):

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml
  ```

* اعمال یک فایل مانیفست از آبجکت‌های RBAC با حذف هرگونه مجوز اضافی (در نقش‌ها) و هر subject اضافی (در bindingها):

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml --remove-extra-subjects --remove-extra-permissions
  ```

## مجوزهای ServiceAccount {#service-account-permissions}

سیاست‌های پیش‌فرض RBAC مجوزهای محدودشده‌ای را به مؤلفه‌های control plane، نودها
و کنترل‌کننده‌ها اعطا می‌کنند، اما به service accountهای خارج از فضای نام `kube-system` *هیچ مجوزی* اعطا نمی‌کنند
(فراتر از مجوزهایی که توسط [نقش‌های کشف API](#discovery-roles) داده می‌شود).

این امر به شما امکان می‌دهد در صورت نیاز، نقش‌های مشخصی را به ServiceAccountهای مشخصی اعطا کنید.
role bindingهای دقیق‌تر امنیت بیشتری فراهم می‌کنند، اما مدیریت آن‌ها به تلاش بیشتری نیاز دارد.
اعطای مجوزهای گسترده‌تر می‌تواند دسترسی غیرضروری (و بالقوه افزایش‌دهنده سطح دسترسی) به API را برای
ServiceAccountها فراهم کند، اما مدیریت آن‌ها آسان‌تر است.

رویکردها، از امن‌ترین به کم‌امن‌ترین، به این ترتیب هستند:

1. اعطای یک نقش به service account اختصاصی هر برنامه (بهترین روش)

   این رویکرد مستلزم آن است که برنامه در مشخصات pod خود یک `serviceAccountName` تعیین کند
   و service account ایجاد شده باشد (از طریق API، مانیفست برنامه، `kubectl create serviceaccount` و غیره).

   برای مثال، مجوز فقط‌خواندنی را در فضای نام "my-namespace" به service account با نام "my-sa" اعطا کنید:

   ```shell
   kubectl create rolebinding my-sa-view \
     --clusterrole=view \
     --serviceaccount=my-namespace:my-sa \
     --namespace=my-namespace
   ```

2. اعطای یک نقش به service account با نام "default" در یک فضای نام

   اگر برنامه‌ای `serviceAccountName` را تعیین نکند، از service account با نام "default" استفاده می‌کند.

   {{< note >}}
   مجوزهایی که به service account با نام "default" داده می‌شوند، در دسترس هر podی در آن فضای نام
   قرار می‌گیرند که `serviceAccountName` را تعیین نکرده باشد.
   {{< /note >}}

   برای مثال، مجوز فقط‌خواندنی را در فضای نام "my-namespace" به service account با نام "default" اعطا کنید:

   ```shell
   kubectl create rolebinding default-view \
     --clusterrole=view \
     --serviceaccount=my-namespace:default \
     --namespace=my-namespace
   ```

3. اعطای یک نقش به همه service accountها در یک فضای نام

   اگر می‌خواهید همه برنامه‌های یک فضای نام، صرف‌نظر از اینکه از کدام service account استفاده می‌کنند، یک نقش داشته باشند،
   می‌توانید نقش را به گروه service accountهای آن فضای نام اعطا کنید.

   برای مثال، مجوز فقط‌خواندنی را در فضای نام "my-namespace" به همه service accountهای آن فضای نام اعطا کنید:

   ```shell
   kubectl create rolebinding serviceaccounts-view \
     --clusterrole=view \
     --group=system:serviceaccounts:my-namespace \
     --namespace=my-namespace
   ```

4. اعطای یک نقش محدود به همه service accountها در سطح کل کلاستر (توصیه نمی‌شود)

   اگر نمی‌خواهید مجوزها را به‌ازای هر فضای نام مدیریت کنید، می‌توانید یک نقش در سطح کلاستر را به همه service accountها اعطا کنید.

   برای مثال، مجوز فقط‌خواندنی را در همه فضاهای نام به همه service accountهای کلاستر اعطا کنید:

   ```shell
   kubectl create clusterrolebinding serviceaccounts-view \
     --clusterrole=view \
    --group=system:serviceaccounts
   ```

5. اعطای دسترسی مدیر کل (super-user) به همه service accountها در سطح کل کلاستر (به‌شدت توصیه نمی‌شود)

   اگر اصلاً به تفکیک مجوزها اهمیت نمی‌دهید، می‌توانید دسترسی مدیر کل را به همه service accountها اعطا کنید.

   {{< warning >}}
   این کار به هر برنامه‌ای دسترسی کامل به کلاستر شما می‌دهد و همچنین به هر کاربری که دسترسی خواندن به Secretها
   (یا توانایی ایجاد هر pod) داشته باشد، دسترسی کامل به کلاستر شما اعطا می‌کند.
   {{< /warning >}}

   ```shell
   kubectl create clusterrolebinding serviceaccounts-cluster-admin \
     --clusterrole=cluster-admin \
     --group=system:serviceaccounts
   ```

## دسترسی نوشتن برای EndpointSlices {#write-access-for-endpoints}

کلاسترهای کوبرنتیز که پیش از نسخه v1.22 کوبرنتیز ایجاد شده‌اند، شامل دسترسی نوشتن به
EndpointSlices (و API منسوخ‌شده Endpoints) در نقش‌های تجمیعی (aggregated) "edit" و "admin" هستند.
به‌عنوان راهکاری برای کاهش مخاطرات [CVE-2021-25740](https://github.com/kubernetes/kubernetes/issues/103675)،
این دسترسی در کلاسترهایی که با کوبرنتیز v1.22 یا بالاتر ایجاد می‌کنید، بخشی از نقش‌های تجمیعی نیست.

کلاسترهای موجودی که به کوبرنتیز v1.22 ارتقا یافته‌اند
مشمول این تغییر نخواهند بود. [اطلاعیه
CVE](https://github.com/kubernetes/kubernetes/issues/103675) شامل
راهنمایی برای محدودکردن این دسترسی در کلاسترهای موجود است.

اگر می‌خواهید کلاسترهای جدید این سطح از دسترسی را در نقش‌های تجمیعی حفظ کنند،
می‌توانید ClusterRole زیر را ایجاد کنید:

{{% code_sample file="access/endpoints-aggregated.yaml" %}}

## ارتقا از ABAC {#upgrading-from-abac}

کلاسترهایی که در ابتدا نسخه‌های قدیمی‌تر کوبرنتیز را اجرا می‌کردند، اغلب از
سیاست‌های ABAC سهل‌گیرانه استفاده می‌کردند، از جمله اعطای دسترسی کامل به API برای همه
service accountها.

سیاست‌های پیش‌فرض RBAC مجوزهای محدودشده‌ای را به مؤلفه‌های control plane، نودها
و کنترل‌کننده‌ها اعطا می‌کنند، اما به service accountهای خارج از فضای نام `kube-system` *هیچ مجوزی* اعطا نمی‌کنند
(فراتر از مجوزهایی که توسط [نقش‌های کشف API](#discovery-roles) داده می‌شود).

اگرچه این رویکرد بسیار امن‌تر است، می‌تواند برای بارهای کاری موجودی که انتظار دارند مجوزهای API را به‌صورت خودکار دریافت کنند، اختلال ایجاد کند.
در اینجا دو رویکرد برای مدیریت این گذار آورده شده است:

### مجوزدهنده‌های موازی {#parallel-authorizers}

هر دو مجوزدهنده RBAC و ABAC را اجرا کنید و فایل سیاستی مشخص کنید که شامل
[سیاست قدیمی ABAC](/docs/reference/access-authn-authz/abac/#policy-file-format) باشد:

```shell
--authorization-mode=...,RBAC,ABAC --authorization-policy-file=mypolicy.json
```

برای توضیح دقیق‌تر گزینه خط فرمان نخست: اگر مجوزدهنده‌های قبلی، مانند Node،
درخواستی را رد کنند، مجوزدهنده RBAC تلاش می‌کند درخواست API را مجاز کند. اگر RBAC
نیز آن درخواست API را رد کند، سپس مجوزدهنده ABAC اجرا می‌شود. این بدان معناست که هر درخواستی
که توسط سیاست‌های RBAC *یا* ABAC مجاز شده باشد، پذیرفته می‌شود.

هنگامی که kube-apiserver با سطح لاگ 5 یا بالاتر برای مؤلفه RBAC اجرا شود
(`--vmodule=rbac*=5` یا `--v=5`)، می‌توانید ردهای RBAC را در لاگ API server مشاهده کنید
(با پیشوند `RBAC`).
می‌توانید از این اطلاعات برای تعیین اینکه کدام نقش‌ها باید به کدام کاربران، گروه‌ها یا service accountها اعطا شوند، استفاده کنید.

پس از آنکه [نقش‌ها را به service accountها اعطا کردید](#service-account-permissions) و بارهای کاری
بدون هیچ پیام رد RBAC در لاگ‌های سرور در حال اجرا هستند، می‌توانید مجوزدهنده ABAC را حذف کنید.

### مجوزهای سهل‌گیرانه RBAC {#permissive-rbac-permissions}

می‌توانید یک سیاست سهل‌گیرانه ABAC را با استفاده از role bindingهای RBAC بازسازی کنید.

{{< warning >}}
سیاست زیر به **همه** service accountها اجازه می‌دهد به‌عنوان مدیر کلاستر عمل کنند.
هر برنامه‌ای که در یک کانتینر اجرا می‌شود، اعتبارنامه‌های service account را به‌صورت خودکار دریافت می‌کند
و می‌تواند هر عملی را روی API انجام دهد، از جمله مشاهده secretها و تغییر مجوزها.
این سیاست توصیه نمی‌شود.

```shell
kubectl create clusterrolebinding permissive-binding \
  --clusterrole=cluster-admin \
  --user=admin \
  --user=kubelet \
  --group=system:serviceaccounts
```
{{< /warning >}}

پس از آنکه به استفاده از RBAC گذار کردید، باید کنترل‌های دسترسی
کلاستر خود را تنظیم کنید تا اطمینان یابید که این کنترل‌ها نیازهای امنیت اطلاعات شما را برآورده می‌کنند.

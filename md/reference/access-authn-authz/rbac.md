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
کنترل دسترسی مبتنی بر نقش (Role-based access control یا RBAC) روشی برای تنظیم دسترسی به منابع رایانه‌ای یا شبکه‌ای بر اساس نقش هر یک از کاربران در سازمان شماست.


<!-- body -->
مجوزدهی RBAC برای اتخاذ تصمیم‌های مجوزدهی از {{< glossary_tooltip text="گروه API" term_id="api-group" >}} با نام `rbac.authorization.k8s.io` استفاده می‌کند. به این ترتیب می‌توانید سیاست‌ها را به‌صورت پویا و از طریق API کوبرنتیز پیکربندی کنید.

برای فعال‌سازی RBAC، {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} را با فلگ `--authorization-config` اجرا کنید و مقدار آن را فایلی قرار دهید که مجوزدهنده‌ی `RBAC` را در بر دارد؛ برای مثال:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AuthorizationConfiguration
authorizers:
  ...
  - type: RBAC
  ...
```

یا اینکه {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}} را با فلگ `--authorization-mode` اجرا کنید و مقدار آن را فهرستی جداشده با ویرگول قرار دهید که `RBAC` را شامل شود؛ برای مثال:
```shell
kube-apiserver --authorization-mode=...,RBAC --other-options --more-options
```

## آبجکت‌های API {#api-overview}

در API مربوط به RBAC چهار نوع آبجکت کوبرنتیز تعریف شده است: _Role_، _ClusterRole_، _RoleBinding_ و _ClusterRoleBinding_. می‌توانید {{< glossary_tooltip text="آبجکت‌های" term_id="object" >}} RBAC را نیز مانند هر آبجکت دیگر کوبرنتیز با ابزارهایی مانند `kubectl` توصیف یا اصلاح کنید.

{{< caution >}}
این آبجکت‌ها بنا بر طراحی، محدودیت‌های دسترسی اعمال می‌کنند. اگر در حین یادگیری در یک کلاستر تغییراتی ایجاد می‌کنید، بخش [جلوگیری از ارتقای سطح دسترسی و راه‌اندازی اولیه](#privilege-escalation-prevention-and-bootstrapping) را ببینید تا متوجه شوید این محدودیت‌ها چگونه ممکن است مانع برخی از تغییرات شما شوند.
{{< /caution >}}

### Role و ClusterRole

هر _Role_ یا _ClusterRole_ در RBAC شامل قوانینی است که مجموعه‌ای از مجوزها را بیان می‌کنند. مجوزها صرفاً افزایشی هستند (هیچ قانون «رد» وجود ندارد).

یک Role همیشه مجوزها را درون یک {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} مشخص تعیین می‌کند؛ هنگام ایجاد یک Role باید فضای نامی را که به آن تعلق دارد مشخص کنید.

در مقابل، ClusterRole منبعی است که به هیچ فضای نامی تعلق ندارد. علت متفاوت بودن نام این دو منبع (Role و ClusterRole) این است که هر آبجکت کوبرنتیز همیشه یا باید به یک فضای نام تعلق داشته باشد یا نداشته باشد؛ هر دو حالت هم‌زمان ممکن نیست.

کاربردهای ClusterRole متعدد است. از یک ClusterRole می‌توانید برای موارد زیر استفاده کنید:

1. تعریف مجوزها روی منابع وابسته به فضای نام و اعطای دسترسی درون یک یا چند فضای نام مشخص
1. تعریف مجوزها روی منابع وابسته به فضای نام و اعطای دسترسی در همه‌ی فضاهای نام
1. تعریف مجوزها روی منابع در سطح کلاستر

اگر می‌خواهید نقشی را درون یک فضای نام تعریف کنید، از Role استفاده کنید؛ و اگر می‌خواهید نقشی را در سطح کل کلاستر تعریف کنید، از ClusterRole استفاده کنید.

#### نمونه‌ای از Role

در اینجا نمونه‌ای از یک Role در فضای نام «default» آمده است که می‌توان از آن برای اعطای دسترسی خواندن به {{< glossary_tooltip text="پادها" term_id="pod" >}} استفاده کرد:

{{% code_sample file="access/simple-role.yaml" %}}

#### نمونه‌ای از ClusterRole

با یک ClusterRole می‌توان همان مجوزهای یک Role را اعطا کرد. از آنجا که ClusterRoleها در سطح کلاستر تعریف می‌شوند، می‌توانید از آن‌ها برای اعطای دسترسی به موارد زیر نیز استفاده کنید:

* منابع در سطح کلاستر (مانند {{< glossary_tooltip text="نودها" term_id="node" >}})
* نقاط پایانی غیرمنبعی (مانند `/healthz`)
* منابع وابسته به فضای نام (مانند Podها) در همه‌ی فضاهای نام

  برای مثال، می‌توانید با یک ClusterRole به کاربری مشخص اجازه دهید دستور `kubectl get pods --all-namespaces` را اجرا کند.

در اینجا نمونه‌ای از یک ClusterRole آمده است که می‌توان از آن برای اعطای دسترسی خواندن به {{< glossary_tooltip text="سکرت‌ها" term_id="secret" >}} در یک فضای نام مشخص یا در همه‌ی فضاهای نام استفاده کرد (بسته به اینکه چگونه [متصل](#rolebinding-and-clusterrolebinding) شود):

{{% code_sample file="access/simple-clusterrole.yaml" %}}

نام هر آبجکت Role یا ClusterRole باید یک [نام بخش مسیر](/docs/concepts/overview/working-with-objects/names#path-segment-names) معتبر باشد.

### RoleBinding و ClusterRoleBinding

اتصال نقش (role binding) مجوزهای تعریف‌شده در یک نقش را به یک کاربر یا مجموعه‌ای از کاربران اعطا می‌کند. هر اتصال نقش فهرستی از *سوژه‌ها* (کاربران، گروه‌ها یا حساب‌های سرویس) و ارجاعی به نقشِ اعطاشده را در خود نگه می‌دارد. یک RoleBinding مجوزها را درون یک فضای نام مشخص اعطا می‌کند، در حالی که یک ClusterRoleBinding همان دسترسی را در سطح کل کلاستر اعطا می‌کند.

یک RoleBinding می‌تواند به هر Role در همان فضای نام ارجاع دهد. همچنین یک RoleBinding می‌تواند به یک ClusterRole ارجاع دهد و آن ClusterRole را به فضای نام خودِ RoleBinding متصل کند. اگر می‌خواهید یک ClusterRole را به همه‌ی فضاهای نام کلاستر خود متصل کنید، از ClusterRoleBinding استفاده کنید.

نام هر آبجکت RoleBinding یا ClusterRoleBinding باید یک [نام بخش مسیر](/docs/concepts/overview/working-with-objects/names#path-segment-names) معتبر باشد.

#### نمونه‌هایی از RoleBinding {#rolebinding-example}

در اینجا نمونه‌ای از یک RoleBinding آمده است که Role با نام «pod-reader» را درون فضای نام «default» به کاربر «jane» اعطا می‌کند. با این کار، «jane» می‌تواند پادهای فضای نام «default» را بخواند.

{{% code_sample file="access/simple-rolebinding-with-role.yaml" %}}

یک RoleBinding می‌تواند به یک ClusterRole نیز ارجاع دهد تا مجوزهای تعریف‌شده در آن ClusterRole را برای منابع درون فضای نام خودِ RoleBinding اعطا کند. با این نوع ارجاع می‌توانید مجموعه‌ای از نقش‌های مشترک را در سطح کلاستر تعریف کنید و سپس آن‌ها را در چندین فضای نام دوباره به کار ببرید.

برای نمونه، با اینکه RoleBinding زیر به یک ClusterRole ارجاع می‌دهد، «dave» (سوژه، با حساسیت به بزرگی و کوچکی حروف) فقط می‌تواند Secretهای فضای نام «development» را بخواند؛ زیرا فضای نام این RoleBinding (در فراداده‌ی آن) «development» است.

{{% code_sample file="access/simple-rolebinding-with-clusterrole.yaml" %}}

#### نمونه‌ای از ClusterRoleBinding

برای اعطای مجوز در سطح کل کلاستر می‌توانید از ClusterRoleBinding استفاده کنید. ClusterRoleBinding زیر به هر کاربری در گروه «manager» اجازه می‌دهد سکرت‌ها را در هر فضای نامی بخواند.

{{% code_sample file="access/simple-clusterrolebinding.yaml" %}}

پس از ایجاد یک اتصال، دیگر نمی‌توانید Role یا ClusterRole‌ای را که به آن ارجاع می‌دهد تغییر دهید. اگر بخواهید فیلد `roleRef` یک اتصال را تغییر دهید، با خطای اعتبارسنجی روبه‌رو می‌شوید. اگر واقعاً لازم است `roleRef` یک اتصال را تغییر دهید، باید آبجکت اتصال را حذف کنید و آبجکت جایگزینی بسازید.

این محدودیت دو دلیل دارد:

1. تغییرناپذیر بودن `roleRef` امکان می‌دهد مجوز `update` روی یک آبجکت اتصال موجود را به کسی اعطا کنید تا بتواند فهرست سوژه‌ها را مدیریت کند، بی‌آنکه بتواند نقشِ اعطاشده به آن سوژه‌ها را تغییر دهد.
1. اتصال به نقشی متفاوت، اساساً اتصالی متفاوت است. الزام به حذف و ایجاد دوباره‌ی اتصال برای تغییر `roleRef` تضمین می‌کند که قصد واقعی، اعطای نقش جدید به کل فهرست سوژه‌های آن اتصال است (نه اینکه فقط roleRef فعال یا به‌طور تصادفی تغییر داده شود، بی‌آنکه بررسی شود همه‌ی سوژه‌های موجود باید مجوزهای نقش جدید را دریافت کنند).

ابزار خط فرمان `kubectl auth reconcile` فایل مانیفستی حاوی آبجکت‌های RBAC را ایجاد یا به‌روزرسانی می‌کند و در صورت نیاز، حذف و ایجاد دوباره‌ی آبجکت‌های اتصال را برای تغییر نقشِ ارجاع‌شده انجام می‌دهد. برای اطلاعات بیشتر، [نحوه‌ی استفاده از دستور و نمونه‌ها](#kubectl-auth-reconcile) را ببینید.

### ارجاع به منابع

در API کوبرنتیز، بیشتر منابع با یک نمایش رشته‌ای از نام آبجکتشان نمایش داده می‌شوند و از همین طریق به آن‌ها دسترسی پیدا می‌شود؛ مثلاً `pods` برای Pod. در RBAC برای ارجاع به منابع دقیقاً از همان نامی استفاده می‌شود که در URL نقطه‌ی پایانی API مربوط ظاهر می‌شود. برخی از APIهای کوبرنتیز شامل یک _زیرمنبع_ (subresource) هستند، مانند لاگ‌های یک Pod. درخواست برای لاگ‌های یک Pod به این شکل است:

```http
GET /api/v1/namespaces/{namespace}/pods/{name}/log
```

در این حالت، `pods` منبع وابسته به فضای نام برای منابع Pod است و `log` زیرمنبعی از `pods` است. برای بیان این موضوع در یک نقش RBAC، منبع و زیرمنبع را با یک اسلش (`/`) از هم جدا کنید. برای اینکه به یک سوژه اجازه دهید `pods` را بخواند و به زیرمنبع `log` هر یک از آن Podها نیز دسترسی داشته باشد، چنین می‌نویسید:

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

همچنین می‌توانید برای برخی درخواست‌ها از طریق فهرست `resourceNames` با نام به منابع ارجاع دهید. در این صورت، درخواست‌ها را می‌توان به نمونه‌های مشخصی از یک منبع محدود کرد. در اینجا نمونه‌ای آمده است که سوژه‌ی خود را محدود می‌کند تا فقط بتواند یک {{< glossary_tooltip term_id="ConfigMap" >}} با نام `my-configmap` را `get` یا `update` کند:

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
درخواست‌های **deletecollection** و درخواست‌های **create** در سطح بالا را نمی‌توان بر اساس نام منبع محدود کرد. علت این محدودیت برای **create** آن است که ممکن است نام آبجکت جدید در زمان مجوزدهی مشخص نباشد. با این حال، محدودیت **create** فقط برای منابع سطح بالا اعمال می‌شود و شامل زیرمنابع نیست. برای مثال، می‌توانید فیلد `resourceNames` را همراه با `pods/exec` به کار ببرید.
اگر **list** یا **watch** را با `resourceName` محدود کنید، کلاینت‌ها برای دریافت مجوز باید در درخواست **list** یا **watch** خود یک انتخابگر فیلد (field selector) روی `metadata.name` قرار دهند که با `resourceName` مشخص‌شده مطابقت داشته باشد.
برای مثال: `kubectl get configmaps --field-selector=metadata.name=my-configmap`
{{< /note >}}

به‌جای ارجاع به تک‌تک موارد `resources`، `apiGroups` و `verbs`، می‌توانید از نماد عام `*` برای ارجاع به همه‌ی این موارد استفاده کنید. برای `nonResourceURLs` می‌توانید نماد عام `*` را به‌عنوان پسوندی برای تطبیق الگو (glob) به کار ببرید. برای `resourceNames`، مجموعه‌ی خالی به این معناست که همه چیز مجاز است. در اینجا نمونه‌ای آمده است که اجازه‌ی انجام هر عمل فعلی و آینده را روی همه‌ی منابع فعلی و آینده در گروه API با نام `example.com` می‌دهد. این نقش شبیه نقش داخلی `cluster-admin` است.

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
استفاده از نمادهای عام در ورودی‌های منبع و فعل ممکن است به اعطای دسترسی بیش از حد به منابع حساس منجر شود. برای نمونه، اگر نوع منبع جدید یا زیرمنبع جدیدی اضافه شود، یا فعل سفارشی جدیدی بررسی شود، ورودی دارای نماد عام به‌طور خودکار دسترسی را اعطا می‌کند که ممکن است مطلوب نباشد. باید [اصل حداقل دسترسی](/docs/concepts/security/rbac-good-practices/#least-privilege) را رعایت کرد و با استفاده از منابع و فعل‌های مشخص، اطمینان حاصل کرد که فقط مجوزهای لازم برای عملکرد درست بار کاری اعمال می‌شوند.
{{< /caution >}}

### ClusterRoleهای تجمیعی

می‌توانید چند ClusterRole را در قالب یک ClusterRole ترکیبی _تجمیع_ کنید. کنترل‌کننده‌ای که به‌عنوان بخشی از control plane کلاستر اجرا می‌شود، آبجکت‌های ClusterRole‌ای را که فیلد `aggregationRule` در آن‌ها تنظیم شده است زیر نظر می‌گیرد. فیلد `aggregationRule` یک {{< glossary_tooltip text="انتخابگر" term_id="selector" >}} برچسب تعریف می‌کند که کنترل‌کننده با آن، آبجکت‌های ClusterRole دیگری را که باید در فیلد `rules` این آبجکت ترکیب شوند پیدا می‌کند.

{{< caution >}}
control plane هر مقداری را که به‌صورت دستی در فیلد `rules` یک ClusterRole تجمیعی مشخص کنید بازنویسی می‌کند. اگر می‌خواهید قوانینی را تغییر دهید یا اضافه کنید، این کار را در آبجکت‌های `ClusterRole`‌ای انجام دهید که `aggregationRule` آن‌ها را انتخاب می‌کند.

فیلد `rules` را در مانیفست‌های ClusterRoleهای تجمیعی قرار ندهید. تنظیم این فیلد، حتی با یک فهرست خالی، هنگام اعمال مانیفست با [اعمال سمت سرور](/docs/reference/using-api/server-side-apply/) مالکیت آن فیلد را ادعا می‌کند. این مالکیت میان اعمال‌کننده و control plane تعارض ایجاد می‌کند: اعمال‌های بعدی یا با تعارض مدیر فیلد روی `.rules` شکست می‌خورند، یا (اگر تعارض‌ها به‌اجبار نادیده گرفته شوند، همان‌طور که کنترل‌کننده‌های GitOps معمولاً چنین می‌کنند) قوانین تجمیع‌شده را مکرراً پاک می‌کنند و control plane دوباره آن‌ها را پر می‌کند.
{{< /caution >}}

در اینجا نمونه‌ای از یک ClusterRole تجمیعی آمده است:

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

اگر ClusterRole جدیدی ایجاد کنید که با انتخابگر برچسب یک ClusterRole تجمیعی موجود مطابقت داشته باشد، این تغییر باعث می‌شود قوانین جدید به ClusterRole تجمیعی اضافه شوند. در اینجا نمونه‌ای آمده است که با ایجاد ClusterRole دیگری با برچسب `rbac.example.com/aggregate-to-monitoring: true`، قوانینی را به ClusterRole با نام «monitoring» اضافه می‌کند.

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

[نقش‌های پیش‌فرضِ مخصوص کاربران](#default-roles-and-role-bindings) از تجمیع ClusterRole استفاده می‌کنند. به این ترتیب شما به‌عنوان مدیر کلاستر می‌توانید قوانین مربوط به منابع سفارشی، مانند منابعی که {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitionها" >}} یا سرورهای API تجمیعی ارائه می‌کنند، را برای گسترش نقش‌های پیش‌فرض اضافه کنید.

برای مثال، ClusterRoleهای زیر به نقش‌های پیش‌فرض «admin» و «edit» اجازه می‌دهند منبع سفارشی‌ای با نام CronTab را مدیریت کنند، در حالی که نقش «view» فقط می‌تواند عملیات خواندن را روی منابع CronTab انجام دهد. می‌توانید فرض کنید که آبجکت‌های CronTab در URLهایی که سرور API می‌بیند با نام `"crontabs"` شناخته می‌شوند.

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

#### نمونه‌هایی از Role

نمونه‌های زیر بخش‌هایی از آبجکت‌های Role یا ClusterRole هستند و فقط قسمت `rules` را نشان می‌دهند.

اجازه‌ی خواندن منابع `"pods"` در {{< glossary_tooltip text="گروه API" term_id="api-group" >}} هسته:

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing Pod
  # objects is "pods"
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

اجازه‌ی خواندن و نوشتن Deploymentها (در سطح HTTP: آبجکت‌هایی که بخش منبع URL آن‌ها `"deployments"` است) در گروه API با نام `"apps"`:

```yaml
rules:
- apiGroups: ["apps"]
  #
  # at the HTTP level, the name of the resource for accessing Deployment
  # objects is "deployments"
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

اجازه‌ی خواندن Podها در گروه API هسته، و همچنین خواندن یا نوشتن منابع Job در گروه API با نام `"batch"`:

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

اجازه‌ی خواندن یک ConfigMap با نام «my-config» (برای محدود شدن به یک ConfigMap در یک فضای نام، باید با یک RoleBinding متصل شود):

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

اجازه‌ی خواندن منبع `"nodes"` در گروه هسته (از آنجا که Node در سطح کلاستر تعریف می‌شود، این قانون فقط در صورتی مؤثر است که در یک ClusterRole قرار گیرد و با یک ClusterRoleBinding متصل شود):

```yaml
rules:
- apiGroups: [""]
  #
  # at the HTTP level, the name of the resource for accessing Node
  # objects is "nodes"
  resources: ["nodes"]
  verbs: ["get", "list", "watch"]
```

اجازه‌ی ارسال درخواست‌های GET و POST به نقطه‌ی پایانی غیرمنبعی `/healthz` و همه‌ی زیرمسیرهای آن (این قانون فقط در صورتی مؤثر است که در یک ClusterRole قرار گیرد و با یک ClusterRoleBinding متصل شود):

```yaml
rules:
- nonResourceURLs: ["/healthz", "/healthz/*"] # '*' in a nonResourceURL is a suffix glob match
  verbs: ["get", "post"]
```

### ارجاع به سوژه‌ها

هر RoleBinding یا ClusterRoleBinding یک نقش را به سوژه‌ها (subjects) متصل می‌کند.
سوژه‌ها می‌توانند گروه‌ها، کاربران یا
{{< glossary_tooltip text="ServiceAccountها" term_id="service-account" >}} باشند.

کوبرنتیز نام‌های کاربری را به‌صورت رشته نمایش می‌دهد. این نام‌ها می‌توانند نام‌های ساده‌ای مانند "alice"، نام‌هایی به سبک ایمیل مانند "bob@example.com" یا شناسه‌های عددی کاربر باشند که به‌صورت رشته نمایش داده می‌شوند. پیکربندی [ماژول‌های احراز هویت](/docs/reference/access-authn-authz/authentication/) بر عهدهٔ شما به‌عنوان مدیر کلاستر است، به‌گونه‌ای که فرایند احراز هویت نام‌های کاربری را در قالب دلخواه شما تولید کند.

{{< caution >}}
پیشوند `system:` برای استفادهٔ سیستمی کوبرنتیز رزرو شده است. بنابراین باید مطمئن شوید که به‌طور تصادفی کاربر یا گروهی ندارید که نامش با `system:` شروع شود.
سیستم مجوزدهی RBAC به‌جز این پیشوند خاص، هیچ قالب مشخصی را برای نام‌های کاربری الزامی نمی‌کند.
{{< /caution >}}

در کوبرنتیز، ماژول‌های احراز هویت (Authenticator) اطلاعات گروه را فراهم می‌کنند.
گروه‌ها نیز مانند کاربران به‌صورت رشته نمایش داده می‌شوند و این رشته هیچ الزام قالبی ندارد، جز اینکه پیشوند `system:` رزرو شده است.

نام [ServiceAccountها](/docs/tasks/configure-pod-container/configure-service-account/) با پیشوند `system:serviceaccount:` شروع می‌شود و این حساب‌ها به گروه‌هایی تعلق دارند که نامشان با پیشوند `system:serviceaccounts:` شروع می‌شود.

{{< note >}}
- پیشوند `system:serviceaccount:` (مفرد) برای نام‌های کاربری حساب‌های سرویس به کار می‌رود.
- پیشوند `system:serviceaccounts:` (جمع) برای گروه‌های حساب‌های سرویس به کار می‌رود.
{{< /note >}}

#### نمونه‌های RoleBinding {#role-binding-examples}

نمونه‌های زیر بخش‌هایی از `RoleBinding` هستند که فقط قسمت `subjects` را نشان می‌دهند.

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

برای حساب سرویس پیش‌فرض در فضای نام (namespace) "kube-system":

```yaml
subjects:
- kind: ServiceAccount
  name: default
  namespace: kube-system
```

برای همهٔ حساب‌های سرویس در فضای نام "qa":

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts:qa
  apiGroup: rbac.authorization.k8s.io
```

برای همهٔ حساب‌های سرویس در هر فضای نامی:

```yaml
subjects:
- kind: Group
  name: system:serviceaccounts
  apiGroup: rbac.authorization.k8s.io
```

برای همهٔ کاربران احراز هویت‌شده:

```yaml
subjects:
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
```

برای همهٔ کاربران احراز هویت‌نشده:

```yaml
subjects:
- kind: Group
  name: system:unauthenticated
  apiGroup: rbac.authorization.k8s.io
```

برای همهٔ کاربران:

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

سرورهای API مجموعه‌ای از آبجکت‌های پیش‌فرض ClusterRole و ClusterRoleBinding را ایجاد می‌کنند.
نام بسیاری از این آبجکت‌ها با پیشوند `system:` شروع می‌شود؛ این پیشوند نشان می‌دهد که منبع مستقیماً توسط control plane کلاستر مدیریت می‌شود.
همهٔ ClusterRoleها و ClusterRoleBindingهای پیش‌فرض برچسب `kubernetes.io/bootstrapping=rbac-defaults` دارند.

{{< caution >}}
هنگام تغییر ClusterRoleها و ClusterRoleBindingهایی که نامشان پیشوند `system:` دارد، احتیاط کنید.
تغییر این منابع ممکن است باعث از کار افتادن کلاستر شود.
{{< /caution >}}

### تطبیق خودکار

سرور API در هر بار راه‌اندازی، مجوزهای جاافتاده را به نقش‌های پیش‌فرض کلاستر و سوژه‌های جاافتاده را به اتصال‌های نقش پیش‌فرض کلاستر اضافه می‌کند.
به این ترتیب کلاستر می‌تواند تغییرات تصادفی را ترمیم کند و با تغییر مجوزها و سوژه‌ها در نسخه‌های جدید کوبرنتیز، نقش‌ها و اتصال‌های نقش به‌روز می‌مانند.

برای غیرفعال کردن این تطبیق، حاشیه‌نویسی (annotation) `rbac.authorization.kubernetes.io/autoupdate` را روی نقش پیش‌فرض کلاستر یا RoleBinding پیش‌فرض کلاستر برابر با `false` قرار دهید.
توجه کنید که نبودِ مجوزها و سوژه‌های پیش‌فرض ممکن است باعث از کار افتادن کلاستر شود.

اگر مجوزدهندهٔ RBAC فعال باشد، تطبیق خودکار به‌طور پیش‌فرض فعال است.

### نقش‌های کشف API {#discovery-roles}

اتصال‌های نقش پیش‌فرض کلاستر به کاربران احراز هویت‌شده و احراز هویت‌نشده اجازه می‌دهند اطلاعاتی از API را بخوانند که دسترسی عمومی به آن‌ها امن تلقی می‌شود (از جمله CustomResourceDefinitionها).
برای غیرفعال کردن دسترسی ناشناس و احراز هویت‌نشده، فلگ `--anonymous-auth=false` را به پیکربندی سرور API اضافه کنید.

برای مشاهدهٔ پیکربندی این نقش‌ها با `kubectl`، دستور زیر را اجرا کنید:

```shell
kubectl get clusterroles system:discovery -o yaml
```

{{< note >}}
اگر این ClusterRole را ویرایش کنید، تغییرات شما هنگام راه‌اندازی مجدد سرور API از طریق [تطبیق خودکار](#auto-reconciliation) بازنویسی می‌شوند. برای جلوگیری از این بازنویسی، یا نقش را به‌صورت دستی ویرایش نکنید یا تطبیق خودکار را غیرفعال کنید.
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
<td>به کاربر اجازهٔ دسترسی فقط‌خواندنی به اطلاعات پایه دربارهٔ خودش را می‌دهد. پیش از نسخهٔ v1.14، این نقش به‌طور پیش‌فرض به <tt>system:unauthenticated</tt> نیز متصل بود.</td>
</tr>
<tr>
<td><b>system:discovery</b></td>
<td>گروه <b>system:authenticated</b></td>
<td>اجازهٔ دسترسی فقط‌خواندنی به نقاط پایانی کشف API را می‌دهد که برای کشف و توافق بر سر سطح API لازم هستند. پیش از نسخهٔ v1.14، این نقش به‌طور پیش‌فرض به <tt>system:unauthenticated</tt> نیز متصل بود.</td>
</tr>
<tr>
<td><b>system:public-info-viewer</b></td>
<td>گروه‌های <b>system:authenticated</b> و <b>system:unauthenticated</b></td>
<td>اجازهٔ دسترسی فقط‌خواندنی به اطلاعات غیرحساس دربارهٔ کلاستر را می‌دهد. این نقش در کوبرنتیز v1.14 معرفی شد.</td>
</tr>
</tbody>
</table>

### نقش‌های کاربرمحور

نام برخی از ClusterRoleهای پیش‌فرض پیشوند `system:` ندارد. این نقش‌ها برای استفادهٔ کاربران در نظر گرفته شده‌اند.
این دسته شامل نقش‌های ابرکاربر (`cluster-admin`)، نقش‌هایی که قرار است با ClusterRoleBindingها در سطح کل کلاستر اعطا شوند و نقش‌هایی است که قرار است با RoleBindingها در فضاهای نام مشخصی اعطا شوند (`admin`، `edit` و `view`).

ClusterRoleهای کاربرمحور از [تجمیع ClusterRole](#aggregated-clusterroles) استفاده می‌کنند تا مدیران بتوانند قواعد مربوط به منابع سفارشی را در این ClusterRoleها بگنجانند. برای افزودن قاعده به نقش‌های `admin`، `edit` یا `view`، یک ClusterRole با یک یا چند برچسب از برچسب‌های زیر ایجاد کنید:

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
<td>دسترسی ابرکاربری برای انجام هر عملی روی هر منبعی را فراهم می‌کند.
اگر در یک <b>ClusterRoleBinding</b> استفاده شود، کنترل کامل بر همهٔ منابع کلاستر و همهٔ فضاهای نام را می‌دهد.
اگر در یک <b>RoleBinding</b> استفاده شود، کنترل کامل بر همهٔ منابع موجود در فضای نام آن اتصال نقش، از جمله خود فضای نام، را می‌دهد.</td>
</tr>
<tr>
<td><b>admin</b></td>
<td>هیچ</td>
<td>دسترسی مدیریتی را فراهم می‌کند و قرار است با یک <b>RoleBinding</b> در داخل یک فضای نام اعطا شود.

اگر در یک <b>RoleBinding</b> استفاده شود، اجازهٔ دسترسی خواندن/نوشتن به بیشتر منابع یک فضای نام را می‌دهد، از جمله امکان ایجاد نقش‌ها و اتصال‌های نقش در آن فضای نام.
این نقش اجازهٔ نوشتن در سهمیهٔ منابع (resource quota) یا خود فضای نام را نمی‌دهد.
همچنین این نقش در کلاسترهایی که با کوبرنتیز v1.22 به بالا ایجاد شده‌اند، اجازهٔ نوشتن در EndpointSliceها را نمی‌دهد. اطلاعات بیشتر در
[بخش «دسترسی نوشتن برای EndpointSliceها»](#write-access-for-endpoints) آمده است.</td>
</tr>
<tr>
<td><b>edit</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی خواندن/نوشتن به بیشتر آبجکت‌های یک فضای نام را می‌دهد.

این نقش اجازهٔ مشاهده یا تغییر نقش‌ها و اتصال‌های نقش را نمی‌دهد.
با این حال، این نقش امکان دسترسی به Secretها و اجرای Podها با هر ServiceAccount موجود در فضای نام را فراهم می‌کند؛ بنابراین می‌توان از آن برای به دست آوردن سطح دسترسی API هر ServiceAccount در آن فضای نام استفاده کرد. همچنین این نقش در کلاسترهایی که با کوبرنتیز v1.22 به بالا ایجاد شده‌اند، اجازهٔ نوشتن در EndpointSliceها را نمی‌دهد. اطلاعات بیشتر در
[بخش «دسترسی نوشتن برای EndpointSliceها»](#write-access-for-endpoints) آمده است.</td>
</tr>
<tr>
<td><b>view</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی فقط‌خواندنی برای مشاهدهٔ بیشتر آبجکت‌های یک فضای نام را می‌دهد.
این نقش اجازهٔ مشاهدهٔ نقش‌ها یا اتصال‌های نقش را نمی‌دهد.

این نقش اجازهٔ مشاهدهٔ Secretها را نمی‌دهد، زیرا خواندن محتوای Secretها امکان دسترسی به اعتبارنامه‌های ServiceAccountهای آن فضای نام را فراهم می‌کند و در نتیجه دسترسی API با هویت هر ServiceAccount در آن فضای نام ممکن می‌شود (که نوعی ارتقای سطح دسترسی است).</td>
</tr>
</tbody>
</table>

### نقش‌های اجزای اصلی

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
<td>اجازهٔ دسترسی به منابعی را می‌دهد که مؤلفهٔ {{< glossary_tooltip term_id="kube-scheduler" text="زمان‌بند" >}} به آن‌ها نیاز دارد.</td>
</tr>
<tr>
<td><b>system:volume-scheduler</b></td>
<td>کاربر <b>system:kube-scheduler</b></td>
<td>اجازهٔ دسترسی به منابع حجم (volume) را می‌دهد که مؤلفهٔ kube-scheduler به آن‌ها نیاز دارد.</td>
</tr>
<tr>
<td><b>system:kube-controller-manager</b></td>
<td>کاربر <b>system:kube-controller-manager</b></td>
<td>اجازهٔ دسترسی به منابعی را می‌دهد که مؤلفهٔ {{< glossary_tooltip term_id="kube-controller-manager" text="مدیر کنترل‌کننده‌ها" >}} به آن‌ها نیاز دارد.
مجوزهای مورد نیاز هر کنترل‌کننده به‌تفصیل در <a href="#controller-roles">نقش‌های کنترل‌کننده</a> آمده است.</td>
</tr>
<tr>
<td><b>system:node</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی به منابعی را می‌دهد که kubelet به آن‌ها نیاز دارد، <b>از جمله دسترسی خواندن به همهٔ Secretها و دسترسی نوشتن به همهٔ آبجکت‌های وضعیت Pod</b>.

به‌جای نقش <tt>system:node</tt> باید از <a href="/docs/reference/access-authn-authz/node/">مجوزدهندهٔ Node</a> و <a href="/docs/reference/access-authn-authz/admission-controllers/#noderestriction">افزونهٔ پذیرش NodeRestriction</a> استفاده کنید و دسترسی API را بر اساس Podهایی که برای اجرا روی هر kubelet زمان‌بندی شده‌اند به آن اعطا کنید.

نقش <tt>system:node</tt> فقط برای سازگاری با کلاسترهای کوبرنتیزی وجود دارد که از نسخه‌های پیش از v1.8 ارتقا یافته‌اند.
</td>
</tr>
<tr>
<td><b>system:node-proxier</b></td>
<td>کاربر <b>system:kube-proxy</b></td>
<td>اجازهٔ دسترسی به منابعی را می‌دهد که مؤلفهٔ {{< glossary_tooltip term_id="kube-proxy" text="kube-proxy" >}} به آن‌ها نیاز دارد.</td>
</tr>
</tbody>
</table>

### نقش‌های سایر اجزا

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
<td>هیچ</td>
<td>امکان واگذاری بررسی‌های احراز هویت و مجوزدهی را فراهم می‌کند.
سرورهای API افزونه معمولاً برای احراز هویت و مجوزدهی یکپارچه از این نقش استفاده می‌کنند.</td>
</tr>
<tr>
<td><b>system:heapster</b></td>
<td>هیچ</td>
<td>نقش مربوط به مؤلفهٔ <a href="https://github.com/kubernetes/heapster">Heapster</a> (منسوخ).</td>
</tr>
<tr>
<td><b>system:kube-aggregator</b></td>
<td>هیچ</td>
<td>نقش مربوط به مؤلفهٔ <a href="https://github.com/kubernetes/kube-aggregator">kube-aggregator</a>.</td>
</tr>
<tr>
<td><b>system:kube-dns</b></td>
<td>حساب سرویس <b>kube-dns</b> در فضای نام <b>kube-system</b></td>
<td>نقش مربوط به مؤلفهٔ منسوخ kube-dns. (<a href="/docs/concepts/services-networking/dns-pod-service/">CoreDNS</a> از این نقش استفاده نمی‌کند.)</td>
</tr>
<tr>
<td><b>system:kubelet-api-admin</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی کامل به API کوبلت (kubelet) را می‌دهد.</td>
</tr>
<tr>
<td><b>system:node-bootstrapper</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی به منابعی را می‌دهد که برای انجام
<a href="/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/">راه‌اندازی اولیهٔ TLS در kubelet</a> لازم هستند.</td>
</tr>
<tr>
<td><b>system:node-problem-detector</b></td>
<td>هیچ</td>
<td>نقش مربوط به مؤلفهٔ <a href="https://github.com/kubernetes/node-problem-detector">node-problem-detector</a>.</td>
</tr>
<tr>
<td><b>system:persistent-volume-provisioner</b></td>
<td>هیچ</td>
<td>اجازهٔ دسترسی به منابعی را می‌دهد که بیشتر <a href="/docs/concepts/storage/persistent-volumes/#dynamic">تأمین‌کننده‌های پویای حجم</a> به آن‌ها نیاز دارند.</td>
</tr>
<tr>
<td><b>system:monitoring</b></td>
<td>گروه <b>system:monitoring</b></td>
<td>اجازهٔ دسترسی خواندن به نقاط پایانی پایش control plane را می‌دهد (یعنی نقاط پایانی زنده‌بودن و آمادگی {{< glossary_tooltip term_id="kube-apiserver" text="kube-apiserver" >}} (<tt>/healthz</tt>، <tt>/livez</tt>، <tt>/readyz</tt>)، نقاط پایانی بررسی سلامت مجزا (<tt>/healthz/*</tt>، <tt>/livez/*</tt>، <tt>/readyz/*</tt>) و <tt>/metrics</tt>) و باعث می‌شود kube-apiserver سرآیند traceparent ارسال‌شده همراه درخواست‌ها را برای ردیابی در نظر بگیرد. توجه کنید که نقاط پایانی بررسی سلامت مجزا و نقطهٔ پایانی متریک ممکن است اطلاعات حساسی را افشا کنند.</td>
</tr>
</tbody>
</table>

### نقش‌های کنترل‌کننده‌های داخلی {#controller-roles}

{{< glossary_tooltip term_id="kube-controller-manager" text="مدیر کنترل‌کننده‌های" >}} کوبرنتیز،
{{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌هایی" >}} را اجرا می‌کند که در control plane کوبرنتیز تعبیه شده‌اند.
اگر kube-controller-manager با `--use-service-account-credentials` فراخوانی شود، هر کنترل‌کننده را با یک حساب سرویس جداگانه راه‌اندازی می‌کند.
برای هر کنترل‌کنندهٔ داخلی، نقش متناظری با پیشوند `system:controller:` وجود دارد.
اگر مدیر کنترل‌کننده‌ها با `--use-service-account-credentials` راه‌اندازی نشود، همهٔ حلقه‌های کنترلی را با اعتبارنامهٔ خودش اجرا می‌کند و این اعتبارنامه باید همهٔ نقش‌های مربوط را دریافت کرده باشد.
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

## جلوگیری از ارتقای سطح دسترسی و راه‌اندازی اولیه

‏API مربوط به RBAC مانع می‌شود که کاربران با ویرایش نقش‌ها یا اتصال‌های نقش، سطح دسترسی خود را ارتقا دهند.
از آنجا که این محدودیت در سطح API اعمال می‌شود، حتی زمانی که مجوزدهندهٔ RBAC استفاده نمی‌شود نیز برقرار است.

### محدودیت‌های ایجاد یا به‌روزرسانی نقش

فقط در صورتی می‌توانید نقشی را ایجاد یا به‌روزرسانی کنید که دست‌کم یکی از شرایط زیر برقرار باشد:

1. همهٔ مجوزهای موجود در آن نقش را از قبل، در همان دامنه‌ای که آبجکت در حال تغییر در آن قرار دارد، داشته باشید
   (در سطح کل کلاستر برای ClusterRole، و در همان فضای نام یا در سطح کل کلاستر برای Role).
2. مجوز صریح برای اجرای فعل `escalate` روی منبع `roles` یا
   `clusterroles` در گروه API `rbac.authorization.k8s.io` به شما اعطا شده باشد.

برای مثال، اگر `user-1` امکان فهرست کردن Secretها در سطح کل کلاستر را نداشته باشد، نمی‌تواند ClusterRoleای ایجاد کند که این مجوز را دربر دارد. برای اینکه کاربری بتواند نقش‌ها را ایجاد یا به‌روزرسانی کند:

1. نقشی به او اعطا کنید که بسته به نیاز، اجازهٔ ایجاد یا به‌روزرسانی آبجکت‌های Role یا ClusterRole را به او بدهد.
2. به او اجازه دهید مجوزهای مشخصی را در نقش‌هایی که ایجاد یا به‌روزرسانی می‌کند بگنجاند:
   * به‌صورت ضمنی، با اعطای همان مجوزها به او (اگر کاربر تلاش کند Role یا
     ClusterRoleای با مجوزهایی ایجاد یا تغییر دهد که خودش آن‌ها را ندارد، درخواست API رد می‌شود)
   * یا به‌صورت صریح، با اعطای مجوز اجرای فعل `escalate` روی منابع `roles` یا `clusterroles` در گروه API
     `rbac.authorization.k8s.io`، تا بتواند هر مجوزی را در یک `Role` یا `ClusterRole` مشخص کند

### محدودیت‌های ایجاد یا به‌روزرسانی اتصال نقش

شما فقط در دو حالت می‌توانید یک اتصال نقش (role binding) را ایجاد یا به‌روزرسانی کنید: اگر از قبل همهٔ مجوزهای موجود در نقش ارجاع‌شده را (در همان دامنهٔ اتصال نقش) داشته باشید، *یا* اگر مجاز باشید فعل `bind` را روی نقش ارجاع‌شده اجرا کنید. برای مثال، اگر `user-1` توانایی فهرست‌کردن Secretها را در سطح کل کلاستر نداشته باشد، نمی‌تواند یک ClusterRoleBinding به نقشی ایجاد کند که این مجوز را اعطا می‌کند. برای اینکه کاربری بتواند اتصال‌های نقش را ایجاد یا به‌روزرسانی کند:

1. نقشی به او اعطا کنید که بسته به نیاز، اجازهٔ ایجاد یا به‌روزرسانی آبجکت‌های RoleBinding یا ClusterRoleBinding را به او بدهد.
2. مجوزهای لازم برای متصل‌کردن یک نقش مشخص را به او اعطا کنید:
   * به‌صورت ضمنی، با دادن مجوزهای موجود در آن نقش به او.
   * به‌صورت صریح، با دادن مجوز اجرای فعل `bind` روی آن Role (یا ClusterRole) مشخص.

برای مثال، با این ClusterRole و RoleBinding، کاربر `user-1` می‌تواند نقش‌های `admin`، `edit` و `view` را در فضای نام `user-1-namespace` به کاربران دیگر اعطا کند:

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

هنگام راه‌اندازی اولیهٔ نخستین نقش‌ها و اتصال‌های نقش، کاربر اولیه ناگزیر است مجوزهایی را اعطا کند که هنوز خودش آن‌ها را ندارد. برای راه‌اندازی اولیهٔ نقش‌ها و اتصال‌های نقش:

* از اعتبارنامه‌ای (credential) با گروه "system:masters" استفاده کنید؛ این گروه از طریق اتصال‌های پیش‌فرض به نقش ابرکاربری "cluster-admin" متصل است.

## ابزارهای خط فرمان

### `kubectl create role`

این دستور یک آبجکت Role ایجاد می‌کند که مجوزها را در یک فضای نام تعریف می‌کند. نمونه‌ها:

* ایجاد یک Role با نام "pod-reader" که به کاربران اجازه می‌دهد عملیات `get`، `watch` و `list` را روی پادها انجام دهند:

  ```shell
  kubectl create role pod-reader --verb=get --verb=list --verb=watch --resource=pods
  ```

* ایجاد یک Role با نام "pod-reader" همراه با مشخص‌کردن resourceNames:

  ```shell
  kubectl create role pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod
  ```

* ایجاد یک Role با نام "foo" همراه با مشخص‌کردن apiGroups:

  ```shell
  kubectl create role foo --verb=get,list,watch --resource=replicasets.apps
  ```

* ایجاد یک Role با نام "foo" همراه با مجوزهای زیرمنبع (subresource):

  ```shell
  kubectl create role foo --verb=get,list,watch --resource=pods,pods/status
  ```

* ایجاد یک Role با نام "my-component-lease-holder" همراه با مجوز خواندن و به‌روزرسانی منبعی با نامی مشخص:

  ```shell
  kubectl create role my-component-lease-holder --verb=get,list,watch,update --resource=lease --resource-name=my-component
  ```

### `kubectl create clusterrole`

این دستور یک ClusterRole ایجاد می‌کند. نمونه‌ها:

* ایجاد یک ClusterRole با نام "pod-reader" که به کاربر اجازه می‌دهد عملیات `get`، `watch` و `list` را روی پادها انجام دهد:

  ```shell
  kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
  ```

* ایجاد یک ClusterRole با نام "pod-reader" همراه با مشخص‌کردن resourceNames:

  ```shell
  kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با مشخص‌کردن apiGroups:

  ```shell
  kubectl create clusterrole foo --verb=get,list,watch --resource=replicasets.apps
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با مجوزهای زیرمنبع:

  ```shell
  kubectl create clusterrole foo --verb=get,list,watch --resource=pods,pods/status
  ```

* ایجاد یک ClusterRole با نام "foo" همراه با مشخص‌کردن nonResourceURL:

  ```shell
  kubectl create clusterrole "foo" --verb=get --non-resource-url=/logs/*
  ```

* ایجاد یک ClusterRole با نام "monitoring" همراه با مشخص‌کردن aggregationRule:

  ```shell
  kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
  ```

### `kubectl create rolebinding`

این دستور یک Role یا ClusterRole را در یک فضای نام مشخص اعطا می‌کند. نمونه‌ها:

* اعطای مجوزهای ClusterRole با نام "admin" به کاربری با نام "bob" در فضای نام "acme":

  ```shell
  kubectl create rolebinding bob-admin-binding --clusterrole=admin --user=bob --namespace=acme
  ```

* اعطای مجوزهای ClusterRole با نام "view" در فضای نام "acme" به حساب سرویسی با نام "myapp" که در همان فضای نام "acme" قرار دارد:

  ```shell
  kubectl create rolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp --namespace=acme
  ```

* اعطای مجوزهای ClusterRole با نام "view" در فضای نام "acme" به حساب سرویسی با نام "myapp" که در فضای نام "myappnamespace" قرار دارد:

  ```shell
  kubectl create rolebinding myappnamespace-myapp-view-binding --clusterrole=view --serviceaccount=myappnamespace:myapp --namespace=acme
  ```

### `kubectl create clusterrolebinding`

این دستور یک ClusterRole را در سطح کل کلاستر (همهٔ فضاهای نام) اعطا می‌کند. نمونه‌ها:

* اعطای مجوزهای ClusterRole با نام "cluster-admin" در سطح کل کلاستر به کاربری با نام "root":

  ```shell
  kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=root
  ```

* اعطای مجوزهای ClusterRole با نام "system:node-proxier" در سطح کل کلاستر به کاربری با نام "system:kube-proxy":

  ```shell
  kubectl create clusterrolebinding kube-proxy-binding --clusterrole=system:node-proxier --user=system:kube-proxy
  ```

* اعطای مجوزهای ClusterRole با نام "view" در سطح کل کلاستر به حساب سرویسی با نام "myapp" در فضای نام "acme":

  ```shell
  kubectl create clusterrolebinding myapp-view-binding --clusterrole=view --serviceaccount=acme:myapp
  ```

### `kubectl auth reconcile` {#kubectl-auth-reconcile}

این دستور آبجکت‌های API از نوع `rbac.authorization.k8s.io/v1` را بر اساس یک فایل مانیفست ایجاد یا به‌روزرسانی می‌کند.

آبجکت‌هایی که وجود ندارند ایجاد می‌شوند و در صورت نیاز، فضای نام دربرگیرندهٔ آبجکت‌های وابسته به فضای نام نیز ایجاد می‌شود.

نقش‌های موجود به‌روزرسانی می‌شوند تا مجوزهای موجود در آبجکت‌های ورودی را شامل شوند. اگر `--remove-extra-permissions` مشخص شده باشد، مجوزهای اضافی نیز حذف می‌شوند.

اتصال‌های موجود به‌روزرسانی می‌شوند تا سوژه‌های (subjects) موجود در آبجکت‌های ورودی را شامل شوند. اگر `--remove-extra-subjects` مشخص شده باشد، سوژه‌های اضافی نیز حذف می‌شوند.

نمونه‌ها:

* آزمودن اعمال یک فایل مانیفست از آبجکت‌های RBAC و نمایش تغییراتی که اعمال خواهند شد:

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml --dry-run=client
  ```

* اعمال یک فایل مانیفست از آبجکت‌های RBAC، با حفظ هرگونه مجوز اضافی (در نقش‌ها) و هرگونه سوژهٔ اضافی (در اتصال‌ها):

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml
  ```

* اعمال یک فایل مانیفست از آبجکت‌های RBAC، با حذف هرگونه مجوز اضافی (در نقش‌ها) و هرگونه سوژهٔ اضافی (در اتصال‌ها):

  ```shell
  kubectl auth reconcile -f my-rbac-rules.yaml --remove-extra-subjects --remove-extra-permissions
  ```

## مجوزهای ServiceAccount {#service-account-permissions}

سیاست‌های پیش‌فرض RBAC مجوزهایی با دامنهٔ محدود به مؤلفه‌های control plane، نودها و کنترل‌کننده‌ها اعطا می‌کنند، اما به حساب‌های سرویس خارج از فضای نام `kube-system` *هیچ مجوزی* نمی‌دهند (به‌جز مجوزهایی که [نقش‌های کشف API](#discovery-roles) فراهم می‌کنند).

به این ترتیب می‌توانید در صورت نیاز، نقش‌های مشخصی را به ServiceAccountهای مشخصی اعطا کنید. اتصال‌های نقش جزئی‌تر امنیت بیشتری فراهم می‌کنند، اما مدیریت آن‌ها زحمت بیشتری دارد. اعطای مجوزهای گسترده‌تر مدیریت ساده‌تری دارد، اما ممکن است دسترسی غیرضروری (و بالقوه قابل‌ارتقا) به API را در اختیار ServiceAccountها قرار دهد.

رویکردها به ترتیب از امن‌ترین تا کم‌امن‌ترین عبارت‌اند از:

1. اعطای نقش به یک حساب سرویس مختص برنامه (بهترین روش)

   در این روش، برنامه باید یک `serviceAccountName` را در مشخصات پاد خود تعیین کند و حساب سرویس نیز باید ایجاد شده باشد (از طریق API، مانیفست برنامه، `kubectl create serviceaccount` و غیره).

   برای مثال، اعطای مجوز فقط‌خواندنی در فضای نام "my-namespace" به حساب سرویس "my-sa":

   ```shell
   kubectl create rolebinding my-sa-view \
     --clusterrole=view \
     --serviceaccount=my-namespace:my-sa \
     --namespace=my-namespace
   ```

2. اعطای نقش به حساب سرویس "default" در یک فضای نام

   اگر برنامه‌ای `serviceAccountName` را مشخص نکند، از حساب سرویس "default" استفاده می‌کند.

   {{< note >}}
   مجوزهایی که به حساب سرویس "default" داده می‌شوند، در اختیار همهٔ پادهایی از آن فضای نام قرار می‌گیرند که `serviceAccountName` را مشخص نکرده‌اند.
   {{< /note >}}

   برای مثال، اعطای مجوز فقط‌خواندنی در فضای نام "my-namespace" به حساب سرویس "default":

   ```shell
   kubectl create rolebinding default-view \
     --clusterrole=view \
     --serviceaccount=my-namespace:default \
     --namespace=my-namespace
   ```

3. اعطای نقش به همهٔ حساب‌های سرویس در یک فضای نام

   اگر می‌خواهید همهٔ برنامه‌های یک فضای نام، صرف‌نظر از حساب سرویسی که استفاده می‌کنند، یک نقش داشته باشند، می‌توانید آن نقش را به گروه حساب‌های سرویس آن فضای نام اعطا کنید.

   برای مثال، اعطای مجوز فقط‌خواندنی در فضای نام "my-namespace" به همهٔ حساب‌های سرویس همان فضای نام:

   ```shell
   kubectl create rolebinding serviceaccounts-view \
     --clusterrole=view \
     --group=system:serviceaccounts:my-namespace \
     --namespace=my-namespace
   ```

4. اعطای یک نقش محدود به همهٔ حساب‌های سرویس در سطح کل کلاستر (توصیه نمی‌شود)

   اگر نمی‌خواهید مجوزها را به تفکیک فضای نام مدیریت کنید، می‌توانید یک نقش در سطح کلاستر را به همهٔ حساب‌های سرویس اعطا کنید.

   برای مثال، اعطای مجوز فقط‌خواندنی در همهٔ فضاهای نام به همهٔ حساب‌های سرویس کلاستر:

   ```shell
   kubectl create clusterrolebinding serviceaccounts-view \
     --clusterrole=view \
    --group=system:serviceaccounts
   ```

5. اعطای دسترسی ابرکاربری به همهٔ حساب‌های سرویس در سطح کل کلاستر (اکیداً توصیه نمی‌شود)

   اگر تفکیک مجوزها برایتان اصلاً اهمیتی ندارد، می‌توانید دسترسی ابرکاربری را به همهٔ حساب‌های سرویس اعطا کنید.

   {{< warning >}}
   با این کار، هر برنامه‌ای دسترسی کامل به کلاستر شما پیدا می‌کند. همچنین هر کاربری که دسترسی خواندن Secretها (یا توانایی ایجاد هر پادی) را داشته باشد، دسترسی کامل به کلاستر شما خواهد داشت.
   {{< /warning >}}

   ```shell
   kubectl create clusterrolebinding serviceaccounts-cluster-admin \
     --clusterrole=cluster-admin \
     --group=system:serviceaccounts
   ```

## دسترسی نوشتن برای EndpointSliceها {#write-access-for-endpoints}

در کلاسترهای کوبرنتیزی که پیش از نسخهٔ v1.22 ایجاد شده‌اند، نقش‌های تجمیعی "edit" و "admin" شامل دسترسی نوشتن به EndpointSliceها (و API منسوخ‌شدهٔ Endpoints) هستند. برای کاهش اثر [CVE-2021-25740](https://github.com/kubernetes/kubernetes/issues/103675)، این دسترسی در کلاسترهایی که با کوبرنتیز v1.22 یا نسخه‌های بعدی ایجاد می‌کنید، بخشی از نقش‌های تجمیعی نیست.

این تغییر روی کلاسترهای موجودی که به کوبرنتیز v1.22 ارتقا یافته‌اند اعمال نمی‌شود. [اطلاعیهٔ CVE](https://github.com/kubernetes/kubernetes/issues/103675) راهنمایی‌هایی برای محدودکردن این دسترسی در کلاسترهای موجود ارائه می‌دهد.

اگر می‌خواهید کلاسترهای جدید این سطح از دسترسی را در نقش‌های تجمیعی حفظ کنند، می‌توانید ClusterRole زیر را ایجاد کنید:

{{% code_sample file="access/endpoints-aggregated.yaml" %}}

## ارتقا از ABAC

کلاسترهایی که در ابتدا نسخه‌های قدیمی‌تر کوبرنتیز را اجرا می‌کردند، اغلب از سیاست‌های ABAC سهل‌گیرانه استفاده می‌کردند که از جملهٔ آن‌ها اعطای دسترسی کامل API به همهٔ حساب‌های سرویس بود.

سیاست‌های پیش‌فرض RBAC مجوزهایی با دامنهٔ محدود به مؤلفه‌های control plane، نودها و کنترل‌کننده‌ها اعطا می‌کنند، اما به حساب‌های سرویس خارج از فضای نام `kube-system` *هیچ مجوزی* نمی‌دهند (به‌جز مجوزهایی که [نقش‌های کشف API](#discovery-roles) فراهم می‌کنند).

این رویکرد بسیار امن‌تر است، اما ممکن است در کار بارهای کاری موجودی که انتظار دارند مجوزهای API را به‌طور خودکار دریافت کنند اختلال ایجاد کند. در ادامه دو رویکرد برای مدیریت این گذار آمده است:

### مجوزدهنده‌های موازی

هر دو مجوزدهندهٔ RBAC و ABAC را اجرا کنید و فایل سیاستی را مشخص کنید که [سیاست قدیمی ABAC](/docs/reference/access-authn-authz/abac/#policy-file-format) را در بر دارد:

```shell
--authorization-mode=...,RBAC,ABAC --authorization-policy-file=mypolicy.json
```

توضیح دقیق‌تر نخستین گزینهٔ خط فرمان چنین است: اگر مجوزدهنده‌های قبلی، مانند Node، درخواستی را رد کنند، مجوزدهندهٔ RBAC تلاش می‌کند درخواست API را مجاز کند. اگر RBAC نیز آن درخواست API را رد کند، مجوزدهندهٔ ABAC اجرا می‌شود. بنابراین هر درخواستی که *یکی از* سیاست‌های RBAC یا ABAC آن را مجاز بداند، پذیرفته می‌شود.

هنگامی که kube-apiserver با سطح لاگ ۵ یا بالاتر برای مؤلفهٔ RBAC اجرا شود (`--vmodule=rbac*=5` یا `--v=5`)، می‌توانید موارد رد درخواست توسط RBAC را در لاگ سرور API (با پیشوند `RBAC`) ببینید. با استفاده از این اطلاعات می‌توانید تعیین کنید چه نقش‌هایی باید به کدام کاربران، گروه‌ها یا حساب‌های سرویس اعطا شوند.

پس از آنکه [نقش‌ها را به حساب‌های سرویس اعطا کردید](#service-account-permissions) و بارهای کاری بدون هیچ پیام رد RBAC در لاگ‌های سرور اجرا شدند، می‌توانید مجوزدهندهٔ ABAC را حذف کنید.

### مجوزهای سهل‌گیرانهٔ RBAC

می‌توانید یک سیاست سهل‌گیرانهٔ ABAC را با استفاده از اتصال‌های نقش RBAC بازسازی کنید.

{{< warning >}}
سیاست زیر به **همهٔ** حساب‌های سرویس اجازه می‌دهد در نقش مدیر کلاستر عمل کنند. هر برنامه‌ای که در یک کانتینر اجرا می‌شود، اعتبارنامه‌های حساب سرویس را به‌طور خودکار دریافت می‌کند و می‌تواند هر عملیاتی را روی API انجام دهد؛ از جمله مشاهدهٔ secretها و تغییر مجوزها. این سیاست توصیه نمی‌شود.

```shell
kubectl create clusterrolebinding permissive-binding \
  --clusterrole=cluster-admin \
  --user=admin \
  --user=kubelet \
  --group=system:serviceaccounts
```
{{< /warning >}}

پس از گذار به RBAC، باید کنترل‌های دسترسی کلاستر خود را تنظیم کنید تا مطمئن شوید با نیازهای امنیت اطلاعات شما سازگار هستند.

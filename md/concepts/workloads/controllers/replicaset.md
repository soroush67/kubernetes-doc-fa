---
# NOTE TO LOCALIZATION TEAMS
#
# If updating front matter for your localization because there is still
# a "feature" key in this page, then you also need to update
# content/??/docs/concepts/architecture/self-healing.md (which is where
# it moved to)
reviewers:
- Kashomon
- bprashanth
- madhusudancs
title: ReplicaSet
api_metadata:
- apiVersion: "apps/v1"
  kind: "ReplicaSet"
content_type: concept
description: >-
  هدف یک ReplicaSet این است که در هر لحظه مجموعه‌ای پایدار از Podهای تکثیری (replica) را در حال اجرا نگه دارد.
  معمولاً یک Deployment تعریف می‌کنید و اجازه می‌دهید آن Deployment به‌طور خودکار ReplicaSetها را مدیریت کند.
weight: 20
hide_summary: true # Listed separately in section index
---

<!-- overview -->

هدف یک ReplicaSet این است که در هر لحظه مجموعه‌ای پایدار از Podهای تکثیری (replica) را در حال اجرا نگه دارد. از این رو،
اغلب برای تضمین در دسترس بودن تعداد مشخصی از Podهای یکسان به کار می‌رود.

<!-- body -->

## یک ReplicaSet چگونه کار می‌کند

یک ReplicaSet با مجموعه‌ای از فیلدها تعریف می‌شود؛ از جمله یک انتخابگر (selector) که مشخص می‌کند Podهایی را که می‌تواند تصاحب کند چگونه شناسایی کند، تعداد
replicaها که نشان می‌دهد چند Pod را باید نگه دارد، و یک قالب Pod که داده‌های Podهای جدیدی را مشخص می‌کند
که باید برای برآورده کردن معیار تعداد replicaها ایجاد شوند. سپس ReplicaSet با ایجاد
و حذف Podها در صورت نیاز برای رسیدن به تعداد مطلوب، هدف خود را محقق می‌کند. هنگامی که یک ReplicaSet نیاز به ایجاد Podهای جدید داشته باشد، از قالب Pod
خود استفاده می‌کند.

یک ReplicaSet از طریق فیلد [metadata.ownerReferences](/docs/concepts/architecture/garbage-collection/#owners-dependents)
Podها به آن‌ها پیوند داده می‌شود؛ این فیلد مشخص می‌کند آبجکت فعلی متعلق به کدام منبع است. همه Podهایی که یک ReplicaSet تصاحب کرده است، اطلاعات شناسایی
ReplicaSet مالک خود را در فیلد ownerReferences دارند. ReplicaSet از طریق همین پیوند
از وضعیت Podهایی که نگهداری می‌کند آگاه می‌شود و بر اساس آن برنامه‌ریزی می‌کند.

یک ReplicaSet با استفاده از انتخابگر خود، Podهای جدیدی را که باید تصاحب کند شناسایی می‌کند. اگر Podای وجود داشته باشد که
OwnerReference نداشته باشد یا OwnerReference آن یک {{< glossary_tooltip term_id="controller" >}} نباشد و
با انتخابگر یک ReplicaSet مطابقت داشته باشد، بی‌درنگ توسط همان ReplicaSet تصاحب می‌شود.

## چه زمانی از ReplicaSet استفاده کنیم

یک ReplicaSet تضمین می‌کند که در هر لحظه تعداد مشخصی از replicaهای Pod در حال اجرا
باشند. با این حال، Deployment مفهومی سطح بالاتر است که ReplicaSetها را مدیریت می‌کند و
به‌روزرسانی‌های اعلانی (declarative) برای Podها را همراه با بسیاری از قابلیت‌های مفید دیگر فراهم می‌کند.
بنابراین توصیه می‌کنیم به‌جای استفاده مستقیم از ReplicaSetها از Deploymentها استفاده کنید، مگر اینکه
به هماهنگ‌سازی سفارشی به‌روزرسانی نیاز داشته باشید یا اصلاً به به‌روزرسانی نیازی نداشته باشید.

این در عمل به این معناست که ممکن است هرگز نیازی به دست‌کاری آبجکت‌های ReplicaSet نداشته باشید:
به‌جای آن از یک Deployment استفاده کنید و برنامه خود را در بخش spec تعریف کنید.

## مثال

{{% code_sample file="controllers/frontend.yaml" %}}

ذخیره این مانیفست در `frontend.yaml` و ارسال آن به یک کلاستر کوبرنتیز،
ReplicaSet تعریف‌شده و Podهایی را که مدیریت می‌کند ایجاد خواهد کرد.

```shell
kubectl apply -f https://kubernetes.io/examples/controllers/frontend.yaml
```

سپس می‌توانید ReplicaSetهای مستقرشده فعلی را دریافت کنید:

```shell
kubectl get rs
```

و ReplicaSet مربوط به frontend را که ایجاد کرده‌اید ببینید:

```
NAME       DESIRED   CURRENT   READY   AGE
frontend   3         3         3       6s
```

همچنین می‌توانید وضعیت ReplicaSet را بررسی کنید:

```shell
kubectl describe rs/frontend
```

و خروجی‌ای مشابه زیر خواهید دید:

```
Name:         frontend
Namespace:    default
Selector:     tier=frontend
Labels:       app=guestbook
              tier=frontend
Annotations:  <none>
Replicas:     3 current / 3 desired
Pods Status:  3 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  tier=frontend
  Containers:
   php-redis:
    Image:        us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-gbgfx
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-rwz57
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-wkl7w
```

و در پایان می‌توانید Podهای راه‌اندازی‌شده را بررسی کنید:

```shell
kubectl get pods
```

باید اطلاعات Podای مشابه زیر ببینید:

```
NAME             READY   STATUS    RESTARTS   AGE
frontend-gbgfx   1/1     Running   0          10m
frontend-rwz57   1/1     Running   0          10m
frontend-wkl7w   1/1     Running   0          10m
```

همچنین می‌توانید بررسی کنید که مرجع مالک (owner reference) این Podها روی ReplicaSet مربوط به frontend تنظیم شده باشد.
برای این کار، yaml یکی از Podهای در حال اجرا را دریافت کنید:

```shell
kubectl get pods frontend-gbgfx -o yaml
```

خروجی مشابه زیر خواهد بود و اطلاعات ReplicaSet مربوط به frontend در فیلد ownerReferences بخش metadata تنظیم شده است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2024-02-28T22:30:44Z"
  generateName: frontend-
  labels:
    tier: frontend
  name: frontend-gbgfx
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: frontend
    uid: e129deca-f864-481b-bb16-b27abfd92292
...
```

## تصاحب Podهای غیرقالبی

اگرچه می‌توانید بدون هیچ مشکلی Podهای مستقل (bare) ایجاد کنید، اکیداً توصیه می‌شود مطمئن شوید که این Podهای مستقل
برچسب‌هایی ندارند که با انتخابگر یکی از ReplicaSetهای شما مطابقت داشته باشد. دلیل این است که یک ReplicaSet
تنها به مالکیت Podهایی که در قالبش مشخص شده‌اند محدود نیست و می‌تواند Podهای دیگر را نیز به روشی که در بخش‌های قبلی توضیح داده شد تصاحب کند.

مثال قبلی ReplicaSet مربوط به frontend و Podهای مشخص‌شده در مانیفست زیر را در نظر بگیرید:

{{% code_sample file="pods/pod-rs.yaml" %}}

از آنجا که این Podها هیچ Controller (یا هیچ آبجکتی) را به‌عنوان مرجع مالک خود ندارند و با انتخابگر ReplicaSet مربوط به frontend
مطابقت دارند، بی‌درنگ توسط آن تصاحب می‌شوند.

فرض کنید این Podها را پس از آن ایجاد می‌کنید که ReplicaSet مربوط به frontend مستقر شده و replicaهای اولیه Pod خود را
برای برآورده کردن الزام تعداد replicaها راه‌اندازی کرده است:

```shell
kubectl apply -f https://kubernetes.io/examples/pods/pod-rs.yaml
```

Podهای جدید توسط ReplicaSet تصاحب می‌شوند و سپس بی‌درنگ خاتمه می‌یابند، زیرا ReplicaSet از تعداد مطلوب خود
فراتر خواهد رفت.

دریافت Podها:

```shell
kubectl get pods
```

خروجی نشان می‌دهد که Podهای جدید یا پیش‌تر خاتمه یافته‌اند یا در حال خاتمه یافتن هستند:

```
NAME             READY   STATUS        RESTARTS   AGE
frontend-b2zdv   1/1     Running       0          10m
frontend-vcmts   1/1     Running       0          10m
frontend-wtsmm   1/1     Running       0          10m
pod1             0/1     Terminating   0          1s
pod2             0/1     Terminating   0          1s
```

اگر ابتدا Podها را ایجاد کنید:

```shell
kubectl apply -f https://kubernetes.io/examples/pods/pod-rs.yaml
```

و سپس ReplicaSet را ایجاد کنید:

```shell
kubectl apply -f https://kubernetes.io/examples/controllers/frontend.yaml
```

خواهید دید که ReplicaSet، Podها را تصاحب کرده و تنها طبق spec خود Podهای جدید ایجاد کرده است تا زمانی که
مجموع Podهای جدید و Podهای اصلی با تعداد مطلوب آن برابر شود. با دریافت Podها:

```shell
kubectl get pods
```

خروجی چنین خواهد بود:
```
NAME             READY   STATUS    RESTARTS   AGE
frontend-hmmj2   1/1     Running   0          9s
pod1             1/1     Running   0          36s
pod2             1/1     Running   0          36s
```

به این ترتیب، یک ReplicaSet می‌تواند مالک مجموعه‌ای ناهمگن از Podها باشد.

## نوشتن مانیفست ReplicaSet

مانند همه آبجکت‌های دیگر API کوبرنتیز، یک ReplicaSet به فیلدهای `apiVersion`، `kind` و `metadata` نیاز دارد.
برای ReplicaSetها، مقدار `kind` همیشه ReplicaSet است.

هنگامی که control plane برای یک ReplicaSet، Podهای جدید ایجاد می‌کند، `.metadata.name` آن
ReplicaSet بخشی از مبنای نام‌گذاری آن Podها است. نام یک ReplicaSet باید یک مقدار معتبر
[زیردامنه DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names)
باشد، اما این ممکن است برای نام میزبان (hostname) Podها نتایج غیرمنتظره‌ای ایجاد کند. برای بهترین سازگاری،
نام باید از قواعد سخت‌گیرانه‌تر یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) پیروی کند.

یک ReplicaSet همچنین به یک [بخش `.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status) نیاز دارد.

### قالب Pod

`.spec.template` یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) است که
داشتن برچسب در آن نیز الزامی است. در مثال `frontend.yaml` ما یک برچسب داشتیم: `tier: frontend`.
مراقب باشید که با انتخابگرهای سایر کنترل‌کننده‌ها هم‌پوشانی نداشته باشد، مبادا آن‌ها تلاش کنند این Pod را به فرزندی بپذیرند.

برای فیلد [سیاست راه‌اندازی مجدد](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) قالب،
یعنی `.spec.template.spec.restartPolicy`، تنها مقدار مجاز `Always` است که مقدار پیش‌فرض نیز هست.

### انتخابگر Pod

فیلد `.spec.selector` یک [انتخابگر برچسب](/docs/concepts/overview/working-with-objects/labels/) است. همان‌طور که
[پیش‌تر](#how-a-replicaset-works) بحث شد، این‌ها برچسب‌هایی هستند که برای شناسایی Podهای بالقوه برای تصاحب استفاده می‌شوند. در
مثال `frontend.yaml` ما، انتخابگر چنین بود:

```yaml
matchLabels:
  tier: frontend
```

در ReplicaSet، `.spec.template.metadata.labels` باید با `spec.selector` مطابقت داشته باشد، در غیر این صورت
توسط API رد خواهد شد.

{{< note >}}
اگر 2 ReplicaSet، `.spec.selector` یکسان اما فیلدهای `.spec.template.metadata.labels` و
`.spec.template.spec` متفاوتی مشخص کنند، هر ReplicaSet Podهای
ایجادشده توسط ReplicaSet دیگر را نادیده می‌گیرد.
{{< /note >}}

### Replicaها

می‌توانید با تنظیم `.spec.replicas` مشخص کنید چند Pod باید به‌طور هم‌زمان اجرا شوند. ReplicaSet برای مطابقت با این عدد،
Podهای خود را ایجاد یا حذف می‌کند.

اگر `.spec.replicas` را مشخص نکنید، مقدار پیش‌فرض آن 1 است.

## کار با ReplicaSetها

### حذف یک ReplicaSet و Podهای آن

برای حذف یک ReplicaSet و همه Podهای آن، از
[`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands#delete) استفاده کنید.
[جمع‌آوری‌کننده زباله (Garbage collector)](/docs/concepts/architecture/garbage-collection/) به‌طور پیش‌فرض همه
Podهای وابسته را به‌طور خودکار حذف می‌کند.

هنگام استفاده از REST API یا کتابخانه `client-go`، باید `propagationPolicy` را در گزینه `-d` روی
`Background` یا `Foreground` تنظیم کنید. برای مثال:

```shell
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
  -H "Content-Type: application/json"
```

### حذف فقط یک ReplicaSet

می‌توانید یک ReplicaSet را بدون تأثیر بر هیچ‌یک از Podهای آن با استفاده از
[`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands#delete)
همراه با گزینه `--cascade=orphan` حذف کنید.
هنگام استفاده از REST API یا کتابخانه `client-go`، باید `propagationPolicy` را روی `Orphan` تنظیم کنید.
برای مثال:

```shell
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
  -H "Content-Type: application/json"
```

پس از حذف ReplicaSet اصلی، می‌توانید یک ReplicaSet جدید برای جایگزینی آن ایجاد کنید. تا زمانی که
`.spec.selector` قدیمی و جدید یکسان باشند، ReplicaSet جدید Podهای قدیمی را به فرزندی می‌پذیرد.
با این حال، هیچ تلاشی برای منطبق کردن Podهای موجود با یک قالب Pod جدید و متفاوت انجام نمی‌دهد.
برای به‌روزرسانی کنترل‌شده Podها به یک spec جدید، از یک
[Deployment](/docs/concepts/workloads/controllers/deployment/#creating-a-deployment) استفاده کنید، زیرا
ReplicaSetها به‌طور مستقیم از به‌روزرسانی غلتان (rolling update) پشتیبانی نمی‌کنند.

### Podهای در حال خاتمه

{{< feature-state feature_gate_name="DeploymentReplicaSetTerminatingReplicas" >}}

می‌توانید این قابلیت را با فعال کردن
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `DeploymentReplicaSetTerminatingReplicas`
روی [API server](/docs/reference/command-line-tools-reference/kube-apiserver/)
و روی [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) فعال کنید.

Podهایی که به دلیل حذف یا کاهش مقیاس در وضعیت خاتمه قرار می‌گیرند ممکن است خاتمه‌شان زمان زیادی طول بکشد و
در این مدت منابع بیشتری مصرف کنند. در نتیجه، تعداد کل Podها ممکن است به‌طور موقت از
`.spec.replicas` بیشتر شود. Podهای در حال خاتمه را می‌توان با استفاده از فیلد `.status.terminatingReplicas` در ReplicaSet ردیابی کرد.

### جدا کردن Podها از یک ReplicaSet

می‌توانید با تغییر برچسب‌های Podها، آن‌ها را از یک ReplicaSet جدا کنید. از این روش می‌توان برای خارج کردن Podها
از سرویس به منظور اشکال‌زدایی، بازیابی داده و موارد مشابه استفاده کرد. Podهایی که به این روش جدا می‌شوند به‌طور خودکار جایگزین خواهند شد
(با فرض اینکه تعداد replicaها نیز تغییر نکرده باشد).

### مقیاس‌دهی یک ReplicaSet

مقیاس یک ReplicaSet را می‌توان به‌سادگی و تنها با به‌روزرسانی فیلد `.spec.replicas` افزایش یا کاهش داد. کنترل‌کننده ReplicaSet
تضمین می‌کند که تعداد مطلوبی از Podهای دارای انتخابگر برچسب منطبق، در دسترس و عملیاتی باشند.

هنگام کاهش مقیاس، کنترل‌کننده ReplicaSet با مرتب‌سازی Podهای موجود، Podهایی را که باید حذف شوند انتخاب می‌کند تا
کاهش مقیاس Podها را بر اساس الگوریتم کلی زیر اولویت‌بندی کند:

1. Podهای Pending (و غیرقابل زمان‌بندی) ابتدا حذف می‌شوند.
1. اگر حاشیه‌نویسی `controller.kubernetes.io/pod-deletion-cost` تنظیم شده باشد،
   Podای که مقدار کمتری دارد زودتر می‌آید.
1. Podهای روی نودهایی با replicaهای بیشتر، پیش از Podهای روی نودهایی با replicaهای کمتر قرار می‌گیرند.
1. اگر زمان ایجاد Podها متفاوت باشد، Podای که جدیدتر ایجاد شده است
   پیش از Pod قدیمی‌تر قرار می‌گیرد (زمان‌های ایجاد روی یک مقیاس لگاریتمی صحیح دسته‌بندی می‌شوند).

اگر همه موارد بالا یکسان باشند، انتخاب به‌صورت تصادفی انجام می‌شود.

### هزینه حذف Pod

{{< feature-state for_k8s_version="v1.22" state="beta" >}}

با استفاده از حاشیه‌نویسی [`controller.kubernetes.io/pod-deletion-cost`](/docs/reference/labels-annotations-taints/#pod-deletion-cost)،
کاربران می‌توانند هنگام کاهش مقیاس یک ReplicaSet، ترجیح خود را درباره اینکه کدام Podها ابتدا حذف شوند تعیین کنند.

این حاشیه‌نویسی باید روی Pod تنظیم شود و بازه آن [-2147483648, 2147483647] است. این مقدار نشان‌دهنده هزینه
حذف یک Pod در مقایسه با سایر Podهای متعلق به همان ReplicaSet است. Podهایی که هزینه حذف کمتری دارند
ترجیحاً پیش از Podهایی با هزینه حذف بیشتر حذف می‌شوند.

مقدار ضمنی این حاشیه‌نویسی برای Podهایی که آن را تنظیم نکرده‌اند 0 است؛ مقادیر منفی مجاز هستند.
مقادیر نامعتبر توسط API server رد خواهند شد.

این قابلیت در مرحله بتا است و به‌طور پیش‌فرض فعال است. می‌توانید آن را با استفاده از
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
`PodDeletionCost` در هر دو kube-apiserver و kube-controller-manager غیرفعال کنید.

{{< note >}}
- این مورد بر اساس بهترین تلاش (best-effort) رعایت می‌شود، بنابراین هیچ تضمینی درباره ترتیب حذف Podها ارائه نمی‌دهد.
- کاربران باید از به‌روزرسانی مکرر این حاشیه‌نویسی، مانند به‌روزرسانی آن بر اساس مقدار یک متریک، خودداری کنند؛
  زیرا این کار تعداد قابل‌توجهی به‌روزرسانی Pod روی apiserver ایجاد می‌کند.
  {{< /note >}}

#### نمونه کاربرد

Podهای مختلف یک برنامه ممکن است سطوح بهره‌وری متفاوتی داشته باشند. هنگام کاهش مقیاس، برنامه
ممکن است ترجیح دهد Podهایی را که بهره‌وری کمتری دارند حذف کند. برای جلوگیری از به‌روزرسانی مکرر Podها، برنامه
باید `controller.kubernetes.io/pod-deletion-cost` را یک بار پیش از صدور فرمان کاهش مقیاس به‌روزرسانی کند (با تنظیم
حاشیه‌نویسی روی مقداری متناسب با سطح بهره‌وری Pod). این روش زمانی کار می‌کند که خود برنامه کاهش مقیاس را
کنترل کند؛ برای مثال، Pod درایور (driver) در یک استقرار Spark.

### ReplicaSet به‌عنوان هدف Horizontal Pod Autoscaler

یک ReplicaSet همچنین می‌تواند هدف
[Horizontal Pod Autoscalerها (HPA)](/docs/tasks/run-application/horizontal-pod-autoscale/) باشد. یعنی
مقیاس یک ReplicaSet می‌تواند توسط یک HPA به‌طور خودکار تنظیم شود. در اینجا نمونه‌ای از یک HPA آمده است که
ReplicaSetای را که در مثال قبلی ایجاد کردیم هدف قرار می‌دهد.

{{% code_sample file="controllers/hpa-rs.yaml" %}}

ذخیره این مانیفست در `hpa-rs.yaml` و ارسال آن به یک کلاستر کوبرنتیز باید
HPA تعریف‌شده را ایجاد کند که مقیاس ReplicaSet هدف را بسته به میزان مصرف CPU
Podهای تکثیرشده به‌طور خودکار تنظیم می‌کند.

```shell
kubectl apply -f https://k8s.io/examples/controllers/hpa-rs.yaml
```

به‌عنوان جایگزین، می‌توانید از فرمان `kubectl autoscale` برای انجام همین کار استفاده کنید
(و این روش ساده‌تر است!)

```shell
kubectl autoscale rs frontend --max=10 --min=3 --cpu=50%
```

## جایگزین‌های ReplicaSet

### Deployment (توصیه‌شده)

[`Deployment`](/docs/concepts/workloads/controllers/deployment/) آبجکتی است که می‌تواند مالک ReplicaSetها باشد و آن‌ها
و Podهایشان را از طریق به‌روزرسانی‌های غلتان اعلانی و سمت سرور به‌روزرسانی کند.
اگرچه ReplicaSetها را می‌توان به‌طور مستقل استفاده کرد، امروزه عمدتاً توسط Deploymentها به‌عنوان سازوکاری برای هماهنگ‌سازی
ایجاد، حذف و به‌روزرسانی Podها به کار می‌روند. هنگامی که از Deploymentها استفاده می‌کنید، لازم نیست نگران مدیریت ReplicaSetهایی باشید که
ایجاد می‌کنند. Deploymentها مالک ReplicaSetهای خود هستند و آن‌ها را مدیریت می‌کنند.
از این رو، هنگامی که به ReplicaSet نیاز دارید، استفاده از Deploymentها توصیه می‌شود.

### Podهای مستقل (Bare Pods)

برخلاف حالتی که کاربر مستقیماً Podها را ایجاد کرده است، یک ReplicaSet Podهایی را که به هر دلیلی حذف شده یا
خاتمه یافته‌اند جایگزین می‌کند؛ برای مثال در صورت خرابی نود یا نگهداری مخرب نود،
مانند ارتقای کرنل. به همین دلیل، توصیه می‌کنیم حتی اگر برنامه شما تنها به یک Pod نیاز دارد،
از یک ReplicaSet استفاده کنید. آن را مشابه یک ناظر فرایند (process supervisor) در نظر بگیرید، با این تفاوت که
به‌جای فرایندهای منفرد روی یک نود، چندین Pod را در چندین نود نظارت می‌کند. یک
ReplicaSet راه‌اندازی مجدد کانتینرهای محلی را به عاملی روی نود، مانند Kubelet، واگذار می‌کند.

### Job

برای Podهایی که انتظار می‌رود خودشان خاتمه یابند (یعنی کارهای دسته‌ای یا batch jobs)، به‌جای ReplicaSet از یک
[`Job`](/docs/concepts/workloads/controllers/job/) استفاده کنید.

### DaemonSet

برای Podهایی که یک عملکرد در سطح ماشین ارائه می‌دهند، مانند پایش ماشین یا ثبت لاگ ماشین، به‌جای ReplicaSet از یک
[`DaemonSet`](/docs/concepts/workloads/controllers/daemonset/) استفاده کنید. طول عمر این Podها به طول عمر
ماشین گره خورده است: Pod باید پیش از شروع سایر Podها روی ماشین در حال اجرا باشد و
خاتمه دادن به آن زمانی که ماشین برای راه‌اندازی مجدد یا خاموش شدن آماده است، بی‌خطر است.

### ReplicationController

ReplicaSetها جانشینان [ReplicationControllerها](/docs/concepts/workloads/controllers/replicationcontroller/) هستند.
این دو هدف یکسانی دارند و رفتار مشابهی نشان می‌دهند، با این تفاوت که ReplicationController از الزامات انتخابگر
مبتنی بر مجموعه (set-based)، آن‌طور که در [راهنمای کاربر برچسب‌ها](/docs/concepts/overview/working-with-objects/labels/#label-selectors) توضیح داده شده است، پشتیبانی نمی‌کند.
از این رو، ReplicaSetها بر ReplicationControllerها ترجیح داده می‌شوند.

## {{% heading "whatsnext" %}}

* درباره [Podها](/docs/concepts/workloads/pods) بیاموزید.
* درباره [Deploymentها](/docs/concepts/workloads/controllers/deployment/) بیاموزید.
* [اجرای یک برنامه بدون حالت با استفاده از Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
  که برای کارکرد خود به ReplicaSetها متکی است.
* `ReplicaSet` یک منبع سطح بالا در REST API کوبرنتیز است.
  تعریف آبجکت {{< api-reference page="apps/replica-set-v1" >}}
  را بخوانید تا API مربوط به replica setها را درک کنید.
* درباره [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) و اینکه چگونه
  می‌توانید از آن برای مدیریت در دسترس بودن برنامه در هنگام اختلال‌ها استفاده کنید، مطالعه کنید.

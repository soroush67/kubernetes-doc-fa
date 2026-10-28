---
title: ابزار خط فرمان (kubectl)
content_type: reference
weight: 110
no_list: true
card:
  name: reference
  title: ابزار خط فرمان kubectl
  weight: 20
---

<!-- overview -->
{{< glossary_definition prepend="کوبرنتیز یک" term_id="kubectl" length="short" >}}

نام این ابزار `kubectl` است.

برای پیکربندی، `kubectl` به دنبال فایلی با نام `config` در مسیر `$HOME/.kube` می‌گردد.
می‌توانید فایل‌های [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) دیگری را
با تنظیم متغیر محیطی `KUBECONFIG` یا با تنظیم فلگ
[`--kubeconfig`](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) مشخص کنید.

این مرور کلی، نحو (syntax) دستور `kubectl` را پوشش می‌دهد، عملیات دستورها را توضیح می‌دهد و مثال‌های رایج ارائه می‌کند.
برای جزئیات هر دستور، شامل تمام فلگ‌ها و زیردستورهای پشتیبانی‌شده، به مستندات مرجع
[kubectl](/docs/reference/kubectl/generated/kubectl/) مراجعه کنید.

برای مرور کلی، [ابزار خط فرمان kubectl](/docs/concepts/overview/kubectl/) را ببینید.
برای دستورالعمل‌های نصب، [نصب kubectl](/docs/tasks/tools/#kubectl) را ببینید؛
برای یک راهنمای سریع، [برگه تقلب (cheat sheet)](/docs/reference/kubectl/quick-reference/) را ببینید.
اگر به استفاده از ابزار خط فرمان `docker` عادت دارید،
[`kubectl` برای کاربران Docker](/docs/reference/kubectl/docker-cli-to-kubectl/) برخی دستورهای معادل در کوبرنتیز را توضیح می‌دهد.

<!-- body -->

## نحو (Syntax) {#syntax}

برای اجرای دستورهای `kubectl` از پنجره ترمینال خود، از نحو زیر استفاده کنید:

```shell
kubectl [command] [TYPE] [NAME] [flags]
```

که در آن `command`، `TYPE`، `NAME` و `flags` عبارت‌اند از:

* `command`: عملیاتی را که می‌خواهید روی یک یا چند منبع انجام دهید مشخص می‌کند،
  برای مثال `create`، `get`، `describe`، `delete`.

* `TYPE`: [نوع منبع](#resource-types) را مشخص می‌کند. نوع‌های منبع به حروف بزرگ و کوچک حساس نیستند و
  می‌توانید شکل مفرد، جمع یا مخفف آن‌ها را به کار ببرید.
  برای مثال، دستورهای زیر خروجی یکسانی تولید می‌کنند:

  ```shell
  kubectl get pod pod1
  kubectl get pods pod1
  kubectl get po pod1
  ```

* `NAME`: نام منبع را مشخص می‌کند. نام‌ها به حروف بزرگ و کوچک حساس هستند. اگر نام حذف شود،
  جزئیات تمام منابع نمایش داده می‌شود، برای مثال `kubectl get pods`.

  هنگام انجام یک عملیات روی چند منبع، می‌توانید هر منبع را با
  نوع و نام آن مشخص کنید یا یک یا چند فایل را مشخص نمایید:

  * برای مشخص کردن منابع با نوع و نام:

    * برای گروه‌بندی منابع در صورتی که همگی از یک نوع باشند:  `TYPE1 name1 name2 name<#>`.<br/>
      مثال: `kubectl get pod example-pod1 example-pod2`

    * برای مشخص کردن جداگانه چند نوع منبع:  `TYPE1/name1 TYPE1/name2 TYPE2/name3 TYPE<#>/name<#>`.<br/>
      مثال: `kubectl get pod/example-pod1 replicationcontroller/example-rc1`

  * برای مشخص کردن منابع با یک یا چند فایل:  `-f file1 -f file2 -f file<#>`

    * به جای JSON از YAML استفاده کنید،
      زیرا YAML معمولاً کاربرپسندتر است، به‌ویژه برای فایل‌های پیکربندی.<br/>
      مثال: `kubectl get -f ./pod.yaml`

* `flags`: فلگ‌های اختیاری را مشخص می‌کند. برای مثال، می‌توانید از فلگ‌های `-s` یا `--server`
  برای مشخص کردن نشانی و پورت سرور API کوبرنتیز استفاده کنید.<br/>

{{< caution >}}
فلگ‌هایی که از خط فرمان مشخص می‌کنید، مقادیر پیش‌فرض و هر متغیر محیطی متناظر را بازنویسی (override) می‌کنند.
{{< /caution >}}

اگر به کمک نیاز دارید، دستور `kubectl help` را در پنجره ترمینال اجرا کنید.

## احراز هویت درون کلاستر و بازنویسی فضای نام {#in-cluster-authentication-and-namespace-overrides}

به‌طور پیش‌فرض `kubectl` ابتدا تشخیص می‌دهد که آیا درون یک Pod و در نتیجه درون یک کلاستر در حال اجراست یا خیر.
این کار را با بررسی متغیرهای محیطی `KUBERNETES_SERVICE_HOST` و `KUBERNETES_SERVICE_PORT`
و وجود یک فایل توکن service account در مسیر `/var/run/secrets/kubernetes.io/serviceaccount/token` آغاز می‌کند.
اگر هر سه مورد یافت شوند، فرض بر احراز هویت درون کلاستر است.

برای حفظ سازگاری با نسخه‌های قبلی، اگر متغیر محیطی `POD_NAMESPACE` در هنگام
احراز هویت درون کلاستر تنظیم شده باشد، فضای نام پیش‌فرض برگرفته از توکن
service account را بازنویسی می‌کند. هر مانیفست یا ابزاری که به فضای نام پیش‌فرض متکی باشد از این موضوع تأثیر می‌پذیرد.

**متغیر محیطی `POD_NAMESPACE`**

اگر متغیر محیطی `POD_NAMESPACE` تنظیم شده باشد، عملیات خط فرمان روی منابع دارای فضای نام
به‌طور پیش‌فرض از مقدار این متغیر استفاده می‌کنند. برای مثال، اگر مقدار متغیر `seattle` باشد،
دستور `kubectl get pods`، Podهای فضای نام `seattle` را برمی‌گرداند. دلیل این است که Podها
منبعی دارای فضای نام هستند و در دستور هیچ فضای نامی مشخص نشده است. برای تعیین اینکه یک منبع دارای فضای نام است یا خیر،
خروجی `kubectl api-resources` را بررسی کنید.

استفاده صریح از `--namespace <value>` این رفتار را بازنویسی می‌کند.

**نحوه برخورد kubectl با توکن‌های ServiceAccount**

اگر:

* یک فایل توکن service account کوبرنتیز در مسیر
  `/var/run/secrets/kubernetes.io/serviceaccount/token` mount شده باشد، و
* متغیر محیطی `KUBERNETES_SERVICE_HOST` تنظیم شده باشد، و
* متغیر محیطی `KUBERNETES_SERVICE_PORT` تنظیم شده باشد، و
* در خط فرمان kubectl صراحتاً فضای نامی مشخص نکرده باشید،

آنگاه kubectl فرض می‌کند که درون کلاستر شما در حال اجراست. ابزار kubectl
فضای نام آن ServiceAccount را (که با فضای نام Pod یکسان است) پیدا می‌کند
و روی آن فضای نام عمل می‌کند. این با آنچه خارج از یک
کلاستر رخ می‌دهد متفاوت است؛ وقتی kubectl خارج از کلاستر اجرا می‌شود و فضای نامی مشخص نمی‌کنید،
دستور kubectl روی فضای نام تنظیم‌شده برای context فعلی در
پیکربندی کلاینت شما عمل می‌کند. برای تغییر فضای نام پیش‌فرض kubectl می‌توانید از
دستور زیر استفاده کنید:

```shell
kubectl config set-context --current --namespace=<namespace-name>
```

## عملیات {#operations}

جدول زیر شامل توضیحات کوتاه و نحو کلی تمام عملیات `kubectl` است:

Operation       | Syntax    |       Description
-------------------- | -------------------- | --------------------
`alpha`    | `kubectl alpha SUBCOMMAND [flags]` | دستورهای موجود مربوط به قابلیت‌های آلفا را فهرست می‌کند؛ این قابلیت‌ها به‌طور پیش‌فرض در کلاسترهای کوبرنتیز فعال نیستند.
`annotate`    | <code>kubectl annotate (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]</code> | حاشیه‌نویسی‌های (annotation) یک یا چند منبع را اضافه یا به‌روزرسانی می‌کند.
`api-resources`    | `kubectl api-resources [flags]` | منابع API موجود را فهرست می‌کند.
`api-versions`    | `kubectl api-versions [flags]` | نسخه‌های API موجود را فهرست می‌کند.
`apply`            | `kubectl apply -f FILENAME [flags]`| یک تغییر پیکربندی را از یک فایل یا stdin روی یک منبع اعمال می‌کند.
`attach`        | `kubectl attach POD -c CONTAINER [-i] [-t] [flags]` | به یک کانتینر در حال اجرا متصل می‌شود تا جریان خروجی را مشاهده کند یا با کانتینر (stdin) تعامل داشته باشد.
`auth`    | `kubectl auth [flags] [options]` | مجوزدهی (authorization) را بررسی می‌کند.
`autoscale`    | <code>kubectl autoscale (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu=CPU] [flags]</code> | مجموعه Podهایی را که توسط یک replication controller مدیریت می‌شوند به‌طور خودکار مقیاس می‌دهد.
`certificate`    | `kubectl certificate SUBCOMMAND [options]` | منابع گواهی (certificate) را تغییر می‌دهد.
`cluster-info`    | `kubectl cluster-info [flags]` | اطلاعات نقطه پایانی (endpoint) مربوط به master و سرویس‌های کلاستر را نمایش می‌دهد.
`completion`    | `kubectl completion SHELL [options]` | کد تکمیل خودکار shell را برای shell مشخص‌شده (bash یا zsh) خروجی می‌دهد.
`config`        | `kubectl config SUBCOMMAND [flags]` | فایل‌های kubeconfig را تغییر می‌دهد. برای جزئیات، زیردستورهای مربوطه را ببینید.
`convert`    | `kubectl convert -f FILENAME [options]` | فایل‌های پیکربندی را بین نسخه‌های مختلف API تبدیل می‌کند. هر دو قالب YAML و JSON پذیرفته می‌شوند. توجه - نیازمند نصب افزونه `kubectl-convert` است.
`cordon`    | `kubectl cordon NODE [options]` | نود را به‌عنوان غیرقابل زمان‌بندی علامت‌گذاری می‌کند.
`cp`    | `kubectl cp <file-spec-src> <file-spec-dest> [options]` | فایل‌ها و دایرکتوری‌ها را از/به کانتینرها کپی می‌کند.
`create`        | `kubectl create -f FILENAME [flags]` | یک یا چند منبع را از یک فایل یا stdin ایجاد می‌کند.
`delete`        | <code>kubectl delete (-f FILENAME &#124; TYPE [NAME &#124; /NAME &#124; -l label &#124; --all]) [flags]</code> | منابع را از یک فایل یا stdin حذف می‌کند، یا با مشخص کردن انتخابگرهای برچسب، نام‌ها، انتخابگرهای منبع یا منابع.
`describe`    | <code>kubectl describe (-f FILENAME &#124; TYPE [NAME_PREFIX &#124; /NAME &#124; -l label]) [flags]</code> | وضعیت تفصیلی یک یا چند منبع را نمایش می‌دهد.
`diff`        | `kubectl diff -f FILENAME [flags]`| فایل یا stdin را با پیکربندی زنده مقایسه می‌کند و تفاوت‌ها را نشان می‌دهد.
`drain`    | `kubectl drain NODE [options]` | نود را برای آماده‌سازی جهت نگهداری تخلیه (drain) می‌کند.
`edit`        | <code>kubectl edit (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [flags]</code> | تعریف یک یا چند منبع را روی سرور با استفاده از ویرایشگر پیش‌فرض ویرایش و به‌روزرسانی می‌کند.
`events`      | `kubectl events` | رویدادها (events) را فهرست می‌کند.
`exec`        | `kubectl exec POD [-c CONTAINER] [-i] [-t] [flags] [-- COMMAND [args...]]` | یک دستور را روی یک کانتینر در یک Pod اجرا می‌کند.
`explain`    | `kubectl explain TYPE [--recursive=false] [flags]` | مستندات منابع مختلف را دریافت می‌کند. برای مثال Podها، نودها، سرویس‌ها و غیره.
`expose`        | <code>kubectl expose (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [--port=port] [--protocol=TCP&#124;UDP] [--target-port=number-or-name] [--name=name] [--external-ip=external-ip-of-service] [--type=type] [flags]</code> | یک replication controller، سرویس یا Pod را به‌صورت یک Service جدید کوبرنتیز در دسترس قرار می‌دهد.
`get`        | <code>kubectl get (-f FILENAME &#124; TYPE [NAME &#124; /NAME &#124; -l label]) [--watch] [--sort-by=FIELD] [[-o &#124; --output]=OUTPUT_FORMAT] [flags]</code> | یک یا چند منبع را فهرست می‌کند.
`kustomize`    | `kubectl kustomize <dir> [flags] [options]` | مجموعه‌ای از منابع API را که از دستورالعمل‌های موجود در یک فایل kustomization.yaml تولید شده‌اند فهرست می‌کند. آرگومان باید مسیر دایرکتوری حاوی فایل باشد، یا نشانی یک مخزن git همراه با پسوند مسیر که همان را نسبت به ریشه مخزن مشخص می‌کند.
`label`        | <code>kubectl label (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]</code> | برچسب‌های یک یا چند منبع را اضافه یا به‌روزرسانی می‌کند.
`logs`        | `kubectl logs POD [-c CONTAINER] [--follow] [flags]` | لاگ‌های یک کانتینر در یک Pod را چاپ می‌کند.
`options`    | `kubectl options` | فهرست گزینه‌های سراسری خط فرمان را نمایش می‌دهد که برای تمام دستورها اعمال می‌شوند.
`patch`        | <code>kubectl patch (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) --patch PATCH [flags]</code> | یک یا چند فیلد از یک منبع را با استفاده از فرایند strategic merge patch به‌روزرسانی می‌کند.
`plugin`    | `kubectl plugin [flags] [options]` | ابزارهایی برای تعامل با افزونه‌ها (plugins) فراهم می‌کند.
`port-forward`    | `kubectl port-forward POD [LOCAL_PORT:]REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N] [flags]` | یک یا چند پورت محلی را به یک Pod هدایت (forward) می‌کند.
`proxy`        | `kubectl proxy [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [--api-prefix=prefix] [flags]` | یک پراکسی به سرور API کوبرنتیز اجرا می‌کند.
`replace`        | `kubectl replace -f FILENAME` | یک منبع را از یک فایل یا stdin جایگزین می‌کند.
`rollout`    | `kubectl rollout SUBCOMMAND [options]` | عرضه تدریجی (rollout) یک منبع را مدیریت می‌کند. نوع‌های منبع معتبر عبارت‌اند از: deployments، daemonsets و statefulsets.
`run`        | <code>kubectl run NAME --image=image [--env="key=value"] [--port=port] [--dry-run=server&#124;client&#124;none] [--overrides=inline-json] [flags]</code> | یک ایمیج مشخص‌شده را روی کلاستر اجرا می‌کند.
`scale`        | <code>kubectl scale (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) --replicas=COUNT [--resource-version=version] [--current-replicas=count] [flags]</code> | اندازه replication controller مشخص‌شده را به‌روزرسانی می‌کند.
`set`    | `kubectl set SUBCOMMAND [options]` | منابع برنامه کاربردی را پیکربندی می‌کند.
`taint`    | `kubectl taint NODE NAME KEY_1=VAL_1:TAINT_EFFECT_1 ... KEY_N=VAL_N:TAINT_EFFECT_N [options]` | taintهای یک یا چند نود را به‌روزرسانی می‌کند.
`top`    | <code>kubectl top (POD &#124; NODE) [flags] [options]</code> | میزان مصرف منابع (CPU/حافظه/ذخیره‌سازی) یک Pod یا نود را نمایش می‌دهد.
`uncordon`    | `kubectl uncordon NODE [options]` | نود را به‌عنوان قابل زمان‌بندی علامت‌گذاری می‌کند.
`version`        | `kubectl version [--client] [flags]` | نسخه کوبرنتیز در حال اجرا روی کلاینت و سرور را نمایش می‌دهد.
`wait`    | <code>kubectl wait ([-f FILENAME] &#124; resource.group/resource.name &#124; resource.group [(-l label &#124; --all)]) [--for=delete&#124;--for condition=available] [options]</code> | آزمایشی: منتظر یک شرط مشخص روی یک یا چند منبع می‌ماند.

برای کسب اطلاعات بیشتر درباره عملیات دستورها، مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) را ببینید.

## انواع منبع {#resource-types}

جدول زیر شامل فهرستی از تمام انواع منبع پشتیبانی‌شده و نام‌های مستعار مخفف آن‌هاست.

(این خروجی را می‌توان از `kubectl api-resources` دریافت کرد و در زمان کوبرنتیز 1.25.0 دقیق بود)

| NAME | SHORTNAMES | APIVERSION | NAMESPACED | KIND |
|---|---|---|---|---|
| `bindings` |  | v1 | true | Binding |
| `componentstatuses` | `cs` | v1 | false | ComponentStatus |
| `configmaps` | `cm` | v1 | true | ConfigMap |
| `endpoints` | `ep` | v1 | true | Endpoints |
| `events` | `ev` | v1 | true | Event |
| `limitranges` | `limits` | v1 | true | LimitRange |
| `namespaces` | `ns` | v1 | false | Namespace |
| `nodes` | `no` | v1 | false | Node |
| `persistentvolumeclaims` | `pvc` | v1 | true | PersistentVolumeClaim |
| `persistentvolumes` | `pv` | v1 | false | PersistentVolume |
| `pods` | `po` | v1 | true | Pod |
| `podtemplates` |  | v1 | true | PodTemplate |
| `replicationcontrollers` | `rc` | v1 | true | ReplicationController |
| `resourcequotas` | `quota` | v1 | true | ResourceQuota |
| `secrets` |  | v1 | true | Secret |
| `serviceaccounts` | `sa` | v1 | true | ServiceAccount |
| `services` | `svc` | v1 | true | Service |
| `mutatingwebhookconfigurations` |  | admissionregistration.k8s.io/v1 | false | MutatingWebhookConfiguration |
| `validatingwebhookconfigurations` |  | admissionregistration.k8s.io/v1 | false | ValidatingWebhookConfiguration |
| `customresourcedefinitions` | `crd,crds` | apiextensions.k8s.io/v1 | false | CustomResourceDefinition |
| `apiservices` |  | apiregistration.k8s.io/v1 | false | APIService |
| `controllerrevisions` |  | apps/v1 | true | ControllerRevision |
| `daemonsets` | `ds` | apps/v1 | true | DaemonSet |
| `deployments` | `deploy` | apps/v1 | true | Deployment |
| `replicasets` | `rs` | apps/v1 | true | ReplicaSet |
| `statefulsets` | `sts` | apps/v1 | true | StatefulSet |
| `tokenreviews` |  | authentication.k8s.io/v1 | false | TokenReview |
| `localsubjectaccessreviews` |  | authorization.k8s.io/v1 | true | LocalSubjectAccessReview |
| `selfsubjectaccessreviews` |  | authorization.k8s.io/v1 | false | SelfSubjectAccessReview |
| `selfsubjectrulesreviews` |  | authorization.k8s.io/v1 | false | SelfSubjectRulesReview |
| `subjectaccessreviews` |  | authorization.k8s.io/v1 | false | SubjectAccessReview |
| `horizontalpodautoscalers` | `hpa` | autoscaling/v2 | true | HorizontalPodAutoscaler |
| `cronjobs` | `cj` | batch/v1 | true | CronJob |
| `jobs` |  | batch/v1 | true | Job |
| `certificatesigningrequests` | `csr` | certificates.k8s.io/v1 | false | CertificateSigningRequest |
| `leases` |  | coordination.k8s.io/v1 | true | Lease |
| `endpointslices` |  | discovery.k8s.io/v1 | true | EndpointSlice |
| `events` | `ev` | events.k8s.io/v1 | true | Event |
| `flowschemas` |  | flowcontrol.apiserver.k8s.io/v1beta2 | false | FlowSchema |
| `prioritylevelconfigurations` |  | flowcontrol.apiserver.k8s.io/v1beta2 | false | PriorityLevelConfiguration |
| `ingressclasses` |  | networking.k8s.io/v1 | false | IngressClass |
| `ingresses` | `ing` | networking.k8s.io/v1 | true | Ingress |
| `networkpolicies` | `netpol` | networking.k8s.io/v1 | true | NetworkPolicy |
| `runtimeclasses` |  | node.k8s.io/v1 | false | RuntimeClass |
| `poddisruptionbudgets` | `pdb` | policy/v1 | true | PodDisruptionBudget |
| `podsecuritypolicies` | `psp` | policy/v1beta1 | false | PodSecurityPolicy |
| `clusterrolebindings` |  | rbac.authorization.k8s.io/v1 | false | ClusterRoleBinding |
| `clusterroles` |  | rbac.authorization.k8s.io/v1 | false | ClusterRole |
| `rolebindings` |  | rbac.authorization.k8s.io/v1 | true | RoleBinding |
| `roles` |  | rbac.authorization.k8s.io/v1 | true | Role |
| `priorityclasses` | `pc` | scheduling.k8s.io/v1 | false | PriorityClass |
| `csidrivers` |  | storage.k8s.io/v1 | false | CSIDriver |
| `csinodes` |  | storage.k8s.io/v1 | false | CSINode |
| `csistoragecapacities` |  | storage.k8s.io/v1 | true | CSIStorageCapacity |
| `storageclasses` | `sc` | storage.k8s.io/v1 | false | StorageClass |
| `volumeattachments` |  | storage.k8s.io/v1 | false | VolumeAttachment |

## گزینه‌های خروجی {#output-options}

از بخش‌های زیر برای کسب اطلاعات درباره نحوه قالب‌بندی یا مرتب‌سازی خروجی
برخی دستورها استفاده کنید. برای جزئیات اینکه کدام دستورها از گزینه‌های مختلف خروجی پشتیبانی می‌کنند،
مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) را ببینید.

### قالب‌بندی خروجی {#formatting-output}

قالب پیش‌فرض خروجی تمام دستورهای `kubectl`، قالب متن ساده قابل‌خواندن برای انسان است.
برای نمایش جزئیات در پنجره ترمینال با یک قالب مشخص، می‌توانید فلگ `-o`
یا `--output` را به یک دستور `kubectl` پشتیبانی‌شده اضافه کنید.

#### نحو (Syntax) {#syntax-1}

```shell
kubectl [command] [TYPE] [NAME] -o <output_format>
```

بسته به عملیات `kubectl`، قالب‌های خروجی زیر پشتیبانی می‌شوند:

Output format | Description
--------------| -----------
`-o custom-columns=<spec>` | یک جدول را با استفاده از فهرست جداشده با کاما از [ستون‌های سفارشی](#custom-columns) چاپ می‌کند.
`-o custom-columns-file=<filename>` | یک جدول را با استفاده از قالب [ستون‌های سفارشی](#custom-columns) موجود در فایل `<filename>` چاپ می‌کند.
`-o json`     | یک آبجکت API با قالب JSON را خروجی می‌دهد.
`-o jsonpath=<template>` | فیلدهای تعریف‌شده در یک عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) را چاپ می‌کند.
`-o jsonpath-file=<filename>` | فیلدهای تعریف‌شده توسط عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) موجود در فایل `<filename>` را چاپ می‌کند.
`-o kyaml`    | یک آبجکت API با قالب [KYAML](/docs/reference/encodings/kyaml/) را خروجی می‌دهد.
`-o name`     | فقط نام منبع را چاپ می‌کند و چیز دیگری چاپ نمی‌کند.
`-o wide`     | خروجی را با قالب متن ساده همراه با اطلاعات اضافی نمایش می‌دهد. برای Podها، نام نود نیز درج می‌شود.
`-o yaml`     | یک آبجکت API با قالب YAML را خروجی می‌دهد. KYAML گونه‌ای از YAML مختص کوبرنتیز است و می‌توان آن را به‌عنوان YAML تجزیه (parse) کرد.

##### مثال {#example}

در این مثال، دستور زیر جزئیات یک Pod را به‌صورت یک آبجکت با قالب YAML خروجی می‌دهد:

```shell
kubectl get pod web-pod-13je7 -o yaml
```

به یاد داشته باشید: برای جزئیات اینکه هر دستور از کدام قالب خروجی پشتیبانی می‌کند،
مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) را ببینید.

#### ستون‌های سفارشی {#custom-columns}

برای تعریف ستون‌های سفارشی و خروجی گرفتن فقط از جزئیات موردنظر خود در یک جدول، می‌توانید از گزینه `custom-columns` استفاده کنید.
می‌توانید ستون‌های سفارشی را به‌صورت درون‌خطی (inline) تعریف کنید یا از یک فایل قالب استفاده کنید: `-o custom-columns=<spec>` یا `-o custom-columns-file=<filename>`.

##### مثال‌ها {#examples}

درون‌خطی:

```shell
kubectl get pods <pod-name> -o custom-columns=NAME:.metadata.name,RSRC:.metadata.resourceVersion
```

فایل قالب:

```shell
kubectl get pods <pod-name> -o custom-columns-file=template.txt
```

که در آن فایل `template.txt` شامل موارد زیر است:

```
NAME          RSRC
metadata.name metadata.resourceVersion
```
نتیجه اجرای هر یک از این دو دستور مشابه زیر است:

```
NAME           RSRC
submit-queue   610995
```

#### ستون‌های سمت سرور {#server-side-columns}

`kubectl` از دریافت اطلاعات ستون‌های مشخص درباره آبجکت‌ها از سرور پشتیبانی می‌کند.
این بدان معناست که برای هر منبع مشخص، سرور ستون‌ها و ردیف‌های مرتبط با آن منبع را برمی‌گرداند تا کلاینت آن‌ها را چاپ کند.
این کار با آنکه سرور جزئیات چاپ را کپسوله می‌کند، امکان خروجی یکدست و قابل‌خواندن برای انسان را در کلاینت‌های مختلفی که روی یک کلاستر استفاده می‌شوند فراهم می‌کند.

این قابلیت به‌طور پیش‌فرض فعال است. برای غیرفعال کردن آن، فلگ
`--server-print=false` را به دستور `kubectl get` اضافه کنید.

##### مثال‌ها {#examples-1}

برای چاپ اطلاعات مربوط به وضعیت یک Pod، از دستوری مانند دستور زیر استفاده کنید:

```shell
kubectl get pods <pod-name> --server-print=false
```

خروجی مشابه زیر است:

```
NAME       AGE
pod-name   1m
```

### مرتب‌سازی آبجکت‌های فهرست

برای نمایش آبجکت‌ها به‌صورت یک فهرست مرتب‌شده در پنجرهٔ ترمینال، می‌توانید فلگ `--sort-by` را به یکی از دستورهای پشتیبانی‌شدهٔ `kubectl` اضافه کنید. آبجکت‌های خود را با تعیین هر فیلد عددی یا رشته‌ای توسط فلگ `--sort-by` مرتب کنید. برای تعیین فیلد، از یک عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) استفاده کنید.

#### نحو

```shell
kubectl [command] [TYPE] [NAME] --sort-by=<jsonpath_exp>
```

##### مثال

برای چاپ فهرستی از Podها که بر اساس نام مرتب شده‌اند، دستور زیر را اجرا کنید:

```shell
kubectl get pods --sort-by=.metadata.name
```

## مثال‌ها: عملیات رایج

از مجموعه مثال‌های زیر برای آشنایی با اجرای عملیات پرکاربرد `kubectl` استفاده کنید:

`kubectl apply` - اعمال یا به‌روزرسانی یک منبع از یک فایل یا stdin.

```shell
# Create a service using the definition in example-service.yaml.
kubectl apply -f example-service.yaml

# Create a replication controller using the definition in example-controller.yaml.
kubectl apply -f example-controller.yaml

# Create the objects that are defined in any .yaml, .yml, or .json file within the <directory> directory.
kubectl apply -f <directory>
```

`kubectl get` - فهرست‌کردن یک یا چند منبع.

```shell
# List all pods in plain-text output format.
kubectl get pods

# List all pods in plain-text output format and include additional information (such as node name).
kubectl get pods -o wide

# List the replication controller with the specified name in plain-text output format. Tip: You can shorten and replace the 'replicationcontroller' resource type with the alias 'rc'.
kubectl get replicationcontroller <rc-name>

# List all replication controllers and services together in plain-text output format.
kubectl get rc,services

# List all daemon sets in plain-text output format.
kubectl get ds

# List all pods running on node server01
kubectl get pods --field-selector=spec.nodeName=server01
```

`kubectl describe` - نمایش وضعیت تفصیلی یک یا چند منبع، که به‌طور پیش‌فرض منابع مقداردهی‌نشده (uninitialized) را نیز شامل می‌شود.

```shell
# Display the details of the node with name <node-name>.
kubectl describe nodes <node-name>

# Display the details of the pod with name <pod-name>.
kubectl describe pods/<pod-name>

# Display the details of all the pods that are managed by the replication controller named <rc-name>.
# Remember: Any pods that are created by the replication controller get prefixed with the name of the replication controller.
kubectl describe pods <rc-name>

# Describe all pods
kubectl describe pods
```

{{< note >}}
دستور `kubectl get` معمولاً برای بازیابی یک یا چند منبع از یک نوع منبع به کار می‌رود. این دستور مجموعه‌ای غنی از فلگ‌ها دارد که برای مثال به شما امکان می‌دهد قالب خروجی را با فلگ `-o` یا `--output` سفارشی کنید.
می‌توانید با تعیین فلگ `-w` یا `--watch`، پایش به‌روزرسانی‌های یک آبجکت مشخص را آغاز کنید. دستور `kubectl describe` بیشتر بر توصیف جنبه‌های مرتبط و متعدد یک منبع مشخص تمرکز دارد. این دستور ممکن است برای ساخت یک نمای کامل برای کاربر، چندین فراخوانی API به API server انجام دهد. برای مثال، دستور `kubectl describe node` نه‌تنها اطلاعات مربوط به نود، بلکه خلاصه‌ای از Podهای در حال اجرا روی آن، رویدادهای تولیدشده برای نود و موارد مشابه را نیز بازیابی می‌کند.
{{< /note >}}

`kubectl delete` - حذف منابع از یک فایل یا stdin، یا با تعیین انتخابگرهای برچسب (label selector)، نام‌ها، انتخابگرهای منبع یا خود منابع.

```shell
# Delete a pod using the type and name specified in the pod.yaml file.
kubectl delete -f pod.yaml

# Delete all the pods and services that have the label '<label-key>=<label-value>'.
kubectl delete pods,services -l <label-key>=<label-value>

# Delete all pods, including uninitialized ones.
kubectl delete pods --all
```

`kubectl exec` - اجرای یک دستور در یک کانتینر درون یک Pod.

```shell
# Get output from running 'date' from pod <pod-name>. By default, output is from the first container.
kubectl exec <pod-name> -- date

# Get output from running 'date' in container <container-name> of pod <pod-name>.
kubectl exec <pod-name> -c <container-name> -- date

# Get an interactive TTY and run /bin/bash from pod <pod-name>. By default, output is from the first container.
kubectl exec -ti <pod-name> -- /bin/bash
```

`kubectl logs` - چاپ لاگ‌های یک کانتینر درون یک Pod.

```shell
# Return a snapshot of the logs from pod <pod-name>.
kubectl logs <pod-name>

# Start streaming the logs from pod <pod-name>. This is similar to the 'tail -f' Linux command.
kubectl logs -f <pod-name>
```

`kubectl diff` - مشاهدهٔ تفاوت (diff) به‌روزرسانی‌های پیشنهادی برای یک کلاستر.

```shell
# Diff resources included in "pod.json".
kubectl diff -f pod.json

# Diff file read from stdin.
cat service.yaml | kubectl diff -f -
```

## مثال‌ها: ایجاد و استفاده از افزونه‌ها

از مجموعه مثال‌های زیر برای آشنایی با نوشتن و استفاده از افزونه‌های (plugin) `kubectl` استفاده کنید:

```shell
# create a simple plugin in any language and name the resulting executable file
# so that it begins with the prefix "kubectl-"
cat ./kubectl-hello
```
```shell
#!/bin/sh

# this plugin prints the words "hello world"
echo "hello world"
```
پس از نوشتن افزونه، آن را اجرایی می‌کنیم:
```bash
chmod a+x ./kubectl-hello

# and move it to a location in our PATH
sudo mv ./kubectl-hello /usr/local/bin
sudo chown root:root /usr/local/bin

# You have now created and "installed" a kubectl plugin.
# You can begin using this plugin by invoking it from kubectl as if it were a regular command
kubectl hello
```
```
hello world
```

```shell
# You can "uninstall" a plugin, by removing it from the folder in your
# $PATH where you placed it
sudo rm /usr/local/bin/kubectl-hello
```

برای مشاهدهٔ همهٔ افزونه‌هایی که در دسترس `kubectl` هستند، از زیردستور `kubectl plugin list` استفاده کنید:

```shell
kubectl plugin list
```
خروجی مشابه زیر است:
```
The following kubectl-compatible plugins are available:

/usr/local/bin/kubectl-hello
/usr/local/bin/kubectl-foo
/usr/local/bin/kubectl-bar
```

دستور `kubectl plugin list` همچنین دربارهٔ افزونه‌هایی که اجرایی نیستند یا توسط افزونه‌های دیگر پوشانده شده‌اند هشدار می‌دهد؛ برای مثال:

```shell
sudo chmod -x /usr/local/bin/kubectl-foo # remove execute permission
kubectl plugin list
```

```
The following kubectl-compatible plugins are available:

/usr/local/bin/kubectl-hello
/usr/local/bin/kubectl-foo
  - warning: /usr/local/bin/kubectl-foo identified as a plugin, but it is not executable
/usr/local/bin/kubectl-bar

error: one plugin warning was found
```

می‌توانید افزونه‌ها را وسیله‌ای برای ساخت قابلیت‌های پیچیده‌تر بر پایهٔ دستورهای موجود kubectl در نظر بگیرید:

```shell
cat ./kubectl-whoami
```

مثال‌های بعدی فرض می‌کنند که فایل `kubectl-whoami` را با محتوای زیر ساخته‌اید:

```shell
#!/bin/bash

# this plugin makes use of the `kubectl config` command in order to output
# information about the current user, based on the currently selected context
kubectl config view --template='{{ range .contexts }}{{ if eq .name "'$(kubectl config current-context)'" }}Current user: {{ printf "%s\n" .context.user }}{{ end }}{{ end }}'
```

اجرای دستور بالا خروجی‌ای حاوی کاربر مربوط به context فعلی در فایل KUBECONFIG شما تولید می‌کند:

```shell
# make the file executable
sudo chmod +x ./kubectl-whoami

# and move it into your PATH
sudo mv ./kubectl-whoami /usr/local/bin

kubectl whoami
Current user: plugins-user
```

## {{% heading "whatsnext" %}}

* مستندات مرجع `kubectl` را بخوانید:
  * [مرجع دستورها](/docs/reference/kubectl/kubectl/) در kubectl
  * مرجع [آرگومان‌های خط فرمان](/docs/reference/kubectl/generated/kubectl/)
* دربارهٔ [قراردادهای استفاده از `kubectl`](/docs/reference/kubectl/conventions/) بیاموزید
* دربارهٔ [پشتیبانی از JSONPath](/docs/reference/kubectl/jsonpath/) در kubectl مطالعه کنید
* دربارهٔ چگونگی [گسترش kubectl با افزونه‌ها](/docs/tasks/extend-kubectl/kubectl-plugins) مطالعه کنید
  * برای آگاهی بیشتر دربارهٔ افزونه‌ها، [نمونهٔ افزونهٔ CLI](https://github.com/kubernetes/sample-cli-plugin) را ببینید.

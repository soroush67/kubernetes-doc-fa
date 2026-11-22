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
{{< glossary_definition prepend="Kubernetes provides a" term_id="kubectl" length="short" >}}

نام این ابزار `kubectl` است.

ابزار `kubectl` برای پیکربندی، به دنبال فایلی به نام `config` در دایرکتوری `$HOME/.kube` می‌گردد.
می‌توانید با تنظیم متغیر محیطی `KUBECONFIG` یا با استفاده از فلگ
[`--kubeconfig`](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)، فایل‌های
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) دیگری را مشخص کنید.

این نمای کلی، نحو (syntax) دستورهای `kubectl` را پوشش می‌دهد، عملیات دستورها را شرح می‌دهد و نمونه‌های رایجی ارائه می‌کند.
برای جزئیات هر دستور، از جمله همهٔ فلگ‌ها و زیردستورهای پشتیبانی‌شده، به مستندات مرجع
[kubectl](/docs/reference/kubectl/generated/kubectl/) مراجعه کنید.

برای مشاهدهٔ نمای کلی، به [ابزار خط فرمان kubectl](/docs/concepts/overview/kubectl/) مراجعه کنید.
برای دستورالعمل‌های نصب، [نصب kubectl](/docs/tasks/tools/#kubectl) را ببینید؛
و برای راهنمای سریع، به [برگهٔ تقلب](/docs/reference/kubectl/quick-reference/) مراجعه کنید.
اگر به استفاده از ابزار خط فرمان `docker` عادت دارید، صفحهٔ
[`kubectl` برای کاربران Docker](/docs/reference/kubectl/docker-cli-to-kubectl/) برخی از دستورهای معادل در کوبرنتیز را توضیح می‌دهد.

<!-- body -->

## نحو دستورها

برای اجرای دستورهای `kubectl` از پنجرهٔ ترمینال خود، از نحو زیر استفاده کنید:

```shell
kubectl [command] [TYPE] [NAME] [flags]
```

در این نحو، `command`، `TYPE`، `NAME` و `flags` به این معنا هستند:

* `command`: عملیاتی را مشخص می‌کند که می‌خواهید روی یک یا چند منبع انجام دهید؛
  برای مثال `create`، `get`، `describe` و `delete`.

* `TYPE`: [نوع منبع](#resource-types) را مشخص می‌کند. انواع منابع به بزرگی و کوچکی حروف حساس نیستند و
  می‌توانید شکل مفرد، جمع یا کوتاه‌شدهٔ آن‌ها را به کار ببرید.
  برای مثال، دستورهای زیر خروجی یکسانی تولید می‌کنند:

  ```shell
  kubectl get pod pod1
  kubectl get pods pod1
  kubectl get po pod1
  ```

* `NAME`: نام منبع را مشخص می‌کند. نام‌ها به بزرگی و کوچکی حروف حساس هستند. اگر نام را ذکر نکنید،
  جزئیات همهٔ منابع نمایش داده می‌شود؛ برای مثال `kubectl get pods`.

  هنگام انجام عملیات روی چند منبع، می‌توانید هر منبع را با نوع و نام آن مشخص کنید
  یا یک یا چند فایل را تعیین کنید:

  * برای مشخص کردن منابع با نوع و نام:

    * برای گروه‌بندی منابعی که همگی از یک نوع هستند:  `TYPE1 name1 name2 name<#>`.<br/>
      مثال: `kubectl get pod example-pod1 example-pod2`

    * برای مشخص کردن جداگانهٔ چند نوع منبع:  `TYPE1/name1 TYPE1/name2 TYPE2/name3 TYPE<#>/name<#>`.<br/>
      مثال: `kubectl get pod/example-pod1 replicationcontroller/example-rc1`

  * برای مشخص کردن منابع با یک یا چند فایل:  `-f file1 -f file2 -f file<#>`

    * به‌جای JSON از YAML استفاده کنید،
      زیرا YAML معمولاً کاربرپسندتر است، به‌ویژه برای فایل‌های پیکربندی.<br/>
      مثال: `kubectl get -f ./pod.yaml`

* `flags`: فلگ‌های اختیاری را مشخص می‌کند. برای مثال، می‌توانید با فلگ‌های `-s` یا `--server`
  نشانی و پورت سرور API کوبرنتیز را مشخص کنید.<br/>

{{< caution >}}
فلگ‌هایی که در خط فرمان مشخص می‌کنید، مقادیر پیش‌فرض و هر متغیر محیطی متناظر را بازنویسی می‌کنند.
{{< /caution >}}

اگر به راهنمایی نیاز دارید، دستور `kubectl help` را در پنجرهٔ ترمینال اجرا کنید.

## احراز هویت درون کلاستر و بازنویسی فضای نام

ابزار `kubectl` به‌طور پیش‌فرض ابتدا بررسی می‌کند که آیا درون یک پاد، و در نتیجه درون یک کلاستر، اجرا می‌شود یا نه.
این ابزار کار را با بررسی متغیرهای محیطی `KUBERNETES_SERVICE_HOST` و `KUBERNETES_SERVICE_PORT`
و وجود فایل توکن حساب سرویس در مسیر `/var/run/secrets/kubernetes.io/serviceaccount/token` آغاز می‌کند.
اگر هر سه مورد یافت شوند، فرض بر احراز هویت درون کلاستر گذاشته می‌شود.

برای حفظ سازگاری با نسخه‌های قبلی، اگر متغیر محیطی `POD_NAMESPACE` هنگام احراز هویت
درون کلاستر تنظیم شده باشد، فضای نام (namespace) پیش‌فرضِ برگرفته از توکن حساب سرویس را
بازنویسی می‌کند. این موضوع بر همهٔ مانیفست‌ها یا ابزارهایی که به فضای نام پیش‌فرض متکی هستند اثر می‌گذارد.

**متغیر محیطی `POD_NAMESPACE`**

اگر متغیر محیطی `POD_NAMESPACE` تنظیم شده باشد، عملیات خط فرمان روی منابع وابسته به فضای نام
به‌طور پیش‌فرض از مقدار این متغیر استفاده می‌کنند. برای مثال، اگر مقدار این متغیر `seattle` باشد،
دستور `kubectl get pods` پادهای موجود در فضای نام `seattle` را برمی‌گرداند. دلیل این است که پادها
منبعی وابسته به فضای نام هستند و در دستور هیچ فضای نامی مشخص نشده است. برای اینکه بدانید
یک منبع وابسته به فضای نام است یا نه، خروجی `kubectl api-resources` را بررسی کنید.

استفادهٔ صریح از `--namespace <value>` این رفتار را بازنویسی می‌کند.

**نحوهٔ برخورد kubectl با توکن‌های ServiceAccount**

اگر:

* فایل توکن حساب سرویس کوبرنتیز در مسیر
  `/var/run/secrets/kubernetes.io/serviceaccount/token` مانت شده باشد، و
* متغیر محیطی `KUBERNETES_SERVICE_HOST` تنظیم شده باشد، و
* متغیر محیطی `KUBERNETES_SERVICE_PORT` تنظیم شده باشد، و
* در خط فرمان kubectl فضای نامی را به‌صراحت مشخص نکرده باشید،

آنگاه kubectl فرض می‌کند که درون کلاستر شما اجرا می‌شود. ابزار kubectl فضای نام آن
ServiceAccount را (که همان فضای نام Pod است) پیدا می‌کند و روی همان فضای نام عمل می‌کند.
این رفتار با آنچه بیرون از کلاستر رخ می‌دهد متفاوت است؛ وقتی kubectl بیرون از کلاستر اجرا می‌شود
و فضای نامی مشخص نکرده‌اید، دستور kubectl روی فضای نامی عمل می‌کند که برای context فعلی
در پیکربندی کلاینت شما تنظیم شده است. برای تغییر فضای نام پیش‌فرض kubectl می‌توانید از
دستور زیر استفاده کنید:

```shell
kubectl config set-context --current --namespace=<namespace-name>
```

## عملیات

جدول زیر شامل توضیحات کوتاه و نحو کلی همهٔ عملیات `kubectl` است:

عملیات       | نحو    |       توضیح
-------------------- | -------------------- | --------------------
`alpha`    | `kubectl alpha SUBCOMMAND [flags]` | دستورهای موجود مربوط به قابلیت‌های آلفا را فهرست می‌کند؛ این قابلیت‌ها به‌طور پیش‌فرض در کلاسترهای کوبرنتیز فعال نیستند.
`annotate`    | <code>kubectl annotate (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]</code> | حاشیه‌نویسی‌های (annotation) یک یا چند منبع را اضافه یا به‌روزرسانی می‌کند.
`api-resources`    | `kubectl api-resources [flags]` | منابع API موجود را فهرست می‌کند.
`api-versions`    | `kubectl api-versions [flags]` | نسخه‌های API موجود را فهرست می‌کند.
`apply`            | `kubectl apply -f FILENAME [flags]`| تغییری در پیکربندی را از یک فایل یا stdin روی یک منبع اعمال می‌کند.
`attach`        | `kubectl attach POD -c CONTAINER [-i] [-t] [flags]` | به یک کانتینر در حال اجرا متصل می‌شود تا جریان خروجی آن را ببینید یا با کانتینر (از طریق stdin) تعامل کنید.
`auth`    | `kubectl auth [flags] [options]` | مجوزدهی را بررسی می‌کند.
`autoscale`    | <code>kubectl autoscale (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu=CPU] [flags]</code> | مجموعه پادهایی را که یک replication controller مدیریت می‌کند به‌طور خودکار مقیاس‌دهی می‌کند.
`certificate`    | `kubectl certificate SUBCOMMAND [options]` | منابع گواهی را تغییر می‌دهد.
`cluster-info`    | `kubectl cluster-info [flags]` | اطلاعات endpoint مربوط به master و سرویس‌های کلاستر را نمایش می‌دهد.
`completion`    | `kubectl completion SHELL [options]` | کد تکمیل خودکار پوسته را برای پوستهٔ مشخص‌شده (bash یا zsh) خروجی می‌دهد.
`config`        | `kubectl config SUBCOMMAND [flags]` | فایل‌های kubeconfig را تغییر می‌دهد. برای جزئیات، به هر یک از زیردستورها مراجعه کنید.
`convert`    | `kubectl convert -f FILENAME [options]` | فایل‌های پیکربندی را بین نسخه‌های مختلف API تبدیل می‌کند. هر دو قالب YAML و JSON پذیرفته می‌شوند. توجه: این دستور به نصب افزونهٔ `kubectl-convert` نیاز دارد.
`cordon`    | `kubectl cordon NODE [options]` | نود را غیرقابل زمان‌بندی علامت‌گذاری می‌کند.
`cp`    | `kubectl cp <file-spec-src> <file-spec-dest> [options]` | فایل‌ها و دایرکتوری‌ها را به کانتینرها و از آن‌ها کپی می‌کند.
`create`        | `kubectl create -f FILENAME [flags]` | یک یا چند منبع را از یک فایل یا stdin ایجاد می‌کند.
`delete`        | <code>kubectl delete (-f FILENAME &#124; TYPE [NAME &#124; /NAME &#124; -l label &#124; --all]) [flags]</code> | منابع را از روی یک فایل، stdin، یا با مشخص کردن انتخابگرهای (selector) برچسب، نام‌ها، انتخابگرهای منبع یا خود منابع حذف می‌کند.
`describe`    | <code>kubectl describe (-f FILENAME &#124; TYPE [NAME_PREFIX &#124; /NAME &#124; -l label]) [flags]</code> | وضعیت جزئی یک یا چند منبع را نمایش می‌دهد.
`diff`        | `kubectl diff -f FILENAME [flags]`| تفاوت فایل یا stdin را با پیکربندی زنده نشان می‌دهد.
`drain`    | `kubectl drain NODE [options]` | نود را برای آماده‌سازی جهت نگهداری تخلیه می‌کند.
`edit`        | <code>kubectl edit (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [flags]</code> | تعریف یک یا چند منبع را روی سرور با استفاده از ویرایشگر پیش‌فرض ویرایش و به‌روزرسانی می‌کند.
`events`      | `kubectl events` | رویدادها را فهرست می‌کند.
`exec`        | `kubectl exec POD [-c CONTAINER] [-i] [-t] [flags] [-- COMMAND [args...]]` | دستوری را در یک کانتینرِ درون پاد اجرا می‌کند.
`explain`    | `kubectl explain TYPE [--recursive=false] [flags]` | مستندات منابع مختلف، مانند پادها، نودها، سرویس‌ها و غیره را دریافت می‌کند.
`expose`        | <code>kubectl expose (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) [--port=port] [--protocol=TCP&#124;UDP] [--target-port=number-or-name] [--name=name] [--external-ip=external-ip-of-service] [--type=type] [flags]</code> | یک replication controller، سرویس یا پاد را به‌صورت یک سرویس جدید کوبرنتیز در دسترس قرار می‌دهد.
`get`        | <code>kubectl get (-f FILENAME &#124; TYPE [NAME &#124; /NAME &#124; -l label]) [--watch] [--sort-by=FIELD] [[-o &#124; --output]=OUTPUT_FORMAT] [flags]</code> | یک یا چند منبع را فهرست می‌کند.
`kustomize`    | `kubectl kustomize <dir> [flags] [options]` | مجموعه‌ای از منابع API را که از دستورالعمل‌های یک فایل kustomization.yaml تولید شده‌اند فهرست می‌کند. آرگومان باید مسیر دایرکتوری حاوی این فایل باشد، یا نشانی یک مخزن git همراه با پسوند مسیری که همان دایرکتوری را نسبت به ریشهٔ مخزن مشخص می‌کند.
`label`        | <code>kubectl label (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--overwrite] [--all] [--resource-version=version] [flags]</code> | برچسب‌های یک یا چند منبع را اضافه یا به‌روزرسانی می‌کند.
`logs`        | `kubectl logs POD [-c CONTAINER] [--follow] [flags]` | لاگ‌های یک کانتینرِ درون پاد را چاپ می‌کند.
`options`    | `kubectl options` | فهرست گزینه‌های سراسری خط فرمان را نمایش می‌دهد که برای همهٔ دستورها اعمال می‌شوند.
`patch`        | <code>kubectl patch (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) --patch PATCH [flags]</code> | یک یا چند فیلد از یک منبع را با فرایند strategic merge patch به‌روزرسانی می‌کند.
`plugin`    | `kubectl plugin [flags] [options]` | ابزارهایی برای تعامل با افزونه‌ها فراهم می‌کند.
`port-forward`    | `kubectl port-forward POD [LOCAL_PORT:]REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N] [flags]` | یک یا چند پورت محلی را به یک پاد هدایت می‌کند.
`proxy`        | `kubectl proxy [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [--api-prefix=prefix] [flags]` | یک پراکسی به سرور API کوبرنتیز اجرا می‌کند.
`replace`        | `kubectl replace -f FILENAME` | یک منبع را از روی یک فایل یا stdin جایگزین می‌کند.
`rollout`    | `kubectl rollout SUBCOMMAND [options]` | انتشار (rollout) یک منبع را مدیریت می‌کند. انواع منبع معتبر عبارت‌اند از: deployments، daemonsets و statefulsets.
`run`        | <code>kubectl run NAME --image=image [--env="key=value"] [--port=port] [--dry-run=server&#124;client&#124;none] [--overrides=inline-json] [flags]</code> | ایمیج مشخص‌شده را روی کلاستر اجرا می‌کند.
`scale`        | <code>kubectl scale (-f FILENAME &#124; TYPE NAME &#124; TYPE/NAME) --replicas=COUNT [--resource-version=version] [--current-replicas=count] [flags]</code> | اندازهٔ replication controller مشخص‌شده را به‌روزرسانی می‌کند.
`set`    | `kubectl set SUBCOMMAND [options]` | منابع برنامه را پیکربندی می‌کند.
`taint`    | `kubectl taint NODE NAME KEY_1=VAL_1:TAINT_EFFECT_1 ... KEY_N=VAL_N:TAINT_EFFECT_N [options]` | taintهای یک یا چند نود را به‌روزرسانی می‌کند.
`top`    | <code>kubectl top (POD &#124; NODE) [flags] [options]</code> | میزان مصرف منابع (CPU/حافظه/ذخیره‌سازی) پاد یا نود را نمایش می‌دهد.
`uncordon`    | `kubectl uncordon NODE [options]` | نود را قابل زمان‌بندی علامت‌گذاری می‌کند.
`version`        | `kubectl version [--client] [flags]` | نسخهٔ کوبرنتیزِ در حال اجرا روی کلاینت و سرور را نمایش می‌دهد.
`wait`    | <code>kubectl wait ([-f FILENAME] &#124; resource.group/resource.name &#124; resource.group [(-l label &#124; --all)]) [--for=delete&#124;--for condition=available] [options]</code> | آزمایشی: منتظر برقراری یک شرط مشخص روی یک یا چند منبع می‌ماند.

برای آشنایی بیشتر با عملیات دستورها، به مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) مراجعه کنید.

## انواع منابع

جدول زیر فهرستی از همهٔ انواع منابع پشتیبانی‌شده و نام‌های مستعار کوتاه آن‌ها را نشان می‌دهد.

(این خروجی را می‌توان از `kubectl api-resources` به دست آورد و تا نسخهٔ 1.25.0 کوبرنتیز دقیق بوده است.)

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

## گزینه‌های خروجی

در بخش‌های زیر می‌توانید با نحوهٔ قالب‌بندی یا مرتب‌سازی خروجی برخی دستورها آشنا شوید.
برای جزئیات اینکه کدام دستورها از گزینه‌های مختلف خروجی پشتیبانی می‌کنند،
به مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) مراجعه کنید.

### قالب‌بندی خروجی

قالب خروجی پیش‌فرض همهٔ دستورهای `kubectl`، قالب متن سادهٔ خوانا برای انسان است.
برای اینکه جزئیات را در قالبی مشخص در پنجرهٔ ترمینال خود نمایش دهید، می‌توانید یکی از فلگ‌های `-o`
یا `--output` را به یک دستور پشتیبانی‌شدهٔ `kubectl` اضافه کنید.

#### نحو

```shell
kubectl [command] [TYPE] [NAME] -o <output_format>
```

بسته به عملیات `kubectl`، قالب‌های خروجی زیر پشتیبانی می‌شوند:

قالب خروجی | توضیح
--------------| -----------
`-o custom-columns=<spec>` | جدولی را با استفاده از فهرستی از [ستون‌های سفارشی](#custom-columns) که با کاما از هم جدا شده‌اند چاپ می‌کند.
`-o custom-columns-file=<filename>` | جدولی را با استفاده از الگوی [ستون‌های سفارشی](#custom-columns) موجود در فایل `<filename>` چاپ می‌کند.
`-o json`     | یک آبجکت API را در قالب JSON خروجی می‌دهد.
`-o jsonpath=<template>` | فیلدهای تعریف‌شده در یک عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) را چاپ می‌کند.
`-o jsonpath-file=<filename>` | فیلدهای تعریف‌شده در عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) موجود در فایل `<filename>` را چاپ می‌کند.
`-o kyaml`    | یک آبجکت API را در قالب [KYAML](/docs/reference/encodings/kyaml/) خروجی می‌دهد.
`-o name`     | فقط نام منبع را چاپ می‌کند و هیچ چیز دیگری را نمایش نمی‌دهد.
`-o wide`     | خروجی را در قالب متن ساده همراه با اطلاعات تکمیلی نمایش می‌دهد. برای پادها، نام نود نیز درج می‌شود.
`-o yaml`     | یک آبجکت API را در قالب YAML خروجی می‌دهد. KYAML گویشی از YAML مخصوص کوبرنتیز است و می‌توان آن را به‌عنوان YAML تجزیه کرد.

##### مثال

در این مثال، دستور زیر جزئیات یک پاد را به‌صورت آبجکتی در قالب YAML خروجی می‌دهد:

```shell
kubectl get pod web-pod-13je7 -o yaml
```

به یاد داشته باشید: برای جزئیات اینکه هر دستور از کدام قالب خروجی پشتیبانی می‌کند،
به مستندات مرجع [kubectl](/docs/reference/kubectl/kubectl/) مراجعه کنید.

#### ستون‌های سفارشی

برای تعریف ستون‌های سفارشی و نمایش تنها جزئیات موردنظرتان در قالب جدول، می‌توانید از گزینهٔ `custom-columns` استفاده کنید.
می‌توانید ستون‌های سفارشی را به‌صورت درون‌خطی تعریف کنید یا از یک فایل الگو استفاده کنید: `-o custom-columns=<spec>` یا `-o custom-columns-file=<filename>`.

##### مثال‌ها

درون‌خطی:

```shell
kubectl get pods <pod-name> -o custom-columns=NAME:.metadata.name,RSRC:.metadata.resourceVersion
```

فایل الگو:

```shell
kubectl get pods <pod-name> -o custom-columns-file=template.txt
```

که در آن فایل `template.txt` شامل محتوای زیر است:

```
NAME          RSRC
metadata.name metadata.resourceVersion
```
نتیجهٔ اجرای هر یک از این دو دستور مشابه زیر است:

```
NAME           RSRC
submit-queue   610995
```

#### ستون‌های سمت سرور

ابزار `kubectl` از دریافت اطلاعات ستون‌های مشخص دربارهٔ آبجکت‌ها از سرور پشتیبانی می‌کند.
به این معنا که سرور برای هر منبع، ستون‌ها و ردیف‌های مرتبط با آن منبع را برمی‌گرداند تا کلاینت آن‌ها را چاپ کند.
از آنجا که جزئیات چاپ در سرور کپسوله می‌شود، خروجی خوانا برای انسان در همهٔ کلاینت‌هایی که با یک کلاستر کار می‌کنند یکسان خواهد بود.

این قابلیت به‌طور پیش‌فرض فعال است. برای غیرفعال کردن آن، فلگ
`--server-print=false` را به دستور `kubectl get` اضافه کنید.

##### مثال‌ها

برای چاپ اطلاعات مربوط به وضعیت یک پاد، از دستوری مانند دستور زیر استفاده کنید:

```shell
kubectl get pods <pod-name> --server-print=false
```

خروجی مشابه زیر است:

```
NAME       AGE
pod-name   1m
```

### مرتب‌سازی فهرست آبجکت‌ها

برای نمایش آبجکت‌ها به‌صورت فهرستی مرتب‌شده در پنجرهٔ ترمینال، می‌توانید فلگ `--sort-by` را به یکی از دستورهای پشتیبانی‌شدهٔ `kubectl` اضافه کنید. با مشخص کردن هر فیلد عددی یا رشته‌ای در فلگ `--sort-by`، آبجکت‌ها بر اساس آن فیلد مرتب می‌شوند. برای مشخص کردن فیلد، از یک عبارت [jsonpath](/docs/reference/kubectl/jsonpath/) استفاده کنید.

#### نحو دستور

```shell
kubectl [command] [TYPE] [NAME] --sort-by=<jsonpath_exp>
```

##### مثال

برای چاپ فهرست پادها به‌ترتیب نام، دستور زیر را اجرا کنید:

```shell
kubectl get pods --sort-by=.metadata.name
```

## مثال‌ها: عملیات رایج

مجموعه مثال‌های زیر به شما کمک می‌کند با اجرای عملیات پرکاربرد `kubectl` آشنا شوید:

دستور `kubectl apply` یک منبع را از روی یک فایل یا ورودی استاندارد (stdin) اعمال یا به‌روزرسانی می‌کند.

```shell
# Create a service using the definition in example-service.yaml.
kubectl apply -f example-service.yaml

# Create a replication controller using the definition in example-controller.yaml.
kubectl apply -f example-controller.yaml

# Create the objects that are defined in any .yaml, .yml, or .json file within the <directory> directory.
kubectl apply -f <directory>
```

دستور `kubectl get` یک یا چند منبع را فهرست می‌کند.

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

دستور `kubectl describe` وضعیت مفصل یک یا چند منبع را نمایش می‌دهد و به‌طور پیش‌فرض منابع مقداردهی‌نشده را نیز در بر می‌گیرد.

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
دستور `kubectl get` معمولاً برای بازیابی یک یا چند منبع از یک نوع منبع به کار می‌رود. این دستور مجموعهٔ گسترده‌ای از فلگ‌ها دارد؛ برای نمونه، با فلگ `-o` یا `--output` می‌توانید قالب خروجی را سفارشی کنید. همچنین با فلگ `-w` یا `--watch` می‌توانید پایش به‌روزرسانی‌های یک آبجکت مشخص را آغاز کنید. در مقابل، دستور `kubectl describe` بیشتر بر توصیف جنبه‌های مرتبط متعدد یک منبع مشخص تمرکز دارد و ممکن است برای ساختن نمایی برای کاربر، چندین فراخوانی API به سرور API انجام دهد. برای مثال، دستور `kubectl describe node` نه‌تنها اطلاعات خود نود، بلکه خلاصه‌ای از پادهای در حال اجرا روی آن، رویدادهای تولیدشده برای نود و موارد دیگر را نیز بازیابی می‌کند.
{{< /note >}}

دستور `kubectl delete` منابع را از روی یک فایل یا ورودی استاندارد، یا با مشخص کردن انتخابگرهای برچسب، نام‌ها، انتخابگرهای منبع یا خود منابع حذف می‌کند.

```shell
# Delete a pod using the type and name specified in the pod.yaml file.
kubectl delete -f pod.yaml

# Delete all the pods and services that have the label '<label-key>=<label-value>'.
kubectl delete pods,services -l <label-key>=<label-value>

# Delete all pods, including uninitialized ones.
kubectl delete pods --all
```

دستور `kubectl exec` یک فرمان را روی یکی از کانتینرهای یک پاد اجرا می‌کند.

```shell
# Get output from running 'date' from pod <pod-name>. By default, output is from the first container.
kubectl exec <pod-name> -- date

# Get output from running 'date' in container <container-name> of pod <pod-name>.
kubectl exec <pod-name> -c <container-name> -- date

# Get an interactive TTY and run /bin/bash from pod <pod-name>. By default, output is from the first container.
kubectl exec -ti <pod-name> -- /bin/bash
```

دستور `kubectl logs` لاگ‌های یک کانتینر در یک پاد را چاپ می‌کند.

```shell
# Return a snapshot of the logs from pod <pod-name>.
kubectl logs <pod-name>

# Start streaming the logs from pod <pod-name>. This is similar to the 'tail -f' Linux command.
kubectl logs -f <pod-name>
```

دستور `kubectl diff` تفاوت‌های به‌روزرسانی‌های پیشنهادی برای کلاستر را نمایش می‌دهد.

```shell
# Diff resources included in "pod.json".
kubectl diff -f pod.json

# Diff file read from stdin.
cat service.yaml | kubectl diff -f -
```

## مثال‌ها: ساخت و استفاده از افزونه‌ها

مجموعه مثال‌های زیر به شما کمک می‌کند با نوشتن و استفاده از افزونه‌های (plugins) `kubectl` آشنا شوید:

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
اکنون که افزونه نوشته شده است، آن را اجراپذیر می‌کنیم:
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

برای مشاهدهٔ همهٔ افزونه‌هایی که در دسترس `kubectl` هستند، از زیرفرمان `kubectl plugin list` استفاده کنید:

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

زیرفرمان `kubectl plugin list` دربارهٔ افزونه‌هایی که اجراپذیر نیستند یا افزونه‌های دیگری آن‌ها را تحت‌الشعاع قرار داده‌اند نیز هشدار می‌دهد؛ برای مثال:

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

می‌توانید افزونه‌ها را ابزاری برای ساختن قابلیت‌های پیچیده‌تر بر پایهٔ دستورهای موجود kubectl در نظر بگیرید:

```shell
cat ./kubectl-whoami
```

در چند مثال بعدی فرض شده است که محتوای فایل `kubectl-whoami` را از قبل به شکل زیر تنظیم کرده‌اید:

```shell
#!/bin/bash

# this plugin makes use of the `kubectl config` command in order to output
# information about the current user, based on the currently selected context
kubectl config view --template='{{ range .contexts }}{{ if eq .name "'$(kubectl config current-context)'" }}Current user: {{ printf "%s\n" .context.user }}{{ end }}{{ end }}'
```

اجرای دستور بالا خروجی‌ای به شما می‌دهد که کاربر مربوط به context فعلی در فایل KUBECONFIG شما را نشان می‌دهد:

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
  * [مرجع دستورهای](/docs/reference/kubectl/kubectl/) kubectl
  * مرجع [آرگومان‌های خط فرمان](/docs/reference/kubectl/generated/kubectl/)
* با [قراردادهای استفاده از `kubectl`](/docs/reference/kubectl/conventions/) آشنا شوید.
* دربارهٔ [پشتیبانی از JSONPath](/docs/reference/kubectl/jsonpath/) در kubectl بخوانید.
* دربارهٔ نحوهٔ [گسترش kubectl با افزونه‌ها](/docs/tasks/extend-kubectl/kubectl-plugins) بخوانید.
  * برای آشنایی بیشتر با افزونه‌ها، نگاهی به [نمونهٔ افزونهٔ CLI](https://github.com/kubernetes/sample-cli-plugin) بیندازید.

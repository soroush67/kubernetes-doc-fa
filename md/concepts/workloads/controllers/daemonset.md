---
reviewers:
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
title: DaemonSet
api_metadata:
- apiVersion: "apps/v1"
  kind: "DaemonSet"
description: >-
 یک DaemonSet، Podهایی را تعریف می‌کند که امکاناتی محلی برای نود فراهم می‌کنند. این امکانات ممکن است برای عملکرد کلاستر شما بنیادی باشند، مانند یک ابزار کمکی شبکه، یا بخشی از یک افزونه باشند.
content_type: concept
weight: 40
hide_summary: true # Listed separately in section index
---

<!-- overview -->

یک _DaemonSet_ اطمینان حاصل می‌کند که همه‌ی نودها (یا برخی از آن‌ها) یک نسخه از یک Pod را اجرا کنند. با افزوده شدن نودها به
کلاستر، Podها نیز به آن‌ها افزوده می‌شوند. با حذف نودها از کلاستر، آن Podها توسط جمع‌آوری زباله
حذف می‌شوند. حذف یک DaemonSet، Podهایی را که ایجاد کرده است پاک‌سازی می‌کند.

برخی از کاربردهای معمول DaemonSet عبارت‌اند از:

- اجرای یک daemon ذخیره‌سازی کلاستر روی هر نود
- اجرای یک daemon جمع‌آوری لاگ روی هر نود
- اجرای یک daemon پایش نود روی هر نود

در یک حالت ساده، برای هر نوع daemon از یک DaemonSet که همه‌ی نودها را پوشش می‌دهد استفاده می‌شود.
یک پیکربندی پیچیده‌تر ممکن است برای یک نوع daemon از چند DaemonSet استفاده کند، اما با
flagهای متفاوت و/یا درخواست‌های حافظه و cpu متفاوت برای انواع مختلف سخت‌افزار.

<!-- body -->

## نوشتن spec یک DaemonSet

### ایجاد یک DaemonSet

می‌توانید یک DaemonSet را در یک فایل YAML توصیف کنید. برای مثال، فایل `daemonset.yaml` زیر
یک DaemonSet را توصیف می‌کند که ایمیج Docker مربوط به fluentd-elasticsearch را اجرا می‌کند:

{{% code_sample file="controllers/daemonset.yaml" %}}

یک DaemonSet بر اساس فایل YAML ایجاد کنید:

```
kubectl apply -f https://k8s.io/examples/controllers/daemonset.yaml
```

### فیلدهای الزامی

همانند همه‌ی پیکربندی‌های دیگر کوبرنتیز، یک DaemonSet به فیلدهای `apiVersion`، `kind` و `metadata` نیاز دارد. برای
اطلاعات کلی درباره‌ی کار با فایل‌های پیکربندی، به
[اجرای برنامه‌های بی‌حالت](/docs/tasks/run-application/run-stateless-application-deployment/)
و [مدیریت آبجکت با استفاده از kubectl](/docs/concepts/overview/working-with-objects/object-management/) مراجعه کنید.

نام یک آبجکت DaemonSet باید یک
[نام زیردامنه‌ی DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

یک DaemonSet همچنین به یک بخش
[`.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status)
نیاز دارد.

### قالب Pod

`.spec.template` یکی از فیلدهای الزامی در `.spec` است.

`.spec.template` یک [قالب Pod](/docs/concepts/workloads/pods/#pod-templates) است.
این قالب دقیقاً همان شِمای یک {{< glossary_tooltip text="Pod" term_id="pod" >}} را دارد،
با این تفاوت که تودرتو است و `apiVersion` یا `kind` ندارد.

علاوه بر فیلدهای الزامی یک Pod، قالب Pod در یک DaemonSet باید برچسب‌های مناسبی
مشخص کند (به [انتخابگر Pod](#pod-selector) مراجعه کنید).

قالب Pod در یک DaemonSet باید [`RestartPolicy`](/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy)ای
 برابر با `Always` داشته باشد، یا مشخص نشده باشد که در این صورت پیش‌فرض آن `Always` است.

### انتخابگر Pod

فیلد `.spec.selector` یک انتخابگر (selector) Pod است. این فیلد همانند `.spec.selector` یک
[Job](/docs/concepts/workloads/controllers/job/) عمل می‌کند.

باید یک انتخابگر Pod مشخص کنید که با برچسب‌های
`.spec.template` مطابقت داشته باشد.
همچنین، پس از ایجاد یک DaemonSet،
`.spec.selector` آن قابل تغییر نیست. تغییر انتخابگر Pod می‌تواند به
یتیم شدن ناخواسته‌ی Podها منجر شود و مشخص شد که برای کاربران گیج‌کننده است.

`.spec.selector` یک آبجکت متشکل از دو فیلد است:

* `matchLabels` - همانند `.spec.selector` یک
  [ReplicationController](/docs/concepts/workloads/controllers/replicationcontroller/) عمل می‌کند.
* `matchExpressions` - امکان ساخت انتخابگرهای پیچیده‌تر را با مشخص کردن کلید،
  فهرست مقادیر و عملگری که کلید و مقادیر را به هم مرتبط می‌کند فراهم می‌کند.

هنگامی که هر دو مشخص شوند، نتیجه حاصل AND آن‌هاست.

`.spec.selector` باید با `.spec.template.metadata.labels` مطابقت داشته باشد.
پیکربندی‌ای که این دو در آن با هم مطابقت نداشته باشند توسط API رد می‌شود.

### اجرای Podها روی نودهای انتخاب‌شده

اگر `.spec.template.spec.nodeSelector` را مشخص کنید، کنترل‌کننده‌ی DaemonSet
Podها را روی نودهایی ایجاد می‌کند که با آن [انتخابگر نود](/docs/concepts/scheduling-eviction/assign-pod-node/) مطابقت دارند.
به همین ترتیب، اگر `.spec.template.spec.affinity` را مشخص کنید،
کنترل‌کننده‌ی DaemonSet Podها را روی نودهایی ایجاد می‌کند که با آن
[وابستگی نود (node affinity)](/docs/concepts/scheduling-eviction/assign-pod-node/) مطابقت دارند.
اگر هیچ‌کدام را مشخص نکنید، کنترل‌کننده‌ی DaemonSet Podها را روی همه‌ی نودها ایجاد می‌کند.

## Podهای Daemon چگونه زمان‌بندی می‌شوند

از یک DaemonSet می‌توان برای اطمینان از اینکه همه‌ی نودهای واجد شرایط یک نسخه از یک Pod را اجرا می‌کنند استفاده کرد.
کنترل‌کننده‌ی DaemonSet برای هر نود واجد شرایط یک Pod ایجاد می‌کند و فیلد
`spec.affinity.nodeAffinity` آن Pod را برای مطابقت با میزبان هدف اضافه می‌کند. پس از
ایجاد Pod، معمولاً زمان‌بند پیش‌فرض کار را بر عهده می‌گیرد و سپس
Pod را با تنظیم فیلد `.spec.nodeName` به میزبان هدف متصل (bind) می‌کند. اگر Pod
جدید روی نود جا نشود، زمان‌بند پیش‌فرض ممکن است بر اساس
[اولویت](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority)
Pod جدید، برخی از Podهای موجود را پیش‌دستی (بیرون‌رانی) کند.

{{< note >}}
اگر اجرای Pod مربوط به DaemonSet روی هر نود اهمیت دارد، اغلب مطلوب است که
`.spec.template.spec.priorityClassName` مربوط به DaemonSet را روی یک
[PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
با اولویت بالاتر تنظیم کنید تا اطمینان حاصل شود که این بیرون‌رانی رخ می‌دهد.
{{< /note >}}

کاربر می‌تواند با تنظیم فیلد `.spec.template.spec.schedulerName` در DaemonSet،
زمان‌بند متفاوتی برای Podهای DaemonSet مشخص کند.

وابستگی نود اصلی که در فیلد
`.spec.template.spec.affinity.nodeAffinity` مشخص شده است (در صورت مشخص شدن)، توسط
کنترل‌کننده‌ی DaemonSet هنگام ارزیابی نودهای واجد شرایط در نظر گرفته می‌شود،
اما در Pod ایجادشده با وابستگی نودی جایگزین می‌شود که با نام
نود واجد شرایط مطابقت دارد.

```yaml
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
    - matchFields:
      - key: metadata.name
        operator: In
        values:
        - target-host-name
```


### Taintها و tolerationها

کنترل‌کننده‌ی DaemonSet به‌طور خودکار مجموعه‌ای از {{< glossary_tooltip
text="tolerationها" term_id="toleration" >}} را به Podهای DaemonSet اضافه می‌کند:

{{< table caption="Tolerationهای Podهای DaemonSet" >}}

| کلید toleration                                                                                                        | اثر       | جزئیات                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [`node.kubernetes.io/not-ready`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-not-ready)             | `NoExecute`  | Podهای DaemonSet را می‌توان روی نودهایی زمان‌بندی کرد که سالم نیستند یا برای پذیرش Podها آماده نیستند. هیچ‌یک از Podهای DaemonSet که روی چنین نودهایی در حال اجرا هستند بیرون رانده نمی‌شوند. |
| [`node.kubernetes.io/unreachable`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-unreachable)         | `NoExecute`  | Podهای DaemonSet را می‌توان روی نودهایی زمان‌بندی کرد که از سوی کنترل‌کننده‌ی نود قابل دسترسی نیستند. هیچ‌یک از Podهای DaemonSet که روی چنین نودهایی در حال اجرا هستند بیرون رانده نمی‌شوند. |
| [`node.kubernetes.io/disk-pressure`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-disk-pressure)     | `NoSchedule` | Podهای DaemonSet را می‌توان روی نودهایی با مشکل فشار دیسک زمان‌بندی کرد.                                                                         |
| [`node.kubernetes.io/memory-pressure`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-memory-pressure) | `NoSchedule` | Podهای DaemonSet را می‌توان روی نودهایی با مشکل فشار حافظه زمان‌بندی کرد.                                                                        |
| [`node.kubernetes.io/pid-pressure`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-pid-pressure) | `NoSchedule` | Podهای DaemonSet را می‌توان روی نودهایی با مشکل فشار فرایند زمان‌بندی کرد.                                                                        |
| [`node.kubernetes.io/unschedulable`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-unschedulable)   | `NoSchedule` | Podهای DaemonSet را می‌توان روی نودهایی زمان‌بندی کرد که غیرقابل زمان‌بندی هستند.                                                                            |
| [`node.kubernetes.io/network-unavailable`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-network-unavailable) | `NoSchedule` | **فقط برای Podهای DaemonSet که شبکه‌ی میزبان را درخواست می‌کنند اضافه می‌شود**، یعنی Podهایی که `spec.hostNetwork: true` دارند. چنین Podهای DaemonSet را می‌توان روی نودهایی با شبکه‌ی در دسترس نبودن زمان‌بندی کرد.|

{{< /table >}}

همچنین می‌توانید tolerationهای خود را با تعریف آن‌ها در قالب Pod مربوط به DaemonSet،
به Podهای آن DaemonSet اضافه کنید.

از آنجا که کنترل‌کننده‌ی DaemonSet toleration
`node.kubernetes.io/unschedulable:NoSchedule` را به‌طور خودکار تنظیم می‌کند،
کوبرنتیز می‌تواند Podهای DaemonSet را روی نودهایی اجرا کند که به‌عنوان _unschedulable_ (غیرقابل زمان‌بندی) علامت‌گذاری شده‌اند.

اگر از یک DaemonSet برای فراهم کردن یک کارکرد مهم در سطح نود، مانند
[شبکه‌ی کلاستر](/docs/concepts/cluster-administration/networking/)، استفاده می‌کنید،
مفید است که کوبرنتیز Podهای DaemonSet را پیش از آماده شدن نودها روی آن‌ها قرار دهد.
برای مثال، بدون آن toleration ویژه، ممکن است در وضعیت بن‌بستی گرفتار شوید
که در آن نود به‌عنوان آماده علامت‌گذاری نمی‌شود، زیرا پلاگین شبکه
روی آن اجرا نمی‌شود، و در همان حال پلاگین شبکه روی آن نود اجرا نمی‌شود، زیرا نود هنوز آماده نیست.

## ارتباط با Podهای Daemon

برخی الگوهای ممکن برای ارتباط با Podهای یک DaemonSet عبارت‌اند از:

- **Push**: Podهای DaemonSet طوری پیکربندی می‌شوند که به‌روزرسانی‌ها را به سرویس دیگری، مانند
  یک پایگاه داده‌ی آمار، ارسال کنند. این Podها کلاینت ندارند.
- **NodeIP و پورت شناخته‌شده**: Podهای DaemonSet می‌توانند از `hostPort` استفاده کنند، به‌طوری که Podها
  از طریق IPهای نود قابل دسترسی باشند.
  کلاینت‌ها فهرست IPهای نود را به نحوی می‌دانند و پورت را بر اساس قرارداد می‌شناسند.
- **DNS**: یک [سرویس headless](/docs/concepts/services-networking/service/#headless-services)
  با همان انتخابگر Pod ایجاد کنید و سپس DaemonSetها را با استفاده از منبع `endpoints`
  کشف کنید یا چند رکورد A را از DNS بازیابی کنید.
- **Service**: یک سرویس با همان انتخابگر Pod ایجاد کنید و از آن سرویس برای دسترسی به
  یک daemon روی یک نود تصادفی استفاده کنید. از [سیاست ترافیک داخلی Service](/docs/concepts/services-networking/service-traffic-policy/)
  برای محدود کردن به Podهای روی همان نود استفاده کنید.

## به‌روزرسانی یک DaemonSet

اگر برچسب‌های نود تغییر کنند، DaemonSet بی‌درنگ Podها را به نودهایی که به‌تازگی مطابقت پیدا کرده‌اند اضافه می‌کند و
Podها را از نودهایی که دیگر مطابقت ندارند حذف می‌کند.

می‌توانید Podهایی را که یک DaemonSet ایجاد می‌کند تغییر دهید. با این حال، Podها اجازه‌ی به‌روزرسانی همه‌ی
فیلدها را نمی‌دهند. همچنین، کنترل‌کننده‌ی DaemonSet دفعه‌ی بعد که یک نود (حتی با همان نام)
ایجاد شود، از قالب اصلی استفاده خواهد کرد.

می‌توانید یک DaemonSet را حذف کنید. اگر `--cascade=orphan` را همراه با `kubectl` مشخص کنید، Podها
روی نودها باقی می‌مانند. اگر سپس یک DaemonSet جدید با همان انتخابگر ایجاد کنید،
DaemonSet جدید Podهای موجود را به فرزندی می‌پذیرد. اگر لازم باشد Podهایی جایگزین شوند، DaemonSet آن‌ها را
بر اساس `updateStrategy` خود جایگزین می‌کند.

می‌توانید یک [به‌روزرسانی تدریجی](/docs/tasks/manage-daemon/update-daemon-set/) روی یک DaemonSet انجام دهید.

## جایگزین‌های DaemonSet

### اسکریپت‌های Init

قطعاً می‌توان فرایندهای daemon را با آغاز مستقیم آن‌ها روی یک نود اجرا کرد (برای مثال با استفاده از
`init`، `upstartd` یا `systemd`). این کار کاملاً قابل‌قبول است. با این حال، اجرای چنین فرایندهایی
از طریق یک DaemonSet چندین مزیت دارد:

- امکان پایش و مدیریت لاگ‌های daemonها به همان روشی که برای برنامه‌ها انجام می‌شود.
- زبان پیکربندی و ابزارهای یکسان (برای مثال قالب‌های Pod و `kubectl`) برای daemonها و برنامه‌ها.
- اجرای daemonها در کانتینرهایی با محدودیت منابع، جداسازی میان daemonها و کانتینرهای برنامه را
  افزایش می‌دهد. با این حال، این کار را می‌توان با اجرای daemonها در یک کانتینر، اما نه در یک Pod، نیز انجام داد.

### Podهای مستقل (Bare Pods)

می‌توان Podها را مستقیماً ایجاد کرد و نود مشخصی را برای اجرای آن‌ها تعیین کرد. با این حال،
یک DaemonSet، Podهایی را که به هر دلیلی حذف یا خاتمه یافته‌اند جایگزین می‌کند، مانند حالت
خرابی نود یا نگهداری اخلال‌گر نود، مانند ارتقای کرنل. به همین دلیل، باید
به‌جای ایجاد Podهای منفرد از یک DaemonSet استفاده کنید.

### Podهای ایستا

می‌توان Podها را با نوشتن یک فایل در دایرکتوری مشخصی که Kubelet آن را زیر نظر دارد ایجاد کرد. این
Podها [Podهای ایستا](/docs/tasks/configure-pod-container/static-pod/) نامیده می‌شوند.
برخلاف DaemonSet، Podهای ایستا را نمی‌توان با kubectl
یا سایر کلاینت‌های API کوبرنتیز مدیریت کرد. Podهای ایستا به apiserver وابسته نیستند و همین آن‌ها را
در موارد راه‌اندازی اولیه‌ی کلاستر (bootstrapping) مفید می‌سازد. همچنین، Podهای ایستا ممکن است در آینده منسوخ شوند.

### Deploymentها

DaemonSetها از این جهت به [Deploymentها](/docs/concepts/workloads/controllers/deployment/) شباهت دارند که
هر دو Pod ایجاد می‌کنند و آن Podها فرایندهایی دارند که انتظار نمی‌رود خاتمه یابند (برای مثال سرورهای وب،
سرورهای ذخیره‌سازی).

برای سرویس‌های بی‌حالت، مانند frontendها، از Deployment استفاده کنید؛ جایی که افزایش و کاهش
تعداد رپلیکاها و rollout به‌روزرسانی‌ها مهم‌تر از کنترل دقیق این است که Pod روی کدام میزبان
اجرا شود. هنگامی از DaemonSet استفاده کنید که اهمیت دارد یک نسخه از Pod همواره روی
همه‌ی میزبان‌ها یا میزبان‌های مشخصی اجرا شود، در صورتی که DaemonSet کارکردی در سطح نود فراهم می‌کند که به سایر Podها امکان می‌دهد روی آن نود خاص به‌درستی اجرا شوند.

برای مثال، [پلاگین‌های شبکه](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) اغلب شامل جزئی هستند که به‌صورت یک DaemonSet اجرا می‌شود. جزء DaemonSet اطمینان حاصل می‌کند که نودی که روی آن اجرا می‌شود شبکه‌ی کلاستر کارآمدی دارد.


## {{% heading "whatsnext" %}}

* با [Podها](/docs/concepts/workloads/pods) آشنا شوید:
  * با [Podهای ایستا](/docs/tasks/configure-pod-container/static-pod/) آشنا شوید که برای اجرای اجزای
    {{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز مفید هستند.
* نحوه‌ی استفاده از DaemonSetها را بیاموزید:
  * [انجام به‌روزرسانی تدریجی روی یک DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/).
  * [انجام بازگشت (rollback) روی یک DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/)
    (برای مثال، اگر یک rollout آن‌طور که انتظار داشتید کار نکرد).
* بفهمید [کوبرنتیز چگونه Podها را به نودها اختصاص می‌دهد](/docs/concepts/scheduling-eviction/assign-pod-node/).
* با [پلاگین‌های دستگاه](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) و
  [افزونه‌ها](/docs/concepts/cluster-administration/addons/) آشنا شوید که اغلب به‌صورت DaemonSet اجرا می‌شوند.
* `DaemonSet` یک منبع سطح بالا در REST API کوبرنتیز است.
  برای درک API مربوط به daemon setها، تعریف آبجکت
  {{< api-reference page="apps/daemon-set-v1" >}} را بخوانید.

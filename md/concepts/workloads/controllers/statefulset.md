---
reviewers:
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: StatefulSetها
api_metadata:
- apiVersion: "apps/v1"
  kind: "StatefulSet"
content_type: concept
description: >-
  یک StatefulSet گروهی از Podها را اجرا می‌کند و برای هر یک از آن Podها هویتی ماندگار حفظ می‌کند. این ویژگی برای مدیریت
  برنامه‌هایی که به ذخیره‌سازی پایدار یا هویت شبکه‌ای پایدار و یکتا نیاز دارند مفید است.
weight: 30
hide_summary: true # Listed separately in section index
---

<!-- overview -->

StatefulSet آبجکت API بار کاری است که برای مدیریت برنامه‌های دارای حالت (stateful) به کار می‌رود.

{{< glossary_definition term_id="statefulset" length="all" >}}

<!-- body -->

## استفاده از StatefulSetها

StatefulSetها برای برنامه‌هایی ارزشمند هستند که به یک یا چند مورد از موارد زیر
نیاز دارند:

* شناسه‌های شبکه‌ای پایدار و یکتا.
* ذخیره‌سازی پایدار و ماندگار.
* استقرار و مقیاس‌دهی مرتب و مسالمت‌آمیز (graceful).
* به‌روزرسانی‌های غلتان مرتب و خودکار.

در موارد بالا، «پایدار» به معنای ماندگاری در طول زمان‌بندی (مجدد) Pod است.
اگر برنامه‌ای به هیچ شناسه پایداری یا استقرار، حذف یا مقیاس‌دهی مرتب نیاز نداشته باشد،
باید برنامه خود را با استفاده از یک آبجکت بار کاری مستقر کنید
که مجموعه‌ای از replicaهای بدون حالت را فراهم می‌کند.
[Deployment](/docs/concepts/workloads/controllers/deployment/) یا
[ReplicaSet](/docs/concepts/workloads/controllers/replicaset/) ممکن است برای نیازهای بدون حالت شما مناسب‌تر باشند.

## محدودیت‌ها

* ذخیره‌سازی برای یک Pod مشخص باید یا توسط یک
  [PersistentVolume Provisioner](/docs/concepts/storage/dynamic-provisioning/)
  بر اساس _storage class_ درخواست‌شده تأمین شود، یا از پیش توسط یک مدیر تأمین شده باشد.
* حذف و/یا کاهش مقیاس یک StatefulSet، حجم‌های (volume) مرتبط با
  StatefulSet را حذف _نمی‌کند_. این کار برای تضمین ایمنی داده‌ها انجام می‌شود که به‌طور کلی ارزشمندتر از
  پاک‌سازی خودکار همه منابع مرتبط با StatefulSet است.
* StatefulSetها در حال حاضر به یک [Headless Service](/docs/concepts/services-networking/service/#headless-services)
  نیاز دارند که مسئول هویت شبکه‌ای Podها باشد. ایجاد این
  Service بر عهده شماست.
* StatefulSetها هنگام حذف یک StatefulSet، هیچ تضمینی درباره خاتمه Podها ارائه نمی‌دهند.
  برای دستیابی به خاتمه مرتب و مسالمت‌آمیز Podهای StatefulSet،
  می‌توان پیش از حذف، مقیاس StatefulSet را به 0 کاهش داد.
* هنگام استفاده از [به‌روزرسانی‌های غلتان](#rolling-updates) با
  [سیاست مدیریت Pod](#pod-management-policies) پیش‌فرض (`OrderedReady`)،
  ممکن است در وضعیتی معیوب قرار بگیرید که
  [برای ترمیم به مداخله دستی](#forced-rollback) نیاز دارد.

## مؤلفه‌ها

مثال زیر مؤلفه‌های یک StatefulSet را نشان می‌دهد.

{{% code_sample file="controllers/statefulset.yaml" %}}

{{< note >}}
این مثال برای سادگی از حالت دسترسی `ReadWriteOnce` استفاده می‌کند. برای
استفاده در محیط عملیاتی (production)، پروژه کوبرنتیز استفاده از حالت دسترسی `ReadWriteOncePod`
را توصیه می‌کند.
{{< /note >}}

در مثال بالا:

* یک Headless Service با نام `nginx` برای کنترل دامنه شبکه استفاده می‌شود.
* StatefulSet با نام `web` دارای یک Spec است که نشان می‌دهد 3 replica از کانتینر nginx در Podهای یکتا راه‌اندازی خواهند شد.
* `volumeClaimTemplates` با استفاده از
  [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) که توسط یک
  PersistentVolume Provisioner تأمین می‌شوند، ذخیره‌سازی پایدار فراهم می‌کند.

نام یک آبجکت StatefulSet باید یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) معتبر باشد.

### انتخابگر Pod

باید فیلد `.spec.selector` یک StatefulSet را طوری تنظیم کنید که با برچسب‌های
`.spec.template.metadata.labels` آن مطابقت داشته باشد. مشخص نکردن یک انتخابگر Pod منطبق، به
خطای اعتبارسنجی در هنگام ایجاد StatefulSet منجر می‌شود.

### قالب‌های درخواست حجم (Volume Claim Templates)

می‌توانید فیلد `.spec.volumeClaimTemplates` را برای ایجاد یک
[PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) تنظیم کنید.
این کار در صورتی ذخیره‌سازی پایدار برای StatefulSet فراهم می‌کند که یکی از شرایط زیر برقرار باشد:

* StorageClass مشخص‌شده برای درخواست حجم طوری تنظیم شده باشد که از [تأمین
  پویا](/docs/concepts/storage/dynamic-provisioning/) استفاده کند.
* کلاستر از قبل یک PersistentVolume با StorageClass درست
  و فضای ذخیره‌سازی در دسترس کافی داشته باشد.

### حداقل ثانیه‌های آمادگی

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

`.spec.minReadySeconds` یک فیلد اختیاری است که حداقل تعداد ثانیه‌هایی را مشخص می‌کند که یک Pod تازه
ایجادشده باید بدون از کار افتادن هیچ‌یک از کانتینرهایش در حال اجرا و آماده باشد تا در دسترس (available) در نظر گرفته شود.
از این فیلد برای بررسی پیشرفت یک rollout هنگام استفاده از راهبرد [به‌روزرسانی غلتان](#rolling-updates) استفاده می‌شود.
مقدار پیش‌فرض این فیلد 0 است (Pod به محض آماده شدن، در دسترس در نظر گرفته می‌شود). برای آشنایی بیشتر با اینکه
یک Pod چه زمانی آماده در نظر گرفته می‌شود، به [بررسی‌های کانتینر (Container Probes)](/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) مراجعه کنید.

## هویت Pod

Podهای StatefulSet هویتی یکتا دارند که از یک شماره ترتیبی، یک
هویت شبکه‌ای پایدار و یک ذخیره‌سازی پایدار تشکیل شده است. این هویت به Pod می‌چسبد،
صرف‌نظر از اینکه روی کدام نود زمان‌بندی (مجدد) شود.

### اندیس ترتیبی

برای یک StatefulSet با N [replica](#replicas)، به هر Pod در StatefulSet
یک شماره ترتیبی صحیح اختصاص داده می‌شود که در کل مجموعه یکتاست. به‌طور پیش‌فرض،
به Podها شماره‌های ترتیبی از 0 تا N-1 اختصاص داده می‌شود. کنترل‌کننده StatefulSet
همچنین یک برچسب Pod با این اندیس اضافه می‌کند: `apps.kubernetes.io/pod-index`.

### شماره ترتیبی آغازین

{{< feature-state feature_gate_name="StatefulSetStartOrdinal" >}}

`.spec.ordinals` یک فیلد اختیاری است که به شما امکان می‌دهد شماره‌های ترتیبی صحیحی را که
به هر Pod اختصاص داده می‌شود پیکربندی کنید. مقدار پیش‌فرض آن nil است. در این فیلد می‌توانید
گزینه‌های زیر را پیکربندی کنید:

* `.spec.ordinals.start`: اگر فیلد `.spec.ordinals.start` تنظیم شده باشد، به Podها
  شماره‌های ترتیبی از `.spec.ordinals.start` تا
  `.spec.ordinals.start + .spec.replicas - 1` اختصاص داده می‌شود.

### شناسه شبکه پایدار

هر Pod در یک StatefulSet نام میزبان (hostname) خود را از نام StatefulSet
و شماره ترتیبی Pod به دست می‌آورد. الگوی نام میزبان ساخته‌شده
`$(statefulset name)-$(ordinal)` است. مثال بالا سه Pod
با نام‌های `web-0,web-1,web-2` ایجاد می‌کند.
یک StatefulSet می‌تواند از یک [Headless Service](/docs/concepts/services-networking/service/#headless-services)
برای کنترل دامنه Podهای خود استفاده کند. دامنه‌ای که توسط این Service مدیریت می‌شود به این شکل است:
`$(service name).$(namespace).svc.cluster.local`، که در آن «cluster.local»
دامنه کلاستر است.
با ایجاد هر Pod، یک زیردامنه DNS متناظر به آن داده می‌شود که به این شکل است:
`$(podname).$(governing service domain)`، که در آن سرویس حاکم (governing service) توسط
فیلد `serviceName` در StatefulSet تعریف می‌شود.

بسته به نحوه پیکربندی DNS در کلاستر شما، ممکن است نتوانید نام DNS
یک Pod تازه اجراشده را بلافاصله جست‌وجو کنید. این رفتار زمانی رخ می‌دهد که کلاینت‌های دیگر در
کلاستر پیش از ایجاد Pod، پرس‌وجوهایی برای نام میزبان آن ارسال کرده باشند.
کش منفی (negative caching) که در DNS امری عادی است، به این معناست که نتایج جست‌وجوهای ناموفق قبلی
حتی پس از اجرا شدن Pod، دست‌کم برای چند ثانیه به خاطر سپرده شده و دوباره استفاده می‌شوند.

اگر نیاز دارید Podها را بلافاصله پس از ایجاد کشف کنید، چند گزینه دارید:

* به‌جای اتکا به جست‌وجوهای DNS، مستقیماً از API کوبرنتیز پرس‌وجو کنید (برای مثال با استفاده از watch).
* زمان کش کردن را در ارائه‌دهنده DNS کوبرنتیز خود کاهش دهید (معمولاً این به معنای ویرایش
  config map مربوط به CoreDNS است که در حال حاضر به مدت 30 ثانیه کش می‌کند).

همان‌طور که در بخش [محدودیت‌ها](#limitations) اشاره شد، ایجاد
[Headless Service](/docs/concepts/services-networking/service/#headless-services)
که مسئول هویت شبکه‌ای Podها است بر عهده شماست.

در اینجا چند نمونه از انتخاب‌های ممکن برای دامنه کلاستر، نام Service و
نام StatefulSet، و تأثیر آن‌ها بر نام‌های DNS مربوط به Podهای StatefulSet آمده است.

| دامنه کلاستر | Service (ns/name) | StatefulSet (ns/name) | دامنه StatefulSet              | DNS مربوط به Pod                                      | نام میزبان Pod |
| -------------- | ----------------- | --------------------- | ------------------------------- | -------------------------------------------- | ------------ |
| cluster.local  | default/nginx     | default/web           | nginx.default.svc.cluster.local | web-{0..N-1}.nginx.default.svc.cluster.local | web-{0..N-1} |
| cluster.local  | foo/nginx         | foo/web               | nginx.foo.svc.cluster.local     | web-{0..N-1}.nginx.foo.svc.cluster.local     | web-{0..N-1} |
| kube.local     | foo/nginx         | foo/web               | nginx.foo.svc.kube.local        | web-{0..N-1}.nginx.foo.svc.kube.local        | web-{0..N-1} |

{{< note >}}
دامنه کلاستر روی `cluster.local` تنظیم خواهد شد، مگر اینکه
[به شکل دیگری پیکربندی شده باشد](/docs/concepts/services-networking/dns-pod-service/).
{{< /note >}}

### ذخیره‌سازی پایدار

برای هر ورودی VolumeClaimTemplate که در یک StatefulSet تعریف شده است، هر Pod یک
PersistentVolumeClaim دریافت می‌کند. در مثال nginx بالا، هر Pod یک PersistentVolume واحد
با StorageClass برابر `my-storage-class` و 1 GiB ذخیره‌سازی تأمین‌شده دریافت می‌کند. اگر هیچ StorageClassای
مشخص نشده باشد، از StorageClass پیش‌فرض استفاده می‌شود. هنگامی که یک Pod روی یک نود زمان‌بندی (مجدد)
می‌شود، `volumeMounts` آن PersistentVolumeهای مرتبط با
PersistentVolume Claimهای آن را mount می‌کند. توجه داشته باشید که PersistentVolumeهای مرتبط با
PersistentVolume Claimهای Podها، هنگام حذف Podها یا StatefulSet حذف نمی‌شوند.
این کار باید به‌صورت دستی انجام شود.

### برچسب نام Pod

هنگامی که {{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} StatefulSet یک Pod ایجاد می‌کند،
برچسبی با نام `statefulset.kubernetes.io/pod-name` به آن اضافه می‌کند که مقدار آن برابر با نام
Pod است. این برچسب به شما امکان می‌دهد یک Service را به یک Pod مشخص در
StatefulSet متصل کنید.

### برچسب اندیس Pod

{{< feature-state feature_gate_name="PodIndexLabel" >}}

هنگامی که {{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} StatefulSet یک Pod ایجاد می‌کند،
Pod جدید با `apps.kubernetes.io/pod-index` برچسب‌گذاری می‌شود. مقدار این برچسب، اندیس ترتیبی
Pod است. این برچسب به شما امکان می‌دهد ترافیک را به یک اندیس Pod خاص هدایت کنید، لاگ‌ها/متریک‌ها را
با استفاده از برچسب اندیس Pod فیلتر کنید و کارهای دیگری انجام دهید. توجه داشته باشید که feature gate `PodIndexLabel` برای این
قابلیت به‌طور پیش‌فرض فعال و قفل شده است؛ برای غیرفعال کردن آن، کاربران باید از نسخه شبیه‌سازی‌شده سرور (server emulated version) v1.31 استفاده کنند.

## تضمین‌های استقرار و مقیاس‌دهی

* برای یک StatefulSet با N replica، هنگام استقرار Podها، آن‌ها به‌ترتیب و یکی پس از دیگری از {0..N-1} ایجاد می‌شوند.
* هنگام حذف Podها، آن‌ها به ترتیب معکوس، از {N-1..0}، خاتمه می‌یابند.
* پیش از اعمال یک عملیات مقیاس‌دهی روی یک Pod، همه Podهای پیش از آن باید Running و Ready باشند. اگر [`.spec.minReadySeconds`](#minimum-ready-seconds) تنظیم شده باشد، Podهای پیشین باید در دسترس باشند (دست‌کم به مدت `minReadySeconds` در وضعیت Ready باشند).
* پیش از خاتمه یافتن یک Pod، همه Podهای پس از آن باید به‌طور کامل خاموش شده باشند.

StatefulSet نباید `pod.Spec.TerminationGracePeriodSeconds` را برابر 0 مشخص کند. این کار
ناامن است و اکیداً توصیه نمی‌شود. برای توضیح بیشتر، به
[حذف اجباری Podهای StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/) مراجعه کنید.

هنگامی که مثال nginx بالا ایجاد شود، سه Pod به ترتیب
web-0، web-1 و web-2 مستقر می‌شوند. web-1 پیش از آنکه web-0
[Running و Ready](/docs/concepts/workloads/pods/pod-lifecycle/) شود مستقر نخواهد شد، و web-2 تا زمانی که
web-1 در وضعیت Running و Ready قرار نگیرد مستقر نخواهد شد. اگر web-0 پس از Running و Ready شدن web-1، اما پیش از
راه‌اندازی web-2 از کار بیفتد، web-2 تا زمانی که web-0 با موفقیت دوباره راه‌اندازی نشود و
در وضعیت Running و Ready قرار نگیرد، راه‌اندازی نخواهد شد.

اگر کاربری مقیاس مثال مستقرشده را با patch کردن StatefulSet به گونه‌ای تغییر دهد که
`replicas=1` شود، ابتدا web-2 خاتمه می‌یابد. web-1 تا زمانی که web-2
به‌طور کامل خاموش و حذف نشود، خاتمه نخواهد یافت. اگر web-0 پس از خاتمه یافتن و
خاموش شدن کامل web-2، اما پیش از خاتمه web-1 از کار بیفتد، web-1 تا زمانی که
web-0 در وضعیت Running و Ready قرار نگیرد، خاتمه نخواهد یافت.

### سیاست‌های مدیریت Pod

StatefulSet به شما امکان می‌دهد از طریق فیلد `.spec.podManagementPolicy` تضمین‌های ترتیبی آن را
تسهیل کنید، در حالی که تضمین‌های یکتایی و هویت آن حفظ می‌شوند.

#### مدیریت Pod به روش OrderedReady

مدیریت Pod به روش `OrderedReady` حالت پیش‌فرض برای StatefulSetها است. این روش رفتاری را که
در [تضمین‌های استقرار و مقیاس‌دهی](#deployment-and-scaling-guarantees) توضیح داده شد پیاده‌سازی می‌کند.

#### مدیریت موازی Pod

مدیریت Pod به روش `Parallel` به کنترل‌کننده StatefulSet می‌گوید که همه Podها را به‌صورت موازی راه‌اندازی یا
خاتمه دهد و پیش از راه‌اندازی یا خاتمه دادن Pod دیگری، منتظر Running
و Ready شدن یا خاتمه کامل Podها نماند.

در عملیات مقیاس‌دهی، این به آن معناست که همه Podها به‌طور هم‌زمان ایجاد یا خاتمه می‌یابند.

در به‌روزرسانی‌های غلتان، هنگامی که [`.spec.updateStrategy.rollingUpdate.maxUnavailable`](#maximum-unavailable-pods)
بزرگ‌تر از 1 باشد، کنترل‌کننده StatefulSet حداکثر به تعداد `maxUnavailable` Pod را
به‌طور هم‌زمان خاتمه داده و ایجاد می‌کند (که «bursting» نیز نامیده می‌شود). این کار می‌تواند به‌روزرسانی‌ها را سریع‌تر کند، اما ممکن است باعث شود Podها خارج از ترتیب آماده شوند که برای برنامه‌هایی که به ترتیب دقیق نیاز دارند مناسب نیست.

## راهبردهای به‌روزرسانی

فیلد `.spec.updateStrategy` یک StatefulSet به شما امکان می‌دهد به‌روزرسانی‌های غلتان خودکار را
برای کانتینرها، برچسب‌ها، درخواست‌ها/محدودیت‌های منابع و
حاشیه‌نویسی‌های Podهای یک StatefulSet پیکربندی یا غیرفعال کنید. سه مقدار ممکن وجود دارد:

`OnDelete`
: هنگامی که `.spec.updateStrategy.type` یک StatefulSet روی `OnDelete` تنظیم شده باشد،
  کنترل‌کننده StatefulSet، Podهای یک
  StatefulSet را به‌طور خودکار به‌روزرسانی نمی‌کند. کاربران باید Podها را به‌صورت دستی حذف کنند تا کنترل‌کننده
  Podهای جدیدی ایجاد کند که تغییرات اعمال‌شده در `.spec.template` یک StatefulSet را منعکس می‌کنند.

`RollingUpdate`
: راهبرد به‌روزرسانی `RollingUpdate` به‌روزرسانی‌های غلتان و خودکار را برای Podهای یک
  StatefulSet پیاده‌سازی می‌کند. این راهبرد، راهبرد به‌روزرسانی پیش‌فرض است.

`Recreate`
: {{< feature-state feature_gate_name="StatefulSetRecreateStrategy" >}}
  راهبرد به‌روزرسانی `Recreate` همه Podهای StatefulSet را پیش از ایجاد Podهای جدیدی
  که تغییرات اعمال‌شده در `.spec.template` یک StatefulSet را منعکس می‌کنند حذف می‌کند. استفاده از این
  راهبرد مستلزم فعال بودن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy) `StatefulSetRecreateStrategy`
  است. برای جزئیات به [Recreate](#recreate) مراجعه کنید.

## به‌روزرسانی‌های غلتان

هنگامی که `.spec.updateStrategy.type` یک StatefulSet روی `RollingUpdate` تنظیم شده باشد،
کنترل‌کننده StatefulSet هر Pod در StatefulSet را حذف و دوباره ایجاد می‌کند. این کار
به همان ترتیب خاتمه Podها (از بزرگ‌ترین شماره ترتیبی به کوچک‌ترین) پیش می‌رود و
هر بار یک Pod را به‌روزرسانی می‌کند.

control plane کوبرنتیز پیش از به‌روزرسانی Pod قبلی، منتظر می‌ماند تا Pod به‌روزرسانی‌شده در وضعیت Running و Ready
قرار گیرد. اگر `.spec.minReadySeconds` را تنظیم کرده باشید (به
[حداقل ثانیه‌های آمادگی](#minimum-ready-seconds) مراجعه کنید)، control plane پس از آماده شدن Pod، پیش از ادامه کار،
به همان مدت زمان نیز منتظر می‌ماند.

### به‌روزرسانی‌های غلتان بخش‌بندی‌شده {#partitions}

راهبرد به‌روزرسانی `RollingUpdate` را می‌توان با مشخص کردن
`.spec.updateStrategy.rollingUpdate.partition` بخش‌بندی کرد. اگر یک partition مشخص شده باشد، هنگام به‌روزرسانی
`.spec.template` در StatefulSet، همه Podهایی که شماره ترتیبی آن‌ها بزرگ‌تر یا مساوی partition است به‌روزرسانی می‌شوند.
همه Podهایی که شماره ترتیبی آن‌ها کمتر از partition است به‌روزرسانی نمی‌شوند و حتی اگر حذف شوند،
با نسخه قبلی دوباره ایجاد خواهند شد. اگر
`.spec.updateStrategy.rollingUpdate.partition` یک StatefulSet بزرگ‌تر از `.spec.replicas` آن باشد،
به‌روزرسانی‌های `.spec.template` آن به Podهایش منتقل نخواهند شد.
در بیشتر موارد نیازی به استفاده از partition نخواهید داشت، اما اگر بخواهید یک
به‌روزرسانی را مرحله‌بندی کنید، یک canary را منتشر کنید یا یک rollout مرحله‌ای انجام دهید، مفید هستند.

### حداکثر Podهای در دسترس نبودنی

{{< feature-state for_k8s_version="v1.35" state="beta" >}}

می‌توانید حداکثر تعداد Podهایی را که در طول یک به‌روزرسانی می‌توانند در دسترس نباشند،
با مشخص کردن فیلد `.spec.updateStrategy.rollingUpdate.maxUnavailable` کنترل کنید.
مقدار آن می‌تواند یک عدد مطلق (برای مثال `5`) یا درصدی از Podهای مطلوب
(برای مثال `10%`) باشد. عدد مطلق از مقدار درصدی
با گرد کردن به سمت بالا محاسبه می‌شود. این فیلد نمی‌تواند 0 باشد. مقدار پیش‌فرض 1 است.

این فیلد برای همه Podهای بازه `0` تا `replicas - 1` اعمال می‌شود. اگر هر
Pod در دسترس نبودنی در بازه `0` تا `replicas - 1` وجود داشته باشد، در شمارش
`maxUnavailable` به حساب می‌آید.

{{< note >}}
فیلد `maxUnavailable` در مرحله بتا قرار دارد و به‌طور پیش‌فرض فعال است.
{{< /note >}}

### بازگشت اجباری (Forced rollback)

هنگام استفاده از [به‌روزرسانی‌های غلتان](#rolling-updates) با
[سیاست مدیریت Pod](#pod-management-policies) پیش‌فرض (`OrderedReady`)،
ممکن است در وضعیتی معیوب قرار بگیرید که برای ترمیم به مداخله دستی نیاز دارد.

اگر قالب Pod را به پیکربندی‌ای به‌روزرسانی کنید که هرگز به وضعیت Running و
Ready نمی‌رسد (برای مثال، به دلیل یک فایل اجرایی معیوب یا خطای پیکربندی در سطح برنامه)،
StatefulSet روند rollout را متوقف کرده و منتظر می‌ماند.

در این وضعیت، بازگرداندن قالب Pod به یک پیکربندی سالم کافی نیست.
به دلیل یک [مشکل شناخته‌شده](https://github.com/kubernetes/kubernetes/issues/67250)،
StatefulSet همچنان منتظر می‌ماند تا Pod معیوب Ready شود
(که هرگز رخ نمی‌دهد) و پس از آن تلاش می‌کند آن را به پیکربندی
سالم بازگرداند.

پس از بازگرداندن قالب، باید همه Podهایی را که StatefulSet
پیش‌تر تلاش کرده بود با پیکربندی معیوب اجرا کند نیز حذف کنید.
سپس StatefulSet شروع به ایجاد مجدد Podها با استفاده از قالب بازگردانده‌شده می‌کند.

## Recreate

{{< feature-state feature_gate_name="StatefulSetRecreateStrategy" >}}

هنگامی که `.spec.updateStrategy.type` یک StatefulSet روی `Recreate` تنظیم شده باشد، کنترل‌کننده
StatefulSet همه Podهای StatefulSet را یکجا حذف می‌کند و پیش از ایجاد هر Pod جدیدی از `.spec.template` به‌روزرسانی‌شده،
منتظر می‌ماند تا به‌طور کامل خاتمه یابند. برخلاف
[`RollingUpdate`](#rolling-updates)، نسخه‌های قدیمی و جدید یک Pod هرگز
به‌طور هم‌زمان در حال اجرا نیستند، بنابراین این راهبرد در طول مدت به‌روزرسانی باعث قطعی سرویس (downtime) می‌شود. این رفتار مشابه
راهبرد `Recreate` در Deploymentها است و برای برنامه‌هایی مفید است که نمی‌توانند دو
نسخه را به‌طور هم‌زمان اجرا کنند، مانند بارهای کاری که به دسترسی انحصاری به یک منبع مشترک نیاز دارند
یا از قالب ذخیره‌سازی روی دیسکی استفاده می‌کنند که میان نسخه‌ها ناسازگار است.

حذف همیشه همه Podها را با هم حذف می‌کند، صرف‌نظر از
[سیاست مدیریت Pod](#pod-management-policies). پس از خاتمه یافتن همه Podها، Podهای جدید
طبق همان سیاست ایجاد می‌شوند: با `OrderedReady` (حالت پیش‌فرض)، Podها
یکی‌یکی و به ترتیب صعودی شماره ترتیبی دوباره ایجاد می‌شوند و پیش از ایجاد Pod بعدی، منتظر می‌ماند تا هر کدام در وضعیت Running و
Ready قرار گیرد؛ با `Parallel` همه Podها یکجا دوباره ایجاد می‌شوند.

از آنجا که این یک قابلیت آلفا است، برای استفاده از این راهبرد باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy) `StatefulSetRecreateStrategy`
را روی kube-controller-manager و kube-apiserver فعال کنید.

## تاریخچه نسخه‌ها (Revision history)

ControllerRevision یک منبع API کوبرنتیز است که کنترل‌کننده‌ها، مانند کنترل‌کننده StatefulSet، برای ردیابی تغییرات تاریخی پیکربندی از آن استفاده می‌کنند.

StatefulSetها از ControllerRevisionها برای نگهداری تاریخچه نسخه‌ها استفاده می‌کنند تا امکان بازگشت (rollback) و ردیابی نسخه‌ها فراهم شود.

### StatefulSetها چگونه تغییرات را با استفاده از ControllerRevisionها ردیابی می‌کنند

هنگامی که قالب Pod یک StatefulSet (`spec.template`) را به‌روزرسانی می‌کنید، کنترل‌کننده StatefulSet:

1. یک آبجکت ControllerRevision جدید آماده می‌کند
2. یک تصویر لحظه‌ای (snapshot) از قالب Pod و فراداده را ذخیره می‌کند
3. یک شماره نسخه افزایشی اختصاص می‌دهد

#### ویژگی‌های کلیدی

برای آشنایی بیشتر با ویژگی‌های کلیدی و سایر جزئیات، به [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/) مراجعه کنید.

---

### مدیریت تاریخچه نسخه‌ها

نسخه‌های نگهداری‌شده را با `.spec.revisionHistoryLimit` کنترل کنید:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: webapp
spec:
  revisionHistoryLimit: 5  # Keep last 5 revisions
  # ... other spec fields ...
```

* **پیش‌فرض**: در صورت مشخص نشدن، 10 نسخه نگهداری می‌شود
* **پاک‌سازی**: هنگامی که از محدودیت فراتر رود، قدیمی‌ترین نسخه‌ها توسط جمع‌آوری زباله حذف می‌شوند

#### انجام بازگشت (Rollback)

می‌توانید با استفاده از دستورات زیر به یک پیکربندی قبلی بازگردید:

```bash
# View revision history
kubectl rollout history statefulset/webapp

# Rollback to a specific revision
kubectl rollout undo statefulset/webapp --to-revision=3
```

این کار:

* قالب Pod نسخه 3 را اعمال می‌کند
* یک ControllerRevision جدید با شماره نسخه به‌روزشده ایجاد می‌کند

#### بررسی ControllerRevisionها

برای مشاهده ControllerRevisionهای مرتبط:

```bash
# List all revisions for the StatefulSet
kubectl get controllerrevisions -l app.kubernetes.io/name=webapp

# View detailed configuration of a specific revision
kubectl get controllerrevision/webapp-3 -o yaml
```

#### بهترین شیوه‌ها

##### سیاست نگهداری

- برای بیشتر بارهای کاری، `revisionHistoryLimit` را بین **5 تا 10** تنظیم کنید.
- تنها در صورتی که به **تاریخچه بازگشت عمیق** نیاز باشد، آن را افزایش دهید.

##### پایش

* نسخه‌ها را به‌طور منظم با فرمان زیر بررسی کنید:

  ```bash
  kubectl get controllerrevisions
  ```

- برای **رشد سریع تعداد نسخه‌ها** هشدار تنظیم کنید.

##### موارد اجتناب

* ویرایش دستی آبجکت‌های ControllerRevision.
* استفاده از نسخه‌ها به‌عنوان سازوکار پشتیبان‌گیری (از ابزارهای پشتیبان‌گیری واقعی استفاده کنید).
* تنظیم `revisionHistoryLimit: 0` (که قابلیت بازگشت را غیرفعال می‌کند).

## نگهداری PersistentVolumeClaim

{{< feature-state feature_gate_name="StatefulSetAutoDeletePVC" >}}

فیلد اختیاری `.spec.persistentVolumeClaimRetentionPolicy` کنترل می‌کند که آیا
و چگونه PVCها در طول چرخه عمر یک StatefulSet حذف شوند. برای استفاده از این فیلد باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `StatefulSetAutoDeletePVC`
را روی API server و controller manager فعال کنید.
پس از فعال‌سازی، دو سیاست وجود دارد که می‌توانید برای هر StatefulSet پیکربندی کنید:

`whenDeleted`
: رفتار نگهداری حجم را که هنگام حذف StatefulSet اعمال می‌شود پیکربندی می‌کند.

`whenScaled`
: رفتار نگهداری حجم را که هنگام کاهش تعداد replicaهای
  StatefulSet اعمال می‌شود پیکربندی می‌کند؛ برای مثال، هنگام کاهش مقیاس مجموعه.

برای هر سیاستی که می‌توانید پیکربندی کنید، می‌توانید مقدار را روی `Delete` یا `Retain` تنظیم کنید.

`Delete`
: PVCهایی که از `volumeClaimTemplate` در StatefulSet ایجاد شده‌اند، برای هر Pod
  تحت تأثیر این سیاست حذف می‌شوند. با سیاست `whenDeleted`، همه PVCهای حاصل از
  `volumeClaimTemplate` پس از حذف Podهایشان حذف می‌شوند. با سیاست
  `whenScaled`، تنها PVCهای متناظر با replicaهای Podای که مقیاسشان کاهش می‌یابد،
  پس از حذف Podهایشان حذف می‌شوند.

`Retain` (پیش‌فرض)
: PVCهای حاصل از `volumeClaimTemplate` هنگام حذف Podشان تحت تأثیر قرار
  نمی‌گیرند. این همان رفتار پیش از این قابلیت جدید است.

به خاطر داشته باشید که این سیاست‌ها **تنها** زمانی اعمال می‌شوند که Podها به دلیل
حذف یا کاهش مقیاس StatefulSet حذف می‌شوند. برای مثال، اگر یک Pod مرتبط با یک StatefulSet
به دلیل خرابی نود از کار بیفتد و control plane یک Pod جایگزین ایجاد کند، StatefulSet
PVC موجود را حفظ می‌کند. حجم موجود تحت تأثیر قرار نمی‌گیرد و کلاستر آن را به
نودی که Pod جدید قرار است روی آن راه‌اندازی شود متصل می‌کند.

مقدار پیش‌فرض سیاست‌ها `Retain` است که با رفتار StatefulSet پیش از این قابلیت جدید مطابقت دارد.

در اینجا نمونه‌ای از یک سیاست آمده است:

```yaml
apiVersion: apps/v1
kind: StatefulSet
...
spec:
  persistentVolumeClaimRetentionPolicy:
    whenDeleted: Retain
    whenScaled: Delete
...
```

{{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} StatefulSet
[ارجاع‌های مالک (owner references)](/docs/concepts/overview/working-with-objects/owners-dependents/#owner-references-in-object-specifications)
را به PVCهای خود اضافه می‌کند که سپس پس از خاتمه یافتن Pod، توسط {{<glossary_tooltip text="جمع‌آوری‌کننده زباله"
term_id="garbage-collection">}} حذف می‌شوند. این کار به Pod امکان می‌دهد پیش از حذف PVCها
(و پیش از حذف PV و حجم پشتیبان، بسته به سیاست نگهداری) همه حجم‌ها را به‌طور تمیز unmount کند.
هنگامی که سیاست `whenDeleted` را روی `Delete` تنظیم می‌کنید، یک ارجاع مالک به نمونه StatefulSet روی همه PVCهای
مرتبط با آن StatefulSet قرار داده می‌شود.

سیاست `whenScaled` باید PVCها را تنها زمانی حذف کند که مقیاس یک Pod کاهش یابد، نه زمانی که
یک Pod به دلیل دیگری حذف شود. هنگام تطبیق (reconcile)، کنترل‌کننده StatefulSet
تعداد replica مطلوب خود را با Podهای واقعی موجود در کلاستر مقایسه می‌کند. هر Pod متعلق به StatefulSet
که شناسه آن بزرگ‌تر از تعداد replicaها باشد، محکوم شده و برای حذف علامت‌گذاری می‌شود. اگر
سیاست `whenScaled` برابر `Delete` باشد، پیش از حذف Pod، Podهای محکوم ابتدا به‌عنوان مالک
PVCهای قالب StatefulSet مرتبط تنظیم می‌شوند. این کار باعث می‌شود PVCها
تنها پس از خاتمه یافتن Podهای محکوم، توسط جمع‌آوری زباله حذف شوند.

این بدان معناست که اگر کنترل‌کننده از کار بیفتد و دوباره راه‌اندازی شود، هیچ Podای پیش از
به‌روزرسانی مناسب ارجاع مالک آن مطابق با سیاست حذف نخواهد شد. اگر یک Pod محکوم
در زمانی که کنترل‌کننده از کار افتاده است به‌اجبار حذف شود، ممکن است ارجاع مالک
تنظیم شده باشد یا نشده باشد، بسته به اینکه کنترل‌کننده چه زمانی از کار افتاده است. ممکن است چندین حلقه تطبیق طول بکشد تا
ارجاع‌های مالک به‌روزرسانی شوند، بنابراین ممکن است برخی از Podهای محکوم ارجاع مالک را تنظیم کرده باشند و
برخی دیگر نه. به همین دلیل توصیه می‌کنیم منتظر بمانید تا کنترل‌کننده دوباره فعال شود؛
کنترل‌کننده پیش از خاتمه دادن Podها، ارجاع‌های مالک را بررسی می‌کند. اگر این کار ممکن نباشد،
اپراتور باید ارجاع‌های مالک روی PVCها را بررسی کند تا اطمینان حاصل شود که آبجکت‌های مورد انتظار
هنگام حذف اجباری Podها حذف می‌شوند.

### Replicaها

`.spec.replicas` یک فیلد اختیاری است که تعداد Podهای مطلوب را مشخص می‌کند. مقدار پیش‌فرض آن 1 است.

اگر مقیاس یک StatefulSet را به‌صورت دستی، از طریق `kubectl scale
statefulset statefulset --replicas=X`، تغییر دهید و سپس آن StatefulSet را
بر اساس یک مانیفست به‌روزرسانی کنید (برای مثال با اجرای `kubectl apply -f
statefulset.yaml`)، اعمال آن مانیفست، مقیاس‌دهی دستی را که پیش‌تر انجام داده‌اید
بازنویسی می‌کند.

اگر یک [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
(یا هر API مشابه دیگری برای مقیاس‌دهی افقی) مقیاس‌دهی یک
StatefulSet را مدیریت می‌کند، `.spec.replicas` را تنظیم نکنید. در عوض، اجازه دهید
{{<glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز
فیلد `.spec.replicas` را به‌طور خودکار مدیریت کند.

## {{% heading "whatsnext" %}}

* درباره [Podها](/docs/concepts/workloads/pods) بیاموزید.
* با نحوه استفاده از StatefulSetها آشنا شوید
  * مثال [استقرار یک برنامه دارای حالت](/docs/tutorials/stateful-application/basic-stateful-set/) را دنبال کنید.
  * مثال [استقرار Cassandra با Stateful Setها](/docs/tutorials/stateful-application/cassandra/) را دنبال کنید.
  * مثال [اجرای یک برنامه دارای حالت تکثیرشده](/docs/tasks/run-application/run-replicated-stateful-application/) را دنبال کنید.
  * بیاموزید چگونه [مقیاس یک StatefulSet را تغییر دهید](/docs/tasks/run-application/scale-stateful-set/).
  * بیاموزید هنگام [حذف یک StatefulSet](/docs/tasks/run-application/delete-stateful-set/) چه مراحلی در کار است.
  * بیاموزید چگونه [یک Pod را برای استفاده از یک حجم برای ذخیره‌سازی پیکربندی کنید](/docs/tasks/configure-pod-container/configure-volume-storage/).
  * بیاموزید چگونه [یک Pod را برای استفاده از یک PersistentVolume برای ذخیره‌سازی پیکربندی کنید](/docs/tutorials/configuration/configure-persistent-volume-storage/).
* `StatefulSet` یک منبع سطح بالا در REST API کوبرنتیز است.
  تعریف آبجکت {{< api-reference page="apps/stateful-set-v1" >}}
  را بخوانید تا API مربوط به stateful setها را درک کنید.
* درباره [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) و اینکه چگونه
  می‌توانید از آن برای مدیریت در دسترس بودن برنامه در هنگام اختلال‌ها استفاده کنید، مطالعه کنید.

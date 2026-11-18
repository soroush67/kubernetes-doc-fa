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
  هر StatefulSet گروهی از Podها را اجرا می‌کند و برای هر یک از آن‌ها هویتی ماندگار حفظ می‌کند. این قابلیت برای مدیریت
  برنامه‌هایی مفید است که به ذخیره‌سازی ماندگار یا هویت شبکه پایدار و یکتا نیاز دارند.
weight: 30
hide_summary: true # Listed separately in section index
---

<!-- overview -->

آبجکت StatefulSet آبجکتی از API بار کاری است که برای مدیریت برنامه‌های دارای حالت (stateful) به کار می‌رود.

{{< glossary_definition term_id="statefulset" length="all" >}}

<!-- body -->

## استفاده از StatefulSetها

استفاده از StatefulSetها برای برنامه‌هایی مفید است که به یک یا چند مورد از
ویژگی‌های زیر نیاز دارند:

* شناسه‌های شبکه پایدار و یکتا.
* ذخیره‌سازی پایدار و ماندگار.
* استقرار و مقیاس‌دهی مرتب و آرام (graceful).
* به‌روزرسانی‌های غلتان (rolling update) مرتب و خودکار.

در اینجا، «پایدار» به معنای ماندگاری در طول زمان‌بندی (یا زمان‌بندی دوباره) Pod است.
اگر برنامه‌ای به هیچ شناسه پایداری یا استقرار، حذف یا مقیاس‌دهی مرتب نیاز ندارد،
باید آن را با یک آبجکت بار کاری مستقر کنید که مجموعه‌ای از رپلیکاهای بدون حالت (stateless) فراهم می‌کند.
ممکن است [Deployment](/docs/concepts/workloads/controllers/deployment/) یا
[ReplicaSet](/docs/concepts/workloads/controllers/replicaset/) برای نیازهای بدون حالت شما مناسب‌تر باشند.

## محدودیت‌ها

* ذخیره‌سازی هر Pod یا باید با یک
  [تأمین‌کننده PersistentVolume](/docs/concepts/storage/dynamic-provisioning/)
  و بر اساس _کلاس ذخیره‌سازی_ (storage class) درخواست‌شده تأمین شود، یا مدیر کلاستر آن را از پیش تأمین کرده باشد.
* حذف StatefulSet یا کاهش مقیاس آن، حجم‌های (volume) مرتبط با آن را حذف _نمی‌کند_.
  این رفتار برای تضمین ایمنی داده‌ها است که معمولاً از پاک‌سازی خودکار همه منابع مرتبط با
  StatefulSet ارزشمندتر است.
* در حال حاضر StatefulSetها به یک [Service بدون سر (Headless Service)](/docs/concepts/services-networking/service/#headless-services)
  نیاز دارند که مسئول هویت شبکه Podها باشد. ایجاد این Service بر عهده شماست.
* StatefulSetها هنگام حذف شدن هیچ تضمینی درباره خاتمه Podها ارائه نمی‌دهند.
  برای خاتمه مرتب و آرام Podهای یک StatefulSet، می‌توانید پیش از حذف،
  مقیاس آن را به 0 کاهش دهید.
* هنگام استفاده از [به‌روزرسانی‌های غلتان](#rolling-updates) با
  [سیاست مدیریت Pod](#pod-management-policies) پیش‌فرض (`OrderedReady`)،
  ممکن است در وضعیتی خراب قرار بگیرید که برای
  [رفع آن به مداخله دستی](#forced-rollback) نیاز است.

## اجزا

مثال زیر اجزای یک StatefulSet را نشان می‌دهد.

{{% code_sample file="controllers/statefulset.yaml" %}}

{{< note >}}
این مثال برای سادگی از حالت دسترسی `ReadWriteOnce` استفاده می‌کند. پروژه کوبرنتیز
برای استفاده در محیط عملیاتی (production)، استفاده از حالت دسترسی `ReadWriteOncePod`
را توصیه می‌کند.
{{< /note >}}

در مثال بالا:

* یک Headless Service به نام `nginx` برای کنترل دامنه شبکه استفاده می‌شود.
* آبجکت StatefulSet به نام `web` مشخصاتی (Spec) دارد که تعیین می‌کند 3 رپلیکا از کانتینر nginx در Podهای یکتا اجرا شوند.
* فیلد `volumeClaimTemplates` با استفاده از
  [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/)یی که یک
  تأمین‌کننده PersistentVolume آن‌ها را تأمین می‌کند، ذخیره‌سازی پایدار فراهم می‌کند.

نام یک آبجکت StatefulSet باید یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) معتبر باشد.

### انتخابگر Pod

باید فیلد `.spec.selector` یک StatefulSet را طوری تنظیم کنید که با برچسب‌های
`.spec.template.metadata.labels` آن مطابقت داشته باشد. اگر انتخابگر (selector) Pod منطبقی مشخص نکنید،
هنگام ایجاد StatefulSet خطای اعتبارسنجی رخ می‌دهد.

### الگوهای درخواست حجم

می‌توانید فیلد `.spec.volumeClaimTemplates` را برای ایجاد یک
[PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) تنظیم کنید.
در صورتی که یکی از شرایط زیر برقرار باشد، این کار ذخیره‌سازی پایدار را برای StatefulSet فراهم می‌کند:

* کلاس ذخیره‌سازی (StorageClass) مشخص‌شده برای درخواست حجم طوری پیکربندی شده باشد که از
  [تأمین پویا](/docs/concepts/storage/dynamic-provisioning/) استفاده کند.
* کلاستر از قبل یک PersistentVolume با StorageClass درست و فضای ذخیره‌سازی
  کافیِ در دسترس داشته باشد.

### حداقل ثانیه‌های آماده بودن

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

فیلد `.spec.minReadySeconds` فیلدی اختیاری است که حداقل تعداد ثانیه‌هایی را مشخص می‌کند که یک Pod تازه
ایجادشده باید بدون از کار افتادن (crash) هیچ‌یک از کانتینرهایش در حال اجرا و آماده باشد تا در دسترس (available) در نظر گرفته شود.
از این فیلد برای بررسی پیشرفت یک انتشار (rollout) هنگام استفاده از راهبرد [به‌روزرسانی غلتان](#rolling-updates) استفاده می‌شود.
مقدار پیش‌فرض این فیلد 0 است (یعنی Pod به محض آماده شدن، در دسترس در نظر گرفته می‌شود). برای آشنایی بیشتر با اینکه
یک Pod چه زمانی آماده در نظر گرفته می‌شود، به [کاوشگرهای کانتینر](/docs/concepts/workloads/pods/pod-lifecycle/#container-probes) مراجعه کنید.

## هویت Pod

هر Pod در StatefulSet هویتی یکتا دارد که از یک شماره ترتیبی (ordinal)، یک
هویت شبکه پایدار و یک ذخیره‌سازی پایدار تشکیل می‌شود. این هویت، صرف‌نظر از اینکه
Pod روی کدام نود زمان‌بندی (یا دوباره زمان‌بندی) شود، همراه آن باقی می‌ماند.

### اندیس ترتیبی

در یک StatefulSet با N [رپلیکا](#replicas)، به هر Pod در StatefulSet
یک شماره ترتیبی صحیح اختصاص داده می‌شود که در کل مجموعه یکتاست. به‌طور پیش‌فرض،
شماره‌های ترتیبی از 0 تا N-1 به Podها اختصاص می‌یابد. کنترل‌کننده StatefulSet
همچنین برچسبی با این اندیس به Pod اضافه می‌کند: `apps.kubernetes.io/pod-index`.

### شماره ترتیبی آغازین

{{< feature-state feature_gate_name="StatefulSetStartOrdinal" >}}

فیلد `.spec.ordinals` فیلدی اختیاری است که با آن می‌توانید شماره‌های ترتیبی صحیحِ
اختصاص‌یافته به هر Pod را پیکربندی کنید. مقدار پیش‌فرض آن nil است. در این فیلد
می‌توانید گزینه‌های زیر را پیکربندی کنید:

* `.spec.ordinals.start`: اگر فیلد `.spec.ordinals.start` تنظیم شده باشد، شماره‌های ترتیبی
  از `.spec.ordinals.start` تا `.spec.ordinals.start + .spec.replicas - 1` به Podها
  اختصاص داده می‌شود.

### شناسه شبکه پایدار

هر Pod در یک StatefulSet نام میزبان (hostname) خود را از نام StatefulSet
و شماره ترتیبی Pod می‌گیرد. الگوی نام میزبان ساخته‌شده
`$(statefulset name)-$(ordinal)` است. مثال بالا سه Pod با نام‌های
`web-0,web-1,web-2` ایجاد می‌کند.
هر StatefulSet می‌تواند از یک [Headless Service](/docs/concepts/services-networking/service/#headless-services)
برای کنترل دامنه Podهای خود استفاده کند. دامنه‌ای که این Service مدیریت می‌کند به شکل
`$(service name).$(namespace).svc.cluster.local` است که در آن «cluster.local»
دامنه کلاستر است.
هنگام ایجاد هر Pod، یک زیردامنه DNS متناظر به شکل
`$(podname).$(governing service domain)` به آن داده می‌شود که در آن، Service حاکم (governing service)
با فیلد `serviceName` در StatefulSet تعریف می‌شود.

بسته به نحوه پیکربندی DNS در کلاستر شما، ممکن است نتوانید نام DNS یک Pod تازه اجراشده را
بلافاصله جستجو کنید. این رفتار زمانی رخ می‌دهد که کلاینت‌های دیگری در کلاستر، پیش از ایجاد Pod،
درخواست‌هایی برای نام میزبان آن ارسال کرده باشند. کش منفی (negative caching)، که در DNS امری عادی است،
به این معناست که نتایج جستجوهای ناموفق قبلی، حتی پس از اجرای Pod، دست‌کم برای چند ثانیه
به خاطر سپرده و دوباره استفاده می‌شوند.

اگر لازم است Podها را بلافاصله پس از ایجادشان پیدا کنید، چند گزینه در اختیار دارید:

* به‌جای تکیه بر جستجوهای DNS، مستقیماً از API کوبرنتیز پرس‌وجو کنید (برای مثال، با استفاده از watch).
* مدت زمان کش را در ارائه‌دهنده DNS کوبرنتیز خود کاهش دهید (معمولاً این کار به معنای ویرایش
  ConfigMap مربوط به CoreDNS است که در حال حاضر به مدت 30 ثانیه کش می‌کند).

همان‌طور که در بخش [محدودیت‌ها](#limitations) گفته شد، ایجاد
آن [Headless Service](/docs/concepts/services-networking/service/#headless-services)
که مسئول هویت شبکه Podهاست، بر عهده شماست.

در ادامه چند نمونه از انتخاب‌های ممکن برای دامنه کلاستر، نام Service و
نام StatefulSet آمده است، همراه با تأثیری که هر کدام بر نام‌های DNS مربوط به Podهای StatefulSet دارند.

| دامنه کلاستر | Service (فضای نام/نام) | StatefulSet (فضای نام/نام) | دامنه StatefulSet              | نام DNS مربوط به Pod                                      | نام میزبان Pod |
| -------------- | ----------------- | --------------------- | ------------------------------- | -------------------------------------------- | ------------ |
| cluster.local  | default/nginx     | default/web           | nginx.default.svc.cluster.local | web-{0..N-1}.nginx.default.svc.cluster.local | web-{0..N-1} |
| cluster.local  | foo/nginx         | foo/web               | nginx.foo.svc.cluster.local     | web-{0..N-1}.nginx.foo.svc.cluster.local     | web-{0..N-1} |
| kube.local     | foo/nginx         | foo/web               | nginx.foo.svc.kube.local        | web-{0..N-1}.nginx.foo.svc.kube.local        | web-{0..N-1} |

{{< note >}}
دامنه کلاستر روی `cluster.local` تنظیم می‌شود، مگر اینکه
[به شکل دیگری پیکربندی شده باشد](/docs/concepts/services-networking/dns-pod-service/).
{{< /note >}}

### ذخیره‌سازی پایدار

به ازای هر ورودی VolumeClaimTemplate که در یک StatefulSet تعریف شده است، هر Pod یک
PersistentVolumeClaim دریافت می‌کند. در مثال nginx بالا، هر Pod یک PersistentVolume
با StorageClass به نام `my-storage-class` و 1 GiB فضای ذخیره‌سازی تأمین‌شده دریافت می‌کند. اگر هیچ StorageClassی
مشخص نشده باشد، StorageClass پیش‌فرض استفاده می‌شود. هنگامی که یک Pod روی یک نود زمان‌بندی
(یا دوباره زمان‌بندی) می‌شود، `volumeMounts` آن، PersistentVolumeهای مرتبط با
PersistentVolumeClaimهای آن را متصل (mount) می‌کنند. توجه داشته باشید که PersistentVolumeهای مرتبط با
PersistentVolumeClaimهای Podها، با حذف Podها یا StatefulSet حذف نمی‌شوند.
این کار باید به‌صورت دستی انجام شود.

### برچسب نام Pod

هنگامی که {{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} StatefulSet یک Pod ایجاد می‌کند،
برچسب `statefulset.kubernetes.io/pod-name` را به آن اضافه می‌کند که مقدارش برابر با نام
Pod است. با این برچسب می‌توانید یک Service را به یک Pod خاص در
StatefulSet متصل کنید.

### برچسب اندیس Pod

{{< feature-state feature_gate_name="PodIndexLabel" >}}

هنگامی که {{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} StatefulSet یک Pod ایجاد می‌کند،
Pod جدید با برچسب `apps.kubernetes.io/pod-index` برچسب‌گذاری می‌شود. مقدار این برچسب، اندیس ترتیبی
Pod است. با این برچسب می‌توانید ترافیک را به یک اندیس Pod خاص هدایت کنید، لاگ‌ها و متریک‌ها را
با استفاده از برچسب اندیس Pod فیلتر کنید و کارهای دیگری انجام دهید. توجه داشته باشید که feature gate
`PodIndexLabel` برای این قابلیت به‌طور پیش‌فرض فعال و قفل شده است؛ برای غیرفعال کردن آن،
کاربران باید از نسخه شبیه‌سازی‌شده سرور (server emulated version) v1.31 استفاده کنند.

## تضمین‌های استقرار و مقیاس‌دهی

* در یک StatefulSet با N رپلیکا، هنگام استقرار Podها، آن‌ها یکی پس از دیگری و به ترتیب از {0..N-1} ایجاد می‌شوند.
* هنگام حذف Podها، آن‌ها به ترتیب معکوس، یعنی از {N-1..0}، خاتمه می‌یابند.
* پیش از اعمال یک عملیات مقیاس‌دهی روی یک Pod، همه Podهای پیش از آن باید در وضعیت Running و Ready باشند. اگر [`.spec.minReadySeconds`](#minimum-ready-seconds) تنظیم شده باشد، Podهای پیشین باید در دسترس باشند (یعنی دست‌کم به مدت `minReadySeconds` در وضعیت Ready باشند).
* پیش از خاتمه یک Pod، همه Podهای پس از آن باید به‌طور کامل خاموش شده باشند.

در StatefulSet نباید مقدار `pod.Spec.TerminationGracePeriodSeconds` برابر 0 تعیین شود. این کار
ناامن است و اکیداً توصیه نمی‌شود. برای توضیح بیشتر، به
[حذف اجباری Podهای StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/) مراجعه کنید.

هنگامی که مثال nginx بالا ایجاد شود، سه Pod به ترتیب web-0، web-1 و web-2
مستقر می‌شوند. تا زمانی که web-0 در وضعیت
[Running و Ready](/docs/concepts/workloads/pods/pod-lifecycle/) قرار نگیرد، web-1 مستقر نمی‌شود، و تا زمانی که
web-1 در وضعیت Running و Ready قرار نگیرد، web-2 مستقر نمی‌شود. اگر web-0 پس از Running و Ready شدن web-1
اما پیش از راه‌اندازی web-2 از کار بیفتد، web-2 تا زمانی که web-0 با موفقیت دوباره راه‌اندازی شود
و به وضعیت Running و Ready برسد، راه‌اندازی نمی‌شود.

اگر کاربری مقیاس مثال مستقرشده را با patch کردن StatefulSet به‌گونه‌ای تغییر دهد که
`replicas=1` شود، ابتدا web-2 خاتمه می‌یابد. تا زمانی که web-2 به‌طور کامل خاموش و حذف نشود،
web-1 خاتمه نمی‌یابد. اگر web-0 پس از خاتمه و خاموشی کامل web-2
اما پیش از خاتمه web-1 از کار بیفتد، web-1 تا زمانی که web-0 به وضعیت Running و Ready
برسد، خاتمه نمی‌یابد.

### سیاست‌های مدیریت Pod

با فیلد `.spec.podManagementPolicy` در StatefulSet می‌توانید تضمین‌های ترتیبی آن را سهل‌تر کنید
و در عین حال تضمین‌های یکتایی و هویت را حفظ کنید.

#### مدیریت Pod به روش OrderedReady

مدیریت Pod به روش `OrderedReady` حالت پیش‌فرض StatefulSetهاست. این روش رفتاری را پیاده‌سازی می‌کند
که در [تضمین‌های استقرار و مقیاس‌دهی](#deployment-and-scaling-guarantees) شرح داده شد.

#### مدیریت موازی Pod

مدیریت Pod به روش `Parallel` به کنترل‌کننده StatefulSet می‌گوید که همه Podها را به‌صورت موازی
راه‌اندازی یا خاتمه دهد و پیش از راه‌اندازی یا خاتمه Pod دیگر، منتظر نماند تا Podها
به وضعیت Running و Ready برسند یا به‌طور کامل خاتمه یابند.

در عملیات مقیاس‌دهی، این یعنی همه Podها به‌طور هم‌زمان ایجاد یا خاتمه داده می‌شوند.

در به‌روزرسانی‌های غلتان، زمانی که [`.spec.updateStrategy.rollingUpdate.maxUnavailable`](#maximum-unavailable-pods)
بزرگ‌تر از 1 باشد، کنترل‌کننده StatefulSet حداکثر به تعداد `maxUnavailable` Pod را به‌طور هم‌زمان
خاتمه می‌دهد و ایجاد می‌کند (که به آن «انفجاری» یا bursting نیز گفته می‌شود). این کار می‌تواند به‌روزرسانی‌ها را سریع‌تر کند، اما ممکن است باعث شود Podها خارج از ترتیب آماده شوند؛ این وضعیت ممکن است برای برنامه‌هایی که به ترتیب دقیق نیاز دارند مناسب نباشد.

## راهبردهای به‌روزرسانی

با فیلد `.spec.updateStrategy` در StatefulSet می‌توانید به‌روزرسانی‌های غلتان خودکار را
برای کانتینرها، برچسب‌ها، درخواست‌ها و محدودیت‌های منابع، و حاشیه‌نویسی‌های (annotation)
Podهای یک StatefulSet پیکربندی یا غیرفعال کنید. سه مقدار ممکن وجود دارد:

`OnDelete`
: هنگامی که `.spec.updateStrategy.type` در یک StatefulSet روی `OnDelete` تنظیم شده باشد،
  کنترل‌کننده StatefulSet، Podهای آن StatefulSet را به‌طور خودکار به‌روزرسانی نمی‌کند.
  کاربران باید Podها را به‌صورت دستی حذف کنند تا کنترل‌کننده Podهای جدیدی ایجاد کند
  که تغییرات اعمال‌شده در `.spec.template` آن StatefulSet را منعکس می‌کنند.

`RollingUpdate`
: راهبرد به‌روزرسانی `RollingUpdate` به‌روزرسانی‌های غلتان و خودکار را برای Podهای یک
  StatefulSet پیاده‌سازی می‌کند. این راهبرد، راهبرد به‌روزرسانی پیش‌فرض است.

`Recreate`
: {{< feature-state feature_gate_name="StatefulSetRecreateStrategy" >}}
  راهبرد به‌روزرسانی `Recreate` پیش از ایجاد Podهای جدیدی که تغییرات اعمال‌شده در
  `.spec.template` آن StatefulSet را منعکس می‌کنند، همه Podهای StatefulSet را حذف می‌کند.
  استفاده از این راهبرد مستلزم فعال بودن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy)
  `StatefulSetRecreateStrategy` است. برای جزئیات بیشتر، به [Recreate](#recreate) مراجعه کنید.

## به‌روزرسانی‌های غلتان

هنگامی که `.spec.updateStrategy.type` در یک StatefulSet روی `RollingUpdate` تنظیم شده باشد،
کنترل‌کننده StatefulSet هر Pod در StatefulSet را حذف و دوباره ایجاد می‌کند. این کار
با همان ترتیب خاتمه Podها (از بزرگ‌ترین شماره ترتیبی به کوچک‌ترین) انجام می‌شود و
در هر بار فقط یک Pod به‌روزرسانی می‌شود.

لایه control plane کوبرنتیز پیش از به‌روزرسانی Pod پیشین، منتظر می‌ماند تا Pod به‌روزرسانی‌شده
در وضعیت Running و Ready قرار گیرد. اگر `.spec.minReadySeconds` را تنظیم کرده باشید (به
[حداقل ثانیه‌های آماده بودن](#minimum-ready-seconds) مراجعه کنید)، control plane پس از آماده شدن Pod،
به همان مدت نیز صبر می‌کند و سپس کار را ادامه می‌دهد.

### به‌روزرسانی‌های غلتان پارتیشن‌بندی‌شده {#partitions}

راهبرد به‌روزرسانی `RollingUpdate` را می‌توان با تعیین
`.spec.updateStrategy.rollingUpdate.partition` پارتیشن‌بندی کرد. اگر پارتیشنی مشخص شده باشد،
با به‌روزرسانی `.spec.template` در StatefulSet، همه Podهایی که شماره ترتیبی آن‌ها بزرگ‌تر یا
مساوی پارتیشن است به‌روزرسانی می‌شوند. همه Podهایی که شماره ترتیبی آن‌ها کوچک‌تر از پارتیشن است
به‌روزرسانی نمی‌شوند و حتی اگر حذف شوند، با نسخه قبلی دوباره ایجاد می‌شوند. اگر
`.spec.updateStrategy.rollingUpdate.partition` در یک StatefulSet بزرگ‌تر از `.spec.replicas` آن باشد،
به‌روزرسانی‌های `.spec.template` به Podهای آن منتقل نمی‌شوند.
در بیشتر موارد نیازی به استفاده از پارتیشن ندارید، اما اگر بخواهید یک به‌روزرسانی را
مرحله‌بندی (stage) کنید، یک نسخه کاناری (canary) منتشر کنید یا انتشار را به‌صورت مرحله‌ای انجام دهید، پارتیشن‌ها مفید هستند.

### حداکثر تعداد Podهای غیرقابل‌دسترس

{{< feature-state feature_gate_name="MaxUnavailableStatefulSet" >}}

می‌توانید با تعیین فیلد `.spec.updateStrategy.rollingUpdate.maxUnavailable`، حداکثر تعداد
Podهایی را که در طول یک به‌روزرسانی می‌توانند در دسترس نباشند، کنترل کنید.
مقدار آن می‌تواند یک عدد مطلق (برای مثال، `5`) یا درصدی از Podهای مطلوب
(برای مثال، `10%`) باشد. عدد مطلق از مقدار درصدی و با گرد کردن به بالا
محاسبه می‌شود. این فیلد نمی‌تواند 0 باشد. مقدار پیش‌فرض آن 1 است.

این فیلد بر همه Podهای بازه `0` تا `replicas - 1` اعمال می‌شود. اگر Pod غیرقابل‌دسترسی
در بازه `0` تا `replicas - 1` وجود داشته باشد، در شمارش `maxUnavailable`
به حساب می‌آید.

### بازگشت اجباری

هنگام استفاده از [به‌روزرسانی‌های غلتان](#rolling-updates) با
[سیاست مدیریت Pod](#pod-management-policies) پیش‌فرض (`OrderedReady`)،
ممکن است در وضعیتی خراب قرار بگیرید که رفع آن به مداخله دستی نیاز دارد.

اگر الگوی Pod را به پیکربندی‌ای به‌روزرسانی کنید که هرگز به وضعیت Running و
Ready نمی‌رسد (برای مثال، به دلیل یک فایل باینری معیوب یا خطای پیکربندی در سطح برنامه)،
StatefulSet انتشار را متوقف می‌کند و منتظر می‌ماند.

در این وضعیت، برگرداندن الگوی Pod به یک پیکربندی سالم کافی نیست.
به دلیل یک [مشکل شناخته‌شده](https://github.com/kubernetes/kubernetes/issues/67250)،
StatefulSet پیش از آنکه برای برگرداندن Pod خراب به پیکربندی سالم تلاش کند،
همچنان منتظر می‌ماند تا آن Pod به وضعیت Ready برسد
(که هرگز رخ نمی‌دهد).

پس از برگرداندن الگو، باید همه Podهایی را نیز که StatefulSet پیش‌تر
تلاش کرده بود با پیکربندی نادرست اجرا کند، حذف کنید.
سپس StatefulSet ایجاد دوباره Podها را با استفاده از الگوی برگردانده‌شده آغاز می‌کند.

## بازسازی (Recreate)

{{< feature-state feature_gate_name="StatefulSetRecreateStrategy" >}}

اگر `.spec.updateStrategy.type` یک StatefulSet روی `Recreate` تنظیم شود، کنترل‌کنندهٔ StatefulSet همهٔ Podهای آن StatefulSet را یک‌جا حذف می‌کند. سپس صبر می‌کند تا همهٔ آن‌ها به‌طور کامل خاتمه یابند و تنها پس از آن، Podهای جدید را از `.spec.template` به‌روزشده ایجاد می‌کند. برخلاف [`RollingUpdate`](#rolling-updates)، نسخه‌های قدیمی و جدید یک Pod هرگز هم‌زمان اجرا نمی‌شوند؛ بنابراین این راهبرد در طول به‌روزرسانی باعث قطعی سرویس می‌شود. این رفتار مشابه راهبرد `Recreate` در Deploymentها است. این راهبرد برای برنامه‌هایی مناسب است که نمی‌توانند دو نسخه را هم‌زمان اجرا کنند؛ مانند بارهای کاری‌ای که به دسترسی انحصاری به یک منبع مشترک نیاز دارند، یا بارهای کاری‌ای که از قالب ذخیره‌سازی روی دیسک استفاده می‌کنند که میان نسخه‌ها ناسازگار است.

فرایند حذف، صرف‌نظر از [سیاست مدیریت Pod](#pod-management-policies)، همیشه همهٔ Podها را با هم حذف می‌کند. پس از خاتمهٔ همهٔ Podها، Podهای جدید مطابق همان سیاست ایجاد می‌شوند. با سیاست `OrderedReady` (پیش‌فرض)، Podها یکی‌یکی و به ترتیب صعودی شمارهٔ ترتیبی بازسازی می‌شوند و پیش از ایجاد Pod بعدی، کنترل‌کننده صبر می‌کند تا Pod قبلی به وضعیت Running و Ready برسد. با سیاست `Parallel`، همهٔ Podها یک‌جا بازسازی می‌شوند.

از آنجا که این قابلیت در مرحلهٔ آلفا است، برای استفاده از این راهبرد باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy) با نام `StatefulSetRecreateStrategy` را روی kube-controller-manager و kube-apiserver فعال کنید.

## تاریخچهٔ بازبینی‌ها

منبع ControllerRevision یکی از منابع API کوبرنتیز است که کنترل‌کننده‌ها، مانند کنترل‌کنندهٔ StatefulSet، از آن برای ردیابی تغییرات پیکربندی در طول زمان استفاده می‌کنند.

هر StatefulSet با استفاده از ControllerRevisionها تاریخچه‌ای از بازبینی‌ها نگه می‌دارد و به این ترتیب، بازگشت به نسخه‌های قبلی (rollback) و ردیابی نسخه‌ها ممکن می‌شود.

### نحوهٔ ردیابی تغییرات در StatefulSetها با استفاده از ControllerRevisionها

وقتی الگوی Pod یک StatefulSet (`spec.template`) را به‌روزرسانی می‌کنید، کنترل‌کنندهٔ StatefulSet:

1. یک آبجکت ControllerRevision جدید آماده می‌کند
2. یک نمای لحظه‌ای (snapshot) از الگوی Pod و فراداده‌ها را ذخیره می‌کند
3. یک شمارهٔ بازبینی افزایشی به آن اختصاص می‌دهد

#### ویژگی‌های کلیدی

برای آشنایی بیشتر با ویژگی‌های کلیدی و سایر جزئیات، به [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/) مراجعه کنید.

---

### مدیریت تاریخچهٔ بازبینی‌ها

تعداد بازبینی‌های نگه‌داشته‌شده را با `.spec.revisionHistoryLimit` کنترل کنید:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: webapp
spec:
  revisionHistoryLimit: 5  # Keep last 5 revisions
  # ... other spec fields ...
```

* **پیش‌فرض**: اگر مقداری تعیین نشود، ۱۰ بازبینی نگه داشته می‌شود
* **پاک‌سازی**: هنگامی که تعداد بازبینی‌ها از این حد فراتر رود، قدیمی‌ترین بازبینی‌ها با جمع‌آوری زباله (garbage collection) حذف می‌شوند

#### بازگشت به نسخهٔ قبلی

با دستورهای زیر می‌توانید به یک پیکربندی قبلی بازگردید:

```bash
# View revision history
kubectl rollout history statefulset/webapp

# Rollback to a specific revision
kubectl rollout undo statefulset/webapp --to-revision=3
```

این کار:

* الگوی Pod بازبینی ۳ را اعمال می‌کند
* یک ControllerRevision جدید با شمارهٔ بازبینی به‌روزشده ایجاد می‌کند

#### بررسی ControllerRevisionها

برای مشاهدهٔ ControllerRevisionهای مرتبط:

```bash
# List all revisions for the StatefulSet
kubectl get controllerrevisions -l app.kubernetes.io/name=webapp

# View detailed configuration of a specific revision
kubectl get controllerrevision/webapp-3 -o yaml
```

#### بهترین شیوه‌ها

##### سیاست نگه‌داری

- برای بیشتر بارهای کاری، مقدار `revisionHistoryLimit` را بین **۵ تا ۱۰** تنظیم کنید.
- فقط در صورتی این مقدار را افزایش دهید که به **تاریخچهٔ طولانی برای بازگشت** نیاز داشته باشید.

##### پایش

* بازبینی‌ها را به‌طور منظم با دستور زیر بررسی کنید:

  ```bash
  kubectl get controllerrevisions
  ```

- برای **رشد سریع تعداد بازبینی‌ها** هشدار تعریف کنید.

##### از این کارها پرهیز کنید

* ویرایش دستی آبجکت‌های ControllerRevision.
* استفاده از بازبینی‌ها به‌عنوان سازوکار پشتیبان‌گیری (از ابزارهای واقعی پشتیبان‌گیری استفاده کنید).
* تنظیم `revisionHistoryLimit: 0` (این کار قابلیت بازگشت به نسخهٔ قبلی را غیرفعال می‌کند).

## نگه‌داری PersistentVolumeClaim

{{< feature-state feature_gate_name="StatefulSetAutoDeletePVC" >}}

فیلد اختیاری `.spec.persistentVolumeClaimRetentionPolicy` تعیین می‌کند که آیا PVCها در طول چرخهٔ حیات یک StatefulSet حذف شوند یا نه، و اگر حذف می‌شوند، به چه شکلی. برای استفاده از این فیلد باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `StatefulSetAutoDeletePVC` را روی سرور API و مدیر کنترل‌کننده‌ها (controller manager) فعال کنید. پس از فعال‌سازی، دو سیاست وجود دارد که می‌توانید برای هر StatefulSet پیکربندی کنید:

`whenDeleted`
: رفتار نگه‌داری حجم‌ها را هنگام حذف StatefulSet پیکربندی می‌کند.

`whenScaled`
: رفتار نگه‌داری حجم‌ها را هنگام کاهش تعداد رونوشت‌های (replica) StatefulSet پیکربندی می‌کند؛ برای مثال، هنگام کوچک‌سازی مقیاس مجموعه.

برای هر یک از این سیاست‌ها می‌توانید مقدار `Delete` یا `Retain` را تنظیم کنید.

`Delete`
: PVCهایی که از `volumeClaimTemplate` در StatefulSet ایجاد شده‌اند، برای هر Podای که تحت تأثیر این سیاست قرار می‌گیرد حذف می‌شوند. با سیاست `whenDeleted`، همهٔ PVCهای ایجادشده از `volumeClaimTemplate` پس از حذف Podهایشان حذف می‌شوند. با سیاست `whenScaled`، فقط PVCهای مربوط به رونوشت‌هایی از Pod که مقیاسشان کاهش می‌یابد، پس از حذف Podهایشان حذف می‌شوند.

`Retain` (پیش‌فرض)
: حذف Pod هیچ تأثیری بر PVCهای ایجادشده از `volumeClaimTemplate` آن ندارد. این همان رفتار پیش از معرفی این قابلیت جدید است.

توجه داشته باشید که این سیاست‌ها **فقط** زمانی اعمال می‌شوند که Podها به دلیل حذف StatefulSet یا کاهش مقیاس آن حذف شوند. برای مثال، اگر یک Pod مرتبط با StatefulSet به دلیل خرابی نود از کار بیفتد و control plane یک Pod جایگزین ایجاد کند، StatefulSet همان PVC موجود را نگه می‌دارد. حجم موجود دست‌نخورده باقی می‌ماند و کلاستر آن را به نودی متصل می‌کند که Pod جدید قرار است روی آن راه‌اندازی شود.

مقدار پیش‌فرض این سیاست‌ها `Retain` است که با رفتار StatefulSet پیش از معرفی این قابلیت جدید مطابقت دارد.

در ادامه نمونه‌ای از این سیاست آمده است:

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

{{<glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller">}} StatefulSet به PVCهای خود [ارجاع‌های مالک](/docs/concepts/overview/working-with-objects/owners-dependents/#owner-references-in-object-specifications) (owner reference) اضافه می‌کند تا پس از خاتمهٔ Pod، {{<glossary_tooltip text="جمع‌آوری‌کنندهٔ زباله"
term_id="garbage-collection">}} آن‌ها را حذف کند. به این ترتیب، Pod می‌تواند پیش از حذف PVCها (و بسته به سیاست نگه‌داری، پیش از حذف PV و حجم پشتیبان آن‌ها) همهٔ حجم‌ها را به‌طور تمیز جدا (unmount) کند. وقتی سیاست `whenDeleted` را روی `Delete` تنظیم می‌کنید، یک ارجاع مالک به نمونهٔ StatefulSet روی همهٔ PVCهای مرتبط با آن StatefulSet قرار داده می‌شود.

سیاست `whenScaled` باید PVCها را فقط هنگام کاهش مقیاس یک Pod حذف کند، نه زمانی که Pod به دلیل دیگری حذف می‌شود. کنترل‌کنندهٔ StatefulSet هنگام همسان‌سازی (reconcile)، تعداد رونوشت‌های مطلوب خود را با Podهای واقعی موجود در کلاستر مقایسه می‌کند. هر Pod متعلق به StatefulSet که شناسه‌اش بزرگ‌تر از تعداد رونوشت‌ها باشد، محکوم به حذف شده و برای حذف علامت‌گذاری می‌شود. اگر سیاست `whenScaled` روی `Delete` تنظیم شده باشد، Podهای محکوم به حذف پیش از حذف شدن، به‌عنوان مالک PVCهای مرتبط با الگوی StatefulSet تعیین می‌شوند. در نتیجه، این PVCها فقط پس از خاتمهٔ Podهای محکوم به حذف، با جمع‌آوری زباله حذف می‌شوند.

بنابراین اگر کنترل‌کننده از کار بیفتد و دوباره راه‌اندازی شود، هیچ Podای پیش از آنکه ارجاع مالک آن متناسب با سیاست به‌روزرسانی شود، حذف نخواهد شد. اگر یک Pod محکوم به حذف در زمانی که کنترل‌کننده از کار افتاده است به‌اجبار حذف شود، بسته به زمان از کار افتادن کنترل‌کننده، ممکن است ارجاع مالک آن تنظیم شده باشد یا نشده باشد. به‌روزرسانی ارجاع‌های مالک ممکن است به چندین حلقهٔ همسان‌سازی نیاز داشته باشد؛ بنابراین ممکن است برای برخی از Podهای محکوم به حذف ارجاع مالک تنظیم شده باشد و برای برخی دیگر نه. به همین دلیل توصیه می‌کنیم صبر کنید تا کنترل‌کننده دوباره به کار بیفتد؛ کنترل‌کننده پیش از خاتمه دادن به Podها، ارجاع‌های مالک را بررسی می‌کند. اگر این کار ممکن نیست، اپراتور باید ارجاع‌های مالک روی PVCها را بررسی کند تا مطمئن شود هنگام حذف اجباری Podها، آبجکت‌های مورد انتظار حذف می‌شوند.

### رونوشت‌ها

فیلد اختیاری `.spec.replicas` تعداد Podهای مطلوب را مشخص می‌کند. مقدار پیش‌فرض آن ۱ است.

اگر مقیاس یک StatefulSet را به‌صورت دستی و با دستور `kubectl scale
statefulset statefulset --replicas=X` تغییر دهید و سپس آن StatefulSet را بر اساس یک مانیفست به‌روزرسانی کنید (برای مثال با اجرای `kubectl apply -f
statefulset.yaml`)، اعمال آن مانیفست، تغییر مقیاس دستی قبلی شما را بازنویسی می‌کند.

اگر یک [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (یا هر API مشابهی برای مقیاس‌دهی افقی) مدیریت مقیاس یک StatefulSet را بر عهده دارد، `.spec.replicas` را تنظیم نکنید. در عوض، اجازه دهید {{<glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز فیلد `.spec.replicas` را به‌طور خودکار مدیریت کند.

## {{% heading "whatsnext" %}}

* دربارهٔ [Podها](/docs/concepts/workloads/pods) بیاموزید.
* با نحوهٔ استفاده از StatefulSetها آشنا شوید
  * نمونهٔ [استقرار یک برنامهٔ دارای حالت](/docs/tutorials/stateful-application/basic-stateful-set/) را دنبال کنید.
  * نمونهٔ [استقرار Cassandra با StatefulSetها](/docs/tutorials/stateful-application/cassandra/) را دنبال کنید.
  * نمونهٔ [اجرای یک برنامهٔ دارای حالت تکثیرشده](/docs/tasks/run-application/run-replicated-stateful-application/) را دنبال کنید.
  * بیاموزید چگونه [مقیاس یک StatefulSet را تغییر دهید](/docs/tasks/run-application/scale-stateful-set/).
  * بیاموزید [حذف یک StatefulSet](/docs/tasks/run-application/delete-stateful-set/) چه مراحلی دارد.
  * بیاموزید چگونه [یک Pod را برای استفاده از حجم برای ذخیره‌سازی پیکربندی کنید](/docs/tasks/configure-pod-container/configure-volume-storage/).
  * بیاموزید چگونه [یک Pod را برای استفاده از PersistentVolume برای ذخیره‌سازی پیکربندی کنید](/docs/tutorials/configuration/configure-persistent-volume-storage/).
* منبع `StatefulSet` یک منبع سطح بالا در REST API کوبرنتیز است.
  برای درک API مربوط به StatefulSetها، تعریف آبجکت {{< api-reference page="apps/stateful-set-v1" >}} را مطالعه کنید.
* دربارهٔ [PodDisruptionBudget](/docs/concepts/workloads/pods/disruptions/) و نحوهٔ استفاده از آن برای مدیریت دسترس‌پذیری برنامه در هنگام اختلال‌ها مطالعه کنید.

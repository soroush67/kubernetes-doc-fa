---
reviewers:
- jayunit100
- jsturtevant
- marosset
- perithompson
title: کانتینرهای ویندوز در کوبرنتیز
content_type: concept
weight: 65
---

<!-- overview -->

بخش بزرگی از سرویس‌ها و برنامه‌هایی که در بسیاری از سازمان‌ها اجرا می‌شوند، برنامه‌های ویندوزی هستند. [کانتینرهای ویندوز](https://aka.ms/windowscontainers) روشی برای کپسوله‌کردن فرایندها و بسته‌بندی وابستگی‌ها فراهم می‌کنند. به این ترتیب، به‌کارگیری شیوه‌های DevOps و پیروی از الگوهای بومی ابر (cloud native) برای برنامه‌های ویندوزی آسان‌تر می‌شود.

سازمان‌هایی که روی برنامه‌های مبتنی بر ویندوز و برنامه‌های مبتنی بر لینوکس سرمایه‌گذاری کرده‌اند، برای مدیریت بارهای کاری خود به هماهنگ‌کننده‌های (orchestrator) جداگانه نیاز ندارند. نتیجه‌ی این کار، افزایش بهره‌وری عملیاتی در همه‌ی استقرارهای آن‌ها، صرف‌نظر از سیستم‌عامل، است.

<!-- body -->

## نودهای ویندوز در کوبرنتیز

برای فعال‌کردن هماهنگ‌سازی کانتینرهای ویندوز در کوبرنتیز، نودهای ویندوز را به کلاستر لینوکسی موجود خود اضافه کنید. زمان‌بندی کانتینرهای ویندوز در {{< glossary_tooltip text="پادها" term_id="pod" >}} در کوبرنتیز، مشابه زمان‌بندی کانتینرهای مبتنی بر لینوکس است.

برای اجرای کانتینرهای ویندوز، کلاستر کوبرنتیز شما باید چند سیستم‌عامل را در بر بگیرد. هرچند {{< glossary_tooltip text="control plane" term_id="control-plane" >}} را فقط می‌توان روی لینوکس اجرا کرد، نودهای کارگر (worker) را می‌توانید با ویندوز یا لینوکس مستقر کنید.

{{< glossary_tooltip text="نودهای" term_id="node" >}} ویندوز به این شرط [پشتیبانی می‌شوند](#windows-os-version-support) که سیستم‌عامل آن‌ها Windows Server 2022 یا Windows Server 2025 باشد.

در این سند، اصطلاح *کانتینرهای ویندوز* به معنای کانتینرهای ویندوز با جداسازی فرایند (process isolation) است. کوبرنتیز از اجرای کانتینرهای ویندوز با [جداسازی Hyper-V](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container) پشتیبانی نمی‌کند.

## سازگاری و محدودیت‌ها {#limitations}

برخی از قابلیت‌های نود فقط در صورت استفاده از یک [محیط اجرای کانتینر](#container-runtime) خاص در دسترس هستند و برخی دیگر روی نودهای ویندوز در دسترس نیستند، از جمله:

* HugePages: برای کانتینرهای ویندوز پشتیبانی نمی‌شود
* کانتینرهای ممتاز (privileged): برای کانتینرهای ویندوز پشتیبانی نمی‌شوند. [کانتینرهای HostProcess](/docs/tasks/configure-pod-container/create-hostprocess-pod/) قابلیت مشابهی ارائه می‌دهند.
* TerminationGracePeriod: به containerD نیاز دارد

همه‌ی قابلیت‌های فضاهای نام (namespace) مشترک پشتیبانی نمی‌شوند. برای جزئیات بیشتر، [سازگاری API](#api) را ببینید.

برای جزئیات نسخه‌های ویندوزی که کوبرنتیز روی آن‌ها آزمایش می‌شود، [سازگاری نسخه‌ی سیستم‌عامل ویندوز](#windows-os-version-support) را ببینید.

از دیدگاه API و kubectl، کانتینرهای ویندوز تقریباً همانند کانتینرهای مبتنی بر لینوکس رفتار می‌کنند. با این حال، در برخی از قابلیت‌های کلیدی تفاوت‌های قابل‌توجهی وجود دارد که در این بخش شرح داده شده‌اند.

### مقایسه با لینوکس {#compatibility-linux-similarities}

عناصر کلیدی کوبرنتیز در ویندوز به همان شیوه‌ای کار می‌کنند که در لینوکس. این بخش به چند انتزاع کلیدی بار کاری و نحوه‌ی نگاشت آن‌ها به ویندوز می‌پردازد.

* [پادها](/docs/concepts/workloads/pods/)

  هر Pod واحد سازنده‌ی پایه‌ی کوبرنتیز است؛ یعنی کوچک‌ترین و ساده‌ترین واحد در مدل آبجکت کوبرنتیز که ایجاد یا مستقر می‌کنید. نمی‌توانید کانتینرهای ویندوز و لینوکس را در یک Pod مستقر کنید. همه‌ی کانتینرهای یک Pod روی یک نود زمان‌بندی می‌شوند و هر نود نمایانگر یک پلتفرم و معماری مشخص است. قابلیت‌ها، ویژگی‌ها و رویدادهای زیر از Pod با کانتینرهای ویندوز پشتیبانی می‌شوند:

  * یک یا چند کانتینر در هر Pod با جداسازی فرایند و اشتراک حجم (volume)
  * فیلدهای `status` در Pod
  * کاوشگرهای (probe) آمادگی، زنده‌بودن و راه‌اندازی
  * قلاب‌های (hook) چرخه‌ی عمر کانتینر postStart و preStop
  * ConfigMap و Secretها: به‌صورت متغیرهای محیطی یا حجم
  * حجم‌های `emptyDir`
  * اتصال (mount) لوله‌های نام‌دار (named pipe) میزبان
  * محدودیت‌های منابع
  * فیلد سیستم‌عامل:

    برای اینکه مشخص شود Pod فعلی از کانتینرهای ویندوز استفاده می‌کند، فیلد `.spec.os.name` باید روی `windows` تنظیم شود.

    اگر فیلد `.spec.os.name` را روی `windows` تنظیم کنید، نباید فیلدهای زیر را در `.spec` آن Pod تنظیم کنید:

    * `spec.hostPID`
    * `spec.hostIPC`
    * `spec.securityContext.seLinuxOptions`
    * `spec.securityContext.seccompProfile`
    * `spec.securityContext.fsGroup`
    * `spec.securityContext.fsGroupChangePolicy`
    * `spec.securityContext.sysctls`
    * `spec.shareProcessNamespace`
    * `spec.securityContext.runAsUser`
    * `spec.securityContext.runAsGroup`
    * `spec.securityContext.supplementalGroups`
    * `spec.containers[*].securityContext.seLinuxOptions`
    * `spec.containers[*].securityContext.seccompProfile`
    * `spec.containers[*].securityContext.capabilities`
    * `spec.containers[*].securityContext.readOnlyRootFilesystem`
    * `spec.containers[*].securityContext.privileged`
    * `spec.containers[*].securityContext.allowPrivilegeEscalation`
    * `spec.containers[*].securityContext.procMount`
    * `spec.containers[*].securityContext.runAsUser`
    * `spec.containers[*].securityContext.runAsGroup`

    در فهرست بالا، نویسه‌ی عام (`*`) به معنای همه‌ی عناصر یک فهرست است. برای مثال، `spec.containers[*].securityContext` به آبجکت SecurityContext همه‌ی کانتینرها اشاره دارد. اگر هر یک از این فیلدها مشخص شده باشد، سرور API آن Pod را نمی‌پذیرد.

* [منابع بار کاری](/docs/concepts/workloads/controllers/)، از جمله:
  * ReplicaSet
  * Deployment
  * StatefulSet
  * DaemonSet
  * Job
  * CronJob
  * ReplicationController
* {{< glossary_tooltip text="سرویس‌ها" term_id="service" >}}
  برای جزئیات بیشتر، [توزیع بار و سرویس‌ها](/docs/concepts/services-networking/windows-networking/#load-balancing-and-services) را ببینید.

پادها، منابع بار کاری و سرویس‌ها عناصری حیاتی برای مدیریت بارهای کاری ویندوز در کوبرنتیز هستند. با این حال، این عناصر به‌تنهایی برای مدیریت درست چرخه‌ی عمر بارهای کاری ویندوز در یک محیط پویای بومی ابر کافی نیستند.

* `kubectl exec`
* متریک‌های Pod و کانتینر
* {{< glossary_tooltip text="مقیاس‌دهی خودکار افقی پاد" term_id="horizontal-pod-autoscaler" >}}
* {{< glossary_tooltip text="سهمیه‌های منابع" term_id="resource-quota" >}}
* پیش‌دستی (preemption) زمان‌بند

### گزینه‌های خط فرمان kubelet {#kubelet-compatibility}

همان‌طور که در ادامه شرح داده شده است، برخی از گزینه‌های خط فرمان kubelet در ویندوز رفتار متفاوتی دارند:

* با `--windows-priorityclass` می‌توانید اولویت زمان‌بندی فرایند kubelet را تنظیم کنید (بخش [مدیریت منبع CPU](/docs/concepts/configuration/windows-resource-management/#resource-management-cpu) را ببینید)
* پرچم‌های `--kube-reserved`، `--system-reserved` و `--eviction-hard` مقدار [NodeAllocatable](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) را به‌روزرسانی می‌کنند
* بیرون‌راندن (eviction) با استفاده از `--enforce-node-allocable` پیاده‌سازی نشده است
* هنگام اجرا روی نود ویندوز، kubelet هیچ محدودیتی برای حافظه یا CPU ندارد. پرچم‌های `--kube-reserved` و `--system-reserved` فقط از `NodeAllocatable` کم می‌کنند و منابع فراهم‌شده برای بارهای کاری را تضمین نمی‌کنند. برای اطلاعات بیشتر، [مدیریت منابع برای نودهای ویندوز](/docs/concepts/configuration/windows-resource-management/#resource-reservation) را ببینید.
* وضعیت (Condition) `PIDPressure` پیاده‌سازی نشده است
* kubelet هیچ اقدامی برای بیرون‌راندن به دلیل کمبود حافظه (OOM) انجام نمی‌دهد

### سازگاری API {#api}

به دلیل تفاوت سیستم‌عامل و محیط اجرای کانتینر، نحوه‌ی کار APIهای کوبرنتیز در ویندوز تفاوت‌های ظریفی دارد. برخی از ویژگی‌های بار کاری برای لینوکس طراحی شده‌اند و در ویندوز اجرا نمی‌شوند.

در سطح کلی، این مفاهیم سیستم‌عامل با هم تفاوت دارند:

* هویت - لینوکس از شناسه‌ی کاربر (UID) و شناسه‌ی گروه (GID) استفاده می‌کند که به‌صورت نوع عدد صحیح نمایش داده می‌شوند. نام‌های کاربر و گروه مرجع اصلی نیستند؛ آن‌ها صرفاً نام مستعاری در `/etc/groups` یا `/etc/passwd` هستند که به UID+GID برمی‌گردند. ویندوز از یک [شناسه‌ی امنیتی](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers) (SID) دودویی بزرگ‌تر استفاده می‌کند که در پایگاه داده‌ی Windows Security Access Manager (SAM) ذخیره می‌شود. این پایگاه داده نه بین میزبان و کانتینرها و نه بین خود کانتینرها به اشتراک گذاشته نمی‌شود.
* مجوزهای فایل - ویندوز از فهرست کنترل دسترسی مبتنی بر SIDها استفاده می‌کند، در حالی که سیستم‌های POSIX مانند لینوکس از یک ماسک بیتی مبتنی بر مجوزهای آبجکت و UID+GID، به‌علاوه‌ی فهرست‌های کنترل دسترسی _اختیاری_، استفاده می‌کنند.
* مسیرهای فایل - قرارداد رایج در ویندوز استفاده از `\` به جای `/` است. کتابخانه‌های IO زبان Go معمولاً هر دو را می‌پذیرند و به‌درستی کار می‌کنند، اما هنگام تنظیم مسیر یا خط فرمانی که داخل کانتینر تفسیر می‌شود، ممکن است به `\` نیاز باشد.
* سیگنال‌ها - برنامه‌های تعاملی ویندوز خاتمه را به شیوه‌ی متفاوتی مدیریت می‌کنند و می‌توانند یک یا چند مورد از سازوکارهای زیر را پیاده‌سازی کنند:
  * یک رشته‌ی (thread) رابط کاربری، پیام‌های تعریف‌شده‌ای از جمله `WM_CLOSE` را مدیریت می‌کند.
  * برنامه‌های کنسولی Ctrl-C یا Ctrl-break را با استفاده از یک Control Handler مدیریت می‌کنند.
  * سرویس‌ها یک تابع Service Control Handler ثبت می‌کنند که می‌تواند کدهای کنترلی `SERVICE_CONTROL_STOP` را بپذیرد.

کدهای خروج کانتینر از همان قرارداد پیروی می‌کنند: مقدار ۰ به معنای موفقیت و مقدار غیرصفر به معنای شکست است. کدهای خطای مشخص ممکن است در ویندوز و لینوکس متفاوت باشند. با این حال، کدهای خروجی که مؤلفه‌های کوبرنتیز (kubelet و kube-proxy) منتقل می‌کنند، بدون تغییر باقی می‌مانند.

#### سازگاری فیلدها برای مشخصات کانتینر {#compatibility-v1-pod-spec-containers}

فهرست زیر تفاوت‌های نحوه‌ی کار مشخصات کانتینرهای Pod را در ویندوز و لینوکس شرح می‌دهد:

* صفحات بزرگ (huge pages) در محیط اجرای کانتینر ویندوز پیاده‌سازی نشده‌اند و در دسترس نیستند. این صفحات به [احراز یک امتیاز کاربری](https://docs.microsoft.com/en-us/windows/desktop/Memory/large-page-support) نیاز دارند که برای کانتینرها قابل پیکربندی نیست.
* `requests.cpu` و `requests.memory` - درخواست‌ها از منابع در دسترس نود کم می‌شوند، بنابراین می‌توان از آن‌ها برای جلوگیری از تخصیص بیش از ظرفیت (overprovisioning) یک نود استفاده کرد. با این حال، نمی‌توان از آن‌ها برای تضمین منابع در نودی که بیش از ظرفیت تخصیص یافته است استفاده کرد. اگر اپراتور بخواهد به‌طور کامل از تخصیص بیش از ظرفیت جلوگیری کند، بهتر است این درخواست‌ها را روی همه‌ی کانتینرها اعمال کند.
* `securityContext.allowPrivilegeEscalation` -
   در ویندوز امکان‌پذیر نیست؛ هیچ‌یک از قابلیت‌ها (capabilities) متصل نشده‌اند
* `securityContext.capabilities` -
   قابلیت‌های POSIX در ویندوز پیاده‌سازی نشده‌اند
* `securityContext.privileged` -
   ویندوز از کانتینرهای ممتاز پشتیبانی نمی‌کند؛ به جای آن از [کانتینرهای HostProcess](/docs/tasks/configure-pod-container/create-hostprocess-pod/) استفاده کنید
* `securityContext.procMount` -
   ویندوز سیستم فایل `/proc` ندارد
* `securityContext.readOnlyRootFilesystem` -
   در ویندوز امکان‌پذیر نیست؛ برای اجرای رجیستری و فرایندهای سیستمی داخل کانتینر، دسترسی نوشتن لازم است
* `securityContext.runAsGroup` -
   در ویندوز امکان‌پذیر نیست، زیرا از GID پشتیبانی نمی‌شود
* `securityContext.runAsNonRoot` -
   این تنظیم از اجرای کانتینرها با کاربر `ContainerAdministrator` جلوگیری می‌کند که نزدیک‌ترین معادل کاربر root در ویندوز است.
* `securityContext.runAsUser` -
   به جای آن از [`runAsUserName`](/docs/tasks/configure-pod-container/configure-runasusername) استفاده کنید
* `securityContext.seLinuxOptions` -
   در ویندوز امکان‌پذیر نیست، زیرا SELinux مختص لینوکس است
* `terminationMessagePath` -
   این فیلد محدودیت‌هایی دارد، زیرا ویندوز از نگاشت تک‌فایل‌ها پشتیبانی نمی‌کند. مقدار پیش‌فرض آن `/dev/termination-log` است که کار می‌کند، زیرا این مسیر به‌طور پیش‌فرض در ویندوز وجود ندارد.

#### سازگاری فیلدها برای مشخصات Pod {#compatibility-v1-pod}

فهرست زیر تفاوت‌های نحوه‌ی کار مشخصات Pod را در ویندوز و لینوکس شرح می‌دهد:

* `hostIPC` و `hostpid` - اشتراک فضای نام میزبان در ویندوز امکان‌پذیر نیست
* `hostNetwork` - شبکه‌ی میزبان در ویندوز امکان‌پذیر نیست
* `dnsPolicy` - تنظیم `dnsPolicy` در Pod روی `ClusterFirstWithHostNet` در ویندوز پشتیبانی نمی‌شود، زیرا شبکه‌ی میزبان فراهم نشده است. پادها همیشه با شبکه‌ی کانتینر اجرا می‌شوند.
* `podSecurityContext` [بخش زیر را ببینید](#compatibility-v1-pod-spec-containers-securitycontext)
* `shareProcessNamespace` - این یک قابلیت بتا است و به فضاهای نام لینوکس وابسته است که در ویندوز پیاده‌سازی نشده‌اند. ویندوز نمی‌تواند فضاهای نام فرایند یا سیستم فایل ریشه‌ی کانتینر را به اشتراک بگذارد. فقط شبکه را می‌توان به اشتراک گذاشت.
* `terminationGracePeriodSeconds` - این قابلیت در Docker روی ویندوز به‌طور کامل پیاده‌سازی نشده است؛ [مسئله‌ی GitHub](https://github.com/moby/moby/issues/25982) را ببینید. رفتار کنونی به این صورت است که ابتدا رویداد CTRL_SHUTDOWN_EVENT به فرایند ENTRYPOINT ارسال می‌شود، سپس ویندوز به‌طور پیش‌فرض ۵ ثانیه صبر می‌کند و در پایان همه‌ی فرایندها را با رفتار عادی خاموش‌سازی ویندوز متوقف می‌کند. مقدار پیش‌فرض ۵ ثانیه در واقع در رجیستری ویندوز [داخل کانتینر](https://github.com/moby/moby/issues/25982#issuecomment-426441183) قرار دارد، بنابراین می‌توان آن را هنگام ساخت کانتینر بازنویسی کرد.
* `volumeDevices` - این یک قابلیت بتا است و در ویندوز پیاده‌سازی نشده است. ویندوز نمی‌تواند دستگاه‌های بلوکی خام را به پادها متصل کند.
* `volumes`
  * اگر یک حجم `emptyDir` تعریف کنید، نمی‌توانید منبع حجم آن را روی `memory` تنظیم کنید.
* نمی‌توانید `mountPropagation` را برای اتصال‌های حجم فعال کنید، زیرا این قابلیت در ویندوز پشتیبانی نمی‌شود.

#### دسترسی به شبکه‌ی میزبان {#compatibility-v1-pod-sec-containers-hostnetwork}

کوبرنتیز از نسخه‌ی v1.26 تا v1.32 پشتیبانی آلفا از اجرای پادهای ویندوز در فضای نام شبکه‌ی میزبان را در بر داشت.

کوبرنتیز v{{< skew currentVersion >}} نه feature gate با نام `WindowsHostNetwork` را در بر دارد و نه از اجرای پادهای ویندوز در فضای نام شبکه‌ی میزبان پشتیبانی می‌کند (**پشتیبانی نمی‌کند**).

#### سازگاری فیلدها برای زمینه‌ی امنیتی Pod {#compatibility-v1-pod-spec-containers-securitycontext}

از میان فیلدهای [`securityContext`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context) در Pod، فقط `securityContext.runAsNonRoot` و `securityContext.windowsOptions` در ویندوز کار می‌کنند.

## تشخیص‌دهنده‌ی مشکلات نود

تشخیص‌دهنده‌ی مشکلات نود (node problem detector) (بخش [پایش سلامت نود](/docs/tasks/debug/debug-cluster/monitor-node-health/) را ببینید) پشتیبانی اولیه از ویندوز دارد. برای اطلاعات بیشتر، به [صفحه‌ی GitHub](https://github.com/kubernetes/node-problem-detector#windows) این پروژه مراجعه کنید.

## کانتینر pause

در یک Pod کوبرنتیز، ابتدا یک کانتینر زیرساختی یا «pause» ایجاد می‌شود تا میزبان کانتینر باشد. در لینوکس، گروه‌های کنترلی (cgroups) و فضاهای نامی که یک پاد را تشکیل می‌دهند، برای تداوم وجود خود به یک فرایند نیاز دارند و فرایند pause این نیاز را برآورده می‌کند. کانتینرهای متعلق به یک پاد، از جمله کانتینرهای زیرساختی و کارگر، یک نقطه‌ی پایانی شبکه‌ی مشترک دارند (نشانی IPv4 و/یا IPv6 یکسان و فضاهای درگاه شبکه‌ی یکسان). کوبرنتیز از کانتینرهای pause استفاده می‌کند تا کانتینرهای کارگر بتوانند بدون از دست رفتن هیچ‌یک از پیکربندی‌های شبکه، از کار بیفتند یا دوباره راه‌اندازی شوند.

کوبرنتیز یک ایمیج چندمعماری نگهداری می‌کند که از ویندوز پشتیبانی می‌کند. برای کوبرنتیز v{{< skew currentPatchVersion >}}، ایمیج pause پیشنهادی `registry.k8s.io/pause:3.6` است. [کد منبع](https://github.com/kubernetes/kubernetes/tree/master/build/pause) آن در GitHub در دسترس است.

مایکروسافت ایمیج چندمعماری دیگری با پشتیبانی از لینوکس و ویندوز روی amd64 نگهداری می‌کند که می‌توانید آن را با نام `mcr.microsoft.com/oss/kubernetes/pause:3.6` بیابید. این ایمیج از همان کد منبع ایمیج نگهداری‌شده توسط کوبرنتیز ساخته می‌شود، اما همه‌ی فایل‌های دودویی ویندوزی آن را مایکروسافت با [امضای authenticode](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) امضا کرده است. اگر در محیط عملیاتی (production) یا محیطی مشابه آن مستقر می‌کنید که به فایل‌های دودویی امضاشده نیاز دارد، پروژه‌ی کوبرنتیز استفاده از ایمیج نگهداری‌شده توسط مایکروسافت را توصیه می‌کند.

## محیط‌های اجرای کانتینر {#container-runtime}

برای اینکه پادها بتوانند روی هر نود کلاستر اجرا شوند، باید یک {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} روی آن نود نصب کنید.

محیط‌های اجرای کانتینر زیر با ویندوز کار می‌کنند:

{{% thirdparty-content %}}

### ContainerD

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

می‌توانید از {{< glossary_tooltip term_id="containerd" text="ContainerD" >}} نسخه‌ی 1.4.0 به بالا به‌عنوان محیط اجرای کانتینر برای نودهای کوبرنتیز که ویندوز اجرا می‌کنند استفاده کنید.

با نحوه‌ی [نصب ContainerD روی نود ویندوز](/docs/setup/production-environment/container-runtimes/#containerd) آشنا شوید.
{{< note >}}
هنگام استفاده از GMSA همراه با containerd برای دسترسی به اشتراک‌های شبکه‌ی ویندوز، یک [محدودیت شناخته‌شده](/docs/tasks/configure-pod-container/configure-gmsa/#gmsa-limitations) وجود دارد که رفع آن به یک وصله‌ی هسته (kernel patch) نیاز دارد.
{{< /note >}}

### Mirantis Container Runtime {#mcr}

محیط اجرای [Mirantis Container Runtime](https://docs.mirantis.com/mcr/25.0/overview.html) (MCR) به‌عنوان محیط اجرای کانتینر برای همه‌ی نسخه‌های Windows Server 2019 و نسخه‌های بعدی در دسترس است.

برای اطلاعات بیشتر، [نصب MCR روی سرورهای ویندوز](https://docs.mirantis.com/mcr/25.0/install/mcr-windows.html) را ببینید.

## سازگاری نسخه‌ی سیستم‌عامل ویندوز {#windows-os-version-support}

روی نودهای ویندوز، قواعد سازگاری سخت‌گیرانه‌ای اعمال می‌شود؛ به این معنا که نسخه‌ی سیستم‌عامل میزبان باید با نسخه‌ی سیستم‌عامل ایمیج پایه‌ی کانتینر مطابقت داشته باشد.

برای کوبرنتیز v{{< skew currentVersion >}}، سازگاری سیستم‌عامل برای نودهای ویندوز (و پادها) به شرح زیر است:

نسخه‌ی LTSC ویندوز سرور
: Windows Server 2022
: Windows Server 2025

[سیاست اختلاف نسخه (version-skew)](/docs/setup/release/version-skew-policy/) کوبرنتیز نیز اعمال می‌شود.

## توصیه‌ها و ملاحظات سخت‌افزاری {#windows-hardware-recommendations}

{{% thirdparty-content %}}

{{< note >}}
مشخصات سخت‌افزاری زیر را باید مقادیر پیش‌فرض معقولی در نظر گرفت.
این مقادیر حداقل الزامات یا توصیه‌های مشخصی برای محیط‌های عملیاتی (production) نیستند.
بسته به نیازهای بار کاری شما، ممکن است لازم باشد این مقادیر را تنظیم کنید.
{{< /note >}}

- پردازنده‌ی ۶۴ بیتی با ۴ هسته‌ی CPU یا بیشتر که از مجازی‌سازی پشتیبانی کند
- حافظه‌ی RAM به اندازه‌ی ۸ گیگابایت یا بیشتر
- فضای خالی دیسک به اندازه‌ی ۵۰ گیگابایت یا بیشتر

برای به‌روزترین اطلاعات درباره‌ی حداقل الزامات سخت‌افزاری، به
[الزامات سخت‌افزاری Windows Server در مستندات Microsoft](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements)
مراجعه کنید. برای راهنمایی درباره‌ی تعیین منابع نودهای کارگر عملیاتی، به [نودهای کارگر عملیاتی در مستندات کوبرنتیز](/docs/setup/production-environment/#production-worker-nodes) مراجعه کنید.

برای بهینه‌سازی منابع سیستم، اگر به رابط کاربری گرافیکی نیازی ندارید،
بهتر است سیستم‌عامل Windows Server را بدون گزینه‌ی نصب
[Windows Desktop Experience](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server-core-desktop-experience)
نصب کنید، زیرا این پیکربندی معمولاً منابع بیشتری از سیستم را آزاد می‌کند.

هنگام برآورد فضای دیسک برای نودهای کارگر ویندوز، توجه کنید که ایمیج‌های کانتینر ویندوز معمولاً از ایمیج‌های کانتینر
لینوکس بزرگ‌تر هستند و اندازه‌ی هر ایمیج
از [۳۰۰ مگابایت تا بیش از ۱۰ گیگابایت](https://techcommunity.microsoft.com/t5/containers/nano-server-x-server-core-x-server-which-base-image-is-the-right/ba-p/2835785)
متغیر است. همچنین توجه کنید که درایو `C:` در کانتینرهای ویندوز به‌طور پیش‌فرض اندازه‌ی خالی مجازی ۲۰ گیگابایتی را نشان می‌دهد.
این مقدار فضای واقعی مصرف‌شده نیست، بلکه حداکثر اندازه‌ی دیسکی است که یک کانتینر هنگام استفاده از ذخیره‌سازی محلی میزبان
می‌تواند تا آن حد رشد کند.
برای جزئیات بیشتر، به [کانتینرها در ویندوز - مستندات ذخیره‌سازی کانتینر](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-storage#storage-limits)
مراجعه کنید.

## دریافت کمک و عیب‌یابی {#troubleshooting}

منبع اصلی کمک برای عیب‌یابی کلاستر کوبرنتیز شما باید صفحه‌ی
[عیب‌یابی](/docs/tasks/debug/)
باشد.

در این بخش، راهنمایی‌های تکمیلی برای عیب‌یابی مختص ویندوز آمده است.
لاگ‌ها بخش مهمی از عیب‌یابی مشکلات در کوبرنتیز هستند. هر بار که از سایر
مشارکت‌کنندگان برای عیب‌یابی کمک می‌خواهید، حتماً لاگ‌ها را نیز ارائه دهید.
دستورالعمل‌های
[راهنمای مشارکت درباره‌ی جمع‌آوری لاگ‌ها](https://github.com/kubernetes/community/blob/main/sig-windows/CONTRIBUTING.md#gathering-logs) در SIG Windows را دنبال کنید.

### گزارش مشکلات و درخواست قابلیت‌ها

اگر با چیزی شبیه به یک باگ روبه‌رو شده‌اید یا می‌خواهید
قابلیت جدیدی درخواست کنید، لطفاً برای ایجاد یک issue جدید از [راهنمای مشارکت SIG Windows](https://github.com/kubernetes/community/blob/main/sig-windows/CONTRIBUTING.md#reporting-issues-and-feature-requests) پیروی کنید.
ابتدا فهرست issueها را جست‌وجو کنید تا مطمئن شوید این مشکل
پیش‌تر گزارش نشده است؛ در این صورت، تجربه‌ی خود را در همان issue به‌صورت نظر بنویسید و لاگ‌های
بیشتری اضافه کنید. کانال SIG Windows در Slack کوبرنتیز نیز پیش از ایجاد تیکت، مسیر بسیار خوبی برای دریافت پشتیبانی اولیه و
ایده‌هایی برای عیب‌یابی است.

### اعتبارسنجی عملکرد کلاستر ویندوز

پروژه‌ی کوبرنتیز مشخصه‌ای با عنوان _Windows Operational Readiness_ (آمادگی عملیاتی ویندوز) ارائه می‌دهد
که همراه با یک مجموعه‌ی آزمون ساختاریافته است. این مجموعه به دو دسته آزمون،
یعنی آزمون‌های پایه (core) و توسعه‌یافته (extended)، تقسیم می‌شود و هر دسته شامل گروه‌هایی برای آزمودن حوزه‌های مشخص است.
با این مجموعه می‌توان همه‌ی قابلیت‌های یک سیستم ویندوزی و ترکیبی
(همراه با نودهای لینوکس) را با پوشش کامل اعتبارسنجی کرد.

برای راه‌اندازی این پروژه روی یک کلاستر تازه ایجادشده، به دستورالعمل‌های
[راهنمای پروژه](https://github.com/kubernetes-sigs/windows-operational-readiness/blob/main/README.md) مراجعه کنید.

## ابزارهای استقرار

ابزار kubeadm به شما کمک می‌کند یک کلاستر کوبرنتیز را مستقر کنید و control
plane را برای مدیریت کلاستر و نودها را برای اجرای بارهای کاری شما فراهم می‌کند.

پروژه‌ی [Cluster API](https://cluster-api.sigs.k8s.io/) کوبرنتیز نیز ابزارهایی برای خودکارسازی استقرار نودهای ویندوز فراهم می‌کند.

## کانال‌های توزیع ویندوز

برای توضیح مفصل درباره‌ی کانال‌های توزیع ویندوز، به
[مستندات Microsoft](https://docs.microsoft.com/en-us/windows-server/get-started-19/servicing-channels-19) مراجعه کنید.

اطلاعات مربوط به کانال‌های سرویس‌دهی مختلف Windows Server،
از جمله مدل‌های پشتیبانی آن‌ها، در
[کانال‌های سرویس‌دهی Windows Server](https://docs.microsoft.com/en-us/windows-server/get-started/servicing-channels-comparison) آمده است.

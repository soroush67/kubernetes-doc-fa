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

برنامه‌های ویندوزی بخش بزرگی از سرویس‌ها و برنامه‌هایی را تشکیل می‌دهند که در بسیاری از سازمان‌ها اجرا می‌شوند. [کانتینرهای ویندوز](https://aka.ms/windowscontainers)
راهی برای کپسوله‌سازی فرایندها و بسته‌بندی وابستگی‌ها فراهم می‌کنند و استفاده از رویکردهای DevOps و پیروی از الگوهای cloud native را برای برنامه‌های ویندوزی آسان‌تر می‌سازند.

سازمان‌هایی که در برنامه‌های مبتنی بر ویندوز و برنامه‌های مبتنی بر لینوکس سرمایه‌گذاری کرده‌اند، لازم نیست برای مدیریت بارهای کاری خود به دنبال ارکستریتورهای جداگانه باشند. این امر به افزایش کارایی عملیاتی در تمامی استقرارها منجر می‌شود، فارغ از اینکه از چه سیستم‌عاملی استفاده می‌شود.

<!-- body -->

## نودهای ویندوز در کوبرنتیز

برای فعال‌سازی ارکستریشن کانتینرهای ویندوز در کوبرنتیز، نودهای ویندوز را به کلاستر لینوکسی موجود خود اضافه کنید. زمان‌بندی کانتینرهای ویندوز در
{{< glossary_tooltip text="Podها" term_id="pod" >}} در کوبرنتیز مشابه زمان‌بندی کانتینرهای مبتنی بر لینوکس است.

برای اجرای کانتینرهای ویندوز، کلاستر کوبرنتیز شما باید شامل چند سیستم‌عامل باشد.
در حالی که {{< glossary_tooltip text="control plane" term_id="control-plane" >}} را فقط می‌توان روی لینوکس اجرا کرد،
می‌توانید نودهای کارگری را که ویندوز یا لینوکس اجرا می‌کنند، مستقر کنید.

{{< glossary_tooltip text="نودهای" term_id="node" >}} ویندوز در صورتی
[پشتیبانی](#windows-os-version-support) می‌شوند که سیستم‌عامل آن‌ها
Windows Server 2022 یا Windows Server 2025 باشد.

در این سند، منظور از اصطلاح *کانتینرهای ویندوز*، کانتینرهای ویندوز با ایزوله‌سازی در سطح فرایند (process isolation) است.
کوبرنتیز از اجرای کانتینرهای ویندوز با
[ایزوله‌سازی Hyper-V](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container) پشتیبانی نمی‌کند.

## سازگاری و محدودیت‌ها {#limitations}

برخی از قابلیت‌های نود فقط در صورتی در دسترس هستند که از یک
[container runtime](#container-runtime) مشخص استفاده کنید؛ برخی دیگر روی نودهای ویندوز در دسترس نیستند،
از جمله:

* HugePages: برای کانتینرهای ویندوز پشتیبانی نمی‌شود
* کانتینرهای دارای دسترسی ویژه (Privileged): برای کانتینرهای ویندوز پشتیبانی نمی‌شوند.
  [HostProcess Containers](/docs/tasks/configure-pod-container/create-hostprocess-pod/) قابلیت مشابهی ارائه می‌دهند.
* TerminationGracePeriod: به containerD نیاز دارد

همه قابلیت‌های فضاهای نام اشتراکی (shared namespaces) پشتیبانی نمی‌شوند. برای جزئیات بیشتر به [سازگاری API](#api) مراجعه کنید.

برای جزئیات مربوط به نسخه‌های ویندوزی که کوبرنتیز روی آن‌ها آزمایش می‌شود، به [سازگاری نسخه سیستم‌عامل ویندوز](#windows-os-version-support) مراجعه کنید.

از دیدگاه API و kubectl، کانتینرهای ویندوز تقریباً مانند کانتینرهای مبتنی بر لینوکس رفتار می‌کنند. با این حال، در برخی قابلیت‌های کلیدی تفاوت‌های قابل‌توجهی وجود دارد که در این بخش شرح داده شده‌اند.

### مقایسه با لینوکس {#compatibility-linux-similarities}

عناصر کلیدی کوبرنتیز در ویندوز همانند لینوکس کار می‌کنند. این بخش به چند انتزاع کلیدی بار کاری و نحوه نگاشت آن‌ها به ویندوز می‌پردازد.

* [Podها](/docs/concepts/workloads/pods/)

  Pod بلوک سازنده پایه کوبرنتیز است؛ کوچک‌ترین و ساده‌ترین واحد در مدل آبجکت‌های کوبرنتیز که ایجاد یا مستقر می‌کنید. نمی‌توانید کانتینرهای ویندوز و
  لینوکس را در یک Pod مستقر کنید. همه کانتینرهای یک Pod روی یک نود واحد زمان‌بندی می‌شوند، که هر نود یک پلتفرم و معماری مشخص را نمایندگی می‌کند. قابلیت‌ها، ویژگی‌ها و رویدادهای Pod زیر با کانتینرهای ویندوز پشتیبانی می‌شوند:

  * یک یا چند کانتینر در هر Pod با ایزوله‌سازی فرایند و اشتراک‌گذاری حجم (volume)
  * فیلدهای `status` در Pod
  * probeهای readiness، liveness و startup
  * هوک‌های چرخه عمر کانتینر یعنی postStart و preStop
  * ConfigMap و Secret: به صورت متغیر محیطی یا حجم (volume)
  * حجم‌های `emptyDir`
  * mountهای named pipe از میزبان
  * محدودیت‌های منابع
  * فیلد OS:

    فیلد `.spec.os.name` باید روی `windows` تنظیم شود تا نشان دهد Pod جاری از کانتینرهای ویندوز استفاده می‌کند.

    اگر فیلد `.spec.os.name` را روی `windows` تنظیم کنید،
    نباید فیلدهای زیر را در `.spec` آن Pod تنظیم کنید:

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

    در فهرست بالا، نویسه‌های عام (`*`) نشان‌دهنده همه عناصر یک فهرست هستند.
    برای مثال، `spec.containers[*].securityContext` به آبجکت SecurityContext
    همه کانتینرها اشاره دارد. اگر هر یک از این فیلدها مشخص شود، Pod
    توسط API server پذیرفته نخواهد شد.

* [منابع بار کاری](/docs/concepts/workloads/controllers/) از جمله:
  * ReplicaSet
  * Deployment
  * StatefulSet
  * DaemonSet
  * Job
  * CronJob
  * ReplicationController
* {{< glossary_tooltip text="Serviceها" term_id="service" >}}
  برای جزئیات بیشتر به [توزیع بار و Serviceها](/docs/concepts/services-networking/windows-networking/#load-balancing-and-services) مراجعه کنید.

Podها، منابع بار کاری و Serviceها عناصر حیاتی برای مدیریت بارهای کاری ویندوز در کوبرنتیز هستند. با این حال، به‌تنهایی برای فعال‌سازی مدیریت مناسب چرخه عمر بارهای کاری ویندوز در یک محیط پویای cloud native کافی نیستند.

* `kubectl exec`
* معیارهای (metrics) Pod و کانتینر
* {{< glossary_tooltip text="مقیاس‌گذاری خودکار افقی Pod" term_id="horizontal-pod-autoscaler" >}}
* {{< glossary_tooltip text="سهمیه‌های منابع" term_id="resource-quota" >}}
* پیشدستی (preemption) زمان‌بند

### گزینه‌های خط فرمان برای kubelet {#kubelet-compatibility}

برخی گزینه‌های خط فرمان kubelet در ویندوز رفتار متفاوتی دارند، که در ادامه شرح داده شده است:

* گزینه `--windows-priorityclass` به شما امکان می‌دهد اولویت زمان‌بندی فرایند kubelet را تنظیم کنید
  (به [مدیریت منابع CPU](/docs/concepts/configuration/windows-resource-management/#resource-management-cpu) مراجعه کنید)
* فلگ‌های `--kube-reserved`، `--system-reserved` و `--eviction-hard`
  [NodeAllocatable](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) را به‌روزرسانی می‌کنند
* Eviction با استفاده از `--enforce-node-allocable` پیاده‌سازی نشده است
* هنگام اجرا روی نود ویندوز، kubelet محدودیتی بر حافظه یا CPU ندارد.
  `--kube-reserved` و `--system-reserved` فقط از `NodeAllocatable` کم می‌کنند
  و منابع تأمین‌شده برای بارهای کاری را تضمین نمی‌کنند.
  برای اطلاعات بیشتر به [مدیریت منابع برای نودهای ویندوز](/docs/concepts/configuration/windows-resource-management/#resource-reservation)
  مراجعه کنید.
* Condition با نام `PIDPressure` پیاده‌سازی نشده است
* kubelet اقدامات eviction ناشی از OOM را انجام نمی‌دهد

### سازگاری API {#api}

به دلیل تفاوت در سیستم‌عامل و container runtime، تفاوت‌های ظریفی در نحوه کار APIهای کوبرنتیز برای ویندوز وجود دارد. برخی ویژگی‌های بار کاری برای لینوکس طراحی شده‌اند و روی ویندوز اجرا نمی‌شوند.

در سطح کلی، این مفاهیم سیستم‌عامل با هم تفاوت دارند:

* هویت (Identity) - لینوکس از userID (UID) و groupID (GID) استفاده می‌کند که
  به صورت نوع عدد صحیح نمایش داده می‌شوند. نام کاربر و گروه
  مرجع اصلی نیستند؛ آن‌ها صرفاً نام مستعاری در `/etc/groups`
  یا `/etc/passwd` برای UID+GID هستند. ویندوز از یک
  [شناسه امنیتی](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/security-identifiers) (SID)
  باینری بزرگ‌تر استفاده می‌کند که در پایگاه داده Windows Security Access Manager (SAM) ذخیره می‌شود. این
  پایگاه داده بین میزبان و کانتینرها یا بین کانتینرها به اشتراک گذاشته نمی‌شود.
* مجوزهای فایل - ویندوز از فهرست کنترل دسترسی مبتنی بر SIDها استفاده می‌کند، در حالی که
  سیستم‌های POSIX مانند لینوکس از یک bitmask مبتنی بر مجوزهای آبجکت و UID+GID
  به‌علاوه فهرست‌های کنترل دسترسی _اختیاری_ استفاده می‌کنند.
* مسیرهای فایل - قرارداد در ویندوز استفاده از `\` به جای `/` است. کتابخانه‌های IO زبان Go
  معمولاً هر دو را می‌پذیرند و کار را پیش می‌برند، اما وقتی مسیر یا خط فرمانی را تنظیم می‌کنید
  که درون کانتینر تفسیر می‌شود، ممکن است به `\` نیاز باشد.
* سیگنال‌ها - برنامه‌های تعاملی ویندوز خاتمه را به شکل متفاوتی مدیریت می‌کنند و
  می‌توانند یک یا چند مورد از موارد زیر را پیاده‌سازی کنند:
  * یک thread رابط کاربری پیام‌های کاملاً تعریف‌شده‌ای از جمله `WM_CLOSE` را مدیریت می‌کند.
  * برنامه‌های کنسولی Ctrl-C یا Ctrl-break را با استفاده از یک Control Handler مدیریت می‌کنند.
  * سرویس‌ها یک تابع Service Control Handler ثبت می‌کنند که می‌تواند
    کدهای کنترلی `SERVICE_CONTROL_STOP` را بپذیرد.

کدهای خروج کانتینر از همان قرارداد پیروی می‌کنند: مقدار 0 به معنای موفقیت و مقدار غیرصفر به معنای شکست است.
کدهای خطای مشخص ممکن است در ویندوز و لینوکس متفاوت باشند. با این حال، کدهای خروجی که
از مؤلفه‌های کوبرنتیز (kubelet، kube-proxy) منتقل می‌شوند بدون تغییر هستند.

#### سازگاری فیلدها برای مشخصات کانتینر {#compatibility-v1-pod-spec-containers}

فهرست زیر تفاوت‌های نحوه کار مشخصات کانتینر Pod بین ویندوز و لینوکس را شرح می‌دهد:

* Huge pages در container runtime ویندوز پیاده‌سازی نشده‌اند
  و در دسترس نیستند. آن‌ها نیازمند [اعمال یک امتیاز
  کاربری](https://docs.microsoft.com/en-us/windows/desktop/Memory/large-page-support)
  هستند که برای کانتینرها قابل پیکربندی نیست.
* `requests.cpu` و `requests.memory` - درخواست‌ها از منابع در دسترس نود کسر می‌شوند، بنابراین می‌توان از آن‌ها برای جلوگیری از تخصیص بیش‌ازحد (overprovisioning) به یک
  نود استفاده کرد. با این حال، نمی‌توان از آن‌ها برای تضمین منابع در یک
  نود دچار تخصیص بیش‌ازحد استفاده کرد. اگر اپراتور بخواهد به‌طور کامل از تخصیص بیش‌ازحد جلوگیری کند، به عنوان بهترین روش باید آن‌ها را برای همه کانتینرها اعمال کند.
* `securityContext.allowPrivilegeEscalation` -
   در ویندوز امکان‌پذیر نیست؛ هیچ‌یک از capabilityها متصل نشده‌اند
* `securityContext.capabilities` -
   capabilityهای POSIX در ویندوز پیاده‌سازی نشده‌اند
* `securityContext.privileged` -
   ویندوز از کانتینرهای دارای دسترسی ویژه پشتیبانی نمی‌کند؛ به جای آن از [HostProcess Containers](/docs/tasks/configure-pod-container/create-hostprocess-pod/) استفاده کنید
* `securityContext.procMount` -
   ویندوز فایل‌سیستم `/proc` ندارد
* `securityContext.readOnlyRootFilesystem` -
   در ویندوز امکان‌پذیر نیست؛ برای اجرای رجیستری و فرایندهای سیستمی درون کانتینر،
   دسترسی نوشتن لازم است
* `securityContext.runAsGroup` -
   در ویندوز امکان‌پذیر نیست زیرا از GID پشتیبانی نمی‌شود
* `securityContext.runAsNonRoot` -
   این تنظیم مانع از اجرای کانتینرها با کاربر `ContainerAdministrator` می‌شود
   که نزدیک‌ترین معادل کاربر root در ویندوز است.
* `securityContext.runAsUser` -
   به جای آن از [`runAsUserName`](/docs/tasks/configure-pod-container/configure-runasusername)
   استفاده کنید
* `securityContext.seLinuxOptions` -
   در ویندوز امکان‌پذیر نیست زیرا SELinux مختص لینوکس است
* `terminationMessagePath` -
   این مورد محدودیت‌هایی دارد، از جمله اینکه ویندوز از نگاشت فایل‌های منفرد پشتیبانی نمی‌کند. مقدار
   پیش‌فرض `/dev/termination-log` است که کار می‌کند، زیرا به‌طور پیش‌فرض
   در ویندوز وجود ندارد.

#### سازگاری فیلدها برای مشخصات Pod {#compatibility-v1-pod}

فهرست زیر تفاوت‌های نحوه کار مشخصات Pod بین ویندوز و لینوکس را شرح می‌دهد:

* `hostIPC` و `hostpid` - اشتراک‌گذاری فضای نام میزبان در ویندوز امکان‌پذیر نیست
* `hostNetwork` - شبکه میزبان در ویندوز امکان‌پذیر نیست
* `dnsPolicy` - تنظیم `dnsPolicy` در Pod روی `ClusterFirstWithHostNet` در ویندوز
   پشتیبانی نمی‌شود، زیرا شبکه میزبان ارائه نمی‌شود. Podها همیشه
   با یک شبکه کانتینر اجرا می‌شوند.
* `podSecurityContext` [به بخش زیر مراجعه کنید](#compatibility-v1-pod-spec-containers-securitycontext)
* `shareProcessNamespace` - این یک قابلیت بتا است و به فضاهای نام لینوکس وابسته است
  که در ویندوز پیاده‌سازی نشده‌اند. ویندوز نمی‌تواند فضاهای نام فرایند یا
  فایل‌سیستم ریشه کانتینر را به اشتراک بگذارد. فقط شبکه قابل اشتراک‌گذاری است.
* `terminationGracePeriodSeconds` - این مورد در Docker روی ویندوز به‌طور کامل پیاده‌سازی نشده است،
  به [issue در GitHub](https://github.com/moby/moby/issues/25982) مراجعه کنید.
  رفتار فعلی به این صورت است که رویداد CTRL_SHUTDOWN_EVENT به فرایند ENTRYPOINT ارسال می‌شود،
  سپس ویندوز به‌طور پیش‌فرض ۵ ثانیه صبر می‌کند و در نهایت
  همه فرایندها را با استفاده از رفتار عادی خاموش‌سازی ویندوز متوقف می‌کند. مقدار پیش‌فرض ۵
  ثانیه در واقع در رجیستری ویندوز
  [درون کانتینر](https://github.com/moby/moby/issues/25982#issuecomment-426441183) قرار دارد،
  بنابراین می‌توان آن را هنگام ساخت کانتینر بازنویسی کرد.
* `volumeDevices` - این یک قابلیت بتا است و در ویندوز پیاده‌سازی نشده است.
  ویندوز نمی‌تواند دستگاه‌های بلاک خام را به Podها متصل کند.
* `volumes`
  * اگر یک حجم `emptyDir` تعریف کنید، نمی‌توانید منبع حجم آن را روی `memory` تنظیم کنید.
* نمی‌توانید `mountPropagation` را برای mountهای حجم فعال کنید، زیرا این مورد
  در ویندوز پشتیبانی نمی‌شود.

#### دسترسی به شبکه میزبان {#compatibility-v1-pod-sec-containers-hostnetwork}

کوبرنتیز نسخه‌های v1.26 تا v1.32 شامل پشتیبانی آلفا برای اجرای Podهای ویندوز در فضای نام شبکه میزبان بودند.

کوبرنتیز v{{< skew currentVersion >}} شامل feature gate با نام `WindowsHostNetwork`
یا پشتیبانی از اجرای Podهای ویندوز در فضای نام شبکه میزبان **نیست**.

#### سازگاری فیلدها برای security context در Pod {#compatibility-v1-pod-spec-containers-securitycontext}

از میان فیلدهای [`securityContext`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context) در Pod، فقط `securityContext.runAsNonRoot` و `securityContext.windowsOptions` در ویندوز کار می‌کنند.

## Node problem detector

Node problem detector (به
[پایش سلامت نود](/docs/tasks/debug/debug-cluster/monitor-node-health/) مراجعه کنید)
پشتیبانی اولیه‌ای از ویندوز دارد.
برای اطلاعات بیشتر، از [صفحه GitHub](https://github.com/kubernetes/node-problem-detector#windows) این پروژه دیدن کنید.

## کانتینر Pause

در یک Pod کوبرنتیز، ابتدا یک کانتینر زیرساختی یا «pause» ایجاد می‌شود
تا میزبان کانتینر باشد. در لینوکس، cgroupها و فضاهای نامی که یک Pod را تشکیل می‌دهند
به یک فرایند نیاز دارند تا تداوم وجودشان را حفظ کند؛ فرایند pause این کار را انجام
می‌دهد. کانتینرهای متعلق به یک Pod، از جمله کانتینرهای زیرساختی و کارگر،
یک نقطه پایانی شبکه مشترک دارند (آدرس IPv4 و/یا IPv6 یکسان، فضای پورت شبکه
یکسان). کوبرنتیز از کانتینرهای pause استفاده می‌کند تا کانتینرهای کارگر بتوانند
بدون از دست رفتن پیکربندی شبکه، از کار بیفتند یا دوباره راه‌اندازی شوند.

کوبرنتیز یک ایمیج چندمعماری نگهداری می‌کند که از ویندوز پشتیبانی می‌کند.
برای کوبرنتیز v{{< skew currentPatchVersion >}} ایمیج pause توصیه‌شده `registry.k8s.io/pause:3.6` است.
[کد منبع](https://github.com/kubernetes/kubernetes/tree/master/build/pause)
در GitHub در دسترس است.

مایکروسافت ایمیج چندمعماری دیگری را نگهداری می‌کند که از لینوکس و ویندوز
amd64 پشتیبانی می‌کند و می‌توانید آن را با نام `mcr.microsoft.com/oss/kubernetes/pause:3.6` بیابید.
این ایمیج از همان منبعی ساخته شده است که ایمیج نگهداری‌شده توسط کوبرنتیز ساخته می‌شود، اما
همه فایل‌های باینری ویندوز توسط مایکروسافت [با authenticode امضا شده‌اند](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/authenticode).
پروژه کوبرنتیز توصیه می‌کند اگر در یک محیط تولید یا شبیه تولید که به
باینری‌های امضاشده نیاز دارد استقرار انجام می‌دهید، از ایمیج نگهداری‌شده توسط مایکروسافت استفاده کنید.

## Container runtimeها {#container-runtime}

باید یک
{{< glossary_tooltip text="container runtime" term_id="container-runtime" >}}
روی هر نود کلاستر نصب کنید تا Podها بتوانند در آنجا اجرا شوند.

container runtimeهای زیر با ویندوز کار می‌کنند:

{{% thirdparty-content %}}

### ContainerD

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

می‌توانید از {{< glossary_tooltip term_id="containerd" text="ContainerD" >}} نسخه 1.4.0 یا بالاتر
به عنوان container runtime برای نودهای کوبرنتیز که ویندوز اجرا می‌کنند استفاده کنید.

یاد بگیرید چگونه [ContainerD را روی یک نود ویندوز نصب کنید](/docs/setup/production-environment/container-runtimes/#containerd).
{{< note >}}
هنگام استفاده از GMSA با containerd برای دسترسی به اشتراک‌های شبکه ویندوز،
یک [محدودیت شناخته‌شده](/docs/tasks/configure-pod-container/configure-gmsa/#gmsa-limitations) وجود دارد
که به یک وصله (patch) کرنل نیاز دارد.
{{< /note >}}

### Mirantis Container Runtime {#mcr}

[Mirantis Container Runtime](https://docs.mirantis.com/mcr/25.0/overview.html) (MCR)
به عنوان container runtime برای همه نسخه‌های Windows Server 2019 و جدیدتر در دسترس است.

برای اطلاعات بیشتر به [نصب MCR روی Windows Serverها](https://docs.mirantis.com/mcr/25.0/install/mcr-windows.html) مراجعه کنید.

## سازگاری نسخه سیستم‌عامل ویندوز {#windows-os-version-support}

روی نودهای ویندوز، قوانین سخت‌گیرانه‌ای برای سازگاری اعمال می‌شود: نسخه سیستم‌عامل میزبان باید
با نسخه سیستم‌عامل ایمیج پایه کانتینر مطابقت داشته باشد.

برای کوبرنتیز v{{< skew currentVersion >}}، سازگاری سیستم‌عامل برای نودهای ویندوز (و Podها)
به شرح زیر است:

انتشار Windows Server LTSC
: Windows Server 2022
: Windows Server 2025

[سیاست انحراف نسخه](/docs/setup/release/version-skew-policy/) کوبرنتیز نیز اعمال می‌شود.

## توصیه‌ها و ملاحظات سخت‌افزاری {#windows-hardware-recommendations}

{{% thirdparty-content %}}

{{< note >}}
مشخصات سخت‌افزاری ذکرشده در اینجا باید به‌عنوان مقادیر پیش‌فرض معقول در نظر گرفته شوند.
این مقادیر نه حداقل الزامات را نشان می‌دهند و نه توصیه‌هایی مشخص برای محیط‌های production هستند.
بسته به نیازهای بار کاری شما، ممکن است لازم باشد این مقادیر تنظیم شوند.
{{< /note >}}

- پردازنده ۶۴ بیتی با ۴ هسته CPU یا بیشتر، با قابلیت پشتیبانی از مجازی‌سازی
- ۸ گیگابایت یا بیشتر RAM
- ۵۰ گیگابایت یا بیشتر فضای آزاد دیسک

برای آگاهی از به‌روزترین اطلاعات درباره حداقل الزامات سخت‌افزاری، به
[الزامات سخت‌افزاری در مستندات مایکروسافت برای Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements)
مراجعه کنید. برای راهنمایی در تعیین منابع لازم برای نودهای کارگر در محیط production، به
[مستندات کوبرنتیز درباره نودهای کارگر در محیط production](/docs/setup/production-environment/#production-worker-nodes) مراجعه کنید.

برای بهینه‌سازی منابع سیستم، اگر به رابط کاربری گرافیکی نیاز ندارید،
ممکن است بهتر باشد از نصبی از سیستم‌عامل Windows Server استفاده کنید که گزینه نصب
[Windows Desktop Experience](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server-core-desktop-experience)
را شامل نمی‌شود، زیرا این پیکربندی معمولاً منابع سیستمی بیشتری را آزاد می‌کند.

هنگام ارزیابی فضای دیسک برای نودهای کارگر ویندوزی، توجه داشته باشید که ایمیج‌های کانتینر ویندوزی معمولاً از ایمیج‌های کانتینر لینوکسی بزرگ‌تر هستند و اندازه هر ایمیج می‌تواند
از [۳۰۰ مگابایت تا بیش از ۱۰ گیگابایت](https://techcommunity.microsoft.com/t5/containers/nano-server-x-server-core-x-server-which-base-image-is-the-right/ba-p/2835785)
باشد. همچنین توجه داشته باشید که درایو `C:` در کانتینرهای ویندوزی به‌طور پیش‌فرض اندازه آزاد مجازی ۲۰ گیگابایت را نشان می‌دهد؛ این مقدار فضای مصرف‌شده واقعی نیست، بلکه اندازه‌ای از دیسک است که یک کانتینر منفرد هنگام استفاده از ذخیره‌سازی محلی روی میزبان می‌تواند تا آن حد رشد کند و آن را اشغال کند.
برای جزئیات بیشتر، به [Containers on Windows - Container Storage Documentation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-storage#storage-limits) مراجعه کنید.

## دریافت کمک و عیب‌یابی {#troubleshooting}

منبع اصلی کمک برای عیب‌یابی کلاستر کوبرنتیز شما باید صفحه
[عیب‌یابی](/docs/tasks/debug/) باشد.

برخی راهنمایی‌های عیب‌یابی اضافی و مختص ویندوز در همین بخش آمده است.
لاگ‌ها عنصری مهم در عیب‌یابی مشکلات در کوبرنتیز هستند. هرگاه از
سایر مشارکت‌کنندگان درخواست کمک برای عیب‌یابی می‌کنید، حتماً آن‌ها را ضمیمه کنید.
دستورالعمل‌های موجود در
[راهنمای مشارکت SIG Windows درباره جمع‌آوری لاگ‌ها](https://github.com/kubernetes/community/blob/main/sig-windows/CONTRIBUTING.md#gathering-logs)
را دنبال کنید.

### گزارش مشکلات و درخواست قابلیت‌ها

اگر به نظر می‌رسد با یک باگ مواجه شده‌اید، یا می‌خواهید
درخواست قابلیتی جدید ثبت کنید، لطفاً برای ایجاد یک issue جدید از
[راهنمای مشارکت SIG Windows](https://github.com/kubernetes/community/blob/main/sig-windows/CONTRIBUTING.md#reporting-issues-and-feature-requests) پیروی کنید.
ابتدا باید فهرست issueها را جست‌وجو کنید، چون ممکن است پیش‌تر گزارش شده باشد؛ در این صورت تجربه خود را در همان issue بنویسید و لاگ‌های بیشتری را به آن اضافه کنید. کانال SIG Windows در Slack کوبرنتیز نیز راهی عالی برای دریافت پشتیبانی اولیه و ایده‌های عیب‌یابی پیش از ایجاد تیکت است.

### اعتبارسنجی operability کلاستر ویندوزی

پروژه کوبرنتیز یک مشخصات _Windows Operational Readiness_ همراه با
یک مجموعه تست ساختاریافته ارائه می‌دهد. این مجموعه به دو دسته تست،
اصلی و گسترده، تقسیم می‌شود که هر کدام شامل دسته‌بندی‌هایی برای آزمودن بخش‌های مشخصی هستند.
از آن می‌توان برای اعتبارسنجی تمام قابلیت‌های یک سیستم ویندوزی و ترکیبی
(آمیخته با نودهای لینوکسی) با پوشش کامل استفاده کرد.

برای راه‌اندازی این پروژه روی یک کلاستر تازه ایجادشده، به دستورالعمل‌های
[راهنمای پروژه](https://github.com/kubernetes-sigs/windows-operational-readiness/blob/main/README.md) مراجعه کنید.

## ابزارهای استقرار

ابزار kubeadm به شما کمک می‌کند یک کلاستر کوبرنتیز را مستقر کنید و
control plane را برای مدیریت کلاستر و نودها را برای اجرای بارهای کاری شما فراهم می‌کند.

پروژه [cluster API](https://cluster-api.sigs.k8s.io/) کوبرنتیز نیز ابزارهایی برای خودکارسازی استقرار نودهای ویندوزی فراهم می‌کند.

## کانال‌های توزیع ویندوز

برای توضیح مفصل درباره کانال‌های توزیع ویندوز به
[مستندات مایکروسافت](https://docs.microsoft.com/en-us/windows-server/get-started-19/servicing-channels-19) مراجعه کنید.

اطلاعات مربوط به کانال‌های سرویس‌دهی مختلف Windows Server
از جمله مدل‌های پشتیبانی آن‌ها در
[Windows Server servicing channels](https://docs.microsoft.com/en-us/windows-server/get-started/servicing-channels-comparison)
در دسترس است.

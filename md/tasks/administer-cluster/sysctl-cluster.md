---
title: استفاده از sysctlها در یک کلاستر کوبرنتیز
reviewers:
- sttts
content_type: task
weight: 400
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

این سند توضیح می‌دهد که چگونه می‌توان پارامترهای کرنل را در یک کلاستر کوبرنتیز با استفاده از رابط {{< glossary_tooltip term_id="sysctl" >}} پیکربندی و استفاده کرد.

{{< note >}}
از نسخهٔ ۱.۲۳ کوبرنتیز، kubelet از هر دو نویسهٔ `/` و `.` به‌عنوان جداکننده در نام‌های sysctl پشتیبانی می‌کند.
از نسخهٔ ۱.۲۵ کوبرنتیز، هنگام تنظیم sysctlها برای یک Pod می‌توان از نام‌هایی با اسلش نیز استفاده کرد.
برای مثال، یک نام sysctl واحد را می‌توان با جداکنندهٔ نقطه به‌صورت `kernel.shm_rmid_forced` یا با جداکنندهٔ اسلش به‌صورت `kernel/shm_rmid_forced` نوشت.
برای جزئیات بیشتر دربارهٔ روش تبدیل پارامترهای sysctl، به صفحهٔ [sysctl.d(5)](https://man7.org/linux/man-pages/man5/sysctl.d.5.html) از پروژهٔ Linux man-pages مراجعه کنید.
{{< /note >}}
## {{% heading "prerequisites" %}}

{{< note >}}
ابزار `sysctl` یک ابزار خط فرمان مختص لینوکس است که برای پیکربندی پارامترهای گوناگون کرنل به کار می‌رود و در سیستم‌عامل‌های غیرلینوکسی در دسترس نیست.
{{< /note >}}

{{< include "task-tutorial-prereqs.md" >}}

برای برخی از مراحل، باید بتوانید گزینه‌های خط فرمان kubeletهای در حال اجرا در کلاستر خود را نیز دوباره پیکربندی کنید.


<!-- steps -->

## فهرست کردن همهٔ پارامترهای sysctl

در لینوکس، رابط sysctl به مدیر سیستم امکان می‌دهد پارامترهای کرنل را در زمان اجرا تغییر دهد. این پارامترها از طریق سامانهٔ فایل مجازی پردازه‌ها در مسیر `/proc/sys/` در دسترس هستند. این پارامترها زیرسامانه‌های گوناگونی را پوشش می‌دهند، از جمله:

- کرنل (پیشوند رایج: `kernel.`)
- شبکه (پیشوند رایج: `net.`)
- حافظهٔ مجازی (پیشوند رایج: `vm.`)
- ‏MDADM (پیشوند رایج: `dev.`)
- زیرسامانه‌های دیگر در [مستندات کرنل](https://www.kernel.org/doc/Documentation/sysctl/README) شرح داده شده‌اند.

برای دریافت فهرست همهٔ پارامترها می‌توانید این فرمان را اجرا کنید:

```shell
sudo sysctl -a
```

## sysctlهای امن و ناامن

کوبرنتیز sysctlها را به دو دستهٔ _امن_ و _ناامن_ تقسیم می‌کند. یک sysctl _امن_ علاوه بر داشتن فضای نام (namespace) مناسب، باید میان پادهای روی یک نود به‌درستی _ایزوله_ باشد. یعنی تنظیم یک sysctl _امن_ برای یک پاد:

- نباید هیچ تأثیری بر پادهای دیگر روی آن نود داشته باشد
- نباید امکان آسیب رساندن به سلامت نود را فراهم کند
- نباید امکان به دست آوردن منابع CPU یا حافظه فراتر از محدودیت‌های منابع پاد را فراهم کند.

بیشتر sysctlهای _دارای فضای نام_ لزوماً _امن_ به شمار نمی‌آیند. sysctlهای زیر در مجموعهٔ _امن_ پشتیبانی می‌شوند:

- `kernel.shm_rmid_forced`؛
- `net.ipv4.ip_local_port_range`؛
- `net.ipv4.tcp_syncookies`؛
- `net.ipv4.ping_group_range` (از کوبرنتیز ۱.۱۸)؛
- `net.ipv4.ip_unprivileged_port_start` (از کوبرنتیز ۱.۲۲)؛
- `net.ipv4.ip_local_reserved_ports` (از کوبرنتیز ۱.۲۷، نیازمند کرنل ۳.۱۶ یا بالاتر)؛
- `net.ipv4.tcp_keepalive_time` (از کوبرنتیز ۱.۲۹، نیازمند کرنل ۴.۵ یا بالاتر)؛
- `net.ipv4.tcp_fin_timeout` (از کوبرنتیز ۱.۲۹، نیازمند کرنل ۴.۶ یا بالاتر)؛
- `net.ipv4.tcp_keepalive_intvl` (از کوبرنتیز ۱.۲۹، نیازمند کرنل ۴.۵ یا بالاتر)؛
- `net.ipv4.tcp_keepalive_probes` (از کوبرنتیز ۱.۲۹، نیازمند کرنل ۴.۵ یا بالاتر).
- `net.ipv4.tcp_rmem` (از کوبرنتیز ۱.۳۲، نیازمند کرنل ۴.۱۵ یا بالاتر).
- `net.ipv4.tcp_wmem` (از کوبرنتیز ۱.۳۲، نیازمند کرنل ۴.۱۵ یا بالاتر).
- `net.ipv4.tcp_slow_start_after_idle` (از کوبرنتیز ۱.۳۷، نیازمند کرنل ۴.۱۵ یا بالاتر).
- `net.ipv4.tcp_notsent_lowat` (از کوبرنتیز ۱.۳۷، نیازمند کرنل ۴.۶ یا بالاتر).

{{< note >}}
مجموعهٔ sysctlهای امن چند استثنا دارد:

- استفاده از sysctlهای `net.*` در حالتی که شبکهٔ میزبان (host networking) فعال باشد مجاز نیست.
- ‏sysctl مربوط به `net.ipv4.tcp_syncookies` در کرنل لینوکس نسخهٔ ۴.۵ یا پایین‌تر فضای نام ندارد.
{{< /note >}}

این فهرست در نسخه‌های آیندهٔ کوبرنتیز، هم‌زمان با پشتیبانی kubelet از سازوکارهای ایزوله‌سازی بهتر، گسترش خواهد یافت.

### فعال‌سازی sysctlهای ناامن

همهٔ sysctlهای _امن_ به‌طور پیش‌فرض فعال هستند.

همهٔ sysctlهای _ناامن_ به‌طور پیش‌فرض غیرفعال هستند و مدیر کلاستر باید آن‌ها را به‌صورت دستی و جداگانه برای هر نود مجاز کند. پادهایی که sysctlهای ناامنِ غیرفعال دارند زمان‌بندی می‌شوند، اما راه‌اندازی آن‌ها با شکست مواجه می‌شود.

با در نظر گرفتن هشدار بالا، مدیر کلاستر می‌تواند برخی sysctlهای _ناامن_ را برای موقعیت‌های بسیار خاص، مانند تنظیم دقیق برنامه‌های پرکارایی یا بلادرنگ، مجاز کند. sysctlهای _ناامن_ به‌صورت نود به نود و با یک فلگ kubelet فعال می‌شوند؛ برای مثال:

```shell
kubelet --allowed-unsafe-sysctls \
  'kernel.msg*,net.core.somaxconn' ...
```

در {{< glossary_tooltip term_id="minikube" >}}، این کار را می‌توان با فلگ `extra-config` انجام داد:

```shell
minikube start --extra-config="kubelet.allowed-unsafe-sysctls=kernel.msg*,net.core.somaxconn"...
```

تنها sysctlهای _دارای فضای نام_ را می‌توان به این روش فعال کرد.

## تنظیم sysctlها برای یک Pod

در کرنل‌های امروزی لینوکس، شماری از sysctlها _دارای فضای نام_ هستند. یعنی می‌توان آن‌ها را برای هر پاد روی یک نود به‌طور مستقل تنظیم کرد. در کوبرنتیز تنها sysctlهای دارای فضای نام را می‌توان از طریق securityContext پاد پیکربندی کرد.

sysctlهای زیر دارای فضای نام شناخته می‌شوند. این فهرست ممکن است در نسخه‌های آیندهٔ کرنل لینوکس تغییر کند.

- `kernel.shm*`،
- `kernel.msg*`،
- `kernel.sem`،
- `fs.mqueue.*`،
- آن دسته از `net.*`هایی که می‌توان آن‌ها را در فضای نام شبکهٔ کانتینر تنظیم کرد. با این حال، استثناهایی وجود دارد (برای مثال، `net.netfilter.nf_conntrack_max` و `net.netfilter.nf_conntrack_expect_max` را می‌توان در فضای نام شبکهٔ کانتینر تنظیم کرد، اما پیش از لینوکس ۵.۱۲.۲ فضای نام ندارند).

به sysctlهایی که فضای نام ندارند sysctlهای _سطح نود_ گفته می‌شود. اگر نیاز به تنظیم آن‌ها دارید، باید آن‌ها را به‌صورت دستی روی سیستم‌عامل هر نود پیکربندی کنید یا از یک DaemonSet با کانتینرهای دارای امتیاز ویژه (privileged) استفاده کنید.

برای پیکربندی sysctlهای دارای فضای نام از securityContext پاد استفاده کنید. securityContext بر همهٔ کانتینرهای یک پاد اعمال می‌شود.

در این مثال، با استفاده از securityContext پاد، یک sysctl امن یعنی `kernel.shm_rmid_forced` و دو sysctl ناامن یعنی `net.core.somaxconn` و `kernel.msgmax` تنظیم می‌شوند. در مشخصات (specification) هیچ تمایزی میان sysctlهای _امن_ و _ناامن_ وجود ندارد.

{{< warning >}}
برای جلوگیری از ناپایدار شدن سیستم‌عامل، پارامترهای sysctl را تنها پس از درک کامل اثرات آن‌ها تغییر دهید.
{{< /warning >}}

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.core.somaxconn
      value: "1024"
    - name: kernel.msgmax
      value: "65536"
  ...
```


<!-- discussion -->

{{< warning >}}
به دلیل ماهیت _ناامن_ این sysctlها، مسئولیت استفاده از sysctlهای _ناامن_ بر عهدهٔ خود شماست و این کار می‌تواند به مشکلات جدی مانند رفتار نادرست کانتینرها، کمبود منابع یا از کار افتادن کامل یک نود منجر شود.
{{< /warning >}}

توصیه می‌شود نودهایی را که تنظیمات sysctl ویژه دارند در کلاستر _لکه‌دار_ (tainted) در نظر بگیرید و تنها پادهایی را روی آن‌ها زمان‌بندی کنید که به آن تنظیمات sysctl نیاز دارند. برای پیاده‌سازی این کار، استفاده از [قابلیت _taints and toleration_](/docs/reference/generated/kubectl/kubectl-commands/#taint) کوبرنتیز پیشنهاد می‌شود.

پادی که sysctlهای _ناامن_ دارد، روی هر نودی که آن دو sysctl _ناامن_ را صریحاً فعال نکرده باشد، با شکست در راه‌اندازی مواجه می‌شود. همانند sysctlهای _سطح نود_، توصیه می‌شود برای زمان‌بندی این پادها روی نودهای مناسب، از [قابلیت _taints and toleration_](/docs/reference/generated/kubectl/kubectl-commands/#taint) یا [taintها روی نودها](/docs/concepts/scheduling-eviction/taint-and-toleration/) استفاده کنید.

## تنظیم sysctlها برای همهٔ پادها

{{< feature-state feature_gate_name="DefaultPodSysctls" >}}

می‌توانید مجموعه‌ای پیش‌فرض از پارامترهای کرنل (sysctlها) را پیکربندی کنید تا `kubelet` آن‌ها را بر همهٔ پادهای در حال اجرا روی یک نود لینوکسی، از جمله {{< glossary_tooltip text="پادهای ایستا" term_id="static-pod" >}}، اعمال کند.
این قابلیت زمانی سودمند است که مدیران نود بخواهند تنظیم یکسانی از پارامترهای کرنل را بر همهٔ بارهای کاری روی یک نود یا در یک گروه نود اعمال کنند (برای مثال، تنظیم اندازهٔ بافرهای TCP برای شبکه‌های پرکارایی)، بی‌آنکه لازم باشد در مشخصات تک‌تک پادها فیلد `securityContext.sysctls` تنظیم شود.

برای استفاده از این قابلیت، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `DefaultPodSysctls` را برای `kubelet` فعال کنید و جفت‌های کلید-مقدار را در فیلد `defaultPodSysctls` در [KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) خود مشخص کنید.

فیلد `defaultPodSysctls` از همهٔ sysctlهای دارای فضای نام (`kernel.shm*`، `kernel.msg*`، `kernel.sem`، `kernel.domainname`، `fs.mqueue.*`، `net.*` و `user.*`) پشتیبانی می‌کند و هم sysctlهای _امن_ و هم _ناامن_ را در بر می‌گیرد. از آنجا که این مقادیر پیش‌فرض را مدیر نود مستقیماً روی `kubelet` پیکربندی می‌کند، لازم نیست sysctlهای ناامن را در `allowedUnsafeSysctls` به فهرست مجاز اضافه کنید.

مثال زیر `kubelet` را طوری پیکربندی می‌کند که sysctlهای پیش‌فرض را در چند زیرسامانهٔ دارای فضای نام (شبکه، IPC و فضاهای نام کاربر) بر همهٔ پادهای روی نود اعمال کند:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  DefaultPodSysctls: true
defaultPodSysctls:
  # Network namespace sysctls (skipped if Pod uses hostNetwork: true)
  net.ipv4.ip_forward: "1"
  net.ipv4.tcp_rmem: "4096 87380 16777216"
  net.ipv4.tcp_wmem: "4096 65536 16777216"
  net.core.somaxconn: "1024"
  # IPC namespace sysctls (skipped if Pod uses hostIPC: true)
  kernel.shmall: "1048576"
  kernel.msgmax: "65536"
  kernel.sem: "250 32000 32 128"
  fs.mqueue.msg_max: "1024"
  # User namespace sysctls (skipped if Pod shares the host user namespace)
  user.max_user_namespaces: "1000"
```

### اولویت و بازنویسی مقادیر

مقادیری که صریحاً در `spec.securityContext.sysctls` یک پاد تنظیم شده‌اند، همواره مقادیر پیش‌فرض متناظر در `defaultPodSysctls` مربوط به `kubelet` را بازنویسی می‌کنند. بازنویسی‌ها به‌صورت جداگانه و برای هر کلید اعمال می‌شوند: اگر پادی مقداری را برای یک sysctl مشخص کند که در `defaultPodSysctls` نیز تعریف شده است، تنظیم سطح پاد برای همان sysctl اولویت دارد و سایر مقادیر پیش‌فرض همچنان اعمال می‌شوند. توجه کنید که هیچ گروهی از تنظیمات sysctl به‌هم‌پیوسته وجود ندارد؛ اگر بار کاری شما sysctlی را بازنویسی کند که بخشی از یک گروه مرتبط است (برای مثال، اندازهٔ بافرهای شبکه)، مشخصات پاد باید در صورت نیاز همهٔ تنظیمات مرتبط را در نظر بگیرد.

### فضاهای نام میزبان و فیلتر کردن

‏`kubelet` تنها در صورتی sysctlهای پیش‌فرض را هنگام ایجاد sandbox پاد اعمال می‌کند که پاد در یک فضای نام جداگانه برای زیرسامانهٔ مربوط اجرا شود. اگر پادی یک فضای نام میزبان را به اشتراک بگذارد، sysctlهای پیش‌فرض آن فضای نام برای آن پاد نادیده گرفته می‌شوند:

- اگر پاد از شبکهٔ میزبان استفاده کند (`hostNetwork: true`)، sysctlهای `net.*` نادیده گرفته می‌شوند.
- اگر پاد از IPC میزبان استفاده کند (`hostIPC: true`)، sysctlهای IPC (`kernel.sem`، `kernel.msg*`، `kernel.shm*`، `fs.mqueue.*`) نادیده گرفته می‌شوند.
- اگر پاد فضای نام کاربر میزبان را به اشتراک بگذارد (`hostUsers: true` یا تنظیم‌نشده)، sysctlهای `user.*` نادیده گرفته می‌شوند.
- اگر پاد از شبکهٔ میزبان استفاده کند (`hostNetwork: true`)، sysctlهای UTS (`kernel.domainname`) نادیده گرفته می‌شوند.

### اعتبارسنجی و محدودیت‌ها

‏`kubelet` فیلد `defaultPodSysctls` را هنگام راه‌اندازی اعتبارسنجی می‌کند. وجود sysctlهای بدون فضای نام، نام‌های نامعتبر sysctl یا کلیدهای تکراری مانع راه‌اندازی `kubelet` می‌شود.

افزون بر این، برخی sysctlهای `net.*` بسته به نسخهٔ کرنل شما ممکن است فضای نام نداشته باشند. مشخص کردن یک sysctl بدون فضای نام از نوع `net.*` در `defaultPodSysctls` باعث می‌شود ایجاد sandbox پاد با خطای `FailedCreatePodSandBox` شکست بخورد. در این حالت، پاد بی‌پایان برای ایجاد sandbox تلاش دوباره می‌کند. مطمئن شوید همهٔ sysctlهای مشخص‌شده در کرنل نود شما دارای فضای نام هستند.

تغییرات `defaultPodSysctls` تنها بر پادهای تازه ایجادشده اعمال می‌شوند. ‏`kubelet` پادهای موجود را به‌صورت پویا دوباره پیکربندی نمی‌کند (به [پس از راه‌اندازی دوبارهٔ نود چه اتفاقی می‌افتد](/docs/reference/node/what-happens-on-restart/#impact-of-a-kubelet-restart) مراجعه کنید).
پادهای موجود با همان sysctlهایی به اجرا ادامه می‌دهند که هنگام ایجاد sandbox آن‌ها اعمال شده بود.
اگر می‌خواهید پادهای موجود sysctlهای پیش‌فرض به‌روزشده را بپذیرند، باید آن پادها را دوباره ایجاد کنید (برای مثال، با cordon و drain کردن نود).

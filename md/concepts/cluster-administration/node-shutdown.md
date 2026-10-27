---
title: خاموش شدن نودها
content_type: concept
weight: 10
---

<!-- overview -->

در یک کلاستر کوبرنتیز، یک {{< glossary_tooltip text="نود" term_id="node" >}}
می‌تواند به‌صورت برنامه‌ریزی‌شده و آرام (graceful) خاموش شود، یا به‌طور ناگهانی و به دلایلی
مانند قطع برق یا یک عامل خارجی دیگر از کار بیفتد. اگر نود پیش از خاموش شدن تخلیه (drain) نشود،
خاموش شدن آن می‌تواند به از کار افتادن بار کاری منجر شود. خاموش شدن نود می‌تواند
**آرام (graceful)** یا **غیرآرام (non-graceful)** باشد.

{{< caution >}}
بسته `unattended-upgrades` در دبیان، با پیکربندی عادی خود، با خاموش شدن آرام نود تداخل دارد.
اگر از پیکربندی پیش‌فرض `unattended-upgrades` استفاده کنید که مهلت آرام خاموش شدن سرور را سفارشی‌سازی می‌کند،
kubelet نمی‌تواند قفل لازم را برای مدیریت صحیح رویدادهای خاموش شدن به دست آورد.

این مشکل زمانی رخ می‌دهد که مقدار `shutdownGracePeriod` بیشتر از ۳۰ ثانیه باشد.
برای جلوگیری از این مشکل، می‌توانید بخشی از پیکربندی `unattended-upgrades` را با تبدیل
`/etc/systemd/logind.conf.d/unattended-upgrades-logind-maxdelay.conf` به یک پیوند نمادین (symbolic link)
به `/dev/null` بی‌اثر کنید.

برای جزئیات بیشتر، به
[مستندات `logind.conf`](https://www.freedesktop.org/software/systemd/man/latest/logind.conf.html)
مراجعه کنید.
{{< /caution >}}

<!-- body -->

## خاموش شدن آرام نود {#graceful-node-shutdown}

kubelet تلاش می‌کند خاموش شدن سیستم نود را تشخیص دهد و Podهای در حال اجرا روی نود را خاتمه دهد.

kubelet تضمین می‌کند که Podها در طول خاموش شدن نود، از
[فرایند عادی خاتمه Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)
پیروی کنند. در طول خاموش شدن نود، kubelet هیچ Pod جدیدی را نمی‌پذیرد
(حتی اگر آن Podها پیش‌تر به نود متصل (bound) شده باشند).

### فعال‌سازی خاموش شدن آرام نود

{{< tabs name="graceful_shutdown_os" >}}
{{% tab name="Linux" %}}
{{< feature-state feature_gate_name="GracefulNodeShutdown" >}}

در لینوکس، قابلیت خاموش شدن آرام نود با
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) به نام `GracefulNodeShutdown`
کنترل می‌شود که از نسخه ۱.۲۱ به‌صورت پیش‌فرض فعال است.

{{< note >}}
قابلیت خاموش شدن آرام نود به systemd وابسته است، زیرا از
[قفل‌های بازدارنده systemd (systemd inhibitor locks)](https://www.freedesktop.org/wiki/Software/systemd/inhibit/)
برای به‌تأخیر انداختن خاموش شدن نود به مدت یک بازه زمانی مشخص استفاده می‌کند.
{{</ note >}}
{{% /tab %}}

{{% tab name="Windows" %}}
{{< feature-state feature_gate_name="WindowsGracefulNodeShutdown" >}}

در ویندوز، قابلیت خاموش شدن آرام نود با
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) به نام `WindowsGracefulNodeShutdown`
کنترل می‌شود که در نسخه ۱.۳۲ به‌صورت یک قابلیت آلفا معرفی شد. در کوبرنتیز ۱.۳۴ این قابلیت بتا است
و به‌صورت پیش‌فرض فعال است.

{{< note >}}
قابلیت خاموش شدن آرام نود در ویندوز به اجرای kubelet به‌صورت یک سرویس ویندوز وابسته است؛
در این حالت kubelet یک [service control handler](https://learn.microsoft.com/en-us/windows/win32/services/service-control-handler-function)
ثبت‌شده خواهد داشت تا رویداد preshutdown را به مدت یک بازه زمانی مشخص به تأخیر بیندازد.
{{</ note >}}

خاموش شدن آرام نود در ویندوز قابل لغو نیست.

اگر kubelet به‌صورت یک سرویس ویندوز اجرا نشود، نمی‌تواند رویداد
[Preshutdown](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_preshutdown_info)
را تنظیم و پایش کند و نود باید از رویه
[خاموش شدن غیرآرام نود](#non-graceful-node-shutdown) که در بالا ذکر شد عبور کند.

در حالتی که قابلیت خاموش شدن آرام نود در ویندوز فعال باشد، اما kubelet به‌صورت
سرویس ویندوز اجرا نشود، kubelet به‌جای شکست خوردن به اجرای خود ادامه می‌دهد. با این حال،
خطایی ثبت می‌کند که نشان می‌دهد باید به‌صورت یک سرویس ویندوز اجرا شود.
{{% /tab %}}

{{< /tabs >}}

### پیکربندی خاموش شدن آرام نود

توجه کنید که به‌طور پیش‌فرض هر دو گزینه پیکربندی توضیح داده‌شده در ادامه،
یعنی `shutdownGracePeriod` و `shutdownGracePeriodCriticalPods`، روی صفر تنظیم شده‌اند
و بنابراین قابلیت خاموش شدن آرام نود فعال نمی‌شود.
برای فعال‌سازی این قابلیت، هر دو گزینه باید به‌درستی پیکربندی شوند و
روی مقادیر غیرصفر تنظیم گردند.

هنگامی که kubelet از خاموش شدن نود مطلع شود، یک condition با مقدار `NotReady` روی
Node تنظیم می‌کند و `reason` را برابر `"node is shutting down"` قرار می‌دهد. kube-scheduler به این condition
احترام می‌گذارد و هیچ Podی را روی نود متأثر زمان‌بندی نمی‌کند؛ انتظار می‌رود زمان‌بندهای شخص ثالث
نیز از همین منطق پیروی کنند. این بدان معناست که Podهای جدید روی آن نود زمان‌بندی نخواهند شد
و در نتیجه هیچ‌یک شروع به کار نخواهند کرد.

kubelet **همچنین** در مرحله `PodAdmission` اگر خاموش شدن در حال انجام نود را تشخیص دهد، Podها را رد می‌کند،
به‌طوری که حتی Podهایی که یک
{{< glossary_tooltip text="toleration" term_id="toleration" >}} برای
`node.kubernetes.io/not-ready:NoSchedule` دارند نیز روی آن نود شروع به کار نکنند.

هنگامی که kubelet آن condition را از طریق API روی Node خود تنظیم می‌کند،
شروع به خاتمه دادن هر Podی نیز می‌کند که به‌صورت محلی در حال اجراست.

در طول یک خاموش شدن آرام، kubelet Podها را در دو مرحله خاتمه می‌دهد:

1. Podهای معمولی در حال اجرا روی نود را خاتمه می‌دهد.
1. [Podهای حیاتی (critical pods)](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)
   در حال اجرا روی نود را خاتمه می‌دهد.

قابلیت خاموش شدن آرام نود با دو گزینه
[`KubeletConfiguration`](/docs/tasks/administer-cluster/kubelet-config-file/) پیکربندی می‌شود:

- `shutdownGracePeriod`:

  کل مدتی را مشخص می‌کند که نود باید خاموش شدن را به تأخیر بیندازد. این مقدار، کل
  مهلت آرام برای خاتمه Podها، اعم از Podهای معمولی و
  [Podهای حیاتی](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)،
  است.

- `shutdownGracePeriodCriticalPods`:

  مدتی را مشخص می‌کند که برای خاتمه
  [Podهای حیاتی](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)
  در طول خاموش شدن نود استفاده می‌شود. این مقدار باید کمتر از `shutdownGracePeriod` باشد.

{{< note >}}

مواردی وجود دارد که خاتمه یافتن Node توسط سیستم (یا شاید به‌صورت دستی
توسط یک مدیر) لغو شده است. در هر یک از این وضعیت‌ها، Node به حالت `Ready` بازمی‌گردد.
با این حال، Podهایی که فرایند خاتمه را آغاز کرده بودند توسط kubelet بازیابی نخواهند شد
و باید دوباره زمان‌بندی شوند.

{{< /note >}}

برای مثال، اگر `shutdownGracePeriod=30s` و
`shutdownGracePeriodCriticalPods=10s` باشد، kubelet خاموش شدن نود را
۳۰ ثانیه به تأخیر می‌اندازد. در طول خاموش شدن، ۲۰ ثانیه اول (۱۰-۳۰)
برای خاتمه آرام Podهای معمولی رزرو می‌شود و ۱۰ ثانیه آخر برای
خاتمه [Podهای حیاتی](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/#marking-pod-as-critical)
رزرو خواهد شد.

{{< note >}}
هنگامی که Podها در طول خاموش شدن آرام نود تخلیه (evict) می‌شوند، به‌عنوان خاموش‌شده علامت‌گذاری می‌شوند.
اجرای `kubectl get pods` وضعیت Podهای تخلیه‌شده را `Terminated` نشان می‌دهد.
و `kubectl describe pod` نشان می‌دهد که Pod به دلیل خاموش شدن نود تخلیه شده است:

```
Reason:         Terminated
Message:        Pod was terminated in response to imminent node shutdown.
```

{{< /note >}}

### خاموش شدن آرام نود بر اساس اولویت Pod {#pod-priority-graceful-node-shutdown}

{{< feature-state feature_gate_name="GracefulNodeShutdownBasedOnPodPriority" >}}

برای ایجاد انعطاف‌پذیری بیشتر در ترتیب خاموش شدن Podها در طول خاموش شدن آرام نود،
خاموش شدن آرام نود به PriorityClass مربوط به Podها احترام می‌گذارد، مشروط بر اینکه
این قابلیت را در کلاستر خود فعال کرده باشید. این قابلیت
به مدیران کلاستر اجازه می‌دهد ترتیب Podها را در طول خاموش شدن آرام نود
بر اساس
[کلاس‌های اولویت (priority classes)](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass)
به‌صراحت تعریف کنند.

قابلیت [خاموش شدن آرام نود](#graceful-node-shutdown) که در بالا توضیح داده شد،
Podها را در دو مرحله خاموش می‌کند: ابتدا Podهای غیرحیاتی و سپس Podهای
حیاتی. اگر انعطاف بیشتری برای تعریف صریح ترتیب
Podها در طول خاموش شدن، به شکلی دقیق‌تر، لازم باشد، می‌توان از خاموش شدن
آرام مبتنی بر اولویت Pod استفاده کرد.

هنگامی که خاموش شدن آرام نود به اولویت Podها احترام می‌گذارد، امکان انجام
خاموش شدن آرام نود در چند مرحله فراهم می‌شود که در هر مرحله یک
کلاس اولویت مشخص از Podها خاموش می‌شود. kubelet را می‌توان با مراحل دقیق
و زمان خاموش شدن هر مرحله پیکربندی کرد.

فرض کنید کلاس‌های اولویت سفارشی Pod زیر
([priority classes](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass))
در یک کلاستر وجود دارند:

| نام کلاس اولویت Pod | مقدار کلاس اولویت Pod |
| ----------------------- | ------------------------ |
| `custom-class-a`        | 100000                   |
| `custom-class-b`        | 10000                    |
| `custom-class-c`        | 1000                     |
| `regular/unset`         | 0                        |

در [پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/)،
تنظیمات `shutdownGracePeriodByPodPriority` می‌تواند به این صورت باشد:

| مقدار کلاس اولویت Pod | مدت خاموش شدن |
| ------------------------ | --------------- |
| 100000                   | ۱۰ ثانیه      |
| 10000                    | ۱۸۰ ثانیه     |
| 1000                     | ۱۲۰ ثانیه     |
| 0                        | ۶۰ ثانیه      |

پیکربندی YAML متناظر kubelet به این صورت خواهد بود:

```yaml
shutdownGracePeriodByPodPriority:
  - priority: 100000
    shutdownGracePeriodSeconds: 10
  - priority: 10000
    shutdownGracePeriodSeconds: 180
  - priority: 1000
    shutdownGracePeriodSeconds: 120
  - priority: 0
    shutdownGracePeriodSeconds: 60
```

جدول بالا به این معناست که هر Pod با مقدار `priority` بزرگ‌تر یا مساوی ۱۰۰۰۰۰ فقط
۱۰ ثانیه برای خاموش شدن خواهد داشت، هر Pod با مقدار بزرگ‌تر یا مساوی ۱۰۰۰۰ و کوچک‌تر از ۱۰۰۰۰۰،
۱۸۰ ثانیه برای خاموش شدن خواهد داشت و هر Pod با مقدار بزرگ‌تر یا مساوی ۱۰۰۰ و کوچک‌تر از ۱۰۰۰۰،
۱۲۰ ثانیه برای خاموش شدن خواهد داشت.
در نهایت، تمام Podهای دیگر ۶۰ ثانیه برای خاموش شدن خواهند داشت.

لازم نیست مقادیری متناظر با همه کلاس‌ها مشخص شود. برای
مثال، می‌توانید به‌جای آن از این تنظیمات استفاده کنید:

| مقدار کلاس اولویت Pod | مدت خاموش شدن |
| ------------------------ | --------------- |
| 100000                   | ۳۰۰ ثانیه     |
| 1000                     | ۱۲۰ ثانیه     |
| 0                        | ۶۰ ثانیه      |

در حالت بالا، Podهای دارای `custom-class-b` برای خاموش شدن در همان دسته
`custom-class-c` قرار می‌گیرند.

اگر در یک بازه مشخص هیچ Podی وجود نداشته باشد، kubelet برای
Podهای آن بازه اولویت منتظر نمی‌ماند. در عوض، kubelet بلافاصله به
بازه مقدار کلاس اولویت بعدی می‌پرد.

اگر این قابلیت فعال باشد و هیچ پیکربندی ارائه نشده باشد، هیچ
اقدامی برای ترتیب‌دهی انجام نخواهد شد.

استفاده از این قابلیت مستلزم فعال کردن
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) به نام `GracefulNodeShutdownBasedOnPodPriority`
و تنظیم `ShutdownGracePeriodByPodPriority` در
[پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/)
روی پیکربندی دلخواه است که شامل مقادیر کلاس اولویت Pod
و مدت‌های خاموش شدن متناظر با آنهاست.

{{< note >}}
امکان در نظر گرفتن اولویت Pod در طول خاموش شدن آرام نود در کوبرنتیز v1.23
به‌عنوان یک قابلیت آلفا معرفی شد. در کوبرنتیز {{< skew currentVersion >}}
این قابلیت بتا است و به‌صورت پیش‌فرض فعال است.
{{< /note >}}

متریک‌های `graceful_shutdown_start_time_seconds` و `graceful_shutdown_end_time_seconds`
در زیرسیستم kubelet منتشر می‌شوند تا خاموش شدن نودها پایش شود.

## مدیریت خاموش شدن غیرآرام نود {#non-graceful-node-shutdown}

{{< feature-state feature_gate_name="NodeOutOfServiceVolumeDetach" >}}

ممکن است یک اقدام خاموش‌سازی نود توسط Node Shutdown Manager در kubelet تشخیص داده نشود،
یا به این دلیل که دستور مورد استفاده سازوکار قفل‌های بازدارنده (inhibitor locks) مورد استفاده
kubelet را فعال نمی‌کند، یا به دلیل خطای کاربر، یعنی ShutdownGracePeriod و
ShutdownGracePeriodCriticalPods به‌درستی پیکربندی نشده‌اند. لطفاً برای جزئیات بیشتر به
بخش [خاموش شدن آرام نود](#graceful-node-shutdown) در بالا مراجعه کنید.

هنگامی که یک نود خاموش شده است اما توسط Node Shutdown Manager در kubelet تشخیص داده نمی‌شود،
Podهایی که بخشی از یک {{< glossary_tooltip text="StatefulSet" term_id="statefulset" >}} هستند
در وضعیت terminating روی نود خاموش‌شده گیر می‌کنند و نمی‌توانند به یک نود جدید در حال اجرا منتقل شوند.
دلیل این است که kubelet روی نود خاموش‌شده برای حذف Podها در دسترس نیست، بنابراین
StatefulSet نمی‌تواند Pod جدیدی با همان نام ایجاد کند. اگر Podها از حجم‌هایی (volumes) استفاده کنند،
VolumeAttachmentها از نود خاموش‌شده اصلی حذف نخواهند شد، بنابراین حجم‌های
مورد استفاده این Podها نمی‌توانند به یک نود جدید در حال اجرا متصل شوند. در نتیجه،
برنامه در حال اجرا روی StatefulSet نمی‌تواند به‌درستی کار کند. اگر نود خاموش‌شده اصلی
دوباره روشن شود، Podها توسط kubelet حذف می‌شوند و Podهای جدید روی یک نود
در حال اجرای دیگر ایجاد خواهند شد. اگر نود خاموش‌شده اصلی دوباره روشن نشود،
این Podها برای همیشه در وضعیت terminating روی نود خاموش‌شده باقی می‌مانند.

برای کاهش اثر وضعیت بالا، کاربر می‌تواند به‌صورت دستی taint با نام `node.kubernetes.io/out-of-service`
را با اثر `NoExecute` یا `NoSchedule` به یک Node اضافه کند و آن را خارج از سرویس (out-of-service) علامت‌گذاری نماید.
اگر یک Node با این taint به‌عنوان خارج از سرویس علامت‌گذاری شود، Podهای روی آن نود در صورتی که
toleration منطبقی روی آنها وجود نداشته باشد، به‌اجبار حذف می‌شوند و عملیات جداسازی حجم (volume detach)
برای Podهایی که روی آن نود در حال خاتمه‌اند بلافاصله انجام خواهد شد. این کار به Podهای روی نود خارج از سرویس اجازه می‌دهد
به‌سرعت روی یک نود دیگر بازیابی شوند.

در طول یک خاموش شدن غیرآرام، Podها در دو مرحله خاتمه داده می‌شوند:

1. Podهایی که toleration منطبق با `out-of-service` ندارند، به‌اجبار حذف می‌شوند.
1. عملیات جداسازی حجم برای چنین Podهایی بلافاصله انجام می‌شود.

{{< note >}}

- پیش از افزودن taint با نام `node.kubernetes.io/out-of-service`، باید بررسی شود
  که نود از قبل در وضعیت خاموش یا قطع برق است (و در میانه راه‌اندازی مجدد نیست).
- کاربر موظف است پس از اینکه Podها به یک نود جدید منتقل شدند و کاربر بررسی کرد که نود خاموش‌شده
  بازیابی شده است، taint مربوط به out-of-service را به‌صورت دستی حذف کند،
  زیرا کاربر همان کسی بوده که در ابتدا taint را اضافه کرده است.

{{< /note >}}

### جداسازی اجباری ذخیره‌سازی پس از اتمام مهلت {#storage-force-detach-on-timeout}

در هر وضعیتی که حذف یک Pod به مدت ۶ دقیقه موفق نشده باشد، اگر نود در آن لحظه ناسالم باشد،
کوبرنتیز حجم‌هایی را که در حال unmount شدن هستند به‌اجبار جدا (detach) می‌کند. هر
بار کاری که هنوز روی نود در حال اجرا باشد و از یک حجم جداشده به‌اجبار استفاده کند، موجب
نقض
[مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#controllerunpublishvolume)
خواهد شد؛ این مشخصات بیان می‌کند که `ControllerUnpublishVolume` "**باید** پس از فراخوانی و موفقیت
همه `NodeUnstageVolume` و `NodeUnpublishVolume` روی حجم فراخوانی شود".
در چنین شرایطی، حجم‌های روی نود مورد نظر ممکن است دچار خرابی داده شوند.

رفتار جداسازی اجباری ذخیره‌سازی اختیاری است؛ کاربران ممکن است ترجیح دهند به‌جای آن از قابلیت
«خاموش شدن غیرآرام نود» استفاده کنند.

جداسازی اجباری ذخیره‌سازی پس از اتمام مهلت را می‌توان با تنظیم فیلد پیکربندی `disable-force-detach-on-timeout`
در `kube-controller-manager` غیرفعال کرد. غیرفعال کردن قابلیت جداسازی اجباری پس از اتمام مهلت به این معناست
که برای حجمی که روی نودی میزبانی می‌شود که بیش از ۶ دقیقه ناسالم بوده است،
[VolumeAttachment](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)
مرتبط با آن حذف نخواهد شد.

پس از اعمال این تنظیم، Podهای ناسالمی که هنوز به حجم‌ها متصل هستند باید از طریق رویه
[خاموش شدن غیرآرام نود](#non-graceful-node-shutdown) که در بالا ذکر شد بازیابی شوند.

{{< note >}}

- هنگام استفاده از رویه [خاموش شدن غیرآرام نود](#non-graceful-node-shutdown) باید احتیاط کرد.
- انحراف از مراحل مستندشده در بالا می‌تواند به خرابی داده منجر شود.

{{< /note >}}

## {{% heading "whatsnext" %}}

درباره موارد زیر بیشتر بیاموزید:

- وبلاگ: [Non-Graceful Node Shutdown](/blog/2023/08/16/kubernetes-1-28-non-graceful-node-shutdown-ga/).
- معماری کلاستر: [نودها](/docs/concepts/architecture/nodes/).

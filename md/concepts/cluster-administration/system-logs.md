---
reviewers:
- dims
- 44past4
title: لاگ‌های سیستم
content_type: concept
weight: 80
---

<!-- overview -->

لاگ‌های اجزای سیستم رویدادهایی را که در کلاستر رخ می‌دهند ثبت می‌کنند و این لاگ‌ها برای اشکال‌زدایی بسیار سودمندند.
می‌توانید میزان جزئیات (verbosity) لاگ را پیکربندی کنید تا جزئیات بیشتر یا کمتری ببینید.
لاگ‌ها می‌توانند درشت‌دانه باشند و تنها خطاهای درون یک جزء را نشان دهند، یا ریزدانه باشند و
ردگیری گام‌به‌گام رویدادها را نشان دهند (مانند لاگ‌های دسترسی HTTP، تغییرات وضعیت Pod، اقدامات کنترل‌کننده یا
تصمیم‌های زمان‌بند).

<!-- body -->

{{< warning >}}
برخلاف پرچم‌های خط فرمانی که در اینجا شرح داده شده‌اند، خودِ *خروجی
لاگ* مشمول تضمین‌های پایداری API کوبرنتیز *نیست*:
مدخل‌های منفرد لاگ و قالب‌بندی آن‌ها ممکن است از یک انتشار
به انتشار بعدی تغییر کنند!
{{< /warning >}}

## Klog

klog کتابخانهٔ لاگ‌برداری کوبرنتیز است. [klog](https://github.com/kubernetes/klog)
پیام‌های لاگ را برای اجزای سیستم کوبرنتیز تولید می‌کند.

کوبرنتیز در حال ساده‌سازی لاگ‌برداری در اجزای خود است.
پرچم‌های خط فرمان klog زیر
از کوبرنتیز v1.23 [منسوخ شده‌اند](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2845-deprecate-klog-specific-flags-in-k8s-components)
و در کوبرنتیز v1.26 حذف شده‌اند:

- `--add-dir-header`
- `--alsologtostderr`
- `--log-backtrace-at`
- `--log-dir`
- `--log-file`
- `--log-file-max-size`
- `--logtostderr`
- `--one-output`
- `--skip-headers`
- `--skip-log-headers`
- `--stderrthreshold`

خروجی، صرف‌نظر از قالب خروجی، همیشه در stderr نوشته می‌شود. انتظار می‌رود هدایت خروجی (redirection)
توسط جزئی انجام شود که یک جزء کوبرنتیز را فراخوانی می‌کند. این جزء می‌تواند یک پوستهٔ POSIX
یا ابزاری مانند systemd باشد.

در برخی موارد، برای نمونه در یک کانتینر distroless یا یک سرویس سیستمی ویندوز، این گزینه‌ها
در دسترس نیستند. در این صورت می‌توان از باینری
[`kube-log-runner`](https://github.com/kubernetes/kubernetes/blob/d2a8a81639fcff8d1221b900f66d28361a170654/staging/src/k8s.io/component-base/logs/kube-log-runner/README.md)
به‌عنوان پوششی (wrapper) پیرامون یک جزء کوبرنتیز برای هدایت
خروجی استفاده کرد. یک باینری ازپیش‌ساخته در چندین ایمیج پایهٔ کوبرنتیز با
نام سنتی آن یعنی `/go-runner` و با نام `kube-log-runner` در آرشیوهای انتشار سرور و
نود گنجانده شده است.

این جدول نشان می‌دهد که فراخوانی‌های `kube-log-runner` چگونه با هدایت خروجی در پوسته متناظرند:

| کاربرد                                    | پوستهٔ POSIX (مانند bash) | `kube-log-runner <options> <cmd>`                           |
| -----------------------------------------|----------------------------|-------------------------------------------------------------|
| ادغام stderr و stdout و نوشتن در stdout | `2>&1`                     | `kube-log-runner` (رفتار پیش‌فرض)                        |
| هدایت هر دو به فایل لاگ              | `1>>/tmp/log 2>&1`         | `kube-log-runner -log-file=/tmp/log`                        |
| کپی در فایل لاگ و در stdout         | `2>&1 \| tee -a /tmp/log`  | `kube-log-runner -log-file=/tmp/log -also-stdout`           |
| هدایت فقط stdout به فایل لاگ       | `>/tmp/log`                | `kube-log-runner -log-file=/tmp/log -redirect-stderr=false` |

### خروجی Klog

نمونه‌ای از قالب بومی سنتی klog:

```
I1025 00:15:15.525108       1 httplog.go:79] GET /api/v1/namespaces/kube-system/pods/metrics-server-v0.3.1-57c75779f-9p8wg: (1.512ms) 200 [pod_nanny/v0.0.0 (linux/amd64) kubernetes/$Format 10.56.1.19:51756]
```

رشتهٔ پیام ممکن است شامل شکست خط باشد:

```
I1025 00:15:15.525108       1 example.go:79] This is a message
which has a line break.
```

### لاگ‌برداری ساختاریافته

{{< feature-state for_k8s_version="v1.23" state="beta" >}}

{{< warning >}}
مهاجرت به پیام‌های لاگ ساختاریافته فرایندی در حال انجام است. در این نسخه همهٔ پیام‌های لاگ
ساختاریافته نیستند. هنگام تجزیهٔ فایل‌های لاگ، باید پیام‌های لاگ بدون ساختار را نیز مدیریت کنید.

قالب‌بندی لاگ و سریال‌سازی مقادیر ممکن است تغییر کنند.
{{< /warning>}}

لاگ‌برداری ساختاریافته ساختاری یکنواخت را در پیام‌های لاگ معرفی می‌کند که امکان استخراج
برنامه‌نویسی‌شدهٔ اطلاعات را فراهم می‌کند. می‌توانید لاگ‌های ساختاریافته را با تلاش و هزینهٔ کمتری ذخیره و پردازش کنید.
کدی که یک پیام لاگ را تولید می‌کند تعیین می‌کند که از خروجی سنتی و بدون ساختار
klog استفاده کند یا از لاگ‌برداری ساختاریافته.

قالب‌بندی پیش‌فرض پیام‌های لاگ ساختاریافته به‌صورت متنی است، با قالبی که با klog سنتی
سازگاری رو به عقب دارد:

```
<klog header> "<message>" <key1>="<value1>" <key2>="<value2>" ...
```

مثال:

```
I1025 00:15:15.525108       1 controller_utils.go:116] "Pod status updated" pod="kube-system/kubedns" status="ready"
```

رشته‌ها داخل نقل‌قول قرار می‌گیرند. سایر مقادیر با
[`%+v`](https://pkg.go.dev/fmt#hdr-Printing) قالب‌بندی می‌شوند، که ممکن است باعث شود پیام‌های لاگ
[بسته به داده‌ها](https://github.com/kubernetes/kubernetes/issues/106428) در خط بعدی ادامه یابند.

```
I1025 00:15:15.525108       1 example.go:116] "Example" data="This is text with a line break\nand \"quotation marks\"." someInt=1 someFloat=0.1 someStruct={StringField: First line,
second line.}
```

### لاگ‌برداری زمینه‌ای (Contextual Logging)

{{< feature-state for_k8s_version="v1.30" state="beta" >}}

لاگ‌برداری زمینه‌ای بر پایهٔ لاگ‌برداری ساختاریافته بنا شده است. این مفهوم عمدتاً به
نحوهٔ استفادهٔ توسعه‌دهندگان از فراخوانی‌های لاگ‌برداری مربوط است: کدی که بر این مفهوم مبتنی است انعطاف‌پذیرتر است
و از موارد کاربرد اضافی‌ای پشتیبانی می‌کند که در [KEP لاگ‌برداری
زمینه‌ای](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/3077-contextual-logging) شرح داده شده‌اند.

اگر توسعه‌دهندگان از توابع اضافی مانند `WithValues` یا `WithName` در
اجزای خود استفاده کنند، مدخل‌های لاگ حاوی اطلاعات اضافی‌ای خواهند بود که
توسط فراخواننده به توابع ارسال می‌شود.

در کوبرنتیز {{< skew currentVersion >}}، این قابلیت پشت
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ContextualLogging` قرار دارد و
به‌طور پیش‌فرض فعال است. زیرساخت این قابلیت در نسخهٔ 1.24 بدون
تغییر اجزا اضافه شد. فرمان
[`component-base/logs/example`](https://github.com/kubernetes/kubernetes/blob/v1.24.0-beta.0/staging/src/k8s.io/component-base/logs/example/cmd/logger.go)
نشان می‌دهد که چگونه از فراخوانی‌های جدید لاگ‌برداری استفاده کنید و جزئی که
از لاگ‌برداری زمینه‌ای پشتیبانی می‌کند چگونه رفتار می‌کند.

```console
$ cd $GOPATH/src/k8s.io/kubernetes/staging/src/k8s.io/component-base/logs/example/cmd/
$ go run . --help
...
      --feature-gates mapStringBool  A set of key=value pairs that describe feature gates for alpha/experimental features. Options are:
                                     AllAlpha=true|false (ALPHA - default=false)
                                     AllBeta=true|false (BETA - default=false)
                                     ContextualLogging=true|false (BETA - default=true)
$ go run . --feature-gates ContextualLogging=true
...
I0222 15:13:31.645988  197901 example.go:54] "runtime" logger="example.myname" foo="bar" duration="1m0s"
I0222 15:13:31.646007  197901 example.go:55] "another runtime" logger="example" foo="bar" duration="1h0m0s" duration="1m0s"
```

کلید `logger` و `foo="bar"` توسط فراخوانندهٔ تابعی اضافه شده‌اند
که پیام `runtime` و مقدار `duration="1m0s"` را لاگ می‌کند، بدون آنکه نیازی به
تغییر آن تابع باشد.

با غیرفعال بودن لاگ‌برداری زمینه‌ای، `WithValues` و `WithName` هیچ کاری انجام نمی‌دهند و فراخوانی‌های
لاگ از طریق لاگر سراسری klog انجام می‌شوند. بنابراین این اطلاعات اضافی
دیگر در خروجی لاگ وجود ندارد:

```console
$ go run . --feature-gates ContextualLogging=false
...
I0222 15:14:40.497333  198174 example.go:54] "runtime" duration="1m0s"
I0222 15:14:40.497346  198174 example.go:55] "another runtime" duration="1h0m0s" duration="1m0s"
```

### قالب لاگ JSON

{{< feature-state for_k8s_version="v1.19" state="alpha" >}}

{{<warning >}}
خروجی JSON از بسیاری از پرچم‌های استاندارد klog پشتیبانی نمی‌کند. برای فهرست پرچم‌های klog پشتیبانی‌نشده،
[مرجع ابزارهای خط فرمان](/docs/reference/command-line-tools-reference/) را ببینید.

تضمینی وجود ندارد که همهٔ لاگ‌ها با قالب JSON نوشته شوند (برای نمونه، هنگام شروع فرایند).
اگر قصد تجزیهٔ لاگ‌ها را دارید، مطمئن شوید که می‌توانید خطوط لاگی را که JSON نیستند نیز مدیریت کنید.

نام فیلدها و سریال‌سازی JSON ممکن است تغییر کنند.
{{< /warning >}}

پرچم `--logging-format=json` قالب لاگ‌ها را از قالب بومی klog به قالب JSON تغییر می‌دهد.
نمونه‌ای از قالب لاگ JSON (با چاپ خوانا):

```json
{
   "ts": 1580306777.04728,
   "v": 4,
   "msg": "Pod status updated",
   "pod":{
      "name": "nginx-1",
      "namespace": "default"
   },
   "status": "ready"
}
```

کلیدهای دارای معنای ویژه:

* `ts` - مهر زمانی به‌صورت زمان یونیکس (الزامی، float)
* `v` - میزان جزئیات (فقط برای پیام‌های info و نه برای پیام‌های خطا، int)
* `err` - رشتهٔ خطا (اختیاری، string)
* `msg` - پیام (الزامی، string)

فهرست اجزایی که در حال حاضر از قالب JSON پشتیبانی می‌کنند:

* {{< glossary_tooltip term_id="kube-controller-manager" text="kube-controller-manager" >}}
* {{< glossary_tooltip term_id="kube-apiserver" text="kube-apiserver" >}}
* {{< glossary_tooltip term_id="kube-scheduler" text="kube-scheduler" >}}
* {{< glossary_tooltip term_id="kubelet" text="kubelet" >}}

### سطح جزئیات لاگ

پرچم `-v` میزان جزئیات لاگ را کنترل می‌کند. افزایش مقدار آن تعداد رویدادهای لاگ‌شده را افزایش می‌دهد.
کاهش مقدار آن تعداد رویدادهای لاگ‌شده را کاهش می‌دهد. افزایش تنظیم جزئیات باعث می‌شود رویدادهایی
با اهمیت کمتر و کمتر نیز لاگ شوند. تنظیم جزئیات روی 0 فقط رویدادهای بحرانی را لاگ می‌کند.

### محل لاگ‌ها

دو نوع جزء سیستمی وجود دارد: اجزایی که در یک کانتینر اجرا می‌شوند و اجزایی
که در کانتینر اجرا نمی‌شوند. برای نمونه:

* زمان‌بند کوبرنتیز و kube-proxy در یک کانتینر اجرا می‌شوند.
* kubelet و {{<glossary_tooltip term_id="container-runtime" text="زمان اجرای کانتینر">}}
  در کانتینر اجرا نمی‌شوند.

روی ماشین‌های دارای systemd، kubelet و زمان اجرای کانتینر در journald می‌نویسند.
در غیر این صورت، در فایل‌های `.log` در دایرکتوری `/var/log` می‌نویسند.
اجزای سیستمی درون کانتینرها همیشه در فایل‌های `.log` در دایرکتوری `/var/log` می‌نویسند
و سازوکار پیش‌فرض لاگ‌برداری را دور می‌زنند.
مشابه لاگ‌های کانتینر، باید لاگ‌های اجزای سیستم را در دایرکتوری `/var/log` چرخش (rotate) دهید.
در کلاسترهای کوبرنتیزی که با اسکریپت `kube-up.sh` ایجاد شده‌اند، چرخش لاگ توسط ابزار `logrotate` پیکربندی می‌شود.
ابزار `logrotate` لاگ‌ها را روزانه، یا هنگامی که اندازهٔ لاگ از 100MB بیشتر شود، چرخش می‌دهد.

## پرس‌وجوی لاگ

{{< feature-state feature_gate_name="NodeLogQuery" >}}

قابلیت پرس‌وجوی لاگ (Log Query) می‌تواند به اشکال‌زدایی مشکلات در نودهای لینوکسی و ویندوزی
کمک کند. این قابلیت که در کوبرنتیز v1.27 معرفی شد، امکان مشاهدهٔ لاگ‌های
سرویس‌هایی را که روی نود اجرا می‌شوند فراهم می‌کند. برای استفاده از این قابلیت، اطمینان حاصل کنید که گزینه‌های پیکربندی kubelet
یعنی `enableSystemLogHandler` و `enableSystemLogQuery`
هر دو برای نود هدف روی _true_ تنظیم شده باشند.

در کوبرنتیز v1.36 این قابلیت به وضعیت پایدار ارتقا یافت و [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `NodeLogQuery`
اکنون روی _true_ قفل شده است؛ بنابراین feature gate به‌طور پیش‌فرض فعال است و
`enableSystemLogHandler` تنها گزینهٔ لازم برای فعال یا غیرفعال کردن
قابلیت پرس‌وجوی لاگ باقی می‌ماند.

مقدار پیش‌فرض `enableSystemLogHandler` برابر _false_ است و توصیه می‌شود
غیرفعال باقی بماند، مگر آنکه در حال اشکال‌زدایی فعال باشید.

{{< warning >}}
اعطای مجوز به `nodes/proxy` (حتی فقط مجوز **get**) دسترسی به
APIهای قدرتمند kubelet را نیز مجاز می‌کند که می‌توان از آن‌ها برای اجرای فرمان
در هر کانتینری که روی نود اجرا می‌شود استفاده کرد؛ بنابراین در نحوهٔ مدیریت آن‌ها دقت کنید.
برای اطلاعات بیشتر
[احراز هویت/مجوزدهی Kubelet](/docs/reference/access-authn-authz/kubelet-authn-authz/#get-nodes-proxy-warning) را ببینید.
{{< /warning >}}

در لینوکس، فرض بر این است که لاگ‌های سرویس از طریق _journald_ در دسترس‌اند. در
ویندوز فرض بر این است که لاگ‌های سرویس در فراهم‌کنندهٔ لاگ برنامه (application log
provider) در دسترس‌اند. در هر دو سیستم‌عامل، لاگ‌ها با خواندن فایل‌های
درون `/var/log/` نیز در دسترس‌اند.

به شرط آنکه مجوز تعامل با آبجکت‌های نود را داشته باشید، می‌توانید این قابلیت را روی همهٔ نودهای خود یا
فقط زیرمجموعه‌ای از آن‌ها امتحان کنید. در اینجا نمونه‌ای برای بازیابی لاگ‌های سرویس kubelet از یک نود آمده است:

```shell
# Fetch kubelet logs from a node named node-1.example
kubectl get --raw "/api/v1/nodes/node-1.example/proxy/logs/?query=kubelet"
```

همچنین می‌توانید فایل‌ها را دریافت کنید، به شرط آنکه فایل‌ها در دایرکتوری‌ای باشند که kubelet اجازهٔ دریافت لاگ
از آن را می‌دهد. برای نمونه، می‌توانید یک لاگ را از `/var/log` روی یک نود لینوکسی دریافت کنید:

```shell
kubectl get --raw "/api/v1/nodes/<insert-node-name-here>/proxy/logs/?query=/<insert-log-file-name-here>"
```

kubelet برای بازیابی لاگ‌ها از روش‌های اکتشافی (heuristics) استفاده می‌کند. این کار در مواقعی کمک می‌کند که نمی‌دانید یک سرویس سیستمی مشخص
لاگ‌ها را در لاگر بومی سیستم‌عامل مانند journald می‌نویسد یا در یک فایل لاگ در `/var/log/`. روش اکتشافی
ابتدا لاگر بومی را بررسی می‌کند و اگر در دسترس نباشد، تلاش می‌کند نخستین لاگ‌ها را از
`/var/log/<servicename>` یا `/var/log/<servicename>.log` یا `/var/log/<servicename>/<servicename>.log` بازیابی کند.

فهرست کامل گزینه‌های قابل استفاده عبارت است از:

| گزینه      | توضیح                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------|
| `boot`      | boot پیام‌های یک راه‌اندازی (boot) مشخص سیستم را نشان می‌دهد                                                      |
| `pattern`   | pattern مدخل‌های لاگ را بر اساس عبارت منظم سازگار با PERL ارائه‌شده فیلتر می‌کند                      |
| `query`     | query سرویس(ها) یا فایل‌هایی را که لاگ‌ها باید از آن‌ها بازگردانده شوند مشخص می‌کند (الزامی)                           |
| `sinceTime` | یک مهر زمانی [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) که لاگ‌ها از آن به بعد نشان داده می‌شوند (شامل خود آن)  |
| `untilTime` | یک مهر زمانی [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) که لاگ‌ها تا آن نشان داده می‌شوند (شامل خود آن) |
| `tailLines` | مشخص می‌کند چند خط از انتهای لاگ بازیابی شود؛ پیش‌فرض دریافت کل لاگ است   |

نمونه‌ای از یک پرس‌وجوی پیچیده‌تر:

```shell
# Fetch kubelet logs from a node named node-1.example that have the word "error"
kubectl get --raw "/api/v1/nodes/node-1.example/proxy/logs/?query=kubelet&pattern=error"
```

## {{% heading "whatsnext" %}}

* دربارهٔ [معماری لاگ‌برداری کوبرنتیز](/docs/concepts/cluster-administration/logging/) بخوانید
* دربارهٔ [لاگ‌برداری ساختاریافته](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/1602-structured-logging) بخوانید
* دربارهٔ [لاگ‌برداری زمینه‌ای](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/3077-contextual-logging) بخوانید
* دربارهٔ [منسوخ شدن پرچم‌های klog](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2845-deprecate-klog-specific-flags-in-k8s-components) بخوانید
* دربارهٔ [قراردادهای سطح اهمیت لاگ‌برداری](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-instrumentation/logging.md) بخوانید
* دربارهٔ [پرس‌وجوی لاگ](https://kep.k8s.io/2258) بخوانید

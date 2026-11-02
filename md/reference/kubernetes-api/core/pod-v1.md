---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "Pod"
content_type: "api_reference"
description: "Pod مجموعه‌ای از کانتینرهاست که می‌تواند روی یک میزبان اجرا شود. این منبع توسط کلاینت‌ها ایجاد می‌شود و روی میزبان‌ها زمان‌بندی می‌گردد."
title: "Pod"
weight: 100
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## Pod {#Pod}

Pod مجموعه‌ای از کانتینرهاست که می‌تواند روی یک میزبان اجرا شود. این منبع توسط کلاینت‌ها ایجاد می‌شود و روی میزبان‌ها زمان‌بندی می‌گردد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind مقداری رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. قابل به‌روزرسانی نیست. با قالب CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#PodSpec" >}}">PodSpec</a></em></td>
      <td>مشخصات رفتار مطلوب Pod. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#PodStatus" >}}">PodStatus</a></em></td>
      <td>آخرین وضعیت مشاهده‌شده Pod. ممکن است این داده به‌روز نباشد. توسط سیستم مقداردهی می‌شود. فقط‌خواندنی است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
  </tbody>
</table>

## PodSpec {#PodSpec}

PodSpec توصیف یک pod است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>activeDeadlineSeconds</code><br/><em>integer</em></td>
      <td>مدت‌زمان اختیاری، بر حسب ثانیه، که pod می‌تواند نسبت به StartTime روی نود فعال بماند؛ پس از آن سامانه به‌طور فعال تلاش می‌کند آن را ناموفق علامت‌گذاری کند و کانتینرهای وابسته به آن را از بین ببرد. مقدار باید عددی صحیح و مثبت باشد.</td>
    </tr>
    <tr>
      <td><code>affinity</code><br/><em><a href="{{< ref "#Affinity" >}}">Affinity</a></em></td>
      <td>در صورت تعیین، محدودیت‌های زمان‌بندی pod را مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>automountServiceAccountToken</code><br/><em>boolean</em></td>
      <td>AutomountServiceAccountToken مشخص می‌کند که آیا توکن service account باید به‌طور خودکار mount شود یا نه.</td>
    </tr>
    <tr>
      <td><code>containers</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#Container" >}}">Container array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>فهرست کانتینرهای متعلق به pod. در حال حاضر نمی‌توان کانتینری را اضافه یا حذف کرد. هر Pod باید دست‌کم یک کانتینر داشته باشد. این فیلد قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>dnsConfig</code><br/><em><a href="{{< ref "#PodDNSConfig" >}}">PodDNSConfig</a></em></td>
      <td>پارامترهای DNS یک pod را مشخص می‌کند. پارامترهای تعیین‌شده در اینجا با پیکربندی DNS تولیدشده بر اساس DNSPolicy ادغام می‌شوند.</td>
    </tr>
    <tr>
      <td><code>dnsPolicy</code><br/><em>string</em></td>
      <td>سیاست DNS مربوط به pod را تعیین می‌کند. مقدار پیش‌فرض "ClusterFirst" است. مقادیر معتبر عبارت‌اند از 'ClusterFirstWithHostNet'، 'ClusterFirst'، 'Default' و 'None'. پارامترهای DNS که در DNSConfig داده می‌شوند با سیاست انتخاب‌شده در DNSPolicy ادغام می‌شوند. برای اینکه گزینه‌های DNS همراه با hostNetwork تنظیم شوند، باید سیاست DNS را صراحتاً روی 'ClusterFirstWithHostNet' بگذارید.<br/><br/>مقادیر ممکن enum:<br/> - `"ClusterFirst"` نشان می‌دهد که pod باید ابتدا از DNS کلاستر استفاده کند، مگر اینکه hostNetwork برابر true باشد؛ اگر DNS کلاستر در دسترس نباشد، به تنظیمات پیش‌فرض DNS (که kubelet تعیین می‌کند) بازمی‌گردد.<br/> - `"ClusterFirstWithHostNet"` نشان می‌دهد که pod باید ابتدا از DNS کلاستر استفاده کند و اگر در دسترس نباشد، به تنظیمات پیش‌فرض DNS (که kubelet تعیین می‌کند) بازگردد.<br/> - `"Default"` نشان می‌دهد که pod باید از تنظیمات پیش‌فرض DNS (که kubelet تعیین می‌کند) استفاده کند.<br/> - `"None"` نشان می‌دهد که pod باید از تنظیمات خالی DNS استفاده کند. پارامترهای DNS مانند nameserverها و مسیرهای جست‌وجو باید از طریق DNSConfig تعریف شوند.</td>
    </tr>
    <tr>
      <td><code>enableServiceLinks</code><br/><em>boolean</em></td>
      <td>EnableServiceLinks مشخص می‌کند که آیا اطلاعات مربوط به سرویس‌ها، مطابق با نحو Docker links، باید در متغیرهای محیطی pod تزریق شود یا نه. اختیاری: مقدار پیش‌فرض true است.</td>
    </tr>
    <tr>
      <td><code>ephemeralContainers</code><br/><em><a href="{{< ref "#EphemeralContainer" >}}">EphemeralContainer array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>فهرست کانتینرهای موقت (ephemeral) که در این pod اجرا می‌شوند. کانتینرهای موقت را می‌توان در یک pod موجود اجرا کرد تا اقدامات آغازشده توسط کاربر، مانند اشکال‌زدایی، انجام شود. این فهرست را هنگام ایجاد pod نمی‌توان تعیین کرد و با به‌روزرسانی spec مربوط به pod نیز قابل تغییر نیست. برای افزودن یک کانتینر موقت به pod موجود، از زیرمنبع ephemeralcontainers مربوط به pod استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>evictionResponders</code><br/><em><a href="{{< ref "#EvictionResponder" >}}">EvictionResponder array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>evictionResponders به پاسخ‌دهنده‌هایی ارجاع می‌دهد که بر اساس EvictionRequestها به Evictionها واکنش نشان می‌دهند. پاسخ‌دهنده‌ها باید از طریق Eviction Resource API رویدادها را زیر نظر بگیرند و با آن ارتباط برقرار کنند تا به خاتمه‌ی مناسب و ملایم pod کمک کنند. پاسخ‌دهنده‌ها به‌ترتیب و مطابق اولویت تعیین‌شده‌شان انتخاب می‌شوند. پاسخ‌دهنده‌ها باید به‌طور دوره‌ای پیشرفت eviction را با به‌روزرسانی فیلد .status.responders[].heartbeatTime در آبجکت Eviction گزارش کنند. اگر این فیلد در مهلت heartbeat که Eviction API تعریف می‌کند (در حال حاضر ۲۰ دقیقه) به‌روزرسانی نشود، eviction به پاسخ‌دهنده‌ی بعدی با اولویت پایین‌تر واگذار می‌شود. اگر پاسخ‌دهنده‌ی دیگری وجود نداشته باشد، آخرین پاسخ‌دهنده‌ی پیش‌فرض با نام imperative-eviction.k8s.io/evictor و اولویت ۱۰۰، pod را با استفاده از Eviction API دستوری (imperative) (زیرمنبع pods/\<name>/eviction) خارج می‌کند. حداکثر طول فهرست پاسخ‌دهنده‌ها ۱۰ است. هنگامی که pod بخشی از یک PodGroup باشد (یعنی .spec.schedulingGroup تنظیم شده باشد)، پاسخ‌دهنده‌ها پشتیبانی نمی‌شوند. این فیلد را فقط هنگام ایجاد می‌توان تنظیم کرد و پس از آن تغییرناپذیر است.</td>
    </tr>
    <tr>
      <td><code>hostAliases</code><br/><em><a href="{{< ref "#HostAlias" >}}">HostAlias array</a></em><br/><em>patch strategy: merge on key <code>ip</code></em></td>
      <td>HostAliases فهرستی اختیاری از میزبان‌ها و IPها است که در صورت تعیین، در فایل hosts مربوط به pod تزریق می‌شود.</td>
    </tr>
    <tr>
      <td><code>hostIPC</code><br/><em>boolean</em></td>
      <td>از فضای نام ipc میزبان استفاده می‌کند. اختیاری: مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>hostNetwork</code><br/><em>boolean</em></td>
      <td>شبکه‌ی میزبان برای این pod درخواست شده است و از فضای نام شبکه‌ی میزبان استفاده می‌شود. هنگام استفاده از HostNetwork باید پورت‌ها را مشخص کنید تا زمان‌بند از آن‌ها آگاه باشد. وقتی `hostNetwork` برابر true باشد، فیلدهای `hostPort` تعیین‌شده در تعریف پورت‌ها باید با `containerPort` یکسان باشند و فیلدهای `hostPort` تعیین‌نشده به‌طور پیش‌فرض با `containerPort` برابر می‌شوند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>hostPID</code><br/><em>boolean</em></td>
      <td>از فضای نام pid میزبان استفاده می‌کند. اختیاری: مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>hostUsers</code><br/><em>boolean</em></td>
      <td>از فضای نام کاربر میزبان استفاده می‌کند. اختیاری: مقدار پیش‌فرض true است. اگر مقدار true باشد یا فیلد وجود نداشته باشد، pod در فضای نام کاربر میزبان اجرا می‌شود؛ این حالت زمانی مفید است که pod به قابلیتی نیاز دارد که فقط در فضای نام کاربر میزبان در دسترس است، مانند بارگذاری ماژول هسته با CAP_SYS_MODULE. اگر مقدار false باشد، یک userns جدید برای pod ایجاد می‌شود. تنظیم false برای کاهش آسیب‌پذیری‌های فرار از کانتینر (container breakout) مفید است و حتی به کاربران اجازه می‌دهد کانتینرهای خود را به‌عنوان root اجرا کنند، بدون اینکه در عمل دسترسی root روی میزبان داشته باشند.</td>
    </tr>
    <tr>
      <td><code>hostname</code><br/><em>string</em></td>
      <td>نام میزبان (hostname) Pod را مشخص می‌کند. اگر تعیین نشود، نام میزبان pod روی مقداری که سامانه تعریف می‌کند تنظیم می‌شود.</td>
    </tr>
    <tr>
      <td><code>hostnameOverride</code><br/><em>string</em></td>
      <td>HostnameOverride یک بازنویسی صریح برای نام میزبان pod، آن‌گونه که خود pod آن را می‌بیند، مشخص می‌کند. این فیلد فقط نام میزبان pod را تعیین می‌کند و بر رکوردهای DNS آن تأثیری ندارد. وقتی این فیلد روی یک رشته‌ی غیرخالی تنظیم شود: - بر مقادیر تنظیم‌شده در `hostname` و `subdomain` اولویت دارد. - نام میزبان Pod روی همین مقدار تنظیم می‌شود.<br/> - `setHostnameAsFQDN` باید nil یا false باشد.<br/> - `hostNetwork` باید روی false تنظیم شده باشد.  این فیلد باید یک زیردامنه‌ی DNS معتبر مطابق RFC 1123 باشد و حداکثر ۶۴ نویسه داشته باشد.</td>
    </tr>
    <tr>
      <td><code>imagePullSecrets</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>ImagePullSecrets فهرستی اختیاری از ارجاع‌ها به secretها در همان فضای نام است که برای دریافت (pull) هر یک از ایمیج‌های استفاده‌شده در این PodSpec به کار می‌رود. در صورت تعیین، این secretها به پیاده‌سازی‌های جداگانه‌ی pull کننده ارسال می‌شوند تا از آن‌ها استفاده کنند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod</td>
    </tr>
    <tr>
      <td><code>initContainers</code><br/><em><a href="{{< ref "#Container" >}}">Container array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>فهرست کانتینرهای مقداردهی اولیه (init) متعلق به pod. کانتینرهای init پیش از راه‌اندازی کانتینرهای اصلی و به‌ترتیب اجرا می‌شوند. اگر هر کانتینر init با شکست مواجه شود، pod ناموفق در نظر گرفته می‌شود و مطابق restartPolicy آن با آن برخورد می‌شود. نام کانتینر init یا کانتینر معمولی باید میان همه‌ی کانتینرها یکتا باشد. کانتینرهای init نمی‌توانند اقدام‌های Lifecycle، probeهای Readiness، probeهای Liveness یا probeهای Startup داشته باشند. resourceRequirements یک کانتینر init هنگام زمان‌بندی لحاظ می‌شود؛ به این صورت که بیشترین request/limit برای هر نوع منبع پیدا می‌شود و سپس بیشینه‌ی این مقدار و مجموع مقادیر کانتینرهای معمولی به کار می‌رود. محدودیت‌ها (limits) نیز به شیوه‌ای مشابه برای کانتینرهای init اعمال می‌شوند. در حال حاضر نمی‌توان کانتینرهای init را اضافه یا حذف کرد. این فیلد قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/</td>
    </tr>
    <tr>
      <td><code>nodeName</code><br/><em>string</em></td>
      <td>NodeName مشخص می‌کند این pod روی کدام نود زمان‌بندی شده است. اگر خالی باشد، این pod کاندیدای زمان‌بندی توسط زمان‌بندی است که در schedulerName تعریف شده است. پس از تنظیم این فیلد، kubelet مربوط به این نود مسئول چرخه‌ی عمر این pod می‌شود. از این فیلد نباید برای بیان تمایل به زمان‌بندی pod روی یک نود مشخص استفاده کرد. https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename</td>
    </tr>
    <tr>
      <td><code>nodeSelector</code><br/><em>object</em></td>
      <td>NodeSelector انتخابگری است که برای قرار گرفتن pod روی یک نود باید برقرار باشد؛ یعنی باید با برچسب‌های نود مطابقت داشته باشد تا pod روی آن نود زمان‌بندی شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/</td>
    </tr>
    <tr>
      <td><code>os</code><br/><em><a href="{{< ref "#PodOS" >}}">PodOS</a></em></td>
      <td>سیستم‌عامل کانتینرهای pod را مشخص می‌کند. در صورت تنظیم این فیلد، برخی فیلدهای pod و کانتینر محدود می‌شوند.  اگر فیلد OS روی linux تنظیم شود، فیلدهای زیر باید تنظیم‌نشده باشند: -securityContext.windowsOptions  اگر فیلد OS روی windows تنظیم شود، فیلدهای زیر باید تنظیم‌نشده باشند: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.resources - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.securityContext.supplementalGroupsPolicy - spec.containers[*].securityContext.appArmorProfile - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup</td>
    </tr>
    <tr>
      <td><code>overhead</code><br/><em>object</em></td>
      <td>Overhead سربار منابع مرتبط با اجرای یک pod را برای یک RuntimeClass مشخص نشان می‌دهد. این فیلد هنگام admission توسط کنترل‌کننده‌ی admission مربوط به RuntimeClass به‌طور خودکار مقداردهی می‌شود. اگر کنترل‌کننده‌ی admission مربوط به RuntimeClass فعال باشد، نباید overhead در درخواست‌های ایجاد Pod تنظیم شود. این کنترل‌کننده‌ی admission درخواست‌های ایجاد Podی را که overhead از قبل در آن‌ها تنظیم شده باشد رد می‌کند. اگر RuntimeClass پیکربندی و در PodSpec انتخاب شده باشد، Overhead روی مقداری تنظیم می‌شود که در RuntimeClass متناظر تعریف شده است؛ در غیر این صورت تنظیم‌نشده می‌ماند و صفر در نظر گرفته می‌شود. اطلاعات بیشتر: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md</td>
    </tr>
    <tr>
      <td><code>preemptionPolicy</code><br/><em>string</em></td>
      <td>PreemptionPolicy سیاست مربوط به preempt کردن (جایگزینی) podهای با اولویت پایین‌تر است. یکی از مقادیر Never یا PreemptLowerPriority. وقتی Priority Admission Controller فعال باشد، کاربران نمی‌توانند این فیلد را تنظیم کنند. کنترل‌کننده‌ی admission این فیلد را از روی PriorityClassName مقداردهی می‌کند. در صورت تنظیم‌نشدن، مقدار پیش‌فرض PreemptLowerPriority است.<br/><br/>مقادیر ممکن enum:<br/> - `"Never"` یعنی pod هرگز podهای با اولویت پایین‌تر را preempt نمی‌کند.<br/> - `"PreemptLowerPriority"` یعنی pod می‌تواند podهای با اولویت پایین‌تر را preempt کند.</td>
    </tr>
    <tr>
      <td><code>priority</code><br/><em>integer</em></td>
      <td>مقدار اولویت. اجزای مختلف سامانه از این فیلد برای تعیین اولویت pod استفاده می‌کنند. وقتی Priority Admission Controller فعال باشد، کاربران نمی‌توانند این فیلد را تنظیم کنند. کنترل‌کننده‌ی admission این فیلد را از روی PriorityClassName مقداردهی می‌کند. هرچه مقدار بزرگ‌تر باشد، اولویت بالاتر است.</td>
    </tr>
    <tr>
      <td><code>priorityClassName</code><br/><em>string</em></td>
      <td>در صورت تعیین، اولویت pod را مشخص می‌کند. "system-node-critical" و "system-cluster-critical" دو کلیدواژه‌ی ویژه هستند که بالاترین اولویت‌ها را نشان می‌دهند و اولی بالاترین اولویت را دارد. هر نام دیگری باید با ایجاد یک آبجکت PriorityClass با همان نام تعریف شود. اگر تعیین نشود، اولویت pod برابر مقدار پیش‌فرض خواهد بود، یا اگر مقدار پیش‌فرضی وجود نداشته باشد، صفر می‌شود.</td>
    </tr>
    <tr>
      <td><code>readinessGates</code><br/><em><a href="{{< ref "#PodReadinessGate" >}}">PodReadinessGate array</a></em></td>
      <td>در صورت تعیین، همه‌ی readiness gateها برای تعیین آمادگی pod ارزیابی می‌شوند. یک pod زمانی آماده است که همه‌ی کانتینرهایش آماده باشند و همچنین همه‌ی شرایط (conditions) مشخص‌شده در readiness gateها وضعیتی برابر با "True" داشته باشند. اطلاعات بیشتر: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates</td>
    </tr>
    <tr>
      <td><code>resourceClaims</code><br/><em><a href="{{< ref "#PodResourceClaim" >}}">PodResourceClaim array</a></em><br/><em>patch strategy: merge,retainKeys on key <code>name</code></em></td>
      <td>ResourceClaims تعیین می‌کند کدام ResourceClaimها باید پیش از اجازه‌ی شروع به کار Pod تخصیص داده و رزرو شوند. منابع برای کانتینرهایی که آن‌ها را با نام مصرف می‌کنند در دسترس قرار می‌گیرند.  این فیلد پایدار است، اما نیاز دارد که feature gate با نام DynamicResourceAllocation فعال باشد.  این فیلد تغییرناپذیر است.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em><a href="{{< ref "#ResourceRequirements" >}}">ResourceRequirements</a></em></td>
      <td>Resources مقدار کل منابع CPU و حافظه است که همه‌ی کانتینرهای pod به آن نیاز دارند. فقط تعیین Requests و Limits برای نام منابع "cpu"، "memory" و "hugepages-" پشتیبانی می‌شود. ResourceClaimها پشتیبانی نمی‌شوند.  این فیلد کنترل دقیق بر تخصیص منابع را برای کل pod فراهم می‌کند و اشتراک منابع میان کانتینرهای یک pod را ممکن می‌سازد.  این فیلد آلفا است و نیاز دارد که feature gate با نام PodLevelResources فعال باشد.</td>
    </tr>
    <tr>
      <td><code>restartPolicy</code><br/><em>string</em></td>
      <td>سیاست راه‌اندازی مجدد برای همه‌ی کانتینرهای درون pod. یکی از مقادیر Always، OnFailure یا Never. در برخی زمینه‌ها ممکن است فقط زیرمجموعه‌ای از این مقادیر مجاز باشد. مقدار پیش‌فرض Always است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy<br/><br/>مقادیر ممکن enum:<br/> - `"Always"`<br/> - `"Never"`<br/> - `"OnFailure"`</td>
    </tr>
    <tr>
      <td><code>runtimeClassName</code><br/><em>string</em></td>
      <td>RuntimeClassName به یک آبجکت RuntimeClass در گروه node.k8s.io ارجاع می‌دهد که باید برای اجرای این pod استفاده شود.  اگر هیچ منبع RuntimeClass با نام داده‌شده مطابقت نداشته باشد، pod اجرا نخواهد شد. اگر تنظیم نشود یا خالی باشد، RuntimeClass با نام "legacy" استفاده می‌شود؛ این یک کلاس ضمنی با تعریف خالی است که از handler پیش‌فرض محیط اجرا استفاده می‌کند. اطلاعات بیشتر: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class</td>
    </tr>
    <tr>
      <td><code>schedulerName</code><br/><em>string</em></td>
      <td>در صورت تعیین، pod توسط زمان‌بند مشخص‌شده توزیع (dispatch) می‌شود. در غیر این صورت، pod توسط زمان‌بند پیش‌فرض توزیع می‌شود.</td>
    </tr>
    <tr>
      <td><code>schedulingGates</code><br/><em><a href="{{< ref "#PodSchedulingGate" >}}">PodSchedulingGate array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>SchedulingGates فهرستی مبهم (opaque) از مقادیر است که در صورت تعیین، زمان‌بندی pod را مسدود می‌کند. اگر schedulingGates خالی نباشد، pod در وضعیت SchedulingGated می‌ماند و زمان‌بند تلاشی برای زمان‌بندی pod نمی‌کند.  SchedulingGates را فقط هنگام ایجاد pod می‌توان تنظیم کرد و پس از آن فقط می‌توان آن‌ها را حذف کرد.</td>
    </tr>
    <tr>
      <td><code>schedulingGroup</code><br/><em><a href="{{< ref "#PodSchedulingGroup" >}}">PodSchedulingGroup</a></em></td>
      <td>SchedulingGroup ارجاعی به آبجکت گروه‌بندی زمان‌بندیِ بلافصل در زمان اجرا است که این Pod به آن تعلق دارد. زمان‌بند از این فیلد برای شناسایی گروه و اعمال سیاست‌های صحیح زمان‌بندی گروهی استفاده می‌کند. عضویت در یک گروه بر دیگر جنبه‌های چرخه‌ی عمر Pod که در بستر وسیع‌تر زمان‌بندی اهمیت دارند، مانند preemption و اتصال منابع، نیز اثر می‌گذارد. اگر تعیین نشود، Pod در همه‌ی این جنبه‌ها یک واحد مستقل در نظر گرفته می‌شود. آبجکت گروهی که این فیلد به آن ارجاع می‌دهد ممکن است در زمان ایجاد Pod وجود نداشته باشد. این فیلد تغییرناپذیر است، اما یک آبجکت گروه با همان نام را می‌توان با سیاست‌های متفاوت دوباره ایجاد کرد. انجام این کار در حین زمان‌بندی pod ممکن است باعث شود جایگذاری با سیاست‌های مورد انتظار مطابقت نداشته باشد.</td>
    </tr>
    <tr>
      <td><code>securityContext</code><br/><em><a href="{{< ref "#PodSecurityContext" >}}">PodSecurityContext</a></em></td>
      <td>SecurityContext ویژگی‌های امنیتی در سطح pod و تنظیمات مشترک کانتینرها را نگه می‌دارد. اختیاری: مقدار پیش‌فرض خالی است.  مقادیر پیش‌فرض هر فیلد را در توضیحات نوع ببینید.</td>
    </tr>
    <tr>
      <td><code>serviceAccount</code><br/><em>string</em></td>
      <td>DeprecatedServiceAccount نام مستعار منسوخ‌شده‌ی ServiceAccountName است. منسوخ‌شده: به‌جای آن از serviceAccountName استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>serviceAccountName</code><br/><em>string</em></td>
      <td>ServiceAccountName نام ServiceAccountی است که برای اجرای این pod استفاده می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/</td>
    </tr>
    <tr>
      <td><code>setHostnameAsFQDN</code><br/><em>boolean</em></td>
      <td>اگر true باشد، نام میزبان pod به‌جای نام برگ (leaf name) که حالت پیش‌فرض است، روی FQDN مربوط به pod تنظیم می‌شود. در کانتینرهای Linux این یعنی FQDN در فیلد hostname هسته (فیلد nodename از struct utsname) قرار می‌گیرد. در کانتینرهای Windows این یعنی مقدار رجیستری hostname برای کلید رجیستری HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters روی FQDN تنظیم می‌شود. اگر pod فاقد FQDN باشد، این تنظیم تأثیری ندارد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>shareProcessNamespace</code><br/><em>boolean</em></td>
      <td>یک فضای نام فرایند واحد را میان همه‌ی کانتینرهای pod به اشتراک می‌گذارد. وقتی این فیلد تنظیم شود، کانتینرها می‌توانند فرایندهای کانتینرهای دیگر در همان pod را ببینند و به آن‌ها سیگنال بفرستند، و به اولین فرایند در هر کانتینر PID 1 اختصاص داده نمی‌شود. HostPID و ShareProcessNamespace را نمی‌توان هم‌زمان تنظیم کرد. اختیاری: مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>subdomain</code><br/><em>string</em></td>
      <td>در صورت تعیین، نام میزبان کاملاً مشخص (fully qualified) Pod به شکل "\<hostname>.\<subdomain>.\<pod namespace>.svc.\<cluster domain>" خواهد بود. اگر تعیین نشود، pod اصلاً نام دامنه (domainname) نخواهد داشت.</td>
    </tr>
    <tr>
      <td><code>terminationGracePeriodSeconds</code><br/><em>integer</em></td>
      <td>مدت‌زمان اختیاری، بر حسب ثانیه، که pod برای خاتمه‌ی مناسب و ملایم به آن نیاز دارد. این مقدار را می‌توان در درخواست حذف کاهش داد. مقدار باید عددی صحیح و نامنفی باشد. مقدار صفر یعنی توقف فوری از طریق سیگنال kill (بدون فرصت برای خاموش‌شدن مناسب). اگر این مقدار nil باشد، به‌جای آن از مهلت پیش‌فرض استفاده می‌شود. مهلت خاتمه (grace period) فاصله‌ی زمانی بر حسب ثانیه است میان لحظه‌ای که سیگنال خاتمه به فرایندهای در حال اجرا در pod ارسال می‌شود و لحظه‌ای که فرایندها با سیگنال kill به‌اجبار متوقف می‌شوند. این مقدار را بیشتر از زمان مورد انتظار برای پاک‌سازی فرایند خود تنظیم کنید. مقدار پیش‌فرض ۳۰ ثانیه است.</td>
    </tr>
    <tr>
      <td><code>tolerations</code><br/><em><a href="{{< ref "../definitions/toleration-v1#Toleration" >}}">Toleration array</a></em></td>
      <td>در صورت تعیین، tolerationهای pod را مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>topologySpreadConstraints</code><br/><em><a href="{{< ref "#TopologySpreadConstraint" >}}">TopologySpreadConstraint array</a></em><br/><em>patch strategy: merge on key <code>topologyKey</code></em></td>
      <td>TopologySpreadConstraints توضیح می‌دهد که یک گروه از podها چگونه باید در دامنه‌های توپولوژی پخش شوند. زمان‌بند podها را به‌گونه‌ای زمان‌بندی می‌کند که از این محدودیت‌ها پیروی شود. همه‌ی topologySpreadConstraintها با هم AND می‌شوند.</td>
    </tr>
    <tr>
      <td><code>volumes</code><br/><em><a href="{{< ref "#Volume" >}}">Volume array</a></em><br/><em>patch strategy: merge,retainKeys on key <code>name</code></em></td>
      <td>فهرست حجم‌هایی (volume) که کانتینرهای متعلق به pod می‌توانند mount کنند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes</td>
    </tr>
  </tbody>
</table>

## PodStatus {#PodStatus}

PodStatus اطلاعات مربوط به وضعیت یک Pod را نشان می‌دهد. ممکن است وضعیت از حالت واقعی سیستم عقب باشد، به‌ویژه زمانی که نودی که Pod را میزبانی می‌کند نتواند با control plane ارتباط برقرار کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allocatedResources</code><br/><em>object</em></td>
      <td>allocatedResources مجموع درخواست‌هایی است که نود برای این Pod اختصاص داده است. اگر درخواست‌ها در سطح Pod تنظیم نشده باشند، این مقدار برابر با مجموع درخواست‌های تمام کانتینرهای Pod خواهد بود.</td>
    </tr>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#PodCondition" >}}">PodCondition array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>وضعیت فعلی سرویس Pod. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions</td>
    </tr>
    <tr>
      <td><code>containerStatuses</code><br/><em>ContainerStatus array</em></td>
      <td>وضعیت کانتینرهای این Pod. هر کانتینر در Pod باید حداکثر یک وضعیت در این فهرست داشته باشد و همه وضعیت‌ها باید مربوط به کانتینرهای همین Pod باشند؛ با این حال، این موضوع اعمال نمی‌شود. اگر در فهرست وضعیتی برای یک کانتینر ناموجود وجود داشته باشد یا نام‌های تکراری در آن دیده شود، رفتار مؤلفه‌های مختلف کوبرنتیز تعریف‌نشده است و ممکن است آن وضعیت‌ها نادیده گرفته شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status</td>
    </tr>
    <tr>
      <td><code>ephemeralContainerStatuses</code><br/><em>ContainerStatus array</em></td>
      <td>وضعیت همه کانتینرهای موقت (ephemeral) که در این Pod اجرا شده‌اند. هر کانتینر موقت در Pod باید حداکثر یک وضعیت در این فهرست داشته باشد و همه وضعیت‌ها باید مربوط به کانتینرهای همین Pod باشند؛ با این حال، این موضوع اعمال نمی‌شود. اگر در فهرست وضعیتی برای یک کانتینر ناموجود وجود داشته باشد یا نام‌های تکراری در آن دیده شود، رفتار مؤلفه‌های مختلف کوبرنتیز تعریف‌نشده است و ممکن است آن وضعیت‌ها نادیده گرفته شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status</td>
    </tr>
    <tr>
      <td><code>extendedResourceClaimStatus</code><br/><em><a href="{{< ref "#PodExtendedResourceClaimStatus" >}}">PodExtendedResourceClaimStatus</a></em></td>
      <td>وضعیت extended resource claim که توسط DRA پشتیبانی می‌شود.</td>
    </tr>
    <tr>
      <td><code>hostIP</code><br/><em>string</em></td>
      <td>hostIP آدرس IP میزبانی را نگه می‌دارد که Pod به آن اختصاص یافته است. اگر Pod هنوز شروع به کار نکرده باشد، این مقدار خالی است. ممکن است Pod به نودی اختصاص یابد که kubelet آن مشکل دارد؛ در این صورت حتی با وجود اختصاص یک نود به Pod، مقدار HostIP به‌روزرسانی نخواهد شد.</td>
    </tr>
    <tr>
      <td><code>hostIPs</code><br/><em><a href="{{< ref "#HostIP" >}}">HostIP array</a></em><br/><em>patch strategy: merge on key <code>ip</code></em></td>
      <td>hostIPs آدرس‌های IP اختصاص‌یافته به میزبان را نگه می‌دارد. اگر این فیلد مشخص شود، اولین مورد باید با فیلد hostIP مطابقت داشته باشد. اگر Pod هنوز شروع به کار نکرده باشد، این فهرست خالی است. ممکن است Pod به نودی اختصاص یابد که kubelet آن مشکل دارد؛ در این صورت حتی با وجود اختصاص یک نود به این Pod، مقدار HostIPs به‌روزرسانی نخواهد شد.</td>
    </tr>
    <tr>
      <td><code>initContainerStatuses</code><br/><em>ContainerStatus array</em></td>
      <td>وضعیت init containerهای این Pod. آخرین init container غیرقابل‌راه‌اندازی‌مجدد که با موفقیت اجرا شده باشد، مقدار ready = true خواهد داشت و برای کانتینری که اخیراً شروع به کار کرده است، startTime تنظیم می‌شود. هر init container در Pod باید حداکثر یک وضعیت در این فهرست داشته باشد و همه وضعیت‌ها باید مربوط به کانتینرهای همین Pod باشند؛ با این حال، این موضوع اعمال نمی‌شود. اگر در فهرست وضعیتی برای یک کانتینر ناموجود وجود داشته باشد یا نام‌های تکراری در آن دیده شود، رفتار مؤلفه‌های مختلف کوبرنتیز تعریف‌نشده است و ممکن است آن وضعیت‌ها نادیده گرفته شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-and-container-status</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی خوانا برای انسان که جزئیات دلیل قرار داشتن Pod در این شرایط را بیان می‌کند.</td>
    </tr>
    <tr>
      <td><code>nodeAllocatableResourceClaimStatuses</code><br/><em><a href="{{< ref "#NodeAllocatableResourceClaimStatus" >}}">NodeAllocatableResourceClaimStatus array</a></em><br/><em>patch strategy: merge on key <code>resourceClaimName</code></em></td>
      <td>nodeAllocatableResourceClaimStatuses وضعیت منابع قابل تخصیص نود را نگه می‌دارد که از طریق claimهای DRA برای این Pod اختصاص یافته‌اند. این شامل منابعی است که در حال حاضر در `status.allocatable` آبجکت v1.Node گزارش می‌شوند و جزو extended resourceها نیستند (به https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources مراجعه کنید). نمونه‌ها عبارت‌اند از "cpu"، "memory"، "ephemeral-storage" و hugepages.</td>
    </tr>
    <tr>
      <td><code>nominatedNodeName</code><br/><em>string</em></td>
      <td>nominatedNodeName فقط زمانی تنظیم می‌شود که این Pod چند Pod دیگر را در نود preempt کند، اما نتواند بلافاصله زمان‌بندی شود، زیرا Podهای قربانیِ preemption از دوره پایان تدریجی (graceful termination) خود برخوردارند. این فیلد تضمین نمی‌کند که Pod روی این نود زمان‌بندی شود. اگر نودهای دیگر زودتر در دسترس قرار بگیرند، زمان‌بند ممکن است Pod را در جای دیگری قرار دهد. همچنین زمان‌بند ممکن است منابع این نود را به Podی با اولویت بالاتر بدهد که پس از preemption ایجاد شده است. در نتیجه، هنگام زمان‌بندی Pod ممکن است این فیلد با PodSpec.nodeName متفاوت باشد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>اگر تنظیم شده باشد، نشان‌دهنده مقدار .metadata.generation است که وضعیت Pod بر اساس آن تعیین شده است. برای استفاده از این فیلد باید feature gate با نام PodObservedGenerationTracking فعال باشد.</td>
    </tr>
    <tr>
      <td><code>phase</code><br/><em>string</em></td>
      <td>فاز (phase) یک Pod خلاصه‌ای ساده و سطح بالا از جایگاه Pod در چرخه عمر آن است. آرایه conditions، فیلدهای reason و message و آرایه‌های وضعیت تک‌تک کانتینرها جزئیات بیشتری درباره وضعیت Pod ارائه می‌دهند. پنج مقدار ممکن برای phase وجود دارد:  Pending: Pod توسط سیستم کوبرنتیز پذیرفته شده است، اما یک یا چند ایمیج کانتینر هنوز ایجاد نشده است. این شامل زمان پیش از زمان‌بندی و همچنین زمان دانلود ایمیج‌ها از طریق شبکه است که ممکن است مدتی طول بکشد. Running: Pod به یک نود متصل شده و همه کانتینرها ایجاد شده‌اند. دست‌کم یک کانتینر هنوز در حال اجراست یا در حال شروع یا راه‌اندازی مجدد است. Succeeded: همه کانتینرهای Pod با موفقیت پایان یافته‌اند و دیگر راه‌اندازی مجدد نخواهند شد. Failed: همه کانتینرهای Pod پایان یافته‌اند و دست‌کم یک کانتینر با شکست پایان یافته است. کانتینر یا با وضعیت غیرصفر خارج شده یا توسط سیستم متوقف شده است. Unknown: به دلیلی نمی‌توان وضعیت Pod را به دست آورد، که معمولاً ناشی از خطا در ارتباط با میزبان Pod است.  اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase<br/><br/>Possible enum values:<br/> - `"Failed"` به این معناست که همه کانتینرهای Pod پایان یافته‌اند و دست‌کم یک کانتینر با شکست پایان یافته است (با کد خروج غیرصفر خارج شده یا توسط سیستم متوقف شده است).<br/> - `"Pending"` به این معناست که Pod توسط سیستم پذیرفته شده است، اما یک یا چند کانتینر هنوز شروع به کار نکرده است. این شامل زمان پیش از اتصال به نود و همچنین زمان pull کردن ایمیج‌ها روی میزبان است.<br/> - `"Running"` به این معناست که Pod به یک نود متصل شده و همه کانتینرها شروع به کار کرده‌اند. دست‌کم یک کانتینر هنوز در حال اجراست یا در حال راه‌اندازی مجدد است.<br/> - `"Succeeded"` به این معناست که همه کانتینرهای Pod با کد خروج 0 به‌صورت داوطلبانه پایان یافته‌اند و سیستم قصد ندارد هیچ‌یک از این کانتینرها را مجدداً راه‌اندازی کند.<br/> - `"Unknown"` به این معناست که به دلیلی نمی‌توان وضعیت Pod را به دست آورد، که معمولاً ناشی از خطا در ارتباط با میزبان Pod است. منسوخ‌شده: این مقدار از سال 2015 تنظیم نمی‌شود (74da3b14b0c0f658b3bb8d2def5094686d0e9095)</td>
    </tr>
    <tr>
      <td><code>podIP</code><br/><em>string</em></td>
      <td>podIP آدرس IP اختصاص‌یافته به Pod است که دست‌کم در داخل کلاستر قابل مسیریابی است. اگر هنوز اختصاص نیافته باشد، خالی است.</td>
    </tr>
    <tr>
      <td><code>podIPs</code><br/><em><a href="{{< ref "#PodIP" >}}">PodIP array</a></em><br/><em>patch strategy: merge on key <code>ip</code></em></td>
      <td>podIPs آدرس‌های IP اختصاص‌یافته به Pod را نگه می‌دارد. اگر این فیلد مشخص شود، مورد صفرم باید با فیلد podIP مطابقت داشته باشد. به هر Pod حداکثر یک مقدار برای هر یک از IPv4 و IPv6 می‌تواند اختصاص یابد. اگر هنوز هیچ IP اختصاص نیافته باشد، این فهرست خالی است.</td>
    </tr>
    <tr>
      <td><code>qosClass</code><br/><em>string</em></td>
      <td>طبقه‌بندی کیفیت سرویس (QoS) که بر اساس نیازمندی‌های منابع به Pod اختصاص داده می‌شود. برای مشاهده کلاس‌های QoS موجود، نوع PodQOSClass را ببینید. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes<br/><br/>Possible enum values:<br/> - `"BestEffort"` کلاس QoS با نام BestEffort است.<br/> - `"Burstable"` کلاس QoS با نام Burstable است.<br/> - `"Guaranteed"` کلاس QoS با نام Guaranteed است.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>پیامی کوتاه به‌صورت CamelCase که جزئیات دلیل قرار داشتن Pod در این وضعیت را بیان می‌کند؛ برای مثال 'Evicted'</td>
    </tr>
    <tr>
      <td><code>resize</code><br/><em>string</em></td>
      <td>وضعیت تغییر اندازه منابع مورد نظر برای کانتینرهای Pod. اگر هیچ تغییر اندازه منابعی در انتظار نباشد، خالی است. هر تغییر در منابع کانتینر به‌طور خودکار این مقدار را روی "Proposed" تنظیم می‌کند. منسوخ‌شده: وضعیت تغییر اندازه به دو condition از Pod با نام‌های PodResizePending و PodResizeInProgress منتقل شده است. PodResizePending حالت‌هایی را دنبال می‌کند که در آن‌ها spec تغییر اندازه یافته، اما Kubelet هنوز منابع را اختصاص نداده است. PodResizeInProgress تغییر اندازه‌های در حال انجام را دنبال می‌کند و هرگاه منابع اختصاص‌یافته با منابع تأییدشده برابر نباشند، باید وجود داشته باشد.</td>
    </tr>
    <tr>
      <td><code>resourceClaimStatuses</code><br/><em>PodResourceClaimStatus array</em><br/><em>patch strategy: merge,retainKeys on key <code>name</code></em></td>
      <td>وضعیت resource claimها.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em><a href="{{< ref "#ResourceRequirements" >}}">ResourceRequirements</a></em></td>
      <td>resources نشان‌دهنده درخواست‌ها و محدودیت‌های منابع محاسباتی است که در سطح Pod اعمال شده‌اند، در صورتی که درخواست‌ها یا محدودیت‌های سطح Pod در PodSpec.Resources تنظیم شده باشند.</td>
    </tr>
    <tr>
      <td><code>startTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>تاریخ و زمان بر اساس RFC 3339 که در آن Kubelet آبجکت را تأیید کرده است. این زمان پیش از آن است که Kubelet ایمیج‌های کانتینر Pod را pull کند.</td>
    </tr>
    <tr>
      <td><code>volumeHealth</code><br/><em><a href="{{< ref "#PodVolumeHealth" >}}">PodVolumeHealth array</a></em></td>
      <td>volumeHealth وضعیت سلامتی هر حجم (volume) مورد استفاده Pod را که توسط نود گزارش شده است، نگه می‌دارد. این فیلد توسط kubelet روی نود Pod مقداردهی می‌شود.</td>
    </tr>
  </tbody>
</table>


## PodList {#PodList}

PodList فهرستی از Podها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحواره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "pod-v1#Pod" >}}">Pod array</a></em></td>
      <td>فهرست Podها. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مورد نمایش این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## Affinity {#Affinity}

Affinity مجموعه‌ای از قواعد زمان‌بندی مبتنی بر affinity است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nodeAffinity</code><br/><em><a href="{{< ref "#NodeAffinity" >}}">NodeAffinity</a></em></td>
      <td>قواعد زمان‌بندی مبتنی بر node affinity را برای Pod توصیف می‌کند.</td>
    </tr>
    <tr>
      <td><code>podAffinity</code><br/><em><a href="{{< ref "#PodAffinity" >}}">PodAffinity</a></em></td>
      <td>قواعد زمان‌بندی مبتنی بر pod affinity را توصیف می‌کند (برای مثال، قرار دادن این Pod در همان نود، زون و غیره که Podهای دیگری در آن هستند).</td>
    </tr>
    <tr>
      <td><code>podAntiAffinity</code><br/><em><a href="{{< ref "#PodAntiAffinity" >}}">PodAntiAffinity</a></em></td>
      <td>قواعد زمان‌بندی مبتنی بر pod anti-affinity را توصیف می‌کند (برای مثال، پرهیز از قرار دادن این Pod در همان نود، زون و غیره که Podهای دیگری در آن هستند).</td>
    </tr>
  </tbody>
</table>


## AppArmorProfile {#AppArmorProfile}

AppArmorProfile تنظیمات AppArmor یک Pod یا کانتینر را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>localhostProfile</code><br/><em>string</em></td>
      <td>localhostProfile پروفایلی را مشخص می‌کند که روی نود بارگذاری شده است و باید استفاده شود. برای کارکرد صحیح، پروفایل باید از پیش روی نود پیکربندی شده باشد. این مقدار باید با نام بارگذاری‌شده پروفایل مطابقت داشته باشد. این فیلد فقط و فقط در صورتی باید تنظیم شود که type برابر "Localhost" باشد.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>type مشخص می‌کند که چه نوع پروفایل AppArmor اعمال خواهد شد. گزینه‌های معتبر عبارت‌اند از:   Localhost - پروفایلی که از پیش روی نود بارگذاری شده است.   RuntimeDefault - پروفایل پیش‌فرض محیط اجرای کانتینر.   Unconfined - بدون اعمال AppArmor.<br/><br/>Possible enum values:<br/> - `"Localhost"` نشان می‌دهد که باید از پروفایلی که از پیش روی نود بارگذاری شده است استفاده شود.<br/> - `"RuntimeDefault"` نشان می‌دهد که باید از پروفایل پیش‌فرض AppArmor در محیط اجرای کانتینر استفاده شود.<br/> - `"Unconfined"` نشان می‌دهد که هیچ پروفایل AppArmor اعمال نشود.</td>
    </tr>
  </tbody>
</table>


## AzureFileVolumeSource {#AzureFileVolumeSource}

AzureFile یک mount از سرویس Azure File را روی میزبان نشان می‌دهد که به‌صورت bind mount به Pod متصل می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly به‌طور پیش‌فرض false است (خواندن/نوشتن). مقدار ReadOnly در اینجا، تنظیم ReadOnly را در VolumeMounts اجباری می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>secretName نام Secret حاوی نام و کلید حساب Azure Storage است.</td>
    </tr>
    <tr>
      <td><code>shareName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>shareName نام اشتراک Azure است.</td>
    </tr>
  </tbody>
</table>

## CSIVolumeSource {#CSIVolumeSource}

نشان‌دهنده محل منبع یک حجم (volume) برای mount کردن است که توسط یک درایور CSI خارجی مدیریت می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>driver نام درایور CSI است که این حجم را مدیریت می‌کند. برای دریافت نام صحیحی که در کلاستر ثبت شده است، با مدیر سیستم خود مشورت کنید.</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که mount می‌شود؛ برای مثال "ext4"، "xfs" و "ntfs". اگر مقداری ارائه نشود، مقدار خالی به درایور CSI مرتبط ارسال می‌شود و آن درایور سیستم فایل پیش‌فرض را تعیین و اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>nodePublishSecretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>nodePublishSecretRef ارجاعی به آبجکت secret است که اطلاعات حساس لازم را برای ارسال به درایور CSI و تکمیل فراخوانی‌های CSI NodePublishVolume و NodeUnpublishVolume در خود دارد. این فیلد اختیاری است و اگر به secret نیازی نباشد می‌تواند خالی بماند. اگر آبجکت secret بیش از یک secret داشته باشد، همه ارجاع‌های secret ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly پیکربندی فقط‌خواندنی را برای حجم مشخص می‌کند. مقدار پیش‌فرض false است (خواندن/نوشتن).</td>
    </tr>
    <tr>
      <td><code>volumeAttributes</code><br/><em>object</em></td>
      <td>volumeAttributes ویژگی‌های مختص درایور را نگه می‌دارد که به درایور CSI ارسال می‌شوند. برای مشاهده مقادیر پشتیبانی‌شده، مستندات درایور خود را بررسی کنید.</td>
    </tr>
  </tbody>
</table>


## Capabilities {#Capabilities}

قابلیت‌های (capabilities) POSIX را به کانتینرهای در حال اجرا اضافه یا از آن‌ها حذف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>add</code><br/><em>string array</em></td>
      <td>قابلیت‌های اضافه‌شده</td>
    </tr>
    <tr>
      <td><code>drop</code><br/><em>string array</em></td>
      <td>قابلیت‌های حذف‌شده</td>
    </tr>
  </tbody>
</table>


## CephFSVolumeSource {#CephFSVolumeSource}

نشان‌دهنده یک mount از سیستم فایل Ceph است که تا پایان عمر pod باقی می‌ماند. حجم‌های Cephfs از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>monitors</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>monitors الزامی است: مجموعه‌ای از مانیتورهای Ceph. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>path اختیاری است: به‌جای کل درخت Ceph، به‌عنوان ریشه mount شده استفاده می‌شود. مقدار پیش‌فرض / است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض false است (خواندن/نوشتن). تنظیم ReadOnly در اینجا، تنظیم ReadOnly را در VolumeMounts اجباری می‌کند. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretFile</code><br/><em>string</em></td>
      <td>secretFile اختیاری است: SecretFile مسیر key ring مربوط به User است. مقدار پیش‌فرض /etc/ceph/user.secret است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef اختیاری است: SecretRef ارجاعی به secret احراز هویت برای User است. مقدار پیش‌فرض خالی است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user اختیاری است: User نام کاربری rados است. مقدار پیش‌فرض admin است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
  </tbody>
</table>


## CinderVolumeSource {#CinderVolumeSource}

نشان‌دهنده یک منبع حجم cinder در Openstack است. حجم Cinder باید پیش از mount شدن به کانتینر وجود داشته باشد. همچنین حجم باید در همان region ای باشد که kubelet در آن قرار دارد. حجم‌های Cinder از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که mount می‌شود. این نوع باید توسط سیستم‌عامل میزبان پشتیبانی شود؛ برای مثال "ext4"، "xfs" و "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly به‌طور پیش‌فرض false است (خواندن/نوشتن). تنظیم ReadOnly در اینجا، تنظیم ReadOnly را در VolumeMounts اجباری می‌کند. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef اختیاری است: به آبجکت secret ای اشاره می‌کند که پارامترهای مورد استفاده برای اتصال به OpenStack را در خود دارد.</td>
    </tr>
    <tr>
      <td><code>volumeID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumeID برای شناسایی حجم در cinder استفاده می‌شود. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
  </tbody>
</table>


## ClusterTrustBundleProjection {#ClusterTrustBundleProjection}

ClusterTrustBundleProjection توضیح می‌دهد که چگونه مجموعه‌ای از آبجکت‌های ClusterTrustBundle انتخاب شوند و محتوای آن‌ها در سیستم فایل pod نگاشت (project) شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>labelSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>همه ClusterTrustBundleهایی را که با این انتخابگر برچسب (label selector) مطابقت دارند انتخاب می‌کند. فقط در صورتی اثر دارد که signerName تنظیم شده باشد. با name متقابلاً ناسازگار است. اگر تنظیم نشود، به معنی «هیچ‌چیز را مطابقت نده» تفسیر می‌شود. اگر تنظیم شده ولی خالی باشد، به معنی «همه‌چیز را مطابقت بده» تفسیر می‌شود.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>یک ClusterTrustBundle را بر اساس نام آبجکت انتخاب می‌کند. با signerName و labelSelector متقابلاً ناسازگار است.</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>اگر true باشد، در صورت در دسترس نبودن ClusterTrustBundle یا ClusterTrustBundleهای ارجاع‌شده، راه‌اندازی pod مسدود نمی‌شود. اگر از name استفاده شود، ClusterTrustBundle نام‌برده‌شده مجاز است وجود نداشته باشد. اگر از signerName استفاده شود، ترکیب signerName و labelSelector مجاز است با هیچ ClusterTrustBundle ای مطابقت نداشته باشد.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مسیر نسبی از ریشه حجم برای نوشتن bundle.</td>
    </tr>
    <tr>
      <td><code>signerName</code><br/><em>string</em></td>
      <td>همه ClusterTrustBundleهایی را که با این نام signer مطابقت دارند انتخاب می‌کند. با name متقابلاً ناسازگار است. محتوای همه ClusterTrustBundleهای انتخاب‌شده یکپارچه و تکرارزدایی می‌شود.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>integer</em></td>
      <td>user اختیاری است: UID مالک فایل ایجادشده. در صورت مشخص شدن، فیلد user در سطح آیتم بر defaultUser اولویت دارد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
  </tbody>
</table>


## ConfigMapEnvSource {#ConfigMapEnvSource}

ConfigMapEnvSource یک ConfigMap را برای مقداردهی متغیرهای محیطی انتخاب می‌کند.

محتوای فیلد Data در ConfigMap هدف، جفت‌های کلید-مقدار را به‌صورت متغیرهای محیطی نمایش می‌دهد. کلیدهای فیلد BinaryData در حال حاضر به متغیرهای محیطی کانتینر منتقل نمی‌شوند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده (referent). این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که در اینجا مقدار خالی دارند تقریباً به‌طور قطع نادرست هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا ConfigMap باید تعریف شده باشد یا خیر.</td>
    </tr>
  </tbody>
</table>


## ConfigMapKeySelector {#ConfigMapKeySelector}

یک کلید را از یک ConfigMap انتخاب می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>کلیدی که از فیلد Data در ConfigMap انتخاب می‌شود. کلیدهای فیلد BinaryData در حال حاضر به متغیرهای محیطی کانتینر منتقل نمی‌شوند.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده (referent). این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که در اینجا مقدار خالی دارند تقریباً به‌طور قطع نادرست هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا ConfigMap یا کلید آن باید تعریف شده باشد یا خیر.</td>
    </tr>
  </tbody>
</table>


## ConfigMapProjection {#ConfigMapProjection}

یک ConfigMap را به یک حجم نگاشت‌شده (projected volume) تطبیق می‌دهد.

محتوای فیلد Data در ConfigMap هدف، در یک projected volume به‌صورت فایل ارائه می‌شود و کلیدهای فیلد Data به‌عنوان نام فایل‌ها استفاده می‌شوند، مگر آنکه عنصر items با نگاشت‌های مشخصی از کلیدها به مسیرها مقداردهی شده باشد. توجه کنید که این مورد با منبع حجم configmap یکسان است، با این تفاوت که حالت (mode) پیش‌فرض ندارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#KeyToPath" >}}">KeyToPath array</a></em></td>
      <td>اگر items مشخص نشود، هر جفت کلید-مقدار در فیلد Data از ConfigMap ارجاع‌شده به‌صورت یک فایل در حجم نگاشت می‌شود که نام آن کلید و محتوای آن مقدار است. اگر مشخص شود، کلیدهای فهرست‌شده در مسیرهای تعیین‌شده نگاشت می‌شوند و کلیدهای فهرست‌نشده وجود نخواهند داشت. اگر کلیدی مشخص شود که در ConfigMap وجود ندارد، راه‌اندازی حجم با خطا مواجه می‌شود، مگر آنکه به‌عنوان اختیاری علامت‌گذاری شده باشد. مسیرها باید نسبی باشند و نباید شامل مسیر '..' باشند یا با '..' شروع شوند.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده (referent). این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که در اینجا مقدار خالی دارند تقریباً به‌طور قطع نادرست هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>optional مشخص می‌کند که آیا ConfigMap یا کلیدهای آن باید تعریف شده باشند یا خیر.</td>
    </tr>
  </tbody>
</table>


## ConfigMapVolumeSource {#ConfigMapVolumeSource}

یک ConfigMap را به یک حجم تطبیق می‌دهد.

محتوای فیلد Data در ConfigMap هدف، در یک حجم به‌صورت فایل ارائه می‌شود و کلیدهای فیلد Data به‌عنوان نام فایل‌ها استفاده می‌شوند، مگر آنکه عنصر items با نگاشت‌های مشخصی از کلیدها به مسیرها مقداردهی شده باشد. حجم‌های ConfigMap از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>defaultMode</code><br/><em>integer</em></td>
      <td>defaultMode اختیاری است: بیت‌های حالت (mode) که به‌طور پیش‌فرض برای تنظیم مجوزهای فایل‌های ایجادشده استفاده می‌شوند. باید یک مقدار octal بین 0000 و 0777 یا یک مقدار decimal بین 0 و 511 باشد. YAML هر دو مقدار octal و decimal را می‌پذیرد، اما JSON برای بیت‌های mode مقدار decimal می‌طلبد. مقدار پیش‌فرض 0644 است. دایرکتوری‌های درون مسیر تحت تأثیر این تنظیم قرار نمی‌گیرند. ممکن است این مقدار با گزینه‌های دیگری که بر حالت فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های mode دیگری اعمال شوند.</td>
    </tr>
    <tr>
      <td><code>defaultUser</code><br/><em>integer</em></td>
      <td>defaultUser اختیاری است: UID مالک پیش‌فرض فایل‌های ایجادشده. فیلد defaultUser فقط زمانی به‌عنوان مقدار جایگزین استفاده می‌شود که فیلد user در سطح آیتم تنظیم نشده باشد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#KeyToPath" >}}">KeyToPath array</a></em></td>
      <td>اگر items مشخص نشود، هر جفت کلید-مقدار در فیلد Data از ConfigMap ارجاع‌شده به‌صورت یک فایل در حجم نگاشت می‌شود که نام آن کلید و محتوای آن مقدار است. اگر مشخص شود، کلیدهای فهرست‌شده در مسیرهای تعیین‌شده نگاشت می‌شوند و کلیدهای فهرست‌نشده وجود نخواهند داشت. اگر کلیدی مشخص شود که در ConfigMap وجود ندارد، راه‌اندازی حجم با خطا مواجه می‌شود، مگر آنکه به‌عنوان اختیاری علامت‌گذاری شده باشد. مسیرها باید نسبی باشند و نباید شامل مسیر '..' باشند یا با '..' شروع شوند.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده (referent). این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که در اینجا مقدار خالی دارند تقریباً به‌طور قطع نادرست هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>optional مشخص می‌کند که آیا ConfigMap یا کلیدهای آن باید تعریف شده باشند یا خیر.</td>
    </tr>
  </tbody>
</table>

## Container {#Container}

یک کانتینر برنامهٔ منفرد که می‌خواهید درون یک pod اجرا کنید.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>args</code><br/><em>string array</em></td>
      <td>آرگومان‌های entrypoint. اگر این فیلد مشخص نشود، از CMD ایمیج کانتینر استفاده می‌شود. ارجاع‌های متغیر به شکل $(VAR_NAME) با استفاده از محیط کانتینر جایگزین می‌شوند. اگر متغیری قابل شناسایی نباشد، ارجاع در رشتهٔ ورودی بدون تغییر باقی می‌ماند. دو علامت $$ به یک $ تبدیل می‌شوند که امکان escape کردن نحو $(VAR_NAME) را فراهم می‌کند؛ یعنی "$$(VAR_NAME)" رشتهٔ لفظی "$(VAR_NAME)" را تولید می‌کند. ارجاع‌های escape‌شده هرگز جایگزین نمی‌شوند، چه آن متغیر وجود داشته باشد و چه نداشته باشد. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</td>
    </tr>
    <tr>
      <td><code>command</code><br/><em>string array</em></td>
      <td>آرایهٔ entrypoint. درون یک shell اجرا نمی‌شود. اگر این فیلد مشخص نشود، از ENTRYPOINT ایمیج کانتینر استفاده می‌شود. ارجاع‌های متغیر به شکل $(VAR_NAME) با استفاده از محیط کانتینر جایگزین می‌شوند. اگر متغیری قابل شناسایی نباشد، ارجاع در رشتهٔ ورودی بدون تغییر باقی می‌ماند. دو علامت $$ به یک $ تبدیل می‌شوند که امکان escape کردن نحو $(VAR_NAME) را فراهم می‌کند؛ یعنی "$$(VAR_NAME)" رشتهٔ لفظی "$(VAR_NAME)" را تولید می‌کند. ارجاع‌های escape‌شده هرگز جایگزین نمی‌شوند، چه آن متغیر وجود داشته باشد و چه نداشته باشد. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</td>
    </tr>
    <tr>
      <td><code>env</code><br/><em><a href="{{< ref "#EnvVar" >}}">EnvVar array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>فهرست متغیرهای محیطی که باید در کانتینر تنظیم شوند. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>envFrom</code><br/><em><a href="{{< ref "#EnvFromSource" >}}">EnvFromSource array</a></em></td>
      <td>فهرست منابعی که متغیرهای محیطی کانتینر از آن‌ها پر می‌شوند. کلیدهای تعریف‌شده در یک منبع می‌توانند از هر نویسهٔ ASCII قابل چاپ به‌جز '=' تشکیل شوند. اگر یک کلید در چند منبع وجود داشته باشد، مقدار مربوط به آخرین منبع اولویت دارد. مقادیری که با Env و کلید تکراری تعریف شده باشند نیز اولویت دارند. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>image</code><br/><em>string</em></td>
      <td>نام ایمیج کانتینر. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images این فیلد اختیاری است تا مدیریت پیکربندی در سطح بالاتر بتواند ایمیج‌های کانتینر را در کنترل‌کننده‌های بار کاری مانند Deployment و StatefulSet به‌صورت پیش‌فرض تنظیم یا بازنویسی کند.</td>
    </tr>
    <tr>
      <td><code>imagePullPolicy</code><br/><em>string</em></td>
      <td>سیاست دریافت (pull) ایمیج. یکی از Always، Never و IfNotPresent. اگر تگ :latest مشخص شده باشد، مقدار پیش‌فرض Always و در غیر این صورت IfNotPresent است. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images#updating-images<br/><br/>مقادیر ممکن enum:<br/> - `"Always"` به این معناست که kubelet همواره تلاش می‌کند جدیدترین ایمیج را دریافت کند. اگر دریافت ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"IfNotPresent"` به این معناست که kubelet فقط در صورتی ایمیج را دریافت می‌کند که روی دیسک موجود نباشد. اگر ایمیج موجود نباشد و دریافت آن ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"Never"` به این معناست که kubelet هرگز ایمیجی دریافت نمی‌کند و فقط از ایمیج محلی استفاده می‌کند. اگر ایمیج موجود نباشد، کانتینر با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>lifecycle</code><br/><em><a href="{{< ref "#Lifecycle" >}}">Lifecycle</a></em></td>
      <td>اقداماتی که سامانهٔ مدیریت باید در پاسخ به رویدادهای چرخهٔ حیات کانتینر انجام دهد. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>livenessProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>بررسی دوره‌ای زنده بودن کانتینر. اگر این probe ناموفق باشد، کانتینر دوباره راه‌اندازی می‌شود. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام کانتینر که به‌صورت DNS_LABEL مشخص می‌شود. هر کانتینر در یک pod باید نامی یکتا (DNS_LABEL) داشته باشد. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>ports</code><br/><em><a href="{{< ref "#ContainerPort" >}}">ContainerPort array</a></em><br/><em>patch strategy: merge on key <code>containerPort</code></em></td>
      <td>فهرست پورت‌هایی که از کانتینر در دسترس قرار می‌گیرند. مشخص نکردن یک پورت در اینجا مانع از در دسترس بودن آن پورت NEMI‌شود؛ هر پورتی که درون کانتینر روی نشانی پیش‌فرض "0.0.0.0" گوش می‌دهد، از طریق شبکه قابل دسترسی خواهد بود. تغییر این آرایه با strategic merge patch ممکن است داده‌ها را خراب کند. برای اطلاعات بیشتر به https://github.com/kubernetes/kubernetes/issues/108255 مراجعه کنید. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>readinessProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>بررسی دوره‌ای آماده بودن سرویس کانتینر. اگر این probe ناموفق باشد، کانتینر از endpointهای سرویس حذف می‌شود. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes</td>
    </tr>
    <tr>
      <td><code>resizePolicy</code><br/><em><a href="{{< ref "#ContainerResizePolicy" >}}">ContainerResizePolicy array</a></em></td>
      <td>سیاست تغییر اندازهٔ منابع برای کانتینر. این فیلد را نمی‌توان روی کانتینرهای ephemeral تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em><a href="{{< ref "#ResourceRequirements" >}}">ResourceRequirements</a></em></td>
      <td>منابع محاسباتی مورد نیاز این کانتینر. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</td>
    </tr>
    <tr>
      <td><code>restartPolicy</code><br/><em>string</em></td>
      <td>RestartPolicy رفتار راه‌اندازی مجدد هر کانتینر را در یک pod تعیین می‌کند و سیاست راه‌اندازی مجدد در سطح pod را بازنویسی می‌کند. اگر این فیلد مشخص نشود، رفتار راه‌اندازی مجدد بر اساس سیاست راه‌اندازی مجدد Pod و نوع کانتینر تعیین می‌شود. افزون بر این، تنظیم RestartPolicy روی "Always" برای یک init container این اثر را دارد: این init container پس از هر خروج به‌طور مداوم دوباره راه‌اندازی می‌شود تا زمانی که همهٔ کانتینرهای معمولی پایان یابند. پس از اتمام همهٔ کانتینرهای معمولی، تمام init containerهایی که restartPolicy آن‌ها "Always" است خاموش می‌شوند. این چرخهٔ حیات با init containerهای معمولی تفاوت دارد و اغلب از آن با عنوان کانتینر «sidecar» یاد می‌شود. اگرچه این init container همچنان در توالی init containerها شروع می‌شود، پیش از رفتن به init container بعدی منتظر پایان آن نمی‌ماند. در عوض، init container بعدی بلافاصله پس از شروع این init container یا پس از موفقیت هر startupProbe آغاز می‌شود.</td>
    </tr>
    <tr>
      <td><code>restartPolicyRules</code><br/><em><a href="{{< ref "#ContainerRestartRule" >}}">ContainerRestartRule array</a></em></td>
      <td>فهرستی از قواعد را نشان می‌دهد که برای تعیین اینکه کانتینر هنگام خروج باید دوباره راه‌اندازی شود یا نه، بررسی می‌شوند. قواعد به‌ترتیب ارزیابی می‌شوند. به‌محض اینکه یک قاعده با شرط خروج کانتینر مطابقت پیدا کند، قواعد باقی‌مانده نادیده گرفته می‌شوند. اگر هیچ قاعده‌ای با شرط خروج کانتینر مطابقت نداشته باشد، سیاست راه‌اندازی مجدد در سطح کانتینر تعیین می‌کند که کانتینر دوباره راه‌اندازی شود یا نه. محدودیت‌های قواعد: - حداکثر ۲۰ قاعده مجاز است. - قواعد می‌توانند action یکسان داشته باشند. - قواعد یکسان در اعتبارسنجی‌ها ممنوع نشده‌اند. وقتی قواعد مشخص می‌شوند، کانتینر باید RestartPolicy را صراحتاً تنظیم کند، حتی اگر با RestartPolicy مربوط به Pod یکسان باشد.</td>
    </tr>
    <tr>
      <td><code>securityContext</code><br/><em><a href="{{< ref "#SecurityContext" >}}">SecurityContext</a></em></td>
      <td>SecurityContext گزینه‌های امنیتی‌ای را تعیین می‌کند که کانتینر باید با آن‌ها اجرا شود. در صورت تنظیم، فیلدهای SecurityContext فیلدهای متناظر در PodSecurityContext را بازنویسی می‌کنند. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/</td>
    </tr>
    <tr>
      <td><code>startupProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>StartupProbe نشان می‌دهد که Pod با موفقیت مقداردهی اولیه شده است. در صورت تعیین، تا زمانی که این probe با موفقیت کامل نشود، هیچ probe دیگری اجرا نمی‌شود. اگر این probe ناموفق باشد، Pod دوباره راه‌اندازی می‌شود، درست مانند وقتی که livenessProbe ناموفق باشد. از این probe می‌توان برای تعیین پارامترهای متفاوت probe در ابتدای چرخهٔ حیات Pod استفاده کرد، یعنی زمانی که بارگذاری داده‌ها یا گرم کردن حافظهٔ نهان ممکن است زمان زیادی ببرد، در مقایسه با عملکرد پایدار. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes</td>
    </tr>
    <tr>
      <td><code>stdin</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا این کانتینر باید برای stdin در محیط اجرای کانتینر یک بافر اختصاص دهد یا نه. اگر این فیلد تنظیم نشود، خواندن از stdin در کانتینر همواره به EOF منجر می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdinOnce</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا محیط اجرای کانتینر باید کانال stdin را پس از باز شدن توسط یک attach واحد ببندد یا نه. وقتی stdin برابر true باشد، جریان stdin در چندین نشست attach باز می‌ماند. اگر stdinOnce روی true تنظیم شود، stdin هنگام شروع کانتینر باز می‌شود، تا اتصال نخستین کلاینت به stdin خالی است، سپس باز می‌ماند و داده می‌پذیرد تا زمانی که کلاینت قطع شود؛ در آن زمان stdin بسته می‌شود و تا راه‌اندازی مجدد کانتینر بسته می‌ماند. اگر این پرچم false باشد، فرایند کانتینری که از stdin می‌خواند هرگز EOF دریافت نمی‌کند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>terminationMessagePath</code><br/><em>string</em></td>
      <td>اختیاری: مسیری که فایل حاوی پیام پایان کانتینر در آن نوشته می‌شود و در فایل‌سیستم کانتینر mount شده است. پیام نوشته‌شده باید یک وضعیت نهایی مختصر باشد، مانند پیام شکست یک assertion. اگر اندازهٔ پیام از ۴۰۹۶ بایت بیشتر باشد، نود آن را کوتاه می‌کند. مجموع طول پیام در همهٔ کانتینرها به ۱۲ کیلوبایت محدود می‌شود. مقدار پیش‌فرض /dev/termination-log است. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>terminationMessagePolicy</code><br/><em>string</em></td>
      <td>نحوهٔ پر شدن پیام پایان را مشخص می‌کند. File از محتوای terminationMessagePath برای پر کردن پیام وضعیت کانتینر، چه در موفقیت و چه در شکست، استفاده می‌کند. FallbackToLogsOnError اگر فایل پیام پایان خالی باشد و کانتینر با خطا خارج شده باشد، از آخرین بخش خروجی لاگ کانتینر استفاده می‌کند. خروجی لاگ به ۲۰۴۸ بایت یا ۸۰ خط، هر کدام کمتر باشد، محدود می‌شود. مقدار پیش‌فرض File است. قابل به‌روزرسانی نیست.<br/><br/>مقادیر ممکن enum:<br/> - `"FallbackToLogsOnError"` هنگامی که کانتینر با خطا خارج شود و terminationMessagePath محتوایی نداشته باشد، جدیدترین محتوای لاگ‌های کانتینر را برای پیام وضعیت کانتینر می‌خواند.<br/> - `"File"` رفتار پیش‌فرض است و هنگام خروج کانتینر، پیام وضعیت کانتینر را برابر محتوای terminationMessagePath کانتینر قرار می‌دهد.</td>
    </tr>
    <tr>
      <td><code>tty</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا این کانتینر باید برای خود یک TTY اختصاص دهد یا نه؛ این کار مستلزم آن است که 'stdin' نیز true باشد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>volumeDevices</code><br/><em><a href="{{< ref "#VolumeDevice" >}}">VolumeDevice array</a></em><br/><em>patch strategy: merge on key <code>devicePath</code></em></td>
      <td>volumeDevices فهرست دستگاه‌های بلوکی است که کانتینر از آن‌ها استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>volumeMounts</code><br/><em><a href="{{< ref "#VolumeMount" >}}">VolumeMount array</a></em><br/><em>patch strategy: merge on key <code>mountPath</code></em></td>
      <td>حجم‌های (volume) Pod که باید در فایل‌سیستم کانتینر mount شوند. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>workingDir</code><br/><em>string</em></td>
      <td>دایرکتوری کاری کانتینر. اگر مشخص نشود، از مقدار پیش‌فرض محیط اجرای کانتینر استفاده می‌شود که ممکن است در ایمیج کانتینر پیکربندی شده باشد. قابل به‌روزرسانی نیست.</td>
    </tr>
  </tbody>
</table>


## ContainerExtendedResourceRequest {#ContainerExtendedResourceRequest}

ContainerExtendedResourceRequest نگاشت نام کانتینر و نام منبع توسعه‌یافته (extended resource) به نام درخواست دستگاه را نگه می‌دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام کانتینری که منابع را درخواست می‌کند.</td>
    </tr>
    <tr>
      <td><code>requestName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام درخواستی در ResourceClaim ویژه که با منبع توسعه‌یافته متناظر است.</td>
    </tr>
    <tr>
      <td><code>resourceName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام منبع توسعه‌یافته در آن کانتینر که با DRA پشتیبانی می‌شود.</td>
    </tr>
  </tbody>
</table>


## ContainerPort {#ContainerPort}

ContainerPort یک پورت شبکه را در یک کانتینر منفرد نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerPort</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>شمارهٔ پورتی که روی نشانی IP مربوط به pod در دسترس قرار می‌گیرد. این مقدار باید شمارهٔ پورت معتبر باشد، 0 \< x \< 65536.</td>
    </tr>
    <tr>
      <td><code>hostIP</code><br/><em>string</em></td>
      <td>نشانی IP میزبانی که پورت خارجی به آن bind می‌شود.</td>
    </tr>
    <tr>
      <td><code>hostPort</code><br/><em>integer</em></td>
      <td>شمارهٔ پورتی که روی میزبان در دسترس قرار می‌گیرد. در صورت تعیین، باید شمارهٔ پورت معتبر باشد، 0 \< x \< 65536. اگر HostNetwork مشخص شده باشد، این مقدار باید با ContainerPort برابر باشد. بیشتر کانتینرها به این فیلد نیاز ندارند.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>در صورت تعیین، باید یک IANA_SVC_NAME باشد و درون pod یکتا باشد. هر پورت نام‌دار در یک pod باید نام یکتا داشته باشد. نام پورتی که سرویس‌ها می‌توانند به آن ارجاع دهند.</td>
    </tr>
    <tr>
      <td><code>protocol</code><br/><em>string</em></td>
      <td>پروتکل پورت. باید UDP، TCP یا SCTP باشد. مقدار پیش‌فرض "TCP" است.<br/><br/>مقادیر ممکن enum:<br/> - `"SCTP"` پروتکل SCTP است.<br/> - `"TCP"` پروتکل TCP است.<br/> - `"UDP"` پروتکل UDP است.</td>
    </tr>
  </tbody>
</table>


## ContainerResizePolicy {#ContainerResizePolicy}

ContainerResizePolicy سیاست تغییر اندازهٔ منابع کانتینر را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>resourceName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام منبعی که این سیاست تغییر اندازهٔ منبع برای آن اعمال می‌شود. مقادیر پشتیبانی‌شده: cpu و memory.</td>
    </tr>
    <tr>
      <td><code>restartPolicy</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>سیاست راه‌اندازی مجددی که هنگام تغییر اندازهٔ منبع مشخص‌شده اعمال می‌شود. اگر مشخص نشود، مقدار پیش‌فرض NotRequired است.</td>
    </tr>
  </tbody>
</table>


## ContainerRestartRule {#ContainerRestartRule}

ContainerRestartRule توصیف می‌کند که خروج یک کانتینر چگونه مدیریت می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>action</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>اقدامی را مشخص می‌کند که در صورت برقرار بودن شرایط، هنگام خروج کانتینر انجام می‌شود. تنها مقدار ممکن "Restart" است که کانتینر را دوباره راه‌اندازی می‌کند.</td>
    </tr>
    <tr>
      <td><code>exitCodes</code><br/><em><a href="{{< ref "#ContainerRestartRuleOnExitCodes" >}}">ContainerRestartRuleOnExitCodes</a></em></td>
      <td>کدهای خروجی‌ای را نشان می‌دهد که هنگام خروج کانتینر بررسی می‌شوند.</td>
    </tr>
  </tbody>
</table>


## ContainerRestartRuleOnExitCodes {#ContainerRestartRuleOnExitCodes}

ContainerRestartRuleOnExitCodes شرط مدیریت یک کانتینر خارج‌شده را بر اساس کدهای خروج آن توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>operator</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>رابطهٔ بین کد(های) خروج کانتینر و مقادیر مشخص‌شده را نشان می‌دهد. مقادیر ممکن: - In: اگر کد خروج کانتینر در مجموعهٔ مقادیر مشخص‌شده باشد، شرط برقرار است. - NotIn: اگر کد خروج کانتینر در مجموعهٔ مقادیر مشخص‌شده نباشد، شرط برقرار است.</td>
    </tr>
    <tr>
      <td><code>values</code><br/><em>integer array</em></td>
      <td>مجموعهٔ مقادیری را مشخص می‌کند که برای کدهای خروج کانتینر بررسی می‌شوند. حداکثر ۲۵۵ عنصر مجاز است.</td>
    </tr>
  </tbody>
</table>

## ContainerState {#ContainerState}

ContainerState یکی از حالت‌های ممکن یک کانتینر را نگه می‌دارد. فقط یکی از اعضای آن را می‌توان مشخص کرد. اگر هیچ‌کدام مشخص نشود، حالت پیش‌فرض ContainerStateWaiting است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>running</code><br/><em><a href="{{< ref "#ContainerStateRunning" >}}">ContainerStateRunning</a></em></td>
      <td>جزئیات مربوط به یک کانتینر در حال اجرا</td>
    </tr>
    <tr>
      <td><code>terminated</code><br/><em><a href="{{< ref "#ContainerStateTerminated" >}}">ContainerStateTerminated</a></em></td>
      <td>جزئیات مربوط به یک کانتینر خاتمه‌یافته</td>
    </tr>
    <tr>
      <td><code>waiting</code><br/><em><a href="{{< ref "#ContainerStateWaiting" >}}">ContainerStateWaiting</a></em></td>
      <td>جزئیات مربوط به یک کانتینر در حال انتظار</td>
    </tr>
  </tbody>
</table>


## ContainerStateRunning {#ContainerStateRunning}

ContainerStateRunning حالت اجرای یک کانتینر است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>startedAt</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>زمانی که کانتینر آخرین بار (دوباره) شروع به کار کرده است</td>
    </tr>
  </tbody>
</table>


## ContainerStateTerminated {#ContainerStateTerminated}

ContainerStateTerminated حالت خاتمه‌یافته یک کانتینر است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerID</code><br/><em>string</em></td>
      <td>شناسه کانتینر با قالب '\<type>://\<container_id>'</td>
    </tr>
    <tr>
      <td><code>exitCode</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>وضعیت خروج در آخرین خاتمه کانتینر</td>
    </tr>
    <tr>
      <td><code>finishedAt</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>زمانی که کانتینر آخرین بار خاتمه یافته است</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی درباره آخرین خاتمه کانتینر</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل (مختصر) آخرین خاتمه کانتینر</td>
    </tr>
    <tr>
      <td><code>signal</code><br/><em>integer</em></td>
      <td>سیگنال مربوط به آخرین خاتمه کانتینر</td>
    </tr>
    <tr>
      <td><code>startedAt</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>زمانی که اجرای قبلی کانتینر شروع شده است</td>
    </tr>
  </tbody>
</table>


## ContainerStateWaiting {#ContainerStateWaiting}

ContainerStateWaiting حالت انتظار یک کانتینر است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی درباره دلیل اینکه کانتینر هنوز در حال اجرا نیست.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل (مختصر) اینکه کانتینر هنوز در حال اجرا نیست.</td>
    </tr>
  </tbody>
</table>


## ContainerUser {#ContainerUser}

ContainerUser اطلاعات هویت کاربر را نمایش می‌دهد

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>linux</code><br/><em><a href="{{< ref "#LinuxContainerUser" >}}">LinuxContainerUser</a></em></td>
      <td>این فیلد اطلاعات هویت کاربری را نگه می‌دارد که در لینوکس در ابتدا به نخستین پردازش کانتینرها اختصاص می‌یابد. توجه داشته باشید که اگر پردازش دسترسی کافی داشته باشد، هویت واقعی در حال اجرا می‌تواند تغییر کند.</td>
    </tr>
  </tbody>
</table>


## DownwardAPIProjection {#DownwardAPIProjection}

اطلاعات downward API را برای فرافکنی (projection) در یک projected volume نمایش می‌دهد. توجه داشته باشید که این آبجکت با منبع حجم downwardAPI یکسان است، با این تفاوت که حالت پیش‌فرض (default mode) ندارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#DownwardAPIVolumeFile" >}}">DownwardAPIVolumeFile array</a></em></td>
      <td>Items فهرستی از فایل‌های DownwardAPIVolume است</td>
    </tr>
  </tbody>
</table>


## DownwardAPIVolumeFile {#DownwardAPIVolumeFile}

DownwardAPIVolumeFile اطلاعات لازم برای ایجاد فایلی را نمایش می‌دهد که فیلد pod را در خود دارد

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fieldRef</code><br/><em><a href="{{< ref "#ObjectFieldSelector" >}}">ObjectFieldSelector</a></em></td>
      <td>الزامی: یک فیلد از pod را انتخاب می‌کند. فقط annotations، labels، name، namespace و uid پشتیبانی می‌شوند.</td>
    </tr>
    <tr>
      <td><code>mode</code><br/><em>integer</em></td>
      <td>اختیاری: بیت‌های mode که برای تنظیم مجوزهای این فایل استفاده می‌شوند. باید یک مقدار octal بین 0000 و 0777 یا یک مقدار decimal بین 0 و 511 باشد. YAML هر دو مقدار octal و decimal را می‌پذیرد، اما JSON برای بیت‌های mode مقدار decimal می‌خواهد. اگر مشخص نشود، از defaultMode حجم استفاده می‌شود. این مقدار ممکن است با گزینه‌های دیگری که بر mode فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های mode دیگری تنظیم شوند.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>الزامی: Path مسیر نسبی فایلی است که باید ایجاد شود. این مسیر نباید مطلق باشد و نباید شامل مسیر '..' باشد. باید با کدگذاری utf-8 باشد. اولین بخش مسیر نسبی نباید با '..' شروع شود.</td>
    </tr>
    <tr>
      <td><code>resourceFieldRef</code><br/><em><a href="{{< ref "#ResourceFieldSelector" >}}">ResourceFieldSelector</a></em></td>
      <td>یک منبع از کانتینر را انتخاب می‌کند. در حال حاضر فقط limits و requests منابع (limits.cpu، limits.memory، requests.cpu و requests.memory) پشتیبانی می‌شوند.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>integer</em></td>
      <td>user اختیاری است: UID مالک فایل ایجادشده. اگر مشخص شود، فیلد user در سطح آیتم بر defaultUser اولویت دارد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
  </tbody>
</table>


## DownwardAPIVolumeSource {#DownwardAPIVolumeSource}

DownwardAPIVolumeSource یک حجم (volume) حاوی اطلاعات downward API را نمایش می‌دهد. حجم‌های Downward API از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>defaultMode</code><br/><em>integer</em></td>
      <td>اختیاری: بیت‌های mode که به‌طور پیش‌فرض برای فایل‌های ایجادشده استفاده می‌شوند. بیت‌های mode که به‌طور پیش‌فرض برای تنظیم مجوزهای فایل‌های ایجادشده استفاده می‌شوند و باید یک مقدار octal بین 0000 و 0777 یا یک مقدار decimal بین 0 و 511 باشند. YAML هر دو مقدار octal و decimal را می‌پذیرد، اما JSON برای بیت‌های mode مقدار decimal می‌خواهد. مقدار پیش‌فرض 0644 است. دایرکتوری‌های درون مسیر تحت تأثیر این تنظیم قرار نمی‌گیرند. این مقدار ممکن است با گزینه‌های دیگری که بر mode فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های mode دیگری تنظیم شوند.</td>
    </tr>
    <tr>
      <td><code>defaultUser</code><br/><em>integer</em></td>
      <td>defaultUser اختیاری است: UID مالک پیش‌فرض فایل‌های ایجادشده. فیلد defaultUser فقط زمانی به‌عنوان مقدار جایگزین استفاده می‌شود که فیلد user در سطح آیتم تنظیم نشده باشد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#DownwardAPIVolumeFile" >}}">DownwardAPIVolumeFile array</a></em></td>
      <td>Items فهرستی از فایل‌های حجم downward API است</td>
    </tr>
  </tbody>
</table>


## EmptyDirVolumeSource {#EmptyDirVolumeSource}

یک دایرکتوری خالی برای یک pod را نمایش می‌دهد. حجم‌های دایرکتوری خالی از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>medium</code><br/><em>string</em></td>
      <td>medium مشخص می‌کند که این دایرکتوری باید روی چه نوع رسانه ذخیره‌سازی قرار گیرد. مقدار پیش‌فرض "" است که به معنای استفاده از رسانه پیش‌فرض نود است. باید یک رشته خالی (پیش‌فرض) یا Memory باشد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#emptydir</td>
    </tr>
    <tr>
      <td><code>mode</code><br/><em>integer</em></td>
      <td>mode بیت‌های مجوز دایرکتوری emptyDir را با نمایش عددی (برای مثال 0755 و 01777) مشخص می‌کند. باید مقداری بین 0000 و 01777 باشد. اگر مشخص نشود، مقدار پیش‌فرض 0777 است. این مقدار ممکن است با گزینه‌های دیگری که بر mode فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد. اگر fsGroup مشخص شده باشد، مجوزهای fsGroup بر mode مشخص‌شده در اینجا اولویت پیدا می‌کنند. این فیلد در ویندوز تأثیری ندارد. این فیلد آلفا است و نیازمند فعال بودن featuregate با نام EmptyDirVolumeMode است.</td>
    </tr>
    <tr>
      <td><code>sizeLimit</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>sizeLimit مقدار کل ذخیره‌سازی محلی مورد نیاز برای این حجم EmptyDir است. این محدودیت اندازه برای رسانه memory نیز اعمال می‌شود. بیشینه مصرف در EmptyDir با رسانه memory برابر با کمینه‌ی دو مقدار SizeLimit مشخص‌شده در اینجا و مجموع محدودیت‌های حافظه همه کانتینرهای یک pod است. مقدار پیش‌فرض nil است که به معنای تعریف‌نشده بودن محدودیت است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#emptydir</td>
    </tr>
  </tbody>
</table>


## EnvFromSource {#EnvFromSource}

EnvFromSource منبع مجموعه‌ای از ConfigMapها یا Secretها را نمایش می‌دهد

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>configMapRef</code><br/><em><a href="{{< ref "#ConfigMapEnvSource" >}}">ConfigMapEnvSource</a></em></td>
      <td>ConfigMap که باید از آن انتخاب شود</td>
    </tr>
    <tr>
      <td><code>prefix</code><br/><em>string</em></td>
      <td>متن اختیاری که به ابتدای نام هر متغیر محیطی اضافه می‌شود. می‌تواند از هر نویسه ASCII قابل چاپ به‌جز '=' تشکیل شده باشد.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretEnvSource" >}}">SecretEnvSource</a></em></td>
      <td>Secret که باید از آن انتخاب شود</td>
    </tr>
  </tbody>
</table>


## EnvVar {#EnvVar}

EnvVar یک متغیر محیطی موجود در یک Container را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام متغیر محیطی. می‌تواند از هر نویسه ASCII قابل چاپ به‌جز '=' تشکیل شده باشد.</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em>string</em></td>
      <td>ارجاع‌های متغیر به‌شکل $(VAR_NAME) با استفاده از متغیرهای محیطی تعریف‌شده قبلی در کانتینر و هر متغیر محیطی سرویس گسترش داده می‌شوند. اگر متغیری قابل تعیین نباشد، ارجاع در رشته ورودی بدون تغییر باقی می‌ماند. دو علامت $$ به یک $ کاهش می‌یابند که امکان escape کردن نحو $(VAR_NAME) را فراهم می‌کند؛ یعنی "$$(VAR_NAME)" رشته لفظی "$(VAR_NAME)" را تولید می‌کند. ارجاع‌های escapeشده هرگز گسترش داده نمی‌شوند، چه متغیر وجود داشته باشد و چه نداشته باشد. مقدار پیش‌فرض "" است.</td>
    </tr>
    <tr>
      <td><code>valueFrom</code><br/><em><a href="{{< ref "#EnvVarSource" >}}">EnvVarSource</a></em></td>
      <td>منبع مقدار متغیر محیطی. اگر value خالی نباشد، نمی‌توان از این فیلد استفاده کرد.</td>
    </tr>
  </tbody>
</table>


## EnvVarSource {#EnvVarSource}

EnvVarSource منبع مقدار یک EnvVar را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>configMapKeyRef</code><br/><em><a href="{{< ref "#ConfigMapKeySelector" >}}">ConfigMapKeySelector</a></em></td>
      <td>یک کلید از ConfigMap را انتخاب می‌کند.</td>
    </tr>
    <tr>
      <td><code>fieldRef</code><br/><em><a href="{{< ref "#ObjectFieldSelector" >}}">ObjectFieldSelector</a></em></td>
      <td>یک فیلد از pod را انتخاب می‌کند. از metadata.name، metadata.namespace، `metadata.labels['\<KEY>']`، `metadata.annotations['\<KEY>']`، spec.nodeName، spec.serviceAccountName، status.hostIP، status.podIP و status.podIPs پشتیبانی می‌شود.</td>
    </tr>
    <tr>
      <td><code>fileKeyRef</code><br/><em><a href="{{< ref "#FileKeySelector" >}}">FileKeySelector</a></em></td>
      <td>FileKeyRef یک کلید از فایل env را انتخاب می‌کند. نیازمند فعال بودن feature gate با نام EnvFiles است.</td>
    </tr>
    <tr>
      <td><code>resourceFieldRef</code><br/><em><a href="{{< ref "#ResourceFieldSelector" >}}">ResourceFieldSelector</a></em></td>
      <td>یک منبع از کانتینر را انتخاب می‌کند. در حال حاضر فقط limits و requests منابع (limits.cpu، limits.memory، limits.ephemeral-storage، requests.cpu، requests.memory و requests.ephemeral-storage) پشتیبانی می‌شوند.</td>
    </tr>
    <tr>
      <td><code>secretKeyRef</code><br/><em><a href="{{< ref "#SecretKeySelector" >}}">SecretKeySelector</a></em></td>
      <td>یک کلید از یک secret را در فضای نام (namespace) مربوط به pod انتخاب می‌کند</td>
    </tr>
  </tbody>
</table>

## EphemeralContainer {#EphemeralContainer}

EphemeralContainer کانتینری موقت است که می‌توانید برای فعالیت‌های آغازشده توسط کاربر، مانند اشکال‌زدایی، به یک Pod موجود اضافه کنید. کانتینرهای موقت هیچ تضمینی برای منابع یا زمان‌بندی ندارند و پس از خروج از اجرا، یا زمانی که Pod حذف یا راه‌اندازی مجدد می‌شود، دوباره راه‌اندازی نمی‌شوند. اگر یک کانتینر موقت باعث شود Pod از منابع تخصیص‌یافته‌اش فراتر رود، kubelet ممکن است آن Pod را اخراج (evict) کند.

برای افزودن یک کانتینر موقت، از زیرمنبع ephemeralcontainers یک Pod موجود استفاده کنید. کانتینرهای موقت را نمی‌توان حذف یا راه‌اندازی مجدد کرد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>args</code><br/><em>string array</em></td>
      <td>آرگومان‌های entrypoint. اگر این مقدار ارائه نشود، از CMD ایمیج استفاده می‌شود. ارجاع‌های متغیر به شکل $(VAR_NAME) با استفاده از محیط کانتینر گسترش داده می‌شوند. اگر متغیری قابل تفکیک و تعیین مقدار نباشد، ارجاع در رشته ورودی بدون تغییر باقی می‌ماند. دو علامت $$ به یک $ تبدیل می‌شوند و این امکان را فراهم می‌کنند که نحو $(VAR_NAME) از گسترش مستثنا شود؛ یعنی "$$(VAR_NAME)" رشته لفظی "$(VAR_NAME)" را تولید می‌کند. ارجاع‌های مستثناشده هرگز گسترش داده نمی‌شوند، چه متغیر وجود داشته باشد و چه نه. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</td>
    </tr>
    <tr>
      <td><code>command</code><br/><em>string array</em></td>
      <td>آرایه entrypoint. درون shell اجرا نمی‌شود. اگر این مقدار ارائه نشود، از ENTRYPOINT ایمیج استفاده می‌شود. ارجاع‌های متغیر به شکل $(VAR_NAME) با استفاده از محیط کانتینر گسترش داده می‌شوند. اگر متغیری قابل تفکیک و تعیین مقدار نباشد، ارجاع در رشته ورودی بدون تغییر باقی می‌ماند. دو علامت $$ به یک $ تبدیل می‌شوند و این امکان را فراهم می‌کنند که نحو $(VAR_NAME) از گسترش مستثنا شود؛ یعنی "$$(VAR_NAME)" رشته لفظی "$(VAR_NAME)" را تولید می‌کند. ارجاع‌های مستثناشده هرگز گسترش داده نمی‌شوند، چه متغیر وجود داشته باشد و چه نه. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell</td>
    </tr>
    <tr>
      <td><code>env</code><br/><em><a href="{{< ref "#EnvVar" >}}">EnvVar array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>فهرست متغیرهای محیطی که باید در کانتینر تنظیم شوند. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>envFrom</code><br/><em><a href="{{< ref "#EnvFromSource" >}}">EnvFromSource array</a></em></td>
      <td>فهرست منابعی که متغیرهای محیطی کانتینر از آن‌ها مقداردهی می‌شوند. کلیدهای تعریف‌شده در یک منبع می‌توانند از هر کاراکتر ASCII قابل چاپ، به‌جز '='، تشکیل شوند. هنگامی که یک کلید در چند منبع وجود داشته باشد، مقدار مربوط به آخرین منبع اولویت دارد. مقادیری که با Env و کلید تکراری تعریف شده باشند نیز اولویت دارند. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>image</code><br/><em>string</em></td>
      <td>نام ایمیج کانتینر. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images</td>
    </tr>
    <tr>
      <td><code>imagePullPolicy</code><br/><em>string</em></td>
      <td>سیاست دریافت ایمیج. یکی از Always، Never و IfNotPresent. اگر تگ :latest مشخص شده باشد، مقدار پیش‌فرض Always است و در غیر این صورت IfNotPresent خواهد بود. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images#updating-images<br/><br/>Possible enum values:<br/> - `"Always"` به این معناست که kubelet همواره تلاش می‌کند جدیدترین ایمیج را دریافت کند. اگر دریافت ایمیج ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"IfNotPresent"` به این معناست که kubelet تنها در صورتی ایمیج را دریافت می‌کند که روی دیسک موجود نباشد. اگر ایمیج موجود نباشد و دریافت آن ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"Never"` به این معناست که kubelet هرگز ایمیجی را دریافت نمی‌کند و فقط از ایمیج محلی استفاده می‌کند. اگر ایمیج موجود نباشد، کانتینر با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>lifecycle</code><br/><em><a href="{{< ref "#Lifecycle" >}}">Lifecycle</a></em></td>
      <td>استفاده از Lifecycle برای کانتینرهای موقت مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>livenessProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>استفاده از probe برای کانتینرهای موقت مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام کانتینر موقت که به‌صورت DNS_LABEL مشخص می‌شود. این نام باید میان همه کانتینرها، init containerها و کانتینرهای موقت یکتا باشد.</td>
    </tr>
    <tr>
      <td><code>ports</code><br/><em><a href="{{< ref "#ContainerPort" >}}">ContainerPort array</a></em><br/><em>patch strategy: merge on key <code>containerPort</code></em></td>
      <td>استفاده از پورت برای کانتینرهای موقت مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>readinessProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>استفاده از probe برای کانتینرهای موقت مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>resizePolicy</code><br/><em><a href="{{< ref "#ContainerResizePolicy" >}}">ContainerResizePolicy array</a></em></td>
      <td>سیاست تغییر اندازه منابع برای کانتینر.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em><a href="{{< ref "#ResourceRequirements" >}}">ResourceRequirements</a></em></td>
      <td>تعیین منابع برای کانتینرهای موقت مجاز نیست. کانتینرهای موقت از منابع مازادی استفاده می‌کنند که پیش‌تر به Pod تخصیص داده شده است.</td>
    </tr>
    <tr>
      <td><code>restartPolicy</code><br/><em>string</em></td>
      <td>سیاست راه‌اندازی مجدد کانتینر برای مدیریت رفتار راه‌اندازی مجدد هر کانتینر درون یک Pod. نمی‌توانید این فیلد را برای کانتینرهای موقت تنظیم کنید.</td>
    </tr>
    <tr>
      <td><code>restartPolicyRules</code><br/><em><a href="{{< ref "#ContainerRestartRule" >}}">ContainerRestartRule array</a></em></td>
      <td>فهرستی از قواعد را نشان می‌دهد که برای تعیین اینکه آیا کانتینر پس از خروج باید دوباره راه‌اندازی شود، بررسی می‌شوند. نمی‌توانید این فیلد را برای کانتینرهای موقت تنظیم کنید.</td>
    </tr>
    <tr>
      <td><code>securityContext</code><br/><em><a href="{{< ref "#SecurityContext" >}}">SecurityContext</a></em></td>
      <td>اختیاری: SecurityContext گزینه‌های امنیتی‌ای را تعریف می‌کند که کانتینر موقت باید با آن‌ها اجرا شود. در صورت تنظیم، فیلدهای SecurityContext بر فیلدهای معادل در PodSecurityContext اولویت دارند.</td>
    </tr>
    <tr>
      <td><code>startupProbe</code><br/><em><a href="{{< ref "#Probe" >}}">Probe</a></em></td>
      <td>استفاده از probe برای کانتینرهای موقت مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>stdin</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا این کانتینر باید در محیط اجرای کانتینر یک بافر برای stdin تخصیص دهد یا نه. اگر این مقدار تنظیم نشود، خواندن از stdin در کانتینر همواره به EOF منجر می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdinOnce</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا محیط اجرای کانتینر باید کانال stdin را پس از باز شدن توسط یک attach واحد ببندد یا نه. هنگامی که stdin برابر true باشد، جریان stdin در چندین نشست attach باز می‌ماند. اگر stdinOnce روی true تنظیم شود، stdin هنگام شروع کانتینر باز می‌شود، تا زمانی که نخستین کلاینت به stdin متصل شود خالی است، سپس باز می‌ماند و داده می‌پذیرد تا زمانی که کلاینت قطع شود؛ در آن زمان stdin بسته می‌شود و تا راه‌اندازی مجدد کانتینر بسته می‌ماند. اگر این پرچم false باشد، فرایند کانتینری که از stdin می‌خواند هرگز EOF دریافت نخواهد کرد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>targetContainerName</code><br/><em>string</em></td>
      <td>در صورت تنظیم، نام کانتینری از PodSpec است که این کانتینر موقت آن را هدف قرار می‌دهد. کانتینر موقت در namespaceهای (مانند IPC و PID) این کانتینر اجرا می‌شود. اگر تنظیم نشود، کانتینر موقت از namespaceهای پیکربندی‌شده در spec مربوط به Pod استفاده می‌کند. محیط اجرای کانتینر باید از این قابلیت پشتیبانی کند. اگر محیط اجرا از هدف‌گیری namespace پشتیبانی نکند، نتیجه تنظیم این فیلد تعریف‌نشده است.</td>
    </tr>
    <tr>
      <td><code>terminationMessagePath</code><br/><em>string</em></td>
      <td>اختیاری: مسیری در فایل‌سیستم کانتینر که فایل حاوی پیام خاتمه کانتینر در آن mount شده و پیام در آن نوشته می‌شود. پیام نوشته‌شده باید وضعیت نهایی کوتاهی باشد، مانند پیام شکست یک assertion. اگر حجم پیام از ۴۰۹۶ بایت بیشتر باشد، نود آن را کوتاه می‌کند. طول کل پیام در همه کانتینرها به ۱۲ کیلوبایت محدود است. مقدار پیش‌فرض /dev/termination-log است. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>terminationMessagePolicy</code><br/><em>string</em></td>
      <td>مشخص می‌کند پیام خاتمه چگونه تولید شود. File از محتوای terminationMessagePath برای تکمیل پیام وضعیت کانتینر، چه در موفقیت و چه در شکست، استفاده می‌کند. FallbackToLogsOnError در صورتی که فایل پیام خاتمه خالی باشد و کانتینر با خطا خارج شده باشد، از آخرین بخش خروجی لاگ کانتینر استفاده می‌کند. خروجی لاگ به ۲۰۴۸ بایت یا ۸۰ خط، هرکدام کمتر باشد، محدود است. مقدار پیش‌فرض File است. قابل به‌روزرسانی نیست.<br/><br/>Possible enum values:<br/> - `"FallbackToLogsOnError"` هنگامی که کانتینر با خطا خارج شود و terminationMessagePath محتوایی نداشته باشد، جدیدترین محتوای لاگ‌های کانتینر را برای پیام وضعیت کانتینر می‌خواند.<br/> - `"File"` رفتار پیش‌فرض است و هنگام خروج کانتینر، پیام وضعیت کانتینر را برابر با محتوای terminationMessagePath قرار می‌دهد.</td>
    </tr>
    <tr>
      <td><code>tty</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا این کانتینر باید برای خود یک TTY تخصیص دهد یا نه؛ این کار مستلزم آن است که 'stdin' نیز برابر true باشد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>volumeDevices</code><br/><em><a href="{{< ref "#VolumeDevice" >}}">VolumeDevice array</a></em><br/><em>patch strategy: merge on key <code>devicePath</code></em></td>
      <td>volumeDevices فهرست دستگاه‌های بلوکی است که کانتینر از آن‌ها استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>volumeMounts</code><br/><em><a href="{{< ref "#VolumeMount" >}}">VolumeMount array</a></em><br/><em>patch strategy: merge on key <code>mountPath</code></em></td>
      <td>حجم‌های (volume) Pod که باید در فایل‌سیستم کانتینر mount شوند. mount کردن زیرمسیر (subpath) برای کانتینرهای موقت مجاز نیست. قابل به‌روزرسانی نیست.</td>
    </tr>
    <tr>
      <td><code>workingDir</code><br/><em>string</em></td>
      <td>دایرکتوری کاری کانتینر. اگر مشخص نشود، از مقدار پیش‌فرض محیط اجرای کانتینر استفاده می‌شود که ممکن است در ایمیج کانتینر پیکربندی شده باشد. قابل به‌روزرسانی نیست.</td>
    </tr>
  </tbody>
</table>


## EphemeralVolumeSource {#EphemeralVolumeSource}

یک حجم (volume) موقت را نشان می‌دهد که توسط یک درایور ذخیره‌سازی معمولی مدیریت می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>volumeClaimTemplate</code><br/><em><a href="{{< ref "#PersistentVolumeClaimTemplate" >}}">PersistentVolumeClaimTemplate</a></em></td>
      <td>برای ایجاد یک PVC مستقل و تأمین حجم از آن استفاده می‌شود. Pod‌ای که این EphemeralVolumeSource در آن قرار گرفته، مالک PVC خواهد بود؛ یعنی PVC همراه با Pod حذف می‌شود. نام PVC به صورت `\<pod name>-\<volume name>` خواهد بود که در آن `\<volume name>` نامی است که از عنصر آرایه `PodSpec.Volumes` گرفته می‌شود. اگر نام ترکیب‌شده برای یک PVC معتبر نباشد (برای مثال، بیش از حد طولانی باشد)، اعتبارسنجی Pod آن را رد می‌کند. یک PVC موجود با همین نام که مالک آن Pod نباشد، برای Pod *استفاده نخواهد شد* تا از استفاده اشتباهی از یک حجم نامرتبط جلوگیری شود. در این حالت، شروع Pod تا زمان حذف PVC نامرتبط مسدود می‌شود. اگر قرار باشد Pod از چنین PVC از پیش ایجادشده‌ای استفاده کند، باید پس از ایجاد Pod، PVC با یک owner reference به Pod به‌روزرسانی شود. معمولاً این کار لازم نیست، اما ممکن است هنگام بازسازی دستی یک کلاستر خراب مفید باشد. این فیلد فقط‌خواندنی است و کوبرنتیز پس از ایجاد PVC هیچ تغییری در آن اعمال نمی‌کند. الزامی است و نباید nil باشد.</td>
    </tr>
  </tbody>
</table>


## EvictionResponder {#EvictionResponder}

EvictionResponder به شما امکان می‌دهد پاسخ‌دهنده‌ای را مشخص کنید که به یک Eviction واکنش نشان می‌دهد. پاسخ‌دهنده‌ها باید از طریق Eviction Resource API رویدادها را مشاهده کنند و با آن ارتباط برقرار کنند تا به اخراج تدریجی (graceful) یک هدف کمک کنند (برای مثال، خاتمه یک Pod).

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name به شما امکان می‌دهد پاسخ‌دهنده‌ای را که به Eviction پاسخ می‌دهد شناسایی کنید. این مقدار باید یک کلید معتبر با پیشوند دامنه باشد (مانند "acme.io/foo"). نام‌های دامنه *.k8s.io و *.kubernetes.io رزرو شده‌اند. این فیلد باید برای هر پاسخ‌دهنده یکتا باشد. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>priority</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>اولویت این پاسخ‌دهنده. اولویت‌های بالاتر ابتدا توسط evictionrequest-controller انتخاب می‌شوند. اگر چند پاسخ‌دهنده اولویت یکسان داشته باشند، پاسخ‌دهنده‌ای انتخاب می‌شود که نام دامنه آن در ترتیب الفبایی دامنه‌های بالاتر زودتر می‌آید. این بدان معناست که ابتدا برچسب‌های دامنه سطح بالا به‌صورت الفبایی مقایسه می‌شوند و پس از آن برچسب‌های دامنه سطح پایین‌تر. کلید در آخر مقایسه می‌شود. پاسخ‌دهنده‌ای که کنترل‌کننده مدیر Pod است، باید مقدار این فیلد را روی 10000 تنظیم کند تا هم پیش‌دستی (preemption) و هم ثبت جایگزین (fallback) توسط پاسخ‌دهنده‌های دیگر امکان‌پذیر باشد. کمترین مقدار 0 و بیشترین مقدار 100000 است. بازه 0 تا 999 برای پاسخ‌دهنده‌های دارای پسوند *.k8s.io رزرو شده است. این فیلد الزامی است.</td>
    </tr>
  </tbody>
</table>


## ExecAction {#ExecAction}

ExecAction یک اقدام «اجرا در کانتینر» را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>command</code><br/><em>string array</em></td>
      <td>Command همان خط فرمانی است که باید درون کانتینر اجرا شود؛ دایرکتوری کاری این دستور، ریشه ('/') در فایل‌سیستم کانتینر است. دستور مستقیماً exec می‌شود و درون shell اجرا نمی‌گردد، بنابراین دستورهای متداول shell (مانند '|') کار نمی‌کنند. برای استفاده از shell باید آن را صراحتاً فراخوانی کنید. کد خروج 0 به معنای زنده/سالم و هر کد غیر صفر به معنای ناسالم است.</td>
    </tr>
  </tbody>
</table>


## FileKeySelector {#FileKeySelector}

FileKeySelector یک کلید از فایل env را انتخاب می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>کلید درون فایل env. کلید نامعتبر مانع از شروع Pod می‌شود. کلیدهای تعریف‌شده در یک منبع می‌توانند از هر کاراکتر ASCII قابل چاپ، به‌جز '='، تشکیل شوند. در مرحله آلفای feature gate با نام EnvFiles، اندازه کلید به ۱۲۸ کاراکتر محدود است.</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا فایل یا کلید آن باید تعریف شده باشد یا نه. اگر فایل یا کلید وجود نداشته باشد، متغیر محیطی منتشر نمی‌شود. اگر optional روی true تنظیم شده باشد و کلید مشخص‌شده وجود نداشته باشد، متغیر محیطی در کانتینرهای Pod تنظیم نخواهد شد. اگر optional روی false تنظیم شده باشد و کلید مشخص‌شده وجود نداشته باشد، هنگام ایجاد Pod خطا بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مسیر درون حجم (volume) که فایل از آن انتخاب می‌شود. مسیر باید نسبی باشد و نباید شامل '..' باشد یا با '..' شروع شود.</td>
    </tr>
    <tr>
      <td><code>volumeName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام volume mount که حاوی فایل env است.</td>
    </tr>
  </tbody>
</table>

## FlexVolumeSource {#FlexVolumeSource}

FlexVolume یک منبع حجم عمومی (generic) را نشان می‌دهد که با استفاده از یک افزونه مبتنی بر exec فراهم‌سازی یا متصل می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>driver نام درایوری است که برای این حجم استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سامانه فایل برای mount است. این نوع باید سامانه فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند؛ برای مثال "ext4"، "xfs" و "ntfs". سامانه فایل پیش‌فرض به اسکریپت FlexVolume بستگی دارد.</td>
    </tr>
    <tr>
      <td><code>options</code><br/><em>object</em></td>
      <td>options اختیاری است: این فیلد در صورت وجود، گزینه‌های دستوری اضافی را نگه می‌دارد.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض آن false (خواندن/نوشتن) است. مقدار ReadOnly در این‌جا تنظیم ReadOnly در VolumeMounts را اجباری می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef اختیاری است: secretRef ارجاعی به آبجکت Secret است که اطلاعات حساس را برای ارسال به اسکریپت‌های افزونه در خود دارد. اگر هیچ آبجکت Secret ای مشخص نشده باشد، این فیلد می‌تواند خالی باشد. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها به اسکریپت‌های افزونه ارسال می‌شوند.</td>
    </tr>
  </tbody>
</table>


## GRPCAction {#GRPCAction}

GRPCAction یک عمل مربوط به سرویس GRPC را مشخص می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>mode</code><br/><em>string</em></td>
      <td>mode حالت اتصال را برای probe سلامت gRPC مشخص می‌کند. برای استفاده از TLS بدون تأیید گواهی، مقدار "TLS" را تنظیم کنید. برای استفاده صریح از اتصال plaintext (ناامن)، مقدار "Plaintext" را تنظیم کنید. اگر مشخص نشود، probe از اتصال plaintext (ناامن) استفاده می‌کند.<br/><br/>مقادیر ممکن enum:<br/> - `"Plaintext"` نشان می‌دهد که probe باید از اتصال gRPC به‌صورت plaintext (ناامن) استفاده کند.<br/> - `"TLS"` نشان می‌دهد که probe باید با TLS و بدون تأیید گواهی متصل شود.</td>
    </tr>
    <tr>
      <td><code>port</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>شماره پورت سرویس gRPC. این عدد باید در بازه 1 تا 65535 باشد.</td>
    </tr>
    <tr>
      <td><code>service</code><br/><em>string</em></td>
      <td>Service نام سرویسی است که در HealthCheckRequest مربوط به gRPC قرار می‌گیرد (به https://github.com/grpc/grpc/blob/master/doc/health-checking.md مراجعه کنید). اگر این فیلد مشخص نشود، رفتار پیش‌فرض را خود gRPC تعیین می‌کند.</td>
    </tr>
  </tbody>
</table>


## GitRepoVolumeSource {#GitRepoVolumeSource}

حجمی را نشان می‌دهد که با محتوای یک مخزن git پر می‌شود. حجم‌های مخزن Git از مدیریت مالکیت پشتیبانی نمی‌کنند. این حجم‌ها از برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

منسوخ‌شده: GitRepo منسوخ شده است. برای فراهم کردن یک مخزن git در کانتینر، یک EmptyDir را در یک InitContainer که مخزن را با git کلون می‌کند mount کنید و سپس همان EmptyDir را در کانتینر Pod mount کنید.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>directory</code><br/><em>string</em></td>
      <td>directory نام دایرکتوری مقصد است. این نام نباید شامل '..' باشد یا با '..' شروع شود. اگر '.' داده شود، دایرکتوری حجم همان مخزن git خواهد بود. در غیر این صورت، اگر مقداری مشخص شده باشد، حجم مخزن git را در زیردایرکتوری‌ای با همان نام در خود خواهد داشت.</td>
    </tr>
    <tr>
      <td><code>repository</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>repository نشانی URL مخزن است</td>
    </tr>
    <tr>
      <td><code>revision</code><br/><em>string</em></td>
      <td>revision هش commit مربوط به revision مشخص‌شده است.</td>
    </tr>
  </tbody>
</table>


## GlusterfsVolumeSource {#GlusterfsVolumeSource}

یک mount از Glusterfs را نشان می‌دهد که به اندازه عمر یک pod باقی می‌ماند. حجم‌های Glusterfs از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>endpoints</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>endpoints نام endpoint ای است که توپولوژی Glusterfs را توصیف می‌کند.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر حجم Glusterfs است. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در این‌جا باعث می‌شود حجم Glusterfs با مجوزهای فقط‌خواندنی mount شود. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
  </tbody>
</table>


## HTTPGetAction {#HTTPGetAction}

HTTPGetAction یک عمل مبتنی بر درخواست‌های HTTP Get را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>host</code><br/><em>string</em></td>
      <td>نام میزبانی که اتصال به آن برقرار می‌شود؛ مقدار پیش‌فرض آن IP پاد است. به احتمال زیاد باید به‌جای آن، "Host" را در httpHeaders تنظیم کنید.</td>
    </tr>
    <tr>
      <td><code>httpHeaders</code><br/><em><a href="{{< ref "#HTTPHeader" >}}">HTTPHeader array</a></em></td>
      <td>سربرگ‌های سفارشی که باید در درخواست تنظیم شوند. HTTP اجازه تکرار سربرگ‌ها را می‌دهد.</td>
    </tr>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>مسیری که روی سرور HTTP به آن دسترسی پیدا می‌شود.</td>
    </tr>
    <tr>
      <td><code>port</code>&nbsp;<strong>*</strong><br/><em></em></td>
      <td>نام یا شماره پورتی که روی کانتینر به آن دسترسی پیدا می‌شود. شماره باید در بازه 1 تا 65535 باشد. نام باید یک IANA_SVC_NAME باشد.</td>
    </tr>
    <tr>
      <td><code>protocol</code><br/><em>string</em></td>
      <td>Protocol پروتکل شبکه‌ای را برای اتصال probe انتخاب می‌کند. مقدار nil به‌طور پیش‌فرض HTTP/1.1 است.<br/><br/>مقادیر ممکن enum:<br/> - `"HTTP1"` از HTTP/1.1 استفاده می‌کند (پیش‌فرض فعلی).<br/> - `"HTTP2"` از HTTP/2 استفاده می‌کند. در حال حاضر فقط cleartext با آگاهی قبلی (h2c) پشتیبانی می‌شود و باید همراه با scheme برابر HTTP به کار رود.</td>
    </tr>
    <tr>
      <td><code>scheme</code><br/><em>string</em></td>
      <td>Scheme که برای اتصال به میزبان استفاده می‌شود. مقدار پیش‌فرض HTTP است.<br/><br/>مقادیر ممکن enum:<br/> - `"HTTP"` یعنی scheme مورد استفاده http:// خواهد بود<br/> - `"HTTPS"` یعنی scheme مورد استفاده https:// خواهد بود</td>
    </tr>
  </tbody>
</table>


## HTTPHeader {#HTTPHeader}

HTTPHeader یک سربرگ سفارشی را توصیف می‌کند که در probeهای HTTP استفاده می‌شود

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام فیلد سربرگ. این نام هنگام خروجی به شکل متعارف (canonical) درمی‌آید؛ بنابراین نام‌هایی که فقط در بزرگی و کوچکی حروف تفاوت دارند، سربرگ یکسان در نظر گرفته می‌شوند.</td>
    </tr>
    <tr>
      <td><code>value</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مقدار فیلد سربرگ</td>
    </tr>
  </tbody>
</table>


## HostAlias {#HostAlias}

HostAlias نگاشت میان IP و نام‌های میزبان را نگه می‌دارد که به‌صورت یک ورودی در فایل hosts پاد درج می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>hostnames</code><br/><em>string array</em></td>
      <td>نام‌های میزبان برای نشانی IP بالا.</td>
    </tr>
    <tr>
      <td><code>ip</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نشانی IP ورودی فایل hosts.</td>
    </tr>
  </tbody>
</table>


## HostIP {#HostIP}

HostIP یک نشانی IP منفرد را نشان می‌دهد که به میزبان اختصاص یافته است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>ip</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>IP نشانی IP اختصاص‌یافته به میزبان است</td>
    </tr>
  </tbody>
</table>


## ISCSIVolumeSource {#ISCSIVolumeSource}

یک دیسک ISCSI را نشان می‌دهد. حجم‌های ISCSI را فقط یک بار می‌توان به‌صورت خواندن/نوشتن mount کرد. حجم‌های ISCSI از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>chapAuthDiscovery</code><br/><em>boolean</em></td>
      <td>chapAuthDiscovery مشخص می‌کند که آیا احراز هویت CHAP برای Discovery در iSCSI پشتیبانی شود یا خیر</td>
    </tr>
    <tr>
      <td><code>chapAuthSession</code><br/><em>boolean</em></td>
      <td>chapAuthSession مشخص می‌کند که آیا احراز هویت CHAP برای Session در iSCSI پشتیبانی شود یا خیر</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سامانه فایل حجمی است که می‌خواهید mount کنید. نکته: مطمئن شوید که سیستم‌عامل میزبان از این نوع سامانه فایل پشتیبانی می‌کند. مثال‌ها: "ext4"، "xfs" و "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#iscsi</td>
    </tr>
    <tr>
      <td><code>initiatorName</code><br/><em>string</em></td>
      <td>initiatorName نام سفارشی iSCSI Initiator است. اگر initiatorName همزمان با iscsiInterface مشخص شود، یک رابط iSCSI جدید به شکل \<target portal>:\<volume name> برای اتصال ایجاد خواهد شد.</td>
    </tr>
    <tr>
      <td><code>iqn</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>iqn نام واجد شرایط (Qualified Name) در iSCSI برای target است.</td>
    </tr>
    <tr>
      <td><code>iscsiInterface</code><br/><em>string</em></td>
      <td>iscsiInterface نام رابطی است که از انتقال iSCSI استفاده می‌کند. مقدار پیش‌فرض 'default' (tcp) است.</td>
    </tr>
    <tr>
      <td><code>lun</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>lun شماره Lun مربوط به iSCSI Target را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>portals</code><br/><em>string array</em></td>
      <td>portals فهرست Portalهای iSCSI Target است. هر portal یا یک IP است یا، اگر پورت متفاوت از پورت پیش‌فرض باشد (معمولاً پورت‌های TCP شماره 860 و 3260)، به شکل ip_addr:port است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در این‌جا تنظیم ReadOnly در VolumeMounts را اجباری می‌کند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef همان Secret مربوط به CHAP برای احراز هویت target و initiator در iSCSI است</td>
    </tr>
    <tr>
      <td><code>targetPortal</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>targetPortal همان iSCSI Target Portal است. این Portal یا یک IP است یا، اگر پورت متفاوت از پورت پیش‌فرض باشد (معمولاً پورت‌های TCP شماره 860 و 3260)، به شکل ip_addr:port است.</td>
    </tr>
  </tbody>
</table>


## ImageVolumeSource {#ImageVolumeSource}

ImageVolumeSource یک منبع حجم از نوع ایمیج را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pullPolicy</code><br/><em>string</em></td>
      <td>سیاست دریافت (pull) آبجکت‌های OCI. مقادیر ممکن عبارت‌اند از: Always: kubelet همیشه تلاش می‌کند مرجع را دریافت کند. اگر دریافت ناموفق باشد، ایجاد کانتینر با شکست مواجه می‌شود. Never: kubelet هرگز مرجع را دریافت نمی‌کند و فقط از ایمیج یا artifact محلی استفاده می‌کند. اگر مرجع موجود نباشد، ایجاد کانتینر با شکست مواجه می‌شود. IfNotPresent: kubelet فقط در صورتی دریافت می‌کند که مرجع از قبل روی دیسک موجود نباشد. اگر مرجع موجود نباشد و دریافت ناموفق باشد، ایجاد کانتینر با شکست مواجه می‌شود. اگر تگ :latest مشخص شده باشد، مقدار پیش‌فرض Always است و در غیر این صورت IfNotPresent است.<br/><br/>مقادیر ممکن enum:<br/> - `"Always"` یعنی kubelet همیشه تلاش می‌کند آخرین ایمیج را دریافت کند. اگر دریافت ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"IfNotPresent"` یعنی kubelet فقط در صورتی دریافت می‌کند که ایمیج روی دیسک موجود نباشد. اگر ایمیج موجود نباشد و دریافت ناموفق باشد، کانتینر با شکست مواجه می‌شود.<br/> - `"Never"` یعنی kubelet هرگز ایمیج را دریافت نمی‌کند و فقط از ایمیج محلی استفاده می‌کند. اگر ایمیج موجود نباشد، کانتینر با شکست مواجه می‌شود</td>
    </tr>
    <tr>
      <td><code>reference</code><br/><em>string</em></td>
      <td>الزامی: مرجع ایمیج یا artifact که باید استفاده شود. رفتار آن مانند pod.spec.containers[*].image است. Secretهای دریافت (pull) به همان روشی که برای ایمیج کانتینر گردآوری می‌شوند، با جست‌وجوی اعتبارنامه‌های نود، Secretهای دریافت ایمیج مربوط به SA و Secretهای دریافت ایمیج در مشخصات پاد جمع‌آوری می‌شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/images این فیلد اختیاری است تا مدیریت پیکربندی در سطح بالاتر بتواند ایمیج‌های کانتینر را در کنترل‌کننده‌های بار کاری مانند Deployments و StatefulSets به‌صورت پیش‌فرض تعیین یا بازنویسی کند.</td>
    </tr>
  </tbody>
</table>


## ImageVolumeStatus {#ImageVolumeStatus}

ImageVolumeStatus وضعیت حجم مبتنی بر ایمیج را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>imageRef</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ImageRef همان digest ایمیجی است که برای این حجم استفاده شده است. مقدار آن باید مشابه status.containerStatuses[i].imageID در پاد باشد. طول ImageRef نباید از 256 نویسه بیشتر شود.</td>
    </tr>
  </tbody>
</table>


## KeyToPath {#KeyToPath}

یک کلید رشته‌ای را به یک مسیر درون حجم نگاشت می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>key کلیدی است که باید project شود.</td>
    </tr>
    <tr>
      <td><code>mode</code><br/><em>integer</em></td>
      <td>mode اختیاری است: بیت‌های mode که برای تنظیم مجوزهای این فایل استفاده می‌شوند. این مقدار باید یک عدد هشت‌هشتی (octal) بین 0000 و 0777 یا یک عدد دهدهی بین 0 و 511 باشد. YAML هر دو مقدار octal و دهدهی را می‌پذیرد، اما JSON برای بیت‌های mode مقدار دهدهی لازم دارد. اگر مشخص نشود، از defaultMode حجم استفاده می‌شود. ممکن است این مقدار با گزینه‌های دیگری که بر mode فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های mode دیگری تنظیم شوند.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر نسبی فایلی است که کلید به آن نگاشت می‌شود. نباید مسیر مطلق باشد. نباید شامل عنصر مسیر '..' باشد. نباید با رشته '..' شروع شود.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>integer</em></td>
      <td>user اختیاری است: UID مالک فایل ایجاد‌شده. اگر مشخص شود، فیلد user در سطح آیتم بر defaultUser اولویت دارد. (آلفا) این فیلد نیاز دارد که feature gate با نام AtomicWriteVolumeUserFields فعال باشد.</td>
    </tr>
  </tbody>
</table>

## Lifecycle {#Lifecycle}

Lifecycle مشخص می‌کند که سیستم مدیریت در پاسخ به رویدادهای چرخه‌حیات کانتینر چه اقداماتی باید انجام دهد. در handlerهای چرخه‌حیات PostStart و PreStop، مدیریت کانتینر تا زمان اتمام اقدام مسدود می‌شود، مگر آنکه فرایند کانتینر با شکست مواجه شود؛ در این صورت handler متوقف می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>postStart</code><br/><em><a href="{{< ref "#LifecycleHandler" >}}">LifecycleHandler</a></em></td>
      <td>PostStart بلافاصله پس از ایجاد کانتینر فراخوانی می‌شود. اگر handler با شکست مواجه شود، کانتینر متوقف می‌شود و بر اساس سیاست راه‌اندازی مجدد (restart policy) خود دوباره راه‌اندازی می‌شود. سایر اقدامات مدیریتی مربوط به کانتینر تا پایان اجرای hook مسدود می‌مانند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks</td>
    </tr>
    <tr>
      <td><code>preStop</code><br/><em><a href="{{< ref "#LifecycleHandler" >}}">LifecycleHandler</a></em></td>
      <td>PreStop بلافاصله پیش از خاتمه یافتن کانتینر فراخوانی می‌شود؛ خاتمه می‌تواند به دلیل یک درخواست API یا رویداد مدیریتی مانند شکست probe های liveness/startup، preemption، رقابت بر سر منابع و موارد مشابه باشد. اگر کانتینر از کار بیفتد (crash) یا خارج شود، این handler فراخوانی نمی‌شود. شمارش معکوس مهلت خاتمه (termination grace period) مربوط به Pod پیش از اجرای hook مربوط به PreStop آغاز می‌شود. صرف‌نظر از نتیجه handler، کانتینر در نهایت در مهلت خاتمه Pod متوقف خواهد شد (مگر آنکه finalizerها آن را به تأخیر بیندازند). سایر اقدامات مدیریتی مربوط به کانتینر تا پایان اجرای hook یا رسیدن به پایان مهلت خاتمه مسدود می‌مانند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks</td>
    </tr>
    <tr>
      <td><code>stopSignal</code><br/><em>string</em></td>
      <td>StopSignal مشخص می‌کند هنگام توقف کانتینر کدام سیگنال به آن ارسال شود. اگر مقداری تعیین نشود، پیش‌فرض را محیط اجرای کانتینر مورد استفاده تعیین می‌کند. StopSignal را فقط برای Podهایی می‌توان تنظیم کرد که مقدار .spec.os.name در آن‌ها خالی نباشد.<br/><br/>Possible enum values:<br/> - `"SIGABRT"`<br/> - `"SIGALRM"`<br/> - `"SIGBUS"`<br/> - `"SIGCHLD"`<br/> - `"SIGCLD"`<br/> - `"SIGCONT"`<br/> - `"SIGFPE"`<br/> - `"SIGHUP"`<br/> - `"SIGILL"`<br/> - `"SIGINT"`<br/> - `"SIGIO"`<br/> - `"SIGIOT"`<br/> - `"SIGKILL"`<br/> - `"SIGPIPE"`<br/> - `"SIGPOLL"`<br/> - `"SIGPROF"`<br/> - `"SIGPWR"`<br/> - `"SIGQUIT"`<br/> - `"SIGRTMAX"`<br/> - `"SIGRTMAX-1"`<br/> - `"SIGRTMAX-10"`<br/> - `"SIGRTMAX-11"`<br/> - `"SIGRTMAX-12"`<br/> - `"SIGRTMAX-13"`<br/> - `"SIGRTMAX-14"`<br/> - `"SIGRTMAX-2"`<br/> - `"SIGRTMAX-3"`<br/> - `"SIGRTMAX-4"`<br/> - `"SIGRTMAX-5"`<br/> - `"SIGRTMAX-6"`<br/> - `"SIGRTMAX-7"`<br/> - `"SIGRTMAX-8"`<br/> - `"SIGRTMAX-9"`<br/> - `"SIGRTMIN"`<br/> - `"SIGRTMIN+1"`<br/> - `"SIGRTMIN+10"`<br/> - `"SIGRTMIN+11"`<br/> - `"SIGRTMIN+12"`<br/> - `"SIGRTMIN+13"`<br/> - `"SIGRTMIN+14"`<br/> - `"SIGRTMIN+15"`<br/> - `"SIGRTMIN+2"`<br/> - `"SIGRTMIN+3"`<br/> - `"SIGRTMIN+4"`<br/> - `"SIGRTMIN+5"`<br/> - `"SIGRTMIN+6"`<br/> - `"SIGRTMIN+7"`<br/> - `"SIGRTMIN+8"`<br/> - `"SIGRTMIN+9"`<br/> - `"SIGSEGV"`<br/> - `"SIGSTKFLT"`<br/> - `"SIGSTOP"`<br/> - `"SIGSYS"`<br/> - `"SIGTERM"`<br/> - `"SIGTRAP"`<br/> - `"SIGTSTP"`<br/> - `"SIGTTIN"`<br/> - `"SIGTTOU"`<br/> - `"SIGURG"`<br/> - `"SIGUSR1"`<br/> - `"SIGUSR2"`<br/> - `"SIGVTALRM"`<br/> - `"SIGWINCH"`<br/> - `"SIGXCPU"`<br/> - `"SIGXFSZ"`</td>
    </tr>
  </tbody>
</table>


## LifecycleHandler {#LifecycleHandler}

LifecycleHandler یک اقدام مشخص را تعریف می‌کند که باید در یک lifecycle hook انجام شود. باید یکی و تنها یکی از فیلدها تعیین شود؛ فیلد TCPSocket از این قاعده مستثنا است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>exec</code><br/><em><a href="{{< ref "#ExecAction" >}}">ExecAction</a></em></td>
      <td>Exec دستوری را مشخص می‌کند که باید در کانتینر اجرا شود.</td>
    </tr>
    <tr>
      <td><code>httpGet</code><br/><em><a href="{{< ref "#HTTPGetAction" >}}">HTTPGetAction</a></em></td>
      <td>HTTPGet یک درخواست HTTP GET را مشخص می‌کند که باید انجام شود.</td>
    </tr>
    <tr>
      <td><code>sleep</code><br/><em><a href="{{< ref "#SleepAction" >}}">SleepAction</a></em></td>
      <td>Sleep مدت زمانی را نشان می‌دهد که کانتینر باید در حالت انتظار (sleep) بماند.</td>
    </tr>
    <tr>
      <td><code>tcpSocket</code><br/><em><a href="{{< ref "#TCPSocketAction" >}}">TCPSocketAction</a></em></td>
      <td>منسوخ‌شده. TCPSocket به‌عنوان LifecycleHandler پشتیبانی نمی‌شود و تنها برای سازگاری با نسخه‌های قبلی نگه داشته شده است. این فیلد اعتبارسنجی نمی‌شود و در صورت تعیین آن، lifecycle hookها در زمان اجرا با شکست مواجه می‌شوند.</td>
    </tr>
  </tbody>
</table>


## LinuxContainerUser {#LinuxContainerUser}

LinuxContainerUser اطلاعات هویت کاربر را در کانتینرهای لینوکسی نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>gid</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>GID شناسه گروه اصلی (primary gid) است که در ابتدا به نخستین فرایند کانتینر اختصاص داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>supplementalGroups</code><br/><em>integer array</em></td>
      <td>SupplementalGroups گروه‌های تکمیلی هستند که در ابتدا به نخستین فرایند کانتینر اختصاص داده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>uid</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>UID شناسه کاربر اصلی (primary uid) است که در ابتدا به نخستین فرایند کانتینر اختصاص داده می‌شود.</td>
    </tr>
  </tbody>
</table>


## NodeAffinity {#NodeAffinity}

Node affinity مجموعه‌ای از قوانین زمان‌بندی مبتنی بر تمایل به نود (node affinity) است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>preferredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "#PreferredSchedulingTerm" >}}">PreferredSchedulingTerm array</a></em></td>
      <td>زمان‌بند ترجیح می‌دهد Podها را روی نودهایی زمان‌بندی کند که عبارات affinity مشخص‌شده در این فیلد را برآورده می‌کنند، اما ممکن است نودی را انتخاب کند که یک یا چند عبارت را نقض می‌کند. نودی که بیشتر از همه ترجیح داده می‌شود، نودی است که بیشترین مجموع وزن‌ها را دارد. به این صورت که برای هر نودی که همه الزامات زمان‌بندی (درخواست منابع، عبارات affinity از نوع requiredDuringScheduling و غیره) را برآورده می‌کند، با پیمایش عناصر این فیلد مجموعی محاسبه می‌شود و اگر نود با matchExpressions متناظر مطابقت داشته باشد، مقدار «weight» به مجموع افزوده می‌شود. نودهایی که بیشترین مجموع را داشته باشند، بیشتر از همه ترجیح داده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>requiredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "../definitions/node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>اگر الزامات affinity مشخص‌شده در این فیلد در زمان زمان‌بندی برآورده نشوند، Pod روی آن نود زمان‌بندی نخواهد شد. اگر این الزامات در مقطعی در حین اجرای Pod دیگر برآورده نشوند (برای مثال به‌دلیل یک به‌روزرسانی)، سیستم ممکن است در نهایت تلاش کند Pod را از نود خود بیرون براند (evict) یا ممکن است چنین تلاشی نکند.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableMappedResources {#NodeAllocatableMappedResources}

NodeAllocatableMappedResources تخصیص‌های منابع قابل تخصیص نود (node allocatable) را که نگاشت شده‌اند توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نام منبع است (برای مثال cpu یا memory).</td>
    </tr>
    <tr>
      <td><code>quantity</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Quantity ظرفیت کل منبع قابل تخصیص نود است که برای claim تخصیص داده شده است. دستگاه‌های تخصیص‌یافته به این claim میان همه کانتینرهایی که به claim ارجاع می‌دهند مشترک است. Kubelet این مقدار را هم به requests و هم به limits در cgroup سطح Pod اضافه می‌کند و برای هر کانتینری که به claim ارجاع می‌دهد، آن را به limits در cgroup سطح کانتینر نیز می‌افزاید.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableOverheadResources {#NodeAllocatableOverheadResources}

NodeAllocatableOverheadResources تخصیص‌های منابع سربار (overhead) کمکی را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نام منبع است (برای مثال cpu یا memory).</td>
    </tr>
    <tr>
      <td><code>perContainer</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>PerContainer مقدار سربار متغیری است که برای هر کانتینری که به claim ارجاع می‌دهد اعمال می‌شود. ارجاع‌های کانتینرها در `nodeAllocatableResourceClaimStatuses.containers` ثبت می‌شوند. مقدار کل سربار تخصیص‌یافته برای claim به این صورت محاسبه می‌شود: Quantity = PerPod + (PerContainer * NumReferences). Kubelet این سربار را در cgroupها چنین در نظر می‌گیرد: - cgroup سطح Pod (requests و limits): Kubelet مقدار PerPod + (PerContainer * NumReferences) را اضافه می‌کند. - cgroup سطح کانتینر (فقط limits): Kubelet برای هر کانتینر ارجاع‌دهنده مقدار PerPod + PerContainer را اضافه می‌کند. با این کار هر کانتینر به‌تنهایی می‌تواند به سربار سطح Pod دسترسی داشته باشد، در حالی که cgroup والد مجموع مصرف را محدود می‌کند تا PerPod دقیقاً یک بار محاسبه شود. دست‌کم یکی از PerPod یا PerContainer باید تعیین شود. تعیین‌نکردن هیچ‌کدام پیکربندی نامعتبر است.</td>
    </tr>
    <tr>
      <td><code>perPod</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>PerPod مقدار سربار ثابتی است که به‌ازای هر Pod تخصیص داده می‌شود. افزودن این مقدار به limit هر کانتینر به کانتینرهای منفرد اجازه می‌دهد از سربار استفاده کنند، در حالی که limit مربوط به cgroup والد در سطح Pod، مجموع مصرف را در مرز Pod محدود می‌کند، جایی که سربار دقیقاً یک بار محاسبه می‌شود. دست‌کم یکی از PerPod یا PerContainer باید تعیین شود. تعیین‌نکردن هیچ‌کدام پیکربندی نامعتبر است.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableResourceClaimStatus {#NodeAllocatableResourceClaimStatus}

NodeAllocatableResourceClaimStatus وضعیت منابع قابل تخصیص نود را که از طریق DRA تخصیص داده شده‌اند توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containers</code><br/><em>string array</em></td>
      <td>Containers نام همه کانتینرهای این Pod را فهرست می‌کند که به claim ارجاع می‌دهند.</td>
    </tr>
    <tr>
      <td><code>mapping</code><br/><em><a href="{{< ref "#NodeAllocatableMappedResources" >}}">NodeAllocatableMappedResources array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>Mapping شامل تخصیص‌هایی است که از طریق دستگاه‌های نگاشت‌شده در فیلد `nodeAllocatableResources[...].mapping` مشخصات دستگاه انجام شده‌اند. Kubelet از این مقدار برای اعمال محدودیت در cgroupهای سطح Pod و سطح کانتینر استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>overhead</code><br/><em><a href="{{< ref "#NodeAllocatableOverheadResources" >}}">NodeAllocatableOverheadResources array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>Overhead شامل تخصیص‌هایی است که از طریق دستگاه‌های نگاشت‌شده در فیلد `nodeAllocatableResources[...].overhead` مشخصات دستگاه انجام شده‌اند. Kubelet از این مقدار برای اعمال محدودیت در cgroupهای سطح Pod و سطح کانتینر استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceClaimName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ResourceClaimName نام resource claim ای است که Pod به آن ارجاع داده و این تخصیص منبع قابل تخصیص نود از آن حاصل شده است.</td>
    </tr>
  </tbody>
</table>


## ObjectFieldSelector {#ObjectFieldSelector}

ObjectFieldSelector یک فیلد از آبجکت را همراه با نسخه API آن انتخاب می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>نسخه‌ای از schema که FieldPath بر اساس آن نوشته شده است. مقدار پیش‌فرض آن «v1» است.</td>
    </tr>
    <tr>
      <td><code>fieldPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مسیر فیلدی که باید در نسخه API مشخص‌شده انتخاب شود.</td>
    </tr>
  </tbody>
</table>


## PersistentVolumeClaimTemplate {#PersistentVolumeClaimTemplate}

PersistentVolumeClaimTemplate برای تولید آبجکت‌های PersistentVolumeClaim به‌عنوان بخشی از EphemeralVolumeSource استفاده می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>می‌تواند شامل برچسب‌ها و حاشیه‌نویسی‌هایی باشد که هنگام ایجاد PVC در آن کپی می‌شوند. هیچ فیلد دیگری مجاز نیست و در اعتبارسنجی رد خواهد شد.</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "persistent-volume-claim-v1#PersistentVolumeClaimSpec" >}}">PersistentVolumeClaimSpec</a></em></td>
      <td>مشخصات PersistentVolumeClaim. کل محتوا بدون تغییر در PVC ای که از این قالب ایجاد می‌شود کپی می‌شود. فیلدهای معتبر در یک PersistentVolumeClaim در اینجا نیز معتبر هستند.</td>
    </tr>
  </tbody>
</table>


## PersistentVolumeClaimVolumeSource {#PersistentVolumeClaimVolumeSource}

PersistentVolumeClaimVolumeSource به PVC کاربر در همان فضای نام (namespace) ارجاع می‌دهد. این حجم (volume)، PV متصل‌شده را پیدا می‌کند و آن حجم را برای Pod مانت می‌کند. PersistentVolumeClaimVolumeSource در اصل پوششی (wrapper) است پیرامون نوع دیگری از حجم که مالک آن فرد دیگری (سیستم) است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>claimName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>claimName نام یک PersistentVolumeClaim در همان فضای نام Pod است که از این حجم استفاده می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly تنظیم ReadOnly را در VolumeMounts اجباری می‌کند. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>


## PodAffinity {#PodAffinity}

Pod affinity مجموعه‌ای از قوانین زمان‌بندی مبتنی بر تمایل میان Podها (inter pod affinity) است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>preferredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "#WeightedPodAffinityTerm" >}}">WeightedPodAffinityTerm array</a></em></td>
      <td>زمان‌بند ترجیح می‌دهد Podها را روی نودهایی زمان‌بندی کند که عبارات affinity مشخص‌شده در این فیلد را برآورده می‌کنند، اما ممکن است نودی را انتخاب کند که یک یا چند عبارت را نقض می‌کند. نودی که بیشتر از همه ترجیح داده می‌شود، نودی است که بیشترین مجموع وزن‌ها را دارد. به این صورت که برای هر نودی که همه الزامات زمان‌بندی (درخواست منابع، عبارات affinity از نوع requiredDuringScheduling و غیره) را برآورده می‌کند، با پیمایش عناصر این فیلد مجموعی محاسبه می‌شود و اگر نود دارای Podهایی باشد که با podAffinityTerm متناظر مطابقت دارند، مقدار «weight» به مجموع افزوده می‌شود. نودهایی که بیشترین مجموع را داشته باشند، بیشتر از همه ترجیح داده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>requiredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "#PodAffinityTerm" >}}">PodAffinityTerm array</a></em></td>
      <td>اگر الزامات affinity مشخص‌شده در این فیلد در زمان زمان‌بندی برآورده نشوند، Pod روی آن نود زمان‌بندی نخواهد شد. اگر این الزامات در مقطعی در حین اجرای Pod دیگر برآورده نشوند (برای مثال به‌دلیل به‌روزرسانی برچسب Pod)، سیستم ممکن است در نهایت تلاش کند Pod را از نود خود بیرون براند (evict) یا ممکن است چنین تلاشی نکند. وقتی چند عنصر وجود دارد، فهرست نودهای متناظر با هر podAffinityTerm با هم اشتراک‌گیری می‌شوند؛ یعنی همه termها باید برآورده شوند.</td>
    </tr>
  </tbody>
</table>

## PodAffinityTerm {#PodAffinityTerm}

مجموعه‌ای از Podها را تعریف می‌کند (یعنی Podهایی که با labelSelector در فضای(های) نام داده‌شده مطابقت دارند) که این Pod باید با آن‌ها هم‌مکان (affinity) باشد یا هم‌مکان نباشد (anti-affinity). منظور از هم‌مکانی این است که Pod روی نودی اجرا شود که مقدار برچسب با کلید &lt;topologyKey&gt; در آن با مقدار همان برچسب در هر نودی که یک Pod از این مجموعه روی آن اجرا می‌شود، یکسان باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>labelSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>یک پرس‌وجوی برچسب روی مجموعه‌ای از منابع، که در اینجا Podها هستند. اگر مقدار آن null باشد، این PodAffinityTerm با هیچ Podی مطابقت نخواهد داشت.</td>
    </tr>
    <tr>
      <td><code>matchLabelKeys</code><br/><em>string array</em></td>
      <td>MatchLabelKeys مجموعه‌ای از کلیدهای برچسب Pod است که برای انتخاب Podهای مدنظر به کار می‌رود. از این کلیدها برای یافتن مقادیر از برچسب‌های Pod ورودی استفاده می‌شود و این برچسب‌های کلید-مقدار به‌صورت `key in (value)` با `labelSelector` ادغام می‌شوند تا گروه Podهای موجودی که برای affinity یا anti-affinity بین Podهای Pod ورودی در نظر گرفته می‌شوند، انتخاب شود. کلیدهایی که در برچسب‌های Pod ورودی وجود ندارند نادیده گرفته می‌شوند. مقدار پیش‌فرض خالی است. وجود یک کلید یکسان هم در matchLabelKeys و هم در labelSelector مجاز نیست. همچنین اگر labelSelector تنظیم نشده باشد، نمی‌توان matchLabelKeys را تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>mismatchLabelKeys</code><br/><em>string array</em></td>
      <td>MismatchLabelKeys مجموعه‌ای از کلیدهای برچسب Pod است که برای انتخاب Podهای مدنظر به کار می‌رود. از این کلیدها برای یافتن مقادیر از برچسب‌های Pod ورودی استفاده می‌شود و این برچسب‌های کلید-مقدار به‌صورت `key notin (value)` با `labelSelector` ادغام می‌شوند تا گروه Podهای موجودی که برای affinity یا anti-affinity بین Podهای Pod ورودی در نظر گرفته می‌شوند، انتخاب شود. کلیدهایی که در برچسب‌های Pod ورودی وجود ندارند نادیده گرفته می‌شوند. مقدار پیش‌فرض خالی است. وجود یک کلید یکسان هم در mismatchLabelKeys و هم در labelSelector مجاز نیست. همچنین اگر labelSelector تنظیم نشده باشد، نمی‌توان mismatchLabelKeys را تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>namespaceSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>یک پرس‌وجوی برچسب روی مجموعه فضاهای نامی که این term برای آن‌ها اعمال می‌شود. این term روی اجتماع فضاهای نام انتخاب‌شده توسط این فیلد و فضاهای نام فهرست‌شده در فیلد namespaces اعمال می‌شود. انتخابگر null همراه با فهرست namespaces برابر null یا خالی به معنای «فضای نام همین Pod» است. انتخابگر خالی ({}) با همه فضاهای نام مطابقت دارد.</td>
    </tr>
    <tr>
      <td><code>namespaces</code><br/><em>string array</em></td>
      <td>namespaces فهرستی ایستا از نام فضاهای نام را مشخص می‌کند که این term برای آن‌ها اعمال می‌شود. این term روی اجتماع فضاهای نام فهرست‌شده در این فیلد و فضاهای نام انتخاب‌شده توسط namespaceSelector اعمال می‌شود. فهرست namespaces برابر null یا خالی همراه با namespaceSelector برابر null به معنای «فضای نام همین Pod» است.</td>
    </tr>
    <tr>
      <td><code>topologyKey</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>این Pod باید با Podهایی که در فضاهای نام مشخص‌شده با labelSelector مطابقت دارند هم‌مکان (affinity) باشد یا هم‌مکان نباشد (anti-affinity). منظور از هم‌مکانی این است که Pod روی نودی اجرا شود که مقدار برچسب با کلید topologyKey در آن با مقدار همان برچسب در هر نودی که یکی از Podهای انتخاب‌شده روی آن اجرا می‌شود، یکسان باشد. topologyKey خالی مجاز نیست.</td>
    </tr>
  </tbody>
</table>


## PodAntiAffinity {#PodAntiAffinity}

Pod anti affinity مجموعه‌ای از قواعد زمان‌بندی anti-affinity بین Podها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>preferredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "#WeightedPodAffinityTerm" >}}">WeightedPodAffinityTerm array</a></em></td>
      <td>زمان‌بند ترجیح می‌دهد Podها را روی نودهایی زمان‌بندی کند که عبارت‌های anti-affinity مشخص‌شده در این فیلد را برآورده می‌کنند، اما ممکن است نودی را انتخاب کند که یک یا چند عبارت را نقض می‌کند. نود دارای بیشترین ترجیح، نودی است که مجموع وزن‌های آن بیشترین مقدار را دارد. به این صورت که برای هر نودی که همه الزامات زمان‌بندی (درخواست منابع، عبارت‌های anti-affinity از نوع requiredDuringScheduling و غیره) را برآورده می‌کند، با پیمایش عناصر این فیلد یک مجموع محاسبه می‌شود و اگر نود دارای Podهایی باشد که با podAffinityTerm متناظر مطابقت دارند، مقدار «weight» از مجموع کم می‌شود. نود(های) دارای بیشترین مجموع، بیشترین ترجیح را دارند.</td>
    </tr>
    <tr>
      <td><code>requiredDuringSchedulingIgnoredDuringExecution</code><br/><em><a href="{{< ref "#PodAffinityTerm" >}}">PodAffinityTerm array</a></em></td>
      <td>اگر الزامات anti-affinity مشخص‌شده در این فیلد در زمان زمان‌بندی برآورده نشوند، Pod روی آن نود زمان‌بندی نخواهد شد. اگر الزامات anti-affinity مشخص‌شده در این فیلد در نقطه‌ای در طول اجرای Pod دیگر برآورده نباشند (برای مثال به‌دلیل به‌روزرسانی برچسب Pod)، سیستم ممکن است در نهایت تلاش کند Pod را از نود خود خارج (evict) کند یا تلاش نکند. هنگامی که چند عنصر وجود دارد، فهرست نودهای متناظر با هر podAffinityTerm با هم اشتراک‌گیری می‌شوند، یعنی همه termها باید برآورده شوند.</td>
    </tr>
  </tbody>
</table>


## PodCertificateProjection {#PodCertificateProjection}

PodCertificateProjection یک کلید خصوصی و گواهی X.509 را در سیستم فایل Pod فراهم می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>certificateChainPath</code><br/><em>string</em></td>
      <td>زنجیره گواهی را در این مسیر درون حجم projected می‌نویسد. بیشتر برنامه‌ها باید از credentialBundlePath استفاده کنند. هنگام استفاده از keyPath و certificateChainPath، برنامه شما باید بررسی کند که کلید و گواهی leaf با هم سازگار هستند، زیرا ممکن است فایل‌ها در میانه چرخش (rotation) خوانده شوند.</td>
    </tr>
    <tr>
      <td><code>credentialBundlePath</code><br/><em>string</em></td>
      <td>بسته اعتبارنامه را در این مسیر درون حجم projected می‌نویسد. بسته اعتبارنامه یک فایل واحد است که شامل چند بلوک PEM است. نخستین بلوک PEM از نوع PRIVATE KEY است و یک کلید خصوصی PKCS#8 را دربر دارد. بلوک‌های باقی‌مانده از نوع CERTIFICATE هستند و زنجیره گواهی صادرشده توسط signer (گواهی leaf و هر گواهی میانی) را دربر دارند. با استفاده از credentialBundlePath، کد برنامه Pod شما می‌تواند با یک خواندن اتمیک، کلید و زنجیره گواهی سازگار را دریافت کند. اگر آن‌ها را در فایل‌های جداگانه projected کنید، کد برنامه شما باید علاوه بر آن بررسی کند که گواهی leaf برای همین کلید صادر شده است.</td>
    </tr>
    <tr>
      <td><code>keyPath</code><br/><em>string</em></td>
      <td>کلید را در این مسیر درون حجم projected می‌نویسد. بیشتر برنامه‌ها باید از credentialBundlePath استفاده کنند. هنگام استفاده از keyPath و certificateChainPath، برنامه شما باید بررسی کند که کلید و گواهی leaf با هم سازگار هستند، زیرا ممکن است فایل‌ها در میانه چرخش (rotation) خوانده شوند.</td>
    </tr>
    <tr>
      <td><code>keyType</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع جفت‌کلیدی که Kubelet برای Pod تولید می‌کند. مقادیر معتبر عبارت‌اند از "RSA3072"، "RSA4096"، "ECDSAP256"، "ECDSAP384"، "ECDSAP521" و "ED25519".</td>
    </tr>
    <tr>
      <td><code>maxExpirationSeconds</code><br/><em>integer</em></td>
      <td>maxExpirationSeconds بیشینه طول عمر مجاز برای گواهی است. Kubelet این مقدار را عیناً در PodCertificateRequestهایی که برای این projection تولید می‌کند، کپی می‌کند. اگر مشخص نشود، kube-apiserver آن را روی 86400 (۲۴ ساعت) تنظیم می‌کند. kube-apiserver مقادیر کمتر از 3600 (یک ساعت) را رد می‌کند. بیشینه مقدار مجاز 7862400 (۹۱ روز) است. پیاده‌سازی signer آزاد است گواهی‌ای با هر طول عمری *کوتاه‌تر* از MaxExpirationSeconds صادر کند، اما نه کمتر از 3600 ثانیه (یک ساعت). این محدودیت توسط kube-apiserver اعمال می‌شود. signerهای `kubernetes.io` هرگز گواهی‌ای با طول عمر بیش از ۲۴ ساعت صادر نمی‌کنند.</td>
    </tr>
    <tr>
      <td><code>signerName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>درخواست‌های CSR تولیدشده توسط Kubelet به این signer ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>integer</em></td>
      <td>user اختیاری است: UID مالک فایل ایجادشده. در صورت مشخص شدن، فیلد user در سطح آیتم بر defaultUser اولویت دارد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
    <tr>
      <td><code>userAnnotations</code><br/><em>object</em></td>
      <td>userAnnotations به سازندگان Pod امکان می‌دهد اطلاعات اضافی را به پیاده‌سازی signer منتقل کنند. کوبرنتیز هیچ محدودیتی بر این فراداده اعمال نمی‌کند و آن را به هیچ شکلی اعتبارسنجی نمی‌کند. این مقادیر عیناً در فیلد `spec.unverifiedUserAnnotations` آبجکت‌های PodCertificateRequest که Kubelet ایجاد می‌کند کپی می‌شوند. ورودی‌ها مشمول همان اعتبارسنجی حاشیه‌نویسی‌های (annotation) فراداده آبجکت هستند، با این تفاوت که همه کلیدها باید پیشوند دامنه داشته باشند. هیچ محدودیتی بر مقادیر اعمال نمی‌شود، مگر محدودیت اندازه کلی برای کل فیلد. signerها باید کلیدها و مقادیری را که پشتیبانی می‌کنند مستند کنند. signerها باید درخواست‌هایی را که شامل کلیدهای ناشناخته برای آن‌ها هستند رد کنند.</td>
    </tr>
  </tbody>
</table>


## PodCondition {#PodCondition}

PodCondition جزئیات وضعیت (condition) فعلی این Pod را دربر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastProbeTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که condition بررسی (probe) شده است.</td>
    </tr>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که condition از یک وضعیت به وضعیت دیگر تغییر کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی قابل‌خواندن برای انسان که جزئیات آخرین تغییر وضعیت را بیان می‌کند.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>در صورت تنظیم، نشان‌دهنده مقدار .metadata.generation است که condition مربوط به Pod بر اساس آن تنظیم شده است.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیلی یکتا، تک‌کلمه‌ای و با قالب CamelCase برای آخرین تغییر وضعیت condition.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Status وضعیت condition است. می‌تواند True، False یا Unknown باشد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Type نوع condition است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions</td>
    </tr>
  </tbody>
</table>


## PodDNSConfig {#PodDNSConfig}

PodDNSConfig پارامترهای DNS یک Pod را علاوه بر پارامترهای تولیدشده از DNSPolicy تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nameservers</code><br/><em>string array</em></td>
      <td>فهرستی از نشانی‌های IP سرورهای نام DNS. این فهرست به nameserverهای پایه تولیدشده از DNSPolicy افزوده می‌شود. nameserverهای تکراری حذف می‌شوند.</td>
    </tr>
    <tr>
      <td><code>options</code><br/><em><a href="{{< ref "#PodDNSConfigOption" >}}">PodDNSConfigOption array</a></em></td>
      <td>فهرستی از گزینه‌های resolver در DNS. این فهرست با گزینه‌های پایه تولیدشده از DNSPolicy ادغام می‌شود. ورودی‌های تکراری حذف می‌شوند. گزینه‌های resolution که در Options داده شده‌اند، بر گزینه‌هایی که در DNSPolicy پایه آمده‌اند اولویت دارند.</td>
    </tr>
    <tr>
      <td><code>searches</code><br/><em>string array</em></td>
      <td>فهرستی از دامنه‌های جست‌وجوی DNS برای یافتن نام میزبان. این فهرست به مسیرهای جست‌وجوی پایه تولیدشده از DNSPolicy افزوده می‌شود. مسیرهای جست‌وجوی تکراری حذف می‌شوند.</td>
    </tr>
  </tbody>
</table>


## PodDNSConfigOption {#PodDNSConfigOption}

PodDNSConfigOption گزینه‌های resolver در DNS یک Pod را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>Name نام این گزینه resolver در DNS است. الزامی است.</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em>string</em></td>
      <td>Value مقدار این گزینه resolver در DNS است.</td>
    </tr>
  </tbody>
</table>


## PodExtendedResourceClaimStatus {#PodExtendedResourceClaimStatus}

PodExtendedResourceClaimStatus در PodStatus برای درخواست‌های منبع توسعه‌یافته (extended resource) که توسط DRA پشتیبانی می‌شوند ذخیره می‌شود. این آبجکت نام تولیدشده برای ResourceClaim ویژه متناظر را که توسط زمان‌بند ایجاد شده است نگه می‌دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>requestMappings</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#ContainerExtendedResourceRequest" >}}">ContainerExtendedResourceRequest array</a></em></td>
      <td>RequestMappings نگاشت \<container, extended resource backed by DRA> به درخواست دستگاه (device request) را در ResourceClaim تولیدشده مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceClaimName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ResourceClaimName نام ResourceClaim ای است که برای Pod در فضای نام همان Pod تولید شده است.</td>
    </tr>
  </tbody>
</table>


## PodIP {#PodIP}

PodIP یک نشانی IP واحد را که به Pod اختصاص داده شده است نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>ip</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>IP نشانی IP اختصاص‌یافته به Pod است.</td>
    </tr>
  </tbody>
</table>


## PodOS {#PodOS}

PodOS پارامترهای سیستم‌عامل یک Pod را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نام سیستم‌عامل است. مقادیر پشتیبانی‌شده فعلی linux و windows هستند. ممکن است در آینده مقادیر دیگری نیز تعریف شوند که می‌توانند یکی از مقادیر موجود در https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration باشند. کلاینت‌ها باید انتظار مقادیر اضافی را داشته باشند و مقادیر ناشناخته در این فیلد را معادل os: null در نظر بگیرند.</td>
    </tr>
  </tbody>
</table>


## PodReadinessGate {#PodReadinessGate}

PodReadinessGate ارجاعی به یک condition از Pod را دربر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conditionType</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ConditionType به یک condition در فهرست conditionهای Pod اشاره می‌کند که type آن مطابقت دارد.</td>
    </tr>
  </tbody>
</table>


## PodResourceClaim {#PodResourceClaim}

PodResourceClaim دقیقاً به یک ResourceClaim ارجاع می‌دهد، یا به‌صورت مستقیم یا با ذکر نام یک ResourceClaimTemplate که سپس برای Pod به یک ResourceClaim تبدیل می‌شود.

این آبجکت یک نام به آن اضافه می‌کند که ResourceClaim را درون Pod به‌طور یکتا شناسایی می‌کند. کانتینرهایی که به ResourceClaim نیاز دارند، با همین نام به آن ارجاع می‌دهند.

هنگامی که feature gate با نام DRAWorkloadResourceClaims فعال باشد و این Pod به یک PodGroup تعلق داشته باشد، یک PodResourceClaim در صورتی با یک PodGroupResourceClaim مطابقت داده می‌شود که همه فیلدهای آن‌ها (Name، ResourceClaimName و ResourceClaimTemplateName) برابر باشند. یک claim مطابقت‌یافته به یک ResourceClaim واحد ارجاع می‌دهد که میان همه Podهای PodGroup مشترک است و به‌جای تک‌تک Podها، برای PodGroup در ResourceClaimStatus.ReservedFor رزرو می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name این resource claim را درون Pod به‌طور یکتا شناسایی می‌کند. این مقدار باید یک DNS_LABEL باشد.</td>
    </tr>
    <tr>
      <td><code>resourceClaimName</code><br/><em>string</em></td>
      <td>ResourceClaimName نام یک آبجکت ResourceClaim در همان فضای نام این Pod است. دقیقاً یکی از ResourceClaimName و ResourceClaimTemplateName باید تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>resourceClaimTemplateName</code><br/><em>string</em></td>
      <td>ResourceClaimTemplateName نام یک آبجکت ResourceClaimTemplate در همان فضای نام این Pod است. از این قالب برای ایجاد یک ResourceClaim جدید استفاده می‌شود که به این Pod متصل (bind) خواهد شد. هنگامی که این Pod حذف شود، ResourceClaim نیز حذف می‌شود. نام Pod و نام منبع، به‌همراه یک بخش تولیدشده، برای ساخت نام یکتای ResourceClaim به کار می‌روند که در pod.status.resourceClaimStatuses ثبت می‌شود. هنگامی که feature gate با نام DRAWorkloadResourceClaims فعال باشد و Pod به یک PodGroup تعلق داشته باشد که یک PodGroupResourceClaim با همان Name و ResourceClaimTemplateName تعریف کرده است، این PodResourceClaim به ResourceClaim تولیدشده برای PodGroup ارجاع می‌یابد. همه Podهای گروه که یک PodResourceClaim معادل با Name و ResourceClaimTemplateName مربوط به PodGroupResourceClaim تعریف کرده‌اند، از همان ResourceClaim تولیدشده به‌صورت مشترک استفاده می‌کنند. ResourceClaimهای تولیدشده برای یک PodGroup متعلق به همان PodGroup هستند و چرخه عمر آن‌ها به‌جای هر Pod منفرد، به PodGroup وابسته است. این فیلد تغییرناپذیر (immutable) است و control plane پس از ایجاد ResourceClaim هیچ تغییری در ResourceClaim متناظر اعمال نمی‌کند. دقیقاً یکی از ResourceClaimName و ResourceClaimTemplateName باید تنظیم شود.</td>
    </tr>
  </tbody>
</table>

## PodSchedulingGate {#PodSchedulingGate}

PodSchedulingGate به یک Pod متصل می‌شود تا زمان‌بندی آن را مهار کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام scheduling gate. هر scheduling gate باید فیلد name یکتا داشته باشد.</td>
    </tr>
  </tbody>
</table>


## PodSchedulingGroup {#PodSchedulingGroup}

PodSchedulingGroup نمونهٔ زمان اجرای گروه زمان‌بندی را مشخص می‌کند که یک Pod به آن تعلق دارد. زمان‌بند از این اطلاعات برای اعمال معناشناسی زمان‌بندی آگاه از بار کاری استفاده می‌کند. دقیقاً یک فیلد باید مشخص شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>podGroupName</code><br/><em>string</em></td>
      <td>PodGroupName نام آبجکت مستقل PodGroup را مشخص می‌کند که نمونهٔ زمان اجرای این گروه را نمایندگی می‌کند. باید یک DNS subdomain باشد.</td>
    </tr>
  </tbody>
</table>


## PodSecurityContext {#PodSecurityContext}

PodSecurityContext ویژگی‌های امنیتی در سطح Pod و تنظیمات مشترک کانتینرها را نگه می‌دارد. برخی فیلدها در container.securityContext نیز وجود دارند. مقادیر فیلدهای container.securityContext بر مقادیر فیلدهای PodSecurityContext اولویت دارند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>appArmorProfile</code><br/><em><a href="{{< ref "#AppArmorProfile" >}}">AppArmorProfile</a></em></td>
      <td>appArmorProfile گزینه‌های AppArmor است که کانتینرهای این Pod از آن‌ها استفاده می‌کنند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>fsGroup</code><br/><em>integer</em></td>
      <td>یک گروه تکمیلی ویژه که برای همهٔ کانتینرهای یک Pod اعمال می‌شود. برخی انواع حجم (volume) به Kubelet اجازه می‌دهند مالکیت آن حجم را به‌گونه‌ای تغییر دهد که متعلق به Pod باشد:  1. GID مالک برابر FSGroup خواهد بود 2. بیت setgid تنظیم می‌شود (فایل‌های جدیدی که در حجم ایجاد می‌شوند متعلق به FSGroup خواهند بود) 3. بیت‌های مجوز با rw-rw---- به‌صورت OR ترکیب می‌شوند  اگر تنظیم نشود، Kubelet مالکیت و مجوزهای هیچ حجمی را تغییر نمی‌دهد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>fsGroupChangePolicy</code><br/><em>string</em></td>
      <td>fsGroupChangePolicy رفتار تغییر مالکیت و مجوزهای حجم را پیش از در دسترس قرار گرفتن آن در داخل Pod تعیین می‌کند. این فیلد فقط برای انواع حجمی اعمال می‌شود که از مالکیت (و مجوزهای) مبتنی بر fsGroup پشتیبانی می‌کنند. این فیلد بر انواع حجم موقتی مانند secret، configmaps و emptydir تأثیری ندارد. مقادیر معتبر "OnRootMismatch" و "Always" هستند. اگر مشخص نشود، از "Always" استفاده می‌شود. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.<br/><br/>Possible enum values:<br/> - `"Always"` نشان می‌دهد که مالکیت و مجوزهای حجم باید هر بار که حجم در داخل یک Pod مانت می‌شود تغییر کند. این رفتار پیش‌فرض است.<br/> - `"OnRootMismatch"` نشان می‌دهد که مالکیت و مجوزهای حجم فقط زمانی تغییر می‌کند که مجوزها و مالکیت دایرکتوری ریشه با مجوزهای مورد انتظار روی حجم مطابقت نداشته باشد. این کار می‌تواند زمان لازم برای تغییر مالکیت و مجوزهای یک حجم را کوتاه کند.</td>
    </tr>
    <tr>
      <td><code>runAsGroup</code><br/><em>integer</em></td>
      <td>GID برای اجرای entrypoint فرایند کانتینر. اگر تنظیم نشود، از مقدار پیش‌فرض محیط اجرا استفاده می‌شود. این مقدار را می‌توان در SecurityContext نیز تنظیم کرد. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext برای آن کانتینر اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>runAsNonRoot</code><br/><em>boolean</em></td>
      <td>نشان می‌دهد که کانتینر باید با کاربری غیر از root اجرا شود. اگر true باشد، Kubelet ایمیج را در زمان اجرا اعتبارسنجی می‌کند تا مطمئن شود با UID برابر 0 (root) اجرا نمی‌شود، و در صورت اجرا با این UID، راه‌اندازی کانتینر را با شکست مواجه می‌کند. اگر تنظیم نشود یا false باشد، چنین اعتبارسنجی‌ای انجام نخواهد شد. این مقدار را می‌توان در SecurityContext نیز تنظیم کرد. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext اولویت دارد.</td>
    </tr>
    <tr>
      <td><code>runAsUser</code><br/><em>integer</em></td>
      <td>UID برای اجرای entrypoint فرایند کانتینر. اگر مشخص نشود، مقدار پیش‌فرض کاربری است که در فراداده (metadata) ایمیج تعیین شده است. این مقدار را می‌توان در SecurityContext نیز تنظیم کرد. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext برای آن کانتینر اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>seLinuxChangePolicy</code><br/><em>string</em></td>
      <td>seLinuxChangePolicy تعیین می‌کند برچسب SELinux کانتینر چگونه بر همهٔ حجم‌هایی که Pod استفاده می‌کند اعمال شود. این فیلد روی نودهایی که از SELinux پشتیبانی نمی‌کنند یا روی حجم‌هایی که از SELinux پشتیبانی نمی‌کنند تأثیری ندارد. مقادیر معتبر "MountOption" و "Recursive" هستند.  "Recursive" به این معناست که محیط اجرای کانتینر همهٔ فایل‌های موجود در همهٔ حجم‌های Pod را دوباره برچسب‌گذاری می‌کند. این کار ممکن است برای حجم‌های بزرگ کند باشد، اما اجازه می‌دهد Podهای دارای دسترسی ویژه و بدون دسترسی ویژه، یک حجم مشترک را روی یک نود به‌صورت ترکیبی استفاده کنند.  "MountOption" همهٔ حجم‌های واجد شرایط Pod را با گزینهٔ مانت `-o context` مانت می‌کند. این کار مستلزم آن است که همهٔ Podهایی که یک حجم را به اشتراک می‌گذارند از یک برچسب SELinux یکسان استفاده کنند. اشتراک یک حجم میان Podهای دارای دسترسی ویژه و بدون دسترسی ویژه ممکن نیست. حجم‌های واجد شرایط عبارت‌اند از حجم‌های in-tree از نوع FibreChannel و iSCSI، و همهٔ حجم‌های CSI که درایور CSI آن‌ها با تنظیم spec.seLinuxMount: true در نمونهٔ CSIDriver خود، پشتیبانی از SELinux را اعلام می‌کند. سایر حجم‌ها همیشه به‌صورت بازگشتی دوباره برچسب‌گذاری می‌شوند.  اگر مشخص نشود، از "MountOption" استفاده می‌شود.  این فیلد فقط بر Podهایی اثر می‌گذارد که برچسب SELinux در PodSecurityContext یا در SecurityContext همهٔ کانتینرهایشان تنظیم شده باشد.  همهٔ Podهایی که از یک حجم یکسان استفاده می‌کنند باید seLinuxChangePolicy یکسانی داشته باشند، در غیر این صورت ممکن است برخی Podها در وضعیت ContainerCreating باقی بمانند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>seLinuxOptions</code><br/><em><a href="{{< ref "#SELinuxOptions" >}}">SELinuxOptions</a></em></td>
      <td>زمینهٔ (context) SELinux که باید بر همهٔ کانتینرها اعمال شود. اگر مشخص نشود، محیط اجرای کانتینر برای هر کانتینر یک زمینهٔ SELinux تصادفی اختصاص می‌دهد.  این مقدار را می‌توان در SecurityContext نیز تنظیم کرد. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext برای آن کانتینر اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>seccompProfile</code><br/><em><a href="{{< ref "#SeccompProfile" >}}">SeccompProfile</a></em></td>
      <td>گزینه‌های seccomp که کانتینرهای این Pod از آن‌ها استفاده می‌کنند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>supplementalGroups</code><br/><em>integer array</em></td>
      <td>فهرستی از گروه‌ها که علاوه بر GID اصلی کانتینر و fsGroup (در صورت مشخص بودن)، به اولین فرایندی که در هر کانتینر اجرا می‌شود اعمال می‌گردد.  اگر ویژگی SupplementalGroupsPolicy فعال باشد، فیلد supplementalGroupsPolicy تعیین می‌کند که این گروه‌ها علاوه بر عضویت‌های گروهی تعریف‌شده در ایمیج کانتینر اعمال شوند یا جایگزین آن‌ها گردند. اگر مشخص نشود، هیچ گروه اضافه‌ای افزوده نمی‌شود، هرچند بسته به فیلد supplementalGroupsPolicy ممکن است عضویت‌های گروهی تعریف‌شده در ایمیج کانتینر همچنان استفاده شوند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>supplementalGroupsPolicy</code><br/><em>string</em></td>
      <td>تعیین می‌کند گروه‌های تکمیلی فرایندهای اولین کانتینر چگونه محاسبه شوند. مقادیر معتبر "Merge" و "Strict" هستند. اگر مشخص نشود، از "Merge" استفاده می‌شود. (آلفا) استفاده از این فیلد مستلزم فعال بودن feature gate با نام SupplementalGroupsPolicy است و محیط اجرای کانتینر باید از این ویژگی پشتیبانی کند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.<br/><br/>Possible enum values:<br/> - `"Merge"` به این معناست که SupplementalGroups و FsGroup ارائه‌شدهٔ کانتینر (که در SecurityContext مشخص شده‌اند) با گروه‌های کاربر اصلی که در ایمیج کانتینر (در /etc/group) تعریف شده‌اند ادغام می‌شوند.<br/> - `"Strict"` به این معناست که SupplementalGroups و FsGroup ارائه‌شدهٔ کانتینر (که در SecurityContext مشخص شده‌اند) به‌جای هر گروهی که در ایمیج کانتینر تعریف شده است استفاده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>sysctls</code><br/><em><a href="{{< ref "#Sysctl" >}}">Sysctl array</a></em></td>
      <td>Sysctls فهرستی از sysctlهای دارای namespace را نگه می‌دارد که برای Pod استفاده می‌شوند. Podهایی که sysctlهای پشتیبانی‌نشده (توسط محیط اجرای کانتینر) داشته باشند ممکن است راه‌اندازی نشوند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>windowsOptions</code><br/><em><a href="{{< ref "#WindowsSecurityContextOptions" >}}">WindowsSecurityContextOptions</a></em></td>
      <td>تنظیمات ویژهٔ Windows که بر همهٔ کانتینرها اعمال می‌شود. اگر مشخص نشود، از گزینه‌های موجود در SecurityContext کانتینر استفاده می‌شود. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext اولویت دارد. توجه کنید که وقتی spec.os.name برابر linux باشد، این فیلد را نمی‌توان تنظیم کرد.</td>
    </tr>
  </tbody>
</table>


## PodVolumeHealth {#PodVolumeHealth}

PodVolumeHealth اطلاعات سلامت یک حجم را که یک Pod استفاده می‌کند در بر دارد و توسط افزونهٔ نود CSI از طریق kubelet گزارش می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>healthConditions</code><br/><em><a href="{{< ref "../definitions/volume-health-condition-v1#VolumeHealthCondition" >}}">VolumeHealthCondition array</a></em><br/><em>patch strategy: merge on key <code>status</code></em></td>
      <td>conditions مجموعهٔ شرایط نامطلوبی است که افزونهٔ نود CSI برای این حجم روی این نود گزارش کرده است. حداکثر 16 شرط را می‌توان گزارش کرد.</td>
    </tr>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>lastTransitionTime زمانی است که مجموعهٔ فعلی شرایط برای نخستین بار ظاهر شد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name با یکی از ورودی‌های pod.spec.volumes مطابقت دارد.</td>
    </tr>
  </tbody>
</table>


## PreferredSchedulingTerm {#PreferredSchedulingTerm}

یک preferred scheduling term خالی با وزن ضمنی 0 با همهٔ آبجکت‌ها مطابقت دارد (یعنی بی‌اثر است). یک preferred scheduling term برابر null با هیچ آبجکتی مطابقت ندارد (یعنی آن هم بی‌اثر است).

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>preference</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/node-selector-term-v1#NodeSelectorTerm" >}}">NodeSelectorTerm</a></em></td>
      <td>یک node selector term که با وزن متناظر مرتبط است.</td>
    </tr>
    <tr>
      <td><code>weight</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>وزن مرتبط با تطابق nodeSelectorTerm متناظر، در بازهٔ 1 تا 100.</td>
    </tr>
  </tbody>
</table>


## Probe {#Probe}

Probe یک بررسی سلامت را توصیف می‌کند که روی یک کانتینر انجام می‌شود تا مشخص شود کانتینر زنده است یا آمادهٔ دریافت ترافیک است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>exec</code><br/><em><a href="{{< ref "#ExecAction" >}}">ExecAction</a></em></td>
      <td>Exec دستوری را مشخص می‌کند که باید در کانتینر اجرا شود.</td>
    </tr>
    <tr>
      <td><code>failureThreshold</code><br/><em>integer</em></td>
      <td>حداقل تعداد شکست‌های متوالی که لازم است تا probe پس از موفقیت قبلی، ناموفق در نظر گرفته شود. مقدار پیش‌فرض 3 است. حداقل مقدار 1 است.</td>
    </tr>
    <tr>
      <td><code>grpc</code><br/><em><a href="{{< ref "#GRPCAction" >}}">GRPCAction</a></em></td>
      <td>GRPC یک GRPC HealthCheckRequest را مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>httpGet</code><br/><em><a href="{{< ref "#HTTPGetAction" >}}">HTTPGetAction</a></em></td>
      <td>HTTPGet یک درخواست HTTP GET را مشخص می‌کند که باید انجام شود.</td>
    </tr>
    <tr>
      <td><code>initialDelaySeconds</code><br/><em>integer</em></td>
      <td>تعداد ثانیه‌هایی که پس از شروع کانتینر سپری می‌شود تا liveness probeها آغاز شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes</td>
    </tr>
    <tr>
      <td><code>periodSeconds</code><br/><em>integer</em></td>
      <td>هر چند وقت (بر حسب ثانیه) probe انجام شود. مقدار پیش‌فرض 10 ثانیه است. حداقل مقدار 1 است.</td>
    </tr>
    <tr>
      <td><code>successThreshold</code><br/><em>integer</em></td>
      <td>حداقل تعداد موفقیت‌های متوالی که لازم است تا probe پس از شکست قبلی، موفق در نظر گرفته شود. مقدار پیش‌فرض 1 است. برای liveness و startup باید 1 باشد. حداقل مقدار 1 است.</td>
    </tr>
    <tr>
      <td><code>tcpSocket</code><br/><em><a href="{{< ref "#TCPSocketAction" >}}">TCPSocketAction</a></em></td>
      <td>TCPSocket یک اتصال به یک پورت TCP را مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>terminationGracePeriodSeconds</code><br/><em>integer</em></td>
      <td>مدت زمان اختیاری (بر حسب ثانیه) که Pod پس از شکست probe برای خاتمه‌یافتن با مدیریت ملایم (graceful) نیاز دارد. این مهلت، فاصلهٔ زمانی (بر حسب ثانیه) میان ارسال سیگنال خاتمه به فرایندهای در حال اجرا در Pod و زمانی است که فرایندها با سیگنال kill به‌اجبار متوقف می‌شوند. این مقدار را بیشتر از زمان پاک‌سازی مورد انتظار فرایند خود تنظیم کنید. اگر این مقدار nil باشد، از terminationGracePeriodSeconds خود Pod استفاده می‌شود؛ در غیر این صورت، این مقدار جایگزین مقداری می‌شود که در spec مربوط به Pod ارائه شده است. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای توقف فوری از طریق سیگنال kill است (بدون فرصتی برای خاموش‌شدن). این فیلد بتا است و نیازمند فعال بودن feature gate با نام ProbeTerminationGracePeriod است. حداقل مقدار 1 است. اگر تنظیم نشود، از spec.terminationGracePeriodSeconds استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code><br/><em>integer</em></td>
      <td>تعداد ثانیه‌هایی که پس از آن probe با تایم‌اوت مواجه می‌شود. مقدار پیش‌فرض 1 ثانیه است. حداقل مقدار 1 است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes</td>
    </tr>
  </tbody>
</table>


## ProjectedVolumeSource {#ProjectedVolumeSource}

یک منبع حجم projected را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>defaultMode</code><br/><em>integer</em></td>
      <td>defaultMode بیت‌های مجوزی است که به‌طور پیش‌فرض برای تنظیم مجوزهای فایل‌های ایجادشده استفاده می‌شود. باید یک مقدار هشتایی (octal) بین 0000 و 0777 یا یک مقدار دهدهی بین 0 و 511 باشد. YAML هر دو مقدار هشتایی و دهدهی را می‌پذیرد، اما JSON برای بیت‌های مجوز به مقادیر دهدهی نیاز دارد. دایرکتوری‌های درون مسیر تحت تأثیر این تنظیم قرار نمی‌گیرند. ممکن است این مقدار با سایر گزینه‌هایی که بر مجوز فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های مجوز دیگری تنظیم شوند.</td>
    </tr>
    <tr>
      <td><code>defaultUser</code><br/><em>integer</em></td>
      <td>defaultUser اختیاری است: UID مالک فایل‌های ایجادشده به‌طور پیش‌فرض. فیلد defaultUser فقط زمانی به‌عنوان مقدار جایگزین استفاده می‌شود که فیلد user در سطح هر آیتم تنظیم نشده باشد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
    <tr>
      <td><code>sources</code><br/><em><a href="{{< ref "#VolumeProjection" >}}">VolumeProjection array</a></em></td>
      <td>sources فهرست projectionهای حجم است. هر ورودی در این فهرست یک منبع را مدیریت می‌کند.</td>
    </tr>
  </tbody>
</table>

## RBDVolumeSource {#RBDVolumeSource}

یک حجم Rados Block Device را نمایش می‌دهد که به‌اندازهٔ چرخهٔ عمر Pod روی نود مانت می‌شود. حجم‌های RBD از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایل حجمی است که می‌خواهید مانت کنید. نکته: مطمئن شوید که سیستم‌عامل میزبان از این نوع سیستم فایل پشتیبانی می‌کند. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#rbd</td>
    </tr>
    <tr>
      <td><code>image</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>image نام ایمیج rados است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>keyring</code><br/><em>string</em></td>
      <td>keyring مسیر key ring مربوط به RBDUser است. مقدار پیش‌فرض /etc/ceph/keyring است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>monitors</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>monitors مجموعه‌ای از مانیتورهای Ceph است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>pool</code><br/><em>string</em></td>
      <td>pool نام pool در rados است. مقدار پیش‌فرض rbd است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا تنظیم ReadOnly را در VolumeMounts اجباری می‌کند. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef نام Secret احراز هویت برای RBDUser است. در صورت تعیین، بر keyring اولویت پیدا می‌کند. مقدار پیش‌فرض nil است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user نام کاربر rados است. مقدار پیش‌فرض admin است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
  </tbody>
</table>


## ResourceClaim {#ResourceClaim}

ResourceClaim به یکی از ورودی‌های PodSpec.ResourceClaims ارجاع می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name باید با نام یکی از ورودی‌های pod.spec.resourceClaims در Pod محل استفاده از این فیلد مطابقت داشته باشد. با این کار، آن منبع درون کانتینر در دسترس قرار می‌گیرد.</td>
    </tr>
    <tr>
      <td><code>request</code><br/><em>string</em></td>
      <td>Request نامی است که برای یک درخواست در claim ارجاع‌شده انتخاب شده است. اگر خالی باشد، همهٔ موارد claim در دسترس قرار می‌گیرند؛ در غیر این صورت فقط نتیجهٔ همین درخواست در دسترس خواهد بود.</td>
    </tr>
  </tbody>
</table>


## ResourceFieldSelector {#ResourceFieldSelector}

ResourceFieldSelector منابع کانتینر (cpu و memory) و قالب خروجی آن‌ها را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerName</code><br/><em>string</em></td>
      <td>نام کانتینر: برای حجم‌ها الزامی و برای متغیرهای محیطی اختیاری است.</td>
    </tr>
    <tr>
      <td><code>divisor</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>قالب خروجی منابع در معرض‌گذاشته‌شده را مشخص می‌کند. مقدار پیش‌فرض "1" است.</td>
    </tr>
    <tr>
      <td><code>resource</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>الزامی: منبعی که باید انتخاب شود.</td>
    </tr>
  </tbody>
</table>


## ResourceHealth {#ResourceHealth}

ResourceHealth وضعیت سلامت یک منبع را نمایش می‌دهد و آخرین اطلاعات سلامت دستگاه را در بر دارد. این بخشی از KEP به نشانی https://kep.k8s.io/4680 است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>health</code><br/><em>string</em></td>
      <td>سلامت منبع. می‌تواند یکی از مقادیر زیر باشد:  - Healthy: عملکرد عادی  - Unhealthy: ناسالم گزارش شده است. این وضعیت را یک مشکل موقت سلامت در نظر می‌گیریم، زیرا در حال حاضر سازوکاری برای تمایز مشکلات موقت و دائمی وجود ندارد.  - Unknown: وضعیت قابل تعیین نیست. برای مثال، ثبت Device Plugin لغو شده و پس از آن دوباره ثبت نشده است.  در آینده ممکن است وضعیت PermanentlyUnhealthy نیز معرفی شود.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>Message توضیحی قابل‌خواندن برای انسان دربارهٔ Health ارائه می‌دهد (مثلاً "ECC error count exceeded threshold"). وقتی ResourceHealthStatusMessage فعال باشد و افزونهٔ DRA پیامی برگرداند، kubelet این فیلد را مقداردهی می‌کند؛ در غیر این صورت مقدار آن null است.</td>
    </tr>
    <tr>
      <td><code>resourceID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ResourceID شناسهٔ یکتای منبع است. برای اطلاعات بیشتر به نوع ResourceID مراجعه کنید.</td>
    </tr>
  </tbody>
</table>


## ResourceRequirements {#ResourceRequirements}

ResourceRequirements نیازمندی‌های منابع محاسباتی را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>claims</code><br/><em><a href="{{< ref "#ResourceClaim" >}}">ResourceClaim array</a></em></td>
      <td>Claims نام منابعی را فهرست می‌کند که در spec.resourceClaims تعریف شده‌اند و این کانتینر از آن‌ها استفاده می‌کند.  این فیلد به feature gate با نام DynamicResourceAllocation وابسته است.  این فیلد تغییرناپذیر است و فقط برای کانتینرها قابل تنظیم است.</td>
    </tr>
    <tr>
      <td><code>limits</code><br/><em>object</em></td>
      <td>Limits حداکثر مقدار مجاز منابع محاسباتی را توصیف می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</td>
    </tr>
    <tr>
      <td><code>requests</code><br/><em>object</em></td>
      <td>Requests حداقل مقدار لازم از منابع محاسباتی را توصیف می‌کند. اگر Requests برای یک کانتینر حذف شود، در صورت تعیین صریح Limits مقدار آن برابر Limits خواهد بود؛ در غیر این صورت مقداری می‌گیرد که پیاده‌سازی تعیین می‌کند. مقدار Requests نمی‌تواند از Limits بیشتر باشد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</td>
    </tr>
  </tbody>
</table>


## ResourceStatus {#ResourceStatus}

ResourceStatus وضعیت یک منبع منفرد را نمایش می‌دهد که به یک Pod تخصیص داده شده است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام منبع. این نام باید در Pod یکتا باشد و در مورد منابع غیر DRA باید با یکی از منابع موجود در مشخصات Pod مطابقت داشته باشد. برای منابع DRA، وقتی container.resources.claims[*].request تنظیم شده باشد مقدار باید "claim:\<claim_name>/\<request>" و وقتی container.resources.claims[*].request خالی باشد باید "claim:\<claim_name>" باشد. برای منابع توسعه‌یافتهٔ مبتنی بر DRA، وقتی نام claim و نام request در pod.status.extendedResourceClaimStatus ثبت شده باشند، از "claim:\<claim_name>/\<request>" استفاده می‌شود. وقتی این وضعیت دربارهٔ یک کانتینر گزارش می‌شود، "claim_name" و "request" باید با یکی از claimهای آن کانتینر مطابقت داشته باشند.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em><a href="{{< ref "#ResourceHealth" >}}">ResourceHealth array</a></em></td>
      <td>فهرست سلامت منابع یکتا. هر عنصر فهرست شامل یک شناسهٔ منبع یکتا و وضعیت سلامت آن است. شناسهٔ منبع باید دست‌کم در طول عمر یک Pod، منبع تخصیص‌یافته به آن Pod روی نود را به‌طور یکتا مشخص کند. اگر Pod دیگری روی همان نود وضعیتی با همان شناسهٔ منبع گزارش کند، باید همان منبع مشترک باشد. قالب خاص شناسه در موارد استفادهٔ مختلف در تعریف نوع ResourceID آمده است.</td>
    </tr>
  </tbody>
</table>


## SELinuxOptions {#SELinuxOptions}

SELinuxOptions برچسب‌هایی است که باید به کانتینر اعمال شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>level</code><br/><em>string</em></td>
      <td>Level برچسب سطح SELinux است که به کانتینر اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>role</code><br/><em>string</em></td>
      <td>Role برچسب نقش SELinux است که به کانتینر اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>type</code><br/><em>string</em></td>
      <td>Type برچسب نوع SELinux است که به کانتینر اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>User برچسب کاربر SELinux است که به کانتینر اعمال می‌شود.</td>
    </tr>
  </tbody>
</table>


## ScaleIOVolumeSource {#ScaleIOVolumeSource}

ScaleIOVolumeSource یک حجم پایدار ScaleIO را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید مانت شود. این نوع باید توسط سیستم‌عامل میزبان پشتیبانی شود. مثال: "ext4"، "xfs"، "ntfs". مقدار پیش‌فرض "xfs" است.</td>
    </tr>
    <tr>
      <td><code>gateway</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>gateway نشانی میزبان ScaleIO API Gateway است.</td>
    </tr>
    <tr>
      <td><code>protectionDomain</code><br/><em>string</em></td>
      <td>protectionDomain نام ScaleIO Protection Domain برای ذخیره‌سازی پیکربندی‌شده است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly به‌طور پیش‌فرض false است (خواندن/نوشتن). مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اجباری می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef به Secret حاوی کاربر ScaleIO و سایر اطلاعات حساس ارجاع می‌دهد. اگر این مقدار ارائه نشود، عملیات Login ناموفق خواهد بود.</td>
    </tr>
    <tr>
      <td><code>sslEnabled</code><br/><em>boolean</em></td>
      <td>sslEnabled پرچمی برای فعال یا غیرفعال کردن ارتباط SSL با Gateway است. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>storageMode</code><br/><em>string</em></td>
      <td>storageMode مشخص می‌کند که ذخیره‌سازی یک حجم به‌صورت ThickProvisioned یا ThinProvisioned تخصیص یابد. مقدار پیش‌فرض ThinProvisioned است.</td>
    </tr>
    <tr>
      <td><code>storagePool</code><br/><em>string</em></td>
      <td>storagePool همان ScaleIO Storage Pool مرتبط با protection domain است.</td>
    </tr>
    <tr>
      <td><code>system</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>system نام سیستم ذخیره‌سازی است که در ScaleIO پیکربندی شده است.</td>
    </tr>
    <tr>
      <td><code>volumeName</code><br/><em>string</em></td>
      <td>volumeName نام حجمی است که پیش‌تر در سیستم ScaleIO ایجاد شده و با این منبع حجم مرتبط است.</td>
    </tr>
  </tbody>
</table>


## SeccompProfile {#SeccompProfile}

SeccompProfile تنظیمات پروفایل seccomp یک Pod یا کانتینر را تعریف می‌کند. فقط یک منبع پروفایل را می‌توان تعیین کرد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>localhostProfile</code><br/><em>string</em></td>
      <td>localhostProfile نشان می‌دهد که باید از پروفایلی استفاده شود که در یک فایل روی نود تعریف شده است. برای کارکرد صحیح، پروفایل باید از قبل روی نود پیکربندی شده باشد. این مقدار باید یک مسیر نزولی و نسبت به مسیر پروفایل seccomp پیکربندی‌شده در kubelet باشد. اگر type برابر "Localhost" باشد، باید تنظیم شود و برای هر نوع دیگری نباید تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>type نشان می‌دهد کدام نوع پروفایل seccomp اعمال خواهد شد. گزینه‌های معتبر عبارت‌اند از:  Localhost - باید از پروفایلی استفاده شود که در یک فایل روی نود تعریف شده است. RuntimeDefault - باید از پروفایل پیش‌فرض محیط اجرای کانتینر استفاده شود. Unconfined - هیچ پروفایلی اعمال نشود.<br/><br/>مقادیر enum ممکن:<br/> - `"Localhost"` نشان می‌دهد که باید از پروفایلی استفاده شود که در یک فایل روی نود تعریف شده است. مسیر فایل نسبت به \<kubelet-root-dir>/seccomp است.<br/> - `"RuntimeDefault"` پروفایل seccomp پیش‌فرض محیط اجرای کانتینر را نشان می‌دهد.<br/> - `"Unconfined"` نشان می‌دهد که هیچ پروفایل seccomp اعمال نمی‌شود (که unconfined نیز نامیده می‌شود).</td>
    </tr>
  </tbody>
</table>


## SecretEnvSource {#SecretEnvSource}

SecretEnvSource یک Secret را برای مقداردهی متغیرهای محیطی انتخاب می‌کند.

محتوای فیلد Data در Secret هدف، جفت‌های کلید-مقدار را به‌صورت متغیرهای محیطی نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده. این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که مقدار این فیلد در آن‌ها خالی باشد، تقریباً حتماً نادرست‌اند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا تعریف Secret الزامی است یا خیر.</td>
    </tr>
  </tbody>
</table>


## SecretKeySelector {#SecretKeySelector}

SecretKeySelector یک کلید از Secret را انتخاب می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>کلید secret که باید انتخاب شود.  باید یک کلید معتبر secret باشد.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده. این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که مقدار این فیلد در آن‌ها خالی باشد، تقریباً حتماً نادرست‌اند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا تعریف Secret یا کلید آن الزامی است یا خیر.</td>
    </tr>
  </tbody>
</table>


## SecretProjection {#SecretProjection}

یک secret را به یک حجم projected تطبیق می‌دهد.

محتوای فیلد Data در Secret هدف در یک حجم projected به‌صورت فایل ارائه می‌شود و کلیدهای فیلد Data نام فایل‌ها خواهند بود. توجه کنید که این رفتار با منبع حجم secret بدون حالت پیش‌فرض (default mode) یکسان است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#KeyToPath" >}}">KeyToPath array</a></em></td>
      <td>items در صورت مشخص نشدن، هر جفت کلید-مقدار در فیلد Data از Secret ارجاع‌شده به‌صورت یک فایل در حجم projected می‌شود که نام آن کلید و محتوای آن مقدار است. در صورت تعیین، کلیدهای فهرست‌شده در مسیرهای مشخص‌شده projected می‌شوند و کلیدهای فهرست‌نشده وجود نخواهند داشت. اگر کلیدی مشخص شود که در Secret وجود ندارد، راه‌اندازی حجم با خطا مواجه می‌شود، مگر اینکه اختیاری علامت‌گذاری شده باشد. مسیرها باید نسبی باشند و نباید شامل مسیر '..' باشند یا با '..' شروع شوند.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده. این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی مجاز است خالی باشد. نمونه‌هایی از این نوع که مقدار این فیلد در آن‌ها خالی باشد، تقریباً حتماً نادرست‌اند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>فیلد optional مشخص می‌کند که آیا تعریف Secret یا کلید آن الزامی است یا خیر.</td>
    </tr>
  </tbody>
</table>

## SecretVolumeSource {#SecretVolumeSource}

یک Secret را به یک حجم (volume) تطبیق می‌دهد.

محتوای فیلد Data در Secret هدف، به‌صورت فایل در یک حجم ارائه می‌شود و کلیدهای فیلد Data به‌عنوان نام فایل‌ها استفاده می‌شوند. حجم‌های Secret از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>defaultMode</code><br/><em>integer</em></td>
      <td>defaultMode اختیاری است: بیت‌های حالت (mode) که به‌طور پیش‌فرض برای تنظیم مجوزهای فایل‌های ایجادشده استفاده می‌شوند. مقدار باید یک عدد در مبنای هشت بین 0000 و 0777 یا یک عدد در مبنای ده بین 0 و 511 باشد. YAML هر دو مقدار مبنای هشت و مبنای ده را می‌پذیرد، اما JSON برای بیت‌های حالت فقط مقدار مبنای ده را می‌پذیرد. مقدار پیش‌فرض 0644 است. دایرکتوری‌های درون مسیر تحت‌تأثیر این تنظیم قرار نمی‌گیرند. ممکن است این مقدار با گزینه‌های دیگری که بر حالت فایل اثر می‌گذارند، مانند fsGroup، تداخل داشته باشد و در نتیجه بیت‌های حالت دیگری تنظیم شوند.</td>
    </tr>
    <tr>
      <td><code>defaultUser</code><br/><em>integer</em></td>
      <td>defaultUser اختیاری است: شناسه UID مالک فایل‌های ایجادشده به‌صورت پیش‌فرض. فیلد defaultUser فقط زمانی به‌عنوان مقدار جایگزین استفاده می‌شود که فیلد user در سطح آیتم تنظیم نشده باشد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#KeyToPath" >}}">KeyToPath array</a></em></td>
      <td>items: اگر مشخص نشود، هر جفت کلید-مقدار در فیلد Data مربوط به Secret ارجاع‌شده به‌صورت یک فایل در حجم قرار می‌گیرد که نام آن کلید و محتوای آن مقدار است. اگر مشخص شود، کلیدهای فهرست‌شده در مسیرهای تعیین‌شده قرار می‌گیرند و کلیدهای فهرست‌نشده در حجم حضور نخواهند داشت. اگر کلیدی مشخص شود که در Secret وجود ندارد، راه‌اندازی حجم با خطا مواجه می‌شود، مگر آنکه به‌عنوان اختیاری (optional) علامت‌گذاری شده باشد. مسیرها باید نسبی باشند و نباید شامل مسیر '..' باشند یا با '..' شروع شوند.</td>
    </tr>
    <tr>
      <td><code>optional</code><br/><em>boolean</em></td>
      <td>فیلد optional مشخص می‌کند که آیا Secret یا کلیدهای آن باید تعریف شده باشند یا نه.</td>
    </tr>
    <tr>
      <td><code>secretName</code><br/><em>string</em></td>
      <td>secretName نام Secret موجود در فضای نام (namespace) پاد است که باید استفاده شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#secret</td>
    </tr>
  </tbody>
</table>


## SecurityContext {#SecurityContext}

SecurityContext پیکربندی امنیتی‌ای را در خود نگه می‌دارد که بر یک کانتینر اعمال می‌شود. برخی فیلدها هم در SecurityContext و هم در PodSecurityContext وجود دارند. وقتی هر دو تنظیم شده باشند، مقادیر SecurityContext اولویت دارند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowPrivilegeEscalation</code><br/><em>boolean</em></td>
      <td>AllowPrivilegeEscalation کنترل می‌کند که آیا یک فرایند می‌تواند امتیازهای بیشتری نسبت به فرایند والد خود به دست آورد یا نه. این مقدار بولی مستقیماً تعیین می‌کند که آیا پرچم no_new_privs روی فرایند کانتینر تنظیم شود یا خیر. اگر کانتینر 1) به‌صورت Privileged اجرا شود یا 2) دارای CAP_SYS_ADMIN باشد، مقدار AllowPrivilegeEscalation همیشه true است. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>appArmorProfile</code><br/><em><a href="{{< ref "#AppArmorProfile" >}}">AppArmorProfile</a></em></td>
      <td>appArmorProfile گزینه‌های AppArmor است که این کانتینر استفاده می‌کند. اگر تنظیم شود، این پروفایل بر appArmorProfile پاد غلبه می‌کند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>capabilities</code><br/><em><a href="{{< ref "#Capabilities" >}}">Capabilities</a></em></td>
      <td>قابلیت‌هایی (capabilities) که هنگام اجرای کانتینرها باید اضافه یا حذف شوند. مقدار پیش‌فرض مجموعه پیش‌فرض قابلیت‌هایی است که محیط اجرای کانتینر اعطا می‌کند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>privileged</code><br/><em>boolean</em></td>
      <td>کانتینر را در حالت privileged اجرا می‌کند. فرایندهای درون کانتینرهای privileged اساساً با کاربر root روی میزبان معادل هستند. مقدار پیش‌فرض false است. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>procMount</code><br/><em>string</em></td>
      <td>procMount نوع proc mount را که برای کانتینرها استفاده می‌شود تعیین می‌کند. مقدار پیش‌فرض Default است که برای مسیرهای فقط‌خواندنی و مسیرهای پوشانده‌شده (masked) از پیش‌فرض‌های محیط اجرای کانتینر استفاده می‌کند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.<br/><br/>مقادیر enum ممکن:<br/> - `"Default"` برای مسیرهای فقط‌خواندنی و پوشانده‌شده در /proc از پیش‌فرض‌های محیط اجرای کانتینر استفاده می‌کند. بیشتر محیط‌های اجرای کانتینر برخی مسیرهای /proc را می‌پوشانند تا از افشای تصادفی امنیتی دستگاه‌ها یا اطلاعات خاص جلوگیری کنند.<br/> - `"Unmasked"` رفتار پیش‌فرض پوشاندن در محیط اجرای کانتینر را دور می‌زند و تضمین می‌کند که /proc تازه‌ایجادشده برای کانتینر بدون هیچ تغییری دست‌نخورده باقی بماند.</td>
    </tr>
    <tr>
      <td><code>readOnlyRootFilesystem</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که آیا این کانتینر سامانه فایل ریشه فقط‌خواندنی دارد یا نه. مقدار پیش‌فرض false است. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>runAsGroup</code><br/><em>integer</em></td>
      <td>شناسه GID برای اجرای نقطه ورود (entrypoint) فرایند کانتینر. اگر تنظیم نشود، از مقدار پیش‌فرض محیط اجرا استفاده می‌شود. ممکن است در PodSecurityContext نیز تنظیم شود. اگر در هر دو SecurityContext و PodSecurityContext تنظیم شده باشد، مقدار مشخص‌شده در SecurityContext اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>runAsNonRoot</code><br/><em>boolean</em></td>
      <td>نشان می‌دهد که کانتینر باید با کاربری غیر از root اجرا شود. اگر true باشد، Kubelet ایمیج را هنگام اجرا بررسی می‌کند تا مطمئن شود با UID 0 (root) اجرا نمی‌شود، و در صورت اجرا با این شناسه، کانتینر را راه‌اندازی نمی‌کند. اگر تنظیم نشده یا false باشد، چنین بررسی‌ای انجام نخواهد شد. ممکن است در PodSecurityContext نیز تنظیم شود. اگر در هر دو SecurityContext و PodSecurityContext تنظیم شده باشد، مقدار مشخص‌شده در SecurityContext اولویت دارد.</td>
    </tr>
    <tr>
      <td><code>runAsUser</code><br/><em>integer</em></td>
      <td>شناسه UID برای اجرای نقطه ورود (entrypoint) فرایند کانتینر. اگر مشخص نشود، کاربر تعیین‌شده در فراداده ایمیج استفاده می‌شود. ممکن است در PodSecurityContext نیز تنظیم شود. اگر در هر دو SecurityContext و PodSecurityContext تنظیم شده باشد، مقدار مشخص‌شده در SecurityContext اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>seLinuxOptions</code><br/><em><a href="{{< ref "#SELinuxOptions" >}}">SELinuxOptions</a></em></td>
      <td>زمینه SELinux که باید بر کانتینر اعمال شود. اگر مشخص نشود، محیط اجرای کانتینر برای هر کانتینر یک زمینه SELinux تصادفی اختصاص می‌دهد. ممکن است در PodSecurityContext نیز تنظیم شود. اگر در هر دو SecurityContext و PodSecurityContext تنظیم شده باشد، مقدار مشخص‌شده در SecurityContext اولویت دارد. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>seccompProfile</code><br/><em><a href="{{< ref "#SeccompProfile" >}}">SeccompProfile</a></em></td>
      <td>گزینه‌های seccomp که این کانتینر استفاده می‌کند. اگر گزینه‌های seccomp هم در سطح پاد و هم در سطح کانتینر ارائه شوند، گزینه‌های کانتینر بر گزینه‌های پاد غلبه می‌کنند. توجه کنید که وقتی spec.os.name برابر windows باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
    <tr>
      <td><code>windowsOptions</code><br/><em><a href="{{< ref "#WindowsSecurityContextOptions" >}}">WindowsSecurityContextOptions</a></em></td>
      <td>تنظیمات مخصوص Windows که بر همه کانتینرها اعمال می‌شود. اگر مشخص نشود، گزینه‌های PodSecurityContext استفاده خواهند شد. اگر در هر دو SecurityContext و PodSecurityContext تنظیم شده باشد، مقدار مشخص‌شده در SecurityContext اولویت دارد. توجه کنید که وقتی spec.os.name برابر linux باشد، این فیلد قابل تنظیم نیست.</td>
    </tr>
  </tbody>
</table>


## ServiceAccountTokenProjection {#ServiceAccountTokenProjection}

ServiceAccountTokenProjection یک حجم توکن حساب سرویس (service account) از نوع projected را نشان می‌دهد. از این projection می‌توان برای درج توکن حساب سرویس در سامانه فایل زمان اجرای پاد استفاده کرد تا برای فراخوانی APIها (سرور API کوبرنتیز یا غیر آن) به کار رود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>audience</code><br/><em>string</em></td>
      <td>audience مخاطب مورد نظر توکن است. گیرنده یک توکن باید خود را با شناسه‌ای که در audience توکن مشخص شده معرفی کند، و در غیر این صورت باید توکن را رد کند. مقدار پیش‌فرض audience شناسه apiserver است.</td>
    </tr>
    <tr>
      <td><code>expirationSeconds</code><br/><em>integer</em></td>
      <td>expirationSeconds مدت اعتبار درخواست‌شده برای توکن حساب سرویس است. با نزدیک شدن توکن به زمان انقضا، افزونه حجم kubelet به‌صورت پیشگیرانه توکن حساب سرویس را چرخش (rotate) می‌دهد. kubelet زمانی تلاش برای چرخش توکن را آغاز می‌کند که عمر توکن از ۸۰ درصد مدت زمان حیات آن بیشتر شده باشد یا توکن بیش از ۲۴ ساعت از عمرش گذشته باشد. مقدار پیش‌فرض ۱ ساعت است و باید دست‌کم ۱۰ دقیقه باشد.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر فایلی است که توکن در آن قرار می‌گیرد و نسبت به نقطه اتصال (mount point) سنجیده می‌شود.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>integer</em></td>
      <td>user اختیاری است: شناسه UID مالک فایل ایجادشده. در صورت مشخص شدن، فیلد user در سطح آیتم بر defaultUser اولویت دارد. (آلفا) این فیلد نیازمند فعال بودن feature gate با نام AtomicWriteVolumeUserFields است.</td>
    </tr>
  </tbody>
</table>


## SleepAction {#SleepAction}

SleepAction یک اقدام «sleep» (انتظار) را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>seconds</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>Seconds تعداد ثانیه‌هایی است که باید منتظر ماند.</td>
    </tr>
  </tbody>
</table>


## StorageOSVolumeSource {#StorageOSVolumeSource}

یک منبع حجم پایدار StorageOS را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سامانه فایلی است که باید mount شود. باید نوع سامانه فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند؛ برای مثال "ext4"، "xfs" و "ntfs". اگر مشخص نشود، به‌صورت ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار پیش‌فرض readOnly برابر false (خواندنی/نوشتنی) است. تنظیم ReadOnly در اینجا، تنظیم ReadOnly در VolumeMounts را اجباری می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/local-object-reference-v1#LocalObjectReference" >}}">LocalObjectReference</a></em></td>
      <td>secretRef مشخص می‌کند که از کدام Secret برای دریافت اعتبارنامه‌های API مربوط به StorageOS استفاده شود. اگر مشخص نشود، از مقادیر پیش‌فرض استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>volumeName</code><br/><em>string</em></td>
      <td>volumeName نام قابل‌خواندن برای انسان حجم StorageOS است. نام حجم‌ها فقط درون یک فضای نام (namespace) یکتا است.</td>
    </tr>
    <tr>
      <td><code>volumeNamespace</code><br/><em>string</em></td>
      <td>volumeNamespace دامنه حجم را درون StorageOS مشخص می‌کند. اگر فضای نامی مشخص نشود، از فضای نام پاد استفاده می‌شود. این کار امکان می‌دهد دامنه‌بندی نام‌ها در کوبرنتیز درون StorageOS بازتاب یابد تا یکپارچگی بیشتری حاصل شود. برای نادیده گرفتن رفتار پیش‌فرض، VolumeName را روی هر نام دلخواهی تنظیم کنید. اگر درون StorageOS از فضای نام استفاده نمی‌کنید، مقدار را روی "default" تنظیم کنید. فضاهای نامی که از قبل در StorageOS وجود نداشته باشند ایجاد خواهند شد.</td>
    </tr>
  </tbody>
</table>


## Sysctl {#Sysctl}

Sysctl یک پارامتر هسته را که باید تنظیم شود تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام ویژگی‌ای که باید تنظیم شود</td>
    </tr>
    <tr>
      <td><code>value</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مقدار ویژگی‌ای که باید تنظیم شود</td>
    </tr>
  </tbody>
</table>


## TCPSocketAction {#TCPSocketAction}

TCPSocketAction اقدامی مبتنی بر باز کردن یک سوکت را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>host</code><br/><em>string</em></td>
      <td>اختیاری: نام میزبانی که باید به آن متصل شد. مقدار پیش‌فرض IP پاد است.</td>
    </tr>
    <tr>
      <td><code>port</code>&nbsp;<strong>*</strong><br/><em></em></td>
      <td>شماره یا نام پورتی که باید روی کانتینر به آن دسترسی پیدا کرد. شماره باید در بازه ۱ تا ۶۵۵۳۵ باشد. نام باید یک IANA_SVC_NAME باشد.</td>
    </tr>
  </tbody>
</table>

## TopologySpreadConstraint {#TopologySpreadConstraint}

TopologySpreadConstraint مشخص می‌کند که Podهای منطبق چگونه میان توپولوژی داده‌شده توزیع شوند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>labelSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>از LabelSelector برای یافتن Podهای منطبق استفاده می‌شود. Podهایی که با این انتخابگر برچسب مطابقت دارند شمارش می‌شوند تا تعداد Podها در دامنه توپولوژی متناظرشان تعیین شود.</td>
    </tr>
    <tr>
      <td><code>matchLabelKeys</code><br/><em>string array</em></td>
      <td>MatchLabelKeys مجموعه‌ای از کلیدهای برچسب Pod است که برای انتخاب Podهایی به کار می‌رود که توزیع بر اساس آن‌ها محاسبه می‌شود. از این کلیدها برای جست‌وجوی مقادیر در برچسب‌های Pod ورودی استفاده می‌شود و این جفت‌های کلید-مقدار با labelSelector به‌صورت AND ترکیب می‌شوند تا گروه Podهای موجودی که توزیع برای Pod ورودی روی آن‌ها محاسبه می‌شود انتخاب شود. وجود یک کلید یکسان هم در MatchLabelKeys و هم در LabelSelector ممنوع است. در صورتی که LabelSelector تنظیم نشده باشد، نمی‌توان MatchLabelKeys را تنظیم کرد. کلیدهایی که در برچسب‌های Pod ورودی وجود نداشته باشند نادیده گرفته می‌شوند. فهرست null یا خالی به این معناست که تنها با labelSelector مطابقت داده می‌شود.  این فیلد بتا است و نیاز دارد که feature gate با نام MatchLabelKeysInPodTopologySpread فعال باشد (به‌طور پیش‌فرض فعال است).</td>
    </tr>
    <tr>
      <td><code>maxSkew</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>MaxSkew میزان توزیع نامتوازن مجاز Podها را مشخص می‌کند. هنگامی که `whenUnsatisfiable=DoNotSchedule` باشد، این مقدار بیشینه اختلاف مجاز میان تعداد Podهای منطبق در توپولوژی هدف و کمینه سراسری است. کمینه سراسری، کمینه تعداد Podهای منطبق در یک دامنه واجد شرایط است، یا صفر در صورتی که تعداد دامنه‌های واجد شرایط کمتر از MinDomains باشد. برای مثال، در یک کلاستر با ۳ زون، MaxSkew برابر 1 است و Podهای دارای labelSelector یکسان به‌صورت 2/2/1 توزیع شده‌اند: در این حالت کمینه سراسری 1 است. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - اگر MaxSkew برابر 1 باشد، Pod ورودی فقط می‌تواند در zone3 زمان‌بندی شود تا توزیع به 2/2/2 برسد؛ زمان‌بندی آن در zone1 (یا zone2) باعث می‌شود ActualSkew(3-1) در zone1 (یا zone2) از MaxSkew(1) تخطی کند. - اگر MaxSkew برابر 2 باشد، Pod ورودی را می‌توان در هر زونی زمان‌بندی کرد. هنگامی که `whenUnsatisfiable=ScheduleAnyway` باشد، از این مقدار برای اولویت دادن به توپولوژی‌هایی استفاده می‌شود که آن را برآورده می‌کنند. این فیلد الزامی است. مقدار پیش‌فرض 1 است و مقدار 0 مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>minDomains</code><br/><em>integer</em></td>
      <td>MinDomains کمینه تعداد دامنه‌های واجد شرایط را مشخص می‌کند. هنگامی که تعداد دامنه‌های واجد شرایط با کلیدهای توپولوژی منطبق کمتر از minDomains باشد، Pod Topology Spread «کمینه سراسری» را 0 در نظر می‌گیرد و سپس Skew را محاسبه می‌کند. هنگامی که تعداد دامنه‌های واجد شرایط با کلیدهای توپولوژی منطبق برابر یا بیشتر از minDomains باشد، این مقدار بر زمان‌بندی تأثیری ندارد. در نتیجه، وقتی تعداد دامنه‌های واجد شرایط کمتر از minDomains باشد، زمان‌بند بیش از maxSkew عدد Pod را در آن دامنه‌ها زمان‌بندی نمی‌کند. اگر مقدار nil باشد، قید به‌گونه‌ای رفتار می‌کند که گویی MinDomains برابر 1 است. مقادیر معتبر، اعداد صحیح بزرگ‌تر از 0 هستند. هنگامی که مقدار nil نباشد، WhenUnsatisfiable باید DoNotSchedule باشد.  برای مثال، در یک کلاستر با ۳ زون، MaxSkew برابر 2 و MinDomains برابر 5 است و Podهای دارای labelSelector یکسان به‌صورت 2/2/2 توزیع شده‌اند: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | تعداد دامنه‌ها کمتر از 5 (MinDomains) است، بنابراین «کمینه سراسری» برابر 0 در نظر گرفته می‌شود. در این وضعیت، Pod جدید با labelSelector یکسان را نمی‌توان زمان‌بندی کرد، زیرا اگر Pod جدید در هر یک از سه زون زمان‌بندی شود، skew محاسبه‌شده 3 (3 - 0) خواهد بود و از MaxSkew تخطی می‌کند.</td>
    </tr>
    <tr>
      <td><code>nodeAffinityPolicy</code><br/><em>string</em></td>
      <td>NodeAffinityPolicy مشخص می‌کند که هنگام محاسبه skew توزیع توپولوژی Pod، با nodeAffinity/nodeSelector مربوط به Pod چگونه رفتار شود. گزینه‌ها عبارت‌اند از: - Honor: فقط نودهایی که با nodeAffinity/nodeSelector مطابقت دارند در محاسبات لحاظ می‌شوند. - Ignore: nodeAffinity/nodeSelector نادیده گرفته می‌شوند و همه نودها در محاسبات لحاظ می‌شوند.  اگر این مقدار nil باشد، رفتار معادل سیاست Honor است.<br/><br/>مقادیر enum ممکن:<br/> - `"Honor"` به این معناست که هنگام محاسبه skew توزیع توپولوژی Pod از این دستورالعمل زمان‌بندی استفاده شود.<br/> - `"Ignore"` به این معناست که هنگام محاسبه skew توزیع توپولوژی Pod این دستورالعمل زمان‌بندی نادیده گرفته شود.</td>
    </tr>
    <tr>
      <td><code>nodeTaintsPolicy</code><br/><em>string</em></td>
      <td>NodeTaintsPolicy مشخص می‌کند که هنگام محاسبه skew توزیع توپولوژی Pod، با taintهای نود چگونه رفتار شود. گزینه‌ها عبارت‌اند از: - Honor: نودهای بدون taint، به‌همراه نودهای دارای taint که Pod ورودی برای آن‌ها toleration دارد، لحاظ می‌شوند. - Ignore: taintهای نود نادیده گرفته می‌شوند و همه نودها لحاظ می‌شوند.  اگر این مقدار nil باشد، رفتار معادل سیاست Ignore است.<br/><br/>مقادیر enum ممکن:<br/> - `"Honor"` به این معناست که هنگام محاسبه skew توزیع توپولوژی Pod از این دستورالعمل زمان‌بندی استفاده شود.<br/> - `"Ignore"` به این معناست که هنگام محاسبه skew توزیع توپولوژی Pod این دستورالعمل زمان‌بندی نادیده گرفته شود.</td>
    </tr>
    <tr>
      <td><code>topologyKey</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>TopologyKey کلید برچسب‌های نود است. نودهایی که برچسبی با این کلید و مقادیر یکسان دارند، در یک توپولوژی قرار دارند. هر \<key, value> یک «سطل» (bucket) در نظر گرفته می‌شود و تلاش می‌شود تعداد متوازنی از Podها در هر سطل قرار گیرد. دامنه (domain) را نمونه‌ای مشخص از یک توپولوژی تعریف می‌کنیم. همچنین دامنه واجد شرایط را دامنه‌ای تعریف می‌کنیم که نودهای آن الزامات nodeAffinityPolicy و nodeTaintsPolicy را برآورده کنند. برای مثال، اگر TopologyKey برابر "kubernetes.io/hostname" باشد، هر Node یک دامنه از آن توپولوژی است. و اگر TopologyKey برابر "topology.kubernetes.io/zone" باشد، هر زون یک دامنه از آن توپولوژی است. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>whenUnsatisfiable</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>WhenUnsatisfiable مشخص می‌کند در صورتی که Pod قید توزیع را برآورده نکند، با آن چگونه رفتار شود. - DoNotSchedule (پیش‌فرض) به زمان‌بند می‌گوید آن را زمان‌بندی نکند. - ScheduleAnyway به زمان‌بند می‌گوید Pod را در هر مکانی زمان‌بندی کند، اما به توپولوژی‌هایی که به کاهش skew کمک می‌کنند اولویت بالاتری بدهد. قید برای یک Pod ورودی «Unsatisfiable» (ناپذیرفتنی) در نظر گرفته می‌شود، اگر و تنها اگر هر تخصیص ممکن نود برای آن Pod، «MaxSkew» را در یک توپولوژی نقض کند. برای مثال، در یک کلاستر با ۳ زون، MaxSkew برابر 1 است و Podهای دارای labelSelector یکسان به‌صورت 3/1/1 توزیع شده‌اند: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | اگر WhenUnsatisfiable روی DoNotSchedule تنظیم شده باشد، Pod ورودی فقط می‌تواند در zone2 (یا zone3) زمان‌بندی شود تا توزیع به 3/2/1 (یا 3/1/2) برسد، زیرا ActualSkew(2-1) در zone2 (یا zone3) شرط MaxSkew(1) را برآورده می‌کند. به بیان دیگر، کلاستر همچنان می‌تواند نامتوازن باشد، اما زمان‌بند آن را *نامتوازن‌تر* نمی‌کند. این فیلد الزامی است.<br/><br/>مقادیر enum ممکن:<br/> - `"DoNotSchedule"` به زمان‌بند دستور می‌دهد در صورت برآورده نشدن قیدها، Pod را زمان‌بندی نکند.<br/> - `"ScheduleAnyway"` به زمان‌بند دستور می‌دهد حتی در صورت برآورده نشدن قیدها، Pod را زمان‌بندی کند.</td>
    </tr>
  </tbody>
</table>

## Volume {#Volume}

Volume یک حجم (volume) نام‌دار را در یک pod نشان می‌دهد که هر کانتینر درون آن pod می‌تواند به آن دسترسی داشته باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>awsElasticBlockStore</code><br/><em><a href="{{< ref "persistent-volume-v1#AWSElasticBlockStoreVolumeSource" >}}">AWSElasticBlockStoreVolumeSource</a></em></td>
      <td>awsElasticBlockStore یک منبع AWS Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل شده و سپس در اختیار pod قرار می‌گیرد. منسوخ‌شده: AWSElasticBlockStore منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت (in-tree) awsElasticBlockStore به درایور CSI با نام ebs.csi.aws.com هدایت می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</td>
    </tr>
    <tr>
      <td><code>azureDisk</code><br/><em><a href="{{< ref "persistent-volume-v1#AzureDiskVolumeSource" >}}">AzureDiskVolumeSource</a></em></td>
      <td>azureDisk یک Azure Data Disk را نشان می‌دهد که روی میزبان مونت شده و به‌صورت bind mount به pod متصل می‌شود. منسوخ‌شده: AzureDisk منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت azureDisk به درایور CSI با نام disk.csi.azure.com هدایت می‌شود.</td>
    </tr>
    <tr>
      <td><code>azureFile</code><br/><em><a href="{{< ref "#AzureFileVolumeSource" >}}">AzureFileVolumeSource</a></em></td>
      <td>azureFile یک Azure File Service را نشان می‌دهد که روی میزبان مونت شده و به‌صورت bind mount به pod متصل می‌شود. منسوخ‌شده: AzureFile منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت azureFile به درایور CSI با نام file.csi.azure.com هدایت می‌شود.</td>
    </tr>
    <tr>
      <td><code>cephfs</code><br/><em><a href="{{< ref "#CephFSVolumeSource" >}}">CephFSVolumeSource</a></em></td>
      <td>cephFS یک Ceph FS را نشان می‌دهد که روی میزبان مونت شده و هم‌عمر با pod است. منسوخ‌شده: CephFS منسوخ شده و نوع درون‌درخت cephfs دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>cinder</code><br/><em><a href="{{< ref "#CinderVolumeSource" >}}">CinderVolumeSource</a></em></td>
      <td>cinder یک حجم cinder را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن مونت شده است. منسوخ‌شده: Cinder منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت cinder به درایور CSI با نام cinder.csi.openstack.org هدایت می‌شود. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>configMap</code><br/><em><a href="{{< ref "#ConfigMapVolumeSource" >}}">ConfigMapVolumeSource</a></em></td>
      <td>configMap یک configMap را نشان می‌دهد که باید محتوای این حجم را تأمین کند.</td>
    </tr>
    <tr>
      <td><code>csi</code><br/><em><a href="{{< ref "#CSIVolumeSource" >}}">CSIVolumeSource</a></em></td>
      <td>csi (Container Storage Interface) ذخیره‌سازی موقتی را نشان می‌دهد که برخی درایورهای CSI خارجی آن را مدیریت می‌کنند.</td>
    </tr>
    <tr>
      <td><code>downwardAPI</code><br/><em><a href="{{< ref "#DownwardAPIVolumeSource" >}}">DownwardAPIVolumeSource</a></em></td>
      <td>downwardAPI اطلاعات downward API مربوط به pod را نشان می‌دهد که باید محتوای این حجم را تأمین کند.</td>
    </tr>
    <tr>
      <td><code>emptyDir</code><br/><em><a href="{{< ref "#EmptyDirVolumeSource" >}}">EmptyDirVolumeSource</a></em></td>
      <td>emptyDir یک دایرکتوری موقت را نشان می‌دهد که هم‌عمر با pod است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#emptydir</td>
    </tr>
    <tr>
      <td><code>ephemeral</code><br/><em><a href="{{< ref "#EphemeralVolumeSource" >}}">EphemeralVolumeSource</a></em></td>
      <td>ephemeral حجمی را نشان می‌دهد که یک درایور ذخیره‌سازی کلاستر آن را مدیریت می‌کند. چرخه عمر این حجم به pod تعریف‌کننده آن وابسته است: حجم پیش از شروع pod ایجاد می‌شود و با حذف pod پاک می‌شود. در این موارد از آن استفاده کنید: الف) حجم فقط در مدت اجرای pod لازم باشد، ب) قابلیت‌های حجم‌های معمولی مانند بازیابی از snapshot یا ردیابی ظرفیت لازم باشد، ج) درایور ذخیره‌سازی از طریق یک storage class مشخص شده باشد و د) درایور ذخیره‌سازی از تأمین پویای حجم از طریق PersistentVolumeClaim پشتیبانی کند (برای اطلاعات بیشتر درباره ارتباط این نوع حجم با PersistentVolumeClaim به EphemeralVolumeSource مراجعه کنید). برای حجم‌هایی که بیش از چرخه عمر یک pod منفرد باقی می‌مانند، از PersistentVolumeClaim یا یکی از APIهای اختصاصی فروشندگان استفاده کنید. اگر قرار است درایور CSI برای حجم‌های موقتی محلی سبک به کار رود، از CSI استفاده کنید؛ برای اطلاعات بیشتر مستندات آن درایور را ببینید. یک pod می‌تواند هر دو نوع حجم موقتی و حجم پایدار را هم‌زمان به کار ببرد.</td>
    </tr>
    <tr>
      <td><code>fc</code><br/><em><a href="{{< ref "persistent-volume-v1#FCVolumeSource" >}}">FCVolumeSource</a></em></td>
      <td>fc یک منبع Fibre Channel را نشان می‌دهد که به ماشین میزبان kubelet متصل شده و سپس در اختیار pod قرار می‌گیرد.</td>
    </tr>
    <tr>
      <td><code>flexVolume</code><br/><em><a href="{{< ref "#FlexVolumeSource" >}}">FlexVolumeSource</a></em></td>
      <td>flexVolume یک منبع حجم عمومی را نشان می‌دهد که با یک افزونه مبتنی بر exec تأمین یا متصل می‌شود. منسوخ‌شده: FlexVolume منسوخ شده است. به‌جای آن از CSIDriver استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>flocker</code><br/><em><a href="{{< ref "persistent-volume-v1#FlockerVolumeSource" >}}">FlockerVolumeSource</a></em></td>
      <td>flocker یک حجم Flocker را نشان می‌دهد که به ماشین میزبان kubelet متصل شده است. این حجم به اجرای سرویس کنترل Flocker وابسته است. منسوخ‌شده: Flocker منسوخ شده و نوع درون‌درخت flocker دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>gcePersistentDisk</code><br/><em><a href="{{< ref "persistent-volume-v1#GCEPersistentDiskVolumeSource" >}}">GCEPersistentDiskVolumeSource</a></em></td>
      <td>gcePersistentDisk یک منبع GCE Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل شده و سپس در اختیار pod قرار می‌گیرد. منسوخ‌شده: GCEPersistentDisk منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت gcePersistentDisk به درایور CSI با نام pd.csi.storage.gke.io هدایت می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
    <tr>
      <td><code>gitRepo</code><br/><em><a href="{{< ref "#GitRepoVolumeSource" >}}">GitRepoVolumeSource</a></em></td>
      <td>gitRepo یک مخزن git را در یک نسخه (revision) مشخص نشان می‌دهد. منسوخ‌شده: GitRepo منسوخ شده است. برای فراهم کردن مخزن git در یک کانتینر، یک EmptyDir را به یک InitContainer مونت کنید که مخزن را با git کلون می‌کند، سپس همان EmptyDir را به کانتینر Pod مونت کنید.</td>
    </tr>
    <tr>
      <td><code>glusterfs</code><br/><em><a href="{{< ref "#GlusterfsVolumeSource" >}}">GlusterfsVolumeSource</a></em></td>
      <td>glusterfs یک Glusterfs را نشان می‌دهد که روی میزبان مونت شده و هم‌عمر با pod است. منسوخ‌شده: Glusterfs منسوخ شده و نوع درون‌درخت glusterfs دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>hostPath</code><br/><em><a href="{{< ref "persistent-volume-v1#HostPathVolumeSource" >}}">HostPathVolumeSource</a></em></td>
      <td>hostPath یک فایل یا دایرکتوری از پیش موجود روی ماشین میزبان را نشان می‌دهد که مستقیماً در اختیار کانتینر قرار می‌گیرد. این نوع حجم معمولاً برای عامل‌های سیستمی یا سایر مواردی به کار می‌رود که دارای سطح دسترسی ویژه‌اند و مجاز به مشاهده ماشین میزبان هستند. بیشتر کانتینرها به آن نیازی ندارند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#hostpath</td>
    </tr>
    <tr>
      <td><code>image</code><br/><em><a href="{{< ref "#ImageVolumeSource" >}}">ImageVolumeSource</a></em></td>
      <td>image یک آبجکت OCI (ایمیج کانتینر یا artifact) را نشان می‌دهد که روی ماشین میزبان kubelet دریافت و مونت می‌شود. این حجم هنگام شروع pod و بسته به مقدار PullPolicy تعیین‌شده resolve می‌شود:  - Always: kubelet همیشه تلاش می‌کند مرجع را دریافت کند. اگر دریافت ناموفق باشد، ایجاد کانتینر نیز شکست می‌خورد. - Never: kubelet هرگز مرجع را دریافت نمی‌کند و فقط از ایمیج یا artifact محلی استفاده می‌کند. اگر مرجع موجود نباشد، ایجاد کانتینر شکست می‌خورد. - IfNotPresent: kubelet فقط در صورتی مرجع را دریافت می‌کند که روی دیسک موجود نباشد. اگر مرجع موجود نباشد و دریافت آن ناموفق باشد، ایجاد کانتینر شکست می‌خورد.  اگر pod حذف و دوباره ایجاد شود، حجم دوباره resolve می‌شود؛ یعنی محتوای راه دور جدید با ایجاد مجدد pod در دسترس قرار می‌گیرد. شکست در resolve یا دریافت ایمیج هنگام شروع pod مانع از شروع کانتینرها می‌شود و ممکن است تأخیر قابل‌توجهی ایجاد کند. تلاش مجدد برای این خطاها با backoff معمول حجم انجام می‌شود و خطا در reason و message مربوط به pod گزارش می‌شود. انواع آبجکت‌هایی که این حجم می‌تواند مونت کند را پیاده‌سازی محیط اجرای کانتینر روی ماشین میزبان تعیین می‌کند و دست‌کم باید همه انواع معتبر پشتیبانی‌شده توسط فیلد ایمیج کانتینر را شامل شود. آبجکت OCI با ادغام لایه‌های مانیفست، به همان روشی که برای ایمیج‌های کانتینر انجام می‌شود، در یک دایرکتوری واحد (spec.containers[*].volumeMounts.mountPath) مونت می‌شود. این حجم به‌صورت فقط‌خواندنی (ro) مونت می‌شود. پیش از نسخه 1.33، مونت مسیر فرعی (sub path) برای کانتینرها پشتیبانی نمی‌شود (spec.containers[*].volumeMounts.subpath). فیلد spec.securityContext.fsGroupChangePolicy روی این نوع حجم تأثیری ندارد.</td>
    </tr>
    <tr>
      <td><code>iscsi</code><br/><em><a href="{{< ref "#ISCSIVolumeSource" >}}">ISCSIVolumeSource</a></em></td>
      <td>iscsi یک منبع ISCSI Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل شده و سپس در اختیار pod قرار می‌گیرد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes/#iscsi</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام حجم است. باید یک DNS_LABEL باشد و در سطح pod یکتا باشد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
    <tr>
      <td><code>nfs</code><br/><em><a href="{{< ref "persistent-volume-v1#NFSVolumeSource" >}}">NFSVolumeSource</a></em></td>
      <td>nfs یک NFS را نشان می‌دهد که روی میزبان مونت شده و هم‌عمر با pod است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#nfs</td>
    </tr>
    <tr>
      <td><code>persistentVolumeClaim</code><br/><em><a href="{{< ref "#PersistentVolumeClaimVolumeSource" >}}">PersistentVolumeClaimVolumeSource</a></em></td>
      <td>persistentVolumeClaimVolumeSource ارجاعی به یک PersistentVolumeClaim در همان فضای نام (namespace) را نشان می‌دهد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims</td>
    </tr>
    <tr>
      <td><code>photonPersistentDisk</code><br/><em><a href="{{< ref "persistent-volume-v1#PhotonPersistentDiskVolumeSource" >}}">PhotonPersistentDiskVolumeSource</a></em></td>
      <td>photonPersistentDisk یک دیسک پایدار PhotonController را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن مونت شده است. منسوخ‌شده: PhotonPersistentDisk منسوخ شده و نوع درون‌درخت photonPersistentDisk دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>portworxVolume</code><br/><em><a href="{{< ref "persistent-volume-v1#PortworxVolumeSource" >}}">PortworxVolumeSource</a></em></td>
      <td>portworxVolume یک حجم portworx را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن مونت شده است. منسوخ‌شده: PortworxVolume منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت portworxVolume به درایور CSI با نام pxd.portworx.com هدایت می‌شود.</td>
    </tr>
    <tr>
      <td><code>projected</code><br/><em><a href="{{< ref "#ProjectedVolumeSource" >}}">ProjectedVolumeSource</a></em></td>
      <td>projected مجموعه‌ای از منابع secrets، configmaps و downward API را در قالب یک حجم واحد ارائه می‌کند.</td>
    </tr>
    <tr>
      <td><code>quobyte</code><br/><em><a href="{{< ref "persistent-volume-v1#QuobyteVolumeSource" >}}">QuobyteVolumeSource</a></em></td>
      <td>quobyte یک Quobyte را نشان می‌دهد که روی میزبان مونت شده و هم‌عمر با pod است. منسوخ‌شده: Quobyte منسوخ شده و نوع درون‌درخت quobyte دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>rbd</code><br/><em><a href="{{< ref "#RBDVolumeSource" >}}">RBDVolumeSource</a></em></td>
      <td>rbd یک Rados Block Device را نشان می‌دهد که روی میزبان مونت شده و هم‌عمر با pod است. منسوخ‌شده: RBD منسوخ شده و نوع درون‌درخت rbd دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>scaleIO</code><br/><em><a href="{{< ref "#ScaleIOVolumeSource" >}}">ScaleIOVolumeSource</a></em></td>
      <td>scaleIO یک حجم پایدار ScaleIO را نشان می‌دهد که به نودهای کوبرنتیز متصل و روی آن‌ها مونت شده است. منسوخ‌شده: ScaleIO منسوخ شده و نوع درون‌درخت scaleIO دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>secret</code><br/><em><a href="{{< ref "#SecretVolumeSource" >}}">SecretVolumeSource</a></em></td>
      <td>secret یک secret را نشان می‌دهد که باید محتوای این حجم را تأمین کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#secret</td>
    </tr>
    <tr>
      <td><code>storageos</code><br/><em><a href="{{< ref "#StorageOSVolumeSource" >}}">StorageOSVolumeSource</a></em></td>
      <td>storageOS یک حجم StorageOS را نشان می‌دهد که به نودهای کوبرنتیز متصل و روی آن‌ها مونت شده است. منسوخ‌شده: StorageOS منسوخ شده و نوع درون‌درخت storageos دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>vsphereVolume</code><br/><em><a href="{{< ref "persistent-volume-v1#VsphereVirtualDiskVolumeSource" >}}">VsphereVirtualDiskVolumeSource</a></em></td>
      <td>vsphereVolume یک حجم vSphere را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن مونت شده است. منسوخ‌شده: VsphereVolume منسوخ شده است. تمام عملیات مربوط به نوع درون‌درخت vsphereVolume به درایور CSI با نام csi.vsphere.vmware.com هدایت می‌شود.</td>
    </tr>
  </tbody>
</table>


## VolumeDevice {#VolumeDevice}

volumeDevice نگاشت یک دستگاه بلاکی خام (raw block device) را درون یک کانتینر توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>devicePath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>devicePath مسیری درون کانتینر است که دستگاه به آن نگاشت می‌شود.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name باید با نام یکی از persistentVolumeClaimهای pod مطابقت داشته باشد.</td>
    </tr>
  </tbody>
</table>


## VolumeMount {#VolumeMount}

VolumeMount مونت شدن یک Volume را درون یک کانتینر توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>bindMountOptions</code><br/><em>string array</em></td>
      <td>bindMountOptions فهرست گزینه‌های اضافی bind mount است که هنگام مونت این حجم درون کانتینر اعمال می‌شوند. مقادیر مجاز noexec، nodev و nosuid هستند. این‌ها گزینه‌های مونت در لینوکس هستند و روی نودهای ویندوز تأثیری ندارند. این فیلد برای حجم‌های image پشتیبانی نمی‌شود. این فیلد آلفا است و برای استفاده از آن باید feature gate با نام VolumeBindMountOptions فعال شود.</td>
    </tr>
    <tr>
      <td><code>mountPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>مسیر درون کانتینر که حجم باید در آن مونت شود.</td>
    </tr>
    <tr>
      <td><code>mountPropagation</code><br/><em>string</em></td>
      <td>mountPropagation تعیین می‌کند مونت‌ها چگونه از میزبان به کانتینر و برعکس منتشر شوند. اگر مقداردهی نشود، از MountPropagationNone استفاده می‌شود. این فیلد در نسخه 1.10 بتا است. هنگامی که RecursiveReadOnly روی IfPossible یا Enabled تنظیم شده باشد، MountPropagation باید None یا نامشخص باشد (که به‌طور پیش‌فرض None در نظر گرفته می‌شود).<br/><br/>مقادیر ممکن enum:<br/> - `"Bidirectional"` یعنی حجم درون کانتینر مونت‌های جدید را از میزبان یا کانتینرهای دیگر دریافت می‌کند و مونت‌های خودش نیز از کانتینر به میزبان یا کانتینرهای دیگر منتشر می‌شود. توجه کنید که این حالت به‌صورت بازگشتی روی همه مونت‌های درون حجم اعمال می‌شود (در اصطلاح لینوکس: "rshared").<br/> - `"HostToContainer"` یعنی حجم درون کانتینر مونت‌های جدید را از میزبان یا کانتینرهای دیگر دریافت می‌کند، اما فایل‌سیستم‌هایی که درون کانتینر مونت می‌شوند به میزبان یا کانتینرهای دیگر منتشر نمی‌شوند. توجه کنید که این حالت به‌صورت بازگشتی روی همه مونت‌های درون حجم اعمال می‌شود (در اصطلاح لینوکس: "rslave").<br/> - `"None"` یعنی حجم درون کانتینر مونت‌های جدید را از میزبان یا کانتینرهای دیگر دریافت نمی‌کند و فایل‌سیستم‌هایی که درون کانتینر مونت می‌شوند نیز به میزبان یا کانتینرهای دیگر منتشر نمی‌شوند. توجه کنید که این حالت معادل "private" در اصطلاح لینوکس است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>این مقدار باید با Name یکی از Volumeها مطابقت داشته باشد.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>اگر true باشد، مونت به‌صورت فقط‌خواندنی انجام می‌شود؛ در غیر این صورت (false یا نامشخص) خواندنی-نوشتنی است. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>recursiveReadOnly</code><br/><em>string</em></td>
      <td>RecursiveReadOnly مشخص می‌کند که آیا مونت‌های فقط‌خواندنی باید به‌صورت بازگشتی مدیریت شوند یا خیر.  اگر ReadOnly برابر false باشد، این فیلد بی‌معنی است و باید نامشخص بماند.  اگر ReadOnly برابر true باشد و این فیلد روی Disabled تنظیم شده باشد، مونت به‌صورت بازگشتی فقط‌خواندنی نمی‌شود.  اگر این فیلد روی IfPossible تنظیم شده باشد، در صورتی که محیط اجرای کانتینر از آن پشتیبانی کند، مونت به‌صورت بازگشتی فقط‌خواندنی می‌شود.  اگر این فیلد روی Enabled تنظیم شده باشد، در صورتی که محیط اجرای کانتینر از آن پشتیبانی کند، مونت به‌صورت بازگشتی فقط‌خواندنی می‌شود؛ در غیر این صورت pod شروع نمی‌شود و خطایی برای بیان علت تولید می‌شود.  اگر این فیلد روی IfPossible یا Enabled تنظیم شده باشد، MountPropagation باید روی None تنظیم شود (یا نامشخص باشد که به‌طور پیش‌فرض None در نظر گرفته می‌شود).  اگر این فیلد مشخص نشود، معادل Disabled در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>subPath</code><br/><em>string</em></td>
      <td>مسیر درون حجم که حجم کانتینر باید از آن مونت شود. مقدار پیش‌فرض "" است (ریشه حجم).</td>
    </tr>
    <tr>
      <td><code>subPathExpr</code><br/><em>string</em></td>
      <td>مسیر گسترش‌یافته درون حجم که حجم کانتینر باید از آن مونت شود. رفتار آن مشابه SubPath است، با این تفاوت که ارجاع‌های متغیر محیطی $(VAR_NAME) با استفاده از محیط کانتینر گسترش داده می‌شوند. مقدار پیش‌فرض "" است (ریشه حجم). SubPathExpr و SubPath با یکدیگر ناسازگارند و نمی‌توان هم‌زمان از هر دو استفاده کرد.</td>
    </tr>
  </tbody>
</table>

## VolumeProjection {#VolumeProjection}

پروجکشنی که می‌توان آن را همراه با سایر انواع حجم (volume) پشتیبانی‌شده پروجکت کرد. دقیقاً یکی از این فیلدها باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>clusterTrustBundle</code><br/><em><a href="{{< ref "#ClusterTrustBundleProjection" >}}">ClusterTrustBundleProjection</a></em></td>
      <td>ClusterTrustBundle به یک Pod اجازه می‌دهد فیلد `.spec.trustBundle` آبجکت‌های ClusterTrustBundle را در یک فایل با به‌روزرسانی خودکار در اختیار داشته باشد. این قابلیت آلفا است و با feature gate با نام ClusterTrustBundleProjection کنترل می‌شود. آبجکت‌های ClusterTrustBundle را می‌توان بر اساس نام، یا با ترکیب نام signer و یک انتخابگر برچسب (label selector) انتخاب کرد. Kubelet محتوای PEM نوشته‌شده در فایل‌سیستم Pod را به‌شدت نرمال‌سازی می‌کند. ویژگی‌های نامعمول PEM، مانند توضیحات میان بلوک‌ها و سرایندهای بلوک، حذف می‌شوند. گواهی‌های تکراری نیز حذف می‌شوند. ترتیب گواهی‌ها در فایل دلخواه است و Kubelet ممکن است آن را در طول زمان تغییر دهد.</td>
    </tr>
    <tr>
      <td><code>configMap</code><br/><em><a href="{{< ref "#ConfigMapProjection" >}}">ConfigMapProjection</a></em></td>
      <td>اطلاعات configMap درباره داده‌های configMap که باید پروجکت شوند</td>
    </tr>
    <tr>
      <td><code>downwardAPI</code><br/><em><a href="{{< ref "#DownwardAPIProjection" >}}">DownwardAPIProjection</a></em></td>
      <td>اطلاعات downwardAPI درباره داده‌های downwardAPI که باید پروجکت شوند</td>
    </tr>
    <tr>
      <td><code>podCertificate</code><br/><em><a href="{{< ref "#PodCertificateProjection" >}}">PodCertificateProjection</a></em></td>
      <td>یک بسته اعتبارنامه با چرخش خودکار (کلید خصوصی و زنجیره گواهی) را پروجکت می‌کند که Pod می‌تواند آن را چه به‌عنوان کلاینت TLS و چه به‌عنوان سرور TLS به کار ببرد. Kubelet یک کلید خصوصی تولید می‌کند و با آن یک PodCertificateRequest را برای signer مشخص‌شده ارسال می‌کند. پس از آنکه signer درخواست را تأیید کند و زنجیره گواهی را صادر کند، Kubelet کلید و زنجیره گواهی را در فایل‌سیستم Pod می‌نویسد. Pod شروع به کار نمی‌کند، مگر آنکه برای هر منبع حجم podCertificate پروجکت‌شده در spec آن گواهی صادر شده باشد. Kubelet در زمانی که signer از طریق مهر زمانی PodCertificateRequest.Status.BeginRefreshAt اعلام کرده است، تلاش برای چرخش گواهی را آغاز می‌کند. Kubelet می‌تواند یک فایل واحد را که با فیلد credentialBundlePath مشخص می‌شود، یا فایل‌های جداگانه را که با فیلدهای keyPath و certificateChainPath مشخص می‌شوند، بنویسد. بسته اعتبارنامه یک فایل واحد با قالب PEM است. نخستین ورودی PEM کلید خصوصی (با قالب PKCS#8) و ورودی‌های PEM باقی‌مانده زنجیره گواهی صادرشده توسط signer هستند (معمولاً signerها زنجیره گواهی خود را به ترتیب از برگ به ریشه برمی‌گردانند). استفاده از قالب بسته اعتبارنامه ترجیح داده می‌شود، زیرا کد برنامه شما می‌تواند آن را به‌صورت اتمیک بخواند. اگر از keyPath و certificateChainPath استفاده کنید، برنامه شما باید دو خواندن جداگانه از فایل انجام دهد. اگر این خواندن‌ها با چرخش گواهی هم‌زمان شوند، ممکن است کلید خصوصی و گواهی برگی که خوانده‌اید با یکدیگر متناظر نباشند. برنامه شما باید این وضعیت را بررسی کند و تا زمانی که داده‌ها سازگار شوند، دوباره بخواند. قالب گواهی صادرشده را signer مشخص‌شده تعیین می‌کند؛ برای آگاهی از نحوه استفاده از گواهی‌های صادرشده، به مستندات پیاده‌سازی آن signer مراجعه کنید.</td>
    </tr>
    <tr>
      <td><code>secret</code><br/><em><a href="{{< ref "#SecretProjection" >}}">SecretProjection</a></em></td>
      <td>اطلاعات secret درباره داده‌های secret که باید پروجکت شوند</td>
    </tr>
    <tr>
      <td><code>serviceAccountToken</code><br/><em><a href="{{< ref "#ServiceAccountTokenProjection" >}}">ServiceAccountTokenProjection</a></em></td>
      <td>serviceAccountToken اطلاعاتی درباره داده‌های serviceAccountToken است که باید پروجکت شوند</td>
    </tr>
  </tbody>
</table>


## WeightedPodAffinityTerm {#WeightedPodAffinityTerm}

وزن تمام فیلدهای WeightedPodAffinityTerm منطبق، به‌ازای هر نود با هم جمع می‌شود تا ترجیح‌داده‌شده‌ترین نود (یا نودها) پیدا شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>podAffinityTerm</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#PodAffinityTerm" >}}">PodAffinityTerm</a></em></td>
      <td>الزامی. یک podAffinityTerm که با وزن متناظر مرتبط است.</td>
    </tr>
    <tr>
      <td><code>weight</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>وزن مرتبط با تطابق podAffinityTerm متناظر، در بازه ۱ تا ۱۰۰.</td>
    </tr>
  </tbody>
</table>


## WindowsSecurityContextOptions {#WindowsSecurityContextOptions}

WindowsSecurityContextOptions شامل گزینه‌ها و اعتبارنامه‌های مختص ویندوز است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>gmsaCredentialSpec</code><br/><em>string</em></td>
      <td>GMSACredentialSpec جایی است که webhook پذیرش GMSA (https://github.com/kubernetes-sigs/windows-gmsa) محتوای مشخصات اعتبارنامه GMSA را که با فیلد GMSACredentialSpecName نام‌گذاری شده است، به‌صورت درون‌خطی در آن قرار می‌دهد.</td>
    </tr>
    <tr>
      <td><code>gmsaCredentialSpecName</code><br/><em>string</em></td>
      <td>GMSACredentialSpecName نام مشخصات اعتبارنامه GMSA است که باید استفاده شود.</td>
    </tr>
    <tr>
      <td><code>hostProcess</code><br/><em>boolean</em></td>
      <td>HostProcess مشخص می‌کند که آیا کانتینر باید به‌صورت کانتینر «Host Process» اجرا شود یا خیر. تمام کانتینرهای یک Pod باید مقدار مؤثر HostProcess یکسانی داشته باشند (ترکیب کانتینرهای HostProcess و غیر HostProcess مجاز نیست). افزون بر این، اگر HostProcess برابر true باشد، HostNetwork نیز باید روی true تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>runAsUserName</code><br/><em>string</em></td>
      <td>نام کاربری در ویندوز برای اجرای entrypoint فرایند کانتینر. اگر مشخص نشود، به‌طور پیش‌فرض کاربر تعیین‌شده در فراداده ایمیج استفاده می‌شود. این مقدار را می‌توان در PodSecurityContext نیز تنظیم کرد. اگر هم در SecurityContext و هم در PodSecurityContext تنظیم شود، مقدار مشخص‌شده در SecurityContext اولویت دارد.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /api/v1/namespaces/{namespace}/pods


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا قالب‌بندی می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار باید کمتر از یا برابر با ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرایند استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `post` Create Eviction

#### HTTP Request

POST /api/v1/namespaces/{namespace}/pods/{name}/eviction


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Eviction</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار باید کمتر از یا برابر با ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرایند استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا قالب‌بندی می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../lifecycle/eviction-v1alpha1#Eviction" >}}">Eviction</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../lifecycle/eviction-v1alpha1#Eviction" >}}">Eviction</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "../lifecycle/eviction-v1alpha1#Eviction" >}}">Eviction</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "../lifecycle/eviction-v1alpha1#Eviction" >}}">Eviction</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /api/v1/namespaces/{namespace}/pods/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا قالب‌بندی می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار باید کمتر از یا برابر با ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرایند استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر apply، پرچم Force باید تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>

### `put` جایگزینی (Replace)

#### درخواست HTTP

PUT /api/v1/namespaces/{namespace}/pods/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست در همان مرحله متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای که بی‌سروصدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از بین فیلدهای تکراری، همه به‌جز آخرین فیلدی که decoder با آن مواجه می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از بین فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف (Delete)

#### درخواست HTTP

DELETE /api/v1/namespaces/{namespace}/pods/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست در همان مرحله متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت باید حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت پیش‌فرض (grace period) نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای خراب بودن آبجکت (corrupt object) شکست بخورد، حذف ناامن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به‌دلیل یکی از موارد زیر نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد: الف) داده‌های آن قابل تبدیل نباشد، مثلاً در اثر شکست در رمزگشایی، یا ب) رمزگشایی (decode) آن به یک آبجکت ناموفق باشد. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط زمانی از آن استفاده کنید که واقعاً از کار خود مطمئن هستید. مقدار پیش‌فرض false است و کاربر باید برای فعال‌سازی آن به‌صراحت اقدام کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام «orphan» به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص هر منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری است که تمام وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /api/v1/namespaces/{namespace}/pods


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از یک کوئری قبلی را با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده باشند، تا زمانی که کلیدشان بعد از «کلید بعدی» قرار داشته باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، به‌طور پیش‌فرض مقداری مختص هر آبجکت به کار می‌رود. مقدار صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. یک منبع در صورتی خراب در نظر گرفته می‌شود که به‌دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً شکست در رمزگشایی، یا ب) ناموفق بودن رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد. نکته: حذف ناایمن، محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی پاک می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط زمانی از آن استفاده کنید که واقعاً بدانید چه کار می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست برگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعهٔ بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد کمتری از موارد درخواستی (حتی صفر مورد) را برگرداند، به این دلیل که همهٔ آبجکت‌های درخواستی فیلتر شده باشند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به حضور فیلد continue تکیه کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با اجرای یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده است، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این وضعیت گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجهٔ بسیار بزرگ از limit استفاده می‌کند، همهٔ آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در طول فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبهٔ اولین نتیجهٔ فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و چگونه. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض را finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌کنند. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - garbage collector اجازه می‌یابد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion در فراخوانی‌های فهرست چگونه اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌دهد و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan به معنای «داده‌ای که دست‌کم به اندازهٔ `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازهٔ hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشهٔ object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لفظی CEL درون single-quote با پیشوند '0x' هستند که کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای hash شصت‌وچهاربیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است و کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، مدت زمان فراخوانی را محدود می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن

#### درخواست HTTP

GET /api/v1/namespaces/{namespace}/pods/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست

#### درخواست HTTP

GET /api/v1/namespaces/{namespace}/pods


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک کوئری قبلی را با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری را که تشخیص نمی‌دهد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به‌همراه یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از "کلید بعدی" باشد، در پاسخ خواهند بود. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج استفاده کرد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) بازگرداند و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و در آن صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت تکه‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده خواهد کرد. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه اولین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه می‌دهند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معناست که «داده‌ای دست‌کم به‌روز به‌اندازه `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض: اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون single-quote با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  نمونه‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#PodList" >}}">PodList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست‌کردن در همه فضاهای نام

#### درخواست HTTP

GET /api/v1/pods



#### پارامترهای پرس‌وجو (Query Parameters)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmarkها را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند، و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>برای دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) به کار ببرند، و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرست سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته می‌شود و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراوداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. اگر همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند با یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌کردن تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه اولین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات، <a href="https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions">https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions</a> را ببینید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات، https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions را ببینید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از آن RV) در آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص‌کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل single quote قرار می‌گیرند و پیشوند '0x' دارند؛ آن‌ها کران پایین (شامل) و کران بالای (غیرشامل) بازه را بر فضای hash ‏64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌بودن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی فهرست/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#PodList" >}}">PodList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### HTTP Request

GET /api/v1/watch/namespaces/{namespace}/pods/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی ارسال می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از یک پرسوجوی قبلی را با پارامترهای پرسوجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده باشند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرسوجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، ویرایش یا حذف شده است در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) آمده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی روی نسخه‌های منبعی که یک درخواست می‌تواند از آن‌ها پاسخ داده شود اعمال می‌کند. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود که «داده‌ها دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشند» و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را ندارد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون single-quote قرار می‌گیرند و پیشوند '0x' دارند. این مقادیر کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش FNV-1a شصت‌وچهار بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List

#### درخواست HTTP

GET /api/v1/watch/namespaces/{namespace}/pods


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند، و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی استفاده کنند که پارامترهای کوئری آن (به‌جز مقدار continue) کاملاً یکسان باشد، و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد در حالتی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit بیشترین تعداد پاسخی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تعیین limit ممکن است تعداد آیتم‌هایی کمتر از مقدار درخواستی (حتی صفر آیتم) بازگرداند، در حالتی که همه آبجکت‌های درخواستی فیلتر شوند؛ از این رو کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر، فقط به حضور فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد در حالتی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌هایی که از یک فراخوانی فهرست واحد بدون limit به دست می‌آیند یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، اصلاح یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که هنگام محاسبه اولین نتیجه فهرست موجود بوده است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را برای نسخه‌های منبعی تعیین می‌کند که درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم می‌شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan   به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - در صورتی که `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد،   خطای Invalid بازگردانده می‌شود.  مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و با قالب fieldSelector ("metadata.uid") متفاوت است. مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لیترال CEL درون single-quote با پیشوند '0x' هستند و کران پایین شامل (inclusive) و کران بالای غیرشامل (exclusive) را در فضای هش 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار، فارغ از هرگونه فعالیت یا عدم فعالیت، مدت زمان فراخوانی را محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List All Namespaces

#### درخواست HTTP

`GET /api/v1/watch/pods`



#### پارامترهای پرس‌وجو (Query)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی برگردانده می‌شوند و نیز نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور می‌تواند مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافتی همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است؛ یعنی آبجکت‌هایی که پس از درخواست اول فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت نتایج بسیار بزرگ در بخش‌های کوچک‌تر از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در جریان یک فهرست تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion در فراخوانی‌های فهرست چگونه اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنی «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL داخل تک‌نقل‌قول با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای hash ‏64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به فعالیت یا عدم فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch Status

#### درخواست HTTP

`PATCH /api/v1/namespaces/{namespace}/pods/{name}/status`


#### پارامترهای مسیر (Path)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو (Query)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مربوط می‌شود. طول مقدار باید کمتر از یا برابر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری فقط آخرین فیلدی را که رمزگشا با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest رد می‌کند. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معنی که کاربر مالکیت فیلدهای دارای تعارض را که متعلق به دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force باید تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه (Body)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `get` Read Status

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/status`


#### پارامترهای مسیر (Path)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو (Query)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Status

#### درخواست HTTP

`PUT /api/v1/namespaces/{namespace}/pods/{name}/status`


#### پارامترهای مسیر (Path)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو (Query)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مربوط می‌شود. طول مقدار باید کمتر از یا برابر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری فقط آخرین فیلدی را که رمزگشا با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest رد می‌کند. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه (Body)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>

### `get` خواندن Resize

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/resize`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` اعمال Patch روی Resize

#### درخواست HTTP

`PATCH /api/v1/namespaces/{namespace}/pods/{name}/resize`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط باید شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این پارامتر برای درخواست‌های apply (‏application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (‏JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرآیند استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و فقط آخرین مورد از هر فیلد تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معناست که کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force نباید تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی Resize

#### درخواست HTTP

`PUT /api/v1/namespaces/{namespace}/pods/{name}/resize`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط باید شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرآیند استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و فقط آخرین مورد از هر فیلد تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` اعمال Patch روی EphemeralContainers

#### درخواست HTTP

`PATCH /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط باید شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این پارامتر برای درخواست‌های apply (‏application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (‏JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرآیند استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و فقط آخرین مورد از هر فیلد تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معناست که کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force نباید تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن EphemeralContainers

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی EphemeralContainers

#### درخواست HTTP

`PUT /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط باید شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرآیند استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و فقط آخرین مورد از هر فیلد تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "pod-v1#Pod" >}}">Pod</a></em></td>
    </tr>
  </tbody>
</table>

### `post` ایجاد Connect Portforward

#### درخواست HTTP

برای جلوگیری از شروع خط با کاراکتر لاتین، درخواست در بلوک کد قرار داده نشده است؛ مقدار آن بدون تغییر در ادامه آمده است:

`POST /api/v1/namespaces/{namespace}/pods/{name}/portforward`


#### پارامترهای مسیر (Path Parameters)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodPortForwardOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری (Query Parameters)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>ports</code></td>
      <td><em>integer</em></td>
      <td>فهرست پورت‌هایی که باید فوروارد شوند. هنگام استفاده از WebSockets الزامی است</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `post` ایجاد Connect Proxy

#### درخواست HTTP

`POST /api/v1/namespaces/{namespace}/pods/{name}/proxy`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `post` ایجاد Connect Proxy Path

#### درخواست HTTP

`POST /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف Connect Proxy

#### درخواست HTTP

`DELETE /api/v1/namespaces/{namespace}/pods/{name}/proxy`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف Connect Proxy Path

#### درخواست HTTP

`DELETE /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` دریافت Connect Portforward

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/portforward`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodPortForwardOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>ports</code></td>
      <td><em>integer</em></td>
      <td>فهرست پورت‌هایی که باید فوروارد شوند. هنگام استفاده از WebSockets الزامی است</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` دریافت Connect Proxy

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/proxy`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` دریافت Connect Proxy Path

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `head` Head Connect Proxy

#### درخواست HTTP

`HEAD /api/v1/namespaces/{namespace}/pods/{name}/proxy`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `head` Head Connect Proxy Path

#### درخواست HTTP

`HEAD /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی Connect Proxy

#### درخواست HTTP

`PUT /api/v1/namespaces/{namespace}/pods/{name}/proxy`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی Connect Proxy Path

#### درخواست HTTP

`PUT /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodProxyOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پراکسی جاری به Pod استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>

### `get` خواندن لاگ

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/log`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Pod</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای نمونه برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>container</code></td>
      <td><em>string</em></td>
      <td>کانتینری که لاگ‌های آن باید به‌صورت جریانی دریافت شود. اگر Pod فقط یک کانتینر داشته باشد، مقدار پیش‌فرض همان کانتینر است.</td>
    </tr>
    <tr>
      <td><code>follow</code></td>
      <td><em>boolean</em></td>
      <td>جریان لاگ Pod را دنبال می‌کند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>insecureSkipTLSVerifyBackend</code></td>
      <td><em>boolean</em></td>
      <td>مقدار insecureSkipTLSVerifyBackend نشان می‌دهد که apiserver نباید اعتبار گواهی سرویس‌دهنده‌ی backend متصل‌شده را تأیید کند. این کار اتصال HTTPS میان apiserver و backend را ناامن می‌کند و به این معناست که apiserver نمی‌تواند تأیید کند داده‌های لاگ دریافتی واقعاً از kubelet اصلی آمده‌اند. اگر kubelet طوری پیکربندی شده باشد که اعتبارنامه‌های TLS مربوط به apiserver را تأیید کند، این به آن معنا نیست که اتصال به kubelet اصلی در برابر حمله‌ی مرد میانی (man in the middle) آسیب‌پذیر است (برای مثال، مهاجم نمی‌تواند داده‌های واقعی لاگ را که از kubelet اصلی می‌آید شنود کند).</td>
    </tr>
    <tr>
      <td><code>limitBytes</code></td>
      <td><em>integer</em></td>
      <td>در صورت تنظیم، تعداد بایت‌هایی را مشخص می‌کند که پیش از پایان‌دادن به خروجی لاگ از سرور خوانده می‌شود. ممکن است آخرین خط لاگ به‌طور کامل نمایش داده نشود و مقدار بازگشتی اندکی بیشتر یا کمتر از حد مشخص‌شده باشد.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>previous</code></td>
      <td><em>boolean</em></td>
      <td>لاگ‌های کانتینر پیشین را که خاتمه یافته است بازمی‌گرداند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>sinceSeconds</code></td>
      <td><em>integer</em></td>
      <td>زمانی نسبی بر حسب ثانیه پیش از لحظه‌ی کنونی که لاگ‌ها از آن به بعد نمایش داده می‌شوند. اگر این مقدار پیش از زمان آغاز Pod باشد، فقط لاگ‌های پس از آغاز Pod بازگردانده می‌شود. اگر این مقدار در آینده باشد، هیچ لاگی بازگردانده نمی‌شود. فقط یکی از sinceSeconds یا sinceTime را می‌توان مشخص کرد.</td>
    </tr>
    <tr>
      <td><code>stream</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند کدام جریان لاگ کانتینر به کلاینت بازگردانده شود. مقادیر مجاز "All"، "Stdout" و "Stderr" هستند. اگر مشخص نشود، "All" استفاده می‌شود و هر دو جریان stdout و stderr به‌صورت درهم‌آمیخته بازگردانده می‌شوند. توجه کنید که در صورت تعیین "TailLines"، مقدار "Stream" فقط می‌تواند nil یا "All" باشد.</td>
    </tr>
    <tr>
      <td><code>tailLines</code></td>
      <td><em>integer</em></td>
      <td>در صورت تنظیم، تعداد خطوطی را از انتهای لاگ‌ها مشخص می‌کند که نمایش داده می‌شود. اگر مشخص نشود، لاگ‌ها از زمان ایجاد کانتینر یا از sinceSeconds یا sinceTime نمایش داده می‌شوند. توجه کنید که در صورت تعیین "TailLines"، مقدار "Stream" فقط می‌تواند nil یا "All" باشد.</td>
    </tr>
    <tr>
      <td><code>timestamps</code></td>
      <td><em>boolean</em></td>
      <td>اگر true باشد، یک مهر زمانی (timestamp) با قالب RFC3339 یا RFC3339Nano به ابتدای هر خط از خروجی لاگ افزوده می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` دریافت Connect Exec

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/exec`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodExecOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای نمونه برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>command</code></td>
      <td><em>string</em></td>
      <td>فرمان راه‌دوری که باید اجرا شود، به‌صورت آرایه‌ی argv. این فرمان درون یک shell اجرا نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>container</code></td>
      <td><em>string</em></td>
      <td>کانتینری که فرمان در آن اجرا می‌شود. اگر Pod فقط یک کانتینر داشته باشد، مقدار پیش‌فرض همان کانتینر است.</td>
    </tr>
    <tr>
      <td><code>stderr</code></td>
      <td><em>boolean</em></td>
      <td>جریان خطای استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد.</td>
    </tr>
    <tr>
      <td><code>stdin</code></td>
      <td><em>boolean</em></td>
      <td>جریان ورودی استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdout</code></td>
      <td><em>boolean</em></td>
      <td>جریان خروجی استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد.</td>
    </tr>
    <tr>
      <td><code>tty</code></td>
      <td><em>boolean</em></td>
      <td>اگر TTY برابر true باشد، برای فراخوانی exec یک tty اختصاص داده می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `post` ایجاد Connect Exec

#### درخواست HTTP

`POST /api/v1/namespaces/{namespace}/pods/{name}/exec`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodExecOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای نمونه برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>command</code></td>
      <td><em>string</em></td>
      <td>فرمان راه‌دوری که باید اجرا شود، به‌صورت آرایه‌ی argv. این فرمان درون یک shell اجرا نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>container</code></td>
      <td><em>string</em></td>
      <td>کانتینری که فرمان در آن اجرا می‌شود. اگر Pod فقط یک کانتینر داشته باشد، مقدار پیش‌فرض همان کانتینر است.</td>
    </tr>
    <tr>
      <td><code>stderr</code></td>
      <td><em>boolean</em></td>
      <td>جریان خطای استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد.</td>
    </tr>
    <tr>
      <td><code>stdin</code></td>
      <td><em>boolean</em></td>
      <td>جریان ورودی استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdout</code></td>
      <td><em>boolean</em></td>
      <td>جریان خروجی استاندارد Pod را برای این فراخوانی تغییر مسیر می‌دهد.</td>
    </tr>
    <tr>
      <td><code>tty</code></td>
      <td><em>boolean</em></td>
      <td>اگر TTY برابر true باشد، برای فراخوانی exec یک tty اختصاص داده می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` دریافت Connect Attach

#### درخواست HTTP

`GET /api/v1/namespaces/{namespace}/pods/{name}/attach`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodAttachOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای نمونه برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>container</code></td>
      <td><em>string</em></td>
      <td>کانتینری که فرمان در آن اجرا می‌شود. اگر Pod فقط یک کانتینر داشته باشد، مقدار پیش‌فرض همان کانتینر است.</td>
    </tr>
    <tr>
      <td><code>stderr</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stderr برابر true باشد، نشان می‌دهد که stderr برای فراخوانی attach تغییر مسیر داده می‌شود. مقدار پیش‌فرض true است.</td>
    </tr>
    <tr>
      <td><code>stdin</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stdin برابر true باشد، جریان ورودی استاندارد Pod برای این فراخوانی تغییر مسیر داده می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdout</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stdout برابر true باشد، نشان می‌دهد که stdout برای فراخوانی attach تغییر مسیر داده می‌شود. مقدار پیش‌فرض true است.</td>
    </tr>
    <tr>
      <td><code>tty</code></td>
      <td><em>boolean</em></td>
      <td>اگر TTY برابر true باشد، برای فراخوانی attach یک tty اختصاص داده می‌شود. این مقدار به محیط اجرای کانتینر منتقل می‌شود، بنابراین tty توسط محیط اجرای کانتینر روی نود کارگر اختصاص می‌یابد. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `post` ایجاد Connect Attach

#### درخواست HTTP

`POST /api/v1/namespaces/{namespace}/pods/{name}/attach`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PodAttachOptions</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای نمونه برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>container</code></td>
      <td><em>string</em></td>
      <td>کانتینری که فرمان در آن اجرا می‌شود. اگر Pod فقط یک کانتینر داشته باشد، مقدار پیش‌فرض همان کانتینر است.</td>
    </tr>
    <tr>
      <td><code>stderr</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stderr برابر true باشد، نشان می‌دهد که stderr برای فراخوانی attach تغییر مسیر داده می‌شود. مقدار پیش‌فرض true است.</td>
    </tr>
    <tr>
      <td><code>stdin</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stdin برابر true باشد، جریان ورودی استاندارد Pod برای این فراخوانی تغییر مسیر داده می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>stdout</code></td>
      <td><em>boolean</em></td>
      <td>اگر Stdout برابر true باشد، نشان می‌دهد که stdout برای فراخوانی attach تغییر مسیر داده می‌شود. مقدار پیش‌فرض true است.</td>
    </tr>
    <tr>
      <td><code>tty</code></td>
      <td><em>boolean</em></td>
      <td>اگر TTY برابر true باشد، برای فراخوانی attach یک tty اختصاص داده می‌شود. این مقدار به محیط اجرای کانتینر منتقل می‌شود، بنابراین tty توسط محیط اجرای کانتینر روی نود کارگر اختصاص می‌یابد. مقدار پیش‌فرض false است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>

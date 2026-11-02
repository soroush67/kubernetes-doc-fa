---
api_metadata:
  apiVersion: "batch/v1"
  import: "k8s.io/api/batch/v1"
  kind: "Job"
content_type: "api_reference"
description: "Job پیکربندی یک Job منفرد را نمایش می‌دهد."
title: "Job"
weight: 20
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

`apiVersion: batch/v1`

`import "k8s.io/api/batch/v1"`


## Job {#Job}

Job پیکربندی یک Job منفرد را نمایش می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره (schema) نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. قالب آن CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#JobSpec" >}}">JobSpec</a></em></td>
      <td>مشخصات رفتار مطلوب یک Job. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#JobStatus" >}}">JobStatus</a></em></td>
      <td>وضعیت فعلی یک Job. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
  </tbody>
</table>


## JobSpec {#JobSpec}

JobSpec توصیف می‌کند که اجرای Job چگونه خواهد بود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>activeDeadlineSeconds</code><br/><em>integer</em></td>
      <td>مدت زمان را بر حسب ثانیه، نسبت به startTime، مشخص می‌کند که Job می‌تواند پیش از آنکه سیستم تلاش کند آن را خاتمه دهد، به‌طور پیوسته فعال بماند؛ مقدار باید عدد صحیح مثبت باشد. اگر یک Job معلق شود (هنگام ایجاد یا از طریق به‌روزرسانی)، این تایمر عملاً متوقف می‌شود و هنگام از سرگیری مجدد Job بازنشانی خواهد شد.</td>
    </tr>
    <tr>
      <td><code>backoffLimit</code><br/><em>integer</em></td>
      <td>تعداد تلاش‌های مجدد را پیش از علامت‌گذاری این Job به‌عنوان ناموفق مشخص می‌کند. مقدار پیش‌فرض 6 است، مگر آنکه backoffLimitPerIndex (فقط برای Indexed Job) مشخص شده باشد. در صورت مشخص بودن backoffLimitPerIndex، مقدار پیش‌فرض backoffLimit برابر 2147483647 است.</td>
    </tr>
    <tr>
      <td><code>backoffLimitPerIndex</code><br/><em>integer</em></td>
      <td>حد تعداد تلاش‌های مجدد درون یک ایندکس را پیش از علامت‌گذاری آن ایندکس به‌عنوان ناموفق مشخص می‌کند. در صورت فعال بودن، تعداد شکست‌ها به ازای هر ایندکس در حاشیه‌نویسی (annotation) با نام batch.kubernetes.io/job-index-failure-count در Pod نگهداری می‌شود. این فیلد را فقط زمانی می‌توان تنظیم کرد که completionMode مربوط به Job برابر Indexed باشد و سیاست راه‌اندازی مجدد (restart policy) در Pod برابر Never باشد. این فیلد تغییرناپذیر (immutable) است.</td>
    </tr>
    <tr>
      <td><code>completionMode</code><br/><em>string</em></td>
      <td>completionMode مشخص می‌کند که تکمیل Podها چگونه ردیابی شود. مقدار آن می‌تواند `NonIndexed` (پیش‌فرض) یا `Indexed` باشد.  حالت `NonIndexed` به این معناست که Job زمانی کامل‌شده در نظر گرفته می‌شود که به تعداد .spec.completions، Pod با موفقیت تکمیل شده باشد. تکمیل هر Pod با تکمیل Podهای دیگر هم‌ارز است.  حالت `Indexed` به این معناست که Podهای یک Job یک ایندکس تکمیل مرتبط از 0 تا (.spec.completions - 1) دریافت می‌کنند که در حاشیه‌نویسی batch.kubernetes.io/job-completion-index در دسترس است. Job زمانی کامل‌شده در نظر گرفته می‌شود که برای هر ایندکس یک Pod با موفقیت تکمیل شده باشد. وقتی مقدار `Indexed` باشد، باید .spec.completions مشخص شود و `.spec.parallelism` باید کوچک‌تر از یا برابر با 10^5 باشد. افزون بر این، نام Pod به‌شکل `$(job-name)-$(index)-$(random-string)` و نام میزبان (hostname) آن به‌شکل `$(job-name)-$(index)` است.  حالت‌های تکمیل بیشتری ممکن است در آینده افزوده شود. اگر کنترل‌کننده Job با حالتی روبه‌رو شود که آن را نمی‌شناسد، که ممکن است در هنگام ارتقا به‌دلیل اختلاف نسخه رخ دهد، کنترل‌کننده به‌روزرسانی‌های آن Job را نادیده می‌گیرد.<br/><br/>مقادیر ممکن enum:<br/> - `"Indexed"` یک حالت تکمیل Job است. در این حالت، Podهای یک Job یک ایندکس تکمیل مرتبط از 0 تا (.spec.completions - 1) دریافت می‌کنند. Job زمانی کامل‌شده در نظر گرفته می‌شود که برای هر ایندکس تکمیل، یک Pod تکمیل شده باشد.<br/> - `"NonIndexed"` یک حالت تکمیل Job است. در این حالت، Job زمانی کامل‌شده در نظر گرفته می‌شود که به تعداد .spec.completions، Pod با موفقیت تکمیل شده باشد. تکمیل Podها با یکدیگر هم‌ارز است.</td>
    </tr>
    <tr>
      <td><code>completions</code><br/><em>integer</em></td>
      <td>تعداد مطلوب Podهایی را مشخص می‌کند که باید با موفقیت به پایان برسند تا Job اجرا شده تلقی شود.  مقدار null به این معناست که موفقیت هر Pod نشان‌دهنده موفقیت همه Podها است و به parallelism اجازه می‌دهد هر مقدار مثبتی داشته باشد.  مقدار 1 به این معناست که parallelism به 1 محدود می‌شود و موفقیت آن Pod نشان‌دهنده موفقیت Job است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</td>
    </tr>
    <tr>
      <td><code>managedBy</code><br/><em>string</em></td>
      <td>فیلد ManagedBy کنترل‌کننده‌ای را مشخص می‌کند که یک Job را مدیریت می‌کند. کنترل‌کننده Job در کوبرنتیز، Jobهایی را که این فیلد را ندارند یا مقدار آن رشته رزروشده `kubernetes.io/job-controller` است reconcile می‌کند، اما Jobهایی را که مقدار سفارشی برای این فیلد دارند نادیده می‌گیرد. مقدار باید یک مسیر معتبر با پیشوند دامنه (مثلاً acme.io/foo) باشد؛ همه نویسه‌های پیش از اولین "/" باید یک زیردامنه معتبر طبق RFC 1123 باشند. همه نویسه‌های پس از اولین "/" باید نویسه‌های معتبر مسیر HTTP طبق RFC 3986 باشند. مقدار نمی‌تواند از 63 نویسه بیشتر باشد. این فیلد تغییرناپذیر (immutable) است.</td>
    </tr>
    <tr>
      <td><code>manualSelector</code><br/><em>boolean</em></td>
      <td>manualSelector تولید برچسب‌ها و انتخابگرهای Pod را کنترل می‌کند. تا زمانی که از کار خود کاملاً مطمئن نیستید، `manualSelector` را تنظیم‌نشده رها کنید. وقتی مقدار آن false باشد یا تنظیم نشده باشد، سیستم برچسب‌هایی منحصربه‌فرد برای این Job انتخاب می‌کند و آن‌ها را به قالب Pod می‌افزاید.  وقتی مقدار آن true باشد، کاربر مسئول انتخاب برچسب‌های منحصربه‌فرد و مشخص کردن انتخابگر است.  انتخاب نکردن برچسب منحصربه‌فرد ممکن است باعث شود این Job و Jobهای دیگر به‌درستی کار نکنند.  با این حال، ممکن است `manualSelector=true` را در Jobهایی ببینید که با API قدیمی `extensions/v1beta1` ایجاد شده‌اند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors</td>
    </tr>
    <tr>
      <td><code>maxFailedIndexes</code><br/><em>integer</em></td>
      <td>حداکثر تعداد ایندکس‌های ناموفق را پیش از علامت‌گذاری Job به‌عنوان ناموفق مشخص می‌کند، در حالتی که backoffLimitPerIndex تنظیم شده باشد. وقتی تعداد ایندکس‌های ناموفق از این عدد فراتر رود، کل Job با وضعیت Failed علامت‌گذاری و اجرای آن خاتمه داده می‌شود. اگر این فیلد null بماند، Job اجرای همه ایندکس‌های خود را ادامه می‌دهد و با شرط (condition) `Complete` برای Job علامت‌گذاری می‌شود. این فیلد را فقط زمانی می‌توان مشخص کرد که backoffLimitPerIndex تنظیم شده باشد. مقدار آن می‌تواند null یا حداکثر برابر با completions باشد. هنگامی که completions بزرگ‌تر از 10^5 است، تعیین این فیلد الزامی است و باید کوچک‌تر از یا برابر با 10^4 باشد.</td>
    </tr>
    <tr>
      <td><code>parallelism</code><br/><em>integer</em></td>
      <td>حداکثر تعداد مطلوب Podهایی را مشخص می‌کند که Job باید در هر لحظه اجرا کند. تعداد واقعی Podهای در حال اجرا در حالت پایدار، زمانی کمتر از این عدد خواهد بود که ((.spec.completions - .status.successful) \< .spec.parallelism) برقرار باشد، یعنی وقتی کار باقی‌مانده کمتر از حداکثر parallelism است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</td>
    </tr>
    <tr>
      <td><code>podFailurePolicy</code><br/><em><a href="{{< ref "#PodFailurePolicy" >}}">PodFailurePolicy</a></em></td>
      <td>سیاست رسیدگی به Podهای ناموفق را مشخص می‌کند. به‌طور خاص، با این فیلد می‌توان مجموعه اقدام‌ها و شرایطی را که برای انجام اقدام مرتبط باید برقرار باشند تعیین کرد. اگر این فیلد خالی باشد، رفتار پیش‌فرض اعمال می‌شود: شمارنده Podهای ناموفق، که با فیلد .status.failed مربوط به Job نمایش داده می‌شود، افزایش می‌یابد و با backoffLimit مقایسه می‌شود. این فیلد را نمی‌توان همراه با restartPolicy=OnFailure به کار برد.</td>
    </tr>
    <tr>
      <td><code>podReplacementPolicy</code><br/><em>string</em></td>
      <td>podReplacementPolicy مشخص می‌کند که Podهای جایگزین چه زمانی ایجاد شوند. مقادیر ممکن عبارت‌اند از: - TerminatingOrFailed به این معناست که Podها را زمانی که در حال خاتمه یافتن هستند (دارای metadata.deletionTimestamp) یا ناموفق شده‌اند دوباره ایجاد می‌کنیم. - Failed به این معناست که پیش از ایجاد Pod جایگزین، باید منتظر ماند تا Pod ایجادشده قبلی کاملاً خاتمه یابد (در فاز Failed یا Succeeded باشد).  هنگام استفاده از podFailurePolicy، تنها مقدار مجاز Failed است. وقتی podFailurePolicy استفاده نمی‌شود، مقادیر TerminatingOrFailed و Failed هر دو مجاز هستند.<br/><br/>مقادیر ممکن enum:<br/> - `"Failed"` به این معناست که پیش از ایجاد Pod جایگزین، باید منتظر ماند تا Pod ایجادشده قبلی کاملاً خاتمه یابد (در فاز Failed یا Succeeded باشد).<br/> - `"TerminatingOrFailed"` به این معناست که Podها را زمانی که در حال خاتمه یافتن هستند (دارای metadata.deletionTimestamp) یا ناموفق شده‌اند دوباره ایجاد می‌کنیم.</td>
    </tr>
    <tr>
      <td><code>scheduling</code><br/><em><a href="{{< ref "#JobSchedulingConfiguration" >}}">JobSchedulingConfiguration</a></em></td>
      <td>scheduling پیکربندی زمان‌بندی مبتنی بر Workload (Workload-aware Scheduling) را برای این Job تعریف می‌کند. در صورت تنظیم، سیاست زمان‌بندی (basic یا gang)، محدودیت‌های توپولوژی، حالت اختلال (disruption mode) و claimهای منبع مشترک را مشخص می‌کند. در صورت حذف این فیلد، Job به‌طور پیش‌فرض از سیاست زمان‌بندی basic استفاده می‌کند که مانند زمان‌بندی استاندارد Pod به Pod رفتار می‌کند. این فیلد در سطح آلفا است و به feature gate با نام WorkloadWithJob نیاز دارد. این فیلد تغییرناپذیر است، از جمله اینکه اصلاً تنظیم شده باشد یا نه؛ پس از ایجاد، تنها policy.gang.minCount را می‌توان تغییر داد.</td>
    </tr>
    <tr>
      <td><code>selector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>یک پرس‌وجوی برچسب روی Podها که باید با تعداد Podها مطابقت داشته باشد. معمولاً سیستم این فیلد را برای شما تنظیم می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors</td>
    </tr>
    <tr>
      <td><code>successPolicy</code><br/><em><a href="{{< ref "#SuccessPolicy" >}}">SuccessPolicy</a></em></td>
      <td>successPolicy مشخص می‌کند که Job در چه شرایطی می‌تواند موفق اعلام شود. اگر این فیلد خالی باشد، رفتار پیش‌فرض اعمال می‌شود: Job تنها زمانی موفق اعلام می‌شود که تعداد Podهای موفق با completions برابر باشد. وقتی این فیلد مشخص شود، باید تغییرناپذیر باشد و فقط برای Jobهای Indexed کار می‌کند. پس از آنکه Job شرایط SuccessPolicy را برآورده کرد، Podهای باقی‌مانده خاتمه داده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>suspend</code><br/><em>boolean</em></td>
      <td>suspend مشخص می‌کند که کنترل‌کننده Job باید Pod ایجاد کند یا نه. اگر Job با مقدار true برای suspend ایجاد شود، کنترل‌کننده Job هیچ Podی ایجاد نمی‌کند. اگر Job پس از ایجاد معلق شود (یعنی مقدار پرچم از false به true تغییر کند)، کنترل‌کننده Job همه Podهای فعال مرتبط با این Job را حذف می‌کند. کاربران باید بار کاری خود را طوری طراحی کنند که این وضعیت را به‌خوبی مدیریت کند. معلق کردن یک Job فیلد StartTime آن را بازنشانی می‌کند و در نتیجه تایمر ActiveDeadlineSeconds نیز عملاً بازنشانی می‌شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>template</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../core/pod-template-v1#PodTemplateSpec" >}}">PodTemplateSpec</a></em></td>
      <td>Podی را توصیف می‌کند که هنگام اجرای یک Job ایجاد خواهد شد. تنها مقادیر مجاز template.spec.restartPolicy برابر "Never" یا "OnFailure" هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</td>
    </tr>
    <tr>
      <td><code>ttlSecondsAfterFinished</code><br/><em>integer</em></td>
      <td>ttlSecondsAfterFinished طول عمر یک Job را که اجرای آن به پایان رسیده است (با وضعیت Complete یا Failed) محدود می‌کند. اگر این فیلد تنظیم شود، پس از گذشت ttlSecondsAfterFinished از پایان Job، آن Job واجد شرایط حذف خودکار می‌شود. هنگام حذف Job، تضمین‌های چرخه عمر آن (مانند finalizerها) رعایت خواهد شد. اگر این فیلد تنظیم نشده باشد، Job به‌طور خودکار حذف نخواهد شد. اگر این فیلد روی صفر تنظیم شود، Job بلافاصله پس از پایان یافتن واجد شرایط حذف می‌شود.</td>
    </tr>
  </tbody>
</table>

## JobStatus {#JobStatus}

JobStatus وضعیت فعلی یک Job را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>active</code><br/><em>integer</em></td>
      <td>تعداد Podهای در حالت pending و running که در حال خاتمه یافتن نیستند (یعنی deletionTimestamp ندارند). برای Jobهای پایان‌یافته، این مقدار صفر است.</td>
    </tr>
    <tr>
      <td><code>completedIndexes</code><br/><em>string</em></td>
      <td>وقتی .spec.completionMode برابر "Indexed" باشد، completedIndexes اندیس‌های تکمیل‌شده را در قالب متنی نگه می‌دارد. اندیس‌ها به‌صورت اعداد صحیح دهدهی و جدا‌شده با کاما نمایش داده می‌شوند. اعداد به‌ترتیب صعودی فهرست می‌شوند. سه عدد متوالی یا بیشتر فشرده می‌شوند و با اولین و آخرین عنصر آن دنباله، با یک خط تیره از هم جدا شده، نمایش داده می‌شوند. برای مثال، اگر اندیس‌های تکمیل‌شده 1، 3، 4، 5 و 7 باشند، به‌صورت "1,3-5,7" نمایش داده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>completionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>زمان تکمیل شدن Job را نشان می‌دهد. تضمین نمی‌شود که این مقدار در عملیات‌های جداگانه بر اساس ترتیب happens-before تنظیم شود. این مقدار با قالب RFC3339 و بر پایه UTC نمایش داده می‌شود. زمان تکمیل فقط هنگامی تنظیم می‌شود که Job با موفقیت پایان یابد، و در هیچ حالت دیگری تنظیم نمی‌شود. این مقدار را نمی‌توان به‌روزرسانی یا حذف کرد. این مقدار همان لحظه‌ی مقدار فیلد startTime یا زمانی پس از آن را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#JobCondition" >}}">JobCondition array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>آخرین مشاهدات موجود از وضعیت فعلی یک آبجکت. هنگامی که یک Job با شکست مواجه شود، یکی از شرایط (conditions) از نوع "Failed" با وضعیت true خواهد بود. هنگامی که یک Job معلق (suspend) شود، یکی از شرایط از نوع "Suspended" با وضعیت true خواهد بود؛ و هنگامی که Job از سر گرفته شود، وضعیت این شرط false می‌شود. هنگامی که یک Job تکمیل شود، یکی از شرایط از نوع "Complete" با وضعیت true خواهد بود. Job زمانی پایان‌یافته تلقی می‌شود که در یکی از شرایط نهایی، یعنی "Complete" یا "Failed"، باشد. یک Job نمی‌تواند هم‌زمان شرط‌های "Complete" و "Failed" را داشته باشد. همچنین نمی‌تواند هم‌زمان در شرط‌های "Complete" و "FailureTarget" باشد. شرط‌های "Complete"، "Failed" و "FailureTarget" را نمی‌توان غیرفعال کرد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/</td>
    </tr>
    <tr>
      <td><code>failed</code><br/><em>integer</em></td>
      <td>تعداد Podهایی که به فاز Failed رسیده‌اند. این مقدار به‌صورت یکنوا افزایش می‌یابد.</td>
    </tr>
    <tr>
      <td><code>failedIndexes</code><br/><em>string</em></td>
      <td>وقتی spec.backoffLimitPerIndex تنظیم شده باشد، failedIndexes اندیس‌های ناموفق را نگه می‌دارد. اندیس‌ها در قالب متنی مشابه فیلد `completedIndexes` نمایش داده می‌شوند، یعنی به‌صورت اعداد صحیح دهدهی و جدا‌شده با کاما نگهداری می‌شوند. اعداد به‌ترتیب صعودی فهرست می‌شوند. سه عدد متوالی یا بیشتر فشرده می‌شوند و با اولین و آخرین عنصر آن دنباله، با یک خط تیره از هم جدا شده، نمایش داده می‌شوند. برای مثال، اگر اندیس‌های ناموفق 1، 3، 4، 5 و 7 باشند، به‌صورت "1,3-5,7" نمایش داده می‌شوند. مجموعه‌ی اندیس‌های ناموفق نمی‌تواند با مجموعه‌ی اندیس‌های تکمیل‌شده هم‌پوشانی داشته باشد.</td>
    </tr>
    <tr>
      <td><code>ready</code><br/><em>integer</em></td>
      <td>تعداد Podهای فعالی که شرط Ready را دارند و در حال خاتمه یافتن نیستند (یعنی deletionTimestamp ندارند).</td>
    </tr>
    <tr>
      <td><code>startTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>زمانی را نشان می‌دهد که کنترل‌کننده‌ی Job پردازش یک Job را آغاز کرده است. اگر Job در حالت معلق ایجاد شود، این فیلد تا نخستین باری که Job از سر گرفته شود تنظیم نمی‌شود. این فیلد هر بار که یک Job از حالت تعلیق خارج می‌شود، بازنشانی می‌شود. این مقدار با قالب RFC3339 و بر پایه UTC نمایش داده می‌شود. پس از تنظیم شدن، این فیلد را فقط زمانی می‌توان حذف کرد که Job معلق باشد. تا زمانی که Job از حالت تعلیق خارج شده یا پایان یافته باشد، نمی‌توان این فیلد را تغییر داد.</td>
    </tr>
    <tr>
      <td><code>succeeded</code><br/><em>integer</em></td>
      <td>تعداد Podهایی که به فاز Succeeded رسیده‌اند. این مقدار برای یک spec مشخص به‌صورت یکنوا افزایش می‌یابد. با این حال، ممکن است در واکنش به کاهش مقیاس Jobهای ایندکس‌دار الاستیک کاهش یابد.</td>
    </tr>
    <tr>
      <td><code>terminating</code><br/><em>integer</em></td>
      <td>تعداد Podهایی که در حال خاتمه یافتن هستند (در فاز Pending یا Running قرار دارند و deletionTimestamp دارند).</td>
    </tr>
    <tr>
      <td><code>uncountedTerminatedPods</code><br/><em><a href="{{< ref "#UncountedTerminatedPods" >}}">UncountedTerminatedPods</a></em></td>
      <td>uncountedTerminatedPods شناسه‌های UID مربوط به Podهایی را نگه می‌دارد که خاتمه یافته‌اند، اما کنترل‌کننده‌ی Job هنوز آن‌ها را در شمارنده‌های وضعیت محاسبه نکرده است. کنترل‌کننده‌ی Job، Podها را با یک finalizer ایجاد می‌کند. هنگامی که یک Pod خاتمه می‌یابد (با موفقیت یا با شکست)، کنترل‌کننده برای محاسبه‌ی آن در وضعیت Job سه گام را انجام می‌دهد: ۱. UID مربوط به Pod را به آرایه‌های این فیلد اضافه می‌کند. ۲. finalizer مربوط به Pod را حذف می‌کند. ۳. UID مربوط به Pod را از آرایه‌ها حذف می‌کند و هم‌زمان شمارنده‌ی متناظر را افزایش می‌دهد. ممکن است Jobهای قدیمی با استفاده از این فیلد ردیابی نشده باشند؛ در این صورت فیلد null باقی می‌ماند. برای Jobهای پایان‌یافته، این ساختار خالی است.</td>
    </tr>
  </tbody>
</table>


## JobList {#JobList}

JobList مجموعه‌ای از Jobها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره‌ی نسخه‌دار این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "job-v1#Job" >}}">Job array</a></em></td>
      <td>items فهرست Jobها است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST را نشان می‌دهد که این آبجکت بازنمایی می‌کند. سرورها می‌توانند این مقدار را از نقطه‌ی انتهایی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده‌ی استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
  </tbody>
</table>


## JobCondition {#JobCondition}

JobCondition وضعیت فعلی یک Job را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastProbeTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که شرط بررسی شده است.</td>
    </tr>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که شرط از یک وضعیت به وضعیت دیگر گذار کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی قابل‌خواندن برای انسان که جزئیات آخرین گذار را بیان می‌کند.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل (مختصر) آخرین گذار شرط.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>وضعیت شرط؛ یکی از True، False یا Unknown.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع شرط Job؛ Complete یا Failed.</td>
    </tr>
  </tbody>
</table>


## JobSchedulingConfiguration {#JobSchedulingConfiguration}

JobSchedulingConfiguration بلوک‌های سازنده‌ی قابل‌استفاده‌ی مجدد برای زمان‌بندی آگاه از بار کاری را با هم ترکیب می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>disruptionMode</code><br/><em><a href="{{< ref "#WorkloadPodGroupDisruptionMode" >}}">WorkloadPodGroupDisruptionMode</a></em></td>
      <td>DisruptionMode حالتی را تعریف می‌کند که در آن Podهای Job می‌توانند دچار اختلال (disruption) شوند. یکی از Single یا All. این فیلد پس از ایجاد تغییرناپذیر است: نمی‌توان آن را اضافه یا حذف کرد و حالت انتخاب‌شده را نیز نمی‌توان تغییر داد.</td>
    </tr>
    <tr>
      <td><code>resourceClaims</code><br/><em><a href="{{< ref "#WorkloadPodGroupResourceClaim" >}}">WorkloadPodGroupResourceClaim array</a></em><br/><em>patch strategy: merge on key <code>name</code></em></td>
      <td>ResourceClaims مشخص می‌کند کدام ResourceClaimها می‌توانند میان Podهای Job به اشتراک گذاشته شوند. Podها با تعریف یک claim در Spec.ResourceClaims خودشان که دقیقاً با claim مربوط به PodGroup مطابقت داشته باشد، از دستگاه‌های تخصیص‌یافته به آن claim استفاده می‌کنند. claim باید نام یکسان داشته باشد و به همان ResourceClaim یا ResourceClaimTemplate ارجاع دهد. حداکثر ۴ claim را می‌توان تنظیم کرد که با محدودیت PodGroup حاصل مطابقت دارد. این فهرست پس از ایجاد تغییرناپذیر است: نمی‌توان به آن عنصری اضافه کرد، از آن حذف کرد یا عنصری را تغییر داد.</td>
    </tr>
    <tr>
      <td><code>schedulingConstraints</code><br/><em><a href="{{< ref "#WorkloadPodGroupSchedulingConstraints" >}}">WorkloadPodGroupSchedulingConstraints</a></em></td>
      <td>SchedulingConstraints محدودیت‌های زمان‌بندی (مثلاً توپولوژی) را برای Podهای Job تعریف می‌کند. این فیلد پس از ایجاد تغییرناپذیر است.</td>
    </tr>
    <tr>
      <td><code>schedulingPolicy</code><br/><em><a href="{{< ref "#WorkloadPodGroupSchedulingPolicy" >}}">WorkloadPodGroupSchedulingPolicy</a></em></td>
      <td>SchedulingPolicy سیاست زمان‌بندی این Job را تعریف می‌کند. دقیقاً یکی از Basic یا Gang باید تنظیم شود. این فیلد پس از ایجاد تغییرناپذیر است: نمی‌توان سیاست را اضافه یا حذف کرد. نوع سیاست (basic/gang) با اعتبارسنجی دستی ثابت نگه داشته می‌شود؛ فقط schedulingPolicy.gang.minCount قابل تغییر است.</td>
    </tr>
  </tbody>
</table>


## PodFailurePolicy {#PodFailurePolicy}

PodFailurePolicy توصیف می‌کند که Podهای ناموفق چگونه بر backoffLimit اثر می‌گذارند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>rules</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#PodFailurePolicyRule" >}}">PodFailurePolicyRule array</a></em></td>
      <td>فهرستی از قواعد سیاست شکست Pod. قواعد به‌ترتیب ارزیابی می‌شوند. به‌محض اینکه یک قاعده با شکست یک Pod مطابقت کند، بقیه‌ی قواعد نادیده گرفته می‌شوند. اگر هیچ قاعده‌ای با شکست Pod مطابقت نداشته باشد، رفتار پیش‌فرض اعمال می‌شود: شمارنده‌ی شکست‌های Pod افزایش می‌یابد و با backoffLimit مقایسه می‌شود. حداکثر ۲۰ عنصر مجاز است.</td>
    </tr>
  </tbody>
</table>


## PodFailurePolicyOnExitCodesRequirement {#PodFailurePolicyOnExitCodesRequirement}

PodFailurePolicyOnExitCodesRequirement الزام لازم برای مدیریت یک Pod ناموفق را بر اساس کدهای خروج کانتینرهای آن توصیف می‌کند. به‌طور مشخص، مقدار .state.terminated.exitCode را برای وضعیت هر کانتینر برنامه و هر init container بررسی می‌کند که به‌ترتیب در فیلدهای .status.containerStatuses و .status.initContainerStatuses در وضعیت Pod نمایش داده می‌شوند. کانتینرهایی که با موفقیت تکمیل شده‌اند (کد خروج 0) از بررسی این الزام کنار گذاشته می‌شوند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>containerName</code><br/><em>string</em></td>
      <td>بررسی کدهای خروج را به کانتینری با نام مشخص‌شده محدود می‌کند. وقتی null باشد، قاعده بر همه‌ی کانتینرها اعمال می‌شود. در صورت تعیین، باید با یکی از نام‌های container یا initContainer در قالب Pod مطابقت داشته باشد.</td>
    </tr>
    <tr>
      <td><code>operator</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>رابطه‌ی میان کد(های) خروج کانتینر و مقادیر مشخص‌شده را نشان می‌دهد. کانتینرهایی که با موفقیت تکمیل شده‌اند (کد خروج 0) از بررسی این الزام کنار گذاشته می‌شوند. مقادیر ممکن عبارت‌اند از: - In: اگر دست‌کم یک کد خروج کانتینر (در صورت وجود چند کانتینر که با فیلد 'containerName' محدود نشده‌اند، ممکن است چند کد وجود داشته باشد) در مجموعه‌ی مقادیر مشخص‌شده باشد، الزام برآورده شده است. - NotIn: اگر دست‌کم یک کد خروج کانتینر (در صورت وجود چند کانتینر که با فیلد 'containerName' محدود نشده‌اند، ممکن است چند کد وجود داشته باشد) در مجموعه‌ی مقادیر مشخص‌شده نباشد، الزام برآورده شده است. ممکن است در آینده مقادیر دیگری اضافه شوند. کلاینت‌ها باید در برابر یک operator ناشناخته چنین واکنش نشان دهند که الزام را برآورده‌نشده فرض کنند.<br/><br/>Possible enum values:<br/> - `"In"`<br/> - `"NotIn"`</td>
    </tr>
    <tr>
      <td><code>values</code>&nbsp;<strong>*</strong><br/><em>integer array</em></td>
      <td>مجموعه‌ی مقادیر را مشخص می‌کند. هر کد خروج کانتینر برگردانده‌شده (در صورت وجود چند کانتینر ممکن است چند کد وجود داشته باشد) با توجه به operator با این مجموعه‌ی مقادیر مقایسه می‌شود. فهرست مقادیر باید مرتب باشد و نباید مقدار تکراری داشته باشد. مقدار '0' را نمی‌توان برای operator از نوع In به کار برد. دست‌کم یک عنصر لازم است. حداکثر ۲۵۵ عنصر مجاز است.</td>
    </tr>
  </tbody>
</table>


## PodFailurePolicyOnPodConditionsPattern {#PodFailurePolicyOnPodConditionsPattern}

PodFailurePolicyOnPodConditionsPattern الگویی را برای تطبیق با نوع یک شرط واقعی Pod توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>status</code><br/><em>string</em></td>
      <td>وضعیت موردنیاز شرط Pod را مشخص می‌کند. برای تطبیق با یک شرط Pod لازم است وضعیت مشخص‌شده با وضعیت آن شرط برابر باشد. مقدار پیش‌فرض True است.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع موردنیاز شرط Pod را مشخص می‌کند. برای تطبیق با یک شرط Pod لازم است نوع مشخص‌شده با نوع آن شرط برابر باشد.</td>
    </tr>
  </tbody>
</table>


## PodFailurePolicyRule {#PodFailurePolicyRule}

PodFailurePolicyRule توصیف می‌کند که وقتی الزامات برآورده شوند، شکست یک Pod چگونه مدیریت می‌شود. در هر قاعده فقط یکی از onExitCodes و onPodConditions را می‌توان به کار برد، نه هر دو را.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>action</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>اقدامی را مشخص می‌کند که در صورت برآورده شدن الزامات، هنگام شکست یک Pod انجام می‌شود. مقادیر ممکن عبارت‌اند از: - FailJob: نشان می‌دهد که Job مربوط به Pod به‌عنوان Failed علامت‌گذاری می‌شود و همه‌ی Podهای در حال اجرا خاتمه داده می‌شوند. - FailIndex: نشان می‌دهد که اندیس Pod به‌عنوان Failed علامت‌گذاری می‌شود و دوباره راه‌اندازی نخواهد شد. - Ignore: نشان می‌دهد که شمارنده‌ی مربوط به .backoffLimit افزایش نمی‌یابد و یک Pod جایگزین ایجاد می‌شود. - Count: نشان می‌دهد که Pod به شیوه‌ی پیش‌فرض مدیریت می‌شود، یعنی شمارنده‌ی مربوط به .backoffLimit افزایش می‌یابد. ممکن است در آینده مقادیر دیگری اضافه شوند. کلاینت‌ها باید در برابر یک action ناشناخته چنین واکنش نشان دهند که آن قاعده را نادیده بگیرند.<br/><br/>Possible enum values:<br/> - `"Count"` این اقدامی است که ممکن است هنگام شکست یک Pod انجام شود: شکست Pod به شیوه‌ی پیش‌فرض مدیریت می‌شود و شمارنده‌ی مربوط به .backoffLimit که با فیلد .status.failed در Job نمایش داده می‌شود، افزایش می‌یابد.<br/> - `"FailIndex"` این اقدامی است که ممکن است هنگام شکست یک Pod انجام شود: اندیس Job به‌عنوان ناموفق علامت‌گذاری می‌شود تا از راه‌اندازی‌های مجدد در این اندیس جلوگیری شود. این اقدام فقط زمانی قابل استفاده است که backoffLimitPerIndex تنظیم شده باشد.<br/> - `"FailJob"` این اقدامی است که ممکن است هنگام شکست یک Pod انجام شود: Job مربوط به Pod به‌عنوان Failed علامت‌گذاری می‌شود و همه‌ی Podهای در حال اجرا خاتمه داده می‌شوند.<br/> - `"Ignore"` این اقدامی است که ممکن است هنگام شکست یک Pod انجام شود: شمارنده‌ی مربوط به .backoffLimit که با فیلد .status.failed در Job نمایش داده می‌شود، افزایش نمی‌یابد و یک Pod جایگزین ایجاد می‌شود.</td>
    </tr>
    <tr>
      <td><code>onExitCodes</code><br/><em><a href="{{< ref "#PodFailurePolicyOnExitCodesRequirement" >}}">PodFailurePolicyOnExitCodesRequirement</a></em></td>
      <td>الزام مربوط به کدهای خروج کانتینر را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>onPodConditions</code><br/><em><a href="{{< ref "#PodFailurePolicyOnPodConditionsPattern" >}}">PodFailurePolicyOnPodConditionsPattern array</a></em></td>
      <td>الزام مربوط به شرط‌های Pod را نشان می‌دهد. این الزام به‌صورت فهرستی از الگوهای شرط Pod بیان می‌شود. اگر دست‌کم یک الگو با یک شرط واقعی Pod مطابقت داشته باشد، الزام برآورده شده است. حداکثر ۲۰ عنصر مجاز است.</td>
    </tr>
  </tbody>
</table>


## SuccessPolicy {#SuccessPolicy}

SuccessPolicy توصیف می‌کند که یک Job بر اساس موفقیت برخی اندیس‌ها چه زمانی می‌تواند موفق اعلام شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>rules</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SuccessPolicyRule" >}}">SuccessPolicyRule array</a></em></td>
      <td>rules فهرست قواعد جایگزین را برای اعلام موفقیت Jobها پیش از برقراری `.status.succeeded >= .spec.completions` نشان می‌دهد. به‌محض برآورده شدن هر یک از قواعد، شرط "SuccessCriteriaMet" اضافه می‌شود و Podهای باقی‌مانده حذف می‌شوند. وضعیت نهایی چنین Jobی شرط "Complete" را دارد. افزون بر این، این قواعد به‌ترتیب ارزیابی می‌شوند؛ به‌محض اینکه Job یکی از قواعد را برآورده کند، قواعد دیگر نادیده گرفته می‌شوند. حداکثر ۲۰ عنصر مجاز است.</td>
    </tr>
  </tbody>
</table>

## SuccessPolicyRule {#SuccessPolicyRule}

SuccessPolicyRule قاعده‌ای را برای اعلام موفقیت یک Job توصیف می‌کند. هر قاعده باید دست‌کم یکی از فیلدهای &#34;succeededIndexes&#34; یا &#34;succeededCount&#34; را مشخص کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>succeededCount</code><br/><em>integer</em></td>
      <td>succeededCount حداقل اندازه‌ی لازم برای مجموعه‌ی واقعی ایندکس‌های موفق Job را مشخص می‌کند. هنگامی که succeededCount همراه با succeededIndexes استفاده شود، بررسی فقط به مجموعه ایندکس‌هایی محدود می‌شود که succeededIndexes مشخص کرده است. برای مثال، اگر succeededIndexes برابر "1-4"، مقدار succeededCount برابر "3" و ایندکس‌های تکمیل‌شده "1"، "3" و "5" باشند، Job موفق اعلام نمی‌شود، زیرا در این قاعده فقط ایندکس‌های "1" و "3" در نظر گرفته می‌شوند. اگر این فیلد null باشد، مقدار پیش‌فرضی ندارد و هرگز ارزیابی نمی‌شود. در صورت تعیین، مقدار آن باید یک عدد صحیح مثبت باشد.</td>
    </tr>
    <tr>
      <td><code>succeededIndexes</code><br/><em>string</em></td>
      <td>succeededIndexes مجموعه ایندکس‌هایی را مشخص می‌کند که باید در مجموعه‌ی واقعی ایندکس‌های موفق Job وجود داشته باشند. فهرست ایندکس‌ها باید در بازه‌ی 0 تا ".spec.completions-1" قرار گیرد و نباید عنصر تکراری داشته باشد. دست‌کم یک عنصر لازم است. ایندکس‌ها به‌صورت بازه‌هایی نمایش داده می‌شوند که با ویرگول از هم جدا شده‌اند. هر بازه می‌تواند یک عدد صحیح دهدهی یا یک جفت عدد صحیح دهدهی باشد که با خط تیره از هم جدا شده‌اند. اعداد پشت‌سرهم با عنصر اول و آخر دنباله و جداکننده‌ی خط تیره نمایش داده می‌شوند. برای مثال، اگر ایندکس‌های تکمیل‌شده 1، 3، 4، 5 و 7 باشند، به‌صورت "1,3-5,7" نمایش داده می‌شوند. اگر این فیلد null باشد، مقدار پیش‌فرضی ندارد و هرگز ارزیابی نمی‌شود.</td>
    </tr>
  </tbody>
</table>


## UncountedTerminatedPods {#UncountedTerminatedPods}

UncountedTerminatedPods شناسه‌های UID مربوط به Podهایی را نگهداری می‌کند که خاتمه یافته‌اند، اما هنوز در شمارنده‌های وضعیت Job به حساب نیامده‌اند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>failed</code><br/><em>string array</em></td>
      <td>failed شناسه‌های UID مربوط به Podهای ناموفق را نگهداری می‌کند.</td>
    </tr>
    <tr>
      <td><code>succeeded</code><br/><em>string array</em></td>
      <td>succeeded شناسه‌های UID مربوط به Podهای موفق را نگهداری می‌کند.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupAllDisruptionMode {#WorkloadPodGroupAllDisruptionMode}

WorkloadPodGroupAllDisruptionMode نشان می‌دهد که همه‌ی Podهای گروه باید با هم دچار اختلال (disruption) شوند.

<hr>



## WorkloadPodGroupBasicSchedulingPolicy {#WorkloadPodGroupBasicSchedulingPolicy}

WorkloadPodGroupBasicSchedulingPolicy رفتار استاندارد زمان‌بندی کوبرنتیز را نشان می‌دهد.

<hr>



## WorkloadPodGroupDisruptionMode {#WorkloadPodGroupDisruptionMode}

WorkloadPodGroupDisruptionMode تعیین می‌کند که Podهای منفرد درون یک گروه چگونه می‌توانند دچار اختلال شوند. دقیقاً یک حالت باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>all</code><br/><em><a href="{{< ref "#WorkloadPodGroupAllDisruptionMode" >}}">WorkloadPodGroupAllDisruptionMode</a></em></td>
      <td>all مشخص می‌کند که همه‌ی Podهای گروه باید با هم دچار اختلال شوند.</td>
    </tr>
    <tr>
      <td><code>single</code><br/><em><a href="{{< ref "#WorkloadPodGroupSingleDisruptionMode" >}}">WorkloadPodGroupSingleDisruptionMode</a></em></td>
      <td>single مشخص می‌کند که Podها می‌توانند مستقل از یکدیگر دچار اختلال شوند.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupGangSchedulingPolicy {#WorkloadPodGroupGangSchedulingPolicy}

WorkloadPodGroupGangSchedulingPolicy پارامترهای زمان‌بندی گروهی (gang یا همه‌یا‌هیچ) را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>minCount</code><br/><em>integer</em></td>
      <td>minCount حداقل تعداد Podهایی است که برای پذیرش کل گروه توسط زمان‌بند باید هم‌زمان زمان‌بندی شوند. این فیلد اختیاری است. اگر مشخص نشود، کنترل‌کننده باید یک مقدار پیش‌فرض معقول و متناسب با زمینه‌ی کاربرد را تزریق کند (برای مثال parallelism در یک Job). در صورت تعیین، مقدار آن باید یک عدد صحیح مثبت باشد.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupResourceClaim {#WorkloadPodGroupResourceClaim}

WorkloadPodGroupResourceClaim به یک درخواست منبع پویا (dynamic resource claim) اشاره می‌کند که میان Podهای گروه به اشتراک گذاشته می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name این درخواست منبع را در درون گروه به‌طور یکتا شناسایی می‌کند. این فیلد الزامی است و باید یک DNS_LABEL باشد.</td>
    </tr>
    <tr>
      <td><code>resourceClaimName</code><br/><em>string</em></td>
      <td>resourceClaimName نام یک آبجکت ResourceClaim در همان فضای نام است. این فیلد اختیاری است. اگر مشخص نشود، هیچ درخواست منبعی استفاده نمی‌شود. در صورت تعیین، مقدار آن باید یک زیردامنه‌ی DNS باشد.</td>
    </tr>
    <tr>
      <td><code>resourceClaimTemplateName</code><br/><em>string</em></td>
      <td>resourceClaimTemplateName نام یک آبجکت ResourceClaimTemplate در همان فضای نام است. این فیلد اختیاری است. اگر مشخص نشود، هیچ قالب درخواست منبعی استفاده نمی‌شود. در صورت تعیین، مقدار آن باید یک زیردامنه‌ی DNS باشد.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupSchedulingConstraints {#WorkloadPodGroupSchedulingConstraints}

WorkloadPodGroupSchedulingConstraints محدودیت‌های زمان‌بندی در سطح پایانی، مانند توپولوژی، را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>topology</code><br/><em><a href="{{< ref "../scheduling/pod-group-v1beta1#TopologyConstraint" >}}">TopologyConstraint array</a></em></td>
      <td>topology جایگذاری‌های توپولوژیک مطلوب را برای همه‌ی Podهای درون گروه Pod مشخص می‌کند. اگر تنظیم نشود، هیچ جایگذاری توپولوژیکی درخواست نمی‌شود.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupSchedulingPolicy {#WorkloadPodGroupSchedulingPolicy}

WorkloadPodGroupSchedulingPolicy سیاست زمان‌بندی گروهی از Podها را که یک کنترل‌کننده‌ی بار کاری مدیریت می‌کند، تعریف می‌کند. دقیقاً یک سیاست باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>basic</code><br/><em><a href="{{< ref "#WorkloadPodGroupBasicSchedulingPolicy" >}}">WorkloadPodGroupBasicSchedulingPolicy</a></em></td>
      <td>basic مشخص می‌کند که باید از رفتار استاندارد زمان‌بندی کوبرنتیز، یعنی زمان‌بندی Pod به Pod، استفاده شود.</td>
    </tr>
    <tr>
      <td><code>gang</code><br/><em><a href="{{< ref "#WorkloadPodGroupGangSchedulingPolicy" >}}">WorkloadPodGroupGangSchedulingPolicy</a></em></td>
      <td>gang معناشناسی زمان‌بندی همه‌یا‌هیچ را مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>


## WorkloadPodGroupSingleDisruptionMode {#WorkloadPodGroupSingleDisruptionMode}

WorkloadPodGroupSingleDisruptionMode نشان می‌دهد که Podهای منفرد می‌توانند مستقل از یکدیگر دچار اختلال شوند.

<hr>




## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /apis/batch/v1/namespaces/{namespace}/jobs


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده‌ی احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند، مرتبط است. طول این مقدار باید کمتر از ۱۲۸ نویسه یا برابر با آن باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های درخواست (POST/PUT/PATCH) که دارای فیلدهای ناشناخته یا تکراری هستند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای که بی‌سروصدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، جز آخرین مورد که رمزگشا (decoder) به آن می‌رسد، همه نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه‌ی v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد هشدار پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار در نسخه‌ی v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر هر فیلد ناشناخته‌ای قرار باشد از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه‌ی فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
      <td></td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /apis/batch/v1/namespaces/{namespace}/jobs/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده‌ی احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند، مرتبط است. طول این مقدار باید کمتر از ۱۲۸ نویسه یا برابر با آن باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (یعنی JsonPatch، MergePatch و StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های درخواست (POST/PUT/PATCH) که دارای فیلدهای ناشناخته یا تکراری هستند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای که بی‌سروصدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، جز آخرین مورد که رمزگشا (decoder) به آن می‌رسد، همه نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه‌ی v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد هشدار پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار در نسخه‌ی v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر هر فیلد ناشناخته‌ای قرار باشد از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه‌ی فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر مالکیت فیلدهای دارای تداخل را که در اختیار دیگران است، دوباره به دست می‌آورد. این پرچم برای درخواست‌های patch از نوع غیر apply باید تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

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


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### HTTP Request

PUT /apis/batch/v1/namespaces/{namespace}/jobs/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده‌ی احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند، مرتبط است. طول این مقدار باید کمتر از ۱۲۸ نویسه یا برابر با آن باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های درخواست (POST/PUT/PATCH) که دارای فیلدهای ناشناخته یا تکراری هستند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای که بی‌سروصدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، جز آخرین مورد که رمزگشا (decoder) به آن می‌رسد، همه نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه‌ی v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد هشدار پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار در نسخه‌ی v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر هر فیلد ناشناخته‌ای قرار باشد از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه‌ی فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
      <td></td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف

#### درخواست HTTP

DELETE /apis/batch/v1/namespaces/{namespace}/jobs/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه، پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح غیرمنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف به‌دلیل خطای آبجکت خراب با شکست مواجه شود، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) عدم امکان تبدیل داده‌های آن، برای مثال شکست در رمزگشایی، یا ب) شکست در رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیرین بازیابی کرد. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آبجکت‌های وابسته به‌صورت یتیم (orphan) رها شوند یا خیر. اگر true یا false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس مجموعه finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص همان منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم رها می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/batch/v1/namespaces/{namespace}/jobs


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی روی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است. این snapshot با نتایج فهرست قبلی سازگار نیست - آبجکت‌هایی که پس از درخواست فهرست اول ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند.  این فیلد هنگامی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه، پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح غیرمنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف به‌دلیل خطای آبجکت خراب با شکست مواجه شود، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) عدم امکان تبدیل داده‌های آن، برای مثال شکست در رمزگشایی، یا ب) شکست در رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیرین بازیابی کرد. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تعداد کمتری از آیتم‌های درخواست‌شده (حتی صفر آیتم) برگرداند و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد هنگامی که watch برابر true باشد پشتیبانی نمی‌شود.  سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده خواهد کرد. اگر آبجکت‌ها در طول یک فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اولین فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آبجکت‌های وابسته به‌صورت یتیم (orphan) رها شوند یا خیر. اگر true یا false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس مجموعه finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص همان منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم رها می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  مقدار پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  مقدار پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظارت را ارسال می‌کند.  هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا یک `resourceVersion` همسطح یا تازه‌تر از مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid برگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون تک‌نقل‌قول با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای هش ۶۴ بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز دارد feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار، بدون توجه به وجود یا نبود هرگونه فعالیت، مدت زمان فراخوانی را محدود می‌کند.</td>
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

GET /apis/batch/v1/namespaces/{namespace}/jobs/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### HTTP Request

GET /apis/batch/v1/namespaces/{namespace}/jobs


#### Path Parameters

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


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی سرور، سرور همراه با یک توکن continue با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. سرور با فهرستی پاسخ می‌دهد که از «کلید بعدی» آغاز می‌شود، اما از جدیدترین snapshot گرفته می‌شود و با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراپاده (metadata) فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است تعداد کمتری از موارد درخواستی (حتی صفر مورد) را بازگرداند و کلاینت‌ها برای تشخیص اینکه نتایج بیشتری وجود دارد یا نه، فقط باید به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت قطعه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌سازد درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌کوتیشن قرار می‌گیرند و پیشوند '0x' دارند. این دو به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash از نوع FNV-1a شصت‌وچهار بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "job-v1#JobList" >}}">JobList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست همه فضاهای نام (namespace)

#### درخواست HTTP

GET /apis/batch/v1/jobs



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله زمانی مشخصی بازگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد هنگامی که watch برابر true است پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تعداد کمتری از آیتم‌های درخواستی (حتی صفر آیتم) را بازگرداند، و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد هنگامی که watch برابر true است پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رویکرد گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست‌کردن تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که هنگام محاسبه نتیجه اولین فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌سازد یک درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. شدیداً توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌صورت «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (یای منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو شیء‌ریشه‌ای به سبک CEL (مثلاً "object.metadata.uid") استفاده می‌کنند، نه قالب fieldSelector (یعنی "metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لفظی CEL درون تک‌کوتیشن با پیشوند '0x' هستند که کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به 2 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "job-v1#JobList" >}}">JobList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### HTTP Request

GET /apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
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
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌ای مشخص برگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند در پاسخ گنجانده می‌شوند، مادامی که کلیدهایشان بعد از «کلید بعدی» باشد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست نخواهند داد.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) برگرداند و کلاینت‌ها برای تشخیص وجود نتایج بیشتر فقط باید به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده است در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، می‌تواند همه آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌کردن تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌صورت معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معناشناسی درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan   به معنای «داده‌هایی دست‌کم به‌روز به اندازه `resourceVersion` ارائه‌شده» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion` ای همگام شده باشد   که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است.   اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و   رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که   پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد،   خطای Invalid برگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و از قالب fieldSelector (یعنی "metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL داخل single-quote با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای hash 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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

#### HTTP Request

GET /apis/batch/v1/watch/namespaces/{namespace}/jobs


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی ارسال می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از یک پرس‌وجوی قبلی استفاده کنند، مشروط بر اینکه پارامترهای پرس‌وجو (به جز مقدار continue) کاملاً یکسان باشند؛ همچنین سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue خطای 410 ResourceExpired را برمی‌گرداند. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراوداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است باعث شود تعداد آیتم‌های برگردانده‌شده کمتر از مقدار درخواستی (حتی صفر) باشد، چنانچه همه آبجکت‌های درخواستی فیلتر شوند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، ویرایش یا حذف شده باشد در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلایلنتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه اولین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را بازتاب می‌دهند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، باید گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به اندازه `resourceVersion` ارائه‌شده جدید باشد»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار مشخص‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector (یعنی "metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل single-quote قرار می‌گیرند و با پیشوند '0x' شروع می‌شوند. آن‌ها کران پایین شامل‌شونده (inclusive) و کران بالای شامل‌نشونده (exclusive) را روی فضای hash ‏FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List All Namespaces

#### درخواست HTTP

`GET /apis/batch/v1/watch/jobs`



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به‌همراه یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است، پاسخ می‌دهد. این فهرست با نتایج قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از "کلید بعدی" باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تعداد آیتم‌هایی کمتر از مقدار درخواستی (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها برای تشخیص اینکه نتایج بیشتری وجود دارد یا نه، باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan   به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد»   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و   رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - در صورتی که `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد،   خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و نه قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لیترال CEL درون single-quote با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را روی فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به هرگونه فعالیت یا عدم فعالیت محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch Status

#### درخواست HTTP

`PATCH /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط است. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از فیلدهای تکراری، همه را به‌جز آخرین مورد که دیکودر با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و فقط آخرین مورد از فیلدهای تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest رد می‌کند. خطای بازگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. این یعنی کاربر فیلدهای دارای تعارض را که در مالکیت دیگران است دوباره در اختیار می‌گیرد. پرچم Force برای درخواست‌های patch غیر از apply باید تنظیم نشده باشد.</td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>


### `get` Read Status

#### درخواست HTTP

`GET /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Status

#### درخواست HTTP

`PUT /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Job</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط است. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از فیلدهای تکراری، همه را به‌جز آخرین مورد که دیکودر با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و فقط آخرین مورد از فیلدهای تکراری ماندگار می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest رد می‌کند. خطای بازگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
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
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "job-v1#Job" >}}">Job</a></em></td>
    </tr>
  </tbody>
</table>

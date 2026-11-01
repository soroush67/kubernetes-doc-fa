---
api_metadata:
  apiVersion: "apps/v1"
  import: "k8s.io/api/apps/v1"
  kind: "Deployment"
content_type: "api_reference"
description: "آبجکت Deployment امکان به‌روزرسانی اعلانی (declarative) Podها و ReplicaSetها را فراهم می‌کند."
title: "Deployment"
weight: 30
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

`apiVersion: apps/v1`

`import "k8s.io/api/apps/v1"`


## Deployment {#Deployment}

آبجکت Deployment امکان به‌روزرسانی اعلانی (declarative) Podها و ReplicaSetها را فراهم می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ (schema) نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointی که کلاینت درخواست‌ها را به آن می‌فرستد استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. مقدار آن به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فرادادهٔ استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#DeploymentSpec" >}}">DeploymentSpec</a></em></td>
      <td>مشخصات رفتار مطلوب Deployment.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#DeploymentStatus" >}}">DeploymentStatus</a></em></td>
      <td>آخرین وضعیت مشاهده‌شدهٔ Deployment.</td>
    </tr>
  </tbody>
</table>


## DeploymentSpec {#DeploymentSpec}

ساختار DeploymentSpec مشخصات رفتار مطلوب Deployment را تعیین می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>minReadySeconds</code><br/><em>integer</em></td>
      <td>حداقل تعداد ثانیه‌هایی که یک پاد تازه‌ایجادشده باید بدون از کار افتادن هیچ‌یک از کانتینرهایش در حالت آماده باقی بماند تا در دسترس (available) در نظر گرفته شود. مقدار پیش‌فرض 0 است (در این حالت، پاد به‌محض آماده شدن در دسترس در نظر گرفته می‌شود).</td>
    </tr>
    <tr>
      <td><code>paused</code><br/><em>boolean</em></td>
      <td>نشان می‌دهد که Deployment متوقف (paused) شده است.</td>
    </tr>
    <tr>
      <td><code>progressDeadlineSeconds</code><br/><em>integer</em></td>
      <td>حداکثر زمانی، بر حسب ثانیه، که یک Deployment برای پیشرفت فرصت دارد، پیش از آن‌که شکست‌خورده در نظر گرفته شود. کنترل‌کنندهٔ Deployment به پردازش Deploymentهای شکست‌خورده ادامه می‌دهد و یک شرط (condition) با دلیل ProgressDeadlineExceeded در وضعیت Deployment نمایش داده می‌شود. توجه کنید که در مدتی که Deployment متوقف است، پیشرفت آن ارزیابی نمی‌شود. مقدار پیش‌فرض 600 ثانیه است.</td>
    </tr>
    <tr>
      <td><code>replicas</code><br/><em>integer</em></td>
      <td>تعداد پادهای مطلوب. این فیلد یک اشاره‌گر است تا بتوان میان مقدار صفرِ صریح و مقدار مشخص‌نشده تمایز قائل شد. مقدار پیش‌فرض 1 است.</td>
    </tr>
    <tr>
      <td><code>revisionHistoryLimit</code><br/><em>integer</em></td>
      <td>تعداد ReplicaSetهای قدیمی که برای امکان بازگشت (rollback) نگه داشته می‌شوند. این فیلد یک اشاره‌گر است تا بتوان میان مقدار صفرِ صریح و مقدار مشخص‌نشده تمایز قائل شد. مقدار پیش‌فرض 10 است.</td>
    </tr>
    <tr>
      <td><code>selector</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>انتخابگر (selector) برچسب برای پادها. ReplicaSetهای موجودی که پادهایشان با این انتخابگر انتخاب شوند، همان‌هایی هستند که از این Deployment تأثیر می‌پذیرند. این انتخابگر باید با برچسب‌های قالب پاد مطابقت داشته باشد.</td>
    </tr>
    <tr>
      <td><code>strategy</code><br/><em><a href="{{< ref "deployment-v1#DeploymentStrategy" >}}">DeploymentStrategy</a></em><br/><em>راهبرد patch: retainKeys</em></td>
      <td>راهبرد استقراری که برای جایگزینی پادهای موجود با پادهای جدید به کار می‌رود.</td>
    </tr>
    <tr>
      <td><code>strategy.rollingUpdate</code><br/><em><a href="{{< ref "deployment-v1#RollingUpdateDeployment" >}}">RollingUpdateDeployment</a></em></td>
      <td>پارامترهای پیکربندی به‌روزرسانی غلتان (rolling update). این فیلد فقط زمانی وجود دارد که DeploymentStrategyType = RollingUpdate باشد.</td>
    </tr>
    <tr>
      <td><code>strategy.rollingUpdate.maxSurge</code><br/><em></em></td>
      <td>حداکثر تعداد پادهایی که می‌توان بیش از تعداد مطلوب پادها زمان‌بندی کرد. مقدار آن می‌تواند یک عدد مطلق (مثلاً 5) یا درصدی از پادهای مطلوب (مثلاً 10%) باشد. اگر MaxUnavailable برابر 0 باشد، این مقدار نمی‌تواند 0 باشد. عدد مطلق با گرد کردن درصد به سمت بالا محاسبه می‌شود. مقدار پیش‌فرض 25% است. مثال: اگر این مقدار 30% باشد، ReplicaSet جدید می‌تواند بلافاصله پس از شروع به‌روزرسانی غلتان مقیاس‌افزایی شود، به‌طوری که مجموع پادهای قدیمی و جدید از 130% پادهای مطلوب بیشتر نشود. پس از آن‌که پادهای قدیمی از بین رفتند، ReplicaSet جدید می‌تواند بیشتر مقیاس‌افزایی شود، به‌گونه‌ای که مجموع پادهای در حال اجرا در هر لحظه از به‌روزرسانی حداکثر 130% پادهای مطلوب باشد.</td>
    </tr>
    <tr>
      <td><code>strategy.rollingUpdate.maxUnavailable</code><br/><em></em></td>
      <td>حداکثر تعداد پادهایی که می‌توانند در طول به‌روزرسانی در دسترس نباشند. مقدار آن می‌تواند یک عدد مطلق (مثلاً 5) یا درصدی از پادهای مطلوب (مثلاً 10%) باشد. عدد مطلق با گرد کردن درصد به سمت پایین محاسبه می‌شود. اگر MaxSurge برابر 0 باشد، این مقدار نمی‌تواند 0 باشد. مقدار پیش‌فرض 25% است. مثال: اگر این مقدار 30% باشد، ReplicaSet قدیمی می‌تواند بلافاصله پس از شروع به‌روزرسانی غلتان تا 70% پادهای مطلوب مقیاس‌کاهی شود. پس از آن‌که پادهای جدید آماده شدند، ReplicaSet قدیمی می‌تواند بیشتر مقیاس‌کاهی شود و سپس ReplicaSet جدید مقیاس‌افزایی می‌شود، به‌گونه‌ای که مجموع پادهای در دسترس در تمام طول به‌روزرسانی دست‌کم 70% پادهای مطلوب باشد.</td>
    </tr>
    <tr>
      <td><code>strategy.type</code><br/><em>string</em></td>
      <td>نوع استقرار. مقدار آن می‌تواند "Recreate" یا "RollingUpdate" باشد. مقدار پیش‌فرض RollingUpdate است.<br/><br/>مقادیر ممکن enum:<br/> - `"Recreate"` پیش از ایجاد پادهای جدید، همهٔ پادهای موجود را از بین می‌برد.<br/> - `"RollingUpdate"` با استفاده از به‌روزرسانی غلتان، ReplicaSetهای قدیمی را با ReplicaSet جدید جایگزین می‌کند؛ یعنی ReplicaSetهای قدیمی را به‌تدریج مقیاس‌کاهی و ReplicaSet جدید را مقیاس‌افزایی می‌کند.</td>
    </tr>
    <tr>
      <td><code>template</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../core/pod-template-v1#PodTemplateSpec" >}}">PodTemplateSpec</a></em></td>
      <td>این قالب، پادهایی را که ایجاد خواهند شد توصیف می‌کند. تنها مقدار مجاز برای template.spec.restartPolicy، مقدار "Always" است.</td>
    </tr>
  </tbody>
</table>


## DeploymentStatus {#DeploymentStatus}

ساختار DeploymentStatus آخرین وضعیت مشاهده‌شدهٔ Deployment را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>availableReplicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهای در دسترسی که در حال خاتمه نیستند (دست‌کم به مدت minReadySeconds آماده بوده‌اند) و این Deployment آن‌ها را هدف گرفته است.</td>
    </tr>
    <tr>
      <td><code>collisionCount</code><br/><em>integer</em></td>
      <td>شمار برخوردهای هش (hash collision) برای Deployment. کنترل‌کنندهٔ Deployment هنگامی که باید نام جدیدترین ReplicaSet را بسازد، از این فیلد به‌عنوان سازوکاری برای جلوگیری از برخورد استفاده می‌کند.</td>
    </tr>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#DeploymentCondition" >}}">آرایه‌ای از DeploymentCondition</a></em><br/><em>راهبرد patch: ادغام (merge) بر اساس کلید <code>type</code></em></td>
      <td>آخرین مشاهدات موجود از وضعیت فعلی Deployment را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>نسلی (generation) که کنترل‌کنندهٔ Deployment مشاهده کرده است.</td>
    </tr>
    <tr>
      <td><code>readyReplicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهایی که در حال خاتمه نیستند، این Deployment آن‌ها را هدف گرفته است و شرط Ready دارند.</td>
    </tr>
    <tr>
      <td><code>replicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهایی که در حال خاتمه نیستند و این Deployment آن‌ها را هدف گرفته است (یعنی برچسب‌هایشان با انتخابگر مطابقت دارد).</td>
    </tr>
    <tr>
      <td><code>terminatingReplicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهای در حال خاتمه که این Deployment آن‌ها را هدف گرفته است. پادهای در حال خاتمه مقدار غیرتهی برای .metadata.deletionTimestamp دارند و مقدار .status.phase آن‌ها هنوز به Failed یا Succeeded نرسیده است. این یک فیلد بتا است و به فعال بودن قابلیت DeploymentReplicaSetTerminatingReplicas نیاز دارد (این قابلیت به‌طور پیش‌فرض فعال است).</td>
    </tr>
    <tr>
      <td><code>unavailableReplicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهای غیرقابل‌دسترسی که این Deployment آن‌ها را هدف گرفته است. این مقدار برابر با تعداد کل پادهایی است که هنوز لازم است تا Deployment به ظرفیت در دسترس 100% برسد. این پادها ممکن است پادهایی باشند که در حال اجرا هستند اما هنوز در دسترس نیستند، یا پادهایی که هنوز ایجاد نشده‌اند.</td>
    </tr>
    <tr>
      <td><code>updatedReplicas</code><br/><em>integer</em></td>
      <td>تعداد کل پادهایی که در حال خاتمه نیستند، این Deployment آن‌ها را هدف گرفته است و مشخصات قالب مطلوب را دارند.</td>
    </tr>
  </tbody>
</table>


## DeploymentList {#DeploymentList}

ساختار DeploymentList فهرستی از Deploymentها است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "deployment-v1#Deployment" >}}">آرایه‌ای از Deployment</a></em></td>
      <td>فیلد Items فهرست Deploymentها است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointی که کلاینت درخواست‌ها را به آن می‌فرستد استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. مقدار آن به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فرادادهٔ استاندارد فهرست.</td>
    </tr>
  </tbody>
</table>


## DeploymentCondition {#DeploymentCondition}

ساختار DeploymentCondition وضعیت یک Deployment را در یک لحظهٔ مشخص توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که شرط از یک وضعیت به وضعیت دیگر تغییر کرد.</td>
    </tr>
    <tr>
      <td><code>lastUpdateTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که این شرط به‌روزرسانی شد.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی خوانا برای انسان که جزئیات این تغییر وضعیت را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل آخرین تغییر وضعیت شرط.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em>string</em></td>
      <td>وضعیت شرط؛ یکی از مقادیر True، False یا Unknown.</td>
    </tr>
    <tr>
      <td><code>type</code><br/><em>string</em></td>
      <td>نوع شرط Deployment.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>


### `post` ایجاد

#### درخواست HTTP

POST /apis/apps/v1/namespaces/{namespace}/deployments


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آن‌که user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست بیش از این پردازش نمی‌شود. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی مرتبط با عامل یا موجودیتی است که این تغییرات را اعمال می‌کند. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل‌چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه برخورد کند. مقادیر معتبر عبارت‌اند از: - Ignore: همهٔ فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی را که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها روبه‌رو شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
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
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>

### `patch` وصله (Patch)

#### درخواست HTTP

`PATCH /apis/apps/v1/namespaces/{namespace}/deployments/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات مرتبط است. طول این مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همهٔ فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراریِ شناسایی‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر مالکیت فیلدهای متعارضی را که به دیگران تعلق دارند دوباره به دست می‌گیرد. برای درخواست‌های patch غیر از apply، پرچم Force نباید تنظیم شود.</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی

#### درخواست HTTP

`PUT /apis/apps/v1/namespaces/{namespace}/deployments/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات مرتبط است. طول این مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همهٔ فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراریِ شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف

#### درخواست HTTP

`DELETE /apis/apps/v1/namespaces/{namespace}/deployments/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان برحسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض (grace period) برای نوع مشخص‌شده استفاده می‌شود. اگر مشخص نشود، مقدار پیش‌فرضِ مختص هر آبجکت به کار می‌رود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) ناموفق شود، حذف ناایمن منبع را آغاز می‌کند. منبعی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً رمزگشایی آن‌ها ناموفق است، یا ب) واکدگذاری (decode) آن به یک آبجکت ناموفق است. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاریِ مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا و چگونه زباله‌روبی (garbage collection) انجام شود. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس finalizer موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - زباله‌روب وابسته‌ها را در پس‌زمینه حذف می‌کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد (Accepted)</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `delete`: حذف مجموعه

#### درخواست HTTP

DELETE /apis/apps/v1/namespaces/{namespace}/deployments


#### پارامترهای مسیر

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


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید دریافت فهرست را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایه‌ی آخرین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگشتی بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دوره‌ی مهلت پیش‌فرض برای نوع مشخص‌شده به کار می‌رود. در صورت مشخص نشدن، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب شکست بخورد، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً به دلیل شکست رمزگشایی، یا ب) تبدیل آن به یک آبجکت (decode) با شکست مواجه می‌شود. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگشتی بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی را که یک فراخوانی فهرست برمی‌گرداند تعیین می‌کند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه‌ی بعدی نتایج به کار برد. اگر همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌هایی کمتر از مقدار درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همه‌ی نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری وجود ندارد. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجه‌ی یک فراخوانی فهرست بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی تصویر لحظه‌ای سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه‌ی بسیار بزرگ استفاده می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت بخش‌بخش فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه‌ی 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد را تنظیم کرد یا PropagationPolicy را، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و به چه شکلی. می‌توان یا این فیلد را تنظیم کرد یا OrphanDependents را، اما نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض ویژه‌ی منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به جمع‌آوری‌کننده‌ی زباله اجازه داده می‌شود وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همه‌ی وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست را بتوان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخه‌ی منبع (ResourceVersion یا RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه‌ی `sendInitialEvents` تنظیم شده باشد، گزینه‌ی `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های برگشتی را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه‌ی هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object پیروی می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون نقل‌قول تکی و با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
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


### عملیات `get`: خواندن

#### درخواست HTTP

GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده‌ی احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get` برای فهرست

#### درخواست HTTP

GET /apis/apps/v1/namespaces/{namespace}/deployments


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوکمارک را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال بوکمارک‌ها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که بوکمارک‌ها در بازه‌های زمانی مشخصی برگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام بازیابی نتایج بیشتر از سرور، باید گزینهٔ continue را تنظیم کرد. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue یک نتیجهٔ پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت، سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از آخرین تصویر لحظه‌ای (snapshot) گرفته شده و با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، به شرطی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه همان پرس‌وجوی اولیه برای بازیابی مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، ویرایش یا حذف شده باشد، در درخواست‌های ادامهٔ بعدی گنجانده نمی‌شود. به این ویژگی گاهی تصویر لحظه‌ای سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت نتیجه‌ای بسیار بزرگ در تکه‌های کوچک‌تر استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوکمارک، ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی نسخهٔ ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت برابر false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های برگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش استفاده می‌شود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object پیروی می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL داخل نقل‌قول تکی و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالایِ غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) فراخوانی list/watch. این مقدار، مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "deployment-v1#DeploymentList" >}}">DeploymentList</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get`: فهرست‌گیری در همهٔ فضاهای نام

#### درخواست HTTP

GET /apis/apps/v1/deployments



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ آخرین اسنپ‌شات است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) که فهرست آبجکت‌های بازگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری که فهرست آبجکت‌های بازگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست با مقداری پر می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است به بازگشت مواردی کمتر از تعداد درخواست‌شده (حتی صفر مورد) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند که در این صورت همهٔ نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ صدور یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این وضعیت اسنپ‌شات سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>مقدار `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (یای منطقی) برای تعیین یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object پیروی می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "deployment-v1#DeploymentList" >}}">DeploymentList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` پایش (Watch)

#### درخواست HTTP

GET /apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده‌ی مجوزدهی، برای مثال برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmarkها را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی روی سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از آخرین اسنپ‌شات (snapshot) تهیه شده است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سوی سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه همان پرس‌وجوی اولیه برای دریافت مجموعه‌ی بعدی نتایج به کار برد. اگر همه‌ی آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است تعدادی کمتر از مقدار درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با نتیجه‌ی یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی از این ویژگی با عنوان اسنپ‌شات سازگار یاد می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجه‌ی بسیار بزرگ استفاده می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان‌دهنده‌ی یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت پایش را ارسال می‌کند. وقتی گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به‌صورت «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازه‌ی هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود هرگونه فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get` برای Watch List

#### درخواست HTTP

GET /apis/apps/v1/watch/namespaces/{namespace}/deployments


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوکمارک (bookmark) را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند، و ارسال بوکمارک‌ها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوکمارک‌ها در بازه‌های زمانی مشخصی بازگردانده می‌شوند، و همچنین نباید فرض کنند که سرور در طول یک نشست (session) حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) را به کار ببرند، و سرور ممکن است مقدار continue‌ای را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما از جدیدترین اسنپ‌شات (snapshot) گرفته شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آن‌که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از مقدار درخواستی (حتی صفر مورد) بازگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص موجودبودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری موجود نیست. اگر watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی اسنپ‌شات سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر این‌که user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه روی فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>گزینهٔ `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوکمارک، ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌معنای «داده‌هایی دست‌کم به جدیدیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص‌کردن یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را روی فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌کردن feature gate ‏ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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

### `get` پایش فهرست در همهٔ فضاهای نام

#### درخواست HTTP

`GET /apis/apps/v1/watch/deployments`



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوک‌مارک‌ها را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند. ارسال بوک‌مارک‌ها نیز به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوک‌مارک‌ها در بازهٔ زمانی مشخصی بازگردانده می‌شوند. همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. این مقدار را سرور تعریف می‌کند. بنابراین کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) را به کار ببرند، و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند. در این حالت، سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود. این فهرست بر پایهٔ آخرین snapshot ساخته می‌شود و با نتایج فهرست قبلی سازگار نیست. یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند، در صورتی در پاسخ گنجانده می‌شوند که کلیدشان پس از «کلید بعدی» باشد. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سوی سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در متادیتای فهرست مقداردهی می‌کند. با این مقدار و همان کوئری اولیه می‌توان مجموعهٔ بعدی نتایج را دریافت کرد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، ممکن است با تنظیم limit تعداد آیتم‌های بازگردانده‌شده کمتر از مقدار درخواستی باشد (حتی صفر). بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را بازگردانند. اگر limit مشخص شده و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. اگر watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که با استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد و بدون limit یکسان باشند. یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، اصلاح یا حذف شده باشد، در درخواست‌های بعدی continue گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود. این ویژگی تضمین می‌کند کلاینتی که با limit نتیجه‌ای بسیار بزرگ را در بخش‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که هنگام محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی با قالب‌بندی خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion تعیین می‌کند که درخواست را می‌توان بر اساس کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازتولید کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوک‌مارک مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات آبجکت‌های تحت پایش (پس از RV) را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این شرح است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود. در این حالت، رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` همگام‌سازی شده باشد که دست‌کم به تازگی نسخهٔ ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود. در این صورت، رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام‌سازی شده باشد.<br/> - اگر `resourceVersionMatch` به هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد، مقدار پیش‌فرض true است (به دلایل سازگاری با نسخه‌های قبلی). در غیر این صورت، مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (یای منطقی) یک یا چند بازهٔ هش را مشخص می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object پیروی می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی و با پیشوند '0x' هستند. این دو مقدار کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحلهٔ آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` وصله کردن وضعیت

#### درخواست HTTP

`PATCH /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی با قالب‌بندی خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. این مقدار باید حداکثر ۱۲۸ نویسه داشته باشد و فقط شامل نویسه‌های قابل چاپ طبق تعریف https://golang.org/pkg/unicode/#IsPrint باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که یافت می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 به بعد است. - Strict: اگر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگردانده‌شده از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را به‌صورت «اجباری» اعمال می‌کند. یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌گیرد. در درخواست‌های patch غیر از apply، پرچم Force نباید تنظیم شود.</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن وضعیت

#### درخواست HTTP

`GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی با قالب‌بندی خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزین کردن وضعیت

#### درخواست HTTP

`PUT /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Deployment</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنهٔ احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی با قالب‌بندی خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. این مقدار باید حداکثر ۱۲۸ نویسه داشته باشد و فقط شامل نویسه‌های قابل چاپ طبق تعریف https://golang.org/pkg/unicode/#IsPrint باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که یافت می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 به بعد است. - Strict: اگر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگردانده‌شده از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را شامل می‌شود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "deployment-v1#Deployment" >}}">Deployment</a></em></td>
    </tr>
  </tbody>
</table>

### خواندن Scale (`get`)

#### درخواست HTTP

متد و مسیر: `GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Scale</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
    </tr>
  </tbody>
</table>


### جایگزینی Scale (`put`)

#### درخواست HTTP

متد و مسیر: `PUT /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Scale</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره و ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست بیش از آن پردازش نمی‌شود. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهنده‌ی این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه به‌جز آخرین مورد نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه‌ی v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همه‌ی فیلدهای ناشناخته و تکراریِ یافت‌شده را در بر خواهد داشت.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
    </tr>
  </tbody>
</table>


### وصله کردن Scale (`patch`)

#### درخواست HTTP

متد و مسیر: `PATCH /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Scale</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه‌ی احراز هویت، مثلاً برای تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره و ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست بیش از آن پردازش نمی‌شود. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهنده‌ی این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه به‌جز آخرین مورد نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه‌ی v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همه‌ی فیلدهای ناشناخته و تکراریِ یافت‌شده را در بر خواهد داشت.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را به‌صورت «اجباری» اعمال می‌کند؛ یعنی کاربر مالکیت فیلدهای متعارضی را که در اختیار دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر از apply، این پرچم نباید تنظیم شود.</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "../definitions/scale-v1-autoscaling#Scale" >}}">Scale</a></em></td>
    </tr>
  </tbody>
</table>

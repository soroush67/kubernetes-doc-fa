---
api_metadata:
  apiVersion: "apiregistration.k8s.io/v1"
  import: "k8s.io/kube-aggregator/pkg/apis/apiregistration/v1"
  kind: "APIService"
content_type: "api_reference"
description: "آبجکت APIService نمایانگر یک سرور برای یک GroupVersion مشخص است. نام آن باید به شکل &#34;version.group&#34; باشد."
title: "APIService"
weight: 10
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

`apiVersion: apiregistration.k8s.io/v1`

`import "k8s.io/kube-aggregator/pkg/apis/apiregistration/v1"`


## APIService {#APIService}

آبجکت APIService نمایانگر یک سرور برای یک GroupVersion مشخص است. نام آن باید به شکل &#34;version.group&#34; باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره (schema) نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointای که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به شکل CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده (metadata) استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#APIServiceSpec" >}}">APIServiceSpec</a></em></td>
      <td>این فیلد شامل اطلاعات لازم برای یافتن یک سرور و برقراری ارتباط با آن است.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#APIServiceStatus" >}}">APIServiceStatus</a></em></td>
      <td>این فیلد شامل اطلاعات استنتاج‌شده درباره یک سرور API است.</td>
    </tr>
  </tbody>
</table>


## APIServiceSpec {#APIServiceSpec}

آبجکت APIServiceSpec شامل اطلاعات لازم برای یافتن یک سرور و برقراری ارتباط با آن است. فقط https پشتیبانی می‌شود، هرچند می‌توانید بررسی گواهی را غیرفعال کنید.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>caBundle</code><br/><em>string</em></td>
      <td>فیلد CABundle یک بسته CA با کدگذاری PEM است که برای اعتبارسنجی گواهی ارائه‌شده از سوی سرور API به کار می‌رود. اگر مشخص نشود، ریشه‌های اعتماد سیستمی روی apiserver استفاده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>group</code><br/><em>string</em></td>
      <td>نام گروه API که این سرور میزبان آن است.</td>
    </tr>
    <tr>
      <td><code>groupPriorityMinimum</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد GroupPriorityMinimum کمترین اولویتی است که این گروه باید داشته باشد. اولویت بالاتر به این معناست که کلاینت‌ها این گروه را بر گروه‌های با اولویت پایین‌تر ترجیح می‌دهند. توجه کنید که نسخه‌های دیگر این گروه ممکن است مقادیر GroupPriorityMinimum بالاتری مشخص کنند تا کل گروه اولویت بالاتری بگیرد. مرتب‌سازی اصلی بر اساس GroupPriorityMinimum و از بزرگ‌ترین عدد به کوچک‌ترین انجام می‌شود (۲۰ پیش از ۱۰). مرتب‌سازی ثانویه بر اساس مقایسه الفبایی نام آبجکت انجام می‌شود (v1.bar پیش از v1.foo). پیشنهاد ما چیزی شبیه این است: ‎*.k8s.io (به‌جز extensions) در مقدار ۱۸۰۰۰، و برای PaaSها (OpenShift، Deis) مقادیری در محدوده ۲۰۰۰ تا ۲۹۹۹ توصیه می‌شود.</td>
    </tr>
    <tr>
      <td><code>insecureSkipTLSVerify</code><br/><em>boolean</em></td>
      <td>فیلد InsecureSkipTLSVerify بررسی گواهی TLS را هنگام ارتباط با این سرور غیرفعال می‌کند. استفاده از آن به‌شدت توصیه نمی‌شود و به‌جای آن باید از CABundle استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>service</code><br/><em><a href="{{< ref "#ServiceReference" >}}">ServiceReference</a></em></td>
      <td>این فیلد ارجاعی به سرویس این سرور API است. ارتباط با این سرویس باید روی پورت ۴۴۳ برقرار شود. اگر مقدار Service برابر nil باشد، رسیدگی به groupversion این API به‌صورت محلی روی همین سرور انجام می‌شود؛ در این حالت فراخوانی به‌سادگی به زنجیره معمول handlerها واگذار می‌شود تا پاسخ داده شود.</td>
    </tr>
    <tr>
      <td><code>version</code><br/><em>string</em></td>
      <td>نسخه API که این سرور میزبان آن است؛ برای مثال "v1".</td>
    </tr>
    <tr>
      <td><code>versionPriority</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>فیلد VersionPriority ترتیب این نسخه API را درون گروه آن تعیین می‌کند و باید بزرگ‌تر از صفر باشد. مرتب‌سازی اصلی بر اساس VersionPriority و از بزرگ‌ترین به کوچک‌ترین انجام می‌شود (۲۰ پیش از ۱۰). از آنجا که این مقدار درون یک گروه سنجیده می‌شود، می‌تواند عدد کوچکی باشد، احتمالاً در حد ده‌ها. در صورت برابر بودن اولویت نسخه‌ها، از رشته نسخه برای محاسبه ترتیب درون گروه استفاده می‌شود. اگر رشته نسخه «شبیه کوبرنتیز» (kube-like) باشد، بالاتر از رشته‌های نسخه غیر kube-like قرار می‌گیرد؛ رشته‌های غیر kube-like به ترتیب واژه‌نامه‌ای مرتب می‌شوند. نسخه‌های kube-like با یک "v" شروع می‌شوند، سپس یک عدد (نسخه اصلی) می‌آید و پس از آن، به‌صورت اختیاری، رشته "alpha" یا "beta" و یک عدد دیگر (نسخه فرعی) قرار می‌گیرد. این نسخه‌ها ابتدا به ترتیب GA > beta > alpha مرتب می‌شوند (GA نسخه‌ای است که پسوندی مانند beta یا alpha ندارد) و سپس بر اساس مقایسه نسخه اصلی و پس از آن نسخه فرعی مرتب می‌شوند. نمونه‌ای از فهرست مرتب‌شده نسخه‌ها: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.</td>
    </tr>
  </tbody>
</table>


## APIServiceStatus {#APIServiceStatus}

آبجکت APIServiceStatus شامل اطلاعات استنتاج‌شده درباره یک سرور API است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#APIServiceCondition" >}}">APIServiceCondition array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>وضعیت فعلی سرویس apiService.</td>
    </tr>
  </tbody>
</table>


## APIServiceList {#APIServiceList}

آبجکت APIServiceList فهرستی از آبجکت‌های APIService است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService array</a></em></td>
      <td>فهرست آبجکت‌های APIService.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointای که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به شکل CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
  </tbody>
</table>


## APIServiceCondition {#APIServiceCondition}

آبجکت APIServiceCondition وضعیت یک APIService را در یک لحظه مشخص توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که این شرط از یک وضعیت به وضعیت دیگر تغییر کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی خوانا برای انسان که جزئیات آخرین تغییر وضعیت را شرح می‌دهد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل یکتا، تک‌کلمه‌ای و به شکل CamelCase برای آخرین تغییر وضعیت این شرط.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>وضعیت این شرط است و می‌تواند True، False یا Unknown باشد.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع این شرط است.</td>
    </tr>
  </tbody>
</table>


## ServiceReference {#ServiceReference}

آبجکت ServiceReference ارجاعی به Service.legacy.k8s.io را در خود نگه می‌دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام سرویس است.</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>فضای نام (namespace) سرویس است.</td>
    </tr>
    <tr>
      <td><code>port</code><br/><em>integer</em></td>
      <td>در صورت مشخص شدن، پورتی از سرویس است که webhook روی آن میزبانی می‌شود. برای حفظ سازگاری با نسخه‌های قبلی، مقدار پیش‌فرض آن ۴۴۳ است. مقدار `port` باید یک شماره پورت معتبر (از ۱ تا ۶۵۵۳۵، با احتساب هر دو) باشد.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>


### ایجاد (`post`)

#### درخواست HTTP

POST /apis/apiregistration.k8s.io/v1/apiservices



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره و ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل اجرای آزمایشی (dry run) پردازش می‌شوند.</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف شود نادیده گرفته می‌شود و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگردانده‌شده از سوی سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>


### وصله (`patch`)

#### درخواست HTTP

PATCH /apis/apiregistration.k8s.io/v1/apiservices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره و ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل اجرای آزمایشی پردازش می‌شوند.</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف شود نادیده گرفته می‌شود و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگردانده‌شده از سوی سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را به‌صورت «اجباری» اعمال می‌کند؛ یعنی کاربر مالکیت فیلدهای متعارضی را که در اختیار دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر apply، این پرچم نباید تنظیم شود.</td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>

### `put` جایگزینی

#### درخواست HTTP

PUT /apis/apiregistration.k8s.io/v1/apiservices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض آن 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید به‌طور ماندگار ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به بازگرداندن پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: با این مقدار، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: با این مقدار، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که مشاهده می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و نسخه‌های بعدی است. - Strict: با این مقدار، اگر هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراریِ مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف

#### درخواست HTTP

DELETE /apis/apiregistration.k8s.io/v1/apiservices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض آن 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید به‌طور ماندگار ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به بازگرداندن پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمانی برحسب ثانیه که پیش از حذف آبجکت باید سپری شود. این مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت (grace period) پیش‌فرضِ نوع مشخص‌شده استفاده می‌شود. اگر مشخص نشود، مقدار پیش‌فرض آن مقداری مختص هر آبجکت است. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) ناموفق شود، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیربنایی بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نباشد، برای مثال رمزگشایی آن ناموفق باشد، یا ب) تبدیل آن به یک آبجکت (decode) ناموفق باشد. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، از بررسی‌های پیش‌شرط صرف‌نظر می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاریِ مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر مقدار آن true یا false باشد، finalizer «orphan» به‌ترتیب به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و اگر انجام می‌شود، به چه شیوه‌ای. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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

### حذف مجموعه (`delete`)

#### درخواست HTTP

DELETE /apis/apiregistration.k8s.io/v1/apiservices



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ آخرین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) که فهرست آبجکت‌های بازگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. مقدار پیش‌فرض آن، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت (grace period) پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) با شکست مواجه شود، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) decode کردن آن به یک آبجکت با شکست مواجه می‌شود. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری که فهرست آبجکت‌های بازگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. مقدار پیش‌فرض آن، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست به مقداری تنظیم می‌کند که می‌توان از آن همراه با همان پرس‌وجوی اولیه برای بازیابی دستهٔ بعدی نتایج استفاده کرد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی واحد فهرست بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی تصویر لحظه‌ای سازگار گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و چگونه. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بسازد. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند.  هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام‌سازی شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام‌سازی شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود.  مقدار پیش‌فرض در صورت `resourceVersion=""` یا `resourceVersion="0"` (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازهٔ hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (برای نمونه "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالای (غیرشامل) را در فضای hash ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت‌زمان فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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


### خواندن (`get`)

#### درخواست HTTP

GET /apis/apiregistration.k8s.io/v1/apiservices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>

### فهرست کردن با `get`

#### درخواست HTTP

GET /apis/apiregistration.k8s.io/v1/apiservices



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
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند، و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌ی زمانی مشخصی بازگردانده می‌شوند، و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند، و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایه‌ی آخرین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست. یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) که فهرست آبجکت‌های بازگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. به‌طور پیش‌فرض همه‌چیز بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری که فهرست آبجکت‌های بازگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. به‌طور پیش‌فرض همه‌چیز بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت دسته‌ی بعدی نتایج به کار برد. اگر همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است به بازگرداندن مواردی کمتر از تعداد درخواستی (حتی صفر مورد) منجر شود؛ بنابراین کلاینت‌ها باید فقط با بررسی وجود فیلد continue تشخیص دهند که آیا نتایج بیشتری در دسترس است یا نه. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجه‌ی یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی تصویر لحظه‌ای سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت یک نتیجه‌ی بسیار بزرگ در قطعه‌های کوچک‌تر از limit استفاده می‌کند، بتواند همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>مقدار `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) را برای آبجکت‌های تحت نظر ارسال می‌کند. هنگامی که گزینه‌ی `sendInitialEvents` تنظیم شده باشد، گزینه‌ی `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازه‌ی hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL (مثلاً "object.metadata.uid") استفاده می‌کنند، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای hash ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  نمونه‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
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
      <td><em><a href="{{< ref "api-service-v1#APIServiceList" >}}">APIServiceList</a></em></td>
    </tr>
  </tbody>
</table>

### دیدبانی (Watch) با `get`

#### درخواست HTTP

GET /apis/apiregistration.k8s.io/v1/watch/apiservices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند. ارسال bookmarkها نیز به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی برگردانده می‌شوند. همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>برای دریافت نتایج بیشتر از سرور باید گزینه‌ی continue را تنظیم کرد. این مقدار را سرور تعیین می‌کند. بنابراین کلاینت‌ها فقط می‌توانند از مقدار continue به‌دست‌آمده از نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند. سرور نیز ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. سرور در این حالت فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایه‌ی آخرین snapshot ساخته شده و با نتایج فهرست قبلی سازگار نیست. یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، در صورتی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند تا هیچ تغییری از دستشان نرود.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی را تعیین می‌کند که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست با مقداری پر می‌کند. می‌توان از این مقدار همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه‌ی بعدی نتایج استفاده کرد. اگر همه‌ی آبجکت‌های درخواستی فیلتر شوند، ممکن است با تعیین limit تعداد آیتم‌های برگردانده‌شده کمتر از تعداد درخواستی (حتی صفر) باشد. بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجه‌ی یک فراخوانی list واحد بدون limit یکسان باشند. یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌ی بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود. این ویژگی تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجه‌ی بسیار بزرگ را در بخش‌های کوچک‌تر دریافت می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که پاسخ یک درخواست از کدام نسخه‌های منبع می‌تواند ارائه شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض، تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض، تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند. وقتی گزینه‌ی `sendInitialEvents` تنظیم شده باشد، گزینه‌ی `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، درخواست به‌صورت «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود. در این حالت، رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، درخواست به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد، مقدار پیش‌فرض (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های برگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازه‌ی hash به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object پیروی می‌کنند (برای نمونه "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول و با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (ناشامل) را در فضای hash ‏۶۴ بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای ناشامل برابر 2^64 است.  نمونه‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### پایش فهرست (`get`)

#### درخواست HTTP

GET /apis/apiregistration.k8s.io/v1/watch/apiservices



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>فیلد allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند. ارسال bookmarkها نیز به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی برگردانده می‌شوند. همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue را تنظیم کرد. از آنجا که سرور این مقدار را تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند. سرور نیز ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست list دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت، سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ آخرین اسنپ‌شات است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست list ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست با مقداری پر می‌کند که می‌توان آن را همراه همان کوئری اولیه برای دریافت دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواستی (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی اسنپ‌شات سازگار (consistent snapshot) می‌گویند. این ویژگی تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر، https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions را ببینید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر، https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions را ببینید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای ساختگی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد ساختگی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت پایش را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، باید گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای ناشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای ناشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کرد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### به‌روزرسانی جزئی وضعیت (`patch`)

#### درخواست HTTP

PATCH /apis/apiregistration.k8s.io/v1/apiservices/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیت ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید ۱۲۸ نویسه یا کمتر باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های درون درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که مشاهده می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest شکست می‌خورد. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>گزینهٔ Force درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر مالکیت فیلدهای دارای تعارض را که متعلق به دیگران است دوباره به دست می‌گیرد. در درخواست‌های patch غیر apply، پرچم Force نباید تنظیم شود.</td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>


### خواندن وضعیت (`get`)

#### درخواست HTTP

GET /apis/apiregistration.k8s.io/v1/apiservices/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>


### جایگزینی وضعیت (`put`)

#### درخواست HTTP

PUT /apis/apiregistration.k8s.io/v1/apiservices/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام APIService</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیت ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید ۱۲۸ نویسه یا کمتر باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌های درون درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که مشاهده می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest شکست می‌خورد. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
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
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "api-service-v1#APIService" >}}">APIService</a></em></td>
    </tr>
  </tbody>
</table>

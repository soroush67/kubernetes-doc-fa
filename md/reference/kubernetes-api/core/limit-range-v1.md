---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "LimitRange"
content_type: "api_reference"
description: "LimitRange محدودیت‌های استفاده از منابع را برای هر نوع منبع در یک Namespace تعیین می‌کند."
title: "LimitRange"
weight: 50
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


## LimitRange {#LimitRange}

LimitRange محدودیت‌های استفاده از منابع را برای هر نوع منبع در یک Namespace تعیین می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌هایش را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#LimitRangeSpec" >}}">LimitRangeSpec</a></em></td>
      <td>Spec محدودیت‌های اعمال‌شده را تعریف می‌کند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
  </tbody>
</table>


## LimitRangeSpec {#LimitRangeSpec}

LimitRangeSpec یک محدودیت حداقل/حداکثر استفاده را برای منابعی که با kind مطابقت دارند تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>limits</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#LimitRangeItem" >}}">LimitRangeItem array</a></em></td>
      <td>Limits فهرست آبجکت‌های LimitRangeItem است که اعمال می‌شوند.</td>
    </tr>
  </tbody>
</table>


## LimitRangeList {#LimitRangeList}

LimitRangeList فهرستی از آیتم‌های LimitRange است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange array</a></em></td>
      <td>Items فهرستی از آبجکت‌های LimitRange است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌هایش را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## LimitRangeItem {#LimitRangeItem}

LimitRangeItem یک محدودیت حداقل/حداکثر استفاده را برای هر منبعی که با kind مطابقت دارد تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>default</code><br/><em>object</em></td>
      <td>مقدار پیش‌فرض محدودیت نیازمندی منبع بر اساس نام منبع، در صورتی که محدودیت منبع مشخص نشده باشد.</td>
    </tr>
    <tr>
      <td><code>defaultRequest</code><br/><em>object</em></td>
      <td>DefaultRequest مقدار پیش‌فرض درخواست نیازمندی منبع بر اساس نام منبع است، در صورتی که درخواست منبع مشخص نشده باشد.</td>
    </tr>
    <tr>
      <td><code>max</code><br/><em>object</em></td>
      <td>محدودیت‌های حداکثر استفاده برای این kind بر اساس نام منبع.</td>
    </tr>
    <tr>
      <td><code>maxLimitRequestRatio</code><br/><em>object</em></td>
      <td>MaxLimitRequestRatio در صورت مشخص شدن، منبع نام‌برده باید هم درخواست (request) و هم محدودیت (limit) غیرصفر داشته باشد، به‌طوری که حاصل تقسیم محدودیت بر درخواست کوچک‌تر یا مساوی مقدار تعیین‌شده باشد؛ این مقدار بیشترین میزان burst را برای منبع نام‌برده نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>min</code><br/><em>object</em></td>
      <td>محدودیت‌های حداقل استفاده برای این kind بر اساس نام منبع.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع منبعی که این محدودیت برای آن اعمال می‌شود.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /api/v1/namespaces/{namespace}/limitranges


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
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را انجام می‌دهد مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرایند پاسخ هشدار استاندارد ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار پیش‌فرض در نسخه v1.23 به بعد است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل تمام فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /api/v1/namespaces/{namespace}/limitranges/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام LimitRange</td>
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
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را انجام می‌دهد مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرایند پاسخ هشدار استاندارد ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار پیش‌فرض در نسخه v1.23 به بعد است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل تمام فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر مالکیت فیلدهای دارای تداخل را که متعلق به دیگران است دوباره به دست می‌آورد. پرچم force برای درخواست‌های patch غیر از apply نباید تنظیم شود.</td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### HTTP Request

PUT /api/v1/namespaces/{namespace}/limitranges/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام LimitRange</td>
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
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر: - All: تمام مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را انجام می‌دهد مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق سرایند پاسخ هشدار استاندارد ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این مقدار پیش‌فرض در نسخه v1.23 به بعد است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل تمام فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف (Delete)

#### درخواست HTTP

DELETE /api/v1/namespaces/{namespace}/limitranges/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام LimitRange</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت (auth scope)، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت باید حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت مجاز پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را راه‌اندازی می‌کند. یک منبع در این موارد خراب در نظر گرفته می‌شود که بازیابی آن از ذخیره‌سازی زیرین با موفقیت انجام نشود، چون الف) داده‌های آن قابل تبدیل نیست، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) رمزگشایی آن به یک آبجکت ناموفق است. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط زمانی از آن استفاده کنید که دقیقاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس مجموعه finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص همان منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری است که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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


### `delete` حذف مجموعه (Delete Collection)

#### درخواست HTTP

DELETE /api/v1/namespaces/{namespace}/limitranges


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت (auth scope)، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت باید حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت مجاز پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را راه‌اندازی می‌کند. یک منبع در این موارد خراب در نظر گرفته می‌شود که بازیابی آن از ذخیره‌سازی زیرین با موفقیت انجام نشود، چون الف) داده‌های آن قابل تبدیل نیست، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) رمزگشایی آن به یک آبجکت ناموفق است. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط زمانی از آن استفاده کنید که دقیقاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را برگرداند، در حالتی که همه آبجکت‌های درخواست‌شده فیلتر شوند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا خیر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس مجموعه finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص همان منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری است که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan   به‌معنای «داده‌هایی دست‌کم به‌روز به اندازه `resourceVersion` ارائه‌شده» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion` ای همگام شده باشد   که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه باشد.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای   که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - `resourceVersionMatch` با هر مقدار دیگر یا تنظیم‌نشده   خطای Invalid برگردانده می‌شود.   مقدار پیش‌فرض: اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) true است و در غیر این صورت false.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal در CEL هستند که داخل تک‌نقل‌قول قرار می‌گیرند و پیشوند '0x' دارند؛ آن‌ها کران پایین (شامل) و کران بالای (غیرشامل) فضای هش 64 بیتی FNV-1a را تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و فعال بودن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت‌زمان فراخوانی را محدود می‌کند، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت.</td>
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


### `get` خواندن (Read)

#### درخواست HTTP

GET /api/v1/namespaces/{namespace}/limitranges/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام LimitRange</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت (auth scope)، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRange" >}}">LimitRange</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### درخواست HTTP

GET /api/v1/namespaces/{namespace}/limitranges


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


#### پارامترهای پرس‌وجو

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
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌ی زمانی مشخصی برگردانده می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه‌ی continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه‌ی یک پرس‌وجوی قبلی و با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار خود continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند، تا زمانی که کلیدشان بعد از "کلید بعدی" باشد، در پاسخ قرار می‌گیرند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادده‌ی فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه‌ی بعدی نتایج استفاده کرد. در صورتی که همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را برگرداند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌هایی که از یک فراخوانی فهرست واحد بدون limit به دست می‌آیند یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، اصلاح یا حذف شده باشد در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه‌ی بسیار بزرگ از limit استفاده می‌کند، همه‌ی آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه‌ی نتیجه‌ی اولین فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion در فراخوانی‌های فهرست چگونه اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. هنگامی که گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه‌ی مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه‌ی hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه‌ی object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لفظی CEL داخل single-quote با پیشوند '0x' هستند و به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash ‏FNV-1a ۶۴بیتی تعیین می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت زمان فراخوانی را، فارغ از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را دنبال می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRangeList" >}}">LimitRangeList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست همه فضاهای نام (namespace)

#### درخواست HTTP

GET /api/v1/limitranges



#### پارامترهای کوئری

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks درخواست می‌کند رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی ارسال می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند، و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی سرور، سرور همراه با یک توکن continue خطای 410 ResourceExpired برمی‌گرداند. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را از کلید بعدی و از جدیدترین snapshot برمی‌گرداند که با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ خواهند آمد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشند، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد آیتم‌هایی کمتر از مقدار درخواست‌شده (حتی صفر آیتم) برگرداند، در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر فقط باید به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، ویرایش یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی نمی‌آید. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اولین فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض برابر true است، اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل single-quote قرار می‌گیرند و پیشوند '0x' دارند؛ این دو به‌ترتیب کران پایین شمولی و کران بالای غیرشمولی را بر فضای هش FNV-1a شصت‌وچهار بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشمولی آن برابر 2^64 است.  نمونه‌ها:   تقسیم به ۲ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "limit-range-v1#LimitRangeList" >}}">LimitRangeList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /api/v1/watch/namespaces/{namespace}/limitranges/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام LimitRange</td>
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
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله زمانی مشخصی بازگردانده می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه با خطای 410 دریافت کرده ارسال کند؛ سرور با فهرستی که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده است، پاسخ می‌دهد. این فهرست با نتایج قبلی ناسازگار است؛ آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده شروع کنند، بدون اینکه تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی را مشخص می‌کند که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است باعث شود تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) بازگردانده شود؛ این اتفاق زمانی رخ می‌دهد که همه آبجکت‌های درخواست‌شده فیلتر شوند. به همین دلیل کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit بخش‌های کوچک‌تری از یک نتیجه بسیار بزرگ را دریافت می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌کردن تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از آن RV) در آبجکت‌های تحت نظر ارسال می‌شوند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌نقل‌قول قرار می‌گیرند و با پیشوند '0x' شروع می‌شوند؛ آن‌ها کران پایین شامل و کران بالای غیرشامل را بر فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و فعال‌کردن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
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

### `get` Watch List

#### درخواست HTTP

GET /api/v1/watch/namespaces/{namespace}/limitranges


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
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue مربوط به نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم بازگرداند (حتی صفر آیتم)؛ از این رو کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت یک نتیجه بسیار بزرگ در تکه‌های کوچک‌تر از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه اولین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را برای نسخه‌های منبعی تعیین می‌کند که درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` برابر NotOlderThan   به‌معنای «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با   `resourceVersion`ی همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای   که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد،   خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد، مقدار پیش‌فرض true است (به دلیل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های لفظی CEL درون single-quote با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را بر فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است و کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی فهرست/watch. این مقدار مدت فراخوانی را بدون توجه به فعالیت یا عدم فعالیت محدود می‌کند.</td>
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

### `get` فهرست Watch در همه فضاهای نام

#### درخواست HTTP

GET /api/v1/watch/limitranges



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی ارسال می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک پرس‌وجوی قبلی که پارامترهای آن (به‌جز مقدار continue) کاملاً یکسان است استفاده کنند و سرور می‌تواند مقدار continueای را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. سرور با فهرستی پاسخ می‌دهد که از «کلید بعدی» شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست؛ آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده می‌کند. اگر آبجکت‌ها در حین فهرست‌کردن تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود که resourceVersionMatch برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، مقداردهی شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را ایجاد می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌معنای «داده‌هایی که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشند» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions جدید است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص‌کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برند. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون single quote قرار می‌گیرند و پیشوند '0x' دارند. این مقادیر کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash ‏FNV-1a ۶۴ بیتی تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز دارد feature gate با نام ShardedListAndWatch فعال شود.</td>
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

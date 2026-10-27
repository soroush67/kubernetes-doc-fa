---
reviewers:
- chenopis
title: API کوبرنتیز
content_type: concept
weight: 40
description: >
  API کوبرنتیز به شما امکان می‌دهد وضعیت آبجکت‌ها در کوبرنتیز را پرس‌وجو و دستکاری کنید.
  هسته‌ی control plane کوبرنتیز، API server و HTTP APIای است که این سرور در دسترس قرار می‌دهد. کاربران، بخش‌های مختلف کلاستر شما و مؤلفه‌های خارجی همگی از طریق API server با یکدیگر ارتباط برقرار می‌کنند.
card:
  name: concepts
  weight: 30
---

<!-- overview -->

هسته‌ی {{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز،
{{< glossary_tooltip text="API server" term_id="kube-apiserver" >}} است. API server
یک HTTP API در دسترس قرار می‌دهد که به کاربران نهایی، بخش‌های مختلف کلاستر شما و
مؤلفه‌های خارجی امکان می‌دهد با یکدیگر ارتباط برقرار کنند.

API کوبرنتیز به شما امکان می‌دهد وضعیت آبجکت‌های API در کوبرنتیز را پرس‌وجو و دستکاری کنید
(برای مثال: Podها، Namespaceها، ConfigMapها و Eventها).

بیشتر عملیات را می‌توان از طریق رابط خط فرمان [kubectl](/docs/reference/kubectl/)
یا سایر ابزارهای خط فرمان، مانند
[kubeadm](/docs/reference/setup-tools/kubeadm/)، انجام داد که آن‌ها نیز به نوبه‌ی خود از API استفاده می‌کنند.
با این حال، می‌توانید با استفاده از فراخوانی‌های REST نیز مستقیماً به API دسترسی داشته باشید. کوبرنتیز
مجموعه‌ای از [کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/)
را برای کسانی فراهم می‌کند که می‌خواهند
با استفاده از API کوبرنتیز برنامه بنویسند.

هر کلاستر کوبرنتیز مشخصات APIهایی را که ارائه می‌کند منتشر می‌کند.
کوبرنتیز از دو سازوکار برای انتشار این مشخصات API استفاده می‌کند؛ هر دو سازوکار
برای فراهم‌کردن تعامل‌پذیری خودکار مفید هستند. برای مثال، ابزار `kubectl` مشخصات API را
برای فعال‌سازی تکمیل خودکار در خط فرمان و سایر قابلیت‌ها دریافت و در حافظه‌ی نهان ذخیره می‌کند.
دو سازوکار پشتیبانی‌شده به شرح زیر هستند:

- [Discovery API](#discovery-api) اطلاعاتی درباره‌ی APIهای کوبرنتیز ارائه می‌دهد:
  نام‌های API، منابع، نسخه‌ها و عملیات پشتیبانی‌شده. این اصطلاحی مختص
  کوبرنتیز است، زیرا این API از OpenAPI کوبرنتیز جدا است.
  هدف آن ارائه‌ی خلاصه‌ای کوتاه از منابع موجود است و جزئیات
  شِمای (schema) مشخص منابع را شرح نمی‌دهد. برای مرجع شِمای منابع،
  لطفاً به سند OpenAPI مراجعه کنید.

- [سند OpenAPI کوبرنتیز](#openapi-interface-definition) شِماهای (کامل)
  [OpenAPI v2.0 و 3.0](https://www.openapis.org/) را برای همه‌ی endpointهای API کوبرنتیز
ارائه می‌دهد.
  OpenAPI v3 روش ترجیحی برای دسترسی به OpenAPI است، زیرا
دیدی
  جامع‌تر و دقیق‌تر از API فراهم می‌کند. این سند همه‌ی مسیرهای API موجود
  و نیز همه‌ی منابعی را که در هر عملیات روی هر endpoint مصرف و تولید می‌شوند
  در بر می‌گیرد. همچنین شامل همه‌ی مؤلفه‌های توسعه‌پذیری است که یک کلاستر پشتیبانی می‌کند.
  این داده‌ها یک مشخصات کامل هستند و به‌طور قابل‌توجهی حجیم‌تر از داده‌های
  Discovery API هستند.

## Discovery API

کوبرنتیز فهرستی از همه‌ی نسخه‌های گروه (group version) و منابع پشتیبانی‌شده را از طریق
Discovery API منتشر می‌کند. این فهرست برای هر منبع شامل موارد زیر است:

- نام
- دامنه‌ی کلاستری یا مبتنی بر فضای نام (namespace)
- URL مربوط به endpoint و فعل‌های (verb) پشتیبانی‌شده
- نام‌های جایگزین
- گروه، نسخه، kind

این API هم به شکل تجمیع‌شده (aggregated) و هم به شکل تجمیع‌نشده (unaggregated) در دسترس است. discovery
تجمیع‌شده دو endpoint ارائه می‌کند، در حالی که discovery تجمیع‌نشده برای هر نسخه‌ی گروه
یک endpoint جداگانه ارائه می‌کند.

### discovery تجمیع‌شده

{{< feature-state feature_gate_name="AggregatedDiscoveryEndpoint" >}}

کوبرنتیز پشتیبانی پایدار از _discovery تجمیع‌شده_ را ارائه می‌دهد و
همه‌ی منابع پشتیبانی‌شده توسط یک کلاستر را از طریق دو endpoint (`/api` و
`/apis`) منتشر می‌کند. درخواست به این
endpoint تعداد درخواست‌هایی را که برای دریافت داده‌های
discovery از کلاستر ارسال می‌شوند به‌شدت کاهش می‌دهد. می‌توانید با
درخواست به endpointهای مربوطه همراه با سرآیند `Accept` که
منبع discovery تجمیع‌شده را مشخص می‌کند، به این داده‌ها دسترسی پیدا کنید:
`Accept: application/json;v=v2;g=apidiscovery.k8s.io;as=APIGroupDiscoveryList`.

اگر نوع منبع با استفاده از سرآیند `Accept` مشخص نشود، پاسخ پیش‌فرض
برای endpointهای `/api` و `/apis` یک سند discovery
تجمیع‌نشده است.

[سند discovery](https://github.com/kubernetes/kubernetes/blob/release-{{< skew currentVersion >}}/api/discovery/aggregated_v2.json)
مربوط به منابع داخلی را می‌توان در مخزن GitHub کوبرنتیز یافت.
در صورتی که کلاستر کوبرنتیزی برای پرس‌وجو در دسترس نباشد، می‌توان از این سند GitHub به‌عنوان مرجعی
برای مجموعه‌ی پایه‌ی منابع موجود استفاده کرد.

این endpoint از ETag و رمزگذاری protobuf نیز پشتیبانی می‌کند.

### discovery تجمیع‌نشده

بدون تجمیع discovery، اطلاعات discovery به‌صورت سطح‌بندی‌شده منتشر می‌شود؛ به این صورت که
endpointهای ریشه اطلاعات discovery مربوط به اسناد پایین‌دستی را منتشر می‌کنند.

فهرستی از همه‌ی نسخه‌های گروه که یک کلاستر پشتیبانی می‌کند، در
endpointهای `/api` و `/apis` منتشر می‌شود. نمونه:

```
{
  "kind": "APIGroupList",
  "apiVersion": "v1",
  "groups": [
    {
      "name": "apiregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "apiregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apps",
      "versions": [
        {
          "groupVersion": "apps/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apps/v1",
        "version": "v1"
      }
    },
    ...
}
```

برای دریافت سند discovery هر نسخه‌ی گروه، به درخواست‌های بیشتری به
`/apis/<group>/<version>` نیاز است (برای مثال:
`/apis/rbac.authorization.k8s.io/v1alpha1`) که فهرست
منابع ارائه‌شده ذیل یک نسخه‌ی گروه مشخص را اعلام می‌کند. kubectl از این endpointها
برای دریافت فهرست منابع پشتیبانی‌شده توسط یک کلاستر استفاده می‌کند.

<!-- body -->

<a id="#api-specification" />

## تعریف رابط OpenAPI

برای جزئیات درباره‌ی مشخصات OpenAPI، [مستندات OpenAPI](https://www.openapis.org/) را ببینید.

کوبرنتیز هم OpenAPI v2.0 و هم OpenAPI v3.0 را ارائه می‌کند. OpenAPI v3
روش ترجیحی برای دسترسی به OpenAPI است، زیرا بازنمایی جامع‌تر
(و بدون اتلاف) از منابع کوبرنتیز ارائه می‌دهد. به دلیل محدودیت‌های OpenAPI
نسخه‌ی ۲، برخی فیلدها از OpenAPI منتشرشده حذف می‌شوند؛ از جمله، اما نه محدود به،
`default`، `nullable` و `oneOf`.
### OpenAPI V2

API server کوبرنتیز یک مشخصات تجمیع‌شده‌ی OpenAPI v2 را از طریق
endpoint `/openapi/v2` ارائه می‌کند. می‌توانید قالب پاسخ را با استفاده از
سرآیندهای درخواست به شرح زیر درخواست کنید:

<table>
  <caption style="display:none">مقادیر معتبر سرآیند درخواست برای پرس‌وجوهای OpenAPI v2</caption>
  <thead>
     <tr>
        <th>سرآیند</th>
        <th style="min-width: 50%;">مقادیر ممکن</th>
        <th>توضیحات</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td><code>Accept-Encoding</code></td>
        <td><code>gzip</code></td>
        <td><em>ارسال‌نکردن این سرآیند نیز پذیرفتنی است</em></td>
     </tr>
     <tr>
        <td rowspan="3"><code>Accept</code></td>
        <td><code>application/com.github.proto-openapi.spec.v2@v1.0+protobuf</code></td>
        <td><em>عمدتاً برای استفاده‌ی درون‌کلاستری</em></td>
     </tr>
     <tr>
        <td><code>application/json</code></td>
        <td><em>پیش‌فرض</em></td>
     </tr>
     <tr>
        <td><code>*</code></td>
        <td><em>ارائه‌ی </em><code>application/json</code></td>
     </tr>
  </tbody>
</table>

{{< warning >}}
قواعد اعتبارسنجی‌ای که به‌عنوان بخشی از شِماهای OpenAPI منتشر می‌شوند ممکن است کامل نباشند و معمولاً هم کامل نیستند.
اعتبارسنجی‌های بیشتری درون API server انجام می‌شود. اگر بررسی دقیق و کامل می‌خواهید،
فرمان `kubectl apply --dry-run=server` همه‌ی اعتبارسنجی‌های قابل‌اعمال را اجرا می‌کند (و بررسی‌های
زمان پذیرش (admission) را نیز فعال می‌کند).
{{< /warning >}}

### OpenAPI V3

{{< feature-state feature_gate_name="OpenAPIV3" >}}

کوبرنتیز از انتشار توصیف APIهای خود به‌صورت OpenAPI v3 پشتیبانی می‌کند.

یک endpoint discovery با نشانی `/openapi/v3` فراهم شده است تا فهرست همه‌ی
گروه/نسخه‌های موجود را ببینید. این endpoint فقط JSON بازمی‌گرداند. این
گروه/نسخه‌ها در قالب زیر ارائه می‌شوند:

```yaml
{
    "paths": {
        ...,
        "api/v1": {
            "serverRelativeURL": "/openapi/v3/api/v1?hash=CC0E9BFD992D8C59AEC98A1E2336F899E8318D3CF4C68944C3DEC640AF5AB52D864AC50DAA8D145B3494F75FA3CFF939FCBDDA431DAD3CA79738B297795818CF"
        },
        "apis/admissionregistration.k8s.io/v1": {
            "serverRelativeURL": "/openapi/v3/apis/admissionregistration.k8s.io/v1?hash=E19CC93A116982CE5422FC42B590A8AFAD92CDE9AE4D59B5CAAD568F083AD07946E6CB5817531680BCE6E215C16973CD39003B0425F3477CFD854E89A9DB6597"
        },
        ....
    }
}
```
<!-- for editors: intentionally use yaml instead of json here, to prevent syntax highlight error. -->

URLهای نسبی به توصیف‌های تغییرناپذیر OpenAPI اشاره می‌کنند تا
ذخیره‌سازی در حافظه‌ی نهان سمت کلاینت بهبود یابد. API server برای همین منظور
سرآیندهای مناسب ذخیره‌سازی نهان HTTP را نیز تنظیم می‌کند (`Expires` به یک سال
بعد و `Cache-Control` به `immutable`). هنگامی که از یک URL منسوخ
استفاده شود، API server یک تغییر مسیر (redirect) به جدیدترین URL بازمی‌گرداند.

API server کوبرنتیز برای هر نسخه‌ی گروه کوبرنتیز، یک مشخصات OpenAPI v3 را
در endpoint `/openapi/v3/apis/<group>/<version>?hash=<hash>`
منتشر می‌کند.

برای سرآیندهای درخواست پذیرفته‌شده، به جدول زیر مراجعه کنید.

<table>
  <caption style="display:none">مقادیر معتبر سرآیند درخواست برای پرس‌وجوهای OpenAPI v3</caption>
  <thead>
     <tr>
        <th>سرآیند</th>
        <th style="min-width: 50%;">مقادیر ممکن</th>
        <th>توضیحات</th>
     </tr>
  </thead>
  <tbody>
     <tr>
        <td><code>Accept-Encoding</code></td>
        <td><code>gzip</code></td>
        <td><em>ارسال‌نکردن این سرآیند نیز پذیرفتنی است</em></td>
     </tr>
     <tr>
        <td rowspan="3"><code>Accept</code></td>
        <td><code>application/com.github.proto-openapi.spec.v3@v1.0+protobuf</code></td>
        <td><em>عمدتاً برای استفاده‌ی درون‌کلاستری</em></td>
     </tr>
     <tr>
        <td><code>application/json</code></td>
        <td><em>پیش‌فرض</em></td>
     </tr>
     <tr>
        <td><code>*</code></td>
        <td><em>ارائه‌ی </em><code>application/json</code></td>
     </tr>
  </tbody>
</table>

یک پیاده‌سازی به زبان Golang برای دریافت OpenAPI V3 در بسته‌ی
[`k8s.io/client-go/openapi3`](https://pkg.go.dev/k8s.io/client-go/openapi3) فراهم شده است.

کوبرنتیز {{< skew currentVersion >}}،
OpenAPI v2.0 و v3.0 را منتشر می‌کند؛ هیچ برنامه‌ای برای پشتیبانی از نسخه‌ی 3.1 در آینده‌ی نزدیک وجود ندارد.

### سریال‌سازی Protobuf

کوبرنتیز یک قالب سریال‌سازی جایگزین مبتنی بر Protobuf را پیاده‌سازی می‌کند که
عمدتاً برای ارتباطات درون‌کلاستری در نظر گرفته شده است. برای اطلاعات بیشتر
درباره‌ی این قالب، پیشنهاد طراحی [سریال‌سازی Protobuf در کوبرنتیز](https://git.k8s.io/design-proposals-archive/api-machinery/protobuf.md)
و فایل‌های
زبان تعریف رابط (IDL) هر شِما را ببینید که در بسته‌های Go
تعریف‌کننده‌ی آبجکت‌های API قرار دارند.

## ماندگاری

کوبرنتیز وضعیت سریال‌شده‌ی آبجکت‌ها را با نوشتن آن‌ها در
{{< glossary_tooltip term_id="etcd" >}} ذخیره می‌کند.

## گروه‌های API و نسخه‌بندی

برای آسان‌ترکردن حذف فیلدها یا بازسازی ساختار بازنمایی منابع،
کوبرنتیز از چندین نسخه‌ی API پشتیبانی می‌کند که هر کدام در مسیر API متفاوتی قرار دارند،
مانند `/api/v1` یا `/apis/rbac.authorization.k8s.io/v1alpha1`.

نسخه‌بندی در سطح API و نه در سطح منبع یا فیلد انجام می‌شود
تا اطمینان حاصل شود که API دیدی روشن و یکپارچه از منابع و رفتار سیستم
ارائه می‌دهد و نیز امکان کنترل دسترسی به APIهای پایان‌عمر و/یا
آزمایشی فراهم شود.

برای آسان‌ترکردن تکامل و گسترش API خود، کوبرنتیز
[گروه‌های API](/docs/reference/using-api/#api-groups) را پیاده‌سازی می‌کند که می‌توان آن‌ها را
[فعال یا غیرفعال کرد](/docs/reference/using-api/#enabling-or-disabling).

منابع API با گروه API، نوع منبع، فضای نام
(برای منابع مبتنی بر فضای نام) و نام خود از یکدیگر متمایز می‌شوند. API server تبدیل میان
نسخه‌های API را به‌صورت شفاف انجام می‌دهد: همه‌ی نسخه‌های مختلف در واقع بازنمایی‌هایی
از همان داده‌های ماندگار هستند. API server ممکن است همان داده‌های زیرین را
از طریق چندین نسخه‌ی API ارائه کند.

برای مثال، فرض کنید دو نسخه‌ی API، یعنی `v1` و `v1beta1`، برای یک
منبع واحد وجود داشته باشد. اگر آبجکتی را در ابتدا با استفاده از نسخه‌ی `v1beta1`
API آن ایجاد کرده باشید، می‌توانید بعداً آن آبجکت را با استفاده از نسخه‌ی `v1beta1`
یا نسخه‌ی `v1` API بخوانید، به‌روزرسانی یا حذف کنید، تا زمانی که نسخه‌ی `v1beta1` منسوخ و حذف شود.
از آن پس می‌توانید به دسترسی و تغییر آبجکت با استفاده از API نسخه‌ی `v1` ادامه دهید.

### تغییرات API

هر سیستم موفقی باید با پدیدآمدن موارد استفاده‌ی جدید یا تغییر موارد موجود، رشد کند و تغییر یابد.
بنابراین، کوبرنتیز API خود را طوری طراحی کرده است که به‌طور پیوسته تغییر کند و رشد یابد.
هدف پروژه‌ی کوبرنتیز این است که سازگاری با کلاینت‌های موجود را _نشکند_ و این
سازگاری را برای مدت زمانی حفظ کند تا پروژه‌های دیگر فرصت تطبیق داشته باشند.

به‌طور کلی، منابع جدید API و فیلدهای جدید منابع را می‌توان به‌دفعات و به‌طور مکرر اضافه کرد.
حذف منابع یا فیلدها مستلزم پیروی از
[سیاست منسوخ‌سازی API](/docs/reference/using-api/deprecation-policy/) است.

کوبرنتیز تعهدی قوی به حفظ سازگاری APIهای رسمی کوبرنتیز
پس از رسیدن به وضعیت دسترس‌پذیری عمومی (GA)، که معمولاً در نسخه‌ی API `v1` است، دارد. علاوه بر این،
کوبرنتیز سازگاری با داده‌هایی را که از طریق نسخه‌های _بتای_ APIهای رسمی کوبرنتیز ذخیره شده‌اند حفظ می‌کند
و تضمین می‌کند که وقتی قابلیت به وضعیت پایدار می‌رسد، این داده‌ها را بتوان از طریق نسخه‌های GA API تبدیل کرد و به آن‌ها دسترسی داشت.

اگر از یک نسخه‌ی بتای API استفاده کنید، پس از ارتقای آن API باید به نسخه‌ی بتای بعدی یا نسخه‌ی پایدار API
منتقل شوید. بهترین زمان برای این کار، دوره‌ای است که API بتا در دوره‌ی منسوخ‌سازی خود قرار دارد،
زیرا آبجکت‌ها هم‌زمان از طریق هر دو نسخه‌ی API قابل‌دسترسی هستند. هنگامی که دوره‌ی منسوخ‌سازی API بتا
به پایان برسد و دیگر ارائه نشود، باید از نسخه‌ی جایگزین API استفاده کرد.

{{< note >}}
اگرچه کوبرنتیز تلاش می‌کند سازگاری نسخه‌های _آلفای_ API را نیز حفظ کند، در برخی
شرایط این کار ممکن نیست. اگر از هر نسخه‌ی آلفای API استفاده می‌کنید، هنگام ارتقای کلاستر خود
یادداشت‌های انتشار کوبرنتیز را بررسی کنید، چرا که ممکن است API به شکلی ناسازگار
تغییر کرده باشد که حذف همه‌ی آبجکت‌های آلفای موجود پیش از ارتقا را الزامی کند.
{{< /note >}}

برای جزئیات بیشتر درباره‌ی تعاریف سطوح نسخه‌ی API، به
[مرجع نسخه‌های API](/docs/reference/using-api/#api-versioning) مراجعه کنید.

## گسترش API

API کوبرنتیز را می‌توان به یکی از دو روش زیر گسترش داد:

1. [منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
   به شما امکان می‌دهند به‌صورت اعلانی تعریف کنید که API server چگونه API منبع انتخابی شما را ارائه کند.
1. همچنین می‌توانید API کوبرنتیز را با پیاده‌سازی یک
   [لایه‌ی تجمیع (aggregation layer)](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) گسترش دهید.

## {{% heading "whatsnext" %}}

- بیاموزید که چگونه API کوبرنتیز را با افزودن
  [CustomResourceDefinition](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) خود گسترش دهید.
- [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) توضیح می‌دهد
  که کلاستر چگونه احراز هویت و مجوزدهی را برای دسترسی به API مدیریت می‌کند.
- با مطالعه‌ی [مرجع API](/docs/reference/kubernetes-api/)، با endpointهای API، انواع منابع و نمونه‌ها
  آشنا شوید.
- از طریق سند
  [تغییرات API](https://git.k8s.io/community/contributors/devel/sig-architecture/api_changes.md#readme) بیاموزید که چه چیزی یک تغییر سازگار به شمار می‌رود و چگونه می‌توان API را تغییر داد.

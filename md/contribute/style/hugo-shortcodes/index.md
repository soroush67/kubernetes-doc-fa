---
title: شورت‌کدهای سفارشی Hugo
content_type: concept
weight: 120
---

<!-- overview -->
این صفحه شورت‌کدهای سفارشی Hugo را توضیح می‌دهد که می‌توان از آن‌ها در مستندات Markdown کوبرنتیز استفاده کرد.

درباره شورت‌کدها بیشتر در [مستندات Hugo](https://gohugo.io/content-management/shortcodes) بخوانید.

<!-- body -->

## وضعیت ویژگی (Feature state) {#feature-state}

در یک صفحه Markdown (فایل `.md`) در این وب‌سایت می‌توانید یک شورت‌کد اضافه کنید تا
نسخه و وضعیت ویژگیِ مستندشده را نمایش دهد.

### نمونه نمایشی وضعیت ویژگی {#feature-state-demo}

در ادامه نمونه‌ای از قطعه کد وضعیت ویژگی آمده است که ویژگی را به‌صورت
پایدار در آخرین نسخه کوبرنتیز نمایش می‌دهد.

```
{{</* feature-state state="stable" */>}}
```

نتیجه نمایش:

{{< feature-state state="stable" >}}

مقادیر معتبر برای `state` عبارت‌اند از:

* alpha
* beta
* deprecated
* stable

### کد وضعیت ویژگی {#feature-state-code}

نسخه کوبرنتیزِ نمایش‌داده‌شده به‌صورت پیش‌فرض همان نسخه صفحه یا وب‌سایت است. می‌توانید
نسخه وضعیت ویژگی را با ارسال پارامتر `for_k8s_version` به شورت‌کد تغییر دهید. برای مثال:

```
{{</* feature-state for_k8s_version="v1.10" state="beta" */>}}
```

نتیجه نمایش:

{{< feature-state for_k8s_version="v1.10" state="beta" >}}

### دریافت وضعیت ویژگی از فایل توضیحات {#feature-state-retrieval-from-description-file}

برای تعیین پویای وضعیت ویژگی، از پارامتر `feature_gate_name` شورت‌کد استفاده کنید.
جزئیات وضعیت ویژگی از فایل توضیحات feature gate متناظر که در
`content/en/docs/reference/command-line-tools-reference/feature-gates/`
قرار دارد استخراج می‌شود.
برای مثال:

```
{{</* feature-state feature_gate_name="NodeSwap" */>}}
```

نتیجه نمایش:

{{< feature-state feature_gate_name="NodeSwap" >}}

## توضیحات feature gate {#feature-gate-description}

در یک صفحه Markdown (فایل `.md`) در این وب‌سایت می‌توانید یک شورت‌کد اضافه کنید تا
توضیحات یک شورت‌کد را نمایش دهد.

### نمونه نمایشی توضیحات feature gate {#feature-gate-description-demo}

در ادامه نمونه‌ای از قطعه کد وضعیت ویژگی آمده است که ویژگی را به‌صورت
پایدار در آخرین نسخه کوبرنتیز نمایش می‌دهد.

```
{{</* feature-gate-description name="DryRun" */>}}
```

نتیجه نمایش:

{{< feature-gate-description name="DryRun" >}}

## واژه‌نامه {#glossary}

دو شورت‌کد واژه‌نامه وجود دارد: `glossary_tooltip` و `glossary_definition`.

می‌توانید با یک شورت‌کد درج‌شونده به اصطلاحات واژه‌نامه ارجاع دهید؛ این شورت‌کد به‌صورت خودکار
محتوا را به‌روزرسانی می‌کند و با پیوندهای مربوط از [واژه‌نامه ما](/docs/reference/glossary/) جایگزین می‌کند.
وقتی نشانگر ماوس روی یک اصطلاح واژه‌نامه قرار می‌گیرد، مدخل واژه‌نامه یک راهنمای شناور (tooltip) نمایش می‌دهد.
اصطلاح واژه‌نامه همچنین به‌صورت پیوند نمایش داده می‌شود.

علاوه بر درج‌هایی که tooltip دارند، می‌توانید تعریف‌های واژه‌نامه را در
محتوای صفحه نیز بازاستفاده کنید.

داده خام اصطلاحات واژه‌نامه در
[دایرکتوری واژه‌نامه](https://github.com/kubernetes/website/tree/main/content/en/docs/reference/glossary)
نگهداری می‌شود و برای هر اصطلاح یک فایل محتوا وجود دارد.

### نمونه نمایشی واژه‌نامه {#glossary-demo}

برای مثال، درج زیر در Markdown به
{{< glossary_tooltip text="کلاستر" term_id="cluster" >}} همراه با یک tooltip تبدیل می‌شود:

```
{{</* glossary_tooltip text="cluster" term_id="cluster" */>}}
```

این یک تعریف کوتاه از واژه‌نامه است:

```
{{</* glossary_definition prepend="A cluster is" term_id="cluster" length="short" */>}}
```

که به این صورت نمایش داده می‌شود:
{{< glossary_definition prepend="A cluster is" term_id="cluster" length="short" >}}

همچنین می‌توانید تعریف کامل را درج کنید:

```
{{</* glossary_definition term_id="cluster" length="all" */>}}
```

که به این صورت نمایش داده می‌شود:
{{< glossary_definition term_id="cluster" length="all" >}}

## پیوند به مرجع API {#links-to-api-reference}

می‌توانید با استفاده از شورت‌کد `api-reference` به یک صفحه از مرجع API کوبرنتیز پیوند دهید؛ برای مثال به
مرجع {{< api-reference page="core/pod-v1" >}}:

```
{{</* api-reference page="core/pod-v1" */>}}
```

مقدار پارامتر `page` پسوند URL صفحه مرجع API است.


با مشخص کردن پارامتر `anchor` می‌توانید به یک محل مشخص در صفحه پیوند دهید؛
برای مثال به مرجع {{< api-reference page="core/pod-v1" anchor="PodSpec" >}}
یا به بخش {{< api-reference page="core/pod-v1" anchor="environment-variables" >}}
از صفحه:

```
{{</* api-reference page="core/pod-v1" anchor="PodSpec" */>}}
{{</* api-reference page="core/pod-v1" anchor="environment-variables" */>}}
```


با مشخص کردن پارامتر `text` می‌توانید متن پیوند را تغییر دهید؛
برای مثال با پیوند دادن به بخش
{{< api-reference page="core/pod-v1" anchor="environment-variables" text="Environment Variables">}}
از صفحه:

```
{{</* api-reference page="core/pod-v1" anchor="environment-variables" text="Environment Variable" */>}}
```

## عنوان جدول‌ها (Table captions) {#table-captions}

با افزودن عنوان به جدول می‌توانید دسترسی‌پذیری جدول‌ها را برای صفحه‌خوان‌ها بهبود دهید. برای افزودن
[caption](https://www.w3schools.com/tags/tag_caption.asp) به یک جدول،
جدول را درون شورت‌کد `table` قرار دهید و عنوان را با پارامتر `caption` مشخص کنید.

{{< note >}}
عنوان جدول‌ها برای صفحه‌خوان‌ها قابل مشاهده است، اما در نمایش استاندارد HTML نامرئی است.
{{< /note >}}

یک مثال:

```go-html-template
{{</* table caption="Configuration parameters" >}}
Parameter | Description | Default
:---------|:------------|:-------
`timeout` | The timeout for requests | `30s`
`logLevel` | The log level for log output | `INFO`
{{< /table */>}}
```

جدول نمایش‌داده‌شده به این شکل است:

{{< table caption="Configuration parameters" >}}
Parameter | Description | Default
:---------|:------------|:-------
`timeout` | The timeout for requests | `30s`
`logLevel` | The log level for log output | `INFO`
{{< /table >}}

اگر HTML جدول را بررسی کنید، باید این المان را بلافاصله
پس از المان آغازین `<table>` ببینید:

```html
<caption style="display: none;">Configuration parameters</caption>
```

## تب‌ها (Tabs) {#tabs}

در یک صفحه Markdown (فایل `.md`) در این وب‌سایت می‌توانید یک مجموعه تب اضافه کنید تا
گونه‌های مختلف یک راه‌حل را نمایش دهد.

شورت‌کد `tabs` این پارامترها را می‌پذیرد:

* `name`: نامی که روی تب نمایش داده می‌شود.
* `codelang`: اگر محتوای داخلی را به شورت‌کد `tab` بدهید، می‌توانید به Hugo بگویید
  برای هایلایت کردن از چه زبان کدی استفاده کند.
* `include`: فایلی که باید در تب درج شود. اگر تب در یک
  [leaf bundle](https://gohugo.io/content-management/page-bundles/#leaf-bundles) از Hugo قرار داشته باشد،
  فایل -- که می‌تواند هر نوع MIME پشتیبانی‌شده توسط Hugo باشد -- در خود bundle جست‌وجو می‌شود.
  در غیر این صورت، صفحه محتوایی که باید درج شود نسبت به صفحه جاری جست‌وجو می‌شود.
  توجه کنید که با `include` هیچ محتوای داخلی شورت‌کد ندارید و باید از
  نحو خودبسته (self-closing) استفاده کنید. برای مثال،
  `{{</* tab name="Content File #1" include="example1" /*/>}}`. زبان باید با
  `codelang` مشخص شود، در غیر این صورت زبان بر اساس نام فایل تعیین می‌شود.
  فایل‌های غیرمحتوایی به‌صورت پیش‌فرض هایلایت کد می‌شوند.
* اگر محتوای داخلی شما Markdown است، باید برای احاطه کردن تب از جداکننده `%` استفاده کنید.
  برای مثال، `{{%/* tab name="Tab 1" %}}This is **markdown**{{% /tab */%}}`
* می‌توانید گونه‌های ذکرشده در بالا را درون یک مجموعه تب با هم ترکیب کنید.

در ادامه نمونه‌ای از شورت‌کد tabs آمده است.

{{< note >}}
**نام** تب در تعریف `tabs` باید در یک صفحه محتوا یکتا باشد.
{{< /note >}}

### نمونه تب‌ها: هایلایت کد {#tabs-demo-code-highlighting}

```go-text-template
{{</* tabs name="tab_with_code" >}}
{{< tab name="Tab 1" codelang="bash" >}}
echo "This is tab 1."
{{< /tab >}}
{{< tab codelang="go" >}}
println "This is tab 2."
{{< /tab >}}
{{< /tabs */>}}
```

نتیجه نمایش:

{{< tabs name="tab_with_code" >}}
{{< tab name="Tab A" codelang="bash" >}}
echo "This is tab A."
{{< /tab >}}
{{< tab codelang="go" >}}
// If you don't set a tab name, the site supplies one.
println "This tab has a default name";
{{< /tab >}}
{{< /tabs >}}

### نمونه تب‌ها: Markdown و HTML درون‌خطی {#tabs-demo-inline-markdown-and-html}

```go-html-template
{{</* tabs name="tab_with_md" >}}
{{% tab name="Markdown" %}}
This is **some markdown.**
{{< note >}}
It can even contain shortcodes.
{{< /note >}}
{{% /tab %}}
{{< tab name="HTML" >}}
<div>
	<h3>Plain HTML</h3>
	<p>This is some <i>plain</i> HTML.</p>
</div>
{{< /tab >}}
{{< /tabs */>}}
```

نتیجه نمایش:

{{< tabs name="tab_with_md" >}}
{{% tab name="Markdown" %}}
This is **some markdown.**

{{< note >}}
It can even contain shortcodes.
{{< /note >}}

{{% /tab %}}
{{< tab name="HTML" >}}
<div>
	<h3>Plain HTML</h3>
	<p>This is some <i>plain</i> HTML.</p>
</div>
{{< /tab >}}
{{< /tabs >}}

### نمونه تب‌ها: درج فایل {#tabs-demo-file-include}

```go-text-template
{{</* tabs name="tab_with_file_include" >}}
{{< tab name="Content File #1" include="example1" />}}
{{< tab name="Content File #2" include="example2" />}}
{{< tab name="JSON File" include="podtemplate" />}}
{{< /tabs */>}}
```

نتیجه نمایش:

{{< tabs name="tab_with_file_include" >}}
{{< tab name="Content File #1" include="example1" />}}
{{< tab name="Content File #2" include="example2" />}}
{{< tab name="JSON File" include="podtemplate.json" />}}
{{< /tabs >}}

## فایل‌های کد منبع {#source-code-files}

می‌توانید از شورت‌کد `{{%/* code_sample */%}}` برای درج محتوای یک فایل در یک بلوک کد استفاده کنید تا کاربران بتوانند محتوای آن را دانلود یا در کلیپ‌بورد خود کپی کنند. این شورت‌کد زمانی به کار می‌رود که محتوای فایل نمونه عمومی و قابل استفاده مجدد باشد و بخواهید کاربران خودشان آن را امتحان کنند.

این شورت‌کد دو پارامتر نام‌دار می‌پذیرد: `language` و `file`. پارامتر اجباری `file` برای مشخص کردن مسیر فایلی که نمایش داده می‌شود استفاده می‌شود. پارامتر اختیاری `language` برای مشخص کردن زبان برنامه‌نویسی فایل به کار می‌رود. اگر پارامتر `language` ارائه نشود، شورت‌کد تلاش می‌کند زبان را بر اساس پسوند فایل حدس بزند.

برای مثال:

```none
{{%/* code_sample language="yaml" file="application/deployment-scale.yaml" */%}}
```

خروجی به این صورت است:

{{% code_sample language="yaml" file="application/deployment-scale.yaml" %}}

هنگام افزودن یک فایل نمونه جدید، مانند یک فایل YAML، فایل را در یکی از زیردایرکتوری‌های `<LANG>/examples/` ایجاد کنید، که `<LANG>` زبان صفحه است. در Markdown صفحه خود از شورت‌کد `code` استفاده کنید:

```none
{{%/* code_sample file="<RELATIVE-PATH>/example-yaml>" */%}}
```
که `<RELATIVE-PATH>` مسیر فایل نمونه‌ای است که باید درج شود، نسبت به دایرکتوری `examples`. شورت‌کد زیر به یک فایل YAML در مسیر `/content/en/examples/configmap/configmaps.yaml` ارجاع می‌دهد.

```none
{{%/* code_sample file="configmap/configmaps.yaml" */%}}
```

شورت‌کد قدیمی `{{%/* codenew */%}}` در حال جایگزینی با `{{%/* code_sample */%}}` است.
در مستندات جدید از `{{%/* code_sample */%}}` استفاده کنید (نه `{{%/* codenew */%}}` یا `{{%/* code */%}}`).

## نشانگر محتوای شخص ثالث {#third-party-content-marker}

اجرای کوبرنتیز به نرم‌افزارهای شخص ثالث نیاز دارد. برای مثال: معمولاً باید
یک [سرور DNS](/docs/tasks/administer-cluster/dns-custom-nameservers/#introduction)
به کلاستر خود اضافه کنید تا تفکیک نام (name resolution) کار کند.

وقتی به نرم‌افزار شخص ثالث پیوند می‌دهیم یا به‌گونه‌ای دیگر به آن اشاره می‌کنیم،
از [راهنمای محتوا](/docs/contribute/style/content-guide/) پیروی می‌کنیم
و آن موارد شخص ثالث را نیز علامت‌گذاری می‌کنیم.

استفاده از این شورت‌کدها یک سلب مسئولیت (disclaimer) به هر صفحه مستنداتی
که از آن‌ها استفاده می‌کند اضافه می‌کند.

### فهرست‌ها {#third-party-content-list}

برای فهرستی از چند مورد شخص ثالث، این را اضافه کنید:
```
{{%/* thirdparty-content */%}}
```
درست زیر عنوان بخشی که همه موارد را در بر می‌گیرد.

### موارد منفرد {#third-party-content-item}

اگر فهرستی دارید که بیشتر موارد آن به نرم‌افزارهای داخل پروژه اشاره می‌کنند (برای مثال:
خود کوبرنتیز و مؤلفه جداگانه
[Descheduler](https://github.com/kubernetes-sigs/descheduler))،
باید از شکل دیگری استفاده کنید.

شورت‌کد زیر را اضافه کنید:
```
{{%/* thirdparty-content single="true" */%}}
```

پیش از آن مورد، یا درست زیر عنوان آن مورد مشخص.

## جزئیات (Details) {#details}

می‌توانید با استفاده از یک شورت‌کد یک المان HTML به نام `<details>` را رندر کنید:

```markdown
{{</* details summary="More about widgets" */>}}
The frobnicator extension API implements _widgets_ using example running text.

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem.
{{</* /details */>}}
```

این به صورت زیر نمایش داده می‌شود:
{{< details summary="More about widgets" >}}
The frobnicator extension API implements _widgets_ using example running text.

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem.
{{< /details >}}

{{< note >}}
از این شورت‌کد کم استفاده کنید؛ معمولاً بهتر است همه متن مستقیماً به
خوانندگان نمایش داده شود.
{{< /note >}}

## رشته‌های نسخه {#version-strings}

برای تولید یک رشته نسخه جهت درج در مستندات، می‌توانید از میان
چند شورت‌کد نسخه انتخاب کنید. هر شورت‌کد نسخه، رشته‌ای را نمایش می‌دهد که از
مقدار یک پارامتر نسخه در فایل پیکربندی وب‌سایت، یعنی `hugo.toml`، به دست می‌آید.
دو پارامتر نسخه که بیشتر استفاده می‌شوند `latest` و `version` هستند.

### `{{</* param "version" */>}}`

شورت‌کد `{{</* param "version" */>}}` مقدار نسخه جاری
مستندات کوبرنتیز را از پارامتر وب‌سایت `version` تولید می‌کند.
شورت‌کد `param` نام یک پارامتر وب‌سایت را می‌پذیرد که در اینجا
`version` است.

{{< note >}}
در مستندات منتشرشده قبلی، مقادیر پارامترهای `latest` و `version`
یکسان نیستند. پس از انتشار یک نسخه جدید، `latest` افزایش می‌یابد
و مقدار `version` برای مجموعه مستندات بدون تغییر باقی می‌ماند. برای
مثال، یک نسخه منتشرشده قبلی از مستندات، `version`
را `v1.19` و `latest` را `v1.20` نمایش می‌دهد.
{{< /note >}}

نتیجه نمایش:

{{< param "version" >}}

### `{{</* latest-version */>}}`

شورت‌کد `{{</* latest-version */>}}` مقدار پارامتر وب‌سایت `latest` را برمی‌گرداند.
پارامتر `latest` هنگام انتشار نسخه جدید مستندات به‌روزرسانی می‌شود.
این پارامتر همیشه با مقدار `version` در یک مجموعه مستندات برابر نیست.

نتیجه نمایش:

{{< latest-version >}}

### `{{</* latest-semver */>}}`

شورت‌کد `{{</* latest-semver */>}}` مقدار `latest` را
بدون پیشوند «v» تولید می‌کند.

نتیجه نمایش:

{{< latest-semver >}}

### `{{</* version-check */>}}`

شورت‌کد `{{</* version-check */>}}` بررسی می‌کند که آیا پارامتر صفحه `min-kubernetes-server-version`
وجود دارد یا نه، و سپس از این مقدار برای مقایسه با `version` استفاده می‌کند.

نتیجه نمایش:

{{< version-check >}}

### `{{</* latest-release-notes */>}}`

شورت‌کد `{{</* latest-release-notes */>}}` یک رشته نسخه را
از `latest` تولید می‌کند و پیشوند «v» را حذف می‌کند. این شورت‌کد یک URL جدید برای
صفحه CHANGELOG یادداشت‌های انتشار با رشته نسخه اصلاح‌شده چاپ می‌کند.

نتیجه نمایش:

{{< latest-release-notes >}}


## {{% heading "whatsnext" %}}

* درباره [Hugo](https://gohugo.io/) بیاموزید.
* درباره [نوشتن یک موضوع جدید](/docs/contribute/style/write-new-topic/) بیاموزید.
* درباره [انواع محتوای صفحه](/docs/contribute/style/page-content-types/) بیاموزید.
* درباره [ایجاد یک pull request](/docs/contribute/new-content/open-a-pr/) بیاموزید.
* درباره [مشارکت پیشرفته](/docs/contribute/advanced/) بیاموزید.

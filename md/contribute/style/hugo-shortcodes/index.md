---
title: شورت‌کدهای سفارشی Hugo
content_type: concept
weight: 120
---

<!-- overview -->
این صفحه شورت‌کدهای (shortcode) سفارشی Hugo را توضیح می‌دهد که می‌توان از آن‌ها در مستندات Markdown کوبرنتیز استفاده کرد.

برای آشنایی بیشتر با شورت‌کدها، [مستندات Hugo](https://gohugo.io/content-management/shortcodes) را بخوانید.

<!-- body -->

## وضعیت قابلیت

در هر صفحهٔ Markdown (فایل `.md`) این وب‌سایت، می‌توانید یک شورت‌کد اضافه کنید تا نسخه و وضعیت قابلیتِ مستندشده نمایش داده شود.

### نمونهٔ نمایشی وضعیت قابلیت

در ادامه نمونه‌ای از قطعهٔ وضعیت قابلیت آمده است که قابلیت را در آخرین نسخهٔ کوبرنتیز، پایدار نشان می‌دهد.

```
{{</* feature-state state="stable" */>}}
```

خروجی آن چنین است:

{{< feature-state state="stable" >}}

مقادیر معتبر برای `state` عبارت‌اند از:

* alpha
* beta
* deprecated
* stable

### کد وضعیت قابلیت

نسخهٔ کوبرنتیزی که نمایش داده می‌شود، به‌طور پیش‌فرض نسخهٔ صفحه یا وب‌سایت است. با ارسال پارامتر `for_k8s_version` به شورت‌کد می‌توانید نسخهٔ وضعیت قابلیت را تغییر دهید. برای مثال:

```
{{</* feature-state for_k8s_version="v1.10" state="beta" */>}}
```

خروجی آن چنین است:

{{< feature-state for_k8s_version="v1.10" state="beta" >}}

### دریافت وضعیت قابلیت از فایل توضیحات

برای تعیین پویای وضعیت یک قابلیت، از پارامتر `feature_gate_name` در شورت‌کد استفاده کنید. جزئیات وضعیت قابلیت از فایل توضیحات feature gate متناظر استخراج می‌شود که در مسیر `content/en/docs/reference/command-line-tools-reference/feature-gates/` قرار دارد.
برای مثال:

```
{{</* feature-state feature_gate_name="NodeSwap" */>}}
```

خروجی آن چنین است:

{{< feature-state feature_gate_name="NodeSwap" >}}

## توضیحات feature gate

در هر صفحهٔ Markdown (فایل `.md`) این وب‌سایت، می‌توانید یک شورت‌کد اضافه کنید تا توضیحات یک شورت‌کد نمایش داده شود.

### نمونهٔ نمایشی توضیحات feature gate

در ادامه نمونه‌ای از قطعهٔ وضعیت قابلیت آمده است که قابلیت را در آخرین نسخهٔ کوبرنتیز، پایدار نشان می‌دهد.

```
{{</* feature-gate-description name="DryRun" */>}}
```

خروجی آن چنین است:

{{< feature-gate-description name="DryRun" >}}

## واژه‌نامه

دو شورت‌کد برای واژه‌نامه وجود دارد: `glossary_tooltip` و `glossary_definition`.

می‌توانید با یک درج (inclusion) به اصطلاحات واژه‌نامه ارجاع دهید. این درج به‌طور خودکار به‌روز می‌شود و محتوا را با پیوندهای مرتبط از [واژه‌نامهٔ ما](/docs/reference/glossary/) جایگزین می‌کند.
وقتی نشانگر ماوس روی اصطلاح واژه‌نامه قرار می‌گیرد، مدخل واژه‌نامه به‌صورت یک راهنمای ابزار (tooltip) نمایش داده می‌شود.
اصطلاح واژه‌نامه به‌صورت پیوند نیز نمایش داده می‌شود.

افزون بر درج‌های همراه با راهنمای ابزار، می‌توانید تعریف‌های واژه‌نامه را در محتوای صفحه نیز دوباره به کار ببرید.

داده‌های خام اصطلاحات واژه‌نامه در [پوشهٔ واژه‌نامه](https://github.com/kubernetes/website/tree/main/content/en/docs/reference/glossary) ذخیره می‌شود و برای هر اصطلاح، یک فایل محتوا وجود دارد.

### نمونهٔ نمایشی واژه‌نامه

برای مثال، درج زیر در Markdown به
{{< glossary_tooltip text="کلاستر" term_id="cluster" >}} همراه با راهنمای ابزار تبدیل می‌شود:

```
{{</* glossary_tooltip text="cluster" term_id="cluster" */>}}
```

این هم یک تعریف کوتاه از واژه‌نامه:

```
{{</* glossary_definition prepend="A cluster is" term_id="cluster" length="short" */>}}
```

که خروجی آن چنین است:
{{< glossary_definition prepend="کلاستر عبارت است از" term_id="cluster" length="short" >}}

می‌توانید تعریف کامل را نیز درج کنید:

```
{{</* glossary_definition term_id="cluster" length="all" */>}}
```

که خروجی آن چنین است:
{{< glossary_definition term_id="cluster" length="all" >}}

## پیوند به مرجع API

با شورت‌کد `api-reference` می‌توانید به یکی از صفحه‌های مرجع API کوبرنتیز پیوند دهید؛ برای مثال به مرجع
{{< api-reference page="core/pod-v1" >}}:

```
{{</* api-reference page="core/pod-v1" */>}}
```

مقدار پارامتر `page` پسوند نشانی URL صفحهٔ مرجع API است.


با تعیین پارامتر `anchor` می‌توانید به بخش مشخصی از یک صفحه پیوند دهید؛ برای مثال به مرجع {{< api-reference page="core/pod-v1" anchor="PodSpec" >}}
یا بخش {{< api-reference page="core/pod-v1" anchor="environment-variables" >}}
از آن صفحه:

```
{{</* api-reference page="core/pod-v1" anchor="PodSpec" */>}}
{{</* api-reference page="core/pod-v1" anchor="environment-variables" */>}}
```


با تعیین پارامتر `text` می‌توانید متن پیوند را تغییر دهید؛ برای مثال با پیوند دادن به بخش
{{< api-reference page="core/pod-v1" anchor="environment-variables" text="متغیرهای محیطی">}}
از آن صفحه:

```
{{</* api-reference page="core/pod-v1" anchor="environment-variables" text="Environment Variable" */>}}
```

## عنوان جدول‌ها

با افزودن عنوان به جدول، می‌توانید دسترسی‌پذیری آن را برای صفحه‌خوان‌ها بهتر کنید. برای افزودن یک
[عنوان (caption)](https://www.w3schools.com/tags/tag_caption.asp) به جدول، جدول را درون شورت‌کد `table` قرار دهید و عنوان را با پارامتر `caption` مشخص کنید.

{{< note >}}
عنوان جدول‌ها برای صفحه‌خوان‌ها قابل‌دریافت است، اما در نمایش عادی HTML دیده نمی‌شود.
{{< /note >}}

نمونه‌ای از آن در ادامه آمده است:

```go-html-template
{{</* table caption="Configuration parameters" >}}
Parameter | Description | Default
:---------|:------------|:-------
`timeout` | The timeout for requests | `30s`
`logLevel` | The log level for log output | `INFO`
{{< /table */>}}
```

جدول نمایش‌داده‌شده چنین است:

{{< table caption="پارامترهای پیکربندی" >}}
پارامتر | توضیحات | پیش‌فرض
:---------|:------------|:-------
`timeout` | مهلت زمانی درخواست‌ها | `30s`
`logLevel` | سطح لاگ برای خروجی لاگ | `INFO`
{{< /table >}}

اگر HTML جدول را بررسی کنید، باید این عنصر را بلافاصله پس از عنصر آغازین `<table>` ببینید:

```html
<caption style="display: none;">Configuration parameters</caption>
```

## زبانه‌ها

در هر صفحهٔ Markdown (فایل `.md`) این وب‌سایت، می‌توانید مجموعه‌ای از زبانه‌ها اضافه کنید تا گونه‌های مختلف یک راه‌حل را نمایش دهید.

شورت‌کد `tabs` این پارامترها را می‌پذیرد:

* `name`: نامی که روی زبانه نمایش داده می‌شود.
* `codelang`: اگر برای شورت‌کد `tab` محتوای درونی فراهم کنید، می‌توانید به Hugo بگویید برای برجسته‌سازی از کدام زبان برنامه‌نویسی استفاده کند.
* `include`: فایلی که باید در زبانه درج شود. اگر زبانه درون یک
  [بستهٔ برگ (leaf bundle)](https://gohugo.io/content-management/page-bundles/#leaf-bundles) در Hugo قرار داشته باشد،
  فایل در خود بسته جست‌وجو می‌شود؛ این فایل می‌تواند از هر نوع MIME پشتیبانی‌شده در Hugo باشد.
  در غیر این صورت، صفحهٔ محتوایی که باید درج شود، نسبت به صفحهٔ فعلی جست‌وجو می‌شود.
  توجه کنید که هنگام استفاده از `include`، شورت‌کد هیچ محتوای درونی ندارد و باید از نحو خودبسته (self-closing) استفاده کنید؛ برای مثال
  `{{</* tab name="Content File #1" include="example1" /*/>}}`. زبان باید در `codelang` مشخص شود؛ در غیر این صورت، زبان بر اساس نام فایل تعیین می‌شود.
  فایل‌های غیرمحتوایی به‌طور پیش‌فرض با برجسته‌سازی کد نمایش داده می‌شوند.
* اگر محتوای درونی شما Markdown است، باید زبانه را با جداکنندهٔ `%` احاطه کنید.
  برای مثال: `{{%/* tab name="Tab 1" %}}This is **markdown**{{% /tab */%}}`
* می‌توانید گونه‌های یادشده در بالا را درون یک مجموعه زبانه با هم ترکیب کنید.

در ادامه نمونه‌ای نمایشی از شورت‌کد tabs آمده است.

{{< note >}}
**نام** زبانه در تعریف `tabs` باید درون هر صفحهٔ محتوا یکتا باشد.
{{< /note >}}

### نمونهٔ نمایشی زبانه‌ها: برجسته‌سازی کد

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

خروجی آن چنین است:

{{< tabs name="tab_with_code" >}}
{{< tab name="زبانهٔ A" codelang="bash" >}}
echo "این زبانهٔ A است."
{{< /tab >}}
{{< tab codelang="go" >}}
// اگر نامی برای زبانه تعیین نکنید، وب‌سایت خودش یک نام برای آن در نظر می‌گیرد.
println "این زبانه یک نام پیش‌فرض دارد";
{{< /tab >}}
{{< /tabs >}}

### نمونهٔ نمایشی زبانه‌ها: Markdown و HTML درون‌خطی

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

خروجی آن چنین است:

{{< tabs name="tab_with_md" >}}
{{% tab name="Markdown" %}}
این **مقداری Markdown است.**

{{< note >}}
این محتوا حتی می‌تواند شامل شورت‌کد هم باشد.
{{< /note >}}

{{% /tab %}}
{{< tab name="HTML" >}}
<div>
	<h3>HTML ساده</h3>
	<p>این مقداری HTML <i>ساده</i> است.</p>
</div>
{{< /tab >}}
{{< /tabs >}}

### نمونهٔ نمایشی زبانه‌ها: درج فایل

```go-text-template
{{</* tabs name="tab_with_file_include" >}}
{{< tab name="Content File #1" include="example1" />}}
{{< tab name="Content File #2" include="example2" />}}
{{< tab name="JSON File" include="podtemplate" />}}
{{< /tabs */>}}
```

خروجی آن چنین است:

{{< tabs name="tab_with_file_include" >}}
{{< tab name="فایل محتوای ۱" include="example1" />}}
{{< tab name="فایل محتوای ۲" include="example2" />}}
{{< tab name="فایل JSON" include="podtemplate.json" />}}
{{< /tabs >}}

## فایل‌های کد منبع

با شورت‌کد `{{%/* code_sample */%}}` می‌توانید محتوای یک فایل را درون یک بلوک کد جاسازی کنید تا کاربران بتوانند آن را دانلود کنند یا محتوایش را در کلیپ‌بورد خود کپی کنند. این شورت‌کد زمانی به کار می‌رود که محتوای فایل نمونه عمومی و قابل‌استفادهٔ مجدد باشد و بخواهید کاربران خودشان آن را امتحان کنند.

این شورت‌کد دو پارامتر نام‌دار می‌پذیرد: `language` و `file`. پارامتر الزامی `file` مسیر فایلی را که نمایش داده می‌شود مشخص می‌کند. پارامتر اختیاری `language` زبان برنامه‌نویسی فایل را مشخص می‌کند. اگر پارامتر `language` ارائه نشود، شورت‌کد تلاش می‌کند زبان را بر اساس پسوند فایل حدس بزند.

برای مثال:

```none
{{%/* code_sample language="yaml" file="application/deployment-scale.yaml" */%}}
```

خروجی آن چنین است:

{{% code_sample language="yaml" file="application/deployment-scale.yaml" %}}

هنگام افزودن یک فایل نمونهٔ جدید، مانند یک فایل YAML، آن را در یکی از زیرپوشه‌های `<LANG>/examples/` ایجاد کنید؛ در اینجا `<LANG>` زبان صفحه است. در Markdown صفحهٔ خود از شورت‌کد `code` استفاده کنید:

```none
{{%/* code_sample file="<RELATIVE-PATH>/example-yaml>" */%}}
```
در اینجا `<RELATIVE-PATH>` مسیر فایل نمونه‌ای است که باید درج شود و نسبت به پوشهٔ `examples` سنجیده می‌شود. شورت‌کد زیر به یک فایل YAML ارجاع می‌دهد که در مسیر `/content/en/examples/configmap/configmaps.yaml` قرار دارد.

```none
{{%/* code_sample file="configmap/configmaps.yaml" */%}}
```

شورت‌کد قدیمی `{{%/* codenew */%}}` در حال جایگزین شدن با `{{%/* code_sample */%}}` است.
در مستندات جدید از `{{%/* code_sample */%}}` استفاده کنید (نه `{{%/* codenew */%}}` یا `{{%/* code */%}}`).

## نشانگر محتوای شخص ثالث

اجرای کوبرنتیز به نرم‌افزارهای شخص ثالث نیاز دارد. برای مثال، معمولاً باید یک
[سرور DNS](/docs/tasks/administer-cluster/dns-custom-nameservers/#introduction)
به کلاستر خود اضافه کنید تا تفکیک نام کار کند.

وقتی به نرم‌افزارهای شخص ثالث پیوند می‌دهیم یا به هر شکل دیگری از آن‌ها نام می‌بریم، از [راهنمای محتوا](/docs/contribute/style/content-guide/) پیروی می‌کنیم و آن موارد شخص ثالث را نیز علامت‌گذاری می‌کنیم.

استفاده از این شورت‌کدها یک سلب مسئولیت به هر صفحه‌ای از مستندات که از آن‌ها استفاده کند اضافه می‌کند.

### فهرست‌ها {#third-party-content-list}

برای فهرستی از چند مورد شخص ثالث، شورت‌کد زیر را:
```
{{%/* thirdparty-content */%}}
```
درست زیر عنوان بخشی اضافه کنید که همهٔ موارد را در بر می‌گیرد.

### موارد {#third-party-content-item}

اگر فهرستی دارید که بیشتر موارد آن به نرم‌افزارهای درون پروژه اشاره دارند (برای مثال خود کوبرنتیز و مؤلفهٔ جداگانهٔ
[Descheduler](https://github.com/kubernetes-sigs/descheduler))، باید از شکل دیگری استفاده کنید.

شورت‌کد زیر را:
```
{{%/* thirdparty-content single="true" */%}}
```

پیش از آن مورد، یا درست زیر عنوان آن مورد خاص اضافه کنید.

## جزئیات

با یک شورت‌کد می‌توانید یک عنصر HTML از نوع `<details>` نمایش دهید:

```markdown
{{</* details summary="More about widgets" */>}}
The frobnicator extension API implements _widgets_ using example running text.

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem.
{{</* /details */>}}
```

خروجی آن چنین است:
{{< details summary="دربارهٔ ویجت‌ها بیشتر بدانید" >}}
API افزونهٔ frobnicator، _ویجت‌ها_ را با استفاده از متن نمونهٔ جاری پیاده‌سازی می‌کند.

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem.
{{< /details >}}

{{< note >}}
از این شورت‌کد به‌ندرت استفاده کنید؛ معمولاً بهتر است همهٔ متن مستقیماً به خوانندگان نمایش داده شود.
{{< /note >}}

## رشته‌های نسخه

برای تولید یک رشتهٔ نسخه جهت درج در مستندات، می‌توانید از میان چند شورت‌کد نسخه یکی را انتخاب کنید. هر شورت‌کد نسخه، رشته‌ای را نمایش می‌دهد که از مقدار یک پارامتر نسخه در فایل پیکربندی وب‌سایت، یعنی `hugo.toml`، به دست می‌آید.
دو پارامتر نسخه‌ای که بیش از همه استفاده می‌شوند `latest` و `version` هستند.

### `{{</* param "version" */>}}`

شورت‌کد `{{</* param "version" */>}}` مقدار نسخهٔ فعلی مستندات کوبرنتیز را از پارامتر `version` وب‌سایت تولید می‌کند. شورت‌کد `param` نام یک پارامتر وب‌سایت را می‌پذیرد که در اینجا `version` است.

{{< note >}}
در مستنداتی که پیش‌تر منتشر شده‌اند، مقادیر پارامترهای `latest` و `version` با هم برابر نیستند. پس از انتشار یک نسخهٔ جدید، مقدار `latest` افزایش می‌یابد، اما مقدار `version` برای آن مجموعه از مستندات بدون تغییر می‌ماند. برای مثال، یک نسخهٔ پیشین از مستندات، `version` را `v1.19` و `latest` را `v1.20` نمایش می‌دهد.
{{< /note >}}

خروجی آن چنین است:

{{< param "version" >}}

### `{{</* latest-version */>}}`

شورت‌کد `{{</* latest-version */>}}` مقدار پارامتر `latest` وب‌سایت را برمی‌گرداند.
پارامتر `latest` وب‌سایت هنگام انتشار نسخهٔ جدیدی از مستندات به‌روز می‌شود.
این پارامتر همیشه با مقدار `version` در یک مجموعه از مستندات یکسان نیست.

خروجی آن چنین است:

{{< latest-version >}}

### `{{</* latest-semver */>}}`

شورت‌کد `{{</* latest-semver */>}}` مقدار `latest` را بدون پیشوند «v» تولید می‌کند.

خروجی آن چنین است:

{{< latest-semver >}}

### `{{</* version-check */>}}`

شورت‌کد `{{</* version-check */>}}` بررسی می‌کند که آیا پارامتر صفحهٔ `min-kubernetes-server-version` وجود دارد یا نه، و سپس از این مقدار برای مقایسه با `version` استفاده می‌کند.

خروجی آن چنین است:

{{< version-check >}}

### `{{</* latest-release-notes */>}}`

شورت‌کد `{{</* latest-release-notes */>}}` یک رشتهٔ نسخه از `latest` تولید می‌کند و پیشوند «v» را از آن حذف می‌کند. این شورت‌کد با رشتهٔ نسخهٔ تغییریافته، نشانی URL جدیدی برای صفحهٔ CHANGELOG یادداشت‌های انتشار چاپ می‌کند.

خروجی آن چنین است:

{{< latest-release-notes >}}


## {{% heading "whatsnext" %}}

* دربارهٔ [Hugo](https://gohugo.io/) بیشتر بدانید.
* دربارهٔ [نوشتن یک موضوع جدید](/docs/contribute/style/write-new-topic/) بیشتر بدانید.
* دربارهٔ [انواع محتوای صفحه](/docs/contribute/style/page-content-types/) بیشتر بدانید.
* دربارهٔ [باز کردن یک pull request](/docs/contribute/new-content/open-a-pr/) بیشتر بدانید.
* دربارهٔ [مشارکت پیشرفته](/docs/contribute/advanced/) بیشتر بدانید.

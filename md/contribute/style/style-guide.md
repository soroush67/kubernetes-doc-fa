---
title: راهنمای سبک مستندات
linktitle: راهنمای سبک
content_type: concept
weight: 40
math: true
---

<!-- overview -->
این صفحه رهنمودهای سبک نگارش برای مستندات کوبرنتیز را ارائه می‌دهد.
این موارد رهنمود هستند، نه قانون. از بهترین قضاوت خود استفاده کنید و در صورت تمایل
پیشنهاد تغییرات این سند را در قالب یک pull request مطرح کنید.

برای کسب اطلاعات بیشتر درباره ایجاد محتوای جدید برای مستندات کوبرنتیز،
[راهنمای محتوای مستندات](/docs/contribute/style/content-guide/) را مطالعه کنید.

تغییرات راهنمای سبک به‌صورت گروهی توسط SIG Docs انجام می‌شود. برای پیشنهاد یک تغییر
یا افزودن مورد جدید، [آن را به دستور جلسه اضافه کنید](https://bit.ly/sig-docs-agenda)
تا در یکی از جلسات آتی SIG Docs بررسی شود، و در آن جلسه شرکت کنید تا در بحث مشارکت داشته باشید.

<!-- body -->

{{< alert color="info" title="Note" >}}
مستندات کوبرنتیز از
[Goldmark Markdown Renderer](https://github.com/yuin/goldmark)
با برخی تنظیمات، به‌همراه چند
[Hugo Shortcode](/docs/contribute/style/hugo-shortcodes/) برای پشتیبانی از
مدخل‌های واژه‌نامه، تب‌ها و نمایش وضعیت ویژگی‌ها استفاده می‌کند.
{{< /alert >}}

## زبان {#language}

مستندات کوبرنتیز به زبان‌های متعددی ترجمه شده است
(به [Localization READMEs](https://github.com/kubernetes/website/blob/main/README.md#localization-readmemds) مراجعه کنید).

روش بومی‌سازی مستندات برای یک زبان دیگر در [بومی‌سازی مستندات کوبرنتیز](/docs/contribute/localization/) توضیح داده شده است.

مستندات انگلیسی‌زبان از املا و دستور زبان انگلیسی آمریکایی استفاده می‌کند.

{{< comment >}}[If you're localizing this page, you can omit the point about US English.]{{< /comment >}}

## استانداردهای قالب‌بندی مستندات

### برای آبجکت‌های API از UpperCamelCase استفاده کنید

هنگامی که به‌طور مشخص به تعامل با یک آبجکت API اشاره می‌کنید، از
[UpperCamelCase](https://en.wikipedia.org/wiki/Camel_case)، که با نام Pascal case نیز شناخته می‌شود، استفاده کنید.
ممکن است در [مرجع API](/docs/reference/kubernetes-api/) با حروف‌نویسی متفاوتی مانند «configMap» روبه‌رو شوید.
در نگارش مستندات عمومی بهتر است از UpperCamelCase استفاده کنید و آن را «ConfigMap» بنامید.

هنگامی که به‌صورت کلی درباره یک آبجکت API صحبت می‌کنید، از
[حروف‌نویسی به سبک جمله](https://docs.microsoft.com/en-us/style-guide/text-formatting/using-type/use-sentence-style-capitalization) استفاده کنید.

مثال‌های زیر بر حروف‌نویسی تمرکز دارند. برای اطلاعات بیشتر درباره قالب‌بندی
نام آبجکت‌های API، رهنمود مرتبط در [سبک کد](#code-style-inline-code) را مطالعه کنید.

{{< table caption = "انجام دهید و انجام ندهید - برای آبجکت‌های API از Pascal case استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
The HorizontalPodAutoscaler resource is responsible for ... | The Horizontal pod autoscaler is responsible for ...
A PodList object is a list of pods. | A Pod List object is a list of pods.
The Volume object contains a `hostPath` field. | The volume object contains a hostPath field.
Every ConfigMap object is part of a namespace. | Every configMap object is part of a namespace.
For managing confidential data, consider using the Secret API. | For managing confidential data, consider using the secret API.
{{< /table >}}

### برای جایگزین‌ها (placeholder) از کروشه زاویه‌دار استفاده کنید

برای جایگزین‌ها از کروشه زاویه‌دار استفاده کنید. به خواننده بگویید که هر جایگزین
چه چیزی را نشان می‌دهد، برای مثال:

نمایش اطلاعات درباره یک pod:

```shell
kubectl describe pod <pod-name> -n <namespace>
```

اگر فضای نام (namespace) مربوط به pod برابر `default` است، می‌توانید پارامتر '-n' را حذف کنید.

### برای عناصر رابط کاربری از حروف درشت استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - عناصر رابط را درشت بنویسید" >}}
انجام دهید | انجام ندهید
:--| :-----
Click **Fork**. | Click "Fork".
Select **Other**. | Select "Other".
{{< /table >}}

### برای تعریف یا معرفی اصطلاحات جدید از حروف ایتالیک استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای اصطلاحات جدید از ایتالیک استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
A _cluster_ is a set of nodes ... | A "cluster" is a set of nodes ...
These components form the _control plane_. | These components form the **control plane**.
{{< /table >}}

### برای نام فایل‌ها، دایرکتوری‌ها و مسیرها از سبک کد استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای نام فایل‌ها، دایرکتوری‌ها و مسیرها از سبک کد استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
Open the `envars.yaml` file. | Open the envars.yaml file.
Go to the `/docs/tutorials` directory. | Go to the /docs/tutorials directory.
Open the `/_data/concepts.yaml` file. | Open the /\_data/concepts.yaml file.
{{< /table >}}

### برای علائم نگارشی درون گیومه از استاندارد بین‌المللی استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای علائم نگارشی درون گیومه از استاندارد بین‌المللی استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
events are recorded with an associated "stage". | events are recorded with an associated "stage."
The copy is called a "fork". | The copy is called a "fork."
{{< /table >}}

### برای مراحل ارتقای قابلیت‌ها از start case استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای مراحل ارتقای قابلیت‌ها از start case استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
Dynamic Resource Allocation (DRA) is Beta. | Dynamic Resource Allocation (DRA) is beta.
{{< /table >}}

## قالب‌بندی کد درون‌خطی

### برای کد درون‌خطی و دستورها از سبک کد استفاده کنید {#code-style-inline-code}

برای کد درون‌خطی در یک سند HTML از تگ `<code>` استفاده کنید. در یک سند
Markdown از بک‌تیک (`` ` ``) استفاده کنید. با این حال، kindهای API مانند StatefulSet
یا ConfigMap به‌صورت عینی و بدون بک‌تیک نوشته می‌شوند؛ این کار امکان استفاده از
آپاستروف مالکیت را فراهم می‌کند.

{{< table caption = "انجام دهید و انجام ندهید - برای کد درون‌خطی، دستورها و آبجکت‌های API از سبک کد استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
The `kubectl run` command creates a Pod. | The "kubectl run" command creates a Pod.
The kubelet on each node acquires a Lease… | The kubelet on each node acquires a `Lease`…
A PersistentVolume represents durable storage… | A `PersistentVolume` represents durable storage…
The CustomResourceDefinition's `.spec.group` field… | The `CustomResourceDefinition.spec.group` field…
For declarative management, use `kubectl apply`. | For declarative management, use "kubectl apply".
Enclose code samples with triple backticks. (\`\`\`)| Enclose code samples with any other syntax.
Use single backticks to enclose inline code. For example, `var example = true`. | Use two asterisks (`**`) or an underscore (`_`) to enclose inline code. For example, **var example = true**.
Use triple backticks before and after a multi-line block of code for fenced code blocks. | Use multi-line blocks of code to create diagrams, flowcharts, or other illustrations.
Use meaningful variable names that have a context. | Use variable names such as 'foo','bar', and 'baz' that are not meaningful and lack context.
Remove trailing spaces in the code. | Add trailing spaces in the code, where these are important, because the screen reader will read out the spaces as well.
{{< /table >}}

{{< alert color="info" title="Note" >}}
وب‌سایت از هایلایت نحو (syntax highlighting) برای نمونه‌های کد پشتیبانی می‌کند، اما تعیین زبان
اختیاری است. هایلایت نحو در بلوک کد باید با
[رهنمودهای کنتراست](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0&showtechniques=141%2C143#contrast-minimum) مطابقت داشته باشد.
{{< /alert >}}

### برای نام فیلدهای آبجکت و فضاهای نام از سبک کد استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای نام فیلدهای آبجکت از سبک کد استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
Set the value of the `replicas` field in the configuration file. | Set the value of the "replicas" field in the configuration file.
The value of the `exec` field is an ExecAction object. | The value of the "exec" field is an ExecAction object.
Run the process as a DaemonSet in the `kube-system` namespace. | Run the process as a DaemonSet in the kube-system namespace.
{{< /table >}}

### برای نام ابزارهای خط فرمان و اجزای کوبرنتیز از سبک کد استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - برای نام ابزارهای خط فرمان و اجزای کوبرنتیز از سبک کد استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
The `kubelet` preserves node stability. | The kubelet preserves node stability.
The `kubectl` handles locating and authenticating to the API server. | The kubectl handles locating and authenticating to the apiserver.
Run the process with the certificate, `kube-apiserver --client-ca-file=FILENAME`. | Run the process with the certificate, kube-apiserver --client-ca-file=FILENAME. |
{{< /table >}}

### شروع یک جمله با نام ابزار یا مؤلفه

{{< table caption = "انجام دهید و انجام ندهید - شروع یک جمله با نام ابزار یا مؤلفه" >}}
انجام دهید | انجام ندهید
:--| :-----
The `kubeadm` tool bootstraps and provisions machines in a cluster. | `kubeadm` tool bootstraps and provisions machines in a cluster.
The kube-scheduler is the default scheduler for Kubernetes. | kube-scheduler is the default scheduler for Kubernetes.
{{< /table >}}

### به‌جای نام مؤلفه از یک توصیف‌گر عمومی استفاده کنید

{{< table caption = "انجام دهید و انجام ندهید - به‌جای نام مؤلفه از یک توصیف‌گر عمومی استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
The Kubernetes API server offers an OpenAPI spec. | The apiserver offers an OpenAPI spec.
Aggregated APIs are subordinate API servers. | Aggregated APIs are subordinate APIServers.
{{< /table >}}

### برای مقادیر فیلدهای رشته‌ای و عدد صحیح از سبک عادی استفاده کنید

برای مقادیر فیلد از نوع رشته یا عدد صحیح، از سبک عادی و بدون گیومه استفاده کنید.

{{< table caption = "انجام دهید و انجام ندهید - برای مقادیر فیلدهای رشته‌ای و عدد صحیح از سبک عادی استفاده کنید" >}}
انجام دهید | انجام ندهید
:--| :-----
Set the value of `imagePullPolicy` to Always. | Set the value of `imagePullPolicy` to "Always".
Set the value of `image` to nginx:1.16. | Set the value of `image` to `nginx:1.16`.
Set the value of the `replicas` field to 2. | Set the value of the `replicas` field to `2`.
{{< /table >}}

با این حال، در مواردی که خطر دارد خوانندگان مقدار را با یک kind از API اشتباه بگیرند،
قرار دادن مقدار در گیومه را در نظر بگیرید.

## ارجاع به منابع API کوبرنتیز

این بخش درباره نحوه ارجاع به منابع API در مستندات است.

### توضیح درباره «منبع» (resource)

کوبرنتیز از واژه _resource_ برای اشاره به منابع API استفاده می‌کند. برای مثال،
مسیر URL به‌صورت `/apis/apps/v1/namespaces/default/deployments/my-app` یک
Deployment با نام «my-app» را در
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} «default» نشان می‌دهد. در اصطلاح HTTP،
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} یک منبع است -
همان‌طور که همه URLهای وب یک منبع را مشخص می‌کنند.

مستندات کوبرنتیز همچنین از «منبع» برای صحبت درباره درخواست‌ها و محدودیت‌های
CPU و حافظه استفاده می‌کند. اغلب ایده خوبی است که به منابع API با عنوان
«منابع API» اشاره شود؛ این کار به جلوگیری از اشتباه با منابع CPU و حافظه
یا انواع دیگر منبع کمک می‌کند.

اگر از شکل جمع با حروف کوچک نام یک منبع، مانند
`deployments` یا `configmaps`، استفاده می‌کنید، زمینه نوشتاری اضافی ارائه دهید تا به خوانندگان
در درک منظور شما کمک شود. اگر از این اصطلاح در بافتی استفاده می‌کنید که نام
UpperCamelCase نیز می‌تواند کاربرد داشته باشد و خطر ابهام وجود دارد،
استفاده از kind مربوط به API را با UpperCamelCase در نظر بگیرید.

### زمان استفاده از اصطلاحات API کوبرنتیز

اصطلاحات مختلف API کوبرنتیز عبارت‌اند از:

- _API kinds_: نامی که در URL مربوط به API استفاده می‌شود (مانند `pods` و `namespaces`).
  API kindها گاهی _resource types_ نیز نامیده می‌شوند.
- _API resource_: یک نمونه منفرد از یک API kind (مانند `pod` و `secret`).
- _Object_: منبعی که به‌عنوان «رکورد نیت» (record of intent) عمل می‌کند. یک آبجکت وضعیت مطلوب
  برای بخش مشخصی از کلاستر شماست که control plane کوبرنتیز تلاش می‌کند آن را حفظ کند.
  همه آبجکت‌ها در API کوبرنتیز در عین حال منبع نیز هستند.

برای وضوح، می‌توانید هنگام اشاره به یک منبع API در مستندات کوبرنتیز، «resource» یا «object» را اضافه کنید.
برای مثال: به‌جای «a Secret» بنویسید «a Secret object».
اگر وضوح مطلب تنها از روی حروف‌نویسی (بزرگ بودن حرف اول) مشخص است، نیازی به افزودن واژه اضافی نیست.

در صورتی که بازنویسی به جلوگیری از سوءتفاهم کمک می‌کند، آن را در نظر بگیرید. یک وضعیت رایج
زمانی است که می‌خواهید جمله را با یک API kind مانند «Secret» شروع کنید؛ زیرا در انگلیسی
و زبان‌های دیگر حرف اول جمله بزرگ نوشته می‌شود، خوانندگان نمی‌توانند تشخیص دهند که منظور شما
API kind است یا مفهوم عمومی. بازنویسی جمله می‌تواند کمک کند.

### نام منابع API

نام منابع API را همیشه با [UpperCamelCase](https://en.wikipedia.org/wiki/Camel_case)،
که با نام PascalCase نیز شناخته می‌شود، قالب‌بندی کنید. API kindها را با قالب‌بندی کد ننویسید.

نام یک آبجکت API را به چند واژه جداگانه تقسیم نکنید. برای مثال، از PodTemplateList استفاده کنید، نه Pod Template List.

برای اطلاعات بیشتر درباره PascalCase و قالب‌بندی کد، رهنمود مرتبط در
[برای آبجکت‌های API از UpperCamelCase استفاده کنید](/docs/contribute/style/style-guide/#use-upper-camel-case-for-api-objects)
و [برای کد درون‌خطی، دستورها و آبجکت‌های API از سبک کد استفاده کنید](/docs/contribute/style/style-guide/#code-style-inline-code) را مطالعه کنید.

برای اطلاعات بیشتر درباره اصطلاحات API کوبرنتیز، رهنمود مرتبط در
[اصطلاحات API کوبرنتیز](/docs/reference/using-api/api-concepts/#standard-api-terminology) را مطالعه کنید.

## قالب‌بندی قطعه‌کدها

### اعلان خط فرمان (command prompt) را درج نکنید

{{< table caption = "انجام دهید و انجام ندهید - اعلان خط فرمان را درج نکنید" >}}
انجام دهید | انجام ندهید
:--| :-----
`kubectl get pods` | `$ kubectl get pods`
{{< /table >}}

### دستورها را از خروجی جدا کنید

بررسی کنید که pod روی نودی که انتخاب کرده‌اید در حال اجرا است:

```shell
kubectl get pods --output=wide
```

خروجی مشابه زیر است:

```console
NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
nginx    1/1       Running   0          13s    10.200.0.4   worker0
```

### نسخه‌بندی نمونه‌های کوبرنتیز

نمونه‌های کد و نمونه‌های پیکربندی که شامل اطلاعات نسخه هستند باید
با متن همراه خود سازگار باشند.

اگر اطلاعات وابسته به نسخه است، نسخه کوبرنتیز باید در بخش `prerequisites`
از [قالب Task](/docs/contribute/style/page-content-types/#task)
یا [قالب Tutorial](/docs/contribute/style/page-content-types/#tutorial) تعریف شود.
پس از ذخیره صفحه، بخش `prerequisites` با عنوان **Before you begin** نمایش داده می‌شود.

برای تعیین نسخه کوبرنتیز در یک صفحه وظیفه (task) یا آموزش (tutorial)،
`min-kubernetes-server-version` را در front matter صفحه درج کنید.

اگر YAML نمونه در یک فایل مستقل قرار دارد، موضوعاتی را که آن را به‌عنوان مرجع شامل می‌شوند پیدا و بررسی کنید.
اطمینان حاصل کنید که برای همه موضوعاتی که از YAML مستقل استفاده می‌کنند، اطلاعات نسخه مناسب تعریف شده است.
اگر هیچ موضوعی به یک فایل YAML مستقل ارجاع نمی‌دهد، حذف آن را به‌جای به‌روزرسانی در نظر بگیرید.

برای مثال، اگر در حال نوشتن آموزشی هستید که به کوبرنتیز نسخه 1.8 مربوط است،
front-matter فایل markdown شما باید چیزی شبیه به این باشد:

```yaml
---
title: <your tutorial title here>
min-kubernetes-server-version: v1.8
---
```

در نمونه‌های کد و پیکربندی، توضیحاتی درباره نسخه‌های جایگزین درج نکنید.
مراقب باشید عبارت‌های نادرست را در قالب کامنت در نمونه‌های خود نگنجانید، مانند:

```yaml
apiVersion: v1 # earlier versions use...
kind: Pod
...
```

## فرمول‌ها و معادله‌ها

می‌توانید از پشتیبانی Docsy برای [نمودارها و فرمول‌ها](https://www.docsy.dev/docs/adding-content/diagrams-and-formulae/#latex-support-with-katex) استفاده کنید.

برای مثال: `\\(\frac{7}{9} \sqrt{K^8 s}\\)`، که به‌صورت \\(\frac{7}{9} \sqrt{K^8 s}\\) نمایش داده می‌شود.

در صورت امکان فرمول‌های درون‌خطی را ترجیح دهید، اما اگر استفاده از بلوک `math` احتمالاً به خوانندگان کمک می‌کند، می‌توانید از آن استفاده کنید.

راهنمای Docsy را مطالعه کنید تا بدانید برای فعال‌سازی این پشتیبانی چه چیزی را باید در صفحه خود تغییر دهید؛
اگر به مشکل برخوردید، `math: true` را به [front matter](https://gohugo.io/content-management/front-matter/) صفحه اضافه کنید
(حتی اگر فکر می‌کنید فعال‌سازی خودکار باید کافی باشد، می‌توانید این کار را انجام دهید).

## فهرست واژگان Kubernetes.io

فهرستی از اصطلاحات و واژگان ویژه کوبرنتیز که باید در سراسر وب‌سایت به‌صورت یکسان استفاده شوند.

{{< table caption = "فهرست واژگان Kubernetes.io" >}}
اصطلاح | نحوه استفاده
:--- | :----
Kubernetes | Kubernetes should always be capitalized.
Docker | Docker should always be capitalized.
SIG Docs | SIG Docs rather than SIG-DOCS or other variations.
On-premises | On-premises or On-prem rather than On-premise or other variations.
cloud native | Cloud native or cloud native as appropriate for sentence structure rather than cloud-native or Cloud Native.
open source | Open source or open source as appropriate for sentence structure rather than open-source or Open Source.
{{< /table >}}

## Shortcodeها

[Shortcodeهای](https://gohugo.io/content-management/shortcodes) Hugo به ایجاد
سطوح مختلفی از تأکید بلاغی کمک می‌کنند. مستندات ما در این دسته از سه گونه
shortcode با نام [`alert`](https://www.docsy.dev/docs/adding-content/shortcodes/#alert)
در Docsy پشتیبانی می‌کند: **Note**، **Caution** و **Warning**.

1. متن را میان یک shortcode باز و بسته `alert` قرار دهید و
   ویژگی‌های `color` و `title` را متناسب با گونه موردنیاز خود انتخاب کنید.

2. برای اعمال یک سبک از نحو زیر استفاده کنید:

   ```none
   {{</* alert color="info" title="Note" */>}}
   The shortcode renders the title as a heading, so do not repeat it inside the body.
   {{</* /alert */>}}
   ```

   خروجی به این صورت است:

   {{< alert color="info" title="Note" >}}
   shortcode عنوان را به‌صورت یک سرفصل نمایش می‌دهد، بنابراین آن را درون متن تکرار نکنید.
   {{< /alert >}}

بسیاری از صفحات موجود هنوز از shortcodeهای قدیمی `{{</* note */>}}`، `{{</* caution */>}}`
و `{{</* warning */>}}` استفاده می‌کنند. این موارد همچنان کار می‌کنند — برای محتوای جدید و
هنگام ویرایش صفحات موجود، shortcode با نام `alert` را ترجیح دهید.

### یادداشت (Note)

از `{{</* alert color="info" title="Note" */>}}` برای برجسته‌کردن یک نکته یا اطلاعاتی استفاده کنید که دانستن آن می‌تواند مفید باشد.

برای مثال:

```
{{</* alert color="info" title="Note" */>}}
You can _still_ use Markdown inside these callouts.
{{</* /alert */>}}
```

خروجی به این صورت است:

{{< alert color="info" title="Note" >}}
شما می‌توانید _همچنان_ از Markdown در داخل این کادرهای توضیحی استفاده کنید.
{{< /alert >}}

می‌توانید شورت‌کد `alert` را در یک فهرست نیز به کار ببرید:

```
1. Use the alert shortcode in a list

1. A second item with an embedded note

   {{</* alert color="info" title="Note" */>}}
   Warning, Caution, and Note shortcodes, embedded in lists, need to be indented four spaces. See [Common Shortcode Issues](#common-shortcode-issues).
   {{</* /alert */>}}

1. A third item in a list

1. A fourth item in a list
```

خروجی به این صورت است:

1. از شورت‌کد alert در یک فهرست استفاده کنید

1. آیتم دوم همراه با یک یادداشت درون‌متنی

    {{< alert color="info" title="Note" >}}
    شورت‌کدهای Warning، Caution و Note که درون فهرست‌ها قرار می‌گیرند باید چهار فاصله تورفتگی داشته باشند. به [مشکلات رایج شورت‌کد](#common-shortcode-issues) مراجعه کنید.
    {{< /alert >}}

1. آیتم سوم در یک فهرست

1. آیتم چهارم در یک فهرست

### احتیاط (Caution)

از `{{</* alert color="caution" title="Caution" */>}}` برای جلب توجه به اطلاعات مهمی استفاده کنید که برای پرهیز از مشکلات احتمالی لازم است.

برای مثال:

```
{{</* alert color="caution" title="Caution" */>}}
The callout style only applies to the line directly above the tag.
{{</* /alert */>}}
```

خروجی به این صورت است:

{{< alert color="caution" title="Caution" >}}
سبک کادر توضیحی فقط بر خطی اعمال می‌شود که بلافاصله بالای تگ قرار دارد.
{{< /alert >}}

### هشدار (Warning)

از `{{</* alert color="danger" title="Warning" */>}}` برای نشان‌دادن خطر یا اطلاعاتی استفاده کنید که رعایت آن حیاتی است.

برای مثال:

```
{{</* alert color="danger" title="Warning" */>}}
Beware.
{{</* /alert */>}}
```

خروجی به این صورت است:

{{< alert color="danger" title="Warning" >}}
مراقب باشید.
{{< /alert >}}

## مشکلات رایج شورت‌کدها {#common-shortcode-issues}

### فهرست‌های شماره‌دار

شورت‌کدها فهرست‌های شماره‌دار را قطع می‌کنند، مگر اینکه پیش از اعلان و تگ، چهار فاصله تورفتگی قرار دهید.

برای مثال:

    1. Preheat oven to 350˚F

    1. Prepare the batter, and pour into springform pan.
       {{</* alert color="info" title="Note" */>}}Grease the pan for best results.{{</* /alert */>}}

    1. Bake for 20-25 minutes or until set.

خروجی به این صورت است:

1. فر را تا ۳۵۰ درجه فارنهایت گرم کنید

1. خمیر را آماده کنید و در قالب فنری بریزید.

   {{< alert color="info" title="Note" >}}برای بهترین نتیجه، قالب را چرب کنید.{{< /alert >}}

1. به مدت ۲۰ تا ۲۵ دقیقه بپزید یا تا زمانی که سفت شود.

### دستورهای include

شورت‌کدهایی که درون دستورهای include قرار بگیرند، فرایند build را با خطا مواجه می‌کنند. شما باید آن‌ها را
در سند والد، پیش و پس از فراخوانی include درج کنید. برای مثال:

```
{{</* alert color="info" title="Note" */>}}
{{</* include "task-tutorial-prereqs.md" */>}}
{{</* /alert */>}}
```

## عناصر Markdown

### شکستن خطوط

برای جداکردن محتوای سطح بلوک مانند سرفصل‌ها، فهرست‌ها، تصاویر،
بلوک‌های کد و موارد مشابه از یک خط جدید استفاده کنید. استثنا سرفصل‌های سطح دوم است که باید
دو خط جدید داشته باشند. سرفصل‌های سطح دوم بدون هیچ پاراگراف یا متنی در میان، بعد از سرفصل سطح اول (یا عنوان) می‌آیند.
فاصله‌گذاری دو خطی به نمایش بهتر ساختار کلی محتوا در ویرایشگر کد کمک می‌کند.

در صورت لزوم، پاراگراف‌ها را در منبع Markdown به‌صورت دستی بشکنید. از آنجا که ابزار git
و وب‌سایت GitHub تفاوت‌های فایل را به‌صورت خط‌به‌خط تولید می‌کنند،
شکستن دستی خطوط طولانی به بازبین‌ها کمک می‌کند تا تغییرات
انجام‌شده در یک PR را به‌سادگی پیدا کنند و بازخورد بدهند. همچنین به تیم‌های بومی‌سازی پایین‌دستی
که تغییرات بالادستی را به‌صورت خط‌به‌خط دنبال می‌کنند کمک می‌کند. شکستن
خط می‌تواند برای مثال در انتهای یک جمله یا در یک علامت نگارشی انجام شود. یک استثنا این است که
انتظار می‌رود هر پیوند Markdown یا شورت‌کد در یک خط واحد باشد.

### سرفصل‌ها و عنوان‌ها {#headings}

افرادی که به این مستندات دسترسی پیدا می‌کنند ممکن است از صفحه‌خوان یا فناوری کمکی (AT) استفاده کنند.
[صفحه‌خوان‌ها](https://en.wikipedia.org/wiki/Screen_reader) دستگاه‌های خروجی خطی هستند
و موارد موجود در صفحه را یکی‌یکی بیان می‌کنند. اگر محتوای صفحه زیاد باشد، می‌توانید
از سرفصل‌ها برای ایجاد ساختار داخلی صفحه استفاده کنید. ساختار مناسب صفحه به همه خوانندگان کمک می‌کند
به‌راحتی در صفحه پیمایش کنند یا موضوعات مورد علاقه خود را پیدا کنند.

{{< table caption = "Do and Don't - Headings" >}}
انجام دهید | انجام ندهید
:--| :-----
عنوان را در front matter صفحه یا نوشته وبلاگ به‌روزرسانی کنید. | از سرفصل سطح اول استفاده کنید، زیرا Hugo عنوان موجود در front matter صفحه را به‌طور خودکار به سرفصل سطح اول تبدیل می‌کند.
از سرفصل‌های مرتب برای ارائه یک طرح کلی معنادار و سطح بالا از محتوای خود استفاده کنید. | از سرفصل‌های سطح ۴ تا ۶ استفاده کنید، مگر اینکه کاملاً ضروری باشد. اگر محتوای شما تا این حد جزئی است، ممکن است لازم باشد به چند مقاله جداگانه تقسیم شود.
برای محتوایی که نوشته وبلاگ نیست، از علامت شارپ (`#`) استفاده کنید. | برای تعیین سرفصل‌های سطح اول از خط زیر (`---` یا `===`) استفاده کنید.
برای سرفصل‌های بدنه صفحه از sentence case استفاده کنید. برای مثال، **Extend kubectl with plugins** | برای سرفصل‌های بدنه صفحه از title case استفاده کنید. برای مثال، **Extend Kubectl With Plugins**
برای عنوان صفحه در front matter از title case استفاده کنید. برای مثال، `title: Kubernetes API Server Bypass Risks` | برای عنوان صفحه در front matter از sentence case استفاده کنید. برای مثال، از `title: Kubernetes API server bypass risks` استفاده نکنید.
پیوندهای مرتبط را در متن اصلی قرار دهید. | در سرفصل‌ها ابرپیوند (`<a href=""></a>`) قرار دهید.
برای نشان‌دادن سرفصل‌ها از علامت شارپ (`#`) استفاده کنید. | برای جداکردن پاراگراف‌ها از متن **پررنگ** یا نشانگرهای دیگر استفاده کنید.
{{< /table >}}

### پاراگراف‌ها

{{< table caption = "Do and Don't - Paragraphs" >}}
انجام دهید | انجام ندهید
:--| :-----
سعی کنید پاراگراف‌ها را کمتر از ۶ جمله نگه دارید. | اولین پاراگراف را با کاراکترهای فاصله تورفتگی بدهید. برای مثال، ⋅⋅⋅سه فاصله پیش از یک پاراگراف باعث تورفتگی آن می‌شود.
از سه خط تیره (`---`) برای ایجاد خط افقی استفاده کنید. از خطوط افقی برای جداکردن بخش‌های محتوای پاراگراف استفاده کنید. برای مثال، تغییر صحنه در یک داستان یا تغییر موضوع در یک بخش. | از خطوط افقی برای تزئین استفاده کنید.
{{< /table >}}

### پیوندها

{{< table caption = "Do and Don't - Links" >}}
انجام دهید | انجام ندهید
:--| :-----
ابرپیوندهایی بنویسید که زمینه‌ای از محتوای مقصد را به شما بدهند. برای مثال: برخی پورت‌ها روی ماشین‌های شما باز هستند. برای جزئیات بیشتر به <a href="#check-required-ports">بررسی پورت‌های موردنیاز</a> مراجعه کنید. | از عبارت‌های مبهم مانند «اینجا را کلیک کنید» استفاده کنید. برای مثال: برخی پورت‌ها روی ماشین‌های شما باز هستند. برای جزئیات بیشتر <a href="#check-required-ports">اینجا</a> را ببینید.
پیوندها را به سبک Markdown بنویسید: `[link text](URL)`. برای مثال: `[Hugo shortcodes](/docs/contribute/style/hugo-shortcodes/#table-captions)` و خروجی آن [Hugo shortcodes](/docs/contribute/style/hugo-shortcodes/#table-captions) است. | پیوندها را به سبک HTML بنویسید: `<a href="/media/examples/link-element-example.css" target="_blank">Visit our tutorial!</a>`، یا پیوندهایی بسازید که در زبانه یا پنجره جدید باز شوند. برای مثال: `[example website](https://example.com){target="_blank"}`
{{< /table >}}

### فهرست‌ها

آیتم‌هایی را که به یکدیگر مرتبط هستند و باید به ترتیب مشخصی ظاهر شوند، یا برای نشان‌دادن ارتباط میان چند آیتم،
در یک فهرست گروه‌بندی کنید. هنگامی که صفحه‌خوان
به یک فهرست (چه مرتب و چه نامرتب) می‌رسد، به کاربر اعلام می‌کند
که گروهی از آیتم‌های فهرست وجود دارد. سپس کاربر می‌تواند با کلیدهای جهت‌نما
میان آیتم‌های مختلف فهرست به بالا و پایین حرکت کند. پیوندهای ناوبری وب‌سایت نیز می‌توانند
به‌صورت آیتم‌های فهرست علامت‌گذاری شوند؛ زیرا در نهایت چیزی جز گروهی از پیوندهای مرتبط نیستند.

- اگر یک یا چند آیتم فهرست جمله کامل هستند، انتهای هر آیتم را با نقطه تمام کنید. برای حفظ یکنواختی، معمولاً یا همه آیتم‌ها باید جمله کامل باشند یا هیچ‌کدام.

  {{< alert color="info" title="Note" >}}
  فهرست‌های مرتبی که بخشی از یک جمله مقدماتی ناتمام هستند، می‌توانند با حروف کوچک
  و علامت‌گذاری‌ای نوشته شوند که گویی هر آیتم بخشی از جمله مقدماتی است.
  {{< /alert >}}

- برای فهرست‌های مرتب از عدد یک (`1.`) استفاده کنید.

- برای فهرست‌های نامرتب از (`+`)، (`*`) یا (`-`) استفاده کنید.

- پس از هر فهرست یک خط خالی بگذارید.

- فهرست‌های تودرتو را با چهار فاصله تورفتگی بدهید (برای مثال، ⋅⋅⋅⋅).

- آیتم‌های فهرست می‌توانند از چند پاراگراف تشکیل شوند. هر پاراگراف بعدی در یک آیتم فهرست
  باید با چهار فاصله یا یک تب تورفتگی داشته باشد.

### جدول‌ها

هدف معنایی یک جدول داده، ارائه داده‌های جدولی است. کاربران بینا می‌توانند
جدول را به‌سرعت مرور کنند، اما صفحه‌خوان آن را خط‌به‌خط می‌خواند. عنوان جدول (table caption)
برای ایجاد یک عنوان توصیفی برای جدول داده استفاده می‌شود. فناوری‌های کمکی (AT)
از عنصر caption در HTML برای معرفی محتوای جدول به کاربر در ساختار صفحه استفاده می‌کنند.

- با استفاده از [شورت‌کدهای Hugo](/docs/contribute/style/hugo-shortcodes/#table-captions) برای جدول‌ها عنوان جدول اضافه کنید.

## بهترین روش‌ها برای محتوا

این بخش شامل بهترین روش‌های پیشنهادی برای تولید محتوایی واضح، مختصر و یکدست است.

### از زمان حال استفاده کنید

{{< table caption = "Do and Don't - Use present tense" >}}
انجام دهید | انجام ندهید
:--| :-----
This command starts a proxy. (این دستور یک پراکسی را راه‌اندازی می‌کند.) | This command will start a proxy. (این دستور یک پراکسی را راه‌اندازی خواهد کرد.)
 {{< /table >}}

استثنا: اگر برای انتقال معنای درست لازم است، از زمان آینده یا گذشته استفاده کنید.

### از جمله‌های معلوم استفاده کنید

{{< table caption = "Do and Don't - Use active voice" >}}
انجام دهید | انجام ندهید
:--| :-----
You can explore the API using a browser. (شما می‌توانید API را با یک مرورگر بررسی کنید.) | The API can be explored using a browser. (API را می‌توان با یک مرورگر بررسی کرد.)
The YAML file specifies the replica count. (فایل YAML تعداد replica را مشخص می‌کند.) | The replica count is specified in the YAML file. (تعداد replica در فایل YAML مشخص می‌شود.)
{{< /table >}}

استثنا: اگر استفاده از جمله معلوم به ساختاری نامناسب منجر می‌شود، از جمله مجهول استفاده کنید.

### از زبان ساده و مستقیم استفاده کنید

از زبان ساده و مستقیم استفاده کنید. از به‌کاربردن عبارت‌های غیرضروری، مانند گفتن «please» (لطفاً)، پرهیز کنید.

{{< table caption = "Do and Don't - Use simple and direct language" >}}
انجام دهید | انجام ندهید
:--| :-----
To create a ReplicaSet, ... (برای ایجاد یک ReplicaSet، ...) | In order to create a ReplicaSet, ... (به‌منظور ایجاد یک ReplicaSet، ...)
See the configuration file. (فایل پیکربندی را ببینید.) | Please see the configuration file. (لطفاً فایل پیکربندی را ببینید.)
View the pods. (پادها را مشاهده کنید.) | With this next command, we'll view the pods. (با دستور بعدی، پادها را مشاهده می‌کنیم.)
{{< /table >}}

### خواننده را «شما» خطاب کنید

{{< table caption = "Do and Don't - Addressing the reader" >}}
انجام دهید | انجام ندهید
:--| :-----
You can create a Deployment by ... (شما می‌توانید با ... یک Deployment ایجاد کنید.) | We'll create a Deployment by ... (ما با ... یک Deployment ایجاد می‌کنیم.)
In the preceding output, you can see... (در خروجی بالا می‌توانید ... را ببینید.) | In the preceding output, we can see ... (در خروجی بالا می‌توانیم ... را ببینیم.)
{{< /table >}}

### از عبارت‌های لاتین پرهیز کنید

به‌جای اختصارهای لاتین، از واژه‌های انگلیسی استفاده کنید.

{{< table caption = "Do and Don't - Avoid Latin phrases" >}}
انجام دهید | انجام ندهید
:--| :-----
For example, ... | e.g., ...
That is, ...| i.e., ...
{{< /table >}}

استثنا: برای et cetera از «etc.» استفاده کنید.

## الگوهایی که باید از آن‌ها پرهیز کرد

### از به‌کاربردن «ما» (we) پرهیز کنید

استفاده از «we» در یک جمله می‌تواند گیج‌کننده باشد، زیرا خواننده ممکن است نداند
آیا جزو «ما»یی است که شما توصیف می‌کنید یا نه.

{{< table caption = "Do and Don't - Patterns to avoid" >}}
انجام دهید | انجام ندهید
:--| :-----
Version 1.4 includes ... (نسخه ۱.۴ شامل ... است.) | In version 1.4, we have added ... (در نسخه ۱.۴، ... را اضافه کرده‌ایم.)
Kubernetes provides a new feature for ... (کوبرنتیز قابلیت جدیدی برای ... ارائه می‌دهد.) | We provide a new feature ... (ما قابلیت جدیدی ارائه می‌دهیم ...)
This page teaches you how to use pods. (این صفحه به شما نشان می‌دهد چگونه از پادها استفاده کنید.) | In this page, we are going to learn about pods. (در این صفحه می‌خواهیم درباره پادها یاد بگیریم.)
{{< /table >}}

### از اصطلاحات تخصصی و اصطلاحات عامیانه پرهیز کنید

برخی خوانندگان انگلیسی را به‌عنوان زبان دوم صحبت می‌کنند. برای درک بهتر آن‌ها، از اصطلاحات تخصصی (jargon) و اصطلاحات عامیانه (idiom) پرهیز کنید.

{{< table caption = "Do and Don't - Avoid jargon and idioms" >}}
انجام دهید | انجام ندهید
:--| :-----
Internally, ... (در سطح داخلی، ...) | Under the hood, ... (زیر کاپوت، ...)
Create a new cluster. (یک کلاستر جدید ایجاد کنید.) | Turn up a new cluster. (یک کلاستر جدید راه بیندازید.)
{{< /table >}}

### از بیان مطالب درباره آینده پرهیز کنید

از دادن وعده یا اشاره درباره آینده خودداری کنید. اگر لازم است درباره
یک قابلیت آلفا صحبت کنید، متن را زیر سرفصلی قرار دهید که آن را به‌عنوان اطلاعات آلفا
مشخص می‌کند.

استثنای این قاعده، مستندات مربوط به منسوخ‌شدن‌های اعلام‌شده‌ای است
که حذف آن‌ها در نسخه‌های آینده هدف‌گذاری شده است. یک نمونه از این مستندات،
[راهنمای مهاجرت API های منسوخ‌شده](/docs/reference/using-api/deprecation-guide/) است.

### از بیانی که به‌زودی منسوخ می‌شود پرهیز کنید

از واژه‌هایی مانند «currently» (در حال حاضر) و «new» (جدید) پرهیز کنید. قابلیتی که امروز جدید است ممکن است
چند ماه دیگر جدید به حساب نیاید.

{{< table caption = "Do and Don't - Avoid statements that will soon be out of date" >}}
انجام دهید | انجام ندهید
:--| :-----
In version 1.4, ... (در نسخه ۱.۴، ...) | In the current version, ... (در نسخه فعلی، ...)
The Federation feature provides ... (قابلیت Federation ... را فراهم می‌کند.) | The new Federation feature provides ... (قابلیت جدید Federation ... را فراهم می‌کند.)
{{< /table >}}

### از واژه‌هایی که سطح خاصی از درک را فرض می‌کنند پرهیز کنید

از واژه‌هایی مانند «just» (فقط)، «simply» (به‌سادگی)، «easy» (آسان)، «easily» (به‌آسانی) یا «simple» (ساده) پرهیز کنید. این واژه‌ها ارزشی اضافه نمی‌کنند.

{{< table caption = "Do and Don't - Avoid insensitive words" >}}
انجام دهید | انجام ندهید
:--| :-----
Include one command in ... (یک دستور را در ... بگنجانید) | Include just one command in ... (فقط یک دستور را در ... بگنجانید)
Run the container ... (کانتینر را اجرا کنید ...) | Simply run the container ... (به‌سادگی کانتینر را اجرا کنید ...)
You can remove ... (می‌توانید ... را حذف کنید) | You can easily remove ... (می‌توانید ... را به‌آسانی حذف کنید)
These steps ... (این مراحل ...) | These simple steps ... (این مراحل ساده ...)
{{< /table >}}

### فایل EditorConfig
پروژه کوبرنتیز یک فایل EditorConfig نگهداری می‌کند که ترجیحات سبک مشترک را در ویرایشگرهای متن
مانند VS Code تنظیم می‌کند. اگر می‌خواهید مطمئن شوید مشارکت‌های شما با
سایر بخش‌های پروژه یکدست است، می‌توانید از این فایل استفاده کنید. برای مشاهده فایل، به
[`.editorconfig`](https://github.com/kubernetes/website/blob/main/.editorconfig) در ریشه مخزن مراجعه کنید.

## {{% heading "whatsnext" %}}

* درباره [نوشتن یک موضوع جدید](/docs/contribute/style/write-new-topic/) بیاموزید.
* درباره [استفاده از قالب‌های صفحه](/docs/contribute/style/page-content-types/) بیاموزید.
* درباره [شورت‌کدهای سفارشی Hugo](/docs/contribute/style/hugo-shortcodes/) بیاموزید.
* درباره [ایجاد یک pull request](/docs/contribute/new-content/open-a-pr/) بیاموزید.

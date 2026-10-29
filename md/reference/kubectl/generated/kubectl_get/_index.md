---
title: kubectl get
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  نمایش یک یا چند منبع
no_list: true
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


## {{% heading "synopsis" %}}


یک یا چند منبع را نمایش می‌دهد.

 این دستور جدولی از مهم‌ترین اطلاعات منابع مشخص‌شده را چاپ می‌کند. می‌توانید فهرست را با یک انتخابگر برچسب (label selector) و فلگ ‎--selector فیلتر کنید. اگر نوع منبع موردنظر وابسته به فضای نام (namespace) باشد و هیچ فضای نامی مشخص نکنید، فقط نتایج موجود در فضای نام جاری را خواهید دید.

 اگر خروجی را 'template' تعیین کنید و یک قالب Go را به‌عنوان مقدار فلگ ‎--template بدهید، می‌توانید ویژگی‌های منابع دریافت‌شده را فیلتر کنید.

برای دیدن فهرست کامل منابع پشتیبانی‌شده، از دستور "kubectl api-resources" استفاده کنید.

```
kubectl get [(-o|--output=)json|yaml|kyaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file|custom-columns|custom-columns-file|wide] (TYPE[.VERSION][.GROUP] [NAME | -l label] | TYPE[.VERSION][.GROUP]/NAME ...) [flags]
```

## {{% heading "examples" %}}

```
  # List all pods in ps output format
  kubectl get pods
  
  # List all pods in ps output format with more information (such as node name)
  kubectl get pods -o wide
  
  # List a single replication controller with specified NAME in ps output format
  kubectl get replicationcontroller web
  
  # List deployments in JSON output format, in the "v1" version of the "apps" API group
  kubectl get deployments.v1.apps -o json
  
  # List a single pod in JSON output format
  kubectl get -o json pod web-pod-13je7
  
  # List a pod identified by type and name specified in "pod.yaml" in JSON output format
  kubectl get -f pod.yaml -o json
  
  # List resources from a directory with kustomization.yaml - e.g. dir/kustomization.yaml
  kubectl get -k dir/
  
  # Return only the phase value of the specified pod
  kubectl get -o template pod/web-pod-13je7 --template={{.status.phase}}
  
  # List resource information in custom columns
  kubectl get pod test-pod -o custom-columns=CONTAINER:.spec.containers[0].name,IMAGE:.spec.containers[0].image
  
  # List all replication controllers and services together in ps output format
  kubectl get rc,services
  
  # List one or more resources by their type and names
  kubectl get rc/web service/frontend pods/web-pod-13je7
  
  # List the 'status' subresource for a single pod
  kubectl get pod web-pod-13je7 --subresource status
  
  # List all deployments in namespace 'backend'
  kubectl get deployments.apps --namespace backend
  
  # List all pods existing in all namespaces
  kubectl get pods --all-namespaces
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">-A, --all-namespaces</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، آبجکت‌های درخواست‌شده را در همهٔ فضاهای نام فهرست می‌کند. فضای نام موجود در context جاری نادیده گرفته می‌شود، حتی اگر با ‎--namespace مشخص شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--allow-missing-template-keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگامی که یک فیلد یا کلید map در قالب وجود نداشته باشد، از هرگونه خطا در قالب‌ها چشم‌پوشی می‌شود. این گزینه فقط برای قالب‌های خروجی golang و jsonpath اعمال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--chunk-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 500</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست‌های بزرگ را به‌جای ارسال یکجا، در چند بخش برمی‌گرداند. برای غیرفعال‌کردن این قابلیت، مقدار 0 را بدهید.</p></td>
</tr>

<tr>
<td colspan="2">--field-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی فیلد) برای فیلترکردن؛ از عملگرهای '=' و '==' و '!=' پشتیبانی می‌کند (برای نمونه ‎--field-selector key1=value1,key2=value2). سرور برای هر نوع، فقط تعداد محدودی از پرس‌وجوهای فیلد را پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایل، دایرکتوری یا URL فایل‌هایی که منبع موردنظر برای دریافت از سرور را مشخص می‌کنند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور get</p></td>
</tr>

<tr>
<td colspan="2">--ignore-not-found</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر روی true تنظیم شود، خطای NotFound را برای آبجکت‌های مشخصی که وجود ندارند سرکوب می‌کند. استفاده از این فلگ همراه با دستورهایی که مجموعه‌ای از منابع را پرس‌وجو می‌کنند، در صورت پیدا نشدن هیچ منبعی، اثری ندارد.</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با ‎-f یا ‎-R استفاده کرد.</p></td>
</tr>

<tr>
<td colspan="2">-L, --label-columns strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از برچسب‌ها را که با ویرگول از هم جدا شده‌اند می‌پذیرد تا به‌صورت ستون نمایش داده شوند. نام‌ها به بزرگی و کوچکی حروف حساس هستند. همچنین می‌توانید این فلگ را چند بار به کار ببرید، مانند ‎-L label1 -L label2...</p></td>
</tr>

<tr>
<td colspan="2">--no-headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگام استفاده از قالب خروجی پیش‌فرض یا custom-column، سرستون‌ها را چاپ نمی‌کند (به‌طور پیش‌فرض سرستون‌ها چاپ می‌شوند).</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب خروجی. یکی از این موارد: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file, custom-columns, custom-columns-file, wide). برای اطلاعات بیشتر، ستون‌های سفارشی [https://kubernetes.io/docs/reference/kubectl/#custom-columns]، قالب golang [http://golang.org/pkg/text/template/#pkg-overview] و قالب jsonpath [https://kubernetes.io/docs/reference/kubectl/jsonpath/] را ببینید.</p></td>
</tr>

<tr>
<td colspan="2">--output-watch-events</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگام استفاده از ‎--watch یا ‎--watch-only، آبجکت‌های رویداد watch را در خروجی نمایش می‌دهد. آبجکت‌های موجود به‌صورت رویدادهای اولیهٔ ADDED در خروجی می‌آیند.</p></td>
</tr>

<tr>
<td colspan="2">--raw string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URI خامی که باید از سرور درخواست شود. از سازوکار انتقالی استفاده می‌کند که در فایل kubeconfig مشخص شده است.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری استفاده‌شده در ‎-f یا ‎--filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلترکردن؛ از عملگرهای '=' و '==' و '!=' و 'in' و 'notin' پشتیبانی می‌کند (برای نمونه ‎-l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسب مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--server-print&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، سرور خروجی جدولی مناسب را برمی‌گرداند. از APIهای افزونه و CRDها پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--show-kind</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، نوع منبع آبجکت‌های درخواست‌شده را فهرست می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--show-labels</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگام چاپ، همهٔ برچسب‌ها را در ستون آخر نمایش می‌دهد (به‌طور پیش‌فرض ستون برچسب‌ها پنهان است).</p></td>
</tr>

<tr>
<td colspan="2">--show-managed-fields</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام چاپ آبجکت‌ها در قالب JSON یا YAML، فیلد managedFields حفظ می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--sort-by string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر خالی نباشد، انواع فهرستی را بر اساس این مشخصهٔ فیلد مرتب می‌کند. مشخصهٔ فیلد به‌صورت یک عبارت JSONPath بیان می‌شود (برای نمونه '{.metadata.name}'). فیلدی از منبع API که این عبارت JSONPath مشخص می‌کند، باید از نوع عدد صحیح یا رشته باشد.</p></td>
</tr>

<tr>
<td colspan="2">--subresource string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، زیرمنبع (subresource) آبجکت درخواست‌شده را دریافت می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--template string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رشتهٔ قالب یا مسیر فایل قالب که هنگام استفاده از ‎-o=go-template یا ‎-o=go-template-file به کار می‌رود. قالب آن، قالب‌های golang است [http://golang.org/pkg/text/template/#pkg-overview].</p></td>
</tr>

<tr>
<td colspan="2">-w, --watch</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پس از فهرست‌کردن یا دریافت آبجکت درخواست‌شده، تغییرات آن را زیر نظر می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--watch-only</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تغییرات آبجکت‌های درخواست‌شده را بدون فهرست‌کردن یا دریافت اولیهٔ آن‌ها زیر نظر می‌گیرد.</p></td>
</tr>

</tbody>
</table>

## {{% heading "parentoptions" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--as string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری‌ای که عملیات با جعل هویت (impersonate) آن انجام می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات با جعل هویت آن انجام می‌شود. برای مشخص کردن چند گروه می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات با جعل هویت آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات اضافی کاربر که عملیات با جعل هویت آن انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پوشهٔ پیش‌فرض حافظهٔ نهان (cache)</p></td>
</tr>

<tr>
<td colspan="2">--certificate-authority string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی مرجع صدور گواهی (certificate authority)</p></td>
</tr>

<tr>
<td colspan="2">--client-certificate string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی کلاینت برای TLS</p></td>
</tr>

<tr>
<td colspan="2">--client-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل کلید کلاینت برای TLS</p></td>
</tr>

<tr>
<td colspan="2">--cluster string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام context از kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فشرده‌سازی پاسخ برای همهٔ درخواست‌ها به سرور غیرفعال می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. با این کار اتصال‌های HTTPS شما ناامن می‌شوند</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig برای استفاده در درخواست‌های CLI.</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در تنظیمات ترجیحی. می‌توان این قابلیت را با export کردن feature gate به‌صورت KUBECTL_KUBERC=false یا خاموش کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام به یکسان بودن نسخهٔ سرور با نسخهٔ کلاینت</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، دامنهٔ فضای نام برای این درخواست CLI</p></td>
</tr>

<tr>
<td colspan="2">--password string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه (basic authentication) در API server</p></td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از مقادیر (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
</tr>

<tr>
<td colspan="2">--profile-output string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "profile.pprof"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که پروفایل در آن نوشته می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--proxy-url string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی برای استفاده در درخواست‌ها به API server</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (مثلاً 1s، 2m، 3h). مقدار صفر یعنی درخواست‌ها هیچ‌گاه به پایان مهلت نمی‌رسند.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و درگاه (port) سرور API کوبرنتیز</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به همین مدت در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای (non memory backends) ثبت می‌شوند</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-db string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "cadvisor"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-host string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "localhost:8086"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و درگاه پایگاه داده به‌صورت host:port</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژهٔ پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-secure</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>استفاده از اتصال امن با پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-table string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "stats"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام جدول</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-user string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--tls-server-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر این مقدار ارائه نشود، از نام میزبانی (hostname) که برای برقراری ارتباط با سرور به کار رفته است استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن Bearer برای احراز هویت در API server</p></td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری از kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--username string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری برای احراز هویت پایه در API server</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ گزینهٔ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - ابزار kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

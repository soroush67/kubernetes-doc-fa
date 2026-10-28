---
title: kubectl annotate
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  به‌روزرسانی حاشیه‌نویسی‌های (annotation) یک منبع
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


حاشیه‌نویسی‌های (annotation) یک یا چند منبع را به‌روزرسانی می‌کند.

 همه آبجکت‌های کوبرنتیز قابلیت ذخیره داده‌های اضافی را به‌صورت حاشیه‌نویسی (annotation) همراه با آبجکت دارند. حاشیه‌نویسی‌ها جفت‌های کلید/مقدار هستند که می‌توانند از برچسب‌ها بزرگ‌تر باشند و مقادیر رشته‌ای دلخواه، مانند JSON ساختاریافته، را در بر بگیرند. ابزارها و افزونه‌های سیستمی می‌توانند از حاشیه‌نویسی‌ها برای ذخیره داده‌های خود استفاده کنند.

 تلاش برای تنظیم حاشیه‌نویسی‌ای که از قبل وجود دارد با شکست مواجه می‌شود، مگر اینکه --overwrite تنظیم شده باشد. اگر --resource-version مشخص شده باشد و با نسخه فعلی منبع روی سرور مطابقت نداشته باشد، دستور با شکست مواجه خواهد شد.

برای مشاهده فهرست کامل منابع پشتیبانی‌شده از "kubectl api-resources" استفاده کنید.

```
kubectl annotate [--overwrite] (-f FILENAME | TYPE NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--resource-version=version]
```

## {{% heading "examples" %}}

```
  # Update pod 'foo' with the annotation 'description' and the value 'my frontend'
  # If the same annotation is set multiple times, only the last value will be applied
  kubectl annotate pods foo description='my frontend'
  
  # Update a pod identified by type and name in "pod.json"
  kubectl annotate -f pod.json description='my frontend'
  
  # Update pod 'foo' with the annotation 'description' and the value 'my frontend running nginx', overwriting any existing value
  kubectl annotate --overwrite pods foo description='my frontend running nginx'
  
  # Update all pods in the namespace
  kubectl annotate pods --all description='my frontend running nginx'
  
  # Update pod 'foo' only if the resource is unchanged from version 1
  kubectl annotate pods foo description='my frontend running nginx' --resource-version=1
  
  # Update pod 'foo' by removing an annotation named 'description' if it exists
  # Does not require the --overwrite flag
  kubectl annotate pods foo description-
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--all</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>همه منابع موجود در فضای نام (namespace) برای نوع‌های منبع مشخص‌شده را انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-A, --all-namespaces</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، آبجکت(های) درخواستی را در همه فضاهای نام (namespace) فهرست می‌کند. فضای نام موجود در context فعلی نادیده گرفته می‌شود، حتی اگر با --namespace مشخص شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--allow-missing-template-keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هرگونه خطا در قالب‌ها (template) را هنگامی که یک فیلد یا کلید map در قالب وجود ندارد نادیده می‌گیرد. فقط برای قالب‌های خروجی golang و jsonpath اعمال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run string[="unchanged"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>باید یکی از مقادیر &quot;none&quot;، &quot;server&quot; یا &quot;client&quot; باشد. در راهبرد client، فقط آبجکتی که ارسال می‌شد چاپ می‌شود، بدون آنکه ارسال شود. در راهبرد server، درخواست سمت سرور ثبت می‌شود، بدون آنکه منبع ذخیره (persist) شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-manager string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kubectl-annotate"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مدیری که برای ردیابی مالکیت فیلدها استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (selector) (پرس‌وجوی فیلد) برای فیلتر کردن؛ از '='، '==' و '!=' پشتیبانی می‌کند. (مثال: --field-selector key1=value1,key2=value2). سرور برای هر نوع فقط تعداد محدودی پرس‌وجوی فیلد را پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای شناسایی منبع.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنما برای annotate</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با -f یا -R استفاده کرد.</p></td>
</tr>

<tr>
<td colspan="2">--list</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، حاشیه‌نویسی‌های (annotation) یک منبع مشخص را نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--local</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، annotate با api-server ارتباط برقرار نمی‌کند و به‌صورت محلی اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب خروجی. یکی از: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).</p></td>
</tr>

<tr>
<td colspan="2">--overwrite</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اجازه می‌دهد حاشیه‌نویسی‌ها بازنویسی شوند؛ در غیر این صورت به‌روزرسانی‌هایی که حاشیه‌نویسی‌های موجود را بازنویسی می‌کنند رد می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری استفاده‌شده در -f, --filename را به‌صورت بازگشتی پردازش می‌کند. زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری قرار دارند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">--resource-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر خالی نباشد، به‌روزرسانی حاشیه‌نویسی (annotation) تنها در صورتی موفق می‌شود که این مقدار همان resource-version فعلی آبجکت باشد. فقط هنگام مشخص کردن یک منبع واحد معتبر است.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (selector) (پرس‌وجوی برچسب) برای فیلتر کردن؛ از '='، '==' و '!=' پشتیبانی می‌کند. (مثال: -l key1=value1,key2=value2)</p></td>
</tr>

<tr>
<td colspan="2">--show-managed-fields</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام چاپ آبجکت‌ها در قالب JSON یا YAML، managedFields را نگه می‌دارد.</p></td>
</tr>

<tr>
<td colspan="2">--template string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رشته قالب یا مسیر فایل قالب برای استفاده هنگام -o=go-template و -o=go-template-file. قالب‌بندی آن از نوع قالب‌های golang است [http://golang.org/pkg/text/template/#pkg-overview].</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که برای عملیات جعل هویت (impersonate) می‌شود. کاربر می‌تواند یک کاربر عادی یا یک service account در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که برای عملیات جعل هویت (impersonate) می‌شود؛ این فلگ را می‌توان برای مشخص کردن چند گروه تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>UID که برای عملیات جعل هویت (impersonate) می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات اضافی کاربر که برای عملیات جعل هویت (impersonate) می‌شود؛ این فلگ را می‌توان برای مشخص کردن چند مقدار برای یک کلید یکسان تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری پیش‌فرض کش</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستر kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام context در kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فشرده‌سازی پاسخ برای همه درخواست‌ها به سرور غیرفعال می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نخواهد شد. این کار اتصال‌های HTTPS شما را ناامن می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig که برای درخواست‌های CLI استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای تنظیمات ترجیحی استفاده می‌شود. این قابلیت را می‌توان با export کردن feature gate به‌صورت KUBECTL_KUBERC=false یا با خاموش کردن قابلیت از طریق KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه سرور را ملزم به تطابق با نسخه کلاینت می‌کند</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، دامنه فضای نام (namespace) برای این درخواست CLI</p></td>
</tr>

<tr>
<td colspan="2">--password string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه (basic authentication) به API server</p></td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پروکسی که برای درخواست‌ها به API server استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار قبل از صرف‌نظر کردن از یک درخواست واحد به سرور. مقادیر غیرصفر باید شامل واحد زمانی مربوطه باشند (مثلاً 1s، 2m، 3h). مقدار صفر به معنای عدم اعمال زمان انتظار (timeout) برای درخواست‌ها است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در storage driver به مدت این بازه بافر می‌شوند و به‌صورت یک تراکنش واحد در بک‌اندهای غیرحافظه‌ای ثبت (commit) می‌شوند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان:درگاه پایگاه داده (host:port)</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه پایگاه داده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر ارائه نشود، از نام میزبانی که برای ارتباط با سرور استفاده شده است استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن Bearer برای احراز هویت به API server</p></td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربر kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--username string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری برای احراز هویت پایه (basic authentication) به API server</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ کرده و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

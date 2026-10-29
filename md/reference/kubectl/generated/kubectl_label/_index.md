---
title: kubectl label
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  به‌روزرسانی برچسب‌های یک منبع
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


برچسب‌های یک منبع را به‌روزرسانی می‌کند.

  *  کلید و مقدار هر برچسب باید با یک حرف یا عدد شروع شوند و می‌توانند شامل حروف، اعداد، خط تیره، نقطه و زیرخط باشند. طول هر یک از آن‌ها حداکثر ۶۳ نویسه است.
  *  کلید می‌تواند به‌صورت اختیاری با یک پیشوند زیردامنهٔ DNS و یک «/» شروع شود؛ مانند example.com/my-app.
  *  اگر مقدار `--overwrite` برابر true باشد، برچسب‌های موجود را می‌توان بازنویسی کرد؛ در غیر این صورت، تلاش برای بازنویسی یک برچسب به خطا می‌انجامد.
  *  اگر `--resource-version` مشخص شده باشد، به‌روزرسانی‌ها از همین نسخهٔ منبع استفاده می‌کنند؛ در غیر این صورت، از resource-version فعلی استفاده می‌شود.

```
kubectl label [--overwrite] (-f FILENAME | TYPE NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--resource-version=version]
```

## {{% heading "examples" %}}

```
  # Update pod 'foo' with the label 'unhealthy' and the value 'true'
  kubectl label pods foo unhealthy=true
  
  # Update pod 'foo' with the label 'status' and the value 'unhealthy', overwriting any existing value
  kubectl label --overwrite pods foo status=unhealthy
  
  # Update all pods in the namespace
  kubectl label pods --all status=unhealthy
  
  # Update a pod identified by the type and name in "pod.json"
  kubectl label -f pod.json status=unhealthy
  
  # Update pod 'foo' only if the resource is unchanged from version 1
  kubectl label pods foo status=unhealthy --resource-version=1
  
  # Update pod 'foo' by removing a label named 'bar' if it exists
  # Does not require the --overwrite flag
  kubectl label pods foo bar-
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>همهٔ منابعِ انواع مشخص‌شده را در فضای نام انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-A, --all-namespaces</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، عملیات مشخص‌شده در همهٔ فضاهای نام بررسی می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--allow-missing-template-keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگامی که یک فیلد یا کلید map در الگو وجود نداشته باشد، از خطاهای الگو چشم‌پوشی می‌شود. این گزینه فقط برای قالب‌های خروجی golang و jsonpath کاربرد دارد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run string[="unchanged"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار آن باید یکی از &quot;none&quot;، &quot;server&quot; یا &quot;client&quot; باشد. در راهبرد client، فقط آبجکتی که قرار است ارسال شود چاپ می‌شود و ارسالی صورت نمی‌گیرد. در راهبرد server، درخواست سمت سرور ارسال می‌شود، اما منبع ذخیره نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-manager string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kubectl-label"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مدیری که برای ردیابی مالکیت فیلدها استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی فیلد) برای فیلترکردن، که از '='، '==' و '!=' پشتیبانی می‌کند (برای نمونه: --field-selector key1=value1,key2=value2). سرور برای هر نوع فقط از تعداد محدودی پرس‌وجوی فیلد پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایل، دایرکتوری یا URL فایل‌هایی که منبعِ موردنظر برای به‌روزرسانی برچسب‌ها را مشخص می‌کنند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای label</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با -f یا -R به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">--list</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، برچسب‌های منبع داده‌شده نمایش داده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--local</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فرمان label با api-server ارتباط برقرار نمی‌کند و به‌صورت محلی اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب خروجی؛ یکی از موارد زیر: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).</p></td>
</tr>

<tr>
<td colspan="2">--overwrite</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، بازنویسی برچسب‌ها مجاز است؛ در غیر این صورت، به‌روزرسانی‌هایی که برچسب‌های موجود را بازنویسی می‌کنند رد می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری استفاده‌شده در -f, --filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">--resource-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر خالی نباشد، به‌روزرسانی برچسب‌ها فقط زمانی موفق می‌شود که این مقدار همان resource-version فعلی آبجکت باشد. این گزینه فقط هنگام مشخص‌کردن یک منبع واحد معتبر است.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلترکردن، که از '='، '=='، '!='، 'in' و 'notin' پشتیبانی می‌کند (برای نمونه: -l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسبِ مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--show-managed-fields</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام چاپ آبجکت‌ها در قالب JSON یا YAML، فیلد managedFields حفظ می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--template string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رشتهٔ الگو یا مسیر فایل الگو که هنگام استفاده از -o=go-template یا -o=go-template-file به کار می‌رود. قالب الگو همان الگوهای golang است [http://golang.org/pkg/text/template/#pkg-overview].</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که عملیات به نام آن انجام می‌شود (جعل هویت). این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات به نام آن انجام می‌شود. برای مشخص‌کردن چند گروه می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات به نام آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که عملیات به نام آن انجام می‌شود. برای مشخص‌کردن چند مقدار برای یک کلید می‌توان این فلگ را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی مرجع صدور گواهی (CA)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینه (context) از kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فشرده‌سازی پاسخ برای همهٔ درخواست‌ها به سرور غیرفعال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. با این کار، اتصال‌های HTTPS شما ناامن می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای ترجیحات استفاده می‌شود. می‌توان این قابلیت را با export کردن feature gate به‌صورت KUBECTL_KUBERC=false یا خاموش‌کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام می‌کند که نسخهٔ سرور با نسخهٔ کلاینت مطابقت داشته باشد.</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، دامنهٔ فضای نام برای این درخواست CLI را مشخص می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود؛ یکی از موارد (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی برای درخواست‌ها به API server</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از چشم‌پوشی از یک درخواست به سرور باید منتظر ماند. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای نمونه 1s، 2m، 3h). مقدار صفر به این معناست که درخواست‌ها هیچ‌گاه منقضی نمی‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و پورت API server کوبرنتیز</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به مدت این بازه بافر می‌شوند و سپس به‌صورت یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و پورت پایگاه داده (host:port)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر تعیین نشود، از نام میزبانی که برای ارتباط با سرور به کار رفته است استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ گزینهٔ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تنظیم می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - فرمان kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

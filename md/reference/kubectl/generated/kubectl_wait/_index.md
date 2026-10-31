--- 
title: kubectl wait
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  منتظر ماندن برای برقرار شدن شرطی مشخص روی یک یا چند منبع
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


منتظر می‌ماند تا شرطی مشخص روی یک یا چند منبع برقرار شود.

 این فرمان چند منبع را دریافت می‌کند و منتظر می‌ماند تا شرط تعیین‌شده در فیلد Status همهٔ منابع داده‌شده دیده شود.

 همچنین اگر کلیدواژهٔ "create" یا "delete" را به‌عنوان مقدار پرچم ‎--for‎ بدهید، این فرمان منتظر می‌ماند تا مجموعهٔ منابع داده‌شده ایجاد یا حذف شوند.

 هنگامی که شرط تعیین‌شده برقرار شود، پیامی مبنی بر موفقیت در stdout چاپ می‌شود. برای تغییر مقصد خروجی می‌توانید از گزینهٔ ‎-o‎ استفاده کنید.

```
kubectl wait ([-f FILENAME] | resource.group/resource.name | resource.group [(-l label | --all)]) [--for=create|--for=delete|--for condition=available|--for=jsonpath='{}'[=value]]
```

## {{% heading "examples" %}}

```
  # Wait for the pod "busybox1" to contain the status condition of type "Ready"
  kubectl wait --for=condition=Ready pod/busybox1
  
  # The default value of status condition is true; you can wait for other targets after an equal delimiter (compared after Unicode simple case folding, which is a more general form of case-insensitivity)
  kubectl wait --for=condition=Ready=false pod/busybox1
  
  # Wait for the pod "busybox1" to contain the status phase to be "Running"
  kubectl wait --for=jsonpath='{.status.phase}'=Running pod/busybox1
  
  # Wait for pod "busybox1" to be Ready
  kubectl wait --for='jsonpath={.status.conditions[?(@.type=="Ready")].status}=True' pod/busybox1
  
  # Wait for the service "loadbalancer" to have ingress
  kubectl wait --for=jsonpath='{.status.loadBalancer.ingress}' service/loadbalancer
  
  # Wait for the secret "busybox1" to be created, with a timeout of 30s
  kubectl create secret generic busybox1
  kubectl wait --for=create secret/busybox1 --timeout=30s
  
  # Wait for the pod "busybox1" to be deleted, with a timeout of 60s, after having issued the "delete" command
  kubectl delete pod/busybox1
  kubectl wait --for=delete pod/busybox1 --timeout=60s
  
  # Wait for pod "busybox1" to be created AND reach the "Ready" status condition
  kubectl wait --for=condition=Ready --for=create pod/busybox1
  
  # Wait for pod "busybox1" to reach the "Ready" status OR for its containers to report a "False" readiness state
  until kubectl wait pod/busybox1 --for=condition=Ready --timeout=1s 2>/dev/null || \
  kubectl wait pod/busybox1 --for=condition=ContainersReady=False --timeout=1s 2>/dev/null; \
  do echo "Checking conditions..."; sleep 1; done
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>همهٔ منابعِ انواع منبع تعیین‌شده را در فضای نام (namespace) انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-A, --all-namespaces</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، آبجکت‌های درخواست‌شده را در همهٔ فضاهای نام فهرست می‌کند. فضای نامِ زمینهٔ (context) فعلی نادیده گرفته می‌شود، حتی اگر با ‎--namespace‎ تعیین شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--allow-missing-template-keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگامی که فیلد یا کلید نگاشتی (map) در قالب وجود نداشته باشد، از هر خطایی در قالب‌ها چشم‌پوشی می‌شود. این گزینه فقط برای قالب‌های خروجی golang و jsonpath کاربرد دارد.</p></td>
</tr>

<tr>
<td colspan="2">--field-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (selector) مبتنی بر فیلد (پرس‌وجوی فیلد) برای فیلتر کردن، که از '='، '==' و '!=' پشتیبانی می‌کند (برای مثال ‎--field-selector key1=value1,key2=value2‎). سرور برای هر نوع فقط از تعداد محدودی پرس‌وجوی فیلد پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای شناسایی منبع.</p></td>
</tr>

<tr>
<td colspan="2">--for strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شرطی که باید منتظر آن ماند: [create|delete|condition=condition-name[=condition-value]|jsonpath='{JSONPath expression}'=[JSONPath value]]. مقدار پیش‌فرض condition-value برابر true است. مقادیر شرط پس از تبدیل سادهٔ حروف یونیکد (Unicode simple case folding) مقایسه می‌شوند که شکل کلی‌ترِ حساس نبودن به بزرگی و کوچکی حروف است. چند شرط پشتیبانی می‌شود و این شرط‌ها به ترتیب با یکدیگر AND می‌شوند. اگر ‎--for=create‎ داده شود، همیشه ابتدا منتظر آن می‌ماند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای wait</p></td>
</tr>

<tr>
<td colspan="2">--local</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، حاشیه‌نویسی (annotation) با api-server ارتباط برقرار نمی‌کند و به‌صورت محلی اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب خروجی. یکی از این مقادیر: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پوشهٔ استفاده‌شده در ‎-f, --filename‎ را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک پوشه سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر مبتنی بر برچسب (پرس‌وجوی برچسب) برای فیلتر کردن، که از '='، '==' و '!=' پشتیبانی می‌کند (برای مثال ‎-l key1=value1,key2=value2‎).</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رشتهٔ قالب یا مسیر فایل قالب که هنگام استفاده از ‎-o=go-template‎ یا ‎-o=go-template-file‎ به کار می‌رود. قالب‌بندی آن مطابق قالب‌های golang است [http://golang.org/pkg/text/template/#pkg-overview].</p></td>
</tr>

<tr>
<td colspan="2">--timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از منصرف شدن. مقدار صفر یعنی یک بار بررسی شود و منتظر نماند، و مقدار منفی یعنی به مدت یک هفته منتظر بماند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری‌ای که عملیات از طرف آن جعل هویت (impersonate) می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات از طرف آن جعل هویت می‌شود. برای تعیین چند گروه می‌توان این پرچم را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات از طرف آن جعل هویت می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که عملیات با آن جعل هویت می‌شود. برای تعیین چند مقدار برای یک کلید می‌توان این پرچم را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستر kubeconfig مورد نظر برای استفاده</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینهٔ kubeconfig مورد نظر برای استفاده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. این کار اتصال‌های HTTPS شما را ناامن می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در تنظیمات ترجیحی. می‌توان آن را با export کردن feature gate ‏KUBECTL_KUBERC=false یا خاموش کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از این مقادیر: (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از منصرف شدن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای مثال 1s، 2m، 3h). مقدار صفر یعنی درخواست‌ها هیچ‌گاه منقضی نشوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به این مدت بافر می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های (backend) غیرحافظه‌ای ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>استفاده از اتصال امن به پایگاه داده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سرور برای اعتبارسنجی گواهی سرور. اگر تعیین نشود، نام میزبانی که برای ارتباط با سرور به کار رفته است استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربر kubeconfig مورد نظر برای استفاده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های ‎--version‎ و ‎--version=raw‎ اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ ‎--version=vX.Y.Z...‎ نسخهٔ گزارش‌شده را تنظیم می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - فرمان kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

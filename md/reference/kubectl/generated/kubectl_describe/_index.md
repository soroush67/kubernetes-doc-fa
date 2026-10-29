---
title: kubectl describe
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  نمایش جزئیات یک منبع مشخص یا گروهی از منابع
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


جزئیات یک منبع مشخص یا گروهی از منابع را نمایش می‌دهد.

 این دستور توضیحی مفصل از منابع انتخاب‌شده، همراه با منابع مرتبط مانند رویدادها یا کنترل‌کننده‌ها، چاپ می‌کند. می‌توانید یک آبجکت را با نامش انتخاب کنید، همهٔ آبجکت‌های یک نوع را برگزینید، یک پیشوند نام بدهید یا از انتخابگر برچسب (label selector) استفاده کنید. برای مثال:

        $ kubectl describe TYPE NAME_PREFIX
        
 این دستور ابتدا به دنبال تطابق دقیق با TYPE و NAME_PREFIX می‌گردد. اگر چنین منبعی وجود نداشته باشد، جزئیات همهٔ منابعی را که نامشان با NAME_PREFIX آغاز می‌شود نمایش می‌دهد.

برای دیدن فهرست کامل منابع پشتیبانی‌شده، از دستور "kubectl api-resources" استفاده کنید.

```
kubectl describe (-f FILENAME | TYPE [NAME_PREFIX | -l label] | TYPE/NAME)
```

## {{% heading "examples" %}}

```
  # Describe a node
  kubectl describe nodes kubernetes-node-emt8.c.myproject.internal
  
  # Describe a pod
  kubectl describe pods/nginx
  
  # Describe a pod identified by type and name in "pod.json"
  kubectl describe -f pod.json
  
  # Describe all pods
  kubectl describe pods
  
  # Describe pods by label name=myLabel
  kubectl describe pods -l name=myLabel
  
  # Describe all pods managed by the 'frontend' replication controller
  # (rc-created pods get the name of the rc as a prefix in the pod name)
  kubectl describe pods frontend
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، آبجکت‌های درخواست‌شده را در همهٔ فضاهای نام (namespace) فهرست می‌کند. فضای نامِ زمینهٔ فعلی نادیده گرفته می‌شود، حتی اگر با --namespace مشخص شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--chunk-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 500</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست‌های بزرگ را به‌جای ارسال یکجا، در چند بخش برمی‌گرداند. برای غیرفعال کردن، مقدار 0 را بدهید.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایل، دایرکتوری یا URL فایل‌هایی که منبع موردنظر برای توصیف را در بر دارند</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور describe</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با -f یا -R به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری مشخص‌شده در -f یا --filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلتر کردن؛ از عملگرهای '=' و '==' و '!=' و 'in' و 'notin' پشتیبانی می‌کند (برای مثال -l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسبِ مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--show-events&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، رویدادهای مرتبط با آبجکتِ توصیف‌شده را نمایش می‌دهد. مقدار پیش‌فرض برای یک آبجکت true و برای چند آبجکت و تطابق پیشوندی false است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری‌ای که عملیات به جای آن انجام می‌شود (جعل هویت). این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس در یک فضای نام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات به جای آن انجام می‌شود. برای مشخص کردن چند گروه می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات به جای آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربری که عملیات به جای آن انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید می‌توان این فلگ را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینه‌ای (context) از kubeconfig که باید استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در ترجیحات. می‌توان این قابلیت را با export کردن feature gate به صورت KUBECTL_KUBERC=false یا خاموش کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام می‌کند که نسخهٔ سرور با نسخهٔ کلاینت مطابقت داشته باشد</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه (basic authentication) در سرور API</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پروکسی برای استفاده در درخواست‌ها به سرور API</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست به سرور منتظر می‌ماند. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای مثال 1s، 2m، 3h). مقدار صفر یعنی درخواست‌ها هیچ‌گاه منقضی نمی‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و پورت سرور API کوبرنتیز</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به این مدت بافر می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای ثبت می‌شوند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و پورت پایگاه داده به صورت host:port</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور به کار می‌رود. اگر مشخص نشود، از نام میزبانی که برای برقراری ارتباط با سرور استفاده شده است استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن Bearer برای احراز هویت در سرور API</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری برای احراز هویت پایه در سرور API</p></td>
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

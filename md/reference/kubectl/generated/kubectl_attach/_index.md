---
title: kubectl attach
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  اتصال به یک کانتینر در حال اجرا
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


این دستور به فرایندی متصل می‌شود که از پیش درون یک کانتینر موجود در حال اجرا است.

```
kubectl attach (POD | TYPE/NAME) -c CONTAINER
```

## {{% heading "examples" %}}

```
  # Get output from running pod mypod; use the 'kubectl.kubernetes.io/default-container' annotation
  # for selecting the container to be attached or the first container in the pod will be chosen
  kubectl attach mypod
  
  # Get output from ruby-container from pod mypod
  kubectl attach mypod -c ruby-container
  
  # Switch to raw terminal mode; sends stdin to 'bash' in ruby-container from pod mypod
  # and sends stdout/stderr from 'bash' back to the client
  kubectl attach mypod -c ruby-container -i -t
  
  # Get output from the first pod of a replica set named nginx
  kubectl attach rs/nginx
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">-c, --container string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کانتینر. اگر این مقدار مشخص نشود، برای انتخاب کانتینری که باید به آن متصل شد از حاشیه‌نویسی (annotation) kubectl.kubernetes.io/default-container استفاده می‌شود؛ در غیر این صورت، نخستین کانتینر موجود در پاد انتخاب خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--detach-keys string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "ctrl-p,ctrl-q"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دنباله‌ی کلیدهایی را که برای جدا شدن از یک کانتینر به کار می‌رود، با مقدار دلخواه جایگزین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور attach را نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--pod-running-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی (مانند 5s، 2m یا 3h و بزرگ‌تر از صفر) که باید منتظر ماند تا دست‌کم یک پاد در حال اجرا باشد.</p></td>
</tr>

<tr>
<td colspan="2">-q, --quiet</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فقط خروجی نشست راه دور را چاپ می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-i, --stdin</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ورودی استاندارد (stdin) را به کانتینر ارسال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-t, --tty</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که ورودی استاندارد یک ترمینال (TTY) است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که عملیات از طرف او و با هویت او انجام می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات با هویت آن انجام می‌شود. برای مشخص کردن چند گروه می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسه‌ی یکتا (UID) که عملیات با هویت آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که عملیات با هویت آن انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری پیش‌فرض حافظه‌ی نهان (cache).</p></td>
</tr>

<tr>
<td colspan="2">--certificate-authority string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی مرجع صدور گواهی (certificate authority).</p></td>
</tr>

<tr>
<td colspan="2">--client-certificate string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی کلاینت برای TLS.</p></td>
</tr>

<tr>
<td colspan="2">--client-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل کلید کلاینت برای TLS.</p></td>
</tr>

<tr>
<td colspan="2">--cluster string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از فایل kubeconfig که باید استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینه (context) ای از فایل kubeconfig که باید استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، فشرده‌سازی پاسخ برای همه‌ی درخواست‌هایی که به سرور فرستاده می‌شوند غیرفعال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، اعتبار گواهی سرور بررسی نمی‌شود. در این حالت، اتصال‌های HTTPS شما ناامن خواهند بود.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig که برای درخواست‌های خط فرمان (CLI) استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای ترجیحات کاربر استفاده می‌شود. برای غیرفعال کردن آن می‌توانید feature gate مربوط را با اکسپورت کردن KUBECTL_KUBERC=false غیرفعال کنید یا قابلیت را با KUBERC=off خاموش کنید.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام می‌کند که نسخه‌ی سرور با نسخه‌ی کلاینت مطابقت داشته باشد.</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، دامنه‌ی فضای نام این درخواست خط فرمان را مشخص می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--password string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه (basic authentication) در سرور API.</p></td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از این مقادیر است: (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
</tr>

<tr>
<td colspan="2">--profile-output string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "profile.pprof"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که پروفایل در آن نوشته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--proxy-url string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی که برای درخواست‌ها به سرور API استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور باید منتظر ماند. مقادیر غیرصفر باید واحد زمانی متناظر را داشته باشند (مثلاً 1s، 2m یا 3h). مقدار صفر به این معناست که برای درخواست‌ها هیچ مهلت زمانی‌ای در نظر گرفته نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و پورت سرور API کوبرنتیز.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عملیات نوشتن در درایور ذخیره‌سازی به مدت این بازه‌ی زمانی در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای (non memory backends) ثبت می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-db string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "cadvisor"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پایگاه داده.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-host string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "localhost:8086"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و پورت پایگاه داده به شکل host:port.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه‌ی پایگاه داده.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-secure</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای ارتباط با پایگاه داده از اتصال امن استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-table string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "stats"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام جدول.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-user string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری پایگاه داده.</p></td>
</tr>

<tr>
<td colspan="2">--tls-server-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر این مقدار ارائه نشود، از نام میزبانی که برای برقراری ارتباط با سرور به کار رفته است استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن حامل (bearer token) برای احراز هویت در سرور API.</p></td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری از فایل kubeconfig که باید استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--username string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری برای احراز هویت پایه در سرور API.</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و از برنامه خارج می‌شوند؛ گزینه‌ی --version=vX.Y.Z... نسخه‌ی گزارش‌شده را تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافت‌شده از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - ابزار kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

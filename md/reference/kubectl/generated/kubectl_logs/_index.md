---
title: kubectl logs
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  چاپ لاگ‌های یک کانتینر در یک پاد
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


این فرمان لاگ‌های یک کانتینر را در یک پاد یا منبع مشخص‌شده چاپ می‌کند. اگر پاد فقط یک کانتینر داشته باشد، ذکر نام کانتینر اختیاری است.

```
kubectl logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER]
```

## {{% heading "examples" %}}

```
  # Return snapshot logs from pod nginx with only one container
  kubectl logs nginx
  
  # Return snapshot logs from pod nginx, prefixing each line with the source pod and container name
  kubectl logs nginx --prefix
  
  # Return snapshot logs from pod nginx, limiting output to 500 bytes
  kubectl logs nginx --limit-bytes=500
  
  # Return snapshot logs from pod nginx, waiting up to 20 seconds for it to start running.
  kubectl logs nginx --pod-running-timeout=20s
  
  # Return snapshot logs from pod nginx with multi containers
  kubectl logs nginx --all-containers=true
  
  # Return snapshot logs from all pods in the deployment nginx
  kubectl logs deployment/nginx --all-pods=true
  
  # Return snapshot logs from all containers in pods defined by label app=nginx
  kubectl logs -l app=nginx --all-containers=true
  
  # Return snapshot logs from all pods defined by label app=nginx, limiting concurrent log requests to 10 pods
  kubectl logs -l app=nginx --max-log-requests=10
  
  # Return snapshot of previous terminated ruby container logs from pod web-1
  kubectl logs -p -c ruby web-1
  
  # Begin streaming the logs from pod nginx, continuing even if errors occur
  kubectl logs nginx -f --ignore-errors=true
  
  # Begin streaming the logs of the ruby container in pod web-1
  kubectl logs -f -c ruby web-1
  
  # Begin streaming the logs from all containers in pods defined by label app=nginx
  kubectl logs -f -l app=nginx --all-containers=true
  
  # Display only the most recent 20 lines of output in pod nginx
  kubectl logs --tail=20 nginx
  
  # Show all logs from pod nginx written in the last hour
  kubectl logs --since=1h nginx
  
  # Show all logs with timestamps from pod nginx starting from August 30, 2024, at 06:00:00 UTC
  kubectl logs nginx --since-time=2024-08-30T06:00:00Z --timestamps=true
  
  # Show logs from a kubelet with an expired serving certificate
  kubectl logs --insecure-skip-tls-verify-backend nginx
  
  # Return snapshot logs from first container of a job named hello
  kubectl logs job/hello
  
  # Return snapshot logs from container nginx-1 of a deployment named nginx
  kubectl logs deployment/nginx -c nginx-1
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--all-containers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌های همهٔ کانتینرهای موجود در پاد(ها) را دریافت می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--all-pods</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌ها را از همهٔ پادها دریافت می‌کند. این گزینه مقدار prefix را برابر true قرار می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-c, --container string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>لاگ‌های این کانتینر را چاپ می‌کند</p></td>
</tr>

<tr>
<td colspan="2">-f, --follow</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا لاگ‌ها باید به‌صورت جریانی (stream) ارسال شوند یا نه.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان logs</p></td>
</tr>

<tr>
<td colspan="2">--ignore-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگام پایش یا دنبال‌کردن لاگ‌های پاد، باعث می‌شود هیچ‌یک از خطاهای رخ‌داده مهلک تلقی نشود</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify-backend</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از راستی‌آزمایی هویت kubelet‌ای که لاگ‌ها از آن درخواست می‌شوند صرف‌نظر می‌کند. از نظر تئوری، در این حالت مهاجم می‌تواند محتوای لاگ نامعتبری را بازگرداند. اگر گواهی‌های سرویس‌دهی kubelet شما منقضی شده‌اند، می‌توانید از این گزینه استفاده کنید.</p></td>
</tr>

<tr>
<td colspan="2">--limit-bytes int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد بایت‌های لاگ که بازگردانده می‌شود. به‌طور پیش‌فرض محدودیتی وجود ندارد.</p></td>
</tr>

<tr>
<td colspan="2">--max-log-requests int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد لاگ‌هایی را که هنگام استفاده از انتخابگر (selector) به‌طور هم‌زمان دنبال می‌شوند مشخص می‌کند. مقدار پیش‌فرض 5 است.</p></td>
</tr>

<tr>
<td colspan="2">--pod-running-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 20s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی (مانند 5s، 2m یا 3h و بزرگ‌تر از صفر) که باید منتظر ماند تا دست‌کم یک پاد در حال اجرا باشد</p></td>
</tr>

<tr>
<td colspan="2">--prefix</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منبع لاگ (نام پاد و نام کانتینر) را به ابتدای هر خط لاگ اضافه می‌کند</p></td>
</tr>

<tr>
<td colspan="2">-p, --previous</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، لاگ‌های نمونهٔ قبلی کانتینر در پاد را، در صورت وجود، چاپ می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلترکردن که از عملگرهای '='، '=='، '!='، 'in' و 'notin' پشتیبانی می‌کند (برای نمونه: -l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسبِ مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--since duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فقط لاگ‌هایی را بازمی‌گرداند که از یک مدت نسبی مانند 5s، 2m یا 3h جدیدتر باشند. به‌طور پیش‌فرض همهٔ لاگ‌ها بازگردانده می‌شوند. فقط یکی از گزینه‌های since-time و since را می‌توان به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">--since-time string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فقط لاگ‌های پس از یک تاریخ مشخص (در قالب RFC3339) را بازمی‌گرداند. به‌طور پیش‌فرض همهٔ لاگ‌ها بازگردانده می‌شوند. فقط یکی از گزینه‌های since-time و since را می‌توان به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">--tail int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد خطوط اخیر فایل لاگ که نمایش داده می‌شود. اگر انتخابگری ارائه نشود، مقدار پیش‌فرض ‎-1 است و همهٔ خطوط لاگ نمایش داده می‌شوند؛ در غیر این صورت، یعنی اگر انتخابگری ارائه شود، مقدار پیش‌فرض 10 است.</p></td>
</tr>

<tr>
<td colspan="2">--timestamps</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در خروجی لاگ، مُهر زمانی را در ابتدای هر خط درج می‌کند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که هویت آن برای این عملیات جعل (impersonate) می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که هویت آن برای این عملیات جعل می‌شود. برای تعیین چند گروه می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که هویت آن برای این عملیات جعل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که برای این عملیات جعل می‌شود. برای تعیین چند مقدار برای یک کلید می‌توان این فلگ را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام context‌ای از kubeconfig که باید استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. این کار اتصال‌های HTTPS شما را ناامن می‌کند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در تنظیمات ترجیحی. می‌توان این قابلیت را با export کردن feature gate ‏KUBECTL_KUBERC=false یا خاموش کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، دامنهٔ فضای نام برای این درخواست CLI</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی پراکسی برای درخواست‌ها به سرور API</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید یکای زمانی متناظر داشته باشند (برای نمونه 1s، 2m یا 3h). مقدار صفر یعنی برای درخواست‌ها مهلت زمانی در نظر گرفته نمی‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عملیات نوشتن در درایور ذخیره‌سازی به مدت این بازه بافر می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای (non-memory backends) ثبت می‌شوند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی host:port پایگاه داده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر این مقدار ارائه نشود، نام میزبانی که برای برقراری ارتباط با سرور به کار رفته است استفاده می‌شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ گزینهٔ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تعیین می‌کند</p></td>
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

* [kubectl](../kubectl/)	 - فرمان kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

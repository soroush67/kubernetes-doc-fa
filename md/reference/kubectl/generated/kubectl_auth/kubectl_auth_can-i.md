---
title: kubectl auth can-i
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  بررسی اینکه آیا انجام یک عمل مجاز است یا نه
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


این فرمان بررسی می‌کند که آیا انجام یک عمل مجاز است یا نه.

 پارامتر VERB یک فعل منطقی در API کوبرنتیز است، مانند 'get'، 'list'، 'watch'، 'delete' و موارد مشابه. پارامتر TYPE یک منبع کوبرنتیز است و نام‌های کوتاه (shortcuts) و گروه‌ها به‌طور خودکار به نام کامل تبدیل می‌شوند. پارامتر NONRESOURCEURL یک URL جزئی است که با "/" آغاز می‌شود. پارامتر NAME نام یک منبع مشخص در کوبرنتیز است. این فرمان به‌خوبی همراه با جعل هویت (impersonation) کار می‌کند؛ برای اطلاعات بیشتر، فلگ سراسری --as را ببینید.

```
kubectl auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL]
```

## {{% heading "examples" %}}

```
  # Check to see if I can create pods in any namespace
  kubectl auth can-i create pods --all-namespaces
  
  # Check to see if I can list deployments in my current namespace
  kubectl auth can-i list deployments.apps
  
  # Check to see if service account "foo" of namespace "dev" can list pods in the namespace "prod"
  # You must be allowed to use impersonation for the global option "--as"
  kubectl auth can-i list pods --as=system:serviceaccount:dev:foo -n prod
  
  # Check to see if I can do everything in my current namespace ("*" means all)
  kubectl auth can-i '*' '*'
  
  # Check to see if I can get the job named "bar" in namespace "foo"
  kubectl auth can-i list jobs.batch/bar -n foo
  
  # Check to see if I can read pod logs
  kubectl auth can-i get pods --subresource=log
  
  # Check to see if I can access the URL /logs/
  kubectl auth can-i get /logs/
  
  # Check to see if I can approve certificates.k8s.io
  kubectl auth can-i approve certificates.k8s.io
  
  # List all allowed actions in namespace "foo"
  kubectl auth can-i --list --namespace=foo
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، عمل مشخص‌شده در همهٔ فضاهای نام (namespace) بررسی می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان can-i</p></td>
</tr>

<tr>
<td colspan="2">--list</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، همهٔ عمل‌های مجاز چاپ می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--no-headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، عمل‌های مجاز بدون سرستون‌ها چاپ می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-q, --quiet</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، هیچ خروجی‌ای نمایش داده نمی‌شود و فقط کد خروج برگردانده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--subresource string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>زیرمنبع (subresource)، مانند pod/log یا deployment/scale</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که هویت آن برای انجام این عملیات جعل می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که هویت آن برای انجام این عملیات جعل می‌شود. برای مشخص‌کردن چند گروه می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که هویت آن برای انجام این عملیات جعل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که برای انجام این عملیات جعل می‌شود. برای مشخص‌کردن چند مقدار برای یک کلید واحد می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر پیش‌فرض دایرکتوری کش</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از فایل kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کانتکستی (context) از فایل kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، فشرده‌سازی پاسخ برای همهٔ درخواست‌هایی که به سرور ارسال می‌شوند غیرفعال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، اعتبار گواهی سرور بررسی نمی‌شود. با این کار، اتصال‌های HTTPS شما ناامن می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای ترجیحات کاربر استفاده می‌شود. برای غیرفعال‌کردن آن می‌توانید feature gate مربوط را با export کردن KUBECTL_KUBERC=false تنظیم کنید یا این قابلیت را با KUBERC=off خاموش کنید.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام می‌کند که نسخهٔ سرور با نسخهٔ کلاینت یکسان باشد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی که برای درخواست‌های ارسالی به سرور API استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور، منتظر پاسخ می‌مانیم. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای مثال 1s، 2m، 3h). مقدار صفر به این معناست که درخواست‌ها هیچ‌گاه به پایان مهلت زمانی نمی‌رسند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عملیات نوشتن در درایور ذخیره‌سازی به مدت این بازهٔ زمانی در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در بک‌اندهای غیرحافظه‌ای ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و پورت پایگاه داده به‌صورت host:port</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر این مقدار تعیین نشود، از نام میزبانی استفاده می‌شود که برای برقراری ارتباط با سرور به کار رفته است.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن حامل (bearer token) برای احراز هویت در سرور API</p></td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری از فایل kubeconfig که باید استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فلگ‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و از برنامه خارج می‌شوند؛ فلگ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تنظیم می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر از برنامه خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl auth](../)	 - بررسی مجوزهای دسترسی

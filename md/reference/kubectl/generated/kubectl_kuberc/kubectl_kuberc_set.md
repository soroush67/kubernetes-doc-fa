---
title: kubectl kuberc set
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  تنظیم مقادیر در پیکربندی kuberc
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


این فرمان مقادیر را در فایل پیکربندی kuberc تنظیم می‌کند.

 با فلگ ‎--section مشخص کنید که می‌خواهید مقادیر پیش‌فرض (defaults) را تنظیم کنید یا نام‌های مستعار (aliases) را.

 برای مقادیر پیش‌فرض: این فرمان مقادیر پیش‌فرض فلگ‌ها را برای فرمان‌های kubectl تنظیم می‌کند. فلگ ‎--command باید فقط نام فرمان را مشخص کند (مثلاً "get"، "create"، "set env")، نه منابع را.

 برای نام‌های مستعار: این فرمان نام‌های مستعاری برای فرمان‌ها ایجاد می‌کند که می‌توانند به‌طور اختیاری مقادیر پیش‌فرض فلگ‌ها و آرگومان‌ها را نیز داشته باشند. برای افزودن منابع یا آرگومان‌های دیگر، از ‎--prependarg و ‎--appendarg استفاده کنید.

```
kubectl kuberc set --section (defaults|aliases) --command COMMAND
```

## {{% heading "examples" %}}

```
  # Set default output format for 'get' command
  kubectl kuberc set --section defaults --command get --option output=wide
  
  # Set default output format for a subcommand
  kubectl kuberc set --section defaults --command "set env" --option output=yaml
  
  # Create an alias 'getn' for 'get' command with prepended 'nodes' resource
  kubectl kuberc set --section aliases --name getn --command get --prependarg nodes --option output=wide
  
  # Create an alias 'runx' for 'run' command with appended arguments
  kubectl kuberc set --section aliases --name runx --command run --option image=nginx --appendarg "--" --appendarg custom-arg1
  
  # Overwrite an existing default
  kubectl kuberc set --section defaults --command get --option output=json --overwrite
  
  # Set the credential plugin policy and allowlist
  kubectl kuberc set --section credentialplugin --policy Allowlist --allowlist-entry command=cloud-credential-helper
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allowlist-entry strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک ورودی فهرست مجاز (allowlist) به شکل field=value (می‌توان آن را چند بار مشخص کرد)</p></td>
</tr>

<tr>
<td colspan="2">--appendarg strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آرگومانی که به انتهای فرمان افزوده می‌شود (می‌توان آن را چند بار مشخص کرد؛ فقط برای نام‌های مستعار)</p></td>
</tr>

<tr>
<td colspan="2">--command string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فرمانی که باید پیکربندی شود (مثلاً 'get'، 'create'، 'set env')</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای set</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای ترجیحات استفاده می‌شود. می‌توان این قابلیت را با export کردن feature gate ‏KUBECTL_KUBERC=false یا خاموش کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مستعار (برای ‎--section=aliases الزامی است)</p></td>
</tr>

<tr>
<td colspan="2">--option strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینهٔ فلگ به شکل flag=value (می‌توان آن را چند بار مشخص کرد)</p></td>
</tr>

<tr>
<td colspan="2">--overwrite</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اجازهٔ بازنویسی ورودی‌های موجود را می‌دهد</p></td>
</tr>

<tr>
<td colspan="2">--policy string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سیاست افزونه‌ای که برای افزونه‌های اعتبارنامهٔ exec استفاده می‌شود؛ باید یکی از مقادیر 'AllowAll'، 'DenyAll' یا 'Allowlist' باشد</p></td>
</tr>

<tr>
<td colspan="2">--prependarg strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آرگومانی که به ابتدای فرمان افزوده می‌شود (می‌توان آن را چند بار مشخص کرد؛ فقط برای نام‌های مستعار)</p></td>
</tr>

<tr>
<td colspan="2">--section string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بخشی که باید تغییر کند: 'defaults'، 'aliases' یا 'credentialplugin'</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که عملیات با هویت آن انجام می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات با هویت آن انجام می‌شود. برای مشخص کردن چند گروه می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات با هویت آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که عملیات با هویت آن انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید می‌توان این فلگ را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig که برای درخواست‌های CLI استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام می‌کند که نسخهٔ سرور با نسخهٔ کلاینت یکسان باشد</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، دامنهٔ فضای نام برای این درخواست CLI را مشخص می‌کند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی که برای درخواست‌ها به API server استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست به سرور منتظر می‌ماند. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (مثلاً 1s، 2m، 3h). مقدار صفر به این معناست که درخواست‌ها هیچ‌گاه منقضی نمی‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به این مدت در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در بک‌اندهای غیرحافظه‌ای ثبت می‌شوند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از اتصال امن با پایگاه داده استفاده می‌کند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر مشخص نشود، از نام میزبانی استفاده می‌شود که برای برقراری ارتباط با سرور به کار رفته است</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فلگ‌های ‎--version و ‎--version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ ‎--version=vX.Y.Z...‎ نسخهٔ گزارش‌شده را تنظیم می‌کند</p></td>
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

* [kubectl kuberc](../)	 - مدیریت فایل‌های پیکربندی kuberc

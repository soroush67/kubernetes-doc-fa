---
title: kubectl diff
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  مقایسهٔ نسخهٔ در حال اجرا با نسخه‌ای که در صورت اعمال پدید می‌آید
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


این فرمان پیکربندی‌هایی را که با نام فایل یا از طریق ورودی استاندارد (stdin) مشخص شده‌اند بررسی می‌کند و تفاوت میان پیکربندی فعلی در حال اجرا و پیکربندی‌ای را که در صورت اعمال پدید می‌آید نشان می‌دهد.

 خروجی همیشه با قالب YAML است.

 برای انتخاب فرمان diff دلخواه می‌توانید از متغیر محیطی KUBECTL_EXTERNAL_DIFF استفاده کنید. کاربران می‌توانند فرمان‌های خارجی را همراه با پارامتر نیز به کار ببرند؛ برای نمونه: KUBECTL_EXTERNAL_DIFF="colordiff -N -u"

 به‌طور پیش‌فرض، فرمان «diff» موجود در مسیر (path) شما با گزینه‌های «-u» (نمایش تفاوت به‌صورت یکپارچه) و «-N» (در نظر گرفتن فایل‌های ناموجود به‌عنوان فایل خالی) اجرا می‌شود.

 وضعیت خروج: ۰ یعنی هیچ تفاوتی یافت نشد؛ ۱ یعنی تفاوت‌هایی یافت شد؛ بزرگ‌تر از ۱ یعنی kubectl یا diff با خطا روبه‌رو شده است.

 نکته: اگر از KUBECTL_EXTERNAL_DIFF استفاده می‌کنید، فرمان موردنظر باید از همین قرارداد پیروی کند.

```
kubectl diff -f FILENAME
```

## {{% heading "examples" %}}

```
  # Diff resources included in pod.json
  kubectl diff -f pod.json
  
  # Diff file read from stdin
  cat service.yaml | kubectl diff -f -
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--concurrency int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌هایی که هنگام مقایسه با نسخهٔ در حال اجرا به‌صورت موازی پردازش می‌شوند. عدد بزرگ‌تر سرعت بیشتری دارد، اما در همان بازهٔ زمانی کوتاه‌تر، حافظه، ورودی/خروجی و پردازندهٔ بیشتری مصرف می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--field-manager string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kubectl-client-side-apply"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مدیری که برای پیگیری مالکیت فیلدها به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایل، دایرکتوری یا نشانی URL فایل‌هایی که پیکربندی موردنظر برای مقایسه را در بر دارند</p></td>
</tr>

<tr>
<td colspan="2">--force-conflicts</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعمال سمت سرور (server-side apply) تغییرات را به‌رغم وجود تعارض‌ها به‌اجبار اعمال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای diff</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با -f یا -R به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">--prune</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>منابعی را که با هرس‌کردن (pruning) حذف خواهند شد نیز در نظر می‌گیرد. می‌توان آن را همراه با -l به کار برد و به‌طور پیش‌فرض همهٔ منابعی که هرس خواهند شد نمایش داده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--prune-allowlist strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مجاز پیش‌فرض برای --prune را با &lt;group/version/kind&gt; بازنویسی می‌کند</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری مشخص‌شده در -f, --filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی سودمند است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (selector) یا همان پرس‌وجوی برچسب برای فیلترکردن، که از '=' و '==' و '!=' و 'in' و 'notin' پشتیبانی می‌کند (برای نمونه: -l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسب مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--server-side</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، عملیات apply به‌جای کلاینت در سرور اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--show-managed-fields</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فیلدهای مدیریت‌شده (managed fields) نیز در خروجی مقایسه گنجانده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--show-secrets</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، مقادیر محرمانه در خروجی مقایسه پوشانده نمی‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری‌ای که عملیات به نام آن انجام می‌شود (جعل هویت). این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری پیش‌فرض حافظهٔ نهان (cache)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینه (context) از kubeconfig که باید استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig برای استفاده در درخواست‌های CLI</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در ترجیحات. می‌توان این قابلیت را با export کردن feature gate به‌صورت KUBECTL_KUBERC=false یا خاموش‌کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>الزام به یکسان‌بودن نسخهٔ سرور با نسخهٔ کلاینت</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه در سرور API</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی برای استفاده در درخواست‌ها به سرور API</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای نمونه 1s، 2m، 3h). مقدار صفر یعنی درخواست‌ها هیچ‌گاه به پایان مهلت نمی‌رسند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به این مدت در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای ثبت می‌شوند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور به کار می‌رود. اگر مشخص نشود، نام میزبانی که برای برقراری ارتباط با سرور استفاده شده است به کار می‌رود</p></td>
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

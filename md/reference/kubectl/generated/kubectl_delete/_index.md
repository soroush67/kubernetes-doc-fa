---
title: kubectl delete
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  حذف منابع بر اساس نام فایل‌ها، stdin، منابع و نام‌ها، یا بر اساس منابع و انتخابگر برچسب
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


این دستور منابع را بر اساس نام فایل‌ها، ورودی استاندارد (stdin)، منابع و نام‌ها، یا بر اساس منابع و انتخابگر (selector) برچسب حذف می‌کند.

 هر دو قالب JSON و YAML پذیرفته می‌شوند. فقط یک نوع آرگومان را می‌توان مشخص کرد: نام فایل‌ها، منابع و نام‌ها، یا منابع و انتخابگر برچسب.

 برخی منابع، مانند پادها، از حذف مؤدبانه (graceful deletion) پشتیبانی می‌کنند. این منابع یک بازه‌ی زمانی پیش‌فرض پیش از خاتمه‌ی اجباری تعریف می‌کنند (دوره‌ی مهلت یا grace period)، اما می‌توانید این مقدار را با فلگ ‎--grace-period بازنویسی کنید یا با ارسال ‎--now دوره‌ی مهلت را روی ۱ تنظیم کنید. از آنجا که این منابع اغلب نماینده‌ی موجودیت‌هایی در کلاستر هستند، ممکن است حذف آن‌ها بلافاصله تأیید نشود. اگر نودی که میزبان یک پاد است از کار افتاده باشد یا نتواند به سرور API دسترسی پیدا کند، خاتمه ممکن است به‌مراتب بیشتر از دوره‌ی مهلت طول بکشد. برای حذف اجباری یک منبع، باید فلگ ‎--force را مشخص کنید. توجه: تنها بخشی از منابع از حذف مؤدبانه پشتیبانی می‌کنند. در صورت نبود این پشتیبانی، فلگ ‎--grace-period نادیده گرفته می‌شود.

 مهم: حذف اجباری پادها منتظر تأیید خاتمه‌ی پردازه‌های پاد نمی‌ماند. در نتیجه ممکن است این پردازه‌ها تا زمانی که نود حذف را تشخیص دهد و حذف مؤدبانه را کامل کند، همچنان در حال اجرا بمانند. اگر پردازه‌های شما از ذخیره‌سازی مشترک استفاده می‌کنند یا با یک API راه دور ارتباط دارند و برای شناسایی خود به نام پاد وابسته‌اند، حذف اجباری آن پادها ممکن است باعث شود چند پردازه با شناسه‌ی یکسان روی ماشین‌های مختلف اجرا شوند که می‌تواند به خرابی یا ناسازگاری داده‌ها بینجامد. پادها را فقط زمانی به‌صورت اجباری حذف کنید که مطمئن باشید پاد خاتمه یافته است، یا برنامه‌ی شما بتواند اجرای هم‌زمان چند نسخه از یک پاد را تحمل کند. همچنین اگر پادها را به‌صورت اجباری حذف کنید، ممکن است زمان‌بند پیش از آنکه نود آن منابع را آزاد کند، پادهای جدیدی روی آن نودها قرار دهد و همین امر باعث اخراج (evict) فوری آن پادها شود.

 توجه داشته باشید که دستور delete هیچ بررسی‌ای روی نسخه‌ی منبع انجام نمی‌دهد. بنابراین اگر کسی درست هم‌زمان با ارسال درخواست حذف شما، به‌روزرسانی‌ای برای یک منبع ارسال کند، به‌روزرسانی او همراه با بقیه‌ی منبع از بین می‌رود.

 پس از حذف یک CustomResourceDefinition، بی‌اعتبار شدن حافظه‌ی نهان discovery ممکن است تا ۶ ساعت طول بکشد. اگر نمی‌خواهید منتظر بمانید، می‌توانید دستور "kubectl api-resources" را اجرا کنید تا حافظه‌ی نهان discovery تازه‌سازی شود.

```
kubectl delete ([-f FILENAME] | [-k DIRECTORY] | TYPE [(NAME | -l label | --all)])
```

## {{% heading "examples" %}}

```
  # Delete a pod using the type and name specified in pod.json
  kubectl delete -f ./pod.json
  
  # Delete resources from a directory containing kustomization.yaml - e.g. dir/kustomization.yaml
  kubectl delete -k dir
  
  # Delete resources from all files that end with '.json'
  kubectl delete -f '*.json'
  
  # Delete a pod based on the type and name in the JSON passed into stdin
  cat pod.json | kubectl delete -f -
  
  # Delete pods and services with same names "baz" and "foo"
  kubectl delete pod,service baz foo
  
  # Delete pods and services with label name=myLabel
  kubectl delete pods,services -l name=myLabel
  
  # Delete a pod with minimal delay
  kubectl delete pod foo --now
  
  # Force delete a pod on a dead node
  kubectl delete pod foo --force
  
  # Delete all pods
  kubectl delete pods --all
  
  # Delete all pods only if the user confirms the deletion
  kubectl delete pods --all --interactive
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>همه‌ی منابع از انواع منبع مشخص‌شده را در فضای نام (namespace) حذف می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-A, --all-namespaces</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، آبجکت‌های درخواست‌شده را در همه‌ی فضاهای نام فهرست می‌کند. فضای نامِ context جاری نادیده گرفته می‌شود، حتی اگر با ‎--namespace مشخص شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cascade string[="background"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "background"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار آن باید یکی از &quot;background&quot;، &quot;orphan&quot; یا &quot;foreground&quot; باشد. راهبرد حذف آبشاری را برای وابسته‌ها (برای نمونه، پادهایی که یک ReplicationController ایجاد کرده است) انتخاب می‌کند. مقدار پیش‌فرض background است.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run string[="unchanged"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار آن باید یکی از &quot;none&quot;، &quot;server&quot; یا &quot;client&quot; باشد. در راهبرد client، فقط آبجکتی که قرار است ارسال شود چاپ می‌شود و ارسالی صورت نمی‌گیرد. در راهبرد server، درخواست سمت سرور ارسال می‌شود، بدون آنکه منبع ذخیره شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی فیلد) برای فیلتر کردن که از '='، '==' و '!=' پشتیبانی می‌کند (برای نمونه ‎--field-selector key1=value1,key2=value2). سرور برای هر نوع فقط از تعداد محدودی پرس‌وجوی فیلد پشتیبانی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی که منبعِ مورد نظر برای حذف را در بر دارد.</p></td>
</tr>

<tr>
<td colspan="2">--force</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، منابع بلافاصله از API حذف می‌شوند و حذف مؤدبانه نادیده گرفته می‌شود. توجه داشته باشید که حذف فوری برخی منابع ممکن است به ناسازگاری یا از دست رفتن داده‌ها بینجامد و به تأیید نیاز دارد.</p></td>
</tr>

<tr>
<td colspan="2">--grace-period int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی بر حسب ثانیه که به منبع داده می‌شود تا به‌صورت مؤدبانه خاتمه یابد. مقدار منفی نادیده گرفته می‌شود. برای خاموش شدن فوری، آن را روی ۱ تنظیم کنید. فقط زمانی می‌توان آن را روی ۰ تنظیم کرد که ‎--force برابر true باشد (حذف اجباری).</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور delete</p></td>
</tr>

<tr>
<td colspan="2">--ignore-not-found</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>خطای &quot;resource not found&quot; را به‌عنوان حذف موفق در نظر می‌گیرد. هنگامی که ‎--all مشخص شده باشد، مقدار پیش‌فرض آن &quot;true&quot; است.</p></td>
</tr>

<tr>
<td colspan="2">-i, --interactive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، منبع فقط زمانی حذف می‌شود که کاربر آن را تأیید کند.</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک دایرکتوری kustomization را پردازش می‌کند. این فلگ را نمی‌توان همراه با ‎-f یا ‎-R استفاده کرد.</p></td>
</tr>

<tr>
<td colspan="2">--now</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، به منابع برای خاموش شدن فوری سیگنال داده می‌شود (معادل ‎--grace-period=1).</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حالت خروجی. برای خروجی کوتاه‌تر (resource/name) از &quot;-o name&quot; استفاده کنید.</p></td>
</tr>

<tr>
<td colspan="2">--raw string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URI خامی که درخواست DELETE به آن روی سرور ارسال می‌شود. از transport مشخص‌شده در فایل kubeconfig استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری استفاده‌شده در ‎-f, --filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را که در یک دایرکتوری سازمان‌دهی شده‌اند مدیریت کنید.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلتر کردن که از '='، '=='، '!='، 'in' و 'notin' پشتیبانی می‌کند (برای نمونه ‎-l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همه‌ی قیدهای برچسبِ مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از حذف منتظر می‌ماند. مقدار صفر به این معناست که مهلت زمانی بر اساس اندازه‌ی آبجکت تعیین شود.</p></td>
</tr>

<tr>
<td colspan="2">--wait&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، پیش از بازگشت منتظر می‌ماند تا منابع از بین بروند. این گزینه منتظر finalizerها نیز می‌ماند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که این عملیات به جای آن و با هویت آن انجام می‌شود (جعل هویت یا impersonation). این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که این عملیات با هویت آن انجام می‌شود. برای مشخص کردن چند گروه، می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که این عملیات با هویت آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که این عملیات با هویت آن‌ها انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید واحد، می‌توانید این فلگ را چند بار تکرار کنید.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی مربوط به مرجع صدور گواهی (certificate authority)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از فایل kubeconfig که باید از آن استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کانتکستی (context) از فایل kubeconfig که باید از آن استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن true باشد، اعتبار گواهی سرور بررسی نمی‌شود. در این صورت، اتصال‌های HTTPS شما ناامن خواهند بود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای تنظیم ترجیحات کاربر استفاده می‌شود. می‌توان این قابلیت را با export کردن feature gate به صورت KUBECTL_KUBERC=false یا با خاموش کردن قابلیت به صورت KUBERC=off غیرفعال کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت مشخص شدن، دامنهٔ فضای نام را برای این درخواست خط فرمان تعیین می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. مقدار آن یکی از این گزینه‌هاست: (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL پراکسی که برای ارسال درخواست‌ها به سرور API استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور، منتظر پاسخ می‌مانیم. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای نمونه 1s، 2m یا 3h). مقدار صفر به این معناست که برای درخواست‌ها هیچ مهلت زمانی (timeout) در نظر گرفته نمی‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عملیات نوشتن در درایور ذخیره‌سازی به اندازهٔ این مدت در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در بک‌اندهای غیرحافظه‌ای (non-memory) ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان و درگاه پایگاه داده به صورت host:port</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای اتصال به پایگاه داده از اتصال امن استفاده می‌شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر این مقدار مشخص نشود، از نام میزبانی (hostname) که برای برقراری ارتباط با سرور به کار رفته است استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری از فایل kubeconfig که باید از آن استفاده شود</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های ‎--version و ‎--version=raw اطلاعات نسخه را چاپ می‌کنند و از برنامه خارج می‌شوند؛ گزینهٔ ‎--version=vX.Y.Z...‎ نسخهٔ گزارش‌شده را تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافت‌شده از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر از برنامه خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - ابزار kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

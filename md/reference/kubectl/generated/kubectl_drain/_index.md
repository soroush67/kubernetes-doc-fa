---
title: kubectl drain
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  تخلیهٔ نود برای آماده‌سازی آن جهت نگهداری
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


این فرمان نود را برای آماده‌سازی جهت نگهداری تخلیه (drain) می‌کند.

 نود مشخص‌شده غیرقابل‌زمان‌بندی (unschedulable) علامت‌گذاری می‌شود تا Podهای جدید روی آن قرار نگیرند. اگر سرور API از بیرون‌رانی (eviction) پشتیبانی کند، فرمان 'drain' پادها را بیرون می‌راند (https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ eviction https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ ). در غیر این صورت، برای حذف پادها از درخواست معمولی DELETE استفاده می‌کند. فرمان 'drain' همهٔ پادها را به‌جز mirror podها (که از طریق سرور API قابل حذف نیستند) بیرون می‌راند یا حذف می‌کند. اگر پادهایی وجود داشته باشند که توسط daemon set مدیریت می‌شوند، این فرمان بدون ‎--ignore-daemonsets ادامه نمی‌یابد و در هر حال هیچ‌یک از پادهای مدیریت‌شده با daemon set را حذف نمی‌کند، زیرا کنترل‌کنندهٔ daemon set که علامت‌گذاری غیرقابل‌زمان‌بندی را نادیده می‌گیرد، بلافاصله پادهای دیگری را جایگزین آن‌ها می‌کند. اگر پادهایی وجود داشته باشند که نه mirror pod هستند و نه توسط replication controller، replica set، daemon set، stateful set یا job مدیریت می‌شوند، فرمان drain هیچ پادی را حذف نمی‌کند، مگر آنکه از ‎--force استفاده کنید. همچنین با ‎--force، اگر منبع مدیریت‌کنندهٔ یک یا چند پاد وجود نداشته باشد، عملیات حذف ادامه می‌یابد.

 فرمان 'drain' منتظر خاتمهٔ آرام (graceful termination) پادها می‌ماند. تا پایان اجرای این فرمان نباید هیچ عملیاتی روی ماشین انجام دهید.

 هنگامی که آماده شدید نود را دوباره به چرخهٔ سرویس‌دهی بازگردانید، از kubectl uncordon استفاده کنید تا نود دوباره قابل‌زمان‌بندی شود.

تصویر گردش کار: https://kubernetes.io/images/docs/kubectl_drain.svg Workflowhttps://kubernetes.io/images/docs/kubectl_drain.svg

```
kubectl drain NODE
```

## {{% heading "examples" %}}

```
  # Drain node "foo", even if there are pods not managed by a replication controller, replica set, job, daemon set, or stateful set on it
  kubectl drain foo --force
  
  # As above, but abort if there are pods not managed by a replication controller, replica set, job, daemon set, or stateful set, and use a grace period of 15 minutes
  kubectl drain foo --grace-period=900
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--chunk-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 500</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست‌های بزرگ به‌جای اینکه یکجا برگردانده شوند، در قطعه‌های جداگانه برگردانده می‌شوند. برای غیرفعال‌کردن، مقدار 0 را بدهید.</p></td>
</tr>

<tr>
<td colspan="2">--delete-emptydir-data</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حتی اگر پادهایی از emptyDir (داده‌های محلی که هنگام تخلیهٔ نود حذف می‌شوند) استفاده کنند، عملیات ادامه می‌یابد.</p></td>
</tr>

<tr>
<td colspan="2">--disable-eviction</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فرمان drain را وادار می‌کند حتی در صورت پشتیبانی از بیرون‌رانی، از حذف استفاده کند. با این کار بررسی PodDisruptionBudgetها دور زده می‌شود؛ بنابراین با احتیاط از آن استفاده کنید.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run string[="unchanged"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار آن باید یکی از &quot;none&quot;، &quot;server&quot; یا &quot;client&quot; باشد. در راهبرد client، آبجکتی که قرار است ارسال شود فقط چاپ می‌شود و ارسال نمی‌شود. در راهبرد server، درخواست سمت سرور ارسال می‌شود، بی‌آنکه منبع ذخیره شود.</p></td>
</tr>

<tr>
<td colspan="2">--force</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حتی اگر پادهایی وجود داشته باشند که کنترل‌کننده‌ای برایشان اعلام نشده است، عملیات ادامه می‌یابد.</p></td>
</tr>

<tr>
<td colspan="2">--grace-period int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: -1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی بر حسب ثانیه که به هر پاد برای خاتمهٔ آرام داده می‌شود. اگر منفی باشد، مقدار پیش‌فرض تعیین‌شده در پاد استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان drain</p></td>
</tr>

<tr>
<td colspan="2">--ignore-daemonsets</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پادهای مدیریت‌شده با DaemonSet نادیده گرفته می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--pod-selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر برچسب برای فیلترکردن پادهای روی نود</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (پرس‌وجوی برچسب) برای فیلترکردن؛ از عملگرهای '=' و '==' و '!=' و 'in' و 'notin' پشتیبانی می‌کند (برای مثال ‎-l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسب مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--skip-wait-for-delete-timeout int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار DeletionTimestamp پاد قدیمی‌تر از N ثانیه باشد، از انتظار برای آن پاد صرف‌نظر می‌شود. برای صرف‌نظر کردن، تعداد ثانیه‌ها باید بزرگ‌تر از 0 باشد.</p></td>
</tr>

<tr>
<td colspan="2">--timeout duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از توقف تلاش؛ مقدار صفر به معنای انتظار نامحدود است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات با هویت آن انجام می‌شود. برای مشخص‌کردن چند گروه، می‌توان این فلگ را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات تکمیلی کاربر که عملیات با هویت آن انجام می‌شود. برای مشخص‌کردن چند مقدار برای یک کلید، می‌توان این فلگ را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "$HOME/.kube/cache"</td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستر موردنظر در kubeconfig</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام context موردنظر در kubeconfig</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. با این کار اتصال‌های HTTPS شما ناامن می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای تنظیم ترجیحات. می‌توان این قابلیت را با export کردن feature gate ‏KUBECTL_KUBERC=false یا خاموش‌کردن قابلیت با KUBERC=off غیرفعال کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه در سرور API</p></td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود؛ یکی از مقادیر (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
</tr>

<tr>
<td colspan="2">--profile-output string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "profile.pprof"</td>
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
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از رها کردن یک درخواست منفرد به سرور. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (برای مثال 1s، 2m، 3h). مقدار صفر یعنی برای درخواست‌ها مهلت زمانی تعیین نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و پورت سرور API کوبرنتیز</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به این مدت در بافر نگه داشته می‌شوند و سپس به‌صورت یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای ثبت می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-db string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "cadvisor"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-host string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "localhost:8086"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی host:port پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "root"</td>
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
<td colspan="2">--storage-driver-table string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "stats"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام جدول</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-user string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--tls-server-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سرور برای اعتبارسنجی گواهی سرور. اگر تعیین نشود، از نام میزبانی که برای برقراری ارتباط با سرور به کار رفته است استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربر موردنظر در kubeconfig</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های ‎--version و ‎--version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ گزینهٔ ‎--version=vX.Y.Z...‎ نسخهٔ گزارش‌شده را تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور به‌عنوان خطا در نظر گرفته می‌شوند و برنامه با کد خروج غیرصفر خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - فرمان kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

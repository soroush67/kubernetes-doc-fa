---
title: kubectl set env
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  به‌روزرسانی متغیرهای محیطی در یک قالب پاد
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


این دستور متغیرهای محیطی را در یک قالب پاد (pod template) به‌روزرسانی می‌کند.

 این دستور تعریف‌های متغیرهای محیطی را در یک یا چند پاد یا قالب پاد فهرست می‌کند. همچنین تعریف‌های متغیرهای محیطی کانتینر را در یک یا چند قالب پاد (درون replication controllerها یا پیکربندی‌های استقرار) اضافه، به‌روزرسانی یا حذف می‌کند. با این دستور می‌توانید تعریف‌های متغیرهای محیطی همهٔ کانتینرهای پادها یا قالب‌های پاد مشخص‌شده را مشاهده یا تغییر دهید، یا این کار را فقط برای کانتینرهایی انجام دهید که با یک الگوی عام (wildcard) مطابقت دارند.

 اگر "--env -" داده شود، متغیرهای محیطی را می‌توان با نحو استاندارد env از STDIN خواند.

 منابع ممکن عبارت‌اند از (بدون حساسیت به بزرگی و کوچکی حروف):

        pod (po), replicationcontroller (rc), deployment (deploy), daemonset (ds), statefulset (sts), cronjob (cj), replicaset (rs)

```
kubectl set env RESOURCE/NAME KEY_1=VAL_1 ... KEY_N=VAL_N
```

## {{% heading "examples" %}}

```
  # Update deployment 'registry' with a new environment variable
  kubectl set env deployment/registry STORAGE_DIR=/local
  
  # List the environment variables defined on a deployments 'sample-build'
  kubectl set env deployment/sample-build --list
  
  # List the environment variables defined on all pods
  kubectl set env pods --all --list
  
  # Output modified deployment in YAML, and does not alter the object on the server
  kubectl set env deployment/sample-build STORAGE_DIR=/data -o yaml
  
  # Update all containers in all replication controllers in the project to have ENV=prod
  kubectl set env rc --all ENV=prod
  
  # Import environment from a secret
  kubectl set env --from=secret/mysecret deployment/myapp
  
  # Import environment from a config map with a prefix
  kubectl set env --from=configmap/myconfigmap --prefix=MYSQL_ deployment/myapp
  
  # Import specific keys from a config map
  kubectl set env --keys=my-example-key --from=configmap/myconfigmap deployment/myapp
  
  # Remove the environment variable ENV from container 'c1' in all deployment configs
  kubectl set env deployments --all --containers="c1" ENV-
  
  # Remove the environment variable ENV from a deployment definition on disk and
  # update the deployment config on the server
  kubectl set env -f deploy.json ENV-
  
  # Set some of the local shell environment into a deployment config on the server
  env | grep RAILS_ | kubectl set env -e - deployment/registry
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، همهٔ منابعِ انواع منبع مشخص‌شده در فضای نام انتخاب می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--allow-missing-template-keys&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگامی که یک فیلد یا کلید نگاشت (map) در قالب وجود نداشته باشد، از خطاهای قالب صرف‌نظر می‌شود. این گزینه فقط برای قالب‌های خروجی golang و jsonpath اعمال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-c, --containers string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "*"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کانتینرهایی از قالب‌های پاد انتخاب‌شده که باید تغییر کنند؛ می‌توان از نویسه‌های عام (wildcard) استفاده کرد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run string[="unchanged"]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار آن باید یکی از &quot;none&quot;، &quot;server&quot; یا &quot;client&quot; باشد. در راهبرد client، فقط آبجکتی که قرار است ارسال شود چاپ می‌شود و ارسالی صورت نمی‌گیرد. در راهبرد server، درخواست سمت سرور ارسال می‌شود، اما منبع ذخیره نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-e, --env strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک جفت کلید-مقدار برای متغیر محیطی‌ای مشخص می‌کند که باید در هر کانتینر تنظیم شود.</p></td>
</tr>

<tr>
<td colspan="2">--field-manager string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kubectl-set"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مدیری که برای ردیابی مالکیت فیلدها به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">-f, --filename strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایل، دایرکتوری یا URL فایل‌های منبعی که متغیرهای محیطی آن باید به‌روزرسانی شوند.</p></td>
</tr>

<tr>
<td colspan="2">--from string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام منبعی که متغیرهای محیطی از آن تزریق می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای env</p></td>
</tr>

<tr>
<td colspan="2">--keys strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از کلیدها، جداشده با ویرگول، که باید از منبع مشخص‌شده وارد شوند.</p></td>
</tr>

<tr>
<td colspan="2">-k, --kustomize string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری kustomization را پردازش می‌کند. این پرچم را نمی‌توان همراه با -f یا -R به کار برد.</p></td>
</tr>

<tr>
<td colspan="2">--list</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، متغیرهای محیطی و هرگونه تغییر در آن‌ها با قالب استاندارد نمایش داده می‌شوند. این پرچم پس از افزوده شدن دستور kubectl view env حذف خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--local</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، دستور set env با api-server ارتباط برقرار نمی‌کند و به‌صورت محلی اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب خروجی، که یکی از این مقادیر است: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).</p></td>
</tr>

<tr>
<td colspan="2">--overwrite&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، بازنویسی متغیرهای محیطی مجاز است؛ در غیر این صورت، به‌روزرسانی‌هایی که متغیرهای محیطی موجود را بازنویسی می‌کنند رد می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--prefix string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پیشوندی که به نام متغیرها افزوده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-R, --recursive</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری تعیین‌شده در -f, --filename را به‌صورت بازگشتی پردازش می‌کند. این گزینه زمانی مفید است که بخواهید مانیفست‌های مرتبطی را مدیریت کنید که در یک دایرکتوری سازمان‌دهی شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--resolve</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام فهرست کردن متغیرها، ارجاع‌های secret یا configmap نمایش داده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">-l, --selector string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>انتخابگر (selector)، یعنی پرس‌وجوی برچسب، برای فیلتر کردن؛ از '='، '=='، '!='، 'in' و 'notin' پشتیبانی می‌کند (مثلاً -l key1=value1,key2=value2,key3 in (value3)). آبجکت‌های منطبق باید همهٔ محدودیت‌های برچسب مشخص‌شده را برآورده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--show-managed-fields</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام چاپ آبجکت‌ها با قالب JSON یا YAML، فیلد managedFields حفظ می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--template string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رشتهٔ قالب یا مسیر فایل قالب که هنگام تعیین -o=go-template یا -o=go-template-file به کار می‌رود. قالب‌ها از نوع قالب‌های golang هستند [http://golang.org/pkg/text/template/#pkg-overview].</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که این عملیات با جعل هویت (impersonation) آن انجام می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که این عملیات با جعل هویت آن انجام می‌شود؛ برای تعیین چند گروه می‌توان این پرچم را تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که این عملیات با جعل هویت آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات اضافی کاربر که این عملیات با جعل هویت آن انجام می‌شود؛ برای تعیین چند مقدار برای یک کلید می‌توان این پرچم را تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc برای استفاده در تنظیمات ترجیحی. می‌توان این قابلیت را با export کردن feature gate به‌صورت KUBECTL_KUBERC=false یا با خاموش کردن قابلیت به‌صورت KUBERC=off غیرفعال کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، محدودهٔ فضای نام برای این درخواست CLI</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود؛ یکی از مقادیر (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (مثلاً 1s، 2m، 3h). مقدار صفر به این معناست که برای درخواست‌ها مهلت زمانی (timeout) در نظر گرفته نمی‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عملیات نوشتن در درایور ذخیره‌سازی به مدت این بازه بافر می‌شوند و سپس به‌صورت یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای (non-memory backends) ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور به کار می‌رود. اگر این مقدار ارائه نشود، از نام میزبانی (hostname) استفاده می‌شود که برای ارتباط با سرور به کار رفته است.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن حامل (Bearer token) برای احراز هویت در سرور API</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ گزینهٔ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تنظیم می‌کند.</p></td>
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

* [kubectl set](../)	 - تنظیم ویژگی‌های مشخص روی آبجکت‌ها

---
title: kubectl
content_type: tool-reference
weight: 30
---

## {{% heading "synopsis" %}}

{{< glossary_definition term_id="kubectl" length="short" >}}

اطلاعات بیشتر را در [ابزار خط فرمان](/docs/reference/kubectl/) (`kubectl`) بیابید.

```shell
kubectl [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--add-dir-header</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر true باشد، دایرکتوری فایل به سرآیند پیام‌های لاگ اضافه می‌شود</td>
</tr>

<tr>
<td colspan="2">--alsologtostderr</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">لاگ‌ها علاوه بر فایل‌ها در خروجی خطای استاندارد نیز نوشته می‌شوند</td>
</tr>

<tr>
<td colspan="2">--as string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام کاربری که عملیات با جعل هویت (impersonation) آن انجام می‌شود</td>
</tr>

<tr>
<td colspan="2">--as-group stringArray</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">گروهی که عملیات با جعل هویت آن انجام می‌شود؛ برای مشخص کردن چند گروه می‌توان این فلگ را تکرار کرد.</td>
</tr>

<tr>
<td colspan="2">--azure-container-registry-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایلی که اطلاعات پیکربندی رجیستری کانتینر Azure را در خود دارد.</td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">دایرکتوری پیش‌فرض کش</td>
</tr>

<tr>
<td colspan="2">--certificate-authority string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایل گواهی مرجع صدور گواهی (certificate authority)</td>
</tr>

<tr>
<td colspan="2">--client-certificate string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایل گواهی کلاینت برای TLS</td>
</tr>

<tr>
<td colspan="2">--client-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایل کلید کلاینت برای TLS</td>
</tr>

<tr>
<td colspan="2">--cloud-provider-gce-l7lb-src-cidrs cidrs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 130.211.0.0/22,35.191.0.0/16</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">محدوده‌های CIDR که در فایروال GCE برای پراکسی ترافیک متعادل‌کنندهٔ بار لایهٔ ۷ (L7 LB) و بررسی‌های سلامت باز شده‌اند</td>
</tr>

<tr>
<td colspan="2">--cloud-provider-gce-lb-src-cidrs cidrs&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 130.211.0.0/22,209.85.152.0/22,209.85.204.0/22,35.191.0.0/16</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">محدوده‌های CIDR که در فایروال GCE برای پراکسی ترافیک متعادل‌کنندهٔ بار لایهٔ ۴ (L4 LB) و بررسی‌های سلامت باز شده‌اند</td>
</tr>

<tr>
<td colspan="2">--cluster string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام کلاستری از kubeconfig که باید استفاده شود</td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام زمینه‌ای (context) از kubeconfig که باید استفاده شود</td>
</tr>

<tr>
<td colspan="2">--default-not-ready-toleration-seconds int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 300</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مقدار tolerationSeconds را برای toleration مربوط به notReady:NoExecute مشخص می‌کند؛ این toleration به‌طور پیش‌فرض به هر پادی که از قبل چنین tolerationای نداشته باشد اضافه می‌شود.</td>
</tr>

<tr>
<td colspan="2">--default-unreachable-toleration-seconds int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 300</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مقدار tolerationSeconds را برای toleration مربوط به unreachable:NoExecute مشخص می‌کند؛ این toleration به‌طور پیش‌فرض به هر پادی که از قبل چنین tolerationای نداشته باشد اضافه می‌شود.</td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">راهنمای kubectl</td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر true باشد، اعتبار گواهی سرور بررسی نمی‌شود. با این کار، اتصال‌های HTTPS شما ناامن می‌شوند</td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایل kubeconfig برای استفاده در درخواست‌های CLI.</td>
</tr>

<tr>
<td colspan="2">--log-backtrace-at traceLocation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: :0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">هنگامی که لاگ‌گیری به خط file:N برسد، یک ردپای پشته (stack trace) چاپ می‌شود</td>
</tr>

<tr>
<td colspan="2">--log-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر خالی نباشد، فایل‌های لاگ در این دایرکتوری نوشته می‌شوند</td>
</tr>

<tr>
<td colspan="2">--log-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر خالی نباشد، از این فایل لاگ استفاده می‌شود</td>
</tr>

<tr>
<td colspan="2">--log-file-max-size uint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 1800</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">حداکثر اندازه‌ای را که یک فایل لاگ می‌تواند به آن برسد تعیین می‌کند. واحد آن مگابایت است. اگر مقدار آن 0 باشد، حداکثر اندازهٔ فایل نامحدود است.</td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">حداکثر فاصلهٔ زمانی بر حسب ثانیه میان دو بار تخلیهٔ (flush) لاگ‌ها</td>
</tr>

<tr>
<td colspan="2">--logtostderr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">لاگ‌ها به‌جای فایل‌ها در خروجی خطای استاندارد نوشته می‌شوند</td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">الزام می‌کند که نسخهٔ سرور با نسخهٔ کلاینت یکسان باشد</td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">در صورت تعیین، دامنهٔ فضای نام (namespace) این درخواست CLI را مشخص می‌کند</td>
</tr>

<tr>
<td colspan="2">--one-output</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر true باشد، لاگ‌ها فقط در سطح شدت اصلی خودشان نوشته می‌شوند (به‌جای اینکه در همهٔ سطوح شدت پایین‌تر نیز نوشته شوند)</td>
</tr>

<tr>
<td colspan="2">--password string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">گذرواژه برای احراز هویت پایه (basic authentication) در سرور API</td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام پروفایلی که باید ثبت شود. یکی از مقادیر (none|cpu|heap|goroutine|threadcreate|block|mutex)</td>
</tr>

<tr>
<td colspan="2">--profile-output string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "profile.pprof"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام فایلی که پروفایل در آن نوشته می‌شود</td>
</tr>

<tr>
<td colspan="2">--request-timeout string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "0"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور باید منتظر ماند. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (مثلاً 1s، 2m، 3h). مقدار صفر به این معناست که درخواست‌ها هیچ‌گاه به مهلت زمانی نمی‌رسند.</td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نشانی و پورت سرور API کوبرنتیز</td>
</tr>

<tr>
<td colspan="2">--skip-headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر true باشد، پیشوندهای سرآیند در پیام‌های لاگ نوشته نمی‌شوند</td>
</tr>

<tr>
<td colspan="2">--skip-log-headers</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر true باشد، هنگام باز کردن فایل‌های لاگ سرآیندی نوشته نمی‌شود</td>
</tr>

<tr>
<td colspan="2">--stderrthreshold severity&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 2</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">لاگ‌هایی که در این آستانه یا بالاتر از آن باشند به stderr فرستاده می‌شوند</td>
</tr>

<tr>
<td colspan="2">--tls-server-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام سروری که برای اعتبارسنجی گواهی سرور به کار می‌رود. اگر تعیین نشود، از نام میزبانی استفاده می‌شود که برای برقراری ارتباط با سرور به کار رفته است</td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">توکن حامل (Bearer) برای احراز هویت در سرور API</td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام کاربری از kubeconfig که باید استفاده شود</td>
</tr>

<tr>
<td colspan="2">--username string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">نام کاربری برای احراز هویت پایه در سرور API</td>
</tr>

<tr>
<td colspan="2">-v, --v Level</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">عدد سطح جزئیات (verbosity) لاگ</td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اطلاعات نسخه را چاپ می‌کند و خارج می‌شود</td>
</tr>

<tr>
<td colspan="2">--vmodule moduleSpec</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">فهرستی از تنظیمات pattern=N، جداشده با کاما، برای لاگ‌گیری فیلترشده بر اساس فایل</td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">هشدارهای دریافت‌شده از سرور را خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود</td>
</tr>

</tbody>
</table>

## {{% heading "envvars" %}}

<table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">KUBECONFIG</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">مسیر فایل پیکربندی kubectl ("kubeconfig"). پیش‌فرض: "$HOME/.kube/config"</td>
</tr>

<tr>
<td colspan="2">KUBECTL_EXPLAIN_OPENAPIV3</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">تعیین می‌کند که فراخوانی‌های `kubectl explain` از منبع دادهٔ جدید و در دسترس OpenAPIv3 استفاده کنند یا نه. از کوبرنتیز 1.24 به بعد، OpenAPIV3 به‌طور پیش‌فرض فعال است.
</td>
</tr>

<tr>
<td colspan="2">KUBECTL_ENABLE_CMD_SHADOW</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر روی true تنظیم شود، در صورتی که زیرفرمانی وجود نداشته باشد، می‌توان از افزونه‌های خارجی به‌عنوان زیرفرمانِ فرمان‌های داخلی استفاده کرد. در مرحلهٔ آلفا، این قابلیت فقط برای فرمان create قابل استفاده است (برای نمونه kubectl create networkpolicy).
</td>
</tr>

<tr>
<td colspan="2">KUBECTL_PORT_FORWARD_WEBSOCKETS</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر روی true تنظیم شود، فرمان kubectl port-forward تلاش می‌کند جریان داده را با پروتکل websockets منتقل کند. اگر ارتقا به websockets ناموفق باشد، فرمان‌ها به استفاده از پروتکل فعلی SPDY بازمی‌گردند.
</td>
</tr>

<tr>
<td colspan="2">KUBECTL_REMOTE_COMMAND_WEBSOCKETS</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر روی true تنظیم شود، فرمان‌های kubectl exec، cp و attach تلاش می‌کنند جریان داده را با پروتکل websockets منتقل کنند. اگر ارتقا به websockets ناموفق باشد، فرمان‌ها به استفاده از پروتکل فعلی SPDY بازمی‌گردند.
</td>
</tr>

<tr>
<td colspan="2">KUBECTL_KUBERC</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;">اگر روی true تنظیم شود، فایل kuberc برای تعریف ترجیحات مختص هر کاربر در نظر گرفته می‌شود.
</td>
</tr>

</tbody>
</table>

## {{% heading "seealso" %}}

* [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/) - به‌روزرسانی حاشیه‌نویسی‌های (annotation) یک منبع
* [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/) - چاپ منابع API پشتیبانی‌شده روی سرور
* [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/) - چاپ نسخه‌های API پشتیبانی‌شده روی سرور،
  به شکل "group/version"
* [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/) - اعمال یک پیکربندی بر یک منبع با استفاده از نام فایل یا stdin
* [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/) - اتصال به یک کانتینر در حال اجرا
* [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/) - بررسی مجوزدهی
* [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/) - مقیاس‌دهی خودکار یک Deployment، ReplicaSet یا ReplicationController
* [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/) - تغییر منابع گواهی.
* [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/) - نمایش اطلاعات کلاستر
* [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/) - تولید کد تکمیل خودکار پوسته برای پوستهٔ مشخص‌شده (bash یا zsh)
* [kubectl config](/docs/reference/kubectl/generated/kubectl_config/) - تغییر فایل‌های kubeconfig
* [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/) - علامت‌گذاری نود به‌عنوان غیرقابل زمان‌بندی
* [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/) - کپی فایل‌ها و دایرکتوری‌ها به کانتینرها و از آن‌ها.
* [kubectl create](/docs/reference/kubectl/generated/kubectl_create/) - ایجاد یک منبع از فایل یا از stdin.
* [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/) - ایجاد نشست‌های اشکال‌زدایی برای عیب‌یابی بارهای کاری و نودها
* [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/) - حذف منابع بر اساس نام فایل‌ها،
  stdin، منابع و نام‌ها، یا منابع و انتخابگر (selector) برچسب
* [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/) - نمایش جزئیات یک منبع مشخص یا گروهی از منابع
* [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/) - مقایسهٔ نسخهٔ فعلی با نسخه‌ای که اعمال خواهد شد
* [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/) - تخلیهٔ نود برای آماده‌سازی جهت نگهداری
* [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/) - ویرایش یک منبع روی سرور
* [kubectl events](/docs/reference/kubectl/generated/kubectl_events/)  - فهرست کردن رویدادها
* [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/) - اجرای یک فرمان در یک کانتینر
* [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/) - مستندات منابع
* [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/) - گرفتن یک replication controller،
  service، deployment یا pod و ارائهٔ آن به‌صورت یک Service جدید کوبرنتیز
* [kubectl get](/docs/reference/kubectl/generated/kubectl_get/) - نمایش یک یا چند منبع
* [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/) - ساخت یک هدف kustomization
  از یک دایرکتوری یا یک URL راه دور.
* [kubectl label](/docs/reference/kubectl/generated/kubectl_label/) - به‌روزرسانی برچسب‌های یک منبع
* [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/) - چاپ لاگ‌های یک کانتینر در یک پاد
* [kubectl options](/docs/reference/kubectl/generated/kubectl_options/) - چاپ فهرست فلگ‌هایی که همهٔ فرمان‌ها به ارث می‌برند
* [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/) - به‌روزرسانی فیلد(های) یک منبع
* [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/) - ابزارهایی برای تعامل با افزونه‌ها فراهم می‌کند.
* [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/) - هدایت یک یا چند پورت محلی به یک پاد
* [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/) - اجرای یک پراکسی به سرور API کوبرنتیز
* [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/) - جایگزینی یک منبع با استفاده از نام فایل یا stdin
* [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/) - مدیریت انتشار (rollout) یک منبع
* [kubectl run](/docs/reference/kubectl/generated/kubectl_run/) - اجرای یک ایمیج مشخص روی کلاستر
* [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/) - تعیین اندازهٔ جدید برای یک Deployment، ReplicaSet یا Replication Controller
* [kubectl set](/docs/reference/kubectl/generated/kubectl_set/) - تنظیم ویژگی‌های مشخص روی آبجکت‌ها
* [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/) - به‌روزرسانی taintهای یک یا چند نود
* [kubectl top](/docs/reference/kubectl/generated/kubectl_top/) - نمایش میزان مصرف منابع (CPU/حافظه/ذخیره‌سازی).
* [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/) - علامت‌گذاری نود به‌عنوان قابل زمان‌بندی
* [kubectl version](/docs/reference/kubectl/generated/kubectl_version/) - چاپ اطلاعات نسخهٔ کلاینت و سرور
* [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/) - آزمایشی: انتظار برای برقراری یک وضعیت مشخص روی یک یا چند منبع.

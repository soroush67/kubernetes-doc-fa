---
title: kubectl
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند
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


kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند.

 اطلاعات بیشتر را در این نشانی بیابید: https://kubernetes.io/docs/reference/kubectl/

```
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
<td colspan="2">--as string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که برای انجام عملیات جعل هویت (impersonate) می‌شود. کاربر می‌تواند یک کاربر معمولی یا یک service account در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که برای انجام عملیات جعل هویت می‌شود؛ برای مشخص کردن چند گروه می‌توان این فلگ را چندین بار تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>UID که برای انجام عملیات جعل هویت می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات اضافی کاربر که برای انجام عملیات جعل هویت می‌شود؛ برای مشخص کردن چند مقدار برای یک کلید یکسان می‌توان این فلگ را چندین بار تکرار کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستر kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام context در kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فشرده‌سازی پاسخ برای همه درخواست‌ها به سرور غیرفعال می‌شود</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kubectl</p></td>
</tr>

<tr>
<td colspan="2">--insecure-skip-tls-verify</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، اعتبار گواهی سرور بررسی نخواهد شد. این کار اتصالات HTTPS شما را ناامن می‌کند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای تنظیمات ترجیحی استفاده می‌شود. این قابلیت را می‌توان با صادرکردن feature gate با مقدار KUBECTL_KUBERC=false یا با خاموش کردن قابلیت از طریق KUBERC=off غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--match-server-version</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مطابقت نسخه سرور با نسخه کلاینت را الزامی می‌کند</p></td>
</tr>

<tr>
<td colspan="2">-n, --namespace string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت وجود، محدوده فضای نام (namespace) را برای این درخواست CLI مشخص می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--password string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه برای احراز هویت پایه (basic authentication) به API server</p></td>
</tr>

<tr>
<td colspan="2">--profile string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور. مقادیر غیرصفر باید شامل یک واحد زمانی متناظر باشند (برای مثال 1s، 2m، 3h). مقدار صفر به معنای عدم اعمال محدودیت زمانی برای درخواست‌هاست.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به‌مدت این بازه زمانی بافر می‌شوند و به‌صورت یک تراکنش واحد در بک‌اندهای غیرحافظه‌ای ثبت می‌گردند</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>میزبان:درگاه پایگاه داده</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژه پایگاه داده</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر ارائه نشود، از نام میزبانی که برای برقراری ارتباط با سرور استفاده شده است، استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن Bearer برای احراز هویت به API server</p></td>
</tr>

<tr>
<td colspan="2">--user string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربر kubeconfig که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--username string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری برای احراز هویت پایه (basic authentication) به API server</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ کرده و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافتی از سرور را به‌عنوان خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl annotate](../kubectl_annotate/)	 - به‌روزرسانی حاشیه‌نویسی‌ها (annotations) روی یک منبع
* [kubectl api-resources](../kubectl_api-resources/)	 - چاپ منابع API پشتیبانی‌شده روی سرور
* [kubectl api-versions](../kubectl_api-versions/)	 - چاپ نسخه‌های API پشتیبانی‌شده روی سرور، به‌صورت «group/version»
* [kubectl apply](../kubectl_apply/)	 - اعمال یک پیکربندی بر یک منبع بر اساس نام فایل یا stdin
* [kubectl attach](../kubectl_attach/)	 - اتصال به یک کانتینر در حال اجرا
* [kubectl auth](../kubectl_auth/)	 - بررسی مجوزدهی (authorization)
* [kubectl autoscale](../kubectl_autoscale/)	 - مقیاس‌دهی خودکار یک Deployment، ReplicaSet، StatefulSet یا ReplicationController
* [kubectl certificate](../kubectl_certificate/)	 - تغییر منابع گواهی
* [kubectl cluster-info](../kubectl_cluster-info/)	 - نمایش اطلاعات کلاستر
* [kubectl completion](../kubectl_completion/)	 - تولید کد تکمیل خودکار شل برای شل مشخص‌شده (bash، zsh، fish یا powershell)
* [kubectl config](../kubectl_config/)	 - تغییر فایل‌های kubeconfig
* [kubectl cordon](../kubectl_cordon/)	 - علامت‌گذاری نود به‌عنوان غیرقابل زمان‌بندی
* [kubectl cp](../kubectl_cp/)	 - کپی فایل‌ها و دایرکتوری‌ها به کانتینرها و از آن‌ها
* [kubectl create](../kubectl_create/)	 - ایجاد یک منبع از یک فایل یا از stdin
* [kubectl debug](../kubectl_debug/)	 - ایجاد نشست‌های اشکال‌زدایی برای عیب‌یابی بارهای کاری و نودها
* [kubectl delete](../kubectl_delete/)	 - حذف منابع بر اساس نام فایل، stdin، منابع و نام‌ها، یا منابع و انتخابگر برچسب (label selector)
* [kubectl describe](../kubectl_describe/)	 - نمایش جزئیات یک منبع مشخص یا گروهی از منابع
* [kubectl diff](../kubectl_diff/)	 - مقایسه نسخه فعال با نسخه‌ای که قرار است اعمال شود
* [kubectl drain](../kubectl_drain/)	 - تخلیه نود در آماده‌سازی برای نگهداری
* [kubectl edit](../kubectl_edit/)	 - ویرایش یک منبع روی سرور
* [kubectl events](../kubectl_events/)	 - فهرست رویدادها
* [kubectl exec](../kubectl_exec/)	 - اجرای یک دستور در یک کانتینر
* [kubectl explain](../kubectl_explain/)	 - دریافت مستندات یک منبع
* [kubectl expose](../kubectl_expose/)	 - دریافت یک ReplicationController، Service، Deployment یا Pod و در دسترس قرار دادن آن به‌عنوان یک Service جدید کوبرنتیز
* [kubectl get](../kubectl_get/)	 - نمایش یک یا چند منبع
* [kubectl kuberc](../kubectl_kuberc/)	 - مدیریت فایل‌های پیکربندی kuberc
* [kubectl kustomize](../kubectl_kustomize/)	 - ساخت یک هدف kustomization از یک دایرکتوری یا URL
* [kubectl label](../kubectl_label/)	 - به‌روزرسانی برچسب‌ها (labels) روی یک منبع
* [kubectl logs](../kubectl_logs/)	 - چاپ لاگ‌های یک کانتینر در یک Pod
* [kubectl options](../kubectl_options/)	 - چاپ فهرست فلگ‌هایی که همه دستورها به ارث می‌برند
* [kubectl patch](../kubectl_patch/)	 - به‌روزرسانی فیلدهای یک منبع
* [kubectl plugin](../kubectl_plugin/)	 - ارائه ابزارهایی برای تعامل با افزونه‌ها (plugins)
* [kubectl port-forward](../kubectl_port-forward/)	 - هدایت یک یا چند درگاه محلی به یک Pod
* [kubectl proxy](../kubectl_proxy/)	 - اجرای یک پراکسی به API server کوبرنتیز
* [kubectl replace](../kubectl_replace/)	 - جایگزینی یک منبع بر اساس نام فایل یا stdin
* [kubectl rollout](../kubectl_rollout/)	 - مدیریت رول‌اوت (rollout) یک منبع
* [kubectl run](../kubectl_run/)	 - اجرای یک ایمیج مشخص روی کلاستر
* [kubectl scale](../kubectl_scale/)	 - تنظیم اندازه جدید برای یک Deployment، ReplicaSet یا ReplicationController
* [kubectl set](../kubectl_set/)	 - تنظیم ویژگی‌های مشخص روی آبجکت‌ها
* [kubectl taint](../kubectl_taint/)	 - به‌روزرسانی taintها روی یک یا چند نود
* [kubectl top](../kubectl_top/)	 - نمایش میزان مصرف منابع (CPU/حافظه)
* [kubectl uncordon](../kubectl_uncordon/)	 - علامت‌گذاری نود به‌عنوان قابل زمان‌بندی
* [kubectl version](../kubectl_version/)	 - چاپ اطلاعات نسخه کلاینت و سرور
* [kubectl wait](../kubectl_wait/)	 - انتظار برای یک شرط مشخص روی یک یا چند منبع

---
title: kubectl kustomize
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  ساختن یک هدف kustomization از یک دایرکتوری یا URL
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


این دستور مجموعه‌ای از منابع KRM را با استفاده از یک فایل 'kustomization.yaml' می‌سازد. آرگومان DIR باید مسیر دایرکتوری‌ای باشد که فایل 'kustomization.yaml' را در خود دارد، یا URL یک مخزن git باشد که پسوند مسیر آن، همان دایرکتوری را نسبت به ریشهٔ مخزن مشخص می‌کند. اگر DIR ذکر نشود، مقدار '.' در نظر گرفته می‌شود.

```
kubectl kustomize DIR [flags]
```

## {{% heading "examples" %}}

```
  # Build the current working directory
  kubectl kustomize
  
  # Build some shared configuration directory
  kubectl kustomize /home/config/production
  
  # Build from github
  kubectl kustomize https://github.com/kubernetes-sigs/kustomize.git/examples/helloWorld?ref=v1.0.6
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--as-current-user</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای اجرای تابع در کانتینر، از uid و gid کاربری که دستور را اجرا می‌کند استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--enable-alpha-plugins</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>افزونه‌های (plugins) kustomize را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--enable-helm</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>استفاده از مولد بازکنندهٔ چارت Helm (Helm chart inflator generator) را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-e, --env strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از متغیرهای محیطی که توابع از آن‌ها استفاده می‌کنند.</p></td>
</tr>

<tr>
<td colspan="2">--helm-api-versions strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌های API کوبرنتیز که Helm برای Capabilities.APIVersions از آن‌ها استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--helm-command string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "helm"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دستور helm (مسیر فایل اجرایی).</p></td>
</tr>

<tr>
<td colspan="2">--helm-debug</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>خروجی اشکال‌زدایی (debug) مولد بازکنندهٔ چارت Helm را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--helm-kube-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ کوبرنتیز که Helm برای Capabilities.KubeVersion از آن استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور kustomize را نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--load-restrictor string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "LoadRestrictionsRootOnly"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن 'LoadRestrictionsNone' باشد، kustomizationهای محلی می‌توانند فایل‌هایی را از بیرون از ریشهٔ خود بارگذاری کنند. با این حال، این کار قابلیت جابه‌جایی (relocatability) آن kustomization را از بین می‌برد.</p></td>
</tr>

<tr>
<td colspan="2">--mount strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از گزینه‌های ذخیره‌سازی که از سیستم فایل خوانده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--network</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دسترسی به شبکه را برای توابعی که آن را اعلام کرده‌اند فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--network-name string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "bridge"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شبکهٔ docker که کانتینر در آن اجرا می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-o, --output string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مشخص شود، خروجی در این مسیر نوشته می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری که عملیات به جای او (impersonate) انجام می‌شود. این کاربر می‌تواند یک کاربر عادی یا یک حساب سرویس (service account) در یک فضای نام (namespace) باشد.</p></td>
</tr>

<tr>
<td colspan="2">--as-group strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروهی که عملیات به جای آن انجام می‌شود. برای مشخص کردن چند گروه، می‌توان این فلگ را چند بار تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--as-uid string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسهٔ UID که عملیات به جای آن انجام می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--as-user-extra strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اطلاعات اضافی کاربری که عملیات به جای او انجام می‌شود. برای مشخص کردن چند مقدار برای یک کلید، می‌توان این فلگ را چند بار تکرار کرد.</p></td>
</tr>

<tr>
<td colspan="2">--cache-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "$HOME/.kube/cache"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری پیش‌فرض حافظهٔ نهان (cache).</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کلاستری از kubeconfig که باید استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--context string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام زمینه‌ای (context) از kubeconfig که باید استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--disable-compression</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، فشرده‌سازی پاسخ برای همهٔ درخواست‌هایی که به سرور فرستاده می‌شوند غیرفعال می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig که برای درخواست‌های CLI استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--kuberc string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kuberc که برای ترجیحات (preferences) استفاده می‌شود. برای غیرفعال کردن آن می‌توان feature gate مربوط را با export کردن KUBECTL_KUBERC=false غیرفعال کرد یا قابلیت را با KUBERC=off خاموش کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مشخص شود، دامنهٔ فضای نام برای این درخواست CLI را تعیین می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام پروفایلی که باید ثبت شود. یکی از مقادیر (none|cpu|heap|goroutine|threadcreate|block|mutex|trace)</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پیش از صرف‌نظر کردن از یک درخواست منفرد به سرور، منتظر می‌ماند. مقادیر غیرصفر باید واحد زمانی متناظر داشته باشند (مثلاً 1s، 2m، 3h). مقدار صفر یعنی درخواست‌ها هیچ‌گاه به پایان مهلت (timeout) نمی‌رسند.</p></td>
</tr>

<tr>
<td colspan="2">-s, --server string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی و درگاه (port) سرور API کوبرنتیز.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-buffer-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوشتن‌ها در درایور ذخیره‌سازی به همین مدت در بافر نگه داشته می‌شوند و سپس در قالب یک تراکنش واحد در پشتیبان‌های غیرحافظه‌ای (non memory backends) ثبت می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی host:port پایگاه داده.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-password string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "root"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گذرواژهٔ پایگاه داده.</p></td>
</tr>

<tr>
<td colspan="2">--storage-driver-secure</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از اتصال امن با پایگاه داده استفاده می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام سروری که برای اعتبارسنجی گواهی سرور استفاده می‌شود. اگر مشخص نشود، از نام میزبانی (hostname) استفاده می‌شود که برای برقراری ارتباط با سرور به کار رفته است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربری از kubeconfig که باید استفاده شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گزینه‌های --version و --version=raw اطلاعات نسخه را چاپ می‌کنند و از برنامه خارج می‌شوند؛ گزینهٔ --version=vX.Y.Z... نسخهٔ گزارش‌شده را تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--warnings-as-errors</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هشدارهای دریافت‌شده از سرور را خطا در نظر می‌گیرد و با کد خروج غیرصفر خارج می‌شود.</p></td>
</tr>

</tbody>
</table>



## {{% heading "seealso" %}}

* [kubectl](../kubectl/)	 - دستور kubectl مدیر کلاستر کوبرنتیز را کنترل می‌کند

---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "WebhookClientConfig"
content_type: "api_reference"
description: "WebhookClientConfig اطلاعات لازم برای برقراری اتصال TLS با webhook را در بر دارد"
title: "WebhookClientConfig"
weight: 660
auto_generated: true
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

`apiVersion: admissionregistration.k8s.io/v1`

`import "k8s.io/api/admissionregistration/v1"`


## WebhookClientConfig {#WebhookClientConfig}

WebhookClientConfig اطلاعات لازم برای برقراری اتصال TLS با webhook را در بر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>caBundle</code><br/><em>string</em></td>
      <td>caBundle یک بسته CA با کدگذاری PEM است که برای اعتبارسنجی گواهی سرور webhook استفاده می‌شود. اگر مقداردهی نشود، از ریشه‌های اعتماد سیستمی موجود روی apiserver استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>service</code><br/><em><a href="{{< ref "../apiregistration/api-service-v1#ServiceReference" >}}">ServiceReference</a></em></td>
      <td>service ارجاعی به سرویس این webhook است. باید یکی از `service` یا `url` مشخص شود. اگر webhook درون کلاستر اجرا می‌شود، باید از `service` استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>url</code><br/><em>string</em></td>
      <td>url نشانی webhook را به قالب استاندارد URL (`scheme://host:port/path`) مشخص می‌کند. دقیقاً یکی از `url` یا `service` باید مشخص شود. `host` نباید به سرویسی اشاره کند که درون کلاستر اجرا می‌شود؛ به‌جای آن از فیلد `service` استفاده کنید. در برخی apiserverها ممکن است host از طریق DNS خارجی تفکیک شود (برای مثال، `kube-apiserver` نمی‌تواند DNS درون کلاستر را تفکیک کند، زیرا این کار نقض لایه‌بندی خواهد بود). `host` می‌تواند یک نشانی IP نیز باشد. توجه داشته باشید که استفاده از `localhost` یا `127.0.0.1` به‌عنوان `host` پرخطر است، مگر اینکه با دقت زیاد این webhook را روی تمام هاست‌هایی اجرا کنید که apiserver آن‌ها ممکن است لازم باشد به این webhook درخواست ارسال کند. چنین نصب‌هایی احتمالاً قابل‌حمل نیستند، یعنی راه‌اندازی آن‌ها در یک کلاستر جدید آسان نیست. scheme باید "https" باشد؛ یعنی URL باید با "https://" آغاز شود. بخش path اختیاری است و در صورت وجود می‌تواند هر رشته‌ای باشد که در URL مجاز است. می‌توانید از path برای ارسال یک رشته دلخواه به webhook استفاده کنید، برای مثال شناسه کلاستر. استفاده از کاربر یا احراز هویت basic، مانند "user:password@"، مجاز نیست. fragmentها ("#...") و پارامترهای query ("?...") نیز مجاز نیستند.</td>
    </tr>
  </tbody>
</table>

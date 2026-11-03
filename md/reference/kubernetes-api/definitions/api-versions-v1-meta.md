---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "APIVersions"
content_type: "api_reference"
description: "APIVersions نسخه‌های در دسترس را فهرست می‌کند تا کلاینت‌ها بتوانند API را در مسیر /api، که مسیر ریشه‌ی API قدیمی v1 است، کشف کنند."
title: "APIVersions"
weight: 40
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

`apiVersion: meta/v1`

`import "k8s.io/apimachinery/pkg/apis/meta/v1"`


## APIVersions {#APIVersions}

آبجکت APIVersions نسخه‌های در دسترس را فهرست می‌کند تا کلاینت‌ها بتوانند API را در مسیر /api، که مسیر ریشه‌ی API قدیمی v1 است، کشف کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحواره‌ی نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه‌ی دسترسی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این مقدار قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>serverAddressByClientCIDRs</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "server-address-by-client-cidr-v1-meta#ServerAddressByClientCIDR" >}}">ServerAddressByClientCIDR array</a></em></td>
      <td>نگاشتی از CIDR کلاینت به آدرس سروری که به این گروه سرویس می‌دهد. این نگاشت به کلاینت‌ها کمک می‌کند از کارآمدترین مسیر شبکه‌ای به سرورها دسترسی پیدا کنند. کلاینت‌ها می‌توانند آدرس سرور مناسب را بر اساس CIDRای که با آن مطابقت دارند انتخاب کنند. در صورت وجود چند تطابق، کلاینت‌ها باید CIDR با طولانی‌ترین تطابق را به کار ببرند. سرور فقط CIDRهایی را برمی‌گرداند که تشخیص می‌دهد کلاینت می‌تواند با آن‌ها تطابق داشته باشد. برای مثال، اگر کلاینت با یک IP داخلی به سرور دسترسی پیدا کند، master فقط CIDR مربوط به IP داخلی را برمی‌گرداند. سرور برای به‌دست آوردن IP کلاینت، به‌ترتیب هدر X-Forwarded-For، هدر X-Real-Ip و request.RemoteAddr را بررسی می‌کند.</td>
    </tr>
    <tr>
      <td><code>versions</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>versions نسخه‌های API در دسترس را مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>

---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "APIGroup"
content_type: "api_reference"
description: "APIGroup شامل نام، نسخه‌های پشتیبانی‌شده و نسخه ترجیحی یک گروه است."
title: "APIGroup"
weight: 20
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


## APIGroup {#APIGroup}

APIGroup شامل نام، نسخه‌های پشتیبانی‌شده و نسخه ترجیحی یک گروه است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام گروه است.</td>
    </tr>
    <tr>
      <td><code>preferredVersion</code><br/><em><a href="{{< ref "group-version-for-discovery-v1-meta#GroupVersionForDiscovery" >}}">GroupVersionForDiscovery</a></em></td>
      <td>preferredVersion نسخه‌ای است که API server ترجیح می‌دهد و احتمالاً همان نسخه ذخیره‌سازی (storage version) است.</td>
    </tr>
    <tr>
      <td><code>serverAddressByClientCIDRs</code><br/><em><a href="{{< ref "server-address-by-client-cidr-v1-meta#ServerAddressByClientCIDR" >}}">ServerAddressByClientCIDR array</a></em></td>
      <td>نگاشتی از CIDR کلاینت به آدرس سروری که به این گروه سرویس می‌دهد. هدف از این نگاشت آن است که کلاینت‌ها بتوانند با بهینه‌ترین مسیر شبکه‌ای به سرورها دسترسی پیدا کنند. کلاینت‌ها می‌توانند آدرس سرور مناسب را بر اساس CIDRی که با آن مطابقت دارند انتخاب کنند. اگر چند CIDR مطابقت داشته باشند، کلاینت‌ها باید طولانی‌ترین CIDR منطبق را به کار ببرند. سرور فقط CIDRهایی را برمی‌گرداند که تشخیص می‌دهد کلاینت می‌تواند با آن‌ها مطابقت پیدا کند. برای مثال، اگر کلاینت با یک IP داخلی به سرور دسترسی پیدا کند، master فقط CIDR مربوط به IP داخلی را برمی‌گرداند. سرور برای به‌دست آوردن IP کلاینت، به‌ترتیب هدر X-Forwarded-For، هدر X-Real-Ip و request.RemoteAddr را بررسی می‌کند.</td>
    </tr>
    <tr>
      <td><code>versions</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "group-version-for-discovery-v1-meta#GroupVersionForDiscovery" >}}">GroupVersionForDiscovery array</a></em></td>
      <td>versions نسخه‌هایی هستند که در این گروه پشتیبانی می‌شوند.</td>
    </tr>
  </tbody>
</table>


## APIGroupList {#APIGroupList}

APIGroupList فهرستی از APIGroupها است تا کلاینت‌ها بتوانند API را در مسیر /apis کشف کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>groups</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "api-group-v1-meta#APIGroup" >}}">APIGroup array</a></em></td>
      <td>groups فهرستی از APIGroupها است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>

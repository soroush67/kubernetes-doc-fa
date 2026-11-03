---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "Status"
content_type: "api_reference"
description: "Status مقدار بازگشتی فراخوانی‌هایی است که آبجکت دیگری برنمی‌گردانند."
title: "Status"
weight: 510
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


## Status {#Status}

Status مقدار بازگشتی فراخوانی‌هایی است که آبجکت دیگری برنمی‌گردانند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>code</code><br/><em>integer</em></td>
      <td>کد بازگشتی HTTP پیشنهادی برای این وضعیت؛ در صورت تنظیم نشدن، مقدار آن 0 است.</td>
    </tr>
    <tr>
      <td><code>details</code><br/><em><a href="{{< ref "status-details-v1-meta#StatusDetails" >}}">StatusDetails</a></em></td>
      <td>داده‌های تکمیلی مرتبط با دلیل (reason). هر دلیل می‌تواند جزئیات تکمیلی مختص خود را تعریف کند. این فیلد اختیاری است و تضمینی وجود ندارد که داده‌های بازگشتی با طرح‌واره‌ای جز طرح‌واره تعریف‌شده توسط نوع دلیل مطابقت داشته باشند.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST معرفی‌شده توسط این آبجکت را نشان می‌دهد. سرورها می‌توانند آن را از نقطه دسترسی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این مقدار قابل به‌روزرسانی نیست و باید به صورت CamelCase باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>توضیحی قابل‌خواندن برای انسان درباره وضعیت این عملیات.</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>توضیحی قابل‌پردازش توسط ماشین درباره اینکه چرا این عملیات در وضعیت «Failure» قرار دارد. اگر این مقدار خالی باشد، هیچ اطلاعاتی در دسترس نیست. Reason کد وضعیت HTTP را روشن‌تر می‌کند، اما جایگزین آن نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em>string</em></td>
      <td>وضعیت عملیات. یکی از مقادیر «Success» یا «Failure». اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
  </tbody>
</table>

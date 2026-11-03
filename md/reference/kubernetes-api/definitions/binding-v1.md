---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "Binding"
content_type: "api_reference"
description: "Binding یک آبجکت را به آبجکت دیگر متصل می‌کند؛ برای مثال، زمان‌بند یک Pod را به یک نود متصل می‌کند."
title: "Binding"
weight: 60
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## Binding {#Binding}

Binding یک آبجکت را به آبجکت دیگر متصل می‌کند؛ برای مثال، زمان‌بند یک Pod را به یک نود متصل (bind) می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره (schema) نسخه‌دار این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این مقدار قابل به‌روزرسانی نیست و باید به صورت CamelCase باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>target</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "object-reference-v1#ObjectReference" >}}">ObjectReference</a></em></td>
      <td>آبجکت هدفی که می‌خواهید آبجکت استاندارد را به آن متصل کنید.</td>
    </tr>
  </tbody>
</table>

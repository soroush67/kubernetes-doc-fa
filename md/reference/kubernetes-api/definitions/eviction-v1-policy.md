---
api_metadata:
  apiVersion: "policy/v1"
  import: "k8s.io/api/policy/v1"
  kind: "Eviction"
content_type: "api_reference"
description: "Eviction یک Pod را با رعایت سیاست‌ها و محدودیت‌های ایمنی مشخص از نود آن خارج می‌کند. این آبجکت یک زیرمنبع (subresource) از Pod است. درخواست انجام چنین خروج‌سازی‌ای با ارسال POST به .../pods/&lt;pod name&gt;/evictions ایجاد می‌شود."
title: "Eviction"
weight: 100
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

`apiVersion: policy/v1`

`import "k8s.io/api/policy/v1"`


## Eviction {#Eviction}

آبجکت Eviction یک Pod را با رعایت سیاست‌ها و محدودیت‌های ایمنی مشخص از نود آن خارج می‌کند. این آبجکت یک زیرمنبع (subresource) از Pod است. درخواست انجام چنین خروج‌سازی‌ای با ارسال POST به .../pods/&lt;pod name&gt;/evictions ایجاد می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره (schema) نسخه‌دار این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>deleteOptions</code><br/><em><a href="{{< ref "delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td>deleteOptions را می‌توان مشخص کرد.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST مرتبط با این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌هایش را به آن ارسال می‌کند استنباط کنند. این مقدار قابل به‌روزرسانی نیست و باید به‌صورت CamelCase باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata، Pod را که در حال خارج‌سازی است توصیف می‌کند.</td>
    </tr>
  </tbody>
</table>

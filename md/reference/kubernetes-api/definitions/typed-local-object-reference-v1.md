---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "TypedLocalObjectReference"
content_type: "api_reference"
description: "TypedLocalObjectReference اطلاعات کافی برای یافتن آبجکت تایپ‌دارِ ارجاع‌شده در همان فضای نام (namespace) را در اختیار می‌گذارد."
title: "TypedLocalObjectReference"
weight: 600
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


## TypedLocalObjectReference {#TypedLocalObjectReference}

TypedLocalObjectReference اطلاعات کافی برای یافتن آبجکت تایپ‌دارِ ارجاع‌شده در همان فضای نام (namespace) را در اختیار می‌گذارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>APIGroup گروه منبعِ ارجاع‌شده است. اگر APIGroup مشخص نشود، Kind مشخص‌شده باید در گروه API هسته (core) باشد. برای هر نوع شخص ثالث دیگر، تعیین APIGroup الزامی است.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Kind نوعِ منبعِ ارجاع‌شده است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نامِ منبعِ ارجاع‌شده است.</td>
    </tr>
  </tbody>
</table>

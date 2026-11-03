---
api_metadata:
  apiVersion: "scheduling.k8s.io/v1beta1"
  import: "k8s.io/api/scheduling/v1beta1"
  kind: "TypedLocalObjectReference"
content_type: "api_reference"
description: "TypedLocalObjectReference امکان ارجاع به یک آبجکت دارای نوع را در همان namespace فراهم می‌کند."
title: "TypedLocalObjectReference"
weight: 610
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

`apiVersion: scheduling.k8s.io/v1beta1`

`import "k8s.io/api/scheduling/v1beta1"`


## TypedLocalObjectReference {#TypedLocalObjectReference}

TypedLocalObjectReference امکان ارجاع به یک آبجکت دارای نوع را در همان فضای نام (namespace) فراهم می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>apiGroup گروهِ منبعی است که به آن ارجاع داده می‌شود. اگر apiGroup خالی باشد، Kind مشخص‌شده باید در گروه API هسته (core) باشد. برای هر نوع شخص ثالث دیگر، تعیین apiGroup الزامی است. مقدار آن باید یک زیردامنه DNS باشد.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>kind نوع منبعی است که به آن ارجاع داده می‌شود. مقدار آن باید یک نام قطعه مسیر (path segment) باشد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام منبعی است که به آن ارجاع داده می‌شود. مقدار آن باید یک نام قطعه مسیر (path segment) باشد.</td>
    </tr>
  </tbody>
</table>

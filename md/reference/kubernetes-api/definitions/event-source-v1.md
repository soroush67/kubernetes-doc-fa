---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "EventSource"
content_type: "api_reference"
description: "EventSource شامل اطلاعاتی درباره یک رویداد (event) است."
title: "EventSource"
weight: 90
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


## EventSource {#EventSource}

آبجکت EventSource شامل اطلاعاتی درباره یک رویداد (event) است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>component</code><br/><em>string</em></td>
      <td>مؤلفه‌ای که رویداد از آن تولید شده است.</td>
    </tr>
    <tr>
      <td><code>host</code><br/><em>string</em></td>
      <td>نام نودی که رویداد روی آن تولید شده است.</td>
    </tr>
  </tbody>
</table>

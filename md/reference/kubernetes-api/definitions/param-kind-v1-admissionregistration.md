---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "ParamKind"
content_type: "api_reference"
description: "ParamKind یک چندتایی (tuple) از Group، Kind و Version است."
title: "ParamKind"
weight: 340
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


## ParamKind {#ParamKind}

ParamKind یک چندتایی (tuple) از Group، Kind و Version است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>apiVersion نسخهٔ گروه API است که منابع به آن تعلق دارند. قالب آن به صورت «group/version» است. الزامی است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>kind نوع API (API kind) است که منابع به آن تعلق دارند. الزامی است.</td>
    </tr>
  </tbody>
</table>

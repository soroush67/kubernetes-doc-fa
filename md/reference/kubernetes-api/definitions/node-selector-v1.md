---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "NodeSelector"
content_type: "api_reference"
description: "یک node selector نمایانگر اجتماع نتایج یک یا چند پرس‌وجوی برچسب روی مجموعه‌ای از نودهاست؛ یعنی نمایانگر OR انتخابگرهایی است که node selector termها تعیین می‌کنند."
title: "NodeSelector"
weight: 270
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


## NodeSelector {#NodeSelector}

یک node selector نمایانگر اجتماع نتایج یک یا چند پرس‌وجوی برچسب روی مجموعه‌ای از نودهاست؛ یعنی نمایانگر OR انتخابگرهایی است که node selector termها تعیین می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nodeSelectorTerms</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "node-selector-term-v1#NodeSelectorTerm" >}}">آرایه‌ای از NodeSelectorTerm</a></em></td>
      <td>الزامی. فهرستی از node selector termها. این termها با عملگر OR با یکدیگر ترکیب می‌شوند.</td>
    </tr>
  </tbody>
</table>

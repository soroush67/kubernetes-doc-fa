---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "NodeSelectorTerm"
content_type: "api_reference"
description: "یک node selector term تهی (null) یا خالی با هیچ آبجکتی مطابقت ندارد. الزامات آن با عملگر AND با یکدیگر ترکیب می‌شوند. نوع TopologySelectorTerm زیرمجموعه‌ای از NodeSelectorTerm را پیاده‌سازی می‌کند."
title: "NodeSelectorTerm"
weight: 280
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


## NodeSelectorTerm {#NodeSelectorTerm}

یک node selector term تهی (null) یا خالی با هیچ آبجکتی مطابقت ندارد. الزامات آن با عملگر AND با یکدیگر ترکیب می‌شوند. نوع TopologySelectorTerm زیرمجموعه‌ای از NodeSelectorTerm را پیاده‌سازی می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>matchExpressions</code><br/><em><a href="{{< ref "../resource/resource-slice-v1#NodeSelectorRequirement" >}}">NodeSelectorRequirement array</a></em></td>
      <td>فهرستی از الزامات انتخابگر نود بر اساس برچسب‌های نود.</td>
    </tr>
    <tr>
      <td><code>matchFields</code><br/><em><a href="{{< ref "../resource/resource-slice-v1#NodeSelectorRequirement" >}}">NodeSelectorRequirement array</a></em></td>
      <td>فهرستی از الزامات انتخابگر نود بر اساس فیلدهای نود.</td>
    </tr>
  </tbody>
</table>

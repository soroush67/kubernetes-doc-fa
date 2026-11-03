---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "LabelSelector"
content_type: "api_reference"
description: "یک label selector، پرس‌وجویی مبتنی بر برچسب روی مجموعه‌ای از منابع است. نتایج matchLabels و matchExpressions با هم AND می‌شوند. یک label selector خالی با همه آبجکت‌ها مطابقت دارد. یک label selector با مقدار null با هیچ آبجکتی مطابقت ندارد."
title: "LabelSelector"
weight: 160
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


## LabelSelector {#LabelSelector}

یک label selector، پرس‌وجویی مبتنی بر برچسب روی مجموعه‌ای از منابع است. نتایج matchLabels و matchExpressions با هم AND می‌شوند. یک label selector خالی با همه آبجکت‌ها مطابقت دارد. یک label selector با مقدار null با هیچ آبجکتی مطابقت ندارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>matchExpressions</code><br/><em><a href="{{< ref "label-selector-requirement-v1-meta#LabelSelectorRequirement" >}}">LabelSelectorRequirement array</a></em></td>
      <td>matchExpressions فهرستی از الزامات label selector است. این الزامات با هم AND می‌شوند.</td>
    </tr>
    <tr>
      <td><code>matchLabels</code><br/><em>object</em></td>
      <td>matchLabels نگاشتی از جفت‌های {key,value} است. هر جفت {key,value} در نگاشت matchLabels معادل یک عنصر از matchExpressions است که فیلد key آن برابر "key"، عملگر آن "In" و آرایه values آن فقط شامل "value" است. این الزامات با هم AND می‌شوند.</td>
    </tr>
  </tbody>
</table>

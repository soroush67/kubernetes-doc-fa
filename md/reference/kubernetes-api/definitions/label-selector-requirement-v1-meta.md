---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "LabelSelectorRequirement"
content_type: "api_reference"
description: "یک LabelSelectorRequirement شرطی در انتخابگر برچسب است که شامل یک کلید، یک عملگر و مجموعه‌ای از مقادیر است و عملگر، رابطهٔ کلید با مقادیر را مشخص می‌کند."
title: "LabelSelectorRequirement"
weight: 180
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


## LabelSelectorRequirement {#LabelSelectorRequirement}

یک LabelSelectorRequirement شرطی در انتخابگر برچسب (label selector) است که شامل یک کلید، یک عملگر و مجموعه‌ای از مقادیر است و عملگر، رابطهٔ کلید با مقادیر را مشخص می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>key کلید برچسبی است که انتخابگر روی آن اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>operator</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>operator رابطهٔ یک کلید را با مجموعه‌ای از مقادیر مشخص می‌کند. عملگرهای معتبر عبارتند از In، NotIn، Exists و DoesNotExist.</td>
    </tr>
    <tr>
      <td><code>values</code><br/><em>string array</em></td>
      <td>values آرایه‌ای از مقادیر رشته‌ای است. اگر عملگر In یا NotIn باشد، آرایهٔ values نباید خالی باشد. اگر عملگر Exists یا DoesNotExist باشد، آرایهٔ values باید خالی باشد. این آرایه در جریان strategic merge patch جایگزین می‌شود.</td>
    </tr>
  </tbody>
</table>

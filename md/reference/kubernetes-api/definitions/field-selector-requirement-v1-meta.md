---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "FieldSelectorRequirement"
content_type: "api_reference"
description: "FieldSelectorRequirement یک انتخابگر (selector) است که شامل مقادیر، یک کلید و یک عملگر است که کلید و مقادیر را به یکدیگر مرتبط می‌کند."
title: "FieldSelectorRequirement"
weight: 120
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


## FieldSelectorRequirement {#FieldSelectorRequirement}

FieldSelectorRequirement یک انتخابگر (selector) است که شامل مقادیر، یک کلید و یک عملگر است که کلید و مقادیر را به یکدیگر مرتبط می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>key کلید انتخابگر فیلد است که این الزام (requirement) برای آن اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>operator</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>operator رابطه یک کلید را با مجموعه‌ای از مقادیر مشخص می‌کند. عملگرهای معتبر عبارت‌اند از In، NotIn، Exists و DoesNotExist. فهرست عملگرها ممکن است در آینده گسترش یابد.</td>
    </tr>
    <tr>
      <td><code>values</code><br/><em>string array</em></td>
      <td>values آرایه‌ای از مقادیر رشته‌ای است. اگر operator برابر In یا NotIn باشد، آرایه values نباید خالی باشد. اگر operator برابر Exists یا DoesNotExist باشد، آرایه values باید خالی باشد.</td>
    </tr>
  </tbody>
</table>

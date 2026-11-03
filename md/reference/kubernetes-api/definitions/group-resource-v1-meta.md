---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "GroupResource"
content_type: "api_reference"
description: "GroupResource یک Group و یک Resource را مشخص می‌کند، اما نسخه‌ای را اجباری نمی‌کند. این ویژگی در مراحل جستجو برای شناسایی مفاهیم، بدون نیاز به انواع نیمه‌معتبر، مفید است."
title: "GroupResource"
weight: 140
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


## GroupResource {#GroupResource}

GroupResource یک Group و یک Resource را مشخص می‌کند، اما نسخه‌ای را اجباری نمی‌کند. این ویژگی در مراحل جستجو برای شناسایی مفاهیم، بدون نیاز به انواع نیمه‌معتبر، مفید است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>group</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>resource</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td></td>
    </tr>
  </tbody>
</table>

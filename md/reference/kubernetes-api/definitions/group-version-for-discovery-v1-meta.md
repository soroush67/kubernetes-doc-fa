---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "GroupVersionForDiscovery"
content_type: "api_reference"
description: "GroupVersion شامل رشته‌های «group/version» و «version» یک نسخه است. این مورد برای حفظ قابلیت توسعه‌پذیری به‌صورت یک struct تعریف شده است."
title: "GroupVersionForDiscovery"
weight: 150
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


## GroupVersionForDiscovery {#GroupVersionForDiscovery}

GroupVersion شامل رشته‌های «group/version» و «version» یک نسخه است. این مورد برای حفظ قابلیت توسعه‌پذیری به‌صورت یک struct تعریف شده است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>groupVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد groupVersion گروه API و نسخه را به‌صورت «group/version» مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>version</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد version نسخه را به‌صورت «version» مشخص می‌کند. این فیلد وجود دارد تا کلاینت‌ها مجبور نباشند GroupVersion را خودشان تفکیک کنند.</td>
    </tr>
  </tbody>
</table>

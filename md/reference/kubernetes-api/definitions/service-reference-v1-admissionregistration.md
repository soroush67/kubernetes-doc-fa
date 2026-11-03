---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "ServiceReference"
content_type: "api_reference"
description: "ServiceReference holds a reference to Service.legacy.k8s.io"
title: "ServiceReference"
weight: 490
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


## ServiceReference {#ServiceReference}

ServiceReference شامل یک ارجاع به Service.legacy.k8s.io است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام سرویس است. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>namespace</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>namespace فضای نام (namespace) سرویس است. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>path یک مسیر URL اختیاری است که در هر درخواست ارسالی به این سرویس فرستاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>port</code><br/><em>integer</em></td>
      <td>port درگاهی از سرویس است که webhook را میزبانی می‌کند. برای سازگاری با نسخه‌های قبلی، مقدار پیش‌فرض ۴۴۳ است. مقدار `port` باید یک شماره درگاه معتبر (از ۱ تا ۶۵۵۳۵، با احتساب هر دو مقدار) باشد.</td>
    </tr>
  </tbody>
</table>

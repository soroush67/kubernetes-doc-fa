---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "Variable"
content_type: "api_reference"
description: "Variable تعریف یک متغیر است که برای ترکیب (composition) استفاده می‌شود. هر متغیر به‌صورت یک عبارت نام‌دار تعریف می‌شود."
title: "Variable"
weight: 630
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


## Variable {#Variable}

Variable تعریف یک متغیر است که برای ترکیب (composition) استفاده می‌شود. هر متغیر به‌صورت یک عبارت نام‌دار تعریف می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>expression عبارتی است که به‌عنوان مقدار متغیر ارزیابی می‌شود. عبارت CEL به همان شناسه‌هایی دسترسی دارد که عبارت‌های CEL در Validation به آن‌ها دسترسی دارند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام متغیر است. این نام باید یک شناسه معتبر CEL و در میان همه متغیرها یکتا باشد. می‌توان از طریق `variables` در عبارت‌های دیگر به متغیر دسترسی داشت. برای مثال، اگر name برابر "foo" باشد، متغیر با عنوان `variables.foo` در دسترس خواهد بود.</td>
    </tr>
  </tbody>
</table>

---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "NonResourceRule"
content_type: "api_reference"
description: "NonResourceRule قاعده‌ای را توصیف می‌کند که برای درخواست‌های غیرمنبعی (non-resource) اعمال می‌شود"
title: "NonResourceRule"
weight: 300
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

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`


## NonResourceRule {#NonResourceRule}

NonResourceRule اطلاعاتی را نگهداری می‌کند که یک قاعده را برای درخواست‌های غیرمنبعی (non-resource) توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nonResourceURLs</code><br/><em>string array</em></td>
      <td>nonResourceURLs مجموعه‌ای از URLهای جزئی است که کاربر باید به آن‌ها دسترسی داشته باشد. استفاده از «*» مجاز است، اما فقط به‌عنوان آخرین گام کامل مسیر. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>verbs</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>verbs فهرستی از فعل‌های (verb) API غیرمنبعی کوبرنتیز است، مانند: get، post، put، delete، patch، head و options. مقدار "*" به معنای همه است.</td>
    </tr>
  </tbody>
</table>

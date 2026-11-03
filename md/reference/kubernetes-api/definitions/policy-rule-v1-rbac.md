---
api_metadata:
  apiVersion: "rbac.authorization.k8s.io/v1"
  import: "k8s.io/api/rbac/v1"
  kind: "PolicyRule"
content_type: "api_reference"
description: "PolicyRule اطلاعاتی را نگهداری می‌کند که یک قانون سیاستی (policy rule) را توصیف می‌کند، اما شامل اطلاعاتی درباره اینکه قانون برای چه کسی یا در کدام فضای نام (namespace) اعمال می‌شود نیست."
title: "PolicyRule"
weight: 370
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

`apiVersion: rbac.authorization.k8s.io/v1`

`import "k8s.io/api/rbac/v1"`


## PolicyRule {#PolicyRule}

PolicyRule اطلاعاتی را نگهداری می‌کند که یک قانون سیاستی را توصیف می‌کند، اما شامل اطلاعاتی درباره اینکه قانون برای چه کسی یا در کدام فضای نام اعمال می‌شود نیست.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroups</code><br/><em>string array</em></td>
      <td>apiGroups نام APIGroup‌ای است که منابع را در بر می‌گیرد. اگر چندین API group مشخص شده باشد، هر اقدامی که روی یکی از منابع فهرست‌شده در هر یک از این API groupها درخواست شود، مجاز خواهد بود. مقدار "" نشان‌دهنده core API group و مقدار "*" نشان‌دهنده همه API groupها است.</td>
    </tr>
    <tr>
      <td><code>nonResourceURLs</code><br/><em>string array</em></td>
      <td>nonResourceURLs مجموعه‌ای از URLهای جزئی است که کاربر باید به آن‌ها دسترسی داشته باشد. کاراکتر * مجاز است، اما فقط به‌عنوان آخرین و کامل‌ترین بخش مسیر. از آنجا که URLهای غیرمنبع (non-resource) به فضای نام تعلق ندارند، این فیلد فقط برای ClusterRoleهایی کاربرد دارد که از یک ClusterRoleBinding به آن‌ها ارجاع داده شده است. هر قانون می‌تواند یا به منابع API (مانند "pods" یا "secrets") اعمال شود یا به مسیرهای URL غیرمنبع (مانند "/api")، اما نه به هر دو.</td>
    </tr>
    <tr>
      <td><code>resourceNames</code><br/><em>string array</em></td>
      <td>resourceNames فهرست سفید (white list) اختیاری از نام‌هایی است که قانون برای آن‌ها اعمال می‌شود. مجموعه خالی به این معناست که همه چیز مجاز است.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em>string array</em></td>
      <td>resources فهرستی از منابعی است که این قانون برای آن‌ها اعمال می‌شود. مقدار '\*' نشان‌دهنده همه منابع است.</td>
    </tr>
    <tr>
      <td><code>verbs</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>verbs فهرستی از Verbها است که برای همه ResourceKindهای موجود در این قانون اعمال می‌شود. مقدار '\*' نشان‌دهنده همه verbها است.</td>
    </tr>
  </tbody>
</table>

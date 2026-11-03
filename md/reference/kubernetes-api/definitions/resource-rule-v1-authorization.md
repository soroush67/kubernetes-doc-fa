---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "ResourceRule"
content_type: "api_reference"
description: "ResourceRule فهرست اقدام‌هایی است که سوژه مجاز است روی منابع انجام دهد. ترتیب فهرست اهمیتی ندارد، ممکن است شامل موارد تکراری باشد و ممکن است ناقص باشد."
title: "ResourceRule"
weight: 410
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


## ResourceRule {#ResourceRule}

ResourceRule فهرست اقدام‌هایی است که سوژه مجاز است روی منابع انجام دهد. ترتیب فهرست اهمیتی ندارد، ممکن است شامل موارد تکراری باشد و ممکن است ناقص باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroups</code><br/><em>string array</em></td>
      <td>apiGroups نام APIGroup حاوی منابع است. اگر چند API group مشخص شده باشد، هر اقدامی که روی یکی از منابع فهرست‌شده در هر یک از این API groupها درخواست شود، مجاز خواهد بود. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>resourceNames</code><br/><em>string array</em></td>
      <td>resourceNames فهرست سفید اختیاری از نام‌هایی است که قاعده بر آن‌ها اعمال می‌شود. مجموعه خالی به این معناست که همه‌چیز مجاز است. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em>string array</em></td>
      <td>resources فهرستی از منابع است که این قاعده بر آن‌ها اعمال می‌شود. مقدار "*" به معنای همه منابع در apiGroups مشخص‌شده است. مقدار "*/foo" نمایانگر زیرمنبع 'foo' برای همه منابع در apiGroups مشخص‌شده است.</td>
    </tr>
    <tr>
      <td><code>verbs</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>verbs فهرستی از فعل‌های (verb) API منابع کوبرنتیز است، مانند: get, list, watch, create, update, delete, proxy. مقدار "*" به معنای همه است.</td>
    </tr>
  </tbody>
</table>

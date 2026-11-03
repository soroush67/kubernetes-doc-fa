---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "ShardInfo"
content_type: "api_reference"
description: "ShardInfo انتخابگر شارد (shard) را توصیف می‌کند که برای تولید یک پاسخ فهرست اعمال شده است. وجود این آبجکت در یک پاسخ فهرست نشان می‌دهد که فهرست، زیرمجموعه‌ای فیلترشده است."
title: "ShardInfo"
weight: 500
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


## ShardInfo {#ShardInfo}

ShardInfo انتخابگر شارد (shard) را توصیف می‌کند که برای تولید یک پاسخ فهرست اعمال شده است. وجود این آبجکت در یک پاسخ فهرست نشان می‌دهد که فهرست، زیرمجموعه‌ای فیلترشده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>selector</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>selector همان رشته انتخابگر شارد در درخواست است که در پاسخ نیز بازگردانده می‌شود تا کلاینت‌ها بتوانند بررسی کنند کدام شارد را دریافت کرده‌اند و پاسخ‌های چند شارد را با یکدیگر ادغام کنند.</td>
    </tr>
  </tbody>
</table>

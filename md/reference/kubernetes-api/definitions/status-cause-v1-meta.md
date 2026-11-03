---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "StatusCause"
content_type: "api_reference"
description: "StatusCause اطلاعات بیشتری درباره‌ی یک شکست api.Status ارائه می‌دهد، از جمله مواردی که با چندین خطا مواجه می‌شویم."
title: "StatusCause"
weight: 520
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


## StatusCause {#StatusCause}

StatusCause اطلاعات بیشتری درباره‌ی یک شکست api.Status ارائه می‌دهد، از جمله مواردی که با چندین خطا مواجه می‌شویم.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>field</code><br/><em>string</em></td>
      <td>فیلدی از منبع که این خطا را ایجاد کرده است، با نامی که در سریال‌سازی JSON آن آمده است. برای ویژگی‌های تودرتو ممکن است از نمادگذاری نقطه و پسوند استفاده شود. اندیس آرایه‌ها از صفر شروع می‌شود. به دلیل اینکه یک فیلد ممکن است چندین خطا داشته باشد، ممکن است یک فیلد بیش از یک بار در آرایه‌ی causes ظاهر شود. اختیاری است. نمونه‌ها: "name" - فیلد "name" در منبع جاری؛ "items[0].name" - فیلد "name" در اولین عنصر آرایه‌ی "items"</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>توضیحی قابل‌خواندن برای انسان درباره‌ی علت خطا. این فیلد را می‌توان بدون تغییر به خواننده نمایش داد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>توضیحی قابل‌پردازش برای ماشین درباره‌ی علت خطا. اگر این مقدار خالی باشد، هیچ اطلاعاتی در دسترس نیست.</td>
    </tr>
  </tbody>
</table>

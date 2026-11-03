---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "VolumeHealthCondition"
content_type: "api_reference"
description: "VolumeHealthCondition یک وضعیت سلامت نامطلوب را نشان می‌دهد که برای یک حجم (volume) گزارش شده است."
title: "VolumeHealthCondition"
weight: 640
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## VolumeHealthCondition {#VolumeHealthCondition}

VolumeHealthCondition یک وضعیت سلامت نامطلوب را نشان می‌دهد که برای یک حجم (volume) گزارش شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>message توضیحی قابل‌خواندن برای انسان است. حداکثر طول مجاز یک message برابر با ۱۰۲۴ بایت است.</td>
    </tr>
    <tr>
      <td><code>reason</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>reason یک دلیل کوتاه به‌صورت CamelCase است که ماشین می‌تواند آن را تحلیل (parse) کند. این فیلد همراه با status هویت یکتای یک مدخل وضعیت (condition) را تشکیل می‌دهد. حداکثر طول مجاز یک reason برابر با ۲۵۶ بایت است.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>status دسته‌بندی سلامت است که ماشین می‌تواند آن را تحلیل کند. مقادیر ممکن: - "Inaccessible": دسترسی به حجم امکان‌پذیر نیست. - "DataLoss": از دست رفتن داده در حجم شناسایی شده است. - "Degraded": حجم با قابلیت کاهش‌یافته کار می‌کند.<br/><br/>مقادیر enum ممکن:<br/> - `"DataLoss"` نشان می‌دهد از دست رفتن داده در حجم شناسایی شده است.<br/> - `"Degraded"` نشان می‌دهد حجم کار می‌کند، اما با قابلیت کاهش‌یافته.<br/> - `"Inaccessible"` نشان می‌دهد دسترسی به حجم امکان‌پذیر نیست.</td>
    </tr>
  </tbody>
</table>

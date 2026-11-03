---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "Condition"
content_type: "api_reference"
description: "Condition جزئیات یکی از جنبه‌های وضعیت فعلی این منبع API را در بر می‌گیرد."
title: "Condition"
weight: 70
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


## Condition {#Condition}

Condition جزئیات یکی از جنبه‌های وضعیت فعلی این منبع API را در بر می‌گیرد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastTransitionTime</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "time-v1-meta#Time" >}}">Time</a></em></td>
      <td>lastTransitionTime آخرین زمانی است که condition از یک وضعیت به وضعیت دیگر تغییر کرده است. این مقدار باید زمان تغییر condition اصلی و زیربنایی باشد. اگر این زمان مشخص نیست، می‌توان از زمان تغییر فیلد API استفاده کرد.</td>
    </tr>
    <tr>
      <td><code>message</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>message پیامی قابل‌خواندن برای انسان است که جزئیات مربوط به این انتقال وضعیت را بیان می‌کند. این مقدار می‌تواند یک رشته خالی باشد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>observedGeneration نشان‌دهنده مقدار <code>.metadata.generation</code> است که condition بر اساس آن تنظیم شده است. برای مثال، اگر مقدار فعلی <code>.metadata.generation</code> برابر 12 باشد، اما مقدار <code>.status.conditions[x].observedGeneration</code> برابر 9 باشد، condition نسبت به وضعیت فعلی نمونه قدیمی (منقضی‌شده) است.</td>
    </tr>
    <tr>
      <td><code>reason</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>reason شامل یک شناسه برنامه‌نویسی‌شده است که دلیل آخرین انتقال وضعیت condition را مشخص می‌کند. تولیدکنندگان انواع خاصی از condition می‌توانند مقادیر مورد انتظار و معانی آن‌ها را برای این فیلد تعریف کنند و مشخص کنند که آیا این مقادیر یک API تضمین‌شده به شمار می‌روند یا خیر. مقدار این فیلد باید یک رشته با قالب CamelCase باشد. این فیلد نباید خالی باشد.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>status وضعیت condition است و یکی از مقادیر True، False یا Unknown را دارد.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>type نوع condition است و به قالب CamelCase یا foo.example.com/CamelCase نوشته می‌شود.</td>
    </tr>
  </tbody>
</table>

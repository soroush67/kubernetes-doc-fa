---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "WatchEvent"
content_type: "api_reference"
description: "Event یک رویداد منفرد را برای یک منبع تحت نظر (watch) نشان می‌دهد."
title: "WatchEvent"
weight: 650
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


## WatchEvent {#WatchEvent}

Event یک رویداد منفرد را برای یک منبع تحت نظر (watch) نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>object</code>&nbsp;<strong>*</strong><br/><em></em></td>
      <td>مقدار object به شرح زیر است: * اگر Type برابر Added یا Modified باشد: وضعیت جدید آبجکت. * اگر Type برابر Deleted باشد: وضعیت آبجکت بلافاصله پیش از حذف. * اگر Type برابر Error باشد: استفاده از *Status توصیه می‌شود؛ بسته به زمینه، انواع دیگر نیز می‌توانند مناسب باشند.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td></td>
    </tr>
  </tbody>
</table>

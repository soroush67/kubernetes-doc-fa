---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "LocalObjectReference"
content_type: "api_reference"
description: "LocalObjectReference اطلاعات کافی را در اختیار شما قرار می‌دهد تا بتوانید آبجکت ارجاع‌شده را در همان فضای نام (namespace) پیدا کنید."
title: "LocalObjectReference"
weight: 200
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


## LocalObjectReference {#LocalObjectReference}

LocalObjectReference اطلاعات کافی را برای پیدا کردن آبجکت ارجاع‌شده در همان فضای نام (namespace) فراهم می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام آبجکت ارجاع‌شده. این فیلد در عمل الزامی است، اما به‌دلیل سازگاری با نسخه‌های قبلی، مقدار خالی نیز برای آن پذیرفته می‌شود. نمونه‌هایی از این نوع که مقدار این فیلد در آن‌ها خالی باشد، تقریباً به‌طور قطع نادرست هستند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</td>
    </tr>
  </tbody>
</table>

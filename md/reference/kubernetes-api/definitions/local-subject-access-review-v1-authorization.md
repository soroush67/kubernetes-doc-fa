---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "LocalSubjectAccessReview"
content_type: "api_reference"
description: "LocalSubjectAccessReview بررسی می‌کند که آیا یک کاربر یا گروه می‌تواند عملی را در یک فضای نام (namespace) مشخص انجام دهد یا خیر. وجود یک منبع با دامنه فضای نام، اعطای سیاست‌هایی با دامنه فضای نام را که شامل بررسی مجوزها هستند، بسیار ساده‌تر می‌کند."
title: "LocalSubjectAccessReview"
weight: 210
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


## LocalSubjectAccessReview {#LocalSubjectAccessReview}

LocalSubjectAccessReview بررسی می‌کند که آیا یک کاربر یا گروه می‌تواند عملی را در یک فضای نام (namespace) مشخص انجام دهد یا خیر. وجود یک منبع با دامنه فضای نام، اعطای سیاست‌هایی با دامنه فضای نام را که شامل بررسی مجوزها هستند، بسیار ساده‌تر می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST را نشان می‌دهد که این آبجکت بیانگر آن است. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند، استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em>SubjectAccessReviewSpec</em></td>
      <td>spec اطلاعات مربوط به درخواستی را که در حال ارزیابی است نگه می‌دارد. مقدار spec.namespace باید با فضای نامی که درخواست را علیه آن ثبت کرده‌اید برابر باشد. اگر این مقدار خالی باشد، به‌صورت پیش‌فرض تنظیم می‌شود.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em>SubjectAccessReviewStatus</em></td>
      <td>status توسط سرور پر می‌شود و نشان می‌دهد که درخواست مجاز است یا خیر</td>
    </tr>
  </tbody>
</table>

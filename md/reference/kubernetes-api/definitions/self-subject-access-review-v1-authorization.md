---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "SelfSubjectAccessReview"
content_type: "api_reference"
description: "SelfSubjectAccessReview بررسی می‌کند که آیا کاربر فعلی می‌تواند یک عملیات را انجام دهد یا خیر. خالی گذاشتن spec.namespace به معنای «در همه فضاهای نام» است. حالت Self یک مورد خاص است، زیرا کاربران همواره باید بتوانند بررسی کنند که آیا اجازه انجام یک عملیات را دارند یا نه"
title: "SelfSubjectAccessReview"
weight: 450
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


## SelfSubjectAccessReview {#SelfSubjectAccessReview}

SelfSubjectAccessReview بررسی می‌کند که آیا کاربر فعلی می‌تواند یک عملیات را انجام دهد یا خیر. خالی گذاشتن spec.namespace به معنای «در همه فضاهای نام» است. حالت Self یک مورد خاص است، زیرا کاربران همواره باید بتوانند بررسی کنند که آیا اجازه انجام یک عملیات را دارند یا نه

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحواره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌های خود را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SelfSubjectAccessReviewSpec" >}}">SelfSubjectAccessReviewSpec</a></em></td>
      <td>spec اطلاعات مربوط به درخواستی را که ارزیابی می‌شود نگه می‌دارد. user و groups باید خالی باشند</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em>SubjectAccessReviewStatus</em></td>
      <td>status توسط سرور پر می‌شود و نشان می‌دهد که درخواست مجاز است یا خیر</td>
    </tr>
  </tbody>
</table>


## SelfSubjectAccessReviewSpec {#SelfSubjectAccessReviewSpec}

SelfSubjectAccessReviewSpec توصیف‌کننده درخواست دسترسی است. دقیقاً یکی از resourceAttributes و nonResourceAttributes باید مقداردهی شود

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>nonResourceAttributes</code><br/><em><a href="{{< ref "non-resource-attributes-v1-authorization#NonResourceAttributes" >}}">NonResourceAttributes</a></em></td>
      <td>nonResourceAttributes اطلاعات مربوط به یک درخواست دسترسی غیرمنبعی (non-resource) را توصیف می‌کند</td>
    </tr>
    <tr>
      <td><code>resourceAttributes</code><br/><em><a href="{{< ref "resource-attributes-v1-authorization#ResourceAttributes" >}}">ResourceAttributes</a></em></td>
      <td>resourceAttributes اطلاعات مربوط به یک درخواست دسترسی به منبع را توصیف می‌کند</td>
    </tr>
  </tbody>
</table>

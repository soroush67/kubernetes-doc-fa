---
api_metadata:
  apiVersion: "authentication.k8s.io/v1"
  import: "k8s.io/api/authentication/v1"
  kind: "SelfSubjectReview"
content_type: "api_reference"
description: "SelfSubjectReview اطلاعات کاربری را که kube-apiserver درباره‌ی کاربر ارسال‌کننده‌ی این درخواست در اختیار دارد، در بر می‌گیرد. هنگام استفاده از impersonation، کاربر اطلاعات کاربری را دریافت می‌کند که هویتش جعل‌شده (impersonate) است. اگر از impersonation یا احراز هویت با هدر درخواست استفاده شود، حروف بزرگ و کوچک کلیدهای extra نادیده گرفته می‌شود و این کلیدها با حروف کوچک بازگردانده می‌شوند."
title: "SelfSubjectReview"
weight: 460
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

`apiVersion: authentication.k8s.io/v1`

`import "k8s.io/api/authentication/v1"`


## SelfSubjectReview {#SelfSubjectReview}

SelfSubjectReview اطلاعات کاربری را که kube-apiserver درباره‌ی کاربر ارسال‌کننده‌ی این درخواست در اختیار دارد، در بر می‌گیرد. هنگام استفاده از impersonation، کاربر اطلاعات کاربری را دریافت می‌کند که هویتش جعل‌شده (impersonate) است. اگر از impersonation یا احراز هویت با هدر درخواست استفاده شود، حروف بزرگ و کوچک کلیدهای extra نادیده گرفته می‌شود و این کلیدها با حروف کوچک بازگردانده می‌شوند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره‌ی نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطه‌ی انتهایی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست. مقدار آن به قالب CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده‌ی استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#SelfSubjectReviewStatus" >}}">SelfSubjectReviewStatus</a></em></td>
      <td>status را سرور با ویژگی‌های کاربر پر می‌کند.</td>
    </tr>
  </tbody>
</table>


## SelfSubjectReviewStatus {#SelfSubjectReviewStatus}

SelfSubjectReviewStatus توسط kube-apiserver پر می‌شود و به کاربر بازگردانده می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>userInfo</code><br/><em><a href="{{< ref "user-info-v1-authentication#UserInfo" >}}">UserInfo</a></em></td>
      <td>userInfo مجموعه‌ای از ویژگی‌های متعلق به کاربری است که این درخواست را ارسال کرده است.</td>
    </tr>
  </tbody>
</table>

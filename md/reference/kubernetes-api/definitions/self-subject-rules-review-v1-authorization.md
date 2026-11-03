---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "SelfSubjectRulesReview"
content_type: "api_reference"
description: "SelfSubjectRulesReview مجموعه اقداماتی را که کاربر فعلی می‌تواند درون یک فضای نام (namespace) انجام دهد فهرست می‌کند. بسته به حالت احراز مجوز (authorization mode) سرور و خطاهایی که هنگام ارزیابی رخ می‌دهد، ممکن است فهرست اقدامات بازگردانده‌شده ناقص باشد. رابط‌های کاربری باید از SelfSubjectRulesReview برای نمایش یا پنهان کردن اقدامات یا برای آگاه کردن سریع کاربر نهایی از مجوزهایش استفاده کنند. سامانه‌های خارجی نباید از آن برای تصمیم‌گیری درباره مجوزدهی استفاده کنند، زیرا این کار مشکلاتی مانند confused deputy، طول عمر کش و ابطال مجوز، و نگرانی‌های مربوط به درستی ایجاد می‌کند. SubjectAccessReview و LocalAccessReview روش صحیح برای واگذاری تصمیم‌های مجوزدهی به سرور API هستند."
title: "SelfSubjectRulesReview"
weight: 470
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


## SelfSubjectRulesReview {#SelfSubjectRulesReview}

SelfSubjectRulesReview مجموعه اقداماتی را که کاربر فعلی می‌تواند درون یک فضای نام (namespace) انجام دهد فهرست می‌کند. بسته به حالت احراز مجوز (authorization mode) سرور و خطاهایی که هنگام ارزیابی رخ می‌دهد، ممکن است فهرست اقدامات بازگردانده‌شده ناقص باشد. رابط‌های کاربری باید از SelfSubjectRulesReview برای نمایش یا پنهان کردن اقدامات یا برای آگاه کردن سریع کاربر نهایی از مجوزهایش استفاده کنند. سامانه‌های خارجی نباید از آن برای تصمیم‌گیری درباره مجوزدهی استفاده کنند، زیرا این کار مشکلاتی مانند confused deputy، طول عمر کش و ابطال مجوز، و نگرانی‌های مربوط به درستی ایجاد می‌کند. SubjectAccessReview و LocalAccessReview روش صحیح برای واگذاری تصمیم‌های مجوزدهی به سرور API هستند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion نسخه‌دار بودن طرح‌واره (schema) این بازنمایی از یک آبجکت را مشخص می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را نشان می‌دهد. سرورها ممکن است آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این مقدار قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SelfSubjectRulesReviewSpec" >}}">SelfSubjectRulesReviewSpec</a></em></td>
      <td>spec اطلاعات مربوط به درخواستی را که ارزیابی می‌شود در خود نگه می‌دارد.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "subject-rules-review-status-v1-authorization#SubjectRulesReviewStatus" >}}">SubjectRulesReviewStatus</a></em></td>
      <td>status توسط سرور پر می‌شود و مجموعه اقداماتی را که کاربر می‌تواند انجام دهد نشان می‌دهد.</td>
    </tr>
  </tbody>
</table>


## SelfSubjectRulesReviewSpec {#SelfSubjectRulesReviewSpec}

SelfSubjectRulesReviewSpec مشخصات (specification) مربوط به SelfSubjectRulesReview را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>namespace فضای نامی است که قوانین برای آن ارزیابی می‌شوند. الزامی است.</td>
    </tr>
  </tbody>
</table>

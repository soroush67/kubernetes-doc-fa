---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "SubjectAccessReview"
content_type: "api_reference"
description: "SubjectAccessReview بررسی می‌کند که آیا یک کاربر یا گروه می‌تواند یک عمل را انجام دهد یا خیر."
title: "SubjectAccessReview"
weight: 550
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


## SubjectAccessReview {#SubjectAccessReview}

SubjectAccessReview بررسی می‌کند که آیا یک کاربر یا گروه می‌تواند یک عمل را انجام دهد یا خیر.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion نسخه‌ی طرحواره (schema) این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST مربوط به این آبجکت را نشان می‌دهد. سرورها می‌توانند آن را از نقطه‌ی انتهایی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این مقدار قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده‌ی استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SubjectAccessReviewSpec" >}}">SubjectAccessReviewSpec</a></em></td>
      <td>spec اطلاعاتی درباره‌ی درخواستی که در حال ارزیابی است نگه می‌دارد.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#SubjectAccessReviewStatus" >}}">SubjectAccessReviewStatus</a></em></td>
      <td>status توسط سرور مقداردهی می‌شود و نشان می‌دهد که درخواست مجاز است یا خیر.</td>
    </tr>
  </tbody>
</table>


## SubjectAccessReviewSpec {#SubjectAccessReviewSpec}

SubjectAccessReviewSpec توصیف یک درخواست دسترسی است. دقیقاً یکی از فیلدهای resourceAttributes و nonResourceAttributes باید تنظیم شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>extra</code><br/><em>object</em></td>
      <td>extra متناظر با متد user.Info.GetExtra() در احراز‌هویت‌کننده (authenticator) است. از آنجا که این مقدار ورودی مجازکننده (authorizer) است، باید در اینجا نیز بازتاب داده شود.</td>
    </tr>
    <tr>
      <td><code>groups</code><br/><em>string array</em></td>
      <td>groups گروه‌هایی است که برای آن‌ها بررسی انجام می‌دهید.</td>
    </tr>
    <tr>
      <td><code>nonResourceAttributes</code><br/><em><a href="{{< ref "non-resource-attributes-v1-authorization#NonResourceAttributes" >}}">NonResourceAttributes</a></em></td>
      <td>nonResourceAttributes اطلاعات مربوط به یک درخواست دسترسی غیرمنبعی (non-resource) را توصیف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceAttributes</code><br/><em><a href="{{< ref "resource-attributes-v1-authorization#ResourceAttributes" >}}">ResourceAttributes</a></em></td>
      <td>resourceAttributes اطلاعات مربوط به یک درخواست دسترسی به منبع را توصیف می‌کند.</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>uid اطلاعات مربوط به شناسه‌ی کاربر درخواست‌کننده است.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user کاربری است که برای آن بررسی انجام می‌دهید. اگر "User" را مشخص کنید اما "Groups" را مشخص نکنید، این حالت به‌صورت «اگر User عضو هیچ گروهی نبود چه می‌شد» تفسیر می‌شود.</td>
    </tr>
  </tbody>
</table>


## SubjectAccessReviewStatus {#SubjectAccessReviewStatus}

SubjectAccessReviewStatus

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowed</code>&nbsp;<strong>*</strong><br/><em>boolean</em></td>
      <td>allowed الزامی است. اگر عمل مجاز باشد مقدار آن true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>denied</code><br/><em>boolean</em></td>
      <td>denied اختیاری است. اگر عمل ممنوع باشد مقدار آن true و در غیر این صورت false است. اگر هر دو مقدار allowed و denied برابر false باشند، مجازکننده (authorizer) درباره‌ی مجاز بودن یا نبودن عمل نظری ندارد. اگر Allowed برابر true باشد، Denied نمی‌تواند true باشد.</td>
    </tr>
    <tr>
      <td><code>evaluationError</code><br/><em>string</em></td>
      <td>evaluationError نشان می‌دهد که در جریان بررسی مجوز خطایی رخ داده است. ممکن است با وجود چنین خطایی همچنان بتوان وضعیت مجوز را تعیین کرد. برای مثال، ممکن است در RBAC یک نقش (role) وجود نداشته باشد، اما نقش‌های کافی همچنان موجود و متصل (bound) باشند تا بتوان درباره‌ی درخواست تصمیم‌گیری کرد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>reason اختیاری است و نشان می‌دهد که چرا یک درخواست مجاز یا ممنوع شده است.</td>
    </tr>
  </tbody>
</table>

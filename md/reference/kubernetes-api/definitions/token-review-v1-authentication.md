---
api_metadata:
  apiVersion: "authentication.k8s.io/v1"
  import: "k8s.io/api/authentication/v1"
  kind: "TokenReview"
content_type: "api_reference"
description: "TokenReview تلاش می‌کند یک توکن را برای یک کاربر شناخته‌شده احراز هویت کند. توجه: درخواست‌های TokenReview ممکن است توسط افزونه webhook token authenticator در kube-apiserver در حافظهٔ نهان (cache) ذخیره شوند."
title: "TokenReview"
weight: 580
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


## TokenReview {#TokenReview}

TokenReview تلاش می‌کند یک توکن را برای یک کاربر شناخته‌شده احراز هویت کند. توجه: درخواست‌های TokenReview ممکن است توسط افزونه webhook token authenticator در kube-apiserver در حافظهٔ نهان ذخیره شوند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحوارهٔ نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را نشان می‌دهد. سرورها ممکن است آن را از نقطه دسترسی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>metadata فراداده استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#TokenReviewSpec" >}}">TokenReviewSpec</a></em></td>
      <td>spec اطلاعات مربوط به درخواستی را که در حال ارزیابی است نگه می‌دارد.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#TokenReviewStatus" >}}">TokenReviewStatus</a></em></td>
      <td>status توسط سرور پر می‌شود و نشان می‌دهد که آیا درخواست قابل احراز هویت است یا خیر.</td>
    </tr>
  </tbody>
</table>


## TokenReviewSpec {#TokenReviewSpec}

TokenReviewSpec توصیف درخواست احراز هویت توکن است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>audiences</code><br/><em>string array</em></td>
      <td>audiences فهرستی از شناسه‌هایی است که سرور منبع ارائه‌دهندهٔ توکن خود را با آن‌ها معرفی می‌کند. احراز هویت‌کننده‌های توکنِ آگاه از audience بررسی می‌کنند که توکن دست‌کم برای یکی از audienceهای این فهرست صادر شده باشد. اگر هیچ audience ای مشخص نشود، مقدار پیش‌فرض audience برابر با audience سرور API کوبرنتیز خواهد بود.</td>
    </tr>
    <tr>
      <td><code>token</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>token همان bearer token مبهم (opaque) است.</td>
    </tr>
  </tbody>
</table>


## TokenReviewStatus {#TokenReviewStatus}

TokenReviewStatus نتیجهٔ درخواست احراز هویت توکن است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>audiences</code><br/><em>string array</em></td>
      <td>audiences شناسه‌های audience هستند که احراز هویت‌کننده انتخاب کرده و با TokenReview و توکن هر دو سازگارند. شناسه، هر شناسه‌ای در اشتراک audienceهای TokenReviewSpec و audienceهای توکن است. کلاینتی از API مربوط به TokenReview که فیلد spec.audiences را تنظیم می‌کند، باید بررسی کند که یک شناسهٔ audience سازگار در فیلد status.audiences برگردانده شده باشد تا مطمئن شود سرور TokenReview از audience آگاه است. اگر TokenReview فیلد status.audience را خالی برگرداند و status.authenticated برابر "true" باشد، توکن نسبت به audience سرور API کوبرنتیز معتبر است.</td>
    </tr>
    <tr>
      <td><code>authenticated</code><br/><em>boolean</em></td>
      <td>authenticated نشان می‌دهد که توکن به یک کاربر شناخته‌شده مرتبط بوده است.</td>
    </tr>
    <tr>
      <td><code>error</code><br/><em>string</em></td>
      <td>error نشان می‌دهد که بررسی توکن امکان‌پذیر نبوده است.</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em><a href="{{< ref "user-info-v1-authentication#UserInfo" >}}">UserInfo</a></em></td>
      <td>user همان UserInfo مرتبط با توکن ارائه‌شده است.</td>
    </tr>
  </tbody>
</table>

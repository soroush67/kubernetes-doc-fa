---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "ParamRef"
content_type: "api_reference"
description: "ParamRef توضیح می‌دهد که پارامترهایی که به‌عنوان ورودی عبارت‌های قواعدِ اعمال‌شده توسط یک policy binding استفاده می‌شوند، چگونه پیدا شوند."
title: "ParamRef"
weight: 350
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

`apiVersion: admissionregistration.k8s.io/v1`

`import "k8s.io/api/admissionregistration/v1"`


## ParamRef {#ParamRef}

ParamRef توضیح می‌دهد که پارامترهایی که به‌عنوان ورودی عبارت‌های قواعدِ اعمال‌شده توسط یک policy binding استفاده می‌شوند، چگونه پیدا شوند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>name نام منبعی است که به آن ارجاع داده می‌شود. باید یکی از دو فیلد `name` یا `selector` تنظیم شود، اما این دو فیلد دو ویژگی ناسازگار با یکدیگر هستند؛ اگر یکی تنظیم شده باشد، دیگری باید تنظیم‌نشده باقی بماند. برای پیکربندی یک پارامتر واحد که برای همه درخواست‌های admission استفاده شود، می‌توان فیلد `name` را تنظیم کرد، فیلد `selector` را خالی گذاشت و در صورتی که `paramKind` در سطح namespace باشد، namespace را نیز تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>namespace فضای نامِ منبع ارجاع‌شده است. با این فیلد می‌توان جست‌وجوی پارامترها را به یک فضای نام مشخص محدود کرد. این فیلد هم برای فیلد `name` و هم برای فیلد `selector` اعمال می‌شود.  با تعیین یک `paramKind` با دامنه namespace در policy و خالی گذاشتن این فیلد، می‌توان برای هر فضای نام یک پارامتر جداگانه داشت.  - اگر `paramKind` در سطح کلاستر (cluster-scoped) باشد، این فیلد باید تنظیم‌نشده باشد. تنظیم این فیلد به خطای پیکربندی منجر می‌شود.  - اگر `paramKind` در سطح namespace باشد و این فیلد تنظیم نشده باشد، از فضای نامِ آبجکتی که برای admission ارزیابی می‌شود استفاده خواهد شد. توجه کنید که اگر این فیلد خالی بماند، binding نباید با هیچ منبع cluster-scoped مطابقت داشته باشد؛ در غیر این صورت خطا رخ می‌دهد.</td>
    </tr>
    <tr>
      <td><code>parameterNotFoundAction</code><br/><em>string</em></td>
      <td>parameterNotFoundAction رفتار binding را در حالتی تعیین می‌کند که منبع وجود دارد و `name` یا `selector` معتبر است، اما هیچ پارامتری با binding مطابقت ندارد. اگر مقدار آن `Allow` باشد، نبودِ پارامترِ منطبق توسط binding به‌عنوان اعتبارسنجی موفق در نظر گرفته می‌شود. اگر مقدار آن `Deny` باشد، نبودِ پارامترِ منطبق تابع `failurePolicy` مربوط به policy خواهد بود.  مقادیر مجاز `Allow` یا `Deny` هستند.  الزامی</td>
    </tr>
    <tr>
      <td><code>selector</code><br/><em><a href="{{< ref "label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>selector را می‌توان برای تطبیق چند آبجکت پارامتر بر اساس برچسب‌های آن‌ها به کار برد. برای تطبیق همه منابع از نوع ParamKind، مقدار selector: {} را تعیین کنید.  اگر چند پارامتر پیدا شود، همه آن‌ها با عبارت‌های policy ارزیابی می‌شوند و نتایج با عملگر AND با یکدیگر ترکیب می‌شوند.  باید یکی از دو فیلد `name` یا `selector` تنظیم شود، اما این دو فیلد دو ویژگی ناسازگار با یکدیگر هستند؛ اگر یکی تنظیم شده باشد، دیگری باید تنظیم‌نشده باقی بماند.</td>
    </tr>
  </tbody>
</table>

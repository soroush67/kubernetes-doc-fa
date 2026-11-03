---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "ResourceAttributes"
content_type: "api_reference"
description: "ResourceAttributes شامل ویژگی‌های مجوزدهی است که برای درخواست‌های مربوط به منابع، در رابط Authorizer در دسترس قرار دارند"
title: "ResourceAttributes"
weight: 400
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


## ResourceAttributes {#ResourceAttributes}

ResourceAttributes شامل ویژگی‌های مجوزدهی است که برای درخواست‌های مربوط به منابع، در رابط Authorizer در دسترس قرار دارند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fieldSelector</code><br/><em><a href="{{< ref "field-selector-attributes-v1-authorization#FieldSelectorAttributes" >}}">FieldSelectorAttributes</a></em></td>
      <td>fieldSelector محدودیت دسترسی را بر اساس فیلد توصیف می‌کند. این فیلد فقط می‌تواند دسترسی را محدود کند و نمی‌تواند آن را گسترش دهد.</td>
    </tr>
    <tr>
      <td><code>group</code><br/><em>string</em></td>
      <td>group گروه API (API Group) منبع است. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code><br/><em><a href="{{< ref "label-selector-attributes-v1-authorization#LabelSelectorAttributes" >}}">LabelSelectorAttributes</a></em></td>
      <td>labelSelector محدودیت دسترسی را بر اساس برچسب‌ها توصیف می‌کند. این فیلد فقط می‌تواند دسترسی را محدود کند و نمی‌تواند آن را گسترش دهد.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>name نام منبعی است که برای عملیات "get" درخواست شده یا برای عملیات "delete" حذف می‌شود. مقدار "" (خالی) به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>namespace فضای نام (namespace) عملیاتی است که درخواست شده است. در حال حاضر میان نبودن فضای نام و همه فضاهای نام تفاوتی وجود ندارد. مقدار "" (خالی) برای LocalSubjectAccessReviews به‌صورت پیش‌فرض تنظیم می‌شود. مقدار "" (خالی) برای منابع با دامنه کلاستر، خالی در نظر گرفته می‌شود. مقدار "" (خالی) برای منابع دارای دامنه فضای نام در SubjectAccessReview یا SelfSubjectAccessReview به معنای «همه» است.</td>
    </tr>
    <tr>
      <td><code>resource</code><br/><em>string</em></td>
      <td>resource یکی از انواع منابع موجود است. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>subresource</code><br/><em>string</em></td>
      <td>subresource یکی از انواع منابع موجود است. مقدار "" به معنای هیچ است.</td>
    </tr>
    <tr>
      <td><code>verb</code><br/><em>string</em></td>
      <td>verb یکی از فعل‌های API منابع کوبرنتیز است، مانند get، list، watch، create، update، delete و proxy. مقدار "*" به معنای همه است.</td>
    </tr>
    <tr>
      <td><code>version</code><br/><em>string</em></td>
      <td>version نسخه API (API Version) منبع است. مقدار "*" به معنای همه است.</td>
    </tr>
  </tbody>
</table>

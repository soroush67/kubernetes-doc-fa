---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "ManagedFieldsEntry"
content_type: "api_reference"
description: "ManagedFieldsEntry شامل یک workflow-id، یک FieldSet و نسخه گروه منبعی است که این fieldset برای آن اعمال می‌شود."
title: "ManagedFieldsEntry"
weight: 220
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


## ManagedFieldsEntry {#ManagedFieldsEntry}

ManagedFieldsEntry شامل یک workflow-id، یک FieldSet و نسخه گروه منبعی است که این fieldset برای آن اعمال می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion نسخه‌ای از این منبع را مشخص می‌کند که این field set برای آن اعمال می‌شود. قالب آن به‌صورت «group/version» است، درست مانند فیلد APIVersion در سطح بالای آبجکت. ردیابی نسخه یک field set ضروری است، زیرا این نسخه را نمی‌توان به‌طور خودکار تبدیل کرد.</td>
    </tr>
    <tr>
      <td><code>fieldsType</code><br/><em>string</em></td>
      <td>FieldsType تعیین‌کننده قالب و نسخه‌های مختلف فیلدهاست. در حال حاضر تنها یک مقدار ممکن وجود دارد: "FieldsV1"</td>
    </tr>
    <tr>
      <td><code>fieldsV1</code><br/><em><a href="{{< ref "fields-v1-v1-meta#FieldsV1" >}}">FieldsV1</a></em></td>
      <td>FieldsV1 قالب نخست JSON را نگه می‌دارد، همان‌گونه که در نوع "FieldsV1" توضیح داده شده است.</td>
    </tr>
    <tr>
      <td><code>manager</code><br/><em>string</em></td>
      <td>Manager شناسه‌ای برای گردش‌کاری (workflow) است که این فیلدها را مدیریت می‌کند.</td>
    </tr>
    <tr>
      <td><code>operation</code><br/><em>string</em></td>
      <td>Operation نوع عملیاتی است که باعث ایجاد این ManagedFieldsEntry شده است. تنها مقادیر معتبر برای این فیلد 'Apply' و 'Update' هستند.</td>
    </tr>
    <tr>
      <td><code>subresource</code><br/><em>string</em></td>
      <td>Subresource نام زیرمنبعی است که برای به‌روزرسانی آن آبجکت استفاده شده است، یا اگر آبجکت از طریق منبع اصلی به‌روزرسانی شده باشد، رشته خالی است. از مقدار این فیلد برای تمایز میان managerها استفاده می‌شود، حتی اگر نام یکسانی داشته باشند. برای مثال، به‌روزرسانی status با یک به‌روزرسانی معمولی که از همان نام manager استفاده می‌کند متمایز است. توجه کنید که فیلد APIVersion به فیلد Subresource مربوط نیست و همیشه با نسخه منبع اصلی مطابقت دارد.</td>
    </tr>
    <tr>
      <td><code>time</code><br/><em><a href="{{< ref "time-v1-meta#Time" >}}">Time</a></em></td>
      <td>Time زمان افزوده شدن ورودی ManagedFields است. این زمان همچنین هنگامی به‌روز می‌شود که فیلدی اضافه شود، manager مقدار هر یک از فیلدهای تحت مالکیت خود را تغییر دهد یا فیلدی را حذف کند. اگر فیلدی از ورودی حذف شود، چون manager دیگری مالکیت آن را به دست گرفته است، این زمان به‌روز نمی‌شود.</td>
    </tr>
  </tbody>
</table>

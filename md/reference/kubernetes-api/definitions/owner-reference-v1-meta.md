---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "OwnerReference"
content_type: "api_reference"
description: "OwnerReference شامل اطلاعات کافی برای شناسایی یک آبجکت مالک است. آبجکت مالک باید در همان فضای نام (namespace) آبجکت وابسته قرار داشته باشد یا در سطح کلاستر تعریف شده باشد؛ به همین دلیل فیلد namespace وجود ندارد."
title: "OwnerReference"
weight: 330
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


## OwnerReference {#OwnerReference}

OwnerReference شامل اطلاعات کافی برای شناسایی یک آبجکت مالک است. آبجکت مالک باید در همان فضای نام (namespace) آبجکت وابسته قرار داشته باشد یا در سطح کلاستر تعریف شده باشد؛ به همین دلیل فیلد namespace وجود ندارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نسخه API آبجکت مرجع (referent).</td>
    </tr>
    <tr>
      <td><code>blockOwnerDeletion</code><br/><em>boolean</em></td>
      <td>اگر مقدار این فیلد true باشد و مالک نیز finalizer با نام «foregroundDeletion» را داشته باشد، تا زمانی که این ارجاع حذف نشده است، مالک را نمی‌توان از ذخیره‌ساز کلید-مقدار (key-value store) حذف کرد. برای آگاهی از نحوه تعامل garbage collector با این فیلد و اعمال حذف پیش‌زمینه (foreground deletion)، به https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion مراجعه کنید. مقدار پیش‌فرض false است. برای تنظیم این فیلد، کاربر باید مجوز «delete» را روی مالک داشته باشد؛ در غیر این صورت خطای 422 (Unprocessable Entity) بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>controller</code><br/><em>boolean</em></td>
      <td>اگر مقدار این فیلد true باشد، این ارجاع به کنترل‌کننده مدیریت‌کننده اشاره می‌کند.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع (Kind) آبجکت مرجع. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام آبجکت مرجع. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names</td>
    </tr>
    <tr>
      <td><code>uid</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>شناسه یکتای (UID) آبجکت مرجع. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids</td>
    </tr>
  </tbody>
</table>

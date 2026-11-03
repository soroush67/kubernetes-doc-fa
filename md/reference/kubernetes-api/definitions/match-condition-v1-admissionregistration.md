---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "MatchCondition"
content_type: "api_reference"
description: "MatchCondition شرطی را نشان می‌دهد که برای ارسال یک درخواست به webhook باید برقرار باشد."
title: "MatchCondition"
weight: 230
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


## MatchCondition {#MatchCondition}

MatchCondition شرطی را نشان می‌دهد که برای ارسال یک درخواست به webhook باید برقرار باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>expression عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند. نتیجهٔ ارزیابی باید از نوع bool باشد. عبارت‌های CEL به محتوای AdmissionRequest و Authorizer دسترسی دارند که در قالب متغیرهای CEL زیر سازمان‌دهی شده‌اند:  'object' - آبجکت موجود در درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است. 'oldObject' - آبجکت موجود فعلی. مقدار آن برای درخواست‌های CREATE برابر null است. 'request' - ویژگی‌های درخواست admission (/pkg/apis/admission/types.go#AdmissionRequest). 'authorizer' - یک CEL Authorizer. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای principal (کاربر یا service account) مربوط به درخواست استفاده کرد.   به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید. 'authorizer.requestResource' - یک CEL ResourceCheck که از 'authorizer' ساخته شده و با منبع درخواست پیکربندی شده است. مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/  الزامی است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name شناسهٔ این شرط تطبیق است و برای strategic merge کردن MatchConditionها و همچنین به‌عنوان شناسه برای مقاصد ثبت لاگ استفاده می‌شود. نام مناسب باید توصیف‌کنندهٔ عبارت مرتبط با آن باشد. name باید یک qualified name متشکل از نویسه‌های الفبایی-عددی، '-'، '_' یا '.' باشد و با یک نویسهٔ الفبایی-عددی شروع و به آن ختم شود (برای مثال 'MyName' یا 'my.name' یا '123-abc'؛ عبارت باقاعدهٔ مورد استفاده برای اعتبارسنجی '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]' است). همچنین می‌تواند یک پیشوند اختیاری به‌صورت DNS subdomain و '/' داشته باشد (برای مثال 'example.com/MyName').  الزامی است.</td>
    </tr>
  </tbody>
</table>

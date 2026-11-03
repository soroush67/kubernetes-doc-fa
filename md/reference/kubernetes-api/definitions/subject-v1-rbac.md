---
api_metadata:
  apiVersion: "rbac.authorization.k8s.io/v1"
  import: "k8s.io/api/rbac/v1"
  kind: "Subject"
content_type: "api_reference"
description: "Subject به هویت‌های آبجکت یا کاربر ارجاع می‌دهد که یک role binding برای آن‌ها اعمال می‌شود. این مقدار می‌تواند یا یک ارجاع مستقیم به آبجکت API باشد، یا مقداری برای موجودیت‌های غیرآبجکتی مانند نام کاربر و گروه."
title: "Subject"
weight: 540
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

`apiVersion: rbac.authorization.k8s.io/v1`

`import "k8s.io/api/rbac/v1"`


## Subject {#Subject}

Subject به هویت‌های آبجکت یا کاربر ارجاع می‌دهد که یک role binding برای آن‌ها اعمال می‌شود. این مقدار می‌تواند یا یک ارجاع مستقیم به آبجکت API باشد، یا مقداری برای موجودیت‌های غیرآبجکتی مانند نام کاربر و گروه.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>apiGroup گروه API مربوط به subject مورد ارجاع را نگه می‌دارد. برای subjectهای از نوع ServiceAccount مقدار پیش‌فرض "" است و برای subjectهای از نوع User و Group مقدار پیش‌فرض "rbac.authorization.k8s.io" است.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>kind نوع آبجکتی است که به آن ارجاع داده می‌شود. مقادیری که این گروه API تعریف می‌کند عبارت‌اند از "User"، "Group" و "ServiceAccount". اگر Authorizer مقدار kind را نشناسد، باید یک خطا گزارش کند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام آبجکتی است که به آن ارجاع داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>namespace فضای نام آبجکت مورد ارجاع است. اگر kind آبجکت فاقد فضای نام باشد، مانند "User" یا "Group"، و این مقدار خالی نباشد، Authorizer باید یک خطا گزارش کند.</td>
    </tr>
  </tbody>
</table>

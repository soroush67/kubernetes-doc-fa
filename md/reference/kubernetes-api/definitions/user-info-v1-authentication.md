---
api_metadata:
  apiVersion: "authentication.k8s.io/v1"
  import: "k8s.io/api/authentication/v1"
  kind: "UserInfo"
content_type: "api_reference"
description: "UserInfo اطلاعات مربوط به کاربر را که برای پیاده‌سازی رابط user.Info لازم است نگهداری می‌کند."
title: "UserInfo"
weight: 620
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


## UserInfo {#UserInfo}

آبجکت UserInfo اطلاعات مربوط به کاربر را که برای پیاده‌سازی رابط user.Info لازم است نگهداری می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>extra</code><br/><em>object</em></td>
      <td>فیلد extra هرگونه اطلاعات اضافی را که احرازکننده هویت (authenticator) ارائه کرده است شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>groups</code><br/><em>string array</em></td>
      <td>فیلد groups فهرست نام گروه‌هایی است که این کاربر عضو آن‌هاست.</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>فیلد uid مقداری یکتا است که این کاربر را در طول زمان شناسایی می‌کند. اگر این کاربر حذف شود و کاربر دیگری با همین نام اضافه شود، آن دو UID متفاوتی خواهند داشت.</td>
    </tr>
    <tr>
      <td><code>username</code><br/><em>string</em></td>
      <td>فیلد username نامی است که این کاربر را در میان همه کاربران فعال به‌طور یکتا شناسایی می‌کند.</td>
    </tr>
  </tbody>
</table>

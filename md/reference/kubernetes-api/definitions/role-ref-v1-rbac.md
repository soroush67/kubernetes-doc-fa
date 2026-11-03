---
api_metadata:
  apiVersion: "rbac.authorization.k8s.io/v1"
  import: "k8s.io/api/rbac/v1"
  kind: "RoleRef"
content_type: "api_reference"
description: "RoleRef شامل اطلاعاتی است که به نقش (role) مورد استفاده اشاره می‌کند"
title: "RoleRef"
weight: 420
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


## RoleRef {#RoleRef}

RoleRef شامل اطلاعاتی است که به نقش (role) مورد استفاده اشاره می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>apiGroup گروه منبعی است که به آن ارجاع داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>kind نوع منبعی است که به آن ارجاع داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>name نام منبعی است که به آن ارجاع داده می‌شود.</td>
    </tr>
  </tbody>
</table>

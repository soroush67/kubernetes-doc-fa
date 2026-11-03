---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "ServerAddressByClientCIDR"
content_type: "api_reference"
description: "ServerAddressByClientCIDR به کلاینت کمک می‌کند تا بر اساس clientCIDR منطبق با خود، آدرس سروری را که باید استفاده کند تعیین نماید."
title: "ServerAddressByClientCIDR"
weight: 480
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


## ServerAddressByClientCIDR {#ServerAddressByClientCIDR}

ServerAddressByClientCIDR به کلاینت کمک می‌کند تا بر اساس clientCIDR منطبق با خود، آدرس سروری را که باید استفاده کند تعیین نماید.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>clientCIDR</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>محدوده CIDR ای که کلاینت‌ها می‌توانند IP خود را با آن مطابقت دهند تا آدرس سروری را که باید استفاده کنند تشخیص دهند.</td>
    </tr>
    <tr>
      <td><code>serverAddress</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>آدرس این سرور که برای کلاینتی مناسب است که با CIDR بالا مطابقت دارد. این مقدار می‌تواند hostname، hostname:port، IP یا IP:port باشد.</td>
    </tr>
  </tbody>
</table>

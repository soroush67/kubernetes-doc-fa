---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "RuleWithOperations"
content_type: "api_reference"
description: "RuleWithOperations یک چندتایی (tuple) از عملیات‌ها و منابع است. توصیه می‌شود اطمینان حاصل شود که تمام بسط‌های این چندتایی معتبر هستند."
title: "RuleWithOperations"
weight: 430
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


## RuleWithOperations {#RuleWithOperations}

RuleWithOperations یک چندتایی (tuple) از عملیات‌ها و منابع است. توصیه می‌شود اطمینان حاصل شود که تمام بسط‌های این چندتایی معتبر هستند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroups</code><br/><em>string array</em></td>
      <td>apiGroups گروه‌های API است که منابع به آن‌ها تعلق دارند. '\*' به معنای همه گروه‌هاست. اگر '\*' وجود داشته باشد، طول slice باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>apiVersions</code><br/><em>string array</em></td>
      <td>apiVersions نسخه‌های API است که منابع به آن‌ها تعلق دارند. '\*' به معنای همه نسخه‌هاست. اگر '\*' وجود داشته باشد، طول slice باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>operations</code><br/><em>string array</em></td>
      <td>operations عملیات‌هایی است که admission hook به آن‌ها توجه دارد: CREATE، UPDATE، DELETE، CONNECT یا * برای همه این عملیات‌ها و هر عملیات admission دیگری که در آینده اضافه شود. اگر '\*' وجود داشته باشد، طول slice باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em>string array</em></td>
      <td>resources فهرستی از منابع است که این قانون برای آن‌ها اعمال می‌شود. برای مثال: 'pods' به معنای Podها است. 'pods/log' به معنای زیرمنبع log مربوط به Podها است. '\*' به معنای همه منابع است، اما شامل زیرمنبع‌ها نمی‌شود. 'pods/\*' به معنای همه زیرمنبع‌های Podها است. '\*/scale' به معنای همه زیرمنبع‌های scale است. '\*/\*' به معنای همه منابع و زیرمنبع‌های آن‌هاست. اگر wildcard وجود داشته باشد، قانون اعتبارسنجی اطمینان حاصل می‌کند که منابع با یکدیگر همپوشانی نداشته باشند. بسته به آبجکت دربرگیرنده، ممکن است استفاده از زیرمنبع‌ها مجاز نباشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>scope</code><br/><em>string</em></td>
      <td>scope دامنه این قانون را مشخص می‌کند. مقادیر معتبر "Cluster"، "Namespaced" و "*" هستند. "Cluster" به این معناست که فقط منابع با دامنه کلاستر با این قانون مطابقت پیدا می‌کنند. آبجکت‌های API از نوع Namespace دارای دامنه کلاستر هستند. "Namespaced" به این معناست که فقط منابعی که به یک فضای نام (namespace) تعلق دارند با این قانون مطابقت پیدا می‌کنند. "*" به این معناست که هیچ محدودیتی در دامنه وجود ندارد. زیرمنبع‌ها از دامنه منبع والد خود پیروی می‌کنند. مقدار پیش‌فرض "*" است.<br/><br/>مقادیر enum ممکن:<br/> - `"*"` به این معناست که همه دامنه‌ها شامل می‌شوند.<br/> - `"Cluster"` به این معناست که دامنه به آبجکت‌های با دامنه کلاستر محدود است. آبجکت‌های Namespace دارای دامنه کلاستر هستند.<br/> - `"Namespaced"` به این معناست که دامنه به آبجکت‌هایی محدود است که به یک فضای نام تعلق دارند.</td>
    </tr>
  </tbody>
</table>

---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "NamedRuleWithOperations"
content_type: "api_reference"
description: "NamedRuleWithOperations چندتایه‌ای از Operations و Resources همراه با ResourceNames است."
title: "NamedRuleWithOperations"
weight: 260
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


## NamedRuleWithOperations {#NamedRuleWithOperations}

NamedRuleWithOperations چندتایه‌ای از Operations و Resources همراه با ResourceNames است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroups</code><br/><em>string array</em></td>
      <td>apiGroups فهرست گروه‌های API است که منابع به آن‌ها تعلق دارند. مقدار '\*' به معنای همه گروه‌هاست. اگر '\*' وجود داشته باشد، طول فهرست باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>apiVersions</code><br/><em>string array</em></td>
      <td>apiVersions فهرست نسخه‌های API است که منابع به آن‌ها تعلق دارند. مقدار '\*' به معنای همه نسخه‌هاست. اگر '\*' وجود داشته باشد، طول فهرست باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>operations</code><br/><em>string array</em></td>
      <td>operations فهرست عملیاتی است که admission hook به آن‌ها توجه دارد: CREATE، UPDATE، DELETE، CONNECT، یا * برای همه این عملیات و هر عملیات admission دیگری که در آینده افزوده شود. اگر '\*' وجود داشته باشد، طول فهرست باید یک باشد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>resourceNames</code><br/><em>string array</em></td>
      <td>resourceNames فهرست سفید اختیاری از نام‌هایی است که قاعده بر آن‌ها اعمال می‌شود. مجموعه خالی به این معناست که همه موارد مجاز هستند.</td>
    </tr>
    <tr>
      <td><code>resources</code><br/><em>string array</em></td>
      <td>resources فهرستی از منابع است که این قاعده بر آن‌ها اعمال می‌شود. برای مثال: 'pods' به معنای podها، 'pods/log' به معنای زیرمنبع log از podها، '\*' به معنای همه منابع (بدون زیرمنابع)، 'pods/\*' به معنای همه زیرمنابع podها، '\*/scale' به معنای همه زیرمنابع scale و '\*/\*' به معنای همه منابع و زیرمنابع آن‌هاست. اگر از wildcard استفاده شده باشد، اعتبارسنجی قاعده اطمینان حاصل می‌کند که منابع با یکدیگر همپوشانی نداشته باشند. بسته به آبجکت دربرگیرنده، ممکن است زیرمنابع مجاز نباشند. الزامی است.</td>
    </tr>
    <tr>
      <td><code>scope</code><br/><em>string</em></td>
      <td>scope دامنه این قاعده را مشخص می‌کند. مقادیر معتبر "Cluster"، "Namespaced" و "*" هستند. مقدار "Cluster" یعنی فقط منابع با دامنه کلاستر با این قاعده تطبیق پیدا می‌کنند؛ آبجکت‌های API از نوع Namespace نیز دامنه کلاستری دارند. مقدار "Namespaced" یعنی فقط منابع دارای فضای نام (namespace) با این قاعده تطبیق پیدا می‌کنند. مقدار "*" یعنی هیچ محدودیتی برای دامنه وجود ندارد. زیرمنابع با دامنه منبع والد خود تطبیق پیدا می‌کنند. مقدار پیش‌فرض "*" است.<br/><br/>Possible enum values:<br/> - `"*"` به معنای آن است که همه دامنه‌ها شامل می‌شوند.<br/> - `"Cluster"` به معنای آن است که دامنه به آبجکت‌های با دامنه کلاستر محدود است. آبجکت‌های Namespace دامنه کلاستری دارند.<br/> - `"Namespaced"` به معنای آن است که دامنه به آبجکت‌های دارای فضای نام محدود است.</td>
    </tr>
  </tbody>
</table>

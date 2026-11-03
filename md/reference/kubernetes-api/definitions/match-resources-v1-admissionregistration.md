---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "MatchResources"
content_type: "api_reference"
description: "MatchResources تعیین می‌کند که سیاست کنترل پذیرش (admission control) بر اساس برآورده شدن معیارهای تطبیق، روی یک آبجکت اجرا شود یا خیر. قواعد exclude بر قواعد include اولویت دارند (اگر یک منبع با هر دو تطبیق پیدا کند، مستثنی می‌شود)"
title: "MatchResources"
weight: 240
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


## MatchResources {#MatchResources}

MatchResources تعیین می‌کند که سیاست کنترل پذیرش (admission control) بر اساس برآورده شدن معیارهای تطبیق، روی یک آبجکت اجرا شود یا خیر. قواعد exclude بر قواعد include اولویت دارند (اگر یک منبع با هر دو تطبیق پیدا کند، مستثنی می‌شود)

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>excludeResourceRules</code><br/><em><a href="{{< ref "named-rule-with-operations-v1-admissionregistration#NamedRuleWithOperations" >}}">NamedRuleWithOperations array</a></em></td>
      <td>excludeResourceRules مشخص می‌کند ValidatingAdmissionPolicy نباید به کدام عملیات روی کدام منابع/زیرمنابع (subresource) توجه کند. قواعد exclude بر قواعد include اولویت دارند (اگر یک منبع با هر دو تطبیق پیدا کند، مستثنی می‌شود)</td>
    </tr>
    <tr>
      <td><code>matchPolicy</code><br/><em>string</em></td>
      <td>matchPolicy تعیین می‌کند فهرست "MatchResources" چگونه برای تطبیق با درخواست‌های ورودی استفاده شود. مقادیر مجاز "Exact" یا "Equivalent" هستند.  - Exact: درخواست فقط در صورتی تطبیق داده می‌شود که دقیقاً با یکی از قواعد مشخص‌شده مطابقت داشته باشد. برای مثال، اگر deploymentها از طریق apps/v1، apps/v1beta1 و extensions/v1beta1 قابل تغییر باشند، اما "rules" فقط شامل `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` باشد، درخواستی که به apps/v1beta1 یا extensions/v1beta1 ارسال شود به ValidatingAdmissionPolicy فرستاده نمی‌شود.  - Equivalent: درخواست در صورتی تطبیق داده می‌شود که منبعی را تغییر دهد که در rules آمده است، حتی اگر این تغییر از طریق یک API group یا نسخه دیگر انجام شود. برای مثال، اگر deploymentها از طریق apps/v1، apps/v1beta1 و extensions/v1beta1 قابل تغییر باشند و "rules" فقط شامل `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` باشد، درخواستی که به apps/v1beta1 یا extensions/v1beta1 ارسال شود به apps/v1 تبدیل و به ValidatingAdmissionPolicy فرستاده می‌شود.  مقدار پیش‌فرض "Equivalent" است.<br/><br/>Possible enum values:<br/> - `"Equivalent"` یعنی اگر درخواستی منبعی را که در rules آمده است از طریق API group یا نسخه دیگری تغییر دهد، باید به webhook ارسال شود.<br/> - `"Exact"` یعنی درخواست‌ها فقط در صورتی باید به webhook ارسال شوند که دقیقاً با یک قاعده مشخص‌شده مطابقت داشته باشند.</td>
    </tr>
    <tr>
      <td><code>namespaceSelector</code><br/><em><a href="{{< ref "label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>namespaceSelector تعیین می‌کند که سیاست کنترل پذیرش بر اساس تطابق فضای نام (namespace) آبجکت با انتخابگر (selector)، روی آن آبجکت اجرا شود یا خیر. اگر خود آبجکت یک namespace باشد، تطبیق روی object.metadata.labels انجام می‌شود. اگر آبجکت یک منبع دیگر با دامنه کلاستر باشد، سیاست هرگز برای آن نادیده گرفته نمی‌شود.  برای مثال، برای اجرای webhook روی همه آبجکت‌هایی که فضای نام آن‌ها با "runlevel" برابر "0" یا "1" مرتبط نیست، انتخابگر را به این صورت تنظیم می‌کنید: "namespaceSelector": {   "matchExpressions": [     {       "key": "runlevel",       "operator": "NotIn",       "values": [         "0",         "1"       ]     }   ] }  اگر در عوض می‌خواهید سیاست را فقط روی آبجکت‌هایی اجرا کنید که فضای نام آن‌ها با "environment" برابر "prod" یا "staging" مرتبط است، انتخابگر را به این صورت تنظیم می‌کنید: "namespaceSelector": {   "matchExpressions": [     {       "key": "environment",       "operator": "In",       "values": [         "prod",         "staging"       ]     }   ] }  برای مثال‌های بیشتر از انتخابگرهای برچسب به https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ مراجعه کنید.  مقدار پیش‌فرض LabelSelector خالی است که با همه‌چیز تطبیق پیدا می‌کند.</td>
    </tr>
    <tr>
      <td><code>objectSelector</code><br/><em><a href="{{< ref "label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>objectSelector تعیین می‌کند که اعتبارسنجی بر اساس داشتن برچسب‌های منطبق در آبجکت اجرا شود یا خیر. objectSelector هم روی oldObject و هم روی newObject که به اعتبارسنجی cel ارسال می‌شوند ارزیابی می‌شود و اگر هر یک از این دو آبجکت با انتخابگر تطبیق داشته باشد، تطبیق یافته در نظر گرفته می‌شود. آبجکت null (oldObject در حالت create یا newObject در حالت delete) یا آبجکتی که نمی‌تواند برچسب داشته باشد (مانند آبجکت DeploymentRollback یا PodProxyOptions) تطبیق یافته در نظر گرفته نمی‌شود. از انتخابگر آبجکت فقط زمانی استفاده کنید که webhook به‌صورت opt-in عمل می‌کند، زیرا کاربران نهایی می‌توانند با تنظیم برچسب‌ها از admission webhook عبور کنند. مقدار پیش‌فرض LabelSelector خالی است که با همه‌چیز تطبیق پیدا می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceRules</code><br/><em><a href="{{< ref "named-rule-with-operations-v1-admissionregistration#NamedRuleWithOperations" >}}">NamedRuleWithOperations array</a></em></td>
      <td>resourceRules مشخص می‌کند ValidatingAdmissionPolicy با کدام عملیات روی کدام منابع/زیرمنابع (subresource) تطبیق پیدا می‌کند. اگر یک عملیات با _هر_ Rule تطبیق داشته باشد، سیاست به آن توجه می‌کند.</td>
    </tr>
  </tbody>
</table>

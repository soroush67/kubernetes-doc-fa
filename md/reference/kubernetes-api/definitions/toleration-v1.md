---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "Toleration"
content_type: "api_reference"
description: "Pod ای که این Toleration به آن متصل است، هر taint را که با سه‌تایی &lt;key,value,effect&gt; و با عملگر تطبیق &lt;operator&gt; مطابقت داشته باشد تحمل می‌کند."
title: "Toleration"
weight: 590
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## Toleration {#Toleration}

Pod ای که این Toleration به آن متصل است، هر taint را که با سه‌تایی &lt;key,value,effect&gt; و با عملگر تطبیق &lt;operator&gt; مطابقت داشته باشد تحمل می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>effect</code><br/><em>string</em></td>
      <td>effect نشان می‌دهد که با کدام اثر taint باید تطبیق انجام شود. مقدار خالی به معنای تطبیق با همه اثرهای taint است. در صورت مشخص شدن، مقادیر مجاز NoSchedule، PreferNoSchedule و NoExecute هستند.<br/><br/>مقادیر enum ممکن:<br/> - `"NoExecute"` هر Pod در حال اجرا را که taint را تحمل نمی‌کند، بیرون می‌راند (evict). در حال حاضر توسط NodeController اعمال می‌شود.<br/> - `"NoSchedule"` مانع از زمان‌بندی Podهای جدید روی نود می‌شود، مگر اینکه taint را تحمل کنند؛ اما اجازه می‌دهد همه Podهایی که بدون عبور از زمان‌بند به Kubelet ارسال شده‌اند شروع به کار کنند و همه Podهای در حال اجرا به کار خود ادامه دهند. توسط زمان‌بند اعمال می‌شود.<br/> - `"PreferNoSchedule"` مشابه TaintEffectNoSchedule است، با این تفاوت که زمان‌بند تلاش می‌کند Podهای جدید را روی نود زمان‌بندی نکند، اما زمان‌بندی Podهای جدید روی نود را به‌طور کامل ممنوع نمی‌کند. توسط زمان‌بند اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>key</code><br/><em>string</em></td>
      <td>key کلید taint است که toleration برای آن اعمال می‌شود. مقدار خالی به معنای تطبیق با همه کلیدهای taint است. اگر key خالی باشد، operator باید Exists باشد؛ این ترکیب به معنای تطبیق با همه مقادیر و همه کلیدهاست.</td>
    </tr>
    <tr>
      <td><code>operator</code><br/><em>string</em></td>
      <td>operator رابطه یک کلید با مقدار را مشخص می‌کند. عملگرهای معتبر Exists، Equal، Lt و Gt هستند. مقدار پیش‌فرض Equal است. Exists معادل علامت عام (wildcard) برای value است، به‌طوری که یک Pod می‌تواند همه taintهای یک دسته مشخص را تحمل کند. Lt و Gt مقایسه عددی انجام می‌دهند (به feature gate با نام TaintTolerationComparisonOperators نیاز دارند).<br/><br/>مقادیر enum ممکن:<br/> - `"Equal"`<br/> - `"Exists"`<br/> - `"Gt"`<br/> - `"Lt"`</td>
    </tr>
    <tr>
      <td><code>tolerationSeconds</code><br/><em>integer</em></td>
      <td>tolerationSeconds مدت زمانی را نشان می‌دهد که toleration (که اثر آن باید NoExecute باشد، در غیر این صورت این فیلد نادیده گرفته می‌شود) taint را تحمل می‌کند. به‌طور پیش‌فرض این فیلد تنظیم نشده است، یعنی taint برای همیشه تحمل می‌شود (Pod بیرون رانده نمی‌شود). سامانه مقادیر صفر و منفی را برابر 0 در نظر می‌گیرد (بیرون راندن فوری).</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em>string</em></td>
      <td>value مقدار taint است که toleration با آن تطبیق داده می‌شود. اگر operator برابر Exists باشد، value باید خالی باشد؛ در غیر این صورت یک رشته معمولی است.</td>
    </tr>
  </tbody>
</table>

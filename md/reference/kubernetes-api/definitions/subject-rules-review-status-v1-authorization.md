---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "SubjectRulesReviewStatus"
content_type: "api_reference"
description: "SubjectRulesReviewStatus نتیجه‌ی بررسی قوانین را در بر دارد. بسته به مجموعه‌ی authorizerهایی که سرور با آن‌ها پیکربندی شده و خطاهایی که هنگام ارزیابی رخ می‌دهد، این بررسی ممکن است ناقص باشد. از آنجا که قوانین مجوزدهی جنبه‌ی افزایشی دارند، اگر قانونی در یک فهرست وجود داشته باشد، می‌توان با اطمینان فرض کرد که سوژه آن مجوز را دارد، حتی اگر آن فهرست ناقص باشد."
title: "SubjectRulesReviewStatus"
weight: 560
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

`apiVersion: authorization.k8s.io/v1`

`import "k8s.io/api/authorization/v1"`


## SubjectRulesReviewStatus {#SubjectRulesReviewStatus}

SubjectRulesReviewStatus نتیجه‌ی بررسی قوانین را در بر دارد. بسته به مجموعه‌ی authorizerهایی که سرور با آن‌ها پیکربندی شده و خطاهایی که هنگام ارزیابی رخ می‌دهد، این بررسی ممکن است ناقص باشد. از آنجا که قوانین مجوزدهی جنبه‌ی افزایشی دارند، اگر قانونی در یک فهرست وجود داشته باشد، می‌توان با اطمینان فرض کرد که سوژه آن مجوز را دارد، حتی اگر آن فهرست ناقص باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>evaluationError</code><br/><em>string</em></td>
      <td>evaluationError می‌تواند همراه با Rules ظاهر شود. این فیلد نشان می‌دهد که هنگام ارزیابی قوانین خطایی رخ داده است (برای مثال وجود یک authorizer که از ارزیابی قوانین پشتیبانی نمی‌کند) و ممکن است ResourceRules و/یا NonResourceRules ناقص باشند.</td>
    </tr>
    <tr>
      <td><code>incomplete</code>&nbsp;<strong>*</strong><br/><em>boolean</em></td>
      <td>اگر قوانین بازگردانده‌شده در این فراخوانی ناقص باشند، مقدار incomplete برابر true است. این وضعیت بیشتر زمانی پیش می‌آید که یک authorizer، مانند یک authorizer خارجی، از ارزیابی قوانین پشتیبانی نکند.</td>
    </tr>
    <tr>
      <td><code>nonResourceRules</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "non-resource-rule-v1-authorization#NonResourceRule" >}}">آرایه‌ی NonResourceRule</a></em></td>
      <td>nonResourceRules فهرست اقدام‌هایی است که سوژه مجاز است روی منابع غیرمنبعی (non-resource) انجام دهد. ترتیب فهرست اهمیتی ندارد، ممکن است شامل موارد تکراری باشد و احتمالاً ناقص است.</td>
    </tr>
    <tr>
      <td><code>resourceRules</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "resource-rule-v1-authorization#ResourceRule" >}}">آرایه‌ی ResourceRule</a></em></td>
      <td>resourceRules فهرست اقدام‌هایی است که سوژه مجاز است روی منابع انجام دهد. ترتیب فهرست اهمیتی ندارد، ممکن است شامل موارد تکراری باشد و احتمالاً ناقص است.</td>
    </tr>
  </tbody>
</table>

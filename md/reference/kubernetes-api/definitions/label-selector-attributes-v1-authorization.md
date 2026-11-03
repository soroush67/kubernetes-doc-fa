---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "LabelSelectorAttributes"
content_type: "api_reference"
description: "LabelSelectorAttributes دسترسیِ محدودشده با برچسب را مشخص می‌کند. به نویسندگان webhook توصیه می‌شود: * مطمئن شوند rawSelector و requirements هر دو هم‌زمان تنظیم نشده باشند؛ * در صورت تنظیم‌بودن فیلد requirements، آن را در نظر بگیرند؛ * در صورت تنظیم‌بودن فیلد rawSelector، تلاش نکنند آن را تجزیه کنند یا در نظر بگیرند. هدف از این کار جلوگیری از بروز آسیب‌پذیری دیگری مانند CVE-2022-2880 است (یعنی نباید سیستم‌های مختلف را وادار کنیم که بر سر چگونگی دقیق تجزیه یک کوئری به توافق برسند). برای جزئیات بیشتر به https://www.oxeye.io/resources/golang-parameter-smuggling-attack مراجعه کنید. برای endpointهای *SubjectAccessReview در kube-apiserver: * اگر rawSelector و requirements هر دو خالی باشند، درخواست محدود نیست. * اگر rawSelector وجود داشته باشد و requirements خالی باشد، rawSelector تجزیه می‌شود و در صورت موفق‌بودن تجزیه، درخواست محدود می‌شود. * اگر rawSelector خالی باشد و requirements وجود داشته باشد، باید requirements اعمال شود. * اگر rawSelector و requirements هر دو وجود داشته باشند، درخواست نامعتبر است."
title: "LabelSelectorAttributes"
weight: 170
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


## LabelSelectorAttributes {#LabelSelectorAttributes}

LabelSelectorAttributes دسترسیِ محدودشده با برچسب را مشخص می‌کند. به نویسندگان webhook توصیه می‌شود: * مطمئن شوند rawSelector و requirements هر دو هم‌زمان تنظیم نشده باشند؛ * در صورت تنظیم‌بودن فیلد requirements، آن را در نظر بگیرند؛ * در صورت تنظیم‌بودن فیلد rawSelector، تلاش نکنند آن را تجزیه کنند یا در نظر بگیرند. هدف از این کار جلوگیری از بروز آسیب‌پذیری دیگری مانند CVE-2022-2880 است (یعنی نباید سیستم‌های مختلف را وادار کنیم که بر سر چگونگی دقیق تجزیه یک کوئری به توافق برسند). برای جزئیات بیشتر به https://www.oxeye.io/resources/golang-parameter-smuggling-attack مراجعه کنید. برای endpointهای *SubjectAccessReview در kube-apiserver: * اگر rawSelector و requirements هر دو خالی باشند، درخواست محدود نیست. * اگر rawSelector وجود داشته باشد و requirements خالی باشد، rawSelector تجزیه می‌شود و در صورت موفق‌بودن تجزیه، درخواست محدود می‌شود. * اگر rawSelector خالی باشد و requirements وجود داشته باشد، باید requirements اعمال شود. * اگر rawSelector و requirements هر دو وجود داشته باشند، درخواست نامعتبر است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>rawSelector</code><br/><em>string</em></td>
      <td>rawSelector شکل سریال‌شده یک field selector است که در یک پارامتر کوئری قرار می‌گیرد. به پیاده‌سازی‌های webhook توصیه می‌شود rawSelector را نادیده بگیرند. تا زمانی که requirements وجود نداشته باشد، *SubjectAccessReview در kube-apiserver مقدار rawSelector را تجزیه می‌کند.</td>
    </tr>
    <tr>
      <td><code>requirements</code><br/><em><a href="{{< ref "label-selector-requirement-v1-meta#LabelSelectorRequirement" >}}">آرایه‌ای از LabelSelectorRequirement</a></em></td>
      <td>requirements تفسیر تجزیه‌شده یک انتخابگر برچسب (label selector) است. برای اینکه یک نمونه از منبع با انتخابگر مطابقت داشته باشد، باید همه requirementها برقرار باشند. پیاده‌سازی‌های webhook باید requirements را پردازش کنند، اما نحوه پردازش آن‌ها بر عهده خود webhook است. از آنجا که requirements فقط می‌تواند درخواست را محدود کند، اگر requirements درک نشود، می‌توان با اطمینان درخواست را به‌صورت نامحدود مجاز دانست.</td>
    </tr>
  </tbody>
</table>

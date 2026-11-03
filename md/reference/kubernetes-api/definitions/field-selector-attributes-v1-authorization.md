---
api_metadata:
  apiVersion: "authorization.k8s.io/v1"
  import: "k8s.io/api/authorization/v1"
  kind: "FieldSelectorAttributes"
content_type: "api_reference"
description: "FieldSelectorAttributes دسترسیِ محدود‌شده بر اساس فیلد را مشخص می‌کند. به نویسندگان webhook توصیه می‌شود: * مطمئن شوند rawSelector و requirements هر دو هم‌زمان تنظیم نشده باشند * در صورت تنظیم بودن فیلد requirements آن را در نظر بگیرند * در صورت تنظیم بودن فیلد rawSelector تلاش نکنند آن را تجزیه کنند یا در نظر بگیرند. هدف از این کار جلوگیری از بروز آسیب‌پذیری دیگری مانند CVE-2022-2880 است (یعنی هماهنگ کردن سیستم‌های مختلف بر سر چگونگی دقیق تجزیه یک کوئری چیزی نیست که بخواهیم). برای جزئیات بیشتر به https://www.oxeye.io/resources/golang-parameter-smuggling-attack مراجعه کنید. برای endpointهای *SubjectAccessReview در kube-apiserver: * اگر rawSelector خالی و requirements نیز خالی باشد، درخواست محدود نمی‌شود. * اگر rawSelector وجود داشته باشد و requirements خالی باشد، rawSelector تجزیه می‌شود و در صورت موفقیت تجزیه، محدودیت اعمال می‌شود. * اگر rawSelector خالی باشد و requirements وجود داشته باشد، باید requirements رعایت شود. * اگر هم rawSelector و هم requirements وجود داشته باشند، درخواست نامعتبر است."
title: "FieldSelectorAttributes"
weight: 110
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


## FieldSelectorAttributes {#FieldSelectorAttributes}

FieldSelectorAttributes دسترسیِ محدود‌شده بر اساس فیلد را مشخص می‌کند. به نویسندگان webhook توصیه می‌شود: * مطمئن شوند rawSelector و requirements هر دو هم‌زمان تنظیم نشده باشند * در صورت تنظیم بودن فیلد requirements آن را در نظر بگیرند * در صورت تنظیم بودن فیلد rawSelector تلاش نکنند آن را تجزیه کنند یا در نظر بگیرند. هدف از این کار جلوگیری از بروز آسیب‌پذیری دیگری مانند CVE-2022-2880 است (یعنی هماهنگ کردن سیستم‌های مختلف بر سر چگونگی دقیق تجزیه یک کوئری چیزی نیست که بخواهیم). برای جزئیات بیشتر به https://www.oxeye.io/resources/golang-parameter-smuggling-attack مراجعه کنید. برای endpointهای *SubjectAccessReview در kube-apiserver: * اگر rawSelector خالی و requirements نیز خالی باشد، درخواست محدود نمی‌شود. * اگر rawSelector وجود داشته باشد و requirements خالی باشد، rawSelector تجزیه می‌شود و در صورت موفقیت تجزیه، محدودیت اعمال می‌شود. * اگر rawSelector خالی باشد و requirements وجود داشته باشد، باید requirements رعایت شود. * اگر هم rawSelector و هم requirements وجود داشته باشند، درخواست نامعتبر است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>rawSelector</code><br/><em>string</em></td>
      <td>rawSelector شکل سریال‌شده‌ی یک انتخابگر فیلد (field selector) است که در یک پارامتر کوئری قرار می‌گیرد. به پیاده‌سازی‌های webhook توصیه می‌شود rawSelector را نادیده بگیرند. *SubjectAccessReview در kube-apiserver تا زمانی که requirements وجود نداشته باشد، rawSelector را تجزیه می‌کند.</td>
    </tr>
    <tr>
      <td><code>requirements</code><br/><em><a href="{{< ref "field-selector-requirement-v1-meta#FieldSelectorRequirement" >}}">FieldSelectorRequirement array</a></em></td>
      <td>requirements تفسیر تجزیه‌شده‌ی یک انتخابگر فیلد است. برای اینکه یک نمونه از منبع با انتخابگر مطابقت داشته باشد، باید همه‌ی requirements برآورده شوند. پیاده‌سازی‌های webhook باید requirements را پردازش کنند، اما نحوه‌ی پردازش آن‌ها بر عهده‌ی خود webhook است. از آنجا که requirements فقط می‌توانند درخواست را محدود کنند، اگر requirements درک نشوند، مجوز دادن به درخواست به‌صورت نامحدود بی‌خطر است.</td>
    </tr>
  </tbody>
</table>

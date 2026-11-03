---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "StatusDetails"
content_type: "api_reference"
description: "StatusDetails مجموعه‌ای از ویژگی‌های اضافی است که سرور ممکن است برای ارائهٔ اطلاعات بیشتر درباره یک پاسخ تنظیم کند. فیلد Reason در آبجکت Status مشخص می‌کند که کدام ویژگی‌ها تنظیم خواهند شد. کلاینت‌ها باید فیلدهایی را که با نوع تعریف‌شدهٔ هر ویژگی مطابقت ندارند نادیده بگیرند و باید فرض کنند که هر ویژگی ممکن است خالی، نامعتبر یا ناقص تعریف‌شده باشد."
title: "StatusDetails"
weight: 530
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


## StatusDetails {#StatusDetails}

StatusDetails مجموعه‌ای از ویژگی‌های اضافی است که سرور ممکن است برای ارائهٔ اطلاعات بیشتر درباره یک پاسخ تنظیم کند. فیلد Reason در آبجکت Status مشخص می‌کند که کدام ویژگی‌ها تنظیم خواهند شد. کلاینت‌ها باید فیلدهایی را که با نوع تعریف‌شدهٔ هر ویژگی مطابقت ندارند نادیده بگیرند و باید فرض کنند که هر ویژگی ممکن است خالی، نامعتبر یا ناقص تعریف‌شده باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>causes</code><br/><em><a href="{{< ref "status-cause-v1-meta#StatusCause" >}}">StatusCause array</a></em></td>
      <td>آرایهٔ Causes شامل جزئیات بیشتری دربارهٔ شکست مرتبط با StatusReason است. همهٔ StatusReasonها دلایل تفصیلی ارائه نمی‌کنند.</td>
    </tr>
    <tr>
      <td><code>group</code><br/><em>string</em></td>
      <td>ویژگی group مربوط به منبعی که با StatusReason وضعیت مرتبط است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>ویژگی kind مربوط به منبعی که با StatusReason وضعیت مرتبط است. در برخی عملیات ممکن است با Kind منبع درخواست‌شده متفاوت باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>ویژگی name مربوط به منبعی که با StatusReason وضعیت مرتبط است (در صورتی که فقط یک نام قابل توصیف وجود داشته باشد).</td>
    </tr>
    <tr>
      <td><code>retryAfterSeconds</code><br/><em>integer</em></td>
      <td>در صورت مشخص شدن، مدت زمان بر حسب ثانیه است که پس از آن باید عملیات دوباره تلاش شود. برخی خطاها نشان می‌دهند که کلاینت باید اقدام جایگزینی انجام دهد؛ برای این خطاها، این فیلد ممکن است مشخص کند پیش از انجام اقدام جایگزین چه مدت باید منتظر ماند.</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>UID منبع (در صورتی که فقط یک منبع قابل توصیف وجود داشته باشد). اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids</td>
    </tr>
  </tbody>
</table>

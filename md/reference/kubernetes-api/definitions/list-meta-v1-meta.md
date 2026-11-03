---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "ListMeta"
content_type: "api_reference"
description: "ListMeta فراداده‌ای را توصیف می‌کند که منابع مصنوعی (synthetic) باید داشته باشند؛ از جمله لیست‌ها و آبجکت‌های وضعیت گوناگون. یک منبع فقط می‌تواند یکی از {ObjectMeta, ListMeta} را داشته باشد."
title: "ListMeta"
weight: 190
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


## ListMeta {#ListMeta}

ListMeta فراداده‌ای را توصیف می‌کند که منابع مصنوعی (synthetic) باید داشته باشند؛ از جمله لیست‌ها و آبجکت‌های وضعیت گوناگون. یک منبع فقط می‌تواند یکی از {ObjectMeta, ListMeta} را داشته باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>continue</code><br/><em>string</em></td>
      <td>اگر کاربر محدودیتی برای تعداد آیتم‌های بازگشتی تعیین کرده باشد، ممکن است continue تنظیم شود و نشان می‌دهد که سرور داده‌های بیشتری در اختیار دارد. این مقدار مبهم (opaque) است و می‌توان از آن برای ارسال درخواستی دیگر به همان endpoint که این لیست را ارائه کرده استفاده کرد تا مجموعه بعدی آبجکت‌های موجود دریافت شود. اگر پیکربندی سرور تغییر کرده باشد یا بیش از چند دقیقه گذشته باشد، ممکن است ادامه‌دادن یک لیست سازگار ممکن نباشد. مقدار فیلد resourceVersion که هنگام استفاده از این مقدار continue برگردانده می‌شود، با مقدار موجود در پاسخ اول یکسان خواهد بود، مگر اینکه این توکن را از یک پیام خطا دریافت کرده باشید.</td>
    </tr>
    <tr>
      <td><code>remainingItemCount</code><br/><em>integer</em></td>
      <td>remainingItemCount تعداد آیتم‌های بعدی لیست است که در این پاسخ لیست گنجانده نشده‌اند. اگر درخواست لیست شامل انتخابگرهای برچسب یا فیلد بوده باشد، تعداد آیتم‌های باقی‌مانده نامشخص است و این فیلد تنظیم نمی‌شود و هنگام سریال‌سازی حذف می‌گردد. اگر لیست کامل باشد (چه به این دلیل که تکه‌تکه (chunk) نمی‌شود و چه به این دلیل که این آخرین تکه است)، آیتم باقی‌مانده‌ای وجود ندارد و این فیلد تنظیم نمی‌شود و هنگام سریال‌سازی حذف می‌گردد. سرورهای قدیمی‌تر از v1.15 این فیلد را تنظیم نمی‌کنند. کاربرد مورد نظر remainingItemCount *تخمین* اندازه یک مجموعه است. کلاینت‌ها نباید به تنظیم‌شدن یا دقیق‌بودن remainingItemCount تکیه کنند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code><br/><em>string</em></td>
      <td>رشته‌ای که نسخه داخلی سرور از این آبجکت را مشخص می‌کند و کلاینت‌ها می‌توانند از آن برای تشخیص تغییر آبجکت‌ها استفاده کنند. کلاینت‌ها باید این مقدار را مبهم (opaque) در نظر بگیرند و بدون تغییر به سرور بازگردانند. این مقدار را سیستم مقداردهی می‌کند و فقط‌خواندنی است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency</td>
    </tr>
    <tr>
      <td><code>selfLink</code><br/><em>string</em></td>
      <td>منسوخ‌شده: selfLink یک فیلد قدیمی و فقط‌خواندنی است که دیگر توسط سیستم مقداردهی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>shardInfo</code><br/><em><a href="{{< ref "shard-info-v1-meta#ShardInfo" >}}">ShardInfo</a></em></td>
      <td>shardInfo زمانی تنظیم می‌شود که لیست، زیرمجموعه‌ای فیلترشده از کل مجموعه باشد که با یک انتخابگر شارد (shard selector) در درخواست انتخاب شده است. این فیلد انتخابگر را بازتاب می‌دهد تا کلاینت‌ها بتوانند بررسی کنند کدام شارد را دریافت کرده‌اند و پاسخ‌های شاردشده را با هم ادغام کنند. کلاینت‌ها نباید پاسخ‌های لیست شاردشده را به عنوان نمایش کامل مجموعه در حافظه نهان نگه دارند. این فیلد آلفا است و فعال‌کردن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
  </tbody>
</table>

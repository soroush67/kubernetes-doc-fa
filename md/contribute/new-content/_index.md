---
title: مشارکت در محتوای جدید
content_type: concept
main_menu: true
weight: 25
simple_list: true # for whatsnext section
---



<!-- overview -->

این بخش اطلاعاتی را در بر دارد که پیش از مشارکت در محتوای جدید باید بدانید.

همچنین صفحه‌های جداگانه‌ای برای ارسال [مطالعات موردی](/docs/contribute/new-content/case-studies)
و [مقاله‌های وبلاگ](/docs/contribute/blog/) وجود دارد.

<!-- body -->

## روند کار برای محتوای جدید

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->
{{< mermaid >}}
flowchart LR 
    subgraph second[پیش از شروع]
    direction TB
    S[ ] -.-
    A[امضای CLA بنیاد CNCF] --> B[انتخاب شاخه Git]
    B --> C[یک زبان در هر PR]
    C --> F[آشنایی با<br>ابزارهای مشارکت‌کنندگان]
    end
    subgraph first[مبانی مشارکت]
    direction TB
       T[ ] -.-
       D[نوشتن مستندات با Markdown<br>و ساخت سایت با Hugo] --- E[کد منبع در GitHub]
       E --- G['پوشه /content/../docs' مستندات<br>چند زبان را در بر دارد]
       G --- H[مرور انواع محتوای صفحه<br>و shortcodeهای Hugo]
    end
    

    first ----> second
     

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,B,C,D,E,F,G,H grey
class S,T spacewhite
class first,second white
{{</ mermaid >}}

***شکل - آماده‌سازی برای مشارکت در محتوای جدید***

شکل بالا اطلاعاتی را نشان می‌دهد که پیش از ارسال محتوای جدید باید بدانید.
جزئیات این اطلاعات در ادامه آمده است.



<!-- body -->

## مبانی مشارکت

- مستندات کوبرنتیز را با Markdown بنویسید و سایت کوبرنتیز را با
  [Hugo](https://gohugo.io/) بسازید.
- مستندات کوبرنتیز از [CommonMark](https://commonmark.org/) به‌عنوان گونه‌ی Markdown خود استفاده می‌کند.
- کد منبع در [GitHub](https://github.com/kubernetes/website) قرار دارد. مستندات
  کوبرنتیز را می‌توانید در `/content/en/docs/` پیدا کنید. بخشی از مستندات مرجع
  به‌طور خودکار با اسکریپت‌های موجود در پوشه‌ی `update-imported-docs/` تولید می‌شود.
- [انواع محتوای صفحه](/docs/contribute/style/page-content-types/) شیوه‌ی نمایش
  محتوای مستندات را در Hugo توصیف می‌کنند.
- برای مشارکت در مستندات کوبرنتیز می‌توانید از [shortcodeهای Docsy](https://www.docsy.dev/docs/adding-content/shortcodes/) یا [shortcodeهای سفارشی Hugo](/docs/contribute/style/hugo-shortcodes/) استفاده کنید.
- افزون بر shortcodeهای استاندارد Hugo، در مستندات خود از شماری
  [shortcode سفارشی Hugo](/docs/contribute/style/hugo-shortcodes/) نیز برای کنترل
  شیوه‌ی نمایش محتوا استفاده می‌کنیم.
- کد منبع مستندات به چند زبان در `/content/` موجود است. هر زبان پوشه‌ی مخصوص
  خود را دارد که با یک کد دوحرفی مطابق
  [استاندارد ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)
  نام‌گذاری شده است. برای مثال، کد منبع مستندات انگلیسی در `/content/en/docs/` ذخیره می‌شود.
- برای اطلاعات بیشتر درباره‌ی مشارکت در مستندات به زبان‌های مختلف یا آغاز یک
  ترجمه‌ی جدید، به [بومی‌سازی](/docs/contribute/localization) مراجعه کنید.

## پیش از شروع {#before-you-begin}

### امضای CLA بنیاد CNCF {#sign-the-cla}

همه‌ی مشارکت‌کنندگان کوبرنتیز **باید**
[راهنمای مشارکت‌کنندگان](https://github.com/kubernetes/community/blob/main/contributors/guide/README.md)
را بخوانند و [توافق‌نامه‌ی مجوز مشارکت‌کننده (CLA) را امضا کنند](https://github.com/kubernetes/community/blob/main/CLA.md).

درخواست‌های ادغام (pull request) مشارکت‌کنندگانی که CLA را امضا نکرده‌اند، در
آزمون‌های خودکار رد می‌شوند. نام و ایمیلی که وارد می‌کنید باید با مقادیر موجود
در `git config` شما یکسان باشد، و نام و ایمیل git شما نیز باید با نام و ایمیلی
که برای CLA بنیاد CNCF به کار برده‌اید مطابقت داشته باشد.

### انتخاب شاخه‌ی Git مناسب

هنگام باز کردن یک درخواست ادغام، باید از پیش بدانید کار خود را بر پایه‌ی کدام
شاخه انجام دهید.

سناریو | شاخه
:---------|:------------
محتوای موجود یا جدید به زبان انگلیسی برای نسخه‌ی فعلی | `main`
محتوا برای نسخه‌ای که در آن یک قابلیت تغییر می‌کند | شاخه‌ای که با نسخه‌ی اصلی (major) و فرعی (minor) دربردارنده‌ی تغییر قابلیت مطابقت دارد و از الگوی `dev-<version>` پیروی می‌کند. برای مثال، اگر قابلیتی در نسخه‌ی `v{{< skew nextMinorVersion >}}` تغییر کند، تغییرات مستندات را به شاخه‌ی ``dev-{{< skew nextMinorVersion >}}`` اضافه کنید.
محتوا به زبان‌های دیگر (بومی‌سازی‌ها) | از قرارداد همان بومی‌سازی پیروی کنید. برای اطلاعات بیشتر به [راهبرد شاخه‌بندی در بومی‌سازی](/docs/contribute/localization/#branch-strategy) مراجعه کنید.

اگر هنوز مطمئن نیستید کدام شاخه را انتخاب کنید، در کانال `#sig-docs` در Slack بپرسید.

{{< note >}} اگر درخواست ادغام خود را ارسال کرده‌اید و می‌دانید شاخه‌ی پایه
اشتباه بوده است، شما (و فقط شما، به‌عنوان ارسال‌کننده) می‌توانید آن را تغییر دهید. {{<
/note >}}

### زبان‌ها در هر PR

هر درخواست ادغام را به یک زبان محدود کنید. اگر لازم است تغییری یکسان را در یک
نمونه‌کد مشترک به چند زبان اعمال کنید، برای هر زبان یک PR جداگانه باز کنید.

## ابزارهای مشارکت‌کنندگان

پوشه‌ی [ابزارهای مشارکت‌کنندگان مستندات](https://github.com/kubernetes/website/tree/main/content/en/docs/doc-contributor-tools)
در مخزن `kubernetes/website` ابزارهایی را در بر دارد که مسیر مشارکت شما را
هموارتر می‌کنند.

## {{% heading "whatsnext" %}}

<!-- relies on simple_list: true in front matter for remaining links -->
* درباره‌ی ارسال [مقاله‌های وبلاگ](/docs/contribute/blog/article-submission/) بخوانید.

---
title: مشارکت با محتوای جدید
content_type: concept
main_menu: true
weight: 25
simple_list: true # for whatsnext section
---



<!-- overview -->

این بخش حاوی اطلاعاتی است که پیش از مشارکت با محتوای جدید باید بدانید.

همچنین صفحه‌هایی اختصاصی درباره‌ی ارسال [مطالعات موردی](/docs/contribute/new-content/case-studies)
و [مقالات وبلاگ](/docs/contribute/blog/) وجود دارد.

<!-- body -->

## روند کاری محتوای جدید {#new-content-task-flow}

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->
{{< mermaid >}}
flowchart LR 
    subgraph second[Before you begin]
    direction TB
    S[ ] -.-
    A[Sign the CNCF CLA] --> B[Choose Git branch]
    B --> C[One language per PR]
    C --> F[Check out<br>contributor tools]
    end
    subgraph first[Contributing Basics]
    direction TB
       T[ ] -.-
       D[Write docs in markdown<br>and build site with Hugo] --- E[source in GitHub]
       E --- G['/content/../docs' folder contains docs<br>for multiple languages]
       G --- H[Review Hugo page content<br>types and shortcodes]
    end
    

    first ----> second
     

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,B,C,D,E,F,G,H grey
class S,T spacewhite
class first,second white
{{</ mermaid >}}

***شکل - آماده‌سازی برای مشارکت با محتوای جدید***

شکل بالا اطلاعاتی را نشان می‌دهد که پیش از ارسال محتوای جدید باید بدانید.
جزئیات این اطلاعات در ادامه آمده است.



<!-- body -->

## اصول مشارکت {#contributing-basics}

- مستندات کوبرنتیز را با Markdown بنویسید و سایت کوبرنتیز را با
  [Hugo](https://gohugo.io/) بسازید.
- مستندات کوبرنتیز از [CommonMark](https://commonmark.org/) به‌عنوان گونه‌ی Markdown خود استفاده می‌کند.
- منبع مستندات در [GitHub](https://github.com/kubernetes/website) قرار دارد. مستندات
  کوبرنتیز را می‌توانید در مسیر `/content/en/docs/` بیابید. بخشی از مستندات مرجع
  به‌صورت خودکار از روی اسکریپت‌های موجود در دایرکتوری `update-imported-docs/` تولید می‌شود.
- [انواع محتوای صفحه](/docs/contribute/style/page-content-types/) نحوه‌ی
  ارائه‌ی محتوای مستندات در Hugo را توصیف می‌کنند.
- برای مشارکت در مستندات کوبرنتیز می‌توانید از [shortcodeهای Docsy](https://www.docsy.dev/docs/adding-content/shortcodes/) یا [shortcodeهای سفارشی Hugo](/docs/contribute/style/hugo-shortcodes/) استفاده کنید.
- افزون بر shortcodeهای استاندارد Hugo، در مستندات خود شماری
  [shortcode سفارشی Hugo](/docs/contribute/style/hugo-shortcodes/) به کار می‌بریم
  تا نحوه‌ی ارائه‌ی محتوا را کنترل کنیم.
- منبع مستندات در چندین زبان و در مسیر `/content/` در دسترس است. هر
  زبان پوشه‌ی مخصوص خود را دارد که نام آن یک کد دوحرفی بر پایه‌ی
  [استاندارد ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)
  است. برای مثال، منبع مستندات انگلیسی در `/content/en/docs/` ذخیره شده است.
- برای اطلاعات بیشتر درباره‌ی مشارکت در مستندات به زبان‌های مختلف
  یا شروع یک ترجمه‌ی جدید،
  به [بومی‌سازی](/docs/contribute/localization) مراجعه کنید.

## پیش از شروع {#before-you-begin}

### امضای CNCF CLA {#sign-the-cla}

همه‌ی مشارکت‌کنندگان کوبرنتیز **باید**
[راهنمای مشارکت‌کنندگان](https://github.com/kubernetes/community/blob/main/contributors/guide/README.md)
را بخوانند و
[توافقنامه‌ی مجوز مشارکت‌کننده (CLA) را امضا کنند](https://github.com/kubernetes/community/blob/main/CLA.md).

درخواست‌های ادغام (pull request) مشارکت‌کنندگانی که CLA را امضا نکرده‌اند در
آزمون‌های خودکار ناموفق می‌شوند. نام و ایمیلی که ارائه می‌کنید باید با مواردی که در
`git config` شما ثبت شده است مطابقت داشته باشد، و نام و ایمیل git شما باید با مواردی که برای
CNCF CLA استفاده شده است یکسان باشد.

### انتخاب شاخه‌ی Git مناسب {#choose-which-git-branch-to-use}

هنگام باز کردن یک pull request باید از پیش بدانید که کار خود را بر پایه‌ی کدام شاخه (branch) انجام دهید.

سناریو | شاخه
:---------|:------------
محتوای انگلیسی موجود یا جدید برای نسخه‌ی فعلی | `main`
محتوا برای انتشار تغییر یک قابلیت | شاخه‌ای که با نسخه‌ی major و minor مربوط به تغییر قابلیت متناظر است و از الگوی `dev-<version>` پیروی می‌کند. برای مثال، اگر قابلیتی در نسخه‌ی `v{{< skew nextMinorVersion >}}` تغییر می‌کند، تغییرات مستندات را به شاخه‌ی ``dev-{{< skew nextMinorVersion >}}`` اضافه کنید.
محتوا به زبان‌های دیگر (بومی‌سازی‌ها) | از قرارداد همان بومی‌سازی پیروی کنید. برای اطلاعات بیشتر به [راهبرد شاخه‌بندی بومی‌سازی](/docs/contribute/localization/#branch-strategy) مراجعه کنید.

اگر هنوز مطمئن نیستید کدام شاخه را انتخاب کنید، در کانال `#sig-docs` در Slack بپرسید.

{{< note >}} اگر pull request خود را ارسال کرده‌اید و می‌دانید که
شاخه‌ی پایه اشتباه بوده است، شما (و فقط شما، به‌عنوان ارسال‌کننده) می‌توانید آن را تغییر دهید. {{<
/note >}}

### زبان‌ها در هر PR {#languages-per-pr}

هر PR را به یک زبان محدود کنید. اگر لازم است یک تغییر یکسان را
در نمونه کد مشابه در چند زبان اعمال کنید، برای هر زبان یک PR جداگانه باز کنید.

## ابزارهای مشارکت‌کنندگان {#tools-for-contributors}

دایرکتوری [ابزارهای مشارکت‌کنندگان مستندات](https://github.com/kubernetes/website/tree/main/content/en/docs/doc-contributor-tools)
در مخزن `kubernetes/website` شامل ابزارهایی است که به روان‌تر شدن مسیر
مشارکت شما کمک می‌کنند.

## {{% heading "whatsnext" %}}

<!-- relies on simple_list: true in front matter for remaining links -->
* درباره‌ی ارسال [مقالات وبلاگ](/docs/contribute/blog/article-submission/) مطالعه کنید.

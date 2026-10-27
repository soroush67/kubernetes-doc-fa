---
title: مستندسازی یک ویژگی برای یک انتشار
linktitle: مستندسازی برای یک انتشار
content_type: concept
main_menu: true
weight: 20
card:
  name: contribute
  weight: 45
  title: مستندسازی یک ویژگی برای یک انتشار
---
<!-- overview -->

هر انتشار اصلی کوبرنتیز ویژگی‌های جدیدی را معرفی می‌کند که به مستندات نیاز دارند.
انتشارهای جدید همچنین شامل به‌روزرسانی‌هایی برای ویژگی‌ها و مستندات موجود هستند
(مانند ارتقای یک ویژگی از آلفا به بتا).

به‌طور معمول، SIG مسئول یک ویژگی، پیش‌نویس مستندات آن ویژگی را در قالب یک pull request
به شاخهٔ توسعهٔ مناسب در مخزن `kubernetes/website` ارسال می‌کند و یکی از اعضای تیم SIG Docs
بازخورد ویرایشی ارائه می‌دهد یا پیش‌نویس را مستقیماً ویرایش می‌کند. این بخش قراردادهای شاخه‌بندی
و فرایندی را که هر دو گروه در طول یک انتشار به کار می‌برند توضیح می‌دهد.

برای آشنایی با نحوهٔ اعلام ویژگی‌ها در وبلاگ، بخش
[ارتباطات پس از انتشار](/docs/contribute/blog/release-comms/) را بخوانید.

<!-- body -->

## برای مشارکت‌کنندگان مستندات {#for-documentation-contributors}

به‌طور کلی، مشارکت‌کنندگان مستندات محتوای مربوط به یک انتشار را از ابتدا نمی‌نویسند.
در عوض، آن‌ها با SIG که ویژگی جدید را ایجاد می‌کند همکاری می‌کنند تا پیش‌نویس مستندات را
اصلاح کرده و آن را برای انتشار آماده سازند.

پس از آنکه ویژگی‌ای را برای مستندسازی یا کمک به آن انتخاب کردید، دربارهٔ آن در کانال Slack با نام `#sig-docs`،
در یکی از جلسات هفتگی SIG Docs، یا مستقیماً در PR ثبت‌شده توسط SIG مربوط به ویژگی سؤال کنید.
اگر موافقت شد، می‌توانید با یکی از روش‌های شرح‌داده‌شده در
[Commit into another person's PR](/docs/contribute/review/for-approvers/#commit-into-another-person-s-pr)
در همان PR ویرایش انجام دهید.

### آگاهی از ویژگی‌های آینده {#find-out-about-upcoming-features}

برای آگاهی از ویژگی‌های آینده، در جلسهٔ هفتگی SIG Release شرکت کنید (برای جلسات پیش‌رو
به صفحهٔ [community](/community/) مراجعه کنید)
و مستندات ویژهٔ هر انتشار را در مخزن
[kubernetes/sig-release](https://github.com/kubernetes/sig-release/)
پیگیری کنید. هر انتشار یک زیرپوشه در پوشهٔ
[/sig-release/tree/master/releases/](https://github.com/kubernetes/sig-release/tree/master/releases)
دارد. این زیرپوشه شامل برنامهٔ زمانی انتشار، پیش‌نویس یادداشت‌های انتشار
و سندی است که تک‌تک اعضای تیم انتشار را فهرست می‌کند.

برنامهٔ زمانی انتشار شامل پیوندهایی به همهٔ اسناد، جلسات، صورت‌جلسه‌ها
و milestoneهای دیگر مربوط به انتشار است. همچنین اطلاعاتی دربارهٔ اهداف و جدول زمانی انتشار
و هر فرایند ویژه‌ای که برای این انتشار در نظر گرفته شده است در آن آمده است. در بخش‌های پایانی سند،
چند اصطلاح مرتبط با انتشار تعریف شده‌اند.

این سند همچنین پیوندی به **Feature tracking sheet** دارد که روش رسمی برای آگاهی از
همهٔ ویژگی‌های جدیدی است که قرار است در انتشار گنجانده شوند.

سند تیم انتشار مشخص می‌کند که مسئول هر نقش در انتشار چه کسی است. اگر
مشخص نیست که دربارهٔ یک ویژگی خاص یا پرسش شما باید با چه کسی صحبت کنید،
یا در جلسهٔ انتشار شرکت کنید و پرسش خود را مطرح کنید، یا با سرپرست انتشار (release lead) تماس بگیرید
تا او شما را راهنمایی کند.

پیش‌نویس یادداشت‌های انتشار جای مناسبی برای آگاهی از
ویژگی‌های خاص، تغییرات، منسوخ‌شدن‌ها و موارد دیگر دربارهٔ انتشار است. محتوای
آن تا اواخر چرخهٔ انتشار نهایی نمی‌شود، بنابراین با احتیاط از آن استفاده کنید.

### Feature tracking sheet {#feature-tracking-sheet}

Feature tracking sheet [برای یک انتشار مشخص کوبرنتیز](https://github.com/kubernetes/sig-release/tree/master/releases)
هر ویژگی‌ای را که برای آن انتشار برنامه‌ریزی شده است فهرست می‌کند.
هر ردیف شامل نام ویژگی، پیوندی به issue اصلی ویژگی در GitHub، سطح پایداری آن (آلفا، بتا یا پایدار)،
SIG و فرد مسئول پیاده‌سازی آن، اینکه آیا به مستندات نیاز دارد یا خیر، پیش‌نویس یادداشت انتشار
برای آن ویژگی و اینکه آیا merge شده است یا خیر می‌باشد. نکات زیر را در نظر داشته باشید:

- ویژگی‌های بتا و پایدار معمولاً اولویت مستندسازی بالاتری نسبت به ویژگی‌های آلفا دارند.
- آزمایش (و در نتیجه مستندسازی) ویژگی‌ای که merge نشده است، یا دست‌کم در PR خود
  از نظر ویژگی‌ها کامل در نظر گرفته نمی‌شود، دشوار است.
- تعیین اینکه آیا یک ویژگی به مستندات نیاز دارد یا خیر فرایندی دستی است. حتی اگر
  ویژگی‌ای به‌عنوان نیازمند مستندات علامت‌گذاری نشده باشد، ممکن است لازم باشد آن را مستند کنید.

## برای توسعه‌دهندگان یا سایر اعضای SIG {#for-developers-or-other-sig-members}

این بخش اطلاعاتی برای اعضای سایر SIGهای کوبرنتیز است که ویژگی‌های جدید را برای یک انتشار مستند می‌کنند.

اگر عضو یک SIG هستید که ویژگی جدیدی را برای کوبرنتیز توسعه می‌دهد، باید
با SIG Docs همکاری کنید تا مطمئن شوید ویژگی شما به‌موقع برای
انتشار مستند می‌شود. برای اطمینان از جزئیات زمان‌بندی و مهلت‌ها،
[feature tracking spreadsheet](https://github.com/kubernetes/sig-release/tree/master/releases)
را بررسی کنید یا در کانال Slack کوبرنتیز با نام `#sig-release` پرسش کنید.

### ایجاد یک PR جایگزین (placeholder) {#open-a-placeholder-pr}

1. یک pull request از نوع **draft** را روی شاخهٔ
   `dev-{{< skew nextMinorVersion >}}` در مخزن `kubernetes/website` باز کنید، همراه با یک
   commit کوچک که بعداً آن را اصلاح (amend) خواهید کرد. برای ایجاد یک draft pull request، از منوی کشویی
   **Create Pull Request** گزینهٔ **Create Draft Pull Request** را انتخاب کنید
   و سپس روی **Draft Pull Request** کلیک کنید.
1. توضیحات pull request را ویرایش کنید تا شامل پیوند به PR(های) [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
   و issue(های) [kubernetes/enhancements](https://github.com/kubernetes/enhancements) باشد.
1. در issue مرتبط در [kubernetes/enhancements](https://github.com/kubernetes/enhancements)
   یک نظر همراه با پیوند به PR بگذارید تا فرد مسئول مستندات که این انتشار را مدیریت می‌کند آگاه شود که
   مستندات ویژگی در راه است و باید برای انتشار پیگیری شود.

اگر ویژگی شما به هیچ تغییری در مستندات نیاز ندارد، با اشاره به آن در کانال Slack با نام `#sig-release`
مطمئن شوید که تیم sig-release از این موضوع آگاه است. اگر ویژگی به مستندات نیاز داشته باشد
اما PR ایجاد نشده باشد، ممکن است ویژگی از milestone حذف شود.

### PR آماده برای بازبینی {#pr-ready-for-review}

هنگامی که آماده بودید، PR جایگزین خود را با مستندات ویژگی تکمیل کنید و وضعیت PR را از draft
به **ready for review** تغییر دهید. برای علامت‌گذاری یک pull request
به‌عنوان آمادهٔ بازبینی، به بخش merge box بروید و روی **Ready for review** کلیک کنید.

نهایت تلاش خود را بکنید تا ویژگی خود و نحوهٔ استفاده از آن را توضیح دهید. اگر برای ساختاردهی
مستندات به کمک نیاز دارید، در کانال Slack با نام `#sig-docs` بپرسید.

پس از تکمیل محتوا، فرد مسئول مستندات که به ویژگی شما اختصاص داده شده است آن را بازبینی می‌کند.
برای اطمینان از صحت فنی، ممکن است محتوا به بازبینی فنی از سوی SIG(های) مربوط نیز نیاز داشته باشد.
از پیشنهادهای آن‌ها استفاده کنید تا محتوا را به وضعیت آمادهٔ انتشار برسانید.

اگر ویژگی شما به مستندات نیاز دارد و پیش‌نویس اولیهٔ محتوا دریافت نشود،
ممکن است ویژگی از milestone حذف شود.

#### Feature gates {#ready-for-review-feature-gates}

اگر ویژگی شما آلفا یا بتا است و پشت یک feature gate قرار دارد،
به یک فایل feature gate برای آن در مسیر
`content/en/docs/reference/command-line-tools-reference/feature-gates/` نیاز دارید.
نام فایل باید همان نام feature gate با پسوند `.md` باشد.
می‌توانید با نگاه به فایل‌های دیگری که از قبل در همان پوشه وجود دارند، دربارهٔ شکل مناسب فایل خود
ایده بگیرید. معمولاً یک پاراگراف کافی است؛ برای توضیحات طولانی‌تر،
مستندات را در جای دیگری اضافه کنید و به آن پیوند دهید.

همچنین، برای اینکه feature gate شما در جدول
[Alpha/Beta Feature gates](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features)
نمایش داده شود، جزئیات زیر را در
[front matter](https://gohugo.io/content-management/front-matter/)
فایل توضیحات Markdown خود بگنجانید:

```yaml
stages:
  - stage: <alpha/beta/stable/deprecated>  # Specify the development stage of the feature gate
    defaultValue: <true or false>     # Set to true if enabled by default, false otherwise
    fromVersion: <Version>            # Version from which the feature gate is available
    toVersion: <Version>              # (Optional) The version until which the feature gate is available
```

برای feature gateهای کاملاً جدید، یک توضیح جداگانه از feature gate نیز لازم است؛
یک فایل Markdown جدید در مسیر `content/en/docs/reference/command-line-tools-reference/feature-gates/`
ایجاد کنید (از فایل‌های دیگر به‌عنوان الگو استفاده کنید).

هنگامی که یک feature gate را از حالت غیرفعال‌به‌صورت‌پیش‌فرض به فعال‌به‌صورت‌پیش‌فرض تغییر می‌دهید،
ممکن است لازم باشد مستندات دیگری را نیز تغییر دهید (نه فقط فهرست
feature gateها). مراقب عباراتی مانند این باشید: «فیلد `exampleSetting`
یک فیلد بتا است و به‌صورت پیش‌فرض غیرفعال است. می‌توانید آن را با فعال‌کردن
feature gate با نام `ProcessExampleThings` فعال کنید.»

اگر ویژگی شما به GA رسیده یا منسوخ شده است، یک ورودی `stage` اضافی در بلوک
`stages` در فایل توضیحات بگنجانید.
مطمئن شوید که مراحل آلفا و بتا دست‌نخورده باقی بمانند. این گام، feature gate را از جدول
[Feature gates for Alpha/Beta](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features)
به جدول
[Feature gates for graduated or deprecated features](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-graduated-or-deprecated-features)
منتقل می‌کند. برای نمونه:

{{< highlight yaml "linenos=false,hl_lines=10-17" >}}
stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.12"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.13"
  # Added a `toVersion` to the previous stage.
    toVersion: "1.18"
  # Added 'stable' stage block to existing stages.
  - stage: stable
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.27"
{{< / highlight >}}

در نهایت، کوبرنتیز دیگر آن feature gate را اصلاً شامل نخواهد کرد.
برای نشان‌دادن حذف یک feature gate، عبارت `removed: true` را در
front matter فایل توضیحات مربوطه قرار دهید.
این تغییر به این معناست که اطلاعات feature gate از بخش
[Feature gates for graduated or deprecated features](/docs/reference/command-line-tools-reference/feature-gates-removed/#feature-gates-that-are-removed)
به صفحه‌ای اختصاصی با عنوان
[Feature Gates (removed)](/docs/reference/command-line-tools-reference/feature-gates-removed/)
منتقل می‌شود، همراه با توضیحات آن.

### همهٔ PRها بازبینی شده و آمادهٔ merge هستند {#all-prs-reviewed-and-ready-to-merge}

اگر PR شما تا مهلت انتشار در شاخهٔ `dev-{{< skew nextMinorVersion >}}`
merge نشده باشد، با فرد مسئول مستنداتی که انتشار را مدیریت می‌کند همکاری کنید
تا آن را تا مهلت مقرر وارد کنید. اگر ویژگی شما به مستندات نیاز دارد
و مستندات آماده نیست، ممکن است ویژگی از milestone حذف شود.

---
title: نقش‌ها و مسئولیت‌ها
content_type: concept
weight: 10
---

<!-- overview -->

هر کسی می‌تواند در کوبرنتیز مشارکت کند. با افزایش مشارکت‌های شما در SIG Docs،
می‌توانید برای سطوح مختلف عضویت در جامعه درخواست دهید.
این نقش‌ها به شما امکان می‌دهند مسئولیت بیشتری در جامعه بر عهده بگیرید.
هر نقش به زمان و تعهد بیشتری نیاز دارد. نقش‌ها عبارتند از:

- هر فرد (Anyone): مشارکت‌کنندگان عادی در مستندات کوبرنتیز
- اعضا (Members): می‌توانند issueها را تخصیص دهند و دسته‌بندی کنند و بر pull requestها بازبینی غیرالزام‌آور ارائه دهند
- بازبین‌ها (Reviewers): می‌توانند بازبینی pull requestهای مستندات را رهبری کنند و از کیفیت یک تغییر تضمین بدهند
- تأییدکنندگان (Approvers): می‌توانند بازبینی مستندات را رهبری کنند و تغییرات را ادغام (merge) کنند

<!-- body -->

## هر فرد (Anyone) {#anyone}

هر کسی که حساب GitHub داشته باشد می‌تواند در کوبرنتیز مشارکت کند. SIG Docs از همه مشارکت‌کنندگان جدید استقبال می‌کند!

هر فرد می‌تواند:

- در هر مخزن [Kubernetes](https://github.com/kubernetes/)، از جمله
  [`kubernetes/website`](https://github.com/kubernetes/website)،
  یک issue باز کند
- درباره یک pull request بازخورد غیرالزام‌آور بدهد
- در یک محلی‌سازی (localization) مشارکت کند
- پیشنهادهای بهبود را در [Slack](https://slack.k8s.io/) یا
  [فهرست پستی SIG docs](https://groups.google.com/forum/#!forum/kubernetes-sig-docs) مطرح کند.

پس از [امضای CLA](https://github.com/kubernetes/community/blob/main/CLA.md)، هر فرد همچنین می‌تواند:

- یک pull request باز کند تا محتوای موجود را بهبود بخشد، محتوای جدید اضافه کند، یا یک نوشته وبلاگ یا مطالعه موردی (case study) بنویسد
- نمودارها، دارایی‌های گرافیکی و اسکرین‌کست‌ها و ویدیوهای قابل جاسازی تولید کند

برای اطلاعات بیشتر، [مشارکت با محتوای جدید](/docs/contribute/new-content/) را ببینید.

## اعضا (Members) {#members}

عضو کسی است که چندین pull request را به
`kubernetes/website` ارسال کرده است. اعضا بخشی از
[سازمان GitHub کوبرنتیز](https://github.com/kubernetes) هستند.

اعضا می‌توانند:

- هر کاری را که در بخش [هر فرد (Anyone)](#anyone) فهرست شده است انجام دهند
- با استفاده از دیدگاه `/lgtm`، برچسب LGTM (looks good to me) را به یک pull request اضافه کنند

  {{< note >}}
  استفاده از `/lgtm` یک فرایند خودکار را فعال می‌کند. اگر می‌خواهید تأیید
  غیرالزام‌آور ارائه دهید، نوشتن دیدگاه "LGTM" نیز کافی است!
  {{< /note >}}

- با استفاده از دیدگاه `/hold`، ادغام یک pull request را مسدود کنند
- با استفاده از دیدگاه `/assign`، یک بازبین را به یک pull request تخصیص دهند
- بر pull requestها بازبینی غیرالزام‌آور ارائه دهند
- با استفاده از خودکارسازی، issueها را اولویت‌بندی و دسته‌بندی کنند
- ویژگی‌های جدید را مستندسازی کنند

### عضو شدن {#becoming-a-member}

پس از ارسال دست‌کم ۵ pull request اساسی و برآورده کردن سایر
[الزامات](https://github.com/kubernetes/community/blob/main/community-membership.md#member):

1. دو [بازبین](#reviewers) یا [تأییدکننده](#approvers) پیدا کنید تا از عضویت شما
   [حمایت (sponsor)](/docs/contribute/advanced#sponsor-a-new-contributor) کنند.

   درخواست حمایت را در [کانال #sig-docs در Slack](https://kubernetes.slack.com) یا در
   [فهرست پستی SIG Docs](https://groups.google.com/forum/#!forum/kubernetes-sig-docs) مطرح کنید.

   {{< note >}}
   به یکی از اعضای SIG Docs ایمیل مستقیم یا پیام مستقیم Slack نفرستید.
   باید پیش از ارسال درخواست خود، درخواست حمایت را مطرح کنید.
   {{< /note >}}

1. یک issue در GitHub در مخزن
   [`kubernetes/org`](https://github.com/kubernetes/org/) باز کنید. از قالب issue با عنوان
   **Organization Membership Request** استفاده کنید.

1. حامیان خود را از issue در GitHub مطلع کنید. می‌توانید یکی از این کارها را انجام دهید:
   - نام کاربری GitHub آن‌ها را در issue ذکر کنید (`@<GitHub-username>`)
   - پیوند issue را از طریق Slack یا ایمیل برای آن‌ها بفرستید.

     حامیان درخواست شما را با رأی `+1` تأیید می‌کنند. پس از آنکه حامیان شما
     درخواست را تأیید کردند، یک مدیر GitHub کوبرنتیز شما را به‌عنوان عضو اضافه می‌کند.
     تبریک می‌گوییم!

     اگر درخواست عضویت شما پذیرفته نشود، بازخورد دریافت خواهید کرد.
     پس از رسیدگی به بازخورد، دوباره درخواست دهید.

1. دعوت‌نامه پیوستن به سازمان GitHub کوبرنتیز را در حساب ایمیل خود بپذیرید.

   {{< note >}}
   GitHub دعوت‌نامه را به نشانی ایمیل پیش‌فرض حساب شما ارسال می‌کند.
   {{< /note >}}

## بازبین‌ها (Reviewers) {#reviewers}

بازبین‌ها مسئول بازبینی pull requestهای باز هستند. برخلاف بازخورد اعضا،
نویسنده PR باید به بازخورد بازبین‌ها رسیدگی کند. بازبین‌ها اعضای تیم GitHub با نام
[@kubernetes/sig-docs-{language}-reviews](https://github.com/orgs/kubernetes/teams?query=sig-docs)
هستند.

بازبین‌ها می‌توانند:

- هر کاری را که در بخش [هر فرد (Anyone)](#anyone) و [اعضا (Members)](#members) فهرست شده است انجام دهند
- pull requestها را بازبینی کنند و بازخورد الزام‌آور ارائه دهند

  {{< note >}}
  برای ارائه بازخورد غیرالزام‌آور، دیدگاه‌های خود را با عبارتی مانند "Optionally: " آغاز کنید.
  {{< /note >}}

- رشته‌های رو به کاربر را در کد ویرایش کنند
- توضیحات (comments) کد را بهبود دهند

می‌توانید بازبین SIG Docs باشید، یا بازبین مستندات در یک حوزه موضوعی خاص.

### تخصیص بازبین‌ها به pull requestها {#assigning-reviewers-to-pull-requests}

خودکارسازی، بازبین‌ها را به همه pull requestها تخصیص می‌دهد. می‌توانید با نوشتن دیدگاه
`/assign [@_github_handle]` از یک فرد مشخص درخواست بازبینی کنید.

اگر بازبین تخصیص‌یافته درباره PR دیدگاهی ننوشته باشد، بازبین دیگری می‌تواند
وارد عمل شود. همچنین می‌توانید در صورت نیاز بازبین‌های فنی را نیز تخصیص دهید.

### استفاده از `/lgtm` {#using-lgtm}

LGTM مخفف "Looks good to me" (به نظر من خوب است) است و نشان می‌دهد که یک pull request
از نظر فنی دقیق و آماده ادغام است. ادغام همه PRها به یک دیدگاه `/lgtm` از طرف
بازبین و یک دیدگاه `/approve` از طرف تأییدکننده نیاز دارد.

دیدگاه `/lgtm` از طرف بازبین الزام‌آور است و فرایند خودکاری را فعال می‌کند که برچسب `lgtm` را اضافه می‌کند.

### بازبین شدن {#becoming-a-reviewer}

وقتی [الزامات](https://github.com/kubernetes/community/blob/main/community-membership.md#reviewer)
را برآورده کردید، می‌توانید بازبین SIG Docs شوید. بازبین‌ها در سایر SIGها باید
جداگانه برای وضعیت بازبین در SIG Docs درخواست دهند.

برای درخواست:

1. یک pull request باز کنید که نام کاربری GitHub شما را به یکی از بخش‌های فایل
   [OWNERS_ALIASES](https://github.com/kubernetes/website/blob/main/OWNERS_ALIASES)
   در مخزن `kubernetes/website` اضافه کند.

   {{< note >}}
   اگر مطمئن نیستید خود را کجا اضافه کنید، خود را به `sig-docs-en-reviews` اضافه کنید.
   {{< /note >}}

1. PR را به یک یا چند تأییدکننده SIG-Docs تخصیص دهید (نام‌های کاربری فهرست‌شده در
   `sig-docs-{language}-owners`).

در صورت تأیید، یکی از سرپرستان SIG Docs شما را به تیم GitHub مناسب اضافه می‌کند. پس از اضافه شدن،
[K8s-ci-robot](https://github.com/kubernetes/test-infra/tree/master/prow#bots-home)
شما را به‌عنوان بازبین در pull requestهای جدید تخصیص می‌دهد و پیشنهاد می‌کند.

## تأییدکنندگان (Approvers) {#approvers}

تأییدکنندگان pull requestها را برای ادغام بازبینی و تأیید می‌کنند. تأییدکنندگان اعضای تیم‌های GitHub با نام
[@kubernetes/sig-docs-{language}-owners](https://github.com/orgs/kubernetes/teams/?query=sig-docs)
هستند.

تأییدکنندگان می‌توانند کارهای زیر را انجام دهند:

- هر کاری که در بخش [هر فرد (Anyone)](#anyone)، [اعضا (Members)](#members) و [بازبین‌ها (Reviewers)](#reviewers) فهرست شده است
- با تأیید و ادغام pull requestها با استفاده از دیدگاه `/approve`، محتوای مشارکت‌کنندگان را منتشر کنند
- بهبودهایی را برای راهنمای سبک (style guide) پیشنهاد دهند
- بهبودهایی را برای تست‌های مستندات پیشنهاد دهند
- بهبودهایی را برای وب‌سایت کوبرنتیز یا سایر ابزارها پیشنهاد دهند

اگر PR از قبل دارای `/lgtm` باشد، یا اگر تأییدکننده نیز با
`/lgtm` دیدگاه بگذارد، PR به‌طور خودکار ادغام می‌شود. یک تأییدکننده SIG Docs فقط باید
برای تغییری `/lgtm` بگذارد که به بازبینی فنی بیشتر نیاز ندارد.


### تأیید pull requestها {#approving-pull-requests}

تنها تأییدکنندگان و سرپرستان SIG Docs می‌توانند pull requestها را
در مخزن وب‌سایت ادغام کنند. این امر با مسئولیت‌های مشخصی همراه است.

- تأییدکنندگان می‌توانند از دستور `/approve` استفاده کنند که PRها را در مخزن ادغام می‌کند.

  {{< warning >}}
  یک ادغام بی‌دقت می‌تواند سایت را خراب کند، پس هنگام ادغام هر چیزی مطمئن باشید که قصدتان همین است.
  {{< /warning >}}

- مطمئن شوید تغییرات پیشنهادی با
  [راهنمای محتوای مستندات](/docs/contribute/style/content-guide/) مطابقت دارند.

  اگر هر پرسشی دارید، یا درباره چیزی مطمئن نیستید، با خیال راحت
  درخواست بازبینی بیشتر بدهید.

- پیش از `/approve` کردن یک PR، بررسی کنید که تست‌های Netlify با موفقیت انجام شده باشند.

    <img src="/images/docs/contribute/netlify-pass.png" width="75%" alt="Netlify tests must pass before approving" />

- پیش از تأیید، پیش‌نمایش صفحه Netlify مربوط به PR را مشاهده کنید تا مطمئن شوید همه‌چیز درست به نظر می‌رسد.

- در
  [برنامه چرخشی PR Wrangler](https://github.com/kubernetes/website/wiki/PR-Wranglers)
  برای چرخش‌های هفتگی شرکت کنید. SIG Docs انتظار دارد همه تأییدکنندگان در این
  چرخش مشارکت کنند. برای جزئیات بیشتر، [PR wranglers](/docs/contribute/participate/pr-wranglers/) را ببینید.

### تأییدکننده شدن {#becoming-an-approver}

وقتی [الزامات](https://github.com/kubernetes/community/blob/main/community-membership.md#approver)
را برآورده کردید، می‌توانید تأییدکننده SIG Docs شوید. تأییدکنندگان در سایر SIGها باید
جداگانه برای وضعیت تأییدکننده در SIG Docs درخواست دهند.

برای درخواست:

1. یک pull request باز کنید که خودتان را به یکی از بخش‌های فایل
   [OWNERS_ALIASES](https://github.com/kubernetes/website/blob/main/OWNERS_ALIASES)
   در مخزن `kubernetes/website` اضافه کند.

    {{< note >}}
    اگر مطمئن نیستید خود را کجا اضافه کنید، خود را به `sig-docs-en-owners` اضافه کنید.
    {{< /note >}}

2. PR را به یک یا چند تأییدکننده فعلی SIG Docs تخصیص دهید.

در صورت تأیید، یکی از سرپرستان SIG Docs شما را به تیم GitHub مناسب اضافه می‌کند. پس از اضافه شدن،
[@k8s-ci-robot](https://github.com/kubernetes/test-infra/tree/master/prow#bots-home)
شما را به‌عنوان بازبین در pull requestهای جدید تخصیص می‌دهد و پیشنهاد می‌کند.

## {{% heading "whatsnext" %}}

- درباره [PR wrangling](/docs/contribute/participate/pr-wranglers/) بخوانید؛ نقشی که همه تأییدکنندگان به‌صورت چرخشی بر عهده می‌گیرند.

---
title: بازبینی برای تأییدکنندگان و بازبین‌ها
linktitle: برای تأییدکنندگان و بازبین‌ها
slug: for-approvers
content_type: concept
weight: 20
---

<!-- overview -->

[بازبین‌ها (Reviewers)](/docs/contribute/participate/#reviewers) و
[تأییدکنندگان (Approvers)](/docs/contribute/participate/#approvers) در SIG Docs هنگام
بازبینی یک تغییر، چند کار اضافی نیز انجام می‌دهند.

هر هفته یکی از تأییدکنندگان مستندات داوطلب می‌شود که درخواست‌های ادغام (pull request) را اولویت‌بندی و بازبینی کند.
این فرد در آن هفته «PR Wrangler» است. برای اطلاعات بیشتر به
[زمان‌بند PR Wrangler](https://github.com/kubernetes/website/wiki/PR-Wranglers)
مراجعه کنید. برای اینکه PR Wrangler شوید، در جلسه هفتگی SIG Docs شرکت کنید
و داوطلب شوید. حتی اگر در برنامه هفته جاری قرار نداشته باشید، همچنان می‌توانید
درخواست‌های ادغام (PR) را که هنوز تحت بازبینی فعال نیستند، بازبینی کنید.

علاوه بر این چرخش، یک ربات بر اساس مالکان فایل‌های تغییریافته، بازبین‌ها و تأییدکنندگان
را به PR اختصاص می‌دهد.

<!-- body -->

## بازبینی یک PR

مستندات کوبرنتیز از
[فرایند بازبینی کد کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/guide/owners.md#the-code-review-process)
پیروی می‌کند.

همه آنچه در [بازبینی یک pull request](/docs/contribute/review/reviewing-prs)
شرح داده شده است صادق است، اما بازبین‌ها و تأییدکنندگان باید کارهای زیر را نیز انجام دهند:

- در صورت نیاز، با استفاده از دستور `/assign` در Prow، یک بازبین مشخص را به PR اختصاص دهید.
  این کار به‌ویژه هنگام درخواست بازبینی فنی از مشارکت‌کنندگان کد اهمیت بیشتری دارد.

  {{< note >}}
  برای اینکه ببینید چه کسانی می‌توانند بازبینی فنی انجام دهند، فیلد `reviewers` را در front-matter
  ابتدای فایل Markdown بررسی کنید.
  {{< /note >}}

- مطمئن شوید PR از راهنماهای [محتوا](/docs/contribute/style/content-guide/)
  و [سبک](/docs/contribute/style/style-guide/) پیروی می‌کند؛ اگر چنین نیست،
  نویسنده را به بخش مرتبط راهنما (یا راهنماها) ارجاع دهید.
- در صورت لزوم، از گزینه **Request Changes** در GitHub استفاده کنید تا تغییرات را به نویسنده PR پیشنهاد دهید.
- اگر پیشنهادهای شما اعمال شد، وضعیت بازبینی خود را در GitHub با دستورهای `/approve` یا `/lgtm` در Prow تغییر دهید.

## کامیت کردن در PR شخص دیگر

گذاشتن نظر روی PR مفید است، اما گاهی ممکن است لازم باشد به‌جای آن
مستقیماً در PR شخص دیگری کامیت کنید.

جای فرد دیگری را «نگیرید» مگر اینکه صراحتاً از شما بخواهد
یا بخواهید PR را که مدت‌هاست رها شده است احیا کنید. اگرچه ممکن است
در کوتاه‌مدت سریع‌تر باشد، اما فرصت مشارکت را از آن فرد می‌گیرد.

روشی که استفاده می‌کنید به این بستگی دارد که لازم است فایلی را ویرایش کنید که
از قبل در محدوده PR قرار دارد، یا فایلی که PR هنوز به آن دست نزده است.

اگر هر یک از موارد زیر برقرار باشد، نمی‌توانید در PR شخص دیگری کامیت کنید:

- نویسنده PR شاخه خود را مستقیماً به مخزن
  [https://github.com/kubernetes/website/](https://github.com/kubernetes/website/)
  push کرده باشد. فقط بازبینی که دسترسی push دارد می‌تواند در PR کاربر دیگری کامیت کند.

  {{< note >}}
  نویسنده را تشویق کنید که دفعه بعد پیش از باز کردن PR، شاخه خود را به fork خودش push کند.
  {{< /note >}}

- نویسنده PR صراحتاً ویرایش توسط تأییدکنندگان را غیرمجاز کرده باشد.

## دستورهای Prow برای بازبینی

[Prow](https://github.com/kubernetes/test-infra/blob/master/prow/README.md)
سیستم CI/CD مبتنی بر کوبرنتیز است که کارها را روی درخواست‌های ادغام (PR) اجرا می‌کند. Prow
دستورهایی به سبک چت‌بات فراهم می‌کند تا اقدامات GitHub را در سراسر سازمان کوبرنتیز مدیریت کند، مانند
[افزودن و حذف برچسب‌ها](#adding-and-removing-issue-labels)،
بستن issueها و اختصاص یک تأییدکننده. دستورهای Prow را با قالب `/<command-name>`
به‌صورت نظر در GitHub وارد کنید.

رایج‌ترین دستورهای Prow که بازبین‌ها و تأییدکنندگان استفاده می‌کنند عبارت‌اند از:

{{< table caption="دستورهای Prow برای بازبینی" >}}
دستور Prow | محدودیت نقش | توضیحات
:------------|:------------------|:-----------
`/lgtm` | اعضای سازمان | نشان می‌دهد که بازبینی PR را به پایان رسانده‌اید و از تغییرات راضی هستید.
`/approve` | تأییدکنندگان | یک PR را برای ادغام تأیید می‌کند.
`/assign` | هر فرد | فردی را برای بازبینی یا تأیید یک PR تعیین می‌کند.
`/close` | اعضای سازمان | یک issue یا PR را می‌بندد.
`/hold` | هر فرد | برچسب `do-not-merge/hold` را اضافه می‌کند و نشان می‌دهد PR نمی‌تواند به‌طور خودکار ادغام شود.
`/hold cancel` | هر فرد | برچسب `do-not-merge/hold` را حذف می‌کند.
{{< /table >}}

برای مشاهده دستورهایی که می‌توانید در یک PR استفاده کنید، به
[مرجع دستورهای Prow](https://prow.k8s.io/command-help?repo=kubernetes%2Fwebsite) مراجعه کنید.

## اولویت‌بندی و دسته‌بندی issueها

به‌طور کلی، SIG Docs از فرایند
[اولویت‌بندی issueهای کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/guide/issue-triage.md)
پیروی می‌کند و از همان برچسب‌ها استفاده می‌کند.

این [فیلتر](https://github.com/kubernetes/website/issues?q=is%3Aissue+is%3Aopen+-label%3Apriority%2Fbacklog+-label%3Apriority%2Fimportant-longterm+-label%3Apriority%2Fimportant-soon+-label%3Atriage%2Fneeds-information+-label%3Atriage%2Fsupport+sort%3Acreated-asc) در GitHub Issues
issueهایی را پیدا می‌کند که ممکن است نیاز به اولویت‌بندی داشته باشند.

### اولویت‌بندی یک issue

1. issue را اعتبارسنجی کنید

   - مطمئن شوید issue درباره مستندات وب‌سایت است. برخی issueها را می‌توان سریع با
     پاسخ دادن به یک پرسش یا ارجاع گزارش‌دهنده به یک منبع بست. برای جزئیات به بخش
     [درخواست‌های پشتیبانی یا گزارش‌های باگ کد](#support-requests-or-code-bug-reports) مراجعه کنید.
   - ارزیابی کنید که آیا issue ارزش پیگیری دارد.
   - اگر issue جزئیات کافی برای اقدام ندارد یا قالب آن به‌درستی پر نشده است،
     برچسب `triage/needs-information` را اضافه کنید.
   - اگر issue هر دو برچسب `lifecycle/stale` و `triage/needs-information` را دارد، آن را ببندید.

2. یک برچسب اولویت اضافه کنید (برچسب‌های اولویت در
   [راهنمای اولویت‌بندی issue](https://github.com/kubernetes/community/blob/main/contributors/guide/issue-triage.md#define-priority)
   به‌تفصیل تعریف شده‌اند)

  {{< table caption="برچسب‌های issue" >}}
  برچسب | توضیحات
  :------------|:------------------
  `priority/critical-urgent` | همین حالا انجام دهید.
  `priority/important-soon` | ظرف ۳ ماه انجام دهید.
  `priority/important-longterm` | ظرف ۶ ماه انجام دهید.
  `priority/backlog` | به‌طور نامحدود قابل تعویق است. هنگامی که منابع در دسترس بود انجام دهید.
  `priority/awaiting-more-evidence` | جایگاهی برای issue بالقوه خوب تا گم نشود.
  `help` یا `good first issue` | مناسب کسی که تجربه بسیار کمی در کوبرنتیز یا SIG Docs دارد. برای اطلاعات بیشتر به [برچسب‌های Help Wanted و Good First Issue](https://kubernetes.dev/docs/guide/help-wanted/) مراجعه کنید.

  {{< /table >}}

  به صلاحدید خود، مالکیت یک issue را بر عهده بگیرید و برای آن PR ارسال کنید
  (به‌ویژه اگر سریع است یا به کاری که از قبل انجام می‌دهید مربوط می‌شود).

اگر درباره اولویت‌بندی یک issue پرسشی دارید، در `#sig-docs` در Slack یا
[فهرست پستی kubernetes-sig-docs](https://groups.google.com/forum/#!forum/kubernetes-sig-docs) بپرسید.

## افزودن و حذف برچسب‌های issue

برای افزودن یک برچسب، نظری با یکی از قالب‌های زیر بگذارید:

- `/<label-to-add>` (برای مثال `/good-first-issue`)
- `/<label-category> <label-to-add>` (برای مثال `/triage needs-information` یا `/language ja`)

برای حذف یک برچسب، نظری با یکی از قالب‌های زیر بگذارید:

- `/remove-<label-to-remove>` (برای مثال `/remove-help`)
- `/remove-<label-category> <label-to-remove>` (برای مثال `/remove-triage needs-information`)

در هر دو حالت، برچسب باید از قبل وجود داشته باشد. اگر سعی کنید برچسبی را اضافه کنید که وجود ندارد،
دستور بدون هیچ پیامی نادیده گرفته می‌شود.

برای فهرست همه برچسب‌ها، به [بخش Labels مخزن وب‌سایت](https://github.com/kubernetes/website/labels) مراجعه کنید.
همه برچسب‌ها توسط SIG Docs استفاده نمی‌شوند.

### برچسب‌های چرخه عمر issue

issueها معمولاً سریع باز و بسته می‌شوند.
با این حال، گاهی یک issue پس از باز شدن غیرفعال می‌ماند.
در مواقع دیگر، ممکن است یک issue لازم باشد بیش از ۹۰ روز باز بماند.

{{< table caption="برچسب‌های چرخه عمر issue" >}}
برچسب | توضیحات
:------------|:------------------
`lifecycle/stale` | پس از ۹۰ روز بدون فعالیت، یک issue به‌طور خودکار با برچسب stale علامت‌گذاری می‌شود. اگر چرخه عمر با دستور `/remove-lifecycle stale` به‌صورت دستی بازگردانده نشود، issue به‌طور خودکار بسته خواهد شد.
`lifecycle/frozen` | issue دارای این برچسب پس از ۹۰ روز عدم فعالیت stale نمی‌شود. کاربر این برچسب را به‌صورت دستی به issueهایی اضافه می‌کند که لازم است بسیار بیش از ۹۰ روز باز بمانند، مانند issueهایی که برچسب `priority/important-longterm` دارند.
{{< /table >}}

## رسیدگی به انواع خاص issue

SIG Docs به‌اندازه کافی با انواع issue زیر روبه‌رو می‌شود که نحوه رسیدگی به آن‌ها مستند شده است.

### issueهای تکراری

اگر برای یک مشکل واحد یک یا چند issue باز است، آن‌ها را در یک issue واحد ادغام کنید.
باید تصمیم بگیرید کدام issue باز بماند (یا
issue جدیدی باز کنید)، سپس همه اطلاعات مرتبط را به آن منتقل کنید و issueهای مرتبط را پیوند دهید.
در پایان، همه issueهای دیگری را که همان مشکل را شرح می‌دهند با برچسب
`triage/duplicate` علامت‌گذاری کنید و ببندید. داشتن تنها یک issue برای رسیدگی، سردرگمی را کاهش می‌دهد
و از کار تکراری روی همان مشکل جلوگیری می‌کند.

### issueهای لینک خراب

اگر issue لینک خراب در مستندات API یا `kubectl` است، تا زمانی که مشکل کاملاً درک نشده،
برچسب `/priority critical-urgent` را به آن بدهید. به همه
issueهای لینک خراب دیگر `/priority important-longterm` بدهید، زیرا باید به‌صورت دستی رفع شوند.

### issueهای وبلاگ

انتظار داریم مطالب [وبلاگ کوبرنتیز](/blog/) با گذشت زمان
قدیمی شوند. بنابراین، فقط مطالب وبلاگی را نگهداری می‌کنیم که کمتر از یک سال از آن‌ها گذشته باشد.
اگر یک issue به مطلبی از وبلاگ مربوط است که بیش از یک سال قدمت دارد،
معمولاً باید issue را بدون رفع ببندید.

می‌توانید پیوندی به [به‌روزرسانی و نگهداری مقالات](/docs/contribute/blog/#maintenance)
را در پیامی که هنگام بستن PR ارسال می‌کنید قرار دهید.

در صورت وجود توجیه مرتبط، استثنا قائل شدن اشکالی ندارد.

### درخواست‌های پشتیبانی یا گزارش‌های باگ کد

برخی issueهای مستندات در واقع مشکلاتی در کد زیربنایی هستند، یا درخواست کمک
زمانی که چیزی، مثلاً یک آموزش، کار نمی‌کند.
برای issueهای نامرتبط با مستندات، issue را با برچسب `kind/support` ببندید و با نظری
درخواست‌کننده را به مراجع پشتیبانی (Slack، Stack Overflow) و در صورت
مرتبط بودن، به مخزنی که باید برای باگ‌های قابلیت‌ها issue ثبت کند راهنمایی کنید (`kubernetes/kubernetes`
نقطه شروع بسیار خوبی است).

نمونه پاسخ به یک درخواست پشتیبانی:

```none
This issue sounds more like a request for support and less
like an issue specifically for docs. I encourage you to bring
your question to the `#kubernetes-users` channel in
[Kubernetes slack](https://slack.k8s.io/). You can also search
resources like
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes)
for answers to similar questions.

You can also open issues for Kubernetes functionality in
https://github.com/kubernetes/kubernetes.

If this is a documentation issue, please re-open this issue.
```

نمونه پاسخ به گزارش باگ کد:

```none
This sounds more like an issue with the code than an issue with
the documentation. Please open an issue at
https://github.com/kubernetes/kubernetes/issues.

If this is a documentation issue, please re-open this issue.
```

### Squash کردن

به‌عنوان تأییدکننده، هنگام بازبینی درخواست‌های ادغام (PR)، موارد گوناگونی پیش می‌آید
که ممکن است یکی از کارهای زیر را انجام دهید:

- به مشارکت‌کننده توصیه کنید کامیت‌های خود را squash کند.
- کامیت‌ها را به‌جای مشارکت‌کننده squash کنید.
- به مشارکت‌کننده توصیه کنید فعلاً squash نکند.
- از squash کردن جلوگیری کنید.

**توصیه به مشارکت‌کنندگان برای squash کردن**: ممکن است یک مشارکت‌کننده جدید نداند که
باید کامیت‌های خود را در درخواست‌های ادغام (PR) squash کند. در این صورت، به او توصیه کنید
این کار را انجام دهد، پیوندهایی به اطلاعات مفید ارائه دهید و در صورت نیاز به کمک،
پیشنهاد دهید کمک را هماهنگ کنید. چند پیوند مفید:

- [باز کردن pull requestها و squash کردن کامیت‌ها](/docs/contribute/new-content/open-a-pr#squashing-commits)
  برای مشارکت‌کنندگان مستندات.
- [گردش کار GitHub](https://www.k8s.dev/docs/guide/github-workflow/)، همراه با نمودارها، برای توسعه‌دهندگان.

**squash کردن کامیت‌ها برای مشارکت‌کنندگان**: اگر squash کردن کامیت‌ها برای مشارکت‌کننده
دشوار است یا فشار زمانی برای ادغام یک PR وجود دارد، می‌توانید squash را به‌جای او انجام دهید:

- مخزن kubernetes/website
  [طوری پیکربندی شده است که squash کردن را هنگام ادغام pull requestها مجاز کند](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests).
  کافی است دکمه *Squash commits* را انتخاب کنید.
- در PR، اگر مشارکت‌کننده به نگهدارندگان اجازه مدیریت PR را داده باشد، می‌توانید
  کامیت‌های او را squash کنید و fork او را با نتیجه به‌روزرسانی کنید. پیش از squash،
  به او توصیه کنید آخرین تغییرات خود را ذخیره و در PR push کند. پس از squash،
  به او توصیه کنید کامیت squash‌شده را در کلون محلی خود pull کند.
- می‌توانید با استفاده از یک برچسب، GitHub را وادار به squash کردن کامیت‌ها کنید تا Tide / GitHub
  squash را انجام دهد، یا هنگام ادغام PR روی دکمه *Squash commits* کلیک کنید.

**توصیه به مشارکت‌کنندگان برای پرهیز از squash کردن**

- اگر یک کامیت کاری خراب یا نابخردانه انجام می‌دهد و کامیت آخر این
  خطا را برمی‌گرداند، کامیت‌ها را squash نکنید. حتی اگر زبانه «Files changed» در PR
  در GitHub و پیش‌نمایش Netlify هر دو درست به نظر برسند، ادغام این PR ممکن است برای دیگران
  تعارض‌های rebase یا merge ایجاد کند. هر طور صلاح می‌دانید مداخله کنید تا از این
  خطر برای سایر مشارکت‌کنندگان جلوگیری شود.

**هرگز squash نکنید**

- اگر در حال راه‌اندازی یک بومی‌سازی (localization) یا انتشار مستندات برای یک نسخه جدید هستید،
  و شاخه‌ای را ادغام می‌کنید که از fork یک کاربر نیست، _هرگز کامیت‌ها را squash نکنید_.
  squash نکردن ضروری است، زیرا باید تاریخچه کامیت‌های آن فایل‌ها را حفظ کنید.

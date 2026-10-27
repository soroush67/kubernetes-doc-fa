---
title: مشارکت در SIG Docs
content_type: concept
weight: 60
card:
  name: contribute
  weight: 60
no_list: true
---

<!-- overview -->

SIG Docs یکی از
[گروه‌های ویژه علاقه‌مند (special interest groups)](https://github.com/kubernetes/community/blob/main/sig-list.md)
در پروژه کوبرنتیز است که بر نوشتن، به‌روزرسانی و نگهداری
مستندات کوبرنتیز به‌عنوان یک کل تمرکز دارد. برای اطلاعات بیشتر درباره این گروه، به
[SIG Docs در مخزن گیت‌هاب جامعه](https://github.com/kubernetes/community/tree/main/sig-docs)
مراجعه کنید.

SIG Docs از محتوا و بازبینی‌های همه مشارکت‌کنندگان استقبال می‌کند. هر کسی می‌تواند یک
pull request (PR) باز کند و هر کسی می‌تواند درباره محتوا issue ثبت کند یا
برای pull requestهای در حال انجام نظر بگذارد.

همچنین می‌توانید [عضو (member)](/docs/contribute/participate/roles-and-responsibilities/#members)،
[بازبین (reviewer)](/docs/contribute/participate/roles-and-responsibilities/#reviewers) یا
[تأییدکننده (approver)](/docs/contribute/participate/roles-and-responsibilities/#approvers) شوید.
این نقش‌ها به سطح دسترسی بیشتری نیاز دارند و مسئولیت‌هایی را برای
تأیید و ثبت تغییرات به همراه دارند. برای اطلاعات بیشتر درباره نحوه عملکرد عضویت در جامعه کوبرنتیز، به
[community-membership](https://github.com/kubernetes/community/blob/main/community-membership.md)
مراجعه کنید.

ادامه این سند به شیوه‌های خاصی می‌پردازد که این نقش‌ها در
SIG Docs عمل می‌کنند؛ گروهی که مسئول نگهداری یکی از عمومی‌ترین
بخش‌های کوبرنتیز، یعنی وب‌سایت و مستندات کوبرنتیز، است.

<!-- body -->

## رئیس SIG Docs {#sig-docs-chairperson}

هر SIG، از جمله SIG Docs، یک یا چند نفر از اعضای SIG را برای ایفای نقش
رئیس برمی‌گزیند. این افراد نقاط ارتباطی میان SIG Docs و سایر بخش‌های
سازمان کوبرنتیز هستند. آن‌ها باید دانش گسترده‌ای از ساختار
پروژه کوبرنتیز به‌عنوان یک کل و نحوه عملکرد SIG Docs در آن داشته باشند. برای مشاهده فهرست فعلی روسا،
به [Leadership](https://github.com/kubernetes/community/tree/main/sig-docs#leadership)
مراجعه کنید.

## تیم‌ها و خودکارسازی SIG Docs

خودکارسازی در SIG Docs به دو سازوکار متفاوت متکی است:
تیم‌های GitHub و فایل‌های OWNERS.

### تیم‌های GitHub

دو دسته [تیم](https://github.com/orgs/kubernetes/teams?query=sig-docs) SIG Docs در GitHub وجود دارد:

- `@sig-docs-{language}-owners` تأییدکنندگان و سرپرستان هستند
- `@sig-docs-{language}-reviews` بازبین‌ها هستند

هر یک از آن‌ها را می‌توان با `@name` در نظرهای GitHub مطرح کرد تا با
همه اعضای آن گروه ارتباط برقرار شود.

گاهی تیم‌های Prow و GitHub با هم همپوشانی دارند، بی‌آنکه دقیقاً یکسان باشند. برای
تخصیص issueها و pull requestها و برای پشتیبانی از تأیید PRها، خودکارسازی
از اطلاعات فایل‌های `OWNERS` استفاده می‌کند.

### فایل‌های OWNERS و front-matter

پروژه کوبرنتیز از ابزار خودکارسازی به نام prow برای خودکارسازی
مرتبط با issueها و pull requestهای GitHub استفاده می‌کند.
[مخزن وب‌سایت کوبرنتیز](https://github.com/kubernetes/website) از
دو [افزونه prow](https://github.com/kubernetes-sigs/prow/tree/main/pkg/plugins) استفاده می‌کند:

- blunderbuss
- approve

این دو افزونه از فایل‌های
[OWNERS](https://github.com/kubernetes/website/blob/main/OWNERS) و
[OWNERS_ALIASES](https://github.com/kubernetes/website/blob/main/OWNERS_ALIASES)
در سطح بالای مخزن GitHub با نام `kubernetes/website` استفاده می‌کنند تا
نحوه کار prow را در این مخزن کنترل کنند.

یک فایل OWNERS شامل فهرستی از افرادی است که بازبین‌ها و تأییدکنندگان SIG Docs هستند. فایل‌های OWNERS
می‌توانند در زیرپوشه‌ها نیز وجود داشته باشند و مشخص کنند چه کسانی می‌توانند به‌عنوان بازبین یا تأییدکننده
فایل‌های آن زیرپوشه و زیرمجموعه‌های آن عمل کنند. برای اطلاعات بیشتر درباره فایل‌های OWNERS به‌طور کلی، به
[OWNERS](https://github.com/kubernetes/community/blob/main/contributors/guide/owners.md) مراجعه کنید.

علاوه بر این، یک فایل Markdown منفرد می‌تواند بازبین‌ها و تأییدکنندگان را در
front-matter خود فهرست کند، چه با فهرست کردن نام‌های کاربری GitHub و چه گروه‌های GitHub.

ترکیب فایل‌های OWNERS و front-matter در فایل‌های Markdown تعیین می‌کند
سامانه‌های خودکار به صاحبان PR چه توصیه‌ای درباره درخواست بازبینی فنی
و ویرایشی برای PR آن‌ها ارائه دهند.

## نحوه عملکرد ادغام (merge)

وقتی یک pull request در شاخه‌ای که برای انتشار محتوا استفاده می‌شود ادغام شود، آن محتوا در https://kubernetes.io منتشر می‌شود. برای اطمینان از اینکه
کیفیت محتوای منتشرشده بالا است، ادغام pull requestها را به
تأییدکنندگان SIG Docs محدود می‌کنیم. روند کار به این صورت است.

- وقتی یک pull request هر دو برچسب `lgtm` و `approve` را داشته باشد، برچسب `hold`
  نداشته باشد و همه آزمون‌ها موفق باشند، pull request به‌صورت خودکار ادغام می‌شود.
- اعضای سازمان کوبرنتیز و تأییدکنندگان SIG Docs می‌توانند با افزودن نظر
  از ادغام خودکار یک pull request مشخص جلوگیری کنند (با افزودن نظر `/hold`
  یا خودداری از افزودن نظر `/lgtm`).
- هر عضو کوبرنتیز می‌تواند با افزودن نظر `/lgtm` برچسب `lgtm` را اضافه کند.
- فقط تأییدکنندگان SIG Docs می‌توانند با افزودن نظر `/approve` یک pull request را
  ادغام کنند. برخی تأییدکنندگان نقش‌های ویژه دیگری نیز بر عهده دارند،
  مانند [PR Wrangler](/docs/contribute/participate/pr-wranglers/) یا
  [رئیس SIG Docs](#sig-docs-chairperson).



## {{% heading "whatsnext" %}}

برای آگاهی بیشتر درباره مشارکت در SIG Docs، به این موارد مراجعه کنید:

- [نقش‌ها و مسئولیت‌ها](/docs/contribute/participate/roles-and-responsibilities/)
- [Issue wranglerها](/docs/contribute/participate/issue-wrangler/)
- [PR wranglerها](/docs/contribute/participate/pr-wranglers/)

برای اطلاعات بیشتر درباره مشارکت در مستندات کوبرنتیز، به این موارد مراجعه کنید:

- [مشارکت با محتوای جدید](/docs/contribute/new-content/)
- [بازبینی محتوا](/docs/contribute/review/reviewing-prs)
- [راهنمای سبک نگارش مستندات](/docs/contribute/style/)

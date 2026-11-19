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

‏SIG Docs یکی از [گروه‌های ذی‌نفع ویژه (special interest groups)](https://github.com/kubernetes/community/blob/main/sig-list.md)
در پروژه کوبرنتیز است که بر نوشتن، به‌روزرسانی و نگهداری کل مستندات کوبرنتیز
تمرکز دارد. برای کسب اطلاعات بیشتر درباره این گروه، صفحه
[SIG Docs در مخزن github جامعه](https://github.com/kubernetes/community/tree/main/sig-docs)
را ببینید.

گروه SIG Docs از محتوا و بازبینی‌های همه مشارکت‌کنندگان استقبال می‌کند. هر کسی
می‌تواند یک درخواست ادغام (pull request یا PR) باز کند و همه می‌توانند درباره
محتوا issue ثبت کنند یا روی درخواست‌های ادغامِ در حال بررسی نظر بگذارند.

شما همچنین می‌توانید [عضو](/docs/contribute/participate/roles-and-responsibilities/#members)،
[بازبین](/docs/contribute/participate/roles-and-responsibilities/#reviewers) یا
[تأییدکننده](/docs/contribute/participate/roles-and-responsibilities/#approvers) شوید.
این نقش‌ها به دسترسی بیشتری نیاز دارند و مسئولیت‌های مشخصی را برای تأیید و
ثبت تغییرات به همراه دارند. برای کسب اطلاعات بیشتر درباره نحوه عضویت در جامعه
کوبرنتیز، صفحه
[عضویت در جامعه](https://github.com/kubernetes/community/blob/main/community-membership.md)
را ببینید.

ادامه این سند برخی از شیوه‌های منحصربه‌فرد عملکرد این نقش‌ها را در SIG Docs شرح
می‌دهد؛ گروهی که مسئولیت نگهداری یکی از عمومی‌ترین جنبه‌های کوبرنتیز، یعنی
وب‌سایت و مستندات کوبرنتیز، را بر عهده دارد.

<!-- body -->

## رئیس SIG Docs

هر SIG، از جمله SIG Docs، یک یا چند نفر از اعضای خود را به‌عنوان رئیس انتخاب
می‌کند. این افراد نقطه ارتباط میان SIG Docs و سایر بخش‌های سازمان کوبرنتیز
هستند. آن‌ها باید شناخت گسترده‌ای از ساختار کل پروژه کوبرنتیز و نحوه فعالیت
SIG Docs در آن داشته باشند. برای مشاهده فهرست فعلی رؤسا، صفحه
[رهبری](https://github.com/kubernetes/community/tree/main/sig-docs#leadership)
را ببینید.

## تیم‌ها و خودکارسازی در SIG Docs

خودکارسازی در SIG Docs بر دو سازوکار متفاوت تکیه دارد:
تیم‌های GitHub و فایل‌های OWNERS.

### تیم‌های GitHub

دو دسته از [تیم‌های](https://github.com/orgs/kubernetes/teams?query=sig-docs) SIG Docs در GitHub وجود دارد:

- ‏`@sig-docs-{language}-owners` شامل تأییدکنندگان و راهبران است
- ‏`@sig-docs-{language}-reviews` شامل بازبینان است

برای ارتباط با همه اعضای هر یک از این گروه‌ها، می‌توان در نظرهای GitHub با
`@name` به آن گروه اشاره کرد.

گاهی تیم‌های Prow و GitHub با هم هم‌پوشانی دارند، اما دقیقاً منطبق نیستند.
سازوکار خودکارسازی برای واگذاری issueها و درخواست‌های ادغام و نیز پشتیبانی از
تأیید PRها، از اطلاعات فایل‌های `OWNERS` استفاده می‌کند.

### فایل‌های OWNERS و front-matter

پروژه کوبرنتیز برای خودکارسازی کارهای مربوط به issueها و درخواست‌های ادغام در
GitHub از ابزاری به نام prow استفاده می‌کند.
[مخزن وب‌سایت کوبرنتیز](https://github.com/kubernetes/website) از
دو [افزونه prow](https://github.com/kubernetes-sigs/prow/tree/main/pkg/plugins) استفاده می‌کند:

- blunderbuss
- approve

این دو افزونه از فایل‌های
[OWNERS](https://github.com/kubernetes/website/blob/main/OWNERS) و
[OWNERS_ALIASES](https://github.com/kubernetes/website/blob/main/OWNERS_ALIASES)
در سطح بالای مخزن GitHub ‏`kubernetes/website` برای کنترل نحوه عملکرد prow در
این مخزن استفاده می‌کنند.

هر فایل OWNERS فهرستی از افرادی را در بر دارد که بازبین و تأییدکننده SIG Docs
هستند. فایل‌های OWNERS می‌توانند در زیرشاخه‌ها نیز وجود داشته باشند و تعیین
کنند که چه کسانی بازبین یا تأییدکننده فایل‌های آن زیرشاخه و زیرشاخه‌های فرزند
آن باشند. برای کسب اطلاعات بیشتر درباره فایل‌های OWNERS به‌طور کلی، صفحه
[OWNERS](https://github.com/kubernetes/community/blob/main/contributors/guide/owners.md)
را ببینید.

افزون بر این، هر فایل Markdown می‌تواند در بخش front-matter خود بازبینان و
تأییدکنندگان را فهرست کند؛ چه با ذکر نام کاربری افراد در GitHub و چه با ذکر
گروه‌های GitHub.

ترکیب فایل‌های OWNERS و front-matter فایل‌های Markdown تعیین می‌کند که سامانه‌های
خودکار به صاحبان PRها پیشنهاد دهند برای بازبینی فنی و ویرایشی PR خود از چه
کسانی درخواست کنند.

## ادغام چگونه انجام می‌شود

وقتی یک درخواست ادغام در شاخه‌ای که برای انتشار محتوا استفاده می‌شود ادغام شود،
آن محتوا در https://kubernetes.io منتشر می‌شود. برای اطمینان از کیفیت بالای
محتوای منتشرشده، ادغام درخواست‌ها را به تأییدکنندگان SIG Docs محدود کرده‌ایم.
این فرایند به شرح زیر است:

- وقتی یک درخواست ادغام هر دو برچسب `lgtm` و `approve` را داشته باشد، هیچ برچسب
  `hold` نداشته باشد و همه آزمون‌ها را با موفقیت بگذراند، به‌طور خودکار ادغام
  می‌شود.
- اعضای سازمان کوبرنتیز و تأییدکنندگان SIG Docs می‌توانند با افزودن نظر، از
  ادغام خودکار یک درخواست ادغام جلوگیری کنند (با افزودن نظر `/hold` یا خودداری
  از افزودن نظر `/lgtm`).
- هر عضو کوبرنتیز می‌تواند با افزودن نظر `/lgtm` برچسب `lgtm` را اضافه کند.
- تنها تأییدکنندگان SIG Docs می‌توانند با افزودن نظر `/approve` یک درخواست ادغام
  را ادغام کنند. برخی از تأییدکنندگان نقش‌های مشخص دیگری نیز بر عهده دارند؛ مانند
  [مدیر PRها (PR Wrangler)](/docs/contribute/participate/pr-wranglers/) یا
  [رئیس SIG Docs](#sig-docs-chairperson).



## {{% heading "whatsnext" %}}

برای کسب اطلاعات بیشتر درباره مشارکت در SIG Docs، صفحه‌های زیر را ببینید:

- [نقش‌ها و مسئولیت‌ها](/docs/contribute/participate/roles-and-responsibilities/)
- [مدیران issueها](/docs/contribute/participate/issue-wrangler/)
- [مدیران PRها](/docs/contribute/participate/pr-wranglers/)

برای کسب اطلاعات بیشتر درباره مشارکت در مستندات کوبرنتیز، صفحه‌های زیر را ببینید:

- [مشارکت با محتوای جدید](/docs/contribute/new-content/)
- [بازبینی محتوا](/docs/contribute/review/reviewing-prs)
- [راهنمای سبک نگارش مستندات](/docs/contribute/style/)

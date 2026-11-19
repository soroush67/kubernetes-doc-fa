---
title: مدیران ایشوها (Issue Wranglers)
content_type: concept
weight: 20
---

<!-- overview -->

در کنار [مدیر PRها](/docs/contribute/participate/pr-wranglers)، تأییدکنندگان رسمی،
بازبینان و اعضای SIG Docs در نوبت‌های یک‌هفته‌ای مسئولیت
[تریاژ و دسته‌بندی ایشوهای](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
مخزن را بر عهده می‌گیرند.

<!-- body -->

## وظایف

مدیر ایشوها در هر روز از نوبت یک‌هفته‌ای خود مسئول کارهای زیر است:

- تریاژ و برچسب‌گذاری روزانهٔ ایشوهای جدید. برای آشنایی با رهنمودهای نحوهٔ استفادهٔ SIG Docs از فراداده‌ها،
  به [تریاژ و دسته‌بندی ایشوها](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
  مراجعه کنید.
- زیر نظر داشتن ایشوهای کهنه (stale) و فرسوده (rotten) در مخزن kubernetes/website.
- نگهداری [برد ایشوها](https://github.com/orgs/kubernetes/projects/72/views/1).

## الزامات

- باید عضو فعال سازمان کوبرنتیز باشد.
- دست‌کم ۱۵ مشارکت [غیرجزئی](https://www.kubernetes.dev/docs/guide/pull-requests/#trivial-edits)
  در کوبرنتیز داشته باشد (که بخشی از آن‌ها باید مربوط به مخزن kubernetes/website باشد).
- هم‌اکنون نیز این نقش را به‌صورت غیررسمی انجام دهد.

## دستورهای مفید Prow برای مدیران ایشوها

در ادامه برخی از دستورهای پرکاربرد برای مدیران ایشوها آمده است:

```bash
# reopen an issue
/reopen

# transfer issues that don't fit in k/website to another repository
/transfer[-issue]

# change the state of rotten issues
/remove-lifecycle rotten

# change the state of stale issues
/remove-lifecycle stale

# assign sig to an issue
/sig <sig_name>

# add specific area
/area <area_name>

# for beginner friendly issues
/good-first-issue

# issues that needs help
/help wanted

# tagging issue as support specific
/kind support

# to accept triaging for an issue
/triage accepted

# closing an issue we won't be working on and haven't fixed yet
/close not-planned
```

برای یافتن دستورهای بیشتر Prow، به مستندات [راهنمای دستورها](https://prow.k8s.io/command-help) مراجعه کنید.

## چه زمانی ایشوها را ببندیم

مدیریت درست ایشوها برای موفقیت هر پروژهٔ متن‌باز اهمیتی حیاتی دارد.
با این حال، حل‌وفصل ایشوها نیز برای نگهداری مخزن و برقراری ارتباط روشن با
مشارکت‌کنندگان و کاربران ضروری است.

در موارد زیر ایشوها را ببندید:

- ایشوی مشابهی بیش از یک بار گزارش شده باشد. در این حالت ابتدا باید آن را با `/triage duplicate` برچسب‌گذاری کنید،
  سپس آن را به ایشوی اصلی پیوند دهید و در پایان ببندید. توصیه می‌شود کاربران را نیز به ایشوی اصلی راهنمایی کنید.
- درک و رسیدگی به ایشوی مطرح‌شده از سوی نویسنده با اطلاعات ارائه‌شده بسیار دشوار باشد.
  با این حال، کاربر را تشویق کنید جزئیات بیشتری ارائه دهد یا اگر بعدها توانست مشکل را بازتولید کند، ایشو را دوباره باز کند.
- همین قابلیت در جای دیگری پیاده‌سازی شده باشد. در این صورت می‌توان ایشو را بست و کاربر را به محل مناسب راهنمایی کرد.
- ایشوی گزارش‌شده در حال حاضر در برنامهٔ پروژه نباشد یا با اهداف پروژه هم‌راستا نباشد.
- ایشو هرزنامه به نظر برسد و آشکارا بی‌ارتباط باشد.
- ایشو به محدودیت یا وابستگی‌ای بیرونی مربوط باشد و از کنترل پروژه خارج باشد.

برای بستن یک ایشو، دیدگاهی با محتوای `/close` روی آن بگذارید.

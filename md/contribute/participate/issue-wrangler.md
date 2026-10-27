---
title: Issue Wranglers
content_type: concept
weight: 20
---

<!-- overview -->

در کنار [PR Wrangler](/docs/contribute/participate/pr-wranglers)، تأییدکنندگان (approvers)، بازبینان (reviewers) و اعضای رسمی SIG Docs به‌صورت نوبت‌های یک‌هفته‌ای،
[بررسی اولیه و دسته‌بندی issueها](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
را برای مخزن انجام می‌دهند.

<!-- body -->

## وظایف

در هر روز از نوبت یک‌هفته‌ای، Issue Wrangler مسئول موارد زیر است:

- بررسی اولیه و برچسب‌گذاری issueهای جدید به‌صورت روزانه. برای آشنایی با راهنمای نحوهٔ استفادهٔ SIG Docs از فراداده‌ها (metadata)، به
  [بررسی اولیه و دسته‌بندی issueها](/docs/contribute/review/for-approvers/#triage-and-categorize-issues)
  مراجعه کنید.
- پایش issueهای کهنه (stale) و فرسوده (rotten) در مخزن kubernetes/website.
- نگهداری [برد Issues](https://github.com/orgs/kubernetes/projects/72/views/1).

## الزامات

- باید عضو فعال سازمان کوبرنتیز باشد.
- حداقل ۱۵ مشارکت [غیرپیش‌پاافتاده](https://www.kubernetes.dev/docs/guide/pull-requests/#trivial-edits)
  در کوبرنتیز داشته باشد (که بخشی از آن‌ها باید به kubernetes/website اختصاص یافته باشد).
- هم‌اکنون این نقش را به‌صورت غیررسمی ایفا کرده باشد.

## دستورهای کاربردی Prow برای wranglerها

در ادامه چند دستور پرکاربرد برای Issue Wranglerها آمده است:

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

برای یافتن دستورهای بیشتر Prow، به مستندات [Command Help](https://prow.k8s.io/command-help) مراجعه کنید.

## زمان بستن Issueها

برای موفقیت یک پروژهٔ متن‌باز، مدیریت درست issueها حیاتی است.
اما حل‌وفصل issueها نیز برای نگهداری مخزن
و برقراری ارتباط روشن با مشارکت‌کنندگان و کاربران اهمیت بسیار دارد.

issueها را در موارد زیر ببندید:

- یک issue مشابه بیش از یک بار گزارش شده باشد. ابتدا باید آن را با `/triage duplicate` برچسب‌گذاری کنید؛
  سپس آن را به issue اصلی پیوند دهید و بعد ببندید. همچنین توصیه می‌شود کاربران را به issue اصلی هدایت کنید.
- با اطلاعات ارائه‌شده، درک و رسیدگی به issue مطرح‌شده توسط نویسنده بسیار دشوار باشد.
  با این حال، کاربر را تشویق کنید جزئیات بیشتری ارائه دهد یا در صورتی که بعداً توانست مشکل را بازتولید کند، issue را دوباره باز کند.
- همان قابلیت در جای دیگری پیاده‌سازی شده باشد. می‌توان این issue را بست و کاربر را به مکان مناسب هدایت کرد.
- issue گزارش‌شده در حال حاضر برنامه‌ریزی نشده باشد یا با اهداف پروژه همسو نباشد.
- issue به‌وضوح هرزنامه (spam) و نامرتبط به نظر برسد.
- issue به یک محدودیت یا وابستگی خارجی مربوط باشد و خارج از کنترل پروژه باشد.

برای بستن یک issue، یک نظر با محتوای `/close` روی آن بگذارید.

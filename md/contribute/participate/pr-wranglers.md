---
title: مدیران PR
content_type: concept
weight: 20
---

<!-- overview -->

[تأییدکنندگان](/docs/contribute/participate/roles-and-responsibilities/#approvers) گروه SIG Docs
در نوبت‌های یک‌هفته‌ای، [مدیریت درخواست‌های ادغام (pull request)](https://github.com/kubernetes/website/wiki/PR-Wranglers)
مخزن را بر عهده می‌گیرند.

این بخش وظایف مدیر PR (PR wrangler) را شرح می‌دهد. برای اطلاعات بیشتر دربارهٔ انجام بازبینی‌های خوب،
[بازبینی تغییرات](/docs/contribute/review/) را ببینید.

<!-- body -->

## وظایف

در هر روز از نوبت یک‌هفته‌ای به‌عنوان مدیر PR باید:

- [درخواست‌های ادغام باز](https://github.com/kubernetes/website/pulls) را از نظر کیفیت
  و پایبندی به راهنماهای [سبک نگارش](/docs/contribute/style/style-guide/) و
  [محتوا](/docs/contribute/style/content-guide/) بازبینی کنید.
  - کار را از کوچک‌ترین PRها (`size/XS`) آغاز کنید و با بزرگ‌ترین آن‌ها (`size/XXL`) به پایان برسانید.
    تا جایی که می‌توانید PRهای بیشتری را بازبینی کنید.
- مطمئن شوید که مشارکت‌کنندگانِ PRها [CLA](https://github.com/kubernetes/community/blob/main/CLA.md) را امضا کرده‌اند.
  - با استفاده از [این](https://github.com/zparnold/k8s-docs-pr-botherer) اسکریپت، به مشارکت‌کنندگانی
    که CLA را امضا نکرده‌اند یادآوری کنید که آن را امضا کنند.
- دربارهٔ تغییرات بازخورد بدهید و از اعضای سایر SIGها درخواست بازبینی فنی کنید.
  - برای تغییرات پیشنهادی محتوا، پیشنهادهای خود را به‌صورت درون‌خطی روی PR ثبت کنید.
  - اگر لازم است محتوا را راستی‌آزمایی کنید، روی PR نظر بگذارید و جزئیات بیشتری درخواست کنید.
  - برچسب یا برچسب‌های `sig/` مرتبط را اختصاص دهید.
  - در صورت نیاز، بازبین‌ها را از بلوک `reviewers:` در front matter فایل تعیین کنید.
  - همچنین می‌توانید با نوشتن نظر `@kubernetes/<sig>-pr-reviews` روی PR، یک
    [SIG](https://github.com/kubernetes/community/blob/main/sig-list.md) را برای بازبینی فرابخوانید.
- برای تأیید ادغام یک PR از نظر `/approve` استفاده کنید. وقتی PR آماده شد، آن را ادغام کنید.
  - هر PR پیش از ادغام باید نظر `/lgtm` را از عضو دیگری دریافت کرده باشد.
  - پذیرفتن محتوایی را که از نظر فنی دقیق است اما با
    [رهنمودهای سبک نگارش](/docs/contribute/style/style-guide/) مطابقت ندارد در نظر بگیرید. هنگام تأیید تغییر،
    یک issue جدید برای رسیدگی به مشکل سبک نگارش باز کنید. معمولاً می‌توانید این issueهای اصلاح سبک را
    به‌صورت [issueهای مناسب برای شروع (good first issue)](https://kubernetes.dev/docs/guide/help-wanted/#good-first-issue) بنویسید.
  - استفاده از اصلاحات سبک نگارش به‌عنوان issueهای مناسب برای شروع، راه خوبی برای فراهم کردن
    کارهای ساده‌تر است و به ورود مشارکت‌کنندگان جدید کمک می‌کند.
- درخواست‌های ادغامی را که روی کد [مولد مستندات مرجع](https://github.com/kubernetes-sigs/reference-docs)
  ثبت شده‌اند نیز بررسی و بازبینی کنید (یا از دیگران کمک بگیرید).
- از [مدیر issueها](/docs/contribute/participate/issue-wrangler/) در اولویت‌بندی
  و برچسب‌گذاری روزانهٔ issueهای ورودی پشتیبانی کنید.
  برای آشنایی با رهنمودهای استفادهٔ SIG Docs از فراداده‌ها،
  [اولویت‌بندی و دسته‌بندی issueها](/docs/contribute/review/for-approvers/#triage-and-categorize-issues) را ببینید.

{{< note >}}
وظایف مدیر PR شامل PRهای بومی‌سازی (PRهای غیرانگلیسی) نمی‌شود.
تیم‌های بومی‌سازی فرایندها و تیم‌های خاص خود را برای بازبینی PRهای زبان خود دارند.
با این حال، اغلب مفید است که از برچسب‌گذاری درست PRهای زبان‌ها اطمینان حاصل کنید،
PRهای کوچکی را که به زبان وابسته نیستند (مانند به‌روزرسانی یک پیوند) بازبینی کنید،
یا بازبین‌ها و مشارکت‌کنندگان را در PRهای طولانی‌مدت
(PRهایی که بیش از ۶ ماه پیش باز شده‌اند و یک ماه یا بیشتر به‌روزرسانی نشده‌اند) فرابخوانید.
{{< /note >}}

### کوئری‌های مفید GitHub برای مدیران PR

کوئری‌های زیر هنگام مدیریت PRها مفید هستند.
پس از بررسی این کوئری‌ها، فهرست باقی‌ماندهٔ PRها برای بازبینی معمولاً کوتاه است.
این کوئری‌ها PRهای بومی‌سازی را شامل نمی‌شوند. همهٔ کوئری‌ها به‌جز آخرین مورد روی شاخهٔ main اجرا می‌شوند.

- [بدون CLA، فاقد شرایط ادغام](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+label%3A%22cncf-cla%3A+no%22+-label%3A%22do-not-merge%2Fwork-in-progress%22+-label%3A%22do-not-merge%2Fhold%22+label%3Alanguage%2Fen):
  به مشارکت‌کننده یادآوری کنید که CLA را امضا کند. اگر هم ربات و هم یک انسان به او یادآوری کرده‌اند،
  PR را ببندید و به او یادآوری کنید که پس از امضای CLA می‌تواند آن را دوباره باز کند.
  **PRهایی را که نویسندگانشان CLA را امضا نکرده‌اند بازبینی نکنید!**
- [نیازمند LGTM](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+-label%3A%22cncf-cla%3A+no%22+-label%3Ado-not-merge%2Fwork-in-progress+-label%3Ado-not-merge%2Fhold+label%3Alanguage%2Fen+-label%3Algtm):
  PRهایی را فهرست می‌کند که به LGTM از سوی یک عضو نیاز دارند. اگر PR به بازبینی فنی نیاز دارد،
  یکی از بازبین‌های پیشنهادی ربات را درگیر کنید. اگر محتوا نیاز به اصلاح دارد،
  پیشنهادها و بازخوردهای خود را به‌صورت درون‌خطی اضافه کنید.
- [دارای LGTM، نیازمند تأیید مستندات](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+-label%3Ado-not-merge%2Fwork-in-progress+-label%3Ado-not-merge%2Fhold+label%3Alanguage%2Fen+label%3Algtm+):
  PRهایی را فهرست می‌کند که برای ادغام به نظر `/approve` نیاز دارند.
- [کارهای سریع](https://github.com/kubernetes/website/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Amain+-label%3A%22do-not-merge%2Fwork-in-progress%22+-label%3A%22do-not-merge%2Fhold%22+label%3A%22cncf-cla%3A+yes%22+label%3A%22size%2FXS%22+label%3A%22language%2Fen%22):
  PRهایی را فهرست می‌کند که روی شاخهٔ main ثبت شده‌اند و مانع آشکاری ندارند.
  (همزمان با پیش رفتن در بررسی PRها، مقدار «XS» را در برچسب اندازه تغییر دهید [XS, S, M, L, XL, XXL]).
- [ثبت‌شده روی شاخه‌ای غیر از شاخهٔ اصلی](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+label%3Alanguage%2Fen+-base%3Amain):
  اگر PR روی یک شاخهٔ `dev-` ثبت شده باشد، مربوط به نسخهٔ پیش رو است.
  [مدیر انتشار مستندات](https://github.com/kubernetes/sig-release/tree/master/release-team#kubernetes-release-team-roles)
  را با دستور `/assign @<manager's_github-username>` تعیین کنید. اگر PR روی یک شاخهٔ قدیمی ثبت شده باشد،
  به نویسنده کمک کنید تا مشخص کند آیا مناسب‌ترین شاخه را هدف گرفته است یا نه.

### دستورهای مفید Prow برای مدیران PR

```
# add English label
/language en

# add squash label to PR if more than one commit
/label tide/merge-method-squash

# retitle a PR via Prow (such as a work-in-progress [WIP] or better detail of PR)
/retitle [WIP] <TITLE>
```

### چه زمانی درخواست‌های ادغام را ببندیم

بازبینی‌ها و تأییدها یکی از ابزارهای کوتاه و به‌روز نگه داشتن صف PRها هستند. ابزار دیگر، بستن PRهاست.

PRهایی را ببندید که:

- نویسندهٔ آن‌ها به مدت دو هفته CLA را امضا نکرده است.

  نویسندگان می‌توانند پس از امضای CLA، PR را دوباره باز کنند. این روشی کم‌خطر برای اطمینان
  از این است که هیچ تغییری بدون CLA امضاشده ادغام نشود.

- نویسندهٔ آن‌ها به مدت ۲ هفته یا بیشتر به نظرها یا بازخوردها پاسخ نداده است.

از بستن درخواست‌های ادغام نترسید. مشارکت‌کنندگان به‌راحتی می‌توانند کارهای در جریان را دوباره باز کنند و ادامه دهند.
اغلب، همین اعلان بسته شدن است که نویسنده را به ادامه و تکمیل مشارکتش برمی‌انگیزد.

برای بستن یک درخواست ادغام، نظر `/close` را روی PR بنویسید.

{{< note >}}
ربات [`k8s-triage-robot`](https://github.com/k8s-triage-robot) پس از ۹۰ روز عدم فعالیت،
issueها را به‌عنوان کهنه (stale) علامت‌گذاری می‌کند. پس از ۳۰ روز دیگر، آن‌ها را به‌عنوان فرسوده (rotten)
علامت‌گذاری می‌کند و می‌بندد. مدیران PR باید issueها را پس از ۱۴ تا ۳۰ روز عدم فعالیت ببندند.
{{< /note >}}

## برنامهٔ همراهی مدیر PR

گروه SIG Docs در اواخر سال ۲۰۲۱ برنامهٔ همراهی مدیر PR (PR Wrangler Shadow Program) را راه‌اندازی کرد.
هدف از راه‌اندازی این برنامه، کمک به مشارکت‌کنندگان جدید برای درک فرایند مدیریت PRها بود.

### همراه شوید

- اگر به همراهی با یک مدیر PR علاقه دارید، به
  [صفحهٔ ویکی مدیران PR](https://github.com/kubernetes/website/wiki/PR-Wranglers)
  مراجعه کنید تا برنامهٔ زمانی مدیریت PRها در سال جاری را ببینید و ثبت‌نام کنید.

- دیگران می‌توانند برای درخواست همراهی با مدیر PR تعیین‌شده در یک هفتهٔ مشخص، از طریق
  [کانال Slack با نام ‎#sig-docs](https://kubernetes.slack.com/messages/sig-docs) تماس بگیرند. می‌توانید آزادانه با یکی از
  [رؤسا/رهبران مشترک SIG Docs](https://github.com/kubernetes/community/tree/main/sig-docs#leadership) تماس بگیرید.

- پس از ثبت‌نام برای همراهی با یک مدیر PR، خود را در
  [Slack کوبرنتیز](https://slack.k8s.io) به آن مدیر PR معرفی کنید.

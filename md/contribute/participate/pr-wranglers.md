---
title: PR wranglers
content_type: concept
weight: 20
---

<!-- overview -->

[تأییدکنندگان (approvers)](/docs/contribute/participate/roles-and-responsibilities/#approvers) گروه SIG Docs به‌صورت شیفت‌های یک‌هفته‌ای،
[مدیریت pull requestهای](https://github.com/kubernetes/website/wiki/PR-Wranglers) مخزن را بر عهده می‌گیرند.

این بخش وظایف یک PR wrangler را توضیح می‌دهد. برای اطلاعات بیشتر درباره‌ی نحوه‌ی انجام بازبینی‌های مناسب،
به [بازبینی تغییرات](/docs/contribute/review/) مراجعه کنید.

<!-- body -->

## وظایف {#duties}

در هر روز از شیفت یک‌هفته‌ای به‌عنوان PR Wrangler:

- [pull requestهای باز](https://github.com/kubernetes/website/pulls) را از نظر کیفیت و پایبندی به
  راهنماهای [سبک نگارش](/docs/contribute/style/style-guide/) و
  [محتوا](/docs/contribute/style/content-guide/) بازبینی کنید.
  - ابتدا با کوچک‌ترین PRها (`size/XS`) شروع کنید و با بزرگ‌ترین آن‌ها (`size/XXL`) پایان دهید.
    تا جای ممکن PRهای بیشتری را بازبینی کنید.
- اطمینان حاصل کنید که مشارکت‌کنندگان PR، [CLA](https://github.com/kubernetes/community/blob/main/CLA.md) را امضا کرده‌اند.
  - از [این](https://github.com/zparnold/k8s-docs-pr-botherer) اسکریپت برای یادآوری امضای CLA به مشارکت‌کنندگانی
    که آن را امضا نکرده‌اند استفاده کنید.
- درباره‌ی تغییرات بازخورد بدهید و از اعضای سایر SIGها درخواست بازبینی فنی کنید.
  - برای تغییرات پیشنهادی محتوا، پیشنهادهای درون‌خطی (inline) را روی PR ارائه دهید.
  - اگر نیاز به راستی‌آزمایی محتوا دارید، روی PR نظر بگذارید و جزئیات بیشتری درخواست کنید.
  - برچسب(های) `sig/` مرتبط را اختصاص دهید.
  - در صورت نیاز، از بلوک `reviewers:` در front matter فایل، بازبین‌ها را تعیین کنید.
  - همچنین می‌توانید با درج نظر `@kubernetes/<sig>-pr-reviews` روی PR، یک [SIG](https://github.com/kubernetes/community/blob/main/sig-list.md)
    را برای بازبینی فرا بخوانید.
- برای تأیید یک PR جهت ادغام (merge) از نظر `/approve` استفاده کنید. هنگامی که PR آماده بود، آن را ادغام کنید.
  - پیش از ادغام، PRها باید نظر `/lgtm` را از عضو دیگری دریافت کرده باشند.
  - پذیرش محتوایی را که از نظر فنی دقیق است اما با [رهنمودهای سبک نگارش](/docs/contribute/style/style-guide/) مطابقت ندارد، در نظر بگیرید. هنگام تأیید تغییر،
    یک issue جدید برای رفع مسئله‌ی سبک نگارش باز کنید. معمولاً می‌توانید این issueهای اصلاح سبک را
    به‌عنوان [good first issue](https://kubernetes.dev/docs/guide/help-wanted/#good-first-issue) ثبت کنید.
  - استفاده از اصلاحات سبک نگارش به‌عنوان good first issue راهی مناسب برای تأمین مداوم کارهای ساده‌تر است
    که به آشنایی مشارکت‌کنندگان جدید کمک می‌کند.
- همچنین pull requestهای مربوط به کد [تولیدکننده‌ی مستندات مرجع](https://github.com/kubernetes-sigs/reference-docs)
  را بررسی و بازبینی کنید (یا از دیگران کمک بگیرید).
- از [issue wrangler](/docs/contribute/participate/issue-wrangler/) برای
  اولویت‌بندی و برچسب‌گذاری روزانه‌ی issueهای ورودی پشتیبانی کنید.
  برای رهنمودهای نحوه‌ی استفاده‌ی SIG Docs از فراداده (metadata)، به
  [اولویت‌بندی و دسته‌بندی issueها](/docs/contribute/review/for-approvers/#triage-and-categorize-issues) مراجعه کنید.

{{< note >}}
وظایف PR wrangler شامل PRهای بومی‌سازی (PRهای غیرانگلیسی) نمی‌شود.
تیم‌های بومی‌سازی فرایندها و تیم‌های خاص خود را برای بازبینی PRهای زبان خود دارند.
با این حال، اغلب مفید است که از برچسب‌گذاری درست PRهای زبانی اطمینان حاصل کنید،
PRهای کوچکی را که به زبان وابسته نیستند (مانند به‌روزرسانی یک پیوند) بازبینی کنید،
یا بازبین‌ها و مشارکت‌کنندگان را در PRهای طولانی‌مدت برچسب بزنید
(PRهایی که بیش از ۶ ماه پیش باز شده‌اند و یک ماه یا بیشتر است که به‌روزرسانی نشده‌اند).
{{< /note >}}

### کوئری‌های مفید GitHub برای wranglerها {#helpful-github-queries-for-wranglers}

کوئری‌های زیر هنگام انجام وظایف wrangler مفیدند.
پس از بررسی این کوئری‌ها، فهرست باقی‌مانده‌ی PRها برای بازبینی معمولاً کوتاه است.
این کوئری‌ها PRهای بومی‌سازی را شامل نمی‌شوند. همه‌ی کوئری‌ها، به‌جز آخرین مورد، روی شاخه‌ی main اجرا می‌شوند.

- [بدون CLA، واجد شرایط ادغام نیست](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+label%3A%22cncf-cla%3A+no%22+-label%3A%22do-not-merge%2Fwork-in-progress%22+-label%3A%22do-not-merge%2Fhold%22+label%3Alanguage%2Fen):
  به مشارکت‌کننده یادآوری کنید که CLA را امضا کند. اگر هم ربات و هم یک انسان به او یادآوری کرده باشند،
  PR را ببندید و به او یادآوری کنید که پس از امضای CLA می‌تواند آن را دوباره باز کند.
  **PRهایی را که نویسندگانشان CLA را امضا نکرده‌اند بازبینی نکنید!**
- [نیازمند LGTM](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+-label%3A%22cncf-cla%3A+no%22+-label%3Ado-not-merge%2Fwork-in-progress+-label%3Ado-not-merge%2Fhold+label%3Alanguage%2Fen+-label%3Algtm):
  PRهایی را فهرست می‌کند که به LGTM از یک عضو نیاز دارند. اگر PR به بازبینی فنی نیاز دارد،
  یکی از بازبین‌های پیشنهادی ربات را وارد گفتگو کنید. اگر محتوا نیاز به اصلاح دارد،
  پیشنهادها و بازخوردها را به‌صورت درون‌خطی اضافه کنید.
- [دارای LGTM، نیازمند تأیید مستندات](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+-label%3Ado-not-merge%2Fwork-in-progress+-label%3Ado-not-merge%2Fhold+label%3Alanguage%2Fen+label%3Algtm+):
  PRهایی را فهرست می‌کند که برای ادغام به نظر `/approve` نیاز دارند.
- [موفقیت‌های سریع (Quick Wins)](https://github.com/kubernetes/website/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aopen+base%3Amain+-label%3A%22do-not-merge%2Fwork-in-progress%22+-label%3A%22do-not-merge%2Fhold%22+label%3A%22cncf-cla%3A+yes%22+label%3A%22size%2FXS%22+label%3A%22language%2Fen%22):
  PRهای روی شاخه‌ی main را که مانع آشکاری ندارند فهرست می‌کند.
  (هنگام بررسی PRها، «XS» را در برچسب اندازه تغییر دهید [XS, S, M, L, XL, XXL]).
- [غیر از شاخه‌ی اصلی](https://github.com/kubernetes/website/pulls?q=is%3Aopen+is%3Apr+label%3Alanguage%2Fen+-base%3Amain):
  اگر PR روی یک شاخه‌ی `dev-` باشد، مربوط به نسخه‌ی پیش‌رو است. با دستور
  `/assign @<manager's_github-username>`
  [مدیر انتشار مستندات](https://github.com/kubernetes/sig-release/tree/master/release-team#kubernetes-release-team-roles)
  را تعیین کنید. اگر PR روی یک شاخه‌ی قدیمی باشد،
  به نویسنده کمک کنید تشخیص دهد که آیا شاخه‌ی هدف مناسب‌ترین گزینه است یا خیر.

### دستورهای مفید Prow برای wranglerها {#helpful-prow-commands-for-wranglers}

```
# add English label
/language en

# add squash label to PR if more than one commit
/label tide/merge-method-squash

# retitle a PR via Prow (such as a work-in-progress [WIP] or better detail of PR)
/retitle [WIP] <TITLE>
```

### زمان بستن Pull Requestها {#when-to-close-pull-requests}

بازبینی و تأیید ابزارهایی برای کوتاه و به‌روز نگه‌داشتن صف PRها هستند. ابزار دیگر، بستن PR است.

PRهایی را ببندید که:

- نویسنده به مدت دو هفته CLA را امضا نکرده است.

  نویسندگان می‌توانند پس از امضای CLA، PR را دوباره باز کنند. این روشی کم‌خطر است برای
  اطمینان از اینکه هیچ چیزی بدون CLA امضاشده ادغام نمی‌شود.

- نویسنده به مدت ۲ هفته یا بیشتر به نظرات یا بازخوردها پاسخ نداده است.

از بستن pull requestها نترسید. مشارکت‌کنندگان به‌سادگی می‌توانند آن‌ها را دوباره باز کنند و کار در دست انجام را از سر بگیرند.
اغلب اعلان بسته‌شدن، انگیزه‌ای است تا نویسنده کار خود را از سر بگیرد و مشارکتش را به پایان برساند.

برای بستن یک pull request، نظر `/close` را روی PR بگذارید.

{{< note >}}
ربات [`k8s-triage-robot`](https://github.com/k8s-triage-robot) پس از ۹۰ روز عدم فعالیت، issueها را
به‌عنوان stale علامت‌گذاری می‌کند. پس از ۳۰ روز دیگر، آن‌ها را rotten علامت می‌زند
و می‌بندد. PR wranglerها باید issueها را پس از ۱۴ تا ۳۰ روز عدم فعالیت ببندند.
{{< /note >}}

## برنامه‌ی سایه‌ی PR Wrangler (PR Wrangler shadow program) {#pr-wrangler-shadow-program}

در اواخر سال ۲۰۲۱، SIG Docs برنامه‌ی PR Wrangler Shadow را معرفی کرد.
هدف از این برنامه کمک به مشارکت‌کنندگان جدید برای درک فرایند مدیریت PRها بود.

### تبدیل شدن به سایه (shadow) {#become-a-shadow}

- اگر علاقه‌مندید به‌عنوان سایه‌ی یک PR wrangler فعالیت کنید، لطفاً به
  [صفحه‌ی ویکی PR Wranglers](https://github.com/kubernetes/website/wiki/PR-Wranglers)
  مراجعه کنید تا برنامه‌ی زمانی PR wrangling امسال را ببینید و ثبت‌نام کنید.

- سایر افراد می‌توانند از طریق [کانال Slack با نام #sig-docs](https://kubernetes.slack.com/messages/sig-docs)
  درخواست دهند که در یک هفته‌ی مشخص، سایه‌ی یک PR Wrangler تعیین‌شده باشند. می‌توانید با یکی از
  [هم‌رئیس‌ها/سرپرستان SIG Docs](https://github.com/kubernetes/community/tree/main/sig-docs#leadership) نیز تماس بگیرید.

- پس از ثبت‌نام برای سایه‌بودن در کنار یک PR Wrangler، در
  [Slack کوبرنتیز](https://slack.k8s.io) خود را به آن PR Wrangler معرفی کنید.

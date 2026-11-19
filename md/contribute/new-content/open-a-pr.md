---
title: باز کردن درخواست ادغام (Pull Request)
content_type: concept
weight: 10
card:
  name: contribute
  weight: 40
---

<!-- overview -->

{{< note >}}
**توسعه‌دهندگان کد**: اگر برای یکی از نسخه‌های آیندهٔ کوبرنتیز قابلیت جدیدی را مستند می‌کنید،
به [مستندسازی یک قابلیت جدید](/docs/contribute/new-content/new-features/) مراجعه کنید.
{{< /note >}}

برای افزودن صفحه‌های محتوایی جدید یا بهبود صفحه‌های موجود، یک درخواست ادغام (pull request یا PR) باز کنید.
مطمئن شوید که همهٔ الزامات بخش [پیش از شروع](/docs/contribute/new-content/) را رعایت کرده‌اید.

اگر تغییر شما کوچک است یا با git آشنایی ندارید، برای آشنایی با نحوهٔ ویرایش یک صفحه، بخش
[تغییرات با استفاده از GitHub](#changes-using-github) را بخوانید.

اگر تغییرات شما گسترده است، برای آشنایی با نحوهٔ اعمال تغییرات به‌صورت محلی روی رایانهٔ خود، بخش
[کار از طریق یک فورک محلی](#fork-the-repo) را بخوانید.

<!-- body -->

## تغییرات با استفاده از GitHub

اگر تجربهٔ کمتری با گردش‌کارهای git دارید، روش ساده‌تری برای باز کردن درخواست ادغام وجود دارد.
شکل ۱ مراحل کار را به‌طور خلاصه نشان می‌دهد و جزئیات هر مرحله در ادامه آمده است.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
A([fa:fa-user مشارکت‌کنندهٔ<br>جدید]) --- id1[(مخزن kubernetes/website<br>در GitHub)]
subgraph tasks[تغییرات با استفاده از GitHub]
direction TB
    0[ ] -.-
    1[۱. ویرایش این صفحه] --> 2[۲. استفاده از ویرایشگر مارک‌داون<br>GitHub برای اعمال تغییرات]
    2 --> 3[۳. انتخاب Commit changes...]

end
subgraph tasks2[ ]
direction TB
4[۴. انتخاب Propose changes] --> 5[۵. انتخاب Create pull request] --> 6[۶. تکمیل فرم Open a pull request]
6 --> 7[۷. انتخاب Create pull request] 
end

id1 --> tasks --> tasks2

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class A,1,2,3,4,5,6,7 grey
class 0 spacewhite
class tasks,tasks2 white
class id1 k8s
{{</ mermaid >}}

شکل ۱. مراحل باز کردن درخواست ادغام با استفاده از GitHub.

1. در صفحه‌ای که مشکل را در آن مشاهده کرده‌اید، گزینهٔ **Edit this page** را از پنل پیمایش سمت راست انتخاب کنید.

1. تغییرات خود را در ویرایشگر مارک‌داون GitHub اعمال کنید.

1. در سمت راست و بالای ویرایشگر، گزینهٔ **Commit changes** را انتخاب کنید.
   در فیلد اول، عنوانی برای پیام کامیت خود بنویسید.
   در فیلد دوم، توضیحاتی ارائه دهید.

   {{< note >}}
   در پیام کامیت خود از هیچ‌یک از [کلیدواژه‌های GitHub](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
   استفاده نکنید. می‌توانید بعداً آن‌ها را به توضیحات درخواست ادغام اضافه کنید.
   {{< /note >}}

1. گزینهٔ **Propose changes** را انتخاب کنید.

1. گزینهٔ **Create pull request** را انتخاب کنید.

1. صفحهٔ **Open a pull request** نمایش داده می‌شود. فرم را تکمیل کنید:

   - فیلد **Add a title** در درخواست ادغام به‌طور پیش‌فرض با خلاصهٔ کامیت پر می‌شود.
     در صورت نیاز می‌توانید آن را تغییر دهید.
   - فیلد **Add a description** شامل پیام کامیت تفصیلی شما (در صورت وجود) و مقداری متن قالب است.
     جزئیاتی را که متن قالب درخواست می‌کند اضافه کنید و سپس متن اضافی قالب را حذف کنید.
   - کادر انتخاب **Allow edits from maintainers** را در حالت انتخاب‌شده باقی بگذارید.

   {{< note >}}
   توضیحات درخواست ادغام راه بسیار خوبی برای کمک به بازبین‌ها در درک تغییر شماست.
   برای اطلاعات بیشتر، به [باز کردن درخواست ادغام](#open-a-pr) مراجعه کنید.
   {{</ note >}}

1. گزینهٔ **Create pull request** را انتخاب کنید.

### رسیدگی به بازخوردها در GitHub

پیش از ادغام یک درخواست ادغام، اعضای جامعهٔ کوبرنتیز آن را بازبینی و تأیید می‌کنند.
ربات `k8s-ci-robot` بر اساس نزدیک‌ترین مالکِ ذکرشده در صفحه‌ها، بازبین‌هایی را پیشنهاد می‌کند.
اگر فرد خاصی را در نظر دارید، دیدگاهی حاوی نام کاربری GitHub او بگذارید.

اگر بازبینی از شما خواست تغییراتی اعمال کنید:

1. به زبانهٔ **Files changed** بروید.
1. روی نماد مداد (ویرایش) در هر یک از فایل‌هایی که درخواست ادغام تغییرشان داده است، کلیک کنید.
1. تغییرات درخواست‌شده را اعمال کنید.
1. تغییرات را کامیت کنید.

اگر منتظر پاسخ یک بازبین هستید، هر ۷ روز یک بار با او تماس بگیرید. همچنین می‌توانید در کانال
`#sig-docs` در Slack پیامی ارسال کنید.

پس از تکمیل بازبینی، یکی از بازبین‌ها درخواست ادغام شما را ادغام می‌کند و تغییرات شما چند دقیقه بعد منتشر می‌شوند.

## کار از طریق یک فورک محلی {#fork-the-repo}

اگر تجربهٔ بیشتری با git دارید یا تغییرات شما بیش از چند خط است، از طریق یک فورک محلی کار کنید.

مطمئن شوید که [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) روی رایانهٔ شما
نصب شده است. همچنین می‌توانید از یک برنامهٔ رابط گرافیکی برای git استفاده کنید.

شکل ۲ مراحلی را نشان می‌دهد که هنگام کار از طریق یک فورک محلی باید دنبال کنید. جزئیات هر مرحله در ادامه آمده است.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
1[فورک کردن مخزن<br>kubernetes/website] --> 2[ایجاد کلون محلی<br>و تنظیم upstream]
subgraph changes[تغییرات شما]
direction TB
S[ ] -.-
3[ایجاد یک شاخه<br>مثال: my_new_branch] --> 3a[اعمال تغییرات با<br>ویرایشگر متن] --> 4["پیش‌نمایش محلی تغییرات<br>با استفاده از Hugo<br>(localhost:1313)<br>یا ساخت ایمیج کانتینر"]
end
subgraph changes2[کامیت / پوش]
direction TB
T[ ] -.-
5[کامیت کردن تغییرات] --> 6[پوش کردن کامیت به<br>origin/my_new_branch]
end

2 --> changes --> changes2

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class 1,2,3,3a,4,5,6 grey
class S,T spacewhite
class changes,changes2 white
{{</ mermaid >}}

شکل ۲. کار از طریق یک فورک محلی برای اعمال تغییرات.

### فورک کردن مخزن kubernetes/website

1. به مخزن [`kubernetes/website`](https://github.com/kubernetes/website/) بروید.
1. گزینهٔ **Fork** را انتخاب کنید.

### ایجاد یک کلون محلی و تنظیم upstream

1. در یک پنجرهٔ ترمینال، فورک خود را کلون کنید و [پوستهٔ Docsy Hugo](https://github.com/google/docsy#readme) را به‌روزرسانی کنید:

   ```shell
   git clone git@github.com:<github_username>/website
   cd website
   ```

1. به پوشهٔ جدید `website` بروید. مخزن `kubernetes/website` را به‌عنوان مخزن راه دور `upstream` تنظیم کنید:

   ```shell
   cd website

   git remote add upstream https://github.com/kubernetes/website.git
   ```

1. مخزن‌های `origin` و `upstream` خود را بررسی و تأیید کنید:

   ```shell
   git remote -v
   ```

   خروجی مشابه زیر است:

   ```none
   origin	git@github.com:<github_username>/website.git (fetch)
   origin	git@github.com:<github_username>/website.git (push)
   upstream	https://github.com/kubernetes/website.git (fetch)
   upstream	https://github.com/kubernetes/website.git (push)
   ```

1. کامیت‌ها را از شاخهٔ `origin/main` فورک خود و از شاخهٔ `upstream/main` مخزن `kubernetes/website` دریافت کنید:

   ```shell
   git fetch origin
   git fetch upstream
   ```

   با این کار مطمئن می‌شوید که مخزن محلی شما پیش از شروع اعمال تغییرات به‌روز است.

   {{< note >}}
   این گردش‌کار با
   [گردش‌کار GitHub جامعهٔ کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/guide/github-workflow.md)
   تفاوت دارد. لازم نیست پیش از پوش کردن به‌روزرسانی‌ها به فورک خود، نسخهٔ محلی `main` را با
   `upstream/main` ادغام کنید.
   {{< /note >}}

### ایجاد یک شاخه

1. تصمیم بگیرید که کار خود را بر پایهٔ کدام شاخه انجام دهید:

   - برای بهبود محتوای موجود، از `upstream/main` استفاده کنید.
   - برای محتوای جدید دربارهٔ قابلیت‌های موجود، از `upstream/main` استفاده کنید.
   - برای محتوای بومی‌سازی‌شده، از قراردادهای همان بومی‌سازی پیروی کنید. برای اطلاعات بیشتر، به
     [بومی‌سازی مستندات کوبرنتیز](/docs/contribute/localization/) مراجعه کنید.
   - برای قابلیت‌های جدید در نسخهٔ آیندهٔ کوبرنتیز، از شاخهٔ مربوط به آن قابلیت استفاده کنید. برای
     اطلاعات بیشتر، به [مستندسازی برای یک انتشار](/docs/contribute/new-content/new-features/) مراجعه کنید.
   - برای کارهای بلندمدتی که چند مشارکت‌کنندهٔ SIG Docs روی آن‌ها همکاری می‌کنند، مانند
     سازمان‌دهی مجدد محتوا، از شاخهٔ ویژه‌ای استفاده کنید که برای همان کار ایجاد شده است.

   اگر برای انتخاب شاخه به کمک نیاز دارید، در کانال `#sig-docs` در Slack بپرسید.

1. شاخهٔ جدیدی بر پایهٔ شاخه‌ای که در مرحلهٔ ۱ مشخص کردید ایجاد کنید. در این مثال فرض شده است
   که شاخهٔ پایه `upstream/main` است:

   ```shell
   git checkout -b <my_new_branch> upstream/main
   ```

1. تغییرات خود را با یک ویرایشگر متن اعمال کنید.

هر زمان که خواستید، می‌توانید با فرمان `git status` ببینید چه فایل‌هایی را تغییر داده‌اید.

### کامیت کردن تغییرات

هنگامی که آمادهٔ ارسال درخواست ادغام شدید، تغییرات خود را کامیت کنید.

1. در مخزن محلی خود، بررسی کنید که کدام فایل‌ها را باید کامیت کنید:

   ```shell
   git status
   ```

   خروجی مشابه زیر است:

   ```none
   On branch <my_new_branch>
   Your branch is up to date with 'origin/<my_new_branch>'.

   Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git checkout -- <file>..." to discard changes in working directory)

   modified:   content/en/docs/contribute/new-content/contributing-content.md

   no changes added to commit (use "git add" and/or "git commit -a")
   ```

1. فایل‌هایی را که زیر عنوان **Changes not staged for commit** فهرست شده‌اند به کامیت اضافه کنید:

   ```shell
   git add <your_file_name>
   ```

   این کار را برای هر فایل تکرار کنید.

1. پس از افزودن همهٔ فایل‌ها، یک کامیت ایجاد کنید:

   ```shell
   git commit -m "Your commit message"
   ```

   {{< note >}}
   در پیام کامیت خود از هیچ‌یک از [کلیدواژه‌های GitHub](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
   استفاده نکنید. می‌توانید بعداً آن‌ها را به توضیحات درخواست ادغام اضافه کنید.
   {{< /note >}}

1. شاخهٔ محلی خود و کامیت جدید آن را به فورک راه دور خود پوش کنید:

   ```shell
   git push origin <my_new_branch>
   ```

### پیش‌نمایش محلی تغییرات {#preview-locally}

بهتر است پیش از پوش کردن تغییرات یا باز کردن درخواست ادغام، آن‌ها را به‌صورت محلی پیش‌نمایش کنید.
مقالهٔ [پیش‌نمایش محلی](/docs/contribute/new-content/preview-locally/) توضیح می‌دهد که چگونه
می‌توانید وب‌سایت را به‌صورت محلی اجرا کنید و تغییرات پیشنهادی را پیش‌نمایش کنید.

### باز کردن درخواست ادغام از فورک خود به kubernetes/website {#open-a-pr}

شکل ۳ مراحل باز کردن درخواست ادغام از فورک شما به مخزن [kubernetes/website](https://github.com/kubernetes/website) را نشان می‌دهد. جزئیات در ادامه آمده است.

توجه داشته باشید که مشارکت‌کنندگان ممکن است از `kubernetes/website` با نام `k/website` یاد کنند.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
subgraph first[ ]
direction TB
1[۱. رفتن به مخزن kubernetes/website] --> 2[۲. انتخاب New Pull Request]
2 --> 3[۳. انتخاب compare across forks]
3 --> 4[۴. انتخاب فورک خود از<br>منوی کشویی head repository]
end
subgraph second [ ]
direction TB
5[۵. انتخاب شاخهٔ خود از<br>منوی کشویی compare] --> 6[۶. انتخاب Create Pull Request]
6 --> 7[۷. افزودن توضیحات<br>به درخواست ادغام]
7 --> 8[۸. انتخاب Create pull request]
end

first --> second

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
class 1,2,3,4,5,6,7,8 grey
class first,second white
{{</ mermaid >}}

شکل ۳. مراحل باز کردن درخواست ادغام از فورک شما به مخزن [kubernetes/website](https://github.com/kubernetes/website).

1. در مرورگر وب، به مخزن [`kubernetes/website`](https://github.com/kubernetes/website/) بروید.
1. گزینهٔ **New Pull Request** را انتخاب کنید.
1. گزینهٔ **compare across forks** را انتخاب کنید.
1. از منوی کشویی **head repository**، فورک خود را انتخاب کنید.
1. از منوی کشویی **compare**، شاخهٔ خود را انتخاب کنید.
1. گزینهٔ **Create Pull Request** را انتخاب کنید.
1. توضیحاتی برای درخواست ادغام خود اضافه کنید:

    - **عنوان** (Title، حداکثر ۵۰ نویسه): هدف تغییر را به‌طور خلاصه بیان کنید.
    - **توضیحات** (Description): تغییر را با جزئیات بیشتری شرح دهید.

      - اگر issue مرتبطی در GitHub وجود دارد، عبارت `Fixes #12345` یا `Closes #12345` را در
        توضیحات بگنجانید. در این صورت، سازوکار خودکار GitHub پس از ادغام درخواست، issue
        ذکرشده را می‌بندد. اگر درخواست‌های ادغام مرتبط دیگری وجود دارند، پیوند آن‌ها را نیز اضافه کنید.
      - اگر دربارهٔ موضوع خاصی به راهنمایی نیاز دارید، پرسش‌هایی را که می‌خواهید بازبین‌ها
        درباره‌شان فکر کنند در توضیحات خود بنویسید.

1. دکمهٔ **Create pull request** را انتخاب کنید.

تبریک! درخواست ادغام شما اکنون در بخش [Pull requests](https://github.com/kubernetes/website/pulls) در دسترس است.

پس از باز کردن درخواست ادغام، GitHub آزمون‌های خودکار را اجرا می‌کند و می‌کوشد با استفاده از
[Netlify](https://www.netlify.com/) یک پیش‌نمایش مستقر کند.

- اگر ساخت Netlify ناموفق بود، برای اطلاعات بیشتر گزینهٔ **Details** را انتخاب کنید.
- اگر ساخت Netlify موفق بود، با انتخاب گزینهٔ **Details** نسخهٔ آزمایشی وب‌سایت کوبرنتیز همراه
  با تغییرات اعمال‌شدهٔ شما باز می‌شود. بازبین‌ها تغییرات شما را به همین روش بررسی می‌کنند.

همچنین GitHub برای کمک به بازبین‌ها، به‌طور خودکار برچسب‌هایی به درخواست ادغام اختصاص می‌دهد.
در صورت نیاز، شما نیز می‌توانید برچسب اضافه کنید. برای اطلاعات بیشتر، به [افزودن و حذف برچسب‌های issue](/docs/contribute/review/for-approvers/#adding-and-removing-issue-labels) مراجعه کنید.

### رسیدگی به بازخوردها به‌صورت محلی

1. پس از اعمال تغییرات، کامیت قبلی خود را اصلاح (amend) کنید:

   ```shell
   git commit -a --amend
   ```

   - گزینهٔ `-a`: همهٔ تغییرات را کامیت می‌کند
   - گزینهٔ `--amend`: به‌جای ایجاد کامیت جدید، کامیت قبلی را اصلاح می‌کند

1. در صورت نیاز، پیام کامیت خود را به‌روزرسانی کنید.

1. با فرمان `git push origin <my_new_branch>` تغییرات خود را پوش کنید و آزمون‌های Netlify را دوباره اجرا کنید.

   {{< note >}}
   اگر به‌جای اصلاح کامیت از `git commit -m` استفاده کنید، باید پیش از ادغام
   [کامیت‌های خود را یکی (squash) کنید](#squashing-commits).
   {{< /note >}}

#### تغییرات بازبین‌ها

گاهی بازبین‌ها کامیت‌هایی به درخواست ادغام شما اضافه می‌کنند. پیش از اعمال هر تغییر دیگری، آن کامیت‌ها را دریافت کنید.

1. کامیت‌ها را از فورک راه دور خود دریافت کنید و شاخهٔ کاری خود را ری‌بیس (rebase) کنید:

   ```shell
   git fetch origin
   git rebase origin/<your-branch-name>
   ```

1. پس از ری‌بیس، تغییرات جدید را با force-push به فورک خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

#### تعارض‌های ادغام و ری‌بیس

{{< note >}}
برای اطلاعات بیشتر، به [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)
و [Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging) مراجعه کنید یا برای دریافت کمک در
کانال `#sig-docs` در Slack بپرسید.
{{< /note >}}

اگر مشارکت‌کنندهٔ دیگری در یک درخواست ادغام دیگر، تغییراتی را در همان فایل کامیت کند، ممکن است
تعارض ادغام (merge conflict) ایجاد شود. شما باید همهٔ تعارض‌های ادغام را در درخواست ادغام خود برطرف کنید.

1. فورک خود را به‌روزرسانی کنید و شاخهٔ محلی خود را ری‌بیس کنید:

   ```shell
   git fetch origin
   git rebase origin/<your-branch-name>
   ```

   سپس تغییرات را با force-push به فورک خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

1. تغییرات را از شاخهٔ `upstream/main` مخزن `kubernetes/website` دریافت کنید و شاخهٔ خود را ری‌بیس کنید:

   ```shell
   git fetch upstream
   git rebase upstream/main
   ```

1. نتایج ری‌بیس را بررسی کنید:

   ```shell
   git status
   ```

   در نتیجه، تعدادی از فایل‌ها به‌عنوان دارای تعارض علامت‌گذاری می‌شوند.

1. هر فایل دارای تعارض را باز کنید و به دنبال نشانگرهای تعارض بگردید: `>>>`، `<<<` و `===`.
   تعارض را برطرف کنید و نشانگر تعارض را حذف کنید.

   {{< note >}}
   برای اطلاعات بیشتر، به [How conflicts are presented](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented) مراجعه کنید.
   {{< /note >}}

1. فایل‌ها را به مجموعهٔ تغییرات اضافه کنید:

   ```shell
   git add <filename>
   ```

1. ری‌بیس را ادامه دهید:

   ```shell
   git rebase --continue
   ```

1. مراحل ۲ تا ۵ را در صورت نیاز تکرار کنید.

   پس از اعمال همهٔ کامیت‌ها، فرمان `git status` نشان می‌دهد که ری‌بیس کامل شده است.

1. شاخه را با force-push به فورک خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

   اکنون درخواست ادغام دیگر هیچ تعارضی نشان نمی‌دهد.

### ادغام کامیت‌ها (squash)

{{< note >}}
برای اطلاعات بیشتر، به [Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
مراجعه کنید یا برای دریافت کمک در کانال Slack با نام `#sig-docs` سؤال بپرسید.
{{< /note >}}

اگر PR شما چندین کامیت دارد، باید پیش از ادغام PR، آن‌ها را در یک کامیت واحد ادغام کنید.
برای بررسی تعداد کامیت‌های PR خود می‌توانید به زبانه **Commits** آن مراجعه کنید یا دستور `git log`
را به‌صورت محلی اجرا کنید.

{{< note >}}
در این بخش فرض شده است که از `vim` به‌عنوان ویرایشگر متنی خط فرمان استفاده می‌کنید.
{{< /note >}}

1. یک rebase تعاملی را آغاز کنید:

   ```shell
   git rebase -i HEAD~<number_of_commits_in_branch>
   ```

   ادغام کامیت‌ها نوعی rebase است. سوئیچ `-i` به git اعلام می‌کند که می‌خواهید rebase را به‌صورت تعاملی انجام دهید.
   عبارت `HEAD~<number_of_commits_in_branch` مشخص می‌کند که چه تعداد کامیت برای rebase بررسی شوند.

   خروجی مشابه زیر است:

   ```none
   pick d875112ca Original commit
   pick 4fa167b80 Address feedback 1
   pick 7d54e15ee Address feedback 2

   # Rebase 3d18sf680..7d54e15ee onto 3d183f680 (3 commands)

   ...

   # These lines can be re-ordered; they are executed from top to bottom.
   ```

   بخش اول خروجی، کامیت‌های موجود در rebase را فهرست می‌کند. بخش دوم، گزینه‌های قابل‌استفاده
   برای هر کامیت را نشان می‌دهد. با تغییر واژه `pick`، وضعیت آن کامیت پس از پایان rebase
   تغییر می‌کند.

   برای انجام rebase، روی `squash` و `pick` تمرکز کنید.

   {{< note >}}
   برای اطلاعات بیشتر، به [حالت تعاملی](https://git-scm.com/docs/git-rebase#_interactive_mode) مراجعه کنید.
   {{< /note >}}

1. ویرایش فایل را آغاز کنید.

   متن اصلی زیر را:

   ```none
   pick d875112ca Original commit
   pick 4fa167b80 Address feedback 1
   pick 7d54e15ee Address feedback 2
   ```

   به این صورت تغییر دهید:

   ```none
   pick d875112ca Original commit
   squash 4fa167b80 Address feedback 1
   squash 7d54e15ee Address feedback 2
   ```

   با این کار، کامیت‌های `4fa167b80 Address feedback 1` و `7d54e15ee Address feedback 2` در
   کامیت `d875112ca Original commit` ادغام می‌شوند و تنها `d875112ca Original commit` در تاریخچه باقی می‌ماند.

1. فایل را ذخیره کنید و از آن خارج شوید.

1. کامیت ادغام‌شده خود را push کنید:

   ```shell
   git push --force-with-lease origin <branch_name>
   ```

## مشارکت در مخزن‌های دیگر

[پروژه کوبرنتیز](https://github.com/kubernetes) بیش از ۵۰ مخزن دارد. بسیاری از این
مخزن‌ها شامل مستنداتی مانند متن‌های راهنمای کاربر، پیام‌های خطا، مرجع‌های API یا توضیحات
درون کد هستند.

اگر متنی دیدید که می‌خواهید آن را بهبود دهید، با استفاده از GitHub در همه مخزن‌های سازمان
کوبرنتیز جست‌وجو کنید. این کار به شما کمک می‌کند تشخیص دهید issue یا PR خود را کجا ثبت کنید.

هر مخزن فرایندها و رویه‌های خاص خود را دارد. پیش از ثبت issue یا ارسال PR،
فایل‌های `README.md`، `CONTRIBUTING.md` و `code-of-conduct.md` آن مخزن را، در صورت وجود، مطالعه کنید.

بیشتر مخزن‌ها از قالب‌های issue و PR استفاده می‌کنند. برای آشنایی با فرایندهای هر تیم، نگاهی به
چند issue و PR باز بیندازید. هنگام ثبت issue یا PR، حتماً قالب‌ها را با بیشترین جزئیات
ممکن پر کنید.

## {{% heading "whatsnext" %}}

- برای آشنایی بیشتر با فرایند بازبینی، صفحه [بازبینی](/docs/contribute/review/reviewing-prs) را مطالعه کنید.

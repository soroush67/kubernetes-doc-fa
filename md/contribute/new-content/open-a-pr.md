---
title: باز کردن یک pull request
content_type: concept
weight: 10
card:
  name: contribute
  weight: 40
---

<!-- overview -->

{{< note >}}
**توسعه‌دهندگان کد**: اگر در حال مستندسازی یک قابلیت جدید برای نسخهٔ آتی کوبرنتیز هستید، به
[مستندسازی یک قابلیت جدید](/docs/contribute/new-content/new-features/) مراجعه کنید.
{{< /note >}}

برای مشارکت با افزودن صفحات محتوای جدید یا بهبود صفحات موجود، یک pull request (PR) باز کنید.
مطمئن شوید که همهٔ الزامات بخش
[پیش از شروع](/docs/contribute/new-content/) را رعایت کرده‌اید.

اگر تغییر شما کوچک است یا با git آشنایی ندارید، بخش
[تغییرات با استفاده از GitHub](#changes-using-github) را بخوانید تا نحوهٔ ویرایش یک صفحه را بیاموزید.

اگر تغییرات شما گسترده است، بخش [کار با یک fork محلی](#fork-the-repo) را بخوانید تا یاد بگیرید
چگونه تغییرات را به‌صورت محلی روی رایانهٔ خود انجام دهید.

<!-- body -->

## تغییرات با استفاده از GitHub {#changes-using-github}

اگر تجربهٔ کمتری در کار با جریان‌های کاری git دارید، این روشی ساده‌تر برای
باز کردن یک pull request است. شکل ۱ مراحل را به‌طور خلاصه نشان می‌دهد و جزئیات در ادامه آمده است.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
A([fa:fa-user New<br>Contributor]) --- id1[(kubernetes/website<br>GitHub)]
subgraph tasks[Changes using GitHub]
direction TB
    0[ ] -.-
    1[1. Edit this page] --> 2[2. Use GitHub markdown<br>editor to make changes]
    2 --> 3[3. Select Commit changes...]

end
subgraph tasks2[ ]
direction TB
4[4. Select Propose changes] --> 5[5. Select Create pull request] --> 6[6. Fill in Open a pull request]
6 --> 7[7. Select Create pull request] 
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

شکل ۱. مراحل باز کردن یک PR با استفاده از GitHub.

1. در صفحه‌ای که مشکل را مشاهده می‌کنید، گزینهٔ **Edit this page** را در پنل ناوبری سمت راست انتخاب کنید.

1. تغییرات خود را در ویرایشگر markdown گیت‌هاب اعمال کنید.

1. در بالای ویرایشگر، سمت راست، **Commit changes** را انتخاب کنید.
   در فیلد اول، برای پیام commit خود یک عنوان بنویسید.
   در فیلد دوم، توضیحات را وارد کنید.

   {{< note >}}
   از هیچ‌یک از [کلیدواژه‌های GitHub](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
   در پیام commit خود استفاده نکنید. می‌توانید این کلیدواژه‌ها را بعداً به توضیحات pull request اضافه کنید.
   {{< /note >}}

1. **Propose changes** را انتخاب کنید.

1. **Create pull request** را انتخاب کنید.

1. صفحهٔ **Open a pull request** نمایش داده می‌شود. فرم را تکمیل کنید:

   - فیلد **Add a title** در pull request به‌طور پیش‌فرض برابر با خلاصهٔ commit است.
     در صورت نیاز می‌توانید آن را تغییر دهید.
   - فیلد **Add a description** شامل پیام کامل commit شما (در صورت وجود)
     و مقداری متن قالب است. جزئیاتی را که متن قالب از شما می‌خواهد
     اضافه کنید و سپس متن اضافی قالب را حذف کنید.
   - کادر انتخاب **Allow edits from maintainers** را انتخاب‌شده رها کنید.

   {{< note >}}
   توضیحات PR راه بسیار خوبی برای کمک به بازبین‌ها در درک تغییر شماست.
   برای اطلاعات بیشتر، به [باز کردن یک PR](#open-a-pr) مراجعه کنید.
   {{</ note >}}

1. **Create pull request** را انتخاب کنید.

### رسیدگی به بازخوردها در GitHub

پیش از ادغام یک pull request، اعضای جامعهٔ کوبرنتیز آن را بازبینی و
تأیید می‌کنند. `k8s-ci-robot` بر اساس نزدیک‌ترین مالک ذکرشده در صفحات،
بازبین‌هایی را پیشنهاد می‌دهد. اگر شخص مشخصی را در نظر دارید،
نظری بگذارید که نام کاربری GitHub او در آن آمده باشد.

اگر بازبین از شما خواست تغییراتی اعمال کنید:

1. به زبانهٔ **Files changed** بروید.
1. روی نماد مداد (ویرایش) در کنار هر فایلی که توسط pull request تغییر کرده است کلیک کنید.
1. تغییرات درخواست‌شده را اعمال کنید.
1. تغییرات را commit کنید.

اگر منتظر یک بازبین هستید، هر ۷ روز یک بار با او تماس بگیرید. همچنین می‌توانید در کانال
Slack با نام `#sig-docs` پیام بگذارید.

پس از پایان بازبینی، یک بازبین PR شما را ادغام می‌کند و چند دقیقه بعد تغییرات شما منتشر می‌شود.

## کار با یک fork محلی {#fork-the-repo}

اگر تجربهٔ بیشتری با git دارید یا تغییرات شما بیش از چند خط است،
با یک fork محلی کار کنید.

مطمئن شوید که [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) روی
رایانهٔ شما نصب شده است. همچنین می‌توانید از یک برنامهٔ رابط کاربری git استفاده کنید.

شکل ۲ مراحلی را که هنگام کار با یک fork محلی باید دنبال کنید نشان می‌دهد. جزئیات هر مرحله در ادامه آمده است.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
1[Fork the kubernetes/website<br>repository] --> 2[Create local clone<br>and set upstream]
subgraph changes[Your changes]
direction TB
S[ ] -.-
3[Create a branch<br>example: my_new_branch] --> 3a[Make changes using<br>text editor] --> 4["Preview your changes<br>locally using Hugo<br>(localhost:1313)<br>or build container image"]
end
subgraph changes2[Commit / Push]
direction TB
T[ ] -.-
5[Commit your changes] --> 6[Push commit to<br>origin/my_new_branch]
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

شکل ۲. کار با یک fork محلی برای اعمال تغییرات.

### ایجاد fork از مخزن kubernetes/website

1. به مخزن [`kubernetes/website`](https://github.com/kubernetes/website/) بروید.
1. **Fork** را انتخاب کنید.

### ایجاد یک کلون محلی و تنظیم upstream

1. در یک پنجرهٔ ترمینال، fork خود را کلون کنید و [تم Docsy Hugo](https://github.com/google/docsy#readme) را به‌روزرسانی کنید:

   ```shell
   git clone git@github.com:<github_username>/website
   cd website
   ```

1. به دایرکتوری جدید `website` بروید. مخزن `kubernetes/website` را به‌عنوان remote با نام `upstream` تنظیم کنید:

   ```shell
   cd website

   git remote add upstream https://github.com/kubernetes/website.git
   ```

1. مخازن `origin` و `upstream` خود را بررسی کنید:

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

1. commitها را از `origin/main` در fork خود و `upstream/main` در `kubernetes/website` دریافت (fetch) کنید:

   ```shell
   git fetch origin
   git fetch upstream
   ```

   این کار تضمین می‌کند که پیش از شروع اعمال تغییرات، مخزن محلی شما به‌روز است.

   {{< note >}}
   این جریان کاری با
   [جریان کاری GitHub جامعهٔ کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/guide/github-workflow.md)
   متفاوت است.
   لازم نیست پیش از ارسال (push) به‌روزرسانی‌ها به fork خود، نسخهٔ محلی `main` را با `upstream/main` ادغام کنید.
   {{< /note >}}

### ایجاد یک شاخه (branch)

1. تصمیم بگیرید کار خود را بر پایهٔ کدام شاخه انجام دهید:

   - برای بهبود محتوای موجود، از `upstream/main` استفاده کنید.
   - برای محتوای جدید دربارهٔ قابلیت‌های موجود، از `upstream/main` استفاده کنید.
   - برای محتوای بومی‌سازی‌شده، از قراردادهای همان بومی‌سازی پیروی کنید. برای اطلاعات بیشتر، به
     [بومی‌سازی مستندات کوبرنتیز](/docs/contribute/localization/) مراجعه کنید.
   - برای قابلیت‌های جدید در نسخهٔ آتی کوبرنتیز، از شاخهٔ قابلیت (feature branch) استفاده کنید. برای
     اطلاعات بیشتر، به [مستندسازی برای یک نسخه](/docs/contribute/new-content/new-features/) مراجعه کنید.
   - برای تلاش‌های طولانی‌مدت که چند مشارکت‌کنندهٔ SIG Docs در آن همکاری می‌کنند،
     مانند سازماندهی مجدد محتوا، از یک شاخهٔ قابلیت مخصوص که برای همان تلاش ایجاد شده است استفاده کنید.

   اگر در انتخاب شاخه به کمک نیاز دارید، در کانال Slack با نام `#sig-docs` بپرسید.

1. یک شاخهٔ جدید بر پایهٔ شاخه‌ای که در مرحلهٔ ۱ مشخص کردید ایجاد کنید. این مثال فرض می‌کند که شاخهٔ پایه
   `upstream/main` است:

   ```shell
   git checkout -b <my_new_branch> upstream/main
   ```

1. تغییرات خود را با یک ویرایشگر متن اعمال کنید.

در هر زمان می‌توانید با دستور `git status` فایل‌هایی را که تغییر داده‌اید مشاهده کنید.

### commit کردن تغییرات

وقتی آمادهٔ ارسال یک pull request هستید، تغییرات خود را commit کنید.

1. در مخزن محلی خود بررسی کنید کدام فایل‌ها را باید commit کنید:

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

1. فایل‌های فهرست‌شده در بخش **Changes not staged for commit** را به commit اضافه کنید:

   ```shell
   git add <your_file_name>
   ```

   این کار را برای هر فایل تکرار کنید.

1. پس از افزودن همهٔ فایل‌ها، یک commit ایجاد کنید:

   ```shell
   git commit -m "Your commit message"
   ```

   {{< note >}}
   از هیچ‌یک از [کلیدواژه‌های GitHub](https://help.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
   در پیام commit خود استفاده نکنید. می‌توانید این کلیدواژه‌ها را بعداً به
   توضیحات pull request اضافه کنید.
   {{< /note >}}

1. شاخهٔ محلی خود و commit جدید آن را به fork راه دور (remote) خود ارسال (push) کنید:

   ```shell
   git push origin <my_new_branch>
   ```

### پیش‌نمایش محلی تغییرات {#preview-locally}

بهتر است پیش از ارسال تغییرات یا
باز کردن یک pull request، آن‌ها را به‌صورت محلی پیش‌نمایش کنید. مقالهٔ [پیش‌نمایش محلی](/docs/contribute/new-content/preview-locally/)
توضیح می‌دهد که چگونه می‌توانید وب‌سایت را به‌صورت محلی اجرا کنید و
تغییرات پیشنهادی را پیش‌نمایش کنید.

### باز کردن یک pull request از fork خود به kubernetes/website {#open-a-pr}

شکل ۳ مراحل باز کردن یک PR از fork شما به [kubernetes/website](https://github.com/kubernetes/website) را نشان می‌دهد. جزئیات در ادامه آمده است.

توجه داشته باشید که مشارکت‌کنندگان می‌توانند `kubernetes/website` را به‌صورت `k/website` ذکر کنند.

<!-- See https://github.com/kubernetes/website/issues/28808 for live-editor URL to this figure -->
<!-- You can also cut/paste the mermaid code into the live editor at https://mermaid-js.github.io/mermaid-live-editor to play around with it -->

{{< mermaid >}}
flowchart LR
subgraph first[ ]
direction TB
1[1. Go to kubernetes/website repository] --> 2[2. Select New Pull Request]
2 --> 3[3. Select compare across forks]
3 --> 4[4. Select your fork from<br>head repository drop-down menu]
end
subgraph second [ ]
direction TB
5[5. Select your branch from<br>the compare drop-down menu] --> 6[6. Select Create Pull Request]
6 --> 7[7. Add a description<br>to your PR]
7 --> 8[8. Select Create pull request]
end

first --> second

classDef grey fill:#dddddd,stroke:#ffffff,stroke-width:px,color:#000000, font-size:15px;
classDef white fill:#ffffff,stroke:#000,stroke-width:px,color:#000,font-weight:bold
class 1,2,3,4,5,6,7,8 grey
class first,second white
{{</ mermaid >}}

شکل ۳. مراحل باز کردن یک PR از fork شما به [kubernetes/website](https://github.com/kubernetes/website).

1. در یک مرورگر وب، به مخزن [`kubernetes/website`](https://github.com/kubernetes/website/) بروید.
1. **New Pull Request** را انتخاب کنید.
1. **compare across forks** را انتخاب کنید.
1. از منوی کشویی **head repository**، fork خود را انتخاب کنید.
1. از منوی کشویی **compare**، شاخهٔ خود را انتخاب کنید.
1. **Create Pull Request** را انتخاب کنید.
1. برای pull request خود توضیحات بنویسید:

    - **Title** (حداکثر ۵۰ نویسه): هدف تغییر را خلاصه کنید.
    - **Description**: تغییر را با جزئیات بیشتری شرح دهید.

      - اگر یک issue مرتبط در GitHub وجود دارد، عبارت `Fixes #12345` یا `Closes #12345` را در
        توضیحات بیاورید. در صورت استفاده از این عبارت، خودکارسازی GitHub پس از ادغام PR، issue ذکرشده را می‌بندد.
        اگر PRهای مرتبط دیگری وجود دارد، آن‌ها را نیز پیوند دهید.
      - اگر دربارهٔ موضوع خاصی توصیه می‌خواهید، هر پرسشی را که دوست دارید بازبین‌ها
        به آن فکر کنند در توضیحات خود بیاورید.

1. دکمهٔ **Create pull request** را انتخاب کنید.

تبریک! pull request شما در بخش [Pull requests](https://github.com/kubernetes/website/pulls) در دسترس است.

پس از باز کردن یک PR، GitHub آزمون‌های خودکار را اجرا می‌کند و تلاش می‌کند با استفاده از
[Netlify](https://www.netlify.com/) یک پیش‌نمایش مستقر کند.

- اگر ساخت Netlify شکست بخورد، برای اطلاعات بیشتر **Details** را انتخاب کنید.
- اگر ساخت Netlify موفق باشد، انتخاب **Details** نسخه‌ای آزمایشی (staged) از وب‌سایت
  کوبرنتیز را با تغییرات اعمال‌شدهٔ شما باز می‌کند. بازبین‌ها از همین طریق تغییرات شما را بررسی می‌کنند.

GitHub همچنین به‌طور خودکار برچسب‌هایی را برای کمک به بازبین‌ها به یک PR اختصاص می‌دهد. در صورت
نیاز، شما نیز می‌توانید برچسب اضافه کنید. برای اطلاعات بیشتر، به [افزودن و حذف برچسب‌های issue](/docs/contribute/review/for-approvers/#adding-and-removing-issue-labels) مراجعه کنید.

### رسیدگی به بازخوردها به‌صورت محلی

1. پس از اعمال تغییرات، commit قبلی خود را اصلاح (amend) کنید:

   ```shell
   git commit -a --amend
   ```

   - `-a`: همهٔ تغییرات را commit می‌کند
   - `--amend`: به‌جای ایجاد یک commit جدید، commit قبلی را اصلاح می‌کند

1. در صورت نیاز، پیام commit خود را به‌روزرسانی کنید.

1. با دستور `git push origin <my_new_branch>` تغییرات خود را ارسال کنید و آزمون‌های Netlify را دوباره اجرا کنید.

   {{< note >}}
   اگر به‌جای amend از `git commit -m` استفاده کنید، باید پیش از ادغام، [commitهای خود را squash کنید](#squashing-commits).
   {{< /note >}}

#### تغییرات بازبین‌ها

گاهی بازبین‌ها روی pull request شما commit می‌کنند. پیش از اعمال هر تغییر دیگری، آن commitها را دریافت (fetch) کنید.

1. commitها را از fork راه دور خود دریافت کنید و شاخهٔ کاری خود را rebase کنید:

   ```shell
   git fetch origin
   git rebase origin/<your-branch-name>
   ```

1. پس از rebase، تغییرات جدید را با force-push به fork خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

#### تداخل‌های ادغام و rebase

{{< note >}}
برای اطلاعات بیشتر، به [Git Branching - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts)،
[Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging) مراجعه کنید یا برای کمک در کانال Slack
با نام `#sig-docs` بپرسید.
{{< /note >}}

اگر مشارکت‌کنندهٔ دیگری در یک PR دیگر تغییراتی را در همان فایل commit کند، ممکن است یک تداخل ادغام (merge conflict)
ایجاد شود. شما باید همهٔ تداخل‌های ادغام را در PR خود برطرف کنید.

1. fork خود را به‌روزرسانی کنید و شاخهٔ محلی خود را rebase کنید:

   ```shell
   git fetch origin
   git rebase origin/<your-branch-name>
   ```

   سپس تغییرات را با force-push به fork خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

1. تغییرات را از `upstream/main` در `kubernetes/website` دریافت (fetch) کنید و شاخهٔ خود را rebase کنید:

   ```shell
   git fetch upstream
   git rebase upstream/main
   ```

1. نتایج rebase را بررسی کنید:

   ```shell
   git status
   ```

   در نتیجه، تعدادی فایل به‌عنوان دارای تداخل علامت‌گذاری می‌شوند.

1. هر فایل دارای تداخل را باز کنید و به دنبال نشانگرهای تداخل بگردید: `>>>`، `<<<` و `===`.
   تداخل را برطرف کنید و نشانگر تداخل را حذف کنید.

   {{< note >}}
   برای اطلاعات بیشتر، به [How conflicts are presented](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented) مراجعه کنید.
   {{< /note >}}

1. فایل‌ها را به مجموعه تغییرات (changeset) اضافه کنید:

   ```shell
   git add <filename>
   ```

1. rebase را ادامه دهید:

   ```shell
   git rebase --continue
   ```

1. در صورت نیاز، مراحل ۲ تا ۵ را تکرار کنید.

   پس از اعمال همهٔ commitها، دستور `git status` نشان می‌دهد که rebase کامل شده است.

1. شاخه را با force-push به fork خود ارسال کنید:

   ```shell
   git push --force-with-lease origin <your-branch-name>
   ```

   دیگر هیچ تداخلی در pull request نمایش داده نمی‌شود.

### ادغام کامیت‌ها (Squashing commits)

{{< note >}}
برای اطلاعات بیشتر، [Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) را ببینید،
یا در کانال Slack با نام `#sig-docs` درخواست کمک کنید.
{{< /note >}}

اگر PR شما چند کامیت دارد، پیش از ادغام (merge) PR باید آن‌ها را در یک کامیت واحد ادغام (squash) کنید.
می‌توانید تعداد کامیت‌های PR خود را در زبانه‌ی **Commits** در PR یا با اجرای دستور `git log`
به‌صورت محلی بررسی کنید.

{{< note >}}
این مبحث فرض می‌کند که `vim` ویرایشگر متن خط فرمان است.
{{< /note >}}

1. یک rebase تعاملی را آغاز کنید:

   ```shell
   git rebase -i HEAD~<number_of_commits_in_branch>
   ```

   ادغام کامیت‌ها نوعی rebase است. سوئیچ `-i` به git می‌گوید که می‌خواهید rebase را به‌صورت تعاملی انجام دهید.
   عبارت `HEAD~<number_of_commits_in_branch` مشخص می‌کند که برای rebase چند کامیت بررسی شود.

   خروجی مشابه زیر است:

   ```none
   pick d875112ca Original commit
   pick 4fa167b80 Address feedback 1
   pick 7d54e15ee Address feedback 2

   # Rebase 3d18sf680..7d54e15ee onto 3d183f680 (3 commands)

   ...

   # These lines can be re-ordered; they are executed from top to bottom.
   ```

   بخش اول خروجی کامیت‌های موجود در rebase را فهرست می‌کند. بخش دوم گزینه‌های
   هر کامیت را فهرست می‌کند. تغییر واژه‌ی `pick` پس از اتمام rebase، وضعیت کامیت را تغییر می‌دهد.

   برای اهداف rebase، روی `squash` و `pick` تمرکز کنید.

   {{< note >}}
   برای اطلاعات بیشتر، [Interactive Mode](https://git-scm.com/docs/git-rebase#_interactive_mode) را ببینید.
   {{< /note >}}

1. ویرایش فایل را آغاز کنید.

   متن اصلی را تغییر دهید:

   ```none
   pick d875112ca Original commit
   pick 4fa167b80 Address feedback 1
   pick 7d54e15ee Address feedback 2
   ```

   به:

   ```none
   pick d875112ca Original commit
   squash 4fa167b80 Address feedback 1
   squash 7d54e15ee Address feedback 2
   ```

   این کار کامیت‌های `4fa167b80 Address feedback 1` و `7d54e15ee Address feedback 2` را در
   `d875112ca Original commit` ادغام می‌کند و تنها `d875112ca Original commit` را به‌عنوان بخشی از تاریخچه باقی می‌گذارد.

1. فایل را ذخیره کنید و از آن خارج شوید.

1. کامیت ادغام‌شده‌ی خود را push کنید:

   ```shell
   git push --force-with-lease origin <branch_name>
   ```

## مشارکت در مخزن‌های دیگر

[پروژه‌ی کوبرنتیز](https://github.com/kubernetes) بیش از ۵۰ مخزن (repository) دارد. بسیاری از این
مخزن‌ها شامل مستندات هستند: متن راهنمای کاربرمحور، پیام‌های خطا، مراجع API یا
توضیحات داخل کد.

اگر متنی می‌بینید که مایلید آن را بهبود دهید، از GitHub برای جست‌وجو در تمام مخزن‌های سازمان
کوبرنتیز استفاده کنید. این کار می‌تواند به شما کمک کند تشخیص دهید issue یا PR خود را کجا ارسال کنید.

هر مخزن فرایندها و رویه‌های مخصوص به خود را دارد. پیش از ثبت issue یا ارسال PR،
فایل‌های `README.md`، `CONTRIBUTING.md` و `code-of-conduct.md` آن مخزن را، در صورت وجود، بخوانید.

بیشتر مخزن‌ها از قالب‌های (template) issue و PR استفاده می‌کنند. چند issue و PR باز را مرور کنید تا
با فرایندهای آن تیم آشنا شوید. هنگام ثبت issue یا PR، قالب‌ها را با بیشترین جزئیات ممکن
تکمیل کنید.

## {{% heading "whatsnext" %}}

- برای آشنایی بیشتر با فرایند بازبینی، [Reviewing](/docs/contribute/review/reviewing-prs) را بخوانید.

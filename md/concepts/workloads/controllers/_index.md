---
title: "مدیریت بار کاری"
weight: 20
simple_list: true
---

کوبرنتیز چندین API داخلی برای مدیریت اعلانی
{{< glossary_tooltip text="بارهای کاری" term_id="workload" >}} شما
و اجزای آن بارهای کاری فراهم می‌کند.

در نهایت، برنامه‌های شما به‌صورت کانتینرهایی درون
{{< glossary_tooltip term_id="Pod" text="Podها" >}} اجرا می‌شوند؛ با این حال، مدیریت تک‌تک
Podها زحمت زیادی دارد. برای مثال، اگر یک Pod از کار بیفتد، احتمالاً می‌خواهید
یک Pod جدید برای جایگزینی آن اجرا کنید. کوبرنتیز می‌تواند این کار را برای شما انجام دهد.

شما از API کوبرنتیز برای ایجاد یک
{{< glossary_tooltip text="آبجکت" term_id="object" >}} بار کاری استفاده می‌کنید که سطح انتزاعی بالاتری
نسبت به یک Pod را نمایش می‌دهد، و سپس
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز بر اساس مشخصاتی که برای آبجکت بار کاری تعریف کرده‌اید،
آبجکت‌های Pod را به‌طور خودکار از طرف شما مدیریت می‌کند.

APIهای داخلی برای مدیریت بارهای کاری عبارت‌اند از:

[Deployment](/docs/concepts/workloads/controllers/deployment/) (و به‌طور غیرمستقیم، [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/))،
رایج‌ترین روش برای اجرای یک برنامه روی کلاستر شما.
Deployment برای مدیریت بار کاری یک برنامه‌ی بی‌حالت (stateless) روی کلاستر شما مناسب است؛ جایی که
هر Pod در Deployment قابل جایگزینی با دیگری است و در صورت نیاز می‌توان آن را جایگزین کرد.
(Deploymentها جایگزین API قدیمی
{{< glossary_tooltip text="ReplicationController" term_id="replication-controller" >}} هستند).

یک [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) به شما امکان می‌دهد
یک یا چند Pod را مدیریت کنید – که همگی کد یکسانی از برنامه را اجرا می‌کنند – و این Podها
به داشتن هویتی متمایز وابسته‌اند. این با Deployment متفاوت است که در آن انتظار می‌رود Podها
قابل جایگزینی با یکدیگر باشند.
رایج‌ترین کاربرد StatefulSet این است که بتوان میان Podهای آن و
ذخیره‌سازی پایدارشان پیوند برقرار کرد. برای مثال، می‌توانید یک StatefulSet اجرا کنید که هر Pod را
به یک [PersistentVolume](/docs/concepts/storage/persistent-volumes/) مرتبط می‌کند. اگر یکی از Podهای
StatefulSet از کار بیفتد، کوبرنتیز یک Pod جایگزین می‌سازد که به همان
PersistentVolume متصل است.

یک [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) Podهایی را تعریف می‌کند که
امکاناتی محلی برای یک {{< glossary_tooltip text="نود" term_id="node" >}} خاص فراهم می‌کنند؛
برای مثال، درایوری که به کانتینرهای روی آن نود امکان دسترسی به یک سیستم ذخیره‌سازی را می‌دهد. هنگامی از DaemonSet استفاده می‌کنید
که درایور، یا سرویس دیگری در سطح نود، باید روی نودی اجرا شود که در آن مفید است.
هر Pod در یک DaemonSet نقشی مشابه یک daemon سیستمی روی یک سرور کلاسیک Unix / POSIX
ایفا می‌کند.
یک DaemonSet ممکن است برای عملکرد کلاستر شما بنیادی باشد،
مانند یک پلاگین که به آن نود امکان دسترسی به
[شبکه‌ی کلاستر](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model) را می‌دهد،
ممکن است به شما در مدیریت نود کمک کند،
یا ممکن است امکانات کم‌اهمیت‌تری فراهم کند که پلتفرم کانتینری در حال اجرای شما را بهبود می‌بخشد.
می‌توانید DaemonSetها (و Podهای آن‌ها) را روی همه‌ی نودهای کلاستر خود یا فقط روی زیرمجموعه‌ای از آن‌ها اجرا کنید (برای مثال،
درایور شتاب‌دهنده‌ی GPU را فقط روی نودهایی نصب کنید که GPU روی آن‌ها نصب شده است).

می‌توانید از یک [Job](/docs/concepts/workloads/controllers/job/) و / یا
یک [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) برای
تعریف وظایفی استفاده کنید که تا تکمیل اجرا می‌شوند و سپس متوقف می‌شوند. یک Job یک وظیفه‌ی یک‌باره را نمایش می‌دهد،
در حالی که هر CronJob طبق یک زمان‌بندی تکرار می‌شود.

سایر موضوعات این بخش:
<!-- relies on simple_list: true in the front matter -->

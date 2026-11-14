---
title: "پایش، ثبت لاگ و اشکال‌زدایی"
description: پایش و ثبت لاگ را برای عیب‌یابی یک کلاستر راه‌اندازی کنید، یا یک برنامهٔ کانتینری‌شده را اشکال‌زدایی کنید.
weight: 40
reviewers:
- brendandburns
- davidopp
content_type: concept
no_list: true
card:
  name: tasks
  weight: 999
  title: دریافت کمک
---

<!-- overview -->

گاهی کارها آن‌طور که باید پیش نمی‌روند. این راهنما به شما کمک می‌کند اطلاعات مرتبط را گردآوری کنید و مشکلات را برطرف سازید. این راهنما چهار بخش دارد:

* [اشکال‌زدایی برنامه](/docs/tasks/debug/debug-application/): برای کاربرانی مفید است
  که کد خود را در کوبرنتیز مستقر می‌کنند و نمی‌دانند چرا کار نمی‌کند.
* [اشکال‌زدایی کلاستر](/docs/tasks/debug/debug-cluster/): برای مدیران و اپراتورهای کلاستر مفید است
  که مشکلات خود کلاستر کوبرنتیز را عیب‌یابی می‌کنند.
* [ثبت لاگ در کوبرنتیز](/docs/tasks/debug/logging/): برای مدیران کلاستری مفید است
  که می‌خواهند ثبت لاگ را در کوبرنتیز راه‌اندازی و مدیریت کنند.
* [پایش در کوبرنتیز](/docs/tasks/debug/monitoring/): برای مدیران کلاستری مفید است
  که می‌خواهند پایش را در یک کلاستر کوبرنتیز فعال کنند.

همچنین بهتر است مشکلات شناخته‌شدهٔ [نسخهٔ منتشرشده‌ای](https://github.com/kubernetes/kubernetes/releases)
را که استفاده می‌کنید بررسی کنید.

<!-- body -->

## دریافت کمک

اگر هیچ‌یک از راهنماهای بالا پاسخ مشکل شما را نداد، راه‌های گوناگونی برای
دریافت کمک از جامعهٔ کوبرنتیز وجود دارد.

### پرسش‌ها

مستندات این سایت طوری سازمان‌دهی شده است که به طیف گسترده‌ای از پرسش‌ها پاسخ دهد.
بخش [مفاهیم](/docs/concepts/) معماری کوبرنتیز و نحوهٔ کار هر مؤلفه را توضیح می‌دهد،
و بخش [راه‌اندازی](/docs/setup/) دستورالعمل‌های عملی برای شروع کار ارائه می‌کند.
بخش [وظایف](/docs/tasks/) نشان می‌دهد که کارهای رایج را چگونه انجام دهید، و
[آموزش‌ها](/docs/tutorials/) راهنماهای گام‌به‌گام جامع‌تری برای سناریوهای واقعی،
ویژهٔ صنایع خاص یا توسعهٔ سرتاسری (end-to-end) هستند. بخش [مرجع](/docs/reference/)
مستندات مفصلی دربارهٔ [API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
و رابط‌های خط فرمان (CLI) مانند [`kubectl`](/docs/reference/kubectl/) فراهم می‌کند.

## کمک! پاسخ پرسشم را پیدا نکردم! همین حالا به کمک نیاز دارم!

### سایت‌های Stack Exchange، Stack Overflow یا Server Fault {#stack-exchange}

اگر پرسش‌هایی دربارهٔ *توسعهٔ نرم‌افزار* برای برنامهٔ کانتینری‌شدهٔ خود دارید،
می‌توانید آن‌ها را در [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes) مطرح کنید.

اگر پرسش‌هایی دربارهٔ *مدیریت کلاستر* یا *پیکربندی* کوبرنتیز دارید،
می‌توانید آن‌ها را در
[Server Fault](https://serverfault.com/questions/tagged/kubernetes) مطرح کنید.

همچنین چندین سایت تخصصی‌تر در شبکهٔ Stack Exchange وجود دارد که ممکن است
جای مناسبی برای طرح پرسش‌های کوبرنتیز در حوزه‌هایی مانند
[DevOps](https://devops.stackexchange.com/questions/tagged/kubernetes)،
[مهندسی نرم‌افزار](https://softwareengineering.stackexchange.com/questions/tagged/kubernetes)
یا [امنیت اطلاعات](https://security.stackexchange.com/questions/tagged/kubernetes) باشند.

ممکن است عضو دیگری از جامعه پیش‌تر پرسش مشابهی مطرح کرده باشد یا
بتواند در حل مشکل شما کمک کند.

تیم کوبرنتیز نیز
[پست‌هایی را که برچسب Kubernetes دارند](https://stackoverflow.com/questions/tagged/kubernetes) دنبال می‌کند.
اگر پرسش موجودی نیافتید که به شما کمک کند، پیش از طرح پرسش جدید،
**لطفاً مطمئن شوید که پرسش شما [با موضوع Stack Overflow مرتبط است](https://stackoverflow.com/help/on-topic)،
یا با موضوع [Server Fault](https://serverfault.com/help/on-topic) یا سایتی از شبکهٔ Stack Exchange
که در آن پرسش می‌کنید مرتبط است**، و راهنمای
[نحوهٔ طرح پرسش جدید](https://stackoverflow.com/help/how-to-ask) را مطالعه کنید!

### اسلک (Slack)

بسیاری از اعضای جامعهٔ کوبرنتیز در کانال `#kubernetes-users` در اسلک کوبرنتیز حضور دارند.
استفاده از اسلک نیازمند ثبت‌نام است؛ می‌توانید [درخواست دعوت‌نامه](https://slack.kubernetes.io) بدهید،
و ثبت‌نام برای همه آزاد است. با خیال راحت بیایید و هر پرسشی دارید مطرح کنید.
پس از ثبت‌نام، از طریق مرورگر وب یا برنامهٔ اختصاصی اسلک به
[سازمان کوبرنتیز در اسلک](https://kubernetes.slack.com) دسترسی پیدا کنید.

پس از ثبت‌نام، فهرست رو به رشد کانال‌های مربوط به موضوعات مختلف را مرور کنید.
برای نمونه، افرادی که تازه با کوبرنتیز آشنا شده‌اند ممکن است بخواهند به کانال
[`#kubernetes-novice`](https://kubernetes.slack.com/messages/kubernetes-novice) بپیوندند. به‌عنوان نمونه‌ای دیگر، توسعه‌دهندگان بهتر است به کانال
[`#kubernetes-contributors`](https://kubernetes.slack.com/messages/kubernetes-contributors) بپیوندند.

همچنین کانال‌های بسیاری ویژهٔ کشورها یا زبان‌های محلی وجود دارد. برای دریافت
پشتیبانی و اطلاعات بومی‌سازی‌شده، می‌توانید به این کانال‌ها بپیوندید:

{{< table caption="کانال‌های اسلک ویژهٔ کشورها و زبان‌ها" >}}
کشور | کانال‌ها
:---------|:------------
چین | [`#cn-users`](https://kubernetes.slack.com/messages/cn-users)، [`#cn-events`](https://kubernetes.slack.com/messages/cn-events)
فنلاند | [`#fi-users`](https://kubernetes.slack.com/messages/fi-users)
فرانسه | [`#fr-users`](https://kubernetes.slack.com/messages/fr-users)، [`#fr-events`](https://kubernetes.slack.com/messages/fr-events)
آلمان | [`#de-users`](https://kubernetes.slack.com/messages/de-users)، [`#de-events`](https://kubernetes.slack.com/messages/de-events)
هند | [`#in-users`](https://kubernetes.slack.com/messages/in-users)، [`#in-events`](https://kubernetes.slack.com/messages/in-events)
ایتالیا | [`#it-users`](https://kubernetes.slack.com/messages/it-users)، [`#it-events`](https://kubernetes.slack.com/messages/it-events)
ژاپن | [`#jp-users`](https://kubernetes.slack.com/messages/jp-users)، [`#jp-events`](https://kubernetes.slack.com/messages/jp-events)
کره | [`#kr-users`](https://kubernetes.slack.com/messages/kr-users)
هلند | [`#nl-users`](https://kubernetes.slack.com/messages/nl-users)
نروژ | [`#norw-users`](https://kubernetes.slack.com/messages/norw-users)
لهستان | [`#pl-users`](https://kubernetes.slack.com/messages/pl-users)
روسیه | [`#ru-users`](https://kubernetes.slack.com/messages/ru-users)
اسپانیا | [`#es-users`](https://kubernetes.slack.com/messages/es-users)
سوئد | [`#se-users`](https://kubernetes.slack.com/messages/se-users)
ترکیه | [`#tr-users`](https://kubernetes.slack.com/messages/tr-users)، [`#tr-events`](https://kubernetes.slack.com/messages/tr-events)
{{< /table >}}

### انجمن

از پیوستن شما به انجمن رسمی کوبرنتیز استقبال می‌کنیم: [discuss.kubernetes.io](https://discuss.kubernetes.io).

### باگ‌ها و درخواست قابلیت

اگر با چیزی شبیه به باگ روبه‌رو شده‌اید یا می‌خواهید قابلیت جدیدی درخواست کنید،
لطفاً از [سامانهٔ رهگیری مسائل گیت‌هاب](https://github.com/kubernetes/kubernetes/issues) استفاده کنید.

پیش از ثبت مسئله، لطفاً مسائل موجود را جست‌وجو کنید تا ببینید آیا مسئلهٔ شما
پیش‌تر مطرح شده است یا نه.

اگر باگی را گزارش می‌کنید، لطفاً اطلاعات دقیقی دربارهٔ نحوهٔ بازتولید مشکل
ارائه دهید، مانند:

* نسخهٔ کوبرنتیز: `kubectl version`
* ارائه‌دهندهٔ ابری، توزیع سیستم‌عامل، پیکربندی شبکه و نسخهٔ محیط اجرای کانتینر
* مراحل بازتولید مشکل

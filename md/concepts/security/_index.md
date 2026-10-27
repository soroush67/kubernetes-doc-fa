---
title: "امنیت"
weight: 85
description: >
  مفاهیمی برای ایمن نگه داشتن بار کاری cloud-native شما.
simple_list: true
---

این بخش از مستندات کوبرنتیز با هدف کمک به شما برای یادگیری اجرای ایمن‌تر
بارهای کاری و آشنایی با جنبه‌های اساسی ایمن نگه داشتن یک
کلاستر کوبرنتیز تهیه شده است.

کوبرنتیز بر پایهٔ یک معماری cloud-native بنا شده است و از توصیه‌های
{{< glossary_tooltip text="CNCF" term_id="cncf" >}} دربارهٔ روش‌های خوب
امنیت اطلاعات cloud-native بهره می‌گیرد.

برای آشنایی با زمینهٔ گسترده‌تر دربارهٔ نحوهٔ ایمن‌سازی کلاستر و برنامه‌هایی که
روی آن اجرا می‌کنید، [امنیت Cloud Native و کوبرنتیز](/docs/concepts/security/cloud-native-security/) را مطالعه کنید.

## سازوکارهای امنیتی کوبرنتیز {#security-mechanisms}

کوبرنتیز شامل چندین API و کنترل امنیتی، و نیز روش‌هایی برای
تعریف [سیاست‌ها](#policies) است که می‌توانند بخشی از نحوهٔ مدیریت امنیت اطلاعات شما را تشکیل دهند.

### حفاظت از control plane

یک سازوکار امنیتی کلیدی برای هر کلاستر کوبرنتیز،
[کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access) است.

کوبرنتیز از شما انتظار دارد که TLS را پیکربندی کرده و از آن برای فراهم کردن
[رمزگذاری داده‌ها در حال انتقال](/docs/tasks/tls/managing-tls-in-a-cluster/)
درون control plane، و میان control plane و کلاینت‌های آن استفاده کنید.
همچنین می‌توانید [رمزگذاری در حالت سکون](/docs/tasks/administer-cluster/encrypt-data/)
را برای داده‌های ذخیره‌شده در control plane کوبرنتیز فعال کنید؛ این موضوع جدا از استفاده از
رمزگذاری در حالت سکون برای داده‌های بارهای کاری خودتان است که آن نیز ممکن است ایدهٔ خوبی باشد.

### Secretها

API مربوط به [Secret](/docs/concepts/configuration/secret/) حفاظت پایه‌ای را برای
مقادیر پیکربندی‌ای که نیازمند محرمانگی هستند فراهم می‌کند.

### حفاظت از بار کاری

[استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/) را اعمال کنید تا
اطمینان حاصل شود که پادها و کانتینرهای آن‌ها به‌درستی ایزوله شده‌اند. همچنین در صورت نیاز می‌توانید
از [RuntimeClassها](/docs/concepts/containers/runtime-class) برای تعریف ایزوله‌سازی سفارشی
استفاده کنید.

[سیاست‌های شبکه](/docs/concepts/services-networking/network-policies/) به شما امکان می‌دهند
ترافیک شبکه را میان پادها، یا میان پادها و شبکهٔ خارج از کلاستر، کنترل کنید.

می‌توانید کنترل‌های امنیتی را از اکوسیستم گسترده‌تر مستقر کنید تا کنترل‌های پیشگیرانه
یا کشف‌کننده را پیرامون پادها، کانتینرهای آن‌ها و ایمیج‌هایی که در آن‌ها اجرا می‌شوند پیاده‌سازی کنید.

### کنترل پذیرش {#admission-control}

[کنترل‌کننده‌های پذیرش (Admission controllers)](/docs/reference/access-authn-authz/admission-controllers/)
افزونه‌هایی هستند که درخواست‌های API کوبرنتیز را رهگیری می‌کنند و می‌توانند درخواست‌ها را
بر اساس فیلدهای مشخصی در درخواست اعتبارسنجی یا تغییر (mutate) دهند. طراحی سنجیدهٔ
این کنترل‌کننده‌ها به جلوگیری از اختلال‌های ناخواسته هنگام تغییر APIهای کوبرنتیز
در به‌روزرسانی‌های نسخه کمک می‌کند. برای ملاحظات طراحی، به
[روش‌های خوب برای Admission Webhook](/docs/concepts/cluster-administration/admission-webhooks-good-practices/) مراجعه کنید.

### ممیزی

[ثبت لاگ ممیزی (audit logging)](/docs/tasks/debug/debug-cluster/audit/) در کوبرنتیز مجموعه‌ای
مرتبط با امنیت و به ترتیب زمانی از رکوردها را فراهم می‌کند که توالی اقدامات انجام‌شده
در یک کلاستر را مستند می‌کند. کلاستر فعالیت‌های ایجادشده توسط کاربران، توسط برنامه‌هایی
که از API کوبرنتیز استفاده می‌کنند، و توسط خود control plane را ممیزی می‌کند.

## امنیت ارائه‌دهندهٔ ابری

{{% thirdparty-content vendor="true" %}}

اگر یک کلاستر کوبرنتیز را روی سخت‌افزار خودتان یا روی ارائه‌دهندهٔ ابری دیگری اجرا می‌کنید،
برای بهترین روش‌های امنیتی به مستندات آن مراجعه کنید.
در اینجا پیوندهایی به مستندات امنیتی برخی از ارائه‌دهندگان ابری محبوب آمده است:

{{< table caption="امنیت ارائه‌دهندگان ابری" >}}

ارائه‌دهندهٔ IaaS        | پیوند |
-------------------- | ------------ |
Alibaba Cloud | https://www.alibabacloud.com/trust-center |
Amazon Web Services | https://aws.amazon.com/security |
Google Cloud Platform | https://cloud.google.com/security |
Huawei Cloud | https://www.huaweicloud.com/intl/en-us/securecenter/overallsafety |
IBM Cloud | https://www.ibm.com/cloud/security |
Microsoft Azure | https://docs.microsoft.com/en-us/azure/security/azure-security |
Oracle Cloud Infrastructure | https://www.oracle.com/security |
Tencent Cloud | https://www.tencentcloud.com/solutions/data-security-and-information-protection |
VMware vSphere | https://www.vmware.com/solutions/security/hardening-guides |

{{< /table >}}

## سیاست‌ها

می‌توانید سیاست‌های امنیتی را با استفاده از سازوکارهای بومی کوبرنتیز تعریف کنید،
مانند [NetworkPolicy](/docs/concepts/services-networking/network-policies/)
(کنترل اعلانی بر فیلتر کردن بسته‌های شبکه) یا
[ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) (محدودیت‌های اعلانی بر تغییراتی
که افراد می‌توانند با استفاده از API کوبرنتیز ایجاد کنند).

با این حال، می‌توانید به پیاده‌سازی‌های سیاست از اکوسیستم گسترده‌تر
پیرامون کوبرنتیز نیز تکیه کنید. کوبرنتیز سازوکارهای توسعه‌پذیری را فراهم می‌کند
تا آن پروژه‌های اکوسیستم بتوانند کنترل‌های سیاستی خود را
بر بازبینی کد منبع، تأیید ایمیج کانتینر، کنترل‌های دسترسی API،
شبکه و موارد دیگر پیاده‌سازی کنند.

برای اطلاعات بیشتر دربارهٔ سازوکارهای سیاست و کوبرنتیز،
[سیاست‌ها](/docs/concepts/policy/) را مطالعه کنید.

## {{% heading "whatsnext" %}}

با موضوعات مرتبط امنیتی کوبرنتیز آشنا شوید:

* [ایمن‌سازی کلاستر](/docs/tasks/administer-cluster/securing-a-cluster/)
* [آسیب‌پذیری‌های شناخته‌شده](/docs/reference/issues-security/official-cve-feed/)
  در کوبرنتیز (و پیوندهایی به اطلاعات بیشتر)
* [رمزگذاری داده‌ها در حال انتقال](/docs/tasks/tls/managing-tls-in-a-cluster/) برای control plane
* [رمزگذاری داده‌ها در حالت سکون](/docs/tasks/administer-cluster/encrypt-data/)
* [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access)
* [سیاست‌های شبکه](/docs/concepts/services-networking/network-policies/) برای پادها
* [Secretها در کوبرنتیز](/docs/concepts/configuration/secret/)
* [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/)
* [RuntimeClassها](/docs/concepts/containers/runtime-class)

با زمینهٔ موضوع آشنا شوید:

<!-- if changing this, also edit the front matter of content/en/docs/concepts/security/cloud-native-security.md to match; check the no_list setting -->
* [امنیت Cloud Native و کوبرنتیز](/docs/concepts/security/cloud-native-security/)

گواهی‌نامه بگیرید:

* گواهی‌نامهٔ [Certified Kubernetes Security Specialist](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)
  و دورهٔ آموزشی رسمی.

در این بخش بیشتر بخوانید:


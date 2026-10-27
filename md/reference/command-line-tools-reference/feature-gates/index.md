---
title: Feature Gates
weight: 10
content_type: concept
card:
  name: reference
  weight: 60
---

<!-- overview -->
این صفحه مروری بر feature gateهای مختلفی ارائه می‌دهد که یک مدیر می‌تواند روی مؤلفه‌های گوناگون کوبرنتیز مشخص کند.

برای توضیح مراحل (stage) یک ویژگی، به [مراحل ویژگی](#feature-stages) مراجعه کنید.

<!-- body -->
## مروری کلی

feature gateها مجموعه‌ای از جفت‌های key=value هستند که ویژگی‌های کوبرنتیز را توصیف می‌کنند.
می‌توانید این ویژگی‌ها را با استفاده از فلگ خط فرمان `--feature-gates` روی هر یک از مؤلفه‌های کوبرنتیز فعال یا غیرفعال کنید.

## نحوه فعال‌سازی Feature Gateها

برای فعال یا غیرفعال کردن یک feature gate در یک مؤلفه مشخص کوبرنتیز، از فلگ
`--feature-gates` استفاده کنید.

این فلگ فهرستی از جفت‌های key=value را که با کاما از یکدیگر جدا شده‌اند می‌پذیرد؛ در آن هر key نام یک
feature gate و هر value یکی از مقادیر `true` (فعال‌سازی) یا `false` (غیرفعال‌سازی) است.

**نمونه استفاده:**

```shell
kube-apiserver --feature-gates=FeatureName1=true,FeatureName2=false
kubelet --feature-gates=GracefulNodeShutdown=true
```

هر مؤلفه کوبرنتیز فقط از feature gateهای مرتبط با وظایف خود پشتیبانی می‌کند.
برای مشاهده فهرست feature gateهای موجود برای یک مؤلفه مشخص، از `<component> -h` استفاده کنید.

برای دستورالعمل‌های تفصیلی درباره پیکربندی feature gateها در کلاستر خود، به
[پیکربندی Feature Gateها](/docs/tasks/administer-cluster/configure-feature-gates/) مراجعه کنید.

## Feature gateها در کوبرنتیز v{{% skew currentVersion %}} {#list-of-gates}

جدول‌های زیر خلاصه‌ای از feature gateهایی هستند که می‌توانید روی مؤلفه‌های مختلف کوبرنتیز تنظیم کنید.

- ستون «Since» شامل نسخه کوبرنتیزی است که در آن یک ویژگی معرفی شده
  یا مرحله انتشار آن تغییر کرده است.
- ستون «Until»، در صورتی که خالی نباشد، شامل آخرین نسخه کوبرنتیزی است که در آن
  همچنان می‌توانید از یک feature gate استفاده کنید.
- اگر یک ویژگی در وضعیت آلفا یا بتا باشد، آن را می‌توانید در
  [جدول feature gateهای آلفا/بتا](#feature-gates-for-alpha-or-beta-features) بیابید.
- اگر یک ویژگی پایدار باشد، همه مراحل آن ویژگی را می‌توانید در
  [جدول feature gateهای ارتقایافته/منسوخ‌شده](#feature-gates-for-graduated-or-deprecated-features) بیابید.
- [جدول feature gateهای ارتقایافته/منسوخ‌شده](#feature-gates-for-graduated-or-deprecated-features)
  همچنین ویژگی‌های منسوخ‌شده و پس‌گرفته‌شده را فهرست می‌کند.

{{< note >}}
برای مشاهده مرجع feature gateهای قدیمی که حذف شده‌اند، به
[feature gateهای حذف‌شده](/docs/reference/command-line-tools-reference/feature-gates-removed/) مراجعه کنید.
{{< /note >}}

<!-- Want to edit this table? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
### Feature gateها برای ویژگی‌های آلفا یا بتا

{{< feature-gate-table include="alpha,beta" caption="Feature gates for features in Alpha or Beta states" >}}

<!-- Want to edit this table? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
### Feature gateها برای ویژگی‌های ارتقایافته یا منسوخ‌شده

{{< feature-gate-table include="ga,deprecated" caption="Feature Gates for Graduated or Deprecated Features" >}}

## استفاده از یک ویژگی

### مراحل ویژگی {#feature-stages}

یک ویژگی می‌تواند در مرحله *آلفا*، *بتا* یا *GA* باشد.
ویژگی *آلفا* به این معناست:

* به‌طور پیش‌فرض غیرفعال است.
* ممکن است دارای باگ باشد. فعال‌سازی ویژگی ممکن است باگ‌ها را آشکار کند.
* پشتیبانی از ویژگی ممکن است در هر زمان و بدون اطلاع قبلی حذف شود.
* API ممکن است در نسخه‌های بعدی نرم‌افزار و بدون اطلاع قبلی به شکل ناسازگار تغییر کند.
* به دلیل افزایش خطر باگ و نبود پشتیبانی بلندمدت، فقط برای استفاده در کلاسترهای آزمایشی کوتاه‌مدت توصیه می‌شود.

ویژگی *بتا* به این معناست:

* معمولاً به‌طور پیش‌فرض فعال است. گروه‌های API بتا
  [به‌طور پیش‌فرض غیرفعال هستند](https://github.com/kubernetes/enhancements/tree/master/keps/sig-architecture/3136-beta-apis-off-by-default).
* ویژگی به‌خوبی آزمایش شده است. فعال‌سازی آن ایمن در نظر گرفته می‌شود.
* پشتیبانی از کلیت ویژگی حذف نخواهد شد، هرچند ممکن است جزئیات تغییر کنند.
* طرح‌واره (schema) و/یا معناشناسی (semantics) آبجکت‌ها ممکن است در یک نسخه بتا یا پایدار بعدی به شکل ناسازگار تغییر کند. در این صورت،
  دستورالعمل‌هایی برای مهاجرت به نسخه بعدی ارائه خواهیم کرد. این کار ممکن است نیازمند حذف، ویرایش و
  بازسازی آبجکت‌های API باشد. فرایند ویرایش ممکن است به تأمل نیاز داشته باشد.
  همچنین ممکن است برای برنامه‌هایی که به این ویژگی وابسته‌اند، زمان از دسترس خارج‌بودن (downtime) لازم شود.
* به دلیل احتمال تغییرات ناسازگار در نسخه‌های بعدی، فقط برای کاربردهای غیرحیاتی از نظر کسب‌وکار توصیه می‌شود.
  اگر چندین کلاستر دارید که می‌توانند به‌طور مستقل ارتقا یابند، ممکن است بتوانید این محدودیت را تعدیل کنید.

{{< note >}}
لطفاً ویژگی‌های *بتا* را امتحان کنید و بازخورد خود را درباره آن‌ها ارائه دهید!
پس از خروج از مرحله بتا، ممکن است اعمال تغییرات بیشتر برای ما عملی نباشد.
{{< /note >}}

ویژگی *General Availability* (GA) را ویژگی *پایدار* نیز می‌نامند. این به معنای زیر است:

* ویژگی همیشه فعال است و نمی‌توانید آن را غیرفعال کنید.
* feature gate متناظر دیگر لازم نیست.
* نسخه‌های پایدار ویژگی‌ها در نسخه‌های بسیار بعدی نرم‌افزار منتشرشده نیز حضور خواهند داشت.

## فهرست feature gateها {#feature-gates}

هر feature gate برای فعال یا غیرفعال کردن یک ویژگی مشخص طراحی شده است.

<!-- Want to edit this list? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
{{< feature-gate-list include="alpha,beta,ga,deprecated" >}}

## {{% heading "whatsnext" %}}

* [سیاست منسوخ‌سازی](/docs/reference/using-api/deprecation-policy/) کوبرنتیز
  رویکرد پروژه را برای حذف ویژگی‌ها و مؤلفه‌ها توضیح می‌دهد.
* از کوبرنتیز 1.24 به بعد، APIهای بتای جدید به‌طور پیش‌فرض فعال نیستند. هنگام فعال‌سازی یک ویژگی
  بتا، باید منابع API مرتبط با آن را نیز فعال کنید.
  برای مثال، برای فعال‌سازی یک منبع مشخص مانند
  `storage.k8s.io/v1beta1/csistoragecapacities`، مقدار `--runtime-config=storage.k8s.io/v1beta1/csistoragecapacities` را تنظیم کنید.
  برای جزئیات بیشتر درباره فلگ‌های خط فرمان، به [نسخه‌بندی API](/docs/reference/using-api/#api-versioning) مراجعه کنید.
* برای راهنمایی گام‌به‌گام درباره فعال‌سازی feature gateها، به
  [پیکربندی Feature Gateها](/docs/tasks/administer-cluster/configure-feature-gates/) مراجعه کنید.

---
api_metadata:
  apiVersion: "meta/v1"
  import: "k8s.io/apimachinery/pkg/apis/meta/v1"
  kind: "ObjectMeta"
content_type: "api_reference"
description: "ObjectMeta فراداده‌ای است که همه منابع ماندگار (persisted) باید داشته باشند و شامل همه آبجکت‌هایی می‌شود که کاربران باید ایجاد کنند."
title: "ObjectMeta"
weight: 310
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: meta/v1`

`import "k8s.io/apimachinery/pkg/apis/meta/v1"`


## ObjectMeta {#ObjectMeta}

ObjectMeta فراداده‌ای است که همه منابع ماندگار باید داشته باشند و شامل همه آبجکت‌هایی می‌شود که کاربران باید ایجاد کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>annotations</code><br/><em>object</em></td>
      <td>Annotations یک نگاشت کلید-مقدار بدون ساختار است که همراه با یک منبع ذخیره می‌شود و ابزارهای خارجی می‌توانند آن را برای ذخیره و بازیابی فراداده‌های دلخواه تنظیم کنند. این مقادیر قابل پرس‌وجو نیستند و هنگام تغییر آبجکت‌ها باید حفظ شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations</td>
    </tr>
    <tr>
      <td><code>creationTimestamp</code><br/><em><a href="{{< ref "time-v1-meta#Time" >}}">Time</a></em></td>
      <td>CreationTimestamp یک برچسب زمانی است که زمان سرور را هنگام ایجاد این آبجکت نشان می‌دهد. تضمین نمی‌شود که این مقدار در عملیات‌های جداگانه به ترتیب happens-before تنظیم شود. کلاینت‌ها نمی‌توانند این مقدار را تنظیم کنند. این مقدار به قالب RFC3339 و در منطقه زمانی UTC نمایش داده می‌شود.  توسط سیستم مقداردهی می‌شود. فقط خواندنی است. برای لیست‌ها null است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>deletionGracePeriodSeconds</code><br/><em>integer</em></td>
      <td>تعداد ثانیه‌هایی که به این آبجکت اجازه داده می‌شود پیش از حذف از سیستم، به‌صورت مطمئن (graceful) خاتمه یابد. فقط زمانی تنظیم می‌شود که deletionTimestamp نیز تنظیم شده باشد. این مقدار را فقط می‌توان کوتاه‌تر کرد. فقط خواندنی است.</td>
    </tr>
    <tr>
      <td><code>deletionTimestamp</code><br/><em><a href="{{< ref "time-v1-meta#Time" >}}">Time</a></em></td>
      <td>DeletionTimestamp تاریخ و زمان (طبق RFC 3339) است که در آن این منبع حذف خواهد شد. این فیلد را سرور هنگامی تنظیم می‌کند که کاربر حذف مطمئن (graceful) را درخواست کرده باشد و کلاینت نمی‌تواند آن را مستقیماً تنظیم کند. انتظار می‌رود منبع پس از زمان مندرج در این فیلد و در صورتی که فهرست finalizers خالی باشد، حذف شود (یعنی دیگر در فهرست منابع دیده نشود و با نام قابل دسترسی نباشد). تا زمانی که فهرست finalizers شامل آیتم باشد، حذف مسدود است. پس از تنظیم deletionTimestamp، این مقدار را نمی‌توان لغو کرد یا به آینده‌ای دورتر منتقل کرد، اما می‌توان آن را کوتاه‌تر کرد یا منبع را پیش از این زمان حذف کرد. برای مثال، کاربر ممکن است درخواست کند یک pod ظرف ۳۰ ثانیه حذف شود. Kubelet در پاسخ، یک سیگنال خاتمه مطمئن را به کانتینرهای pod ارسال می‌کند. پس از گذشت ۳۰ ثانیه، Kubelet یک سیگنال خاتمه قطعی (SIGKILL) به کانتینر می‌فرستد و پس از پاک‌سازی، pod را از API حذف می‌کند. در صورت وجود پارتیشن‌بندی شبکه، ممکن است این آبجکت پس از این زمان همچنان وجود داشته باشد، تا زمانی که مدیر سیستم یا یک فرایند خودکار تشخیص دهد منبع کاملاً خاتمه یافته است. اگر تنظیم نشده باشد، حذف مطمئن آبجکت درخواست نشده است.  هنگام درخواست حذف مطمئن توسط سیستم مقداردهی می‌شود. فقط خواندنی است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>finalizers</code><br/><em>string array</em><br/><em>patch strategy: merge</em></td>
      <td>این فهرست باید پیش از حذف آبجکت از registry خالی باشد. هر ورودی شناسه مؤلفه‌ای است که مسئول حذف همان ورودی از فهرست است. اگر deletionTimestamp آبجکت غیر nil باشد، ورودی‌های این فهرست فقط قابل حذف هستند. finalizers را می‌توان به هر ترتیبی پردازش و حذف کرد.  ترتیب اجباری نمی‌شود، زیرا خطر قابل‌توجهی برای گیر کردن finalizers ایجاد می‌کند. finalizers فیلدی مشترک است و هر عاملی که مجوز داشته باشد می‌تواند ترتیب آن را تغییر دهد. اگر فهرست finalizers به ترتیب پردازش شود، ممکن است وضعیتی پیش بیاید که مؤلفه مسئول اولین finalizer در فهرست منتظر سیگنالی (مقدار یک فیلد، سیستم خارجی یا مورد دیگر) باشد که مؤلفه مسئول یک finalizer بعدی در فهرست تولید می‌کند و در نتیجه بن‌بست (deadlock) رخ دهد. بدون اعمال ترتیب، finalizers آزادند میان خودشان ترتیب را تعیین کنند و در برابر تغییر ترتیب در فهرست آسیب‌پذیر نیستند.</td>
    </tr>
    <tr>
      <td><code>generateName</code><br/><em>string</em></td>
      <td>GenerateName پیشوندی اختیاری است که سرور فقط در صورتی از آن برای تولید نام یکتا استفاده می‌کند که فیلد Name ارائه نشده باشد. اگر این فیلد استفاده شود، نامی که به کلاینت بازگردانده می‌شود با نامِ ارسال‌شده متفاوت خواهد بود. این مقدار همچنین با یک پسوند یکتا ترکیب می‌شود. مقدار ارائه‌شده همان قواعد اعتبارسنجی فیلد Name را دارد و ممکن است به‌اندازه طول پسوند لازم برای یکتا کردن مقدار در سرور کوتاه شود.  اگر این فیلد مشخص شده باشد و نام تولیدشده از قبل وجود داشته باشد، سرور خطای 409 بازمی‌گرداند.  فقط در صورتی اعمال می‌شود که Name مشخص نشده باشد. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency</td>
    </tr>
    <tr>
      <td><code>generation</code><br/><em>integer</em></td>
      <td>شماره‌ای ترتیبی که یک نسل (generation) مشخص از وضعیت مطلوب را نشان می‌دهد. توسط سیستم مقداردهی می‌شود. فقط خواندنی است.</td>
    </tr>
    <tr>
      <td><code>labels</code><br/><em>object</em></td>
      <td>نگاشتی از کلیدها و مقدارهای رشته‌ای که می‌توان از آن برای سازمان‌دهی و دسته‌بندی (تعیین دامنه و انتخاب) آبجکت‌ها استفاده کرد. ممکن است با انتخابگرهای (selector) replication controllerها و Serviceها مطابقت داشته باشد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels</td>
    </tr>
    <tr>
      <td><code>managedFields</code><br/><em><a href="{{< ref "managed-fields-entry-v1-meta#ManagedFieldsEntry" >}}">ManagedFieldsEntry array</a></em></td>
      <td>ManagedFields شناسه گردش‌کار (workflow-id) و نسخه را به مجموعه فیلدهایی نگاشت می‌کند که آن گردش‌کار مدیریت می‌کند. این فیلد بیشتر برای نگهداری داخلی است و کاربران معمولاً نیازی به تنظیم یا درک آن ندارند. گردش‌کار می‌تواند نام کاربر، نام یک کنترل‌کننده یا نام یک مسیر apply مشخص مانند "ci-cd" باشد. مجموعه فیلدها همیشه در نسخه‌ای است که گردش‌کار هنگام تغییر آبجکت استفاده کرده است.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>Name باید در یک فضای نام (namespace) یکتا باشد. هنگام ایجاد منابع الزامی است، هرچند برخی منابع اجازه می‌دهند کلاینت تولید خودکار یک نام مناسب را درخواست کند. Name عمدتاً برای ایدمپوتنسی (idempotence) در ایجاد و برای تعریف پیکربندی در نظر گرفته شده است. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>Namespace فضایی را تعریف می‌کند که هر نام باید در آن یکتا باشد. فضای نام خالی معادل فضای نام "default" است، اما نمایش استاندارد آن "default" است. همه آبجکت‌ها ملزم نیستند در دامنه یک فضای نام قرار بگیرند؛ مقدار این فیلد برای چنین آبجکت‌هایی خالی خواهد بود.  باید یک DNS_LABEL باشد. قابل به‌روزرسانی نیست. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces</td>
    </tr>
    <tr>
      <td><code>ownerReferences</code><br/><em><a href="{{< ref "owner-reference-v1-meta#OwnerReference" >}}">OwnerReference array</a></em><br/><em>patch strategy: merge on key <code>uid</code></em></td>
      <td>فهرست آبجکت‌هایی که این آبجکت به آن‌ها وابسته است. اگر همه آبجکت‌های موجود در فهرست حذف شده باشند، این آبجکت زباله‌روبی (garbage collection) می‌شود. اگر این آبجکت توسط یک کنترل‌کننده مدیریت شود، یکی از ورودی‌های این فهرست به آن کنترل‌کننده اشاره می‌کند و فیلد controller آن روی true تنظیم شده است. بیش از یک کنترل‌کننده مدیریت‌کننده نمی‌تواند وجود داشته باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code><br/><em>string</em></td>
      <td>مقداری مبهم (opaque) که نسخه داخلی این آبجکت را نشان می‌دهد و کلاینت‌ها می‌توانند از آن برای تشخیص تغییر آبجکت‌ها استفاده کنند. می‌توان از آن برای کنترل همروندی خوش‌بینانه (optimistic concurrency)، تشخیص تغییر و عملیات watch روی یک منبع یا مجموعه‌ای از منابع استفاده کرد. کلاینت‌ها باید این مقادیر را مبهم در نظر بگیرند و بدون تغییر به سرور بازگردانند. ممکن است فقط برای یک منبع یا مجموعه‌ای مشخص از منابع معتبر باشند.  توسط سیستم مقداردهی می‌شود. فقط خواندنی است. کلاینت‌ها باید این مقدار را مبهم در نظر بگیرند و . اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency</td>
    </tr>
    <tr>
      <td><code>selfLink</code><br/><em>string</em></td>
      <td>منسوخ‌شده: selfLink یک فیلد قدیمی و فقط خواندنی است که دیگر توسط سیستم مقداردهی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>UID مقداری است که در زمان و مکان یکتاست و برای این آبجکت تعیین می‌شود. معمولاً سرور آن را هنگام ایجاد موفق منبع تولید می‌کند و در عملیات PUT اجازه تغییر ندارد.  توسط سیستم مقداردهی می‌شود. فقط خواندنی است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids</td>
    </tr>
  </tbody>
</table>

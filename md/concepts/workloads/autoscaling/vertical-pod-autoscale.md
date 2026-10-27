---
reviewers:
- adrianmoisey
- omerap12
title: مقیاس‌دهی خودکار عمودی Pod
feature:
  title: مقیاس‌دهی عمودی
  description: >
    درخواست‌ها و محدودیت‌های منابع را به‌طور خودکار بر اساس الگوهای واقعی مصرف تنظیم کنید.
content_type: concept
weight: 70
math: true
---

<!-- overview -->

در کوبرنتیز، یک _VerticalPodAutoscaler_ به‌طور خودکار یک {{< glossary_tooltip text="منبع" term_id="api-resource" >}} مدیریت بار کاری (مانند
یک {{< glossary_tooltip text="Deployment" term_id="deployment" >}} یا
{{< glossary_tooltip text="StatefulSet" term_id="statefulset" >}}) را به‌روزرسانی می‌کند، با
این هدف که [درخواست‌ها و محدودیت‌های](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} زیرساختی
به‌طور خودکار متناسب با مصرف واقعی تنظیم شوند.

مقیاس‌دهی عمودی به این معناست که پاسخ به افزایش تقاضای منابع، اختصاص منابع بیشتر (برای مثال: حافظه یا CPU)
به {{< glossary_tooltip text="Podهایی" term_id="pod" >}} است که از قبل برای آن بار کاری در حال اجرا هستند.
این کار با نام _rightsizing_ (تعیین اندازه‌ی درست) یا گاهی _autopilot_ نیز شناخته می‌شود.
این با مقیاس‌دهی افقی متفاوت است؛ مقیاس‌دهی افقی در کوبرنتیز به معنای استقرار Podهای بیشتر برای توزیع بار است.

اگر مصرف منابع کاهش یابد و درخواست‌های منابع Pod بالاتر از سطوح بهینه باشند،
VerticalPodAutoscaler به منبع بار کاری (Deployment، StatefulSet یا منبع مشابه دیگر) دستور می‌دهد
که درخواست‌های منابع را دوباره کاهش دهد و بدین ترتیب از هدررفت منابع جلوگیری می‌کند.

VerticalPodAutoscaler به‌صورت یک منبع API کوبرنتیز و یک
{{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} پیاده‌سازی شده است.
منبع، رفتار کنترل‌کننده را تعیین می‌کند.
کنترل‌کننده‌ی مقیاس‌دهی خودکار عمودی Pod که درون data plane کوبرنتیز اجرا می‌شود،
به‌طور دوره‌ای درخواست‌ها و محدودیت‌های منابع هدف خود (برای مثال، یک Deployment) را
بر اساس تحلیل سوابق میزان استفاده از منابع، مقدار منابع در دسترس در کلاستر،
و رویدادهای بلادرنگ مانند وضعیت‌های کمبود حافظه (OOM) تنظیم می‌کند.

<!-- body -->

## آبجکت API

VerticalPodAutoscaler در کوبرنتیز به‌صورت یک {{< glossary_tooltip text="Custom Resource Definition" term_id="customresourcedefinition" >}} (CRD) تعریف شده است. برخلاف HorizontalPodAutoscaler که بخشی از API هسته‌ی کوبرنتیز است، VPA باید جداگانه در کلاستر شما نصب شود.

نسخه‌ی پایدار فعلی API، `autoscaling.k8s.io/v1` است. جزئیات بیشتر درباره‌ی نصب VPA و API آن را می‌توانید در [مخزن GitHub مربوط به VPA](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) بیابید.

## VerticalPodAutoscaler چگونه کار می‌کند؟

{{< figure
  src="/images/docs/concepts/vpa-architecture.svg"
  alt="معماری مقیاس‌دهی خودکار عمودی Pod"
  class="diagram-large"
  caption="شکل ۱. VerticalPodAutoscaler درخواست‌ها و محدودیت‌های منابع Podهای یک Deployment را کنترل می‌کند"
>}}

<!-- https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqlVG1P2zAQ_iuW-RpY0rVNG6RJpSkSH9hQuzFpLZo850o9nDiznQKj_PddYqcvMGmaSKXG53vuuefuHD9RrjKgCb3VrFyRs8-LguBjqh9uY1SWUnBmhSrIV6XvpGKZg9QPV4XVSkrQ8xRKqR5zKCx5R6Zj_JtZZmFZyRnYm11IqbL5lcrQP8ZgJgrQ3guFZ3b_OVgtuJlfujeZgV5vsawU89HVxYvNLBfGoNL59dWIjFqrSeRU3uwnWJfsO9fza9AWK5QoalRZZXAJmoynqQdr4CrHujIssubdsz2iKjOs1Hn9Gj0HVZDj4w_7ka-oa8BmZpUGQ6btdtN2s_FKW0pnNQHjFfA7Q5ZKE75ixS0g2Cs4kNaAJ2vBrSF18xH_pfEYIgpSSsZhszdMF7uzm_Ap_KrAIEEB9zXJph5CqwmXDeij85Gxhkb8ZjeUFzPynNgdWKMMWYuxu4746Lby16EXxU_gXg02TVWaA1kzWdU9-IuyRhEYp_wfpbZV3Au7Ip9KK3ImcSouCdLjGW7puWTGpLCslZKlkDI5Gp6Pe5NBYJDxDpKjaIK_1JvH9yKzqyQqHwKupNKt-_QFG9eZZ0t7o_5Z-ja29hA6xvPzdNjvv42RlaVnO-un8ej_q93j2_8MAn9gg92wsbH72dvjjx062G5r9O8D3268AY6uFn9KA7zxREYTqysIaA46Z7VJn-rABbUryGFBE1xmsGSVtAu6KJ4xrGTFN6XyNlKr6nZFkyWTBi0nPxUMb88txG1OMoGf9xbJ8K6ZPRZ8y9PUP1ZVYWkSdZs8NHmiDzSJOyedXhiGUe_9IIw63SigjzQZhCfhMO5FcTwcdgaDuPsc0N-NsPBkENf4MBr0O_1uNx4GFJrsl-6ub6785z9_1f9X -->

کوبرنتیز مقیاس‌دهی خودکار عمودی Pod را از طریق چند جزء همکار پیاده‌سازی می‌کند که به‌طور متناوب اجرا می‌شوند (یک فرایند پیوسته نیست). VPA از سه جزء اصلی تشکیل شده است:

* _recommender_ (توصیه‌گر) که مصرف منابع را تحلیل می‌کند و توصیه‌هایی ارائه می‌دهد.
* _updater_ (به‌روزرسان) که درخواست‌های منابع Pod را یا با بیرون‌راندن (evict) Podها یا با تغییر درجای آن‌ها به‌روزرسانی می‌کند.
* و webhook مربوط به _admission controller_ (کنترل‌کننده‌ی پذیرش) VPA که توصیه‌های منابع را روی Podهای جدید یا بازسازی‌شده اعمال می‌کند.

در هر دوره یک بار، Recommender میزان استفاده از منابع را برای Podهایی که هر تعریف VerticalPodAutoscaler هدف قرار داده است پرس‌وجو می‌کند. Recommender منبع هدف تعریف‌شده توسط `targetRef` را پیدا می‌کند، سپس Podها را بر اساس برچسب‌های `.spec.selector` منبع هدف انتخاب می‌کند و متریک‌ها را از API متریک‌های منابع دریافت می‌کند تا مصرف واقعی CPU و حافظه را تحلیل کند.

Recommender داده‌های مصرف منابع (CPU و حافظه) را، هم فعلی و هم تاریخی، برای هر Podای که VerticalPodAutoscaler هدف قرار داده است تحلیل می‌کند. این جزء موارد زیر را بررسی می‌کند:
- الگوهای مصرف تاریخی در طول زمان برای شناسایی روندها
- اوج مصرف و واریانس برای اطمینان از وجود حاشیه‌ی کافی
- رویدادهای کمبود حافظه (OOM) و سایر رخدادهای مرتبط با منابع

بر اساس این تحلیل، Recommender سه نوع توصیه محاسبه می‌کند:
- توصیه‌ی هدف (منابع بهینه برای مصرف معمول)
- کران پایین (حداقل منابع قابل‌قبول)
- کران بالا (حداکثر منابع معقول).

این توصیه‌ها در فیلد `.status.recommendation` منبع VerticalPodAutoscaler ذخیره می‌شوند.


جزء _updater_ منابع VerticalPodAutoscaler را پایش می‌کند و درخواست‌های منابع فعلی Pod را با توصیه‌ها مقایسه می‌کند. هنگامی که اختلاف از آستانه‌های پیکربندی‌شده فراتر رود و سیاست به‌روزرسانی اجازه دهد، updater می‌تواند یکی از کارهای زیر را انجام دهد:

- Podها را بیرون براند و بدین ترتیب بازسازی آن‌ها را با درخواست‌های منابع جدید آغاز کند (رویکرد سنتی)
- در صورتی که کلاستر از به‌روزرسانی درجای منابع Pod پشتیبانی کند، منابع Pod را بدون بیرون‌راندن به‌صورت درجا به‌روزرسانی کند

روش انتخاب‌شده به حالت به‌روزرسانی پیکربندی‌شده، قابلیت‌های کلاستر و نوع تغییر منبع موردنیاز بستگی دارد. به‌روزرسانی‌های درجا، در صورت دسترس بودن، از اختلال در Pod جلوگیری می‌کنند، اما ممکن است درباره‌ی منابعی که قابل تغییر هستند محدودیت‌هایی داشته باشند. updater به PodDisruptionBudgetها احترام می‌گذارد تا اثر بر سرویس را به حداقل برساند.

_admission controller_ به‌صورت یک mutating webhook عمل می‌کند که درخواست‌های ایجاد Pod را رهگیری می‌کند.
این جزء بررسی می‌کند که آیا Pod توسط یک VerticalPodAutoscaler هدف قرار گرفته است یا نه و، در این صورت، درخواست‌ها و محدودیت‌های
منابع توصیه‌شده را پیش از ایجاد Pod اعمال می‌کند. به‌طور دقیق‌تر، admission controller از توصیه‌ی Target در بخش `.status.recommendation` منبع VerticalPodAutoscaler به‌عنوان درخواست‌های منابع جدید استفاده می‌کند. admission controller اطمینان حاصل می‌کند که Podهای جدید با تخصیص منابع با اندازه‌ی مناسب آغاز به کار کنند، خواه در هنگام استقرار اولیه ایجاد شوند، خواه پس از بیرون‌رانده شدن توسط updater، یا به دلیل عملیات مقیاس‌دهی.

VerticalPodAutoscaler به یک منبع متریک، مانند {{< glossary_tooltip text="افزونه‌ی" term_id="addons" >}} Metrics Server کوبرنتیز،
نیاز دارد که در کلاستر نصب شده باشد.
اجزای VPA متریک‌ها را از API `metrics.k8s.io` دریافت می‌کنند. Metrics Server باید جداگانه راه‌اندازی شود، زیرا در بیشتر کلاسترها به‌طور پیش‌فرض مستقر نمی‌شود. برای اطلاعات بیشتر درباره‌ی متریک‌های منابع، به [Metrics Server](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-server) مراجعه کنید.

## حالت‌های به‌روزرسانی

یک VerticalPodAutoscaler از _حالت‌های به‌روزرسانی_ مختلفی پشتیبانی می‌کند که کنترل می‌کنند توصیه‌های منابع
چگونه و چه زمانی روی Podهای شما اعمال شوند. حالت به‌روزرسانی را با استفاده از
فیلد `updateMode` در spec مربوط به VPA، زیر `updatePolicy`، پیکربندی می‌کنید:

```yaml
---
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Recreate"  # Off, Initial, Recreate, InPlaceOrRecreate, InPlace
```

### Off {#updateMode-Off}

در حالت به‌روزرسانی _Off_، recommender مربوط به VPA همچنان مصرف منابع را تحلیل می‌کند و
توصیه‌هایی تولید می‌کند، اما این توصیه‌ها به‌طور خودکار روی Podها اعمال نمی‌شوند.
توصیه‌ها فقط در فیلد `.status` آبجکت VPA ذخیره می‌شوند.

می‌توانید از ابزاری مانند `kubectl` برای مشاهده‌ی `.status` و توصیه‌های موجود در آن استفاده کنید.

### Initial {#updateMode-Initial}

در حالت _Initial_، VPA درخواست‌های منابع را فقط هنگام نخستین ایجاد Podها تنظیم می‌کند. این حالت منابع Podهای در حال اجرا را به‌روزرسانی نمی‌کند، حتی اگر توصیه‌ها در طول زمان تغییر کنند. توصیه‌ها فقط در هنگام ایجاد Pod اعمال می‌شوند.

### Recreate {#updateMode-Recreate}

در حالت _Recreate_، VPA منابع Pod را به‌طور فعال مدیریت می‌کند؛ به این صورت که هرگاه
درخواست‌های منابع فعلی Podها به‌طور قابل‌توجهی با توصیه‌ها تفاوت داشته باشد، آن‌ها را بیرون می‌راند. هنگامی که یک Pod بیرون رانده می‌شود، کنترل‌کننده‌ی
بار کاری (که یک Deployment، StatefulSet و غیره را مدیریت می‌کند) یک Pod جایگزین ایجاد می‌کند و admission
controller مربوط به VPA درخواست‌های منابع به‌روزشده را روی Pod جدید اعمال می‌کند.

### InPlaceOrRecreate {#updateMode-InPlaceOrRecreate}

در حالت `InPlaceOrRecreate`، VPA تلاش می‌کند در صورت امکان درخواست‌ها و محدودیت‌های منابع Pod را بدون راه‌اندازی مجدد Pod به‌روزرسانی کند. با این حال، اگر به‌روزرسانی درجا برای یک تغییر منبع خاص قابل انجام نباشد، VPA به بیرون‌راندن Pod بازمی‌گردد
(مشابه حالت `Recreate`) و به کنترل‌کننده‌ی بار کاری اجازه می‌دهد یک Pod جایگزین با منابع به‌روزشده ایجاد کند.

در این حالت، updater توصیه‌ها را با استفاده از قابلیت [تغییر اندازه‌ی درجای منابع کانتینر](/docs/tasks/configure-pod-container/resize-container-resources/) به‌صورت درجا اعمال می‌کند.


### InPlace {#updateMode-InPlace}

این حالت به‌عنوان یک ویژگی آلفا در VPA 1.7.0 در دسترس است و به
کوبرنتیز 1.33 یا جدیدتر با feature gate کلاستری `InPlacePodVerticalScaling`
فعال، و feature gate `InPlace` فعال روی updater و
admission controller مربوط به VPA نیاز دارد. این حالت از قابلیت
[تغییر اندازه‌ی درجای Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-resize)
برای اعمال به‌روزرسانی‌ها بدون ایجاد اختلال در Pod استفاده می‌کند.

در حالت `InPlace`، VPA تلاش می‌کند درخواست‌ها و محدودیت‌های منابع Pod را بدون
راه‌اندازی مجدد یا بیرون‌راندن Pod به‌روزرسانی کند. برخلاف `InPlaceOrRecreate`، این حالت **هرگز
به بیرون‌راندن بازنمی‌گردد**. اگر یک به‌روزرسانی درجا قابل اعمال نباشد (برای مثال، به این دلیل که
نود ظرفیت کافی ندارد)، VPA به‌روزرسانی را به تعویق می‌اندازد و آن را در
یک حلقه‌ی هماهنگ‌سازی (reconciliation) بعدی دوباره امتحان می‌کند.

برای استفاده از حالت `InPlace`، feature gate `InPlace` را هم روی updater
و هم روی admission controller مربوط به VPA فعال کنید:

```shell
--feature-gates=InPlace=true
```

سپس `updateMode` را در spec مربوط به VPA روی `"InPlace"` تنظیم کنید:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "InPlace"
```

**تفاوت کلیدی با `InPlaceOrRecreate`:** هنگامی که یک تغییر اندازه به تعویق افتاده، در حال انجام،
یا غیرقابل‌انجام باشد، حالت `InPlace` همواره منتظر می‌ماند و دوباره تلاش می‌کند — این حالت هرگز Pod را بیرون نمی‌راند،
صرف‌نظر از اینکه به‌روزرسانی چه مدت در انتظار مانده باشد.

### Auto (منسوخ‌شده) {#updateMode-Auto}

{{< note >}}
حالت به‌روزرسانی `Auto` **از نسخه‌ی 1.4.0 مربوط به VPA منسوخ شده است**. برای به‌روزرسانی‌های مبتنی بر بیرون‌راندن از `Recreate`
و برای به‌روزرسانی‌های درجا با امکان بازگشت به بیرون‌راندن از `InPlaceOrRecreate` استفاده کنید.
{{< /note >}}

حالت `Auto` در حال حاضر نام مستعاری برای حالت `Recreate` است و دقیقاً به همان شکل رفتار می‌کند. این حالت برای فراهم کردن امکان گسترش راهبردهای به‌روزرسانی خودکار در آینده معرفی شد.

## سیاست‌های منابع

سیاست‌های منابع به شما امکان می‌دهند نحوه‌ی تولید توصیه‌ها و اعمال به‌روزرسانی‌ها توسط VerticalPodAutoscaler را به‌دقت تنظیم کنید.
می‌توانید برای توصیه‌های منابع کران تعیین کنید، مشخص کنید کدام منابع مدیریت شوند، و سیاست‌های متفاوتی را برای کانتینرهای منفرد درون یک Pod پیکربندی کنید.

سیاست‌های منابع را در فیلد `resourcePolicy` از spec مربوط به VPA تعریف می‌کنید:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Recreate"
  resourcePolicy:
    containerPolicies:
    - containerName: "application"
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
      controlledResources:
      - cpu
      - memory
      controlledValues: RequestsAndLimits
```

#### minAllowed و maxAllowed

این فیلدها برای توصیه‌های VPA کران تعیین می‌کنند.
VPA هرگز منابعی کمتر از `minAllowed` یا بیشتر از `maxAllowed` توصیه نمی‌کند، حتی اگر داده‌های مصرف واقعی مقادیر متفاوتی را پیشنهاد کنند.

#### controlledResources

فیلد `controlledResources` مشخص می‌کند که VPA کدام انواع منبع را برای یک کانتینر در یک Pod مدیریت کند.
اگر مشخص نشود، VPA به‌طور پیش‌فرض هم CPU و هم حافظه را مدیریت می‌کند. می‌توانید VPA را محدود کنید تا فقط منابع خاصی را مدیریت کند.
نام‌های معتبر منابع شامل `cpu` و `memory` هستند.

### controlledValues

فیلد `controlledValues` تعیین می‌کند که VPA درخواست‌های منابع، محدودیت‌ها، یا هر دو را کنترل کند:

RequestsAndLimits
: VPA هم درخواست‌ها و هم محدودیت‌ها را تنظیم می‌کند. محدودیت بر اساس نسبت درخواست به محدودیت تعریف‌شده در spec مربوط به Pod، متناسب با درخواست مقیاس‌دهی می‌شود. این حالت پیش‌فرض است.

RequestsOnly
: VPA فقط درخواست‌ها را تنظیم می‌کند و محدودیت‌ها را بدون تغییر باقی می‌گذارد. محدودیت‌ها رعایت می‌شوند و اگر مصرف از آن‌ها فراتر رود، همچنان می‌توانند باعث throttling یا کشته شدن به دلیل کمبود حافظه شوند.

برای آشنایی بیشتر با این دو مفهوم، به [درخواست‌ها و محدودیت‌ها](/docs/concepts/configuration/manage-resources-containers/#requests-and-limits) مراجعه کنید.

## منابع LimitRange

اجزای admission controller و updater مربوط به VPA توصیه‌ها را پس‌پردازش می‌کنند تا با قیدهای تعریف‌شده در [LimitRangeها](/docs/concepts/policy/limit-range/) سازگار باشند. منابع LimitRange با `type` برابر Pod و Container در کلاستر کوبرنتیز بررسی می‌شوند.

برای مثال، اگر از مقدار فیلد `max` در یک منبع LimitRange از نوع Container فراتر رفته شود، هر دو جزء VPA محدودیت را به مقدار تعریف‌شده در فیلد `max` کاهش می‌دهند و درخواست به‌طور متناسب کاهش می‌یابد تا نسبت درخواست به محدودیت در spec مربوط به Pod حفظ شود.

## {{% heading "whatsnext" %}}

اگر مقیاس‌دهی خودکار را در کلاستر خود پیکربندی می‌کنید، ممکن است بخواهید استفاده از
[مقیاس‌دهی خودکار نود](/docs/concepts/cluster-administration/node-autoscaling/)
را نیز در نظر بگیرید تا اطمینان حاصل کنید که تعداد مناسبی نود را اجرا می‌کنید.
همچنین می‌توانید درباره‌ی [مقیاس‌دهی خودکار _افقی_ Pod](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) بیشتر بخوانید.

---
title: روش‌های خوب تخصیص پویای منابع برای مدیران کلاستر
content_type: concept
weight: 60
---

<!-- overview -->
این صفحه روش‌های خوب را برای پیکربندی یک کلاستر کوبرنتیز
که از تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) استفاده می‌کند شرح می‌دهد. این دستورالعمل‌ها برای مدیران
کلاستر است.

<!-- body -->
## جداسازی مجوزهای APIهای مرتبط با DRA

DRA از طریق چندین API مختلف هماهنگ می‌شود. از ابزارهای مجوزدهی
(مانند RBAC یا راهکاری دیگر) استفاده کنید تا دسترسی به APIهای مناسب را بسته به
نقش (persona) کاربر خود کنترل کنید.

به‌طور کلی، دسترسی به DeviceClassها و ResourceSliceها باید به مدیران و
درایورهای DRA محدود شود. گردانندگان کلاستری که Podهای دارای claim را مستقر خواهند کرد،
به دسترسی به APIهای ResourceClaim و ResourceClaimTemplate نیاز دارند؛ هر دوی این APIها
دامنهٔ فضای نام دارند.

## استقرار و نگه‌داری درایور DRA

درایورهای DRA برنامه‌های شخص ثالثی هستند که روی هر نود کلاستر شما اجرا می‌شوند
تا میان سخت‌افزار آن نود و اجزای بومی DRA در کوبرنتیز ارتباط برقرار کنند.
روند نصب به درایوری که انتخاب می‌کنید بستگی دارد، اما
به احتمال زیاد به‌صورت یک DaemonSet روی همهٔ نودها یا گزیده‌ای از نودهای کلاستر شما (با استفاده از انتخابگرهای
نود یا سازوکارهای مشابه) مستقر می‌شود.

### در صورت امکان از درایورهایی با ارتقای بی‌وقفه استفاده کنید

درایورهای DRA [رابط بستهٔ
`kubeletplugin`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin) را پیاده‌سازی می‌کنند.
درایور شما ممکن است با پیاده‌سازی یکی از ویژگی‌های این رابط که اجازه می‌دهد
دو نسخه از یک درایور DRA برای مدت کوتاهی هم‌زیستی داشته باشند، از _ارتقای بی‌وقفه_ (seamless upgrades) پشتیبانی کند.
این قابلیت تنها برای kubelet نسخهٔ 1.33 و بالاتر در دسترس است و ممکن است درایور شما
در کلاسترهای ناهمگن که نودهای متصل آن‌ها نسخه‌های قدیمی‌تر کوبرنتیز را اجرا می‌کنند
از آن پشتیبانی نکند؛ برای اطمینان، مستندات درایور خود را بررسی کنید.

اگر ارتقای بی‌وقفه در وضعیت شما در دسترس است، استفاده از آن را در نظر بگیرید تا
تأخیرهای زمان‌بندی هنگام به‌روزرسانی درایور به حداقل برسد.

اگر نمی‌توانید از ارتقای بی‌وقفه استفاده کنید، در زمان از کار افتادن درایور برای ارتقا ممکن است
موارد زیر را مشاهده کنید:
* Podها نمی‌توانند راه‌اندازی شوند، مگر اینکه claimهایی که به آن‌ها وابسته‌اند از قبل برای
  استفاده آماده شده باشند.
* پاک‌سازی پس از آخرین پادی که از یک claim استفاده کرده است، تا زمانی که درایور
  دوباره در دسترس شود به تأخیر می‌افتد. پاد به‌عنوان خاتمه‌یافته علامت‌گذاری نمی‌شود. این امر مانع استفادهٔ مجدد
  از منابع مورد استفادهٔ آن پاد برای پادهای دیگر می‌شود.
* پادهای در حال اجرا به اجرای خود ادامه می‌دهند.

### اطمینان حاصل کنید که درایور DRA یک liveness probe ارائه می‌دهد و از آن استفاده کنید

درایور DRA شما احتمالاً یک سوکت gRPC برای بررسی سلامت، به‌عنوان بخشی از روش‌های خوب
درایورهای DRA، پیاده‌سازی می‌کند. ساده‌ترین راه استفاده از این سوکت gRPC این است که
آن را به‌عنوان liveness probe برای DaemonSetی که درایور DRA شما را مستقر می‌کند پیکربندی کنید.
مستندات یا ابزارهای استقرار درایور شما ممکن است از قبل این مورد را شامل شوند، اما
اگر پیکربندی خود را جداگانه می‌سازید یا درایور DRA خود را به‌صورت یک پاد کوبرنتیز اجرا نمی‌کنید،
اطمینان حاصل کنید که ابزار هماهنگ‌سازی شما در صورت شکست بررسی‌های سلامت این سوکت gRPC،
درایور DRA را دوباره راه‌اندازی کند. این کار هرگونه از کار افتادن تصادفی درایور DRA را به حداقل می‌رساند
و فرصت‌های بیشتری برای خودترمیمی به آن می‌دهد و در نتیجه تأخیرهای زمان‌بندی یا زمان عیب‌یابی را کاهش می‌دهد.

### هنگام تخلیهٔ یک نود، درایور DRA را تا حد امکان دیرتر تخلیه کنید

درایور DRA مسئول لغو آماده‌سازی دستگاه‌هایی است که به
Podها تخصیص داده شده‌اند، و اگر درایور DRA پیش از حذف Podهای دارای claim
{{< glossary_tooltip text="تخلیه"
term_id="drain" >}} شود، نمی‌تواند
پاک‌سازی خود را نهایی کند. اگر منطق تخلیهٔ سفارشی برای نودها پیاده‌سازی می‌کنید،
پیش از خاتمه‌دادن به خود درایور DRA، بررسی کنید که هیچ ResourceClaim یا
ResourceClaimTemplate تخصیص‌یافته/رزروشده‌ای وجود نداشته باشد.


## پایش و تنظیم اجزا برای بار بیشتر، به‌ویژه در محیط‌های با مقیاس بالا

مؤلفهٔ control plane یعنی {{< glossary_tooltip text="kube-scheduler"
term_id="kube-scheduler" >}} و کنترل‌کنندهٔ داخلی ResourceClaim
که توسط مؤلفهٔ {{< glossary_tooltip
text="kube-controller-manager" term_id="kube-controller-manager" >}} هماهنگ می‌شود،
بار اصلی زمان‌بندی Podهای دارای claim را بر اساس فراداده‌های ذخیره‌شده در
APIهای DRA بر عهده دارند. در مقایسه با Podهایی که بدون DRA زمان‌بندی می‌شوند، تعداد فراخوانی‌های
سرور API و میزان مصرف حافظه و پردازنده‌ای که این اجزا نیاز دارند، برای
Podهایی که از claimهای DRA استفاده می‌کنند افزایش می‌یابد. افزون بر این، اجزای محلی نود مانند درایور DRA
و kubelet از APIهای DRA برای تخصیص درخواست سخت‌افزاری در زمان ایجاد
sandbox پاد استفاده می‌کنند. به‌ویژه در محیط‌های با مقیاس بالا که کلاسترها نودهای
فراوانی دارند و/یا بارهای کاری زیادی را مستقر می‌کنند که به‌شدت از resource claimهای تعریف‌شده با DRA
استفاده می‌کنند، مدیر کلاستر باید اجزای مربوط را طوری پیکربندی کند که
بار افزایش‌یافته را پیش‌بینی کنند.

اثرات اجزای نادرست‌تنظیم‌شده می‌تواند مستقیم یا گلوله‌برفی باشد و
در طول چرخهٔ عمر Pod نشانه‌های گوناگونی ایجاد کند. اگر پیکربندی‌های QPS و burst مؤلفهٔ
`kube-scheduler` بیش از حد پایین باشند، زمان‌بند ممکن است
به‌سرعت نود مناسبی برای یک Pod بیابد، اما متصل کردن (bind) Pod به
آن نود زمان بیشتری ببرد. با DRA، در طول زمان‌بندی Pod، پارامترهای QPS و Burst در
پیکربندی client-go درون `kube-controller-manager` حیاتی هستند.

مقادیر مشخص برای تنظیم کلاستر شما به عوامل گوناگونی مانند
تعداد نودها/پادها، نرخ ایجاد پاد و میزان جابه‌جایی (churn) بستگی دارد، حتی در محیط‌های بدون DRA؛
برای اطلاعات بیشتر، به [README گروه SIG Scalability دربارهٔ آستانه‌های
 مقیاس‌پذیری کوبرنتیز](https://github.com/kubernetes/community/blob/main/sig-scalability/configs-and-limits/thresholds.md)
مراجعه کنید. در آزمون‌های مقیاسی که روی یک کلاستر دارای DRA
با ۱۰۰ نود انجام شد و شامل ۷۲۰ پاد بلندمدت (۹۰٪ اشباع) و ۸۰ پاد جابه‌جاشونده
(۱۰٪ جابه‌جایی، ۱۰ بار) با QPS ایجاد job برابر با ۱۰ بود، QPS مؤلفهٔ `kube-controller-manager`
را می‌شد تا ۷۵ و Burst را تا ۱۵۰ پایین آورد و همچنان به اهداف متریک
معادل استقرارهای بدون DRA رسید. در این حد پایین، مشاهده شد که
محدودکنندهٔ نرخ سمت کلاینت به اندازهٔ کافی فعال می‌شد تا از سرور API در برابر
انفجار ناگهانی درخواست‌ها محافظت کند، اما به اندازه‌ای بالا بود که SLOهای راه‌اندازی پاد تحت تأثیر قرار نگیرند.
اگرچه این نقطهٔ شروع خوبی است، می‌توانید با پایش متریک‌های زیر درک بهتری از نحوهٔ تنظیم
اجزای مختلفی که بیشترین اثر را بر کارایی DRA در
استقرار شما دارند به دست آورید. برای اطلاعات بیشتر دربارهٔ همهٔ
متریک‌های پایدار کوبرنتیز، به [مرجع متریک‌های
کوبرنتیز](/docs/reference/instrumentation/metrics/) مراجعه کنید.

### متریک‌های `kube-controller-manager`

متریک‌های زیر به‌طور دقیق کنترل‌کنندهٔ داخلی ResourceClaim را که
توسط مؤلفهٔ `kube-controller-manager` مدیریت می‌شود بررسی می‌کنند.

* نرخ افزودن به صف کار (Workqueue Add Rate): {{< highlight promql "hl_inline=true"  >}} sum(rate(workqueue_adds_total{name="resource_claim"}[5m])) {{< /highlight >}} را پایش کنید تا بسنجید آیتم‌ها با چه سرعتی به کنترل‌کنندهٔ ResourceClaim اضافه می‌شوند.
* عمق صف کار (Workqueue Depth): 
  {{< highlight promql "hl_inline=true" >}}sum(workqueue_depth{endpoint="kube-controller-manager",
  name="resource_claim"}){{< /highlight >}} را دنبال کنید تا هرگونه انباشت کار در کنترل‌کنندهٔ
  ResourceClaim را شناسایی کنید.
* مدت انجام کار در صف (Workqueue Work Duration): {{< highlight promql "hl_inline=true">}}histogram_quantile(0.99,
  sum(rate(workqueue_work_duration_seconds_bucket{name="resource_claim"}[5m]))
  by (le)){{< /highlight >}} را مشاهده کنید تا سرعت پردازش کار توسط کنترل‌کنندهٔ ResourceClaim
  را درک کنید.

اگر نرخ افزودن به صف کار پایین، عمق صف کار بالا و/یا
مدت انجام کار در صف بالا را تجربه می‌کنید، این نشان می‌دهد که کنترل‌کننده
بهینه عمل نمی‌کند. تنظیم پارامترهایی مانند QPS، burst و پیکربندی‌های CPU/حافظه را
در نظر بگیرید.

اگر نرخ افزودن به صف کار بالا و عمق صف کار بالا را تجربه می‌کنید، اما
مدت انجام کار در صف معقول است، این نشان می‌دهد که کنترل‌کننده در حال پردازش
کار است، اما هم‌روندی ممکن است ناکافی باشد. هم‌روندی در
کنترل‌کننده به‌صورت ثابت در کد تعیین شده است، بنابراین شما به‌عنوان مدیر کلاستر می‌توانید با کاهش
QPS ایجاد پاد این وضعیت را تنظیم کنید تا نرخ افزودن به صف کار resource claim
قابل‌مدیریت‌تر شود.

### متریک‌های `kube-scheduler`

متریک‌های زمان‌بند زیر متریک‌هایی سطح بالا هستند که کارایی را
در میان همهٔ Podهای زمان‌بندی‌شده تجمیع می‌کنند، نه فقط آن‌هایی که از DRA استفاده می‌کنند. توجه به این نکته مهم است
که متریک‌های سرتاسری (end-to-end) در نهایت تحت تأثیر
کارایی `kube-controller-manager` در ایجاد ResourceClaimها از
ResourceClaimTemplateها قرار دارند، در استقرارهایی که به‌شدت از ResourceClaimTemplateها استفاده می‌کنند.

* مدت سرتاسری زمان‌بند (Scheduler End-to-End Duration): {{< highlight promql "hl_inline=true" >}}histogram_quantile(0.99,
  sum(increase(scheduler_pod_scheduling_sli_duration_seconds_bucket[5m])) by
  (le)){{< /highlight >}} را پایش کنید.
* تأخیر الگوریتم زمان‌بند (Scheduler Algorithm Latency): {{< highlight promql "hl_inline=true" >}}histogram_quantile(0.99,
  sum(increase(scheduler_scheduling_algorithm_duration_seconds_bucket[5m])) by
  (le)){{< /highlight >}} را دنبال کنید.

### متریک‌های `kubelet`

هنگامی که Podای که به یک نود متصل شده است باید ResourceClaim آن برآورده شود، kubelet
متدهای `NodePrepareResources` و `NodeUnprepareResources` درایور DRA را فراخوانی می‌کند.
می‌توانید این رفتار را از دید kubelet با
متریک‌های زیر مشاهده کنید.

* NodePrepareResources در kubelet: {{< highlight promql "hl_inline=true" >}}histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="PrepareResources"}[5m]))
  by (le)){{< /highlight >}} را پایش کنید.
* NodeUnprepareResources در kubelet: {{< highlight promql "hl_inline=true" >}}histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="UnprepareResources"}[5m]))
  by (le)){{< /highlight >}} را دنبال کنید.

### عملیات kubeletplugin در DRA

درایورهای DRA [رابط بستهٔ
`kubeletplugin`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin) را پیاده‌سازی می‌کنند
که متریک خاص خود را برای عملیات gRPC زیربنایی
`NodePrepareResources` و `NodeUnprepareResources` ارائه می‌دهد. می‌توانید این
رفتار را از دید kubeletplugin داخلی با متریک‌های زیر
مشاهده کنید.

* عملیات gRPC با نام NodePrepareResources در kubeletplugin مربوط به DRA: {{< highlight promql "hl_inline=true" >}}histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodePrepareResources"}[5m]))
  by (le)){{< /highlight >}} را مشاهده کنید.
* عملیات gRPC با نام NodeUnprepareResources در kubeletplugin مربوط به DRA: {{< highlight promql "hl_inline=true" >}} histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodeUnprepareResources"}[5m]))
  by (le)){{< /highlight >}} را مشاهده کنید.


## {{% heading "whatsnext" %}}

* [دربارهٔ
  DRA بیشتر بیاموزید](/docs/concepts/resource-management/dynamic-resource-allocation/)
* [مرجع متریک‌های
کوبرنتیز](/docs/reference/instrumentation/metrics/) را بخوانید

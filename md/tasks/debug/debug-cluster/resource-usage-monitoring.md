---
reviewers:
- mikedanese
content_type: concept
title: ابزارهای پایش منابع
weight: 15
---

<!-- overview -->

برای مقیاس‌دهی یک برنامه و ارائهٔ سرویسی قابل‌اعتماد، باید بدانید که برنامه
پس از استقرار چگونه رفتار می‌کند. می‌توانید کارایی برنامه را در یک کلاستر
کوبرنتیز با بررسی کانتینرها، [پادها](/docs/concepts/workloads/pods/)،
[سرویس‌ها](/docs/concepts/services-networking/service/) و ویژگی‌های کلی
کلاستر ارزیابی کنید. کوبرنتیز در هر یک از این سطوح، اطلاعات دقیقی دربارهٔ
میزان مصرف منابع برنامه فراهم می‌کند. با این اطلاعات می‌توانید کارایی برنامهٔ
خود را ارزیابی کنید و دریابید که با رفع کدام گلوگاه‌ها می‌توان کارایی کلی را
بهبود داد.

<!-- body -->

در کوبرنتیز، پایش برنامه به یک راهکار پایش واحد وابسته نیست. در کلاسترهای
جدید، می‌توانید از خط لوله‌های [معیارهای منابع](#resource-metrics-pipeline) یا
[معیارهای کامل](#full-metrics-pipeline) برای جمع‌آوری آمار پایش استفاده کنید.

## خط لولهٔ معیارهای منابع

خط لولهٔ معیارهای منابع (resource metrics pipeline) مجموعهٔ محدودی از معیارها
را برای اجزای کلاستر، مانند کنترل‌کنندهٔ
[Horizontal Pod Autoscaler](/docs/tasks/run-application/horizontal-pod-autoscale/)
و نیز ابزار `kubectl top`، فراهم می‌کند. این معیارها را
[metrics-server](https://github.com/kubernetes-sigs/metrics-server) جمع‌آوری
می‌کند؛ ابزاری سبک که داده‌ها را برای مدت کوتاه و در حافظه نگه می‌دارد. این
معیارها از طریق API ‏`metrics.k8s.io` در دسترس قرار می‌گیرند.

ابزار metrics-server همهٔ نودهای کلاستر را شناسایی می‌کند و میزان مصرف CPU و
حافظهٔ هر نود را از
[kubelet](/docs/reference/command-line-tools-reference/kubelet/) آن نود
درخواست می‌کند. kubelet همچون پلی میان master کوبرنتیز و نودها عمل می‌کند و
پادها و کانتینرهای در حال اجرا روی هر ماشین را مدیریت می‌کند. kubelet هر پاد
را به کانتینرهای تشکیل‌دهندهٔ آن تفکیک می‌کند و آمار مصرف هر کانتینر را از
طریق رابط محیط اجرای کانتینر (container runtime interface) از محیط اجرای
کانتینر دریافت می‌کند. اگر از محیط اجرایی‌ای استفاده می‌کنید که کانتینرها را
با cgroupها و فضاهای نام لینوکس پیاده‌سازی می‌کند و این محیط اجرایی آمار مصرف
را منتشر نمی‌کند، kubelet می‌تواند این آمار را مستقیماً (با استفاده از کد
[cAdvisor](https://github.com/google/cadvisor)) به دست آورد. این آمار به هر
روشی که دریافت شود، kubelet سپس آمار تجمیع‌شدهٔ مصرف منابع پادها را از طریق
Resource Metrics API ابزار metrics-server در دسترس قرار می‌دهد. این API در
مسیر `/metrics/resource` روی پورت‌های احرازهویت‌شده و فقط‌خواندنی kubelet ارائه
می‌شود.

## خط لولهٔ معیارهای کامل

خط لولهٔ معیارهای کامل (full metrics pipeline) دسترسی به معیارهای غنی‌تری را
برای شما فراهم می‌کند. کوبرنتیز می‌تواند با استفاده از سازوکارهایی مانند
Horizontal Pod Autoscaler به این معیارها واکنش نشان دهد و کلاستر را بر اساس
وضعیت فعلی آن به‌طور خودکار مقیاس‌دهی یا تنظیم کند. خط لولهٔ پایش، معیارها را
از kubelet دریافت می‌کند و سپس آن‌ها را از طریق یک آداپتور که یکی از APIهای
`custom.metrics.k8s.io` یا `external.metrics.k8s.io` را پیاده‌سازی می‌کند، در
اختیار کوبرنتیز قرار می‌دهد.


کوبرنتیز به گونه‌ای طراحی شده است که با [OpenMetrics](https://openmetrics.io/)
کار کند. این پروژه یکی از
[CNCF Observability and Analysis - Monitoring Projects](https://landscape.cncf.io/?group=projects-and-products&view-mode=card#observability-and-analysis--monitoring)
است که بر پایهٔ [Prometheus exposition format](https://prometheus.io/docs/instrumenting/exposition_formats/)
ساخته شده و آن را با دقت و به شکلی تقریباً صددرصد سازگار با نسخه‌های پیشین
گسترش داده است.

اگر نگاهی به
[چشم‌انداز CNCF](https://landscape.cncf.io/?group=projects-and-products&view-mode=card#observability-and-analysis--monitoring)
بیندازید، پروژه‌های پایش متعددی را می‌بینید که می‌توانند با _جمع‌آوری_ (scraping)
داده‌های معیارها و بهره‌گیری از آن‌ها، در مشاهدهٔ کلاستر به شما کمک کنند و با
کوبرنتیز کار کنند. انتخاب ابزار یا ابزارهای متناسب با نیازهایتان بر عهدهٔ
خودتان است. چشم‌انداز CNCF در حوزهٔ مشاهده‌پذیری و تحلیل، ترکیبی از نرم‌افزارهای
متن‌باز، نرم‌افزار به‌عنوان سرویس (SaaS) پولی و دیگر محصولات تجاری را در بر
می‌گیرد.

هنگام طراحی و پیاده‌سازی یک خط لولهٔ معیارهای کامل، می‌توانید داده‌های پایش را
دوباره در اختیار کوبرنتیز قرار دهید. برای نمونه، یک HorizontalPodAutoscaler
می‌تواند با استفاده از معیارهای پردازش‌شده تعیین کند که برای یکی از اجزای بار
کاری شما چند Pod باید اجرا شود.

یکپارچه‌سازی خط لولهٔ معیارهای کامل با پیاده‌سازی کوبرنتیز شما، به دلیل گسترهٔ
بسیار وسیع راهکارهای ممکن، خارج از حوزهٔ مستندات کوبرنتیز است.

انتخاب سکوی پایش تا حد زیادی به نیازها، بودجه و منابع فنی شما بستگی دارد.
کوبرنتیز هیچ خط لولهٔ معیارهای خاصی را توصیه نمی‌کند؛
[گزینه‌های فراوانی](https://landscape.cncf.io/?group=projects-and-products&view-mode=card#observability-and-analysis--monitoring)
در دسترس است. سامانهٔ پایش شما باید از استاندارد انتقال معیارهای
[OpenMetrics](https://openmetrics.io/) پشتیبانی کند و طوری انتخاب شود که به
بهترین شکل با طراحی کلی و استقرار سکوی زیرساخت شما سازگار باشد.


## {{% heading "whatsnext" %}}


با ابزارهای دیگر اشکال‌زدایی آشنا شوید، از جمله:

* [ثبت لاگ](/docs/concepts/cluster-administration/logging/)
* [ورود به کانتینرها با `exec`](/docs/tasks/debug/debug-application/get-shell-running-container/)
* [اتصال به کانتینرها از طریق پراکسی](/docs/tasks/extend-kubernetes/http-proxy-access-api/)
* [اتصال به کانتینرها از طریق port forwarding](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
* [بررسی نود کوبرنتیز با crictl](/docs/tasks/debug/debug-cluster/crictl/)

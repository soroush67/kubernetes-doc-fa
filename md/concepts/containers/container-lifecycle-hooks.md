---
reviewers:
- mikedanese
- thockin
title: هوک‌های چرخه حیات کانتینر
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه توضیح می‌دهد که کانتینرهایی که kubelet آن‌ها را مدیریت می‌کند، چگونه می‌توانند از چارچوب هوک‌های چرخه حیات کانتینر استفاده کنند تا کدی را اجرا کنند که با رویدادهای چرخه حیات مدیریتی‌شان فعال می‌شود.

<!-- body -->

## نمای کلی

کوبرنتیز، مشابه بسیاری از چارچوب‌های زبان‌های برنامه‌نویسی مانند Angular که برای اجزای خود هوک‌های چرخه حیات دارند، هوک‌های چرخه حیات را در اختیار کانتینرها قرار می‌دهد. این هوک‌ها به کانتینرها امکان می‌دهند از رویدادهای چرخه حیات مدیریتی خود آگاه شوند و هنگام اجرای هوک متناظر، کدی را اجرا کنند که در یک هندلر (handler) پیاده‌سازی شده است.

## هوک‌های کانتینر

دو هوک در اختیار کانتینرها قرار گرفته است:

`PostStart`

این هوک بلافاصله پس از ایجاد کانتینر اجرا می‌شود. اجرای آن **هم‌زمان** با `ENTRYPOINT` کانتینر (فرایند اصلی) است؛ یعنی ممکن است هوک پیش از شروع فرایند اصلی، در حین آن یا پس از آن اجرا شود.

هیچ پارامتری به هندلر ارسال نمی‌شود.

{{< note >}}
با اینکه هوک هم‌زمان با فرایند کانتینر اجرا می‌شود، ممکن است به‌روزرسانی وضعیت کانتینر را به تأخیر بیندازد؛ یعنی کانتینر ممکن است تا پایان اجرای هوک به وضعیت `Running` نرود.
{{< /note >}}

`PreStop`

این هوک درست پیش از خاتمه یافتن کانتینر فراخوانی می‌شود؛ خاتمه‌ای که در پی یک درخواست API یا یک رویداد مدیریتی رخ می‌دهد، مانند شکست کاوشگر liveness/startup، پیش‌دستی (preemption)، رقابت بر سر منابع و موارد دیگر. اگر کانتینر از قبل در وضعیت خاتمه‌یافته یا تکمیل‌شده باشد، فراخوانی هوک `PreStop` با شکست مواجه می‌شود. همچنین این هوک باید پیش از ارسال سیگنال TERM برای متوقف کردن کانتینر به پایان برسد. شمارش معکوس مهلت خاتمه (termination grace period) پاد پیش از اجرای هوک `PreStop` آغاز می‌شود؛ بنابراین صرف‌نظر از نتیجه هندلر، کانتینر سرانجام در محدوده مهلت خاتمه Pod متوقف خواهد شد. هیچ پارامتری به هندلر ارسال نمی‌شود.

توضیح دقیق‌تر رفتار خاتمه را می‌توانید در [خاتمه پادها](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) بیابید.

`StopSignal`

با چرخه حیات StopSignal می‌توان سیگنال توقفی را تعریف کرد که هنگام متوقف شدن کانتینر به آن ارسال می‌شود. اگر این مقدار را تنظیم کنید، بر هر دستور `STOPSIGNAL` تعریف‌شده در ایمیج کانتینر اولویت پیدا می‌کند.

توضیح دقیق‌تر رفتار خاتمه با سیگنال‌های توقف سفارشی را می‌توانید در [سیگنال‌های توقف](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-stop-signals) بیابید.

### پیاده‌سازی هندلرهای هوک

کانتینرها با پیاده‌سازی و ثبت یک هندلر برای هر هوک می‌توانند به آن هوک دسترسی داشته باشند. سه نوع هندلر هوک برای کانتینرها قابل پیاده‌سازی است:

* Exec - یک فرمان مشخص، مانند `pre-stop.sh`، را درون cgroupها و فضاهای نام کانتینر اجرا می‌کند. منابع مصرف‌شده توسط این فرمان به حساب کانتینر منظور می‌شود.
* HTTP - یک درخواست HTTP را به یک نقطه پایانی (endpoint) مشخص روی کانتینر ارسال می‌کند.
* Sleep - کانتینر را به مدت زمان مشخصی متوقف نگه می‌دارد.

### اجرای هندلرهای هوک

هنگامی که یک هوک مدیریت چرخه حیات کانتینر فراخوانی می‌شود، سیستم مدیریتی کوبرنتیز هندلر را بر اساس اقدام هوک اجرا می‌کند: `httpGet`، `tcpSocket` ([منسوخ‌شده](/docs/reference/generated/kubernetes-api/v1.35/#lifecyclehandler-v1-core)) و `sleep` توسط فرایند kubelet اجرا می‌شوند و `exec` درون کانتینر اجرا می‌شود.

فراخوانی هندلر هوک `PostStart` هنگام ایجاد کانتینر آغاز می‌شود؛ یعنی ENTRYPOINT کانتینر و هوک `PostStart` به‌طور هم‌زمان فعال می‌شوند. (به همین دلیل، استفاده از هوک HTTP برای `PostStart` معمولاً منطقی نیست، زیرا هیچ تضمینی وجود ندارد که فرایند کانتینر هنگام اجرای هوک به‌طور کامل راه‌اندازی شده باشد.) اگر اجرای هوک `PostStart` بیش از حد طول بکشد یا متوقف و معلق شود، ممکن است مانع رفتن کانتینر به وضعیت `running` شود.

هوک‌های `PreStop` به‌صورت ناهم‌زمان با سیگنال توقف کانتینر اجرا نمی‌شوند؛ هوک باید پیش از ارسال سیگنال TERM اجرای خود را کامل کند. اگر هوک `PreStop` در حین اجرا معلق بماند، فاز Pod برابر `Terminating` خواهد بود و تا زمانی که Pod پس از سپری شدن `terminationGracePeriodSeconds` کشته شود، در همین فاز باقی می‌ماند. این مهلت خاتمه به کل زمان لازم برای اجرای هوک `PreStop` و توقف عادی کانتینر اعمال می‌شود. برای مثال، اگر `terminationGracePeriodSeconds` برابر ۶۰ باشد، اجرای هوک ۵۵ ثانیه طول بکشد و توقف عادی کانتینر پس از دریافت سیگنال ۱۰ ثانیه زمان ببرد، کانتینر پیش از آنکه بتواند به‌طور عادی متوقف شود کشته خواهد شد؛ زیرا `terminationGracePeriodSeconds` کمتر از کل زمان لازم (۵۵+۱۰) برای انجام این دو کار است.

اگر هر یک از هوک‌های `PostStart` یا `PreStop` با شکست مواجه شود، کانتینر کشته می‌شود.

کاربران باید هندلرهای هوک خود را تا حد امکان سبک طراحی کنند. با این حال، مواردی وجود دارد که اجرای فرمان‌های طولانی منطقی است، مانند ذخیره کردن وضعیت پیش از توقف کانتینر.

### تضمین‌های تحویل هوک

تحویل هوک‌ها قرار است *دست‌کم یک بار* انجام شود؛ یعنی ممکن است یک هوک برای هر رویداد مشخص، مانند `PostStart` یا `PreStop`، چندین بار فراخوانی شود. مدیریت درست این وضعیت بر عهده پیاده‌سازی هوک است.

به‌طور کلی، تنها یک بار تحویل انجام می‌شود. برای مثال، اگر گیرنده یک هوک HTTP از کار افتاده باشد و نتواند ترافیک دریافت کند، هیچ تلاشی برای ارسال دوباره صورت نمی‌گیرد. با این حال، در برخی موارد نادر ممکن است تحویل دوباره رخ دهد. برای نمونه، اگر kubelet در میانه ارسال یک هوک راه‌اندازی مجدد شود، ممکن است هوک پس از بالا آمدن دوباره kubelet مجدداً ارسال شود.

### اشکال‌زدایی هندلرهای هوک

لاگ‌های هندلر هوک در رویدادهای Pod نمایش داده نمی‌شوند. اگر هندلری به هر دلیلی با شکست مواجه شود، یک رویداد منتشر می‌کند. برای `PostStart` این رویداد `FailedPostStartHook` و برای `PreStop` رویداد `FailedPreStopHook` است. برای اینکه خودتان یک رویداد `FailedPostStartHook` ایجاد کنید، فایل [lifecycle-events.yaml](https://k8s.io/examples/pods/lifecycle-events.yaml) را طوری ویرایش کنید که فرمان postStart به "badcommand" تغییر کند و سپس آن را اعمال کنید. در ادامه نمونه‌ای از خروجی رویدادهای حاصل را می‌بینید که با اجرای `kubectl describe pod lifecycle-demo` نمایش داده می‌شود:

```
Events:
  Type     Reason               Age              From               Message
  ----     ------               ----             ----               -------
  Normal   Scheduled            7s               default-scheduler  Successfully assigned default/lifecycle-demo to ip-XXX-XXX-XX-XX.us-east-2...
  Normal   Pulled               6s               kubelet            Successfully pulled image "nginx" in 229.604315ms
  Normal   Pulling              4s (x2 over 6s)  kubelet            Pulling image "nginx"
  Normal   Created              4s (x2 over 5s)  kubelet            Created container lifecycle-demo-container
  Normal   Started              4s (x2 over 5s)  kubelet            Started container lifecycle-demo-container
  Warning  FailedPostStartHook  4s (x2 over 5s)  kubelet            Exec lifecycle hook ([badcommand]) for Container "lifecycle-demo-container" in Pod "lifecycle-demo_default(30229739-9651-4e5a-9a32-a8f1688862db)" failed - error: command 'badcommand' exited with 126: , message: "OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: \"badcommand\": executable file not found in $PATH: unknown\r\n"
  Normal   Killing              4s (x2 over 5s)  kubelet            FailedPostStartHook
  Normal   Pulled               4s               kubelet            Successfully pulled image "nginx" in 215.66395ms
  Warning  BackOff              2s (x2 over 3s)  kubelet            Back-off restarting failed container
```



## {{% heading "whatsnext" %}}


* درباره [محیط کانتینر](/docs/concepts/containers/container-environment/) بیشتر بیاموزید.
* با [پیوست کردن هندلرها به رویدادهای چرخه حیات کانتینر](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/) تجربه عملی کسب کنید.

---
reviewers:
- mikedanese
- thockin
title: هوک‌های چرخه عمر کانتینر
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه توضیح می‌دهد که کانتینرهای مدیریت‌شده توسط kubelet چگونه می‌توانند از چارچوب هوک چرخه عمر کانتینر (Container lifecycle hook) استفاده کنند تا کدی را اجرا کنند که با رویدادهای رخ‌داده در طول چرخه عمر مدیریتی آن‌ها فعال می‌شود.

<!-- body -->

## نمای کلی {#overview}

کوبرنتیز، مشابه بسیاری از چارچوب‌های زبان‌های برنامه‌نویسی مانند Angular که هوک‌های چرخه عمر مؤلفه دارند، هوک‌های چرخه عمر را در اختیار کانتینرها قرار می‌دهد.
این هوک‌ها به کانتینرها امکان می‌دهند از رویدادهای چرخه عمر مدیریتی خود آگاه باشند و هنگام اجرای هوک چرخه عمر متناظر، کدی را که در یک handler پیاده‌سازی شده است اجرا کنند.

## هوک‌های کانتینر

دو هوک در اختیار کانتینرها قرار می‌گیرد:

`PostStart`

این هوک بلافاصله پس از ایجاد یک کانتینر اجرا می‌شود.
این هوک **به‌صورت همزمان** با `ENTRYPOINT` کانتینر (فرایند اصلی) اجرا می‌شود،
یعنی ممکن است پیش از شروع فرایند اصلی، در حین آن یا پس از آن اجرا شود.

هیچ پارامتری به handler ارسال نمی‌شود.

{{< note >}}
اگرچه این هوک به‌صورت همزمان با فرایند کانتینر اجرا می‌شود،
می‌تواند به‌روزرسانی وضعیت کانتینر را به تأخیر بیندازد؛
ممکن است کانتینر تا پایان اجرای هوک به وضعیت `Running` منتقل نشود.
{{< /note >}}

`PreStop`

این هوک بلافاصله پیش از خاتمه یافتن یک کانتینر فراخوانی می‌شود؛ خاتمه‌ای که به دلیل یک درخواست API یا یک رویداد مدیریتی مانند شکست probe‌های liveness/startup، preemption، رقابت بر سر منابع و موارد دیگر رخ می‌دهد. اگر کانتینر از قبل در وضعیت خاتمه‌یافته (terminated) یا تکمیل‌شده (completed) باشد، فراخوانی هوک `PreStop` با شکست مواجه می‌شود، و این هوک باید پیش از ارسال سیگنال TERM برای متوقف کردن کانتینر به پایان برسد. شمارش معکوس مهلت خاتمه (termination grace period) پاد پیش از اجرای هوک `PreStop` آغاز می‌شود؛ بنابراین صرف‌نظر از نتیجه اجرای handler، کانتینر سرانجام در مهلت خاتمه پاد متوقف خواهد شد. هیچ پارامتری به handler ارسال نمی‌شود.

توضیح دقیق‌تر درباره رفتار خاتمه را می‌توانید در
[خاتمه پادها](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) بیابید.

`StopSignal`

چرخه عمر StopSignal را می‌توان برای تعریف سیگنال توقفی به کار برد که هنگام متوقف شدن کانتینر به آن ارسال می‌شود. اگر این مقدار را تنظیم کنید، هر دستور `STOPSIGNAL` تعریف‌شده در ایمیج کانتینر را بازنویسی می‌کند.

توضیح دقیق‌تر درباره رفتار خاتمه با سیگنال‌های توقف سفارشی را می‌توانید در
[سیگنال‌های توقف](/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-stop-signals) بیابید.

### پیاده‌سازی‌های handler هوک

کانتینرها می‌توانند با پیاده‌سازی و ثبت یک handler برای یک هوک، به آن هوک دسترسی پیدا کنند.
سه نوع handler هوک وجود دارد که می‌توان برای کانتینرها پیاده‌سازی کرد:

* Exec - یک دستور مشخص، مانند `pre-stop.sh`، را درون cgroupها و namespaceهای کانتینر اجرا می‌کند.
  منابعی که این دستور مصرف می‌کند به حساب کانتینر گذاشته می‌شود.
* HTTP - یک درخواست HTTP را به یک endpoint مشخص روی کانتینر ارسال می‌کند.
* Sleep - کانتینر را برای مدت زمان مشخصی متوقف می‌کند.

### اجرای handler هوک

هنگامی که یک هوک مدیریت چرخه عمر کانتینر فراخوانی می‌شود،
سیستم مدیریتی کوبرنتیز handler را بر اساس اکشن هوک اجرا می‌کند؛
اکشن‌های `httpGet`، `tcpSocket` ([منسوخ‌شده](/docs/reference/generated/kubernetes-api/v1.35/#lifecyclehandler-v1-core))
و `sleep` توسط فرایند kubelet اجرا می‌شوند و `exec` درون کانتینر اجرا می‌شود.

فراخوانی handler هوک `PostStart` هنگام ایجاد کانتینر آغاز می‌شود،
یعنی ENTRYPOINT کانتینر و هوک `PostStart` به‌طور همزمان فعال می‌شوند.
(این بدان معناست که معمولاً استفاده از هوک HTTP برای `PostStart` منطقی نیست، زیرا
تضمینی وجود ندارد که هنگام اجرای هوک، فرایند کانتینر به‌طور کامل راه‌اندازی شده باشد.)
اگر اجرای هوک `PostStart` بیش از حد طول بکشد یا متوقف شود (hang کند)،
می‌تواند مانع از رفتن کانتینر به وضعیت `running` شود.

هوک‌های `PreStop` به‌صورت ناهمگام نسبت به سیگنال توقف کانتینر اجرا نمی‌شوند؛ هوک باید
اجرای خود را پیش از ارسال سیگنال TERM به پایان برساند. اگر یک هوک `PreStop` در حین
اجرا متوقف شود (hang کند)، فاز (phase) پاد `Terminating` خواهد بود و تا زمانی که پاد پس از
انقضای `terminationGracePeriodSeconds` کشته شود، در همان وضعیت باقی می‌ماند. این مهلت برای مجموع زمانی اعمال می‌شود که
اجرای هوک `PreStop` و توقف عادی کانتینر هر دو لازم دارند. برای مثال، اگر
`terminationGracePeriodSeconds` برابر ۶۰ باشد، هوک ۵۵ ثانیه طول بکشد تا کامل شود، و کانتینر
پس از دریافت سیگنال ۱۰ ثانیه برای توقف عادی نیاز داشته باشد، کانتینر پیش از آنکه بتواند
به‌طور عادی متوقف شود کشته خواهد شد، زیرا `terminationGracePeriodSeconds` از مجموع زمان
(۵۵+۱۰) لازم برای این دو کار کمتر است.

اگر هوک `PostStart` یا `PreStop` با شکست مواجه شود،
کانتینر کشته می‌شود.

کاربران باید handlerهای هوک خود را تا حد امکان سبک بنویسند.
با این حال مواردی وجود دارد که اجرای دستورهای طولانی‌مدت منطقی است،
مانند ذخیره حالت (state) پیش از متوقف کردن یک کانتینر.

### تضمین‌های تحویل هوک

تحویل هوک به‌صورت *حداقل یک‌بار* (at least once) در نظر گرفته شده است،
یعنی ممکن است یک هوک برای هر رویداد مشخص، مانند `PostStart` یا `PreStop`، چندین بار فراخوانی شود.
مدیریت صحیح این موضوع بر عهده پیاده‌سازی هوک است.

به‌طور کلی فقط یک‌بار تحویل انجام می‌شود.
برای مثال، اگر گیرنده هوک HTTP از کار افتاده باشد و نتواند ترافیک را دریافت کند،
تلاشی برای ارسال مجدد صورت نمی‌گیرد.
با این حال، در برخی موارد نادر ممکن است تحویل مضاعف رخ دهد.
برای نمونه، اگر kubelet در میانه ارسال یک هوک راه‌اندازی مجدد شود،
ممکن است هوک پس از بازگشت kubelet دوباره ارسال شود.

### اشکال‌زدایی handlerهای هوک

لاگ‌های یک handler هوک در رویدادهای (events) پاد نمایش داده نمی‌شوند.
اگر یک handler به هر دلیلی شکست بخورد، یک رویداد منتشر می‌کند.
برای `PostStart` این رویداد `FailedPostStartHook` و
برای `PreStop` رویداد `FailedPreStopHook` است.
برای ایجاد یک رویداد `FailedPostStartHook` ناموفق به‌دست خودتان، فایل
[lifecycle-events.yaml](https://k8s.io/examples/pods/lifecycle-events.yaml)
را طوری تغییر دهید که دستور postStart برابر "badcommand" شود و آن را اعمال کنید.
در ادامه نمونه‌ای از خروجی رویدادهای حاصل را می‌بینید که از اجرای `kubectl describe pod lifecycle-demo` به‌دست می‌آید:

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
* تجربه عملی کسب کنید:
  [متصل کردن handlerها به رویدادهای چرخه عمر کانتینر](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/).

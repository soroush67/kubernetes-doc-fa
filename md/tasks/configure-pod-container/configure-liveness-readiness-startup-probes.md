---
title: پیکربندی پروب‌های Liveness، Readiness و Startup
content_type: task
weight: 140
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید پروب‌های زنده‌بودن (liveness)، آمادگی (readiness) و راه‌اندازی (startup) را برای کانتینرها پیکربندی کنید.

برای اطلاعات بیشتر دربارهٔ پروب‌ها، به [پروب‌های Liveness، Readiness و Startup](/docs/concepts/workloads/pods/probes) مراجعه کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## تعریف یک فرمان زنده‌بودن

بسیاری از برنامه‌ها پس از مدتی طولانی اجرا، سرانجام به وضعیتی خراب می‌رسند و جز با راه‌اندازی مجدد نمی‌توانند بازیابی شوند. کوبرنتیز پروب‌های زنده‌بودن را برای تشخیص و رفع چنین وضعیت‌هایی فراهم می‌کند.

در این تمرین، یک Pod ایجاد می‌کنید که کانتینری مبتنی بر ایمیج `registry.k8s.io/busybox:1.27.2` را اجرا می‌کند. فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/probe/exec-liveness.yaml" %}}

در فایل پیکربندی می‌بینید که این Pod تنها یک `Container` دارد. فیلد `periodSeconds` مشخص می‌کند که kubelet باید هر ۵ ثانیه یک بار پروب زنده‌بودن را اجرا کند. فیلد `initialDelaySeconds` به kubelet می‌گوید که پیش از اجرای نخستین پروب، ۵ ثانیه صبر کند. برای اجرای پروب، kubelet فرمان `cat /tmp/healthy` را در کانتینر هدف اجرا می‌کند. اگر این فرمان با موفقیت اجرا شود، مقدار 0 را برمی‌گرداند و kubelet کانتینر را زنده و سالم در نظر می‌گیرد. اگر فرمان مقداری غیرصفر برگرداند، kubelet کانتینر را از بین می‌برد و دوباره راه‌اندازی می‌کند.

هنگامی که کانتینر شروع به کار می‌کند، این فرمان را اجرا می‌کند:

```shell
/bin/sh -c "touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600"
```

در ۳۰ ثانیهٔ نخست عمر کانتینر، فایلی با مسیر `/tmp/healthy` وجود دارد. بنابراین در این ۳۰ ثانیه، فرمان `cat /tmp/healthy` کد موفقیت برمی‌گرداند. پس از ۳۰ ثانیه، فرمان `cat /tmp/healthy` کد شکست برمی‌گرداند.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/exec-liveness.yaml
```

پیش از گذشت ۳۰ ثانیه، رویدادهای Pod را مشاهده کنید:

```shell
kubectl describe pod liveness-exec
```

خروجی نشان می‌دهد که هنوز هیچ پروب زنده‌بودنی شکست نخورده است:

```none
Type    Reason     Age   From               Message
----    ------     ----  ----               -------
Normal  Scheduled  11s   default-scheduler  Successfully assigned default/liveness-exec to node01
Normal  Pulling    9s    kubelet, node01    Pulling image "registry.k8s.io/busybox:1.27.2"
Normal  Pulled     7s    kubelet, node01    Successfully pulled image "registry.k8s.io/busybox:1.27.2"
Normal  Created    7s    kubelet, node01    Created container liveness
Normal  Started    7s    kubelet, node01    Started container liveness
```

پس از ۳۵ ثانیه، دوباره رویدادهای Pod را مشاهده کنید:

```shell
kubectl describe pod liveness-exec
```

در انتهای خروجی، پیام‌هایی دیده می‌شود که نشان می‌دهند پروب‌های زنده‌بودن شکست خورده‌اند و کانتینرهای ناموفق از بین رفته و دوباره ایجاد شده‌اند.

```none
Type     Reason     Age                From               Message
----     ------     ----               ----               -------
Normal   Scheduled  57s                default-scheduler  Successfully assigned default/liveness-exec to node01
Normal   Pulling    55s                kubelet, node01    Pulling image "registry.k8s.io/busybox:1.27.2"
Normal   Pulled     53s                kubelet, node01    Successfully pulled image "registry.k8s.io/busybox:1.27.2"
Normal   Created    53s                kubelet, node01    Created container liveness
Normal   Started    53s                kubelet, node01    Started container liveness
Warning  Unhealthy  10s (x3 over 20s)  kubelet, node01    Liveness probe failed: cat: can't open '/tmp/healthy': No such file or directory
Normal   Killing    10s                kubelet, node01    Container liveness failed liveness probe, will be restarted
```

۳۰ ثانیهٔ دیگر صبر کنید و بررسی کنید که کانتینر دوباره راه‌اندازی شده است:

```shell
kubectl get pod liveness-exec
```

خروجی نشان می‌دهد که مقدار `RESTARTS` افزایش یافته است. توجه کنید که شمارندهٔ `RESTARTS` به محض بازگشت کانتینر ناموفق به وضعیت در حال اجرا افزایش می‌یابد:

```none
NAME            READY     STATUS    RESTARTS   AGE
liveness-exec   1/1       Running   1          1m
```

## تعریف یک درخواست HTTP برای بررسی زنده‌بودن

نوع دیگری از پروب زنده‌بودن از درخواست HTTP GET استفاده می‌کند. در ادامه، فایل پیکربندی Podای آمده است که کانتینری مبتنی بر ایمیج `registry.k8s.io/e2e-test-images/agnhost` را اجرا می‌کند.

{{% code_sample file="pods/probe/http-liveness.yaml" %}}

در فایل پیکربندی می‌بینید که این Pod تنها یک کانتینر دارد. فیلد `periodSeconds` مشخص می‌کند که kubelet باید هر ۳ ثانیه یک بار پروب زنده‌بودن را اجرا کند. فیلد `initialDelaySeconds` به kubelet می‌گوید که پیش از اجرای نخستین پروب، ۳ ثانیه صبر کند. برای اجرای پروب، kubelet یک درخواست HTTP GET به سروری می‌فرستد که در کانتینر اجرا می‌شود و به پورت 8080 گوش می‌دهد. اگر کنترل‌گر (handler) مسیر `/healthz` در سرور کد موفقیت برگرداند، kubelet کانتینر را زنده و سالم در نظر می‌گیرد. اگر کنترل‌گر کد شکست برگرداند، kubelet کانتینر را از بین می‌برد و دوباره راه‌اندازی می‌کند.

هر کدِ بزرگ‌تر یا مساوی 200 و کوچک‌تر از 400 نشان‌دهندهٔ موفقیت است. هر کد دیگری نشان‌دهندهٔ شکست است.

کد منبع این سرور را می‌توانید در
[server.go](https://github.com/kubernetes/kubernetes/blob/master/test/images/agnhost/liveness/server.go) ببینید.

در ۱۰ ثانیهٔ نخستی که کانتینر زنده است، کنترل‌گر `/healthz` وضعیت 200 را برمی‌گرداند. پس از آن، این کنترل‌گر وضعیت 500 را برمی‌گرداند.

```go
http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
    duration := time.Now().Sub(started)
    if duration.Seconds() > 10 {
        w.WriteHeader(500)
        w.Write([]byte(fmt.Sprintf("error: %v", duration.Seconds())))
    } else {
        w.WriteHeader(200)
        w.Write([]byte("ok"))
    }
})
```

kubelet سه ثانیه پس از شروع کانتینر، بررسی‌های سلامت را آغاز می‌کند. بنابراین چند بررسی سلامت نخست موفق خواهند بود. اما پس از ۱۰ ثانیه، بررسی‌های سلامت شکست می‌خورند و kubelet کانتینر را از بین می‌برد و دوباره راه‌اندازی می‌کند.

برای آزمودن بررسی زنده‌بودن HTTP، یک Pod ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/http-liveness.yaml
```

پس از ۱۰ ثانیه، رویدادهای Pod را مشاهده کنید تا مطمئن شوید پروب‌های زنده‌بودن شکست خورده‌اند و کانتینر دوباره راه‌اندازی شده است:

```shell
kubectl describe pod liveness-http
```

در نسخه‌های پس از v1.13، تنظیمات متغیرهای محیطی پراکسی HTTP محلی تأثیری بر پروب زنده‌بودن HTTP ندارند.

### استفاده از HTTP/2 بدون رمزنگاری (h2c) در پروب‌های HTTP {#use-h2c-with-http-probes}

{{< feature-state feature_gate_name="H2CContainerProbe" >}}

به‌طور پیش‌فرض، `kubelet` هنگام اجرای پروب HTTP، درخواست‌های HTTP/1.1 می‌فرستد. اگر برنامهٔ شما نقاط پایانی سلامت را فقط از طریق HTTP/2 بدون رمزنگاری (h2c) ارائه می‌کند، می‌توانید فیلد `protocol` را به فیلد `httpGet` در مشخصات پروب اضافه کنید و مقدار `HTTP2` را برای آن تعیین کنید. برای این کار باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `H2CContainerProbe` هم در `kube-apiserver` و هم در `kubelet` فعال باشد.

{{% code_sample file="pods/probe/h2c-liveness.yaml" %}}

هنگامی که مقدار `protocol` برابر `HTTP2` باشد، `kubelet` با استفاده از HTTP/2 بدون رمزنگاری (h2c)، یعنی HTTP/2 روی TCP ساده و بدون TLS، متصل می‌شود. پیکربندی‌های زیر پشتیبانی نمی‌شوند:

*   ترکیب `protocol: HTTP2` و `scheme: HTTPS`
*   ترکیب `protocol: HTTP2` با مقداری در فیلد `host`

اگر این feature gate غیرفعال باشد، API server فیلد `protocol` را از Podهای جدید یا به‌روزرسانی‌شده حذف می‌کند.

## تعریف یک پروب زنده‌بودن TCP

سومین نوع پروب زنده‌بودن از یک سوکت TCP استفاده می‌کند. با این پیکربندی، kubelet تلاش می‌کند روی پورت مشخص‌شده، سوکتی به کانتینر شما باز کند. اگر بتواند اتصال برقرار کند، کانتینر سالم در نظر گرفته می‌شود و اگر نتواند، شکست در نظر گرفته می‌شود.

{{% code_sample file="pods/probe/tcp-liveness-readiness.yaml" %}}

همان‌طور که می‌بینید، پیکربندی بررسی TCP بسیار شبیه به بررسی HTTP است. این مثال از هر دو پروب آمادگی و زنده‌بودن استفاده می‌کند. kubelet نخستین پروب زنده‌بودن را ۱۵ ثانیه پس از شروع کانتینر اجرا می‌کند. این پروب تلاش می‌کند روی پورت 8080 به کانتینر `goproxy` متصل شود. اگر پروب زنده‌بودن شکست بخورد، کانتینر دوباره راه‌اندازی می‌شود. kubelet این بررسی را هر ۱۰ ثانیه یک بار ادامه می‌دهد.

افزون بر پروب زنده‌بودن، این پیکربندی یک پروب آمادگی نیز دارد. kubelet نخستین پروب آمادگی را ۱۵ ثانیه پس از شروع کانتینر اجرا می‌کند. این پروب نیز مانند پروب زنده‌بودن تلاش می‌کند روی پورت 8080 به کانتینر `goproxy` متصل شود. اگر پروب موفق شود، Pod به‌عنوان آماده علامت‌گذاری می‌شود و از سرویس‌ها ترافیک دریافت می‌کند. اگر پروب آمادگی شکست بخورد، Pod به‌عنوان ناآماده علامت‌گذاری می‌شود و از هیچ سرویسی ترافیک دریافت نمی‌کند.

برای آزمودن بررسی زنده‌بودن TCP، یک Pod ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/tcp-liveness-readiness.yaml
```

پس از ۱۵ ثانیه، رویدادهای Pod را مشاهده کنید تا پروب‌های زنده‌بودن را بررسی کنید:

```shell
kubectl describe pod goproxy
```

## تعریف یک پروب زنده‌بودن gRPC

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

اگر برنامهٔ شما
[gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)
را پیاده‌سازی می‌کند، این مثال نشان می‌دهد که چگونه کوبرنتیز را پیکربندی کنید تا از آن برای بررسی زنده‌بودن برنامه استفاده کند. به همین شکل می‌توانید پروب‌های آمادگی و راه‌اندازی را نیز پیکربندی کنید.

در ادامه یک مانیفست نمونه آمده است:

{{% code_sample file="pods/probe/grpc-liveness.yaml" %}}

برای آزمودن بررسی زنده‌بودن gRPC، با فرمان زیر یک Pod ایجاد کنید. در این مثال، Pod مربوط به etcd طوری پیکربندی شده است که از پروب زنده‌بودن gRPC استفاده کند.

```shell
kubectl apply -f https://k8s.io/examples/pods/probe/grpc-liveness.yaml
```

پس از ۱۵ ثانیه، رویدادهای Pod را مشاهده کنید تا مطمئن شوید بررسی زنده‌بودن شکست نخورده است:

```shell
kubectl describe pod etcd-with-grpc
```

هنگام استفاده از پروب gRPC، باید به چند نکتهٔ فنی توجه کنید:

- پروب‌ها روی نشانی IP یا نام میزبان Pod اجرا می‌شوند. حتماً نقطهٔ پایانی gRPC خود را طوری پیکربندی کنید که به نشانی IP مربوط به Pod گوش دهد.
- پروب‌ها به‌طور پیش‌فرض بدون رمزنگاری متصل می‌شوند. برای آشنایی با نحوهٔ فعال‌سازی TLS، به [استفاده از TLS در پروب‌های gRPC](#grpc-probe-tls) مراجعه کنید.
- پروب‌های داخلی هیچ کد خطایی ندارند. همهٔ خطاها شکست پروب در نظر گرفته می‌شوند.
- اگر مقدار feature gate با نام `ExecProbeTimeout` برابر `false` باشد، ابزار grpc-health-probe تنظیم `timeoutSeconds` (با مقدار پیش‌فرض 1s) را رعایت **نمی‌کند**، در حالی که پروب داخلی در صورت پایان مهلت شکست می‌خورد.

### استفاده از TLS در پروب‌های gRPC {#grpc-probe-tls}

{{< feature-state feature_gate_name="GRPCContainerProbeTLS" >}}

به‌طور پیش‌فرض، `kubelet` بدون رمزنگاری به نقاط پایانی سلامت gRPC متصل می‌شود. اگر برنامهٔ شما gRPC را فقط از طریق TLS ارائه می‌کند، می‌توانید فیلد `mode` را به فیلد `grpc` در مشخصات پروب اضافه کنید و مقدار `TLS` را برای آن تعیین کنید. برای این کار باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `GRPCContainerProbeTLS` هم در `kube-apiserver` و هم در `kubelet` فعال باشد.

{{% code_sample file="pods/probe/grpc-tls-liveness.yaml" %}}

هنگامی که مقدار `mode` برابر `TLS` باشد، `kubelet` با گزینهٔ `InsecureSkipVerify` از طریق TLS متصل می‌شود و گواهی سرور را راستی‌آزمایی نمی‌کند. این رفتار با رفتار پروب‌های HTTPS یکسان است. راستی‌آزمایی گواهی پشتیبانی نمی‌شود.

اگر این feature gate غیرفعال باشد، `kube-apiserver` فیلد `mode` را از Podهای جدید یا به‌روزرسانی‌شده حذف می‌کند.

## استفاده از پورت نام‌دار

برای پروب‌های HTTP و TCP می‌توانید از یک [`port`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#ports) نام‌دار استفاده کنید. پروب‌های gRPC از پورت‌های نام‌دار پشتیبانی نمی‌کنند.

برای مثال:

```yaml
ports:
- name: liveness-port
  containerPort: 8080

livenessProbe:
  httpGet:
    path: /healthz
    port: liveness-port
```

## محافظت از کانتینرهای کندآغاز با پروب‌های راه‌اندازی {#define-startup-probes}

گاهی باید با برنامه‌هایی سروکار داشته باشید که در نخستین مقداردهی اولیه به زمان راه‌اندازی بیشتری نیاز دارند. در چنین مواردی، تنظیم پارامترهای پروب زنده‌بودن بدون از دست دادن واکنش سریع به بن‌بست‌ها، که انگیزهٔ اصلی استفاده از این پروب است، می‌تواند دشوار باشد. راه‌حل این است که یک پروب راه‌اندازی با همان فرمان یا بررسی HTTP یا TCP تنظیم کنید و مقدار `failureThreshold * periodSeconds` را به اندازه‌ای بزرگ انتخاب کنید که بدترین حالت زمان راه‌اندازی را پوشش دهد.

بنابراین، مثال قبلی به این شکل درمی‌آید:

```yaml
ports:
- name: liveness-port
  containerPort: 8080

livenessProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 1
  periodSeconds: 10

startupProbe:
  httpGet:
    path: /healthz
    port: liveness-port
  failureThreshold: 30
  periodSeconds: 10
```

به لطف پروب راه‌اندازی، برنامه حداکثر ۵ دقیقه (30 * 10 = 300s) فرصت دارد تا راه‌اندازی خود را کامل کند. به محض اینکه پروب راه‌اندازی یک بار موفق شود، پروب زنده‌بودن کار را به دست می‌گیرد تا به بن‌بست‌های کانتینر واکنش سریع نشان دهد. اگر پروب راه‌اندازی هرگز موفق نشود، کانتینر پس از ۳۰۰ ثانیه از بین می‌رود و تابع `restartPolicy` مربوط به Pod خواهد بود.

## تعریف پروب‌های آمادگی

گاهی برنامه‌ها به‌طور موقت قادر به پاسخ‌گویی به ترافیک نیستند. برای مثال، ممکن است برنامه‌ای هنگام راه‌اندازی نیاز داشته باشد داده‌های حجیم یا فایل‌های پیکربندی را بارگذاری کند، یا پس از راه‌اندازی به سرویس‌های خارجی وابسته باشد. در چنین مواردی نمی‌خواهید برنامه را از بین ببرید، اما نمی‌خواهید درخواستی هم به آن بفرستید. کوبرنتیز پروب‌های آمادگی را برای تشخیص و کاهش اثر این وضعیت‌ها فراهم می‌کند. Podی که کانتینرهایش گزارش می‌دهند آماده نیستند، از طریق Serviceهای کوبرنتیز ترافیکی دریافت نمی‌کند.

{{< note >}}
پروب‌های آمادگی در تمام چرخهٔ حیات کانتینر روی آن اجرا می‌شوند.
{{< /note >}}

{{< caution >}}
موفقیت پروب‌های آمادگی و زنده‌بودن به یکدیگر وابسته نیست. اگر می‌خواهید پیش از اجرای پروب آمادگی صبر کنید، باید از `initialDelaySeconds` یا `startupProbe` استفاده کنید.
{{< /caution >}}

پروب‌های آمادگی به شیوه‌ای مشابه پروب‌های زنده‌بودن پیکربندی می‌شوند. تنها تفاوت این است که به جای فیلد `livenessProbe` از فیلد `readinessProbe` استفاده می‌کنید.

```yaml
readinessProbe:
  exec:
    command:
    - /bin/cat
    - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```

پیکربندی پروب‌های آمادگی HTTP و TCP نیز دقیقاً همانند پروب‌های زنده‌بودن است.

پروب‌های آمادگی و زنده‌بودن را می‌توان به‌طور هم‌زمان برای یک کانتینر به کار برد. استفاده از هر دو تضمین می‌کند که ترافیک به کانتینری که برای دریافت آن آماده نیست نرسد و کانتینرها هنگام شکست دوباره راه‌اندازی شوند.

## {{% heading "whatsnext" %}}

* دربارهٔ [پروب‌های Liveness، Readiness و Startup](/docs/concepts/workloads/pods/probes/) بیشتر بیاموزید.
* برای مشاهدهٔ مشخصات کامل فیلدهای مربوط به پروب، به مرجع API مراجعه کنید:
  [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)،
  [Container](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)،
  [Probe](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Probe)

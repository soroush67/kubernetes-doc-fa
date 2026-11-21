---
title: درک معیارهای اطلاعات توقف ناشی از فشار (PSI)
content_type: reference
weight: 50
description: >-
  توضیح مفصل معیارهای اطلاعات توقف ناشی از فشار (PSI) و نحوهٔ استفاده از آن‌ها برای شناسایی فشار منابع در کوبرنتیز.
---

<!-- overview -->

{{< feature-state feature_gate_name="KubeletPSI" >}}

کوبرنتیز به‌عنوان یک قابلیت پایدار به شما امکان می‌دهد kubelet را طوری پیکربندی کنید که
[اطلاعات توقف ناشی از فشار](https://docs.kernel.org/accounting/psi.html)
(Pressure Stall Information یا PSI) هستهٔ لینوکس را برای مصرف CPU، حافظه و I/O جمع‌آوری کند. این اطلاعات در سطح نود، پاد و کانتینر جمع‌آوری می‌شود.
از نسخهٔ v.1.36 کوبرنتیز، مقدار [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `KubeletPSI` روی true قفل شده است و نمی‌توان آن را غیرفعال کرد.

معیارهای PSI از طریق دو منبع متفاوت در دسترس قرار می‌گیرند:
- [Summary API](/docs/reference/kubelet-api/stats.v1alpha1/) در kubelet که داده‌های PSI را در سطح نود، پاد و کانتینر ارائه می‌کند.
- نقطهٔ پایانی `/metrics/cadvisor` در kubelet که معیارهای PSI را در [قالب Prometheus](/docs/concepts/cluster-administration/system-metrics#psi-metrics) ارائه می‌کند.

### پیش‌نیازها

استفاده از اطلاعات توقف ناشی از فشار به موارد زیر روی نودهای لینوکسی شما نیاز دارد:

- نسخهٔ هستهٔ لینوکس باید **۴.۲۰ یا جدیدتر** باشد.
- هسته باید با گزینهٔ `CONFIG_PSI=y` کامپایل شده باشد. بیشتر توزیع‌های امروزی این گزینه را به‌طور پیش‌فرض فعال می‌کنند. برای بررسی پیکربندی هستهٔ خود می‌توانید دستور `zgrep CONFIG_PSI /proc/config.gz` را اجرا کنید.
- برخی توزیع‌های لینوکس ممکن است PSI را در هسته کامپایل کنند، اما آن را به‌طور پیش‌فرض غیرفعال نگه دارند. در این صورت، باید با افزودن پارامتر `psi=1` به خط فرمان هسته، آن را هنگام راه‌اندازی سیستم فعال کنید.
- نود باید از [cgroup v2](/docs/concepts/architecture/cgroups) استفاده کند.

<!-- body -->

## درک معیارهای PSI

معیارهای اطلاعات توقف ناشی از فشار (PSI) برای سه منبع ارائه می‌شوند: CPU، حافظه و I/O. این معیارها در دو نوع اصلی فشار دسته‌بندی می‌شوند: `some` و `full`.

*   **`some`**: این مقدار نشان می‌دهد که برخی از وظایف (یک یا چند وظیفه) در انتظار یک منبع متوقف شده‌اند. برای مثال، اگر برخی وظایف منتظر I/O باشند، این معیار افزایش می‌یابد. این مقدار می‌تواند نشانهٔ زودهنگامی از رقابت بر سر منابع باشد.
*   **`full`**: این مقدار نشان می‌دهد که *همهٔ* وظایف غیربیکار به‌طور هم‌زمان در انتظار یک منبع متوقف شده‌اند. این وضعیت نشان‌دهندهٔ کمبود شدیدتر منابع است که در آن کل سیستم نمی‌تواند پیشرفتی داشته باشد.

هر نوع فشار چهار معیار ارائه می‌دهد: `avg10`، `avg60`، `avg300` و `total`. مقادیر `avg` درصدی از زمان واقعی (wall-clock) را نشان می‌دهند که وظایف در میانگین‌های متحرک ۱۰ ثانیه‌ای، ۶۰ ثانیه‌ای و ۵ دقیقه‌ای متوقف بوده‌اند. مقدار `total` یک شمارندهٔ تجمعی برحسب میکروثانیه است که کل زمان توقف وظایف را نشان می‌دهد.

برای مثال، پرس‌وجوی زیر را از Summary API در نظر بگیرید:  
`kubectl get --raw "/api/v1/nodes/$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')/proxy/stats/summary" | jq '.pods[].containers[] | select(.name=="<CONTAINER_NAME>") | {name, cpu: .cpu.psi, memory: .memory.psi, io: .io.psi}'`. 
این پرس‌وجو اطلاعات را در قالب JSON به شکل زیر برمی‌گرداند.

```
{
  "name": "<CONTAINER_NAME>",
  "cpu": {
    "full": {
      "total": 0,
      "avg10": 0,
      "avg60": 0,
      "avg300": 0
    },
    "some": {
      "total": 35232438,
      "avg10": 0.74,
      "avg60": 0.52,
      "avg300": 0.21,
    },  
  },
  "memory": {
    "full": {
      "total": 539105,
      "avg10": 0,
      "avg60": 0,
      "avg300": 0
    },
    "some": {
      "total": 658164,
      "avg10": 0.01,
      "avg60": 0.01,
      "avg300": 0.00,
    },
    }
  },
  "io": {
    "full": {
      "total": 33190987,
      "avg10": 0.31,
      "avg60": 0.22,
      "avg300": 0.05,
    },
    "some": {
      "total": 40809937,
      "avg10": 0.52,
      "avg60": 0.45,
      "avg300": 0.12,
    }
  }
}
```

در اینجا یک سناریوی ساده از جهش ناگهانی را می‌بینیم. مقدار `0.74` برای `avg10` در cpu.some نشان می‌دهد که در ۱۰ ثانیهٔ گذشته، دست‌کم یک وظیفه در این کانتینر به مدت ۰.۷۴ درصد از زمان (۰.۰۰۷۴ ثانیه یا ۷۴ میلی‌ثانیه) در انتظار CPU متوقف بوده است. از آنجا که مقدار `avg10` (۰.۷۴) برای همین منبع به‌طور قابل‌توجهی بیشتر از `avg300` (۰.۲۱) است، این وضعیت به افزایش اخیر رقابت بر سر منابع اشاره دارد، نه به یک گلوگاه پایدار و بلندمدت. اگر این معیارها به‌طور پیوسته پایش شوند و مقادیر `avg300` نیز افزایش یابند، می‌توانیم مشکلی جدی‌تر و ماندگارتر را تشخیص دهیم!

علاوه بر این، توجه کنید که در این مثال `cpu.some` فشار را نشان می‌دهد، در حالی که `cpu.full` همچنان روی ۰.۰۰ باقی مانده است. این یعنی اگرچه برخی فرایندها در انتظار زمان CPU با تأخیر مواجه شده‌اند، کانتینر در مجموع همچنان در حال پیشرفت بوده است. مقدار غیرصفر برای full نشان می‌دهد که همهٔ وظایف غیربیکار به‌طور هم‌زمان متوقف شده‌اند که مشکلی بسیار بزرگ‌تر است.
اگرچه مقدار `total` به‌آسانی برای انسان قابل‌خواندن نیست، عدد 35232438 زمان تجمعی توقف را برحسب میکروثانیه نشان می‌دهد و امکان تشخیص جهش‌های تأخیری را فراهم می‌کند که ممکن است در میانگین‌ها دیده نشوند.

در پایان، اگر فشار I/O بالا را همراه با فشار حافظهٔ پایین مشاهده کنید، این وضعیت می‌تواند نشان دهد که برنامه منتظر توان عملیاتی دیسک است و مشکل آن کمبود RAM در دسترس نیست. در این حالت، حافظهٔ نود بیش از ظرفیت تخصیص داده نشده است و می‌توان تشخیص جداگانه‌ای را برای مصرف دیسک بررسی کرد.

## سناریوهای نمونه

می‌توانید با یک Pod ساده که ابزار آزمون فشار (stress-testing) دارد، فشار منابع ایجاد کنید و معیارهای PSI را مشاهده کنید. مثال‌های زیر از ایمیج کانتینر `agnhost` استفاده می‌کنند که ابزار `stress` را در خود دارد.

### ایجاد فشار CPU

یک Pod بسازید که با استفاده از ابزار `stress` فشار CPU ایجاد کند. این بار کاری بار سنگینی را روی یک هستهٔ CPU قرار می‌دهد.

فایلی با نام `cpu-pressure-pod.yaml` بسازید:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cpu-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: cpu-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    args:
    - "stress"
    - "--cpus"
    - "1"
    resources:
      limits:
        cpu: "500m"
      requests:
        cpu: "500m"
```

آن را روی کلاستر خود اعمال کنید: `kubectl apply -f cpu-pressure-pod.yaml`

#### مشاهدهٔ فشار CPU

پس از اجرای Pod، می‌توانید فشار CPU را از طریق Summary API یا نقطهٔ پایانی معیارهای Prometheus مشاهده کنید.

**با استفاده از Summary API:**

آمار خلاصهٔ نود خود را زیر نظر بگیرید. در یک ترمینال جداگانه، دستور زیر را اجرا کنید:
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("cpu-pressure-pod"))'
```
خواهید دید که معیارهای PSI از نوع `some` برای CPU در خروجی Summary API افزایش می‌یابند. مقدار `avg10` برای فشار `some` باید از صفر بالاتر برود که نشان می‌دهد وظایف مدتی را در انتظار CPU متوقف بوده‌اند.

**با استفاده از نقطهٔ پایانی معیارهای Prometheus:**

برای مشاهدهٔ معیار `container_pressure_cpu_waiting_seconds_total`، از نقطهٔ پایانی `/metrics/cadvisor` پرس‌وجو کنید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_cpu_waiting_seconds_total{container="cpu-stress"'
```
خروجی باید مقداری رو به افزایش را نشان دهد. این افزایش یعنی کانتینر مدتی را در انتظار منابع CPU متوقف بوده است.

#### پاک‌سازی

پس از پایان کار، Pod را پاک کنید:
```shell
kubectl delete pod cpu-pressure-pod
```

### ایجاد فشار حافظه

این مثال یک Pod می‌سازد که به‌طور پیوسته در فایل‌هایی در لایهٔ قابل‌نوشتن کانتینر می‌نویسد. این کار باعث رشد حافظهٔ نهان صفحه (page cache) هسته می‌شود و هسته را به بازپس‌گیری حافظه وادار می‌کند که در نتیجه فشار ایجاد می‌شود.

فایلی با نام `memory-pressure-pod.yaml` بسازید:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: memory-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: memory-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    command: ["/bin/sh", "-c"]
    args:
    - "i=0; while true; do dd if=/dev/zero of=testfile.$i bs=1M count=50 &>/dev/null; i=$(((i+1)%5)); sleep 0.1; done"
    resources:
      limits:
        memory: "200M"
      requests:
        memory: "200M"
```

آن را روی کلاستر خود اعمال کنید: `kubectl apply -f memory-pressure-pod.yaml`

#### مشاهدهٔ فشار حافظه

**با استفاده از Summary API:**

در خروجی خلاصه، افزایش معیارهای PSI از نوع `full` را برای حافظه مشاهده خواهید کرد که نشان می‌دهد سیستم زیر فشار قابل‌توجه حافظه قرار دارد.
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("memory-pressure-pod"))'
```

**با استفاده از نقطهٔ پایانی معیارهای Prometheus:**

برای مشاهدهٔ معیار `container_pressure_memory_waiting_seconds_total`، از نقطهٔ پایانی `/metrics/cadvisor` پرس‌وجو کنید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_memory_waiting_seconds_total{container="memory-stress"'
```
در خروجی، مقدار این معیار را رو به افزایش خواهید دید که نشان می‌دهد سیستم زیر فشار قابل‌توجه حافظه قرار دارد.

#### پاک‌سازی

پس از پایان کار، Pod را پاک کنید:
```shell
kubectl delete pod memory-pressure-pod
```

### ایجاد فشار I/O

این Pod با نوشتن مکرر یک فایل روی دیسک و استفاده از `sync` برای انتقال داده‌ها از حافظه به دیسک، فشار I/O ایجاد می‌کند. این کار موجب توقف‌های I/O می‌شود.

فایلی با نام `io-pressure-pod.yaml` بسازید:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: io-pressure-pod
spec:
  restartPolicy: Never
  containers:
  - name: io-stress
    image: registry.k8s.io/e2e-test-images/agnhost:2.47
    command: ["/bin/sh", "-c"]
    args:
      - "while true; do dd if=/dev/zero of=testfile bs=1M count=128 &>/dev/null; sync; rm testfile &>/dev/null; done"
```

این را روی کلاستر خود اعمال کنید: `kubectl apply -f io-pressure-pod.yaml`

#### مشاهدهٔ فشار I/O

**با استفاده از Summary API:**

با نوشتن پیوستهٔ Pod روی دیسک، افزایش معیارهای PSI از نوع `some` را برای I/O خواهید دید.
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("io-pressure-pod"))'
```

**با استفاده از نقطهٔ پایانی معیارهای Prometheus:**

برای مشاهدهٔ معیار `container_pressure_io_waiting_seconds_total`، از نقطهٔ پایانی `/metrics/cadvisor` پرس‌وجو کنید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_io_waiting_seconds_total{container="io-stress"'
```
با نوشتن پیوستهٔ Pod روی دیسک، افزایش مقدار این معیار را خواهید دید.

#### پاک‌سازی

پس از پایان کار، Pod را پاک کنید:
```shell
kubectl delete pod io-pressure-pod
```

## {{% heading "whatsnext" %}}

صفحه‌های وظیفهٔ مربوط به [عیب‌یابی کلاسترها](/docs/tasks/debug/debug-cluster/) توضیح می‌دهند
که چگونه می‌توان از خط لولهٔ معیارهایی استفاده کرد که به این داده‌ها متکی است.

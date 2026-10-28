---
title: درک متریک‌های اطلاعات توقف ناشی از فشار (PSI)
content_type: reference
weight: 50
description: >-
  توضیح تفصیلی متریک‌های اطلاعات توقف ناشی از فشار (Pressure Stall Information یا PSI) و نحوهٔ استفاده از آن‌ها برای شناسایی فشار منابع در کوبرنتیز.
---

<!-- overview -->

{{< feature-state feature_gate_name="KubeletPSI" >}}

به‌عنوان یک قابلیت پایدار، کوبرنتیز به شما امکان می‌دهد kubelet را طوری پیکربندی کنید که اطلاعات [Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
(PSI) هستهٔ لینوکس را برای مصرف CPU، حافظه و I/O جمع‌آوری کند. این اطلاعات در سطح نود، Pod و کانتینر جمع‌آوری می‌شود.
از کوبرنتیز نسخهٔ v.1.36 به بعد، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `KubeletPSI` روی true قفل شده است و نمی‌توان آن را غیرفعال کرد.

متریک‌های PSI از دو منبع مختلف در دسترس قرار می‌گیرند:
- [Summary API](/docs/reference/kubelet-api/stats.v1alpha1/) در kubelet که داده‌های PSI را در سطح نود، Pod و کانتینر ارائه می‌کند.
- نقطهٔ پایانی `/metrics/cadvisor` در kubelet که متریک‌های PSI را با [قالب Prometheus](/docs/concepts/cluster-administration/system-metrics#psi-metrics) ارائه می‌دهد.

### الزامات

اطلاعات توقف ناشی از فشار (Pressure Stall Information) به موارد زیر روی نودهای لینوکسی شما نیاز دارد:

- نسخهٔ هستهٔ لینوکس باید **4.20 یا جدیدتر** باشد.
- هسته باید با گزینهٔ `CONFIG_PSI=y` کامپایل شده باشد. بیشتر توزیع‌های مدرن این گزینه را به‌صورت پیش‌فرض فعال می‌کنند. می‌توانید پیکربندی هستهٔ خود را با اجرای `zgrep CONFIG_PSI /proc/config.gz` بررسی کنید.
- برخی توزیع‌های لینوکس ممکن است PSI را در هسته کامپایل کنند اما آن را به‌صورت پیش‌فرض غیرفعال نگه دارند. در این صورت باید آن را در زمان بوت با افزودن پارامتر `psi=1` به خط فرمان هسته فعال کنید.
- نود باید از [cgroup v2](/docs/concepts/architecture/cgroups) استفاده کند.

<!-- body -->

## درک متریک‌های PSI

متریک‌های اطلاعات توقف ناشی از فشار (PSI) برای سه منبع ارائه می‌شوند: CPU، حافظه و I/O. این متریک‌ها در دو نوع اصلی فشار دسته‌بندی می‌شوند: `some` و `full`.

*   **`some`**: این مقدار نشان می‌دهد که تعدادی از وظایف (یک یا چند وظیفه) روی یک منبع متوقف شده‌اند. برای مثال، اگر برخی وظایف منتظر I/O باشند، این متریک افزایش می‌یابد. این مقدار می‌تواند نشانهٔ اولیهٔ رقابت بر سر منابع باشد.
*   **`full`**: این مقدار نشان می‌دهد که *همهٔ* وظایف غیرِبیکار به‌طور هم‌زمان روی یک منبع متوقف شده‌اند. این وضعیت بیانگر کمبود شدیدتر منابع است، به‌طوری که کل سیستم قادر به پیشرفت نیست.

هر نوع فشار چهار متریک ارائه می‌کند: `avg10`، `avg60`، `avg300` و `total`. مقادیر `avg` درصد زمان واقعی (wall-clock) را نشان می‌دهند که وظایف در میانگین‌های متحرک ۱۰ ثانیه‌ای، ۶۰ ثانیه‌ای و ۵ دقیقه‌ای متوقف بوده‌اند. مقدار `total` یک شمارندهٔ تجمعی بر حسب میکروثانیه است که مجموع زمانی را نشان می‌دهد که وظایف متوقف بوده‌اند.

برای مثال، پرس‌وجوی زیر را از Summary API در نظر بگیرید:  
`kubectl get --raw "/api/v1/nodes/$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')/proxy/stats/summary" | jq '.pods[].containers[] | select(.name=="<CONTAINER_NAME>") | {name, cpu: .cpu.psi, memory: .memory.psi, io: .io.psi}'`. 
این پرس‌وجو اطلاعات را در قالب json و به‌صورت زیر برمی‌گرداند. 

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

این یک سناریوی ساده از جهش ناگهانی است. مقدار `avg10` برای cpu.some برابر `0.74` است و نشان می‌دهد که در ۱۰ ثانیهٔ گذشته، دست‌کم یک وظیفه در این کانتینر به مدت ۰٫۷۴ درصد از زمان (۰٫۰۰۷۴ ثانیه یا ۷۴ میلی‌ثانیه) روی CPU متوقف بوده است. از آنجا که مقدار `avg10` (برابر 0.74) به‌طور قابل‌توجهی از `avg300` (برابر 0.21) برای همان منبع بالاتر است، این وضعیت بیشتر نشان‌دهندهٔ افزایش اخیر رقابت بر سر منابع است تا یک گلوگاه پایدار و بلندمدت. اگر پایش به‌طور پیوسته ادامه یابد و متریک‌های `avg300` نیز افزایش یابند، می‌توان مشکلی جدی‌تر و ماندگارتر را تشخیص داد!

علاوه بر این، توجه کنید که در این مثال `cpu.some` فشار را نشان می‌دهد، در حالی که `cpu.full` برابر 0.00 باقی مانده است. این موضوع به ما می‌گوید که اگرچه برخی فرایندها در انتظار زمان CPU به تأخیر افتاده‌اند، کانتینر در کل همچنان در حال پیشرفت بوده است. مقدار غیرصفر برای full نشان می‌داد که همهٔ وظایف غیرِبیکار به‌طور هم‌زمان متوقف شده‌اند، که مشکلی بسیار بزرگ‌تر است.
اگرچه مقدار `total` برابر 35232438 برای انسان چندان خوانا نیست، زمان توقف تجمعی را بر حسب میکروثانیه نشان می‌دهد و امکان تشخیص جهش‌های تأخیر را فراهم می‌کند که ممکن است در میانگین‌ها دیده نشوند. 

در پایان، وقتی فشار I/O بالا همراه با فشار حافظهٔ پایین مشاهده می‌شود، این می‌تواند نشان دهد که برنامه به‌جای اینکه به دلیل کمبود RAM دچار مشکل شود، منتظر توان عملیاتی دیسک است. حافظهٔ نود بیش از حد تخصیص داده نشده است و می‌توان تشخیص دیگری را برای مصرف دیسک بررسی کرد. 

## سناریوهای نمونه

می‌توانید از یک Pod ساده همراه با یک ابزار تست استرس برای ایجاد فشار بر منابع و مشاهدهٔ متریک‌های PSI استفاده کنید. مثال‌های زیر از ایمیج کانتینر `agnhost` استفاده می‌کنند که شامل ابزار `stress` است.

### ایجاد فشار بر CPU

یک Pod ایجاد کنید که با استفاده از ابزار `stress` فشار CPU ایجاد کند. این بار کاری بار سنگینی را روی یک هستهٔ CPU قرار می‌دهد.

فایلی با نام `cpu-pressure-pod.yaml` ایجاد کنید:
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

پس از اینکه Pod در حال اجرا شد، می‌توانید فشار CPU را از طریق Summary API یا نقطهٔ پایانی متریک‌های Prometheus مشاهده کنید.

**استفاده از Summary API:**

آمار خلاصهٔ نود خود را مشاهده کنید. در یک ترمینال جداگانه، دستور زیر را اجرا کنید:
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("cpu-pressure-pod"))'
```
مشاهده خواهید کرد که متریک‌های `some` در PSI برای CPU در خروجی summary API افزایش می‌یابند. مقدار `avg10` برای فشار `some` باید از صفر بالاتر برود، که نشان می‌دهد وظایف زمانی را در حالت توقف روی CPU سپری می‌کنند.

**استفاده از نقطهٔ پایانی متریک‌های Prometheus:**

نقطهٔ پایانی `/metrics/cadvisor` را پرس‌وجو کنید تا متریک `container_pressure_cpu_waiting_seconds_total` را ببینید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_cpu_waiting_seconds_total{container="cpu-stress"'
```
خروجی باید مقداری افزایشی نشان دهد، که بیانگر آن است که کانتینر زمانی را در انتظار منابع CPU متوقف سپری می‌کند.

#### پاکسازی

پس از پایان کار، Pod را پاکسازی کنید:
```shell
kubectl delete pod cpu-pressure-pod
```

### ایجاد فشار بر حافظه

این مثال یک Pod ایجاد می‌کند که به‌طور پیوسته در فایل‌هایی در لایهٔ قابل‌نوشتن کانتینر می‌نویسد؛ این کار باعث رشد page cache هسته و اجبار به بازیابی حافظه می‌شود و در نتیجه فشار ایجاد می‌کند.

فایلی با نام `memory-pressure-pod.yaml` ایجاد کنید:
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

**استفاده از Summary API:**

در خروجی summary، افزایشی را در متریک‌های `full` در PSI برای حافظه مشاهده خواهید کرد، که نشان می‌دهد سیستم تحت فشار قابل‌توجه حافظه قرار دارد.
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("memory-pressure-pod"))'
```

**استفاده از نقطهٔ پایانی متریک‌های Prometheus:**

نقطهٔ پایانی `/metrics/cadvisor` را پرس‌وجو کنید تا متریک `container_pressure_memory_waiting_seconds_total` را ببینید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_memory_waiting_seconds_total{container="memory-stress"'
```
در خروجی، مقدار افزایشی را برای این متریک مشاهده خواهید کرد، که نشان می‌دهد سیستم تحت فشار قابل‌توجه حافظه قرار دارد.

#### پاکسازی

پس از پایان کار، Pod را پاکسازی کنید:
```shell
kubectl delete pod memory-pressure-pod
```

### ایجاد فشار بر I/O

این Pod با نوشتن مکرر یک فایل روی دیسک و استفاده از `sync` برای تخلیهٔ داده‌ها از حافظه، فشار I/O ایجاد می‌کند که منجر به توقف‌های I/O می‌شود.

فایلی با نام `io-pressure-pod.yaml` ایجاد کنید:
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

**استفاده از Summary API:**

با نوشتن پیوستهٔ Pod روی دیسک، افزایش متریک‌های `some` در PSI را برای I/O مشاهده خواهید کرد.
```shell
# Replace <node-name> with the name of a node in your cluster
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/stats/summary" | jq '.pods[] | select(.podRef.name | contains("io-pressure-pod"))'
```

**استفاده از نقطهٔ پایانی متریک‌های Prometheus:**

نقطهٔ پایانی `/metrics/cadvisor` را پرس‌وجو کنید تا متریک `container_pressure_io_waiting_seconds_total` را ببینید.
```shell
# Replace <node-name> with the name of the node where the pod is running
kubectl get --raw "/api/v1/nodes/<node-name>/proxy/metrics/cadvisor" | \
    grep 'container_pressure_io_waiting_seconds_total{container="io-stress"'
```
با نوشتن پیوستهٔ Pod روی دیسک، افزایش مقدار این متریک را مشاهده خواهید کرد.

#### پاکسازی

پس از پایان کار، Pod را پاکسازی کنید:
```shell
kubectl delete pod io-pressure-pod
```

## {{% heading "whatsnext" %}}

صفحات وظیفهٔ [عیب‌یابی کلاسترها](/docs/tasks/debug/debug-cluster/) دربارهٔ چگونگی استفاده از یک pipeline متریک‌ها که بر این داده‌ها تکیه دارد، توضیح می‌دهند.

---
reviewers:
- dchen1107
- egernst
- tallclair
title: سربار Pod
content_type: concept
weight: 30
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

هنگامی که یک Pod را روی یک نود اجرا می‌کنید، خود Pod مقداری از منابع سیستم را مصرف می‌کند. این
منابع افزون بر منابعی هستند که برای اجرای کانتینر(های) درون Pod لازم است.
در کوبرنتیز، _سربار Pod_ (Pod Overhead) راهی برای به حساب آوردن منابعی است که زیرساخت Pod
افزون بر درخواست‌ها و محدودیت‌های کانتینرها مصرف می‌کند.

<!-- body -->

در کوبرنتیز، سربار Pod در زمان
[پذیرش (admission)](/docs/reference/access-authn-authz/extensible-admission-controllers/#what-are-admission-webhooks)
و بر اساس سربار مرتبط با
[RuntimeClass](/docs/concepts/containers/runtime-class/) مربوط به Pod تنظیم می‌شود.

هنگام زمان‌بندی یک Pod، سربار آن افزون بر مجموع درخواست‌های منبع کانتینرها
در نظر گرفته می‌شود. به همین ترتیب، kubelet هنگام تعیین اندازهٔ cgroup مربوط به Pod
و هنگام رتبه‌بندی Podها برای بیرون‌رانی، سربار Pod را نیز لحاظ می‌کند.

## پیکربندی سربار Pod {#set-up}

باید اطمینان حاصل کنید که از یک `RuntimeClass` استفاده می‌شود که فیلد `overhead` را تعریف می‌کند.

## نمونهٔ استفاده

برای کار با سربار Pod، به یک RuntimeClass نیاز دارید که فیلد `overhead` را تعریف کند. برای
نمونه، می‌توانید از تعریف RuntimeClass زیر با یک container runtime مبتنی بر مجازی‌سازی
(در این مثال، Kata Containers در ترکیب با ناظر ماشین مجازی Firecracker)
استفاده کنید که به‌ازای هر Pod حدود ۱۲۰MiB برای ماشین مجازی و سیستم‌عامل مهمان مصرف می‌کند:

```yaml
# You need to change this example to match the actual runtime name, and per-Pod
# resource overhead, that the container runtime is adding in your cluster.
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: kata-fc
handler: kata-fc
overhead:
  podFixed:
    memory: "120Mi"
    cpu: "250m"
```

بارهای کاری‌ای که با تعیین handler مربوط به RuntimeClass با نام `kata-fc` ایجاد می‌شوند، سربارهای حافظه و
CPU را در محاسبات سهمیهٔ منابع، زمان‌بندی نود و نیز تعیین اندازهٔ cgroup مربوط به Pod در نظر می‌گیرند.

اجرای بار کاری نمونهٔ داده‌شده، یعنی test-pod، را در نظر بگیرید:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  runtimeClassName: kata-fc
  containers:
  - name: busybox-ctr
    image: busybox:1.28
    stdin: true
    tty: true
    resources:
      limits:
        cpu: 500m
        memory: 100Mi
  - name: nginx-ctr
    image: nginx
    resources:
      limits:
        cpu: 1500m
        memory: 100Mi
```

{{< note >}}
اگر در تعریف Pod تنها `limits` مشخص شده باشد، kubelet مقدار `requests` را از روی آن محدودیت‌ها استنتاج می‌کند و آن را برابر با `limits` تعریف‌شده قرار می‌دهد.
{{< /note >}}

در زمان پذیرش، [کنترل‌کنندهٔ پذیرش](/docs/reference/access-authn-authz/admission-controllers/) مربوط به RuntimeClass،
PodSpec بار کاری را به‌روزرسانی می‌کند تا `overhead` توصیف‌شده در RuntimeClass را در بر گیرد. اگر این فیلد از قبل در PodSpec تعریف شده باشد،
Pod رد می‌شود. در مثال داده‌شده، از آنجا که تنها نام RuntimeClass مشخص شده است، کنترل‌کنندهٔ پذیرش Pod را تغییر می‌دهد
تا یک `overhead` را در بر گیرد.

پس از اینکه کنترل‌کنندهٔ پذیرش RuntimeClass تغییرات را اعمال کرد، می‌توانید مقدار به‌روزشدهٔ
سربار Pod را بررسی کنید:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.overhead}'
```

خروجی چنین است:

```
map[cpu:250m memory:120Mi]
```

اگر یک [ResourceQuota](/docs/concepts/policy/resource-quotas/) تعریف شده باشد، مجموع درخواست‌های کانتینرها و نیز
فیلد `overhead` شمرده می‌شوند.

هنگامی که kube-scheduler تصمیم می‌گیرد کدام نود باید یک Pod جدید را اجرا کند، زمان‌بند `overhead` آن Pod
و نیز مجموع درخواست‌های کانتینرهای آن Pod را در نظر می‌گیرد. در این مثال، زمان‌بند
درخواست‌ها و سربار را با هم جمع می‌کند و سپس به دنبال نودی می‌گردد که ۲.۲۵ CPU و ۳۲۰ MiB حافظهٔ در دسترس داشته باشد.

پس از اینکه یک Pod روی یک نود زمان‌بندی شد، kubelet روی آن نود یک {{< glossary_tooltip
text="cgroup" term_id="cgroup" >}} جدید برای Pod ایجاد می‌کند. container runtime زیربنایی
کانتینرها را درون همین Pod ایجاد می‌کند.

اگر برای منبع، محدودیتی برای هر کانتینر تعریف شده باشد (QoS از نوع Guaranteed یا QoS از نوع Burstable با محدودیت‌های تعریف‌شده)،
kubelet یک حد بالا برای cgroup مربوط به Pod در ارتباط با آن منبع تنظیم می‌کند (cpu.cfs_quota_us برای CPU
و memory.limit_in_bytes برای حافظه). این حد بالا بر اساس مجموع محدودیت‌های کانتینرها به‌علاوهٔ `overhead`
تعریف‌شده در PodSpec است.

برای CPU، اگر Pod دارای QoS از نوع Guaranteed یا Burstable باشد، kubelet مقدار `cpu.shares` را بر اساس
مجموع درخواست‌های کانتینرها به‌علاوهٔ `overhead` تعریف‌شده در PodSpec تنظیم می‌کند.

با نگاهی به مثال ما، درخواست‌های کانتینرها را برای بار کاری بررسی کنید:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.containers[*].resources.limits}'
```

کل درخواست‌های کانتینرها ۲۰۰۰m CPU و ۲۰۰MiB حافظه است:

```
map[cpu: 500m memory:100Mi] map[cpu:1500m memory:100Mi]
```

این را با آنچه نود مشاهده می‌کند مقایسه کنید:

```bash
kubectl describe node | grep test-pod -B2
```

خروجی درخواست‌هایی برای ۲۲۵۰m CPU و ۳۲۰MiB حافظه نشان می‌دهد. این درخواست‌ها سربار Pod را نیز شامل می‌شوند:

```
  Namespace    Name       CPU Requests  CPU Limits   Memory Requests  Memory Limits  AGE
  ---------    ----       ------------  ----------   ---------------  -------------  ---
  default      test-pod   2250m (56%)   2250m (56%)  320Mi (1%)       320Mi (1%)     36m
```

## بررسی محدودیت‌های cgroup مربوط به Pod

cgroupهای حافظهٔ Pod را روی نودی که بار کاری روی آن اجرا می‌شود، بررسی کنید. در مثال زیر،
از [`crictl`](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md)
روی نود استفاده می‌شود که یک CLI برای container runtimeهای سازگار با CRI فراهم می‌کند. این یک
مثال پیشرفته برای نمایش رفتار سربار Pod است و انتظار نمی‌رود کاربران نیاز داشته باشند
cgroupها را مستقیماً روی نود بررسی کنند.

ابتدا، روی نود مربوطه، شناسهٔ Pod را تعیین کنید:

```bash
# Run this on the node where the Pod is scheduled
POD_ID="$(sudo crictl pods --name test-pod -q)"
```

از روی این شناسه می‌توانید مسیر cgroup مربوط به Pod را تعیین کنید:

```bash
# Run this on the node where the Pod is scheduled
sudo crictl inspectp -o=json $POD_ID | grep cgroupsPath
```

مسیر cgroup حاصل شامل کانتینر `pause` مربوط به Pod است. cgroup سطح Pod یک پوشه بالاتر قرار دارد.

```
  "cgroupsPath": "/kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2/7ccf55aee35dd16aca4189c952d83487297f3cd760f1bbf09620e206e7d0c27a"
```

در این مورد مشخص، مسیر cgroup مربوط به Pod برابر `kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2` است.
تنظیم cgroup سطح Pod را برای حافظه بررسی کنید:

```bash
# Run this on the node where the Pod is scheduled.
# Also, change the name of the cgroup to match the cgroup allocated for your pod.
 cat /sys/fs/cgroup/memory/kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2/memory.limit_in_bytes
```

همان‌طور که انتظار می‌رفت، این مقدار ۳۲۰ MiB است:

```
335544320
```

### مشاهده‌پذیری

برخی متریک‌های `kube_pod_overhead_*` در [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
در دسترس هستند تا به تشخیص زمان استفاده از سربار Pod و مشاهدهٔ پایداری بارهای کاری‌ای
که با سربار تعریف‌شده اجرا می‌شوند، کمک کنند.

## {{% heading "whatsnext" %}}

* دربارهٔ [RuntimeClass](/docs/concepts/containers/runtime-class/) بیشتر بیاموزید
* برای آگاهی بیشتر از زمینه، پیشنهاد بهبود [طراحی PodOverhead](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/688-pod-overhead)
  را بخوانید

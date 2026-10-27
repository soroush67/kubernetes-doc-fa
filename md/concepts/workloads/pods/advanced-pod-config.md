---
title: پیکربندی پیشرفته Pod
api_metadata:
- apiVersion: "v1"
  kind: "Pod"
content_type: concept
weight: 180
---

<!-- overview -->

این صفحه موضوعات پیشرفته پیکربندی Pod، از جمله [PriorityClassها](#priorityclasses)، [RuntimeClassها](#runtimeclasses) و
[security context](#security-context) درون Podها را پوشش می‌دهد و جنبه‌هایی از [زمان‌بندی](/docs/concepts/scheduling-eviction/#scheduling) را معرفی می‌کند.

<!-- body -->

## PriorityClassها

_PriorityClassها_ به شما امکان می‌دهند اهمیت Podها را نسبت به سایر Podها تعیین کنید.
اگر یک priority class به یک Pod اختصاص دهید، کوبرنتیز فیلد `.spec.priority` آن Pod را
بر اساس PriorityClass مشخص‌شده تنظیم می‌کند (نمی‌توانید `.spec.priority` را مستقیماً تنظیم کنید).
اگر یا هنگامی که یک Pod قابل زمان‌بندی نباشد و مشکل ناشی از کمبود منابع باشد، {{< glossary_tooltip term_id="kube-scheduler" text="kube-scheduler" >}}
تلاش می‌کند Podهای با اولویت پایین‌تر را {{< glossary_tooltip text="پیش‌دستی (preempt)" term_id="preemption" >}} کند
تا زمان‌بندی Pod با اولویت بالاتر ممکن شود.

PriorityClass یک آبجکت API در سطح کلاستر است که نام یک priority class را به یک مقدار اولویت صحیح نگاشت می‌کند. اعداد بزرگ‌تر نشان‌دهنده اولویت بالاتر هستند.

### تعریف یک PriorityClass

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 10000
globalDefault: false
description: "Priority class for high-priority workloads"
```

### مشخص کردن اولویت Pod با استفاده از یک PriorityClass

{{< highlight yaml "hl_lines=9" >}}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  priorityClassName: high-priority
{{< /highlight >}}

### PriorityClassهای داخلی

کوبرنتیز دو PriorityClass داخلی فراهم می‌کند:
- `system-cluster-critical`: برای مؤلفه‌های سیستمی که برای کلاستر حیاتی هستند
- `system-node-critical`: برای مؤلفه‌های سیستمی که برای نودهای منفرد حیاتی هستند. این بالاترین اولویتی است که Podها می‌توانند در کوبرنتیز داشته باشند.

برای اطلاعات بیشتر، به [اولویت و پیش‌دستی Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) مراجعه کنید.

## RuntimeClassها

یک _RuntimeClass_ به شما امکان می‌دهد محیط اجرای کانتینر سطح پایین را برای یک Pod مشخص کنید. این قابلیت زمانی مفید است که بخواهید برای انواع مختلف Pod، محیط‌های اجرای کانتینر متفاوتی مشخص کنید؛ برای مثال هنگامی که به سطوح جداسازی یا قابلیت‌های محیط اجرای متفاوتی نیاز دارید.

### Pod نمونه {#runtimeclass-pod-example}

{{< highlight yaml "hl_lines=6" >}}
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  containers:
  - name: mycontainer
    image: nginx
{{< /highlight >}}

یک [RuntimeClass](/docs/concepts/containers/runtime-class/) آبجکتی در سطح کلاستر است که نمایانگر یک محیط اجرای کانتینر است که روی برخی یا همه نودهای شما در دسترس است.

مدیر کلاستر محیط‌های اجرای مشخصی را که پشتیبان RuntimeClass هستند نصب و پیکربندی می‌کند.

ممکن است آن پیکربندی ویژه محیط اجرای کانتینر را روی همه نودها، یا شاید تنها روی برخی از آن‌ها، راه‌اندازی کند.

برای اطلاعات بیشتر، به مستندات [RuntimeClass](/docs/concepts/containers/runtime-class/) مراجعه کنید.

## پیکربندی security context در سطح Pod و کانتینر {#security-context}

فیلد `Security context` در مشخصات Pod کنترلی جزئی بر تنظیمات امنیتی Podها و کانتینرها فراهم می‌کند.

### `securityContext` در سطح کل Pod {#pod-level-security-context}

برخی جنبه‌های امنیتی برای کل Pod اعمال می‌شوند؛ برای جنبه‌های دیگر،
ممکن است بخواهید یک مقدار پیش‌فرض تنظیم کنید، بدون هیچ بازنویسی در سطح کانتینر.

در اینجا نمونه‌ای از استفاده از `securityContext` در سطح Pod آمده است:

#### Pod نمونه {#pod-level-security-context-example}

{{< highlight yaml "hl_lines=5-9" >}}
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:  # This applies to the entire Pod
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  containers:
  - name: sec-ctx-demo
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: ["sh", "-c", "sleep 1h"]
{{< /highlight >}}

### security context در سطح کانتینر {#container-level-security-context}

می‌توانید security context را تنها برای یک کانتینر مشخص تعیین کنید.
در اینجا یک نمونه آمده است:

#### Pod نمونه {#container-level-security-context-example}

{{< highlight yaml "hl_lines=9-17" >}}
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-2
spec:
  containers:
  - name: sec-ctx-demo-2
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      allowPrivilegeEscalation: false
      runAsNonRoot: true
      runAsUser: 1000
      capabilities:
        drop:
        - ALL
      seccompProfile:
        type: RuntimeDefault
{{< /highlight >}}

### گزینه‌های security context

- **شناسه‌های کاربر و گروه**: کنترل می‌کنند کانتینر با کدام کاربر/گروه اجرا شود
- **Capabilityها**: افزودن یا حذف capabilityهای لینوکس
- **پروفایل‌های Seccomp**: تنظیم پروفایل‌های محاسبات امن (secure computing)
- **گزینه‌های SELinux**: پیکربندی context مربوط به SELinux
- **AppArmor**: پیکربندی پروفایل‌های AppArmor برای کنترل دسترسی بیشتر
- **گزینه‌های Windows**: پیکربندی تنظیمات امنیتی مختص Windows

{{< caution >}}
همچنین می‌توانید از `securityContext` مربوط به Pod برای مجاز کردن
[_حالت ممتاز (privileged mode)_](/docs/concepts/security/linux-kernel-security-constraints/#privileged-containers)
در کانتینرهای لینوکس استفاده کنید. حالت ممتاز بسیاری از تنظیمات امنیتی دیگر در `securityContext` را بازنویسی می‌کند.
از این تنظیم استفاده نکنید، مگر اینکه نتوانید مجوزهای معادل را با استفاده از فیلدهای دیگر `securityContext` اعطا کنید.
می‌توانید کانتینرهای Windows را نیز در حالتی مشابهِ
ممتاز اجرا کنید؛ با تنظیم پرچم `windowsOptions.hostProcess` در
security context سطح Pod. برای جزئیات و دستورالعمل‌ها، به
[ایجاد یک Pod از نوع HostProcess در Windows](/docs/tasks/configure-pod-container/create-hostprocess-pod/) مراجعه کنید.
{{< /caution >}}

برای اطلاعات بیشتر، به [پیکربندی Security Context برای یک Pod یا کانتینر](/docs/tasks/configure-pod-container/security-context/) مراجعه کنید.

## تأثیرگذاری بر تصمیم‌های زمان‌بندی Pod {#scheduling}

کوبرنتیز چندین سازوکار فراهم می‌کند تا کنترل کنید Podهای شما روی کدام نودها زمان‌بندی شوند.

### انتخابگرهای نود (Node selectors)

ساده‌ترین شکل محدودیت انتخاب نود:

{{< highlight yaml "hl_lines=9-11" >}}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disktype: ssd
{{< /highlight >}}

### وابستگی نود (Node affinity)

وابستگی نود به شما امکان می‌دهد قواعدی مشخص کنید که نودهایی را که Pod شما می‌تواند روی آن‌ها زمان‌بندی شود محدود می‌کنند. در اینجا نمونه‌ای از یک Pod آمده است که ترجیح می‌دهد روی نودهایی اجرا شود که با برچسب قرار داشتن در یک قاره خاص مشخص شده‌اند و انتخاب را بر اساس مقدار برچسب [`topology.kubernetes.io/zone`](/docs/reference/labels-annotations-taints/#topologykubernetesiozone) انجام می‌دهد.

{{< highlight yaml "hl_lines=6-15" >}}
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - antarctica-east1
            - antarctica-west1
  containers:
  - name: with-node-affinity
    image: registry.k8s.io/pause:3.8
{{< /highlight >}}

### وابستگی و ضدوابستگی Pod (Pod affinity and anti-affinity)

افزون بر وابستگی نود، می‌توانید نودهایی را که یک Pod می‌تواند روی آن‌ها زمان‌بندی شود، بر اساس برچسب‌های _Podهای دیگری_ که از قبل روی نودها در حال اجرا هستند نیز محدود کنید. وابستگی Pod به شما امکان می‌دهد قواعدی درباره محل قرارگیری یک Pod نسبت به سایر Podها مشخص کنید.

{{< highlight yaml "hl_lines=6-15" >}}
apiVersion: v1
kind: Pod
metadata:
  name: with-pod-affinity
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - database
        topologyKey: topology.kubernetes.io/zone
  containers:
  - name: with-pod-affinity
    image: registry.k8s.io/pause:3.8
{{< /highlight >}}

### Tolerationها

_Tolerationها_ به Podها امکان می‌دهند روی نودهایی با taintهای منطبق زمان‌بندی شوند:

{{< highlight yaml "hl_lines=9-13" >}}
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: myapp
    image: nginx
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
{{< /highlight >}}

برای اطلاعات بیشتر، به [اختصاص Podها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/) مراجعه کنید.

## سربار Pod (Pod overhead)

سربار Pod به شما امکان می‌دهد منابعی را که زیرساخت Pod افزون بر درخواست‌ها و محدودیت‌های کانتینر مصرف می‌کند در نظر بگیرید.

{{< highlight yaml "hl_lines=7-10" >}}
---
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: kvisor-runtime
handler: kvisor-runtime
overhead:
  podFixed:
    memory: "2Gi"
    cpu: "500m"
---
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: kvisor-runtime
  containers:
  - name: myapp
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
{{< /highlight >}}


## {{% heading "whatsnext" %}}

* درباره [اولویت و پیش‌دستی Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) مطالعه کنید
* درباره [RuntimeClassها](/docs/concepts/containers/runtime-class/) مطالعه کنید
* [پیکربندی Security Context برای یک Pod یا کانتینر](/docs/tasks/configure-pod-container/security-context/) را بررسی کنید
* بیاموزید کوبرنتیز چگونه [Podها را به نودها اختصاص می‌دهد](/docs/concepts/scheduling-eviction/assign-pod-node/)
* [سربار Pod](/docs/concepts/scheduling-eviction/pod-overhead/)

---
title: استفاده از منابع در سطح Pod با مدیرهای منابع kubelet
reviewers:
- ffromani
- ndixita
content_type: tutorial
weight: 40
min-kubernetes-server-version: v1.36
---

<!-- overview -->

{{< feature-state feature_gate_name="PodLevelResourceManagers" >}}

این آموزش نشان می‌دهد که چگونه مدیرهای منابع kubelet (توپولوژی، CPU و حافظه) را برای پشتیبانی از تعریف منابع در سطح Pod پیکربندی کنید. با این کار می‌توانید *مدل‌های تخصیص ترکیبی* (hybrid allocation models) تعریف کنید. در این مدل‌ها برخی کانتینرها منابع زیرساختی انحصاری و هم‌تراز با NUMA دریافت می‌کنند و بقیه‌ی کانتینرها منابع باقی‌مانده را از یک مخزن اشتراکی در سطح Pod به‌طور مشترک استفاده می‌کنند.

برای آشنایی بیشتر با مفاهیم پشت این قابلیت، صفحه‌ی مفهومی
[مدیرهای منابع در سطح Pod](/docs/concepts/resource-management/pod-level-resource-managers/)
را مطالعه کنید.

<!-- lessoncontent -->

## {{% heading "objectives" %}}

-   پیکربندی مدیرهای منابع kubelet (CPU، حافظه و توپولوژی) برای پشتیبانی از منابع در سطح Pod.
-   استقرار بارهای کاری با دامنه‌ی `pod` در Topology Manager برای دستیابی به هم‌ترازی با یک نود NUMA، با ترکیبی از کانتینرهای انحصاری و اشتراکی.
-   بررسی و تأیید نحوه‌ی تقسیم منابع CPU و حافظه میان کانتینرهای انحصاری و مخزن اشتراکی Pod.
-   درک قواعد رد پذیرش (admission) در حالتی که مخزن اشتراکی سطح Pod خالی باشد.
-   استقرار بارهای کاری با دامنه‌ی `container` در Topology Manager، با تخصیص‌های ترکیبی برای کانتینرها.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

برای انجام این آموزش به موارد زیر نیاز دارید:

-   یک کلاستر کوبرنتیز با **نودهای کارگر لینوکسی** (مدیرهای منابع در سطح Pod روی نودهای ویندوزی پشتیبانی نمی‌شوند).
-   دست‌کم یک نود کارگر با **توپولوژی NUMA** (ترجیحاً با چند نود NUMA تا بتوانید هم‌ترازی را مشاهده کنید).
-   **دسترسی مدیریتی** (root یا `sudo`) روی نود یا نودهای کارگر، برای تغییر
    [پیکربندی `kubelet`](/docs/reference/config-api/kubelet-config.v1beta1/)
    و راه‌اندازی مجدد سرویس `kubelet`.
-   دسترسی به `kubectl` با مجوز ایجاد فضاهای نام و Podها.

اطمینان حاصل کنید که
[feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/) زیر
برای control plane و نودهای کارگر فعال باشند:

-   `PodLevelResources`
-   `PodLevelResourceManagers`

## ایجاد یک فضای نام {#create-namespace}

یک فضای نام (namespace) ایجاد کنید تا منابعی که در این آموزش ساخته می‌شوند از بقیه‌ی کلاستر جدا بمانند:

```shell
kubectl create namespace plrm-tutorial
```

## استفاده از دامنه‌ی pod با تخصیص ترکیبی {#use-pod-scope-with-mixed-allocation}

وقتی دامنه‌ی Topology Manager روی `pod` تنظیم شده باشد، `kubelet` بر اساس `.spec.resources` یک هم‌ترازی NUMA واحد برای کل Pod انجام می‌دهد. سپس بودجه‌ی منابع حاصل تقسیم می‌شود: کانتینرهایی که منابع `Guaranteed` درخواست می‌کنند سهم‌های انحصاری دریافت می‌کنند و کانتینرهایی که تخصیص انحصاری دریافت نمی‌کنند، بودجه‌ی باقی‌مانده را در یک مخزن اشتراکی سطح Pod به‌طور مشترک استفاده می‌کنند.

### گام ۱: پیکربندی kubelet برای دامنه‌ی pod

برای فعال‌کردن این رفتار، `kubelet` را روی نود یا نودهای کارگری که می‌خواهید این بارهای کاری را روی آن‌ها اجرا کنید، با سیاست‌های لازم پیکربندی کنید. می‌توانید
[پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/)
را برای آن نودها به شکل زیر به‌روزرسانی کنید:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
cpuManagerPolicy: "static"
memoryManagerPolicy: "Static"
topologyManagerScope: "pod"
topologyManagerPolicy: "single-numa-node"
```

-   مقادیر معتبر برای `topologyManagerPolicy` عبارت‌اند از
    `single-numa-node`، `restricted` یا `best-effort`. هنگام استفاده از مدیریت منابع در سطح Pod نمی‌توانید مقدار دیگری تعیین کنید.

برای اعمال پیکربندی، kubelet را دوباره راه‌اندازی کنید. برای مثال، در لینوکس با systemd از دستور `systemctl restart kubelet.service` استفاده کنید.

### گام ۲: استقرار یک Pod با تخصیص ترکیبی

مانیفست نمونه‌ی زیر را در نظر بگیرید. این Pod در سطح Pod (`.spec.resources`) بودجه‌ای در مجموع برابر با ۴ CPU درخواست می‌کند. درون این Pod:

-   کانتینر `main-app` تخصیص انحصاری ۲ هسته‌ی کامل CPU را درخواست می‌کند (`requests` = `limits` = 2 CPU).
-   از آنجا که `metrics-sidecar` و `logging-sidecar` درخواستی در سطح کانتینر تعیین نمی‌کنند، این دو کانتینر جانبی (sidecar) هسته‌های CPU باقی‌مانده در مخزن اشتراکی سطح Pod، یعنی ۲ هسته‌ی CPU، را به‌طور مشترک استفاده می‌کنند.

{{% code_sample file="pods/resource/pod-level-resource-managers-pod-scope-mixed.yaml" %}}

مانیفست را روی کلاستر خود اعمال کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-resource-managers-pod-scope-mixed.yaml --namespace=plrm-tutorial
```

### گام ۳: تأیید و بررسی تقسیم منابع

1.  بررسی کنید که Pod با موفقیت در حال اجرا باشد:

    ```shell
    kubectl get pod pod-scope-mixed --namespace=plrm-tutorial
    ```

2.  آنچه را در پشت صحنه رخ داده است بررسی کنید:

    ```mermaid
    flowchart TD
        subgraph Pod["Pod-Level Budget: 4 CPUs, 4Gi Memory"]
            direction TB
            C1["main-app<br/>(Exclusive: 2 CPUs, 2Gi Memory)"]
            subgraph Pool["Pod Shared Pool: 2 CPUs, 2Gi Memory"]
                C2["metrics-sidecar"]
                C3["logging-sidecar"]
            end
        end
    ```

    -   هم‌ترازی Pod: ابزار Topology Manager درخواست ۴ CPU در سطح Pod
        (`spec.resources`) را ارزیابی کرد و کل Pod را به یک نود NUMA واحد اختصاص داد.
    -   تخصیص انحصاری: ابزار CPU Manager یک سهم اختصاصی ۲ CPU به `main-app` تخصیص داد. محدودسازی (throttling) سهمیه‌ی CFS پردازنده برای `main-app` غیرفعال است و در نتیجه این کانتینر بدون محدودیت به آن هسته‌های انحصاری دسترسی دارد.
    -   مخزن اشتراکی Pod: ۲ CPU باقی‌مانده یک مخزن اشتراکی در سطح Pod تشکیل می‌دهند. کانتینرهای `metrics-sidecar` و `logging-sidecar` هیچ منبعی در سطح کانتینر تعیین نمی‌کنند (`resources: {}`)، بنابراین درون این مخزن اشتراکیِ ایزوله در سطح Pod و با اعمال سهمیه‌ی CFS اجرا می‌شوند. این مخزن اگرچه میان این دو کانتینر جانبی مشترک است، از بارهای کاری بیرونی روی نود جدا است. به این ترتیب کانتینرهای جانبی از محلی‌بودن (locality) اختصاصی NUMA بهره می‌برند و از رقابت بر سر منابع در سطح نود در امان می‌مانند.

## مشاهده‌ی محدودیت‌های پذیرش در حالت مخزن اشتراکی خالی {#empty-shared-pool-restrictions}

هنگام استفاده از دامنه‌ی `pod`، کنترل پذیرش `kubelet` مشخصات Podهایی را که به یک مخزن اشتراکی خالی منجر می‌شوند رد می‌کند، به شرط آنکه کانتینرهایی وجود داشته باشند که به این مخزن نیاز دارند.

اگر مجموع درخواست‌های منابع انحصاری کانتینرهای `Guaranteed` با کل بودجه‌ی سطح Pod برابر باشد و دست‌کم یک کانتینر دیگر به مخزن اشتراکی نیاز داشته باشد، `kubelet` آن Pod را رد می‌کند.

### گام ۴: بررسی مانیفست نامعتبر Pod

مانیفست زیر را در نظر بگیرید. این Pod در مجموع بودجه‌ای برابر با ۴ CPU درخواست می‌کند. کانتینر `container-a` یک CPU انحصاری و کانتینر `container-b` سه CPU انحصاری درخواست می‌کند (در مجموع ۴ CPU). کانتینر `container-c` منابع انحصاری درخواست نمی‌کند و به یک مخزن اشتراکی نیاز دارد، اما هیچ CPUای باقی نمانده است:

{{% code_sample file="pods/resource/pod-level-resource-managers-empty-shared-pool.yaml" %}}

### گام ۵: تلاش برای استقرار و مشاهده‌ی رد شدن

1.  مانیفست را اعمال کنید:

    ```shell
    kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-resource-managers-empty-shared-pool.yaml --namespace=plrm-tutorial
    ```

2.  رویدادهای Pod را بررسی کنید تا خطای پذیرش را ببینید:

    ```shell
    kubectl describe pod empty-shared-pool --namespace=plrm-tutorial
    ```

    به پیام رویداد توجه کنید. این پیام توضیح می‌دهد که `kubelet` این Pod را رد کرده است، زیرا مخزن اشتراکی سطح Pod برای کانتینرهایی که به منابع اشتراکی نیاز دارند خالی می‌ماند:

    ```
    Status:           Failed
    Reason:           TopologyAffinityError
    Message:          Pod was rejected: Pod Scope pod with pod-level resources failed admission under pod-scope topology manager
    ```

    ```mermaid
    flowchart TD
        subgraph Pod["Pod-Level Budget: 4 CPUs, 4Gi Memory"]
            direction TB
            C1["container-a<br/>(Exclusive: 1 CPU, 1Gi Memory)"]
            C2["container-b<br/>(Exclusive: 3 CPUs, 3Gi Memory)"]
            subgraph Pool["Pod Shared Pool: 0 CPUs, 0Gi Memory"]
                C3["container-c<br/>(Requires shared pool)"]
            end
        end
        Pool --> Rejection["Admission Error: Pod Rejected!"]
        style Rejection fill:#ffcccc,stroke:#ff0000,stroke-width:2px
    ```

## استفاده از دامنه‌ی container با تخصیص ترکیبی {#use-container-scope-with-mixed-allocation}

می‌توانید دامنه‌ی Topology Manager را روی `container` نیز تنظیم کنید. در این حالت، `kubelet` هر کانتینر را جداگانه برای تخصیص انحصاری ارزیابی می‌کند، در حالی که بودجه‌ی کلی Pod در `.spec.resources` همچنان مرزهای QoS و محدودیت‌های cgroup را اعمال می‌کند.

### گام ۶: پیکربندی kubelet برای دامنه‌ی container

[پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/) را روی
نود یا نودهای کارگر مورد نظر برای دامنه‌ی `container` به‌روزرسانی کنید:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
cpuManagerPolicy: "static"
memoryManagerPolicy: "Static"
topologyManagerScope: "container"
topologyManagerPolicy: "single-numa-node"
```

برای اعمال پیکربندی، kubelet را دوباره راه‌اندازی کنید. برای مثال، در لینوکس با systemd از دستور `systemctl restart kubelet.service` استفاده کنید.

### گام ۷: استقرار یک بار کاری ترکیبی با دامنه‌ی container

مانیفست نمونه‌ی زیر را در نظر بگیرید. این Pod در مجموع بودجه‌ای برابر با ۴ CPU دارد:

-   کانتینر `infrastructure-sidecar` یک سهم انحصاری ۲ CPU درخواست می‌کند (`requests` =
    `limits` = 2 CPU).
-   کانتینرهای `worker-1` و `worker-2` درخواستی در سطح کانتینر تعیین نمی‌کنند و در مخزن اشتراکی عمومی کل نود اجرا می‌شوند.

{{% code_sample file="pods/resource/pod-level-resource-managers-container-scope-mixed.yaml" %}}

مانیفست را اعمال کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-resource-managers-container-scope-mixed.yaml --namespace=plrm-tutorial
```

### گام ۸: تأیید استقرار

1.  بررسی کنید که Pod در حال اجرا باشد:

    ```shell
    kubectl get pod container-scope-mixed --namespace=plrm-tutorial
    ```

2.  آنچه را در پشت صحنه رخ داده است بررسی کنید:

    ```mermaid
    flowchart TD
        subgraph Pod["Pod-Level Budget: 4 CPUs, 4Gi Memory"]
            direction TB
            C1["infrastructure-sidecar<br/>(Exclusive NUMA Slice: 2 CPUs, 2Gi Memory)"]
            subgraph NodePool["Node Shared Pool: Pod-level limit"]
                C3["worker-2"]
                C2["worker-1"]
            end
        end
    ```

    -   هم‌ترازی در دامنه‌ی کانتینر: در دامنه‌ی `container`، کوبلت (`kubelet`) کانتینرها را جداگانه ارزیابی می‌کند. کانتینر `infrastructure-sidecar` یک سهم انحصاری و هم‌تراز با NUMA به اندازه‌ی ۲ CPU را مستقیماً از مخزن قابل تخصیص نود دریافت می‌کند.
    -   مخزن اشتراکی نود: کانتینرهای `worker-1` و `worker-2` هیچ درخواست منبعی در سطح کانتینر تعیین نمی‌کنند (`resources: {}`)، بنابراین در دامنه‌ی `container` در مخزن اشتراکی عمومی نود اجرا می‌شوند (و نه در یک مخزن ایزوله در سطح Pod).
    -   اعمال محدودیت Pod: مجموع مصرف CPU همه‌ی کانتینرها همچنان با محدودیت سطح Pod
        (`spec.resources.limits`) به ۴ CPU محدود می‌ماند.

## {{% heading "cleanup" %}}

فضای نام و همه‌ی Podهای نمونه‌ای را که در این آموزش ایجاد شده‌اند حذف کنید:

```shell
kubectl delete namespace plrm-tutorial
```

## {{% heading "whatsnext" %}}

- مستندات مفهومی را مطالعه کنید:
  - [مدیرهای منابع در سطح Pod](/docs/concepts/resource-management/pod-level-resource-managers/)
- با نحوه‌ی پیکربندی مدیرهای منابع در سطح نود آشنا شوید:
  - [کنترل سیاست‌های مدیریت توپولوژی روی یک نود](/docs/tasks/administer-cluster/topology-manager/)
  - [کنترل سیاست‌های مدیریت CPU روی نود](/docs/tasks/administer-cluster/cpu-management-policies/)
  - [استفاده از مدیر حافظه‌ی آگاه از NUMA](/docs/tasks/administer-cluster/memory-manager/)
- با نحوه‌ی تخصیص منابع آشنا شوید:
  - [تخصیص منابع CPU و حافظه در سطح Pod](/docs/tasks/configure-pod-container/assign-pod-level-resources/)
  - [تخصیص منابع CPU به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-cpu-resource/)
  - [تخصیص منابع حافظه به کانتینرها و Podها](/docs/tasks/configure-pod-container/assign-memory-resource/)

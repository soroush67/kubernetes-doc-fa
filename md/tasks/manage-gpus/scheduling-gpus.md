---
reviewers:
- vishh
content_type: concept
title: زمان‌بندی GPUها
description: GPUها را پیکربندی و زمان‌بندی کنید تا نودهای یک کلاستر بتوانند از آن‌ها به‌عنوان منبع استفاده کنند.
---

<!-- overview -->

{{< feature-state state="stable" for_k8s_version="v1.26" >}}

کوبرنتیز با استفاده از
{{< glossary_tooltip text="افزونه‌های دستگاه" term_id="device-plugin" >}}
پشتیبانی **پایدار** از مدیریت GPUهای AMD و NVIDIA (واحدهای پردازش گرافیکی) را در نودهای مختلف کلاستر شما فراهم می‌کند.

این صفحه توضیح می‌دهد که کاربران چگونه می‌توانند از GPUها استفاده کنند و برخی از محدودیت‌های این پیاده‌سازی را نیز به‌طور خلاصه بیان می‌کند.

<!-- body -->

## استفاده از افزونه‌های دستگاه

کوبرنتیز افزونه‌های دستگاه (device plugins) را پیاده‌سازی می‌کند تا Podها بتوانند به قابلیت‌های سخت‌افزاری تخصصی مانند GPUها دسترسی داشته باشند.

{{% thirdparty-content %}}

شما به‌عنوان مدیر کلاستر باید درایورهای GPU را از فروشنده‌ی سخت‌افزار مربوطه روی نودها نصب کنید و افزونه‌ی دستگاه متناظر را که فروشنده‌ی GPU ارائه کرده است اجرا کنید. پیوندهای زیر به دستورالعمل‌های فروشندگان اشاره می‌کنند:

* [AMD](https://github.com/ROCm/k8s-device-plugin#deployment)
* [Intel](https://intel.github.io/intel-device-plugins-for-kubernetes/cmd/gpu_plugin/README.html)
* [NVIDIA](https://github.com/NVIDIA/k8s-device-plugin#quick-start)

پس از نصب افزونه، کلاستر شما یک منبع سفارشی قابل زمان‌بندی مانند `amd.com/gpu` یا `nvidia.com/gpu` را در دسترس قرار می‌دهد.

می‌توانید با درخواست این منبع سفارشی GPU، همان‌طور که `cpu` یا `memory` را درخواست می‌کنید، از این GPUها در کانتینرهای خود استفاده کنید.
با این حال، در نحوه‌ی تعیین نیازمندی‌های منابع برای دستگاه‌های سفارشی محدودیت‌هایی وجود دارد.

GPUها فقط باید در بخش `limits` مشخص شوند، به این معنا که:
* می‌توانید `limits` مربوط به GPU را بدون تعیین `requests` مشخص کنید، زیرا
  کوبرنتیز به‌طور پیش‌فرض مقدار limit را به‌عنوان مقدار request در نظر می‌گیرد.
* می‌توانید GPU را هم در `limits` و هم در `requests` مشخص کنید، اما این دو مقدار
  باید با هم برابر باشند.
* نمی‌توانید `requests` مربوط به GPU را بدون تعیین `limits` مشخص کنید.

در ادامه نمونه‌ای از مانیفست یک Pod را می‌بینید که یک GPU درخواست می‌کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-vector-add
spec:
  restartPolicy: OnFailure
  containers:
    - name: example-vector-add
      image: "registry.example/example-vector-add:v42"
      resources:
        limits:
          gpu-vendor.example/example-gpu: 1 # requesting 1 GPU
```

## مدیریت کلاسترهایی با انواع مختلف GPU

اگر نودهای مختلف کلاستر شما انواع متفاوتی از GPU داشته باشند، می‌توانید
از [برچسب‌های نود و انتخابگرهای نود](/docs/tasks/configure-pod-container/assign-pods-nodes/)
برای زمان‌بندی Podها روی نودهای مناسب استفاده کنید.

برای نمونه:

```shell
# Label your nodes with the accelerator type they have.
kubectl label nodes node1 accelerator=example-gpu-x100
kubectl label nodes node2 accelerator=other-gpu-k915
```

کلید برچسب `accelerator` فقط یک نمونه است؛ در صورت تمایل می‌توانید
از کلید برچسب دیگری استفاده کنید.

## برچسب‌گذاری خودکار نودها {#node-labeller}

شما به‌عنوان مدیر کلاستر می‌توانید با استقرار [Node Feature Discovery](https://github.com/kubernetes-sigs/node-feature-discovery) (NFD) کوبرنتیز، همه‌ی نودهای دارای GPU را به‌طور خودکار شناسایی و برچسب‌گذاری کنید.
ابزار NFD قابلیت‌های سخت‌افزاری موجود در هر نود از کلاستر کوبرنتیز را تشخیص می‌دهد.
معمولاً NFD طوری پیکربندی می‌شود که این قابلیت‌ها را به‌صورت برچسب‌های نود اعلام کند، اما می‌تواند منابع توسعه‌یافته (extended resources)، حاشیه‌نویسی‌ها (annotations) و taintهای نود را نیز اضافه کند.
ابزار NFD با همه‌ی [نسخه‌های پشتیبانی‌شده‌ی](/releases/version-skew-policy/#supported-versions) کوبرنتیز سازگار است.
به‌طور پیش‌فرض، NFD برای قابلیت‌های شناسایی‌شده [برچسب‌های قابلیت](https://kubernetes-sigs.github.io/node-feature-discovery/master/usage/features.html) ایجاد می‌کند.
مدیران کلاستر همچنین می‌توانند از NFD برای اعمال taint روی نودهای دارای قابلیت‌های خاص استفاده کنند تا فقط Podهایی که آن قابلیت‌ها را درخواست می‌کنند روی آن نودها زمان‌بندی شوند.

همچنین به افزونه‌ای برای NFD نیاز دارید که برچسب‌های مناسب را به نودهای شما اضافه کند؛ این برچسب‌ها ممکن است عمومی یا مختص فروشنده باشند. فروشنده‌ی GPU شما ممکن است یک افزونه‌ی شخص ثالث برای NFD ارائه کند؛ برای جزئیات بیشتر به مستندات آن فروشنده مراجعه کنید.

{{< highlight yaml "linenos=false,hl_lines=7-18" >}}
apiVersion: v1
kind: Pod
metadata:
  name: example-vector-add
spec:
  restartPolicy: OnFailure
  # می‌توانید از node affinity کوبرنتیز برای زمان‌بندی این Pod روی نودی استفاده کنید
  # که نوع GPU موردنیاز کانتینر آن را برای کارکرد فراهم می‌کند
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: "gpu.gpu-vendor.example/installed-memory"
            operator: Gt # (بزرگ‌تر از)
            values: ["40535"]
          - key: "feature.node.kubernetes.io/pci-10.present" # برچسب قابلیت NFD
            values: ["true"] # (اختیاری) فقط روی نودهای دارای دستگاه PCI شماره‌ی 10 زمان‌بندی شود
  containers:
    - name: example-vector-add
      image: "registry.example/example-vector-add:v42"
      resources:
        limits:
          gpu-vendor.example/example-gpu: 1 # درخواست 1 GPU
{{< /highlight >}}

#### پیاده‌سازی‌های فروشندگان GPU

- [Intel](https://intel.github.io/intel-device-plugins-for-kubernetes/cmd/gpu_plugin/README.html)
- [NVIDIA](https://github.com/NVIDIA/k8s-device-plugin)

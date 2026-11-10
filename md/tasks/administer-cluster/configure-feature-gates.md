---
title: فعال یا غیرفعال کردن feature gateها
content_type: task
weight: 60
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه feature gateها را فعال یا غیرفعال کنید تا قابلیت‌های مشخصی از کوبرنتیز را در کلاستر خود کنترل کنید. با فعال کردن feature gateها می‌توانید قابلیت‌های آلفا یا بتا را پیش از آنکه به‌طور عمومی در دسترس قرار گیرند، آزمایش کنید و به کار ببرید.

{{< note >}}
برخی از gateهای پایدار (GA) را نیز می‌توان غیرفعال کرد؛ این امکان معمولاً تا یک نسخهٔ فرعی (minor) پس از رسیدن به GA وجود دارد. اما اگر چنین کنید، ممکن است کلاستر شما دیگر با استانداردهای انطباق کوبرنتیز سازگار نباشد.
{{< /note >}}

<!--
Changes from original PR proposal:
- Added note about conformance implications when disabling stable gates
- Corrected --help behavior: all components show all gates due to shared definitions
- Clarified that not all components support configuration files (e.g., kube-controller-manager)
- Specified that verification methods apply to kubeadm static pod deployments
- Added context about kubeadm's distributed configuration approach
-->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

همچنین به موارد زیر نیاز دارید:

* دسترسی مدیریتی به کلاستر
* دانستن اینکه کدام feature gate را می‌خواهید فعال کنید (به [مرجع Feature Gateها](/docs/reference/command-line-tools-reference/feature-gates/) مراجعه کنید)

{{< note >}}
قابلیت‌های GA (پایدار) همیشه به‌طور پیش‌فرض فعال هستند. معمولاً gateها را برای قابلیت‌های آلفا یا بتا پیکربندی می‌کنید.
{{< /note >}}

<!-- steps -->

## آشنایی با سطح بلوغ feature gateها

پیش از فعال کردن یک feature gate، سطح بلوغ آن قابلیت را در [مرجع Feature Gateها](/docs/reference/command-line-tools-reference/feature-gates/) بررسی کنید:

- **آلفا**: به‌طور پیش‌فرض غیرفعال است و ممکن است اشکال داشته باشد. فقط در کلاسترهای آزمایشی از آن استفاده کنید.
- **بتا**: معمولاً به‌طور پیش‌فرض فعال است و به‌خوبی آزمایش شده است.
- **GA**: همیشه به‌طور پیش‌فرض فعال است؛ گاهی می‌توان آن را تا یک نسخه پس از رسیدن به GA غیرفعال کرد.

## تشخیص مؤلفه‌هایی که به feature gate نیاز دارند

هر feature gate بر مؤلفه‌های متفاوتی از کوبرنتیز اثر می‌گذارد:

- برخی قابلیت‌ها نیاز دارند که gate روی **چند مؤلفه** فعال شود (برای مثال، API server و controller manager)
- برخی دیگر فقط به فعال شدن gate روی **یک مؤلفه** نیاز دارند (برای مثال، فقط kubelet)

[مرجع Feature Gateها](/docs/reference/command-line-tools-reference/feature-gates/) معمولاً مشخص می‌کند که هر gate بر کدام مؤلفه‌ها اثر می‌گذارد. همهٔ مؤلفه‌های کوبرنتیز تعریف‌های یکسانی از feature gateها دارند؛ از این رو همهٔ gateها در خروجی راهنما (help) نمایش داده می‌شوند، اما فقط gateهای مرتبط بر رفتار هر مؤلفه اثر می‌گذارند.

## پیکربندی

### هنگام راه‌اندازی اولیهٔ کلاستر

یک فایل پیکربندی بسازید تا feature gateها را در مؤلفه‌های مرتبط فعال کنید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
apiServer:
  extraArgs:
    feature-gates: "FeatureName=true"
controllerManager:
  extraArgs:
    feature-gates: "FeatureName=true"
scheduler:
  extraArgs:
    feature-gates: "FeatureName=true"
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  FeatureName: true
```

کلاستر را راه‌اندازی کنید:

```shell
kubeadm init --config kubeadm-config.yaml
```

### روی یک کلاستر موجود

در کلاسترهای kubeadm، پیکربندی feature gateها را می‌توان در چند محل تنظیم کرد؛ از جمله فایل‌های مانیفست، فایل‌های پیکربندی و پیکربندی kubeadm.

مانیفست‌های مؤلفه‌های control plane را در مسیر `/etc/kubernetes/manifests/` ویرایش کنید:

1. برای kube-apiserver، kube-controller-manager یا kube-scheduler، فلگ را به فرمان (command) اضافه کنید:

   ```yaml
   spec:
     containers:
     - command:
       - kube-apiserver
       - --feature-gates=FeatureName=true
       # ... other flags
   ```

   فایل را ذخیره کنید. پاد به‌طور خودکار دوباره راه‌اندازی می‌شود.

2. برای kubelet، فایل `/var/lib/kubelet/config.yaml` را ویرایش کنید:

   ```yaml
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   featureGates:
     FeatureName: true
   ```

   سپس kubelet را دوباره راه‌اندازی کنید:

   ```shell
   sudo systemctl restart kubelet
   ```

3. برای kube-proxy، ConfigMap مربوط را ویرایش کنید:

   ```shell
   kubectl -n kube-system edit configmap kube-proxy
   ```

   feature gateها را به پیکربندی اضافه کنید:

   ```yaml
   featureGates:
     FeatureName: true
   ```

   سپس DaemonSet را دوباره راه‌اندازی کنید:

   ```shell
   kubectl -n kube-system rollout restart daemonset kube-proxy
   ```

## پیکربندی چند feature gate

برای فلگ‌های خط فرمان، از فهرستی که با کاما جدا شده است استفاده کنید:

```shell
--feature-gates=FeatureA=true,FeatureB=false,FeatureC=true
```

برای مؤلفه‌هایی که از فایل پیکربندی پشتیبانی می‌کنند (kubelet و kube-proxy):

```yaml
featureGates:
  FeatureA: true
  FeatureB: false
  FeatureC: true
```

{{< note >}}
در کلاسترهای kubeadm، مؤلفه‌های control plane (یعنی kube-apiserver، kube-controller-manager و kube-scheduler) معمولاً از طریق فلگ‌های خط فرمان در مانیفست‌های پاد ایستای (static pod) خود پیکربندی می‌شوند که در مسیر `/etc/kubernetes/manifests/` قرار دارند. با اینکه این مؤلفه‌ها از طریق فلگ `--config` از فایل‌های پیکربندی نیز پشتیبانی می‌کنند، kubeadm عمدتاً از فلگ‌های خط فرمان استفاده می‌کند.
{{< /note >}}


<!-- discussion -->

## بررسی پیکربندی feature gateها

پس از پیکربندی، بررسی کنید که feature gateها فعال شده باشند. روش‌های زیر برای کلاسترهای kubeadm کاربرد دارند که در آن‌ها مؤلفه‌های control plane به‌صورت پاد ایستا اجرا می‌شوند.

### بررسی مانیفست‌های مؤلفه‌های control plane

feature gateهای پیکربندی‌شده در مانیفست پاد ایستا را مشاهده کنید:
```shell
kubectl -n kube-system get pod kube-apiserver-<node-name> -o yaml | grep feature-gates
```

### بررسی پیکربندی kubelet

از endpoint مربوط به configz در kubelet استفاده کنید:
```shell
kubectl proxy --port=8001 &
curl -sSL "http://localhost:8001/api/v1/nodes/<node-name>/proxy/configz" | grep featureGates -A 5
```

یا فایل پیکربندی را مستقیماً روی نود بررسی کنید:
```shell
cat /var/lib/kubelet/config.yaml | grep -A 10 featureGates
```

### بررسی از طریق endpoint متریک‌ها

مؤلفه‌های کوبرنتیز وضعیت feature gateها را در قالب متریک‌هایی به سبک Prometheus در اختیار می‌گذارند (در دسترس از کوبرنتیز 1.26 به بعد). برای بررسی اینکه کدام feature gateها فعال هستند، endpoint متریک‌ها را پرس‌وجو کنید:
```shell
kubectl get --raw /metrics | grep kubernetes_feature_enabled
```

برای بررسی یک feature gate مشخص:
```shell
kubectl get --raw /metrics | grep kubernetes_feature_enabled | grep FeatureName
```

مقدار این متریک برای gateهای فعال `1` و برای gateهای غیرفعال `0` است.

{{< note >}}
در کلاسترهای kubeadm، همهٔ محل‌های مرتبطی را که ممکن است feature gateها در آن‌ها پیکربندی شده باشند بررسی کنید، زیرا پیکربندی در چندین فایل و محل پخش شده است.
{{< /note >}}

### بررسی از طریق endpoint با مسیر ‎/flagz

اگر به endpointهای اشکال‌زدایی یک مؤلفه دسترسی دارید و feature gate با نام `ComponentFlagz` برای آن مؤلفه فعال است، می‌توانید با مراجعه به endpoint با مسیر `/flagz`، فلگ‌های خط فرمانی را که مؤلفه با آن‌ها اجرا شده است بررسی کنید. feature gateهایی که با فلگ‌های خط فرمان پیکربندی شده‌اند در این خروجی نمایش داده می‌شوند.

مسیر `/flagz` بخشی از *z-pages* کوبرنتیز است که اطلاعات اشکال‌زدایی زمان اجرا را به شکلی خوانا برای انسان، برای مؤلفه‌های اصلی فراهم می‌کند.

برای اطلاعات بیشتر، به
[مستندات z-pages](/docs/reference/instrumentation/zpages/) مراجعه کنید.

## آشنایی با نیازمندی‌های خاص هر مؤلفه

چند نمونه از feature gateهای مختص مؤلفه‌ها:

- **متمرکز بر API server**: قابلیت‌هایی مانند `StructuredAuthenticationConfiguration` عمدتاً بر kube-apiserver اثر می‌گذارند
- **متمرکز بر kubelet**: قابلیت‌هایی مانند `GracefulNodeShutdown` عمدتاً بر kubelet اثر می‌گذارند
- **چند مؤلفه**: برخی قابلیت‌ها به هماهنگی میان مؤلفه‌ها نیاز دارند

{{< caution >}}
هنگامی که یک قابلیت به چند مؤلفه نیاز دارد، باید gate را روی همهٔ مؤلفه‌های مرتبط فعال کنید. فعال کردن آن تنها روی برخی از مؤلفه‌ها ممکن است به رفتار غیرمنتظره یا خطا منجر شود.
{{< /caution >}}

همیشه feature gateها را ابتدا در محیط‌های غیرعملیاتی آزمایش کنید. قابلیت‌های آلفا ممکن است بدون اطلاع قبلی حذف شوند.

## {{% heading "whatsnext" %}}

* [مرجع Feature Gateها](/docs/reference/command-line-tools-reference/feature-gates/) را بخوانید
* دربارهٔ [مراحل قابلیت‌ها](/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) بیاموزید
* [پیکربندی kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4/) را مرور کنید

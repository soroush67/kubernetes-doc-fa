---
reviewers:
- sig-cluster-lifecycle
title: پیکربندی مجدد یک کلاستر kubeadm
content_type: task
weight: 90
---

<!-- overview -->

ابزار kubeadm از روش‌های خودکار برای پیکربندی مجدد مؤلفه‌هایی که روی نودهای مدیریت‌شده مستقر شده‌اند پشتیبانی نمی‌کند. یکی از راه‌های خودکارسازی این کار، استفاده از یک [اپراتور](/docs/concepts/extend-kubernetes/operator/) سفارشی است.

برای تغییر پیکربندی مؤلفه‌ها باید آبجکت‌های کلاستر و فایل‌های مرتبط روی دیسک را به‌صورت دستی ویرایش کنید.

این راهنما ترتیب درست گام‌هایی را نشان می‌دهد که برای پیکربندی مجدد یک کلاستر kubeadm باید انجام شوند.

## {{% heading "prerequisites" %}}

- به کلاستری نیاز دارید که با kubeadm مستقر شده باشد.
- اعتبارنامه‌های مدیر (`/etc/kubernetes/admin.conf`) و اتصال شبکه به یک kube-apiserver در حال اجرا در کلاستر را، از میزبانی که kubectl روی آن نصب شده است، در اختیار داشته باشید.
- یک ویرایشگر متن روی همهٔ میزبان‌ها نصب شده باشد.

<!-- steps -->

## پیکربندی مجدد کلاستر

ابزار kubeadm مجموعه‌ای از گزینه‌های پیکربندی مؤلفه‌ها را در سطح کل کلاستر، در ConfigMapها و آبجکت‌های دیگر می‌نویسد. این آبجکت‌ها باید به‌صورت دستی ویرایش شوند. برای این کار می‌توان از فرمان `kubectl edit` استفاده کرد.

فرمان `kubectl edit` یک ویرایشگر متن باز می‌کند که در آن می‌توانید آبجکت را مستقیماً ویرایش و ذخیره کنید.

با متغیرهای محیطی `KUBECONFIG` و `KUBE_EDITOR` می‌توانید مکان فایل kubeconfig مورد استفادهٔ kubectl و ویرایشگر متن دلخواه خود را مشخص کنید.

برای مثال:
```
KUBECONFIG=/etc/kubernetes/admin.conf KUBE_EDITOR=nano kubectl edit <parameters>
```

{{< note >}}
پس از ذخیرهٔ هر تغییری در این آبجکت‌های کلاستر، ممکن است مؤلفه‌هایی که روی نودها اجرا می‌شوند به‌طور خودکار به‌روزرسانی نشوند. گام‌های زیر نشان می‌دهند که این کار را چگونه به‌صورت دستی انجام دهید.
{{< /note >}}

{{< warning >}}
پیکربندی مؤلفه‌ها در ConfigMapها به‌صورت داده‌های بدون ساختار (رشتهٔ YAML) ذخیره می‌شود. یعنی هنگام به‌روزرسانی محتوای یک ConfigMap هیچ اعتبارسنجی‌ای انجام نمی‌شود. باید مراقب باشید که از قالب مستندشدهٔ API برای پیکربندی هر مؤلفه پیروی کنید و از اشتباه‌های تایپی و خطا در تورفتگی YAML پرهیز کنید.
{{< /warning >}}

### اعمال تغییرات پیکربندی کلاستر

#### به‌روزرسانی `ClusterConfiguration`

هنگام ایجاد و ارتقای کلاستر، kubeadm پیکربندی
[`ClusterConfiguration`](/docs/reference/config-api/kubeadm-config.v1beta4/)
خود را در ConfigMapی به نام `kubeadm-config` در فضای نام (namespace) `kube-system` می‌نویسد.

برای تغییر یک گزینهٔ خاص در `ClusterConfiguration`، می‌توانید ConfigMap را با این فرمان ویرایش کنید:

```shell
kubectl edit cm -n kube-system kubeadm-config
```

این پیکربندی زیر کلید `data.ClusterConfiguration` قرار دارد.

{{< note >}}
پیکربندی `ClusterConfiguration` گزینه‌های گوناگونی دارد که بر پیکربندی تک‌تک مؤلفه‌ها، مانند kube-apiserver، kube-scheduler، kube-controller-manager، CoreDNS، etcd و kube-proxy اثر می‌گذارند. تغییرات این پیکربندی باید به‌صورت دستی روی مؤلفه‌های نود اعمال شوند.
{{< /note >}}

#### اعمال تغییرات `ClusterConfiguration` روی نودهای control plane

ابزار kubeadm مؤلفه‌های control plane را به‌صورت مانیفست‌های Pod ایستا (static Pod) در دایرکتوری `/etc/kubernetes/manifests` مدیریت می‌کند. هر تغییری که در `ClusterConfiguration` زیر کلیدهای `apiServer`، `controllerManager`، `scheduler` یا `etcd` انجام شود، باید در فایل‌های مرتبط در دایرکتوری مانیفست‌ها روی نود control plane نیز اعمال شود.

این تغییرات ممکن است شامل موارد زیر باشند:
- فیلد `extraArgs`: نیازمند به‌روزرسانی فهرست فلگ‌هایی است که به کانتینر مؤلفه داده می‌شوند.
- فیلد `extraVolumes`: نیازمند به‌روزرسانی اتصال‌های حجم (volume mount) برای کانتینر مؤلفه است.
- فیلدهای `*SANs`: نیازمند نوشتن گواهی‌های جدید با نام‌های جایگزین موضوع (Subject Alternative Names) به‌روزشده است.

پیش از اعمال این تغییرات، مطمئن شوید که از دایرکتوری `/etc/kubernetes/` نسخهٔ پشتیبان تهیه کرده‌اید.

برای نوشتن گواهی‌های جدید می‌توانید از این فرمان استفاده کنید:
```shell
kubeadm init phase certs <component-name> --config <config-file>
```

برای نوشتن فایل‌های مانیفست جدید در `/etc/kubernetes/manifests` می‌توانید از این فرمان‌ها استفاده کنید:

```shell
# For Kubernetes control plane components
kubeadm init phase control-plane <component-name> --config <config-file>
# For local etcd
kubeadm init phase etcd local --config <config-file>
```

محتوای `<config-file>` باید با `ClusterConfiguration` به‌روزشده مطابقت داشته باشد. مقدار `<component-name>` نیز باید نام یکی از مؤلفه‌های control plane کوبرنتیز (`apiserver`، `controller-manager` یا `scheduler`) باشد.

{{< note >}}
به‌روزرسانی یک فایل در `/etc/kubernetes/manifests` به kubelet اعلام می‌کند که Pod ایستای مؤلفهٔ مربوط را دوباره راه‌اندازی کند. سعی کنید این تغییرات را هر بار فقط روی یک نود انجام دهید تا کلاستر بدون وقفه در دسترس بماند.
{{< /note >}}

### اعمال تغییرات پیکربندی kubelet

#### به‌روزرسانی `KubeletConfiguration`

هنگام ایجاد و ارتقای کلاستر، kubeadm پیکربندی
[`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/)
خود را در ConfigMapی به نام `kubelet-config` در فضای نام `kube-system` می‌نویسد.

می‌توانید این ConfigMap را با فرمان زیر ویرایش کنید:

```shell
kubectl edit cm -n kube-system kubelet-config
```

این پیکربندی زیر کلید `data.kubelet` قرار دارد.

#### اعمال تغییرات kubelet

برای اعمال تغییر روی نودهای kubeadm باید کارهای زیر را انجام دهید:
- وارد یکی از نودهای kubeadm شوید.
- فرمان `kubeadm upgrade node phase kubelet-config` را اجرا کنید تا آخرین محتوای ConfigMap `kubelet-config` در فایل محلی `/var/lib/kubelet/config.yaml` دانلود شود.
- فایل `/var/lib/kubelet/kubeadm-flags.env` را ویرایش کنید تا پیکربندی‌های تکمیلی را با فلگ‌ها اعمال کنید.
- سرویس kubelet را با فرمان `systemctl restart kubelet` دوباره راه‌اندازی کنید.

{{< note >}}
این تغییرات را هر بار فقط روی یک نود انجام دهید تا بارهای کاری بتوانند به‌درستی دوباره زمان‌بندی شوند.
{{< /note >}}

{{< note >}}
هنگام اجرای `kubeadm upgrade`، ابزار kubeadm پیکربندی `KubeletConfiguration` را از ConfigMap `kubelet-config` دانلود می‌کند و محتوای `/var/lib/kubelet/config.yaml` را بازنویسی می‌کند. بنابراین پیکربندی محلی هر نود باید یا با فلگ‌هایی در `/var/lib/kubelet/kubeadm-flags.env` اعمال شود، یا با به‌روزرسانی دستی محتوای `/var/lib/kubelet/config.yaml` پس از `kubeadm upgrade` و سپس راه‌اندازی دوبارهٔ kubelet.
{{< /note >}}

### اعمال تغییرات پیکربندی kube-proxy

#### به‌روزرسانی `KubeProxyConfiguration`

هنگام ایجاد و ارتقای کلاستر، kubeadm پیکربندی
[`KubeProxyConfiguration`](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
خود را در ConfigMapی به نام `kube-proxy` در فضای نام `kube-system` می‌نویسد.

این ConfigMap را DaemonSet `kube-proxy` در فضای نام `kube-system` استفاده می‌کند.

برای تغییر یک گزینهٔ خاص در `KubeProxyConfiguration`، می‌توانید ConfigMap را با این فرمان ویرایش کنید:

```shell
kubectl edit cm -n kube-system kube-proxy
```

این پیکربندی زیر کلید `data.config.conf` قرار دارد.

#### اعمال تغییرات kube-proxy

پس از به‌روزرسانی ConfigMap `kube-proxy`، می‌توانید همهٔ Podهای kube-proxy را دوباره راه‌اندازی کنید.

برای این کار، Podها را با فرمان زیر حذف کنید:

```shell
kubectl delete po -n kube-system -l k8s-app=kube-proxy
```

پس از آن، Podهای جدیدی ایجاد می‌شوند که از ConfigMap به‌روزشده استفاده می‌کنند.

{{< note >}}
از آنجا که kubeadm مؤلفهٔ kube-proxy را به‌صورت یک DaemonSet مستقر می‌کند، پیکربندی مختص هر نود پشتیبانی نمی‌شود.
{{< /note >}}

### اعمال تغییرات پیکربندی CoreDNS

#### به‌روزرسانی Deployment و Service مربوط به CoreDNS

ابزار kubeadm افزونهٔ CoreDNS را به‌صورت یک Deployment به نام `coredns` و همراه با یک Service به نام `kube-dns` مستقر می‌کند که هر دو در فضای نام `kube-system` قرار دارند.

برای به‌روزرسانی هر یک از تنظیمات CoreDNS، می‌توانید آبجکت‌های Deployment و Service را ویرایش کنید:

```shell
kubectl edit deployment -n kube-system coredns
kubectl edit service -n kube-system kube-dns
```

#### اعمال تغییرات CoreDNS

پس از اعمال تغییرات CoreDNS، می‌توانید Deployment مربوط به CoreDNS را دوباره راه‌اندازی کنید:

```shell
kubectl rollout restart deployment -n kube-system coredns
```

{{< note >}}
ابزار kubeadm اجازهٔ پیکربندی CoreDNS را هنگام ایجاد و ارتقای کلاستر نمی‌دهد. بنابراین اگر `kubeadm upgrade apply` را اجرا کنید، تغییراتی که در آبجکت‌های CoreDNS داده‌اید از بین می‌روند و باید دوباره اعمال شوند.
{{< /note >}}

## ماندگار کردن پیکربندی مجدد

هنگام اجرای `kubeadm upgrade` روی یک نود مدیریت‌شده، ممکن است kubeadm پیکربندی‌ای را که پس از ایجاد کلاستر اعمال شده است (پیکربندی مجدد) بازنویسی کند.

### ماندگار کردن پیکربندی مجدد آبجکت Node

ابزار kubeadm برچسب‌ها، taintها، سوکت CRI و اطلاعات دیگری را روی آبجکت Node مربوط به هر نود کوبرنتیز می‌نویسد. برای تغییر هر بخشی از محتوای این آبجکت Node می‌توانید از این فرمان استفاده کنید:

```shell
kubectl edit no <node-name>
```

هنگام اجرای `kubeadm upgrade` ممکن است محتوای چنین Nodeی بازنویسی شود. اگر می‌خواهید تغییراتتان در آبجکت Node پس از ارتقا حفظ شود، می‌توانید یک [وصله (patch) برای kubectl](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/) آماده کنید و آن را روی آبجکت Node اعمال کنید:

```shell
kubectl patch no <node-name> --patch-file <patch-file>
```

#### ماندگار کردن پیکربندی مجدد مؤلفه‌های control plane

منبع اصلی پیکربندی control plane، آبجکت `ClusterConfiguration` ذخیره‌شده در کلاستر است. برای گسترش پیکربندی مانیفست‌های Pod ایستا می‌توان از [وصله‌ها](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/#patches) استفاده کرد.

این فایل‌های وصله باید به‌صورت فایل روی نودهای control plane باقی بمانند تا فرمان `kubeadm upgrade ... --patches <directory>` بتواند از آن‌ها استفاده کند.

اگر پیکربندی مجدد روی `ClusterConfiguration` و مانیفست‌های Pod ایستا روی دیسک انجام شود، مجموعهٔ وصله‌های مختص هر نود نیز باید متناسب با آن به‌روزرسانی شود.

#### ماندگار کردن پیکربندی مجدد kubelet

هر تغییری در `KubeletConfiguration` ذخیره‌شده در `/var/lib/kubelet/config.yaml`، هنگام اجرای `kubeadm upgrade` با دانلود محتوای ConfigMap سراسری `kubelet-config` بازنویسی می‌شود. برای ماندگار کردن پیکربندی مختص هر نود در kubelet، یا باید فایل `/var/lib/kubelet/config.yaml` را پس از ارتقا به‌صورت دستی به‌روزرسانی کرد، یا می‌توان فلگ‌ها را در فایل `/var/lib/kubelet/kubeadm-flags.env` قرار داد. فلگ‌های kubelet گزینه‌های متناظر در `KubeletConfiguration` را بازنویسی (override) می‌کنند، اما توجه داشته باشید که برخی از این فلگ‌ها منسوخ (deprecated) شده‌اند.

پس از تغییر `/var/lib/kubelet/config.yaml` یا `/var/lib/kubelet/kubeadm-flags.env`، باید kubelet را دوباره راه‌اندازی کنید.

## {{% heading "whatsnext" %}}

- [ارتقای کلاسترهای kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade)
- [سفارشی‌سازی مؤلفه‌ها با API ابزار kubeadm](/docs/setup/production-environment/tools/kubeadm/control-plane-flags)
- [مدیریت گواهی‌ها با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs)
- [اطلاعات بیشتر دربارهٔ راه‌اندازی با kubeadm](/docs/reference/setup-tools/kubeadm/)

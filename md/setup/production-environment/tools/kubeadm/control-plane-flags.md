---
reviewers:
- sig-cluster-lifecycle
title: سفارشی‌سازی مؤلفه‌ها با API ‏kubeadm
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه مؤلفه‌هایی را که kubeadm مستقر می‌کند سفارشی کنید. برای مؤلفه‌های
control plane می‌توانید از فلگ‌های ساختار `ClusterConfiguration` یا از وصله‌های (patch) مختص هر نود استفاده کنید.
برای kubelet و kube-proxy نیز به‌ترتیب می‌توانید از `KubeletConfiguration` و `KubeProxyConfiguration` استفاده کنید.

همهٔ این گزینه‌ها از طریق API پیکربندی kubeadm در دسترس هستند.
برای آشنایی بیشتر با هر یک از فیلدهای پیکربندی، می‌توانید به
[صفحه‌های مرجع API](/docs/reference/config-api/kubeadm-config.v1beta4/) مراجعه کنید.

{{< note >}}
برای پیکربندی دوبارهٔ کلاستری که پیش‌تر ایجاد شده است، به
[پیکربندی دوبارهٔ یک کلاستر kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure) مراجعه کنید.
{{< /note >}}

<!-- body -->

## سفارشی‌سازی control plane با فلگ‌های `ClusterConfiguration`

آبجکت `ClusterConfiguration` در kubeadm راهی در اختیار کاربران می‌گذارد تا فلگ‌های پیش‌فرضی را که
به مؤلفه‌های control plane مانند APIServer، ‏ControllerManager، ‏Scheduler و Etcd داده می‌شوند بازنویسی کنند.
این مؤلفه‌ها با ساختارهای زیر تعریف می‌شوند:

- `apiServer`
- `controllerManager`
- `scheduler`
- `etcd`

این ساختارها فیلد مشترکی به نام `extraArgs` دارند که از جفت‌های `name` / `value` تشکیل شده است.
برای بازنویسی یک فلگ در یکی از مؤلفه‌های control plane:

1.  فیلد `extraArgs` مناسب را به پیکربندی خود اضافه کنید.
2.  فلگ‌ها را به فیلد `extraArgs` اضافه کنید.
3.  دستور `kubeadm init` را با `--config <YOUR CONFIG YAML>` اجرا کنید.

{{< note >}}
می‌توانید با اجرای `kubeadm config print init-defaults` و ذخیرهٔ خروجی آن در فایلی دلخواه،
یک آبجکت `ClusterConfiguration` با مقادیر پیش‌فرض بسازید.
{{< /note >}}

{{< note >}}
آبجکت `ClusterConfiguration` در حال حاضر در کلاسترهای kubeadm سراسری است. یعنی هر فلگی که اضافه کنید
روی همهٔ نمونه‌های یک مؤلفه در نودهای مختلف اعمال می‌شود. برای اعمال پیکربندی جداگانه برای هر مؤلفه
در نودهای مختلف، می‌توانید از [وصله‌ها](#patches) استفاده کنید.
{{< /note >}}

{{< note >}}
فلگ‌های (کلیدهای) تکراری، یا دادن یک فلگ مانند `--foo` به‌دفعات، در حال حاضر پشتیبانی نمی‌شود.
برای دور زدن این محدودیت باید از [وصله‌ها](#patches) استفاده کنید.
{{< /note >}}

### فلگ‌های APIServer

برای جزئیات بیشتر، [مستندات مرجع kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/) را ببینید.

نمونهٔ استفاده:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
apiServer:
  extraArgs:
  - name: "enable-admission-plugins"
    value: "AlwaysPullImages,DefaultStorageClass"
  - name: "audit-log-path"
    value: "/home/johndoe/audit.log"
```

### فلگ‌های ControllerManager

برای جزئیات بیشتر، [مستندات مرجع kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) را ببینید.

نمونهٔ استفاده:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
controllerManager:
  extraArgs:
  - name: "cluster-signing-key-file"
    value: "/home/johndoe/keys/ca.key"
  - name: "deployment-controller-sync-period"
    value: "50"
```

### فلگ‌های Scheduler

برای جزئیات بیشتر، [مستندات مرجع kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/) را ببینید.

نمونهٔ استفاده:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
scheduler:
  extraArgs:
  - name: "config"
    value: "/etc/kubernetes/scheduler-config.yaml"
  extraVolumes:
    - name: schedulerconfig
      hostPath: /home/johndoe/schedconfig.yaml
      mountPath: /etc/kubernetes/scheduler-config.yaml
      readOnly: true
      pathType: "File"
```

### فلگ‌های Etcd

برای جزئیات بیشتر، [مستندات سرور etcd](https://etcd.io/docs/) را ببینید.

نمونهٔ استفاده:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
etcd:
  local:
    extraArgs:
    - name: "election-timeout"
      value: 1000
```

## سفارشی‌سازی با وصله‌ها {#patches}

{{< feature-state for_k8s_version="v1.22" state="beta" >}}

ابزار kubeadm به شما امکان می‌دهد پوشه‌ای حاوی فایل‌های وصله را در نودهای جداگانه به `InitConfiguration`،
`JoinConfiguration` و `UpgradeConfiguration` بدهید.
این وصله‌ها را می‌توان به‌عنوان آخرین گام سفارشی‌سازی، پیش از نوشته شدن پیکربندی مؤلفه‌ها روی دیسک، به کار برد.

می‌توانید این فایل را با `--config <YOUR CONFIG YAML>` به `kubeadm init` بدهید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
patches:
  directory: /home/user/somedir
```

{{< note >}}
برای `kubeadm init` می‌توانید فایلی بدهید که هم `ClusterConfiguration` و هم `InitConfiguration` را
در خود داشته باشد و این دو با `---` از هم جدا شده باشند.
{{< /note >}}

می‌توانید این فایل را با `--config <YOUR CONFIG YAML>` به `kubeadm join` بدهید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
patches:
  directory: /home/user/somedir
```

اگر برای ارتقای نودهای kubeadm از `kubeadm upgrade apply` و `kubeadm upgrade node` استفاده می‌کنید،
باید همان وصله‌ها را دوباره ارائه دهید تا سفارشی‌سازی‌ها پس از ارتقا حفظ شوند.

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: UpgradeConfiguration
apply:
  patches:
    directory: /home/user/somedir
```

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: UpgradeConfiguration
node:
  patches:
    directory: /home/user/somedir
```

نام فایل‌های این پوشه باید به شکل `target[suffix][+patchtype].extension` باشد؛
برای نمونه `kube-apiserver0+merge.yaml` یا فقط `etcd.json`.

- مقدار `target` می‌تواند یکی از `kube-apiserver`، `kube-controller-manager`، `kube-scheduler`، `etcd`،
`kubeletconfiguration` و `corednsdeployment` باشد.
- مقدار `suffix` رشته‌ای اختیاری است که با آن می‌توان ترتیب اعمال وصله‌ها را، بر پایهٔ ترتیب الفبایی-عددی،
تعیین کرد.
- مقدار `patchtype` می‌تواند یکی از `strategic`، `merge` یا `json` باشد و باید با قالب‌های وصله‌ای که
[kubectl پشتیبانی می‌کند](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch) مطابقت داشته باشد.
مقدار پیش‌فرض `patchtype` برابر `strategic` است.
- مقدار `extension` باید `json` یا `yaml` باشد.

## سفارشی‌سازی kubelet {#kubelet}

برای سفارشی‌سازی kubelet می‌توانید یک [`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/)
را در کنار `ClusterConfiguration` یا `InitConfiguration` و جداشده با `---` در همان فایل پیکربندی قرار دهید.
سپس می‌توان این فایل را به `kubeadm init` داد و kubeadm همان `KubeletConfiguration` پایه را
روی همهٔ نودهای کلاستر اعمال می‌کند.

برای اعمال پیکربندی مختص هر نمونه روی `KubeletConfiguration` پایه، می‌توانید از
[هدف وصلهٔ `kubeletconfiguration`](#patches) استفاده کنید.

روش دیگر این است که فلگ‌های kubelet را برای بازنویسی تنظیمات، در فیلد `nodeRegistration.kubeletExtraArgs`
قرار دهید؛ این فیلد هم در `InitConfiguration` و هم در `JoinConfiguration` پشتیبانی می‌شود.
برخی از فلگ‌های kubelet منسوخ شده‌اند؛ بنابراین پیش از استفاده، وضعیت آن‌ها را در
[مستندات مرجع kubelet](/docs/reference/command-line-tools-reference/kubelet) بررسی کنید.

برای جزئیات بیشتر، [پیکربندی هر kubelet در کلاستر با استفاده از kubeadm](/docs/setup/production-environment/tools/kubeadm/kubelet-integration) را ببینید.

## سفارشی‌سازی kube-proxy

برای سفارشی‌سازی kube-proxy می‌توانید یک `KubeProxyConfiguration` را در کنار `ClusterConfiguration` یا
`InitConfiguration` و جداشده با `---` به `kubeadm init` بدهید.

برای جزئیات بیشتر می‌توانید به [صفحه‌های مرجع API](/docs/reference/config-api/kubeadm-config.v1beta4/) مراجعه کنید.

{{< note >}}
ابزار kubeadm، ‏kube-proxy را به‌صورت یک {{< glossary_tooltip text="DaemonSet" term_id="daemonset" >}} مستقر می‌کند؛
بنابراین `KubeProxyConfiguration` روی همهٔ نمونه‌های kube-proxy در کلاستر اعمال می‌شود.
{{< /note >}}

## سفارشی‌سازی CoreDNS

ابزار kubeadm به شما امکان می‌دهد Deployment مربوط به CoreDNS را با وصله‌هایی روی
[هدف وصلهٔ `corednsdeployment`](#patches) سفارشی کنید.

وصله‌کردن دیگر آبجکت‌های API مرتبط با CoreDNS، مانند
{{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} ‏`kube-system/coredns`، در حال حاضر پشتیبانی نمی‌شود.
باید هر یک از این آبجکت‌ها را به‌صورت دستی با kubectl وصله کنید و پس از آن
{{< glossary_tooltip text="Podهای" term_id="pod" >}} CoreDNS را دوباره ایجاد کنید.

روش دیگر این است که با افزودن گزینهٔ زیر به `ClusterConfiguration`، استقرار CoreDNS
توسط kubeadm را غیرفعال کنید:

```yaml
dns:
  disabled: true
```

همچنین با اجرای دستور زیر:

```shell
kubeadm init phase addon coredns --print-manifest --config my-config.yaml`
```

می‌توانید فایل مانیفستی را که kubeadm برای CoreDNS در محیط شما ایجاد می‌کند به دست آورید.

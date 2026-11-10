---
title: پشتیبانی از دو پشته (dual-stack) با kubeadm
content_type: task
weight: 100
min-kubernetes-server-version: 1.21
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

کلاستر کوبرنتیز شما از شبکه‌بندی [دو پشته](/docs/concepts/services-networking/dual-stack/)
پشتیبانی می‌کند؛ یعنی شبکه‌بندی کلاستر به شما امکان می‌دهد از هر یک از دو خانوادهٔ آدرس استفاده کنید.
در یک کلاستر، control plane می‌تواند هم یک آدرس IPv4 و هم یک آدرس IPv6 را به یک
{{< glossary_tooltip text="Pod" term_id="pod" >}} یا یک {{< glossary_tooltip text="Service" term_id="service" >}} اختصاص دهد.

<!-- body -->

## {{% heading "prerequisites" %}}

باید ابزار {{< glossary_tooltip text="kubeadm" term_id="kubeadm" >}} را طبق مراحل
[نصب kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) نصب کرده باشید.

برای هر سروری که می‌خواهید به‌عنوان {{< glossary_tooltip text="نود" term_id="node" >}} از آن استفاده کنید،
مطمئن شوید که ارسال (forwarding) بسته‌های IPv6 در آن مجاز است.

### فعال‌سازی ارسال بسته‌های IPv6 {#prerequisite-ipv6-forwarding}

برای بررسی اینکه ارسال بسته‌های IPv6 فعال است یا نه:

```bash
sysctl net.ipv6.conf.all.forwarding
```
اگر خروجی `net.ipv6.conf.all.forwarding = 1` باشد، این قابلیت از قبل فعال است.
در غیر این صورت هنوز فعال نشده است.

برای فعال‌سازی دستی ارسال بسته‌های IPv6:

```bash
# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee -a /etc/sysctl.d/k8s.conf
net.ipv6.conf.all.forwarding = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```


باید یک محدودهٔ آدرس IPv4 و یک محدودهٔ آدرس IPv6 برای استفاده در اختیار داشته باشید. اپراتورهای کلاستر
معمولاً برای IPv4 از محدوده‌های آدرس خصوصی استفاده می‌کنند. برای IPv6، اپراتور کلاستر معمولاً یک بلوک
آدرس global unicast را از داخل `2000::/3` انتخاب می‌کند و از محدوده‌ای بهره می‌گیرد که به خود او تخصیص داده شده است.
لازم نیست محدوده‌های آدرس IP کلاستر را به اینترنت عمومی مسیریابی کنید.

اندازهٔ تخصیص‌های آدرس IP باید با تعداد Podها و Serviceهایی که قصد اجرای آن‌ها را دارید متناسب باشد.

{{< note >}}
اگر یک کلاستر موجود را با فرمان `kubeadm upgrade` ارتقا می‌دهید، توجه کنید که
`kubeadm` از اعمال تغییر در محدودهٔ آدرس IP پادها («cluster CIDR») و همچنین
محدودهٔ آدرس Serviceهای کلاستر («Service CIDR») پشتیبانی نمی‌کند.
{{< /note >}}

### ایجاد یک کلاستر دو پشته

برای ایجاد یک کلاستر دو پشته با `kubeadm init` می‌توانید آرگومان‌های خط فرمانی
مشابه نمونهٔ زیر را به آن بدهید:

```shell
# These address ranges are examples
kubeadm init --pod-network-cidr=10.244.0.0/16,2001:db8:42:0::/56 --service-cidr=10.96.0.0/16,2001:db8:42:1::/112
```

برای روشن‌تر شدن موضوع، در ادامه نمونه‌ای از
[فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm با نام
`kubeadm-config.yaml` برای نود اصلی control plane دو پشته آمده است.

```yaml
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
networking:
  podSubnet: 10.244.0.0/16,2001:db8:42:0::/56
  serviceSubnet: 10.96.0.0/16,2001:db8:42:1::/112
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: "10.100.0.1"
  bindPort: 6443
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::2"
```

فیلد `advertiseAddress` در InitConfiguration آدرس IPای را مشخص می‌کند که API Server
اعلام می‌کند روی آن گوش می‌دهد. مقدار `advertiseAddress` معادل پرچم
`--apiserver-advertise-address` در `kubeadm init` است.

برای راه‌اندازی نود control plane دو پشته، kubeadm را اجرا کنید:

```shell
kubeadm init --config=kubeadm-config.yaml
```

پرچم‌های `--node-cidr-mask-size-ipv4|--node-cidr-mask-size-ipv6` در kube-controller-manager
با مقادیر پیش‌فرض تنظیم می‌شوند. به [پیکربندی دو پشتهٔ IPv4/IPv6](/docs/concepts/services-networking/dual-stack#configure-ipv4-ipv6-dual-stack) مراجعه کنید.

{{< note >}}
پرچم `--apiserver-advertise-address` از دو پشته پشتیبانی نمی‌کند.
{{< /note >}}

### پیوستن یک نود به کلاستر دو پشته

پیش از پیوستن یک نود، مطمئن شوید که نود یک رابط شبکهٔ قابل مسیریابی IPv6 دارد و ارسال بسته‌های IPv6 در آن مجاز است.

در ادامه نمونه‌ای از [فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm با نام
`kubeadm-config.yaml` برای پیوستن یک نود کارگر به کلاستر آمده است.

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
discovery:
  bootstrapToken:
    apiServerEndpoint: 10.100.0.1:6443
    token: "clvldh.vjjwg16ucnhp94qr"
    caCertHashes:
    - "sha256:a4863cde706cfc580a439f842cc65d5ef112b7b2be31628513a9881cf0d9fe0e"
    # change auth info above to match the actual token and CA certificate hash for your cluster
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::3"
```

همچنین در ادامه نمونه‌ای از [فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm با نام
`kubeadm-config.yaml` برای پیوستن یک نود control plane دیگر به کلاستر آمده است.

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
controlPlane:
  localAPIEndpoint:
    advertiseAddress: "10.100.0.2"
    bindPort: 6443
discovery:
  bootstrapToken:
    apiServerEndpoint: 10.100.0.1:6443
    token: "clvldh.vjjwg16ucnhp94qr"
    caCertHashes:
    - "sha256:a4863cde706cfc580a439f842cc65d5ef112b7b2be31628513a9881cf0d9fe0e"
    # change auth info above to match the actual token and CA certificate hash for your cluster
nodeRegistration:
  kubeletExtraArgs:
  - name: "node-ip"
    value: "10.100.0.2,fd00:1:2:3::4"
```

فیلد `advertiseAddress` در JoinConfiguration.controlPlane آدرس IPای را مشخص می‌کند که
API Server اعلام می‌کند روی آن گوش می‌دهد. مقدار `advertiseAddress` معادل پرچم
`--apiserver-advertise-address` در `kubeadm join` است.

```shell
kubeadm join --config=kubeadm-config.yaml
```

### ایجاد یک کلاستر تک پشته

{{< note >}}
پشتیبانی از دو پشته به این معنا نیست که حتماً باید از آدرس‌دهی دو پشته استفاده کنید.
می‌توانید یک کلاستر تک پشته را مستقر کنید که قابلیت شبکه‌بندی دو پشته در آن فعال باشد.
{{< /note >}}

برای روشن‌تر شدن موضوع، در ادامه نمونه‌ای از
[فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm با نام
`kubeadm-config.yaml` برای نود control plane تک پشته آمده است.

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
networking:
  podSubnet: 10.244.0.0/16
  serviceSubnet: 10.96.0.0/16
```

## {{% heading "whatsnext" %}}

* شبکه‌بندی [دو پشتهٔ IPv4/IPv6 را اعتبارسنجی کنید](/docs/tasks/network/validate-dual-stack)
* دربارهٔ شبکه‌بندی کلاستر [دو پشته](/docs/concepts/services-networking/dual-stack/) بخوانید
* دربارهٔ [قالب پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm بیشتر بیاموزید

---
title: اعمال استانداردهای امنیت Pod در سطح کلاستر
content_type: tutorial
weight: 10
---

{{% alert title="Note" %}}
این آموزش فقط برای کلاسترهای جدید کاربرد دارد.
{{% /alert %}}

قابلیت Pod Security یک کنترل‌کنندهٔ پذیرش (admission controller) است. این کنترل‌کننده هنگام ایجاد Podهای جدید، بررسی‌هایی را بر اساس
[استانداردهای امنیت Pod (Pod Security Standards)](/docs/concepts/security/pod-security-standards/) کوبرنتیز انجام می‌دهد.
این قابلیت در نسخهٔ v1.25 به وضعیت GA رسیده است.
این آموزش نشان می‌دهد که چگونه استاندارد امنیت Pod از نوع `baseline` را در سطح کلاستر اجباری کنید. با این کار، یک پیکربندی استاندارد روی همهٔ فضاهای نام (namespace) کلاستر اعمال می‌شود.

برای اعمال استانداردهای امنیت Pod روی فضاهای نام مشخص، به
[اعمال استانداردهای امنیت Pod در سطح فضای نام](/docs/tutorials/security/ns-level-pss) مراجعه کنید.

اگر نسخه‌ای از کوبرنتیز به‌جز v{{< skew currentVersion >}} را اجرا می‌کنید،
مستندات مربوط به همان نسخه را بررسی کنید.

## {{% heading "prerequisites" %}}

موارد زیر را روی ایستگاه کاری خود نصب کنید:

- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](/docs/tasks/tools/)

این آموزش نشان می‌دهد که در یک کلاستر کوبرنتیز که کنترل کامل آن در اختیار شماست، چه مواردی را می‌توانید پیکربندی کنید. اگر می‌خواهید پیکربندی پذیرش امنیت Pod را برای یک کلاستر مدیریت‌شده یاد بگیرید که در آن امکان پیکربندی control plane را ندارید، آموزش
[اعمال استانداردهای امنیت Pod در سطح فضای نام](/docs/tutorials/security/ns-level-pss) را بخوانید.

## انتخاب استاندارد امنیت Pod مناسب برای اعمال

[پذیرش امنیت Pod (Pod Security Admission)](/docs/concepts/security/pod-security-admission/)
به شما امکان می‌دهد [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/) داخلی را
در حالت‌های `enforce`، `audit` و `warn` اعمال کنید.

برای گردآوری اطلاعاتی که به شما در انتخاب مناسب‌ترین استانداردهای امنیت Pod برای پیکربندی‌تان کمک می‌کند، مراحل زیر را انجام دهید:

1. یک کلاستر بدون اعمال هیچ استاندارد امنیت Pod ایجاد کنید:

   ```shell
   kind create cluster --name psa-wo-cluster-pss
   ```
   خروجی مشابه زیر است:
   ```
   Creating cluster "psa-wo-cluster-pss" ...
   ✓ Ensuring node image (kindest/node:v{{< skew currentPatchVersion >}}) 🖼
   ✓ Preparing nodes 📦
   ✓ Writing configuration 📜
   ✓ Starting control-plane 🕹️
   ✓ Installing CNI 🔌
   ✓ Installing StorageClass 💾
   Set kubectl context to "kind-psa-wo-cluster-pss"
   You can now use your cluster with:

   kubectl cluster-info --context kind-psa-wo-cluster-pss

   Thanks for using kind! 😊
   ```

1. زمینهٔ (context) ابزار kubectl را روی کلاستر جدید تنظیم کنید:

   ```shell
   kubectl cluster-info --context kind-psa-wo-cluster-pss
   ```
   خروجی مشابه زیر است:

   ```
   Kubernetes control plane is running at https://127.0.0.1:61350

   CoreDNS is running at https://127.0.0.1:61350/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

1. فهرست فضاهای نام کلاستر را دریافت کنید:

   ```shell
   kubectl get ns
   ```
   خروجی مشابه زیر است:
   ```
   NAME                 STATUS   AGE
   default              Active   9m30s
   kube-node-lease      Active   9m32s
   kube-public          Active   9m32s
   kube-system          Active   9m32s
   local-path-storage   Active   9m26s
   ```

1. با استفاده از `--dry-run=server` بررسی کنید که با اعمال استانداردهای امنیت Pod مختلف چه اتفاقی می‌افتد:

   1. سطح Privileged
      ```shell
      kubectl label --dry-run=server --overwrite ns --all \
      pod-security.kubernetes.io/enforce=privileged
      ```

      خروجی مشابه زیر است:
      ```
      namespace/default labeled
      namespace/kube-node-lease labeled
      namespace/kube-public labeled
      namespace/kube-system labeled
      namespace/local-path-storage labeled
      ```
   2. سطح Baseline
      ```shell
      kubectl label --dry-run=server --overwrite ns --all \
      pod-security.kubernetes.io/enforce=baseline
      ```

      خروجی مشابه زیر است:
      ```
      namespace/default labeled
      namespace/kube-node-lease labeled
      namespace/kube-public labeled
      Warning: existing pods in namespace "kube-system" violate the new PodSecurity enforce level "baseline:latest"
      Warning: etcd-psa-wo-cluster-pss-control-plane (and 3 other pods): host namespaces, hostPath volumes
      Warning: kindnet-vzj42: non-default capabilities, host namespaces, hostPath volumes
      Warning: kube-proxy-m6hwf: host namespaces, hostPath volumes, privileged
      namespace/kube-system labeled
      namespace/local-path-storage labeled
      ```

   3. سطح Restricted
      ```shell
      kubectl label --dry-run=server --overwrite ns --all \
      pod-security.kubernetes.io/enforce=restricted
      ```

      خروجی مشابه زیر است:
      ```
      namespace/default labeled
      namespace/kube-node-lease labeled
      namespace/kube-public labeled
      Warning: existing pods in namespace "kube-system" violate the new PodSecurity enforce level "restricted:latest"
      Warning: coredns-7bb9c7b568-hsptc (and 1 other pod): unrestricted capabilities, runAsNonRoot != true, seccompProfile
      Warning: etcd-psa-wo-cluster-pss-control-plane (and 3 other pods): host namespaces, hostPath volumes, allowPrivilegeEscalation != false, unrestricted capabilities, restricted volume types, runAsNonRoot != true
      Warning: kindnet-vzj42: non-default capabilities, host namespaces, hostPath volumes, allowPrivilegeEscalation != false, unrestricted capabilities, restricted volume types, runAsNonRoot != true, seccompProfile
      Warning: kube-proxy-m6hwf: host namespaces, hostPath volumes, privileged, allowPrivilegeEscalation != false, unrestricted capabilities, restricted volume types, runAsNonRoot != true, seccompProfile
      namespace/kube-system labeled
      Warning: existing pods in namespace "local-path-storage" violate the new PodSecurity enforce level "restricted:latest"
      Warning: local-path-provisioner-d6d9f7ffc-lw9lh: allowPrivilegeEscalation != false, unrestricted capabilities, runAsNonRoot != true, seccompProfile
      namespace/local-path-storage labeled
      ```

در خروجی بالا مشاهده می‌کنید که اعمال استاندارد امنیت Pod از نوع `privileged` برای هیچ فضای نامی هشداری نشان نمی‌دهد. اما استانداردهای `baseline` و `restricted` هر دو هشدارهایی دارند که به‌طور مشخص مربوط به فضای نام `kube-system` هستند.

## تنظیم حالت‌ها، نسخه‌ها و استانداردها

در این بخش، استانداردهای امنیت Pod زیر را با نسخهٔ `latest` اعمال می‌کنید:

* استاندارد `baseline` در حالت `enforce`.
* استاندارد `restricted` در حالت‌های `warn` و `audit`.

استاندارد امنیت Pod از نوع `baseline` حد وسط مناسبی فراهم می‌کند؛ این استاندارد امکان کوتاه نگه‌داشتن فهرست استثناها را می‌دهد و از ارتقای سطح دسترسی (privilege escalation) از راه‌های شناخته‌شده جلوگیری می‌کند.

افزون بر این، برای جلوگیری از شکست Podها در `kube-system`، این فضای نام را از اعمال استانداردهای امنیت Pod مستثنا می‌کنید.

هنگام پیاده‌سازی پذیرش امنیت Pod در محیط خودتان، به نکات زیر توجه کنید:

1. بسته به سطح ریسکی که برای کلاستر در نظر گرفته‌اید، ممکن است استاندارد امنیت Pod سخت‌گیرانه‌تری مانند `restricted` انتخاب بهتری باشد.
1. مستثنا کردن فضای نام `kube-system` باعث می‌شود Podها بتوانند در این فضای نام با سطح `privileged` اجرا شوند. پروژهٔ کوبرنتیز برای استفاده در محیط واقعی اکیداً توصیه می‌کند که بر اساس اصل حداقل دسترسی، سیاست‌های RBAC سخت‌گیرانه‌ای اعمال کنید که دسترسی به `kube-system` را محدود کنند.
   برای پیاده‌سازی استانداردهای بالا، مراحل زیر را انجام دهید:
1. یک فایل پیکربندی ایجاد کنید که کنترل‌کنندهٔ پذیرش امنیت Pod بتواند از آن برای پیاده‌سازی این استانداردهای امنیت Pod استفاده کند:

   ```
   mkdir -p /tmp/pss
   cat <<EOF > /tmp/pss/cluster-level-pss.yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: AdmissionConfiguration
   plugins:
   - name: PodSecurity
     configuration:
       apiVersion: pod-security.admission.config.k8s.io/v1
       kind: PodSecurityConfiguration
       defaults:
         enforce: "baseline"
         enforce-version: "latest"
         audit: "restricted"
         audit-version: "latest"
         warn: "restricted"
         warn-version: "latest"
       exemptions:
         usernames: []
         runtimeClasses: []
         namespaces: [kube-system]
   EOF
   ```

   {{< alert color="info" title="Note" >}}
   پیکربندی `pod-security.admission.config.k8s.io/v1` به نسخهٔ v1.25 یا بالاتر نیاز دارد.
   برای نسخه‌های v1.23 و v1.24 از [v1beta1](https://v1-24.docs.kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/) استفاده کنید.
   برای نسخهٔ v1.22 از [v1alpha1](https://v1-22.docs.kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/) استفاده کنید.
   {{< /alert >}}


1. سرور API را طوری پیکربندی کنید که هنگام ایجاد کلاستر از این فایل استفاده کند:

   ```
   cat <<EOF > /tmp/pss/cluster-config.yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
   - role: control-plane
     kubeadmConfigPatches:
     - |
       kind: ClusterConfiguration
       apiServer:
           extraArgs:
             admission-control-config-file: /etc/config/cluster-level-pss.yaml
           extraVolumes:
             - name: accf
               hostPath: /etc/config
               mountPath: /etc/config
               readOnly: false
               pathType: "DirectoryOrCreate"
     extraMounts:
     - hostPath: /tmp/pss
       containerPath: /etc/config
       # optional: if set, the mount is read-only.
       # default false
       readOnly: false
       # optional: if set, the mount needs SELinux relabeling.
       # default false
       selinuxRelabel: false
       # optional: set propagation mode (None, HostToContainer or Bidirectional)
       # see https://kubernetes.io/docs/concepts/storage/volumes/#mount-propagation
       # default None
       propagation: None
   EOF
   ```

   {{< alert color="info" title="Note" >}}
   اگر در macOS از Docker Desktop همراه با *kind* استفاده می‌کنید، می‌توانید
   مسیر `/tmp` را از طریق منوی
   **Preferences > Resources > File Sharing** به‌عنوان یک پوشهٔ اشتراکی (Shared Directory) اضافه کنید.
   {{< /alert >}}

1. کلاستری ایجاد کنید که برای اعمال این استانداردهای امنیت Pod از پذیرش امنیت Pod استفاده کند:

   ```shell
   kind create cluster --name psa-with-cluster-pss --config /tmp/pss/cluster-config.yaml
   ```
   خروجی مشابه زیر است:
   ```
   Creating cluster "psa-with-cluster-pss" ...
    ✓ Ensuring node image (kindest/node:v{{< skew currentPatchVersion >}}) 🖼
    ✓ Preparing nodes 📦
    ✓ Writing configuration 📜
    ✓ Starting control-plane 🕹️
    ✓ Installing CNI 🔌
    ✓ Installing StorageClass 💾
   Set kubectl context to "kind-psa-with-cluster-pss"
   You can now use your cluster with:

   kubectl cluster-info --context kind-psa-with-cluster-pss

   Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
   ```

1. ابزار kubectl را به سمت این کلاستر تنظیم کنید:
   ```shell
   kubectl cluster-info --context kind-psa-with-cluster-pss
   ```
   خروجی مشابه زیر است:
   ```
   Kubernetes control plane is running at https://127.0.0.1:63855
   CoreDNS is running at https://127.0.0.1:63855/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

1. یک Pod در فضای نام پیش‌فرض ایجاد کنید:

    {{% code_sample file="security/example-baseline-pod.yaml" %}}

   ```shell
   kubectl apply -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```

   این Pod به‌طور عادی راه‌اندازی می‌شود، اما خروجی شامل یک هشدار است:
   ```
   Warning: would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
   pod/nginx created
   ```

## پاک‌سازی

اکنون کلاسترهایی را که در مراحل بالا ایجاد کردید، با اجرای دستورهای زیر حذف کنید:

```shell
kind delete cluster --name psa-with-cluster-pss
```
```shell
kind delete cluster --name psa-wo-cluster-pss
```

## {{% heading "whatsnext" %}}

- یک
  [اسکریپت شل](/examples/security/kind-with-cluster-level-baseline-pod-security.sh)
  را اجرا کنید تا همهٔ مراحل بالا یک‌جا انجام شوند:
  1. ایجاد یک پیکربندی در سطح کلاستر بر پایهٔ استانداردهای امنیت Pod
  2. ایجاد فایلی که سرور API بتواند از این پیکربندی استفاده کند
  3. ایجاد کلاستری که سرور API آن با این پیکربندی راه‌اندازی می‌شود
  4. تنظیم زمینهٔ kubectl روی این کلاستر جدید
  5. ایجاد یک فایل yaml حداقلی برای Pod
  6. اعمال این فایل برای ایجاد یک Pod در کلاستر جدید
- [پذیرش امنیت Pod](/docs/concepts/security/pod-security-admission/)
- [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/)
- [اعمال استانداردهای امنیت Pod در سطح فضای نام](/docs/tutorials/security/ns-level-pss/)

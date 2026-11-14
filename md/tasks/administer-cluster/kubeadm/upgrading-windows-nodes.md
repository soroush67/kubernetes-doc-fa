---
title: ارتقای نودهای Windows
min-kubernetes-server-version: 1.17
content_type: task
weight: 41
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.18" state="beta" >}}

این صفحه نحوهٔ ارتقای نود Windowsی را توضیح می‌دهد که با kubeadm ایجاد شده است.

## {{% heading "prerequisites" %}}
 
{{< include "task-tutorial-prereqs-node-upgrade.md" >}} {{< version-check >}}
* با [فرایند ارتقای بقیهٔ کلاستر kubeadm خود](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade)
آشنا شوید. پیش از ارتقای نودهای Windows، باید نودهای control plane را ارتقا دهید.

<!-- steps -->

## ارتقای نودهای کارگر

### ارتقای kubeadm

1.  روی نود Windows، ابزار kubeadm را ارتقا دهید:

    ```powershell
    # replace {{< skew currentPatchVersion >}} with your desired version
    curl.exe -Lo <path-to-kubeadm.exe>  "https://dl.k8s.io/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubeadm.exe"
    ```

### تخلیهٔ نود

1.  از ماشینی که به API کوبرنتیز دسترسی دارد، نود را برای نگهداری آماده کنید؛
    به این صورت که آن را غیرقابل‌زمان‌بندی علامت بزنید و بارهای کاری را از آن بیرون کنید:

    ```shell
    # replace <node-to-drain> with the name of your node you are draining
    kubectl drain <node-to-drain> --ignore-daemonsets
    ```

    باید خروجی‌ای مشابه زیر ببینید:

    ```
    node/ip-172-31-85-18 cordoned
    node/ip-172-31-85-18 drained
    ```

### ارتقای پیکربندی kubelet

1.  روی نود Windows، دستور زیر را اجرا کنید تا پیکربندی جدید kubelet همگام‌سازی شود:

    ```powershell
    kubeadm upgrade node
    ```

### ارتقای kubelet و kube-proxy

1.  روی نود Windows، kubelet را ارتقا دهید و دوباره راه‌اندازی کنید:

    ```powershell
    stop-service kubelet
    curl.exe -Lo <path-to-kubelet.exe> "https://dl.k8s.io/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubelet.exe"
    restart-service kubelet
    ```

2. روی نود Windows، kube-proxy را ارتقا دهید و دوباره راه‌اندازی کنید.

    ```powershell
    stop-service kube-proxy
    curl.exe -Lo <path-to-kube-proxy.exe> "https://dl.k8s.io/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kube-proxy.exe"
    restart-service kube-proxy
    ```

{{< note >}}
اگر kube-proxy را به‌جای سرویس Windows، در یک کانتینر HostProcess درون یک Pod اجرا می‌کنید،
می‌توانید با اعمال نسخهٔ جدیدتری از مانیفست‌های kube-proxy آن را ارتقا دهید.
{{< /note >}}

### خارج کردن نود از حالت cordon

1.  از ماشینی که به API کوبرنتیز دسترسی دارد، نود را قابل‌زمان‌بندی علامت بزنید
تا دوباره به چرخهٔ کار بازگردد:

    ```shell
    # replace <node-to-drain> with the name of your node
    kubectl uncordon <node-to-drain>
    ```
 ## {{% heading "whatsnext" %}}

* ببینید چگونه می‌توانید [نودهای Linux را ارتقا دهید](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/).

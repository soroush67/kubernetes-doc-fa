---
reviewers:
- sig-cluster-lifecycle
title: راه‌اندازی یک کلاستر etcd با دسترس‌پذیری بالا با kubeadm
content_type: task
weight: 70
---

<!-- overview -->


به‌طور پیش‌فرض، kubeadm روی هر نود control plane یک نمونهٔ محلی از etcd اجرا می‌کند.
همچنین می‌توان کلاستر etcd را خارجی در نظر گرفت و نمونه‌های etcd را روی میزبان‌های جداگانه
فراهم کرد. تفاوت‌های این دو رویکرد در صفحهٔ
[گزینه‌های توپولوژی با دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/ha-topology) شرح داده شده است.

این وظیفه شما را گام‌به‌گام در فرایند ایجاد یک کلاستر خارجی etcd با دسترس‌پذیری بالا (high availability)
و سه عضو همراهی می‌کند؛ کلاستری که kubeadm می‌تواند هنگام ایجاد کلاستر از آن استفاده کند.

## {{% heading "prerequisites" %}}

- سه میزبان که بتوانند از طریق درگاه‌های TCP شمارهٔ 2379 و 2380 با یکدیگر ارتباط برقرار کنند. این
  سند همین درگاه‌های پیش‌فرض را فرض می‌کند؛ با این حال، می‌توان آن‌ها را از طریق فایل پیکربندی
  kubeadm تغییر داد.
- روی هر میزبان باید systemd و یک پوستهٔ سازگار با bash نصب شده باشد.
- روی هر میزبان باید [یک محیط اجرای کانتینر، kubelet و kubeadm نصب شده باشد](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/).
- هر میزبان باید به رجیستری ایمیج کانتینر کوبرنتیز (`registry.k8s.io`) دسترسی داشته باشد، یا ایمیج
  etcd موردنیاز را با استفاده از `kubeadm config images list/pull` فهرست و دریافت کند. این راهنما
  نمونه‌های etcd را به‌صورت [پادهای ایستا](/docs/tasks/configure-pod-container/static-pod/) راه‌اندازی می‌کند
  که kubelet آن‌ها را مدیریت می‌کند.
- زیرساختی برای کپی‌کردن فایل‌ها میان میزبان‌ها. برای مثال، `ssh` و `scp`
  می‌توانند این نیاز را برآورده کنند.

<!-- steps -->

## راه‌اندازی کلاستر

رویکرد کلی این است که همهٔ گواهی‌ها روی یک نود تولید شوند و تنها فایل‌های _ضروری_
میان نودهای دیگر توزیع شوند.

{{< note >}}
ابزار kubeadm همهٔ سازوکارهای رمزنگاری لازم برای تولید گواهی‌های شرح‌داده‌شده در ادامه را
در خود دارد؛ برای این مثال به هیچ ابزار رمزنگاری دیگری نیاز نیست.
{{< /note >}}

{{< note >}}
مثال‌های زیر از نشانی‌های IPv4 استفاده می‌کنند، اما می‌توانید kubeadm، kubelet و etcd را نیز طوری
پیکربندی کنید که از نشانی‌های IPv6 استفاده کنند. برخی گزینه‌های کوبرنتیز از پشتهٔ دوگانه (dual-stack)
پشتیبانی می‌کنند، اما etcd از آن پشتیبانی نمی‌کند. برای جزئیات بیشتر دربارهٔ پشتیبانی کوبرنتیز از
پشتهٔ دوگانه، به [پشتیبانی از پشتهٔ دوگانه با kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/) مراجعه کنید.
{{< /note >}}

1. kubelet را طوری پیکربندی کنید که مدیر سرویس etcd باشد.

   {{< note >}}باید این کار را روی هر میزبانی انجام دهید که etcd قرار است روی آن اجرا شود.{{< /note >}}
   از آنجا که etcd ابتدا ایجاد شده است، باید با ایجاد یک فایل unit جدید که اولویت بالاتری از
   فایل unit مربوط به kubelet ارائه‌شده توسط kubeadm دارد، اولویت سرویس را بازنویسی کنید.

   ```sh
   cat << EOF > /etc/systemd/system/kubelet.service.d/kubelet.conf
   # Replace "systemd" with the cgroup driver of your container runtime. The default value in the kubelet is "cgroupfs".
   # Replace the value of "containerRuntimeEndpoint" for a different container runtime if needed.
   #
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   authentication:
     anonymous:
       enabled: false
     webhook:
       enabled: false
   authorization:
     mode: AlwaysAllow
   cgroupDriver: systemd
   address: 127.0.0.1
   containerRuntimeEndpoint: unix:///var/run/containerd/containerd.sock
   staticPodPath: /etc/kubernetes/manifests
   EOF

   cat << EOF > /etc/systemd/system/kubelet.service.d/20-etcd-service-manager.conf
   [Service]
   ExecStart=
   ExecStart=/usr/bin/kubelet --config=/etc/systemd/system/kubelet.service.d/kubelet.conf
   Restart=always
   EOF

   systemctl daemon-reload
   systemctl restart kubelet
   ```

   وضعیت kubelet را بررسی کنید تا مطمئن شوید در حال اجراست.

   ```sh
   systemctl status kubelet
   ```

1. فایل‌های پیکربندی kubeadm را ایجاد کنید.

   با استفاده از اسکریپت زیر، برای هر میزبانی که یک عضو etcd روی آن اجرا خواهد شد،
   یک فایل پیکربندی kubeadm تولید کنید.

   ```sh
   # Update HOST0, HOST1 and HOST2 with the IPs of your hosts
   export HOST0=10.0.0.6
   export HOST1=10.0.0.7
   export HOST2=10.0.0.8

   # Update NAME0, NAME1 and NAME2 with the hostnames of your hosts
   export NAME0="infra0"
   export NAME1="infra1"
   export NAME2="infra2"

   # Create temp directories to store files that will end up on other hosts
   mkdir -p /tmp/${HOST0}/ /tmp/${HOST1}/ /tmp/${HOST2}/

   HOSTS=(${HOST0} ${HOST1} ${HOST2})
   NAMES=(${NAME0} ${NAME1} ${NAME2})

   for i in "${!HOSTS[@]}"; do
   HOST=${HOSTS[$i]}
   NAME=${NAMES[$i]}
   cat << EOF > /tmp/${HOST}/kubeadmcfg.yaml
   ---
   apiVersion: "kubeadm.k8s.io/v1beta4"
   kind: InitConfiguration
   nodeRegistration:
       name: ${NAME}
   localAPIEndpoint:
       advertiseAddress: ${HOST}
   ---
   apiVersion: "kubeadm.k8s.io/v1beta4"
   kind: ClusterConfiguration
   etcd:
       local:
           serverCertSANs:
           - "${HOST}"
           peerCertSANs:
           - "${HOST}"
           extraArgs:
           - name: initial-cluster
             value: ${NAMES[0]}=https://${HOSTS[0]}:2380,${NAMES[1]}=https://${HOSTS[1]}:2380,${NAMES[2]}=https://${HOSTS[2]}:2380
           - name: initial-cluster-state
             value: new
           - name: name
             value: ${NAME}
           - name: listen-peer-urls
             value: https://${HOST}:2380
           - name: listen-client-urls
             value: https://${HOST}:2379
           - name: advertise-client-urls
             value: https://${HOST}:2379
           - name: initial-advertise-peer-urls
             value: https://${HOST}:2380
   EOF
   done
   ```

1. مرجع صدور گواهی (certificate authority) را تولید کنید.

   اگر از قبل یک CA دارید، تنها کاری که باید انجام دهید کپی‌کردن فایل‌های `crt` و `key`
   آن CA به `/etc/kubernetes/pki/etcd/ca.crt` و `/etc/kubernetes/pki/etcd/ca.key` است.
   پس از کپی‌شدن این فایل‌ها، به گام بعدی، یعنی «ایجاد گواهی برای هر عضو»، بروید.

   اگر هنوز CA ندارید، این فرمان را روی `$HOST0` (جایی که فایل‌های پیکربندی kubeadm
   را تولید کردید) اجرا کنید.

   ```
   kubeadm init phase certs etcd-ca
   ```

   این فرمان دو فایل ایجاد می‌کند:

   - `/etc/kubernetes/pki/etcd/ca.crt`
   - `/etc/kubernetes/pki/etcd/ca.key`

1. برای هر عضو گواهی ایجاد کنید.

   ```sh
   kubeadm init phase certs etcd-server --config=/tmp/${HOST2}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-peer --config=/tmp/${HOST2}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-healthcheck-client --config=/tmp/${HOST2}/kubeadmcfg.yaml
   kubeadm init phase certs apiserver-etcd-client --config=/tmp/${HOST2}/kubeadmcfg.yaml
   cp -R /etc/kubernetes/pki /tmp/${HOST2}/
   # cleanup non-reusable certificates
   find /etc/kubernetes/pki -not -name ca.crt -not -name ca.key -type f -delete

   kubeadm init phase certs etcd-server --config=/tmp/${HOST1}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-peer --config=/tmp/${HOST1}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-healthcheck-client --config=/tmp/${HOST1}/kubeadmcfg.yaml
   kubeadm init phase certs apiserver-etcd-client --config=/tmp/${HOST1}/kubeadmcfg.yaml
   cp -R /etc/kubernetes/pki /tmp/${HOST1}/
   find /etc/kubernetes/pki -not -name ca.crt -not -name ca.key -type f -delete

   kubeadm init phase certs etcd-server --config=/tmp/${HOST0}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-peer --config=/tmp/${HOST0}/kubeadmcfg.yaml
   kubeadm init phase certs etcd-healthcheck-client --config=/tmp/${HOST0}/kubeadmcfg.yaml
   kubeadm init phase certs apiserver-etcd-client --config=/tmp/${HOST0}/kubeadmcfg.yaml
   # No need to move the certs because they are for HOST0

   # clean up certs that should not be copied off this host
   find /tmp/${HOST2} -name ca.key -type f -delete
   find /tmp/${HOST1} -name ca.key -type f -delete
   ```

1. گواهی‌ها و پیکربندی‌های kubeadm را کپی کنید.

   گواهی‌ها تولید شده‌اند و اکنون باید به میزبان‌های مربوط به خود
   منتقل شوند.

   ```sh
   USER=ubuntu
   HOST=${HOST1}
   scp -r /tmp/${HOST}/* ${USER}@${HOST}:
   ssh ${USER}@${HOST}
   USER@HOST $ sudo -Es
   root@HOST $ chown -R root:root pki
   root@HOST $ mv pki /etc/kubernetes/
   ```

1. مطمئن شوید همهٔ فایل‌های موردانتظار وجود دارند.

   فهرست کامل فایل‌های لازم روی `$HOST0` به این شرح است:

   ```
   /tmp/${HOST0}
   └── kubeadmcfg.yaml
   ---
   /etc/kubernetes/pki
   ├── apiserver-etcd-client.crt
   ├── apiserver-etcd-client.key
   └── etcd
       ├── ca.crt
       ├── ca.key
       ├── healthcheck-client.crt
       ├── healthcheck-client.key
       ├── peer.crt
       ├── peer.key
       ├── server.crt
       └── server.key
   ```

   روی `$HOST1`:

   ```
   $HOME
   └── kubeadmcfg.yaml
   ---
   /etc/kubernetes/pki
   ├── apiserver-etcd-client.crt
   ├── apiserver-etcd-client.key
   └── etcd
       ├── ca.crt
       ├── healthcheck-client.crt
       ├── healthcheck-client.key
       ├── peer.crt
       ├── peer.key
       ├── server.crt
       └── server.key
   ```

   روی `$HOST2`:

   ```
   $HOME
   └── kubeadmcfg.yaml
   ---
   /etc/kubernetes/pki
   ├── apiserver-etcd-client.crt
   ├── apiserver-etcd-client.key
   └── etcd
       ├── ca.crt
       ├── healthcheck-client.crt
       ├── healthcheck-client.key
       ├── peer.crt
       ├── peer.key
       ├── server.crt
       └── server.key
   ```

1. مانیفست‌های پاد ایستا را ایجاد کنید.

   اکنون که گواهی‌ها و پیکربندی‌ها در جای خود قرار دارند، زمان ایجاد مانیفست‌ها
   فرا رسیده است. روی هر میزبان، فرمان `kubeadm` را اجرا کنید تا یک مانیفست ایستا
   برای etcd تولید شود.

   ```sh
   root@HOST0 $ kubeadm init phase etcd local --config=/tmp/${HOST0}/kubeadmcfg.yaml
   root@HOST1 $ kubeadm init phase etcd local --config=$HOME/kubeadmcfg.yaml
   root@HOST2 $ kubeadm init phase etcd local --config=$HOME/kubeadmcfg.yaml
   ```

1. اختیاری: سلامت کلاستر را بررسی کنید.

    اگر `etcdctl` در دسترس نیست، می‌توانید این ابزار را درون یک ایمیج کانتینر اجرا کنید.
    این کار را مستقیماً با محیط اجرای کانتینر خود و با ابزاری مانند `crictl run` انجام
    می‌دهید، نه از طریق کوبرنتیز.

    ```sh
    ETCDCTL_API=3 etcdctl \
    --cert /etc/kubernetes/pki/etcd/peer.crt \
    --key /etc/kubernetes/pki/etcd/peer.key \
    --cacert /etc/kubernetes/pki/etcd/ca.crt \
    --endpoints https://${HOST0}:2379 endpoint health
    ...
    https://[HOST0 IP]:2379 is healthy: successfully committed proposal: took = 16.283339ms
    https://[HOST1 IP]:2379 is healthy: successfully committed proposal: took = 19.44402ms
    https://[HOST2 IP]:2379 is healthy: successfully committed proposal: took = 35.926451ms
    ```

    - مقدار `${HOST0}` را برابر نشانی IP میزبانی قرار دهید که در حال آزمایش آن هستید.


## {{% heading "whatsnext" %}}

پس از آنکه یک کلاستر etcd با ۳ عضو فعال در اختیار داشتید، می‌توانید راه‌اندازی یک
control plane با دسترس‌پذیری بالا را با استفاده از
[روش etcd خارجی با kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/) ادامه دهید.

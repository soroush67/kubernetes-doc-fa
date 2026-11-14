---
reviewers:
- davidopp
title: "عیب‌یابی کلاسترها"
description: اشکال‌زدایی مشکلات رایج کلاستر.
weight: 20
no_list: true
---

<!-- overview -->

این سند به عیب‌یابی کلاستر می‌پردازد و فرض بر این است که پیش‌تر بررسی کرده‌اید و مطمئن شده‌اید که برنامهٔ شما
علت اصلی مشکلی نیست که با آن روبه‌رو هستید. برای نکاتی دربارهٔ اشکال‌زدایی برنامه‌ها،
[راهنمای عیب‌یابی برنامه](/docs/tasks/debug/debug-application/) را ببینید.
برای اطلاعات بیشتر می‌توانید به [سند مرور کلی عیب‌یابی](/docs/tasks/debug/) نیز مراجعه کنید.

برای عیب‌یابی {{<glossary_tooltip text="kubectl" term_id="kubectl">}}، به
[عیب‌یابی kubectl](/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/) مراجعه کنید.

<!-- body -->

## فهرست‌کردن اجزای کلاستر

نخستین چیزی که هنگام اشکال‌زدایی کلاستر باید بررسی کنید این است که آیا همهٔ نودها به‌درستی ثبت شده‌اند یا نه.

دستور زیر را اجرا کنید:

```shell
kubectl get nodes
```

سپس بررسی کنید که همهٔ نودهایی که انتظار دارید، در فهرست حاضر باشند و همگی در وضعیت `Ready` قرار داشته باشند.

برای به‌دست‌آوردن اطلاعات مفصل دربارهٔ سلامت کلی کلاستر، می‌توانید دستور زیر را اجرا کنید:

```shell
kubectl cluster-info dump
```

### مثال: اشکال‌زدایی نودی که از کار افتاده یا در دسترس نیست

گاهی هنگام اشکال‌زدایی، بررسی وضعیت یک نود می‌تواند مفید باشد؛ برای مثال، چون رفتار عجیبی از یک Pod
در حال اجرا روی آن نود مشاهده کرده‌اید، یا می‌خواهید بفهمید چرا یک Pod روی آن نود زمان‌بندی نمی‌شود.
همانند Podها، می‌توانید با `kubectl describe node` و `kubectl get
node -o yaml` اطلاعات مفصلی دربارهٔ نودها به دست آورید. برای نمونه، اگر نودی از کار افتاده باشد
(از شبکه قطع شده باشد، یا kubelet متوقف شده و دوباره راه‌اندازی نشود و مانند آن)، خروجی زیر را خواهید دید.
به رویدادهایی توجه کنید که نشان می‌دهند نود در وضعیت NotReady است، و همچنین دقت کنید که Podها دیگر در حال اجرا نیستند
(پس از پنج دقیقه ماندن در وضعیت NotReady، بیرون رانده (evict) می‌شوند).

```shell
kubectl get nodes
```

```none
NAME                     STATUS       ROLES     AGE     VERSION
kube-worker-1            NotReady     <none>    1h      v1.23.3
kubernetes-node-bols     Ready        <none>    1h      v1.23.3
kubernetes-node-st6x     Ready        <none>    1h      v1.23.3
kubernetes-node-unaj     Ready        <none>    1h      v1.23.3
```

```shell
kubectl describe node kube-worker-1
```

```none
Name:               kube-worker-1
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=kube-worker-1
                    kubernetes.io/os=linux
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Thu, 17 Feb 2022 16:46:30 -0500
Taints:             node.kubernetes.io/unreachable:NoExecute
                    node.kubernetes.io/unreachable:NoSchedule
Unschedulable:      false
Lease:
  HolderIdentity:  kube-worker-1
  AcquireTime:     <unset>
  RenewTime:       Thu, 17 Feb 2022 17:13:09 -0500
Conditions:
  Type                 Status    LastHeartbeatTime                 LastTransitionTime                Reason              Message
  ----                 ------    -----------------                 ------------------                ------              -------
  NetworkUnavailable   False     Thu, 17 Feb 2022 17:09:13 -0500   Thu, 17 Feb 2022 17:09:13 -0500   WeaveIsUp           Weave pod has set this
  MemoryPressure       Unknown   Thu, 17 Feb 2022 17:12:40 -0500   Thu, 17 Feb 2022 17:13:52 -0500   NodeStatusUnknown   Kubelet stopped posting node status.
  DiskPressure         Unknown   Thu, 17 Feb 2022 17:12:40 -0500   Thu, 17 Feb 2022 17:13:52 -0500   NodeStatusUnknown   Kubelet stopped posting node status.
  PIDPressure          Unknown   Thu, 17 Feb 2022 17:12:40 -0500   Thu, 17 Feb 2022 17:13:52 -0500   NodeStatusUnknown   Kubelet stopped posting node status.
  Ready                Unknown   Thu, 17 Feb 2022 17:12:40 -0500   Thu, 17 Feb 2022 17:13:52 -0500   NodeStatusUnknown   Kubelet stopped posting node status.
Addresses:
  InternalIP:  192.168.0.113
  Hostname:    kube-worker-1
Capacity:
  cpu:                2
  ephemeral-storage:  15372232Ki
  hugepages-2Mi:      0
  memory:             2025188Ki
  pods:               110
Allocatable:
  cpu:                2
  ephemeral-storage:  14167048988
  hugepages-2Mi:      0
  memory:             1922788Ki
  pods:               110
System Info:
  Machine ID:                 9384e2927f544209b5d7b67474bbf92b
  System UUID:                aa829ca9-73d7-064d-9019-df07404ad448
  Boot ID:                    5a295a03-aaca-4340-af20-1327fa5dab5c
  Kernel Version:             5.13.0-28-generic
  OS Image:                   Ubuntu 21.10
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  containerd://1.5.9
  Kubelet Version:            v1.23.3
  Kube-Proxy Version:         v1.23.3
Non-terminated Pods:          (4 in total)
  Namespace                   Name                                 CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                 ------------  ----------  ---------------  -------------  ---
  default                     nginx-deployment-67d4bdd6f5-cx2nz    500m (25%)    500m (25%)  128Mi (6%)       128Mi (6%)     23m
  default                     nginx-deployment-67d4bdd6f5-w6kd7    500m (25%)    500m (25%)  128Mi (6%)       128Mi (6%)     23m
  kube-system                 kube-proxy-dnxbz                     0 (0%)        0 (0%)      0 (0%)           0 (0%)         28m
  kube-system                 weave-net-gjxxp                      100m (5%)     0 (0%)      200Mi (10%)      0 (0%)         28m
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests     Limits
  --------           --------     ------
  cpu                1100m (55%)  1 (50%)
  memory             456Mi (24%)  256Mi (13%)
  ephemeral-storage  0 (0%)       0 (0%)
  hugepages-2Mi      0 (0%)       0 (0%)
Events:
...
```

```shell
kubectl get node kube-worker-1 -o yaml
```

```yaml
apiVersion: v1
kind: Node
metadata:
  annotations:
    node.alpha.kubernetes.io/ttl: "0"
    volumes.kubernetes.io/controller-managed-attach-detach: "true"
  creationTimestamp: "2022-02-17T21:46:30Z"
  labels:
    beta.kubernetes.io/arch: amd64
    beta.kubernetes.io/os: linux
    kubernetes.io/arch: amd64
    kubernetes.io/hostname: kube-worker-1
    kubernetes.io/os: linux
  name: kube-worker-1
  resourceVersion: "4026"
  uid: 98efe7cb-2978-4a0b-842a-1a7bf12c05f8
spec: {}
status:
  addresses:
  - address: 192.168.0.113
    type: InternalIP
  - address: kube-worker-1
    type: Hostname
  allocatable:
    cpu: "2"
    ephemeral-storage: "14167048988"
    hugepages-2Mi: "0"
    memory: 1922788Ki
    pods: "110"
  capacity:
    cpu: "2"
    ephemeral-storage: 15372232Ki
    hugepages-2Mi: "0"
    memory: 2025188Ki
    pods: "110"
  conditions:
  - lastHeartbeatTime: "2022-02-17T22:20:32Z"
    lastTransitionTime: "2022-02-17T22:20:32Z"
    message: Weave pod has set this
    reason: WeaveIsUp
    status: "False"
    type: NetworkUnavailable
  - lastHeartbeatTime: "2022-02-17T22:20:15Z"
    lastTransitionTime: "2022-02-17T22:13:25Z"
    message: kubelet has sufficient memory available
    reason: KubeletHasSufficientMemory
    status: "False"
    type: MemoryPressure
  - lastHeartbeatTime: "2022-02-17T22:20:15Z"
    lastTransitionTime: "2022-02-17T22:13:25Z"
    message: kubelet has no disk pressure
    reason: KubeletHasNoDiskPressure
    status: "False"
    type: DiskPressure
  - lastHeartbeatTime: "2022-02-17T22:20:15Z"
    lastTransitionTime: "2022-02-17T22:13:25Z"
    message: kubelet has sufficient PID available
    reason: KubeletHasSufficientPID
    status: "False"
    type: PIDPressure
  - lastHeartbeatTime: "2022-02-17T22:20:15Z"
    lastTransitionTime: "2022-02-17T22:15:15Z"
    message: kubelet is posting ready status
    reason: KubeletReady
    status: "True"
    type: Ready
  daemonEndpoints:
    kubeletEndpoint:
      Port: 10250
  nodeInfo:
    architecture: amd64
    bootID: 22333234-7a6b-44d4-9ce1-67e31dc7e369
    containerRuntimeVersion: containerd://1.5.9
    kernelVersion: 5.13.0-28-generic
    kubeProxyVersion: v1.23.3
    kubeletVersion: v1.23.3
    machineID: 9384e2927f544209b5d7b67474bbf92b
    operatingSystem: linux
    osImage: Ubuntu 21.10
    systemUUID: aa829ca9-73d7-064d-9019-df07404ad448
```


## بررسی لاگ‌ها

در حال حاضر، برای بررسی عمیق‌تر کلاستر باید وارد ماشین‌های مربوط شوید. محل فایل‌های لاگ مربوط در ادامه آمده است.
در سیستم‌های مبتنی بر systemd، ممکن است لازم باشد به‌جای بررسی فایل‌های لاگ از `journalctl` استفاده کنید.

### نودهای Control Plane

* `/var/log/kube-apiserver.log` - سرور API، مسئول ارائهٔ API
* `/var/log/kube-scheduler.log` - زمان‌بند، مسئول تصمیم‌گیری دربارهٔ زمان‌بندی
* `/var/log/kube-controller-manager.log` - مؤلفه‌ای که بیشتر
  {{<glossary_tooltip text="کنترل‌کننده‌های" term_id="controller">}} داخلی کوبرنتیز را اجرا می‌کند؛ استثنای مهم آن زمان‌بندی است
  (زمان‌بندی بر عهدهٔ kube-scheduler است).

### نودهای کارگر

* `/var/log/kubelet.log` - لاگ‌های kubelet، که مسئول اجرای کانتینرها روی نود است
* `/var/log/kube-proxy.log` - لاگ‌های `kube-proxy`، که مسئول هدایت ترافیک به endpointهای Service است

## حالت‌های خرابی کلاستر

فهرست زیر، فهرستی ناقص از مشکلاتی است که ممکن است رخ دهند، همراه با روش‌هایی برای تنظیم پیکربندی کلاستر به‌منظور کاهش این مشکلات.

### علت‌های مؤثر

- خاموش‌شدن یک یا چند ماشین مجازی (VM)
- پارتیشن‌بندی شبکه (network partition) درون کلاستر، یا میان کلاستر و کاربران
- از کار افتادن (crash) نرم‌افزار کوبرنتیز
- از دست رفتن داده یا در دسترس نبودن ذخیره‌سازی پایدار (مانند GCE PD یا حجم AWS EBS)
- خطای اپراتور، برای مثال پیکربندی نادرست نرم‌افزار کوبرنتیز یا نرم‌افزار برنامه

### سناریوهای خاص

- خاموش‌شدن ماشین مجازی سرور API یا از کار افتادن apiserver
  - پیامدها
    - امکان متوقف‌کردن، به‌روزرسانی یا راه‌اندازی Podها، Serviceها و replication controllerهای جدید وجود ندارد
    - Podها و Serviceهای موجود باید به کار عادی خود ادامه دهند، مگر اینکه به API کوبرنتیز وابسته باشند
- از دست رفتن ذخیره‌سازی پشتیبان سرور API
  - پیامدها
    - مؤلفهٔ kube-apiserver نمی‌تواند با موفقیت راه‌اندازی شود و به وضعیت سالم برسد
    - kubeletها نمی‌توانند به آن دسترسی پیدا کنند، اما همچنان همان Podها را اجرا می‌کنند و همان پراکسی Service را فراهم می‌کنند
    - پیش از راه‌اندازی دوبارهٔ apiserver، بازیابی دستی یا بازسازی وضعیت apiserver ضروری است
- خاموش‌شدن ماشین مجازی یا از کار افتادن سرویس‌های پشتیبان (کنترل‌کنندهٔ نود، مدیر replication controller، زمان‌بند و مانند آن)
  - در حال حاضر این سرویس‌ها در کنار apiserver قرار دارند و در دسترس نبودن آن‌ها پیامدهایی مشابه در دسترس نبودن apiserver دارد
  - در آینده، این سرویس‌ها نیز تکثیر خواهند شد و ممکن است در کنار هم قرار نگیرند
  - این سرویس‌ها وضعیت پایدار مخصوص به خود ندارند
- خاموش‌شدن یک نود منفرد (ماشین مجازی یا فیزیکی)
  - پیامدها
    - Podهای روی آن نود از اجرا باز می‌ایستند
- پارتیشن‌بندی شبکه
  - پیامدها
    - پارتیشن A گمان می‌کند نودهای پارتیشن B از کار افتاده‌اند و پارتیشن B گمان می‌کند apiserver از کار افتاده است.
      (با این فرض که ماشین مجازی master در پارتیشن A قرار بگیرد.)
- خرابی نرم‌افزار kubelet
  - پیامدها
    - kubeletِ از کار افتاده نمی‌تواند Podهای جدیدی روی نود راه‌اندازی کند
    - ممکن است kubelet، Podها را حذف کند یا نکند
    - نود ناسالم علامت‌گذاری می‌شود
    - replication controllerها Podهای جدیدی را در جای دیگری راه‌اندازی می‌کنند
- خطای اپراتور کلاستر
  - پیامدها
    - از دست رفتن Podها، Serviceها و مانند آن
    - از دست رفتن ذخیره‌گاه پشتیبان apiserver
    - ناتوانی کاربران در خواندن API
    - و مانند آن.

### راهکارهای کاهش مشکلات

- اقدام: برای ماشین‌های مجازی IaaS از قابلیت راه‌اندازی مجدد خودکار ماشین مجازی ارائه‌دهندهٔ IaaS استفاده کنید
  - کاهش می‌دهد: خاموش‌شدن ماشین مجازی apiserver یا از کار افتادن apiserver
  - کاهش می‌دهد: خاموش‌شدن ماشین مجازی یا از کار افتادن سرویس‌های پشتیبان

- اقدام: برای ماشین‌های مجازی دارای apiserver+etcd از ذخیره‌سازی قابل‌اعتماد ارائه‌دهندگان IaaS (مانند GCE PD یا حجم AWS EBS) استفاده کنید
  - کاهش می‌دهد: از دست رفتن ذخیره‌سازی پشتیبان apiserver

- اقدام: از پیکربندی [دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/high-availability/) استفاده کنید
  - کاهش می‌دهد: خاموش‌شدن نود control plane یا از کار افتادن مؤلفه‌های control plane (زمان‌بند، سرور API، controller-manager)
    - خرابی هم‌زمان یک یا چند نود یا مؤلفه را تحمل می‌کند
  - کاهش می‌دهد: از دست رفتن ذخیره‌سازی پشتیبان سرور API (یعنی دایرکتوری داده‌های etcd)
    - به شرط وجود پیکربندی etcd با دسترس‌پذیری بالا (HA)

- اقدام: به‌صورت دوره‌ای از PDها/حجم‌های EBS مربوط به apiserver اسنپ‌شات بگیرید
  - کاهش می‌دهد: از دست رفتن ذخیره‌سازی پشتیبان apiserver
  - کاهش می‌دهد: برخی موارد خطای اپراتور
  - کاهش می‌دهد: برخی موارد خرابی نرم‌افزار کوبرنتیز

- اقدام: از replication controller و Serviceها در جلوی Podها استفاده کنید
  - کاهش می‌دهد: خاموش‌شدن نود
  - کاهش می‌دهد: خرابی نرم‌افزار kubelet

- اقدام: برنامه‌ها (کانتینرها) طوری طراحی شوند که راه‌اندازی‌های مجدد غیرمنتظره را تحمل کنند
  - کاهش می‌دهد: خاموش‌شدن نود
  - کاهش می‌دهد: خرابی نرم‌افزار kubelet


## {{% heading "whatsnext" %}}

* با متریک‌های موجود در
  [خط لولهٔ متریک‌های منابع](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/) آشنا شوید
* ابزارهای بیشتری برای
  [پایش مصرف منابع](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/) کشف کنید
* با استفاده از Node Problem Detector
  [سلامت نودها را پایش کنید](/docs/tasks/debug/debug-cluster/monitor-node-health/)
* با استفاده از `kubectl debug node` [نودهای کوبرنتیز را اشکال‌زدایی کنید](/docs/tasks/debug/debug-cluster/kubectl-node-debug) 
* با استفاده از `crictl` [نودهای کوبرنتیز را اشکال‌زدایی کنید](/docs/tasks/debug/debug-cluster/crictl/)
* اطلاعات بیشتری دربارهٔ [ممیزی (auditing) در کوبرنتیز](/docs/tasks/debug/debug-cluster/audit/) به دست آورید
* با استفاده از `telepresence` [سرویس‌ها را به‌صورت محلی توسعه دهید و اشکال‌زدایی کنید](/docs/tasks/debug/debug-cluster/local-debugging/)
